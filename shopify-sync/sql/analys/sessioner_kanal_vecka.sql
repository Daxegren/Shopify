-- Var kom sessionshoppet på gorillasports.se ifrån? GA4-sessioner och köp per vecka och kanal (SE och DK), från 2026-08-03.
-- Bakgrund: pengalage_veckovis.sql 2026-10-28 visade SE-sessioner ~7 000/vecka som steg till 18 186 (vecka 2026-10-12) och 13 982 (2026-10-19), medan köpen låg still (61–74).
-- Del 1 visar vilken kanal som växte. Del 2 visar de källor/medium och kampanjer som växte mest i de två veckorna mot de fem veckorna före.
-- Kolumner (verifierade mot trafik_kanal_30d.sql): d, hostname, channel, source_medium, campaign, sessions, purchases, revenue i ga4_channel_daily_gorillasports_se.
-- Kör: sed 's/PROJ/gorilla-sports-data/g' sql/analys/sessioner_kanal_vecka.sql | bq query --use_legacy_sql=false --max_rows=200
-- Läs så här: en kanal som växer mycket i sessioner men inte i köp (konvertering nära 0) är trolig bottrafik, en felmärkt kanal eller en spårningsändring.
-- Det visar INTE orsaken; det pekar ut var man ska titta.

DECLARE slut DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 1 DAY);
DECLARE v_sista DATE DEFAULT DATE_TRUNC(DATE_SUB(slut, INTERVAL 6 DAY), ISOWEEK);
DECLARE v_start DATE DEFAULT DATE '2026-08-03';
DECLARE spik_start DATE DEFAULT DATE '2026-10-12';
DECLARE fore_start DATE DEFAULT DATE '2026-09-07';

-- 0. Kontroll av källan: hur många dagar finns per vecka och värdnamn (en hel vecka har 7).
SELECT DATE_TRUNC(d, ISOWEEK) AS vecka, hostname, COUNT(DISTINCT d) AS dagar, SUM(sessions) AS sessioner
FROM `PROJ.site_audit.ga4_channel_daily_gorillasports_se`
WHERE hostname IN ('www.gorillasports.se', 'www.gorillasports.dk') AND d BETWEEN v_start AND slut
GROUP BY 1, 2 ORDER BY 2, 1;

-- 1. Per vecka och kanal: sessioner, köp och konvertering. Bara hela veckor (7 dagar).
WITH w AS (
  SELECT DATE_TRUNC(d, ISOWEEK) AS vecka, IF(hostname = 'www.gorillasports.dk', 'DK', 'SE') AS land, channel,
         COUNT(DISTINCT d) AS dagar, SUM(sessions) AS sessioner, SUM(purchases) AS kop
  FROM `PROJ.site_audit.ga4_channel_daily_gorillasports_se`
  WHERE hostname IN ('www.gorillasports.se', 'www.gorillasports.dk') AND d BETWEEN v_start AND slut
  GROUP BY 1, 2, 3
)
SELECT land, channel, vecka, sessioner, kop, ROUND(SAFE_DIVIDE(kop, sessioner) * 100, 2) AS konv_pct
FROM w WHERE vecka BETWEEN v_start AND v_sista AND land = 'SE'
ORDER BY channel, vecka;

-- 2. Källa/medium och kampanj som växte mest i sessioner per dag: 2026-10-12 och framåt mot 2026-09-07 till 2026-10-11.
WITH k AS (
  SELECT IF(hostname = 'www.gorillasports.dk', 'DK', 'SE') AS land, channel, source_medium, campaign, d, sessions, purchases
  FROM `PROJ.site_audit.ga4_channel_daily_gorillasports_se`
  WHERE hostname IN ('www.gorillasports.se', 'www.gorillasports.dk') AND d BETWEEN fore_start AND slut
), n AS (
  SELECT COUNT(DISTINCT IF(d >= spik_start, d, NULL)) AS dagar_spik, COUNT(DISTINCT IF(d < spik_start, d, NULL)) AS dagar_fore FROM k
)
SELECT land, channel, source_medium, campaign,
       ROUND(SUM(IF(d < spik_start, sessions, 0)) / ANY_VALUE(n.dagar_fore), 1) AS sess_dag_fore,
       ROUND(SUM(IF(d >= spik_start, sessions, 0)) / ANY_VALUE(n.dagar_spik), 1) AS sess_dag_spik,
       ROUND(SUM(IF(d >= spik_start, sessions, 0)) / ANY_VALUE(n.dagar_spik) - SUM(IF(d < spik_start, sessions, 0)) / ANY_VALUE(n.dagar_fore), 1) AS okning_per_dag,
       SUM(IF(d >= spik_start, purchases, 0)) AS kop_spik
FROM k CROSS JOIN n
WHERE land = 'SE'
GROUP BY land, channel, source_medium, campaign
ORDER BY okning_per_dag DESC
LIMIT 25;
