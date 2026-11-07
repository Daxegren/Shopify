# Granskningsutlåtande k_42a–k_42d, Gymstick (2026-11-07)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.10), BESLUTSLOGG till och med 2026-11-07 (Gymstick-produkterna får text enligt vanliga regler, Gymstick-taggen rörs inte), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_39fg.md` och formatet i `k_utlatande_39fg.json`. Tillverkarsidorna på gymstick.com lästes för varje produkt (alla svarade 200; utkastaren av k_42a fick 403 och skrev utan webbkoll).

Alla 25 utkast och alla 73 avvisade är ACTIVE med lager. Inget utkast står på spärrlistan. `skrivfil_kontroll.py` gav 0 fel och 0 varningar på utkasten och på de rättade texterna (24 st, utan den underkända). Standardblocket är exakt rätt på alla. Ingen har taggen På beställning, och ingen har leveranstidsmeningen. Titlar, SEO-titlar och metatexter efter rättning är unika mot varandra, mot alla andra `*utkast*.json`/`*skriv*.json` och mot live-titlarna (sökning i butiken på varje typord). Titlar ≤70 tecken och ≤2 kommatecken, SEO ≤43, meta 70–155 med verb. Varje rättning är ETT sammanhängande före/efter-par per fält, och varje före-text förekommer exakt en gång i utkastet (kontrollerat i python).

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_42.json`.

## Resultat: 2 GODKÄND, 22 RÄTTA, 1 UNDERKÄND

**Stoppar bygget: dubbla nr.** k_42b och k_42c använder samma nr för olika produkter (42202, 42205 och 42208 finns i båda utkastfilerna, och 42201 är också ett avvisat nr i k_42b). `bygg_k_skriv.py` nycklar på `nr`, så en produkt skulle tyst skrivas över (samma fel som i LARDOMAR 2026-11-05). Numrera om k_42c i både utkast och utlåtande (förslag 42401–42408 i samma ordning) eller bygg filerna var för sig. I JSON står utkastens nr och `fil`.

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 42001 | 10581100265738 | k_42a_utkast.json | RÄTTA | meta, html |
| 42002 | 10581100396810 | k_42a_utkast.json | RÄTTA | meta, html |
| 42003 | 10581100658954 | k_42a_utkast.json | RÄTTA | meta, html |
| 42004 | 10581100822794 | k_42a_utkast.json | RÄTTA | titel, seo_title, meta, html |
| 42005 | 10581102035210 | k_42a_utkast.json | RÄTTA | titel, seo_title, meta, html |
| 42006 | 10581101936906 | k_42a_utkast.json | RÄTTA | titel, seo_title, meta, html |
| 42202 | 10581105770762 | k_42b_utkast.json | GODKÄND | – |
| 42205 | 10581106000138 | k_42b_utkast.json | UNDERKÄND | – |
| 42208 | 10581106426122 | k_42b_utkast.json | RÄTTA | html |
| 42216 | 10581107933450 | k_42b_utkast.json | RÄTTA | html |
| 42221 | 10581108457738 | k_42b_utkast.json | GODKÄND | – |
| 42222 | 10581108588810 | k_42b_utkast.json | RÄTTA | titel, seo_title, meta, html |
| 42201 | 10581109735690 | k_42c_utkast.json | RÄTTA | html |
| 42202 | 10581109801226 | k_42c_utkast.json | RÄTTA | html |
| 42203 | 10581110849802 | k_42c_utkast.json | RÄTTA | meta, html |
| 42204 | 10581111341322 | k_42c_utkast.json | RÄTTA | meta, html |
| 42205 | 10581111636234 | k_42c_utkast.json | RÄTTA | html |
| 42206 | 10581111537930 | k_42c_utkast.json | RÄTTA | meta |
| 42207 | 10581112717578 | k_42c_utkast.json | RÄTTA | meta |
| 42208 | 10581111177482 | k_42c_utkast.json | RÄTTA | titel, seo_title, meta, html |
| 42d-01 | 10593399308554 | k_42d_utkast.json | RÄTTA | meta, html |
| 42d-02 | 10581119205642 | k_42d_utkast.json | RÄTTA | titel, seo_title, meta, html |
| 42d-03 | 10581119435018 | k_42d_utkast.json | RÄTTA | meta, html |
| 42d-04 | 10611442450698 | k_42d_utkast.json | RÄTTA | meta, html |
| 42d-05 | 10623405523210 | k_42d_utkast.json | RÄTTA | html |

## Mönster

- Webbkoll saknades i k_42a: gymstick.com gick att läsa, och alla sex utkasten byggs ut med tillverkarens mått, material och vikt (R1 v1.6, R3 tunn källa). Två faktafel rättas där: Ab Crunch Strap är ett tillbehör till kabelmaskin (inte "remmar"), och Curved Bar har en lastgräns (100 kg) som ska stå enligt v1.10.
- "Enligt tillverkaren" stod två gånger för samma lastgräns (i texten och i specifikationsraden) i sex utkast. R5 säger en gång per påstående; specifikationsraden skrivs som på det skrivna syskonet Door Gym Bar ("Maximal användarvikt: 130 kg").
- Typord enligt R7 och syskon: Minimål (som "Nät till Minimål Gymstick Court"), Curlstång (butikens ord för böjda stänger), Isbadkar (produktens egen svenska källa och MAXXUS-syskonet), Massageboll (som "Massageboll Gymstick MyoFascia Ball" och 19 andra live). Slant Board, Sports Tape, Pulley Station, Lifting Grips och Ab Straps behålls (inget svenskt ord i egen källa, profil eller syskon). Träningsboll stämmer med syskonen.
- Cirkulära inledningar (R11) i Ab Straps, Wrist Support 2.0 och Ab Crunch Strap; metatexter utan verb i Pulley Station och Sports Tape.
- R2: motsägande mått på Lifting Grips (50 x 3,8 cm i texten, 40 x 19 x 1,3 cm "for one strap" i tabellen) tas bort, även ur titeln. Figure 8 Straps: mått och vikt gäller en rem och märks så.
- R12a: Exercise Ball 65 cm har samma EAN som redan skrivna 10411728240906 och underkänns. Ab Straps har samma EAN som 10593398948106 ("Ab Straps", DRAFT, ej skriven); den aktiva skrivs (v1.5), men David bör veta att det finns en utkastkopia.

## Avvisade: bedömning

Avvisningarna i k_42a–d är i huvudsak riktiga (spärrlistan, massage, stöd med hälsopåståenden, olika artiklar v1.9, elektronik). 27 av de 73 står på spärrlistan och lyfts inte. Fyra avvisningar är fel eftersom tillverkarsidan ger entydiga fakta för exakt SKU och EAN (v1.6); de **kan lyftas** till ett nytt utkast. En femte står kvar men med annat skäl:

| id | live-titel | avvisad som | underlag på gymstick.com |
|---|---|---|---|
| 10581097054474 | Träningsslang Gymstick Aktiv med Dörrankare (72009) | k_42a, tunn källa | https://www.gymstick.com/active-workout-tube-with-door-anchor.html: slang med mjuka handtag, dörrankare och länk till onlineträning ingår, TPR+PP+skum, blå-svart, 140 x 12,5 x 3 cm, 0,26 kg. Typord Träningsgummiband/träningsslang |
| 10581100888330 | Court Mini Goal Net (53155) | k_42a, källan motsäger titeln | https://www.gymstick.com/court-mini-goal-net.html: reservnät till Court Mini Goal 79 x 53 cm, 5-ply polyester. Tillverkaren löser motsägelsen; titel som c_3 ("Nät till Minimål Gymstick Court"). Kort text, lager 7 |
| 10581104460042 | Alpha J-Cup (SP-PRO-APR-8) | k_42a, generisk källa | https://www.gymstick.com/alpha-j-cup.html: J-formade stånghållare i stål för Alpha Power Rack och Alpha Cage Rack, säljs parvis, 27 x 8 x 20 cm, 3,7 kg, "maximum distributed load on the brackets is 500 kg" (bärande del: en gång enligt tillverkaren, v1.10) |
| 10581105115402 | Cable Pulley System (61241) | k_42a, oklart vad det är | https://www.gymstick.com/cable-pulley-system.html: set med vertikal skivhållare 33 cm (30+ mm skivor), kabel 200 cm/6 mm, trissa med 48 cm fästrem, 3 karbinhakar, tricepsrep 70 cm; material, 2,1 kg. Lastgräns saknas: "Ej känd" (v1.10) |
| 10581104230666 | Justerbart handtag, lätt (61055) | k_42a, tunn källa | Avvisningen står kvar men med annat skäl: https://www.gymstick.com/adjustable-hand-grip.html visar att varianterna L och S har olika motstånd (5–20 och 10–40 kg) och färg; olika artiklar (v1.9). Räknas inte som lyft |

Övriga noteringar om avvisade: Fascia Roller, Massage Hook och Vivid Massage Stick (manuella) står på spärrlistan trots att typordet massagerulle godkändes 2026-11-07 och ett tjugotal massagebollar redan är skrivna; det är Davids beslut om spärren ska hävas för manuella massageredskap. Fitness Trampoline (lyft till David av utkastaren) ligger utanför v1.10.

## Frågor till David

1. Numreringen i k_42b/k_42c måste rättas före bygget (se ovan).
2. Horisontell stång med remskiva (PRO-550M-HPB): SKU stämmer exakt med tillverkarsidan men EAN skiljer sig (6430016901963 på sidan, 6430016904520 i butiken). Godkänn att texten skrivs på SKU-matchen, annars underkänn.
3. Latsdragstänger: k_42 skriver "Maximal lastgräns: Ej känd" på båda (stången hänger i kabeln). De tidigare skrivna (k_11e) har ingen sådan rad. En regel bör gälla.
4. RecoPod isbadkar: skrivs med bara produktfakta (kar, mått, innehåll). Kallbad är hälsonära; säg till om produkten hellre ska vänta.
5. Spärren för manuella massageredskap (se ovan) och om de fyra lyfta avvisningarna ska få utkast i nästa omgång.

## Skäl och rättningar per produkt

### 42001 (10581100265738, k_42a_utkast.json): RÄTTA

Live ACTIVE, en variant 53140, EAN 6430016902601, lager 53. Egen källa är marknadsföring. Utkastaren skrev att gymstick.com gav 403, men sidan https://www.gymstick.com/court-floorball-goal.html går att läsa (SKU 53140 och EAN 6430016902601 stämmer): standard sized, 160 x 115 x 58 cm, ramprofil 25 x 0.7 mm, stålram, nät av 3-ply polyester, 4,7 kg, inside and outside. Rättning (R1/v1.6, R3 tunn källa): texten byggs ut med tillverkarens mått, material och vikt; meta utan utfyllnaden "Artikelnummer 53140". Utelämnat: durable, weather-proof, "3-ply" (osäker översättning).

| fält | före | efter |
|---|---|---|
| meta | Innebandymålet Gymstick Court Floorball Goal används vid träning och spel, både inomhus och utomhus. Artikelnummer 53140. | Innebandymålet Gymstick Court Floorball Goal mäter 160 x 115 x 58 cm och har stålram och nät av polyester. Det används inomhus och utomhus. |
| html | sammanhängande bit, 404 tecken (se JSON) | sammanhängande bit, 634 tecken (se JSON) |

### 42002 (10581100396810, k_42a_utkast.json): RÄTTA

Live ACTIVE, en variant 53120, EAN 6430016902564, lager 128. Tillverkarens sida https://www.gymstick.com/court-football-goal.html går att läsa (SKU och EAN stämmer): 300 x 200 x 104 cm, vit stålram, ramprofil 38 x 0.8 mm, nät av polyester, U-formade markspett ingår, 14 kg. Rättning (R1/v1.6, R3): texten byggs ut med tillverkarens fakta. Utelämnat: sturdy, durable, weather-proof, ply-antal. Inga stabilitets- eller säkerhetsord.

| fält | före | efter |
|---|---|---|
| meta | Fotbollsmålet Gymstick Court Football Goal används vid träning och lek på gården eller i parken och går att montera och ta isär. | Fotbollsmålet Gymstick Court Football Goal mäter 300 x 200 x 104 cm och har vit stålram och nät av polyester. Markspett ingår. |
| html | sammanhängande bit, 486 tecken (se JSON) | sammanhängande bit, 754 tecken (se JSON) |

### 42003 (10581100658954, k_42a_utkast.json): RÄTTA

Live ACTIVE, en variant 53130, EAN 6430016902588, lager 291. Tillverkarens sida https://www.gymstick.com/court-icehockey-goal.html går att läsa (SKU och EAN stämmer): standard sized, 183 x 122 x 76 cm, ramprofil 38 x 0.8 mm, stålram, nät av polyester, 9,3 kg. Rättning (R1/v1.6, R3): texten byggs ut med tillverkarens fakta; meta utan "Artikelnummer 53130". Utelämnat: durable, weatherproof, long-lasting.

| fält | före | efter |
|---|---|---|
| meta | Ishockeymålet Gymstick Court Icehockey Goal används vid träning och lek, på is eller på annan plan yta. Artikelnummer 53130. | Ishockeymålet Gymstick Court Icehockey Goal mäter 183 x 122 x 76 cm och har stålram och nät av polyester. Det används på is eller annan plan yta. |
| html | sammanhängande bit, 411 tecken (se JSON) | sammanhängande bit, 619 tecken (se JSON) |

### 42004 (10581100822794, k_42a_utkast.json): RÄTTA

Live ACTIVE, en variant 53150, EAN 6430016902618, lager 158. Tillverkarens sida https://www.gymstick.com/court-mini-goal.html (SKU och EAN stämmer): "mini goal", 79 x 53 x 31 cm, ramprofil 25 x 0.7 mm, stålram, nät av polyester, 2 kg. Rättning R7: typordet "Mini Goal" byts mot "Minimål", som redan används i butiken för nätet till samma mål (c_3: "Nät till Minimål Gymstick Court") och är den entydiga översättningen; egen källa säger "kompakt mål". Rättning R1/R3: tillverkarens fakta läggs till.

| fält | före | efter |
|---|---|---|
| titel | Mini Goal Gymstick Court | Minimål Gymstick Court Mini Goal |
| seo_title | Mini Goal Gymstick Court | Minimål Gymstick Court Mini Goal |
| meta | Mini Goal Gymstick Court används vid träning och lek, inomhus och utomhus. Det kompakta målet går att sätta upp och ta ner. Artikelnummer 53150. | Minimålet Gymstick Court Mini Goal mäter 79 x 53 x 31 cm och har stålram och nät av polyester. Det används inomhus och utomhus. |
| html | sammanhängande bit, 460 tecken (se JSON) | sammanhängande bit, 643 tecken (se JSON) |

### 42005 (10581102035210, k_42a_utkast.json): RÄTTA

Live ACTIVE, en variant 61239, EAN 6430016901031, lager 33. Tillverkarens sida https://www.gymstick.com/ab-crunch-strap.html (SKU och EAN stämmer): används "with a cable machine", handtag, D-ring, "maximum load of 80 kg", svart, 40 x 48 x 4 cm, 0,3 kg, enhet PCS. Rättning (R1/R3/R11): utkastets "remmar" (plural) och den cirkulära inledningen "Ab Crunch Strap … är remmar" ersätts; produkten är ett tillbehör till kabelmaskin. Hängande del: 80 kg skrivs en gång enligt tillverkaren (v1.10). Material utelämnat (R2: beskrivningen säger bomullsväv, tabellen polyester och PP). Utelämnat: strong, sturdy, heavy-duty, great grip.

| fält | före | efter |
|---|---|---|
| titel | Ab Crunch Strap Gymstick | Ab Crunch Strap Gymstick för Kabelmaskin |
| seo_title | Ab Crunch Strap Gymstick | Ab Crunch Strap Gymstick för Kabelmaskin |
| meta | Ab Crunch Strap från Gymstick är remmar för crunch-övningar för magmusklerna, hemma eller på träningscentret. Artikelnummer 61239. | Gymstick Ab Crunch Strap används med en kabelmaskin vid crunch-övningar för magmusklerna. Den har handtag och en D-ring och är svart. |
| html | sammanhängande bit, 471 tecken (se JSON) | sammanhängande bit, 611 tecken (se JSON) |

### 42006 (10581101936906, k_42a_utkast.json): RÄTTA

Live ACTIVE, en variant 7/CB-7, EAN 6430062510461, lager 63. Tillverkarens sida https://www.gymstick.com/7kg-curved-bar.html (SKU CB-7 och EAN stämmer): förkromad stålstång 7 kg, "takes standard 31 mm weight discs", ett par fjäderlås ingår, "Bar weight capacity: 100kg", längd 120 cm, diameter 30 mm, greppdel 83 cm. Rättning R7: typordet blir Curlstång, butikens ord för böjda stänger (Movit-curlstänger i k_11b). Rättning v1.10: stången är bärande; 100 kg skrivs en gång enligt tillverkaren (utkastet hade ingen lastgräns). Utelämnat: ergonomisk greppvinkel, minskar belastningen på handleder, hållbar.

| fält | före | efter |
|---|---|---|
| titel | Curved Bar Gymstick, 7 kg | Curlstång Gymstick Curved Bar, 7 kg |
| seo_title | Curved Bar Gymstick, 7 kg | Curlstång Gymstick Curved Bar, 7 kg |
| meta | Curved Bar från Gymstick väger 7 kg och har en böjd design. Stången används vid bicepscurls, hammercurls och pressövningar. | Curlstången Gymstick Curved Bar är förkromad, väger 7 kg och är 120 cm lång. Den används vid curls och pressövningar, och ett par fjäderlås ingår. |
| html | sammanhängande bit, 526 tecken (se JSON) | sammanhängande bit, 770 tecken (se JSON) |

### 42202 (10581105770762, k_42b_utkast.json): GODKÄND

Live ACTIVE, 61103, EAN 6430016903745, lager 1. Tillverkarens sida https://www.gymstick.com/door-anchor-for-pro-exercise-band.html (SKU och EAN stämmer): fäster träningsband eller tube trainer i dörr, mjuka material som inte lämnar märken, PP 52 %, PVC 48 %, svart-röd, 27 x 6 x 5 cm, 0,05 kg. Tillverkarpåståendet om märken står en gång med "enligt tillverkaren". Lastgräns saknas: "Ej känd" (v1.10). Allt stämmer.

### 42205 (10581106000138, k_42b_utkast.json): UNDERKÄND

Dubblett (R12a, beslut 2026-11-05): samma artikel som den redan skrivna och aktiva produkten 10411728240906 "Träningsboll Gymstick, 65 cm, Svart" (SKU GYM62010, samma EAN 6430016901505, texter-klara). Delad streckkod = exakt samma artikel. Ska inte få en andra text. (Om den ändå skrivs: SEO-titeln utan storlek gick inte att skilja från 55 och 75 cm, "Träningsboll Gymstick, 65 cm" är redan upptagen, och lastgränsen ska heta "Maximal användarvikt" med "enligt tillverkaren" en gång; tillverkarsidan https://www.gymstick.com/exercise-ball.html anger "Max user weight (kg) 100" för EAN 6430016901505.)

### 42208 (10581106426122, k_42b_utkast.json): RÄTTA

Live ACTIVE, 61011, EAN 6430016900942, lager 322. Tillverkarens sida https://www.gymstick.com/figure-8-straps.html (SKU och EAN stämmer): "Measurement and weight of the product for one piece", enhet PR. Rättning R2: måtten och vikten gäller en rem; raderna märks så i stället för att tas bort. Övrigt stämmer (marklyft, rodd, vadderad åttaform, polyesterbomull 80 %, SBR 20 %, svart-röd). Typordet Lyftremmar som skrivna syskon (Lyftremmar Gymstick med Vaddering, i Läder).

| fält | före | efter |
|---|---|---|
| html | Mått: 26 x 14 x 4 cm</li>\n<li>Vikt: 0,085 kg | Mått (en rem): 26 x 14 x 4 cm</li>\n<li>Vikt (en rem): 0,085 kg |

### 42216 (10581107933450, k_42b_utkast.json): RÄTTA

Live ACTIVE, HPB/PRO-550M-HPB, EAN 6430016904520, 27 999 kr, lager 17. Tillverkarens sida https://www.gymstick.com/horizontal-bar-with-pulley-for-5-station.html: SKU PRO-550M-HPB stämmer exakt men EAN på sidan är 6430016901963 (avviker, flaggat av utkastaren). Fakta i texten stämmer med sidan (tillägg till 4-Station Multi Gym, andra höjdjusterbar kabelremskiva, multi-grip-handtag, viktstapel 86 kg, ramrör 50 x 100 x 2,5 mm, 230 x 95 x 220 cm, 215 kg, material, manual och delar). Vikt och viktstapel är rimliga för ett kabeltorn: 5-stationsmaskinen kostar 149 989 kr och 4-stationsmaskinen 112 489 kr i butiken. Lastgräns saknas: "Ej känd" enligt v1.10 är rätt. Rättning: sidan säger att garantin gäller vid professionellt bruk "used and assembled according to the manual"; "enligt manualen" i utkastet läses som källangivelse och stryks. Till David: EAN-avvikelsen bör bekräftas före skrivning.

| fält | före | efter |
|---|---|---|
| html | Tillverkarens garanti: 1 år vid professionellt bruk, enligt manualen | Tillverkarens garanti: 1 år vid professionellt bruk |

### 42221 (10581108457738, k_42b_utkast.json): GODKÄND

Live ACTIVE, 61157, EAN 6430062510256, lager 28. Tillverkarens sida https://www.gymstick.com/lateral-pull-down-bar-with-handles.html (SKU och EAN stämmer): förkromad stålstång med handtag och gummigrepp, stål 98 %, termoplastgummi 2 %, krom-svart, 96,5 x 16,3 x 22,5 cm, 5,9 kg. "Maximal lastgräns: Ej känd" enligt v1.10. Typordet Latsdragstång som skrivna syskon. Unik mot "Latsdragstång Gymstick med Handtag, 100 cm" genom 96,5 cm.

### 42222 (10581108588810, k_42b_utkast.json): RÄTTA

Live ACTIVE, 61150, EAN 6430062510188, lager 593. Tillverkarens sida https://www.gymstick.com/lifting-grips.html (61150, EAN stämmer): parvis, justerbar kardborrerem, pull-ups/rodd/styrkelyft, gummi 70 %, SBR 25 %, järn 5 %, svart. Rättning R2: måtten motsäger varandra på sidan ("Size: 50cm (L) x 3,8cm (W)" i texten men "Product (cm) 40 x 19 x 1,3", "Dimensions and weight for one strap" i tabellen); längd och bredd tas bort ur titel, SEO, meta och text. Typordet Lifting Grips behålls (live-titelns ord, inget svenskt ord i källan; Lyftremmar används för andra produkter).

| fält | före | efter |
|---|---|---|
| titel | Lifting Grips Gymstick, 50 cm, Svart | Lifting Grips Gymstick, Svart |
| seo_title | Lifting Grips Gymstick, 50 cm | Lifting Grips Gymstick |
| meta | Lifting Grips från Gymstick säljs parvis och har justerbar kardborrerem. Remmen är 50 cm lång och 3,8 cm bred. | Lifting Grips från Gymstick säljs parvis och har justerbar kardborrerem. De är gjorda av gummi, SBR och järn och är svarta. |
| html | sammanhängande bit, 521 tecken (se JSON) | sammanhängande bit, 441 tecken (se JSON) |

### 42201 (10581109735690, k_42c_utkast.json): RÄTTA

Live ACTIVE, 61006, EAN 6430062514391, lager 18. Tillverkarens sida https://www.gymstick.com/premium-chin-up-bar.html (SKU och EAN stämmer): väggmonterad, triangulära väggfästen, uppruggade greppytor, stål, svart-krom, "Max user weight (kg) 180", stångdiameter 29 mm, 128,5 x 50 x 71,2 cm, 12,5 kg. Maximal användarvikt enligt tillverkaren är ok (v1.10, entydig och exakt artikel). Rättning R5: "enligt tillverkaren" stod två gånger för samma påstående (text och specifikation); specifikationsraden skrivs som på syskonet Door Gym Bar. Typordet Chinsstång som Door Gym Bar.

| fält | före | efter |
|---|---|---|
| html | Maximal användarvikt: 180 kg enligt tillverkaren | Maximal användarvikt: 180 kg |

### 42202 (10581109801226, k_42c_utkast.json): RÄTTA

Live ACTIVE, 61118, EAN 6430016905916, lager 617. Tillverkarens sida https://www.gymstick.com/pro-chinning-bar.html (SKU och EAN stämmer): flera greppositioner, vägg eller tak, stål och PVC, svart, "Max user weight (kg) 130", största hålavstånd 65 cm, stångdiameter 25 mm, 98 x 33 x 22 cm, 3,2 kg, monteringsanvisning och delar. Rättning R5: "enligt tillverkaren" en gång per påstående (stryks i specifikationsraden).

| fält | före | efter |
|---|---|---|
| html | Maximal användarvikt: 130 kg enligt tillverkaren | Maximal användarvikt: 130 kg |

### 42203 (10581110849802, k_42c_utkast.json): RÄTTA

Live ACTIVE, PS/STR-SHR-PS, EAN 6430016904681, lager 61. Tillverkarens sida https://www.gymstick.com/pulley-station-for-smith-half-rack.html (SKU och EAN stämmer): fakta i utkastet stämmer (viktskivebelastat trissystem på rackets baksida, hög och låg trissa, 50 mm viktskivor, vadderat lårstöd, ankelrem, V-handtag, latstång och rak stång, stål, svart, 104 x 106 x 219 cm, 33,5 kg). Lastgräns saknas: "Ej känd" (v1.10) rätt. Rättning R11: metans första mening saknade verb. Rättning stavning: "racket baksida" ska vara "rackets baksida" och "trissstation" skrivs "trisstation" (tre lika konsonanter blir två, jfr "trissystem" i samma text). Typordet Pulley Station behålls (live-titelns ord, inget godkänt svenskt typord).

| fält | före | efter |
|---|---|---|
| meta | Tillbehör till Gymstick Smith Half Rack med hög och låg trissa. Ankelrem, V-handtag, latstång och rak stång ingår. | Pulley Station från Gymstick monteras på Smith Half Rack och har hög och låg trissa. Ankelrem, V-handtag, latstång och rak stång ingår. |
| html | sammanhängande bit, 431 tecken (se JSON) | sammanhängande bit, 431 tecken (se JSON) |

### 42204 (10581111341322, k_42c_utkast.json): RÄTTA

Live ACTIVE, 61236, EAN 6430016900867, lager 568. Tillverkarens sida https://www.gymstick.com/slant-board.html (SKU och EAN stämmer): "flat or slanted at 4 different angles", "Adjustable angle with 5 positions", 28 x 31,5 cm, höjd 8,5–22,5 cm, PP, grå, "Max user weight (kg) 100", 1,22 kg. Rättning: "plant eller i fem lägen" var fel (fem lägen inklusive det plana); rättat i meta och text. Rättning R5: "enligt tillverkaren" en gång per påstående i texten. Typordet Slant Board behålls (inget svenskt ord i källan eller profilen; ev. nytt typord är en fråga till David). Halkskydd och hälsoord korrekt utelämnade.

| fält | före | efter |
|---|---|---|
| meta | Slant Board från Gymstick kan användas plant eller i fem lägen, med höjd 8,5–22,5 cm. Maximal användarvikt är 100 kg enligt tillverkaren. | Slant Board från Gymstick kan ställas i fem lägen, plant eller i fyra vinklar, med höjd 8,5–22,5 cm. Maximal användarvikt är 100 kg enligt tillverkaren. |
| html | sammanhängande bit, 673 tecken (se JSON) | sammanhängande bit, 669 tecken (se JSON) |

### 42205 (10581111636234, k_42c_utkast.json): RÄTTA

Live ACTIVE, 61064, EAN 6430062513974, lager 255. Tillverkarens sida https://www.gymstick.com/step-board.html (SKU och EAN stämmer): två höjder 10/15 cm, hemmabruk, kompakt, 68 x 28 cm, PP, svart-röd, "Max user weight (kg) 100", 2,8 kg, träningsguide och länk till video. Typordet Stepbräda finns i profilen. Rättning R5: "enligt tillverkaren" en gång per påstående i texten.

| fält | före | efter |
|---|---|---|
| html | Maximal användarvikt: 100 kg enligt tillverkaren | Maximal användarvikt: 100 kg |

### 42206 (10581111537930, k_42c_utkast.json): RÄTTA

Live ACTIVE, 63040, EAN 6430062510720, lager 724. Tillverkarens sida https://www.gymstick.com/sports-tape-2pcs.html (SKU och EAN stämmer): set om 2 st, 100 % bomull, bredd 38 mm, längd 10 m, vit. Text och specifikation godkända. Rättning R11/meta: metans första mening ("Set med 2 st tejp av bomull från Gymstick.") saknade verb. "Medical grade", hudpåstående och stöd/skadeord korrekt utelämnade. Typordet Sports Tape behålls (live-titelns ord; butiken har inget godkänt svenskt typord som "sporttejp").

| fält | före | efter |
|---|---|---|
| meta | Set med 2 st tejp av bomull från Gymstick. Tejpen är 38 mm bred och 10 m lång, och färgen är vit. | Setet Sports Tape från Gymstick innehåller 2 st tejp av bomull. Tejpen är vit, 38 mm bred och 10 m lång. |

### 42207 (10581112717578, k_42c_utkast.json): RÄTTA

Live ACTIVE, två varianter 105 (61086-105, 209 kr, EAN 6430016904759, lager 30) och 115 (61086-115, 219 kr, EAN 6430016904773, lager 21): samma artikel i två storlekar med lager (v1.9); titel och SEO låser inte storlek. Tillverkarens sida https://www.gymstick.com/weightlifting-belt-shaped.html (SKU 61086, EAN för 105 cm stämmer; sidan anger båda storlekarna): formad, extra vadderat ryggstöd, dubbla dornar, dubbla hällor, läder och PU, svart. Stöd-, hållnings- och skadepåståenden korrekt utelämnade. Rättning språk i meta: "i storlek 105 och 115 cm" ska vara "i storlekarna 105 och 115 cm".

| fält | före | efter |
|---|---|---|
| meta | Lyftarbältet Gymstick Weightlifting Belt Shaped har extra vadderat ryggstöd och spänne med dubbla dornar. Det finns i storlek 105 och 115 cm. | Lyftarbältet Gymstick Weightlifting Belt Shaped har extra vadderat ryggstöd och spänne med dubbla dornar. Det finns i storlekarna 105 och 115 cm. |

### 42208 (10581111177482, k_42c_utkast.json): RÄTTA

Live ACTIVE, 63085, EAN 6430016909754, lager 358. Tillverkarens sida https://www.gymstick.com/recopod-ice-bath.html (SKU och EAN stämmer): cold pool för hemmabruk, PVC, isolerande termolock, handpump, avloppsslang och tätningar, 75 cm x Ø 85 cm, 420 l, innehållslista, PVC/nylon/kantsnöre, svart och vit, 3 kg. Rättning R7: produktens egen svenska källtext kallar den "isbadkar" ("Denna innovativa isbadkar"), och tidigare utkast c_14 använde Isbadkar; "Ice Bath"/"kallbadpool" byts därför mot Isbadkar i titel, SEO, meta och text. Hälsonära bedömning: produkten är ett uppblåsbart kar, inte en hälsoprodukt i profilens mening; alla återhämtnings-, inflammations- och välmåendelöften är borta och inga nya tillkommer. Skrivs med bara produktfakta; tas upp som upplysning till David. Märke-raden läggs till som på övriga Gymstick-texter.

| fält | före | efter |
|---|---|---|
| titel | Ice Bath RecoPod Gymstick, 420 l, Svart och Vit | Isbadkar Gymstick RecoPod Ice Bath, 420 l, Svart och Vit |
| seo_title | Ice Bath RecoPod Gymstick, 420 l | Isbadkar Gymstick RecoPod, 420 l |
| meta | Kallbadpool för hemmabruk på 420 l från Gymstick med termolock. Handpump och avloppsventil ingår. | Isbadkaret Gymstick RecoPod Ice Bath rymmer 420 l och är avsett för hemmabruk. Det har isolerande termolock, och handpump och avloppsventil ingår. |
| html | sammanhängande bit, 686 tecken (se JSON) | sammanhängande bit, 722 tecken (se JSON) |

### 42d-01 (10593399308554, k_42d_utkast.json): RÄTTA

Live ACTIVE, 61105, EAN 6430016905688, lager 89. Tillverkarens sida https://www.gymstick.com/ab-straps.html (SKU och EAN stämmer): fästs i dragstång eller annat fast ställ "suitable for supporting body weight", polyester och stål, svart, "Max user weight (kg) 100", 65 x 19 x 6,5 cm "on one belt", enhet PR. Hängande del: 100 kg enligt tillverkaren är ok (v1.10). Rättning R11: inledning och meta var cirkulära ("Ab Straps är band/magband"). Rättning R5: "enligt tillverkaren" en gång per påstående. Meta utan "som tål kroppsvikt" (kan läsas som ett löfte om användarens ställ). Utelämnat: ryggskonande och resultatpåståenden.

| fält | före | efter |
|---|---|---|
| meta | Gymstick Ab Straps är hängande magband av polyester och stål. De fästs i en dragstång eller ett fast ställ som tål kroppsvikt. | De hängande magbanden Gymstick Ab Straps är gjorda av polyester och stål och hängs upp i en dragstång eller ett annat fast ställ. |
| html | sammanhängande bit, 699 tecken (se JSON) | sammanhängande bit, 661 tecken (se JSON) |

### 42d-02 (10581119205642, k_42d_utkast.json): RÄTTA

Live ACTIVE, 61347, EAN 6430062515510, lager 358. Inte på spärrlistan; manuell massageboll (inte värme/vibration), och typordet massagerulle godkändes 2026-11-07. Tillverkarens sida https://www.gymstick.com/vivid-myo-ball.html (SKU och EAN stämmer): myofascia ball, diameter 6 cm, 0,15 kg, gummi 65 %, fyllmedel 25 %, mineralolja 10 %, turkos, övningsblad och länk till video. Rättning R7: syskonet "Massageboll Gymstick MyoFascia Ball, Röd" är skrivet med typordet Massageboll; samma ord används här i stället för "Myo Ball"/"myofascia-boll" (inget svenskt ord). Rättning R11: "Tillverkaren kallar den …" är en arbetsformulering. Utelämnat: muskelhinnor, triggerpunkter, ömhet, rehabilitering. Till David: Active Spikey Massage Combo och Vivid Massage Stick står kvar på spärrlistan som massage; om även massagebollar ska vänta, underkänn denna.

| fält | före | efter |
|---|---|---|
| titel | Myo Ball Gymstick Vivid, 6 cm, Turkos | Massageboll Gymstick Vivid Myo Ball, 6 cm, Turkos |
| seo_title | Myo Ball Gymstick Vivid 6 cm | Massageboll Gymstick Vivid Myo Ball |
| meta | Myofascia-bollen Gymstick Vivid Myo Ball är av gummi och har diametern 6 cm. Bollen är turkos och väger 0,15 kg. | Massagebollen Gymstick Vivid Myo Ball är gjord av gummi och har diametern 6 cm. Den är turkos och väger 0,15 kg. |
| html | sammanhängande bit, 530 tecken (se JSON) | sammanhängande bit, 589 tecken (se JSON) |

### 42d-03 (10581119435018, k_42d_utkast.json): RÄTTA

Live ACTIVE, 61339, EAN 6430062515435, lager 608. Tillverkarens sida https://www.gymstick.com/vivid-tube-trainer.html (SKU och EAN stämmer): gummiband med handtag, dörrankare ingår, vadderade handtag, medium resistance, bandlängd 140 cm, PP och TPR, turkos-grå, 0,135 kg. Typordet Träningsgummiband är godkänt 2026-11-07. Rättning språk: "ankare" är ett ett-ord ("ett dörrankare"), i meta och text.

| fält | före | efter |
|---|---|---|
| meta | Träningsgummibandet Gymstick Vivid Tube Trainer har handtag, är 140 cm långt och har medelstort motstånd. En dörrankare medföljer. | Träningsgummibandet Gymstick Vivid Tube Trainer har handtag, är 140 cm långt och har medelstort motstånd. Ett dörrankare medföljer. |
| html | Gymstick Vivid Tube Trainer har vadderade handtag och ett gummiband på 140 cm med medelstort motstånd. En dörrankare medföljer, så att bandet kan fästas i en dörr. | Gymstick Vivid Tube Trainer har vadderade handtag och ett gummiband på 140 cm med medelstort motstånd. Ett dörrankare medföljer, så att bandet kan fästas i en dörr. |

### 42d-04 (10611442450698, k_42d_utkast.json): RÄTTA

Live ACTIVE, 63068, EAN 6430062510898, lager 50. Inte på spärrlistan; syskonet Wrist Support 1.0 är skrivet med typordet Handledsstöd. Tillverkarens sida https://www.gymstick.com/wrist-support-2-0.html (SKU och EAN stämmer): 3 mm neopren, justerbar åtdragning, tumhål, kardborrstängning, polyester 15 %, neopren 45 %, nylon 34 %, spandex 6 %, svart, längd 36 cm, 0,03 kg. Bredden korrekt utelämnad (11,5 mot 11,3 cm). Läknings- och smärtpåståenden korrekt utelämnade. Rättning R11: inledning och meta var cirkulära ("Wrist Support 2.0 är ett handledsstöd").

| fält | före | efter |
|---|---|---|
| meta | Gymstick Wrist Support 2.0 är ett handledsstöd i 3 mm neopren med tumhål och kardborrstängning. Åtdragningen kan justeras. | Handledsstödet Gymstick Wrist Support 2.0 är gjort av 3 mm neopren och har tumhål och kardborrstängning. Åtdragningen kan justeras. |
| html | Gymstick Wrist Support 2.0 är ett handledsstöd i 3 mm neopren. Det har tumhål och kardborrstängning, och åtdragningen kan justeras. | Handledsstödet Gymstick Wrist Support 2.0 är gjort av 3 mm neopren och har tumhål och kardborrstängning. Åtdragningen kan justeras. |

### 42d-05 (10623405523210, k_42d_utkast.json): RÄTTA

Live ACTIVE, 61156, EAN 6430062510249, lager 32. Tillverkarens sida https://www.gymstick.com/lateral-pull-down-bar.html (SKU och EAN stämmer): förkromad stålstång med gummigrepp, stål 95 %, termoplastgummi 5 %, krom-svart, 93 x 18 x 4,5 cm, 4,2 kg; ingen lastgräns. Rättning v1.10: syskonet i samma omgång (k_42b, Latsdragstång med handtag 61157) har "Maximal lastgräns: Ej känd" och samma sak gäller här (stången hänger i kabeln och bär viktstapeln); en regel för båda. Till David: de tidigare skrivna latsdragstängerna (k_11e) har ingen lastgränsrad. Typordet Latsdragstång som syskonen.

| fält | före | efter |
|---|---|---|
| html | sammanhängande bit, 512 tecken (se JSON) | sammanhängande bit, 581 tecken (se JSON) |

