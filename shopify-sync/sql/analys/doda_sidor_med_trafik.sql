-- Produktsidor som inte längre är aktiva men som fortfarande får besök, de senaste 30 dagarna.
-- Grunden för 301-omdirigeringar: börja med sidorna som har flest besök.
--
--   sed -e 's/PROJ/gorilla-sports-data/g' -e 's/KEY/gorillasports_se/g' -e 's/HOST/gorillasports.se/g' sql/analys/doda_sidor_med_trafik.sql | bq query --use_legacy_sql=false
--
-- Förutsättning: GA4-landningssidor (ga4_landing_daily_KEY) och Shopify-synken (shopify.products) finns.
-- Läsning: status ARCHIVED eller DRAFT betyder att sidan oftast ger 404. "saknas_i_shopify" betyder att produkten inte
-- finns alls (raderad). Besök räknas från GA4:s landing-kolumn; filtrera bort språkprefix om landing har sådana.
-- HOST är domänen som ska granskas (t.ex. gorillasports.se). Filtret behövs eftersom GA4-egenskapen delas av flera domäner och
-- Shopify-tabellen bara har huvudspråkets handle: översatta adresser på .dk skulle annars se ut som saknade produkter.
-- Köp på en 'saknad' sida betyder nästan alltid att sidan fungerar, så titta på sessioner utan köp först.
-- OBS: kontrollera målen manuellt innan omdirigering; site-audit föreslår mål i redirects_import.csv.

WITH landing AS (
  SELECT LOWER(REGEXP_EXTRACT(landing, r'/products/([^/?#]+)')) AS handle,
         SUM(sessions) AS sessions, SUM(purchases) AS purchases
  FROM `PROJ.site_audit.ga4_landing_daily_KEY`
  WHERE d >= DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 30 DAY)
    AND REGEXP_CONTAINS(landing, r'/products/')
    AND LOWER(hostname) LIKE '%HOST'
  GROUP BY 1
),
p AS (
  SELECT LOWER(handle) AS handle, ANY_VALUE(status) AS status, ANY_VALUE(title) AS title, ANY_VALUE(total_inventory) AS stock
  FROM `PROJ.shopify.products`
  GROUP BY 1
)
SELECT l.handle, p.title, IFNULL(p.status, 'saknas_i_shopify') AS status, p.stock, l.sessions, l.purchases
FROM landing l LEFT JOIN p USING (handle)
WHERE p.handle IS NULL OR p.status != 'ACTIVE'
ORDER BY l.sessions DESC
LIMIT 100;
