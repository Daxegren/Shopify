-- GEO: kommer besökare från AI-tjänster (ChatGPT, Perplexity, Gemini, Copilot, Claude med flera), och köper de?
-- Svarar på: syns sajten i AI-svar så att det ger trafik, och hur stor del är det av allt?
--
--   sed -e 's/PROJ/gorilla-sports-data/g' -e 's/KEY/bestofsports/g' sql/analys/ai_hanvisningar.sql | bq query --use_legacy_sql=false
--
-- Källa: GA4-kanaltabellen (ga4_channel_daily_KEY). Siffrorna är små och osäkra: många AI-besök syns som Direct eftersom
-- tjänsterna ofta inte skickar någon hänvisning. Läs det som en nedre gräns och följ trenden, inte nivån.
DECLARE since DATE DEFAULT DATE_SUB(CURRENT_DATE('Europe/Stockholm'), INTERVAL 90 DAY);

WITH k AS (
  SELECT d, hostname, source_medium, sessions, purchases, revenue,
         REGEXP_CONTAINS(LOWER(source_medium),
           r'chatgpt|openai|perplexity|gemini|bard\.google|copilot|claude\.ai|anthropic|you\.com|phind|poe\.com|meta\.ai|deepseek|mistral|grok') AS ai
  FROM `PROJ.site_audit.ga4_channel_daily_KEY`
  WHERE d >= since
)
SELECT hostname,
       SUM(sessions) AS besok_totalt,
       SUMIF(sessions, ai) AS besok_fran_ai,
       ROUND(SAFE_DIVIDE(SUMIF(sessions, ai), SUM(sessions)) * 100, 2) AS ai_andel_pct,
       SUMIF(purchases, ai) AS kop_fran_ai,
       ARRAY_TO_STRING(ARRAY_AGG(DISTINCT IF(ai, source_medium, NULL) IGNORE NULLS LIMIT 8), ' | ') AS kallor
FROM k GROUP BY 1 ORDER BY besok_totalt DESC;
