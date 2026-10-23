-- 1. Hur ser efterfrågan och synlighet ut över tid? Klick, visningar, klickfrekvens och snittposition per månad i Google (SE).
--    Svarar på: växer eller krymper sajten i sökning, och är det synligheten eller klicken som saknas?
-- Källa: Search Console via API (16 månader). Kör för bestofsports-se; DK och FI har ingen historik än.
SELECT FORMAT_DATE('%Y-%m', data_date) AS manad,
       SUM(clicks) AS klick, SUM(impressions) AS visningar,
       ROUND(SAFE_DIVIDE(SUM(clicks), SUM(impressions)) * 100, 2) AS ctr_pct,
       ROUND(SAFE_DIVIDE(SUM(sum_position), SUM(impressions)) + 1, 1) AS snittposition
FROM `PROJ.site_audit.gsc_api_url_bestofsports_se`
GROUP BY 1 ORDER BY 1;
