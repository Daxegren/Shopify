# Granskning k_52a (13 utkast, 4 avvisade), Opus, 2026-11-17

Källa: live-läsning 2026-11-17 (`rapporter/shopify-original-2026-11-17/k_52a_kalla_live_granskning.json`) och webbkoll mot tillverkare och återförsäljare. Utlåtandet i JSON-form finns i `vag2_skriv/k_utlatande_52a.json`. Varje ändring (före → efter) är kontrollerad i python: texten som ändras finns exakt en gång i sitt fält. Efter ändringarna är metabeskrivningen (texten under länken i sökresultaten) 91 och 121 tecken på de rättade produkterna. Titlar och SEO-titlar (titeln som visas i sökmotorer) krockar inte med någon titel i butiken (`alla_produkter.json`). Ingen produkt har taggen "På beställning". Ingenting har ändrats i Shopify.

**Resultat:** 9 GODKÄND, 3 RÄTTA, 1 UNDERKÄND. De fyra avvisningarna är rätta.

| nr | Produkt | Dom | Kort skäl |
|---|---|---|---|
| 52002 | Framkorg Basil Robin, 27 l | RÄTTA | Måtten tas bort: källan säger 47 x 31 x 25 cm, Basil 27,5 x 40 x 23,5 cm. Lastgränsen 10 kg får stå: den står i löptext utan etikett i källan, men Basils sida för exakt EAN anger "Max. 10 kg" (v1.10). |
| 52003 | Handtag Giant Tactal Double Lock-On, svart och gul | GODKÄND | "Bilden är illustrativ" motsäger inte titelns färg; färg ur titeln är tillåten (v1.12). |
| 52004 | Inversionsstövlar Tunturi | GODKÄND | Ren fakta, sann, inga hälsopåståenden. Tunturi anger ingen maxvikt, därför "Ej känd". Se beslut nedan. |
| 52006 | Pedaler Look X-Track | GODKÄND | Kort men sann. Kolfiber utelämnat eftersom Look anger komposit. |
| 52007 | Pedaler Giant Pinner Comp, lila | UNDERKÄND | Källtexten beskriver Pinner Elite (R3/R1). Butiken har dessutom en skriven Pinner Elite lila. |
| 52008 | Cykelstöd Azimut Dual | GODKÄND | Hjulstorleken rätt utelämnad (20–29 mot 20–28 tum). Typordet är godkänt i profilen. |
| 52009 | Pedaler Giant Urbano, svart | GODKÄND | Två källfakta, färg ur titeln. |
| 52011 | Golv-/väggankare Axa | GODKÄND | Ren fakta. Säkerhetsnivån rätt utelämnad (20 mot 15). ART 4 är en märkning och får stå en gång "enligt tillverkaren". |
| 52013 | Pedaler Look Trail Fusion, svart | RÄTTA | 100 kg tas bort ur metan så att uppgiften bara står en gång i texten. Svart stöds av EAN, och lime är en egen annons. Frankrike står ordagrant i källan och får stå. |
| 52014 | Handtag Ethic DTC, lila | GODKÄND | "Skoter" rätt utelämnat. Det SKU-nummer som liknar en EAN skrivs som artikelnummer. |
| 52015 | Elastiska band Toorx, set, grön | GODKÄND | Tom källa, men titelns uppgifter räcker enligt v1.12. |
| 52016 | Stänkskydd SKS Veloflexx 55 | RÄTTA | Meningen om sadelstolpen är felöversatt och tas bort. Hjulstorleken utelämnas eftersom källorna går isär. Längdraderna får rätt etikett. Slagtålig plast och Tyskland får stå. |
| 52017 | Handtag Union Honeycomb, svart | GODKÄND | Vikt och längd ur källan, "scooter" utelämnat. |

## Avvisade (k_52a_avvisade.json, 52901–52904 = 52001, 52005, 52010, 52012)
- **52001 Giant Stratus Comp 2.5:** rätt avvisad. Källan har bara märkestext, och titelns "Handtag" är fel: varan är styrtejp (handtagstejp) enligt Giant. Typordet får inte bytas utan stöd i källan (R7), och produkttypen i titeln är fel (v1.12 punkt 5).
- **52005 Star Wars-handskar:** rätt avvisad. Källan är tom och det framgår inte vilken sorts handskar det är. Taggarna (cykelbelysning) stämmer inte. Produkten ingår inte heller i cykeldelsbeslutet.
- **52010 Ass Savers Toetector:** rätt avvisad. Källan beskriver Regular Fender (sadelfäste, 380 mm), inte Toetector (R2/R3).
- **52012 Toorx reflexväst:** avvisningen godtas, men den är försiktig. Enligt v1.12 skulle en kort text med bara titelns uppgifter vara möjlig, som för 52015. Se beslut nedan.

## Viktigaste fynden
1. **52007:** SKU 230000105 och EAN 4713250020495 är Pinner Comp lila (smartech.ee, ebike24). Källtexten säger ändå "Pinner Elite" och har Elite-vikten 380 g. Utkastet tog modellnamnet från titeln och fakta från syskonprodukter, vilket inte är tillåtet (R1).
2. **52016:** Den maskinöversatta källan placerar bakskärmens fäste fel: på sadelstolpen i stället för på sadelstagen. Texten skulle alltså ha varit fel i sak.
3. **52002:** Källans mått stämmer inte med Basils egen sida för samma EAN.
4. **52011:** AXA-sidan som utkastaren hänvisar till har ett annat GTIN (streckkod) än vår produkt (8713249349435 mot 8713249312712). Slutsatsen att utelämna säkerhetsnivån står sig ändå.
5. Inga ursprungs-, kvalitets-, skydds-, hälso- eller stöldpåståenden finns kvar utöver de två som står ordagrant i källan och har "enligt tillverkaren": Look tillverkas i Frankrike, och SKS är tillverkad i Tyskland av slagtålig plast.

## Beslut för David
- **52004 Inversionsstövlar.** Alternativ A (rekommenderas): skriv texten med bara fakta och "Maximal lastgräns: Ej känd". Alternativ B: vänta med produkter som bär hela kroppen upp och ned tills tillverkaren anger en maxvikt. Risk med A: texten ger inga säkerhetsråd. Om inget beslutas gäller A.
- **52007 Pinner Comp lila.** Alternativ A (rekommenderas): skriv ett nytt utkast enbart från webbuppgifter för exakt EAN. Alternativ B: rätta källtexten i butiken först. Om inget beslutas förblir produkten utan text.
- **52012 Reflexväst.** Alternativ A: låt den vara avvisad. Alternativ B: skriv en kort text med titelns uppgifter, utan synlighetslöften, som för 52015. Rekommendation: A, eftersom reflexerna stängdes 2026-11-05 och källan saknar allt utom märket. Om inget beslutas gäller A.
- **52001 Stratus Comp 2.5.** Titeln bör rättas till handtagstejp innan någon text skrivs. Det är en ändring av titeln och kräver Davids ja.

## Webbkällor
- https://www.basil.com/en/p/8715019112188/basil-robin-bicycle-basket-front-black/
- https://www.tunturi.com/en/go/product/97611930
- https://www.smartech.ee/et/products/spordikaubad/sporditarbed/jalg--ja-toukeratta-tarvikud-ja-lisaseadmed/pedalsgiantpinnercomppurple-2438-velm/
- https://www.ebike24.com/giant-pinner-comp-mtb-platform-pedal
- https://www.giant-bicycles.com/us/pinner-elite-flat-pedals-2022
- https://www.ridewill.com/p/en/look-421531491-coppia-pedali-mtb-flat-trail-fusion-nero/1435449
- https://www.lookcycle.com/us-en/products/dh-dirt/trail-fusion
- https://r2-bike.com/LOOK-Pedals-Trail-Fusion-red
- https://axabikesecurity.com/product/axa-floor-anchor/
- https://blog.sks-germany.com/en/?p=17484
- https://www.bike24.com/p2417273.html
- https://hollandbikeshop.com/en-gb/bicycle-parts-city-bike/bicycle-mudguards/bicycle-mudguards/bicycle-mudguard-27-5-inch/sks-veloflexx-55-mudguard-set-26-27-5-55mm-black-914370
