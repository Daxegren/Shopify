-- Genererad av `shopify-sync print-ddl postgres`. Ändra schema.py, inte den här filen.

create schema if not exists "shopify";

do $$ begin
  if exists (select 1 from pg_roles where rolname = 'anon') then
    execute 'revoke all on schema "shopify" from anon, authenticated';
  end if;
end $$;

create table if not exists "shopify"."orders" (
  "id" text not null,
  "name" text,
  "created_at" timestamptz,
  "updated_at" timestamptz,
  "processed_at" timestamptz,
  "cancelled_at" timestamptz,
  "closed_at" timestamptz,
  "financial_status" text,
  "fulfillment_status" text,
  "currency_code" text,
  "total_price" numeric,
  "current_total_price" numeric,
  "subtotal_price" numeric,
  "total_discounts" numeric,
  "total_shipping" numeric,
  "total_tax" numeric,
  "total_refunded" numeric,
  "discount_codes" text,
  "source_name" text,
  "customer_id" text,
  "shipping_country" text,
  "first_visit_source" text,
  "first_visit_utm_source" text,
  "first_visit_utm_medium" text,
  "first_visit_utm_campaign" text,
  "first_visit_landing_page" text,
  "last_visit_source" text,
  "last_visit_utm_source" text,
  "last_visit_utm_medium" text,
  "last_visit_utm_campaign" text,
  "refund_count" bigint,
  "raw" jsonb,
  "_synced_at" timestamptz not null,
  primary key ("id")
);

create table if not exists "shopify"."order_line_items" (
  "id" text not null,
  "order_id" text not null,
  "product_id" text,
  "variant_id" text,
  "sku" text,
  "title" text,
  "variant_title" text,
  "vendor" text,
  "quantity" bigint,
  "current_quantity" bigint,
  "removed_quantity" bigint,
  "original_unit_price" numeric,
  "discounted_total" numeric,
  "raw" jsonb,
  "_synced_at" timestamptz not null,
  primary key ("id")
);

create table if not exists "shopify"."products" (
  "id" text not null,
  "handle" text,
  "title" text,
  "status" text,
  "vendor" text,
  "product_type" text,
  "tags" text,
  "created_at" timestamptz,
  "updated_at" timestamptz,
  "published_at" timestamptz,
  "total_inventory" bigint,
  "online_store_url" text,
  "seo_title" text,
  "seo_description" text,
  "raw" jsonb,
  "_synced_at" timestamptz not null,
  primary key ("id")
);

create table if not exists "shopify"."product_variants" (
  "id" text not null,
  "product_id" text not null,
  "sku" text,
  "title" text,
  "barcode" text,
  "price" numeric,
  "compare_at_price" numeric,
  "unit_cost" numeric,
  "inventory_quantity" bigint,
  "created_at" timestamptz,
  "updated_at" timestamptz,
  "raw" jsonb,
  "_synced_at" timestamptz not null,
  primary key ("id")
);

create table if not exists "shopify"."customers" (
  "id" text not null,
  "created_at" timestamptz,
  "updated_at" timestamptz,
  "number_of_orders" bigint,
  "amount_spent" numeric,
  "currency_code" text,
  "country" text,
  "tags" text,
  "raw" jsonb,
  "_synced_at" timestamptz not null,
  primary key ("id")
);

create table if not exists "shopify"."sync_state" (
  "entity" text not null,
  "watermark" timestamptz,
  "last_run_at" timestamptz,
  "last_object_count" bigint,
  primary key ("entity")
);

create index if not exists orders_created_at_idx on "shopify".orders (created_at);

create index if not exists order_line_items_order_id_idx on "shopify".order_line_items (order_id);

create index if not exists order_line_items_product_id_idx on "shopify".order_line_items (product_id);

create index if not exists product_variants_product_id_idx on "shopify".product_variants (product_id);
