-- Fortsättning på frakt_samband.sql: prisband i stället för enskilda produkter, och vilka produkter som får en order över fraktgränsen.
-- Utgår enbart från Shopify-ordrarna, senaste 90 dagarna. Ordervärde = subtotal_price (efter rabatt, före frakt) i kundens valuta.
-- Körning:
--   sed 's/PROJ/gorilla-sports-data/g' sql/analys/frakt_tippande.sql | bq query --use_legacy_sql=false --max_rows=200
-- Fraktgräns: SE 800 SEK, DK 700 DKK (bekräftade i frakt_samband.sql).
-- Begrepp:
--   enhetspris        = radvärde / antal (efter rabatt)
--   prisband          = enhetspris i förhållande till fraktgränsen (1,00 = precis gränsen)
--   ensam klarar      = orderns största rad är ensam minst lika stor som gränsen
--   kombination       = ingen enskild rad når gränsen, men ordern gör det tillsammans
--   påfyllningsrad    = en rad som inte är orderns största, i en kombinationsorder

DECLARE d1 DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 1 DAY);
DECLARE d0 DATE DEFAULT DATE_SUB(d1, INTERVAL 89 DAY);
DECLARE se_grans FLOAT64 DEFAULT 800.0;
DECLARE dk_grans FLOAT64 DEFAULT 700.0;
DECLARE min_ordrar INT64 DEFAULT 5;

CREATE TEMP TABLE ord AS
SELECT o.id,
       CASE o.presentment_currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' END AS market,
       o.subtotal_price * SAFE_DIVIDE(o.total_price_presentment, o.total_price) AS ordervarde,
       o.total_shipping > 0 AS betalar_frakt,
       IF(o.presentment_currency = 'SEK', se_grans, dk_grans) AS grans
FROM `PROJ.shopify.orders` o
WHERE o.cancelled_at IS NULL AND o.presentment_currency IN ('SEK', 'DKK')
  AND DATE(o.created_at, 'Europe/Stockholm') BETWEEN d0 AND d1 AND o.subtotal_price > 0;

CREATE TEMP TABLE lin AS
SELECT li.order_id, li.product_id, ANY_VALUE(li.title) AS titel, SUM(li.quantity) AS antal,
       SUM(li.discounted_total * SAFE_DIVIDE(o.total_price_presentment, o.total_price)) AS radvarde
FROM `PROJ.shopify.order_line_items` li
JOIN `PROJ.shopify.orders` o ON o.id = li.order_id
WHERE li.order_id IN (SELECT id FROM ord)
GROUP BY 1, 2;

CREATE TEMP TABLE lin2 AS
SELECT l.*, o.market, o.ordervarde, o.betalar_frakt, o.grans,
       SAFE_DIVIDE(l.radvarde, l.antal) AS enhetspris,
       ROW_NUMBER() OVER (PARTITION BY l.order_id ORDER BY l.radvarde DESC) AS rang,
       COUNT(*) OVER (PARTITION BY l.order_id) AS rader,
       MAX(l.radvarde) OVER (PARTITION BY l.order_id) AS storsta_rad
FROM lin l JOIN ord o ON o.id = l.order_id;

-- 1. Prisband: ordrar som innehåller en rad i bandet. Andel som betalar frakt, andel där raden är ensam i ordern, snittvärde.
SELECT market,
       CASE WHEN enhetspris / grans < 0.25 THEN '1: under 0,25 x gräns'
            WHEN enhetspris / grans < 0.5 THEN '2: 0,25-0,5'
            WHEN enhetspris / grans < 0.75 THEN '3: 0,5-0,75'
            WHEN enhetspris / grans < 1 THEN '4: 0,75-1,0'
            WHEN enhetspris / grans < 1.5 THEN '5: 1,0-1,5'
            WHEN enhetspris / grans < 2.5 THEN '6: 1,5-2,5'
            ELSE '7: över 2,5' END AS prisband,
       COUNT(DISTINCT order_id) AS ordrar, COUNT(DISTINCT product_id) AS produkter,
       ROUND(COUNTIF(betalar_frakt) / COUNT(*) * 100) AS andel_betalar_pct,
       ROUND(COUNTIF(rader = 1) / COUNT(*) * 100) AS ensam_rad_pct,
       ROUND(AVG(ordervarde)) AS snitt_ordervarde, ROUND(AVG(enhetspris)) AS snitt_enhetspris
FROM lin2 GROUP BY 1, 2 ORDER BY 1, 2;

-- 2. Hur tar sig ordrarna över gränsen? Bara ordrar över gränsen. Strax över = under 1,25 x gränsen.
SELECT market,
       CASE WHEN storsta_rad >= grans THEN 'ensam rad klarar gränsen' ELSE 'kombination av flera rader' END AS hur,
       COUNT(DISTINCT order_id) AS ordrar,
       ROUND(AVG(ordervarde)) AS snitt_ordervarde,
       COUNT(DISTINCT IF(ordervarde < 1.25 * grans, order_id, NULL)) AS varav_strax_over
FROM lin2 WHERE ordervarde >= grans GROUP BY 1, 2 ORDER BY 1, 2;

-- 3. Påfyllningsprodukter: rader som inte är orderns största, i kombinationsordrar över gränsen (ingen enskild rad når gränsen).
--    Ju fler ordrar och ju lägre enhetspris, desto mer typisk "tilläggsprodukt för att nå fri frakt".
SELECT market, product_id, ANY_VALUE(titel) AS produkt, COUNT(DISTINCT order_id) AS ordrar_som_paafyllning,
       ROUND(AVG(enhetspris)) AS snitt_enhetspris,
       ROUND(AVG(ordervarde)) AS snitt_ordervarde,
       ROUND(COUNTIF(ordervarde - radvarde < grans) / COUNT(*) * 100) AS utan_raden_under_gransen_pct
FROM lin2
WHERE ordervarde >= grans AND storsta_rad < grans AND rang > 1
GROUP BY 1, 2 HAVING COUNT(DISTINCT order_id) >= min_ordrar
ORDER BY 1, ordrar_som_paafyllning DESC LIMIT 40;

-- 4. Samma sak åt andra hållet: produkter som ofta är orderns största rad i ordrar som BETALAR frakt och som saknar en andra rad.
--    Dessa är kandidater för "köp X mer för fri frakt".
SELECT market, product_id, ANY_VALUE(titel) AS produkt, COUNT(DISTINCT order_id) AS ordrar,
       ROUND(AVG(enhetspris)) AS snitt_enhetspris, ROUND(AVG(grans - ordervarde)) AS saknas_till_gransen,
       ROUND(COUNTIF(ordervarde + enhetspris >= grans) / COUNT(*) * 100) AS en_extra_enhet_racker_pct
FROM lin2 WHERE betalar_frakt AND ordervarde < grans AND rang = 1
GROUP BY 1, 2 HAVING COUNT(DISTINCT order_id) >= min_ordrar
ORDER BY 1, ordrar DESC LIMIT 40;
