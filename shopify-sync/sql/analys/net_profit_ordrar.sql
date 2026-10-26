-- Kör Davids ark "SWE - Net Profit" (SE) och "DK - Net Profit" mot Gorillas ordrar de senaste 30 dagarna, per marknad.
-- Visar var fraktgränsen ligger, vilka som betalar frakt, vad en order ger efter varukostnad, frakt och avgifter, och vad som blir kvar efter annonser.
--
-- Förberedelse (en gång, i Cloud Shell efter git pull):
--   1) SKU-tabellen ur arken:
--      bq load --replace --source_format=CSV --skip_leading_rows=1 \
--        --schema='market:STRING,sku:STRING,produkt:STRING,net_selling_eur:FLOAT,buying_eur:FLOAT,shipping_eur:FLOAT,payment_fee_pct:FLOAT,conversion_fee_pct:FLOAT' \
--        gorilla-sports-data:site_audit.net_profit_sku data/net_profit_sku.csv
--   2) Vikter ur Shopify (läs-token räcker), se scripts/hamta_vikter.py, sedan:
--      bq load --replace --source_format=CSV --skip_leading_rows=1 --schema='sku:STRING,vikt_kg:FLOAT' \
--        gorilla-sports-data:site_audit.gorilla_vikter ~/vikter_gorilla.csv
-- Körning:
--   sed 's/PROJ/gorilla-sports-data/g' sql/analys/net_profit_ordrar.sql | bq query --use_legacy_sql=false --max_rows=100
--
-- Antaganden (kontrollera dem):
--  * Allt räknas i EUR enligt arkens egna kurser (cell B2): SEK per EUR 11,4 och DKK per EUR 8,0. Intäkter i kundens valuta (SEK respektive DKK) delas med kursen.
--  * Kolumn D (SE) är pris inklusive moms; kolumn F är nettopris i EUR. Intäkten delas med 1,25 för att få nettoförsäljning.
--  * Orders-tabellens belopp (shop currency, SEK) räknas om till kundens valuta med total_price_presentment / total_price. Orderrader har ingen egen DKK-summa.
--  * Fraktgränsen: SE 800 kr (David). DK: okänd, del 1 visar var den ligger; förinställt 700 DKK (ska bekräftas).
--  * Fraktkostnaden i arken är per produkt. Ett paket får väga högst 30 kg; vikter hämtas ur Shopify. Utan en fraktprislista per vikt redovisas ett spann:
--      FRAKT_LÅG  = dyraste enskilda fraktkostnaden i ordern gånger antalet paket (CEIL(vikt / 30)). Underskattar om den samlade vikten ger ett dyrare paket.
--      FRAKT_HÖG  = summan av antal * fraktkostnad per SKU (varje produkt skickas för sig). Överskattar om produkterna går i samma paket.
--    Verkligheten ligger mellan dem. Saknas vikt antas ett paket för den ordern (avsnitt 3 visar täckningen).
--  * Betalavgift: per SKU ur arket (betalavgift och konverteringsavgift för DK) som procent av nettoförsäljningen; på fraktintäkten 1,8 % (SE) och 3,6 % (DK).
--  * Personal och övrigt enligt arken: SE 10 % och 5 %, DK 8 % och 5 % av nettoförsäljningen.
--  * Bara ordrar där minst 90 % av radvärdet kunde kopplas till en SKU i arket räknas i del 4 och 5.

DECLARE d1 DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 1 DAY);
DECLARE d0 DATE DEFAULT DATE_SUB(d1, INTERVAL 29 DAY);
DECLARE fx_se FLOAT64 DEFAULT 11.4;
DECLARE fx_dk FLOAT64 DEFAULT 8.0;
DECLARE moms FLOAT64 DEFAULT 1.25;
DECLARE se_grans FLOAT64 DEFAULT 800.0;
DECLARE dk_grans FLOAT64 DEFAULT 700.0;
DECLARE paket_kg FLOAT64 DEFAULT 30.0;
DECLARE avg_frakt_se FLOAT64 DEFAULT 0.018;
DECLARE avg_frakt_dk FLOAT64 DEFAULT 0.036;

CREATE TEMP TABLE ord AS
SELECT o.id, CASE o.presentment_currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE o.presentment_currency END AS market,
       SAFE_DIVIDE(o.total_price_presentment, o.total_price) AS kvot,
       o.subtotal_price * SAFE_DIVIDE(o.total_price_presentment, o.total_price) AS ordervarde,
       o.total_shipping * SAFE_DIVIDE(o.total_price_presentment, o.total_price) AS frakt_betald,
       IF(o.presentment_currency = 'DKK', fx_dk, fx_se) AS fx
FROM `PROJ.shopify.orders` o
WHERE o.cancelled_at IS NULL AND DATE(o.created_at, 'Europe/Stockholm') BETWEEN d0 AND d1;

CREATE TEMP TABLE lin AS
SELECT ord.id AS order_id,
       SUM(li.discounted_total * ord.kvot / ord.fx) AS varor_eur,
       SUM(IF(s.sku IS NOT NULL, li.discounted_total * ord.kvot / ord.fx, 0)) AS kopplat_eur,
       SUM(IF(s.sku IS NOT NULL, li.quantity * s.buying_eur, 0)) AS cogs,
       SUM(IF(s.sku IS NOT NULL, li.quantity * s.shipping_eur, 0)) AS frakt_hog,
       MAX(IF(s.sku IS NOT NULL, s.shipping_eur, NULL)) AS frakt_max,
       SUM(IF(s.sku IS NOT NULL, li.discounted_total * ord.kvot / ord.fx / moms * (IFNULL(s.payment_fee_pct, 0.018) + IFNULL(s.conversion_fee_pct, 0)), 0)) AS avgift_varor,
       SUM(li.quantity * IFNULL(v.vikt_kg, 0)) AS kg_total,
       COUNTIF(s.sku IS NOT NULL AND IFNULL(v.vikt_kg, 0) = 0) AS rader_utan_vikt
FROM ord
JOIN `PROJ.shopify.order_line_items` li ON li.order_id = ord.id
LEFT JOIN `PROJ.site_audit.net_profit_sku` s ON s.market = ord.market AND s.sku = TRIM(li.sku)
LEFT JOIN `PROJ.site_audit.gorilla_vikter` v ON v.sku = TRIM(li.sku)
GROUP BY 1;

CREATE TEMP TABLE o2 AS
SELECT ord.*, lin.varor_eur, lin.kopplat_eur, lin.cogs, lin.frakt_hog, lin.frakt_max, lin.avgift_varor, lin.kg_total, lin.rader_utan_vikt,
       SAFE_DIVIDE(lin.kopplat_eur, lin.varor_eur) AS tackning,
       ord.frakt_betald > 0 AS betalar_frakt,
       ord.ordervarde >= IF(ord.market = 'SE', se_grans, dk_grans) AS over_grans,
       IF(lin.kg_total > 0, CEIL(lin.kg_total / paket_kg), 1) AS paket,
       IFNULL(lin.frakt_max, 0) * IF(lin.kg_total > 0, CEIL(lin.kg_total / paket_kg), 1) AS frakt_lag,
       ord.frakt_betald / ord.fx AS frakt_intakt_eur
FROM ord LEFT JOIN lin ON lin.order_id = ord.id;

-- 1. Var ligger fraktgränsen? Andel ordrar där kunden betalade frakt, per ordervärde i kundens valuta (SE i SEK, DK i DKK), steg om 100
SELECT market, CAST(FLOOR(ordervarde / 100) * 100 AS INT64) AS ordervarde_fran, COUNT(*) AS ordrar,
       ROUND(COUNTIF(betalar_frakt) / COUNT(*) * 100) AS andel_med_fraktavgift_pct,
       ROUND(AVG(IF(betalar_frakt, frakt_betald, NULL))) AS snitt_fraktavgift
FROM o2 WHERE market IN ('SE', 'DK') AND ordervarde < 2000 GROUP BY 1, 2 ORDER BY 1, 2;

-- 2. Över/under gränsen mot om kunden faktiskt betalade frakt (nollvärdesordrar är utkast och ersättningsordrar)
SELECT market, over_grans, betalar_frakt AS betalade_frakt, COUNT(*) AS ordrar, COUNTIF(ordervarde = 0) AS varav_nollvarde,
       ROUND(AVG(ordervarde)) AS snitt_ordervarde, ROUND(AVG(IF(betalar_frakt, frakt_betald, NULL))) AS snitt_fraktavgift
FROM o2 WHERE market IN ('SE', 'DK') GROUP BY 1, 2, 3 ORDER BY 1, 2, 3;

-- 3. Täckning: SKU-koppling och vikter, och hur många ordrar som överstiger ett paket (30 kg)
SELECT market, COUNT(*) AS ordrar, ROUND(SUM(kopplat_eur) / SUM(varor_eur) * 100, 1) AS tackning_varde_pct,
       COUNTIF(tackning >= 0.9) AS ordrar_med_minst_90_pct,
       COUNTIF(tackning >= 0.9 AND rader_utan_vikt = 0) AS ordrar_med_alla_vikter,
       COUNTIF(kg_total > paket_kg) AS ordrar_over_30_kg, ROUND(AVG(IF(kg_total > 0, kg_total, NULL)), 1) AS snitt_kg
FROM o2 WHERE market IN ('SE', 'DK') GROUP BY 1 ORDER BY 1;

-- 4. Vad en order ger (ordrar med minst 90 % täckning). EUR, exklusive moms. Spann för frakten: låg och hög.
CREATE TEMP TABLE res AS
SELECT market, over_grans, COUNT(*) AS ordrar,
       SUM((varor_eur + frakt_intakt_eur) / moms) AS nf,
       SUM(frakt_intakt_eur / moms) AS fraktintakt,
       SUM(cogs) AS varukostnad, SUM(frakt_lag) AS frakt_lag, SUM(frakt_hog) AS frakt_hog,
       SUM(avgift_varor + frakt_intakt_eur / moms * IF(market = 'SE', avg_frakt_se, avg_frakt_dk)) AS avgift
FROM o2 WHERE market IN ('SE', 'DK') AND tackning >= 0.9 GROUP BY 1, 2;

SELECT market, over_grans, ordrar, ROUND(nf) AS nettoforsaljning_eur, ROUND(fraktintakt) AS fraktintakt, ROUND(varukostnad) AS varukostnad,
       ROUND(frakt_lag) AS frakt_lag, ROUND(frakt_hog) AS frakt_hog, ROUND(avgift) AS avgift,
       ROUND((nf - varukostnad - frakt_hog - avgift) / nf * 100, 1) AS contribution_pct_hog_frakt,
       ROUND((nf - varukostnad - frakt_lag - avgift) / nf * 100, 1) AS contribution_pct_lag_frakt,
       ROUND(varukostnad / nf * 100, 1) AS varukostnad_pct, ROUND(frakt_lag / nf * 100, 1) AS frakt_lag_pct, ROUND(frakt_hog / nf * 100, 1) AS frakt_hog_pct,
       ROUND(fraktintakt / nf * 100, 1) AS fraktintakt_pct
FROM res ORDER BY market, over_grans;

-- 5. Summa per marknad efter annonser (Google + Meta), personal och övrigt. Procent av nettoförsäljningen (alla ordrar), spann efter frakt.
WITH tot AS (
  SELECT market, SUM(ordrar) AS ordrar, SUM(nf) AS nf, SUM(varukostnad) AS vk, SUM(frakt_lag) AS fl, SUM(frakt_hog) AS fh, SUM(avgift) AS ba FROM res GROUP BY 1
), alla AS (
  SELECT market, ANY_VALUE(fx) AS fx, SUM((varor_eur + frakt_intakt_eur) / moms) AS nf_alla FROM o2 WHERE market IN ('SE', 'DK') GROUP BY 1
), ads AS (
  SELECT market, SUM(kostnad) AS annonskostnad FROM (
    SELECT CASE currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE currency END AS market, SUM(cost) AS kostnad
    FROM `PROJ.site_audit.google_ads_daily_gorillasports_se` WHERE d BETWEEN d0 AND d1 GROUP BY 1
    UNION ALL
    SELECT CASE currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE currency END, SUM(spend)
    FROM `PROJ.site_audit.meta_ads_daily_gorillasports_se` WHERE d BETWEEN d0 AND d1 GROUP BY 1
  ) GROUP BY 1
), cfg AS (
  SELECT 'SE' AS market, 0.10 AS staff, 0.05 AS misc UNION ALL SELECT 'DK', 0.08, 0.05
)
SELECT t.market, t.ordrar AS ordrar_inkluderade, ROUND(t.nf) AS nf_inkluderad_eur, ROUND(a.nf_alla) AS nf_alla_eur,
       ROUND((t.nf - t.vk - t.fh - t.ba) / t.nf * 100, 1) AS contribution_pct_hog_frakt,
       ROUND((t.nf - t.vk - t.fl - t.ba) / t.nf * 100, 1) AS contribution_pct_lag_frakt,
       ROUND(ad.annonskostnad / a.fx / a.nf_alla * 100, 1) AS annonser_pct_av_netto,
       c.staff * 100 AS personal_pct, c.misc * 100 AS ovrigt_pct,
       ROUND((t.nf - t.vk - t.fh - t.ba) / t.nf * 100 - ad.annonskostnad / a.fx / a.nf_alla * 100 - (c.staff + c.misc) * 100, 1) AS nettovinst_pct_hog_frakt,
       ROUND((t.nf - t.vk - t.fl - t.ba) / t.nf * 100 - ad.annonskostnad / a.fx / a.nf_alla * 100 - (c.staff + c.misc) * 100, 1) AS nettovinst_pct_lag_frakt
FROM tot t JOIN alla a USING (market) JOIN ads ad USING (market) JOIN cfg c USING (market) ORDER BY 1;
