-- Produktdata: hur ren är katalogen? Antal och andel aktiva produkter med typiska problem.
-- Svarar på: hur mycket av katalogen lider av tomma titlar, "Default Title", blandade språk, slutsålt, saknad metadata?
--
--   sed -e 's/PROJ/gorilla-sports-data/g' -e 's/SHOPDS/shopify_bestofsports/g' sql/analys/produktdata_kvalitet.sql | bq query --use_legacy_sql=false
--
-- Bara produktnivå (titel, status, typ, SEO, lager). Bilder och beskrivningar finns inte i synktabellen; de kontrolleras av
-- genomlysningen (T1). Språkkontrollen är en grov ordlista (engelska och estniska ord), inte en riktig språkdetektering.
WITH a AS (
  SELECT * FROM `PROJ.SHOPDS.products` WHERE status = 'ACTIVE'
), n AS (SELECT COUNT(*) AS tot FROM a)
SELECT matt, antal, ROUND(SAFE_DIVIDE(antal, (SELECT tot FROM n)) * 100, 1) AS procent_av_aktiva FROM (
  SELECT 'Aktiva produkter' AS matt, COUNT(*) AS antal, 1 AS o FROM a
  UNION ALL SELECT 'Slut i lager (aktiv men lager <= 0)', COUNTIF(IFNULL(total_inventory, 0) <= 0), 2 FROM a
  UNION ALL SELECT 'Lager exakt 1 (risk för oförsäljbart vid dropship)', COUNTIF(total_inventory = 1), 3 FROM a
  UNION ALL SELECT 'Titel slutar på "Default Title"', COUNTIF(REGEXP_CONTAINS(title, r'(?i)default title')), 4 FROM a
  UNION ALL SELECT 'Titel med engelska eller estniska ord',
         COUNTIF(REGEXP_CONTAINS(title, r'(?i)\b(bicycle|bike|electric|saddle|bag|kids|boys|girls|maanteeratas|jalgratas|rattakiiver|tool|ratas)\b')), 5 FROM a
  UNION ALL SELECT 'Titel i VERSALER (mer än 60 % stora bokstäver)',
         COUNTIF(LENGTH(REGEXP_REPLACE(title, r'[^A-ZÅÄÖ]', '')) > 0.6 * LENGTH(REGEXP_REPLACE(title, r'[^A-Za-zÅÄÖåäö]', '')) AND LENGTH(title) > 8), 6 FROM a
  UNION ALL SELECT 'Titel kortare än 20 eller längre än 150 tecken', COUNTIF(LENGTH(title) < 20 OR LENGTH(title) > 150), 7 FROM a
  UNION ALL SELECT 'Saknar produkttyp', COUNTIF(IFNULL(product_type, '') = ''), 8 FROM a
  UNION ALL SELECT 'Saknar SEO-beskrivning', COUNTIF(IFNULL(seo_description, '') = ''), 9 FROM a
  UNION ALL SELECT 'Saknar leverantörsnamn (vendor)', COUNTIF(IFNULL(vendor, '') = ''), 10 FROM a
  UNION ALL SELECT 'Saknar webbadress (inte publicerad i webbshopen)', COUNTIF(IFNULL(online_store_url, '') = ''), 11 FROM a
  UNION ALL SELECT 'Leverantörsetikett Velomarket', COUNTIF(REGEXP_CONTAINS(IFNULL(tags, ''), r'(?i)velomarket')), 12 FROM a
) ORDER BY o;
