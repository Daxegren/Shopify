-- Hur mycket av omsättningstappet ligger på produkter som i dag inte går att köpa, jämfört med produkter som finns men säljer sämre?
-- Delar de senaste 30 dagarnas omsättning mot de 30 innan per produkt, och märker varje produkt med dagens tillgänglighet.
--
--   sed 's/PROJ/gorilla-sports-data/g' sql/analys/omsattning_tapp_per_produkt.sql | bq query --use_legacy_sql=false --max_rows=60
--
-- Perioder (hela dagar, svensk tid): P1 = de senaste 30 dagarna till och med i går, P0 = de 30 dagarna innan.
-- Belopp i butikens valuta (SEK), SE och DK tillsammans.
-- BEGRÄNSNING: tillgängligheten är dagens (ögonblicksbild från Shopify-synken). Det finns ingen lagerhistorik, så en produkt som
-- var slut under en del av P1 men fylldes på syns som "finns". Siffran för "slut nu" är därför en undre gräns för tappet som beror på lager.
-- Lagret styrs av leverantören (dropshipping); frågan är underlag för samtal med inköp, inte en uppgift att åtgärda i butiken.

DECLARE p1_end DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 1 DAY);
DECLARE p1_start DATE DEFAULT DATE_SUB(p1_end, INTERVAL 29 DAY);
DECLARE p0_end DATE DEFAULT DATE_SUB(p1_start, INTERVAL 1 DAY);
DECLARE p0_start DATE DEFAULT DATE_SUB(p0_end, INTERVAL 29 DAY);

CREATE TEMP TABLE per_produkt AS
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
), p AS (
  SELECT REGEXP_EXTRACT(id, r'(\d+)$') AS pid, ANY_VALUE(status) AS status, ANY_VALUE(total_inventory) AS lager
  FROM `PROJ.shopify.products` GROUP BY 1
)
SELECT l.pid, l.title, l.oms_p0, l.oms_p1, l.oms_p1 - l.oms_p0 AS forandring, l.st_p0, l.st_p1,
       CASE WHEN p.pid IS NULL THEN 'borttagen'
            WHEN p.status != 'ACTIVE' THEN 'inte aktiv (utkast/arkiverad)'
            WHEN IFNULL(p.lager, 0) <= 0 THEN 'slut nu'
            ELSE 'finns' END AS tillganglighet,
       p.lager
FROM lines l LEFT JOIN p USING (pid);

-- 1. Tappet uppdelat på dagens tillgänglighet
SELECT tillganglighet, COUNT(*) AS produkter, ROUND(SUM(oms_p0)) AS oms_p0, ROUND(SUM(oms_p1)) AS oms_p1,
       ROUND(SUM(forandring)) AS forandring,
       ROUND(SUM(IF(forandring < 0, forandring, 0))) AS bara_minskningar,
       ROUND(SUM(IF(forandring > 0, forandring, 0))) AS bara_okningar
FROM per_produkt GROUP BY 1 ORDER BY forandring;

-- 2. De 30 produkter som tappat mest, med dagens tillgänglighet
SELECT title, tillganglighet, lager, st_p0, st_p1, ROUND(oms_p0) AS oms_p0, ROUND(oms_p1) AS oms_p1, ROUND(forandring) AS forandring
FROM per_produkt WHERE forandring < 0 ORDER BY forandring LIMIT 30;

-- 3. Nya produkter som sålde bara i P1 (kompenserar delvis)
SELECT title, tillganglighet, st_p1, ROUND(oms_p1) AS oms_p1
FROM per_produkt WHERE oms_p0 = 0 AND oms_p1 > 0 ORDER BY oms_p1 DESC LIMIT 15;
