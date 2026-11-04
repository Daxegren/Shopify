# Genomlysning Alpha Zoo (alphazoo.se, .dk, .fi), 2026-11-04

Fas 1: bara läsning. Inget ändrades i Shopify, tema, Search Console, Analytics eller Google Ads.

## Vad som är undersökt och vad som saknas (läs först)
| Källa | Läge |
|---|---|
| Shopify Admin (status, SEO-fält, översättningar per produkt, kollektionsregler) | **Saknas.** Shopify-verktyget kopplades loss när jag bytte butik (`switch-shop`) och kräver ny inloggning av David. Siffrorna nedan kommer i stället från butikens publika katalog (`/products.json`, `/collections.json`), publika sidor och verktygets genomsökning. Publika katalogen visar bara **publicerade** produkter, så antal utkast/arkiverade är okänt. |
| Search Console, GA4, Google Ads (via Windsor) | **Inte anslutna.** Windsor har bara Facebook Organic. Anslutningslänkar finns i beslutsfilen. |
| Ahrefs | **Ingår inte i planen** (alla anrop ger "Insufficient plan"). Brand Radar och sökvolymer kunde inte läsas. |
| Genomsökning med repots site-audit (utan admin) | **Klar** för alphazoo.se: 816 adresser i 27 sitemaps, 400 genomsökta, 1 061 fynd (0 kritiska, 113 höga). Rådata i `rapporter/alphazoo-2026-11-04/site-audit-se/`. |

Rådata: `rapporter/alphazoo-2026-11-04/` (`se|dk|fi/products_public.json`, `inventering.json`, `sidor_*.json`, `produktsidor_se.json`).

## 1. Inventering (publik katalog, 24 produkter)
- **Butik:** en Shopify-butik (`e71myt-1k.myshopify.com`) med tre domäner som David nämnt (.se, .dk, .fi) **plus alphazoo.no, som svarar 200 och finns i hreflang**. Språk i sajten: sv, da, en, fi, nb.
- **Produkter:** 24 publicerade. Typ: Kosttillskott 11, Hundmat 7, kattmat 2, Vård 2, Bajspåse 2. Märke: "Alpha Zoo" 22 och "AlphaZoo" 2 (stavningsvariant).
- **Varianter:** 1 variant på 2 produkter, 2 på 14, 4 på 8 (t.ex. påsstorlek 120/600 st).
- **Beskrivningar:** 504–1 038 tecken (median 739), inga tomma. Inga dubblettitlar. Titlar max 67 tecken. Inga engelska titlar.
- **Bilder:** 119 produktbilder, **119 utan alt-text** (100 %).
- **Kollektioner:** 62, **alla 62 utan beskrivning**, 4 tomma (fastingspray, hundsnacks, milt schampo, äggskalspulver) men med i sitemap.
- **Taggar:** sökordstaggar på svenska och engelska (hund, dog, hundmat, dog food, kosttillskott, tillskott m.fl.). Blandning av språk i taggar.
- **Översättningar:** sidor finns på da, en, fi, nb för produkter, kategorier, sidor och blogg (24 produkter × 4 språk). Per-produkt-status (översatt/ej översatt/föråldrad) kräver Admin.
- **Okänt (kräver Admin):** produkter per status, SEO-titel/meta-fält som uttryckligen satta, leverantör utöver märket, kollektionsregler.

## 2. Fynd, rangordnade efter effekt och risk
| # | Fynd | Belägg | Effekt | Risk att åtgärda |
|---|---|---|---|---|
| 1 | **.dk och .fi pekar kanoniskt på .se.** På alphazoo.dk och alphazoo.fi är `canonical` `https://alphazoo.se/...` (hem, produkt och kategori; produktadressen byts dessutom till översatt handle på .se). Samtidigt anger hreflang `da-DK → alphazoo.dk` och `fi-FI → alphazoo.fi`. Signalerna säger emot varandra, och Google kan välja att inte indexera .dk/.fi alls. | `sidor_dk.json`, `sidor_fi.json` | **Mycket hög** (hela DK/FI-marknaden) | Medel: gäller domäninställningar i Shopify Markets och tema. Kräver beslut och test. Ändra inte utan plan. |
| 2 | **Ingen H1 på någon sida av 113** (startsida, alla 24 produktsidor, flera sidor). Två sidor har dubbel H1. | site-audit `missing_h1` 113, `produktsidor_se.json` | Hög | Låg–medel (temaändring) |
| 3 | **SEO-titel för "Nötköttsmåltid" är kopierad från "Lax- & kalkonmåltid"** (sidans `<title>` säger Lax & kalkon, sidans rubrik och og:title säger Nötkött). Metabeskrivningarna verkar inte vara satta explicit (att bekräfta med Admin): metan är lika med första raderna av beskrivningen från första raderna av beskrivningen (median 159 tecken, 13 av 24 över 155, genomsökningen fann dessutom 45 sidor utan meta). Dubbelkodad text i meta: `&amp;amp;`. | `produktsidor_se.json` | Hög (klickfrekvens) | Låg (text i SEO-fält) men **faller under spärrad kategori (foder)**, se beslut A |
| 4 | **Alt-text saknas på alla produktbilder** (119/119) och på 399 bilder i genomsökningen (alla språk). | `inventering.json`, site-audit | Medel (bildsök, tillgänglighet) | Låg |
| 5 | **Organization-schemat har trasig logotyp** ("Liquid error ... invalid url input") och säger bara `availableLanguage: Swedish` på alla marknader. sameAs pekar på `facebook.com/alpazoo` (en "h" mindre än butiksnamnet; verifiera). | `by_pdp`/`az_pdp` JSON-LD | Medel (entitetssignal, GEO) | Låg (tema) |
| 6 | **Produktschemat saknar frakt och retur** (`shippingDetails`, `hasMerchantReturnPolicy`) och aggregateRating, fast sajten visar "4,68* baserat på 1 420 omdömen" i sidhuvudet. Offer, brand, sku och gtin13 finns. | site-audit `shipping_details_missing` 103, `product_schema_no_rating` 103 | Medel | Låg. Betygsuppgiften måste ha en verifierbar källa (omdömesapp) innan den marknadsförs i schema. |
| 7 | **Översättningar av låg eller ogranskad kvalitet:** dansk kategori heter "Hundemåtte" (bör vara t.ex. "Hundefoder"; "måtte" betyder matta) och metabeskrivningen är blandad ("Kolla i vores store sortiment af hundemat"). Danska/finska/norska bloggsidor är på svenska (3 sidor, 56 % svensk text). | `sidor_dk.json`, site-audit `language_mismatch` | Medel–hög för DK/FI | Kräver **modersmålstalare**, inte modell |
| 8 | **hreflang med 20 varianter per sida** och blandade språk-/landkombinationer (t.ex. `sv-DK`, `nb-FI`, `fi-NO`). Är ofta korrekt Shopify-beteende, men tillsammans med fynd 1 skapar det oklarhet. | `hreflang_many_variants` | Medel | Medel |
| 9 | **Tunna och tomma kategorier:** 62 kategorier utan beskrivning, 4 tomma i sitemap, 90 kategorisidor visar färre än 4 produkter, `frontpage`-kollektionen är tom men indexerbar. Med 24 produkter men 62 kategorier är strukturen överbyggd (kategorier per ingrediens/funktion). | `inventering.json`, `collection_few_products` 90 | Medel | Medel (omdirigeringar behövs) |
| 10 | **Titlar för långa:** 15 av 24 produkttitlar (`<title>`) över 60 tecken (max 79), 118 sidor totalt. Meta för lång på 139 sidor. | site-audit | Låg–medel | Låg |
| 11 | **Dubblerat innehåll:** "Om oss" och "Intervju" identiska på da/en/fi; felstavat varumärke "alphazoon". | site-audit | Låg | Låg |
| 12 | **Varumärkesstavning:** "Alpha Zoo" vs "AlphaZoo" (leverantörsfält, 2 produkter). | `inventering.json` | Låg | Låg (men blockerar R8-enhetlighet) |

## 3. Risk i innehållet (styr spärrlistan)
Av 24 produkter är **22 foder, kosttillskott eller vård**. Produkttexterna och navigationen innehåller påståenden som "Immunsystem", "Maghälsa", "stödja mage och tarm", "för frisk päls", "Lugnande", "100 % naturliga ingredienser" och "spannmålsfritt". Kosttillskott och fodertillsatser för djur omfattas av foderlagstiftning (bl.a. märkning, bruksanvisning och förbud mot medicinska påståenden). Det är skälet till att jag **föreslår** `utanfor_tills_vidare` enligt butiksprofilen. Slutlig avgränsning är Davids beslut (se Beslut A).

## 4. GEO (synlighet i AI-svar)
- **Bra:** robots.txt blockerar inga AI-botar (GPTBot, ClaudeBot, PerplexityBot m.fl. kan läsa). Shopify publicerar `agents.md`, `llms.txt` (standardinstruktioner för agenter) och UCP-adress (`/.well-known/ucp`, `/api/ucp/mcp`), alltså är katalogen redan maskinläsbar för shoppingagenter.
- **Saknas:** inget märkesspecifikt innehåll för AI-svar: `llms.txt` är Shopifys standardtext, ingen entydig "vad är Alpha Zoo"-sida med fakta (ursprung, ansvarig avsändare, fodertyp), Organization-schemat är trasigt (fynd 5), frakt- och returfakta står på sidor (`leveransinformation`, `byten-och-returer`) men inte i strukturerad data (fynd 6), FAQ finns som sida men saknar FAQPage-schema (liten effekt i Google, men entydiga svar hjälper AI-svar).
- **Mätning:** Brand Radar och Search Console-frågor kunde inte läsas (se tabellen överst). Nuvarande synlighet i AI-sökning är därför **okänd**, inte noll.

## 5. Åtgärdsförslag (inget utfört)
1. Utred kanoniska adresser och marknadsdomäner för .dk/.fi (fynd 1) i Shopify Markets: bekräfta att varje domän är *primär domän för sin marknad* och inte omdirigerad/alias till .se. Mät först i Search Console (indexerade sidor per domän).
2. Lägg en H1 i temat på startsida och produktsidor (fynd 2).
3. Rätta SEO-fälten (fynd 3) som en egen, liten, granskad batch, men först när David beslutat om foderkategorin (Beslut A).
4. Alt-texter på produktbilder som mall `{produkt} – {variant}` (fynd 4), sedan manuell kontroll.
5. Korrigera Organization-schemat (logotyp, sameAs, språk) och komplettera Product-schemat med frakt/retur (fynd 5–6).
6. Låt modersmålstalare granska da/fi/nb-översättningar innan någon ny text läggs in (fynd 7).
7. Slå ihop eller dölj tomma kategorier med omdirigering; skriv kort faktatext på de som blir kvar (fynd 9).

## 6. Beslut som krävs av David
A. **Spärr för foder, kosttillskott och vård** (22 av 24 produkter). Alternativ: (1) alla utanför tills vidare, bara 2 bajspåsar kvar (säkrast, men nästan ingen volym); (2) foder utanför, tillskott/vård som ren fakta utan effektpåståenden; (3) allt som ren fakta, "enligt tillverkaren" för varje påstående. **Rekommendation: (2)**, med produktspecifik genomgång av tillskotten.
B. **Språk:** bara svenska i fas 2 (rekommenderas) eller även da/fi med modersmålsgranskare? Ska .no och nb ingå?
C. **Domänplan** för .dk/.fi (fynd 1): ska domänerna vara egna marknadsdomäner med egen indexering, eller ska allt konsolideras på .se?
D. **Åtkomst:** godkänn Windsor-länkarna (Search Console, GA4, Google Ads) och logga in i Shopify-anslutningen för Alpha Zoo (läs). Ahrefs-planen räcker inte för API.
E. **Tonläge** (profilen: saklig faktatext, inte "Skäm bort din hund").
