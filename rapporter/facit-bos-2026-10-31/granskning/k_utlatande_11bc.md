# Granskningsutlåtande k_11b och k_11c (gymtillbehör)

Granskare: Opus. Endast läsning, inga ändringar i Shopify. Datum 2026-11-04. 50 produkter (48 utkast och 2 avvisade) hämtades live via Admin API, med varianter och priser via GraphQL. Underlag: regelbok v1.6, beslutslogg, butiksprofil, produkttexter-standard §14–17 och LARDOMAR. Maskinläsbart utlåtande: `vag2_skriv/k_utlatande_11bc.json`. Varje post har fälten nr, id och fil, eftersom nr-serien kan krocka med andra batcher. Flera ändringar i samma fält står som lista.

## Sammanfattning

- 48 utkast gav **33 GODKÄND, 13 RÄTTA och 2 UNDERKÄND** (9841 och 9854). Rättningarna lades in i kopior av utkasten och kördes genom `skrivfil_kontroll.py`. Resultat: 0 fel och 0 varningar i båda filerna (22 + 24 produkter). Varje före-text förekommer exakt en gång i sitt fält, vilket kontrollerades med skript.
- **Cirkulära inledningar (R11), som skriptet missar:** åtta texter hade mönstret "namn är en typ", till exempel "Deadlift Wedge är en marklyftskil", "Push Up Board är en armhävningsbräda" och "Slide pads är ett par floor sliders". Det gäller 9829, 9833, 9838, 9848 (meta och html), 9859, 9861 (meta och html) och 9866 (meta). Alla meta har verb.
- **"Finns i" antyder ett val som inte finns:** 9856 (sex färger, men varianterna är bara vikter), 9868 och 9874 (en färgkombination). Texterna rättas.
- **"Enligt tillverkaren":** står högst två gånger i varje text och aldrig två gånger för samma påstående. Hälso- och effektord är strukna överallt där de saknar ordagrant stöd, även på svettdräkten 9867.
- **Typord:** "Landmine Fäste" rättas till "Landmine-fäste" i titel och SEO-titel (9847, R7 v1.5). Källan skriver det med bindestreck, och R7 går före format_regler. Lyftarbälte (9870, 9871), Armhävningshandtag (9862) och Svängstav (9868) stöds av produkternas egna källtexter. Bältena behåller därför olika typord: Träningsbälte på 9869, 9872 och 9873 och Lyftarbälte på 9870 och 9871. Det följer R7, eftersom varje produkt har sitt eget live-ord.

## Produkter som bär last eller som kroppen hänger i

Jag har tillämpat följande princip, som David behöver bekräfta (se beslut 1):

1. **Kroppen hänger i produkten:** produkten skrivs bara om källan har en svensk etiketterad lastgräns med enhet som entydigt gäller produkten. 9833 Gravity Boots (250 kg), 9858 pull up bar på ribbstol (100 kg, samma värde i löptext och rad), 9853 gymringar (200 kg) och 9848 Lifting Hooks (100 kg, 2 x 50 kg) skrivs. Gränsen står en gång med "enligt tillverkaren", och texten ger inga råd om användning eller säkerhet. **9854 Pegboard underkänns.** Det är en väggmonterad bräda som hela kroppen hänger i. Källan anger ingen lastgräns och inget om montering, bara "fyra skruv".
2. **Lastgräns för produkter som säljs i par eller flera delar:** värdet får stå om det anger vad det gäller ("vardera" på 9832 och 9859, "per grepp" på 9860, "2 x 50 kg" på 9848). Det får också stå om delarna används tillsammans och kroppsvikten fördelas mellan dem, som på 9853 gymringar, 9862 armhävningshandtag och armhävningsstängerna i 9849. På **9855 Power Hooks stryks gränsen på 80 kg.** Varje krok bär en egen hantel, och källan säger inte om värdet gäller per krok eller per par. Läses det fel blir den tillåtna lasten per krok dubbelt så hög (R4: oklart, alltså utelämna).
3. **Bärande tillbehör utan lastgräns** (9846 karbinhakar, 9852 nacktränare) skrivs. Texten anger och antyder ingen bärförmåga (§16.3).
4. **Bärande reservdelar till maskiner som vi inte säljer underkänns.** Det gäller 9841 hjulsats och de redan avvisade 9844 och 9845. Källan länkar bara till Gorilla Sports egna maskiner, till exempel kabelhiss-for-latsdrag-och-rodd, och de finns inte i BEST OF SPORTS. Jag sökte på handle och fick inga träffar. Passformen kan alltså inte styrkas. Utkastarens avvisning av 9844 och 9845 godtas. Skälet "utan angiven maskinmodell" stämmer dock inte helt: källan namnger "Latsdrag Kabelstation" som länk, men den maskinen saknas i vår butik.

## Rättningar (före → efter)

| Fil | Nr | Fält | Före | Efter |
|---|---|---|---|---|
| k_11b | 9829 | html | `Deadlift Wedge är en marklyftskil i silikon som levereras i par.` | `Marklyftskilen Deadlift Wedge är gjord av silikon och levereras i par.` |
| k_11b | 9833 | html | `Gravity Boots Six Pack är en magtränare som sätts runt …` | `Magtränaren Gravity Boots Six Pack sätts runt …` |
| k_11b | 9838 | html | `Handledsvikten är en viktmanchett som kan användas som handledsvikt, …` | `Viktmanchetten kan användas som handledsvikt, …` |
| k_11b | 9842 | html | `Indian Clubbells tillhör en kategori av träningsredskap som är formade … Den här är av massivt` | `Indian Clubbell är formad … Den är av massivt` |
| k_11b | 9847 | titel, seo_title | `Landmine Fäste` | `Landmine-fäste` |
| k_11b | 9848 | meta / html | `Lifting Hooks är två svarta stålkrokar` / `…Grip Hooks, är svarta stålkrokar` | `Lifting Hooks består av två svarta stålkrokar` / `…Grip Hooks, består av svarta stålkrokar` |
| k_11c | 9855 | html | `<li>Maximal belastning: 80 kg (enligt tillverkaren)</li>` | (stryks) |
| k_11c | 9856 | meta, html | `finns i sex vikter från 5 till 30 kg och i sex färger.` och raden `Färger: Svart, grön, …` | `finns i sex vikter från 5 till 30 kg.` (raden stryks) |
| k_11c | 9859 | html | `Push Up Bars är handtag för armhävningar, gjorda av stål …` | `Handtagen Push Up Bars för armhävningar är gjorda av stål …` |
| k_11c | 9861 | meta | `Push Up Board 9in1 är en bräda i plast på 61 x 23,5 x 2 cm med två handtag och nio positioner.` | `Push Up Board 9in1 är gjord av plast, mäter 61 x 23,5 x 2 cm och har två handtag och nio positioner.` |
| k_11c | 9861 | html | `Push Up Board 9in1 är en armhävningsbräda i plast med …` | `Armhävningsbrädan Push Up Board 9in1 är gjord av plast och har …` |
| k_11c | 9866 | meta | `Slide pads är ett par floor sliders med diametern 17,5 cm och höjden 0,8 cm.` | `Slide pads, även kallade floor sliders, har diametern 17,5 cm och höjden 0,8 cm och säljs parvis.` (150 tecken) |
| k_11c | 9868 | html | `och finns i svart och rött.` | `och är svart och röd.` |
| k_11c | 9874 | meta, html | `De finns i svart och grått och i storlekarna` | `De är svarta och grå och finns i storlekarna` |

Den exakta före-texten per fält finns i JSON-filen.

## Prisvarianter

Det gäller 9834, 9835, 9838, 9842, 9850, 9853, 9856, 9857 och 9869–9875. Ingen titel låser en variant, och alla påståenden gäller alla varianter. Mått per vikt eller storlek är tagna ur produktens egen tabell. **Prisavvikelser till David.** De är inga fel i texten, och texten nämner inga priser:
- 9870 Lyftarbälte: XL kostar 3815 kr, mot 1339 kr för S, M och L.
- 9873 Träningsbälte Smalt: L kostar 519 kr, mot 579 kr för övriga storlekar.
- 9835 Gymhammare: 25 kg kostar 2919 kr men 30 kg bara 2899 kr. 15 kg kostar 2459 kr men 20 kg bara 2439 kr.
- 9850 Markeringskoner: orange är dyrare än gul i samma höjd (23 cm 299 mot 259 kr, 30 cm 509 mot 429 kr). Det kan vara avsiktligt.

## Beslut som behövs

1. **Princip för hängande och bärande produkter** (punkt 1–4 ovan). Rekommendation: godkänn principen och lägg den i regelboken som R4-tillägg. Om inget beslutas skrivs 9854 inte, och 9841, 9844 och 9845 behåller sina live-texter.
2. **Prisavvikelserna** på 9870, 9873, 9835 och 9850 bör kontrolleras i prissättningen. Texterna kan skrivas oavsett.
3. **Förslag på test i skriptet:** varna när första meningen i meta eller html har formen "<namn> är en/ett <typord>". Två egennamn i rad före "är en" eller "är ett" fångar de flesta fallen. Varna också för "finns i <färg> och <färg>" när produkten bara har storleks- eller viktvarianter.
