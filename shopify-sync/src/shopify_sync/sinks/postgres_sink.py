"""Postgres-sink. Fungerar mot Supabase och mot vanlig Postgres (t.ex. Cloud SQL)."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from ..config import PostgresConfig
from ..schema import ALL_TABLES, PG_TYPES, SYNC_STATE, Table
from .base import Sink


def _ident(name: str) -> str:
    return '"' + name.replace('"', '""') + '"'


def create_table_sql(table: Table, schema: str) -> str:
    cols = [
        f"  {_ident(c.name)} {PG_TYPES[c.type]}{' not null' if c.required else ''}"
        for c in table.columns
    ]
    cols.append(f"  primary key ({_ident(table.primary_key)})")
    return (
        f"create table if not exists {_ident(schema)}.{_ident(table.name)} (\n"
        + ",\n".join(cols)
        + "\n);"
    )


def ddl(schema: str) -> str:
    """Hela schemat som SQL, används också för att generera Supabase-migreringen."""
    parts = [
        "-- Genererad av `shopify-sync print-ddl postgres`. Ändra schema.py, inte den här filen.",
        f"create schema if not exists {_ident(schema)};",
        # Supabase: håll schemat stängt för API-rollerna. Hoppas över på vanlig Postgres.
        "do $$ begin\n"
        "  if exists (select 1 from pg_roles where rolname = 'anon') then\n"
        f"    execute 'revoke all on schema {_ident(schema)} from anon, authenticated';\n"
        "  end if;\n"
        "end $$;",
    ]
    for table in ALL_TABLES.values():
        parts.append(create_table_sql(table, schema))
    parts.append(
        f"create index if not exists orders_created_at_idx on {_ident(schema)}.orders (created_at);"
    )
    parts.append(
        f"create index if not exists order_line_items_order_id_idx "
        f"on {_ident(schema)}.order_line_items (order_id);"
    )
    parts.append(
        f"create index if not exists order_line_items_product_id_idx "
        f"on {_ident(schema)}.order_line_items (product_id);"
    )
    parts.append(
        f"create index if not exists product_variants_product_id_idx "
        f"on {_ident(schema)}.product_variants (product_id);"
    )
    return "\n\n".join(parts) + "\n"


def upsert_sql(table: Table, schema: str) -> str:
    cols = table.column_names
    col_list = ", ".join(_ident(c) for c in cols)
    placeholders = ", ".join(f"%({c})s" for c in cols)
    updates = ", ".join(
        f"{_ident(c)} = excluded.{_ident(c)}" for c in cols if c != table.primary_key
    )
    return (
        f"insert into {_ident(schema)}.{_ident(table.name)} ({col_list}) values ({placeholders}) "
        f"on conflict ({_ident(table.primary_key)}) do update set {updates}"
    )


class PostgresSink(Sink):
    name = "postgres"

    def __init__(self, config: PostgresConfig):
        import psycopg

        self.config = config
        # prepare_threshold=None krävs bakom Supabase pooler i transaktionsläge.
        self.conn = psycopg.connect(config.dsn, autocommit=False, prepare_threshold=None)

    def ensure_tables(self) -> None:
        with self.conn.cursor() as cur:
            cur.execute(ddl(self.config.schema))
        self.conn.commit()

    def upsert(self, table: Table, rows: list[dict[str, Any]]) -> None:
        if not rows:
            return
        from psycopg.types.json import Jsonb

        json_cols = [c.name for c in table.columns if c.type == "JSON"]
        prepared = [
            {**r, **{c: Jsonb(r[c]) if r.get(c) is not None else None for c in json_cols}}
            for r in rows
        ]
        with self.conn.cursor() as cur:
            cur.executemany(upsert_sql(table, self.config.schema), prepared)
        self.conn.commit()

    def get_watermark(self, entity: str) -> datetime | None:
        with self.conn.cursor() as cur:
            cur.execute(
                f"select watermark from {_ident(self.config.schema)}.sync_state where entity = %s",
                (entity,),
            )
            row = cur.fetchone()
        self.conn.commit()
        return row[0] if row else None

    def set_watermark(self, entity: str, watermark: datetime, object_count: int) -> None:
        self.upsert(
            SYNC_STATE,
            [
                {
                    "entity": entity,
                    "watermark": watermark,
                    "last_run_at": datetime.now(timezone.utc),
                    "last_object_count": object_count,
                }
            ],
        )

    def close(self) -> None:
        self.conn.close()
