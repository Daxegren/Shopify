# Genomlysning B YOU UNDERWEAR (byouunderwear.se), fas 1

Datum 2026-11-04. Bara läsning av offentliga sidor. Ingenting ändrades i Shopify, tema, Search Console, Analytics eller Google Ads. Rådata: `produkter_publikt.json`, `kollektioner_publikt.json`, `sidor_genomlysning.json`, `robots.txt`, `sitemap.xml`, `agents.md`, `hem.html`; skript: `hamta_publikt.py`, `genomlys_sidor.py`.

## Begränsningar (läs först)
| Källa | Läge |
|---|---|
| Shopify-verktyget (admin) | Krävde ny inloggning under sessionen. Ingen admin-inventering gjord: status (utkast/arkiverat), SEO-fält, taggar per produkt, marknader, lager och dubbletter bland ej publicerade produkter är **okända**. Allt nedan om produkter gäller bara de 13 publicerade |
| Search Console, GA4, Google Ads | **Inte anslutna.** Windsor.ai visar bara ett konto: Facebook Organic (Gorilla Sports Nordics). Luckor mellan sökefterfrågan och sidor kan inte beräknas |
| Ahrefs | Prenumerationen ger "Insufficient plan" (även för gratisverktyget domain-rating). Brand Radar och sökvolymer ej tillgängliga |
| `site-audit` | Inte installerat i sessionen och B You saknas i `sites.toml`; i stället gjordes en handräknad genomgång av 40 offentliga sidor |

Mått är kontrollerade på exempelsidor, inte bara räknade (lärdom 2026-10-26). Bilder utan alt-text räknades dels på produktbilderna i produktflödet (säkert mått), dels som `<img>` i HTML (osäkert: ikoner kan vara dekorativa).

## Inventering (publik, 2026-11-04)
- **Produkter publicerade: 13.** 12 varor + 1 presentkort. Alla märke "BYOU Underwear". Typer: Hipstertrosor 6, Stringtrosor 6, Presentkort 1.
- **Struktur:** modell (Hipster/Thong) × pack (2/5/10) × färg (Svart/Beige) = 12 produkter, varje med storlekar XS, S, M, L (4 varianter). Priser 229 / 499 / 949 kr. Presentkort 200/500/1000 kr.
- **Lager:** av 48 storleksvarianter är 15 slut (S och M slut på Svart i nästan alla pack).
- **Beskrivningslängd:** 623–628 tecken på alla 12 varor (nästan identisk text; skiljer bara på modellnamn). Presentkortet 501.
- **SKU/streckkod:** saknas i flödet (sku = null).
- **Taggar:** 8 produkter har en enda tagg som är en hashtag-sträng ("#seamless #seamlessunderwear #lingerie ...") plus typ/pack; 4 (10-pack) bara typen.
- **Kollektioner: 16** med 2–25 produkter, ingen har kollektionstext. Marknader/språk: sv + språkvägar /da /fi /de /en (sitemap och hreflang på alla sidor).
- **Engelska titlar:** alla modeller heter "Seamless Hipster"/"Seamless Thong" (engelska ord i svensk titel).
- **Utan SEO-titel/meta:** går inte att avgöra publikt med säkerhet. Titeln i `<title>` är lika med produkttiteln på alla 12 varor (ingen särskild SEO-titel). Meta saknas på 7 av 16 kollektioner.

## Fynd rangordnade (effekt, risk)
| # | Fynd | Bevis | Effekt | Risk | Förslag (ej utfört) |
|---|---|---|---|---|---|
| 1 | **Kollektionerna konkurrerar med varandra och är tunna.** 11 kollektioner handlar om samma 12 produkter (hipster, string, seamless, beige/svart, 2/5-pack). Ingen har text. 7 saknar metabeskrivning (`beige-*`, `svarta-*`, `frontpage`). Kollektionen `frontpage` ("Startsida", 2 produkter) är indexerbar | `kollektioner_publikt.json`, `sidor_genomlysning.json` | Hög: kollektionerna är sidorna som ska ranka på "sömlösa trosor", "stringtrosor dam" | Medel: sammanslagning kräver omdirigeringar och kan tappa nuvarande rankning (GSC-data saknas) | Hämta GSC (fråga 3), välj huvudkollektioner, skriv text och meta, slå ihop resten med 301. Utredning först |
| 2 | **Startsidan saknar H1** (tom H1) på alla språk | `h1: ['']` på /, /da, /de, /en, /fi | Medel | Låg (temaändring på kopia) | Temaändring av David, efter exakta före/efter |
| 3 | **Språkvägarna är delvis oöversatta.** /de har exakt svensk titel och meta som /; /da har meta på 28 tecken, /fi på 33; /fi-titeln är engelsk. Kollektionerna på /de visar samma svenska titlar (ej kontrollerat per sida) | `sidor_genomlysning.json` | Medel-hög om marknaderna är på riktigt, annars risk för tunt/dubblerat innehåll | Låg att läsa, medel att ändra | Fråga 4: vilka marknader ska finnas? Annars ta bort språkvägarna ur sitemap/hreflang |
| 4 | **Produkttexten är dubblerad och tunn.** 12 texter à ~625 tecken, nästan identiska för alla pack och färger; antal i pack, material, sammansättning, mått och tvättråd saknas. Meta på 2- och 5-pack är 320 tecken (trunkeras av Google; 155 är gränsen), 10-pack 147–148 | `produkter_publikt.json` | Hög för både sök och köp (storlek är nästa fråga som köparen har) | Hög för innehåll: påståenden som "mycket god andningsförmåga", "hög träningskvalitet", "syns inte genom dina kläder" är leverantörens egna och behandlas enligt R5 | Fas 2 efter Davids beslut om särregler (profilen). Skriv bara det som står i källan; begär materialuppgifter från tillverkaren |
| 5 | **Strukturerad data: Product ok, men tunn och Organization trasig.** Product(Group) med varianter, pris, valuta, lagerstatus och märke finns. Saknas: SKU/GTIN, färg, storlek-fält, material, retur- och fraktuppgifter, betyg. Organization finns **två gånger** (olika logotyper) och den ena har `sameAs` med tomma strängar | JSON-LD på produkt och startsida | Medel (AI-sökmotorer och Google Shopping läser detta) | Låg-medel (temakod) | Temaändring av David; kräver SKU/GTIN i admin för full effekt |
| 6 | **Bilder utan alt-text.** Alla 60 produktbilder i flödet (13 produkter) saknar alt-text. Kollektionsbilderna har alt | `images[].alt` i flödet | Medel (bildsök, tillgänglighet, AI-beskrivning av produkt) | Låg | Alt-text per färg/vinkel genereras av bildkälla; David godkänner (lågrisk) |
| 7 | **Titlar utan sökord och med engelska ord.** Produkttiteln "BYOU Seamless Thong 2-pack - Svart" innehåller varken "stringtrosor", "dam" eller "sömlösa". Typordet kommer sist. Kollektionstitlarna använder däremot sökorden. `<title>` får radbrytningar i temat (ofarligt) | `<title>` på produktsidor | Medel | Medel: handle ändras inte (R12a), men titel och SEO-titel kan | Fråga 5 om typord ("Thong" eller "Stringtrosa"). Skriv SEO-titel ≤43 tecken |
| 8 | **GEO/AI-sökbarhet: bra grund, tomma luckor.** Finns: `agents.md`, `llms.txt`, UCP-profil (`/.well-known/ucp`), robots.txt släpper in crawlers, policys för retur och frakt (`/policies/refund-policy`, `/shipping-policy`), "Om oss". Saknas: storleksguide, FAQ och kontaktsida på gissade adresser (`/pages/faq`, `/storleksguide`, `/kontakt` ger 404; nav ej kontrollerad), materialuppgifter, omdömen, tydlig varumärkesfakta (designer Jessica Rose nämns i produkttexten men inte som varumärkesfakta) | `agents.md`, `llms.txt`, 404-test | Hög: AI-svar om "sömlösa trosor som syns inte" väljer källor med storlek, material och omdömen | Låg | Lägg storleksguide, material och FAQ (David skickar uppgifter). Brand Radar kräver Ahrefs-uppgradering |
| 9 | **Intern länkning/brödsmulor:** kollektionsrubriker har prefixet "Produktserie:" i H1 ("Produktserie: Beige Hipstertrosor") | H1 på alla 15 kollektioner | Låg-medel | Låg (temaändring) | Ta bort prefixet, sätt kollektionens egen rubrik |
| 10 | **Indexering och canonical i övrigt fungerar:** canonical är självrefererande, robots `index, follow`, hreflang med x-default på alla sidor, sitemap per språk | `sidor_genomlysning.json` | – | – | Inget |

Inget av ovan har verifierats mot sökdata. Fynd 1 och 3 kan kräva helt andra prioriteringar när Search Console finns.

## Hur dagens produkttexter ser ut (underlag för särregler)
Gemensam stomme: modellnamn, "skapades tillsammans med designern Jessica Rose", laserklippning/tunt tyg, "mycket god andningsförmåga", "hög träningskvalitet", tre punkter ("Inga kliande eller skavande sömmar", "Extremt mjuka och stretchiga", "Syns inte genom dina kläder"), storleksråd ("välj den större storleken"). Inga sammansättningsuppgifter, inga mått.

## Tillägg (efter att Alpha Zoo-sessionens B You-arbete hittades)
Alpha Zoo-sessionen publicerade en bredare genomlysning på grenen `claude/alphazoo-byou-onboarding`: `rapporter/byouunderwear-genomlysning-2026-11-04.md`, rådata i `rapporter/byouunderwear-2026-11-04/` (inkl. site-audit på 351 adresser) samt `shopify-sync/config/butiksprofil-byouunderwear.json` och `sparrlista-byouunderwear.json`. Filerna är hämtade hit oförändrade. **Den rapporten och de filerna är huvudspåret; ingenting ovan ska dupliceras.** Det som är unikt här eller skiljer sig:
- **Priset 26,00 mot 229,00:** deras katalogläsning gav 26,00 på 2-pack, min gav 229,00 SEK (`produkter_publikt.json`), samma som i schemat. Hypotes, inte verifierad: katalogen lokaliserades till en annan valuta (26 EUR är ungefär 229 SEK) beroende på varifrån anropet gjordes. Avgörs i admin.
- **Taggar:** 9 produkter (8 varor + presentkortet) bär hashtag-strängen, inte 8 som jag skrev ovan. Rättelse av min uppgift.
- **Fynd 1 ovan ("11 av 16 kollektioner överlappar")** är samma sak som deras fynd 9; fynd 4 och 5 (produkttext, schema) som deras 2, 5 och 6. De har dessutom `product_schema_no_image`, trasig intern länk, 38 sidor med samma titel och språkgranskning, som jag inte hade.
- **Unikt hos mig:** förslaget `underklader_sarregler_forslag` (storlek/passform, material, hygien, kön, barn, genomskinlighet, pack/färg) i `shopify-sync/config/butiksprofil-byou.json`. Förslag: flytta de reglerna in i `butiksprofil-byouunderwear.json` när David beslutat och låt `butiksprofil-byou.json` och `sparrlista-byou.json` utgå. Jag har inte raderat något, eftersom det kräver beslut.
- **Skillnad i spärr:** min `sparrlista-byou.json` har en aktiv förslagsspärr för presentkortet; deras lista är tom. Båda är förslag.
- **Processfel:** jag anropade `switch-shop` två gånger, vilket enligt en annan session bryter BEST OF SPORTS-sessionens koppling. Ingen läsning eller skrivning gjordes i BOS. Regel framåt: ingen `switch-shop` eller `get-shop-info` i delad koppling (se `LARDOMAR.md`).
