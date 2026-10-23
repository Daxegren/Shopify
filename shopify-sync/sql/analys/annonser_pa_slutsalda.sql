-- Annonsklick på produkter som inte går att köpa: utkast, arkiverade eller slut i lager. Senaste 28 dagarna.
-- Svarar på: hur många annonskronor går till produkter där besökaren inte kan köpa?
--
--   sed -e 's/PROJ/gorilla-sports-data/g' -e 's/KEY/bestofsports/g' -e 's/SHOPDS/shopify_bestofsports/g' \
--       sql/analys/annonser_pa_slutsalda.sql | bq query --use_legacy_sql=false
--
-- Annonsernas item_id har formen shopify_<land>_<produkt-id>_<variant-id>; produkt-id kopplas mot Shopify. Förutsätter
-- Shopify-appen Google & YouTube. Produkter utan träff (annan id-form) visas som okopplade.
WITH ads AS (
  SELECT REGEXP_EXTRACT(item_id, r'(?i)^shopify_[a-z]+_(\d+)_\d+$') AS pid, ANY_VALUE(title) AS title, ANY_VALUE(currency) AS valuta,
         SUM(cost) AS kostnad, SUM(clicks) AS klick, SUM(conversions) AS konv
  FROM `PROJ.site_audit.google_ads_products_daily_KEY`
  WHERE d >= DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 28 DAY)
  GROUP BY 1
), p AS (
  SELECT REGEXP_EXTRACT(id, r'(\d+)$') AS pid, status, total_inventory FROM `PROJ.SHOPDS.products`
)
SELECT IFNULL(p.status, 'OKOPPLAD') AS status, IFNULL(p.total_inventory, 0) AS lager, a.title, a.valuta,
       ROUND(a.kostnad) AS kostnad, a.klick, ROUND(a.konv, 1) AS konv
FROM ads a LEFT JOIN p USING (pid)
WHERE a.klick > 0 AND (p.status IS NULL OR p.status != 'ACTIVE' OR IFNULL(p.total_inventory, 0) <= 0)
ORDER BY a.kostnad DESC LIMIT 40;
