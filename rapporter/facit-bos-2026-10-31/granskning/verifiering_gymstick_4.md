# Verifiering Gymstick, omgång 4 (c_skriv_resten_4)

Datum: 2026-11-02. Oberoende kontroll, bara läsning. Inget ändrades i Shopify och inget committades.

## Underlag och metod

- Butik: `get-shop-info` gav BEST OF SPORTS, bestofsports.se (SEK, Basic). Rätt butik.
- Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/c_skriv_resten_4.json`, 41 produkter (nr 3227–3295, alla Gymstick).
- Före-fil: `rapporter/shopify-original-2026-11-02/vag2c_resten_4_fore.json`, samma 41 id:n.
- Live: GraphQL `nodes(ids:…)` i tre omgångar (20 + 20 + 1). Fält: title, handle, status, tags, seo{title description}, descriptionHtml. Dessutom varianter för 7 produkter, för att kontrollera storleks- och viktuppgifter.
- Leveransblocket: läst i varje live-svar och identiskt med blocket i `c_1_utkast.json` (från "Leverans, retur och garanti" till "info@bestofsports.se.</p>"). Alla 41 html-fält i skrivfilen slutar med exakt det blocket. Inget FAQ-avsnitt finns i den här omgången.
- Jämförelse: radbrytningar mellan `<li>` räknas inte. SEO-titel förväntas vara null när seo_title är null eller lika med titeln (18 produkter). Meta förväntas vara null när meta är null (9 produkter).

## Resultat per produkt

| Nr | Id | Titel | SEO-titel | Meta | Beskrivning | Status ACTIVE | Handle oförändrad | Övriga taggar kvar | texter-klara |
|---|---|---|---|---|---|---|---|---|---|
| 3227 | 10581112226058 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3230 | 10581112357130 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3231 | 10581112389898 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3232 | 10581112422666 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3233 | 10581112455434 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3235 | 10581112553738 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3236 | 10581112586506 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3237 | 10581112619274 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3238 | 10581112652042 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3241 | 10581112783114 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3244 | 10581112881418 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3245 | 10581112914186 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3246 | 10581112946954 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3248 | 10581118976266 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3249 | 10581119009034 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3250 | 10581119041802 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3251 | 10581119074570 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3252 | 10581119172874 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3256 | 10581119303946 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3258 | 10581119369482 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3259 | 10581119402250 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3261 | 10581119467786 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3263 | 10593397408010 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3269 | 10593407566090 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3270 | 10593407729930 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3271 | 10598114197770 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3272 | 10598117802250 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3273 | 10598117900554 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3274 | 10604622086410 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3280 | 10611430850826 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3282 | 10611433832714 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3283 | 10611438027018 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3284 | 10611438420234 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3285 | 10611438616842 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3287 | 10611438911754 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3290 | 10611453886730 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3291 | 10611454050570 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3292 | 10611454181642 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3293 | 10611454771466 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3294 | 10634245669130 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3295 | 10634331783434 | ja | ja | ja | ja | ja | ja | ja | ja |

**41 av 41 matchar exakt i alla fält.** Alla har status ACTIVE, samma handle som före, taggen `texter-klara` och alla taggar från före-läget kvar. Ingen annan tagg har tillkommit eller försvunnit.

## Gränser

- Titel: alla ≤70 tecken och ≤2 kommatecken (decimalkomma i "0,70 l", "0,4 cm", "45,7 m" undantaget). Längsta titel: "Träningsmatta Gymstick Vivid 170 x 60 x 0,4 cm, Turkos och Grå" (63).
- SEO-titel ≤43: alla klarar gränsen, även där titeln används som SEO-titel (längst: "Massageboll Gymstick Active Myofascia Ball", 42).
- Meta: 32 produkter har meta, alla 130–155 tecken. 9 har null (godkänt).
- Dubbletter: inga dubbletter av titel, SEO-titel (även räknat med titeln som SEO-titel) eller meta inom de 41. Inga dubbletter mot övriga `c_skriv_*.json` (302 poster i de andra filerna, jämfört på andra id:n).

## Kontrollskriptet

`shopify-sync/scripts/kontrollera_produkttext.py --seo-title-max 43 --seo-suffix " – BEST OF SPORTS"` på en kopia (html → beskrivning, standardblocket inom `[[STANDARDBLOCK]]…[[/STANDARDBLOCK]]`, källtext = före-filens titel, beskrivning och SEO-fält).

- **0 FEL**, 52 varningar, slutkod 0.
- Varningarna: 41 × "saknar avsnittet 'passar dig som'" (texterna har rubriken "Passar för", samma mall som tidigare omgångar), 8 × kort beskrivning under 40 ord (3241, 3250, 3259, 3261, 3269, 3274, 3290, 3291; 30–38 ord, källan ger lite fakta), 3 × engelska ordet "Pink" i 3270 (färgnamnet "Twisted Pink" från tillverkaren, godtagbart).

## Faktakontroll

- Hälsopåståenden i källtexterna (lindra smärta, blodcirkulation, rehabilitering, förebygga skador, kaloriförbränning) är borttagna i alla texter. "Miljövänligt" (3246, 3293) är borttaget. Inga ursprungsuppgifter.
- Storlekar och vikter stämmer med varianterna: 3249 har två storlekar (65 och 75), 3241 har S/M och L/XL. För 3233, 3235, 3236 och 3282 finns flera varianter, så det är rätt att vikten eller nivån inte står i titeln.
- Gymtalk (3273) och stor bokstav i titlar ("för Kabelträning", "Rosa och Grå") följer beslutade regler i `produkttexter-standard.md` och räknas inte som fel.
- Inga arbetstermer ("enligt källan", "enligt titeln") och ingen FAQ.

## Språkfynd

Inga stavfel och inga cirkulära "X är en X"-meningar. Alla första metameningar har verb. Fynden nedan är små och ingen hindrar godkännande.

| Nr | Fält | Före | Efter (förslag) | Typ |
|---|---|---|---|---|
| 3233 | html, första stycket | "skyddar både golv och vikterna" | "skyddar både golvet och vikterna" | Grammatik (blandad bestämdhet) |
| 3249 | html, första stycket | "passar den för core-träning, yoga och stretching, för alla nivåer." | "passar den för core-träning, yoga och stretching på alla nivåer." | Upprepning ("för … för") |
| 3249 | html, specifikation | "Storlekar: Två storlekar" | "Storlekar: 65 och 75 cm" (enligt varianterna) eller "Storlekar: Två" | Upprepning |
| 3285 | html, första stycket | "Gymstick Speed är träningskoner för träning av snabbhet" | "Gymstick Speed är koner för träning av snabbhet" | Upprepning |
| 3290 | meta | "Enligt tillverkaren passar den alla nivåer och är tillverkad av slitstarkt material." | "Enligt tillverkaren passar den alla nivåer och är gjord av slitstarkt material." | Upprepning (tillverkaren/tillverkad) |
| 3292 | html, Passar för | "Dig som vill ha en foamroller för övningar för hela kroppen" | "Dig som vill ha en foamroller för övningar över hela kroppen" | Upprepning ("för … för") |
| 3294 | meta | "skyddar väggen mot missade pilar runt standarddarttavlor." | "passar runt standarddarttavlor och skyddar väggen mot missade pilar." | Tvetydig satsbyggnad |
| 3291 | seo_title | "Träningsband Gymstick Vivid, Set med 3" | "Träningsband Gymstick Vivid, 3 st" | Avhuggen formulering |
| 3248 | titel | "Pannbandsset Gymstick Vivid Head Band Set" | Godtagbart (modellnamnet behålls enligt standarden). Notering: "set … Set" upprepas. | Notering |
| 3252 | html, specifikation | "Motstånd: Olika motståndsnivåer" | "Motstånd: Tre olika nivåer" | Upprepning, notering |
| 3272 | meta/html | "Fot- och handmassagerulle är en rulle för fötter och händer" | Godtagbart. Notering: nästan cirkulär. | Notering |

Iakttagelser utanför språkgranskningen:
- 3259 och 3274 har mycket tunt innehåll ("Dig som söker en foamroller på 33 cm"), men det beror på källan.
- 3282: "Extra Heavy" i det gamla namnet syns inte i den nya texten. Det stämmer med varianterna 1–6, men motståndsnivåerna förklaras inte.

## Slutsats

41/41 matchar skrivfilen exakt och har taggen. Inga avvikelser och 0 FEL i kontrollskriptet. 8 språkfynd att rätta (3233, 3249 ×2, 3285, 3290, 3292, 3294, 3291) och 3 noteringar. Inga påhittade fakta hittades.
