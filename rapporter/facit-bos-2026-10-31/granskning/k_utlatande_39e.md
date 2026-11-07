# Granskningsutlåtande k_39e (2026-11-07)

Granskningen har bara läst i Shopify och har inte ändrat något där. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient) mot BEST OF SPORTS (`6f2e53-67.myshopify.com`). Alla 24 produkter är ACTIVE, och alla har lager.

Underlaget var:
- `regler-v1.md` (R1–R19, v1.5–v1.10)
- BESLUTSLOGG till och med 2026-11-07. Där står att de återaktiverade produkterna får text enligt vanliga regler, och att säkerhetsprodukter, olika artiklar och tunn källa avvisas som förut.
- LARDOMAR
- butiksprofilen
- `produkttexter-standard.md` §3, §4, §10, §14 och §16–17
- praxis i `k_utlatande_39ac`

Kontrollerna gav följande:
- `skrivfil_kontroll.py` gav 0 fel och 5 varningar för cirkulära inledningar (39110, 39111, 39118, 39119 och meta på 39120). Alla rättas nedan. Med rättningarna ger skriptet 0 fel och 0 varningar.
- `kontrollera_produkttext.py` anmärker bara på metalängder under 130 tecken. Det är tillåtet, eftersom R12 och §17 kräver 70–155 tecken och alla utkast ligger inom det. Falsklarmet "halsa" kom inte.
- Standardblocket är exakt som i `b_skriv_24.json` på alla 12 produkter.
- 39120 har taggen "På beställning" och leveranstidsmeningen. Ingen annan produkt har taggen.
- Titlarna har högst 70 tecken och högst 2 kommatecken, och SEO-titlarna högst 43 tecken.
- Titel, SEO-titel och meta är unika mot alla andra utkast och skrivfiler, och det gäller även de nya värdena.

Varje rättning anges som ett sammanhängande före/efter-par per fält. Den gamla texten förekommer exakt en gång i utkastet, och det har kontrollerats med skript. Den maskinläsbara versionen finns i `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_39e.json`.

## Resultat: 4 godkända, 8 att rätta, 0 underkända

| nr | id | produkt | dom |
|---|---|---|---|
| 39098 | 10472294318346 | Barncykel Tabou Mini Lite MG, 18 tum, lila och vit | GODKÄND |
| 39101 | 10472301232394 | Handtag för gummiband Toorx, set om 2 | GODKÄND |
| 39107 | 10472307360010 | Barncykel Tabou Miss ST, 12 tum, lila och vit | GODKÄND |
| 39108 | 10472307392778 | Barncykel Tabou Miss ST, 12 tum, rosa och vit | GODKÄND (obs) |
| 39109 | 10472307458314 | Barncykel Tabou Miss FR, 16 tum | RÄTTA |
| 39110 | 10472308703498 | Spinningcykel Toorx SRX-9000 | RÄTTA |
| 39111 | 10472328823050 | Kettlebell Toorx Vinyl, 18 kg | RÄTTA |
| 39113 | 10472330494218 | Barncykel Tabou Rocket FR, 12 tum | RÄTTA |
| 39114 | 10472330625290 | Barncykel Tabou Poison 20 | RÄTTA |
| 39118 | 10472332722442 | Stuntsparkcykel Union Lite XS, Neochrome | RÄTTA |
| 39119 | 10472333148426 | Damcykel Liv Tempt 3 GE 27,5 tum | RÄTTA |
| 39120 | 10472346812682 | Stepbräda Tunturi Aero Step | RÄTTA |

## Rättningar (html om inget annat anges)

- **39109**: aluminium nämndes två gånger i inledningen.
  - före: `<p>Barncykeln Tabou Miss FR har aluminiumram, 16 tums hjul och en växel. Ramen, fälgarna och vevarmarna är av aluminium, och cykeln har V-bromsar, kedjeskydd, stödhjul och skjutstång.</p>`
  - efter: `<p>Barncykeln Tabou Miss FR har ram, fälgar och vevarmar av aluminium, 16 tums hjul och en växel. Cykeln har V-bromsar, kedjeskydd, stödhjul och skjutstång.</p>`
- **39110**: inledningen var cirkulär (R11).
  - före: `<p>Toorx SRX-9000 är en spinningcykel med remdrift, ett svänghjul på 22 kg och en friktionsbroms med läderbelägg.`
  - efter: `<p>Spinningcykeln Toorx SRX-9000 har remdrift, ett svänghjul på 22 kg och en friktionsbroms med läderbelägg.`
- **39111**: inledningen var cirkulär.
  - före: `<p>Toorx Vinyl är en kettlebell på 18 kg med vinylbelagd yta. Den ingår i en serie med flera vikter.</p>`
  - efter: `<p>Kettlebellen Toorx Vinyl har vinylbelagd yta och väger 18 kg. Den ingår i en serie med flera vikter.</p>`
- **39113**: aluminium nämndes två gånger.
  - före: `<p>Barncykeln Tabou Rocket FR har aluminiumram, 12 tums hjul och en växel. Ramen, fälgarna och vevarmarna är av aluminium, och till cykeln hör skjutstång, stödhjul, ringklocka, kedjeskydd och stänkskärmar.</p>`
  - efter: `<p>Barncykeln Tabou Rocket FR har ram, fälgar och vevarmar av aluminium, 12 tums hjul och en växel. Till cykeln hör skjutstång, stödhjul, ringklocka, kedjeskydd och stänkskärmar.</p>`
- **39114**: hela delen före standardblocket rättas som en bit, se JSON. Två ändringar görs:
  - Inledningen var ogrammatisk och blir "Barncykeln Tabou Poison 20 **är** utformad som en mountainbike **och** har …".
  - `<li>Ingår: Stöd</li>` blir `<li>Ingår: Cykelstöd</li>`, som på det skrivna syskonet Poison 24. Cykelstöd är ett godkänt typord.
- **39118**: inledningen var cirkulär.
  - före: `<p>Union Lite XS är en stuntsparkcykel med aluminiumkonstruktion,`
  - efter: `<p>Stuntsparkcykeln Union Lite XS har aluminiumkonstruktion,`
- **39119**: inledningen var cirkulär.
  - före: `<p>Liv Tempt 3 GE är en damcykel med aluminiumram,`
  - efter: `<p>Damcykeln Liv Tempt 3 GE har aluminiumram,`
- **39120 meta**: inledningen var cirkulär. Den nya metan är 128 tecken.
  - före: `Tunturi Aero Step är en stepbräda av syntetiskt material som är justerbar i tre lägen. Enligt tillverkaren är maxvikten 120 kg.`
  - efter: `Stepbrädan Tunturi Aero Step är justerbar i tre lägen och gjord av syntetiskt material. Enligt tillverkaren är maxvikten 120 kg.`
- **39120 html**:
  - före: `<p>Tunturi Aero Step är en stepbräda som är justerbar i tre lägen, med höjdinställning upp till 20 och 25 cm. Stepbrädan är gjord av syntetiskt material och väger 8 kg.</p>`
  - efter: `<p>Stepbrädan Tunturi Aero Step är justerbar i tre lägen, med höjdinställning upp till 20 och 25 cm. Den är gjord av syntetiskt material och väger 8 kg.</p>`

## Särskilda kontroller

- **Hjulvikt hos Tabou:** "Hjulvikt" tolkas som cykelns vikt, och tolkningen är rätt. Det är en maskinöversättning av estniska "ratta kaal", där ratas kan betyda både hjul och cykel. Raden säger dessutom "(utan tillbehör)". tabou.pl bekräftar vikterna på tre av modellerna:
  - Mini/Miss Lite MG 18": 7 kg
  - Rocket FR 12": 6,5 kg
  - Rocket FR 16": 7,5 kg

  För Miss ST 12" har ingen tillverkarsida hittats. Där står etiketten "utan tillbehör" i källan, och det skrivna syskonet Miss ST 14 skrevs på samma sätt.
- **Bromstyp:** utelämnad på 12" och 18". Det är rätt, eftersom tabou.pl anger V-broms fram och bandbroms bak medan källan bara säger V-bromsar. På Miss FR 16" får V-bromsar stå, eftersom tabou.pl anger V-broms fram och bak för 16". De skrivna syskonen (Rocket FR 12 röd-gul och Mini Lite MG 14) säger "V-bromsar" utan bandbroms. Det står i källan, men det är en inkonsekvens att känna till.
- **Typord:**
  - "Handtag för Gummiband" (39101) är rimligt. Det är en entydig översättning av "Handles for Elastic Bands", och båda orden är butikens live-ord.
  - Kettlebell (39111) är butikens live-ord och står redan på de skrivna Kettlebell Toorx Vinyl 12 kg och 20 kg.

  Inget av dem behöver bytas, men båda bör läggas in i `godkanda_typord`.
- **Spinningcykel SRX-9000 (39110):** produkten får skrivas. Den har manuell friktionsbroms och ingen display, motor eller batteri. Datorn med BLE/ANT+ är ett tillval och nämns inte. §10 gäller spinningcyklar med elektronik.
- **Tunn källa (39101, 39111):** båda har kort meta på 83 och 100 tecken, utan utfyllnad och med verb. Det följer §14 och §17 och Davids beslut 2026-11-05 om tunn källa.
- **Lastgräns (v1.10, R4):**
  - 39110 (150 kg), 39118 (100 kg) och 39120 (120 kg) har rena svenska rader med etikett och enhet. Varje värde står en gång som "enligt tillverkaren" i specifikationen och en gång i meta, som i praxis.
  - Raden "robust metallkärna upp till 150 kg" (39110) är rätt utelämnad.
- **Varianter (v1.9):** alla 12 har en enda variant, så färg och vikt i titeln låser inget.
- **Hälso-, säkerhets- och kvalitetslöften:** inga finns. Utelämnat är bland annat "ultralätt", "maximal säkerhet", "slitstark", "skyddar golvet", "robust" och "ljudlös".
- **Säkerhetsprodukter:** ingen har slunkit med bland utkasten.
- **Obs 39108:** källan säger "stödstång", medan syskonet 39107 säger "skjutstång". Troligen avses samma sak. Ordet godtas eftersom det står i egen källa, men det kan bytas till "skjutstång" om David vill ha samma ord på båda.

## Avvisade (12)

Avvisningen står för 7 av 12. Fyra har fel skäl och kan släppas till ett nytt utkast, och en står men med ändrat skäl.

**Dubbdäck 39102, 39103, 39104 och 39105: skälet är fel, och produkterna kan släppas.** Dubbdäck får skrivas utan prestandapåståenden (BESLUTSLOGG 2026-11-05), och Suomi Tyres skrevs i `k_skriv_26a` utifrån tillverkarens tabell. De trasiga och avklippta live-titlarna löses med tillverkarens tabell per artikelnummer på https://suomityres.fi/products/winter/city/routa:

| nr | SKU | modell | storlek | dubbar |
|---|---|---|---|---|
| 39102 | T506081 | Routa W176 | 47-406, 20 tum | 176 |
| 39104 | T506381 | Routa W106 | 47-507, 24 tum | 106 |
| 39105 | T506281 | Routa W212 | 47-507, 24 tum | 212 |
| 39103 | T600281 | Kide W106 | 47-622, 28 tum | 106 |

Kommentarer till tabellen:
- 39104: live-titelns "Hjul" är fel. Källtexten och tillverkaren anger Routa.
- 39103: uppgifterna kommer från https://suomityres.fi/products/winter/city/kide-w106. Utkastaren ska verifiera dem på sidan.
- 39102: källans "47-406 (24 tum)" motsäger sig själv. Använd tillverkarens 20 tum.

Det nya utkastet ska ha storlek, dubbantal och dubbmaterial (stål, för Routa) och inga grepp-, säkerhets- eller punkteringspåståenden. Tumbredden (1.75 eller 1.85) ska inte låsas.

**Romet Rambler 39117: avvisningen står, men inte bara för titeln.**
- Live-titeln säger R6.0 JR, medan källtexten genomgående beskriver R6.1 JR (21 växlar, framfjädring). Velomarket säljer R6.0 JR som en egen produkt, så modellen kan inte avgöras utan gissning (R2/R3).
- Varianterna är "Default Title" (26170022-A, 7 059 kr) och "L / roheline" (26190023-A, 6 139 kr). SKU-mönstret tyder på ram 17" och 19". Default-varianten saknar storlek, och källans S/M/L stämmer inte med varianterna.
- Även med v1.9 kan titel och text därför inte skrivas säkert.

Produkten kan skrivas om David eller leverantören bekräftar modellen (R6.0 eller R6.1) och vilken storlek default-varianten har.

**Övriga avvisningar står:**
- 39097 Spokey viktplattor: fem olika artiklar och vikter (v1.9).
- 39099 SRX-80 EVO: LCD-display, och svänghjulet anges som både 20 och 24 kg.
- 39100: trampolin.
- 39106 BH Xcalibur: servomotor, LCD och FTMS.
- 39112 Coast Jifo: elcykel med motor och batteri.
- 39115 och 39116: hjälmar.

## Frågor till David

1. **Elcyklar och hjälmar:** de har tidigare skrivits i faktatextläge (§16, `k_skriv_01*`), men i den här omgången avvisas de som säkerhetsprodukter enligt uppdraget. Gäller det fortfarande, eller ska 39112, 39115 och 39116 få faktatext som de tidigare grupperna?
   - Rekommendation: skriv dem som förut med bara fakta.
   - Om inget beslutas förblir de utan vår text.
2. **Dubbdäcken 39102–39105:** ska de få nya utkast enligt tabellen ovan? Rekommendationen är ja.
3. **Typord:** ska "Handtag för gummiband" och "Kettlebell" läggas in i `godkanda_typord`?

Webbkällor: [tabou.pl Mini/Miss Lite MG](https://www.tabou.pl/produkt/rower-dzieciecy-tabou-mini-lite-mg/), [tabou.pl Rocket FR](https://www.tabou.pl/produkt/rower-dzieciecy-tabou-rocket-fr/), [tunturi.com Aerobic Step](https://www.tunturi.com/en/aerobic-step.html), [suomityres.fi Routa](https://suomityres.fi/products/winter/city/routa), [suomityres.fi Kide W106](https://suomityres.fi/products/winter/city/kide-w106), [veloplus Routa W176 20x1.75](https://veloplus.ee/en/naastrehv-suomi-tyres-20x1-75-47-406-routa-w176-naastu-55196), [veloplus Routa W212 24x1.75](https://veloplus.ee/en/naastrehv-suomi-tyres-24x175-47-507-routa-w212-55195).
