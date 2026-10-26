-- COS (annonskostnad i procent av intäkt) för Gorilla Sports, senaste 30 dagarna till och med i går, per marknad.
-- Visar vad olika sätt att räkna ger, vilka produkter som drar upp talet och vad COS blir om de sämsta produkterna tas bort från Google Shopping.
--
--   sed 's/PROJ/gorilla-sports-data/g' sql/analys/cos_30d.sql | bq query --use_legacy_sql=false --max_rows=80
--
-- COS = kostnad / intäkt (= 1 / ROAS). 22 % motsvarar ROAS 4,55; 28,44 % motsvarar ROAS 3,52.
-- Belopp i marknadens valuta (SE i SEK, DK i DKK) och summeras inte över marknader.
-- Simuleringen visar bara kostnad och plattformens konverteringsvärde: den antar att intäkten från borttagna produkter försvinner helt
-- och att kostnaden inte flyttas till andra produkter (Google kan i praktiken lägga om budgeten).

DECLARE d1 DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 1 DAY);
DECLARE d0 DATE DEFAULT DATE_SUB(d1, INTERVAL 29 DAY);

-- 1. Tre sätt att räkna COS
SELECT market,
       ROUND(SUM(revenue)) AS butiksomsattning,
       ROUND(SUM(google_cost)) AS google_kostnad, ROUND(SUM(google_value)) AS google_varde,
       ROUND(SUM(meta_cost)) AS meta_kostnad, ROUND(SUM(meta_value)) AS meta_varde,
       ROUND(SAFE_DIVIDE(SUM(google_cost), SUM(google_value)) * 100, 1) AS cos_google_plattform_pct,
       ROUND(SAFE_DIVIDE(IFNULL(SUM(google_cost), 0) + IFNULL(SUM(meta_cost), 0), IFNULL(SUM(google_value), 0) + IFNULL(SUM(meta_value), 0)) * 100, 1) AS cos_google_och_meta_plattform_pct,
       ROUND(SAFE_DIVIDE(IFNULL(SUM(google_cost), 0) + IFNULL(SUM(meta_cost), 0), SUM(revenue)) * 100, 1) AS annonskostnad_av_butiksomsattning_pct
FROM `PROJ.site_audit.growth_daily_gorillasports_se`
WHERE d BETWEEN d0 AND d1 AND market IN ('SE', 'DK')
GROUP BY 1 ORDER BY 1;

-- 2. Simulering: COS för Google om produkter med ROAS under tröskeln inte annonserades (per marknad)
CREATE TEMP TABLE prod AS
SELECT market, COALESCE(handle, item_id) AS produkt, ANY_VALUE(IFNULL(shopify_title, ads_title)) AS titel,
       SUM(cost) AS kostnad, SUM(clicks) AS klick, SUM(conversions_value) AS varde,
       SAFE_DIVIDE(SUM(conversions_value), SUM(cost)) AS roas
FROM `PROJ.site_audit.growth_product_daily_gorillasports_se`
WHERE d BETWEEN d0 AND d1 AND market IN ('SE', 'DK')
GROUP BY 1, 2 HAVING SUM(cost) > 0;

SELECT p.market, t AS troskel_roas,
       COUNTIF(IFNULL(p.roas, 0) < t) AS produkter_borttagna,
       ROUND(SUM(IF(IFNULL(p.roas, 0) < t, p.kostnad, 0))) AS borttagen_kostnad,
       ROUND(SUM(IF(IFNULL(p.roas, 0) < t, p.varde, 0))) AS borttaget_varde,
       ROUND(SUM(p.kostnad)) AS kostnad_nu, ROUND(SUM(p.varde)) AS varde_nu,
       ROUND(SAFE_DIVIDE(SUM(p.kostnad), SUM(p.varde)) * 100, 1) AS cos_nu_pct,
       ROUND(SAFE_DIVIDE(SUM(IF(IFNULL(p.roas, 0) >= t, p.kostnad, 0)), SUM(IF(IFNULL(p.roas, 0) >= t, p.varde, 0))) * 100, 1) AS cos_efter_pct
FROM prod p CROSS JOIN UNNEST([1.0, 2.0, 3.0, 4.0]) AS t
GROUP BY 1, 2 ORDER BY 1, 2;

-- 3. De 20 produkter som kostat mest per marknad
SELECT * FROM (
  SELECT market, titel, ROUND(kostnad) AS kostnad, klick, ROUND(varde) AS varde, ROUND(roas, 2) AS roas,
         ROW_NUMBER() OVER (PARTITION BY market ORDER BY kostnad DESC) AS rang
  FROM prod
) WHERE rang <= 20 ORDER BY market, rang;
