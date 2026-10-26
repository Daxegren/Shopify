-- Bruttomarginal för Gorilla Sports, senaste 30 dagarna till och med i går, per marknad, ur orderrader och inköpspris (unit_cost) i Shopify.
-- Svarar på vilken COS och ROAS som är break-even: annonskostnaden får inte överstiga bruttovinsten.
--
--   sed 's/PROJ/gorilla-sports-data/g' sql/analys/marginal_30d.sql | bq query --use_legacy_sql=false --max_rows=40
--
-- VIKTIGT att kontrollera:
--  * täckning_pct = andel av radernas omsättning där unit_cost finns. Under cirka 80 % är marginalen osäker.
--  * Moms: antar att radbeloppen (discounted_total) är inklusive 25 % moms och att unit_cost är exklusive moms. Om butikspriserna är exklusive moms
--    är marginalen i kolumnen "exkl_moms" fel; då gäller kolumnen "som_den_ar". Kontrollera mot ett känt pris.
--  * Intäkten är radernas värde i butikens valuta (SEK) för både SE och DK; marginalprocent påverkas inte av valutan.
--  * Frakt och betalavgifter ingår inte.

DECLARE d1 DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 1 DAY);
DECLARE d0 DATE DEFAULT DATE_SUB(d1, INTERVAL 29 DAY);

WITH rader AS (
  SELECT CASE o.presentment_currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE o.presentment_currency END AS market,
         li.discounted_total AS oms, li.quantity AS antal, v.unit_cost AS kostnad_per_st
  FROM `PROJ.shopify.orders` o
  JOIN `PROJ.shopify.order_line_items` li ON li.order_id = o.id
  LEFT JOIN `PROJ.shopify.product_variants` v ON v.id = li.variant_id OR REGEXP_EXTRACT(v.id, r'(\d+)$') = REGEXP_EXTRACT(li.variant_id, r'(\d+)$')
  WHERE o.cancelled_at IS NULL AND DATE(o.created_at, 'Europe/Stockholm') BETWEEN d0 AND d1
)
SELECT market,
       COUNT(*) AS orderrader,
       ROUND(SUM(oms)) AS omsattning,
       ROUND(SAFE_DIVIDE(SUM(IF(kostnad_per_st IS NOT NULL, oms, 0)), SUM(oms)) * 100) AS tackning_pct,
       ROUND(SAFE_DIVIDE(SUM(IF(kostnad_per_st IS NOT NULL, oms - antal * kostnad_per_st, 0)), SUM(IF(kostnad_per_st IS NOT NULL, oms, 0))) * 100, 1) AS bruttomarginal_som_den_ar_pct,
       ROUND(SAFE_DIVIDE(SUM(IF(kostnad_per_st IS NOT NULL, oms / 1.25 - antal * kostnad_per_st, 0)), SUM(IF(kostnad_per_st IS NOT NULL, oms, 0))) * 100, 1) AS break_even_cos_exkl_moms_pct,
       ROUND(SAFE_DIVIDE(SUM(IF(kostnad_per_st IS NOT NULL, oms, 0)), SUM(IF(kostnad_per_st IS NOT NULL, oms / 1.25 - antal * kostnad_per_st, 0))), 2) AS break_even_roas_exkl_moms
FROM rader WHERE market IN ('SE', 'DK') GROUP BY 1 ORDER BY 1;
