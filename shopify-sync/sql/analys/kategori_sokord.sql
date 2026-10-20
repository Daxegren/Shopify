-- Vilka sidor rankar på ett sökord i dag, och vilka närliggande sökningar finns? Underlag för att förbättra en kategorisida.
--
--   sed -e 's#GSCTABLE#gorilla-sports-data.site_audit.gsc_api_url_query_gorillasports_se#g' sql/analys/kategori_sokord.sql | bq query --use_legacy_sql=false --format=pretty
--
-- Byt sökorden i listan nedan. GSCTABLE måste ha kolumnerna data_date, url, query, clicks, impressions, sum_position.
-- Läsning: raderna av typen "sida" visar vilka adresser Google visar för sökordet (om det är en blogg eller en annan kategori än den
-- önskade är det ofta en kannibalisering eller en kategori som saknas); raderna av typen "fråga" visar vad besökarna egentligen skriver.
-- Anonymiserade sökfrågor saknas.

DECLARE since DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 90 DAY);

WITH kws AS (
  SELECT kw FROM UNNEST(['crosstrainer', 'motionscykel', 'ställbara hantlar']) AS kw
),
base AS (
  SELECT k.kw, g.query, g.url, SUM(g.impressions) AS impressions, SUM(g.clicks) AS clicks,
         SAFE_DIVIDE(SUM(g.sum_position), SUM(g.impressions)) + 1 AS position
  FROM `GSCTABLE` g
  JOIN kws k ON LOWER(g.query) LIKE CONCAT('%', k.kw, '%')
  WHERE g.data_date >= since
  GROUP BY 1, 2, 3
),
urls AS (
  SELECT kw, 'sida' AS typ, url AS varde, SUM(impressions) AS impressions, SUM(clicks) AS clicks,
         ROUND(SAFE_DIVIDE(SUM(position * impressions), SUM(impressions)), 1) AS position
  FROM base GROUP BY kw, url
  QUALIFY ROW_NUMBER() OVER (PARTITION BY kw ORDER BY SUM(impressions) DESC) <= 5
),
queries AS (
  SELECT kw, 'fråga' AS typ, query AS varde, SUM(impressions) AS impressions, SUM(clicks) AS clicks,
         ROUND(SAFE_DIVIDE(SUM(position * impressions), SUM(impressions)), 1) AS position
  FROM base GROUP BY kw, query
  QUALIFY ROW_NUMBER() OVER (PARTITION BY kw ORDER BY SUM(impressions) DESC) <= 12
)
SELECT * FROM urls
UNION ALL
SELECT * FROM queries
ORDER BY kw, typ, impressions DESC;
