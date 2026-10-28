-- Vilka varianter är slut på de 30 produkter som sålt mest? En produkt kan vara "i lager" totalt men sakna just de storlekar/vikter som folk köper.
-- Bakgrund: storsaljare_tapp.sql 2026-10-28 visade t.ex. Kettlebell GS Vinyl 2-32kg med 13 av 17 varianter i lager och minskande försäljning, och Kombinerad Chinsstång och Dipsställning Vägg helt slut.
-- Rang: omsättning per produkt (line items) de senaste 90 dagarna, men bara dagar med orderdata (orderdata finns sedan 2026-08-10). Valutor blandas inte: marknad räknas ur orderns presentment_currency.
-- Kolumner verifierade mot src/shopify_sync/schema.py: product_variants(id, product_id, sku, title, unit_cost, inventory_quantity), orders(id, created_at, presentment_currency, cancelled_at), order_line_items(order_id, product_id, variant_id, quantity, discounted_total, title).
-- Kör: sed 's/PROJ/gorilla-sports-data/g' sql/analys/varianter_slut_storsaljare.sql | bq query --use_legacy_sql=false --max_rows=200
-- Läs så här: en variant med inventory_quantity <= 0 och sålda enheter de senaste 90 dagarna är en slutsåld efterfrågad variant. Kolla i Shopify om beställning pågår; detta skript ändrar inget.

DECLARE idag DATE DEFAULT CURRENT_DATE('Europe/Stockholm');
DECLARE r_start DATE DEFAULT DATE_SUB(idag, INTERVAL 90 DAY);

CREATE TEMP TABLE rader AS
SELECT REGEXP_EXTRACT(li.product_id, r'(\d+)$') AS pid, REGEXP_EXTRACT(li.variant_id, r'(\d+)$') AS vkey,
       CASE o.presentment_currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE o.presentment_currency END AS marknad,
       DATE(o.created_at, 'Europe/Stockholm') AS d, li.quantity AS enh, li.discounted_total AS oms
FROM `PROJ.shopify.orders` o JOIN `PROJ.shopify.order_line_items` li ON li.order_id = o.id
WHERE o.cancelled_at IS NULL AND DATE(o.created_at, 'Europe/Stockholm') BETWEEN r_start AND DATE_SUB(idag, INTERVAL 1 DAY);

CREATE TEMP TABLE topp AS
SELECT pid FROM (SELECT pid, SUM(oms) AS o FROM rader WHERE pid IS NOT NULL GROUP BY pid ORDER BY o DESC LIMIT 30);

-- 1. Varje variant på de 30 produkterna: lager, sålda enheter, sista säljdag. Slutsålda efterfrågade varianter överst.
SELECT ANY_VALUE(p.title) AS produkt, v.title AS variant, v.sku, v.inventory_quantity AS lager,
       IFNULL(SUM(r.enh), 0) AS enh_90d, MAX(r.d) AS sista_forsaljning,
       DATE_DIFF(DATE_SUB(idag, INTERVAL 1 DAY), MAX(r.d), DAY) AS dagar_sedan
FROM `PROJ.shopify.product_variants` v
JOIN topp t ON t.pid = REGEXP_EXTRACT(v.product_id, r'(\d+)$')
LEFT JOIN `PROJ.shopify.products` p ON p.id = v.product_id
LEFT JOIN rader r ON r.vkey = REGEXP_EXTRACT(v.id, r'(\d+)$')
GROUP BY v.id, v.title, v.sku, v.inventory_quantity
ORDER BY IF(IFNULL(v.inventory_quantity, 0) <= 0, 0, 1), enh_90d DESC;

-- 2. Sammanfattning: antal slutsålda varianter med försäljning per produkt.
SELECT ANY_VALUE(p.title) AS produkt, COUNT(*) AS varianter, COUNTIF(IFNULL(v.inventory_quantity, 0) <= 0) AS slut,
       COUNTIF(IFNULL(v.inventory_quantity, 0) <= 0 AND s.enh > 0) AS slut_men_salda_90d
FROM `PROJ.shopify.product_variants` v
JOIN topp t ON t.pid = REGEXP_EXTRACT(v.product_id, r'(\d+)$')
LEFT JOIN `PROJ.shopify.products` p ON p.id = v.product_id
LEFT JOIN (SELECT vkey, SUM(enh) AS enh FROM rader GROUP BY vkey) s ON s.vkey = REGEXP_EXTRACT(v.id, r'(\d+)$')
GROUP BY v.product_id ORDER BY slut_men_salda_90d DESC, slut DESC;
