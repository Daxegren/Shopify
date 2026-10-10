-- Vyer för att följa genomlysningar över tid. Ersätt `PROJ` med projekt-id och kör i BigQuery,
-- eller: sed 's/PROJ/gorilla-sports-data/g' sql/audit/views.sql | bq query --use_legacy_sql=false

-- Senaste körningen per sajt
CREATE OR REPLACE VIEW `PROJ.site_audit.latest_run` AS
SELECT * EXCEPT(rn) FROM (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY site ORDER BY started_at DESC) AS rn FROM `PROJ.site_audit.runs`
) WHERE rn = 1;

-- Antal fynd per kontroll och körning (för trendgrafer: "404 i sitemapen 46 -> 3")
CREATE OR REPLACE VIEW `PROJ.site_audit.check_trend` AS
SELECT f.site, r.started_at, f.run_id, f.check_id, f.category, ANY_VALUE(f.severity) AS severity, COUNT(*) AS findings
FROM `PROJ.site_audit.findings` f
JOIN `PROJ.site_audit.runs` r USING (run_id)
GROUP BY 1, 2, 3, 4, 5;

-- Fynd i senaste körningen
CREATE OR REPLACE VIEW `PROJ.site_audit.open_findings` AS
SELECT f.* FROM `PROJ.site_audit.findings` f JOIN `PROJ.site_audit.latest_run` l USING (run_id);

-- Vad som ändrats mellan de två senaste körningarna per sajt
CREATE OR REPLACE VIEW `PROJ.site_audit.finding_changes` AS
WITH ranked AS (
  SELECT run_id, site, ROW_NUMBER() OVER (PARTITION BY site ORDER BY started_at DESC) AS rn FROM `PROJ.site_audit.runs`
),
cur AS (SELECT f.site, f.check_id, COALESCE(f.url, f.resource) AS target, f.message, f.severity
        FROM `PROJ.site_audit.findings` f JOIN ranked r USING (run_id) WHERE r.rn = 1),
prev AS (SELECT f.site, f.check_id, COALESCE(f.url, f.resource) AS target, f.message, f.severity
         FROM `PROJ.site_audit.findings` f JOIN ranked r USING (run_id) WHERE r.rn = 2)
SELECT COALESCE(c.site, p.site) AS site, COALESCE(c.check_id, p.check_id) AS check_id,
       COALESCE(c.target, p.target) AS target, COALESCE(c.message, p.message) AS message,
       CASE WHEN p.check_id IS NULL THEN 'ny' WHEN c.check_id IS NULL THEN 'åtgärdad' ELSE 'kvar' END AS status
FROM cur c FULL OUTER JOIN prev p ON c.site = p.site AND c.check_id = p.check_id AND c.target = p.target;

-- Sidhistorik: statuskod, titel och H1 per URL och körning
CREATE OR REPLACE VIEW `PROJ.site_audit.page_history` AS
SELECT p.site, r.started_at, p.url, p.page_type, p.status, p.redirect_count, p.final_url, p.title, p.h1_count,
       p.word_count, p.html_bytes, p.images_missing_alt
FROM `PROJ.site_audit.pages` p JOIN `PROJ.site_audit.runs` r USING (run_id);

-- Sökdata per URL kopplad till senaste crawlen (kräver Search Console-exporten)
CREATE OR REPLACE VIEW `PROJ.site_audit.pages_with_search` AS
WITH gsc AS (
  SELECT COALESCE(NULLIF(RTRIM(REGEXP_EXTRACT(url, r'^https?://[^/]+(/[^?#]*)'), '/'), ''), '/') AS path,
         SUM(clicks) AS clicks_90d, SUM(impressions) AS impressions_90d,
         SAFE_DIVIDE(SUM(sum_position), SUM(impressions)) + 1 AS avg_position_90d
  FROM `PROJ.searchconsole.searchdata_url_impression`
  WHERE data_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY)
  GROUP BY 1
)
SELECT p.site, p.url, p.page_type, p.status, p.title, p.h1_count, p.word_count,
       gsc.clicks_90d, gsc.impressions_90d, gsc.avg_position_90d
FROM `PROJ.site_audit.pages` p
JOIN `PROJ.site_audit.latest_run` l USING (run_id)
LEFT JOIN gsc ON gsc.path = COALESCE(NULLIF(RTRIM(p.path, '/'), ''), '/');

-- Ändringslogg med effekt i Search Console: klick 90 dagar före/efter per registrerad ändring
CREATE OR REPLACE VIEW `PROJ.site_audit.change_impact_gsc` AS
WITH g AS (
  SELECT data_date, COALESCE(NULLIF(RTRIM(REGEXP_EXTRACT(url, r'^https?://[^/]+(/[^?#]*)'), '/'), ''), '/') AS path, clicks, impressions
  FROM `PROJ.searchconsole.searchdata_url_impression`
)
SELECT c.change_id, c.site, c.change_date, c.description, c.url_pattern,
  SUM(IF(g.data_date BETWEEN DATE_SUB(c.change_date, INTERVAL 90 DAY) AND DATE_SUB(c.change_date, INTERVAL 1 DAY), g.clicks, 0)) AS clicks_before,
  SUM(IF(g.data_date BETWEEN c.change_date AND DATE_ADD(c.change_date, INTERVAL 89 DAY), g.clicks, 0)) AS clicks_after,
  SAFE_DIVIDE(
    SUM(IF(g.data_date BETWEEN c.change_date AND DATE_ADD(c.change_date, INTERVAL 89 DAY), g.clicks, 0)) -
    SUM(IF(g.data_date BETWEEN DATE_SUB(c.change_date, INTERVAL 90 DAY) AND DATE_SUB(c.change_date, INTERVAL 1 DAY), g.clicks, 0)),
    SUM(IF(g.data_date BETWEEN DATE_SUB(c.change_date, INTERVAL 90 DAY) AND DATE_SUB(c.change_date, INTERVAL 1 DAY), g.clicks, 0))) * 100 AS change_pct,
  DATE_DIFF(CURRENT_DATE(), c.change_date, DAY) AS days_since_change
FROM `PROJ.site_audit.changes` c
JOIN g ON REGEXP_CONTAINS(g.path, c.url_pattern)
WHERE c.url_pattern IS NOT NULL
GROUP BY 1, 2, 3, 4, 5;

-- En rad per landningssida senaste 90 dagarna: Google-klick, GA4-sessioner och Shopify-ordrar.
-- Grunden för frågor som "vilka kollektioner drar trafik men säljer inte?"
CREATE OR REPLACE VIEW `PROJ.site_audit.landing_performance_90d` AS
WITH gsc AS (
  SELECT COALESCE(NULLIF(RTRIM(REGEXP_EXTRACT(url, r'^https?://[^/]+(/[^?#]*)'), '/'), ''), '/') AS path,
         SUM(clicks) AS clicks, SUM(impressions) AS impressions,
         SAFE_DIVIDE(SUM(sum_position), SUM(impressions)) + 1 AS avg_position
  FROM `PROJ.site_audit.gsc_combined_gorillasports_se`
  WHERE data_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY) GROUP BY 1
),
ga4 AS (
  SELECT COALESCE(NULLIF(RTRIM(REGEXP_EXTRACT(landing, r'^([^?#]*)'), '/'), ''), '/') AS path,
         SUM(sessions) AS sessions, SUM(purchases) AS purchases, SUM(revenue) AS ga4_revenue
  FROM `PROJ.site_audit.ga4_landing_daily_gorillasports_se`
  WHERE d >= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY) AND hostname = 'www.gorillasports.se' GROUP BY 1
),
shop AS (
  SELECT COALESCE(NULLIF(RTRIM(REGEXP_EXTRACT(first_visit_landing_page, r'^(?:https?://[^/]+)?(/[^?#]*)'), '/'), ''), '/') AS path,
         COUNT(*) AS orders, SUM(CAST(total_price AS FLOAT64)) AS shopify_revenue
  FROM `PROJ.shopify.orders`
  WHERE created_at >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 90 DAY) AND cancelled_at IS NULL
    AND presentment_currency = 'SEK' GROUP BY 1
)
SELECT COALESCE(gsc.path, ga4.path, shop.path) AS path, gsc.clicks, gsc.impressions, gsc.avg_position,
       ga4.sessions, ga4.purchases, ga4.ga4_revenue, shop.orders, shop.shopify_revenue,
       SAFE_DIVIDE(shop.orders, ga4.sessions) AS conversion_rate
FROM gsc FULL OUTER JOIN ga4 USING (path) FULL OUTER JOIN shop USING (path);
