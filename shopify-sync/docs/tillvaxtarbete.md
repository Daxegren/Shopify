# Tillväxtarbete: testlogg, Merchant Center, Klaviyo, åtkomstkontroll och portföljrapport

Tillägg 2026-10-18. Allt här är byggt men **inte driftsatt och inte körd mot riktiga konton**. Svarsformerna från Merchant API och Klaviyo är skrivna från de publika beskrivningarna och är inte verifierade; räkna med att behöva justera efter första riktiga körningen.

## Testlogg
Varje åtgärd i tillväxtarbetet loggas med hypotes, startdatum, mått och förväntat utfall, och utvärderas efter ett fönster (standard 28 dagar) mot samma antal dagar innan, med övriga marknader som grov kontroll.

```
site-audit test add --site gorillasports-se --start 2026-10-20 --channel google_ads --metric mer \
    --hypothesis "Lägre mål-ROAS ger fler ordrar" --what "Sänk mål-ROAS i SE till 3,8" --market SE --expect 10
site-audit test list --site gorillasports-se
site-audit test evaluate --site gorillasports-se --id <id> [--save]
```
Tabellen `site_audit.growth_tests` skapas vid första `add`. Kontrollen är grov: den fångar säsong och plattformseffekter men ersätter inte ett riktigt A/B-test.

## Merchant Center (källa `merchant`)
Produktstatus per produkt (godkända och avvisade länder, problem) som ögonblicksbild till `merchant_products_<butik>`. Slås på med `merchant_account_id` i `sites.toml`. Tjänstkontot måste läggas till som användare i Merchant Center och Merchant API aktiveras i Cloud-projektet. Analys: `sql/analys/merchant_avvisade.sql` (avvisade produkter som ändå får klick).

## Klaviyo (källa `klaviyo`)
Beställningar och värde per dag och tillskriven kanal till `klaviyo_daily_<butik>`. Slås på med `klaviyo_enabled = true`; en privat API-nyckel med läsrätt läggs i Secret Manager (aldrig i chatten) och kopplas som `KLAVIYO_API_KEY` (eller eget namn via `klaviyo_api_key_env` för butiker med eget Klaviyo-konto). Analys: `sql/analys/epost_andel.sql`. Klaviyos tillskrivning är deras egen och summeras inte med Google eller Meta.

## Åtkomstkontroll
`site-audit check-access --site <sajt>` läser en rad från varje konfigurerad källa (BigQuery/Shopify, GA4, Google Ads, Meta, Merchant, Klaviyo) och visar OK, saknas eller FEL. Ändrar ingenting. Kör den för varje ny butik innan den läggs till i nattjobbet.

## Portföljrapport
`site-audit portfolio-weekly --site gorillasports-se [--out fil.md]` rangordnar butiker och marknader efter veckans orderförändring mot portföljens median och markerar avvikare (minst 15 procentenheter, minst 10 ordrar förra veckan). Kräver att portföljvyerna är skapade (`growth-sql`, portföljdelen; ännu inte skapad i BigQuery) och att fler butiker har `growth_views = true`.

## Tillägg 2026-10-22: sidmått i testloggen
Mätarna `gsc_clicks` och `gsc_impressions` mäter klick och visningar i Google för utvalda sidor (Search Console), efter åtgärdens start mot lika många dagar före. Kontrollen är övriga sidor med samma första led i adressen (till exempel övriga `/collections/`), så att säsong och Googles förändringar inte tillskrivs åtgärden. Search Console är slutgiltig efter ungefär tre dagar, så utvärderingen blir preliminär tills fönstret har passerat. Måttet kräver `--pages` (adressfragment, kommaseparerade) och att sajten har `gsc_table` i `sites.toml`.

```
site-audit test add --site gorillasports-se --start 2026-10-22 --channel site --metric gsc_clicks \
    --pages /collections/motionscykel-kondition,/collections/spinningcykel,/collections/crosstrainer-kondition \
    --hypothesis "Länkar mellan kategorierna och från bloggen ger fler klick" \
    --what "Länkblock i bloggartikeln, rena länkar och länkar mellan motionscykel och spinningcykel" --expect 10
site-audit test evaluate --site gorillasports-se --id <id> [--save]
```
Tabellen `site_audit.growth_tests` får vid första körningen en ny kolumn `pages` (`ALTER TABLE … ADD COLUMN IF NOT EXISTS`).

## Kommande utvärderingar
| Test | Butik | Start | Utvärdera | Kommando |
|---|---|---|---|---|
| 44de00d5 (kategorilänkar: motionscykel, spinningcykel, crosstrainer, mått `gsc_clicks`) | gorillasports-se | 2026-10-22 | 2026-11-23 (påminnelse inlagd) | `site-audit test evaluate --site gorillasports-se --id 44de00d5 --save` |
