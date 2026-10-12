-- Varför har omsättningen ändrats de senaste 30 dagarna jämfört med de 30 dagarna innan?
-- Delar upp förändringen i marknad, volym/ordervärde, kanal, produkt, trafik och konvertering.
--
--   sed 's/PROJ/gorilla-sports-data/g' sql/analys/omsattning_30d.sql | bq query --use_legacy_sql=false
--
-- Perioder (hela dagar, svensk tid): P1 = de senaste 30 dagarna till och med i går, P0 = de 30 dagarna innan.
-- Shopify-ordrar finns bara 60 dagar bakåt (read_all_orders saknas), så jämförelse mot förra året görs med GA4.
-- GA4-tabellen fylls via API: kör först  site-audit backfill ga4 --site gorillasports-se --since 2025-07-01

DECLARE p1_end DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 1 DAY);
DECLARE p1_start DATE DEFAULT DATE_SUB(p1_end, INTERVAL 29 DAY);
DECLARE p0_end DATE DEFAULT DATE_SUB(p1_start, INTERVAL 1 DAY);
DECLARE p0_start DATE DEFAULT DATE_SUB(p0_end, INTERVAL 29 DAY);

CREATE TEMP TABLE o AS
SELECT o.*,
       DATE(o.created_at, 'Europe/Stockholm') AS d,
       CASE WHEN DATE(o.created_at, 'Europe/Stockholm') BETWEEN p1_start AND p1_end THEN 'P1'
            WHEN DATE(o.created_at, 'Europe/Stockholm') BETWEEN p0_start AND p0_end THEN 'P0' END AS period,
       CASE o.presentment_currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE o.presentment_currency END AS marknad
FROM `PROJ.shopify.orders` o
WHERE o.cancelled_at IS NULL AND DATE(o.created_at, 'Europe/Stockholm') BETWEEN p0_start AND p1_end;

-- 1. Översikt per marknad, i butikens valuta (total_price) och i kundens valuta (presentment)
SELECT marknad, period, COUNT(*) AS ordrar,
       ROUND(SUM(total_price)) AS oms_butiksvaluta,
       ROUND(SUM(total_price_presentment)) AS oms_kundvaluta,
       ROUND(AVG(total_price_presentment)) AS snittorder_kundvaluta,
       ROUND(SUM(total_discounts) / NULLIF(SUM(subtotal_price + total_discounts), 0) * 100, 1) AS rabatt_pct,
       ROUND(SUM(total_refunded)) AS aterbetalt,
       COUNT(DISTINCT customer_id) AS kunder
FROM o GROUP BY 1, 2 ORDER BY 1, 2;

-- 2. Uppdelning av förändringen: hur mycket beror på antal ordrar och hur mycket på ordervärdet
WITH s AS (
  SELECT marknad,
         COUNTIF(period = 'P0') AS n0, COUNTIF(period = 'P1') AS n1,
         SUM(IF(period = 'P0', total_price, 0)) AS r0, SUM(IF(period = 'P1', total_price, 0)) AS r1
  FROM o GROUP BY 1)
SELECT marknad, n0, n1, ROUND(r0) AS oms_p0, ROUND(r1) AS oms_p1, ROUND(r1 - r0) AS forandring,
       ROUND((n1 - n0) * SAFE_DIVIDE(r0, n0)) AS varav_antal_ordrar,
       ROUND(n1 * (SAFE_DIVIDE(r1, n1) - SAFE_DIVIDE(r0, n0))) AS varav_ordervarde
FROM s ORDER BY marknad;

-- 3. Vecka för vecka, för att se om nedgången är jämn eller började ett visst datum
SELECT marknad, DATE_TRUNC(d, ISOWEEK) AS vecka, COUNT(*) AS ordrar, ROUND(SUM(total_price)) AS oms
FROM o GROUP BY 1, 2 ORDER BY 1, 2;

-- 4. Kanal (senaste besökets källa enligt Shopify)
SELECT marknad,
       COALESCE(NULLIF(last_visit_utm_source, ''), NULLIF(last_visit_source, ''), source_name, 'okänd') AS kanal,
       COUNTIF(period = 'P0') AS ordrar_p0, COUNTIF(period = 'P1') AS ordrar_p1,
       ROUND(SUM(IF(period = 'P0', total_price, 0))) AS oms_p0, ROUND(SUM(IF(period = 'P1', total_price, 0))) AS oms_p1,
       ROUND(SUM(IF(period = 'P1', total_price, 0)) - SUM(IF(period = 'P0', total_price, 0))) AS forandring
FROM o GROUP BY 1, 2 HAVING ordrar_p0 + ordrar_p1 >= 5 ORDER BY marknad, forandring;

-- 5. Produkter som förklarar mest av förändringen (de 25 största skillnaderna)
SELECT o.marknad, li.title,
       SUM(IF(o.period = 'P0', li.quantity, 0)) AS st_p0, SUM(IF(o.period = 'P1', li.quantity, 0)) AS st_p1,
       ROUND(SUM(IF(o.period = 'P1', li.discounted_total, 0)) - SUM(IF(o.period = 'P0', li.discounted_total, 0))) AS forandring
FROM o JOIN `PROJ.shopify.order_line_items` li ON li.order_id = o.id
GROUP BY 1, 2 ORDER BY ABS(forandring) DESC LIMIT 25;

-- 6. Trafik och konvertering (GA4), samma perioder och samma perioder förra året
SELECT hostname,
       CASE WHEN d BETWEEN p1_start AND p1_end THEN 'P1'
            WHEN d BETWEEN p0_start AND p0_end THEN 'P0'
            WHEN d BETWEEN DATE_SUB(p1_start, INTERVAL 1 YEAR) AND DATE_SUB(p1_end, INTERVAL 1 YEAR) THEN 'P1 i fjol'
            WHEN d BETWEEN DATE_SUB(p0_start, INTERVAL 1 YEAR) AND DATE_SUB(p0_end, INTERVAL 1 YEAR) THEN 'P0 i fjol' END AS period,
       SUM(sessions) AS sessioner, SUM(purchases) AS kop, ROUND(SUM(revenue)) AS intakt_ga4,
       ROUND(SAFE_DIVIDE(SUM(purchases), SUM(sessions)) * 100, 2) AS konvertering_pct,
       MAX(d) AS senaste_dag
FROM `PROJ.site_audit.ga4_landing_daily_gorillasports_se`
WHERE hostname IN ('www.gorillasports.se', 'www.gorillasports.dk')
GROUP BY 1, 2 HAVING period IS NOT NULL ORDER BY 1, 2;

-- 7. Organisk trafik från Google (Search Console), .se
SELECT CASE WHEN data_date BETWEEN p1_start AND p1_end THEN 'P1' ELSE 'P0' END AS period,
       SUM(clicks) AS klick, SUM(impressions) AS visningar,
       ROUND(SAFE_DIVIDE(SUM(clicks), SUM(impressions)) * 100, 2) AS ctr_pct
FROM `PROJ.site_audit.gsc_combined_gorillasports_se`
WHERE data_date BETWEEN p0_start AND p1_end
GROUP BY 1 ORDER BY 1;
