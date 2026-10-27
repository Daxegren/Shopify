-- Vilka rabattkoder (och automatiska rabatter) bär rabatten på Gorilla Sports? Senaste 28 dagarna mot de 28 före, per marknad.
-- Bakgrund: rabatten är tre gånger så stor som i fjol i Shopifys egen analys (beslut-2026-10-14.md, 10,5 % mot 3,2 % av bruttoförsäljningen) och i SE
-- låg den på 10,1 % och 11,7 % av ordervärdet i omsattning_30d (resultat 2026-10-13). Frågan är vilka koder som står för den, inte om den är lönsam.
--
--   sed 's/PROJ/gorilla-sports-data/g' sql/analys/rabatter_koder.sql | bq query --use_legacy_sql=false --max_rows=100
--
-- Bara läsning. Källor: PROJ.shopify.orders (created_at, cancelled_at, presentment_currency, subtotal_price, total_discounts, discount_codes).
-- discount_codes är en kommaseparerad sträng (src/shopify_sync/transform.py, _join). NULL betyder ingen kod. Belopp ligger i butikens valuta (SEK) för
-- båda marknaderna (total_discounts och subtotal_price, som i omsattning_30d.sql), så procenttalen är jämförbara men beloppen visar SEK, inte DKK.
--
-- Så här läser du resultaten
--   * Rabatt i procent = total_discounts / (subtotal_price + total_discounts), samma definition som omsattning_30d.sql.
--   * Hamnar en order med flera koder räknas rabatten hos varje kod (summan över koder blir större än totalen). ordrar_med_flera_koder visar hur ofta.
--   * "(automatisk rabatt utan kod)" = order med total_discounts > 0 utan kod (till exempel butikens egna automatiska rabatter).
--   * Detta visar hur mycket rabatt som getts och till vem. Det visar inte om rabatten gett merförsäljning eller bara sänkt priset på köp som ändå skulle ha skett.
--     Det kräver en jämförelse som inte går att göra ur de här tabellerna.
--   * Orderhistoriken i BigQuery kan vara kortare än 56 dagar. Då saknas den äldre perioden (se orderdata_fran).

DECLARE idag DATE DEFAULT CURRENT_DATE('Europe/Stockholm');
DECLARE o_forsta DATE DEFAULT (SELECT MIN(DATE(created_at, 'Europe/Stockholm')) FROM `PROJ.shopify.orders`);
DECLARE p1_slut DATE DEFAULT DATE_SUB(idag, INTERVAL 1 DAY);
DECLARE p1_start DATE DEFAULT DATE_SUB(p1_slut, INTERVAL 27 DAY);
DECLARE p0_slut DATE DEFAULT DATE_SUB(p1_start, INTERVAL 1 DAY);
DECLARE p0_start DATE DEFAULT DATE_SUB(p0_slut, INTERVAL 27 DAY);

CREATE TEMP TABLE o AS
SELECT id,
       IF(DATE(created_at, 'Europe/Stockholm') BETWEEN p1_start AND p1_slut, 'nu', 'fore') AS period,
       CASE presentment_currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE presentment_currency END AS marknad,
       subtotal_price, total_discounts,
       IF(discount_codes IS NULL OR discount_codes = '',
          IF(total_discounts > 0, '(automatisk rabatt utan kod)', '(ingen rabatt)'),
          discount_codes) AS koder,
       discount_codes IS NOT NULL AND discount_codes != '' AS har_kod
FROM `PROJ.shopify.orders`
WHERE cancelled_at IS NULL AND DATE(created_at, 'Europe/Stockholm') BETWEEN p0_start AND p1_slut;

-- 0. Datakontroll
SELECT o_forsta AS orderdata_fran, p0_start AS fore_fran, p0_slut AS fore_till, p1_start AS nu_fran, p1_slut AS nu_till,
       (SELECT COUNT(*) FROM o WHERE marknad NOT IN ('SE', 'DK')) AS ordrar_andra_valutor;

-- 1. Översikt per marknad och period: hur många ordrar har en kod, hur många har någon rabatt alls, och hur stor rabatten är i procent av ordervärdet före rabatt.
SELECT marknad, period, COUNT(*) AS ordrar,
       ROUND(COUNTIF(har_kod) / COUNT(*) * 100, 1) AS andel_med_kod_pct,
       ROUND(COUNTIF(total_discounts > 0) / COUNT(*) * 100, 1) AS andel_med_nagon_rabatt_pct,
       ROUND(SUM(total_discounts)) AS rabatt_sek,
       ROUND(SAFE_DIVIDE(SUM(total_discounts), SUM(subtotal_price + total_discounts)) * 100, 1) AS rabatt_pct_av_ordervarde
FROM o WHERE marknad IN ('SE', 'DK')
GROUP BY 1, 2 ORDER BY 1, 2 DESC;

-- 2. De 12 koder per marknad som hade flest ordrar de senaste 28 dagarna, med samma kod 28 dagar före. Rabatt i SEK är hela orderns rabatt (se kommentaren överst).
WITH per_kod AS (
  SELECT marknad, TRIM(kod) AS kod, period, COUNT(*) AS ordrar, SUM(total_discounts) AS rabatt,
         COUNTIF(ARRAY_LENGTH(SPLIT(koder, ',')) > 1) AS flera_koder
  FROM o, UNNEST(SPLIT(koder, ',')) AS kod
  WHERE marknad IN ('SE', 'DK')
  GROUP BY 1, 2, 3
), piv AS (
  SELECT marknad, kod,
         SUM(IF(period = 'nu', ordrar, 0)) AS ordrar_nu, SUM(IF(period = 'fore', ordrar, 0)) AS ordrar_fore,
         ROUND(SUM(IF(period = 'nu', rabatt, 0))) AS rabatt_sek_nu, ROUND(SUM(IF(period = 'fore', rabatt, 0))) AS rabatt_sek_fore,
         SUM(IF(period = 'nu', flera_koder, 0)) AS ordrar_med_flera_koder_nu
  FROM per_kod GROUP BY 1, 2
)
SELECT * FROM (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY marknad ORDER BY ordrar_nu DESC, ordrar_fore DESC) AS rang FROM piv
  WHERE kod != '(ingen rabatt)'
) WHERE rang <= 12 ORDER BY marknad, rang;
