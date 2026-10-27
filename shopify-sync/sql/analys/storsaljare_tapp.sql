-- Storsäljare som tappat: de 30 produkter som sålde mest (i omsättning) för 28–90 dagar sedan, och hur de säljer nu.
-- Syftet är att se vilka storsäljare som tappat nästan allt, som tecken på slutsåld vara, avvecklad produkt eller en kampanj som stängts.
--
--   sed 's/PROJ/gorilla-sports-data/g' sql/analys/storsaljare_tapp.sql | bq query --use_legacy_sql=false --max_rows=100
--
-- Tre resultat: 0. datakontroll (1 rad), 1. storsäljarna (en rad per produkt och marknad, högst 60 rader), 2. avstämning mot totalen (2 rader).
-- Bara läsning. Inget ändras i butik eller annonskonto.
--
-- Källor (tabell- och kolumnnamn som redan används i omsattning_tapp_per_produkt.sql, omsattning_tapp_annonser.sql och cos_30d.sql):
--   PROJ.shopify.orders, PROJ.shopify.order_line_items (product_id, quantity, discounted_total), PROJ.shopify.products (status, total_inventory, title),
--   PROJ.shopify.product_variants (id, product_id, inventory_quantity), PROJ.site_audit.google_ads_products_daily_gorillasports_se (d, currency, item_id, clicks).
--
-- Rangordning: produkten rangordnas på omsättning (radbelopp, discounted_total) i butikens valuta (SEK) för båda marknaderna tillsammans,
--   under dagarna 90 till 28 dagar före i dag. Samma produkt (Shopify-produkt) i SE och DK är en produkt; resultatet visas sedan per marknad.
-- Veckorna: de 12 senaste hela veckorna (måndag till söndag, svensk tid). enh_per_vecka läses från äldsta veckan till nyaste, åtskilda av bindestreck;
--   "?" betyder att orderdata saknas den veckan (orderhistoriken i BigQuery är begränsad, se orderdata_fran i datakontrollen).
-- Förändring: de 4 senaste hela veckorna mot de 4 hela veckorna före. forandring_oms_sek är radbelopp i SEK och sorterar resultatet (störst förlust överst).
--
-- BEGRÄNSNINGAR som påverkar läsningen
--   * Status och lager är dagens ögonblicksbild (som i omsattning_tapp_per_produkt.sql). Det finns ingen lagerhistorik, så en produkt som var slut en tid
--     men fylldes på visas som "finns i lager".
--   * Lagret styrs av leverantören (dropshipping). total_inventory kan vara 0 också när leverantören kan leverera, om flödet inte är kopplat till lagret;
--     det går inte att avgöra här. Kontrollera i Shopify (se nedan).
--   * Perioden 61–90 dagar bakåt saknas troligen i orderdata (Shopify lämnar bara ut 60 dagars ordrar utan behörigheten read_all_orders).
--     Då baseras rangordningen på en kortare period än 28–90 dagar. Läs orderdata_fran i datakontrollen.
--   * Ett produkt-id som saknas på orderraden (till exempel egna orderrader) kan inte placeras; avstämningen (resultat 2) visar hur stor del det är.
--   * Samband är inte orsak. Att en produkt tappat och är slut i lager passar ihop, men säger inte att slutsåld var det som startade tappet.
--
-- Vad David behöver kontrollera i Shopify för varje produkt märkt "slut i lager nu", "inte aktiv" eller "borttagen":
--   Produkten under Produkter: status (aktiv, utkast, arkiverad), lagersaldo per variant, om "fortsätt sälja när slut" är på,
--   och om leverantören fortfarande har varan. Utan det går inte att skilja slutsåld från avvecklad.

DECLARE idag DATE DEFAULT CURRENT_DATE('Europe/Stockholm');
DECLARE o_forsta DATE DEFAULT (SELECT MIN(DATE(created_at, 'Europe/Stockholm')) FROM `PROJ.shopify.orders`);
DECLARE r_start DATE DEFAULT DATE_SUB(idag, INTERVAL 90 DAY);   -- rangordningsperiod: 90 till 28 dagar före i dag
DECLARE r_slut DATE DEFAULT DATE_SUB(idag, INTERVAL 28 DAY);
DECLARE v_forsta DATE DEFAULT DATE_SUB(DATE_TRUNC(idag, ISOWEEK), INTERVAL 12 WEEK);   -- måndag, första veckan av 12
DECLARE v_sista DATE DEFAULT DATE_SUB(DATE_TRUNC(idag, ISOWEEK), INTERVAL 1 WEEK);     -- måndag, sista hela veckan
DECLARE s4_start DATE DEFAULT DATE_SUB(v_sista, INTERVAL 3 WEEK);      -- de 4 senaste veckorna: s4_start till s4_slut
DECLARE s4_slut DATE DEFAULT DATE_ADD(v_sista, INTERVAL 6 DAY);
DECLARE f4_start DATE DEFAULT DATE_SUB(v_sista, INTERVAL 7 WEEK);      -- de 4 veckorna före: f4_start till f4_slut
DECLARE f4_slut DATE DEFAULT DATE_SUB(s4_start, INTERVAL 1 DAY);

-- Orderrader för alla dagar som behövs (rangordningen och veckorna). Annullerade ordrar utesluts som i övriga filer.
CREATE TEMP TABLE rader AS
SELECT REGEXP_EXTRACT(li.product_id, r'(\d+)$') AS pid,
       CASE o.presentment_currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE o.presentment_currency END AS marknad,
       DATE(o.created_at, 'Europe/Stockholm') AS d, li.quantity AS enh, li.discounted_total AS oms, li.title AS radtitel
FROM `PROJ.shopify.orders` o
JOIN `PROJ.shopify.order_line_items` li ON li.order_id = o.id
WHERE o.cancelled_at IS NULL
  AND DATE(o.created_at, 'Europe/Stockholm') BETWEEN LEAST(r_start, v_forsta) AND DATE_SUB(idag, INTERVAL 1 DAY);

-- De 30 största i rangordningsperioden (båda marknaderna, SEK).
CREATE TEMP TABLE topp AS
SELECT pid, SUM(oms) AS oms_rang, SUM(enh) AS enh_rang
FROM rader
WHERE pid IS NOT NULL AND d BETWEEN r_start AND r_slut
GROUP BY pid ORDER BY oms_rang DESC LIMIT 30;

-- Veckovis försäljning för de 30, per marknad.
CREATE TEMP TABLE vk AS
SELECT pid, marknad, DATE_TRUNC(d, ISOWEEK) AS vecka, SUM(enh) AS enh, SUM(oms) AS oms
FROM rader
WHERE pid IN (SELECT pid FROM topp) AND marknad IN ('SE', 'DK') AND d BETWEEN v_forsta AND s4_slut
GROUP BY 1, 2, 3;

-- Sista orderdatum och rangordningsperiodens omsättning per produkt och marknad.
CREATE TEMP TABLE pm AS
SELECT pid, marknad, MAX(d) AS sista_order, MAX(radtitel) AS radtitel,
       SUM(IF(d BETWEEN r_start AND r_slut, oms, 0)) AS oms_rang,
       SUM(IF(d BETWEEN r_start AND r_slut, enh, 0)) AS enh_rang
FROM rader WHERE pid IN (SELECT pid FROM topp) AND marknad IN ('SE', 'DK')
GROUP BY 1, 2;

-- Produktuppgifter (dagens läge) och annonsklick (Google Ads, varianten kopplas till produkten via sista talet i item_id).
CREATE TEMP TABLE prod AS
SELECT REGEXP_EXTRACT(id, r'(\d+)$') AS pid, ANY_VALUE(title) AS titel, ANY_VALUE(status) AS status, ANY_VALUE(total_inventory) AS lager
FROM `PROJ.shopify.products` GROUP BY 1;

CREATE TEMP TABLE varianter AS
SELECT REGEXP_EXTRACT(product_id, r'(\d+)$') AS pid, COUNT(*) AS antal_varianter, COUNTIF(IFNULL(inventory_quantity, 0) > 0) AS varianter_i_lager
FROM `PROJ.shopify.product_variants` GROUP BY 1;

CREATE TEMP TABLE ads AS
WITH vp AS (
  SELECT REGEXP_EXTRACT(id, r'(\d+)$') AS vkey, REGEXP_EXTRACT(product_id, r'(\d+)$') AS pid
  FROM `PROJ.shopify.product_variants`
)
SELECT vp.pid, CASE a.currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE a.currency END AS marknad,
       SUM(IF(a.d BETWEEN s4_start AND s4_slut, a.clicks, 0)) AS klick_s4,
       SUM(IF(a.d BETWEEN f4_start AND f4_slut, a.clicks, 0)) AS klick_f4
FROM `PROJ.site_audit.google_ads_products_daily_gorillasports_se` a
JOIN vp ON vp.vkey = REGEXP_EXTRACT(a.item_id, r'(\d+)$')
WHERE a.d BETWEEN f4_start AND s4_slut AND vp.pid IN (SELECT pid FROM topp)
GROUP BY 1, 2;

-- 0. Datakontroll. orderdata_fran = äldsta order i tabellen. dagar_med_orderdata_i_rangperioden visar hur stor del av 28–90 dagar som faktiskt finns
--    (63 är full täckning). 4v_fore_tackt = om hela jämförelseperioden "4 veckor före" ligger efter äldsta order (annars är förändringen opålitlig).
SELECT o_forsta AS orderdata_fran, r_start AS rangperiod_fran, r_slut AS rangperiod_till,
       GREATEST(0, DATE_DIFF(r_slut, GREATEST(r_start, o_forsta), DAY) + 1) AS dagar_med_orderdata_i_rangperioden,
       v_forsta AS veckor_fran, v_sista AS sista_hela_veckan_startar, s4_start AS senaste4v_fran, f4_start AS fore4v_fran,
       f4_start >= o_forsta AS fore4v_tackt;

-- 1. Storsäljarna, en rad per produkt och marknad, sorterade efter minskad omsättning (SEK) de senaste 4 veckorna mot de 4 före (störst förlust först).
--    tillganglighet: samma indelning som omsattning_tapp_per_produkt.sql, utifrån dagens status och lager.
--    tapp_tecken: sålde_inget_4v = noll enheter de senaste 4 veckorna; minskade_over_halften; minskade; lika_eller_fler.
--    ads_klick_*: Google Ads-klick på produkten (samma marknad) de senaste 4 veckorna och de 4 före; NULL = inga annonsrader för produkten.
--    Läs: en produkt som "sålde_inget_4v", "slut i lager nu" och där annonsklicken också föll tyder på att Google slutade visa den (som chinsstången
--    på DK i beslut-2026-10-14.md). En produkt som "finns i lager" men sålde_inget_4v och har kvar annonsklick är en annan fråga (pris, sida, flöde).
WITH nyckel AS (
  SELECT pid, marknad FROM pm
), spine AS (
  SELECT n.pid, n.marknad, w AS vecka
  FROM nyckel n CROSS JOIN UNNEST(GENERATE_DATE_ARRAY(v_forsta, v_sista, INTERVAL 1 WEEK)) AS w
), vv AS (
  SELECT s.pid, s.marknad,
         STRING_AGG(IF(s.vecka < o_forsta, '?', CAST(IFNULL(k.enh, 0) AS STRING)), '-' ORDER BY s.vecka) AS enh_per_vecka,
         SUM(IF(s.vecka BETWEEN s4_start AND s4_slut, IFNULL(k.enh, 0), 0)) AS enh_s4,
         SUM(IF(s.vecka BETWEEN f4_start AND f4_slut, IFNULL(k.enh, 0), 0)) AS enh_f4,
         SUM(IF(s.vecka BETWEEN s4_start AND s4_slut, IFNULL(k.oms, 0), 0)) AS oms_s4,
         SUM(IF(s.vecka BETWEEN f4_start AND f4_slut, IFNULL(k.oms, 0), 0)) AS oms_f4
  FROM spine s LEFT JOIN vk k ON k.pid = s.pid AND k.marknad = s.marknad AND k.vecka = s.vecka
  GROUP BY 1, 2
)
SELECT p.marknad, IFNULL(pr.titel, p.radtitel) AS produkt, p.pid,
       ROUND(p.oms_rang) AS oms_rangperiod_sek, p.enh_rang AS enh_rangperiod,
       v.enh_per_vecka, v.enh_f4 AS enh_4v_fore, v.enh_s4 AS enh_4v_senaste,
       ROUND(SAFE_DIVIDE(v.enh_s4 - v.enh_f4, v.enh_f4) * 100) AS enh_forandring_pct,
       ROUND(v.oms_s4 - v.oms_f4) AS forandring_oms_sek,
       p.sista_order, DATE_DIFF(DATE_SUB(idag, INTERVAL 1 DAY), p.sista_order, DAY) AS dagar_sedan_sista_order,
       CASE WHEN pr.pid IS NULL THEN 'borttagen ur butiken'
            WHEN pr.status != 'ACTIVE' THEN 'inte aktiv (utkast/arkiverad)'
            WHEN IFNULL(pr.lager, 0) <= 0 THEN 'slut i lager nu'
            ELSE 'finns i lager' END AS tillganglighet,
       pr.status, pr.lager AS lager_totalt, vr.antal_varianter, vr.varianter_i_lager,
       CASE WHEN v.enh_s4 = 0 THEN 'sålde_inget_4v'
            WHEN v.enh_f4 > 0 AND v.enh_s4 <= 0.5 * v.enh_f4 THEN 'minskade_over_halften'
            WHEN v.enh_s4 < v.enh_f4 THEN 'minskade'
            ELSE 'lika_eller_fler' END AS tapp_tecken,
       a.klick_f4 AS ads_klick_4v_fore, a.klick_s4 AS ads_klick_4v_senaste
FROM pm p
JOIN vv v ON v.pid = p.pid AND v.marknad = p.marknad
LEFT JOIN prod pr ON pr.pid = p.pid
LEFT JOIN varianter vr ON vr.pid = p.pid
LEFT JOIN ads a ON a.pid = p.pid AND a.marknad = p.marknad
ORDER BY forandring_oms_sek ASC, p.oms_rang DESC;

-- 2. Avstämning mot totalen i rangordningsperioden (SEK): hur stor del av marknadens omsättning de 30 produkterna är, och hur mycket som inte gick att
--    placera på en produkt (orderrader utan produkt-id). Totalen räknas från samma orderrader som rangordningen (tabellen "rader"), inte från orders.
SELECT r.marknad,
       ROUND(SUM(r.oms)) AS total_oms_sek,
       ROUND(SUM(IF(r.pid IS NULL, r.oms, 0))) AS utan_produkt_id_sek,
       ROUND(SUM(IF(t.pid IS NOT NULL, r.oms, 0))) AS topp30_sek,
       ROUND(SAFE_DIVIDE(SUM(IF(t.pid IS NOT NULL, r.oms, 0)), SUM(r.oms)) * 100, 1) AS topp30_andel_pct
FROM rader r LEFT JOIN topp t ON t.pid = r.pid
WHERE r.d BETWEEN r_start AND r_slut AND r.marknad IN ('SE', 'DK')
GROUP BY 1 ORDER BY 1;
