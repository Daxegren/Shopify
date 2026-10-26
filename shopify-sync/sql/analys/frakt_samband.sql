-- Samband mellan ordrar som betalar frakt och ordrar som inte gör det, och vilka produkter ordrarna innehåller.
-- Utgår enbart från Shopify-ordrarna (inga ark, inga vikter). Senaste 90 dagarna, per marknad.
-- Körning:
--   sed 's/PROJ/gorilla-sports-data/g' sql/analys/frakt_samband.sql | bq query --use_legacy_sql=false --max_rows=200
-- Ordervärde = subtotal_price (efter rabatt, före frakt) i kundens valuta (SEK för SE, DKK för DK).
-- Fraktgräns: SE 800, DK 700 (del 1 och 2 visar om datan stämmer). Ordrar med värde 0 (utkast/ersättning) och annullerade ingår inte.

DECLARE d1 DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 1 DAY);
DECLARE d0 DATE DEFAULT DATE_SUB(d1, INTERVAL 89 DAY);
DECLARE se_grans FLOAT64 DEFAULT 800.0;
DECLARE dk_grans FLOAT64 DEFAULT 700.0;
DECLARE min_ordrar INT64 DEFAULT 25;

CREATE TEMP TABLE ord AS
SELECT o.id,
       CASE o.presentment_currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' END AS market,
       o.subtotal_price * SAFE_DIVIDE(o.total_price_presentment, o.total_price) AS ordervarde,
       o.total_shipping * SAFE_DIVIDE(o.total_price_presentment, o.total_price) AS frakt,
       o.total_shipping > 0 AS betalar_frakt
FROM `PROJ.shopify.orders` o
WHERE o.cancelled_at IS NULL AND o.presentment_currency IN ('SEK', 'DKK')
  AND DATE(o.created_at, 'Europe/Stockholm') BETWEEN d0 AND d1
  AND o.subtotal_price > 0;

CREATE TEMP TABLE lin AS
SELECT li.order_id, li.product_id, ANY_VALUE(li.title) AS titel, SUM(li.quantity) AS antal,
       SUM(li.discounted_total * SAFE_DIVIDE(o.total_price_presentment, o.total_price)) AS radvarde
FROM `PROJ.shopify.order_line_items` li
JOIN `PROJ.shopify.orders` o ON o.id = li.order_id
WHERE li.order_id IN (SELECT id FROM ord)
GROUP BY 1, 2;

CREATE TEMP TABLE korg AS
SELECT order_id, COUNT(*) AS produkter, SUM(antal) AS enheter, MAX(radvarde) AS storsta_rad FROM lin GROUP BY 1;

CREATE TEMP TABLE o2 AS
SELECT ord.*, korg.produkter, korg.enheter, korg.storsta_rad,
       ordervarde >= IF(market = 'SE', se_grans, dk_grans) AS over_grans
FROM ord JOIN korg ON korg.order_id = ord.id;

-- 1. Stämmer regeln? Över/under gräns mot om frakt betalades. Avvikelser (över gräns men betalar, under men betalar inte) förklaras av rabattkoder, avhämtning eller manuella ordrar.
SELECT market, over_grans, betalar_frakt, COUNT(*) AS ordrar, ROUND(AVG(ordervarde)) AS snitt_ordervarde,
       ROUND(AVG(IF(betalar_frakt, frakt, NULL))) AS snitt_fraktavgift
FROM o2 GROUP BY 1, 2, 3 ORDER BY 1, 2, 3;

-- 2. Ordervärde runt gränsen, steg om 50: finns det en klump precis över gränsen (kunder som fyller på för fri frakt)?
SELECT market, CAST(FLOOR(ordervarde / 50) * 50 AS INT64) AS ordervarde_fran, COUNT(*) AS ordrar,
       ROUND(COUNTIF(betalar_frakt) / COUNT(*) * 100) AS andel_betalar_frakt_pct
FROM o2
WHERE (market = 'SE' AND ordervarde BETWEEN 400 AND 1400) OR (market = 'DK' AND ordervarde BETWEEN 300 AND 1200)
GROUP BY 1, 2 ORDER BY 1, 2;

-- 3. Korgens utseende: betalar frakt mot inte
SELECT market, betalar_frakt, COUNT(*) AS ordrar, ROUND(AVG(ordervarde)) AS snitt_ordervarde, ROUND(APPROX_QUANTILES(ordervarde, 100)[OFFSET(50)]) AS median_ordervarde,
       ROUND(AVG(produkter), 2) AS snitt_produkter, ROUND(AVG(enheter), 2) AS snitt_enheter,
       ROUND(COUNTIF(produkter = 1) / COUNT(*) * 100) AS en_produkt_pct,
       ROUND(COUNTIF(produkter = 1 AND enheter = 1) / COUNT(*) * 100) AS en_enhet_pct,
       ROUND(AVG(storsta_rad / ordervarde) * 100) AS storsta_rad_andel_pct
FROM o2 GROUP BY 1, 2 ORDER BY 1, 2;

-- 4. Per produkt: hur ofta ingår produkten i ordrar som betalar frakt? (minst min_ordrar ordrar)
--    andel_betalar_pct jämförs med marknadens snitt; index 100 = som alla ordrar.
--    ensam_pct = andel av produktens ordrar där den är den enda produkten.
WITH basis AS (
  SELECT o2.market, o2.betalar_frakt, o2.ordervarde, o2.produkter, l.product_id, l.titel, l.antal
  FROM o2 JOIN lin l ON l.order_id = o2.id
), snitt AS (
  SELECT market, COUNTIF(betalar_frakt) / COUNT(*) AS snitt_betalar FROM o2 GROUP BY 1
)
SELECT b.market, b.product_id, ANY_VALUE(b.titel) AS produkt, COUNT(*) AS ordrar,
       ROUND(COUNTIF(b.betalar_frakt) / COUNT(*) * 100) AS andel_betalar_pct,
       ROUND(COUNTIF(b.betalar_frakt) / COUNT(*) / ANY_VALUE(s.snitt_betalar) * 100) AS index_mot_snitt,
       ROUND(COUNTIF(b.produkter = 1) / COUNT(*) * 100) AS ensam_pct,
       ROUND(AVG(b.ordervarde)) AS snitt_ordervarde, ROUND(AVG(b.antal), 2) AS snitt_antal
FROM basis b JOIN snitt s USING (market)
GROUP BY 1, 2 HAVING COUNT(*) >= min_ordrar
ORDER BY 1, andel_betalar_pct DESC LIMIT 60;

-- 5. Påfyllningsprodukter: produkter som är överrepresenterade i ordrar precis över gränsen (gräns till +300) jämfört med alla ordrar.
--    index över 100 = kunderna lägger gärna till produkten för att nå fri frakt.
WITH basis AS (
  SELECT o2.market, o2.id, o2.ordervarde, o2.over_grans, l.product_id, l.titel,
         o2.over_grans AND o2.ordervarde < IF(o2.market = 'SE', se_grans, dk_grans) + IF(o2.market = 'SE', 300, 260) AS strax_over
  FROM o2 JOIN lin l ON l.order_id = o2.id
), tot AS (
  SELECT market, COUNT(DISTINCT id) AS alla, COUNT(DISTINCT IF(strax_over, id, NULL)) AS strax FROM basis GROUP BY 1
)
SELECT b.market, b.product_id, ANY_VALUE(b.titel) AS produkt,
       COUNT(DISTINCT b.id) AS ordrar_totalt, COUNT(DISTINCT IF(b.strax_over, b.id, NULL)) AS ordrar_strax_over,
       ROUND(SAFE_DIVIDE(COUNT(DISTINCT IF(b.strax_over, b.id, NULL)) / ANY_VALUE(t.strax), COUNT(DISTINCT b.id) / ANY_VALUE(t.alla)) * 100) AS index_strax_over
FROM basis b JOIN tot t USING (market)
GROUP BY 1, 2 HAVING COUNT(DISTINCT b.id) >= min_ordrar AND COUNT(DISTINCT IF(b.strax_over, b.id, NULL)) >= 5
ORDER BY 1, index_strax_over DESC LIMIT 40;

-- 6. Vad saknas för att nå gränsen? Ordrar som betalar frakt: hur långt under gränsen och hur ofta räcker en extra enhet av korgens dyraste produkt.
SELECT market,
       COUNT(*) AS ordrar_som_betalar,
       ROUND(AVG(IF(market = 'SE', se_grans, dk_grans) - ordervarde)) AS snitt_saknas,
       ROUND(COUNTIF(IF(market = 'SE', se_grans, dk_grans) - ordervarde <= 100) / COUNT(*) * 100) AS inom_100_pct,
       ROUND(COUNTIF(IF(market = 'SE', se_grans, dk_grans) - ordervarde <= 200) / COUNT(*) * 100) AS inom_200_pct,
       ROUND(COUNTIF(ordervarde + storsta_rad / enheter >= IF(market = 'SE', se_grans, dk_grans)) / COUNT(*) * 100) AS en_extra_enhet_racker_pct,
       ROUND(SUM(frakt)) AS fraktintakt_totalt
FROM o2 WHERE NOT over_grans AND betalar_frakt GROUP BY 1 ORDER BY 1;
