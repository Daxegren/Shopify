# site-audit: genomlysning av Shopify-sajter

`site-audit` gör samma typ av genomlysning som Mankovsky-analysen för alla sajter i `sites.toml`. Varje körning sparas i BigQuery, så att du kan följa vad som har åtgärdats och mäta effekten av ändringar mot Search Console, GA4 och Shopify.

## Vad som kontrolleras

| Område | Kontroller (id) | Exempel på fynd |
|---|---|---|
| Indexering | `sitemap_url_error`, `sitemap_url_redirects`, `sitemap_noindex`, `soft_404`, `canonical_not_ok`, `canonical_offsite`, `collection_product_url_indexable`, `robots_*`, `empty_collection_in_sitemap`, `sitemap_error_explained` | "46 konstnärssidor i sitemapen ger 404", med orsaken från admin (borttagen, utkast, saknad marknad) |
| Omdirigeringar | `redirect_chain`, `redirect_to_error`, `redirect_loop`, `temporary_redirect`, `redirect_table_chain`, `redirect_target_missing`, `redirect_target_mismatch`, `redirect_self`, `redirect_shadowed` | Kedjor som slutar i 404, och mål som pekar på fel konstnär eller stad |
| Marknader och språk | `geo_redirect`, `redirect_changes_locale`, `redirect_table_locale`, `hreflang_*`, `language_mismatch`, `html_lang_mismatch`, `locale_summary`, `primary_locale_unexpected`, `unexpected_locales` | "85 omdirigeringar skickar svenska besökare till /en-ca/", 302 från roten, halvöversatta sidor, 24 hreflang-varianter |
| Metadata | `missing_h1`, `multiple_h1`, `missing_title`, `duplicate_title`, `title_too_long`, `missing_meta_description`, `duplicate_seo_title`, `low_ctr_top10` | Ingen H1 på produktsidor och sex på startsidan, ärvda SEO-titlar |
| Strukturerad data | `product_schema_missing`, `product_schema_bad_image`, `product_schema_no_offers`, `breadcrumb_schema_missing`, `org_schema_missing`, `jsonld_invalid` | Trasig bild-URL i Product-schemat, ArtGallery-schema saknas |
| Katalog | `empty_collection`, `duplicate_collection_products`, `near_duplicate_collection`, `duplicate_collection_description`, `collection_clones`, `collection_rule_suspect`, `filename_handle`, `duplicate_product_title`, `product_no_description`, `product_no_images` | 32 tomma kollektioner, 26 doorway-kollektioner, 24 kloner av "Fine art prints", filnamn som handles |
| Innehåll | `test_page_published`, `test_or_draft_page`, `outdated_page`, `app_generated_page`, `duplicate_role_page`, `thin_page`, `thin_content`, `duplicate_content`, `brand_misspelling`, `keyword_cannibalization`, `no_search_impressions` | AVADA-sitemaps, testsidor, gamla event, dubbla Om oss- och Kontakt-sidor, "Mankosvky" i 15 texter |
| Bilder | `images_missing_alt`, `product_images_no_alt`, `alt_text_summary`, `insecure_resources` | Alt-text saknas på nya produkter |
| Prestanda | `html_too_large`, `large_inline_script`, `html_size_stats` | HTML på 1,35–1,78 MB, trust-badge-skript på 300 KB inline |
| Trafik | `traffic_page_broken`, `traffic_page_redirected` | Sidor som hade klick i Google men nu ger 404 |
| Struktur | `inventory`, `orphan_page` | Sidtyp × språk, sidor i sitemapen som ingen sida länkar till |
| Översättning | `partial_translation`, `outdated_translation` | "'de': bara 34 % av produkterna är fullt översatta" |
| Core Web Vitals | `cwv_lcp`, `cwv_inp`, `cwv_cls`, `lighthouse_performance` | LCP 4,8 s för verkliga mobilbesökare (kräver `--psi N` och `PSI_API_KEY`) |

Varje fynd har en allvarlighetsgrad (kritisk, hög, medel, låg eller info), en URL eller Shopify-resurs, och detaljer (`evidence`).

## Kom igång

```bash
cd shopify-sync
cp sites.example.toml sites.toml      # lägg till sajter, varumärken och sidgrupper
pip install -e '.[all]'

# Full genomlysning: Shopify-admin (om token finns) och crawl
SHOPIFY_ACCESS_TOKEN=... site-audit run --site gorillasports-se

# Spara i BigQuery och koppla ihop med Search Console
site-audit run --site all --bigquery --search-data
```

Varje körning skapar `audits/<körning>/` med följande filer:
- `report.html` och `report.md`: rapporten
- `findings.jsonl`: alla fynd
- `pages.jsonl`: alla URL:er med sidfakta
- `summary.json` och `geo.json`
- `actions.csv`: prioriterad åtgärdslista, där flera fynd på samma mål slås ihop till en rad
- `redirects_import.csv`: färdiga 301:or i Shopifys importformat, för döda URL:er, kedjor som ska peka direkt på slutmålet och sammanslagna kollektioner eller sidor. Importera under *Online Store → Navigation → URL Redirects → Import*. Förslag som verktyget är osäkert på är märkta "kontrollera manuellt" i `actions.csv`. **Gå igenom filen innan du importerar.**

## Följa förändringar

```bash
# Vad är åtgärdat och vad är nytt mellan två körningar?
site-audit diff audits/<gammal> audits/<ny>

# Registrera en ändring, t.ex. omgjorda konstnärssidor
site-audit log-change --site mankovsky --date 2026-07-01 --group konstnarer \
  --description "Nya konstnärssidor med H1, schema och sammanslagna dubbletter"

# Effekt: 90 dagar före och efter, jämfört med resten av sajten
site-audit impact --site mankovsky --group konstnarer --date 2026-07-01 --days 90
#  gsc/Klick (Google): 1200 → 1800 (+50 %, netto +42 p.e. mot resten av sajten)
#  ga4/Sessioner (GA4): ...
#  shopify/Ordrar (Shopify): ...

# Trend per sidgrupp och månad
site-audit trend --site mankovsky --since 2026-01-01
```

"Netto" visar gruppens förändring minus resten av sajtens förändring under samma period, räknat i procentenheter. Utan den jämförelsen kan en säsongsuppgång se ut som en effekt av ändringen.

Vyerna i `sql/audit/views.sql` ger samma data i BigQuery: `check_trend`, `open_findings`, `finding_changes`, `page_history`, `pages_with_search` och `change_impact_gsc`.

```bash
sed 's/PROJ/gorilla-sports-data/g' sql/audit/views.sql | bq query --use_legacy_sql=false
```

*Tillägg 2026-10-10:* kör först `sql/audit/views_sources.sql`, som innehåller de kombinerade Search Console-vyerna `gsc_combined_<sajt>`. Den första genomlysningen behöver dem. Kör `views.sql` efter den första genomlysningen, eftersom vyerna där läser tabellerna `runs`, `findings` och `pages` som genomlysningen skapar.

## Historik från dag ett

Bulkexporterna fyller inte i bakåt i tiden. Hämta därför historiken via API:erna en gång, och därefter vid behov:

```bash
site-audit backfill gsc --site gorillasports-se --days 480   # ca 16 månader, sidnivå
site-audit backfill gsc --site gorillasports-se --days 90 --queries   # med sökfraser
site-audit backfill ga4 --site gorillasports-se --since 2025-01-01    # landningssidor, sessioner, köp, intäkt
```

Förutsättningar:
- Tjänstkontot `shopify-sync@<projekt>.iam.gserviceaccount.com` läggs till som användare i Search Console-egendomen och som *Viewer* i GA4-egendomen.
- *Search Console API* och *Google Analytics Data API* är aktiverade i projektet.

Vyn `gsc_combined_<sajt>` använder API-data fram till den dag bulkexporten började, och därefter exporten. Effekt- och trendanalyserna fungerar mot båda källorna.

## Köra varje natt i Google Cloud

```bash
PROJECT_ID=gorilla-sports-data ./deploy/site_audit_job.sh
```

Skriptet gör följande:
- Skapar Cloud Run-jobbet `site-audit` och schemalägger det kl. 04:00 svensk tid.
- Kör alla sajter i `sites.toml`.
- Sparar körningarna i datasetet `site_audit`.
- Läser Shopify-tokens från Secret Manager. Flera butiker anges med `SECRET_ENV="SHOPIFY_ACCESS_TOKEN=shopify-access-token,MANKOVSKY_SHOPIFY_TOKEN=mankovsky-token"`.

## Exempelfrågor i BigQuery

```sql
-- Hur många 404 i sitemapen per körning?
SELECT started_at, findings FROM `gorilla-sports-data.site_audit.check_trend`
WHERE site = 'mankovsky' AND check_id = 'sitemap_url_error' ORDER BY started_at;

-- Vilka sidor med trafik saknar H1?
SELECT p.url, p.clicks_90d FROM `gorilla-sports-data.site_audit.pages_with_search` p
WHERE p.h1_count = 0 AND p.clicks_90d > 0 ORDER BY p.clicks_90d DESC;

-- Vad åtgärdades sedan förra körningen?
SELECT check_id, COUNT(*) FROM `gorilla-sports-data.site_audit.finding_changes`
WHERE status = 'åtgärdad' GROUP BY 1 ORDER BY 2 DESC;
```

## Begränsningar att känna till

- **Geo-omdirigeringar:** Shopify styr dem på IP-adress. Crawlern simulerar språk med `Accept-Language` och kan sätta en `localization`-cookie. Det fångar språkstyrda omdirigeringar och omdirigeringar i Shopify-tabellen, men för att se exakt vad en svensk IP-adress får måste jobbet köras från en server i Sverige.
- **Språkgissningen** bygger på stoppord och fungerar på sidor med minst cirka 80 ord. Den ska användas för att hitta halvöversatta sidor, inte som en exakt mätning.
- **Admin-kontrollerna** kräver följande behörigheter för Shopify-appen (alla validerade mot Admin API 2026-07):

  | Data | Behörighet |
  |---|---|
  | Produkter, kollektioner, regler | `read_products` |
  | Sidor och artiklar | `read_content`, `read_online_store_pages` |
  | URL-omdirigeringar | `read_online_store_navigation` |
  | Språk | `read_locales` |
  | Marknader | `read_markets` |
  | Översättningsgrad per språk | `read_translations` |

  Saknas en behörighet visas det som `admin_fetch_error` i rapporten, och resten av körningen fortsätter.
- **Google Ads:** koppla kontot med BigQuery Data Transfer Service (*Google Ads* som källa) till samma projekt och plats `EU`. Då kan annonsdatan kopplas ihop med landningssidorna i tabellerna ovan.

## Tillägg 2026-10-10: justeringar efter första körningen mot gorillasports.se

- `redirect_target_missing` stäms nu av mot crawlen. Mål som svarar 200 räknas inte längre som fel, eftersom 716 av 892 fungerade. Det kan bero på översatta handles eller på Shopifys egna omdirigeringar. Mål som inte gick att hämta blir `redirect_target_unverified` (låg).
- `product_schema_relative_image` (låg) är ny. Bild-URL:er som `//www.gorillasports.se/cdn/...` räknas inte längre som trasiga (`product_schema_bad_image`). De rapporteras i stället som en rekommendation om att lägga till `https:`.
- `large_inline_script_sitewide` är ny. Samma skript på 10 sidor eller fler blir ett enda fynd med antal sidor, i stället för ett fynd per sida.
- `redirect_to_other_market` (hög) är ny. Den visas när en URL på .se skickar besökaren till .dk, eller tvärtom.
- Spårningsparametrar (`pr_*`, `shpxid`, `utm_*` m.fl.) tas bort före crawl, så att samma sida inte hämtas flera gånger.
- `fetch_failed` anger nu orsaken, till exempel `429 Too Many Requests`. Crawlern försöker fem gånger i stället för tre.
- Översättningsgraden för sidor använder resurstypen `PAGE`. `ONLINE_STORE_PAGE` var fel. En typ som API:et inte känner till hoppas nu över i stället för att stoppa hela översättningsdelen.

## Tillägg 2026-10-10: justeringar efter andra körningen mot gorillasports.se

- **`redirect_to_error`** gäller nu bara omdirigeringar som slutar i 4xx eller 5xx. Meddelandet anger antalet hopp. En kedja som slutar i fel räknas inte längre också som `redirect_chain`, så samma URL ger ett fynd i stället för två.
- **`redirect_unverified`** (låg) är ny. Den visas när slutmålet inte kunde hämtas, till exempel efter 429. Tidigare räknades sådana omdirigeringar som `redirect_to_error` (kritisk).
- **`redirect_invalid_target`** (kritisk) är ny. Den gäller omdirigeringar vars mål saknar domän, till exempel `//collections/wall-ball`, som webbläsaren tolkar som domänen "collections". Fyndet kommer både från crawlen och från omdirigeringstabellen i Shopify. Tidigare syntes felet som `fetch_failed` med ett DNS-fel.
- **`redirect_target_tracking_params`** (medel) är ny. Den gäller mål i omdirigeringstabellen som innehåller spårningsparametrar, till exempel `pr_prod_strat` eller `shpxid`. Det rensade målet läggs i `redirects_import.csv`.
- **Kundkonto, kassa och varukorg** (`/customer_authentication`, `/account`, `/cart`, `/checkout`) crawlas inte längre. Sidorna omdirigerar alltid till inloggning och är inga fel.
- **Om-hämtning:** URL:er som föll på 429 eller nätverksfel hämtas en gång till i slutet av crawlen, efter 30 sekunders paus och med 1 anrop per sekund. Högst 500 URL:er hämtas om.
- **`fetch_failed`** gäller bara URL:er som inte omdirigeras. Omdirigerade URL:er redovisas under omdirigeringskontrollerna.
- **`redirects_import.csv`** innehåller nu även ersättare för `redirect_target_missing` och `redirect_invalid_target`, samt rensade mål för `redirect_target_tracking_params`.
- **Filerna sparas i Cloud Storage:** `run --upload gs://<bucket>/audits` laddar upp rapporten, `actions.csv` och `redirects_import.csv` till `.../<sajt>/<körning>/` och `.../<sajt>/latest/`. Jobbet i Cloud Run gör det automatiskt till bucketen `<projekt>-site-audit`, som `deploy/site_audit_job.sh` skapar. Hämta filerna med:

  ```bash
  gcloud storage cp -r gs://gorilla-sports-data-site-audit/audits/gorillasports-se/latest .
  ```

## Tillägg 2026-10-10: justeringar efter tredje körningen mot gorillasports.se

- **`redirect_target_tracking_params`** har nu allvarlighetsgrad låg. Målet fungerar, men adressen innehåller sökspårning (`_pos`, `_ss`, `_psq`, `_psid`, `_v`) eller rekommendationsspårning (`pr_*`). `variant=` räknas inte längre som spårning i omdirigeringsmål, eftersom den kan peka på en viss storlek eller färg. `_psid` har lagts till i listan över spårningsparametrar.
- **`redirect_table_other_domain`** (hög) är ny. Den gäller omdirigeringar i Shopify vars mål är en fullständig adress på en annan domän, till exempel `https://www.gorillasports.dk/...`. Omdirigeringstabellen gäller alla domäner i butiken, så även besökare på .se skickas till .dk.
- **`traffic_page_redirected`** bortser nu från `http://` → `https://` till samma sökväg. Det är Shopifys vanliga omdirigering och inget fel.
- **Förslag på nya mål** jämför bara ord som betyder något. Enheter (`10kg`, `40mm`), ord kortare än tre tecken, plattformsord (`p`, `blogg`, `butikk`), landskoder och vanliga småord ignoreras. Singular och plural räknas som samma ord (`rope`/`ropes`).
- **`redirects_import.csv`** innehåller nu bara säkra omdirigeringar:
  - kedjor som pekas om till sitt fungerande slutmål
  - rensade spårningsparametrar
  - sammanslagningar
  - förslag med säkerhet 0,6 eller mer

  Osäkra förslag, till exempel fallback till `/collections/all`, hamnar i **`redirects_review.csv`** med säkerhet och antal klick från Google. Den filen ska gås igenom manuellt och importeras inte direkt.
