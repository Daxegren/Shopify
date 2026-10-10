# shopify-sync

> Paketet innehåller också **site-audit**, genomlysning av Shopify-sajter med crawl, admin-kontroller, rapport och effektmätning. Se [docs/site-audit.md](docs/site-audit.md).

Synkar Shopify-data till **BigQuery** och/eller **Postgres (Supabase)**. Jobbet är inkrementellt och kan köras om utan dubbletter.

- **Data:** ordrar, orderrader, produkter, varianter och kunder. Kunder sparas utan namn, e-post, telefon och adress.
- **Hämtning:** Shopify Bulk Operations (GraphQL Admin API). Det klarar full historik utan att slå i rate limits.
- **Inkrementellt:** ett vattenmärke på `updated_at` per entitet sparas i tabellen `sync_state`. Varje körning hämtar bara det som ändrats sedan dess, med 15 minuters överlapp.
- **Lagring:** typade kolumner för vanliga analyser plus en `raw`-kolumn (JSON/JSONB) med hela Shopify-objektet.
- **Ett schema för båda databaserna:** `src/shopify_sync/schema.py` styr både BigQuery och Postgres.
- **Körmiljö:** samma Docker-image kan köras som Cloud Run Job, på en egen VM eller server med cron, eller lokalt.

## Arkitektur

```
Shopify Admin API ──bulk──> shopify-sync ──┬──> BigQuery  (analys: ihop med GA4- och Search Console-exporterna)
                                           └──> Supabase  (Postgres: appar, API, egen server)
```

Rekommendation: **BigQuery är analyslagret.** GA4 och Search Console exporterar dit gratis och direkt, så alla tre källorna kan kopplas ihop i en och samma SQL-fråga. **Supabase är driftdatabasen** för det du bygger på din egen server. Kör båda med `SINKS=bigquery,postgres`. Om du bara vill ha den ena sätter du `SINKS` till den.

Lägg BigQuery-datamängderna för Shopify, GA4 och Search Console i **samma plats (`EU`)**. BigQuery kan inte koppla ihop tabeller mellan olika platser.

## Kom igång i Google Cloud

### 1. Skapa projekt och aktivera fakturering

```bash
gcloud auth login
gcloud projects create gorilla-sports-data --name "Gorilla Sports Data"   # välj eget id
gcloud config set project gorilla-sports-data
# Koppla ett faktureringskonto i konsolen: Billing -> Link a billing account
```

### 2. Skapa en Shopify-app med läsbehörighet

Gå till Shopify Dev Dashboard → *Create app*, installera appen i butiken och ge den följande scopes:

`read_orders`, `read_all_orders` (krävs för ordrar äldre än 60 dagar), `read_products`, `read_inventory`, `read_customers`.

Du kan autentisera på två sätt:
- med **Client ID och Client secret**, då hämtar jobbet en token själv via client credentials, eller
- med en färdig **Admin API access token** (`shpat_...`) om du har en från en befintlig app.

#### Om appen ägs av ett partnerkonto (annan organisation än butiken)

Då fungerar inte client credentials. Hämta i stället en permanent offline-token en gång via OAuth. Det görs enklast i **Cloud Shell**, där gcloud redan är inloggat:

```bash
cd shopify-sync
read -s SHOPIFY_CLIENT_ID && export SHOPIFY_CLIENT_ID          # klistra in, Enter
read -s SHOPIFY_CLIENT_SECRET && export SHOPIFY_CLIENT_SECRET  # klistra in, Enter
PYTHONPATH=src python3 -m shopify_sync.main authorize \
  --shop BUTIK.myshopify.com \
  --base-url https://8080-<din-web-preview-adress>.cloudshell.dev
```

- Ange **App URL** `<base-url>/` och **Redirect URL** `<base-url>/callback` i appens version, och slå av inbäddning i Shopify admin.
- Installera appen i butiken via installationslänken (Distribution → Custom distribution).
- Tokenen sparas direkt i Secret Manager som `shopify-access-token` och skrivs aldrig ut.

### 3. Lägg hemligheterna i Secret Manager

Lägg bara in de hemligheter du använder:

```bash
printf '%s' 'CLIENT_ID'     | gcloud secrets create shopify-client-id --data-file=-
printf '%s' 'CLIENT_SECRET' | gcloud secrets create shopify-client-secret --data-file=-
# eller:
printf '%s' 'shpat_...'     | gcloud secrets create shopify-access-token --data-file=-

# Endast om Supabase ska användas:
printf '%s' 'postgresql://...' | gcloud secrets create supabase-db-url --data-file=-
```

### 4. Driftsätt

```bash
PROJECT_ID=gorilla-sports-data \
SHOPIFY_SHOP_DOMAIN=din-butik.myshopify.com \
SINKS=bigquery,postgres \
./deploy/cloudrun.sh

# Första körningen gör en full backfill:
gcloud run jobs execute shopify-sync --region europe-north1 --wait
```

Skriptet gör följande: aktiverar de API:er som behövs, skapar tjänstkontot `shopify-sync` med minsta nödvändiga roller, bygger imagen med Cloud Build, skapar Cloud Run-jobbet och schemalägger det varje timme med Cloud Scheduler. Regionen är `europe-north1` (Finland).

### 5. Aktivera GA4- och Search Console-exporterna till samma projekt

- **GA4:** Admin → Product links → BigQuery Links → välj projektet och plats `EU`, dagligen och gärna streaming.
- **Search Console:** Settings → Bulk data export → ange projekt-id och dataset `searchconsole`.

Ingen av exporterna fyller i historik bakåt i tiden, så aktivera dem så tidigt som möjligt.

## Supabase

- Använd anslutningssträngen för **Supavisor-poolern** (Project Settings → Database → Connection string). Den direkta värden är bara IPv6 och nås inte från Cloud Run utan extra nätverkskonfiguration.
- Tabellerna skapas automatiskt i schemat `shopify`. Om du hellre vill använda Supabase-migreringar finns samma SQL i `sql/postgres_schema.sql`:
  ```bash
  supabase migration new shopify_schema
  cp sql/postgres_schema.sql supabase/migrations/<tidsstämpel>_shopify_schema.sql
  ```
- Schemat stängs för rollerna `anon` och `authenticated`, så Shopify-data exponeras inte via Supabase REST-API. Ge åtkomst explicit, eller bygg vyer med RLS, om en app ska läsa datan.

## Köra på egen server

```bash
cp .env.example .env    # fyll i
docker build -t shopify-sync .
docker run --rm --env-file .env shopify-sync run
# cron, varje timme:
# 7 * * * * docker run --rm --env-file /opt/shopify-sync/.env shopify-sync run
```

För BigQuery utanför Google Cloud: montera en tjänstkontonyckel och sätt `GOOGLE_APPLICATION_CREDENTIALS`.

## Kommandon

| Kommando | Funktion |
|---|---|
| `shopify-sync run` | Inkrementell synk av `ENTITIES` till `SINKS` |
| `shopify-sync run --full` | Hämtar allt från `SYNC_START_DATE`, oavsett vattenmärke |
| `shopify-sync run --entities orders` | Synkar bara ordrar |
| `shopify-sync print-ddl postgres` | Skriver ut Postgres-schemat |
| `shopify-sync print-ddl bigquery --schema projekt.shopify` | Skriver ut BigQuery-schemat |

Alla inställningar finns beskrivna i `.env.example`.

## Utveckling

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -e '.[all,dev]'
pytest                                                    # enhetstester
TEST_PG_DSN=postgresql://postgres@localhost:5432/postgres pytest   # inkl. Postgres-integration
```

Om du ändrar `schema.py` behöver du generera om SQL-filerna (ett test kontrollerar att de stämmer):

```bash
shopify-sync print-ddl postgres > sql/postgres_schema.sql
shopify-sync print-ddl bigquery > sql/bigquery_schema.sql
```

## Exempel: returandel per produkt (BigQuery)

```sql
SELECT
  li.title,
  SUM(li.quantity) AS sold,
  SUM(li.removed_quantity) AS removed,
  SAFE_DIVIDE(SUM(li.removed_quantity), SUM(li.quantity)) AS removal_rate
FROM `gorilla-sports-data.shopify.order_line_items` li
JOIN `gorilla-sports-data.shopify.orders` o ON o.id = li.order_id
WHERE o.created_at >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 365 DAY)
GROUP BY li.title
HAVING sold >= 10
ORDER BY removal_rate DESC;
```

`removed_quantity` är `quantity - currentQuantity`, alltså enheter som tagits bort genom återbetalning eller orderändring.
