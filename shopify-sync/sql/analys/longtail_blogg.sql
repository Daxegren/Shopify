-- Long tail-sökfrågor som kan bli blogginlägg (lågt hängande frukt), ur Search Console. Bara läsning.
--
-- Körning (byt tabell och varumärkesord):
--   sed -e 's/PROJ/gorilla-sports-data/g' \
--       -e 's#GSCTABLE#gorilla-sports-data.site_audit.gsc_combined_gorillasports_se#g' \
--       -e 's#BRANDRE#gorilla|gorillasports#g' \
--       sql/analys/longtail_blogg.sql | bq query --use_legacy_sql=false --max_rows=200
-- BRANDRE är ett regex med varumärkesord som ska uteslutas (Best of Sports: 'best of sports|bestofsports').
--
-- Definitioner:
--   long tail      = minst 4 ord i sökfrågan
--   position       = visningsviktat snitt, 6 till 40 (inte redan i toppen, men inom räckhåll)
--   stadium        = See-Think-Do-Care, klassat med nyckelord (sv, da, fi, en); träffar i ordning care, do, think, see
--   sidtyp         = artikel (/blogs/), kategori (/collections/), produkt (/products/), annat
--   åtgärd         = 'ny artikel' (See/Think, bästa sidan är inte en artikel), 'förbättra artikel' (artikel på position över 10),
--                    annars 'ingen blogg' (köpfrågor går till kategori och produkt, care till support)
-- Begränsningar: anonymiserade sökfrågor (cirka en tredjedel av visningarna) saknas. Stadiet är en nyckelordsgissning som ska granskas.
-- Små volymer: en fråga med 10 visningar på 90 dagar är en indikation på ämnet, inte en prognos. Gruppera gärna efter ämne innan artiklar skrivs.

DECLARE since DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 90 DAY);
DECLARE min_visningar INT64 DEFAULT 10;

CREATE TEMP TABLE q AS
SELECT query, url,
       SUM(impressions) AS visningar, SUM(clicks) AS klick,
       SAFE_DIVIDE(SUM(sum_position), SUM(impressions)) + 1 AS position
FROM `GSCTABLE`
WHERE data_date >= since AND query IS NOT NULL AND NOT IFNULL(is_anonymized_query, FALSE)
  AND NOT REGEXP_CONTAINS(LOWER(query), r'BRANDRE')
  AND ARRAY_LENGTH(SPLIT(TRIM(query), ' ')) >= 4
GROUP BY 1, 2;

CREATE TEMP TABLE kand AS
WITH per_fraga AS (
  SELECT query, SUM(visningar) AS visningar, SUM(klick) AS klick,
         SAFE_DIVIDE(SUM(position * visningar), SUM(visningar)) AS position,
         ARRAY_AGG(STRUCT(url, visningar) ORDER BY visningar DESC LIMIT 1)[OFFSET(0)].url AS basta_sida
  FROM q GROUP BY 1
)
SELECT query, visningar, klick, ROUND(position, 1) AS position, basta_sida,
       CASE WHEN REGEXP_CONTAINS(basta_sida, r'/blogs/') THEN 'artikel'
            WHEN REGEXP_CONTAINS(basta_sida, r'/collections/') THEN 'kategori'
            WHEN REGEXP_CONTAINS(basta_sida, r'/products/') THEN 'produkt' ELSE 'annat' END AS sidtyp,
       CASE WHEN REGEXP_CONTAINS(LOWER(query), r'\b(montera|montering|monteringsanvisning|instruktion|manual|garanti|reservdel|rengöra|underhåll|justera|fungerar inte|montering|vejledning|reservedel|rengøring|vedligehold|kokoaminen|ohje|takuu|varaosa|huolto)\b') THEN 'care'
            WHEN REGEXP_CONTAINS(LOWER(query), r'\b(köp|köpa|pris|billig|billigaste|rea|erbjudande|beställ|butik|kampanj|køb|tilbud|bestil|osta|hinta|halpa|tarjous|tilaa)\b') THEN 'do'
            WHEN REGEXP_CONTAINS(LOWER(query), r'\b(bäst|bästa|jämför|jämförelse|vs|kontra|test|recension|omdöme|alternativ|skillnad|vilken|vilket|för- och nackdelar|bedst|bedste|sammenlign|anmeldelse|forskel|hvilken|paras|vertailu|testi|arvostelu|ero|mikä)\b') THEN 'think'
            ELSE 'see' END AS stadium
FROM per_fraga
WHERE visningar >= min_visningar AND position BETWEEN 6 AND 40;

-- 1. Kandidater, mest visade först
SELECT query AS sokfraga, visningar, klick, position, stadium, sidtyp, basta_sida,
       CASE WHEN stadium IN ('see', 'think') AND sidtyp <> 'artikel' THEN 'ny artikel'
            WHEN stadium IN ('see', 'think') AND sidtyp = 'artikel' AND position > 10 THEN 'förbättra artikel'
            ELSE 'ingen blogg' END AS atgard
FROM kand
ORDER BY (stadium IN ('see', 'think')) DESC, visningar DESC
LIMIT 150;

-- 2. Sammanfattning: hur många frågor och visningar per stadium och sidtyp
SELECT stadium, sidtyp, COUNT(*) AS fragor, SUM(visningar) AS visningar, SUM(klick) AS klick, ROUND(AVG(position), 1) AS snittposition
FROM kand GROUP BY 1, 2 ORDER BY stadium, visningar DESC;
