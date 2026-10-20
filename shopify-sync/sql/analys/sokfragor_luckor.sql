-- Frågor och köpguide-sökningar som sajten visas för men tar få klick på, med den sida som redan rankar.
-- Idé: hitta sidor som redan har synlighet och lägg ett kort, tydligt svar högt upp på dem.
--
--   sed -e 's/PROJ/gorilla-sports-data/g' -e 's#GSCTABLE#gorilla-sports-data.searchconsole.searchdata_url_impression#g' \
--       sql/analys/sokfragor_luckor.sql | bq query --use_legacy_sql=false
--
-- GSCTABLE måste innehålla kolumnerna data_date, url, query, clicks, impressions, sum_position (bulkexporten har dem; API-tabellen
-- gsc_api_url_query_<sajt> också). Frågeord med ordgräns undviker falska träffar (kanin, skateboard). Flera språk: sv, da, fi, en.
-- Läsning: "klickgap" är klick som uppnåtts mot vad positionen normalt ger. Position 4–15 med många visningar är mest värd att arbeta med.
-- Sökfrågor som Google döljer (anonymiserade) saknas. Förväntad CTR per position är en grov tumregel, inte en mätning av just den här sajten.

DECLARE since DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 90 DAY);

WITH q AS (
  SELECT query, url,
         SUM(impressions) AS impressions, SUM(clicks) AS clicks,
         SAFE_DIVIDE(SUM(sum_position), SUM(impressions)) + 1 AS position
  FROM `GSCTABLE`
  WHERE data_date >= since AND query IS NOT NULL
    AND REGEXP_CONTAINS(LOWER(query),
        r'^(hur|vad|varför|vilken|vilket|vilka|kan|ska|bör|hvordan|hvad|hvorfor|hvilken|hvilke|skal|miten|mitä|miksi|mikä|mitkä|how|what|why|which|can|should)\s|\b(bäst|bästa|billig|billigaste|jämför|kontra|vs|test|storlek|guide|bedst|paras)\b')
  GROUP BY 1, 2
),
best AS (
  SELECT query, ARRAY_AGG(STRUCT(url, impressions, clicks, position) ORDER BY impressions DESC LIMIT 1)[OFFSET(0)] AS top
  FROM q GROUP BY 1
)
SELECT query, top.url, top.impressions, top.clicks, ROUND(top.position, 1) AS position,
       ROUND(SAFE_DIVIDE(top.clicks, top.impressions) * 100, 2) AS ctr_pct,
       ROUND(top.impressions * CASE WHEN top.position <= 1.5 THEN 0.28 WHEN top.position <= 2.5 THEN 0.15 WHEN top.position <= 3.5 THEN 0.10
         WHEN top.position <= 5.5 THEN 0.06 WHEN top.position <= 10.5 THEN 0.025 WHEN top.position <= 15.5 THEN 0.01 ELSE 0.004 END - top.clicks, 0) AS klickgap
FROM best
WHERE top.impressions >= 50 AND top.position BETWEEN 3.5 AND 20
ORDER BY klickgap DESC
LIMIT 100;
