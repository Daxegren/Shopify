-- COS (annonskostnad i procent av intäkt) för Gorilla Sports, senaste 30 dagarna till och med i går, per marknad.
-- Visar vad olika sätt att räkna ger, vilka produkter som drar upp talet och vad COS blir om de sämsta produkterna tas bort från Google Shopping.
--
--   sed 's/PROJ/gorilla-sports-data/g' sql/analys/cos_30d.sql | bq query --use_legacy_sql=false --max_rows=80
--
-- COS = kostnad / intäkt (= 1 / ROAS). 22 % motsvarar ROAS 4,55; 28,44 % motsvarar ROAS 3,52.
-- Läser bara basetabellerna (inga growth-vyer krävs): google_ads_daily, meta_ads_daily, google_ads_products_daily, shopify.orders, product_variants, products.
-- Belopp i marknadens valuta (SE i SEK, DK i DKK) och summeras inte över marknader.
-- Simuleringen visar bara kostnad och plattformens konverteringsvärde: den antar att intäkten från borttagna produkter försvinner helt
-- och att kostnaden inte flyttas till andra produkter (Google kan i praktiken lägga om budgeten).
-- Del 4 stämmer av att produktnivån täcker kampanjnivåns kostnad; är täckningen låg ska del 2 och 3 inte tolkas.

DECLARE d1 DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 1 DAY);
DECLARE d0 DATE DEFAULT DATE_SUB(d1, INTERVAL 29 DAY);

CREATE TEMP TABLE kamp AS
SELECT CASE currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE currency END AS market,
       SUM(cost) AS google_kostnad, SUM(conversions_value) AS google_varde
FROM `PROJ.site_audit.google_ads_daily_gorillasports_se`
WHERE d BETWEEN d0 AND d1 GROUP BY 1;

CREATE TEMP TABLE meta AS
SELECT CASE currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE currency END AS market,
       SUM(spend) AS meta_kostnad, SUM(purchase_value) AS meta_varde
FROM `PROJ.site_audit.meta_ads_daily_gorillasports_se`
WHERE d BETWEEN d0 AND d1 GROUP BY 1;

CREATE TEMP TABLE oms AS
SELECT CASE presentment_currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE presentment_currency END AS market,
       SUM(total_price_presentment) AS butiksomsattning
FROM `PROJ.shopify.orders`
WHERE cancelled_at IS NULL AND DATE(created_at, 'Europe/Stockholm') BETWEEN d0 AND d1 GROUP BY 1;

-- 1. Tre sätt att räkna COS
SELECT o.market, ROUND(o.butiksomsattning) AS butiksomsattning,
       ROUND(k.google_kostnad) AS google_kostnad, ROUND(k.google_varde) AS google_varde,
       ROUND(m.meta_kostnad) AS meta_kostnad, ROUND(m.meta_varde) AS meta_varde,
       ROUND(SAFE_DIVIDE(k.google_kostnad, k.google_varde) * 100, 1) AS cos_google_plattform_pct,
       ROUND(SAFE_DIVIDE(k.google_kostnad + IFNULL(m.meta_kostnad, 0), k.google_varde + IFNULL(m.meta_varde, 0)) * 100, 1) AS cos_google_och_meta_plattform_pct,
       ROUND(SAFE_DIVIDE(k.google_kostnad + IFNULL(m.meta_kostnad, 0), o.butiksomsattning) * 100, 1) AS annonskostnad_av_butiksomsattning_pct
FROM oms o LEFT JOIN kamp k USING (market) LEFT JOIN meta m USING (market)
WHERE o.market IN ('SE', 'DK') ORDER BY 1;

CREATE TEMP TABLE vp AS
SELECT REGEXP_EXTRACT(v.id, r'(\d+)$') AS vkey, REGEXP_EXTRACT(v.product_id, r'(\d+)$') AS pid
FROM `PROJ.shopify.product_variants` v;

CREATE TEMP TABLE pr AS
SELECT REGEXP_EXTRACT(id, r'(\d+)$') AS pid, ANY_VALUE(title) AS title FROM `PROJ.shopify.products` GROUP BY 1;

CREATE TEMP TABLE prod AS
SELECT CASE a.currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE a.currency END AS market,
       IFNULL(vp.pid, a.item_id) AS produkt, ANY_VALUE(IFNULL(pr.title, a.title)) AS titel,
       SUM(a.cost) AS kostnad, SUM(a.clicks) AS klick, SUM(a.conversions_value) AS varde,
       SAFE_DIVIDE(SUM(a.conversions_value), SUM(a.cost)) AS roas,
       LOGICAL_OR(vp.vkey IS NULL) AS delvis_okopplad
FROM `PROJ.site_audit.google_ads_products_daily_gorillasports_se` a
LEFT JOIN vp ON vp.vkey = REGEXP_EXTRACT(a.item_id, r'(\d+)$')
LEFT JOIN pr ON pr.pid = vp.pid
WHERE a.d BETWEEN d0 AND d1 GROUP BY 1, 2 HAVING SUM(a.cost) > 0;

-- 2. Simulering: COS för Google om produkter med ROAS under tröskeln inte annonserades (per marknad)
SELECT p.market, t AS troskel_roas,
       COUNTIF(IFNULL(p.roas, 0) < t) AS produkter_borttagna, COUNT(*) AS produkter_totalt,
       ROUND(SUM(IF(IFNULL(p.roas, 0) < t, p.kostnad, 0))) AS borttagen_kostnad,
       ROUND(SUM(IF(IFNULL(p.roas, 0) < t, p.varde, 0))) AS borttaget_varde,
       ROUND(SUM(p.kostnad)) AS kostnad_nu, ROUND(SUM(p.varde)) AS varde_nu,
       ROUND(SAFE_DIVIDE(SUM(p.kostnad), SUM(p.varde)) * 100, 1) AS cos_nu_pct,
       ROUND(SAFE_DIVIDE(SUM(IF(IFNULL(p.roas, 0) >= t, p.kostnad, 0)), SUM(IF(IFNULL(p.roas, 0) >= t, p.varde, 0))) * 100, 1) AS cos_efter_pct
FROM prod p CROSS JOIN UNNEST([1.0, 2.0, 3.0, 4.0]) AS t
WHERE p.market IN ('SE', 'DK')
GROUP BY 1, 2 ORDER BY 1, 2;

-- 3. De 20 produkter som kostat mest per marknad
SELECT * FROM (
  SELECT market, titel, ROUND(kostnad) AS kostnad, klick, ROUND(varde) AS varde, ROUND(roas, 2) AS roas, delvis_okopplad,
         ROW_NUMBER() OVER (PARTITION BY market ORDER BY kostnad DESC) AS rang
  FROM prod WHERE market IN ('SE', 'DK')
) WHERE rang <= 20 ORDER BY market, rang;

-- 4. Avstämning: täcker produktnivån kampanjnivåns kostnad och värde?
SELECT k.market, ROUND(k.google_kostnad) AS kampanj_kostnad, ROUND(SUM(p.kostnad)) AS produkt_kostnad,
       ROUND(SAFE_DIVIDE(SUM(p.kostnad), k.google_kostnad) * 100) AS tackning_kostnad_pct,
       ROUND(k.google_varde) AS kampanj_varde, ROUND(SUM(p.varde)) AS produkt_varde,
       ROUND(SAFE_DIVIDE(SUM(p.varde), k.google_varde) * 100) AS tackning_varde_pct,
       ROUND(SUM(IF(p.delvis_okopplad, p.kostnad, 0))) AS okopplad_kostnad
FROM kamp k LEFT JOIN prod p USING (market)
WHERE k.market IN ('SE', 'DK') GROUP BY k.market, k.google_kostnad, k.google_varde ORDER BY 1;
