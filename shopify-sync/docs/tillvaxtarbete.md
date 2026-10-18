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
