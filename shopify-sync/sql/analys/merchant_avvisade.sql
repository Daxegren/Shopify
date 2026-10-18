-- Avvisade produkter i Merchant Center som ändå får annonsklick eller har lager, de senaste 30 dagarna.
--
--   sed -e 's/PROJ/gorilla-sports-data/g' -e 's/KEY/gorillasports/g' sql/analys/merchant_avvisade.sql | bq query --use_legacy_sql=false
--
-- Förutsättning: site-audit backfill merchant (eller nattjobbet) har fyllt merchant_products_KEY och
-- google-ads-produkter har fyllt google_ads_products_daily_KEY. Produktstatus är en ögonblicksbild: senaste dagen används.
-- Kopplingen är offer_id = item_id (versaler/gemener ignoreras); Google Ads visar samma id som feeden. OBS: overifierad mot riktiga id:n.

WITH latest AS (
  SELECT * FROM `PROJ.site_audit.merchant_products_KEY`
  WHERE d = (SELECT MAX(d) FROM `PROJ.site_audit.merchant_products_KEY`)
),
ads AS (
  SELECT LOWER(item_id) AS item_id, ANY_VALUE(currency) AS currency, SUM(clicks) AS clicks, SUM(cost) AS cost, SUM(conversions_value) AS value
  FROM `PROJ.site_audit.google_ads_products_daily_KEY`
  WHERE d >= DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 30 DAY)
  GROUP BY 1
)
SELECT l.offer_id, l.title, l.is_disapproved, l.disapproved_countries, l.top_issue, l.issue_count,
       IFNULL(a.clicks, 0) AS clicks_30d, ROUND(IFNULL(a.cost, 0), 0) AS cost_30d, a.currency
FROM latest l LEFT JOIN ads a ON LOWER(l.offer_id) = a.item_id
WHERE l.is_disapproved OR l.disapproved_countries != '' 
ORDER BY clicks_30d DESC, l.issue_count DESC
LIMIT 100;
