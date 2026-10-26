-- Kör Davids ark "SWE - Net Profit" (flik SWE - Net Profit - Fredrik) mot Gorillas ordrar de senaste 30 dagarna, per marknad.
-- Tar reda på vilka ordrar där kunden betalar frakt och vilka som får fri frakt, vilka som ligger över och under fraktgränsen, och vad en order faktiskt ger.
--
-- Förberedelse (en gång, i Cloud Shell, efter git pull):
--   bq load --replace --source_format=CSV --skip_leading_rows=1 \
--     --schema='sku:STRING,produkt:STRING,selling_price_sek:FLOAT,buying_eur:FLOAT,buying_sek:FLOAT,shipping_eur:FLOAT,payment_fee_pct:FLOAT' \
--     gorilla-sports-data:site_audit.swe_net_profit_sku data/swe_net_profit_sku.csv
-- Körning:
--   sed 's/PROJ/gorilla-sports-data/g' sql/analys/net_profit_ordrar.sql | bq query --use_legacy_sql=false --max_rows=80
--
-- Förutsättningar och antaganden (kontrollera dem):
--  * Skutabellen kommer ur arket: inköpspris i SEK (kolumn H, omräknat), fraktkostnad per st i EUR (kolumn I) och betalavgift i procent av nettoförsäljningen (kolumn J).
--    Två SKU hade felaktig SEK-kolumn i arket (SEK lika med EUR) och är omräknade med arkets kurs 11,13537. Fyra SKU fanns mer än en gång; den sista raden gäller.
--  * Fraktkostnad per order = summan av antal * fraktkostnad per SKU (varje produkt antas skickas för sig), omräknad med EUR till SEK 11,4 (arkets kurs).
--  * Orders-tabellens belopp är i butikens valuta (SEK), även för DK. Radbelopp (discounted_total) och subtotal_price antas innehålla 25 % moms.
--  * "Ordervärde" = subtotal_price (efter rabatt, före frakt). Fraktgränsen för SE är 800 kr (David). Gränsen för DK är okänd: del 1 visar var den ligger i data.
--  * Staff 10 % och övrigt 5 % av nettoförsäljningen enligt arkets SE-flik.
--  * Beräkningen görs bara på ordrar där minst 90 % av radvärdet kunde kopplas till en SKU i arket (täckning visas).

DECLARE d1 DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 1 DAY);
DECLARE d0 DATE DEFAULT DATE_SUB(d1, INTERVAL 29 DAY);
DECLARE fx_frakt FLOAT64 DEFAULT 11.4;
DECLARE moms FLOAT64 DEFAULT 1.25;
DECLARE se_grans FLOAT64 DEFAULT 800.0;
DECLARE dk_grans FLOAT64 DEFAULT 800.0;
DECLARE staff_pct FLOAT64 DEFAULT 0.10;
DECLARE misc_pct FLOAT64 DEFAULT 0.05;

CREATE TEMP TABLE ord AS
SELECT o.id, CASE o.presentment_currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE o.presentment_currency END AS market,
       o.subtotal_price AS ordervarde, o.total_shipping AS frakt_betald, o.total_price, o.total_price_presentment
FROM `PROJ.shopify.orders` o
WHERE o.cancelled_at IS NULL AND DATE(o.created_at, 'Europe/Stockholm') BETWEEN d0 AND d1;

CREATE TEMP TABLE lin AS
SELECT li.order_id, SUM(li.discounted_total) AS varor_inkl_moms,
       SUM(IF(s.sku IS NOT NULL, li.discounted_total, 0)) AS kopplat_varde,
       SUM(IF(s.sku IS NOT NULL, li.quantity * s.buying_sek, 0)) AS cogs,
       SUM(IF(s.sku IS NOT NULL, li.quantity * s.shipping_eur * fx_frakt, 0)) AS fraktkostnad,
       SUM(IF(s.sku IS NOT NULL, li.discounted_total / moms * IFNULL(s.payment_fee_pct, 0.018), 0)) AS betalavgift_varor
FROM `PROJ.shopify.order_line_items` li
LEFT JOIN `PROJ.site_audit.swe_net_profit_sku` s ON TRIM(li.sku) = s.sku
WHERE li.order_id IN (SELECT id FROM ord)
GROUP BY 1;

CREATE TEMP TABLE o2 AS
SELECT ord.*, lin.varor_inkl_moms, lin.kopplat_varde, lin.cogs, lin.fraktkostnad, lin.betalavgift_varor,
       SAFE_DIVIDE(lin.kopplat_varde, lin.varor_inkl_moms) AS tackning,
       CASE ord.market WHEN 'SE' THEN se_grans WHEN 'DK' THEN dk_grans END AS grans,
       ord.frakt_betald > 0 AS betalar_frakt
FROM ord LEFT JOIN lin ON lin.order_id = ord.id;

-- 1. Var ligger fraktgränsen? Andel ordrar där kunden betalade frakt, per ordervärde (steg om 100 kr, butikens valuta)
SELECT market, CAST(FLOOR(ordervarde / 100) * 100 AS INT64) AS ordervarde_fran, COUNT(*) AS ordrar,
       ROUND(COUNTIF(betalar_frakt) / COUNT(*) * 100) AS andel_med_fraktavgift_pct,
       ROUND(AVG(IF(betalar_frakt, frakt_betald, NULL))) AS snitt_fraktavgift
FROM o2 WHERE market IN ('SE', 'DK') AND ordervarde < 2000
GROUP BY 1, 2 ORDER BY 1, 2;

-- 2. Över/under gränsen mot om kunden faktiskt betalade frakt
SELECT market, ordervarde >= grans AS over_grans, betalar_frakt AS betalade_frakt, COUNT(*) AS ordrar,
       ROUND(AVG(ordervarde)) AS snitt_ordervarde, ROUND(AVG(IF(betalar_frakt, frakt_betald, NULL))) AS snitt_fraktavgift
FROM o2 WHERE market IN ('SE', 'DK') GROUP BY 1, 2, 3 ORDER BY 1, 2, 3;

-- 3. Täckning: hur stor del av radvärdet gick att koppla till en SKU i arket
SELECT market, COUNT(*) AS ordrar, ROUND(SUM(kopplat_varde) / SUM(varor_inkl_moms) * 100, 1) AS tackning_varde_pct,
       COUNTIF(tackning >= 0.9) AS ordrar_med_minst_90_pct
FROM o2 WHERE market IN ('SE', 'DK') GROUP BY 1 ORDER BY 1;

-- 4. Vad en order ger (ordrar med minst 90 % täckning), per marknad och över/under fraktgränsen. Belopp i SEK exklusive moms.
CREATE TEMP TABLE res AS
SELECT market, ordervarde >= grans AS over_grans, COUNT(*) AS ordrar,
       SUM((varor_inkl_moms + frakt_betald) / moms) AS nettoforsaljning,
       SUM(frakt_betald / moms) AS fraktintakt,
       SUM(cogs) AS varukostnad, SUM(fraktkostnad) AS fraktkostnad,
       SUM(betalavgift_varor + frakt_betald / moms * 0.018) AS betalavgift
FROM o2 WHERE market IN ('SE', 'DK') AND tackning >= 0.9 GROUP BY 1, 2;

SELECT market, over_grans, ordrar,
       ROUND(nettoforsaljning) AS nettoforsaljning, ROUND(fraktintakt) AS fraktintakt, ROUND(varukostnad) AS varukostnad,
       ROUND(fraktkostnad) AS fraktkostnad, ROUND(betalavgift) AS betalavgift,
       ROUND(nettoforsaljning - varukostnad - fraktkostnad - betalavgift) AS contribution,
       ROUND((nettoforsaljning - varukostnad - fraktkostnad - betalavgift) / nettoforsaljning * 100, 1) AS contribution_pct,
       ROUND(varukostnad / nettoforsaljning * 100, 1) AS varukostnad_pct, ROUND(fraktkostnad / nettoforsaljning * 100, 1) AS fraktkostnad_pct,
       ROUND(fraktintakt / nettoforsaljning * 100, 1) AS fraktintakt_pct
FROM res ORDER BY market, over_grans;

-- 5. Summa per marknad och efter annonser (Google + Meta i SEK), personal och övrigt. Procent av nettoförsäljningen (exkl. moms).
WITH tot AS (
  SELECT market, SUM(ordrar) AS ordrar, SUM(nettoforsaljning) AS nf, SUM(varukostnad) AS vk, SUM(fraktkostnad) AS fk, SUM(betalavgift) AS ba
  FROM res GROUP BY 1
), fxm AS (
  SELECT market, SAFE_DIVIDE(SUM(total_price), SUM(total_price_presentment)) AS sek_per_val,
         SUM((varor_inkl_moms + frakt_betald) / moms) AS nf_alla
  FROM o2 WHERE market IN ('SE', 'DK') GROUP BY 1
), ads AS (
  SELECT market, SUM(kostnad) AS annonskostnad FROM (
    SELECT CASE currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE currency END AS market, SUM(cost) AS kostnad
    FROM `PROJ.site_audit.google_ads_daily_gorillasports_se` WHERE d BETWEEN d0 AND d1 GROUP BY 1
    UNION ALL
    SELECT CASE currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE currency END, SUM(spend)
    FROM `PROJ.site_audit.meta_ads_daily_gorillasports_se` WHERE d BETWEEN d0 AND d1 GROUP BY 1
  ) GROUP BY 1
)
SELECT t.market, t.ordrar AS ordrar_inkluderade, ROUND(t.nf) AS nettoforsaljning_inkluderad, ROUND(f.nf_alla) AS nettoforsaljning_alla_ordrar,
       ROUND((t.nf - t.vk - t.fk - t.ba) / t.nf * 100, 1) AS contribution_pct,
       ROUND(a.annonskostnad * f.sek_per_val / f.nf_alla * 100, 1) AS annonser_pct_av_netto,
       staff_pct * 100 AS personal_pct, misc_pct * 100 AS ovrigt_pct,
       ROUND((t.nf - t.vk - t.fk - t.ba) / t.nf * 100 - a.annonskostnad * f.sek_per_val / f.nf_alla * 100 - staff_pct * 100 - misc_pct * 100, 1) AS nettovinst_pct
FROM tot t JOIN fxm f USING (market) JOIN ads a USING (market) ORDER BY 1;
