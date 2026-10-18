-- Datakvalitet för tillväxtdatan: färskhet, luckor och skillnader mellan tabeller som borde visa samma sak.
--
--   sed 's/PROJ/gorilla-sports-data/g' sql/growth/datakvalitet.sql | bq query --use_legacy_sql=false
--
-- Tabellnamnen gäller butiken gorillasports_se. För en annan butik byts suffixet mot butikens data_key.
-- Varje fråga svarar på en konkret kontrollfråga och är bara läsning.

-- 1. Färskhet: när kom senaste dagen in i varje källa? Mer än 3 dagar efter dagens datum betyder att hämtningen stannat.
SELECT källa, senaste, DATE_DIFF(CURRENT_DATE('Europe/Stockholm'), senaste, DAY) AS dagar_sedan FROM (
  SELECT 'Shopify-ordrar' AS källa, MAX(DATE(created_at, 'Europe/Stockholm')) AS senaste FROM `PROJ.shopify.orders`
  UNION ALL SELECT 'GA4 landningssidor', MAX(d) FROM `PROJ.site_audit.ga4_landing_daily_gorillasports_se`
  UNION ALL SELECT 'GA4 kanaler', MAX(d) FROM `PROJ.site_audit.ga4_channel_daily_gorillasports_se`
  UNION ALL SELECT 'Google Ads kampanjer', MAX(d) FROM `PROJ.site_audit.google_ads_daily_gorillasports_se`
  UNION ALL SELECT 'Google Ads produkter', MAX(d) FROM `PROJ.site_audit.google_ads_products_daily_gorillasports_se`
  UNION ALL SELECT 'Meta-annonser', MAX(d) FROM `PROJ.site_audit.meta_ads_daily_gorillasports_se`
) ORDER BY dagar_sedan DESC;

-- 2. Luckor: dagar utan rader per annonskonto sedan 1 juli 2025 (Meta skapar bara rader för dagar med aktivitet,
--    så en lucka kan vara pausade kampanjer och behöver kontrolleras i Ads Manager).
WITH dagar AS (SELECT d FROM UNNEST(GENERATE_DATE_ARRAY('2025-07-01', DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 1 DAY))) AS d),
konton AS (
  SELECT 'Google Ads' AS källa, currency AS valuta FROM `PROJ.site_audit.google_ads_daily_gorillasports_se` GROUP BY 2
  UNION ALL SELECT 'Meta', currency FROM `PROJ.site_audit.meta_ads_daily_gorillasports_se` GROUP BY 2),
har AS (
  SELECT 'Google Ads' AS källa, currency AS valuta, d FROM `PROJ.site_audit.google_ads_daily_gorillasports_se` GROUP BY 2, 3
  UNION ALL SELECT 'Meta', currency, d FROM `PROJ.site_audit.meta_ads_daily_gorillasports_se` GROUP BY 2, 3)
SELECT k.källa, k.valuta, COUNT(*) AS saknade_dagar, ARRAY_AGG(dg.d ORDER BY dg.d LIMIT 20) AS första_20_dagarna
FROM konton k CROSS JOIN dagar dg
LEFT JOIN har h ON h.källa = k.källa AND h.valuta = k.valuta AND h.d = dg.d
WHERE h.d IS NULL GROUP BY 1, 2 ORDER BY 1, 2;

-- 3. GA4: skillnaden mellan landningssidetabellen och kanaltabellen per dag och domän (beslut AE).
--    Visar om skillnaden är jämn över hela perioden (olika mätsätt) eller kommer från vissa dagar eller domäner (fel).
WITH a AS (SELECT d, hostname, SUM(sessions) AS s FROM `PROJ.site_audit.ga4_landing_daily_gorillasports_se` GROUP BY 1, 2),
     b AS (SELECT d, hostname, SUM(sessions) AS s FROM `PROJ.site_audit.ga4_channel_daily_gorillasports_se` GROUP BY 1, 2)
SELECT COALESCE(a.hostname, b.hostname) AS domän, DATE_TRUNC(COALESCE(a.d, b.d), WEEK(MONDAY)) AS vecka,
       SUM(a.s) AS besök_landningssidor, SUM(b.s) AS besök_kanaler,
       ROUND(SAFE_DIVIDE(SUM(b.s) - SUM(a.s), SUM(a.s)) * 100, 1) AS skillnad_pct
FROM a FULL JOIN b ON a.d = b.d AND a.hostname = b.hostname
WHERE COALESCE(a.d, b.d) >= '2026-03-19' GROUP BY 1, 2 ORDER BY 1, 2;

-- 4. GA4: poster utan kanal eller kampanj ("(not set)") som kan förklara att kanaltabellen räknar annorlunda.
SELECT channel, COUNT(*) AS rader, SUM(sessions) AS besök,
       ROUND(SUM(sessions) / SUM(SUM(sessions)) OVER () * 100, 1) AS andel_pct
FROM `PROJ.site_audit.ga4_channel_daily_gorillasports_se` WHERE d >= '2026-03-19' GROUP BY 1 ORDER BY besök DESC;

-- 5. Annonsprodukter som inte kunde kopplas till en Shopify-variant (kräver att vyn growth_product_daily_* finns).
SELECT market, COUNTIF(matched) AS rader_kopplade, COUNTIF(NOT matched) AS rader_okopplade,
       ROUND(SAFE_DIVIDE(SUM(IF(matched, clicks, 0)), SUM(clicks)) * 100, 1) AS andel_klick_kopplade_pct
FROM `PROJ.site_audit.growth_product_daily_gorillasports_se` GROUP BY 1;

-- 6. Dubbletter: ska vara noll rader. Samma dag, konto och kampanj får inte förekomma två gånger.
SELECT 'Google Ads' AS källa, d, customer_id, campaign_id, COUNT(*) AS antal
FROM `PROJ.site_audit.google_ads_daily_gorillasports_se` GROUP BY 2, 3, 4 HAVING antal > 1
UNION ALL
SELECT 'Meta', d, account_id, campaign_id, COUNT(*)
FROM `PROJ.site_audit.meta_ads_daily_gorillasports_se` GROUP BY 2, 3, 4 HAVING COUNT(*) > 1
LIMIT 50;
