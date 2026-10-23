-- 2. Vilka sidor ger trafik, och vilken typ av sida är det? Senaste 90 dagarna, SE.
--    Svarar på: kommer trafiken till kategorier och produkter (som kan sälja) eller till startsida och information?
WITH s AS (
  SELECT REGEXP_REPLACE(url, r'^https?://[^/]+', '') AS path, SUM(clicks) AS klick, SUM(impressions) AS visningar,
         SAFE_DIVIDE(SUM(sum_position), SUM(impressions)) + 1 AS position
  FROM `PROJ.site_audit.gsc_api_url_bestofsports_se`
  WHERE data_date >= DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 90 DAY)
  GROUP BY 1
)
SELECT CASE WHEN path IN ('', '/') THEN 'startsida' WHEN STARTS_WITH(path, '/collections') THEN 'kategori'
            WHEN STARTS_WITH(path, '/products') THEN 'produkt' WHEN STARTS_WITH(path, '/blogs') THEN 'blogg' ELSE 'annat' END AS typ,
       COUNT(*) AS sidor, SUM(klick) AS klick, SUM(visningar) AS visningar,
       ROUND(SAFE_DIVIDE(SUM(klick), SUM(visningar)) * 100, 2) AS ctr_pct, ROUND(AVG(position), 1) AS snittposition
FROM s GROUP BY 1 ORDER BY klick DESC;
