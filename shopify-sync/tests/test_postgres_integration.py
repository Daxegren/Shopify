"""Körs bara när TEST_PG_DSN pekar på en Postgres-databas som får skrivas till."""

import os

import pytest

from shopify_sync.config import PostgresConfig
from test_sync import FakeShopify, cfg, load

DSN = os.environ.get("TEST_PG_DSN")
pytestmark = pytest.mark.skipif(not DSN, reason="TEST_PG_DSN saknas")


def test_postgres_roundtrip():
    from shopify_sync.sinks.postgres_sink import PostgresSink
    from shopify_sync.sync import sync_entity

    sink = PostgresSink(PostgresConfig(dsn=DSN, schema="shopify_test"))
    try:
        with sink.conn.cursor() as cur:
            cur.execute("drop schema if exists shopify_test cascade")
        sink.conn.commit()
        sink.ensure_tables()
        sink.ensure_tables()  # idempotent

        shop = FakeShopify(load("orders.jsonl") + load("products.jsonl"))
        sync_entity(shop, [sink], "orders", cfg())
        sync_entity(shop, [sink], "orders", cfg())  # upsert, inga dubbletter

        with sink.conn.cursor() as cur:
            cur.execute("select count(*) from shopify_test.orders")
            assert cur.fetchone()[0] == 2
            cur.execute("select count(*) from shopify_test.product_variants")
            assert cur.fetchone()[0] == 1
            cur.execute(
                "select removed_quantity, raw->>'sku' from shopify_test.order_line_items "
                "where id = 'gid://shopify/LineItem/502'"
            )
            assert cur.fetchone() == (1, "VS-2x15")
            cur.execute("select total_price from shopify_test.orders where name = '#1001'")
            assert str(cur.fetchone()[0]) == "8699.0"
        assert sink.get_watermark("orders").isoformat() == "2026-09-03T12:05:00+00:00"
    finally:
        sink.close()
