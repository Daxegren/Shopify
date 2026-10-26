-- Google Ads och Meta per kampanj, senaste 30 dagarna till och med i går, per marknad: kostnad, klick, konverteringsvärde, ROAS och COS.
-- Visar vart pengarna går (Performance Max, Sök, varumärke, Meta-kampanjer) och vilka kampanjer som drar upp eller ner COS.
--
--   sed 's/PROJ/gorilla-sports-data/g' sql/analys/annonser_kampanjer_30d.sql | bq query --use_legacy_sql=false --max_rows=80
--
-- Belopp i marknadens valuta (SE i SEK, DK i DKK) och summeras inte över marknader. COS = kostnad / konverteringsvärde (plattformens eget värde).

DECLARE d1 DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 1 DAY);
DECLARE d0 DATE DEFAULT DATE_SUB(d1, INTERVAL 29 DAY);

SELECT * FROM (
  SELECT CASE currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE currency END AS market,
         'google_ads' AS plattform, IFNULL(channel_type, '-') AS typ, campaign_name AS kampanj,
         ROUND(SUM(cost)) AS kostnad, SUM(clicks) AS klick, ROUND(SUM(conversions_value)) AS varde,
         ROUND(SAFE_DIVIDE(SUM(conversions_value), SUM(cost)), 2) AS roas,
         ROUND(SAFE_DIVIDE(SUM(cost), SUM(conversions_value)) * 100, 1) AS cos_pct
  FROM `PROJ.site_audit.google_ads_daily_gorillasports_se`
  WHERE d BETWEEN d0 AND d1 GROUP BY 1, 2, 3, 4
  UNION ALL
  SELECT CASE currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE currency END,
         'meta', '-', campaign_name,
         ROUND(SUM(spend)), SUM(clicks), ROUND(SUM(purchase_value)),
         ROUND(SAFE_DIVIDE(SUM(purchase_value), SUM(spend)), 2),
         ROUND(SAFE_DIVIDE(SUM(spend), SUM(purchase_value)) * 100, 1)
  FROM `PROJ.site_audit.meta_ads_daily_gorillasports_se`
  WHERE d BETWEEN d0 AND d1 GROUP BY 1, 2, 3, 4
)
WHERE kostnad > 0 ORDER BY market, kostnad DESC;
