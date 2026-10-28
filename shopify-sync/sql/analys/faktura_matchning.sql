-- Matchning av leverantörsfakturor mot Gorillas ordrar (batchnivå, inte artikelnivå).
-- Underlag: "Fryskap - 20261027.xlsx" (öppna poster, belopp i EUR). De 48 fakturorna med numerisk "Ref. 2" (nr 19852–21594) ligger inte i repot (affärsdata) utan i en CSV som David laddar till BigQuery:
--   bq load --replace --source_format=CSV --skip_leading_rows=1 --schema='fakturadatum:DATE,ordernr_till:INTEGER,belopp_eur:FLOAT' gorilla-sports-data:site_audit.lev_fakturor lev_fakturor.csv
-- Hypotes som testas: Ref. 2 är numret på sista ordern som fakturan omfattar, så att faktura n täcker ordrar i intervallet (föregående Ref. 2, Ref. 2]. Stöd för hypotesen:
--   Ref. 2 ökar med 17–134 per dag och orderflödet i Shopify är cirka 25 per dag. Del 1 kontrollerar det direkt: antal ordrar i intervallet ska vara lika med skillnaden i Ref. 2.
-- Det som mäts: fakturabelopp mot (a) nettoförsäljning exkl. moms och (b) arkets inköpspris (net_profit_sku) för samma ordrar. Visar om arkets inköpspriser stämmer i total, inte per artikel.
-- Osäkert: vad fakturorna omfattar (bara varor, eller också moms/frakt), om listan är komplett (det är öppna poster) och om Ref. 2 är ordernummer. Kreditnotor och månadsfakturor (DPD, Shopify) är inte med.
-- Kör: sed 's/PROJ/gorilla-sports-data/g' sql/analys/faktura_matchning.sql | bq query --use_legacy_sql=false --max_rows=100
-- Kolumner verifierade mot src/shopify_sync/schema.py: orders(id, name, created_at, cancelled_at, presentment_currency), order_line_items(order_id, sku, quantity, discounted_total), site_audit.net_profit_sku(market, sku, buying_eur).
-- Detta skript ändrar inget.

DECLARE fx_se FLOAT64 DEFAULT 11.4;
DECLARE fx_dk FLOAT64 DEFAULT 8.0;
DECLARE moms FLOAT64 DEFAULT 1.25;

CREATE TEMP TABLE fak AS
SELECT fakturadatum, ordernr_till, belopp_eur, LAG(ordernr_till) OVER (ORDER BY ordernr_till) AS ordernr_fran_exkl
FROM `PROJ.site_audit.lev_fakturor`;

CREATE TEMP TABLE ord AS
SELECT o.id, SAFE_CAST(REGEXP_EXTRACT(o.name, r'(\d+)$') AS INT64) AS nr,
       CASE o.presentment_currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE o.presentment_currency END AS market,
       IF(o.presentment_currency = 'DKK', fx_dk, fx_se) AS fx, o.cancelled_at IS NOT NULL AS annullerad
FROM `PROJ.shopify.orders` o;

CREATE TEMP TABLE linje AS
SELECT ord.nr, ord.annullerad, ord.market,
       li.discounted_total / moms / ord.fx AS netto_eur,
       li.quantity * s.buying_eur AS cogs_eur,
       s.sku IS NOT NULL AS i_arket
FROM ord JOIN `PROJ.shopify.order_line_items` li ON li.order_id = ord.id
LEFT JOIN `PROJ.site_audit.net_profit_sku` s ON s.market = ord.market AND s.sku = TRIM(li.sku)
WHERE ord.nr BETWEEN 19800 AND 21700;

-- 1. Per faktura: täcker intervallet lika många ordrar som Ref. 2 ökar? (Stämmer hypotesen ska antal_ordrar ≈ ref2_okning.)
CREATE TEMP TABLE per_fak AS
SELECT f.fakturadatum, f.ordernr_till, f.ordernr_fran_exkl, f.ordernr_till - f.ordernr_fran_exkl AS ref2_okning, f.belopp_eur,
       COUNT(DISTINCT IF(NOT l.annullerad, l.nr, NULL)) AS antal_ordrar,
       SUM(IF(NOT l.annullerad, l.netto_eur, 0)) AS netto_eur,
       SUM(IF(NOT l.annullerad AND l.i_arket, l.cogs_eur, 0)) AS cogs_ark_eur,
       SAFE_DIVIDE(SUM(IF(NOT l.annullerad AND l.i_arket, l.netto_eur, 0)), SUM(IF(NOT l.annullerad, l.netto_eur, 0))) AS tackning
FROM fak f LEFT JOIN linje l ON l.nr > f.ordernr_fran_exkl AND l.nr <= f.ordernr_till
WHERE f.ordernr_fran_exkl IS NOT NULL
GROUP BY 1, 2, 3, 4, 5;

SELECT fakturadatum, ordernr_till, ref2_okning, antal_ordrar, ROUND(belopp_eur) AS faktura_eur, ROUND(netto_eur) AS netto_exkl_moms_eur, ROUND(cogs_ark_eur) AS cogs_enligt_ark_eur,
       ROUND(SAFE_DIVIDE(belopp_eur, netto_eur) * 100, 1) AS faktura_pct_av_netto, ROUND(SAFE_DIVIDE(cogs_ark_eur, netto_eur) * 100, 1) AS ark_cogs_pct_av_netto,
       ROUND(tackning * 100) AS tackning_pct
FROM per_fak ORDER BY ordernr_till;

-- 2. Totalt över alla fakturor (utom den första, som saknar startnummer). Läs så här: faktura_pct_av_netto jämfört med ark_cogs_pct_av_netto.
-- Är fakturan mycket högre än arket kan det bero på moms på fakturan (25 %), frakt eller andra tillägg i fakturan, eller att arkets inköpspriser är för låga.
SELECT COUNT(*) AS fakturor, SUM(antal_ordrar) AS ordrar, ROUND(SUM(ref2_okning)) AS ref2_okning_totalt,
       ROUND(SUM(belopp_eur)) AS faktura_eur, ROUND(SUM(netto_eur)) AS netto_exkl_moms_eur, ROUND(SUM(cogs_ark_eur)) AS cogs_enligt_ark_eur,
       ROUND(SAFE_DIVIDE(SUM(belopp_eur), SUM(netto_eur)) * 100, 1) AS faktura_pct_av_netto,
       ROUND(SAFE_DIVIDE(SUM(cogs_ark_eur), SUM(IF(tackning > 0, netto_eur * tackning, 0))) * 100, 1) AS ark_cogs_pct_av_kopplad_netto
FROM per_fak;
