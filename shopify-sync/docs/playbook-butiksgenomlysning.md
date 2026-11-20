# Playbook: genomlysning och åtgärdsarbete i en butik eller sajt

Skapad 2026-11-19 av koordinatorn på Davids uppdrag, efter arbetet med Workout Brands (workoutbrands.com). Filen fylls bara på. Syftet är att göra om det vi lärt oss till en metod som går att upprepa på nästa sajt och, på sikt, att sälja som tjänst. Den här filen **ersätter inte** de äldre dokumenten utan pekar på dem: läs dem först om du ska göra något av det som beskrivs där.

## 0. Vilka dokument gäller för vad

| Behov | Dokument |
|---|---|
| Läsande genomlysning av en Shopify-butik via verktyg (MCP) | `genomlysning-ny-butik.md` |
| SEO, metadata och GEO (metod och leveransformat, mall för kundrapport) | `seo-geo-genomlysning-metod.md` |
| Automatisk kontroll av tekniska fynd i bred skala | `site-audit.md`, `basgenomgang.md`, `scripts/audit_tackning.py` |
| Produkttexter i stor skala | `textutrullning-rutin.md`, `produkttexter-standard.md` |
| Ny sajt i verktygen | `ny-sajt.md`, `ny-butik-checklista.md` |
| Flera butiker samtidigt | `flera-sajter.md`, `arbetsstrommar.md` |
| Den här filen | Katalog- och kollektionsarbete via API, mätning före/efter, skanning av vilken sajt som helst, och vad som är nytt sedan Workout Brands |
| Paket, målgrupper och prissättningens beståndsdelar | `paket-och-malgrupper.md` |

## 1. Principer (gäller varje butik, varje gång)

1. **Läs först, skriv sedan.** Skanningen är alltid läsande. Skrivning kräver ett uttryckligt ja per åtgärd.
2. **Före-fil, kanariefall, återläsning.** Spara före-läget, kör 10 objekt, kontrollera i butiken, kör resten. Skriptet läser tillbaka varje skrivning och stoppar vid första avvikelse.
3. **Mät före och efter.** Utan baslinje går effekten inte att visa. Kör `gsc_baslinje.py` och `gsc_indexering.py` före första ändringen och igen efter 7 och 28 dagar. Ha en kontrollgrupp (sidor som inte rörs).
4. **Ett skript per åtgärd, inga mutationer för hand.** Långa texter som kopieras mellan fönster förstörs. Skript med återläsning gör det inte.
5. **Skriv ner varje misstag direkt** i `LARDOMAR.md`, och logga varje ändring i `ANDRINGSLOGG.md`. Det är så metoden förbättras.
6. **Inga nycklar i chatten eller repot.** Nycklar sätts i terminalen med `read -s`, och en secret som klistrats in i en chatt roteras.
7. **Skanna bara det du har tillstånd att skanna.** Publika sidor är i regel tillåtna att läsa, men en djup genomgång (tusentals anrop, API-åtkomst) kräver kundens godkännande skriftligt.

## 2. Körordning (från första kontakt till uppföljning)

| Steg | Vad | Verktyg | Utfall |
|---|---|---|---|
| 1 | Kommersiell bild: är sajten aktiv, vilka marknader, vad säljs | `genomlysning-ny-butik.md` steg 0–1 | Prioritering efter omsättning eller synlighet |
| 2 | Snabbskanning av publika sidor (vilken plattform som helst) | `sajtskanning.py` | Fynd per paket på några minuter, utan åtkomst |
| 3 | Djupskanning av katalog (Shopify): alla produkter och kollektioner | `wb_export.py` → `skanning_rapport.py` | Fynd med exakta antal |
| 4 | Sökdata: trafik per land, enhet, sida, sökfråga och indexering | `gsc_baslinje.py`, `gsc_indexering.py` | Baslinje och prioritering |
| 5 | Rapport och förslag till kund, med paket | `skanning_rapport.py`, mall i `seo-geo-genomlysning-metod.md` §7.1 | Beslutsunderlag |
| 6 | Åtgärder i prioriterad ordning, ett paket i taget | se tabell i §3 | Före-fil, kanariefall, återläsning |
| 7 | Uppföljning efter 7 och 28 dagar | samma som steg 4 | Jämförelse mot kontrollgrupp |

## 3. Kontroller, åtgärder och skript

Alla skript ligger i `shopify-sync/scripts/`. "Läser" betyder att skriptet inte skriver i butiken.

| Fynd | Källa | Åtgärd | Skript | Läser/skriver |
|---|---|---|---|---|
| Bilder utan alt-text | bulkexport | Alt-text i bulk (produktens titel) | `wb_alt.py` | skriver |
| Produkter utan kategori | bulkexport | Produktkategori efter regel (grupp för grupp, du godkänner listan) | `kategori_satt.py` | skriver |
| Attribut saknas (kön m.m.) | bulkexport | Fyll standardmetafält efter godkänd mappning | `kon_fyll_target_gender.py` | skriver |
| Tomma kollektioner / regelfel | bulkexport + `collectionByIdentifier` | Rätta regel, avpublicera och omdirigera | manuellt via verktyg + redirectlista | skriver (avpublicering görs av ägaren) |
| Kollektioner utan SEO | export + Search Console | Titel och beskrivning, översätt | manuellt via verktyg (se §5) | skriver |
| Översättningstäckning | översättnings-API | Översätt saknade och föråldrade texter | `wb_export.py --bara oversattning` | läser |
| Indexering och trafik | Search Console | Baslinje och jämförelse | `gsc_baslinje.py`, `gsc_indexering.py` | läser |
| Publika sidor (alla plattformar) | HTML | Rapport per paket | `sajtskanning.py` | läser |

Samlad rapport: `skanning_rapport.py --namn … --shopify-export DIR [--url …] [--onsite DIR] --ut DIR`.

## 4. Praktiska fallgropar (kostade oss tid 2026-11-19)

Se `LARDOMAR.md` för datum och detaljer. Kort:

- **Nycklar försvinner när Cloud Shell startas om.** Kontrollera `echo ${#VAR}` före varje körning. Kör långa jobb i bakgrunden: `nohup python3 -u skript.py … > logg 2>&1 &` (`-u` ger direkt loggning).
- **Uppladdade filer får suffix** (`(1)`, `(2)`, `_(2)`). Kör `ls -lt` och kopiera den nyaste, och kontrollera med `grep -c` på ett ord som bara finns i nya versionen.
- **Skript som mot externa API:er kraschar utan omförsök** förlorar sitt arbete. Alla nya skript ska spara löpande, ha timeout med omförsök och kunna återupptas.
- **`tail -f` låser fliken.** Tryck Ctrl+C före nästa kommando, annars skrivs det bara som text.
- **Shopify:** `SEOInput` utan `description` tömmer beskrivningen; kollektionsregler ändras via `collectionUpdate` med `sourcesToUpdate`; `publishableUnpublish` är blockerad i koordinatorns verktyg och görs av ägaren; omdirigering gäller först när sidan inte längre är publicerad; en bild kan sitta på flera produkter.
- **Search Console:** URL Inspection kräver behörigheten `webmasters` (inte bara `.readonly`); `ACCESS_TOKEN_SCOPE_INSUFFICIENT` betyder fel behörighet på inloggningen.
- **Behörigheter i appen** (Dev Dashboard): `read_products`, `write_products`, `read_inventory`, `read_locales`, `read_translations`, `write_files`. En ny version måste släppas och godkännas i butiken innan den gäller.
- **Läs aldrig siffror som framsteg från ett annat mått.** "Antal uppdaterade produkter" i Shopify räknar även andra jobbs ändringar. Använd skriptets egen utskrift.

## 5. Så arbetar vi med SEO på kollektioner (mönstret från 2026-11-18 och -19)

1. Hämta alla kollektioner och deras sökdata, och ranka efter visningar.
2. Börja med sidor som saknar SEO-titel och ligger på plats 8–30 med många visningar.
3. Titel högst 60 tecken, utan butiksnamn (butikens beslut), med sökordet först. Beskrivning högst 160 tecken, utan påståenden som inte kan styrkas.
4. Skicka alltid både `title` och `description` i `seo`, och spara före-värdena.
5. Översätt titel och beskrivning till butikens huvudspråk (hämta `digest` per fält först).
6. Håll tillbaka sidor för varumärken som inte fylls på, och sidor som ska omdirigeras.

## 6. Plattformsoberoende: vad som går och inte går

- **Går på alla plattformar:** `sajtskanning.py` (publika sidor, sitemap, metadata, canonical, schema, alt, tunt innehåll, svarstid) och Search Console-skripten.
- **Går bara för Shopify:** katalogexport, kategori- och attributsättning, kollektionsregler, översättnings-API.
- **För andra plattformar** (WooCommerce, Magento, WordPress, egna system): skanningen ger fynden; åtgärderna görs då via plattformens egen export/import eller admin, och varje plattform kräver sitt eget skript. Det är den största olösta delen, och den beror på vilka plattformar kunderna använder.
- **Informativa företagssajter** (ingen webbshop): paketen P3 (teknik), P4 (innehåll) och P6 (mätning) är relevanta. P1 och P2 gäller inte.

## 7. Tidslogg

Fyll i `tidslogg-genomlysning.csv` efter varje åtgärd (datum, butik, åtgärd, enhet, antal, aktiv tid, väntetid, kommentar). Det är underlaget för en ärlig prissättning. Värdena från 2026-11-19 är grova uppskattningar ur samtalets förlopp och inte stoppur.

## 8. Öppna punkter

- Vilka plattformar kunderna använder (avgör vilka åtgärdsskript som behöver byggas).
- Avtal och behörighetsmodell för kunder (personuppgifter, åtkomst, ansvar).
- Vem som säljer tjänsten (bolag och varumärke): beslutas av David, inte av koordinatorn.
- Effekten av åtgärderna är inte mätt än (jämförelse 2026-11-26 för Workout Brands).

## 9. Tillägg 2026-11-20: flera butiker med samma skript
Skripten som använder `Klient` i `kon_fyll_target_gender.py` (`wb_export.py`, `wb_alt.py`, `kategori_satt.py` m.fl.) är nu butiksoberoende: sätt `SHOPIFY_BUTIK` till butikens `*.myshopify.com`-adress (standard är Workout Brands) och antingen `SHOPIFY_CLIENT_ID` + `SHOPIFY_CLIENT_SECRET` (Dev Dashboard-app, klient-id/hemlighet) eller `SHOPIFY_ADMIN_TOKEN` (äldre egen app med färdig token). Gamla variabelnamn med suffix `_WB` fungerar fortfarande. Ge en skanningsapp bara läsbehörigheter (`read_products`, `read_locales`, `read_translations`); skrivbehörigheter läggs till först när ett skrivuppdrag är godkänt.

## 10. Tillägg 2026-11-20: tre lager som hålls isär (site, kanaler, filter)
Ett vanligt missförstånd, och ett vi själva gjorde på Gorilla Sports: att "kategori" och "kön" skulle vara samma sak som kollektioner. De är tre olika lager, och vi arbetar med dem separat.

| Lager | Vad det styr | Vad det består av | Påverkar sajtens synlighet? | Exempel på uppdrag |
|---|---|---|---|---|
| 1. Site (kollektioner och menyer) | Vilka produkter som visas på vilka sidor, i vilken ordning | Taggar, produkttyp, leverantör, titel, pris, status, kollektionsregler, menyer | Ja, det är lagret som syns | SEO på kollektioner, tomma sidor, omdirigeringar |
| 2. Kanaler (TikTok Shop, Meta/Facebook/Instagram Shop, Google Shopping, Pinterest, Shop) | Hur produkten tas emot och visas i köpkanalerna | Shopifys produktkategori (taxonomin) och kanalernas obligatoriska attribut (till exempel märke, kön, färg, storlek, material, GTIN) | Nej | Kategorisering, flödeskvalitet, attributfyllnad |
| 3. Filter och attribut (Search & Discovery) | Filter och facetter i butikens egen sökning | Standardattribut som "Avsett för" (kön), kopplade till produktkategorin | Bara om filtret används på sajten | Könsfältet på Workout Brands |

**Grundregler**
- Lager 2 och 3 ändras utan att lager 1 rörs. En produkts kategori ska inte avgöra vilka kollektioner den hamnar i. Kollektioner styrs av taggar och regler (lager 1).
- Undantag att alltid kontrollera: kollektioner som själva använder produktkategori som regel. På Gorilla Sports fanns en sådan (`hemmagym-traningsredskap-hemma`, regel: kategori EQUALS en nedlagd, gammal kategori, eller en tagg). Före varje kategoriskrivning: lista kollektioner med kategoriregel, notera deras antal, skriv några produkter först (kanarie) och räkna om. Antalet ska vara oförändrat.
- Kategorier i äldre kategoriträd (id som `archived-…`) finns kvar i butiker och i kollektionsregler. De kan flyttas till det nya trädet, men kollektionsregler som pekar på dem måste kollas först.
- Ett skanningsfynd som "produkter utan kategori" är bara en brist om butikens mål kräver det. Fråga först: säljer butiken via kanaler (lager 2) eller behöver den filter (lager 3)? Gorilla Sports: kanaler är aktiva (Google, Facebook, Pinterest, TikTok, Shop) och kön är irrelevant för gymutrustning. Workout Brands: kön behövs för filter. Dela inte på samma prioritet för båda.

**Rutin för kategorisering (lager 2), så som den kördes på Gorilla Sports**
1. Exportera produkter läsande (`wb_export.py`), skapa förslag med `gorilla_kategori_forslag.py` (regler efter produkttyp och titel, säkerhet hög, medel eller manuell).
2. Verifiera varje kategori-id mot butikens kategoriträd (sökning fungerar på svenska; `nodes(ids:[…]) { … on TaxonomyCategory { fullName } }` ger namnet). Shopifys svenska namn kan vara felöversatta (handtag heter "Användarnamn").
3. Granska fil före skrivning: jämför hög-raderna mot produkttyp. Specifika regler först, regler på titelord bara där produkttypen stödjer dem (lärdom 2026-11-20: en curlbänk fick Viktskivor av ordet i titeln).
4. David godkänner per säkerhetsgrupp. Skriv i ordningen torrkörning, kanarie (5, granska på titel), resten, med före-fil och återläsning (`kategori_satt.py`). Kontrollera efteråt ett slumpurval och antalet i kollektioner med kategoriregel.
5. Skrivbehörighet (`write_products`) kräver en app som butikens ägare godkänt.

**Rutin för attribut och kön (lager 3, Workout Brands)**
Kategori sätts först (via `kategori_satt.py`), därefter fylls attributet (`kon_fyll_target_gender.py`). Attribut fylls bara där det är relevant (gymutrustning har inget kön).

**Att verifiera innan vi lovar något kund (lager 2)**
Vilka attribut TikTok Shop, Meta Shop och Google Merchant Center kräver per kategori, och hur flödenas fel ser ut, är inte undersökt av oss. Det är en antagen nytta, inte en mätt. Mät flödesstatus per kanal (avvisade produkter, varningar) före och efter innan effekten redovisas.
