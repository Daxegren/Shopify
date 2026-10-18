# Driftrutiner för tillväxtdatan

Det här är rutinerna för att hålla datalagret frisk, och en felsökningslista för de fel som har inträffat eller som är rimliga att vänta sig. Inga nycklar eller värden står här, bara namn.

## Rutiner

| När | Vad | Hur |
|---|---|---|
| Varje morgon 05:30 (automatiskt) | Hämtar om de senaste 30 dagarna från GA4, Google Ads och Meta | Cloud Run-jobbet `data-refresh` |
| Måndag förmiddag | Kontrollera att nattkörningen lyckades | `gcloud run jobs executions list --job data-refresh --region europe-north1 --limit 3` |
| Varje måndag 07:00 (när jobbet driftsatts) | Veckorapport med nyckeltal, kanaler, produkter och larm | Cloud Run-jobbet `growth-weekly`, rapporten läses med `gcloud storage cat gs://<projekt>-site-audit/weekly/<sajt>/latest.md` |
| Vid behov | Samma rapport för hand | `site-audit weekly --site gorillasports-se` |
| Efter större förändringar | Datakvalitet: färskhet, luckor, dubbletter | `sql/growth/datakvalitet.sql` |
| Var tredje månad | Kontrollera API-versionen för Google Ads och att Meta-token fungerar | Se felsökningen nedan |

Larmen i veckorapporten (sektionen "Larm") är nivåsatta: **hög** kräver handling samma vecka, **medel** bör undersökas, **info** är ett meddelande om datakvaliteten.

## Felsökning

| Symptom | Trolig orsak | Åtgärd |
|---|---|---|
| Google Ads ger 404 med en HTML-sida | API-versionen finns inte längre (v21 stängdes 2026) | Testa vilka versioner som svarar utan inloggning: `curl -s -o /dev/null -w "%{http_code}" https://googleads.googleapis.com/v26/customers:listAccessibleCustomers`. 404 betyder att versionen saknas, 401 att den finns. Sätt den högsta fungerande i `google_ads_api_version` i `sites.toml`, bygg om imagen och uppdatera jobbet |
| Google Ads ger 403 `CLOUD_PROJECT_NOT_APPROVED_FOR_PRODUCTION` | Cloud-projektet har bara Test-nivå | Ansök om Explorer access under APIs & Services → Google Ads API → Overview i Cloud Console |
| Google Ads ger `AUTHORIZATION_ERROR` trots godkänd nivå | Känt fel hos Google för projekt som uppgraderats efter 9 september 2026 | Ansök om Explorer från ett nytt Cloud-projekt (enligt Googles dokumentation) |
| Google Ads: tjänstkontot nekas | Tjänstkontot saknas som användare i hanterarkontot | Lägg till det under Administration → Åtkomst och säkerhet med rollen Skrivskyddad. Policyvarningen om tillåtna domäner är väntad och hindrar inte åtkomsten |
| Jobbet avbryts med "Out-of-memory" | För mycket data i ett svar | Historik hämtas nu i fönster om 31 dagar. Om det ändå händer, höj jobbets minne tillfälligt (`gcloud run jobs update data-refresh --memory 8Gi`) |
| Meta ger fel med kod 190 | Token är utgången eller återkallad | Generera en ny token för systemanvändaren i Business Manager (behörighet `ads_read`) och lägg den som ny version av hemligheten `meta-access-token` |
| Meta ger kod 4, 17 eller 613 | Begränsning av antal anrop | Hämtningen försöker om med väntetid. Om det upprepas, kör om senare |
| Meta saknar rader för vissa dagar | Meta skapar bara rader för dagar med aktivitet | Kontrollera i Ads Manager om kontot hade utgift dagen. Om ja, kör om perioden |
| GA4 ger 403 | Tjänstkontot saknas som läsare i GA4-egendomen | Lägg till det som Läsare i GA4 |
| GA4: besöken skiljer mellan landningssidetabellen och kanaltabellen | Olika dimensioner ger olika sessionsräkning | Kör fråga 3 och 4 i `sql/growth/datakvalitet.sql` och jämför med GA4:s eget gränssnitt (beslut AE) |
| Vyerna går inte att skapa ("Not found: Table …") | Tabellen har inte hämtats än | Kör `backfill` för källan först, och skapa sedan vyerna med `site-audit growth-sql` |
| Lagerlarm säger "kunde inte kopplas till en Shopify-variant" | Annonsflödets id motsvarar inte variantens id | Kontrollera i Merchant Center vad `item_id` är för format. Kopplingen i `growth_product_daily_*` tar sista talet i id:t |
| Nattkörningen markeras som misslyckad | En källa felade, de andra uppdaterades ändå | Läs loggen: `gcloud logging read` på körningens namn. Raden `<källa>: MISSLYCKADES` visar vilken |

## Hemligheter och åtkomst (namn, aldrig värden)

| Namn | Vad | Var |
|---|---|---|
| `shopify-access-token` | Shopify-synken | Secret Manager |
| `meta-access-token` | Meta, systemanvändaren GS Data Reader, behörighet `ads_read` | Secret Manager, kopplad till jobbet `data-refresh` som `META_ACCESS_TOKEN` |
| `google-ads-developer-token` | Behövs inte längre (Google tog bort kravet 2026) | – |
| Tjänstkontot `shopify-sync@<projekt>` | BigQuery, GA4 (läsare), Search Console (användare), Google Ads (skrivskyddad användare i hanterarkontot) | Google Cloud, GA4, Search Console, Google Ads |

Om en nyckel har visats i en chatt eller i en logg ska den återkallas och bytas ut.

## Vad som inte är automatiserat än

- Larm som skickas ut. Veckorapporten visar larmen, men ingen får ett mejl. Nästa steg är att koppla jobbets fel och rapportens höga larm till e-post.
- Lagerhistorik. Vi ser dagens lagersaldo per variant, inte hur det såg ut den dag annonsen tappade.
  *Inaktuellt sedan 2026-10-18, se ändringsloggen: källan `lager` sparar en ögonblicksbild av lagersaldot per variant varje natt i `inventory_daily_<butik>`. Den börjar gälla när imagen har byggts om, och historiken börjar då. Det går inte att få saldo för tiden före.*
- Rabattkoder och kampanjer. De ligger i Shopify-ordrarna men är inte uppdelade i någon vy än.
- Klaviyo (e-post) som datakälla.
