# Standardtester och rutiner för varje sajt

Tillägg 2026-10-22. Det här är de tester och arbetssätt som togs fram på gorillasports.se och som ska göras på varje ny sajt. Dokumentet kompletterar `basgenomgang.md` (vad som granskas), `tillvaxtarbete.md` (testloggen) och `ny-sajt.md` (hur en sajt kopplas in). Varje test har fått med de fallgropar vi faktiskt råkade ut för.

## Grundregler
1. **Läsning först.** Alla tester är skrivskyddade. Ingenting ändras i Shopify, Search Console eller annonsplattformar utan Davids uttryckliga ja.
2. **En åtgärd, ett test.** Varje ändring som görs loggas i testloggen med hypotes, startdatum, mått och förväntat utfall, och utvärderas efter en bestämd tid.
3. **Siffror före åsikter.** Extern rapport och gissningar prövas mot egna data innan något görs.
4. **Allt dokumenteras:** ändringslogg, beslutsunderlag per arbetspass, före-och-efter-filer för varje ändring.

## Testkatalog
Platshållare: `PROJ` = Google Cloud-projektet, `KEY` = butikens tabellnyckel (`table_key`, till exempel `gorillasports_se`), `HOST` = domänen (till exempel `gorillasports.se`), `GSCTABLE` = tabell med sökfrågor (se T4).

| Nr | Test | Visar | Kör | Fallgropar vi hittat |
|---|---|---|---|---|
| T1 | Teknisk genomlysning | Fynd i indexering, omdirigeringar, metadata, schema, innehåll, prestanda; `actions.csv` och färdiga 301:or | `site-audit run --site <sajt> --bigquery --search-data` | Tre kontroller tillkom 2026-10-20: kod-/AI-rester i produkttext, interna länkar med spårningsparametrar, produktschema utan omdömen. `product_text_residue` är en heuristik som läser textversionen och ser inte HTML-attribut |
| T2 | Åtkomst och datakvalitet | Vilka källor som fungerar, och om siffrorna går att lita på | `site-audit check-access --site <sajt>`, `sql/growth/datakvalitet.sql` | Kräver ny avbildning av nattjobbet innan kommandona finns där; lokalt i Cloud Shell: `pip install -e '.[all]'` (utan `[all]` saknas Googles bibliotek) |
| T3 | Döda produktsidor med trafik | Produktsidor som inte längre är aktiva men får besök (underlag för 301) | `sed -e 's/PROJ/…/g' -e 's/KEY/…/g' -e 's/HOST/…/g' sql/analys/doda_sidor_med_trafik.sql \| bq query --use_legacy_sql=false` | **Filtrera alltid på domän (HOST).** GA4-egenskapen delas av flera domäner. På marknader med översatta adresser (gorillasports.dk) matchar inte handle mot Shopify och ger bara falska träffar; där används genomsökningen i T1. Köp på en "saknad" sida betyder att den fungerar |
| T4 | Sökfrågor med lucka | Frågor och köpguide-sökningar där en sida rankar på plats 4–20 men får få klick | `sql/analys/sokfragor_luckor.sql` med `GSCTABLE` | **Bulkexporten börjar först den dag den slogs på** (för Gorilla 2026-10-07): kontrollera `MIN(data_date)`. Historik med sökfrågor hämtas med `backfill gsc --queries --since <datum>` (API:et ger inte anonymiserade frågor; cirka 36 % av visningarna är dolda). Förväntad CTR per position är en grov tumregel som överskattar vad som går att vinna på informationsfrågor |
| T5 | Kategorisökord | Vilka sidor som rankar på ett sökord och vilka närliggande frågor som skrivs | `sql/analys/kategori_sokord.sql` (byt sökorden) | Externa sökvolymer och rankingar stämde inte med Search Console (en rapport sa "No rank" på ett sökord där sajten låg på plats 2,6). Search Console gäller. Kolumnnamn i frågan får inte krocka med resultatkolumner (BigQuery gav "Aggregations of aggregations") |
| T6 | Sidhastighet | Verkliga besökares LCP/INP/CLS och labbvärden för startsida, kategori, produkt och blogg | `scripts/psi_snapshot.py` med `PSI_API_KEY` | **Fältdata (verkliga besökare) gäller, inte labbet.** Extern rapport sa LCP 5,8 s och underkänt; verkliga besökare hade 1,1–1,5 s. Nyckeln skapas i Cloud Console och matas in med `read -rs`; `gcloud services api-keys create` skriver ut nyckeln i terminalen. Utan nyckel är den delade gratiskvoten slut |
| T7 | Extern genomlysning (valfritt) | Synlighet mot konkurrenter, länkprofil, sökordsluckor | Extern tjänst, manuellt | Uppsidor i procent är verktygets uppskattning. Samma siffra på orelaterade poster (till exempel 1 191) är en artefakt. Korrelation med Googles uppdateringar är inte orsak. FAQ-schema ger sällan synliga utdrag |
| T8 | Testlogg | Effekten av varje åtgärd | `site-audit test add/list/evaluate`, mått `orders`, `revenue`, `sessions`, `ad_cost`, `mer`, `order_rate`, `gsc_clicks`, `gsc_impressions` | Sidmått kräver `--pages`. Search Console är slutgiltig efter cirka tre dagar, så utvärdera tidigast fyra dagar efter att 28-dagarsfönstret slutat. **Sätt en påminnelse när testet loggas.** Kontrollen är grov (övriga sidor av samma typ eller övriga marknader) |
| T9 | Veckorapport och portföljrapport | Nyckeltal, larm och jämförelse mellan butiker | `site-audit weekly --site <sajt>`, `site-audit portfolio-weekly --site <sajt>` | Kräver `growth_views = true` och skapade vyer (`site-audit growth-sql`) |
| T10 | Merchant Center och Klaviyo | Avvisade produkter med annonsklick; e-postens andel av ordrarna | `sql/analys/merchant_avvisade.sql`, `sql/analys/epost_andel.sql` | Svarsformerna är inte verifierade mot riktiga konton; kräver `merchant_account_id` respektive `klaviyo_enabled` |

## Rutin för ändringar i Shopify
Gäller varje ändring av text, länkar, titlar eller metadata. Den här ordningen togs fram efter att ett avskrivningsfel upptäcktes (stavfel som uppstod när text skrevs av för hand).
1. **Läs** nuvarande text och spara den som fil i `rapporter/shopify-original-<datum>/` (exakt kopia, inklusive HTML och SEO-fält). Shopify har ingen ångra-funktion för kollektionstexter.
2. **Visa före och efter** för David, med de exakta orden. Vänta på ett uttryckligt ja per ändring (eller per tydligt avgränsad grupp).
3. **Skriv aldrig om en lång text för hand.** Bygg den nya texten av den sparade originalfilen med ett skript som bara gör de godkända ersättningarna, så att allt annat är identiskt.
4. **Skriv** med Shopify Admin API och **läs tillbaka** texten.
5. **Jämför tecken för tecken** mot originalet: `python3 scripts/diff_text.py <före> <efter>`. Bara de godkända ändringarna får skilja. Rätta och jämför igen tills det stämmer.
6. **Logga**: `docs/ANDRINGSLOGG.md`, `rapporter/shopify-andringar-<datum>.md` (före och efter) och beslutsunderlaget för dagen.
7. **Logga ett test** (T8) och sätt en påminnelse för utvärderingen.

Skrivrättigheter i Shopify-kopplingen bör stå på "fråga" så att varje ändring bekräftas i verktygsprompten.

## Så körs standardtesterna på en ny butik
1. Lägg till butiken enligt `ny-sajt.md` och `flera-sajter.md` (nivå A–C). Börja med T2.
2. Kontrollera datumet då Search Console-exporten startade; hämta sökfrågor bakåt med `backfill gsc --queries` om historik behövs (T4).
3. Kör T1, T3 (bara domäner utan översatta adresser), T4, T5 och T6. Rangordna fynden efter besök och intäkt innan något föreslås.
4. Föreslå ändringar till David med före och efter (rutinen ovan), logga i testloggen (T8).
5. Skriv beslutsunderlaget och ändringsloggen enligt `CLAUDE.md`.

## Var sakerna ligger
| Vad | Var |
|---|---|
| Analysfrågor | `shopify-sync/sql/analys/` och `shopify-sync/sql/growth/` |
| Verktyg | `shopify-sync/src/site_audit/`, `shopify-sync/scripts/` |
| Ändringslogg | `shopify-sync/docs/ANDRINGSLOGG.md` |
| Beslutsunderlag per arbetspass | `rapporter/beslut-<datum>.md` |
| Före/efter och original | `rapporter/shopify-andringar-<datum>.md`, `rapporter/shopify-original-<datum>/` |
| Testlogg | BigQuery: `site_audit.growth_tests` |

## Körning från Cloud Shell: inloggning mot Google-API:erna
Cloud Shells standardinloggning har inte omfång för Search Console eller GA4, så `backfill gsc` och `backfill ga4` ger "403 ACCESS_TOKEN_SCOPE_INSUFFICIENT" (upptäckt 2026-10-22). Nattjobbet påverkas inte, eftersom det kör som tjänstkontot. I Cloud Shell loggar du in en gång så att verktygen får rätt omfång, och helst som tjänstkontot, så att samma åtkomst provas som i produktion:
```
gcloud auth application-default login --impersonate-service-account=shopify-sync@gorilla-sports-data.iam.gserviceaccount.com
```
Du loggar in med ditt eget konto (länk och kod). Ger det felet `iam.serviceAccounts.getAccessToken` saknar du rollen *Service Account Token Creator* på tjänstkontot; då kan du i stället logga in som dig själv (du måste vara ägare av egendomen i Search Console): `gcloud auth application-default login --scopes=https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/webmasters.readonly,https://www.googleapis.com/auth/analytics.readonly`. Verktygen läser bara data.

Search Console-vyerna (`sql/audit/views_sources_*.sql`) kan inte skapas förrän massexporten skapat tabellen `searchdata_url_impression` i datasetet (1–2 dygn efter att exporten slogs på); fel "Table … searchdata_url_impression was not found" före dess är väntat.

## Tillägg 2026-10-23: fler genomgående tester (T11–T20)
Förslag på tester utöver T1–T10, framtagna för Best of Sports men avsedda för varje sajt. Status anger vad som är byggt och testat och vad som kräver beslut, nyckel eller mer arbete. Allt är skrivskyddat.

| Nr | Test | Visar | Status | Kör |
|---|---|---|---|---|
| T11 | Mätintegritet | Stämmer GA4-köp, annonskonverteringar och Shopify-ordrar per vecka? Saknad tagg, trasig köphändelse, dubbelräkning, samtyckesproblem | **Klart** | `sql/analys/matintegritet.sql` (PROJ, KEY, SHOPDS) |
| T12 | Köpflöde (mobil och desktop) | Var stannar en besökare: startsida, kategori, produkt, lägg i varukorg, varukorg, kassa. Tider, konsolfel, saknad frakt- och returinfo, inaktiv köpknapp, tom varukorg | **Klart, testad mot en låtsasbutik** (inte mot en riktig butik än) | `python3 scripts/kopflode_test.py --base-url <butik> --collection <kategori> --viewport mobile` (kräver Playwright, se skriptets huvud) |
| T13 | AI-synlighet (GEO), del 1: trafik och åtkomst | Hur mycket trafik kommer från ChatGPT, Perplexity, Gemini, Copilot, Claude; får AI-botar läsa sajten? | **Klart** | `sql/analys/ai_hanvisningar.sql`; fyndet `ai_crawlers_blocked` eller `ai_crawlers_allowed` i T1 |
| T13b | GEO, del 2: citeringspanel | Nämns eller citeras sajten när AI-tjänster svarar på 30–50 fasta frågor per marknad, och vilka konkurrenter nämns i stället? Körs månadsvis, sparas i BigQuery | **Behöver beslut:** kräver API-nycklar (läggs i Secret Manager, aldrig i chatten) och en kostnad per körning. Bygg först när frågepanelen är godkänd | – |
| T14 | Produktdata | Andel aktiva produkter med "Default Title", blandade språk, versaler, slut i lager, saknad typ eller SEO-text | **Klart** | `sql/analys/produktdata_kvalitet.sql` (PROJ, SHOPDS) |
| T15 | Annonser på produkter som inte går att köpa | Annonskronor till utkast, arkiverade eller slutsålda produkter | **Klart** | `sql/analys/annonser_pa_slutsalda.sql` (PROJ, KEY, SHOPDS) |
| T16 | Sajthastighet, fördjupning | Utveckling över tid (Chrome UX Report-historik), tredjepartsskript och appars vikt per sidtyp, bildstorlek och format, cache | **Delvis:** T6 finns. Historik och skriptvikt är inte byggda | – |
| T17 | SEO, fördjupning | Filter- och sorterings-URL:er i index, paginering, intern länkning (djup och ankartext), indexeringsstatus via URL Inspection API (stickprov), duplicerat leverantörsinnehåll, kategorier med färre än fyra köpbara produkter | **Delvis:** `empty_collection`, `orphan_page`, `duplicate_content` finns. Resten är inte byggt | – |
| T18 | Flera domäner (SE, DK, FI) | hreflang mellan domänerna, språk mot domän, valuta, innehåll som kopierats mellan domänerna | **Delvis:** `hreflang_*` och `language_mismatch` finns. Kontrollen över domängränser saknas | – |
| T19 | Samtycke och tillgänglighet | Cookie- och samtyckesläge (Consent Mode v2 påverkar GA4 och annonsmätning), tillgänglighetsfel (axe-core) | **Inte byggt.** Samtycke är troligen en av orsakerna till låg mätning | – |
| T20 | Konkurrens och auktoritet | Bakåtlänkar, hänvisande domäner, vilka som rankar på första sidan per kategori | **Väntar på Ahrefs** (beslutat 2026-10-23: avvakta) | – |

*Inaktuellt sedan 2026-10-23 för T16, T17, T18 och T19 (nu byggda): se tillägget längst ned i filen och ändringsloggen.*

Prioritet för en ny butik med få ordrar: T12 och T11 först (varför köper ingen, och går det att lita på siffrorna), sedan T14/T15 (katalogen), T13 del 1, och därefter T17 och T16.

## Tillägg 2026-10-23 (senare): T16–T19 är byggda
Byggt och enhetstestat (77 tester). Webbläsarskripten och kontrollerna är provkörda mot låtsasbutiker och **inte** mot en riktig butik än. Alla är skrivskyddade.

| Nr | Test | Så körs det | Vad det visar | Fallgropar |
|---|---|---|---|---|
| T16a | Chrome UX Report, historik | `read -rs CRUX_API_KEY && export CRUX_API_KEY` (eller PSI_API_KEY), sedan `site-audit crux --site <sajt> [--form-factor PHONE]` | p75 för LCP, INP, CLS och TTFB per vecka, bedömning och trend (senaste fyra veckor mot åtta veckorna före) | API:et "Chrome UX Report API" måste vara aktiverat och nyckeln begränsad till det. **Sajter med lite trafik saknar ofta data** (då svarar API:et 404 och kommandot säger det). Nyckeln matas in med `read -rs`, aldrig i chatten |
| T16b | Tredjepartsskript och bilder | Ingår i `site-audit run` (nya fynd `third_party_script_hosts`, `images_without_dimensions`, `images_not_lazy`) | Hur många externa skriptvärdar varje sidtyp laddar och vilka som är vanligast; bilder utan bredd och höjd (CLS) och utan lazy loading | Värdarna är en grov mätare på appars vikt: antalet säger inte hur tunga skripten är. Bilder med `fetchpriority=high` räknas inte som utan lazy loading |
| T17a | Indexeringsstatus | `site-audit inspect --site <sajt> --per-type 20 --out inspektion` | Är ett jämnt urval av sitemapens adresser indexerade, vilken canonical valde Google, och när hämtades sidan senast? Fynd `sitemap_urls_not_indexed` och `google_chose_other_canonical` | Kvot cirka 2 000 per dag och egendom (kommandot stannar vid 400). Tjänstkontot måste vara användare i Search Console-egendomen. Urvalet är litet: läs andelar, inte exakta tal |
| T17b | SEO-kontroller i genomlysningen | Ingår i `site-audit run`: `faceted_url_indexable`, `paginated_canonical_to_first`, `collection_few_products` | Filter- och sorteringsadresser som går att indexera; paginerade sidor med canonical till sida 1; kategorier med färre än fyra produkter i listan (till exempel en tom kategori) | Produktantalet räknas på kategorins första sida. Duplicerat leverantörsinnehåll mot andra butiker går inte att se härifrån |
| T18 | Flera domäner med samma butik | `site-audit cross-domain --sites bestofsports-se,bestofsports-dk,bestofsports-fi --per-type 12 --out domaner` | Oöversatta kopior mellan domäner, canonical till en systerdomän, hreflang som saknas eller inte är ömsesidig, och produktpris i fel valuta i schemat | Jämför bara adresser som finns på alla domäner (samma handle). Har domänerna olika handles jämförs bara startsidorna och kommandot säger det |
| T19a | Samtycke och mätning i webbläsare | `python3 scripts/samtycke_test.py --base-url <butik> --out samtycke` | Skickas spårning före samtycke, startar den efter godkännande, vad säger Googles samtyckessignal (gcs) och Shopifys Customer Privacy API | Bannerknappar hittas på text och kan missas i ovanliga teman: titta på skärmdumparna. Test mot en butik i Sverige säger inget om andra länders regler |
| T19b | Tillgänglighet (axe-core) | `pip install playwright axe-playwright-python && playwright install chromium`, sedan `python3 scripts/tillganglighet_test.py --base-url <butik> --collection /collections/<x> --out tillganglighet` | Överträdelser per allvarlighet och regel på startsida, kategori och produkt | axe hittar bara det som går att mäta automatiskt (ungefär en tredjedel av alla fel). Kommandot ger felkod 1 om något är kritiskt |
| T19c | Samtycke och taggar enligt HTML | Ingår i `site-audit run`: `consent_platform_in_html`/`consent_platform_not_in_html`, `consent_mode_v2_incomplete`, `multiple_ga4_ids` | Vad som syns i sidornas HTML | **Begränsad:** Shopifys cookiebanner och webbpixlar (Customer Events, där GA4 från Google & YouTube-appen ligger) laddas av JavaScript och syns inte här. Fynden är därför information. Avgörande test är T19a |

Nya fält i sidfakta (sparas i kolumnen `row` i BigQuery, ingen schemaändring): `images_no_dimensions`, `images_no_lazy`, `product_link_count`, `consent_platforms`, `analytics_ids`, `consent_mode_default`, `consent_mode_v2` och valutor i produktschemat. De nya genomlysningskontrollerna kommer med först när avbilden byggts om (kräver ditt ja till deploy).


## Tillägg 2026-10-25: nya kontroller efter Best of Sports-genomlysningen
Lagt till efter att första fullständiga genomlysningen av Best of Sports (`.fi`, 8 000 sidor) visat tre saker som tidigare kontroller missade eller flaggade fel. Befintliga rader ovan är oförändrade.

| Nr | Test | Så körs det | Vad det visar | Fallgropar |
|---|---|---|---|---|
| T20a | Länkadresser med mallkod eller HTML | Ingår i `site-audit run`: fynd `malformed_link_href` (samlat per adress, med antal sidor) | Länkar vars adress innehåller `{{ … }}`, `{% … %}`, `<`, `>` eller `notranslate`. Orsak: en tema- eller översättningstext som skrivits sönder, vanligen i sidfot, kundvagn eller produktsida, och då en trasig länk på alla sidor | Bara `<a href>` i HTML:en kontrolleras, inte länkar som byggs av JavaScript. Hittar felet först efter nästa körning. Rättelsen görs i temats textsträngar (Redigera standardtext) och i översättningen |
| T20b | Kategorier vars lista byggs med JavaScript | Ingår i `site-audit run`: samlat fynd `collections_rendered_by_js` (minst 60 % av minst 10 kategorier saknar produktlänkar i HTML:en). `missing_h1` på sådana kategorier blir info. Verifiering: `python3 scripts/rendera_kategorier.py --base-url <butik> --sample 30 --out rendera` | Skiljer en riktigt tom kategori från en som bara bygger listan i webbläsaren (klasserna ok, byggs_med_js, tom, utan_h1) | Genomlysningen läser råa HTML. Att listan byggs med JavaScript är inget fel, men Google måste rendera sidan: bekräfta med Search Console att kategorierna får klick. Skriptet kräver Playwright och en webbläsare |
| T20c | Flera Product-noder i schemat | Ingår i `site-audit run`: fynd `product_schema_extra_node` (info) | En omdömesapp eller ett tema som skriver en andra Product-nod utan bild och pris. Bara fullständiga noder bedöms för bild och pris | Googles verktyg kan behandla extranoden som en egen produkt. Åtgärden är att koppla den till huvudnoden med samma `@id` |
| T20d | Adress med eller utan www | `sites.toml`: `base_url` ska vara den adress sajten landar på. Kontroll: `curl -sIL -o /dev/null -w '%{url_effective}\n' https://www.<domän>/` | Canonical-kontrollen jämställer nu www och adressen utan www, men crawlen och GA4-filtren följer `base_url`, så den ska vara rätt | Fel `base_url` gav 5 998 falska canonical-fynd på Best of Sports. Best of Sports: utan www. Gorilla: med www |
| T20e | Översättningstexter med skadade länkar | Skanning via Shopify Admin API (translatableResources, bara läsning). Mönster: `notranslate`, `{{`, `{%`, `&lt;span`, tomma `href` | Skadade länkar i temat, menyer, sidor, artiklar, kategorier och produkter | Gjord 2026-10-25 för Best of Sports: 5 302 produkter, 349 kategorier, 150 artiklar, 13 sidor, menyer och temats mallar (50 av fler) kontrollerade, inga träffar utöver fem rättade temastexter. Länkar (50 av fler) och resten av mallarna är inte skannade |

Nya fält i sidfakta: `malformed_hrefs`. Nya kontroller kommer med först när avbilden byggts om, vilket gjordes 2026-10-24 för de fem nya jobben.

## Tillägg 2026-10-26: tester som tillkom under dagen (T21–T29) och hur de effektiviseras
Dokumentet nedan lägger bara till rader. Kolumnen **Lärdom** pekar på vad vi lärde oss och vad som gav falsklarm; fler lärdomar står i `LARDOMAR.md`. Status anger vad som har körts mot en riktig sajt.

| Nr | Test | Så körs det | Vad det visar | Status | Lärdom |
|---|---|---|---|---|---|
| T21 | Onsite SEO och GEO (urval) | `python3 scripts/onsite_kontroll.py --base-url <sajt> --ut <katalog>` | robots.txt för sökmotorer och 13 AI-botar, llms.txt, omdirigeringar, sitemap, schema per fält, canonical (antal och domän), H1, alt, textmängd, parametrar, svarstid | Körd mot Gorilla SE och BOS FI. Inte körd mot Gorilla DK, BOS SE och BOS DK | Falsklarm vi rättade: FAQ räknade alla `<details>`, alt räknade SVG-ikoner, `?page=2` med egen canonical är korrekt, och flera canonical-taggar upptäcktes inte när bara den sista lästes. Urvalet är litet (40 och 20 sidor) |
| T22 | Källor till schema, canonical och GTM på en sida | `python3 scripts/schema_kallor.py --base-url <sajt> [--url <adress>]` | Varje JSON-LD-skripts tagg och början, vilka domäner adresserna pekar på, GTM-containrar och direkta laddningar, canonical och og:url | Körd mot Gorilla SE/DK och BOS FI | `shop.url` är alltid primärdomänen och gav fel domän i canonical, brödsmulor och produktschema. GTM på Gorilla laddas två gånger |
| T23 | Fraktgräns och fraktbetalare | `sql/analys/frakt_samband.sql`, `frakt_tippande.sql`, `priser_strax_under_gransen.sql` (PROJ) | Vilka ordrar som betalar frakt, korgens utseende, hur ordrar tar sig över gränsen, produkter strax under gränsen | Körd (de två första) mot Gorilla SE och DK. Den tredje är inte körd | Skilj påfyllning från produktens eget pris innan en orsak antyds. Små urval: läs inte per produkt när det är under 25 ordrar |
| T24 | Lönsamhet per order (Net Profit) | `sql/analys/net_profit_ordrar.sql` (kräver `site_audit.net_profit_sku` och `site_audit.gorilla_vikter`) | Contribution och nettovinst med frakt- och avgiftsspann, per marknad och över/under fraktgräns | Version 1 körd. Version 2 är inte körd: vikter saknas (kräver läs-token för `hamta_vikter.py`) | Arkets EUR-kolumner och kurser gäller, inte Shopifys `unit_cost`. Fraktkostnad per produkt ska inte summeras per paket utan spann |
| T25 | Omsättningstapp | `sql/analys/omsattning_30d.sql`, `omsattning_tapp_per_produkt.sql`, `omsattning_tapp_annonser.sql`, `annonser_pa_slutsalda.sql` | Var omsättningen tappat: produkt, kanal, annonser | Körda tidigare mot Gorilla | Annonsernas `item_id` kopplas till varianter via sista siffrorna. Kontrollera täckningen. Lagernivåer är leverantörens, så slutsålt är en faktor och inte en åtgärdslista |
| T26 | COS och kampanjer | `sql/analys/cos_30d.sql`, `marginal_30d.sql`, `marginal_stickprov.sql`, `annonser_vecka.sql`, `annonser_kampanjer_30d.sql` | COS, marginal och kampanjer per marknad | Körda tidigare mot Gorilla | COS är kostnad delad med intäkt, och måttet skiljer: plattformens värde mot Shopifys nettoförsäljning exklusive moms. Fråga alltid vilket mått en siffra avser |
| T27 | Status för nattens genomlysningar | `bash scripts/audit_status.sh`, `bash scripts/audit_detaljer.sh <sajt>` | Lyckades jobben, nyckeltal per sajt, exempel på allvarliga fynd | Körd dagligen | `missing_h1` och `collection_few_products` på BOS kan vara följd av JavaScript: verifiera med T20b innan åtgärd |
| T28 | Omdirigeringar | `python3 scripts/redirect_jamforelse.py`, `scripts/redirects_gorilla_apply.py` (torrkörning är standard) | Jämför mål mot Shopify och planerar ändringar | Körd mot Gorilla (81 + 11 + 12 ändringar) | Rapportera inte som åtgärdat förrän nästa genomlysning visar det |
| T29 | Samlade körningar | `bash scripts/gorilla_lage.sh`, `scripts/langkorare_gorilla.sh`, `scripts/langkorare_bos.sh` | Flera tester i ett svep | Gorilla-körningarna startade, resultaten för köpflöde, samtycke och tillgänglighet är inte lästa | Långkörarna ligger kvar efter omkoppling i Cloud Shell, men en frånkopplad session kan tappa utdata |

### Tester som saknas eller inte kan köras än
| Behov | Status | Orsak |
|---|---|---|
| Konvertering per varukorgsvärde (GA4) | Inte byggd | Behöver veta vilka GA4-händelser som ligger i BigQuery |
| Nätverkstest av dubbla GTM/GA4-händelser (T22-uppföljning) | Inte byggd | Kräver webbläsare (Playwright) |
| URL-inspektion för BOS (T17a) | Gav 403 | Inloggningen i Cloud Shell saknade omfånget `webmasters.readonly` |
| GEO citeringspanel (T13b) | Väntar på beslut | API-nycklar och kostnad |
| Konkurrens och auktoritet (T20) | Väntar på Ahrefs | Beslutat 2026-10-23 |

### Förslag för att lära och effektivisera (kräver ditt beslut)
1. **Lägg de nya kontrollerna i den nattliga genomlysningen** i stället för som urval. Idag samplar T21 60 sidor; genomlysningen kör 8 000 sidor varje natt. Förslag på nya kontroller: `multiple_canonical_tags`, `schema_url_other_domain` (JSON-LD-adress på annan domän än sidan, Organization undantagen), `gtm_container_loaded_twice`, `shipping_details_missing`, `breadcrumb_missing_on_collections`. Då hade BOS-canonical och Gorillas schema-URL:er hittats första natten.
2. **En ingång per sajt.** Ett skript `scripts/kor_tester.sh <sajt>` som kör alla skrivskyddade tester i fast ordning, sparar resultaten i en katalog med datum och skriver en enda sammanfattning att klistra in. Idag krävs ett tiotal kommandon i flera flikar.
3. **Jämför mot förra körningen.** Spara varje körning som JSON och visa vad som är nytt, åtgärdat och oförändrat. T21 och T22 saknar det, genomlysningen (T1) har det redan.
4. **Fast lärdomsrutin.** Efter varje test: skriv falsklarmen och rättelserna i kolumnen Lärdom här, och i `LARDOMAR.md` om något gick fel. Varje nytt mått får ett enhetstest med ett känt fall innan det används (gjort för T21).
5. **Schemalägg T21 veckovis** för alla fem sajter via Cloud Scheduler och spara i BigQuery, med larm vid försämring. Det är en ändring i Google Cloud och kräver ditt ja.
