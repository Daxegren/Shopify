-- Marginal per variant (SKU) och marknad för Gorilla, ur arkens inköpspris (net_profit_sku) och faktiska säljpriser i orderraderna.
-- Arket gäller, inte Shopifys unit_cost (docs: beslut-2026-10-26.md, avsnitt om att unit_cost avviker från arket). Skriptet visar båda så att avvikelsen syns per variant.
--
-- Förberedelse (en gång): tabellen site_audit.net_profit_sku ska vara laddad ur data/net_profit_sku.csv, se huvudet i net_profit_ordrar.sql (steg 1). Vikter behövs inte här.
-- Kör: sed 's/PROJ/gorilla-sports-data/g' sql/analys/marginal_per_variant.sql | bq query --use_legacy_sql=false --max_rows=100
--
-- Definitioner (alla i EUR enligt arkens kurser SEK 11,4 och DKK 8,0; priserna i orderraderna antas inkludera 25 % moms, som i net_profit_ordrar.sql):
--   netto_intakt   = discounted_total / moms / kurs                         (försäljning exkl. moms, efter rabatt)
--   GM1            = (netto_intakt - antal * buying_eur) / netto_intakt      (bruttomarginal före frakt och avgifter)
--   GM2            = GM1 minus antal * shipping_eur och betal-/konverteringsavgift (procent av netto_intakt) i förhållande till netto_intakt.
--                    GM2 räknar fraktkostnaden men INTE fraktintäkten från kunden (kunden betalar frakt under gränsen). GM2 är alltså en nedre gräns för varor som skickas gratis.
--   GM3            = GM2 plus fraktintäkten kunden betalat (exkl. moms), fördelad på orderns rader efter varuvärde. GM3 är det närmaste verkligheten, men fördelningen är en approximation:
--                    en order med en billig och en dyr vara lägger fraktintäkten på båda efter värde, inte efter vilken vara som orsakade fraktkostnaden.
--   GM1_shopify    = samma som GM1 men med Shopifys unit_cost (SEK) delat med SEK-kursen. Skillnaden mot GM1 visar hur mycket unit_cost avviker från arket.
-- Täckning: bara rader där SKU finns i arket och i orderraden räknas i marginalen. Se del 0 för hur stor andel av omsättningen det är.
-- Period: senaste 90 dagarna, men orderdata finns bara sedan 2026-08-10, så det är i praktiken cirka 80 dagar.
-- Läs så här: GM2 under 20 % eller negativ betyder att varan med full frakt inte bär sig; kolla om kunden betalar frakten (andel ordrar under fraktgränsen) innan något beslut.
-- Detta skript ändrar inget.

DECLARE d1 DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 1 DAY);
DECLARE d0 DATE DEFAULT DATE_SUB(d1, INTERVAL 89 DAY);
DECLARE fx_se FLOAT64 DEFAULT 11.4;
DECLARE fx_dk FLOAT64 DEFAULT 8.0;
DECLARE moms FLOAT64 DEFAULT 1.25;

-- Först en rad per orderrad, med fraktintäkten fördelad på orderns rader efter radens andel av varuvärdet (en approximation).
-- Betald frakt (orders.total_shipping, i butikens valuta) räknas om till kundens valuta med total_price_presentment / total_price och antas inkludera 25 % moms.
CREATE TEMP TABLE lin AS
SELECT CASE o.presentment_currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE o.presentment_currency END AS market,
       TRIM(li.sku) AS sku, li.title AS radtitel, li.quantity AS antal,
       IF(o.presentment_currency = 'DKK', fx_dk, fx_se) AS fx,
       li.discounted_total AS belopp,
       SAFE_DIVIDE(li.discounted_total, SUM(li.discounted_total) OVER (PARTITION BY o.id)) * o.total_shipping * SAFE_DIVIDE(o.total_price_presentment, o.total_price) AS frakt_betald_rad,
       v.unit_cost
FROM `PROJ.shopify.orders` o
JOIN `PROJ.shopify.order_line_items` li ON li.order_id = o.id
LEFT JOIN `PROJ.shopify.product_variants` v ON REGEXP_EXTRACT(v.id, r'(\d+)$') = REGEXP_EXTRACT(li.variant_id, r'(\d+)$')
WHERE o.cancelled_at IS NULL AND o.presentment_currency IN ('SEK', 'DKK') AND DATE(o.created_at, 'Europe/Stockholm') BETWEEN d0 AND d1;

CREATE TEMP TABLE rad AS
SELECT market, sku, ANY_VALUE(radtitel) AS radtitel,
       SUM(antal) AS antal,
       SUM(belopp / moms / fx) AS netto_intakt,
       SUM(IFNULL(frakt_betald_rad, 0) / moms / fx) AS frakt_intakt,
       SUM(IF(unit_cost IS NOT NULL AND unit_cost > 0, antal * unit_cost / fx_se, NULL)) AS cogs_shopify,
       SUM(IF(unit_cost IS NOT NULL AND unit_cost > 0, belopp / moms / fx, 0)) AS intakt_med_shopifykostnad
FROM lin GROUP BY 1, 2;

CREATE TEMP TABLE m AS
SELECT r.market, r.sku, r.radtitel, r.antal, r.netto_intakt,
       s.buying_eur, s.shipping_eur, IFNULL(s.payment_fee_pct, 0) + IFNULL(s.conversion_fee_pct, 0) AS avgift_pct,
       s.sku IS NOT NULL AS i_arket,
       r.frakt_intakt,
       r.antal * s.buying_eur AS cogs,
       r.antal * s.shipping_eur AS frakt,
       r.netto_intakt * (IFNULL(s.payment_fee_pct, 0) + IFNULL(s.conversion_fee_pct, 0)) AS avgift,
       r.cogs_shopify, r.intakt_med_shopifykostnad
FROM rad r LEFT JOIN `PROJ.site_audit.net_profit_sku` s ON s.market = r.market AND s.sku = r.sku;

-- 0. Täckning per marknad: andel av nettointäkten som kunde kopplas till arkets inköpspris (under cirka 80 % är resultatet osäkert).
SELECT market, ROUND(SUM(netto_intakt)) AS netto_intakt_eur,
       ROUND(SUM(IF(i_arket, netto_intakt, 0))) AS kopplat_eur,
       ROUND(SAFE_DIVIDE(SUM(IF(i_arket, netto_intakt, 0)), SUM(netto_intakt)) * 100, 1) AS tackning_pct,
       COUNTIF(NOT i_arket) AS sku_utan_ark, COUNTIF(sku IS NULL OR sku = '') AS rader_utan_sku
FROM m GROUP BY market ORDER BY market;

-- 1. Sammanlagd marginal per marknad (bara kopplade rader).
SELECT market, ROUND(SUM(netto_intakt)) AS netto_intakt_eur,
       ROUND(SAFE_DIVIDE(SUM(netto_intakt) - SUM(cogs), SUM(netto_intakt)) * 100, 1) AS gm1_pct,
       ROUND(SAFE_DIVIDE(SUM(netto_intakt) - SUM(cogs) - SUM(frakt) - SUM(avgift), SUM(netto_intakt)) * 100, 1) AS gm2_pct,
       ROUND(SAFE_DIVIDE(SUM(netto_intakt) - SUM(cogs) - SUM(frakt) - SUM(avgift) + SUM(frakt_intakt), SUM(netto_intakt)) * 100, 1) AS gm3_med_fraktintakt_pct,
       ROUND(SAFE_DIVIDE(SUM(frakt_intakt), SUM(netto_intakt)) * 100, 1) AS fraktintakt_andel_av_varor_pct,
       ROUND(SAFE_DIVIDE(SUM(intakt_med_shopifykostnad) - SUM(cogs_shopify), SUM(intakt_med_shopifykostnad)) * 100, 1) AS gm1_med_shopify_unit_cost_pct
FROM m WHERE i_arket GROUP BY market ORDER BY market;

-- 2. De 40 varianter med störst nettointäkt: marginal enligt arket och enligt Shopifys unit_cost. Sorterat efter intäkt.
SELECT market, sku, radtitel, antal, ROUND(netto_intakt) AS netto_intakt_eur,
       ROUND(SAFE_DIVIDE(netto_intakt - cogs, netto_intakt) * 100, 1) AS gm1_pct,
       ROUND(SAFE_DIVIDE(netto_intakt - cogs - frakt - avgift, netto_intakt) * 100, 1) AS gm2_pct,
       ROUND(SAFE_DIVIDE(netto_intakt - cogs - frakt - avgift + frakt_intakt, netto_intakt) * 100, 1) AS gm3_pct,
       ROUND(SAFE_DIVIDE(intakt_med_shopifykostnad - cogs_shopify, intakt_med_shopifykostnad) * 100, 1) AS gm1_shopify_pct,
       ROUND(buying_eur, 1) AS inkopspris_eur_ark, ROUND(shipping_eur, 1) AS frakt_eur_ark
FROM m WHERE i_arket ORDER BY netto_intakt DESC LIMIT 40;

-- 3. Varianter där GM3 (med fraktintäkt) är negativ eller under 20 % och som sålt minst 3 enheter: kandidater att se över (pris, fraktgräns, avgift). Sorterat efter förlorad marginal i EUR.
SELECT market, sku, radtitel, antal, ROUND(netto_intakt) AS netto_intakt_eur,
       ROUND(SAFE_DIVIDE(netto_intakt - cogs - frakt - avgift, netto_intakt) * 100, 1) AS gm2_pct,
       ROUND(SAFE_DIVIDE(netto_intakt - cogs - frakt - avgift + frakt_intakt, netto_intakt) * 100, 1) AS gm3_pct,
       ROUND(netto_intakt - cogs - frakt - avgift + frakt_intakt) AS bidrag_med_fraktintakt_eur
FROM m WHERE i_arket AND antal >= 3 AND SAFE_DIVIDE(netto_intakt - cogs - frakt - avgift + frakt_intakt, netto_intakt) < 0.2
ORDER BY bidrag_med_fraktintakt_eur ASC LIMIT 30;

-- 4. Skillnaden mellan arket och Shopifys unit_cost: de 20 varianter med störst absolut avvikelse i GM1 (procentenheter), med minst 3 sålda enheter.
SELECT market, sku, radtitel, antal, ROUND(netto_intakt) AS netto_intakt_eur,
       ROUND(SAFE_DIVIDE(netto_intakt - cogs, netto_intakt) * 100, 1) AS gm1_ark_pct,
       ROUND(SAFE_DIVIDE(intakt_med_shopifykostnad - cogs_shopify, intakt_med_shopifykostnad) * 100, 1) AS gm1_shopify_pct
FROM m WHERE i_arket AND antal >= 3 AND cogs_shopify IS NOT NULL
ORDER BY ABS(SAFE_DIVIDE(netto_intakt - cogs, netto_intakt) - SAFE_DIVIDE(intakt_med_shopifykostnad - cogs_shopify, intakt_med_shopifykostnad)) DESC LIMIT 20;
