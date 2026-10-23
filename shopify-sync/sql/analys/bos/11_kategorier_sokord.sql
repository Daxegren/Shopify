-- 11. Underlag för kategorisidorna: de 25 kategorisidorna med flest visningar och deras sex största sökfrågor.
--     Svarar på: vilka sökord är sidan synlig för, på vilken position, och hur många klick blir det?
--     Källa: Search Console via API sedan 2026-07-01 (anonymiserade frågor saknas).
WITH q AS (
  SELECT REGEXP_REPLACE(url, r'^https?://[^/]+', '') AS path, query, SUM(clicks) AS klick, SUM(impressions) AS vis,
         SAFE_DIVIDE(SUM(sum_position), SUM(impressions)) + 1 AS pos
  FROM `PROJ.site_audit.gsc_api_url_query_bestofsports_se`
  WHERE data_date >= '2026-07-01' AND REGEXP_CONTAINS(url, r'^https?://[^/]+/collections/[^/?#]+/?$') AND query IS NOT NULL
  GROUP BY 1, 2
), tot AS (
  SELECT path, SUM(vis) AS path_vis FROM q GROUP BY 1 ORDER BY path_vis DESC LIMIT 25
), r AS (
  SELECT q.path, q.query, q.klick, q.vis, q.pos, tot.path_vis, ROW_NUMBER() OVER (PARTITION BY q.path ORDER BY q.vis DESC) AS rn
  FROM q JOIN tot USING (path)
)
SELECT path, path_vis AS sidans_visningar, query, klick, vis AS visningar, ROUND(pos, 1) AS position
FROM r WHERE rn <= 6 ORDER BY path_vis DESC, path, rn;
