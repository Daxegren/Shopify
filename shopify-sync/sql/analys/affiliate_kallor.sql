-- Vilka ordrar kommer via Vibbar och andra affiliate-/partnerkällor? Underlag för att räkna affiliate-kostnaden (Vibbar, totalt 15 % enligt David 2026-10-28).
-- Vi vet inte hur Vibbar-ordrar märks i Shopify (UTM-källa, kampanj, landningssida eller rabattkod). Del 1 söker efter "vibbar" överallt; del 2 listar alla källor och del 3 alla rabattkoder, så att rätt märkning kan väljas.
-- Kolumner verifierade mot src/shopify_sync/schema.py: orders(created_at, cancelled_at, presentment_currency, subtotal_price, total_price, total_price_presentment, source_name, discount_codes,
--   first_visit_source, first_visit_utm_source, first_visit_utm_medium, first_visit_utm_campaign, first_visit_landing_page, last_visit_source, last_visit_utm_source, last_visit_utm_medium, last_visit_utm_campaign).
-- Period: senaste 30 dagarna till och med i går. Belopp = subtotal_price exkl. frakt, i kundens valuta (SEK respektive DKK); ingen valutaomräkning, ingen momsjustering.
-- Kör: sed 's/PROJ/gorilla-sports-data/g' sql/analys/affiliate_kallor.sql | bq query --use_legacy_sql=false --max_rows=100
-- Detta skript ändrar inget.

DECLARE d1 DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 1 DAY);
DECLARE d0 DATE DEFAULT DATE_SUB(d1, INTERVAL 29 DAY);

CREATE TEMP TABLE o AS
SELECT CASE presentment_currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE presentment_currency END AS marknad,
       subtotal_price * SAFE_DIVIDE(total_price_presentment, total_price) AS varuvarde,
       IFNULL(source_name, '') AS source_name, IFNULL(discount_codes, '') AS koder,
       IFNULL(first_visit_source, '') AS f_src, IFNULL(first_visit_utm_source, '') AS f_utm, IFNULL(first_visit_utm_medium, '') AS f_med,
       IFNULL(first_visit_utm_campaign, '') AS f_camp, IFNULL(first_visit_landing_page, '') AS f_land,
       IFNULL(last_visit_source, '') AS l_src, IFNULL(last_visit_utm_source, '') AS l_utm, IFNULL(last_visit_utm_medium, '') AS l_med,
       IFNULL(last_visit_utm_campaign, '') AS l_camp
FROM `PROJ.shopify.orders`
WHERE cancelled_at IS NULL AND DATE(created_at, 'Europe/Stockholm') BETWEEN d0 AND d1 AND presentment_currency IN ('SEK', 'DKK');

-- 1. Allt som nämner "vibbar" (källa, medium, kampanj, landningssida, rabattkod): antal ordrar och varuvärde. Om tomt märks Vibbar på annat sätt; se del 2 och 3.
SELECT marknad, COUNT(*) AS ordrar, ROUND(SUM(varuvarde)) AS varuvarde,
       ARRAY_AGG(DISTINCT CONCAT(l_utm, '/', l_med, '/', l_camp, ' kod=', koder) LIMIT 5) AS exempel
FROM o
WHERE REGEXP_CONTAINS(LOWER(CONCAT(source_name, ' ', koder, ' ', f_src, ' ', f_utm, ' ', f_med, ' ', f_camp, ' ', f_land, ' ', l_src, ' ', l_utm, ' ', l_med, ' ', l_camp)), r'vibbar')
GROUP BY marknad ORDER BY marknad;

-- 2. Alla senaste-besök-källor med medium och kampanj: antal ordrar och varuvärde (de 40 största). Leta efter affiliate-/partnerkällor (medium som affiliate, partner, cpa eller okänd kod).
SELECT marknad, IF(l_utm != '', l_utm, IF(l_src != '', l_src, source_name)) AS kalla, l_med AS medium, l_camp AS kampanj,
       COUNT(*) AS ordrar, ROUND(SUM(varuvarde)) AS varuvarde
FROM o GROUP BY 1, 2, 3, 4 ORDER BY varuvarde DESC LIMIT 40;

-- 3. Rabattkoder: antal ordrar och varuvärde (de 30 största). En partnerkod kan vara det som identifierar affiliate-försäljning.
SELECT marknad, koder AS rabattkod, COUNT(*) AS ordrar, ROUND(SUM(varuvarde)) AS varuvarde
FROM o WHERE koder != '' GROUP BY 1, 2 ORDER BY varuvarde DESC LIMIT 30;
