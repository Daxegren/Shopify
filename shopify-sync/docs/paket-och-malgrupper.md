# Paket och målgrupper för genomlysning och åtgärder

Skapad 2026-11-19 av koordinatorn på Davids uppdrag. Filen fylls bara på. Det här är ett **förslag**, inte ett beslut: inga priser, avtal eller bolagsfrågor är avgjorda. Metoden finns i `playbook-butiksgenomlysning.md`, skripten i `scripts/` (`sajtskanning.py`, `skanning_rapport.py`, `wb_export.py` m.fl.).

## 1. Idén i en mening

En snabb, läsande skanning hittar konkreta problem som vi vet hur man löser och mäter. Varje problem hör till ett paket. Kunden köper de paket som lönar sig, och effekten visas med före/efter mot en baslinje.

## 2. Målgrupper (i prioritetsordning, ett förslag)

| # | Målgrupp | Varför | Vilka paket passar | Skanning som är möjlig utan åtkomst |
|---|---|---|---|---|
| A | **Shopify-handlare med stor katalog** (1 000–50 000 produkter) | Här har vi bevisad metod och verktyg (Workout Brands, Best of Sports). Problemen är mekaniska och stora i antal, så insatsen är lätt att visa | P1, P2, P4, P5, P6 | Publik skanning (`sajtskanning.py`); djup skanning kräver app i butiken |
| B | **E-handlare på andra plattformar** (WooCommerce, Magento, Centra m.fl.) | Samma typer av problem. Åtgärderna kräver plattformens egna verktyg | P3, P4, P6 först; P1/P2 när vi byggt stöd per plattform | Publik skanning fungerar redan |
| C | **Stora företag med informativ hemsida** (ingen webbshop) | Stor volym sidor, ofta eftersatt teknik och metadata; Shopify behövs inte. Kunden är ofta en marknadsavdelning, inte en handlare | P3, P4, P6 | Publik skanning fungerar redan |
| D | **Byråer som vill vidareförsälja** (white label) | Skalar försäljningen | Samma paket | Beror på avtal |

Det finns en spänning här som du bör avgöra: målgrupp C kräver att tjänsten inte bygger på Shopify-specifika begrepp (kollektioner, produkter). `sajtskanning.py` gör det, men åtgärdsdelen för C är manuell tills vi vet vilka CMS som är vanliga.

## 3. Paketen

Varje paket har: vad som levereras, vad kunden behöver ge, hur det mäts, och enheten som styr insatsen. **Tiderna är grova uppskattningar ur Workout Brands och måste bekräftas** (se `tidslogg-genomlysning.csv`).

| Paket | Levereras | Kunden ger | Mäts med | Enhet för insats | Erfarenhet (WB) |
|---|---|---|---|---|---|
| **P0 Skanning** (ingång) | Rapport med fynd per paket, antal och exempel, och rekommenderade åtgärder | URL; för djup skanning en app med läsbehörighet | Antal fynd | Per sajt (några timmar) | Publik skanning tar minuter; djup skanning ca 1–2 timmar inkl. analys |
| **P1 Katalogstädning** | Produktkategori, attribut (till exempel kön), alt-text, dubbletter | Skrivbehörighet i app, godkännande av regler och mappningar | Andel produkter med kategori/attribut/alt; tomma fält före/efter | Per 1 000 produkter och per 1 000 bilder | Kategori 252 produkter och attribut 6 500 produkter tog var sin kväll; alt-text 45 000 bilder tog ca 1,5 timmar körtid |
| **P2 Kollektioner och struktur** | Regelfixar, tomma sidor omdirigerade, avpublicering, internlänkning | Ägaren avpublicerar (verktygsgräns hos oss); beslut om omdirigeringar | Antal tomma sidor; antal sidor som ger trafik | Per kollektion | 3 regelfixar och 25 omdirigeringar på ca en timme |
| **P3 Teknisk SEO** | Canonical, indexering, sitemap, schema, svarstid | Åtkomst till tema/CMS för ändringar | Indexerade sidor, schemagiltighet, svarstid | Per mall och per sajt | Ej utfört än utanför Shopify-data; kräver temaåtkomst |
| **P4 Innehåll och metadata** | SEO-titlar och beskrivningar, kategoritexter, produkttexter | Godkännande av ton och regler | CTR och position per sida mot kontrollgrupp | Per sida (kollektioner: ca 20–40 minuter per omgång om 7–21 sidor) | 42 kollektioner på tre omgångar inkl. översättning |
| **P5 Språk och marknader** | Översättning av saknat och föråldrat, hreflang | Vilka marknader som är aktiva | Täckning per språk; trafik per land | Per språk och 1 000 texter | Täckningsrapport över 19 språk tog en kväll |
| **P6 Mätning och uppföljning** | Baslinje, jämförelse efter 7 och 28 dagar, månadsrapport | Tillgång till Search Console | Klick, CTR, position, indexering mot kontrollgrupp | Per sajt och månad | Baslinje och indexeringskontroll ca 2 timmar första gången |

## 4. Det jag föreslår att du gör först

1. **Mät Workout Brands efter en vecka (2026-11-26)** och se om titlarna, tomma sidorna och kategorierna har gett något. Utan det är allt löfte.
2. **Kör `sajtskanning.py` på 3–5 sajter du känner** (egna, och gärna en informativ företagssajt) för att se vad en skanning faktiskt hittar och hur lång den tar. Det visar också om målgrupp C är rimlig.
3. **Bestäm ingångserbjudandet.** Mitt förslag är en gratis eller billig skanning (P0) som visar fynd och uppskattad insats per paket, och som är den enda delen som inte kräver att kunden ger någon åtkomst.
4. **Besluta prissättning själv.** Det här dokumentet anger bara vad som driver insatsen.

## 5. Frågor till David (obesvarade)

- Vem säljer tjänsten, och i vilket bolag eller varumärke? (Berör ägande och ansvar; hör ihop med Översikt, och med hur Ecomduct och Cockpit X hålls isär enligt grundlagarna.)
- Vilka plattformar bör vi lära oss först efter Shopify?
- Hur hanteras kunders personuppgifter och åtkomst i avtal? Vem är personuppgiftsansvarig, och var lagras exporterna?
- Ska skanningen vara en tjänst vi kör åt kunden, ett verktyg kunden kör själv, eller båda?

## 6. Risker att vara ärlig om

- **Effekt är inte bevisad än.** Vi har bara en baslinje. En del förbättringar (alt-text, kategorier) är rena kvalitetsåtgärder med osäker sökeffekt.
- **Insatsen beror på kundens katalog.** Workout Brands har 15 000 produkter och 674 kollektioner; en liten butik har betydligt färre fynd och mindre att sälja.
- **Skanningen är underlag, inte facit.** Rapporten säger det själv, och varje fynd ska granskas av en människa före åtgärd.

## 7. Tillägg 2026-11-20: två paket för det som inte syns på sajten
Utöver paketen ovan finns två paket som arbetar utan att röra kollektioner och sajtens synlighet (se playbook, avsnitt 10):
- **Kanaler och produktflöden:** produktkategori och obligatoriska attribut för TikTok Shop, Meta Shop, Google Shopping och Pinterest. Mäts med flödesstatus per kanal. Referens: Gorilla Sports 2026-11-20 (100 produkter kategoriserade, 133 återstår). Effekt inte mätt.
- **Filter och attribut:** standardattribut för filter i butikens sökning, till exempel Avsett för (kön). Referens: Workout Brands (6 186 produkter fick könsvärde via kategori). Gäller bara butiker där filtret används.
Båda sålda separat från paketen för kollektioner och SEO, så att kunden ser vad som syns på sajten och vad som bara förbättrar kanalerna.
