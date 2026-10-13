-- Var kommer besöksfallet ifrån? GA4-besök, köp och konvertering per land och kanal, P1 mot P0.
-- Samma perioder som omsattning_30d.sql. Kräver att tabellen fyllts först:
--   site-audit backfill ga4-kanal --site gorillasports-se --since 2026-08-01
--
--   sed 's/PROJ/gorilla-sports-data/g' sql/analys/trafik_kanal_30d.sql | bq query --use_legacy_sql=false
--
-- Värden per dag, eftersom GA4 kan sakna de sista dagarna i P1.

DECLARE p1_end DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 1 DAY);
DECLARE p1_start DATE DEFAULT DATE_SUB(p1_end, INTERVAL 29 DAY);
DECLARE p0_end DATE DEFAULT DATE_SUB(p1_start, INTERVAL 1 DAY);
DECLARE p0_start DATE DEFAULT DATE_SUB(p0_end, INTERVAL 29 DAY);

CREATE TEMP TABLE k AS
SELECT IF(hostname = 'www.gorillasports.dk', 'DK', 'SE') AS land, channel, source_medium, campaign,
       IF(d >= p1_start, 'P1', 'P0') AS period, d, sessions, purchases, revenue
FROM `PROJ.site_audit.ga4_channel_daily_gorillasports_se`
WHERE hostname IN ('www.gorillasports.se', 'www.gorillasports.dk') AND d BETWEEN p0_start AND p1_end;

CREATE TEMP TABLE dagar AS
SELECT land, period, COUNT(DISTINCT d) AS n FROM k GROUP BY 1, 2;

-- 1. Per kanal: besök och köp per dag, konvertering, och hur stor del av landets besöksfall kanalen står för
WITH s AS (
  SELECT k.land, channel,
         SUM(IF(k.period = 'P0', sessions, 0)) / ANY_VALUE(d0.n) AS besok_p0,
         SUM(IF(k.period = 'P1', sessions, 0)) / ANY_VALUE(d1.n) AS besok_p1,
         SUM(IF(k.period = 'P0', purchases, 0)) / ANY_VALUE(d0.n) AS kop_p0,
         SUM(IF(k.period = 'P1', purchases, 0)) / ANY_VALUE(d1.n) AS kop_p1
  FROM k JOIN dagar d0 ON d0.land = k.land AND d0.period = 'P0' JOIN dagar d1 ON d1.land = k.land AND d1.period = 'P1'
  GROUP BY 1, 2)
SELECT land, channel, ROUND(besok_p0) AS besok_dag_p0, ROUND(besok_p1) AS besok_dag_p1,
       ROUND(SAFE_DIVIDE(besok_p1 - besok_p0, besok_p0) * 100, 1) AS besok_pct,
       ROUND(SAFE_DIVIDE(besok_p1 - besok_p0, SUM(besok_p1 - besok_p0) OVER (PARTITION BY land)) * 100) AS andel_av_besoksfallet_pct,
       ROUND(kop_p0, 1) AS kop_dag_p0, ROUND(kop_p1, 1) AS kop_dag_p1,
       ROUND(SAFE_DIVIDE(kop_p0, besok_p0) * 100, 2) AS konv_p0_pct, ROUND(SAFE_DIVIDE(kop_p1, besok_p1) * 100, 2) AS konv_p1_pct
FROM s WHERE besok_p0 + besok_p1 >= 5 ORDER BY land, besok_p1 - besok_p0;

-- 2. De 20 källor/medium och kampanjer som tappat flest besök per dag
SELECT k.land, source_medium, campaign,
       ROUND(SUM(IF(k.period = 'P0', sessions, 0)) / ANY_VALUE(d0.n)) AS besok_dag_p0,
       ROUND(SUM(IF(k.period = 'P1', sessions, 0)) / ANY_VALUE(d1.n)) AS besok_dag_p1,
       ROUND(SUM(IF(k.period = 'P0', purchases, 0)) / ANY_VALUE(d0.n), 1) AS kop_dag_p0,
       ROUND(SUM(IF(k.period = 'P1', purchases, 0)) / ANY_VALUE(d1.n), 1) AS kop_dag_p1
FROM k JOIN dagar d0 ON d0.land = k.land AND d0.period = 'P0' JOIN dagar d1 ON d1.land = k.land AND d1.period = 'P1'
GROUP BY 1, 2, 3
ORDER BY SUM(IF(k.period = 'P1', sessions, 0)) / ANY_VALUE(d1.n) - SUM(IF(k.period = 'P0', sessions, 0)) / ANY_VALUE(d0.n)
LIMIT 20;

-- 3. Vecka för vecka per kanal, för att se när ett fall började
SELECT land, channel, DATE_TRUNC(d, ISOWEEK) AS vecka, SUM(sessions) AS besok, SUM(purchases) AS kop
FROM k GROUP BY 1, 2, 3 HAVING SUM(sessions) >= 50 ORDER BY 1, 2, 3;
