-- Gemensamma vyer för tillväxtarbetet: annonser (Google Ads, Meta), besök (GA4) och ordrar (Shopify) på samma dag och marknad.
--
--   sed 's/PROJ/gorilla-sports-data/g' sql/growth/views.sql | bq query --use_legacy_sql=false
--
-- Förutsätter att tabellerna fyllts med  site-audit refresh --site gorillasports-se  (se docs/tillvaxtdata.md).
-- Marknaden härleds ur valutan (SEK = SE, DKK = DK), eftersom varje marknad har en egen valuta och egna annonskonton.
-- Belopp ligger i marknadens valuta och ska inte summeras över marknader utan omräkning.

CREATE OR REPLACE VIEW `PROJ.site_audit.growth_ads_daily` AS
SELECT d, 'google_ads' AS platform,
       CASE currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE currency END AS market, currency,
       campaign_id, campaign_name, channel_type AS campaign_type,
       cost, impressions, clicks, conversions, conversions_value
FROM `PROJ.site_audit.google_ads_daily_gorillasports_se`
UNION ALL
SELECT d, 'meta' AS platform,
       CASE currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE currency END AS market, currency,
       campaign_id, campaign_name, CAST(NULL AS STRING) AS campaign_type,
       spend AS cost, impressions, clicks, purchases AS conversions, purchase_value AS conversions_value
FROM `PROJ.site_audit.meta_ads_daily_gorillasports_se`;

-- En rad per dag och marknad. Konverteringsvärde är plattformens egen tillskrivning och överlappar mellan Google och Meta;
-- Shopify-omsättningen är facit. MER (marketing efficiency ratio) = omsättning / total annonskostnad.
CREATE OR REPLACE VIEW `PROJ.site_audit.growth_daily` AS
WITH orders AS (
  SELECT DATE(created_at, 'Europe/Stockholm') AS d,
         CASE presentment_currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE presentment_currency END AS market,
         COUNT(*) AS orders, SUM(total_price_presentment) AS revenue
  FROM `PROJ.shopify.orders`
  WHERE cancelled_at IS NULL
  GROUP BY 1, 2
), ga4 AS (
  SELECT d, IF(hostname = 'www.gorillasports.dk', 'DK', 'SE') AS market,
         SUM(sessions) AS sessions, SUM(purchases) AS ga4_purchases
  FROM `PROJ.site_audit.ga4_landing_daily_gorillasports_se`
  WHERE hostname IN ('www.gorillasports.se', 'www.gorillasports.dk')
  GROUP BY 1, 2
), ads AS (
  SELECT d, market,
         SUM(IF(platform = 'google_ads', cost, 0)) AS google_cost, SUM(IF(platform = 'meta', cost, 0)) AS meta_cost,
         SUM(IF(platform = 'google_ads', conversions_value, 0)) AS google_value, SUM(IF(platform = 'meta', conversions_value, 0)) AS meta_value,
         SUM(clicks) AS ad_clicks
  FROM `PROJ.site_audit.growth_ads_daily`
  GROUP BY 1, 2
)
SELECT d, market, o.orders, o.revenue, g.sessions, g.ga4_purchases,
       a.google_cost, a.meta_cost, a.google_value, a.meta_value, a.ad_clicks,
       SAFE_DIVIDE(o.revenue, IFNULL(a.google_cost, 0) + IFNULL(a.meta_cost, 0)) AS mer,
       SAFE_DIVIDE(o.orders, g.sessions) AS order_rate
FROM orders o
FULL JOIN ga4 g USING (d, market)
FULL JOIN ads a USING (d, market);
