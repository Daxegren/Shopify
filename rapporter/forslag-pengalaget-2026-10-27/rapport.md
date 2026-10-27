# Rapport: underlag för pengalaget på Gorilla Sports (ström 3, 2026-10-27)

## Sammanfattning
Jag har skrivit tre SQL-skript (med sammanlagt elva resultat) och ett webbläsartest som David kan köra i Cloud Shell för att se var pengarna försvinner, samt två förslagsdokument. Frågorna visar försäljning, trafik och annonser vecka för vecka på båda marknaderna, vilka storsäljare som tappat, vilka rabattkoder som bär rabatten och om spårningen laddar samma tagg två gånger. I de tidigare resultaten sitter tappet mest i Google-märkta ordrar och i produkter som tagit slut, och konverteringen har fallit ungefär 10 %; orsakerna är ännu inte bevisade. Break-even-ROAS beräknas till ca 2,7 (SE) och 2,9–3,0 (DK) med en osäker marginal, vilket betyder att Performance Max DK (ROAS 2,94) ligger vid noll i bidrag; ett test av lägre mål-ROAS kräver Davids och Rudes ja (nivå C) och bör föregås av en kontroll utan ändring. Inget har körts mot BigQuery eller någon butik, och inget är ändrat någonstans.

## Filer
| Fil | Rader | Innehåll |
|---|---|---|
| `shopify-sync/sql/analys/pengalage_veckovis.sql` | 251 | En datakontroll och fyra resultat (a–d), 61 rader totalt |
| `shopify-sync/sql/analys/storsaljare_tapp.sql` | 158 | De 30 största för 28–90 dagar sedan: veckoförsäljning, sista order, status, lager, annonsklick (högst 60 rader) |
| `shopify-sync/sql/analys/rabatter_koder.sql` | 68 | **Extra (ej beställd):** rabatt per kod och marknad, 28 mot 28 dagar |
| `shopify-sync/scripts/gtm_natverkstest.py` | 587 | Playwright-test av GTM-containrar, GA4-händelser och Meta-pixel, med och utan samtycke; `--test-logic` och `--selftest` |
| `rapporter/forslag-pengalaget-2026-10-27/roas-golv-och-dk-pmax.md` | 203 | Break-even-ROAS, hypotesen om PMax DK, testförslag (nivå C), falsifiering, vad som inte är känt |
| `rapporter/forslag-pengalaget-2026-10-27/atgardslista.md` | 172 | 12 prioriterade åtgärder med bevis, osäkerhet, vem, nivå och 99,9-bedömning; saknas och körningar |
| `rapporter/forslag-pengalaget-2026-10-27/rapport.md` | (denna) | |

Jag har inte committat. **Obs för samordnaren:** `git log` visar att `pengalage_veckovis.sql`, `storsaljare_tapp.sql` och `gtm_natverkstest.py` redan ingår i commit `c28af98` ("Ström 2: BOS experiment 1 ..."), alltså att en annan commit tagit med mina pågående filer. Innehållet är oförändrat sedan dess (`git status` är rent för dem). `rabatter_koder.sql` och rapportmappen är ospårade.

Ändringar utanför mina filer: inga. En sak i en fil jag inte äger bör rättas av samordnaren (se Öppna frågor, punkt 6).

## Verifierade namn
Alla tabell- och kolumnnamn i mina frågor finns i tidigare SQL i repot (fil:rad nedan) eller i koden som skapar tabellerna. Inga namn är gissade. `PROJ` = `gorilla-sports-data`.

| Tabell / kolumn | Verifierad i |
|---|---|
| `PROJ.shopify.orders` | `omsattning_30d.sql:21`, `cos_30d.sql:31` |
| `orders.created_at`, `cancelled_at` | `omsattning_30d.sql:17`, `:22` |
| `orders.presentment_currency` | `omsattning_30d.sql:20` |
| `orders.total_price_presentment` | `cos_30d.sql:30` |
| `orders.source_name`, `last_visit_utm_source`, `last_visit_source` | `omsattning_30d.sql:51` |
| `orders.subtotal_price`, `total_discounts` | `omsattning_30d.sql:29` |
| `orders.discount_codes` (kommaseparerad sträng) | **inte i någon tidigare SQL**; `sql/bigquery_schema.sql:21`, `src/shopify_sync/transform.py:68` (`_join`, rad 35–38) |
| `PROJ.shopify.order_line_items` | `omsattning_30d.sql:61` |
| `order_line_items.order_id`, `quantity`, `discounted_total`, `title` | `omsattning_30d.sql:61`, `:59`, `:60`, `:58` |
| `order_line_items.product_id` | `omsattning_tapp_per_produkt.sql:19` |
| `PROJ.shopify.products` med `id`, `status`, `total_inventory` | `omsattning_tapp_per_produkt.sql:29–30` |
| `products.title` | `cos_30d.sql:49` |
| `PROJ.shopify.product_variants` med `id`, `product_id` | `omsattning_tapp_annonser.sql:26–27` |
| `product_variants.inventory_quantity` | `sql/growth/views.sql:20`, `sql/bigquery_schema.sql:88` |
| `PROJ.site_audit.ga4_landing_daily_gorillasports_se` med `d`, `hostname`, `sessions`, `purchases` | `omsattning_30d.sql:65–74` |
| `PROJ.site_audit.google_ads_daily_gorillasports_se` med `d`, `currency`, `cost`, `conversions_value` | `cos_30d.sql:17–20` |
| `PROJ.site_audit.meta_ads_daily_gorillasports_se` med `d`, `currency`, `spend`, `purchase_value` | `cos_30d.sql:23–26` |
| `PROJ.site_audit.google_ads_products_daily_gorillasports_se` med `d`, `item_id`, `clicks` (och `currency`) | `omsattning_tapp_annonser.sql:30–34`, `cos_30d.sql:52` |
| Hostnamn `www.gorillasports.se`, `www.gorillasports.dk` | `omsattning_30d.sql:74` |
| Statusvärdet `ACTIVE` | `omsattning_tapp_per_produkt.sql:34` |
| Värden i `source_name`/utm-källa: `Google`, `google`, `Facebook`, `facebook`, `direct`, `adtraction`, `kelkoose`, `pricerunner`, `web`, `shopify_draft_order`, `chatgpt.com`, `Bing` | `omsattning-30d-resultat-2026-10-12.txt` (kanaltabellen), `trafik-konvertering-resultat-2026-10-13.txt` |
| Marknadsmappning SEK→SE, DKK→DK | `omsattning_30d.sql:20`, `cos_30d.sql:17` |
| GA4-tabellens schema (`d`, `hostname`, `sessions`, `purchases`, `revenue`) | `src/site_audit/google_api.py:33–35` |
| Vyerna `growth_*` skapas i `site_audit` (relevant för punkt 6 nedan) | `src/site_audit/growth_sql.py:134`, `src/site_audit/config.py:84` |

**Det som är nytt i mina frågor och inte hämtat från tidigare resultat:** kanalgrupperingen i `pengalage_veckovis.sql` del c (google / meta / direkt / epost_affiliate / ovrigt). Någon sådan gruppering finns inte i `trafik-konvertering-resultat-2026-10-13.txt`; där visas bara den råa kanalen (`COALESCE(NULLIF(last_visit_utm_source,''), NULLIF(last_visit_source,''), source_name, 'okänd')`, som jag använder oförändrad). Indelningen bygger på de värden som syntes i resultatet. `instagram`, `fb`, `ig`, `meta`, `klaviyo`, `email`, `newsletter`, `nyhetsbrev` och `epost` syntes inte i resultatet och är försiktiga tillägg; "pricerunner" och "kelkoose" (jämförelsetjänster) har lagts i gruppen e-post och affiliate enligt uppdraget.

## Hur David kör det
Kör i Cloud Shell i `~/Shopify/shopify-sync` efter `git pull` (samordnaren committar). Allt är läsning. Klistra in utdata, så läser jag det.

```bash
# 1. Finns tabellerna och är de färska? (Merchant och Klaviyo förväntas saknas för Gorilla)
KEY=gorillasports bash scripts/kontrollera_datakallor.sh

# 2. Pengaläget: datakontroll + (a) försäljning, (b) trafik och annonser, (c) kanalgrupper, (d) 28 mot 28 mot fjol. Läs datakontrollen först.
sed 's/PROJ/gorilla-sports-data/g' sql/analys/pengalage_veckovis.sql | bq query --use_legacy_sql=false --max_rows=100 | tee pengalage.txt

# 3. Storsäljare som tappat: datakontroll, 30 produkter per marknad, avstämning
sed 's/PROJ/gorilla-sports-data/g' sql/analys/storsaljare_tapp.sql | bq query --use_legacy_sql=false --max_rows=100 | tee storsaljare.txt

# 4. Rabattkoder (extra)
sed 's/PROJ/gorilla-sports-data/g' sql/analys/rabatter_koder.sql | bq query --use_legacy_sql=false --max_rows=100 | tee rabatter.txt

# 5. GTM-nätverkstest (kräver Playwright: pip install playwright && playwright install chromium)
python3 scripts/gtm_natverkstest.py --test-logic        # enhetstest, ingen webbläsare
python3 scripts/gtm_natverkstest.py --selftest          # lokal testsida, ska sluta med SJÄLVTEST OK
python3 scripts/gtm_natverkstest.py --url https://www.gorillasports.se/ --out gtm-gorilla-se
python3 scripts/gtm_natverkstest.py --url https://www.gorillasports.dk/ --out gtm-gorilla-dk
python3 scripts/gtm_natverkstest.py --url https://www.gorillasports.se/products/<en-produkt> --out gtm-gorilla-se-produkt
```
Övriga körningar som atgardslista.md pekar på (annonser på produkter som inte går att köpa, priser strax under fraktgränsen, långköraren) finns med exakta kommandon i slutet av `atgardslista.md`.

### Utdata från testerna i min miljö
Enhetstest: `Enhetstest av räknelogiken: alla kontroller godkända.` (32 kontroller, varav flera som ska ge *ingen* flagga).

Självtest mot lokal testsida (en enkel HTTP-server som jag startar själv; sidan har tre `gtm.js`-taggar för `GTM-TESTAAA` (två med exakt samma adress), en för `GTM-TESTBBB`, och två för `GTM-TESTCCC` med olika adresser; attrappen skickar GA4-händelser och Meta-pixel). Testet startade Chromium (förinstallerad i `/opt/pw-browsers`, `--no-sandbox`); Playwrights egen nedladdning blockeras i miljön och behövs inte i Cloud Shell:

```
Typ                     Id           Händelse         A före samtycke  B efter klick  C ny laddning  Flagga
GTM-container (gtm.js)  GTM-TESTAAA  gtm.js           1                0              1              <-- kontrollera
GTM-container (gtm.js)  GTM-TESTBBB  gtm.js           1                0              1
GTM-container (gtm.js)  GTM-TESTCCC  gtm.js           2                0              2              <-- kontrollera
GA4-händelse            G-TEST1111   page_view        2                0              2              <-- kontrollera
GA4-händelse            G-TEST1111   scroll           1                0              1
GA4-händelse            G-TEST1111   user_engagement  1                0              1
Meta-pixel              PIXEL111     PageView         0                2              2              <-- kontrollera
  A+B: GTM-TESTAAA: 2 / 0, GTM-TESTBBB: 1 / 0, GTM-TESTCCC: 2 / 0; gtm.js-händelser i dataLayer: 5
SJÄLVTEST OK: tabellen och flaggorna stämmer med vad testsidan är byggd att göra.
```
Självtestet gav en lärdom som styr hur skriptet fungerar: **webbläsaren gör bara ETT nätverksanrop när samma `gtm.js`-adress laddas två gånger, men skriptet körs ändå två gånger** (AAA: nätverksräkning 1, men två skriptelement i DOM och två `page_view`). Ett test som bara räknar nätverksanrop hade därför missat dubbelladdningen. Skriptet flaggar även via DOM (antal skriptelement och inbyggda laddningsskript) och antalet `gtm.js`-händelser i dataLayer. Den första versionen av skriptet missade just detta; självtestet fångade det. Två identiska bildanrop (Meta-pixeln utan `ts`) slås på samma sätt ihop; den riktiga pixeln har `ts` i adressen.

SQL-frågorna har kontrollerats med `sqlglot` (dialekt BigQuery, `PROJ` ersatt med projektnamnet; samma metod som `tests/test_site_audit.py`) och logiken har körts i DuckDB mot syntetiska tabeller med samma kolumner (en testharness utanför repot) för att se att veckogränser, NULL-hantering, kanalgrupper och avstämningar beter sig som beskrivet: summan av kanalgrupperna är lika med ordrarna i del a, veckor före äldsta order blir NULL, fjolårsperioden blir NULL när data saknas, och en storsäljare som slutat sälja hamnar överst. Det bevisar inte att frågorna går igenom i BigQuery (se Öppna frågor, punkt 1). Repots tester: `97 passed, 1 skipped` efter mina tillägg.

## Öppna frågor och osäkerheter
1. **Frågorna är inte körda mot BigQuery.** Syntaxen är kontrollerad med sqlglot och logiken med en DuckDB-simulering på påhittade data. BigQuery-specifika detaljer kan avvika (till exempel typtvång i `UNION ALL`, `DECLARE` med underfråga, `INTERVAL (uttryck) DAY`). Ett fel visar sig direkt vid första körningen och kräver bara en rättning.
2. **Orderhistoriken.** Shopify-ordrar finns troligen bara 60 dagar bakåt (`read_all_orders` saknas, `beslut-2026-10-12-2.md`), vilket gör att de äldsta veckorna i del a och c blir NULL och rangordningen i `storsaljare_tapp.sql` (28–90 dagar) bygger på färre dagar än 63. Båda frågorna visar `orderdata_fran` och antalet dagar som finns. Frakt-frågorna kördes dock på 90 dagar (`beslut-2026-10-26.md` §19–20), så historiken kan vara längre än 60 dagar; datakontrollen avgör.
3. **GA4 och annonser släpar.** Perioderna i del d slutar på den senaste dag som GA4, Google Ads och Meta alla täcker, högst i går. Fjolåret blir NULL tills data finns (GA4 börjar 2026-03-19/20).
4. **Kanalen "Google" är inte Google Ads.** Shopifys `last_visit_source` blandar betald och organisk Google-trafik. GA4:s kanaltabell (`ga4_channel_daily_gorillasports_se`) skulle skilja dem; den ingår inte i min fråga eftersom kolumnerna `channel`/`source_medium` är kända bara från koden, inte från en körd fråga.
5. **Lagerstatus är dagens ögonblicksbild** (ingen lagerhistorik). "Slut i lager nu" i `storsaljare_tapp.sql` säger inte när varan tog slut.
6. **Troligt fel i en fil jag inte äger:** `epost_andel.sql` läser `PROJ.shopify.growth_daily_KEY`, men vyerna `growth_daily_<nyckel>` skapas i datasetet `site_audit` (`growth_sql.py:134`, `config.py:84`), inte i `shopify`. Dessutom är Klaviyo inte påslaget för Gorilla (`klaviyo_enabled` saknas i `sites.toml`; standard `false`). Jag har inte ändrat filen.
7. **GTM-testet är en heuristik.** Samtyckesknappen hittas på text (som i `samtycke_test.py`); Shopifys ruta visas bara i vissa regioner och testet körs från ett datacenter. Dubblettregeln (samma typ, id, namn och sidadress inom 2 s) kan ge falska träffar för händelser som legitimt upprepas (scroll, user_engagement). DOM-kontrollen av inbyggda laddningsskript letar efter standardformen på GTM-snutten med datalagret som tredje argument; en annan form eller ett eget namn på dataLayer räknas inte. Server-side GTM kräver `--extra-host`. **Testet är bara körd mot min lokala testsida, inte mot Gorillas butik.**
8. **Marginalen är inte säkerställd** (vad `unit_cost` är, DK-bidragets 43,3 mot 41,2 %, moms i plattformens värde, fasta mot rörliga kostnader). Allt i `roas-golv-och-dk-pmax.md` avsnitt 1 är därför skattningar med intervall.
9. **Ingen av åtgärderna uppfyller riktlinjen 99,9 %** utom sådant som är ren läsning, eftersom de rör annonser, pris, spårning eller mallar (`atgardslista.md`). De är förslag på nivå A/B/C.
10. **Rudes svar** på frågan om mål-ROAS ändrats (beslut N, `beslut-2026-10-14.md`) finns inte i några filer jag läst.

## Täckning
**Läst fullt ut:** `CLAUDE.md`, `shopify-sync/docs/LARDOMAR.md`, `shopify-sync/docs/arbetsstrommar.md` (inklusive riskprofilen 2026-10-27), `rapporter/trafik-konvertering-resultat-2026-10-13.txt`, `rapporter/omsattning-30d-resultat-2026-10-12.txt`, `rapporter/annonser-resultat-2026-10-14.txt`, `rapporter/tackningskarta-2026-10-26.md`, `shopify-sync/docs/tillvaxtdata.md`, `rapporter/beslut-2026-10-26.md` avsnitt 7–20, och SQL-filerna `omsattning_30d.sql`, `omsattning_tapp_annonser.sql`, `omsattning_tapp_per_produkt.sql`, `annonser_kampanjer_30d.sql`, `annonser_pa_slutsalda.sql`, `annonser_vecka.sql`, `cos_30d.sql`, `marginal_30d.sql`, `marginal_stickprov.sql`, `net_profit_ordrar.sql`, `merchant_avvisade.sql`, `epost_andel.sql`, samt `scripts/kopflode_test.py` och `scripts/samtycke_test.py` (som mönster).
**Läst delvis (kommentarer, struktur och huvudfrågor, inte varje rad):** `frakt_samband.sql`, `frakt_tippande.sql` (resultaten är lästa via `beslut-2026-10-26.md` §19–20; rådata fanns inte), `marginal_stickprov.sql` (korthuvudet), `beslut-2026-10-26.md` avsnitt 21–31 (översiktligt, eftersom de rör BOS och tema), `beslut-2026-10-14.md`, `beslut-2026-10-12-2.md`, `beslut-2026-10-18-7.md` (månadstabellerna; avsnitt 6 om produkttapp per produkt ej läst), `standardtester.md` (T23–T26, T30–T40), `ANDRINGSLOGG.md` (utvalda rader), `sites.toml`, `sql/growth/views.sql`, `src/site_audit/growth_sql.py`, `src/site_audit/config.py`.
**Inte läst:** `priser_strax_under_gransen.sql` utöver rubrikkommentaren, BOS-underlagen, Google Ads, Merchant Center, Shopify admin, arken ("SWE - Net Profit", "Contribution_Model"), och Gorillas riktiga sajt (inget nätverk). Ingen fråga har körts mot BigQuery; ingen webbläsare har öppnat en riktig butik.
