import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

from shopify_sync import queries
from shopify_sync.config import SyncConfig
from shopify_sync.schema import ALL_TABLES
from shopify_sync.sinks.base import Sink
from shopify_sync.sinks.postgres_sink import ddl, upsert_sql
from shopify_sync.sync import sync_entity
from shopify_sync.transform import gid_type, route

FIXTURES = Path(__file__).parent / "fixtures"


def load(name):
    return [json.loads(line) for line in (FIXTURES / name).read_text().splitlines() if line]


def cfg(**overrides):
    base = dict(
        sinks=("bigquery",),
        entities=("orders", "products"),
        start_date=datetime(2018, 1, 1, tzinfo=timezone.utc),
        overlap=timedelta(minutes=15),
        batch_size=2,
        poll_interval_s=0,
        timeout_s=1,
    )
    base.update(overrides)
    return SyncConfig(**base)


class MemorySink(Sink):
    name = "memory"

    def __init__(self):
        self.tables = {}
        self.watermarks = {}
        self.upsert_calls = 0

    def ensure_tables(self):
        pass

    def upsert(self, table, rows):
        self.upsert_calls += 1
        store = self.tables.setdefault(table.name, {})
        for r in rows:
            assert set(r) == set(table.column_names), table.name
            store[r[table.primary_key]] = r

    def get_watermark(self, entity):
        return self.watermarks.get(entity)

    def set_watermark(self, entity, watermark, object_count):
        self.watermarks[entity] = watermark


class FakeShopify:
    def __init__(self, objects):
        self.objects = objects
        self.queries = []

    def run_bulk(self, bulk_query, poll_interval_s, timeout_s):
        self.queries.append(bulk_query)
        return {"status": "COMPLETED"}, iter(self.objects)


def test_gid_type():
    assert gid_type("gid://shopify/LineItem/1") == "LineItem"
    assert gid_type(None) is None
    assert gid_type("123") is None


def test_order_transform():
    rows = list(route(load("orders.jsonl"), "2026-10-09T00:00:00+00:00"))
    tables = [t for t, _ in rows]
    assert tables == ["orders", "order_line_items", "order_line_items", "orders"]

    order = rows[0][1]
    assert order["total_price"] == "8699.0"
    assert order["discount_codes"] == "HOST15"
    assert order["customer_id"] == "gid://shopify/Customer/55"
    assert order["first_visit_utm_medium"] == "cpc"
    assert order["last_visit_utm_source"] is None
    assert order["refund_count"] == 1
    assert "__parentId" not in order["raw"]

    plates = rows[2][1]
    assert plates["order_id"] == "gid://shopify/Order/1001"
    assert plates["removed_quantity"] == 1
    assert plates["product_id"] is None

    sparse = rows[3][1]
    assert sparse["customer_id"] is None and sparse["discount_codes"] is None


def test_product_transform():
    rows = dict(route(load("products.jsonl"), "x"))
    assert rows["products"]["tags"] == "rack,fri-frakt"
    variant = rows["product_variants"]
    assert variant["product_id"] == "gid://shopify/Product/77"
    assert variant["compare_at_price"] == "9699.00"
    assert variant["unit_cost"] == "3100.0"


def test_sync_full_then_incremental():
    sink = MemorySink()
    shop = FakeShopify(load("orders.jsonl"))

    count = sync_entity(shop, [sink], "orders", cfg())
    assert count == 4
    assert len(sink.tables["orders"]) == 2
    assert len(sink.tables["order_line_items"]) == 2
    assert "updated_at:>='2018-01-01T00:00:00Z'" in shop.queries[0]
    # Senaste updatedAt bland ordrarna.
    assert sink.watermarks["orders"] == datetime(2026, 9, 3, 12, 5, tzinfo=timezone.utc)

    # Andra körningen startar från vattenmärket minus överlapp och är idempotent.
    sync_entity(shop, [sink], "orders", cfg())
    assert "updated_at:>='2026-09-03T11:50:00Z'" in shop.queries[1]
    assert len(sink.tables["orders"]) == 2


def test_new_sink_triggers_backfill():
    old, new = MemorySink(), MemorySink()
    old.watermarks["orders"] = datetime(2026, 9, 1, tzinfo=timezone.utc)
    shop = FakeShopify([])
    sync_entity(shop, [old, new], "orders", cfg())
    assert "updated_at:>='2018-01-01T00:00:00Z'" in shop.queries[0]
    # Tomt resultat ska inte flytta tillbaka vattenmärket förbi startpunkten.
    assert new.watermarks["orders"] == datetime(2018, 1, 1, tzinfo=timezone.utc)


def test_query_filter_is_embedded_and_escaped():
    q = queries.build("orders", "updated_at:>='2026-01-01T00:00:00Z'")
    assert 'orders(query: "updated_at:>=\'2026-01-01T00:00:00Z\'"' in q
    assert "{filter}" not in q


def test_postgres_sql():
    sql = ddl("shopify")
    for name in ALL_TABLES:
        assert f'"shopify"."{name}"' in sql
    upsert = upsert_sql(ALL_TABLES["orders"], "shopify")
    assert 'on conflict ("id") do update set' in upsert
    assert '"id" = excluded."id"' not in upsert


def test_committed_migration_matches_schema():
    migration = Path(__file__).parents[1] / "sql" / "postgres_schema.sql"
    assert migration.read_text() == ddl("shopify"), "Kör: shopify-sync print-ddl postgres > sql/postgres_schema.sql"


def test_bigquery_schema_and_merge():
    from shopify_sync.sinks.bigquery_sink import bq_schema, merge_sql

    table = ALL_TABLES["orders"]
    fields = {f.name: (f.field_type, f.mode) for f in bq_schema(table)}
    assert fields["raw"] == ("JSON", "NULLABLE")
    assert fields["id"] == ("STRING", "REQUIRED")
    sql = merge_sql("p.d.orders", "p.d._staging", table)
    assert "ON T.`id` = S.`id`" in sql
    assert "T.`id` = S.`id`," not in sql
