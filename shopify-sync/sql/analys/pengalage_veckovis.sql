-- Pengaläget för Gorilla Sports, vecka för vecka och marknad (SE och DK): försäljning, trafik, annonser och kanaler.
-- Ett skript med en liten datakontroll och fyra resultat (cirka 60 rader totalt) som går att klistra in i ett meddelande.
--
--   sed 's/PROJ/gorilla-sports-data/g' sql/analys/pengalage_veckovis.sql | bq query --use_legacy_sql=false --max_rows=100
--
-- Belopp ligger i marknadens valuta (SE i SEK, DK i DKK) och summeras aldrig över marknader. Kolumnerna står därför sida vid sida
-- per marknad (se_… och dk_…). Bara läsning. Inget ändras i butik, annonskonto eller Google Cloud.
--
-- Källor (tabell- och kolumnnamn som redan används i omsattning_30d.sql, cos_30d.sql och annonser_kampanjer_30d.sql):
--   PROJ.shopify.orders                              created_at, cancelled_at, presentment_currency, total_price_presentment, source_name,
--                                                    last_visit_utm_source, last_visit_source
--   PROJ.site_audit.ga4_landing_daily_gorillasports_se   d, hostname, sessions, purchases      (SE och DK, skiljs på hostname)
--   PROJ.site_audit.google_ads_daily_gorillasports_se    d, currency, cost, conversions_value
--   PROJ.site_audit.meta_ads_daily_gorillasports_se      d, currency, spend, purchase_value
--
-- Så här läser du resultaten
--   NULL betyder att datakällan inte täcker hela veckan (eller de 28 dagarna). Det betyder inte noll. Ordrarna i BigQuery sträcker sig
--   bara så långt bakåt som synken har hämtat (läs "orderdata_fran" i datakontrollen; Shopify lämnar annars bara ut 60 dagars ordrar),
--   GA4 börjar 2026-03-19/20 och annonstabellerna omkring 2026-07-01. Hela veckor räknas måndag till söndag, svensk tid.
--   Plattformens värde (Google respektive Meta) är plattformens egen tillskrivning. Det är inte butikens omsättning, och Google och Meta
--   räknar delvis samma köp, så de två ska inte läggas ihop.
--   Alla jämförelser här visar samband. De visar inte orsak.

DECLARE idag DATE DEFAULT CURRENT_DATE('Europe/Stockholm');
DECLARE o_forsta DATE DEFAULT (SELECT MIN(DATE(created_at, 'Europe/Stockholm')) FROM `PROJ.shopify.orders`);
DECLARE ga_forsta DATE DEFAULT (SELECT MIN(d) FROM `PROJ.site_audit.ga4_landing_daily_gorillasports_se`);
DECLARE ga_sista DATE DEFAULT (SELECT MAX(d) FROM `PROJ.site_audit.ga4_landing_daily_gorillasports_se`);
DECLARE g_forsta DATE DEFAULT (SELECT MIN(d) FROM `PROJ.site_audit.google_ads_daily_gorillasports_se`);
DECLARE g_sista DATE DEFAULT (SELECT MAX(d) FROM `PROJ.site_audit.google_ads_daily_gorillasports_se`);
DECLARE m_forsta DATE DEFAULT (SELECT MIN(d) FROM `PROJ.site_audit.meta_ads_daily_gorillasports_se`);
DECLARE m_sista DATE DEFAULT (SELECT MAX(d) FROM `PROJ.site_audit.meta_ads_daily_gorillasports_se`);

-- Veckor: de 12 senaste hela veckorna. v_forsta och v_sista är måndagen i första respektive sista veckan.
DECLARE v_forsta DATE DEFAULT DATE_SUB(DATE_TRUNC(idag, ISOWEEK), INTERVAL 12 WEEK);
DECLARE v_sista DATE DEFAULT DATE_SUB(DATE_TRUNC(idag, ISOWEEK), INTERVAL 1 WEEK);

-- Jämförelseperioder (del d): n_dagar dagar som slutar den senaste dag som alla källor täcker (högst i går), de n_dagar dagarna före,
-- och samma kalenderdatum ett år tidigare.
DECLARE n_dagar INT64 DEFAULT 28;
DECLARE p1_slut DATE DEFAULT LEAST(DATE_SUB(idag, INTERVAL 1 DAY), ga_sista, g_sista, m_sista);
DECLARE p1_start DATE DEFAULT DATE_SUB(p1_slut, INTERVAL (n_dagar - 1) DAY);
DECLARE p0_slut DATE DEFAULT DATE_SUB(p1_start, INTERVAL 1 DAY);
DECLARE p0_start DATE DEFAULT DATE_SUB(p0_slut, INTERVAL (n_dagar - 1) DAY);
DECLARE f1_slut DATE DEFAULT DATE_SUB(p1_slut, INTERVAL 1 YEAR);
DECLARE f1_start DATE DEFAULT DATE_SUB(p1_start, INTERVAL 1 YEAR);
DECLARE spine_start DATE DEFAULT LEAST(v_forsta, f1_start);

-- Ordrar utan annullerade. Samma urval som omsattning_30d.sql. Kanalen är samma uttryck som i den filen (avsnitt 4);
-- kanalgruppen är en ny gruppering ovanpå (se nedan).
CREATE TEMP TABLE o AS
SELECT DATE(created_at, 'Europe/Stockholm') AS d,
       DATE_TRUNC(DATE(created_at, 'Europe/Stockholm'), ISOWEEK) AS vecka,
       CASE presentment_currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE presentment_currency END AS marknad,
       source_name, total_price_presentment,
       COALESCE(NULLIF(last_visit_utm_source, ''), NULLIF(last_visit_source, ''), source_name, 'okänd') AS kanal
FROM `PROJ.shopify.orders`
WHERE cancelled_at IS NULL AND DATE(created_at, 'Europe/Stockholm') BETWEEN spine_start AND DATE_SUB(idag, INTERVAL 1 DAY);

-- En rad per dag och marknad. NULL där källan inte täcker dagen (se kommentaren överst).
CREATE TEMP TABLE dag AS
WITH sp AS (
  SELECT d, mk AS marknad
  FROM UNNEST(GENERATE_DATE_ARRAY(spine_start, DATE_SUB(idag, INTERVAL 1 DAY))) AS d
  CROSS JOIN UNNEST(['SE', 'DK']) AS mk
), ord AS (
  SELECT d, marknad, COUNT(*) AS ordrar, COUNTIF(source_name = 'shopify_draft_order') AS utkast,
         CAST(SUM(total_price_presentment) AS FLOAT64) AS oms
  FROM o GROUP BY 1, 2
), ga AS (
  SELECT d, CASE hostname WHEN 'www.gorillasports.se' THEN 'SE' WHEN 'www.gorillasports.dk' THEN 'DK' END AS marknad,
         SUM(sessions) AS sessioner, SUM(purchases) AS kop
  FROM `PROJ.site_audit.ga4_landing_daily_gorillasports_se`
  WHERE hostname IN ('www.gorillasports.se', 'www.gorillasports.dk')
  GROUP BY 1, 2
), g AS (
  SELECT d, CASE currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE currency END AS marknad,
         SUM(cost) AS kost, SUM(conversions_value) AS varde
  FROM `PROJ.site_audit.google_ads_daily_gorillasports_se` GROUP BY 1, 2
), m AS (
  SELECT d, CASE currency WHEN 'SEK' THEN 'SE' WHEN 'DKK' THEN 'DK' ELSE currency END AS marknad,
         SUM(spend) AS kost, SUM(purchase_value) AS varde
  FROM `PROJ.site_audit.meta_ads_daily_gorillasports_se` GROUP BY 1, 2
)
SELECT sp.d, sp.marknad,
       IF(sp.d >= o_forsta, IFNULL(ord.ordrar, 0), NULL) AS ordrar,
       IF(sp.d >= o_forsta, IFNULL(ord.utkast, 0), NULL) AS utkast,
       IF(sp.d >= o_forsta, IFNULL(ord.oms, 0), NULL) AS oms,
       IF(sp.d BETWEEN ga_forsta AND ga_sista, IFNULL(ga.sessioner, 0), NULL) AS sessioner,
       IF(sp.d BETWEEN ga_forsta AND ga_sista, IFNULL(ga.kop, 0), NULL) AS kop,
       IF(sp.d BETWEEN g_forsta AND g_sista, IFNULL(CAST(g.kost AS FLOAT64), 0), NULL) AS g_kost,
       IF(sp.d BETWEEN g_forsta AND g_sista, IFNULL(CAST(g.varde AS FLOAT64), 0), NULL) AS g_varde,
       IF(sp.d BETWEEN m_forsta AND m_sista, IFNULL(CAST(m.kost AS FLOAT64), 0), NULL) AS m_kost,
       IF(sp.d BETWEEN m_forsta AND m_sista, IFNULL(CAST(m.varde AS FLOAT64), 0), NULL) AS m_varde
FROM sp
LEFT JOIN ord ON ord.d = sp.d AND ord.marknad = sp.marknad
LEFT JOIN ga ON ga.d = sp.d AND ga.marknad = sp.marknad
LEFT JOIN g ON g.d = sp.d AND g.marknad = sp.marknad
LEFT JOIN m ON m.d = sp.d AND m.marknad = sp.marknad;

-- Veckosummor. En vecka får ett värde bara om alla sju dagar täcks av källan (annars NULL).
CREATE TEMP TABLE vk AS
SELECT DATE_TRUNC(d, ISOWEEK) AS vecka, marknad,
       IF(COUNT(ordrar) = 7, SUM(ordrar), NULL) AS ordrar,
       IF(COUNT(utkast) = 7, SUM(utkast), NULL) AS utkast,
       IF(COUNT(oms) = 7, SUM(oms), NULL) AS oms,
       IF(COUNT(sessioner) = 7, SUM(sessioner), NULL) AS sessioner,
       IF(COUNT(kop) = 7, SUM(kop), NULL) AS kop,
       IF(COUNT(g_kost) = 7, SUM(g_kost), NULL) AS g_kost,
       IF(COUNT(g_varde) = 7, SUM(g_varde), NULL) AS g_varde,
       IF(COUNT(m_kost) = 7, SUM(m_kost), NULL) AS m_kost,
       IF(COUNT(m_varde) = 7, SUM(m_varde), NULL) AS m_varde
FROM dag
WHERE d BETWEEN v_forsta AND DATE_ADD(v_sista, INTERVAL 6 DAY)
GROUP BY 1, 2;

-- 0. Datakontroll: hur långt bakåt och framåt varje källa räcker, och vilka perioder del d använder. Läs den först.
--    orderdata_fran = äldsta order i tabellen. ordrar_andra_valutor ska vara 0 (annars saknas en marknad i resultaten).
SELECT o_forsta AS orderdata_fran, ga_forsta AS ga4_fran, ga_sista AS ga4_till, g_forsta AS google_fran, g_sista AS google_till,
       m_forsta AS meta_fran, m_sista AS meta_till,
       (SELECT COUNT(*) FROM o WHERE marknad NOT IN ('SE', 'DK')) AS ordrar_andra_valutor,
       p1_start AS nu_fran, p1_slut AS nu_till, p0_start AS fore_fran, p0_slut AS fore_till, f1_start AS fjol_fran, f1_slut AS fjol_till;

-- a. Försäljning per vecka och marknad: ordrar, varav utkastsordrar (source_name = shopify_draft_order, oftast värde 0), omsättning och snittorder.
--    Snittorder = omsättning / ordrar, alltså med utkasten medräknade (samma definition som omsattning_30d.sql). Utkasten drar ner snittet.
--    Läs: fallet i ordrar, inte i snittordern, är det som förklarade nedgången i september (omsattning_30d, 2026-10-13).
SELECT vecka,
       MAX(IF(marknad = 'SE', ordrar, NULL)) AS se_ordrar, MAX(IF(marknad = 'SE', utkast, NULL)) AS se_utkast,
       ROUND(MAX(IF(marknad = 'SE', oms, NULL))) AS se_oms, ROUND(MAX(IF(marknad = 'SE', SAFE_DIVIDE(oms, ordrar), NULL))) AS se_snittorder,
       MAX(IF(marknad = 'DK', ordrar, NULL)) AS dk_ordrar, MAX(IF(marknad = 'DK', utkast, NULL)) AS dk_utkast,
       ROUND(MAX(IF(marknad = 'DK', oms, NULL))) AS dk_oms, ROUND(MAX(IF(marknad = 'DK', SAFE_DIVIDE(oms, ordrar), NULL))) AS dk_snittorder
FROM vk GROUP BY vecka ORDER BY vecka;

-- b. Trafik och annonser per vecka och marknad. Sessioner, köp och konvertering kommer från GA4 (köp enligt GA4, inte Shopify).
--    Kostnad och värde per plattform (G = Google Ads, M = Meta) i marknadens valuta. ROAS = värde / kostnad.
--    Läs: sjunker sessionerna (trafik) eller konverteringen (andel som köper), och följer kostnaden efter? Om kostnaden sjunker medan
--    ROAS faller är det inte "mindre annonsering" ensamt som förklarar tappet.
SELECT vecka,
       MAX(IF(marknad = 'SE', sessioner, NULL)) AS se_sessioner, MAX(IF(marknad = 'SE', kop, NULL)) AS se_kop,
       ROUND(MAX(IF(marknad = 'SE', SAFE_DIVIDE(kop, sessioner), NULL)) * 100, 2) AS se_konv_pct,
       ROUND(MAX(IF(marknad = 'SE', g_kost, NULL))) AS se_g_kost, ROUND(MAX(IF(marknad = 'SE', g_varde, NULL))) AS se_g_varde,
       ROUND(MAX(IF(marknad = 'SE', m_kost, NULL))) AS se_m_kost, ROUND(MAX(IF(marknad = 'SE', m_varde, NULL))) AS se_m_varde,
       MAX(IF(marknad = 'DK', sessioner, NULL)) AS dk_sessioner, MAX(IF(marknad = 'DK', kop, NULL)) AS dk_kop,
       ROUND(MAX(IF(marknad = 'DK', SAFE_DIVIDE(kop, sessioner), NULL)) * 100, 2) AS dk_konv_pct,
       ROUND(MAX(IF(marknad = 'DK', g_kost, NULL))) AS dk_g_kost, ROUND(MAX(IF(marknad = 'DK', g_varde, NULL))) AS dk_g_varde,
       ROUND(MAX(IF(marknad = 'DK', m_kost, NULL))) AS dk_m_kost, ROUND(MAX(IF(marknad = 'DK', m_varde, NULL))) AS dk_m_varde
FROM vk GROUP BY vecka ORDER BY vecka;

-- c. Ordrar och omsättning per kanalgrupp, vecka och marknad (omsättning i marknadens valuta).
--    Kanalen är Shopifys senaste besök: utm_source, annars besökskälla, annars ordens source_name (samma uttryck som omsattning_30d.sql, avsnitt 4).
--    Det finns ingen gruppering i de tidigare resultatfilerna; den här är ny och bygger på de värden som syntes där:
--      google          = värden som börjar på "google" (Google, google). Innehåller BÅDE betald och organisk Google-trafik: Shopify skiljer inte här.
--      meta            = facebook, Facebook, instagram, fb, ig, meta (bara facebook och Facebook syntes i tidigare resultat)
--      direkt          = direct
--      epost_affiliate = adtraction, kelkoose, pricerunner (affiliate och jämförelsetjänster) samt klaviyo, email, newsletter, nyhetsbrev, epost.
--                        Inga e-postvärden syntes i tidigare resultat och Klaviyo är inte kopplat för Gorilla (klaviyo_enabled saknas i sites.toml),
--                        så e-post är sannolikt osynlig här.
--      ovrigt          = allt annat. Störst är "web" (butikens egna beställningar utan registrerad källa), men även shopify_draft_order,
--                        chatgpt.com, Bing, adresser som https://www.gorillasports.dk/ (egen sajt som hänvisare) och okänd. Kolumnen ovrigt_web_ordrar visar "web".
--    Läs: vilken grupp faller mest i omsättning? Jämför med del b (annonskostnad). Gruppen "google" kan inte skiljas från Google Ads utan GA4-kanaltabellen.
--    ordrar_totalt ska vara lika med motsvarande vecka i del a.
WITH g AS (
  SELECT vecka, marknad, total_price_presentment,
         CASE WHEN REGEXP_CONTAINS(LOWER(kanal), r'^google') THEN 'google'
              WHEN REGEXP_CONTAINS(LOWER(kanal), r'^(facebook|instagram)') OR LOWER(kanal) IN ('fb', 'ig', 'meta') THEN 'meta'
              WHEN LOWER(kanal) = 'direct' THEN 'direkt'
              WHEN LOWER(kanal) IN ('adtraction', 'kelkoose', 'pricerunner')
                   OR REGEXP_CONTAINS(LOWER(kanal), r'^(klaviyo|email|e-mail|newsletter|nyhetsbrev|epost)') THEN 'epost_affiliate'
              ELSE 'ovrigt' END AS grupp,
         LOWER(kanal) = 'web' AS ar_web
  FROM o WHERE marknad IN ('SE', 'DK') AND vecka BETWEEN v_forsta AND v_sista
), agg AS (
  SELECT vecka, marknad, COUNT(*) AS ordrar_totalt,
         COUNTIF(grupp = 'google') AS google_o, CAST(SUM(IF(grupp = 'google', total_price_presentment, 0)) AS FLOAT64) AS google_s,
         COUNTIF(grupp = 'meta') AS meta_o, CAST(SUM(IF(grupp = 'meta', total_price_presentment, 0)) AS FLOAT64) AS meta_s,
         COUNTIF(grupp = 'direkt') AS direkt_o, CAST(SUM(IF(grupp = 'direkt', total_price_presentment, 0)) AS FLOAT64) AS direkt_s,
         COUNTIF(grupp = 'epost_affiliate') AS epaff_o, CAST(SUM(IF(grupp = 'epost_affiliate', total_price_presentment, 0)) AS FLOAT64) AS epaff_s,
         COUNTIF(grupp = 'ovrigt') AS ovr_o, CAST(SUM(IF(grupp = 'ovrigt', total_price_presentment, 0)) AS FLOAT64) AS ovr_s,
         COUNTIF(ar_web) AS web_o
  FROM g GROUP BY 1, 2
), sp AS (
  SELECT v AS vecka, mk AS marknad
  FROM UNNEST(GENERATE_DATE_ARRAY(v_forsta, v_sista, INTERVAL 1 WEEK)) AS v CROSS JOIN UNNEST(['SE', 'DK']) AS mk
)
SELECT sp.vecka, sp.marknad,
       IF(sp.vecka >= o_forsta, IFNULL(a.ordrar_totalt, 0), NULL) AS ordrar_totalt,
       IF(sp.vecka >= o_forsta, IFNULL(a.google_o, 0), NULL) AS google_ordrar, ROUND(IF(sp.vecka >= o_forsta, IFNULL(a.google_s, 0), NULL)) AS google_oms,
       IF(sp.vecka >= o_forsta, IFNULL(a.meta_o, 0), NULL) AS meta_ordrar, ROUND(IF(sp.vecka >= o_forsta, IFNULL(a.meta_s, 0), NULL)) AS meta_oms,
       IF(sp.vecka >= o_forsta, IFNULL(a.direkt_o, 0), NULL) AS direkt_ordrar, ROUND(IF(sp.vecka >= o_forsta, IFNULL(a.direkt_s, 0), NULL)) AS direkt_oms,
       IF(sp.vecka >= o_forsta, IFNULL(a.epaff_o, 0), NULL) AS epost_aff_ordrar, ROUND(IF(sp.vecka >= o_forsta, IFNULL(a.epaff_s, 0), NULL)) AS epost_aff_oms,
       IF(sp.vecka >= o_forsta, IFNULL(a.ovr_o, 0), NULL) AS ovrigt_ordrar, ROUND(IF(sp.vecka >= o_forsta, IFNULL(a.ovr_s, 0), NULL)) AS ovrigt_oms,
       IF(sp.vecka >= o_forsta, IFNULL(a.web_o, 0), NULL) AS ovrigt_web_ordrar
FROM sp LEFT JOIN agg a ON a.vecka = sp.vecka AND a.marknad = sp.marknad
ORDER BY sp.vecka, sp.marknad;

-- d. Tre jämförelseperioder per marknad och mått: nu (senaste n_dagar dagarna), före (n_dagar dagarna innan) och fjol (samma kalenderdatum förra året).
--    Perioderna står i datakontrollen ovan. Ett värde visas bara om alla dagar i perioden täcks av källan, annars NULL och ingen procent.
--    Fjolåret är sannolikt NULL: orderhistoriken räcker inte så långt och GA4 börjar mars 2026 (beslut-2026-10-12-2.md, beslut-2026-10-18-10.md).
--    Då hänvisas till Shopifys egen analys (beslut-2026-10-14.md) eller Search Console.
--    konvertering_ga4_pct = GA4-köp / GA4-sessioner. mer = butikens omsättning / (Google- + Metakostnad), alltså omsättning per annonskrona
--    (samma mått som MER i growth_daily). annonskostnad = Google + Meta i marknadens valuta.
--    Läs kolumnerna pct_mot_foreg och pct_mot_fjol. Ett mått som sjunker mer än ordrarna (till exempel mer eller konvertering) pekar på effektivitet,
--    inte bara volym.
CREATE TEMP TABLE pp AS
SELECT marknad, per,
       IF(COUNT(ordrar) = n_dagar, SUM(ordrar), NULL) AS ordrar,
       IF(COUNT(oms) = n_dagar, SUM(oms), NULL) AS oms,
       IF(COUNT(sessioner) = n_dagar, SUM(sessioner), NULL) AS sessioner,
       IF(COUNT(kop) = n_dagar, SUM(kop), NULL) AS kop,
       IF(COUNT(g_kost) = n_dagar AND COUNT(m_kost) = n_dagar, SUM(g_kost) + SUM(m_kost), NULL) AS kost
FROM (
  SELECT *, CASE WHEN d BETWEEN p1_start AND p1_slut THEN 'nu'
                 WHEN d BETWEEN p0_start AND p0_slut THEN 'fore'
                 WHEN d BETWEEN f1_start AND f1_slut THEN 'fjol' END AS per
  FROM dag
)
WHERE per IS NOT NULL
GROUP BY 1, 2;

SELECT marknad, matt, nu, foregaende, fjol,
       ROUND(SAFE_DIVIDE(nu - foregaende, foregaende) * 100, 1) AS pct_mot_foreg,
       ROUND(SAFE_DIVIDE(nu - fjol, fjol) * 100, 1) AS pct_mot_fjol
FROM (
  SELECT marknad, 1 AS rang, 'ordrar' AS matt,
         MAX(IF(per = 'nu', ordrar, NULL)) AS nu, MAX(IF(per = 'fore', ordrar, NULL)) AS foregaende, MAX(IF(per = 'fjol', ordrar, NULL)) AS fjol
  FROM pp GROUP BY marknad
  UNION ALL
  SELECT marknad, 2, 'omsattning',
         ROUND(MAX(IF(per = 'nu', oms, NULL))), ROUND(MAX(IF(per = 'fore', oms, NULL))), ROUND(MAX(IF(per = 'fjol', oms, NULL)))
  FROM pp GROUP BY marknad
  UNION ALL
  SELECT marknad, 3, 'sessioner_ga4',
         MAX(IF(per = 'nu', sessioner, NULL)), MAX(IF(per = 'fore', sessioner, NULL)), MAX(IF(per = 'fjol', sessioner, NULL))
  FROM pp GROUP BY marknad
  UNION ALL
  SELECT marknad, 4, 'konvertering_ga4_pct',
         ROUND(MAX(IF(per = 'nu', SAFE_DIVIDE(kop, sessioner), NULL)) * 100, 2),
         ROUND(MAX(IF(per = 'fore', SAFE_DIVIDE(kop, sessioner), NULL)) * 100, 2),
         ROUND(MAX(IF(per = 'fjol', SAFE_DIVIDE(kop, sessioner), NULL)) * 100, 2)
  FROM pp GROUP BY marknad
  UNION ALL
  SELECT marknad, 5, 'annonskostnad_google_meta',
         ROUND(MAX(IF(per = 'nu', kost, NULL))), ROUND(MAX(IF(per = 'fore', kost, NULL))), ROUND(MAX(IF(per = 'fjol', kost, NULL)))
  FROM pp GROUP BY marknad
  UNION ALL
  SELECT marknad, 6, 'mer_oms_per_annonskrona',
         ROUND(MAX(IF(per = 'nu', SAFE_DIVIDE(oms, kost), NULL)), 2),
         ROUND(MAX(IF(per = 'fore', SAFE_DIVIDE(oms, kost), NULL)), 2),
         ROUND(MAX(IF(per = 'fjol', SAFE_DIVIDE(oms, kost), NULL)), 2)
  FROM pp GROUP BY marknad
)
ORDER BY marknad DESC, rang;
