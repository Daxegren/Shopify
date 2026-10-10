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
- **Admin-kontrollerna** kräver en token med `read_products`, `read_content` och `read_online_store_pages` för sidor och artiklar. Omdirigeringar kräver `read_online_store_navigation`. Saknas en behörighet visas det som `admin_fetch_error` i rapporten, och resten av körningen fortsätter.
- **Google Ads:** koppla kontot med BigQuery Data Transfer Service (*Google Ads* som källa) till samma projekt och plats `EU`. Då kan annonsdatan kopplas ihop med landningssidorna i tabellerna ovan.
