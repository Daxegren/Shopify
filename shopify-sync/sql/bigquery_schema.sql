CREATE TABLE IF NOT EXISTS `shopify.orders` (
  `id` STRING NOT NULL,
  `name` STRING,
  `created_at` TIMESTAMP,
  `updated_at` TIMESTAMP,
  `processed_at` TIMESTAMP,
  `cancelled_at` TIMESTAMP,
  `closed_at` TIMESTAMP,
  `financial_status` STRING,
  `fulfillment_status` STRING,
  `currency_code` STRING,
  `total_price` NUMERIC,
  `current_total_price` NUMERIC,
  `subtotal_price` NUMERIC,
  `total_discounts` NUMERIC,
  `total_shipping` NUMERIC,
  `total_tax` NUMERIC,
  `total_refunded` NUMERIC,
  `discount_codes` STRING,
  `source_name` STRING,
  `customer_id` STRING,
  `shipping_country` STRING,
  `first_visit_source` STRING,
  `first_visit_utm_source` STRING,
  `first_visit_utm_medium` STRING,
  `first_visit_utm_campaign` STRING,
  `first_visit_landing_page` STRING,
  `last_visit_source` STRING,
  `last_visit_utm_source` STRING,
  `last_visit_utm_medium` STRING,
  `last_visit_utm_campaign` STRING,
  `refund_count` INT64,
  `raw` JSON,
  `_synced_at` TIMESTAMP NOT NULL
)
PARTITION BY DATE(`created_at`)
CLUSTER BY `customer_id`;

CREATE TABLE IF NOT EXISTS `shopify.order_line_items` (
  `id` STRING NOT NULL,
  `order_id` STRING NOT NULL,
  `product_id` STRING,
  `variant_id` STRING,
  `sku` STRING,
  `title` STRING,
  `variant_title` STRING,
  `vendor` STRING,
  `quantity` INT64,
  `current_quantity` INT64,
  `removed_quantity` INT64,
  `original_unit_price` NUMERIC,
  `discounted_total` NUMERIC,
  `raw` JSON,
  `_synced_at` TIMESTAMP NOT NULL
)
CLUSTER BY `order_id`, `product_id`;

CREATE TABLE IF NOT EXISTS `shopify.products` (
  `id` STRING NOT NULL,
  `handle` STRING,
  `title` STRING,
  `status` STRING,
  `vendor` STRING,
  `product_type` STRING,
  `tags` STRING,
  `created_at` TIMESTAMP,
  `updated_at` TIMESTAMP,
  `published_at` TIMESTAMP,
  `total_inventory` INT64,
  `online_store_url` STRING,
  `seo_title` STRING,
  `seo_description` STRING,
  `raw` JSON,
  `_synced_at` TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS `shopify.product_variants` (
  `id` STRING NOT NULL,
  `product_id` STRING NOT NULL,
  `sku` STRING,
  `title` STRING,
  `barcode` STRING,
  `price` NUMERIC,
  `compare_at_price` NUMERIC,
  `unit_cost` NUMERIC,
  `inventory_quantity` INT64,
  `created_at` TIMESTAMP,
  `updated_at` TIMESTAMP,
  `raw` JSON,
  `_synced_at` TIMESTAMP NOT NULL
)
CLUSTER BY `product_id`;

CREATE TABLE IF NOT EXISTS `shopify.customers` (
  `id` STRING NOT NULL,
  `created_at` TIMESTAMP,
  `updated_at` TIMESTAMP,
  `number_of_orders` INT64,
  `amount_spent` NUMERIC,
  `currency_code` STRING,
  `country` STRING,
  `tags` STRING,
  `raw` JSON,
  `_synced_at` TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS `shopify.sync_state` (
  `entity` STRING NOT NULL,
  `watermark` TIMESTAMP,
  `last_run_at` TIMESTAMP,
  `last_object_count` INT64
);

