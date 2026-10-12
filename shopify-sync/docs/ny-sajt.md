# Lägga till en ny sajt

Samma verktyg används för alla sajter. En ny sajt läggs till med konfiguration och behörigheter. Ingen kod behöver ändras. Gör stegen i ordning. Steg 1–3 görs i webbläsaren, steg 4–8 i Cloud Shell eller av Claude.

## Före start: välj Google Cloud-projekt

| Läge | Rekommendation |
|---|---|
| Sajten tillhör samma bolag eller koncern som Gorilla Sports | Samma projekt, `gorilla-sports-data`, med egna dataset per sajt |
| Sajten tillhör ett annat bolag, till exempel Mankovsky | Eget projekt per bolag. Då hålls data, kostnader och åtkomst åtskilda, och bolaget kan ta över projektet vid en försäljning |

Ett nytt projekt kräver att det första kapitlet i `README.md` görs en gång: fakturering, API:er och tjänstkonto. Använd ditt projekt-id i stället för `gorilla-sports-data` i stegen nedan.

## 1. Shopify: installera appen i butiken

Gäller bara Shopify-sajter. Andra sajter granskas utan admin-kontrollerna.

1. Gå till Partners → Appar → appen → **Distribution** → skapa en ny installationslänk för butikens `xxx.myshopify.com`. En länk gäller en butik.
2. Öppna länken som ägare eller personal med rätt behörighet i butiken och godkänn.
3. Hämta token och spara den med ett eget namn:
   ```bash
   shopify-sync authorize --shop xxx.myshopify.com --base-url <Web Preview-adressen> \
     --project gorilla-sports-data --secret xxx-shopify-token
   ```

## 2. Search Console

1. Lägg till `shopify-sync@<projekt>.iam.gserviceaccount.com` som användare, med fullständig behörighet, i sajtens egendom. Använd domänegendomen (`sc-domain:`) om den finns.
2. Under *Inställningar → Massexport av data*: ange projektet och ett eget dataset, till exempel `searchconsole_xxx`.

## 3. Google Analytics 4

1. Lägg till samma tjänstkonto som **Läsare** i GA4-egendomen.
2. Valfritt: koppla GA4 till BigQuery under *Administratör → BigQuery-länkar*.
3. Anteckna egendoms-id:t, som består av siffror.

## 4. `sites.toml`: lägg till ett block

Kopiera exemplet för Mankovsky i `sites.example.toml` och fyll i:
- `name`, `base_url`
- `shop_domain`, `shopify_token_env`, till exempel `XXX_SHOPIFY_TOKEN`
- `gsc_property`
- `gsc_table = "<projekt>.site_audit.gsc_combined_xxx"`
- `ga4_property_id`
- `ga4_api_table = "<projekt>.site_audit.ga4_landing_daily_xxx"`
- `shopify_dataset = "<projekt>.shopify_xxx"`
- `shopify_currency`
- `bq_project`
- `brand_terms`
- vanliga felstavningar
- `page_groups`, sidgrupper för effektmätning

## 5. Search Console-vyn

Kopiera blocket för `gsc_combined_gorillasports_dk` i `sql/audit/views_sources.sql`. Byt `searchconsole_dk` mot sajtens dataset och suffixet `gorillasports_dk` mot `xxx`. Kör sedan filen:
```bash
sed 's/PROJ/gorilla-sports-data/g' sql/audit/views_sources.sql | bq query --use_legacy_sql=false
```

## 6. Historik bakåt

```bash
site-audit backfill gsc --site xxx --days 480
site-audit backfill ga4 --site xxx --since 2025-01-01
```

Search Console-exporten och GA4:s export fyller bara på framåt. Historiken hämtas därför en gång via API:erna.

## 7. Shopify-synk för butiken

Ett eget jobb per butik, med eget dataset:
```bash
PROJECT_ID=gorilla-sports-data SHOPIFY_SHOP_DOMAIN=xxx.myshopify.com JOB=shopify-sync-xxx \
  BQ_DATASET=shopify_xxx TOKEN_SECRET=xxx-shopify-token ./deploy/cloudrun.sh
```

## 8. Nattlig granskning

Lägg till butikens token i jobbet och bygg om. `SITES=all` granskar alla sajter i `sites.toml`:
```bash
PROJECT_ID=gorilla-sports-data \
  SECRET_ENV="SHOPIFY_ACCESS_TOKEN=shopify-access-token,XXX_SHOPIFY_TOKEN=xxx-shopify-token" \
  ./deploy/site_audit_job.sh
```

Kör därefter den första granskningen direkt och följ samma arbetsgång som för gorillasports.se:
1. Kontrollera fynden för falsklarm.
2. Granska omdirigeringarna.
3. Ta fram beslutsunderlag enligt `CLAUDE.md`.

Resultatet hamnar i `gs://<projekt>-site-audit/audits/xxx/latest/`.

## Det som skiljer sig mellan sajter

- **Inte Shopify:** steg 1 och 7 utgår, och admin-kontrollerna (katalog, omdirigeringstabell, översättningar) körs inte. Crawl, Search Console och GA4 fungerar som vanligt.
- **Flera domäner i samma butik** (som .se och .dk): ett block per domän, samma `shop_domain`, olika `shopify_currency` och filter på värdnamn.
- **Annat språk:** ange `primary_locale` och `expected_locales`. Språkgissningen fungerar för svenska, engelska, danska, norska, tyska, finska, franska, spanska, italienska, nederländska och polska.
