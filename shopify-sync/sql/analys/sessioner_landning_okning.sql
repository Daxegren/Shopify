-- Var landar sessionsökningen på gorillasports.se? GA4-sessioner och köp per landningssida (normaliserad sökväg), SE, senaste veckorna mot veckorna före.
-- Bakgrund: sessioner_kanal_vecka.sql 2026-10-28 visade att SE:s sessioner steg från cirka 6 000–7 000 till 11 000–12 000 per vecka veckorna 2026-10-12 och 2026-10-19, främst i kanalen Direct (cirka 137 till 651 sessioner per dag), medan köpen låg stilla.
-- GA4-tabellen per landningssida har ingen kanal-, enhets- eller landskolumn. Frågan kan därför inte dela upp Direct; den visar bara vilka landningssidor som växte. Är ökningen koncentrerad till en eller några sidor (till exempel startsidan eller en enskild produkt) säger det mer än när den är spridd.
-- Kolumner (verifierade mot src/site_audit/google_api.py GA4_SCHEMA): ga4_landing_daily_gorillasports_se(d, property_id, hostname, landing, sessions, purchases, revenue).
-- Perioder: SPIK = 2026-10-12 till och med senaste dag; FORE = 2026-09-07 till 2026-10-11. Jämförelsen är per dag, eftersom perioderna är olika långa.
-- Kör: sed 's/PROJ/gorilla-sports-data/g' sql/analys/sessioner_landning_okning.sql | bq query --use_legacy_sql=false --max_rows=100
-- Läs så här: en sida med stor ökning i sessioner och nästan inga köp är en kandidat för bottrafik, en felmärkt kampanj eller en spårningsändring. Det är ett fynd att undersöka, inget bevis.
-- Detta skript ändrar inget.

DECLARE fore_start DATE DEFAULT DATE '2026-09-07';
DECLARE spik_start DATE DEFAULT DATE '2026-10-12';
DECLARE slut DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 1 DAY);

-- 0. Kontroll: dagar per period och totala sessioner SE.
SELECT IF(d >= spik_start, 'spik', 'fore') AS period, COUNT(DISTINCT d) AS dagar, SUM(sessions) AS sessioner, SUM(purchases) AS kop,
       ROUND(SAFE_DIVIDE(SUM(sessions), COUNT(DISTINCT d))) AS sessioner_per_dag
FROM `PROJ.site_audit.ga4_landing_daily_gorillasports_se`
WHERE hostname = 'www.gorillasports.se' AND d BETWEEN fore_start AND slut
GROUP BY 1 ORDER BY 1 DESC;

-- 1. De 30 landningssidor som ökade mest i sessioner per dag.
WITH l AS (
  SELECT d, COALESCE(NULLIF(RTRIM(REGEXP_EXTRACT(landing, r'^([^?#]*)'), '/'), ''), '/') AS sida, sessions, purchases
  FROM `PROJ.site_audit.ga4_landing_daily_gorillasports_se`
  WHERE hostname = 'www.gorillasports.se' AND d BETWEEN fore_start AND slut
), n AS (
  SELECT COUNT(DISTINCT IF(d >= spik_start, d, NULL)) AS dagar_spik, COUNT(DISTINCT IF(d < spik_start, d, NULL)) AS dagar_fore FROM l
), a AS (
  SELECT sida,
         SUM(IF(d < spik_start, sessions, 0)) / ANY_VALUE(n.dagar_fore) AS s_fore, SUM(IF(d >= spik_start, sessions, 0)) / ANY_VALUE(n.dagar_spik) AS s_spik,
         SUM(IF(d >= spik_start, purchases, 0)) AS kop_spik, SUM(IF(d < spik_start, purchases, 0)) AS kop_fore
  FROM l CROSS JOIN n GROUP BY sida
)
SELECT sida, ROUND(s_fore, 1) AS sess_dag_fore, ROUND(s_spik, 1) AS sess_dag_spik, ROUND(s_spik - s_fore, 1) AS okning_per_dag,
       kop_fore, kop_spik, ROUND(SAFE_DIVIDE(kop_spik, s_spik * (SELECT dagar_spik FROM n)) * 100, 2) AS konv_spik_pct
FROM a ORDER BY (s_spik - s_fore) DESC LIMIT 30;

-- 2. Hur stor del av ökningen ligger på de 5 största sidorna? (Hög andel betyder koncentrerad ökning.)
WITH l AS (
  SELECT d, COALESCE(NULLIF(RTRIM(REGEXP_EXTRACT(landing, r'^([^?#]*)'), '/'), ''), '/') AS sida, sessions
  FROM `PROJ.site_audit.ga4_landing_daily_gorillasports_se`
  WHERE hostname = 'www.gorillasports.se' AND d BETWEEN fore_start AND slut
), n AS (
  SELECT COUNT(DISTINCT IF(d >= spik_start, d, NULL)) AS dagar_spik, COUNT(DISTINCT IF(d < spik_start, d, NULL)) AS dagar_fore FROM l
), a AS (
  SELECT sida, SUM(IF(d >= spik_start, sessions, 0)) / ANY_VALUE(n.dagar_spik) - SUM(IF(d < spik_start, sessions, 0)) / ANY_VALUE(n.dagar_fore) AS okning
  FROM l CROSS JOIN n GROUP BY sida
), r AS (SELECT okning, ROW_NUMBER() OVER (ORDER BY okning DESC) AS rang FROM a WHERE okning > 0)
SELECT ROUND(SUM(okning)) AS total_okning_per_dag_positiva_sidor, ROUND(SUM(IF(rang <= 5, okning, 0))) AS topp5, ROUND(SAFE_DIVIDE(SUM(IF(rang <= 5, okning, 0)), SUM(okning)) * 100, 1) AS topp5_andel_pct
FROM r;
