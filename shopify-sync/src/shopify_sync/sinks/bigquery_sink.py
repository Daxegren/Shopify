"""BigQuery-sink: laddar till en staging-tabell och kör MERGE in i måltabellen."""

from __future__ import annotations

import uuid
from datetime import datetime, timedelta, timezone
from typing import Any

from ..config import BigQueryConfig
from ..schema import ALL_TABLES, BQ_TYPES, SYNC_STATE, Table
from .base import Sink


def bq_schema(table: Table):
    from google.cloud import bigquery

    return [
        bigquery.SchemaField(c.name, BQ_TYPES[c.type], mode="REQUIRED" if c.required else "NULLABLE")
        for c in table.columns
    ]


def merge_sql(target: str, staging: str, table: Table) -> str:
    cols = table.column_names
    pk = table.primary_key
    updates = ", ".join(f"T.`{c}` = S.`{c}`" for c in cols if c != pk)
    col_list = ", ".join(f"`{c}`" for c in cols)
    values = ", ".join(f"S.`{c}`" for c in cols)
    # Deduplicera staging på primärnyckel om samma objekt kommit två gånger i en batch.
    return f"""
MERGE `{target}` T
USING (
  SELECT * EXCEPT(_rn) FROM (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY `{pk}`) AS _rn FROM `{staging}`
  ) WHERE _rn = 1
) S
ON T.`{pk}` = S.`{pk}`
WHEN MATCHED THEN UPDATE SET {updates}
WHEN NOT MATCHED THEN INSERT ({col_list}) VALUES ({values})
"""


def _jsonable(value: Any) -> Any:
    if isinstance(value, datetime):
        return value.isoformat()
    return value


class BigQuerySink(Sink):
    name = "bigquery"

    def __init__(self, config: BigQueryConfig):
        from google.cloud import bigquery

        self.config = config
        self.client = bigquery.Client(project=config.project, location=config.location)
        self.dataset_ref = f"{config.project}.{config.dataset}"

    def _table_id(self, name: str) -> str:
        return f"{self.dataset_ref}.{name}"

    def ensure_tables(self) -> None:
        from google.cloud import bigquery

        dataset = bigquery.Dataset(self.dataset_ref)
        dataset.location = self.config.location
        self.client.create_dataset(dataset, exists_ok=True)
        for table in ALL_TABLES.values():
            bq_table = bigquery.Table(self._table_id(table.name), schema=bq_schema(table))
            if table.partition_by:
                bq_table.time_partitioning = bigquery.TimePartitioning(field=table.partition_by)
            if table.cluster_by:
                bq_table.clustering_fields = list(table.cluster_by)
            self.client.create_table(bq_table, exists_ok=True)

    def upsert(self, table: Table, rows: list[dict[str, Any]]) -> None:
        if not rows:
            return
        from google.cloud import bigquery

        staging = self._table_id(f"_staging_{table.name}_{uuid.uuid4().hex[:8]}")
        # Utgår automatiskt om jobbet dör innan tabellen hinner tas bort.
        staging_table = bigquery.Table(staging, schema=bq_schema(table))
        staging_table.expires = datetime.now(timezone.utc) + timedelta(hours=1)
        self.client.create_table(staging_table)
        job_config = bigquery.LoadJobConfig(
            schema=bq_schema(table),
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
        )
        payload = [{k: _jsonable(v) for k, v in r.items()} for r in rows]
        try:
            self.client.load_table_from_json(payload, staging, job_config=job_config).result()
            self.client.query(merge_sql(self._table_id(table.name), staging, table)).result()
        finally:
            self.client.delete_table(staging, not_found_ok=True)

    def get_watermark(self, entity: str) -> datetime | None:
        from google.cloud import bigquery

        job = self.client.query(
            f"SELECT watermark FROM `{self._table_id('sync_state')}` WHERE entity = @entity",
            job_config=bigquery.QueryJobConfig(
                query_parameters=[bigquery.ScalarQueryParameter("entity", "STRING", entity)]
            ),
        )
        rows = list(job.result())
        return rows[0]["watermark"] if rows else None

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
        self.client.close()
