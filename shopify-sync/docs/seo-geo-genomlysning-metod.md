# Metod: genomlysning av SEO, metadata, struktur och GEO för en Shopify-butik

Skapad 2026-11-06 på Davids uppdrag. Första tillämpning: Alpha Zoo (alphazoo.se, .dk, .fi) och B You Underwear (byouunderwear.se), enligt beslutet i `BESLUTSLOGG.md` 2026-11-04. **Det här är ett metoddokument. Ingen körning har gjorts, och inget konto, ingen butik och inga nycklar har öppnats eller lästs.**

GEO betyder här optimering för att sidor ska nämnas eller citeras i svar från AI-sökning (till exempel ChatGPT, Perplexity, Gemini och Googles AI-översikter).

Metoden bygger på det som redan är dokumenterat och byggt: `basgenomgang.md`, `site-audit.md`, `standardtester.md` (T1–T40), `tillvaxtdata.md`, `ny-sajt.md`, `flera-sajter.md`, `produkttexter-standard.md`, `regler/regler-v1.md`, `BESLUTSLOGG.md` och `LARDOMAR.md`. Där något inte kunnat verifieras i repot står **"Ej verifierat"**.

**Täckning:** Läst i sin helhet: `CLAUDE.md`, `ny-sajt.md`, `tillvaxtdata.md`, `textutrullning-rutin.md`, `BESLUTSLOGG.md`, `regler-v1.md`, `flera-sajter.md`, `site-audit.md`, `basgenomgang.md`, `tillvaxtarbete.md`, BOS-temagenomgången och temaändringarna (2026-10-26). Delvis läst: `standardtester.md` (T1–T40 i tabellerna), `produkttexter-standard.md` (avsnitt 1–4, 16–17), `LARDOMAR.md` (rubriker och de poster som rör SEO, schema och mätning), koden för datahämtning (`google_api.py`, `ads_api.py`, `growth_sql.py`, kontrollnamn i `checks/`) och fyra SQL-filer. Inte läst: `arbetsstrommar.md`, `driftrutiner.md`, `produkttexter-standard.md` avsnitt 5–15, `ANDRINGSLOGG.md` i sin helhet och Gorilla Sports eller BOS tema i sin helhet utöver temagenomgången.

---

## 1. Syfte och vad kunden får

**Syfte:** visa var butikens sidor tappar synlighet, klick och försäljning i Google och i AI-svar på grund av titlar, metadata, struktur, strukturerad data, indexering och innehåll, och ge en prioriterad lista över vad som ska göras, i vilken ordning, med vilken risk och hur varje åtgärd kontrolleras.

**Leverans:** en rapport (mall i avsnitt 7) med:
1. Nuläge i siffror (synlighet, trafik, försäljning per sidtyp).
2. Fynd, sorterade efter sidor som redan har trafik eller intäkt.
3. **En prioriterad åtgärdslista** där varje rad anger vad som ändras, var (butiken via API, eller temat), effekt, insats, risk, hur det kontrolleras före och efter, och vilket beslut som behövs.
4. En lista över frågor som kunden måste svara på innan något ändras.
5. Det som inte gick att mäta eller verifiera, uttryckt öppet.

**Gräns:** genomlysningen är skrivskyddad. Ingen åtgärd görs i butiken, temat eller något annonskonto utan ett uttryckligt ja per åtgärd eller tydligt avgränsad grupp (se `standardtester.md`, "Rutin för ändringar i Shopify").

---

## 2. Datakällor, mått och koppling till sidor

### 2.1 Vad som hämtas

| Källa | Mått och dimensioner | Status i repot |
|---|---|---|
| **Search Console** (Google) | Per **sida**: klick, visningar, CTR (klick/visningar), genomsnittlig position. Per **sida × sökfråga**: samma fyra mått. Per dag, land och enhet om det behövs. Sökfrågor som Google döljer (anonymiserade, cirka 36 % av visningarna på Gorilla) saknas alltid | Byggt. Massexport till BigQuery (`searchdata_url_impression`, fyller bara på framåt) plus `site-audit backfill gsc --days 480` (sidnivå) och `--queries` (sökfrågor). Vyn `gsc_combined_<sajt>` slår ihop dem (`ny-sajt.md` steg 2, 5, 6; `site-audit.md`) |
| **Search Console, indexering** | Indexeringsstatus och vilken canonical Google valde, i stickprov per sidtyp (URL Inspection API, kvot cirka 2 000 per dag och egendom) | Byggt: `site-audit inspect` (T17a) |
| **Google Ads** | **Kostnad, klick, visningar, konverteringar och konverteringsvärde** per dag och kampanj, och per dag och **produkt** (`item_id`, Shopping och Performance Max) | Byggt: `google_ads_daily_<butik>` och `google_ads_products_daily_<butik>` (`ads_api.py`, `tillvaxtdata.md`). Plattformens egen tillskrivning, aldrig att summera med andra plattformar |
| **Google Ads, söktermer** | Faktiska söktermer som utlöst annonser, med kostnad och konvertering | **Inte byggt.** Koden hämtar bara `campaign` och `shopping_performance_view`. Söktermsrapport (`search_term_view`) måste byggas, och dess utseende i API:et är **Ej verifierat** i repot. Alternativ tills dess: exportera söktermsrapporten ur Google Ads-gränssnittet, om kunden ger rätt behörighet |
| **GA4** | Per dag, värdnamn och **landningssida**: sessioner, köp, intäkt (`ga4_landing_daily_<butik>`). Per dag, källa/medium och kampanj: samma mått (`ga4_channel_daily_<butik>`) | Byggt (`google_api.py`: `landingPage`, `hostName`, `sessions`, `ecommercePurchases`, `purchaseRevenue`) |
| **GA4, produkt** | Intäkt, antal sålda och visningar **per produkt** (artikelmått) | **Inte byggt, Ej verifierat.** Repot hämtar inte artikelmått från GA4. Intäkt per produkt hämtas i stället ur Shopify (`order_line_items`), som är facit (`tillvaxtdata.md`) |
| **GA4, AI-hänvisningar** | Sessioner och köp där källan matchar ChatGPT, Perplexity, Gemini, Copilot, Claude m.fl. | Byggt: `sql/analys/ai_hanvisningar.sql` (T13). Nedre gräns, se avsnitt 4.3 |
| **Shopify (BigQuery)** | `products`, `product_variants`, `orders`, `order_line_items`: titel, handle, status, lager, pris, SKU, ordrar och intäkt | Byggt (jobbet `shopify-sync`, varje timme) |
| **Shopify Admin (läsning)** | Produkter, kategorier (collections) och deras regler, sidor, artiklar, URL-omdirigeringar, språk, marknader, översättningsgrad. Produkters SEO-titel, metabeskrivning, beskrivning och bildernas alt-text | Delvis byggt: `site-audit` admin-kontroller. Alt-text per bild via Admin API är **Ej verifierat** i repot |
| **Genomsökning av sajten** | Titel, meta, H1, canonical, hreflang, robots, JSON-LD (Product, BreadcrumbList, Organization, FAQ), alt-text, interna länkar, sitemap, statuskoder | Byggt: `site-audit run` (T1), `onsite_kontroll.py` (T21), `schema_kallor.py` (T22), `cross-domain` (T18) |
| **Merchant Center** | Avvisade produkter och orsak | Byggt men inte körd mot riktigt konto (`tillvaxtarbete.md`) |

### 2.2 Så kopplas siffrorna till produkt och kategori

Gemensam nyckel är **sidans sökväg** (adressen utan domän), normaliserad: utan `?`-parametrar och utan avslutande snedstreck, domänen sparad som egen kolumn.

| Från | Till | Metod | Kända fallgropar |
|---|---|---|---|
| Search Console-sida och GA4-landningssida | Produkt: `/products/<handle>`. Kategori: `/collections/<handle>`. Övrigt: blogg, sidor, startsida | Mönster i sökvägen, sedan koppling mot `products.handle` och kategoriernas handle | På marknader med **översatta adresser** matchar inte handle mot Shopify och ger falska träffar (`basgenomgang.md`, 2026-10-20: 100 falska träffar på gorillasports.dk). Där används genomsökningens statuskoder i stället. Alpha Zoo har tre domäner, så kontrollera per domän om adresserna är översatta innan kopplingen används |
| `/collections/<kategori>/products/<handle>` | Produkten | Ta bort kategoriledet, räkna trafiken på produkten men notera kategorin | Kategorivarianten ska normalt ha canonical till `/products/<handle>` (kontroll `collection_product_url_indexable`) |
| Google Ads `item_id` | Shopify-variant, sedan produkt | Sista talet i `item_id` mot `product_variants.id`; vyn `growth_product_daily_<butik>` har kolumnen `matched` som visar täckningen | Format på `item_id` i butikens produktflöde är **Ej verifierat** för Alpha Zoo och B You. Mät `matched`-andelen först och rapportera den |
| Produkt | Kategori(er) | Från Shopify Admin (kategorimedlemskap, och regler för automatiska kategorier) | Kategorimedlemskap i BigQuery-tabellerna är **Ej verifierat**; om det saknas hämtas det vid genomlysningen via Admin API (läsning) |
| Sökfråga | Sida | Via Search Console, par sida × fråga | Fråga utan sida (anonymiserad) kan inte kopplas. Redovisa andelen dold |

**Kontroll av kopplingen:** summera varje uppdelning och jämför mot totalen. Redovisa andel klick, visningar och intäkt som inte kunnat kopplas till en produkt eller kategori (lärdom 2026-10-25: aggregeringar ska stämma mot totalsumman).

### 2.3 Åtkomst: minsta behörighet, vem som ger den

**Inga nycklar, tokens eller lösenord i chatten, i repot eller i rapporter.** Hemligheter läggs av ägaren i molnmiljöns hemliga variabler eller Secret Manager. Kan en uppgift inte nås, rapporteras det som "saknas åtkomst", inte som gissning.

| Källa | Minsta behörighet enligt repot | Vem ger den | Anmärkning |
|---|---|---|---|
| Search Console | Tjänstkontot `shopify-sync@<projekt>.iam.gserviceaccount.com` som användare i domänegendomen (`sc-domain:`). `ny-sajt.md` anger "fullständig behörighet". **Om begränsad (skrivskyddad) behörighet räcker för läsning och URL-inspektion är Ej verifierat** | Ägare av egendomen (David, eller kundens ägare) | **Massexport kräver verifierad ägare**, inte bara tjänstkontot (`ny-sajt.md`, tillägg 2026-10-22). Exporten fyller bara på framåt, så starta den först; historik hämtas med `backfill gsc` |
| GA4 | Läsare (Viewer), helst på kontonivå om flera egendomar finns | Administratör av GA4-kontot | Anteckna egendoms-id. Kontrollera att varje domän bara syns i sin egendom (dubbelräkning) |
| Google Ads | Läsrätt för tjänstkontot i kundkontona, och åtkomst till hanterarkontot (MCC) om kontona ligger under ett. Google Ads API måste vara aktiverat i Cloud-projektet. Utvecklartoken är enligt repot numera valfri (*inaktuellt-markering i `tillvaxtdata.md`, 2026-10-18*) | Kontoägare i Google Ads | Kontoägarna för Alpha Zoo och B You är **Ej kända** i repot (`sites.portfolio.draft.toml` har TODO) |
| Shopify (läsning) | Appbehörigheter enligt `site-audit.md`: `read_products`, `read_content`, `read_online_store_pages`, `read_online_store_navigation`, `read_locales`, `read_markets`, `read_translations`. Inget skrivrättigheter | Ägare eller personal med behörighet i butiken installerar appen (`ny-sajt.md` steg 1) | Skrivrättighet (`write_products`) begärs först när en åtgärd är beslutad, inte för genomlysningen |
| Merchant Center | Tjänstkontot som användare, Merchant API aktiverat | Kontoägare | Valfritt; inte körd mot riktigt konto |
| Tema (kod) | Läsning av publicerat tema kräver extra behörighet i Shopify. **Ej verifierat vilken** i denna app | Butiksägaren | För BOS lästes temat med verktyg som blockerar skrivning till publicerat tema (`rapporter/bos-tema-andringar-2026-10-26.md`) |

**Bolagsgräns:** Alpha Zoo och B You kan tillhöra andra bolag än Gorilla Sports (bolag är TODO i utkastet). Om så är fallet ska data, åtkomst och kostnader hållas åtskilda i eget Google Cloud-projekt (`ny-sajt.md`, "Före start"). Det är ett beslut för David innan åtkomst ordnas.

---

## 3. Analyser

Allt nedan är skrivskyddat. Befintlig kontroll anges med id där den finns; annars markeras "ny".

### 3.1 Titel- och metatäckning och kvalitet
- **Täckning:** andel aktiva produkter, kategorier, sidor och artiklar med egen SEO-titel och metabeskrivning (inte ärvd från titeln). Kontroller: `missing_title`, `missing_meta_description`, `duplicate_seo_title`, `duplicate_title`, `title_too_long`, T14 (`produktdata_kvalitet.sql`).
- **Kvalitet:** längd (SEO-titel så att den rymmer inklusive temats suffix, meta cirka 70–155 tecken), unikhet, typord först, ingen versal-rubrik, ingen utfyllnad. Samma gränser som `regler-v1.md` R7–R12 och `produkttexter-standard.md` avsnitt 3 om kunden accepterar dem; annars anges kundens egna gränser i butiksprofilen.
- **Temasuffix:** kontrollera i den renderade sidan, inte bara i temakoden, vad som läggs efter SEO-titeln (BOS: ` – BEST OF SPORTS`). Mät i genomsökt HTML (lärdom 2026-10-28: läs den renderade sidan).
- **Rangordning:** sidor med visningar men låg CTR först (`3_toppsidor_med_svag_klickfrekvens.sql`, `titlar-lag-ctr.csv` som mönster).

### 3.2 Dubbletter och kannibalisering
- **Sida mot sida:** flera sidor som rankar på samma sökfråga (`kategori_sokord.sql`, kontroll `keyword_cannibalization`). Läs raderna av typen "sida": om en blogg eller fel kategori visas före den önskade sidan är det en kannibalisering eller en saknad kategori.
- **Innehållsdubbletter:** `duplicate_content`, `near_duplicate_collection`, `duplicate_collection_products`, `duplicate_collection_description`, `collection_clones`. Leverantörens text kopierad rakt av räknas.
- **Produktdubbletter:** bara **exakt samma artikel** (modell, färg, storlek, vikt) räknas som dubblett (Davids beslut 2026-11-05). Samma SKU eller streckkod räcker inte som test. Arkivering eller sammanslagning är aldrig en del av genomlysningen.
- **Flera domäner (Alpha Zoo):** oöversatta kopior mellan .se, .dk och .fi, canonical mot systerdomän, ömsesidig hreflang, pris i fel valuta i schemat (`site-audit cross-domain`, T18). Mål: varje domän rankar självständigt på sitt språk (samma princip som David bekräftade för BOS 2026-10-26).

### 3.3 Intern länkstruktur och kategoristruktur
- Klickdjup från startsidan, antal inlänkar per sida, **orphan-sidor** (`orphan_page`), interna länkar med spårningsparametrar (`internal_links_tracking_params`), trasiga länkar (`malformed_link_href`).
- **Kategorier:** tomma (`empty_collection`), med färre än fyra köpbara produkter (`collection_few_products`), doorway-liknande (`collection_rule_suspect`), filter- och sorterings-URL:er i indexet (`faceted_url_indexable`), paginering (`paginated_canonical_to_first`).
- **Kategoriträdet mot sökbeteendet:** vilka sökfrågor med många visningar saknar en egen kategori (`kategori_sokord.sql`, `sokfragor_luckor.sql`), och vilka kategorier saknar visningar (`no_search_impressions`).
- **Varning:** kategorier vars produktlista byggs med JavaScript ger falska `missing_h1`; verifiera med `rendera_kategorier.py` (T20b) innan åtgärd.

### 3.4 Strukturerad data
- **Product:** namn, bild (fungerande adress), pris och valuta, tillgänglighet, märke, GTIN/SKU där de finns, leverans- och returuppgifter. Kontroller: `product_schema_missing`, `_no_image`, `_bad_image`, `_no_offers`, `_no_brand`, `shipping_details_missing`, `product_schema_extra_node`.
- **BreadcrumbList:** på produkter och kategorier (`breadcrumb_schema_missing`, `collections_without_breadcrumb_schema`). **Organization:** en gång, rätt namn och adress.
- **Källor och domäner:** vilket skript och vilken tema- eller appfil som skriver varje block, och vilken domän adresserna pekar på (`schema_kallor.py`, T22; fynd `schema_url_other_domain`). På BOS pekade schemat på primärdomänen även på .fi och .dk, och det fanns två canonical-taggar. Alpha Zoo har tre domäner, så samma fel är sannolikt men **Ej kontrollerat**.
- **Omdömen och betyg (aggregateRating, Review): redovisa aldrig som något positivt innan källan är känd** (lärdom 2026-10-26: BOS betyg i schemat kom från påhittade omdömen i temat). Kontrollera varifrån varje betyg kommer: riktig app med riktiga kunder, eller kod. Påhittade eller kopierade omdömen är en risk som ska lyftas till David och jurist, inte en förbättring.
- **FAQ-schema:** bara där sidan har en synlig, riktig fråga-och-svar-del som skrivits för besökaren. Googles utdrag för FAQ är begränsade och värdet är litet för de flesta sajter (`basgenomgang.md`). FAQ läggs till för användarnas och GEO:s skull, aldrig som ren schemadekoration, och aldrig som påhittade frågor.
- **Validering:** `jsonld_invalid`, och manuell kontroll av ett urval i Googles verktyg för rich results (**manuellt steg**, inte automatiserat i repot).

### 3.5 Bild-alt
- Andel produkt- och kategoribilder utan alt-text (`images_missing_alt`, `product_images_no_alt`, `alt_text_summary`). Dekorativa SVG-ikoner ska inte räknas (lärdom 2026-10-26: måttet gav 67,8–88,9 % innan det rättades).
- Kvalitet: alt beskriver vad bilden visar (produkt, färg, vinkel), är inte nyckelordsupprepning och hittar inte på egenskaper som inte syns.
- **Skrivbarhet:** se avsnitt 5. Alt-text per bild via Admin API är **Ej verifierat** i denna app.

### 3.6 Indexering och kanonisering
- Sitemap: adresser som ger 404, omdirigeras, är noindex eller tomma (`sitemap_url_error`, `sitemap_url_redirects`, `sitemap_noindex`, `empty_collection_in_sitemap`). Soft 404 (`soft_404`).
- Canonical: antal per sida (`multiple_canonical_tags`, `duplicate_canonical_tags`), pekar på annan domän (`canonical_offsite`), pekar på sida som inte svarar 200 (`canonical_not_ok`), val som Google gjort (`google_chose_other_canonical` via `site-audit inspect`).
- Robots och AI-botar (`robots_*`, `ai_crawlers_blocked`/`ai_crawlers_allowed`, `llms.txt` i `onsite_kontroll.py`).
- Sidor med trafik som nu ger fel (`traffic_page_broken`, `traffic_page_redirected`, `doda_sidor_med_trafik.sql` bara där adresserna inte är översatta).
- Hreflang och språk (`hreflang_*`, `language_mismatch`, `html_lang_mismatch`). Shopify skriver hreflang själv; temat har normalt inte några (BOS-genomgången).

### 3.7 URL- och handle-regler
- **Handle ändras aldrig utan beslut** (`regler-v1.md` R12a; en handle-ändring kräver 301-omdirigering och påverkar Google, annonser, Merchant Center och externa länkar).
- Genomlysningen **rapporterar** dåliga handles (filnamn som handle `filename_handle`, handle som inte stämmer med titeln, versaler eller tecken) men föreslår dem bara med konsekvenslista: berörda ordrar/visningar i Search Console, antal inkommande länkar, omdirigeringsbehov.
- Omdirigeringar: kedjor, loopar, mål som saknas, tillfälliga (302) där permanenta (301) avses (`redirect_*`). Förslag skrivs till fil (`redirects_import.csv`-formatet) och importeras bara efter Davids ja.

### 3.8 Möjligheter (lyft inte siffror utan underlag)
| Möjlighet | Definition | Källa | Rimlighetskontroll |
|---|---|---|---|
| Hög visning, låg CTR | Sida eller sida × fråga med minst 200 visningar och CTR klart under vad positionen normalt ger | Search Console (`3_toppsidor_med_svag_klickfrekvens.sql`, `sokfragor_luckor.sql`) | Förväntad CTR per position är en **grov tumregel**, inte en mätning av butiken, och överskattar vad som går att vinna på informationsfrågor (T4). Redovisa spannet, inte ett punktvärde |
| Position 5–15 | Sidor och frågor på sidan 1 nederkant eller sidan 2, där titel, rubrik, intern länkning och svarstext kan flytta dem | Search Console | Kontrollera att positionen är ett viktat medel (summerad `sum_position` / visningar + 1), annars blir den fel. Läs sökfrågorna: en informationsfråga på en produktsida är sällan en vinst |
| Köpstarka sidor utan synlighet | Produkter och kategorier med hög konvertering eller intäkt men få visningar | Shopify + GA4 + Search Console | Hög konvertering på få sessioner är brus. Använd fyraveckorsfönster (`flera-sajter.md`) |
| Betalda söktermer utan organisk närvaro | Söktermer som kostar i Ads men saknar organisk sida | Google Ads söktermer (se 2.1: ej byggt) | Kan inte köras förrän söktermsrapporten finns |
| Annonskostnad på produkter som inte kan köpas | Utkast, arkiverade eller slutsålda produkter med annonskostnad | T15 | Ligger utanför SEO men upptäcks i samma datakoppling |

**Rangordning av möjligheterna:** efter intäkt och klick de senaste 90 dagarna, inte efter visningar ensamt. **Små butiker ger brus** (`flera-sajter.md`): redovisa alltid antalet klick bakom en procentsats.

---

## 4. GEO: citerbara sidor i AI-svar

### 4.1 Vad som gör en produkt- eller kategorisida citerbar
Det här är en arbetshypotes. Hur AI-tjänsterna väljer källor går inte att verifiera i repot och ändras. Åtgärderna nedan är också bra för besökare och vanlig sökning, vilket är skälet att göra dem.

1. **Svar först.** Första meningen anger vad produkten eller kategorin är, för vem och viktigaste egenskapen, med verb (`produkttexter-standard.md` avsnitt 4, `regler-v1.md` R11).
2. **Entydiga attribut i fast ordning:** märke, modell, material, mått, vikt, färg, storlek, innehåll/ingredienser, kompatibilitet, i en specifikationsrad eller tabell som kan läsas som text (inte som bild). Enheter skrivs enhetligt.
3. **Bara det som står i produktens egen källa.** Inget hittepå, ingen uppgift från syskonprodukt eller minne (`regler-v1.md` R1). Faktakoll mot tillverkarens sida får göras enligt R1 (v1.6/v1.7) och källan anges.
4. **Jämförelser som hjälper:** på kategorisidor en kort, sann jämförelse mellan typer (till exempel skillnad mellan två modelltyper) och en köpguide som svarar på de frågor besökarna faktiskt skriver (`sokfragor_luckor.sql`). Inga påhittade testresultat eller rangordningar.
5. **Svar på vanliga frågor** (storlek, skötsel, leverans, retur) som kommer från riktiga frågor (Search Console, kundtjänst), står synligt på sidan och är sanna för just den produkten. Standardblocket för leverans, retur och garanti kommer från butiksprofilen, inte från produkttexten.
6. **Ren HTML-text.** Viktig information får inte bara finnas i bilder, flikar som laddas med JavaScript, eller i en app som renderar sent. Verifiera med genomsökt HTML (T20b).
7. **Konsekventa namn** för märke, produkt och butik över sidor, schema och Merchant Center.
8. **Åtkomst:** AI-botar blockeras inte av misstag i robots.txt (`ai_crawlers_blocked`). Att tillåta eller blockera är ett affärsbeslut för kunden, inte en teknisk detalj.
9. **Strukturerad data som stämmer med synlig text** (avsnitt 3.4). Schema som inte stämmer med sidan är värre än inget schema.

### 4.2 Vad som inte ska göras för GEO
- Inga påhittade fakta, omdömen, certifieringar, "testvinnare", priser eller kampanjer (`produkttexter-standard.md` avsnitt 2).
- Inga hälso-, säkerhets- eller skyddslöften utan källa; se faktatextläge nedan.
- Ingen text skriven för att "luras" in i AI-svar (osynlig text, upprepade fraser).

### 4.3 Hur det mäts, och vad som inte kan mätas säkert

| Mått | Källa | Tillförlitlighet |
|---|---|---|
| Besök och köp från AI-tjänster | GA4, `ai_hanvisningar.sql` (T13 del 1) | **Nedre gräns.** Många AI-besök skickar ingen hänvisning och syns som Direct. Följ trenden, inte nivån. Siffrorna är små och osäkra (anges i frågans egen kommentar) |
| AI-botar tillåtna eller blockerade | Genomsökning (`ai_crawlers_*`, `llms.txt`, `onsite_kontroll.py`) | Pålitligt som teknisk kontroll; säger inget om hur ofta sajten citeras |
| Citeras eller nämns sajten i AI-svar | Fast panel med 30–50 frågor per marknad som ställs till AI-tjänster varje månad (T13b), eller Ahrefs Brand Radar (T37) | **Kan inte mätas säkert utan ett beslut.** T13b kräver API-nycklar och kostnad per körning och är inte byggd. Ahrefs-kopplingen svarade "Insufficient" i T36 och är blockerad enligt `standardtester.md`. AI-svar varierar mellan körningar, så en panel visar en tendens, inte en exakt andel |
| AI-översikter i Googles sökresultat | Search Console | **Kan inte mätas säkert.** Om och hur Search Console särskiljer visningar i AI-översikter från vanliga visningar är **Ej verifierat** i repot. Redovisa inte någon siffra för detta |
| Effekt av en GEO-åtgärd | Testlogg (T8), Search Console-klick och GA4-AI-hänvisningar före/efter | Svag för små butiker; se avsnitt 5.3 |

**Rapportregel:** varje GEO-mått i rapporten ska ha en rad "Tillförlitlighet" med en av: *pålitlig*, *nedre gräns*, *tendens*, *kan inte mätas säkert*.

### 4.4 Risker
- **Hittepåfakta.** AI-genererad eller omskriven text som lägger till egenskaper (material, mått, ursprung, kompatibilitet) som inte står i källan. Motmedel: allt som skrivs ska gå att spåra till produktens egen källa eller en angiven webbkälla (`regler-v1.md` R1, R2, R3).
- **Hälso- och säkerhetspåståenden.** Faktatextläget gäller (`regler-v1.md` R4–R6, `produkttexter-standard.md` avsnitt 16): inga skydds-, hälso-, säkerhets-, stabilitets-, effekt- eller kvalitetsord (till exempel "skyddar", "stödjer", "slitstark", "halkfri") utan att de står ordagrant i källan; då återges de som "enligt tillverkaren", högst två per text. Lastgräns, maxvikt, doser och liknande tas bara med ordagrant ur entydig källa.
- **Citerade felaktigheter.** Ett fel i en sida kan spridas via AI-svar och är svårare att rätta än i en sökträff. Därför: hellre kort och sann än lång och osäker.
- **Falska eller kopierade omdömen.** Förbjudna (Omnibus, marknadsföringslagen; se BOS-temagenomgången). Bedömning av juridik tillhör jurist, inte denna metod.
- **Kategorier under spärr.** Om kunden har kategorier där ägaren inte beslutat om påståenden (BOS: `utanfor_tills_vidare` i butiksprofilen) skrivs inga GEO-texter för dem.

---

## 5. Prioritering, verifiering och skrivbarhet

### 5.1 Prioritering: effekt × insats × risk
Varje åtgärd får tre värden och en poäng.

| Värde | Skala | Så sätts det |
|---|---|---|
| **Effekt** (E) | 1–5 | Utifrån de berörda sidornas klick och intäkt de senaste 90 dagarna och hur stor del av dem som berörs. Gäller åtgärder på sidor utan trafik: max 2. Effekt ska bygga på mätt underlag, inte på verktygets "uppsida i procent" (`basgenomgang.md`) |
| **Insats** (I) | 1–5 | 1 = en fil eller en inställning. 3 = hundratals poster via skript. 5 = temaändring, ny struktur eller manuellt arbete per sida |
| **Risk** (R) | 1–3 | 1 = återställbart med sparad före-fil, påverkar inte adresser. 2 = synligt för besökare eller påverkar flera sidor, återställbart. 3 = påverkar adresser/omdirigeringar, tema, strukturerad data, juridik, hälsa/säkerhet, eller går inte att ångra |

**Poäng = (E × 3) ÷ (I × R)**, avrundat. Högre = tidigare. Poängen är en sorteringshjälp, inte ett beslut.

**Regler som går före poängen:**
- Risk 3 görs aldrig i batch och aldrig utan Davids ja per åtgärd.
- Handle-ändringar, borttagning/sammanslagning av produkter, ändring av omdirigeringstabellen och ändring av temakod rapporteras som förslag med konsekvenslista.
- Åtgärder som rör påståenden (hälsa, säkerhet, djurs hälsa, kroppsnära produkter) går via faktatextläget och en granskare.
- Fel i mätningen (taggar, dubbelräkning, samtycke) kommer före åtgärder vars effekt ska mätas (T11, T19), eftersom effekten annars inte går att utvärdera.

### 5.2 Vad är skrivbart via API och vad kräver temaändring

| Åtgärd | Var | Verifierat i repot? |
|---|---|---|
| Produkters SEO-titel och metabeskrivning (skickas alltid som både `title` och `description`) | Admin API (`shopify_api.py:uppdatera_seo`) | **Ja**, används i produktionen för BOS (kräver `write_products`) |
| Produkttitel och beskrivning (HTML) | Admin API | **Ja** (textutrullningen) |
| Kategoritext, SEO-titel och meta för kategorier | Admin API (collections) | Delvis: `kategoritexter-utkast-2026-10-20.md` finns som utkast; skrivväg för kategorier med nuvarande appbehörighet är **Ej verifierat** |
| Alt-text per produktbild | Admin API (bild-/mediafält) | **Ej verifierat** |
| URL-omdirigeringar | Importfil i Shopify-admin (`redirects_import.csv`) eller API | Importfilen är **verifierad** (`site-audit.md`); API-vägen och behörighet för skrivning är **Ej verifierat** |
| Handle | Admin API, men kräver omdirigering | Skrivs inte (R12a) |
| Taggar, status, pris, lager, varianter | Admin API | Rörs inte av genomlysningen |
| **Canonical, hreflang, H1-mallar, strukturerad data (Product, Breadcrumb, Organization, FAQ), robots, Open Graph, laddade appskript** | **Temakod** (Liquid) eller apparnas inställningar | Verifierat för BOS: skrivning till publicerat tema blockeras i verktyget; David gör ändringen i temaredigeraren och Claude verifierar efteråt (`bos-tema-andringar-2026-10-26.md`) |
| `llms.txt` och `robots.txt` | `robots.txt.liquid`-mall i temat; `llms.txt` hanteras av Shopify eller app | **Ej verifierat** hur det styrs per butik |
| Sidor, artiklar (blogg) | Admin API (`read_content`, skriv: annan behörighet) | Skrivbehörighet **Ej verifierat** |
| Appinställningar (omdömesapp, cookiebanner) | Appens egen konfiguration | Ej verifierat per butik |

### 5.3 Verifiering före och efter
Varje åtgärd ska ha tre saker innan den får göras: en **före-fil**, ett **kontrollkommando som kan misslyckas**, och ett **mått med utvärderingsfönster**.

1. **Före-fil:** exakt kopia av nuläget (titel, SEO, beskrivning, HTML, tema-fil) sparad i `rapporter/shopify-original-<datum>/` (R16, R17). Utan före-fil ingen skrivning.
2. **Skrivning:** via skript, aldrig för hand; högst 5 produkter per anrop; torrkörning först; läs tillbaka och jämför tecken för tecken (`diff_text.py`, `verifiera_skrivna.py`); stoppa vid första avvikelse (`textutrullning-rutin.md` avsnitt 1–2).
3. **Teknisk kontroll direkt efter:** kontrollen för just den åtgärden körs om och ska gå från fel till rätt (t.ex. `multiple_canonical_tags` från 2 till 1 per sida, mätt i genomsökt HTML). Nattens nya körning visar det först nästa dygn.
4. **Utfallsmått:** logga i testloggen (T8) med hypotes, startdatum, mått (`gsc_clicks`, `gsc_impressions`, `sessions`, `orders`, `revenue`) och förväntat utfall. Fönstret är valbart; standard 28 dagar mot lika många dagar före, med övriga sidor av samma typ som grov kontrollgrupp. Search Console är slutgiltig först efter cirka tre dagar, så utvärdera tidigast fyra dagar efter fönstrets slut. **Sätt en påminnelse när testet loggas.**
5. **Rapportera inte som åtgärdat** förrän nästa genomlysning visar det (T28).
6. **Små butiker:** med få klick går effekten inte att bevisa statistiskt (BOS experiment 1 hade cirka 36 förväntade klick och hölls inte kvar som test). För Alpha Zoo och B You verifieras därför i första hand att **åtgärden är tekniskt rätt** (rätt text, rätt tagg, rätt canonical), medan trafikutfallet redovisas som tendens med antal klick bakom. Lova inget utfall.
7. **Loggning:** `docs/ANDRINGSLOGG.md`, `rapporter/shopify-andringar-<datum>.md` (före och efter) och beslutsunderlag enligt `CLAUDE.md`.

---

## 6. Särskilt för Alpha Zoo och B You Underwear

Det här är **riskhypoteser från branschkännedom**, inte fynd. Ingenting av detta har kontrollerats mot butikerna eller mot gällande regler, och juridik ska bedömas av jurist eller berörd myndighet. Det som inte kan avgöras utan David står som fråga.

### 6.1 Alpha Zoo (djurprodukter, alphazoo.se / .dk / .fi)
**Risker:**
- **Hälsopåståenden om djur** i foder, kosttillskott och hudvård ("stärker lederna", "förebygger", "hjälper vid allergi"): behandlas som faktatextläge. Endast ordagrant ur källa, "enligt tillverkaren".
- **Preparat som kan vara läkemedel eller bekämpningsmedel** (mot loppor, fästingar, avmaskning): regelverk skiljer sig mellan Sverige, Danmark och Finland, och vissa produkter kan vara förbjudna eller kräva recept i en marknad. Kategorier och produkter där ägaren inte beslutat sätts under spärr (liksom Ashwagandha i Danmark på BOS, `beslut-2026-11-06.md`).
- **Ingredienser, analytiska beståndsdelar och tillsatser** i foder: siffror får bara återges ordagrant och med enhet ur källan; fel i en ingredienslista kan skada djur.
- **Djurart och storlek/ålder:** attribut ska vara entydiga (hund/katt/gnagare, valp/vuxen/senior, viktklass). En produkt som passar fel djur är både en retur och en säkerhetsfråga.
- **Säkerhet:** leksaker, tuggben, koppel, bur och transportbehållare: inga utfästelser om hållfasthet, ofarlighet eller "säker för" utan källa.
- **Tre språk, tre domäner:** Alpha Zoo ska ranka självständigt på svenska, danska och finska. Maskinöversatt eller inkopierad text mellan domäner är en risk (R2 om maskinöversatt källa).
- **Levande djur och djurens välfärd** (om butiken säljer det): kan ha egna regler. **Fråga till David nedan.**

**Frågor som David behöver svara på (Alpha Zoo):**
1. Vilka produktkategorier ska vara **utanför** all textändring och alla GEO-påståenden (läkemedel, loppmedel, kosttillskott för djur, hälsofoder)?
2. Säljer butiken på alla tre marknaderna samma sortiment, eller finns produkter som inte får säljas i en marknad?
3. Är Shopify en butik med tre marknader eller flera butiker? (Utkastet `sites.portfolio.draft.toml` har samma `shop_domain`-TODO för alla tre.)
4. Vilket bolag äger butiken, och vem äger Search Console, GA4 och Google Ads?
5. Är adresserna översatta per språk (`/products/<handle>` olika per domän)? Det avgör om handle-kopplingen i 2.2 fungerar.
6. Finns riktiga kundomdömen, och i vilken app? Finns det omdömen i schemat som inte kommer från kunder?
7. Får AI-botar läsa sajten, eller ska de blockeras?
8. Finns befintliga skrivregler, ordlista (typord) och märken att respektera? Samma som BOS butiksprofil behöver upprättas (`config/butiksprofil-<butik>.json`).

### 6.2 B You Underwear (underkläder, byouunderwear.se)
**Risker:**
- **Bilder och annonspolicy:** underklädesbilder kan begränsas av annonsplattformarna (Google Shopping, Meta) och av filter för säker sökning. Alt-text och bildrubriker ska vara sakliga (plagg, färg, vinkel), aldrig sexualiserande.
- **Storlekar och passform:** storleksguide, måttabell och passform är det besökarna söker efter och ofta det AI-svar citerar; felaktiga mått ger returer. Mått får bara återges ordagrant ur källan, inte omräknas eller antas.
- **Material- och miljöpåståenden** ("ekologisk bomull", "Oeko-Tex", "hållbar", "andas", "antibakteriell"): endast med källa, som "enligt tillverkaren", med certifieringens exakta namn och nummer om källan anger det.
- **Hälso- och komfortpåståenden** ("minskar svett", "ortopedisk", "stöd"): faktatextläge, inga utan källa.
- **Hygienprodukter:** retur- och bytesregler för underkläder (öppnad förpackning) ska stå korrekt i standardblocket och i schemat för returvillkor; felaktig returuppgift i schema eller AI-svar är en konsumentrisk.
- **Kön, kropp och inkludering:** formuleringar om kön, storlek och kropp ska vara kundens egna och konsekventa; genomlysningen ändrar inte profil eller ton.
- **Barnunderkläder (om det finns):** barn- och ungdomsprodukter har i BOS egen linje i beslutsloggen; samma försiktighet gäller. **Fråga till David nedan.**
- **Liten trafik:** `flera-sajter.md` bedömer B You som sannolikt för litet för egna tester. Slutsatser ska därför bygga på tekniskt rätt, inte på trafikutfall.

**Frågor som David behöver svara på (B You):**
1. Finns barn- eller ungdomsmodeller, och ska de ingå?
2. Vilka material- och miljöpåståenden får användas, och vilka certifikat finns som dokument?
3. Vilka bilder får visas i annonser och i Merchant Center, och finns avvisade produkter (T10)?
4. Finns en storleksguide som är kundens egen och stämmer med varje produkts mått?
5. Vilka retur- och bytesvillkor gäller för öppnade underkläder, och står de i butiken?
6. Vilket bolag äger butiken, och vem äger Search Console, GA4 och Google Ads?
7. Finns riktiga kundomdömen, och var visas de?
8. Finns ett skrivet tonläge och en ordlista (typord, märken) att följa?

### 6.3 Frågor som gäller båda
- Får genomlysningen läsa temat i sin helhet (inkl. appinbäddningar)? Utan det blir tema- och schemafynd begränsade och markeras så (BOS-genomgången läste inte `assets/`).
- Vem tar beslut om temaändringar, och vem utför dem?
- Vilka personuppgifts- och bolagsgränser gäller för data i BigQuery (eget Google Cloud-projekt eller samma som Gorilla)?
- Ska genomlysningen vara en engångsrapport eller upprepas kvartalsvis (`basgenomgang.md`)?

---

## 7. Leveransformat

### 7.1 Mall för kundrapporten
Rapporten sparas som `rapporter/seo-geo-genomlysning-<butik>-<datum>.md` och skrivs för en beslutsfattare: vanlig svenska, facktermer förklarade första gången.

1. **Sammanfattning** (högst fem meningar): läget, de tre viktigaste fynden, vad som rekommenderas först.
2. **Omfattning och täckning:** vilka domäner, perioder och källor som ingick, och vad som **inte** kunde läsas eller mätas (med skäl).
3. **Nuläge i siffror:** klick, visningar, CTR, position, sessioner, ordrar och intäkt per sidtyp (produkt, kategori, blogg, övrigt) och per marknad; andel som kunnat kopplas till produkt/kategori; mätkvalitet (T11).
4. **Fynd per område:** (a) titlar och metadata, (b) dubbletter och kannibalisering, (c) länkstruktur och kategoristruktur, (d) strukturerad data, (e) bild-alt, (f) indexering och kanonisering, (g) URL och handle, (h) möjligheter. Varje fynd: vad, antal sidor, exempel (3–5 riktiga adresser), berörda klick/intäkt, källa och period.
5. **GEO:** nuläge (AI-hänvisningar, botåtkomst), citerbarhet per sidtyp, åtgärder, risker, och tillförlitlighet per mått (avsnitt 4.3).
6. **Prioriterad åtgärdslista:** tabell med rang, åtgärd, område, berörda sidor, effekt, insats, risk, poäng, **var den görs** (API eller tema), **verifiering före och efter**, och **beslut som behövs**.
7. **Beslut som behövs från kunden:** en punkt per beslut med alternativ, rekommendation, risk och vad som händer om inget beslutas (samma form som beslutsunderlagen i `CLAUDE.md`).
8. **Frågor till kunden** (avsnitt 6).
9. **Branschspecifika risker** för butiken.
10. **Det som inte är verifierat:** punktlista med "Ej verifierat" och skäl.
11. **Bilagor:** `actions.csv`, listor per fynd, SQL och datum för datakörningarna, före-filer.

### 7.2 Körordning och grov tidsuppskattning
Tiderna är **uppskattningar, inte mätta**, räknade i arbetstid per butik efter att åtkomst finns. Alpha Zoo (tre domäner) bedöms ta cirka 50 % längre än en domän. Väntetiden för åtkomst och för Search Console-export är kalendertid och beror på mottagarna.

| Steg | Innehåll | Vem | Tid |
|---|---|---|---|
| 0 | **Beslut och åtkomst:** David besvarar frågorna i avsnitt 6; åtkomst enligt 2.3 ordnas; Search Console-massexport slås på om den inte redan finns (fyller bara på framåt, så den startas först) | David | 1–3 dagars väntan; cirka 30–60 min per butik |
| 1 | **Åtkomst- och datakontroll:** `site-audit check-access`, `datakvalitet.sql`, mätintegritet (T2, T11), datum då exporterna började, `backfill gsc` och `backfill ga4` | Claude | 0,5 dag |
| 2 | **Teknisk genomlysning:** `site-audit run` (T1), `inspect` (T17a), `cross-domain` för Alpha Zoo (T18), `onsite_kontroll.py` och `schema_kallor.py` (T21, T22), sidhastighet (T6) | Claude | 0,5–1 dag |
| 3 | **Data och koppling:** URL → produkt/kategori, intäkt per produkt ur Shopify, Ads per produkt, täckningsmått (2.2) | Claude | 0,5–1 dag |
| 4 | **Analyser:** 3.1–3.8, möjligheter, kategoristruktur mot sökbeteende | Claude | 1–2 dagar |
| 5 | **GEO:** citerbarhet per sidtyp, AI-hänvisningar, botåtkomst, riskgenomgång; panel (T13b) bara efter beslut | Claude | 0,5–1 dag |
| 6 | **Prioritering och rapport:** poäng, åtgärdslista, verifieringsplan, frågor, beslutsunderlag | Claude | 1 dag |
| 7 | **Genomgång med David:** beslut per åtgärd | David | 1 möte |
| 8 | **Genomförande** (först efter ja): före-filer, skript, återläsning, testlogg, loggning (avsnitt 5.3) | Claude, David för temaändringar | Beror på beslutad omfattning |
| 9 | **Uppföljning:** nattkontroll, utvärdering efter 28 dagar, ny genomlysning vid behov | Claude | Löpande |

**Totalt för steg 1–6:** cirka 4–7 arbetsdagar per butik efter åtkomst. Ordning mellan butikerna: starta åtkomst för båda samtidigt (steg 0), men kör B You först (en domän, minst komplexitet) och använd lärdomarna på Alpha Zoo.

---

## 8. Sammanställning: Ej verifierat och öppna punkter
1. Att begränsad (skrivskyddad) behörighet i Search Console räcker för läsning och URL-inspektion.
2. Hur Search Console redovisar AI-översikter i Google; därför redovisas inget mått för det.
3. Söktermsrapport från Google Ads: finns inte i `ads_api.py`; API-utseendet är inte kontrollerat.
4. Artikelmått (intäkt per produkt) från GA4: inte byggt; Shopify används som facit.
5. Skrivväg via API för alt-text, kategorier, sidor/artiklar och omdirigeringar med denna app och dess behörigheter.
6. Vilken behörighet som krävs för att läsa publicerat tema i denna app, och hur `llms.txt` och `robots.txt` styrs per butik.
7. Format på `item_id` i Alpha Zoos och B Yous produktflöden (avgör `matched`-andelen).
8. Hur AI-tjänster väljer källor; avsnitt 4.1 är en arbetshypotes.
9. Alla branschrisker i avsnitt 6 är hypoteser från branschkännedom; juridiska frågor avgörs av jurist eller berörd myndighet.
10. Ahrefs-baserade mått (sökordsluckor, Brand Radar) är blockerade enligt `standardtester.md` (T36, T37) och ingår inte i metoden förrän David beslutat.
