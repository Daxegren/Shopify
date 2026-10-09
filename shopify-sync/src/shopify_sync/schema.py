"""Tabellschema: en enda källa som både BigQuery- och Postgres-sinken genererar DDL från.

Varje tabell har typade nyckelkolumner för vanliga analyser plus en `raw`-kolumn med hela
objektet från Shopify, så att nya fält kan användas utan schemaändring.
"""

from __future__ import annotations

from dataclasses import dataclass, field

# Neutrala typer -> respektive databas.
BQ_TYPES = {
    "STRING": "STRING",
    "INT64": "INT64",
    "NUMERIC": "NUMERIC",
    "TIMESTAMP": "TIMESTAMP",
    "BOOL": "BOOL",
    "JSON": "JSON",
}
PG_TYPES = {
    "STRING": "text",
    "INT64": "bigint",
    "NUMERIC": "numeric",
    "TIMESTAMP": "timestamptz",
    "BOOL": "boolean",
    "JSON": "jsonb",
}


@dataclass(frozen=True)
class Column:
    name: str
    type: str
    required: bool = False


@dataclass(frozen=True)
class Table:
    name: str
    columns: tuple[Column, ...]
    primary_key: str = "id"
    # Kolumn att partitionera på i BigQuery (dag). Ignoreras av Postgres.
    partition_by: str | None = None
    cluster_by: tuple[str, ...] = field(default_factory=tuple)

    @property
    def column_names(self) -> list[str]:
        return [c.name for c in self.columns]


C = Column

ORDERS = Table(
    name="orders",
    partition_by="created_at",
    cluster_by=("customer_id",),
    columns=(
        C("id", "STRING", required=True),
        C("name", "STRING"),
        C("created_at", "TIMESTAMP"),
        C("updated_at", "TIMESTAMP"),
        C("processed_at", "TIMESTAMP"),
        C("cancelled_at", "TIMESTAMP"),
        C("closed_at", "TIMESTAMP"),
        C("financial_status", "STRING"),
        C("fulfillment_status", "STRING"),
        C("currency_code", "STRING"),
        # Valutan kunden betalade i (Shopify Markets), t.ex. DKK på gorillasports.dk.
        C("presentment_currency", "STRING"),
        C("total_price", "NUMERIC"),
        C("total_price_presentment", "NUMERIC"),
        C("current_total_price", "NUMERIC"),
        C("subtotal_price", "NUMERIC"),
        C("total_discounts", "NUMERIC"),
        C("total_shipping", "NUMERIC"),
        C("total_tax", "NUMERIC"),
        C("total_refunded", "NUMERIC"),
        C("discount_codes", "STRING"),
        C("source_name", "STRING"),
        C("customer_id", "STRING"),
        C("shipping_country", "STRING"),
        C("first_visit_source", "STRING"),
        C("first_visit_utm_source", "STRING"),
        C("first_visit_utm_medium", "STRING"),
        C("first_visit_utm_campaign", "STRING"),
        C("first_visit_landing_page", "STRING"),
        C("last_visit_source", "STRING"),
        C("last_visit_utm_source", "STRING"),
        C("last_visit_utm_medium", "STRING"),
        C("last_visit_utm_campaign", "STRING"),
        C("refund_count", "INT64"),
        C("raw", "JSON"),
        C("_synced_at", "TIMESTAMP", required=True),
    ),
)

ORDER_LINE_ITEMS = Table(
    name="order_line_items",
    cluster_by=("order_id", "product_id"),
    columns=(
        C("id", "STRING", required=True),
        C("order_id", "STRING", required=True),
        C("product_id", "STRING"),
        C("variant_id", "STRING"),
        C("sku", "STRING"),
        C("title", "STRING"),
        C("variant_title", "STRING"),
        C("vendor", "STRING"),
        C("quantity", "INT64"),
        C("current_quantity", "INT64"),
        C("removed_quantity", "INT64"),
        C("original_unit_price", "NUMERIC"),
        C("discounted_total", "NUMERIC"),
        C("raw", "JSON"),
        C("_synced_at", "TIMESTAMP", required=True),
    ),
)

PRODUCTS = Table(
    name="products",
    columns=(
        C("id", "STRING", required=True),
        C("handle", "STRING"),
        C("title", "STRING"),
        C("status", "STRING"),
        C("vendor", "STRING"),
        C("product_type", "STRING"),
        C("tags", "STRING"),
        C("created_at", "TIMESTAMP"),
        C("updated_at", "TIMESTAMP"),
        C("published_at", "TIMESTAMP"),
        C("total_inventory", "INT64"),
        C("online_store_url", "STRING"),
        C("seo_title", "STRING"),
        C("seo_description", "STRING"),
        C("raw", "JSON"),
        C("_synced_at", "TIMESTAMP", required=True),
    ),
)

PRODUCT_VARIANTS = Table(
    name="product_variants",
    cluster_by=("product_id",),
    columns=(
        C("id", "STRING", required=True),
        C("product_id", "STRING", required=True),
        C("sku", "STRING"),
        C("title", "STRING"),
        C("barcode", "STRING"),
        C("price", "NUMERIC"),
        C("compare_at_price", "NUMERIC"),
        C("unit_cost", "NUMERIC"),
        C("inventory_quantity", "INT64"),
        C("created_at", "TIMESTAMP"),
        C("updated_at", "TIMESTAMP"),
        C("raw", "JSON"),
        C("_synced_at", "TIMESTAMP", required=True),
    ),
)

# Kunder sparas utan direkta personuppgifter (namn, e-post, telefon, adress).
CUSTOMERS = Table(
    name="customers",
    columns=(
        C("id", "STRING", required=True),
        C("created_at", "TIMESTAMP"),
        C("updated_at", "TIMESTAMP"),
        C("number_of_orders", "INT64"),
        C("amount_spent", "NUMERIC"),
        C("currency_code", "STRING"),
        C("country", "STRING"),
        C("tags", "STRING"),
        C("raw", "JSON"),
        C("_synced_at", "TIMESTAMP", required=True),
    ),
)

SYNC_STATE = Table(
    name="sync_state",
    primary_key="entity",
    columns=(
        C("entity", "STRING", required=True),
        C("watermark", "TIMESTAMP"),
        C("last_run_at", "TIMESTAMP"),
        C("last_object_count", "INT64"),
    ),
)

DATA_TABLES: dict[str, Table] = {
    t.name: t for t in (ORDERS, ORDER_LINE_ITEMS, PRODUCTS, PRODUCT_VARIANTS, CUSTOMERS)
}
ALL_TABLES: dict[str, Table] = {**DATA_TABLES, SYNC_STATE.name: SYNC_STATE}
