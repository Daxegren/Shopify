-- 5. Vad kostar annonserna och vad ger de? Google Ads, senaste 28 dagarna, per kampanj.
--    Svarar på: går pengar till klick som inte blir köp, och vilka kampanjer bär sig?
SELECT campaign_name, channel_type, currency, ROUND(SUM(cost)) AS kostnad, SUM(impressions) AS visningar, SUM(clicks) AS klick,
       ROUND(SAFE_DIVIDE(SUM(clicks), SUM(impressions)) * 100, 2) AS ctr_pct, ROUND(SAFE_DIVIDE(SUM(cost), SUM(clicks)), 1) AS kr_per_klick,
       ROUND(SUM(conversions), 1) AS konverteringar, ROUND(SUM(conversions_value)) AS varde,
       ROUND(SAFE_DIVIDE(SUM(conversions_value), SUM(cost)), 2) AS roas
FROM `PROJ.site_audit.google_ads_daily_bestofsports`
WHERE d >= DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 28 DAY)
GROUP BY 1, 2, 3 ORDER BY kostnad DESC;
