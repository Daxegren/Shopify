-- Genererad av  site-audit growth-sql  från sites.toml. Ändra inte för hand: ändra konfigurationen och generera om.
-- Kör:  site-audit growth-sql | bq query --use_legacy_sql=false
-- Belopp ligger i marknadens valuta och summeras inte över marknader. Se docs/tillvaxtdata.md och docs/flera-sajter.md.

-- Butik: gorillasports-se (nyckel gorillasports_se)

CREATE OR REPLACE VIEW `gorilla-sports-data.site_audit.growth_ads_daily_gorillasports_se` AS
SELECT d, 'google_ads' AS platform, CASE currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' WHEN 'NOK' THEN 'NO' WHEN 'EUR' THEN 'FI' ELSE currency END AS market, currency,
       campaign_id, campaign_name, channel_type AS campaign_type,
       cost, impressions, clicks, conversions, conversions_value
FROM `gorilla-sports-data.site_audit.google_ads_daily_gorillasports_se`
UNION ALL
SELECT d, 'meta' AS platform, CASE currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' WHEN 'NOK' THEN 'NO' WHEN 'EUR' THEN 'FI' ELSE currency END AS market, currency,
       campaign_id, campaign_name, CAST(NULL AS STRING) AS campaign_type,
       spend AS cost, impressions, clicks, purchases AS conversions, purchase_value AS conversions_value
FROM `gorilla-sports-data.site_audit.meta_ads_daily_gorillasports_se`;

CREATE OR REPLACE VIEW `gorilla-sports-data.site_audit.growth_product_daily_gorillasports_se` AS
WITH v AS (
  SELECT REGEXP_EXTRACT(v.id, r'(\d+)$') AS variant_key, v.sku, v.price, v.unit_cost, v.inventory_quantity,
         pr.title AS shopify_title, pr.status, pr.total_inventory, pr.handle
  FROM `gorilla-sports-data.shopify.product_variants` v LEFT JOIN `gorilla-sports-data.shopify.products` pr ON pr.id = v.product_id
)
SELECT a.d, CASE a.currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' WHEN 'NOK' THEN 'NO' WHEN 'EUR' THEN 'FI' ELSE a.currency END AS market, a.currency, a.item_id, a.title AS ads_title,
       v.shopify_title, v.status, v.sku, v.price, v.unit_cost, v.inventory_quantity, v.total_inventory, v.handle,
       v.variant_key IS NOT NULL AS matched,
       a.cost, a.impressions, a.clicks, a.conversions, a.conversions_value
FROM `gorilla-sports-data.site_audit.google_ads_products_daily_gorillasports_se` a
LEFT JOIN v ON v.variant_key = REGEXP_EXTRACT(a.item_id, r'(\d+)$');

CREATE OR REPLACE VIEW `gorilla-sports-data.site_audit.growth_daily_gorillasports_se` AS
WITH orders AS (
  SELECT DATE(created_at, 'Europe/Stockholm') AS d, CASE presentment_currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' WHEN 'NOK' THEN 'NO' WHEN 'EUR' THEN 'FI' ELSE presentment_currency END AS market,
         COUNT(*) AS orders, SUM(total_price_presentment) AS revenue
  FROM `gorilla-sports-data.shopify.orders`
  WHERE cancelled_at IS NULL
  GROUP BY 1, 2
),
ga4 AS (
  SELECT d, CASE hostname WHEN 'www.gorillasports.se' THEN 'SE' WHEN 'www.gorillasports.dk' THEN 'DK' ELSE 'OTHER' END AS market, SUM(sessions) AS sessions, SUM(purchases) AS ga4_purchases
  FROM `gorilla-sports-data.site_audit.ga4_landing_daily_gorillasports_se`
  GROUP BY 1, 2
),
ads AS (
  SELECT d, market,
         SUM(IF(platform = 'google_ads', cost, 0)) AS google_cost, SUM(IF(platform = 'meta', cost, 0)) AS meta_cost,
         SUM(IF(platform = 'google_ads', conversions_value, 0)) AS google_value, SUM(IF(platform = 'meta', conversions_value, 0)) AS meta_value,
         SUM(clicks) AS ad_clicks
  FROM `gorilla-sports-data.site_audit.growth_ads_daily_gorillasports_se`
  GROUP BY 1, 2
)
SELECT d,
       market,
       o.orders,
       o.revenue,
       g.sessions,
       g.ga4_purchases,
       a.google_cost,
       a.meta_cost,
       a.google_value,
       a.meta_value,
       a.ad_clicks,
       SAFE_DIVIDE(o.revenue, IFNULL(a.google_cost, 0) + IFNULL(a.meta_cost, 0)) AS mer,
       SAFE_DIVIDE(o.orders, g.sessions) AS order_rate
FROM orders o
FULL JOIN ga4 g USING (d, market)
FULL JOIN ads a USING (d, market);

CREATE SCHEMA IF NOT EXISTS `gorilla-sports-data.portfolio` OPTIONS (location = 'EU');

CREATE OR REPLACE VIEW `gorilla-sports-data.portfolio.portfolio_daily` AS
SELECT 'gorillasports_se' AS store, '' AS company, 'traning' AS vertical, d, market,
       CASE market WHEN 'SE' THEN 'SEK' WHEN 'DK' THEN 'DKK' WHEN 'NO' THEN 'NOK' WHEN 'FI' THEN 'EUR' END AS currency, orders, revenue, sessions, ga4_purchases,
       google_cost, meta_cost, google_value, meta_value, ad_clicks, mer, order_rate
FROM `gorilla-sports-data.site_audit.growth_daily_gorillasports_se`;

CREATE OR REPLACE VIEW `gorilla-sports-data.portfolio.portfolio_weekly` AS
SELECT store, company, vertical, market, currency, DATE_TRUNC(d, ISOWEEK) AS week,
       SUM(orders) AS orders, SUM(revenue) AS revenue, SUM(sessions) AS sessions,
       IFNULL(SUM(google_cost), 0) + IFNULL(SUM(meta_cost), 0) AS ad_cost,
       SAFE_DIVIDE(SUM(revenue), IFNULL(SUM(google_cost), 0) + IFNULL(SUM(meta_cost), 0)) AS mer,
       SAFE_DIVIDE(SUM(orders), SUM(sessions)) AS order_rate
FROM `gorilla-sports-data.portfolio.portfolio_daily`
GROUP BY 1, 2, 3, 4, 5, 6;
