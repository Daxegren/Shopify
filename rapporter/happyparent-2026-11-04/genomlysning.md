# Genomlysning Happy Parent (happyparent.store), fas 1, 2026-11-04

**Läge:** bara läsning. Inget ändrades i Shopify, tema, Search Console, Analytics eller Google Ads.
**Källor och begränsning:** Shopify-verktyget krävde ny inloggning och gick inte att använda, så butiken kunde inte verifieras med get-shop-info och ingen admin-data lästes. Allt nedan bygger på butikens **offentliga** data: `products.json` (581 publicerade produkter), `collections.json` (96), sitemaps, robots.txt och 28 hämtade sidor. Det betyder att följande **inte** kunnat kontrolleras: produkter i utkast/arkiverade, sparade SEO-titlar och meta (bara det som renderas), marknader, kollektionsregler, omdirigeringar, sidor utan publicering. Siffror ska läsas som "publicerat och synligt". Skript och rådata: `hamta_offentligt.py`, `inventera_offentligt.py`, `genomlysning_offentlig.py`, `inventering.json`, `inventering_produkter.csv`, `genomlysning_sidor.json`.

## 1. Vad butiken är
581 publicerade produkter i en domän med fyra språkvägar (sv grund, /en, /da, /fi, hreflang finns). Sortiment: leksaker (187 med typen "Leksak", 58 pussel, 29 bilar, 24 babygym), barnkläder från Urban Classics Kids (112) och MT Kids (77), samt egna "Happy Parent"-produkter (367). Priser 29,90–2 199 (valuta antas SEK). 272 produkter har flera varianter; 3 är helt slutsålda; 2 saknar bild.

## 2. Fynd rangordnade efter effekt och risk (åtgärder föreslås, inga utförda)

| # | Fynd | Omfattning | Risk | Effekt | Förslag |
|---|---|---|---|---|---|
| 1 | **CE-märkning och certifiering påstås utan synligt underlag.** Texter säger "CE-märkt", "CE märkning", "CCC-certifikat". Ingen text nämner EN 71, den standard som leksaker normalt prövas mot | ca 210 produkter (189 "CE-märk…") | Hög: regel- och förtroenderisk; felaktigt CE-påstående är ett marknadsföringsproblem | Hög (förtroende, Google Merchant) | Spärra, David anger vilken dokumentation som finns (B3, B4). Ta inte bort i butiken före beslut |
| 2 | **Säkerhetslöften som butikens egen slutsats**: "helt säker för ditt barn att bita på", "säkert material", "Säker och Fällbar Lekhage" (även i titel och meta) | ca 41 produkter | Hög | Hög | Regel B1; omskrivning i faktatextläge efter beslut |
| 3 | **Hälso- och sömnpåståenden**: sovkudde som "förebygger halsbränna" och underlättar matsmältningen; bitleksak som "lindrar obehag vid tandning"; babymobil för "vila och sömn" | ca 29–31 produkter, 1 tydligt medicinskt | Hög | Medel | Spärra (B9, B10). Bör prövas av David först, eventuellt tas produkten ur sortimentet |
| 4 | **Utvecklings- och Montessori-påståenden** ("tränar finmotorik", "främjar inlärning", "pedagogisk") | ca 250 produkter, 153 Montessori/pedagogisk | Medel (varumärkes- och påståenderisk, ingen fara) | Medel | B10: beskriv vad leksaken innehåller i stället för effekt |
| 5 | **Åldersuppgifter varierar och saknas ibland.** 158 texter anger ålder, bara 3 har uttrycklig varning för små delar. Butikens taggar "0 år"–"6 år" ser ut som åldersuppgifter men är sorteringstaggar | 581 | Hög för små delar/batteri (72 nämner batteri, 7 magneter) | Medel | B5–B8: ålder och varning bara ordagrant ur källa; produkter utan varning men med små delar spärras |
| 6 | **Startsidan är 8,3 MB HTML med 2,6 MB inline-skript**, saknar H1 (tom), och svensk startsida har **engelsk meta** ("Handpicked products…"). `/en` har titel "Happy Parents", sv "Happy Parent". 292 av 553 bilder utan alt-text | startsida (alla språk) | Låg risk | Hög (hastighet, första intryck) | Mät med PageSpeed (kräver nyckel, läggs i miljön), rätta H1/meta i tema efter beslut |
| 7 | **Fel H1 på kollektioner.** "Alla produkter", "Bad" och "Present till barn" visar alla H1 "Träpussel för barn som gör lärandet roligt" (3 av 6 provade kollektioner). Pekar på en tema- eller kollektionsmall som återanvänder en rubrik. Kollektioner saknar ofta meta (3 av 6 provade) | 96 kollektioner (urval) | Låg | Hög (kategorisidor driver ofta sökning) | Kontrollera i tema; rätta efter beslut |
| 8 | **Bildernas alt-text saknas nästan överallt**: 579 av 581 produkter har minst en bild utan alt-text (2 766 av produktbilderna i flödet) | 579 produkter | Låg | Medel (SEO, tillgänglighet, GEO) | Alt-text kan genereras från titel + färg ur egen källa (fas 2) |
| 9 | **Titlar**: 25 över 70 tecken; ca 140 klädtitlar på engelska (heuristik: Urban Classics Kids 92, MT Kids 49, plus 33 egna); 16 exakta titeldubbletter; titelsuffix varierar (" – Happy Parent", " \| Happy Parent", " \| Barnkläder online") | se vänster | Låg | Medel | Typordsbeslut (profil TODO), enhetlig titelmall |
| 10 | **Tomma och sällsynta kollektioner**: 14 av 96 tomma (bl.a. `frontpage`, `rabattkod-happy-parent`, `leksaker-for-nyfodda-barn`), 48 av 96 utan beskrivning. `rabattkod-happy-parent` är en tom synlig kollektion vars namn antyder en rabattkod | 14 + 48 | Låg | Låg–medel | Rensa eller fyll; kontrollera att tomma inte ligger i sitemap |
| 11 | **Strukturerad data**: Product-schema finns (brand, sku, offers) och ProductGroup på kläder, men **ingen aggregateRating**, GTIN bara på en del, Organization finns två gånger på alla sidor | alla | Låg | Medel | Dubbel Organization är trolig tema/app-dubblering; kontrollera |
| 12 | **Policytext**: returpolicyn säger "30 dagars öppet köp … ångerrätt i enlighet med distans- och hemförsäljningslagen". Lagstadgad ångerfrist är 14 dagar; 30 dagar är butikens egen frivilliga utökning. Leveranstid 6–12 arbetsdagar och 29 kr frakt under 499 kr står tydligt. Om oss nämner David & Julia men inget bolagsnamn/org.nr på sidan jag läste | policysidor | Medel (formulering) | Medel (förtroende, AI-sök) | David granskar formuleringen; bolagsuppgifter bör synas |
| 13 | **Vendor "redirect"** (1 produkt) och produkttyp tom på 133 + "None" på 53 produkter | 187 | Låg | Låg | Datavård, kräver beslut om typlista |

## 3. Dataåtkomst (utredd)

| Källa | Läge | Konsekvens |
|---|---|---|
| Shopify (MCP) | Kräver ny inloggning; kunde inte köra switch-shop/get-shop-info. Ingen admin-läsning | Inventering och profil bygger på offentlig data. Verifiera butiken och kör om inventeringen när inloggning är ordnad |
| Windsor.ai | Endast `facebook_organic` (konto Gorilla Sports Nordics) är ansluten. **Search Console, GA4, Google Ads, Shopify och Merchant Center är inte anslutna för Happy Parent** | Luckor mellan sökefterfrågan och sidor, och konverteringsdata kan inte analyseras. Kräver att David kopplar källorna (via Windsors anslutningslänk, aldrig nycklar i chatten) |
| Ahrefs | API:t svarar "Insufficient plan" på abonnemang, domänrating och site-audit. Planens gränser kunde inte läsas, och därför gjordes inga fler anrop | Ingen sökordsdata, backlinks eller Brand Radar. Kräver annan plan/åtkomst eller ersättning |
| Repots site-audit-verktyg | Finns (`shopify-sync/src/site_audit`, `docs/site-audit.md`) men Happy Parent finns inte i `sites.toml`; utkastet i `sites.portfolio.draft.toml` har alla TODO (myshopify, bolag, GA4, BigQuery-projekt) | Körs först när åtkomst och `sites.toml`-block finns; ersatt här med en manuell genomlysning av offentliga sidor |
| Offentliga sidor | Fullt läsbara | Underlag för rapporten |

## 4. GEO (hur tydlig butiken är för AI-sökmotorer)
**Styrkor:** Shopifys agentstöd är på (agents.md, `/.well-known/ucp`, `llms.txt`, UCP/MCP-endpoint), robots.txt tillåter crawlning, produktdata har brand/sku/offers, fyra språk med hreflang, leverans- och returvillkor finns som egna sidor och är konkreta (6–12 arbetsdagar, fri frakt över 499 kr, 30 dagars öppet köp).
**Svagheter:** (1) säkerhetsinformation är **oklar och motsägelsefull för en AI**: CE nämns utan standard, "säker" utan grund, åldersuppgifter varierar; en AI-sökmotor som citerar texten sprider löftena vidare, vilket förstärker risk 1–3. (2) Ingen tydlig avsändare (bolagsnamn, org.nr, ansvarig för produktsäkerhet). (3) Startsida utan H1 och med engelsk meta på svensk sida. (4) Inga omdömen/aggregateRating, vilket AI-svar ofta använder som förtroendesignal. (5) Engelska klädtitlar försvagar svenska frågor ("barnbyxor cargo"). **Brand Radar kunde inte köras** (Ahrefs-plan).

## 5. Luckor mellan sökefterfrågan och sidor
Kan **inte** analyseras: Search Console, GA4, Google Ads och Ahrefs saknar åtkomst. Fas 2 (eller fas 1b) kräver att David kopplar åtminstone Search Console och GA4. Utan det är rekommendationerna ovan baserade på sidans egen kvalitet, inte på verklig efterfrågan.

## 6. Frågor till David (gissas inte)
1. Logga in på Shopify-verktyget igen i den här sessionen (claude.ai-konnektorn) så att jag kan verifiera butiken och köra om inventeringen mot admin-data, inklusive utkast och sparade SEO-fält.
2. Vilken `*.myshopify.com` och vilket bolag äger butiken? Vem är tillverkare/importör för "Happy Parent"-etiketten (B4)?
3. Finns försäkran om överensstämmelse (CE) och testrapporter (EN 71) för produkterna? För vilka varumärken?
4. Är butiken bara svensk valuta (SEK) eller säljer den i flera valutor/marknader?
5. Får Search Console och GA4 för happyparent.store kopplas till Windsor (eller till `site-audit`-tjänstkontot)? Finns Google Ads?
6. Vilken Ahrefs-plan gäller? API-åtkomst saknas idag.
7. Är rabattkodskollektionen `rabattkod-happy-parent` avsiktlig?
8. Ska engelska klädtitlar (Urban Classics, MT Kids) översättas, eller är de avsiktligt originalnamn?
