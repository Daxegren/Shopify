-- Hur stor del av ordrarna tillskriver Klaviyo e-post och SMS, per vecka de senaste 12 veckorna?
--
--   sed -e 's/PROJ/gorilla-sports-data/g' -e 's/KEY/gorillasports/g' sql/analys/epost_andel.sql | bq query --use_legacy_sql=false
--
-- Förutsättning: klaviyo_enabled = true för butiken och site-audit backfill klaviyo har fyllt klaviyo_daily_KEY.
-- Klaviyos tillskrivning är deras egen modell och ska inte summeras med Googles eller Metas. Andelen mäts mot Shopify-ordrar
-- (growth_daily_KEY), men Klaviyo-kontot kan täcka fler marknader än en Shopify-valuta: läs andelen per butik, inte per marknad.

WITH k AS (
  SELECT DATE_TRUNC(d, ISOWEEK) AS week,
         SUM(IF(channel IN ('email', 'sms'), orders, 0)) AS klaviyo_orders,
         SUM(IF(channel IN ('email', 'sms'), revenue, 0)) AS klaviyo_revenue,
         SUM(orders) AS klaviyo_total_orders
  FROM `PROJ.site_audit.klaviyo_daily_KEY`
  WHERE d >= DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 84 DAY)
  GROUP BY 1
),
s AS (
  SELECT DATE_TRUNC(d, ISOWEEK) AS week, SUM(orders) AS shopify_orders
  FROM `PROJ.site_audit.growth_daily_KEY`
  WHERE d >= DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 84 DAY)
  GROUP BY 1
)
SELECT k.week, k.klaviyo_orders, s.shopify_orders, ROUND(SAFE_DIVIDE(k.klaviyo_orders, s.shopify_orders) * 100, 1) AS email_sms_share_pct,
       ROUND(k.klaviyo_revenue, 0) AS klaviyo_revenue
FROM k LEFT JOIN s USING (week)
ORDER BY k.week;
