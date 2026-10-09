"""Kör en inkrementell synk per entitet: bulk-fråga -> transform -> upsert i varje sink."""

from __future__ import annotations

import logging
from collections import defaultdict
from datetime import datetime, timezone
from typing import Any, Protocol
from collections.abc import Iterator

from . import queries
from .config import SyncConfig
from .schema import DATA_TABLES
from .sinks.base import Sink
from .transform import route

log = logging.getLogger(__name__)

# Tabellen vars updated_at styr vattenmärket för respektive entitet.
ROOT_TABLE = {"orders": "orders", "products": "products", "customers": "customers"}


class BulkRunner(Protocol):
    def run_bulk(
        self, bulk_query: str, poll_interval_s: float, timeout_s: float
    ) -> tuple[dict[str, Any], Iterator[dict[str, Any]]]: ...


def _parse_ts(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _shopify_ts(value: datetime) -> str:
    return value.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def resolve_since(sinks: list[Sink], entity: str, cfg: SyncConfig, full: bool) -> datetime:
    """Startpunkt för synken. En ny sink utan vattenmärke ger full backfill för alla."""
    if full:
        return cfg.start_date
    marks = [s.get_watermark(entity) for s in sinks]
    if any(m is None for m in marks):
        return cfg.start_date
    oldest = min(m if m.tzinfo else m.replace(tzinfo=timezone.utc) for m in marks)
    return max(cfg.start_date, oldest - cfg.overlap)


def sync_entity(client: BulkRunner, sinks: list[Sink], entity: str, cfg: SyncConfig, full: bool = False) -> int:
    since = resolve_since(sinks, entity, cfg, full)
    filter_ = f"updated_at:>='{_shopify_ts(since)}'"
    log.info("%s: hämtar ändringar sedan %s", entity, _shopify_ts(since))

    synced_at = datetime.now(timezone.utc).isoformat()
    op, objects = client.run_bulk(queries.build(entity, filter_), cfg.poll_interval_s, cfg.timeout_s)

    buffers: dict[str, list[dict[str, Any]]] = defaultdict(list)
    watermark = since
    root = ROOT_TABLE[entity]
    count = 0

    def flush(table_name: str) -> None:
        rows = buffers.pop(table_name, [])
        if rows:
            for sink in sinks:
                sink.upsert(DATA_TABLES[table_name], rows)

    for table_name, row in route(objects, synced_at):
        buffers[table_name].append(row)
        count += 1
        if table_name == root:
            updated = _parse_ts(row.get("updated_at"))
            if updated and updated > watermark:
                watermark = updated
        if len(buffers[table_name]) >= cfg.batch_size:
            flush(table_name)

    for table_name in list(buffers):
        flush(table_name)

    # Vattenmärket flyttas först när allt är skrivet, så ett avbrott ger omkörning, inte hål.
    for sink in sinks:
        sink.set_watermark(entity, watermark, count)
    log.info("%s: %s rader skrivna, nytt vattenmärke %s", entity, count, _shopify_ts(watermark))
    return count
