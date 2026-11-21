# Genomlysning HYPR Nutrition (hyprnutrition.se), fas 1, 2026-11-04

**Läsläge. Inget ändrades i Shopify, tema, Search Console, Analytics eller Google Ads.**
**Begränsning:** Shopify-adminverktyget krävde ny inloggning och kunde inte läsas, så inventeringen bygger på butikens offentliga sidor (products.json, collections.json, sitemap, renderade sidor, hämtade 2026-11-04). Utkast, arkiverade produkter, marknader, kundgrupper, SEO-fält på ej publicerade resurser och temakoden är **inte verifierade**. Butiken är inte verifierad med get-shop-info. Alla siffror nedan gäller publicerat innehåll. Rådata och skript ligger i denna mapp.

## 1. Inventering (publicerat)
| Mått | Värde |
|---|---|
| Produkter | 9 (kreatin 2, energidryck 3, kosttillskott 4). Varumärke: HYPR Nutrition på alla |
| Varianter | 8 produkter har 1 variant; "Singelburk" har 4 (1, 4, 12, 24 burkar: 29/109/199/499 kr) |
| Kollektioner | 5: frontpage (2), all-products (9), energy-drink (3), kreatin (2), protein-water (0 produkter, men sidan är publicerad) |
| Sidor | 9, bloggartiklar 86 (blogg "forskning-o-nyheter") |
| Språk | sv och /en/ i sitemap. Produkttexter svenska, delvis engelska titlar |
| Pris | 29–699 kr. Dyrast: Multivitamin 699 kr |
| Beskrivningslängd (text) | Protect 114 tecken; energidryck 196–283; övriga 911–1 410 |
| Produkter utan egen SEO-titel/meta | Alla har meta. Produkt-SEO-titlar för de två kreatinprodukterna är satta (avviker från produkttiteln); övriga ärver produkttiteln + " – HYPR Nutrition" |
| Dubbletter | Inga exakta titeldubbletter. Typord skiljer: "Energydryck"/"Energidryck", "Kreatin"/"Creatine" |
| Engelska titlar | Delvis: "Micronized Monohydrate", "Micronised Creatine Powder", "Kreatin HYPR – Micronised…"; startsidans meta är på engelska ("Lets get hyped!") |
| Taggar | Blandade och med fel: "kosttillskot" (stavfel), "All products", "creatine", "vitamin"/"vitaminer", "Örter" |

## 2. Påståenden i befintliga produkttexter (listas, ändras inte)
Heuristisk träfflista i `paastaenden_produkter.json` (nyckelord, ska granskas manuellt). Exempel ordagrant ur produkttexterna:
| Produkt | Text | Typ |
|---|---|---|
| Protect (10980689346903) | "Kosttillskott som stärker immunförsvaret." | Hälsopåstående (kräver godkänt påstående och villkor) |
| Multivitamin (10980883628375) | "den ultimata grunden för din hälsa och din energi", "det ditt immunförsvar och ditt skelett behöver", "perfekt balanserad", "potenta antioxidanter" | Hälsopåståenden, generella påståenden, superlativ |
| Kollagen (10980781424983) | "starka leder, spänstig hud", "stimulerar kroppens egen naturliga kollagensyntes", "högkoncentrerad" | Hälsopåståenden |
| PEA Boswellia Curcuminoids (10980734599511) | "låta stelhet … hålla dig tillbaka", "kliniskt relevanta mängder", "välstuderade", "maximal biotillgänglighet" | Hälsopåståenden, nära sjukdom/symptom, studieanspelning |
| Energidryck (3 st) | "höja sin prestation", "uppiggande känsla", 180 mg koffein per burk | Prestationspåstående; koffeinmärkning att kontrollera |
| Kreatin (2 st) | "Ett enkelt och effektivt tillskott", "100% rent"; dosuppgift 5 g per stick; "Följ rekommenderad användning" | Effektpåstående (svagt), näringspåstående ("100 %") |
Bloggen (86 artiklar, i snitt cirka 550 ord): heuristik visar träff på hälsopåstående-ord i 81 av 86 och sjukdomsrelaterade ord i 25 av 86, t.ex. "Vitamin C: stöd för immunförsvar och återhämtning", "Vitamin D: nyckeln till energi", "Så får du djupare sömn med rätt kosttillskott", "Nootropika … mentalskärpa", "Kreatin för hjärnans prestanda". Orden är breda och ger falska träffar (t.ex. "blodtryck" som nämns i allmänna råd); varje artikel måste läsas av människa. 5 artiklar gick inte att läsa ut. Lista: `artiklar_paastaenden.json`.

## 3. Fynd rangordnade efter effekt och risk
| # | Fynd | Effekt | Risk | Förslag (utförs inte) |
|---|---|---|---|---|
| 1 | **Juridiska sidor tillhör ett annat bolag, och leverans-/returpolicy saknas (404).** Köpvillkor och integritetspolicy nämner "Schiacciata AB" och "Bar Schiacciate"; kontaktuppgift info@barschiacciate.se i Organization-data och på "Jobba hos oss"; "Presentkort" gäller "frukost/lunch/middag"; kontakt, ångerrätt, intervju, quiz har tom meta | Hög (förtroende, regelefterlevnad, GEO) | **Hög** (ångerrätt/villkor och personuppgiftsansvarig ska vara rätt bolag, HYPR Sthlm AB) | Fråga ägaren; byt till HYPR:s egna villkor, policy och kontakt; ta bort eller göm irrelevanta sidor (presentkort, jobba hos oss). Kräver beslut |
| 2 | **Hälso- och sjukdomsnära påståenden** i 4 produkttexter och troligen i många artiklar (se avsnitt 2) | Hög | **Hög** (EU 1924/2006, marknadsföringsregler) | Regeluppsättning (`regler-tillskott-utkast.md`) + regulatorisk granskare; sedan granskning produkt för produkt och artikel för artikel. Skriv inget nytt förrän godkänt |
| 3 | **Energidryck: märkning och data.** 180 mg koffein per burk (märkningskrav för högt koffeininnehåll kan gälla, kontrolleras mot etikett); 24-pack har handle "…12-pack" och titel "Energydryck … Rambora" (stavning); "Singelburk" har 4 varianter med inkonsekvent styckepris (29, 27, 16,6, 20,8 kr/burk) och varianternas SKU är omkastade mot antal; taggen "sugar-free" är ett näringspåstående | Medel | Medel–hög | Verifiera mot etikett; rätta titel/typord; dela upp varianter eller förklara prissättning; handle ändras inte utan omdirigering |
| 4 | **Trasig strukturerad data.** Organization-JSON-LD har `"logo": "https:Liquid error (layout/theme line 82): invalid url input"` på alla sidor; sameAs har 8 tomma strängar; två Organization-block per sida; kontaktmail till annat bolag (se #1) | Medel (Google/AI-sökmotorer läser entiteten) | Låg att rätta, kräver temaändring | Rätta i tema (kräver beslut och test på temakopia, jfr LARDOMAR 2026-10-26) |
| 5 | **Produktdata för GEO/Merchant:** SKU är platshållare ("0000-0000-0000-00001" på fyra produkter), inga GTIN/EAN, inga omdömen/betyg i Product-data, kategori är fritext ("Kollagen", "Energidrycker"), Protect beskrivs i 114 tecken | Medel | Låg | Komplettera SKU/GTIN, ingrediens- och näringsdata ur etikett; produkttexter först efter regelgodkännande |
| 6 | **Bloggen är en stor del av sajten:** 86 artiklar mot 9 produkter. Titlar: 84 av 87 sidtitlar över 60 tecken, och suffixet " – HYPR Nutrition" gör att titlar kapas mitt i meningen (t.ex. "…den  – HYPR Nutrition"). Artiklarna riktar sig mot föräldrar ("pappaträning", "mammaträning"), medan startsidans meta och kollektionen "all-products" beskriver "Energy drinks and protein water" (protein water finns inte som produkt) | Medel | Medel (artiklarna bär påståenden, se #2) | Gå igenom artiklar efter trafik (kräver GSC) innan något ändras; behåll, skriv om eller avpublicera efter beslut |
| 7 | **Kollektioner och metadata:** protein-water är en tom publicerad kollektion; frontpage, energy-drink, protein-water och fyra sidor saknar meta; kreatinkollektionen har meta men övriga inte; startsidan har bara märkesnamnet som titel och engelsk meta; endast 2 kollektioner med innehåll | Medel | Låg | Avpublicera/åtgärda tom kollektion; skriv meta (efter regelgodkännande); definiera kollektionsstruktur efter söksökordsdata |
| 8 | **Bilder/alt:** 2–9 bilder utan alt per sida (startsida och energidryckssidor 9) | Låg–medel | Låg | Alt-text efter innehållet |
| 9 | **Tekniskt, positivt/neutralt:** alla 111 sitemap-URL:er ger 200, inga canonical-avvikelser, 1 H1 per sida (utom två sidor utan), inga dubbla titlar, robots tillåter produkter/kollektioner/sidor, `llms`/`agents.md` och UCP-profil finns (Shopifys standard, svarar 200). HTML-storlek 140–255 KB | – | – | Inget |

## 4. Dataåtkomst (verifierat 2026-11-04)
| Källa | Läge |
|---|---|
| Shopify (admin) | **Verktyget krävde ny inloggning** ("sign in again"); inget läst. Du behöver autentisera Shopify-kopplingen i claude.ai-inställningarna. Butiken ska verifieras med get-shop-info före läsning. Ingen API-token för HYPR finns (BOS-appen gäller bara BOS) |
| Windsor.ai `get_connectors` | Endast **Facebook Organic** (konto "Gorilla Sports Nordics"). Ingen Search Console, GA4, Google Ads eller Shopify-koppling för HYPR. Det finns alltså inget Google-konto/projekt för HYPR Sthlm AB kopplat i Windsor |
| Search Console, GA4, Google Ads | **Inte anslutna.** Därmed ingen analys av sökefterfrågan mot sidor (lucka-analys) kan göras. `sites.portfolio.draft.toml` har HYPR med TODO (shop_domain, bq_project, company, ga4_property_id) |
| Ahrefs | MCP svarar **"Insufficient plan"** på prenumerationsfrågan och Site Explorer; Brand Radar prövades inte vidare. Ingen Ahrefs-data använd |
| Repots site-audit-verktyg | HYPR saknas i `sites.toml` (bara utkast). Ingen körning gjord; kräver bolagsbeslut om Google Cloud-projekt (`ny-sajt.md`) och token. Min manuella genomgång ovan täcker titlar, meta, canonical, JSON-LD, H1, alt, sitemap; inte intern länkning, tunna sidor i djup eller Core Web Vitals |
| Bolag | HYPR Sthlm AB är ett annat bolag än Gorilla Sports: eget Google Cloud-projekt (eller bolagets egen) enligt `ny-sajt.md`; ingen data får blandas |

## 5. GEO (hur tydlig är butiken för en AI-sökmotor)
- **Styrkor:** Shopifys agent-/UCP-stöd är aktivt; produkter har namn, pris, valuta, lagerstatus och märke i strukturerad data; artiklar har BlogPosting.
- **Svagheter:** (a) juridisk och kontaktinformation pekar på ett annat företag (#1) vilket ger motstridiga signaler om vem säljaren är; (b) Organization-data är trasig (#4); (c) leverans- och returvillkor saknas: /policies/shipping-policy, /policies/refund-policy och /policies/terms-of-service ger 404, och ångerrättssidan saknar meta (innehållet ej läst); integritetspolicyn under /policies/privacy-policy är Schiacciata AB:s; (d) produktsidorna saknar ingrediens/näringsfakta i strukturerad form och GTIN; (e) texterna är värderande snarare än faktabaserade; (f) varumärkets egen "Om oss" beskriver varumärket i marknadsföringston. Brand Radar kunde inte användas (plan).

## 6. Frågor till David
1. Autentisera Shopify-kopplingen så att admin kan läsas (utkast/arkiverade, marknader, SEO-fält, taggar). Vilken butik är rätt (myshopify-adress)?
2. Köpvillkor, integritetspolicy och kontakt tillhör Schiacciata AB/Bar Schiacciate. Vet du om det? Vilka är HYPR Sthlm AB:s egna villkor, och vem ansvarar för butiken?
3. Vem är regulatorisk granskare för tillskottstexterna (extern jurist, Livsmedelsverkets vägledning, leverantör)?
4. Ska dagens påståenden (immunförsvar, leder, hud, stelhet) tas bort från butiken i en separat, beslutad åtgärd när granskaren sagt sitt, eller ska de ligga kvar tills dess? Detta ändras inte av mig utan beslut.
5. Var finns etikett/deklaration för varje produkt (bild eller leverantörsblad)? Utan dem finns ingen godkänd källa.
6. Ska bloggens 86 artiklar ingå i arbetet (granskning av påståenden) eller hållas utanför?
7. Google-konton: vem äger Search Console, GA4 och Google Ads för HYPR, och ska de kopplas till Windsor eller till ett eget projekt?
8. Ahrefs-planen räcker inte för API. Ska vi uppgradera eller klara oss med Search Console?
9. Typord och ton: Kreatin/Energidryck/Multivitamin? Ska produktnamn som "Rambora/Rambella" behållas?
10. Marknader och språk: ska /en/ vara aktivt, och var säljer ni utöver Sverige?
