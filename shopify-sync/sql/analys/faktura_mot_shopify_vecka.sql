-- Stämmer GSDE:s varufakturor mot Shopify-ordrarna? Fakturabelopp per vecka mot nettoförsäljning och arkets inköpspris (net_profit_sku) för samma veckas ordrar.
-- Underlag: leverantörsfakturorna 2026 (kundkonto hos GSDE), CSV med 408 poster i Davids Drive, mappen "Bokföring 2026 - rapporter till Claude" (filen leverantorsfakturor-2026.csv). Filen ligger inte i repot (affärsdata).
-- Förberedelse (en gång; ladda ned CSV-filen från Drive, ladda upp den till Cloud Shell som ~/leverantorsfakturor-2026.csv):
--   bq load --replace --source_format=CSV --skip_leading_rows=1 \
--     --schema='bokforingsdatum:DATE,forfallodatum:DATE,ursprung:STRING,fakturanr:STRING,ref2:STRING,typ:STRING,belopp_eur:FLOAT' \
--     gorilla-sports-data:site_audit.lev_fakturor_2026 ~/leverantorsfakturor-2026.csv
-- Kör: sed 's/PROJ/gorilla-sports-data/g' sql/analys/faktura_mot_shopify_vecka.sql | bq query --use_legacy_sql=false --max_rows=100
--
-- Antaganden:
--  * Varufaktura = typ som börjar på 'varufaktura' (varufaktura, varufaktura_utan_ref2). Fakturan bokförs vanligen dagen efter ordern, så bokföringsdatum minus 1 dag används som orderdag.
--  * Kreditnotor (typ 'kreditnota') redovisas separat och ingår inte i jämförelsen mot inköpspriset.
--  * Fakturabelopp är exkl. moms (0 % moms, EU-leverans) i EUR. Shopify-beloppen delas med moms 1,25 och kurs SEK 11,4 respektive DKK 8,0 (arkens kurser).
--  * Orderdata finns bara från 2026-08-10, så jämförelsen avser veckor från 2026-08-17. Den sista (pågående) veckan tas inte med.
--  * Arkets täckning av omsättningen redovisas per vecka. Inköpspriset skalas inte upp för okopplade rader; kolumnen cogs_ark_skalad delar med täckningen.
-- Kolumner verifierade mot src/shopify_sync/schema.py: orders(id, created_at, cancelled_at, presentment_currency), order_line_items(order_id, sku, quantity, discounted_total), site_audit.net_profit_sku(market, sku, buying_eur).
-- Läs så här: faktura_per_ark_cogs = 1,00 betyder att arkets inköpspris stämmer med vad GSDE fakturerar. Över 1 betyder att arket är för lågt.
-- Detta skript ändrar inget.

DECLARE fx_se FLOAT64 DEFAULT 11.4;
DECLARE fx_dk FLOAT64 DEFAULT 8.0;
DECLARE moms FLOAT64 DEFAULT 1.25;
DECLARE v_start DATE DEFAULT DATE '2026-08-17';
DECLARE v_slut DATE DEFAULT DATE_SUB(DATE_TRUNC(CURRENT_DATE('Europe/Stockholm'), ISOWEEK), INTERVAL 1 DAY);

CREATE TEMP TABLE fak AS
SELECT DATE_TRUNC(DATE_SUB(bokforingsdatum, INTERVAL 1 DAY), ISOWEEK) AS vecka,
       SUM(IF(STARTS_WITH(typ, 'varufaktura'), belopp_eur, 0)) AS varufaktura_eur,
       SUM(IF(typ = 'kreditnota', belopp_eur, 0)) AS kredit_eur,
       COUNTIF(STARTS_WITH(typ, 'varufaktura')) AS antal_fakturor
FROM `PROJ.site_audit.lev_fakturor_2026`
WHERE DATE_SUB(bokforingsdatum, INTERVAL 1 DAY) BETWEEN v_start AND v_slut
GROUP BY 1;

CREATE TEMP TABLE shop AS
SELECT DATE_TRUNC(DATE(o.created_at, 'Europe/Stockholm'), ISOWEEK) AS vecka,
       SUM(li.discounted_total / moms / IF(o.presentment_currency = 'DKK', fx_dk, fx_se)) AS netto_eur,
       SUM(IF(s.sku IS NOT NULL, li.discounted_total / moms / IF(o.presentment_currency = 'DKK', fx_dk, fx_se), 0)) AS kopplad_netto_eur,
       SUM(IF(s.sku IS NOT NULL, li.quantity * s.buying_eur, 0)) AS cogs_ark_eur
FROM `PROJ.shopify.orders` o
JOIN `PROJ.shopify.order_line_items` li ON li.order_id = o.id
LEFT JOIN `PROJ.site_audit.net_profit_sku` s
  ON s.market = IF(o.presentment_currency = 'DKK', 'DK', 'SE') AND s.sku = TRIM(li.sku)
WHERE o.cancelled_at IS NULL AND o.presentment_currency IN ('SEK', 'DKK')
  AND DATE(o.created_at, 'Europe/Stockholm') BETWEEN v_start AND v_slut
GROUP BY 1;

-- 1. Per vecka.
SELECT f.vecka, f.antal_fakturor, ROUND(f.varufaktura_eur) AS varufaktura_eur, ROUND(f.kredit_eur) AS kredit_eur,
       ROUND(s.netto_eur) AS netto_forsaljning_eur,
       ROUND(SAFE_DIVIDE(s.kopplad_netto_eur, s.netto_eur) * 100, 1) AS ark_tackning_pct,
       ROUND(s.cogs_ark_eur) AS cogs_ark_eur, ROUND(SAFE_DIVIDE(s.cogs_ark_eur, SAFE_DIVIDE(s.kopplad_netto_eur, s.netto_eur))) AS cogs_ark_skalad_eur,
       ROUND(SAFE_DIVIDE(f.varufaktura_eur, s.netto_eur) * 100, 1) AS faktura_pct_av_netto,
       ROUND(SAFE_DIVIDE(f.varufaktura_eur, SAFE_DIVIDE(s.cogs_ark_eur, SAFE_DIVIDE(s.kopplad_netto_eur, s.netto_eur))), 2) AS faktura_per_ark_cogs
FROM fak f JOIN shop s USING (vecka) ORDER BY f.vecka;

-- 2. Totalt över alla veckor ovan.
SELECT COUNT(*) AS veckor, ROUND(SUM(f.varufaktura_eur)) AS varufaktura_eur, ROUND(SUM(f.kredit_eur)) AS kredit_eur, ROUND(SUM(s.netto_eur)) AS netto_forsaljning_eur,
       ROUND(SAFE_DIVIDE(SUM(s.kopplad_netto_eur), SUM(s.netto_eur)) * 100, 1) AS ark_tackning_pct,
       ROUND(SAFE_DIVIDE(SUM(f.varufaktura_eur), SUM(s.netto_eur)) * 100, 1) AS faktura_pct_av_netto,
       ROUND(SAFE_DIVIDE(SUM(f.varufaktura_eur), SAFE_DIVIDE(SUM(s.cogs_ark_eur), SAFE_DIVIDE(SUM(s.kopplad_netto_eur), SUM(s.netto_eur)))), 2) AS faktura_per_ark_cogs
FROM fak f JOIN shop s USING (vecka);
