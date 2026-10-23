-- 4. Var kommer besökarna ifrån och hur många köper? GA4, alla tre domäner, perioden som finns (egendomarna är nya).
--    Svarar på: har sajten trafik som inte köper, och från vilken kanal?
SELECT hostname, channel, MIN(d) AS fran, MAX(d) AS till, SUM(sessions) AS besok, SUM(purchases) AS kop,
       ROUND(SUM(revenue)) AS intakt, ROUND(SAFE_DIVIDE(SUM(purchases), SUM(sessions)) * 100, 2) AS konvertering_pct
FROM `PROJ.site_audit.ga4_channel_daily_bestofsports`
GROUP BY 1, 2 HAVING SUM(sessions) >= 10 ORDER BY hostname, besok DESC;
