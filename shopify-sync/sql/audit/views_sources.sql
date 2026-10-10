-- Källvyer som behövs före första genomlysningen (Search Console: API-historik + bulkexport).
-- Kör: sed 's/PROJ/gorilla-sports-data/g' sql/audit/views_sources.sql | bq query --use_legacy_sql=false

-- Search Console: API-historik (site-audit backfill gsc) före bulkexportens första dag,
-- därefter bulkexporten. En vy per sajt; kopiera blocket och byt export-dataset och tabellsuffix
-- för fler sajter (t.ex. searchconsole_dk och gsc_api_url_gorillasports_dk).
-- Peka gsc_table i sites.toml på vyn.
CREATE OR REPLACE VIEW `PROJ.site_audit.gsc_combined_gorillasports_se` AS
WITH export_start AS (SELECT MIN(data_date) AS d FROM `PROJ.searchconsole.searchdata_url_impression`)
SELECT data_date, site_url, url, query, CAST(is_anonymized_query AS BOOL) AS is_anonymized_query, search_type,
       clicks, impressions, sum_position
FROM `PROJ.searchconsole.searchdata_url_impression`
UNION ALL
SELECT a.data_date, a.site_url, a.url, a.query, a.is_anonymized_query, a.search_type, a.clicks, a.impressions, a.sum_position
FROM `PROJ.site_audit.gsc_api_url_gorillasports_se` a, export_start e
WHERE e.d IS NULL OR a.data_date < e.d;

-- Samma kombinerade Search Console-vy för gorillasports.dk
CREATE OR REPLACE VIEW `PROJ.site_audit.gsc_combined_gorillasports_dk` AS
WITH export_start AS (SELECT MIN(data_date) AS d FROM `PROJ.searchconsole_dk.searchdata_url_impression`)
SELECT data_date, site_url, url, query, CAST(is_anonymized_query AS BOOL) AS is_anonymized_query, search_type,
       clicks, impressions, sum_position
FROM `PROJ.searchconsole_dk.searchdata_url_impression`
UNION ALL
SELECT a.data_date, a.site_url, a.url, a.query, a.is_anonymized_query, a.search_type, a.clicks, a.impressions, a.sum_position
FROM `PROJ.site_audit.gsc_api_url_gorillasports_dk` a, export_start e
WHERE e.d IS NULL OR a.data_date < e.d;
