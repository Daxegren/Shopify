-- Stickprov för att kontrollera att inköpspriserna (unit_cost) stämmer innan vi litar på bruttomarginalen i marginal_30d.sql.
-- Visar de 25 produkter som sålt mest de senaste 30 dagarna med försäljningspris, inköpspris i Shopify och den marginal det ger.
--
--   sed 's/PROJ/gorilla-sports-data/g' sql/analys/marginal_stickprov.sql | bq query --use_legacy_sql=false --max_rows=40
--
-- Jämför ett par rader mot era egna inköpsfakturor eller leverantörslistor. Belopp i butikens valuta (SEK).
-- Kolumn "marginal_pct" räknas på radbeloppet som det ligger i Shopify (om priserna är inklusive moms är marginalen före moms lägre).

DECLARE d1 DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 1 DAY);
DECLARE d0 DATE DEFAULT DATE_SUB(d1, INTERVAL 29 DAY);

SELECT ANY_VALUE(li.title) AS produkt, ANY_VALUE(li.vendor) AS leverantor, SUM(li.quantity) AS antal,
       ROUND(SUM(li.discounted_total)) AS omsattning,
       ROUND(SAFE_DIVIDE(SUM(li.discounted_total), SUM(li.quantity))) AS snittpris_per_st,
       ROUND(AVG(v.unit_cost), 2) AS inkopspris_per_st,
       ROUND(SAFE_DIVIDE(SUM(li.discounted_total) - SUM(li.quantity * v.unit_cost), SUM(li.discounted_total)) * 100, 1) AS marginal_pct,
       ANY_VALUE(v.sku) AS sku
FROM `PROJ.shopify.orders` o
JOIN `PROJ.shopify.order_line_items` li ON li.order_id = o.id
LEFT JOIN `PROJ.shopify.product_variants` v ON REGEXP_EXTRACT(v.id, r'(\d+)$') = REGEXP_EXTRACT(li.variant_id, r'(\d+)$')
WHERE o.cancelled_at IS NULL AND DATE(o.created_at, 'Europe/Stockholm') BETWEEN d0 AND d1
GROUP BY li.product_id
ORDER BY omsattning DESC LIMIT 25;
