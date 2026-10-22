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
