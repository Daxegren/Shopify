-- 3. Sidor som visas mycket men får få klick: titel och beskrivning i sökresultatet är första åtgärden. Senaste 90 dagarna, SE.
--    Klickgap = klick som positionen normalt ger minus verkliga klick (grov tumregel, inte en mätning).
WITH s AS (
  SELECT REGEXP_REPLACE(url, r'^https?://[^/]+', '') AS path, SUM(clicks) AS klick, SUM(impressions) AS visningar,
         SAFE_DIVIDE(SUM(sum_position), SUM(impressions)) + 1 AS position
  FROM `PROJ.site_audit.gsc_api_url_bestofsports_se`
  WHERE data_date >= DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 90 DAY)
  GROUP BY 1
)
SELECT path, klick, visningar, ROUND(position, 1) AS position, ROUND(SAFE_DIVIDE(klick, visningar) * 100, 2) AS ctr_pct,
       ROUND(visningar * CASE WHEN position <= 1.5 THEN 0.28 WHEN position <= 2.5 THEN 0.15 WHEN position <= 3.5 THEN 0.10
         WHEN position <= 5.5 THEN 0.06 WHEN position <= 10.5 THEN 0.025 WHEN position <= 15.5 THEN 0.01 ELSE 0.004 END - klick) AS klickgap
FROM s WHERE visningar >= 200 ORDER BY klickgap DESC LIMIT 25;
