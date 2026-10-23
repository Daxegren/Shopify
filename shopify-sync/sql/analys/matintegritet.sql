-- Mätintegritet: stämmer GA4, annonsplattformen och Shopify överens om hur många köp som skett?
-- Svarar på: kan vi lita på konverteringssiffrorna, eller saknas mätning (taggar, samtycke, dubbelräkning)?
--
--   sed -e 's/PROJ/gorilla-sports-data/g' -e 's/KEY/bestofsports/g' -e 's/SHOPDS/shopify_bestofsports/g' \
--       sql/analys/matintegritet.sql | bq query --use_legacy_sql=false
--
-- Per vecka, senaste 8 veckorna. Shopify är facit (ordrar utan annullerade). GA4-köp och annonskonverteringar jämförs mot det.
-- Förhållande 0,8–1,2 är normalt (samtycke och blockerare gör att GA4 ofta ligger 10–20 % under). Långt under 0,6 eller över 1,4
-- tyder på saknad tagg, trasig köphändelse, dubbelräkning eller samtyckesproblem. Få ordrar ger brusiga kvoter: läs antalen.
DECLARE since DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 56 DAY);

WITH shop AS (
  SELECT DATE_TRUNC(DATE(created_at, 'Europe/Stockholm'), WEEK(MONDAY)) AS vecka, COUNT(*) AS shopify_ordrar
  FROM `PROJ.SHOPDS.orders`
  WHERE cancelled_at IS NULL AND DATE(created_at, 'Europe/Stockholm') >= since
  GROUP BY 1
), ga AS (
  SELECT DATE_TRUNC(d, WEEK(MONDAY)) AS vecka, SUM(purchases) AS ga4_kop, SUM(sessions) AS ga4_besok
  FROM `PROJ.site_audit.ga4_channel_daily_KEY`
  WHERE d >= since GROUP BY 1
), ads AS (
  SELECT DATE_TRUNC(d, WEEK(MONDAY)) AS vecka, ROUND(SUM(conversions), 1) AS annons_konv, ROUND(SUM(cost)) AS annons_kostnad
  FROM `PROJ.site_audit.google_ads_daily_KEY`
  WHERE d >= since GROUP BY 1
)
SELECT vecka, IFNULL(s.shopify_ordrar, 0) AS shopify_ordrar, g.ga4_kop, g.ga4_besok, a.annons_konv, a.annons_kostnad,
       ROUND(SAFE_DIVIDE(g.ga4_kop, s.shopify_ordrar), 2) AS ga4_per_shopify,
       ROUND(SAFE_DIVIDE(a.annons_konv, s.shopify_ordrar), 2) AS annons_per_shopify
FROM ga g FULL JOIN shop s USING (vecka) FULL JOIN ads a USING (vecka)
ORDER BY vecka DESC;
