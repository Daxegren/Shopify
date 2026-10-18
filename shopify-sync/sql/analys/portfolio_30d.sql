-- Är nedgången (eller uppgången) specifik för en butik, eller gäller den hela portföljen?
-- Jämför de senaste 30 dagarna med de 30 dagarna innan (och samma datum förra året där data finns), per butik och marknad,
-- och sätter varje butik mot mediansiffran för portföljen. Kvoter och förändringar i procent jämförs; belopp i olika valutor summeras aldrig.
--
--   sed 's/PROJ/gorilla-sports-data/g' sql/analys/portfolio_30d.sql | bq query --use_legacy_sql=false
--
-- Förutsättning: vyn portfolio_daily finns (site-audit growth-sql). PROJ är projektet där portföljvyerna ligger.
-- Läsning: "relativt_median" är butikens förändring minus medianen för alla butiker och marknader. Ett värde nära noll betyder
-- att butiken följer portföljen (säsong, plattformar, marknad). Ett stort negativt värde betyder att orsaken är butikens egen.

DECLARE p1_end DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 1 DAY);
DECLARE p1_start DATE DEFAULT DATE_SUB(p1_end, INTERVAL 29 DAY);
DECLARE p0_end DATE DEFAULT DATE_SUB(p1_start, INTERVAL 1 DAY);
DECLARE p0_start DATE DEFAULT DATE_SUB(p0_end, INTERVAL 29 DAY);

CREATE TEMP TABLE per AS
SELECT store, vertical, market, currency,
       CASE WHEN d BETWEEN p1_start AND p1_end THEN 'P1'
            WHEN d BETWEEN p0_start AND p0_end THEN 'P0'
            WHEN d BETWEEN DATE_SUB(p1_start, INTERVAL 1 YEAR) AND DATE_SUB(p1_end, INTERVAL 1 YEAR) THEN 'LY' END AS period,
       d, orders, revenue, sessions, IFNULL(google_cost, 0) + IFNULL(meta_cost, 0) AS ad_cost
FROM `PROJ.portfolio.portfolio_daily`
WHERE d >= DATE_SUB(p0_start, INTERVAL 1 YEAR);

CREATE TEMP TABLE agg AS
SELECT store, vertical, market, currency,
       SUM(IF(period = 'P0', orders, 0)) AS orders_p0, SUM(IF(period = 'P1', orders, 0)) AS orders_p1, SUM(IF(period = 'LY', orders, 0)) AS orders_ly,
       SUM(IF(period = 'P0', revenue, 0)) AS revenue_p0, SUM(IF(period = 'P1', revenue, 0)) AS revenue_p1,
       SUM(IF(period = 'P0', sessions, 0)) AS sessions_p0, SUM(IF(period = 'P1', sessions, 0)) AS sessions_p1, SUM(IF(period = 'LY', sessions, 0)) AS sessions_ly,
       SUM(IF(period = 'P0', ad_cost, 0)) AS ad_cost_p0, SUM(IF(period = 'P1', ad_cost, 0)) AS ad_cost_p1,
       COUNT(DISTINCT IF(period = 'LY' AND sessions IS NOT NULL, d, NULL)) AS dagar_ly
FROM per WHERE period IS NOT NULL
GROUP BY 1, 2, 3, 4;

CREATE TEMP TABLE jmf AS
SELECT *,
       SAFE_DIVIDE(revenue_p1 - revenue_p0, revenue_p0) * 100 AS revenue_pct,
       SAFE_DIVIDE(orders_p1 - orders_p0, orders_p0) * 100 AS orders_pct,
       SAFE_DIVIDE(sessions_p1 - sessions_p0, sessions_p0) * 100 AS sessions_pct,
       SAFE_DIVIDE(ad_cost_p1 - ad_cost_p0, ad_cost_p0) * 100 AS ad_cost_pct,
       SAFE_DIVIDE(SAFE_DIVIDE(orders_p1, sessions_p1) - SAFE_DIVIDE(orders_p0, sessions_p0), SAFE_DIVIDE(orders_p0, sessions_p0)) * 100 AS order_rate_pct,
       IF(dagar_ly >= 25, SAFE_DIVIDE(sessions_p1 - sessions_ly, sessions_ly) * 100, NULL) AS sessions_vs_ly_pct,
       SAFE_DIVIDE(SAFE_DIVIDE(revenue_p1, ad_cost_p1) - SAFE_DIVIDE(revenue_p0, ad_cost_p0), SAFE_DIVIDE(revenue_p0, ad_cost_p0)) * 100 AS mer_pct
FROM agg;

-- 1. Per butik och marknad, med avvikelse från portföljens median
SELECT store, market, currency, vertical,
       ROUND(revenue_pct, 1) AS oms_pct, ROUND(orders_pct, 1) AS ordrar_pct, ROUND(sessions_pct, 1) AS besok_pct,
       ROUND(order_rate_pct, 1) AS andel_kop_pct, ROUND(ad_cost_pct, 1) AS annonskostnad_pct, ROUND(mer_pct, 1) AS mer_pct,
       ROUND(sessions_vs_ly_pct, 1) AS besok_mot_fjol_pct,
       ROUND(revenue_pct - (SELECT APPROX_QUANTILES(revenue_pct, 2)[OFFSET(1)] FROM jmf), 1) AS oms_relativt_median
FROM jmf ORDER BY oms_relativt_median;

-- 2. Hela portföljen i ett: hur många butiker och marknader har gått ned mer än 10 procent?
SELECT COUNT(*) AS butiker_marknader,
       COUNTIF(revenue_pct < -10) AS ned_mer_an_10_pct, COUNTIF(revenue_pct > 10) AS upp_mer_an_10_pct,
       ROUND(APPROX_QUANTILES(revenue_pct, 2)[OFFSET(1)], 1) AS median_oms_pct,
       ROUND(APPROX_QUANTILES(sessions_pct, 2)[OFFSET(1)], 1) AS median_besok_pct,
       ROUND(APPROX_QUANTILES(order_rate_pct, 2)[OFFSET(1)], 1) AS median_andel_kop_pct
FROM jmf;
