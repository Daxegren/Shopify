# Tillväxtdata: Shopify, GA4, Google Ads och Meta i BigQuery

Syftet är att alla siffror som behövs för att styra tillväxten ligger på ett ställe, uppdateras varje natt och går att jämföra dag för dag och marknad för marknad. Det är grunden för den löpande tillväxtrapporten.

## Vad som hämtas

| Källa | Tabell i `site_audit` (eller `shopify`) | Innehåll | Hämtas |
|---|---|---|---|
| Shopify | `shopify.orders`, `order_line_items` m.fl. | ordrar, produkter, kunder | varje timme (jobbet `shopify-sync`) |
| GA4 | `ga4_landing_daily_<sajt>` | besök, köp och intäkt per dag, domän och landningssida | `refresh` |
| GA4 | `ga4_channel_daily_<sajt>` | samma per kanal, källa/medium och kampanj | `refresh` |
| Google Ads | `google_ads_daily_<sajt>` | kostnad, klick och konverteringar per dag och kampanj | `refresh` |
| Google Ads | `google_ads_products_daily_<sajt>` | samma per dag och produkt (Shopping och Performance Max) | `refresh` |
| Meta | `meta_ads_daily_<sajt>` | utgift, klick och köp per dag och kampanj | `refresh` |
| Search Console | `gsc_combined_<sajt>` | klick, visningar och position | massexport + `backfill gsc` |

`<sajt>` är sajtens namn med understreck, till exempel `gorillasports_se`. Båda marknaderna (SE och DK) ligger i samma tabeller och skiljs åt med valuta och domän.

Vyerna i `sql/growth/views.sql` slår ihop källorna: `growth_ads_daily` (alla annonser) och `growth_daily` (en rad per dag och marknad med ordrar, omsättning, besök, annonskostnad och MER, omsättning per annonskrona).

*Inaktuellt sedan 2026-10-18, se ändringsloggen: vyerna heter nu `growth_ads_daily_<butik>` och `growth_daily_<butik>` och genereras med `site-audit growth-sql` (se `docs/flera-sajter.md`).*

## Så fungerar det

```bash
site-audit backfill google-ads --site gorillasports-se --since 2025-07-01   # historik, en gång
site-audit backfill meta-ads   --site gorillasports-se --since 2025-07-01
site-audit refresh --site gorillasports-se --days 30                        # nattligt, ersätter 30 dagar
```

De senaste 30 dagarna ersätts varje natt eftersom konverteringar revideras i efterhand (Googles konverteringsfördröjning, Metas attributionsfönster). Ett fel i en källa stoppar inte de andra, men jobbet markeras som misslyckat så att det syns.

Konverteringsvärdet i annonstabellerna är plattformarnas egen tillskrivning. Google och Meta kan räkna samma köp, så de ska aldrig summeras. Shopify-omsättningen är facit, och MER är måttet för helheten.

## Behörigheter som David ordnar (aldrig i chatten)

1. **Google Ads:** lägg tjänstkontot `shopify-sync@<projekt>.iam.gserviceaccount.com` som användare med läsrätt i båda Google Ads-kontona (SE och DK). Skaffa en utvecklartoken (kräver ansökan hos Google om den inte finns) och lägg den som hemligheten `google-ads-developer-token`. Går kontona via en hanterarkonto (MCC), ange dess id som `google_ads_login_customer_id` i `sites.toml`.

*Inaktuellt sedan 2026-10-18, se ändringsloggen: Google har tagit bort kravet på utvecklartoken för Google Ads API (meddelande i API-center). Token är nu valfri, och åtkomstnivåer hanteras i Google Cloud Console. Tjänstkontot behöver åtkomst till hanterarkontot, och Google Ads API måste vara aktiverat i Cloud-projektet.*
2. **Meta:** skapa en systemanvändare i Meta Business Manager med läsrätt (`ads_read`) till de två annonskontona och lägg dess token som hemligheten `meta-access-token`. Systemanvändartoken går inte ut, till skillnad från en personlig token.
3. **Google Cloud:** `deploy/data_refresh_job.sh` skapar jobbet `data-refresh` (05:30 varje morgon). Hemligheterna kopplas om de finns.

## Att kontrollera vid första körningen

- **Google Ads API-versionen** (`google_ads_api_version` i `sites.toml`) måste vara en version som Google fortfarande stöder. Äldre versioner stängs av.
- **Radantal mot plattformen:** summera kostnaden för en period i BigQuery och jämför med Google Ads och Meta Ads Manager. Skillnaden ska vara noll.
- **Valutor:** vyerna härleder marknaden ur valutan (SEK = SE, DKK = DK). Lägg till fler marknader i `CASE`-satsen i `views.sql`.

## Nästa steg i datalagret (inte byggt)

- Koppla Google Ads-produkter till Shopify-produkter via `item_id` (mot SKU eller variant-id i Merchant Center-flödet).
- Annonsnivå (annons och bild) för Meta, för att se vilka budskap som fungerar.
- Lagerhistorik från Shopify, så att slutsålda produkter syns i orderkurvan.
- Annonskostnad per produktkategori och kundtyp (nya mot återkommande kunder).
