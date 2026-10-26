-- Produkter vars enhetspris ligger strax under fraktgränsen (SE 800 SEK, DK 700 DKK), senaste 90 dagarna.
-- Kunden betalar fraktavgiften (SE 179 SEK, DK 89 DKK) om produkten köps ensam. Enhetspriset är efter rabatt (discounted_total / quantity).
-- Körning:
--   sed 's/PROJ/gorilla-sports-data/g' sql/analys/priser_strax_under_gransen.sql | bq query --use_legacy_sql=false --max_rows=100
-- Läsning: lista_pris_kontroll = ja betyder att medianpriset ligger inom 15 % under gränsen. Kontrollera listpriset i Shopify innan något ändras,
-- eftersom rabatter kan ha dragit ner priset under gränsen.
DECLARE d1 DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 1 DAY);
DECLARE d0 DATE DEFAULT DATE_SUB(d1, INTERVAL 89 DAY);

WITH rader AS (
  SELECT CASE o.presentment_currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' END AS market,
         IF(o.presentment_currency = 'SEK', 800.0, 700.0) AS grans,
         li.order_id, li.product_id, li.title, li.quantity,
         SAFE_DIVIDE(li.discounted_total * SAFE_DIVIDE(o.total_price_presentment, o.total_price), li.quantity) AS enhetspris,
         o.subtotal_price * SAFE_DIVIDE(o.total_price_presentment, o.total_price) AS ordervarde,
         o.total_shipping > 0 AS betalar_frakt
  FROM `PROJ.shopify.order_line_items` li
  JOIN `PROJ.shopify.orders` o ON o.id = li.order_id
  WHERE o.cancelled_at IS NULL AND o.presentment_currency IN ('SEK', 'DKK') AND o.subtotal_price > 0
    AND DATE(o.created_at, 'Europe/Stockholm') BETWEEN d0 AND d1
)
SELECT market, product_id, ANY_VALUE(title) AS produkt, COUNT(DISTINCT order_id) AS ordrar,
       ROUND(APPROX_QUANTILES(enhetspris, 100)[OFFSET(50)]) AS median_enhetspris,
       ROUND(MIN(enhetspris)) AS lagsta, ROUND(MAX(enhetspris)) AS hogsta,
       ROUND(COUNTIF(betalar_frakt) / COUNT(*) * 100) AS andel_betalar_frakt_pct,
       ROUND(AVG(grans - ordervarde)) AS saknas_i_snitt
FROM rader
GROUP BY market, product_id, grans
HAVING median_enhetspris BETWEEN 0.85 * ANY_VALUE(grans) AND ANY_VALUE(grans) - 0.01 AND COUNT(DISTINCT order_id) >= 3
ORDER BY market, ordrar DESC LIMIT 40;
