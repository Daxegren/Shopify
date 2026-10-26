-- Följer omsättningstappet per produkt med annonsklicken? Jämför varje produkts omsättning och Google Ads-klick, 30 dagar mot 30 före.
--
--   sed 's/PROJ/gorilla-sports-data/g' sql/analys/omsattning_tapp_annonser.sql | bq query --use_legacy_sql=false --max_rows=60
--
-- Perioder som i omsattning_tapp_per_produkt.sql. Annonstabellen är google_ads_products_daily_gorillasports_se (SE och DK, olika valutor,
-- därför jämförs klick och inte kostnad). Produkter utan annonsrader får klick 0. Annonsernas item_id har formen shopify_<land>_<produkt-id>_<variant-id>.
-- Visar samband, inte orsak: en produkt kan tappa både annonsklick och försäljning av samma skäl (till exempel att den tagit slut).

DECLARE p1_end DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 1 DAY);
DECLARE p1_start DATE DEFAULT DATE_SUB(p1_end, INTERVAL 29 DAY);
DECLARE p0_end DATE DEFAULT DATE_SUB(p1_start, INTERVAL 1 DAY);
DECLARE p0_start DATE DEFAULT DATE_SUB(p0_end, INTERVAL 29 DAY);

CREATE TEMP TABLE sam AS
WITH lines AS (
  SELECT REGEXP_EXTRACT(li.product_id, r'(\d+)$') AS pid, ANY_VALUE(li.title) AS title,
         SUM(IF(DATE(o.created_at, 'Europe/Stockholm') BETWEEN p0_start AND p0_end, li.discounted_total, 0)) AS oms_p0,
         SUM(IF(DATE(o.created_at, 'Europe/Stockholm') BETWEEN p1_start AND p1_end, li.discounted_total, 0)) AS oms_p1,
         SUM(IF(DATE(o.created_at, 'Europe/Stockholm') BETWEEN p0_start AND p0_end, li.quantity, 0)) AS st_p0,
         SUM(IF(DATE(o.created_at, 'Europe/Stockholm') BETWEEN p1_start AND p1_end, li.quantity, 0)) AS st_p1
  FROM `PROJ.shopify.orders` o
  JOIN `PROJ.shopify.order_line_items` li ON li.order_id = o.id
  WHERE o.cancelled_at IS NULL AND DATE(o.created_at, 'Europe/Stockholm') BETWEEN p0_start AND p1_end
  GROUP BY 1
), ads AS (
  SELECT REGEXP_EXTRACT(item_id, r'(?i)^shopify_[a-z]+_(\d+)_\d+$') AS pid,
         SUM(IF(d BETWEEN p0_start AND p0_end, clicks, 0)) AS klick_p0,
         SUM(IF(d BETWEEN p1_start AND p1_end, clicks, 0)) AS klick_p1
  FROM `PROJ.site_audit.google_ads_products_daily_gorillasports_se`
  WHERE d BETWEEN p0_start AND p1_end
  GROUP BY 1
)
SELECT l.pid, l.title, l.oms_p0, l.oms_p1, l.oms_p1 - l.oms_p0 AS forandring, l.st_p0, l.st_p1,
       IFNULL(a.klick_p0, 0) AS klick_p0, IFNULL(a.klick_p1, 0) AS klick_p1,
       CASE WHEN IFNULL(a.klick_p0, 0) < 20 THEN 'liten annonsvolym (<20 klick före)'
            WHEN IFNULL(a.klick_p1, 0) <= 0.5 * a.klick_p0 THEN 'annonsklick minskade mer än hälften'
            WHEN IFNULL(a.klick_p1, 0) < a.klick_p0 THEN 'annonsklick minskade något'
            ELSE 'annonsklick lika eller fler' END AS annonsutveckling
FROM lines l LEFT JOIN ads a USING (pid);

-- 1. Tappet uppdelat på hur produktens annonsklick utvecklats
SELECT annonsutveckling, COUNT(*) AS produkter, ROUND(SUM(oms_p0)) AS oms_p0, ROUND(SUM(oms_p1)) AS oms_p1,
       ROUND(SUM(forandring)) AS forandring, ROUND(SUM(IF(forandring < 0, forandring, 0))) AS bara_minskningar,
       SUM(klick_p0) AS klick_p0, SUM(klick_p1) AS klick_p1
FROM sam GROUP BY 1 ORDER BY forandring;

-- 2. De 25 största minskningarna, med enheter och annonsklick före och nu
SELECT title, st_p0, st_p1, klick_p0, klick_p1, ROUND(oms_p0) AS oms_p0, ROUND(oms_p1) AS oms_p1, ROUND(forandring) AS forandring, annonsutveckling
FROM sam WHERE forandring < 0 ORDER BY forandring LIMIT 25;
