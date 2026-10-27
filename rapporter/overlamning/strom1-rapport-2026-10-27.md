# Ström 1: rapport 2026-10-27 (hjälpagent)

## Sammanfattning
Testloggen har fått åtgärdstyper med egna utvärderingsfönster (56, 28, 21, 21 dagar) och det nya kommandot `site-audit test due`. Datakällskriptet hade två fel som nu är rättade: Merchant-tabellens datumkolumn heter `d` (inte `snapshot_date`), och för Gorilla stämde varken Shopify-datasetet (`shopify`) eller nyckeln för GA4, annonser och Merchant (`gorillasports_se`). Övriga namn är bekräftade mot koden, utom Gorillas DK-tabeller som inte kunde bevisas. Designskissen för utför-ramverket (T39) är skriven, ingenting är byggt. Alla tester är gröna: 97 godkända, 1 överhoppat.

## Ändrade filer (radantal enligt `git diff --stat` mot föregående commit)
| Fil | Rader |
|---|---|
| `shopify-sync/src/site_audit/growth_tests.py` | +80 / −10 (nu 264 rader) |
| `shopify-sync/src/site_audit/main.py` | +13 / −7 (nu 668 rader) |
| `shopify-sync/scripts/kontrollera_datakallor.sh` | +16 / −7 (nu 51 rader) |
| `shopify-sync/tests/test_site_audit.py` | +121 / −0 (4 nya tester; inga befintliga ändrade) |
| `rapporter/overlamning/strom1-utfor-ramverk-design-2026-10-27.md` | ny, 138 rader |
| `rapporter/overlamning/strom1-rapport-2026-10-27.md` | ny (den här) |

Notera: samordnaren hann committa mina kodändringar (`8edd308`) innan jag var klar med rapporten; stat-siffrorna ovan är ungefärliga uppdelningar av commitens totalsiffror (growth_tests 90, main 20, skript 23 rader ändrade). Jag har själv inte committat eller pushat något.

### Uppdrag 1: vad som gjordes
- **Viktig upptäckt:** fönstret var redan sparat per test (`evaluate_days`, skrivs av `add_test`, `growth_tests.py` i INSERT) och `evaluate` använde redan det sparade värdet (`main.py`, `span = ...`). Det som var fast var *förvalet* 28 (`--days` default 28) och att det inte gick att välja efter åtgärdstyp. Jag lade därför **inte** till en ny fönsterkolumn, eftersom `evaluate_days` redan är den. Ny kolumn är bara `kind STRING` (åtgärdstypen, som etikett). Säg till om du hellre vill ha en separat fönsterkolumn.
- `test add --kind {seo_text,technical,ads,price}`: förval 56, 28, 21, 21. `--days` (alias `--window-days`) går före `--kind`; utan båda 28 som förut. Giltigt spann är oförändrat 7–90.
- Migreringen är ett enda uttryck (`ADD COLUMN IF NOT EXISTS pages STRING, ADD COLUMN IF NOT EXISTS kind STRING`) så att ordningen på frågorna i `add_test` är densamma och befintliga tester inte behövde ändras.
- `window_days(test)`: saknat värde, `None` eller NaN ger 28; används av `evaluate`, `evaluate_pages` och `cmd_test`.
- `test due --site X [--today ÅÅÅÅ-MM-DD]` (`--date` fungerar också): lista över tester som inte är `utvärderad` där idag ≥ start + fönster + 4 dagar. Visar id, åtgärd, förväntat utfall, mått, fönster, fönstrets sista dag och hur många dagar sedan den dagen, samt när testet blev utvärderingsbart. Avslutar med en rad om hur många som inte är klara än och närmast kommande datum, och antal redan utvärderade. Status `pågår` (preliminärt sparad) räknas som ej utvärderad. **Tolkning:** "fönstret gick ut" = fönstrets sista dag (start + fönster − 1); gränsen för listning är start + fönster + 4 (för test 44de00d5: 2026-11-23, vilket stämmer med `tillvaxtarbete.md` rad 43).
- Verifierat: `site-audit test --help` och `test add|list|evaluate|due --help` svarar (kört som `python -m site_audit.main`).

## Testresultat
Kommando: `cd /home/user/Shopify/shopify-sync && .venv/bin/python -m pytest -q tests`
```
......s................................................................. [ 73%]
..........................
97 passed, 1 skipped in 1.14s
```
Före: 93 godkända, 1 överhoppat. Nya tester (alla utan BigQuery, med fakes): `test_growth_test_window_per_kind` (förval per kind, uttryckligt fönster går före, okänd kind och 91 dagar avvisas, migrering), `test_growth_test_old_row_without_window_gives_28` (saknat/None/NaN ger 28, `evaluate` använder 56 resp. 28 dagars efterfönster), `test_growth_test_due_boundaries` (dagen före 2026-11-22: ej klar; exakt 2026-11-23: klar, 0 dagar; efter: 3 dagar; 56-dagarstest klart först 2026-12-21; utvärderade räknas men listas inte; `pågår`; datum som text; utskriftsformat), `test_cli_test_subcommands_and_due` (hjälptexter, `due` via `main()` med `--today`, `add --kind seo_text` ger 56 i INSERT). Inga befintliga tester ändrades.
`bash -n scripts/kontrollera_datakallor.sh`: ingen utskrift, felkod 0.

## Verifiering av tabellnamnen (uppdrag 2)
"Koden" nedan är sökvägar relativt `shopify-sync/`. `key` = `SiteConfig.table_key` (= `data_key`, annars sajtnamn med `_`, `config.py:139-141`); `slug` = sajtnamn med `_` (`config.py:135-137`).

| Källa | Tabellnamn enligt koden | Datumkolumn | Bevis (fil:rad) | Ändrat? |
|---|---|---|---|---|
| Search Console, kombinerad vy | `site_audit.gsc_combined_<nyckel>_<se\|dk\|fi>` | `data_date` | Vyer: `sql/audit/views_sources.sql:8` (gorillasports se), `:19` (dk); `sql/audit/views_sources_bestofsports.sql:7,17,27` (se, dk, fi). Kolumn: `views_sources.sql:9-10` (`SELECT data_date, ...`). Används som `gsc_table`: `sites.toml:30,75,105,139,162` | Namnet rätt. **Gorilla har bara se och dk** (ingen fi-vy): skriptet loopar nu `se dk` för `KEY=gorillasports` |
| Search Console, API-historik | `site_audit.gsc_api_url_<slug>` (för `bestofsports_se` = `gsc_api_url_bestofsports_se`) | `data_date` | Namn: `src/site_audit/main.py:262`; schema: `src/site_audit/google_api.py:26-27`; laddning med `("data_date", ...)`: `main.py:263` | Nej (rätt) |
| GA4 landningssidor | `site_audit.ga4_landing_daily_<key>` | `d` | Namn: `main.py:284`; schema `google_api.py:32-33`; `("d", ...)` `main.py:286`; `sites.toml:32,108` | Nej för BOS. För Gorilla är `<key>` = `gorillasports_se` (inte `gorillasports`): **rättat** via ny variabel `DATAKEY` |
| GA4 kanaler | `site_audit.ga4_channel_daily_<key>` | `d` | Namn: `main.py:281`; schema `google_api.py:38-39` | Samma som ovan |
| Shopify ordrar | `<dataset>.orders` | `created_at` (TIMESTAMP) | `src/shopify_sync/schema.py:53-60` (tabell `orders`, `created_at`); dataset från `BQ_DATASET`, standard `shopify` (`shopify_sync/config.py:65`; `deploy/cloudrun.sh:25`); `sites.toml:34` (Gorilla: `shopify`), `:109` (BOS: `shopify_bestofsports`) | **Ja:** standarden `shopify_${KEY}` var fel för Gorilla (datasetet heter `shopify`). BOS rätt |
| Google Ads per dag | `site_audit.google_ads_daily_<key>` | `d` | Namn `main.py:294`; schema `src/site_audit/ads_api.py:31-32`; `main.py:297` | Som GA4 (Gorilla: `_gorillasports_se`) |
| Google Ads per produkt | `site_audit.google_ads_products_daily_<key>` | `d` | `main.py:294`; `ads_api.py:37-38` | Som GA4 |
| Merchant | `site_audit.merchant_products_<key>` | **`d`**, inte `snapshot_date` | Namn `main.py:315`; schema `src/site_audit/merchant_api.py:20-21` (`("d", "DATE", "REQUIRED")`); `main.py:317` `("d", today, today)`; SQL som läser den använder `d`: `sql/analys/merchant_avvisade.sql:11`, `sql/analys/bos/7_merchant_problem.sql:5`. `snapshot_date` förekommer ingenstans i repot utom i skriptet | **Ja: `snapshot_date` rättat till `d`.** Detta hade gett fel "Unrecognized name" på varje körning |

Bekräftat utan ändring: dataset-delen `site_audit` (standard `bq_dataset`, `config.py:84`), projektet `gorilla-sports-data` (`sites.toml:5`), BOS nyckel `bestofsports` (`sites.toml:101,135,158`).

**Obekräftat (ändrat inte):**
- Att tabellerna faktiskt *finns* och är färska i BigQuery: jag har ingen åtkomst. Det avgörs av att David kör skriptet.
- Gorillas DK-sajt har egna tabellnamn enligt `sites.toml:77` (`ga4_landing_daily_gorillasports_dk`), men om nattjobbet fyller dem eller bara `_se` (som i SQL-filerna) är inte undersökt (`deploy/` ej genomläst för detta). Skriptet kontrollerar bara `_se`-tabellerna för Gorilla; `DATAKEY=gorillasports_dk` kan skrivas över.
- Att Gorilla har Merchant-data: `sites.toml` har inget `merchant_account_id` för Gorilla (bara BOS, `:113`), så en rad "SAKNAS" för Merchant vid `KEY=gorillasports` är väntad, inte ett fel.
- GSC-vyn kan saknas tills bulkexporten skapat `searchdata_url_impression` (`standardtester.md:63`); inte ett namnfel.

## Öppna frågor och osäkerheter
1. Fönstret lagras i den befintliga kolumnen `evaluate_days`; `kind` är bara en etikett. Ska `kind` också styra något annat (till exempel veckorapporten T38)? Inte byggt.
2. `due` listar bara på tid. Veckorapporten "över tester vars fönster gått ut, med resultat" (T38) kör inte `evaluate` automatiskt; det kräver BigQuery och är inte byggt.
3. Rad i `standardtester.md` ("Testloggen... fönstret är 28 dagar", rad 156, och T8-raden) blir inaktuell när detta driftsätts. Jag har inte rört dokumenten (utanför mitt ägande); samordnaren bör lägga till markering enligt `CLAUDE.md` regel 4.
4. Koden är inte driftsatt. Kolumnen `kind` skapas första gången `add`/`list` körs mot BigQuery (`ALTER TABLE ... ADD COLUMN IF NOT EXISTS`); den kombinerade ALTER med två kolumner är inte körd mot riktiga BigQuery (bara syntax-/strängtestad). **Hypotes:** BigQuery tillåter flera `ADD COLUMN IF NOT EXISTS` i ett uttryck; det är dokumenterat beteende enligt min kunskap men inte provat här. Om det skulle felas faller `add`/`list` med fel vid första körningen, så gör ett första `site-audit test list` före verklig användning.
5. Skriptet har fortfarande bara Gorilla-SE som "Gorilla"; DK/övriga se ovan.
6. Designskissens Shopify-specifika påståenden (mutationsnamn, kostnad per mutation, scopes) är **obekräftade**; se skissens avsnitt 2.4 och 4.
7. `CLAUDE.md` kräver en beslutsfil `rapporter/beslut-ÅÅÅÅ-MM-DD.md` efter arbetspasset och loggrader till `rapporter/logg/strom1-<datum>.md`. Jag skrev ingen (inte i min äganderätt/uppdrag); samordnaren behöver föra in: ändring av `growth_tests.py`, `main.py`, `kontrollera_datakallor.sh`, tester, två nya dokument. Ingenting ändrades i Shopify.

## Täckning
**Läst fullt ut:** `/home/user/Shopify/CLAUDE.md`, `docs/LARDOMAR.md`, `docs/arbetsstrommar.md`, `docs/tillvaxtarbete.md`, `src/site_audit/growth_tests.py`, `scripts/kontrollera_datakallor.sh`, `scripts/redirects_gorilla_apply.py`, `sql/audit/views_sources.sql` (rad 1–35), `sites.toml` (delar: blocken för gorillasports-se/dk och bestofsports-se samt rad med `data_key`).
**Läst delvis:** `docs/standardtester.md` (rutinen rad 27–37, T8-raden, tillägget rad 145–213; inte T1–T29), `src/site_audit/main.py` (rad 1–40, 245–335, 436–530, 610–668; inte `run`, `inspect` m.fl.), `src/site_audit/google_api.py`, `ads_api.py`, `merchant_api.py` (bara schemablocken), `src/shopify_sync/schema.py` (orders-tabellen), `config.py` (båda), `shopify_client.py` (rad 50–90), `deploy/cloudrun.sh` (grep), `sql/audit/views_sources_bestofsports.sql` (rad 1–20 samt grep), SQL-filer under `sql/analys` och `sql/growth` (bara grep på tabellnamn).
**Inte läst:** `deploy/**` i övrigt (vad nattjobben faktiskt fyller), `src/site_audit/access_check.py` utöver grep, `actions.py`, `shopify_admin.py`, `sites.toml` för DK/FI-blocken i detalj, tidigare `rapporter/`. Inga anrop mot Shopify, Google Cloud eller nätverk gjordes.
