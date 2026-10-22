-- Search Console-vyer för Best of Sports (SE, DK, FI): API-historik före bulkexportens första dag, därefter bulkexporten.
-- Samma mönster som views_sources.sql. Kör först när (1) historiken är hämtad med `site-audit backfill gsc` (tabellerna
-- gsc_api_url_bestofsports_se/dk/fi finns) och (2) bulkexporten har skapat tabellen searchdata_url_impression i varje dataset
-- (normalt 1–2 dygn efter att exporten slogs på, 2026-10-22).
--   sed 's/PROJ/gorilla-sports-data/g' sql/audit/views_sources_bestofsports.sql | bq query --use_legacy_sql=false

CREATE OR REPLACE VIEW `PROJ.site_audit.gsc_combined_bestofsports_se` AS
WITH export_start AS (SELECT MIN(data_date) AS d FROM `PROJ.searchconsole_bestofsports_se.searchdata_url_impression`)
SELECT data_date, site_url, url, query, CAST(is_anonymized_query AS BOOL) AS is_anonymized_query, search_type,
       clicks, impressions, sum_position
FROM `PROJ.searchconsole_bestofsports_se.searchdata_url_impression`
UNION ALL
SELECT a.data_date, a.site_url, a.url, a.query, a.is_anonymized_query, a.search_type, a.clicks, a.impressions, a.sum_position
FROM `PROJ.site_audit.gsc_api_url_bestofsports_se` a, export_start e
WHERE e.d IS NULL OR a.data_date < e.d;

CREATE OR REPLACE VIEW `PROJ.site_audit.gsc_combined_bestofsports_dk` AS
WITH export_start AS (SELECT MIN(data_date) AS d FROM `PROJ.searchconsole_bestofsports_dk.searchdata_url_impression`)
SELECT data_date, site_url, url, query, CAST(is_anonymized_query AS BOOL) AS is_anonymized_query, search_type,
       clicks, impressions, sum_position
FROM `PROJ.searchconsole_bestofsports_dk.searchdata_url_impression`
UNION ALL
SELECT a.data_date, a.site_url, a.url, a.query, a.is_anonymized_query, a.search_type, a.clicks, a.impressions, a.sum_position
FROM `PROJ.site_audit.gsc_api_url_bestofsports_dk` a, export_start e
WHERE e.d IS NULL OR a.data_date < e.d;

CREATE OR REPLACE VIEW `PROJ.site_audit.gsc_combined_bestofsports_fi` AS
WITH export_start AS (SELECT MIN(data_date) AS d FROM `PROJ.searchconsole_bestofsports_fi.searchdata_url_impression`)
SELECT data_date, site_url, url, query, CAST(is_anonymized_query AS BOOL) AS is_anonymized_query, search_type,
       clicks, impressions, sum_position
FROM `PROJ.searchconsole_bestofsports_fi.searchdata_url_impression`
UNION ALL
SELECT a.data_date, a.site_url, a.url, a.query, a.is_anonymized_query, a.search_type, a.clicks, a.impressions, a.sum_position
FROM `PROJ.site_audit.gsc_api_url_bestofsports_fi` a, export_start e
WHERE e.d IS NULL OR a.data_date < e.d;
