# Granskningsutlåtande k_39a och k_39c (2026-11-07)

Den här granskningen har bara läst i Shopify och har inte ändrat något där. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient) mot BEST OF SPORTS (`6f2e53-67.myshopify.com`). Underlaget är `regler-v1.md` (R1–R19, v1.5–v1.10), BESLUTSLOGG till och med 2026-11-07, LARDOMAR (inklusive 2026-11-05 om rättningar med flera delar), butiksprofilen och praxis i `k_utlatande_34ab.json`, `36ab` och `38a`. `skrivfil_kontroll.py` gav 0 fel. Den varnade för två cirkulära inledningar, 39021 och 39023, och båda rättas nedan. Standardblocket är exakt som i `b_skriv_24.json` på alla 25 produkter, och 39072 har dessutom leveranstidsmeningen. Titel, SEO-titel och meta är unika mot alla andra utkast och skrivfiler. Samma gäller de föreslagna nya värdena.

Varje rättning anges som **ett** sammanhängande före/efter-par per fält. När en html-rättning gäller flera ställen ersätts hela textdelen före standardblocket som en enda bit. Den maskinläsbara versionen finns i `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_39ac.json`.

## Resultat: 18 godkända, 7 att rätta, 0 underkända

| nr | id | produkt | dom |
|---|---|---|---|
| 39001 | 10406816186634 | Kettlebell Tunturi 24 kg | GODKÄND |
| 39002 | 10411603558666 | Träningsgummiband Tunturi Textile Medium | GODKÄND |
| 39003 | 10411704320266 | Sadel Selle Monte Grappa Venice, brun | GODKÄND |
| 39004 | 10411761336586 | Massagerulle Tunturi Yoga Foam Grid Roller | GODKÄND |
| 39006 | 10411861213450 | Klassiska skidor Peltonen Infra C 188 cm | RÄTTA |
| 39012 | 10462199120138 | Mountainbike Giant Talon 29 3 GE | GODKÄND |
| 39013 | 10462224777482 | Hantlar Tunturi Neoprene 2 x 2 kg | GODKÄND |
| 39014 | 10462756405514 | Gymnastikboll Zipro Premium 65 cm | GODKÄND |
| 39015 | 10462764040458 | Massagebollar Tunturi, 4 delar | GODKÄND |
| 39016 | 10462770987274 | Proteinpulver Trec Gold Core Whey, jordnötssmör | GODKÄND (obs) |
| 39017 | 10462771151114 | Proteinpulver Trec Gold Core Line, choklad | GODKÄND |
| 39018 | 10462773182730 | Vitaminkapslar Trec D3 + K2 | GODKÄND (obs) |
| 39021 | 10462847467786 | Hammer Puzzlemat Professional | RÄTTA |
| 39022 | 10462853136650 | Balanscykel Giant Pre Push Bike, Phoenix Fire | GODKÄND |
| 39023 | 10468718051594 | Multigym Hammer Ferrum TX3 | RÄTTA |
| 39050 | 10472237465866 | Solglasögon Shimano S23X | GODKÄND |
| 39054 | 10472240087306 | Innerslang Continental MTB 29+ | GODKÄND |
| 39057 | 10472242086154 | Skidstavar Alpina ST Plus | GODKÄND |
| 39062 | 10472244281610 | Antifrys Start Skin Glide Spray | GODKÄND |
| 39064 | 10472245002506 | Handtagstejp Giant Connect Gel, gul | RÄTTA |
| 39066 | 10472246837514 | Stänkskärmset Hebie Taipan 26 tum | GODKÄND |
| 39067 | 10472248443146 | Stänkskärmar SKS Beavertail Set | GODKÄND |
| 39068 | 10472251523338 | Cykelstöd Azimut 20–29 tum | RÄTTA |
| 39070 | 10472261878026 | Damcykel Liv Tempt 2, 29 tum | RÄTTA |
| 39072 | 10472263123210 | Mountainbike Giant Talon 29 2 | RÄTTA |

## Rättningar

**39006 Peltonen Infra C** (html). Källan säger "För skidbindningar rekommenderar vi", alltså säljaren och inte tillverkaren. Raden skrivs därför som på det skrivna syskonet 10411722506506.
- före: `<li>Rekommenderade bindningar enligt tillverkaren: Xcelerator 2.0 CL eller Performance CL</li>`
- efter: `<li>Rekommenderade bindningar: Xcelerator 2.0 CL eller Performance CL</li>`

Längden 188 cm godtas. smartech.ee svarar 403 för granskaren, men adressens sökväg (`...infrac2122stiff188...`) och leverantörens längdkod `T###` stämmer. Samma kod gäller Alpina-stavarna 39057, där varianterna 135–160 cm motsvarar T135–T160. Syskonet R00T202 är en annan längd, så produkten är ingen dubblett.

**39021 Hammer Puzzlemat Professional** (titel, seo_title, meta, html). Utkastet motiverar typordet med att syskonet heter "Golvmatta Hammer Puzzlemat Basic", men det stämmer inte: det skrivna syskonet 10650169508106 heter **Träningsmatta** Hammer Puzzlemat Basic. Live-titeln här säger också "träningsmatta". Typordet byts därför, och den cirkulära inledningen tas bort.
- titel: `Golvmatta Hammer Puzzlemat Professional, 156 x 104 x 2,5 cm` → `Träningsmatta Hammer Puzzlemat Professional, 156 x 104 x 2,5 cm` (63 tecken, 2 kommatecken)
- seo_title: `Golvmatta Hammer Puzzlemat Professional` → `Träningsmatta Hammer Puzzlemat Professional` (43 tecken)
- meta: `Golvmattan Hammer Puzzlemat Professional består av ...` → `Träningsmattan Hammer Puzzlemat Professional består av sex delar och mäter 156 x 104 x 2,5 cm. Den går att fälla ihop och utöka med en 2-delad förlängning.` (155 tecken)
- html (hela delen före standardblocket, se JSON): första meningen blir "Hammer Puzzlemat Professional består av sex delar och mäter 156 x 104 x 2,5 cm. Träningsmattan är avsedd att ...", "golvmatta" blir "träningsmatta" i Passar för, och raden blir `Typ: Träningsmatta`.

**39023 Multigym Hammer Ferrum TX3** (meta, html). Typordet Multigym behålls. Det är etablerad svenska, står i live-titeln ("Multi-gym") och är samma som på det skrivna syskonet Ferrum TX2.

Raden "Maximal belastningsvikt: 120 kg" är rätt utelämnad. Den är en maskinöversättning av leverantörens "Maximum operating weight" (LARDOMAR 2026-11-04), och det framgår inte vad lasten gäller. Webbsökningen enligt v1.10 gav 120 kg bara hos återförsäljare (OTTO, discounto.de, velomarket). Manualen på manualslib gäller art.-nr 9035, inte 9038. Enligt v1.10 och beslutet om 32069/32070 ska texten då ange "Ej känd". Det saknades i utkastet.
- meta: `Hammer Ferrum TX3 är ett multigym med bröstpress, ...` → `Multigymmet Hammer Ferrum TX3 har bröstpress, ryggpress, benpress och kabelpress och väger 147 kg. Maximal lastgräns är inte känd.` (130 tecken)
- html (hela delen före standardblocket, se JSON): inledningen blir "Multigymmet Hammer Ferrum TX3 för styrketräning hemma har bröstpress, ryggpress, benpress och kabelpress. Det är 210 x 120 x 198 cm och väger 147 kg. Maximal lastgräns är inte känd.", och raden `<li>Maximal lastgräns: Ej känd</li>` läggs till efter Vikt.

**39064 Giant Connect Gel, gul** (html). "Material: Gel" står inte i källan, som bara säger att tejpen har "en gel". Raden tas bort.
- före: `<li>Material: Gel</li>\n<li>Ingår:` → efter: `<li>Ingår:`

**39068 Cykelstöd Azimut** (titel, seo_title). Typordet ska stå först (R7), som på de skrivna Cykelstöd OXC Deluxe och Giant KSA. Raden "Ej känd" (v1.10) är rätt.
- titel och seo_title: `Justerbart Cykelstöd Azimut, 20–29 tum` → `Cykelstöd Azimut, Justerbart, 20–29 tum` (39 tecken)

**39070 Liv Tempt 2** (titel, seo_title, meta). Produkten har två varianter med samma SKU och EAN men olika pris (13 449 och 11 699 kr), och den ena är en överbliven Default Title. Både v1.7 ("skrivs utan färg … i titeln", som 10113) och v1.9 (titel och SEO låser inte färg när priserna skiljer) ger samma svar: färgnamnet Ocean Wave tas bort ur titel, SEO och meta. Raden `Färg: Ocean Wave` i specifikationen får stå, eftersom båda varianterna är samma artikel.
- titel: `Damcykel Liv Tempt 2, 29 tum, Ocean Wave` → `Damcykel Liv Tempt 2, 29 tum`
- seo_title: `Damcykel Liv Tempt 2 29 tum, Ocean Wave` → `Damcykel Liv Tempt 2, 29 tum`
- meta: `Damcykeln Liv Tempt 2 i Ocean Wave har ...` → `Damcykeln Liv Tempt 2 har aluminiumram, Shimano Altus, hydrauliska skivbromsar och en gaffel med 100 mm slaglängd. Däcken är 29 x 2,2 tum.` (138 tecken)

**39072 Giant Talon 29 2** (seo_title). SEO-titeln saknade typordet (R7). Med komma blir den 44 tecken, så kommat tas bort. Leveranstidsmeningen finns och är rätt placerad (taggen På beställning), och storlekar och priser låses inte (v1.9).
- `Giant Talon 29 2, 29 tum, Phantom Green` → `Mountainbike Giant Talon 29 2 Phantom Green` (43 tecken)

## Särskilda kontroller

- **Kosttillskott (39016–39018):** texterna innehåller bara produktfakta, ingredienser, dos, förvaring och tillverkarens varningar. Inga hälso-, viktminsknings- eller prestationspåståenden finns, och typordet anger kosttillskott. Upplägget är detsamma som på de skrivna syskonen. Falsklarmet "halsa" gäller produktnamn och ingredienser och har bedömts manuellt utan anmärkning.
- **Typord:** Träningsgummiband (39002) och Massagerulle (39004) är korrekt svenska och samma som på de skrivna syskonen 10472238547210 och 10472259092746. Multigym (39023) är också korrekt svenska, se ovan. Ingen av dem behöver rättas, men de tre orden bör läggas in i profilens `godkanda_typord`.
- **39014 Zipro (tunn källa):** EAN, 65 cm och grå bekräftades på morele.net. Maxlasten 150 kg finns bara hos återförsäljare och används inte, vilket är rätt. Gymnastikbollen Spokey skrevs också utan lastgräns.
- **39012 och 39072 Talon:** de har olika modeller och färger. Det finns ingen skriven dubblett live.
- **39003 Venice:** produkten är ingen dubblett. Det skrivna syskonet (SKU 1730) var ursprungligen svart, och den här är brun.
- **Säkerhetsprodukter:** ingen har slunkit med bland utkasten.

## Avvisade

Avvisningen står för 21 av 23 produkter. En avvisning har fel skäl och en produkt bör lyftas:

- **39010 Shimano CS-M8000 11-42 (kassett): avvisningsskälet är fel, och produkten kan släppas till ett nytt utkast.** Kassetter avvisas inte enligt praxis. Kassett Shimano CS-HG41-7 skrevs i `k_skriv_32ab` som bärande del med "Maximal lastgräns: Ej känd" (v1.10), och v1.10 undantar bara bromsdelar, trampoliner, hjälmar och barntransport. Källan ger entydigt Deore XT, DYNA-SYS11, drevbärare i legering och en kombination av aluminium- och ståldrev, och titeln anger 11–42 och 11 växlar. Ett nytt utkast ska ha "Ej känd" om webbsökningen inte ger en lastgräns.
- **39065 Hebie Fix 18:** avvisningen står. Butikens titel "Bakre stödhjul" är troligen fel, eftersom artikeln och taggen gäller ett stödben. Det bör rättas av David eller leverantören, inte i en text.
- Avvisningen står också för hjälmar (39008, 39024, 39051, 39071), lås (39007), belysning och batteri (39011, 39053), bromsdelar (39055, 39059, 39061, 39063), trampolin (39019), elcykel (39069), olika artiklar (39005, 39020), motsägelser (39009, 39056, 39058, 39060) och tunn källa utan webbträff (39049, 39052).

## Frågor till David

1. **39016 (jordnötssmak):** ska källans allergenrad "Kan innehålla mjölk, soja, vete, korn, havre, ägg, jordnötter och nötter" tas med ordagrant på kosttillskott? Den är utelämnad på alla skrivna Trec-produkter. Rekommendationen är ja, åtminstone på produkter med nötsmak. Om inget beslutas förblir det som idag.
2. **39018:** källan har varningen om azorubin ("kan ha negativa effekter på barns aktivitet och uppmärksamhet") men ingen ingredienslista. Ska varningen återges? Den kan vara en lagstadgad märkning. Rekommendationen är att ta med den ordagrant som "enligt tillverkaren".
3. Ska Träningsgummiband, Massagerulle och Multigym läggas in i `godkanda_typord`?

Webbkällor: [manualslib Ferrum TX 3 (art. 9035)](https://www.manualslib.de/manual/2478/Hammer-Ferrum-Tx-3.html), [discounto Ferrum TX3](https://www.discounto.de/Angebot/HAMMER-Kraftstation-FERRUM-TX3-10201059/), [brack 9038](https://business.brack.ch/en/product/1096686), [morele Zipro](https://www.morele.net/zipro-pilka-gimnastyczna-anti-burst-premium-65-cm-szara-10947211/), [rubbex Continental MTB 29+](https://rubbex.com/en-be/continental-mtb-tube-wide-29-a40-re-65-622-70-622-4019238043839), [bike-components SKS Beavertail](https://bike-components.de/en/SKS/Beavertail-Front-Rear-Mudguard-Set-p22107), [sportano SKS 10100](https://sportano.com/p/51149/sks-beavertail-bicycle-mudguards-black-10100).
