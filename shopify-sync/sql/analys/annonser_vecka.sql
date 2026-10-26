-- Google Ads och Meta per vecka och marknad: kostnad, visningar, klick, klickfrekvens, kostnad per klick, konverteringsvärde och ROAS.
-- Svarar på om annonstappet är färre visningar (synlighet), lägre klickfrekvens eller dyrare klick.
--
--   sed 's/PROJ/gorilla-sports-data/g' sql/analys/annonser_vecka.sql | bq query --use_legacy_sql=false --max_rows=80
--
-- Använder vyn growth_ads_daily_gorillasports_se (skapad av site-audit growth-sql). Belopp i marknadens valuta och summeras inte över marknader.
-- Senaste 12 hela veckor (måndag till söndag, svensk tid).

SELECT DATE_TRUNC(d, ISOWEEK) AS vecka, platform, market, ANY_VALUE(currency) AS valuta,
       ROUND(SUM(cost)) AS kostnad, SUM(impressions) AS visningar, SUM(clicks) AS klick,
       ROUND(SAFE_DIVIDE(SUM(clicks), SUM(impressions)) * 100, 2) AS ctr_pct,
       ROUND(SAFE_DIVIDE(SUM(cost), SUM(clicks)), 2) AS kr_per_klick,
       ROUND(SUM(conversions_value)) AS konv_varde,
       ROUND(SAFE_DIVIDE(SUM(conversions_value), SUM(cost)), 2) AS roas
FROM `PROJ.site_audit.growth_ads_daily_gorillasports_se`
WHERE d >= DATE_SUB(DATE_TRUNC(CURRENT_DATE('Europe/Stockholm'), ISOWEEK), INTERVAL 12 WEEK)
  AND d < DATE_TRUNC(CURRENT_DATE('Europe/Stockholm'), ISOWEEK)
GROUP BY 1, 2, 3
ORDER BY market, platform, vecka;
