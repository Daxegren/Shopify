# Granskningsutlåtande k_28e–k_28h (BEST OF SPORTS), 2026-11-05

Granskaren är Opus och har bara läst. Underlaget är `vag2_skriv/k_28e_utkast.json` (6), `k_28f_utkast.json` (7), `k_28g_utkast.json` (8) och `k_28h_utkast.json` (10), alltså 31 produkter. Källtext, varianter (pris, SKU, EAN), vendor och taggar lästes live via Admin API 2026-11-05. Butiken bekräftades som BEST OF SPORTS (6f2e53-67.myshopify.com). Ingenting skrevs i Shopify. Regler: regler-v1.md v1.4–v1.8, BESLUTSLOGG 2026-11-05 och profilens `frislappta_2026_11_05.barn`.

**Resultat:** 19 GODKÄND, 12 RÄTTA, 0 UNDERKÄND. `skrivfil_kontroll.py` gav 0 fel och 0 varningar, både på utkasten och på en rättad kopia. Varje 'före' förekommer exakt en gång i sitt fält (kontrollerat i python). Alla metatexter, titlar och SEO-titlar i kopian är unika inom de fyra filerna, och de rättade metatexterna har 97–140 tecken.

**Genomgående:**
- **Barnregeln:** ingen produkt är underkänd. Ingen text har säkerhets-, skydds- eller utvecklingspåståenden. Stödhjul, kedjeskydd, stänkskärmar, korgar, ringklockor och stödben nämns bara som medföljande delar. 'Skydd för ankel, häl och tå' (28066), 'barnsäkerhet' (28067, 28084), 'maximal säkerhet' (Tabou) och hjälmtillbehören är utelämnade. Inget faller under barnhjälm, stol eller säte, bälte, babyprodukt eller barntransport.
- **Korgar och pakethållare (28055, 28056, 28065, 28067, 28084, 28092, 28095, 28096):** ingen lastgräns anges eller antyds, och källorna har ingen svensk lastgräns. Det följer praxis 28044 och 28045. Om David räknar cykelkorgar eller pakethållare på barncyklar som bärande delar (v1.7) ska de hållas, och då gäller det också redan skrivna korgar.
- **Belysning:** 28067 och 28084 räknade upp fram- och bakljus som medföljande. Det stryks, eftersom ljus är en synbarhetsfunktion (§16.2, praxis 28026 och utkastarens egen 28095).
- **Lås (28061):** säkerhetsnivån stryks (§16.5, praxis k_23 och k_25). Modellnamnet 6-60 är belagt på nätet.
- **Märket S´COOL** (28049, 28054, 28057, 28077, 28085, 28086) var skrivet i versaler. Det rättas till S'cool, som i 28026 (R8). Skriptet missade det, eftersom märket inte finns i profilens `marken`. Förslag till koordinatorn: lägg till S'cool i profilens märkeslista, så att skriptet kan upptäcka versaler.
- **Typord:** Rideoo blir Sparkcykel, som syskonet 28037 (R7). Löparcykel (28080) och Cykeldekorationer (28081) är belagda.
- **Leveranstid:** bara 28082 har taggen 'På beställning', och bara den har leveranstidsmeningen. Det är rätt.
- **Titlar och färg:** alla 31 produkter har en variant (Default Title), och ingen titel låser en variant som inte finns. Färgen står bara där live-titeln eller källan anger den. Titlarna har versal efter bindestreck. I specifikationerna har en rad versal efter bindestreck (28049 'Blå-Rosa'), och den rättas.
- **Meta:** alla metatexter har verb. 28080 rättas för innehållet, inte för formen.
- **Att notera för butiken (rörs inte):** 28072 har taggen 16" men titeln säger 18 tum, 28066 har vendor Jagwire och storleken bara i SKU:n, 28076 har taggen Hybridcykel och 28077 har taggen Cykelbelysning.

## 28049 (10472248541450, k_28e_utkast.json): RÄTTA

Live: en variant (4067S), 6249 kr. Aluminium, 1 växel, V-broms och fotbroms, 8,3 kg och 16 tum (egen rad) stämmer. Kedjeskydd, stödhjul och stänkskärmar nämns bara som medföljande delar ('Inkluderar'), utan skydds- eller lastpåstående (praxis 28030). Marknadsföringen är rätt utelämnad. Färgen står i live-titeln och produkten har en variant. Rättningar: Märket skrivs S'cool som i 28026 (R8, versaler bara för SOKE och TRYM); skriptet känner inte märket och missade det. Dubbelt 'och' i första meningen, och specifikationsraden får gemen efter bindestreck (praxis 'Lime-grå').

- `titel` före: `Barncykel S´COOL niXe, 16 tum, Blå-Rosa`
  efter: `Barncykel S'cool niXe, 16 tum, Blå-Rosa`

- `seo_title` före: `Barncykel S´COOL niXe, Blå-Rosa`
  efter: `Barncykel S'cool niXe, Blå-Rosa`

- `meta` före: `Barncykeln S´COOL niXe i blå-rosa har aluminiumram, 1 växel och 16-tumshjul. Stödhjul, kedjeskydd och stänkskärmar medföljer.`
  efter: `Barncykeln S'cool niXe i blå-rosa har aluminiumram, 1 växel och 16-tumshjul. Stödhjul, kedjeskydd och stänkskärmar medföljer.`

- `html` före: `Barncykeln S´COOL niXe har aluminiumram och en växel och 16-tumshjul.`
  efter: `Barncykeln S'cool niXe har aluminiumram, en växel och 16-tumshjul.`

- `html` före: `<li>Färg: Blå-Rosa</li>`
  efter: `<li>Färg: Blå-rosa</li>`

## 28054 (10472250409226, k_28e_utkast.json): RÄTTA

Live: en variant (4069), 5289 kr. Källan saknar raden Hjulstorlek, så 16 tum står rätt nog bara i titeln (från live-titeln). Aluminium, 1 växel, bromsar, 8,3 kg och medföljande delar stämmer. 'Valfria tillbehör som hjälmar, lås' är rätt utelämnat. Webbkällorna i att_bekrafta används inte i texten. Rättning: Märket skrivs S'cool som i 28026 (R8, versaler bara för SOKE och TRYM); skriptet känner inte märket och missade det.

- `titel` före: `Barncykel S´COOL niXe, 16 tum, Grön`
  efter: `Barncykel S'cool niXe, 16 tum, Grön`

- `seo_title` före: `Barncykel S´COOL niXe, Grön`
  efter: `Barncykel S'cool niXe, Grön`

- `meta` före: `Barncykeln S´COOL niXe i grön har aluminiumram, 1 växel samt V-broms och fotbroms. Stödhjul, kedjeskydd och stänkskärmar medföljer.`
  efter: `Barncykeln S'cool niXe i grön har aluminiumram, 1 växel samt V-broms och fotbroms. Stödhjul, kedjeskydd och stänkskärmar medföljer.`

- `html` före: `Barncykeln S´COOL niXe har`
  efter: `Barncykeln S'cool niXe har`

## 28055 (10472250671370, k_28e_utkast.json): GODKÄND

Live: en variant (59227), 99 kr. Plast, Musse Pigg-tema och fäste på styret med medföljande band stämmer. Ingen lastgräns anges eller antyds (cykelkorg, praxis 28044/28045). Måtten är försiktigt utelämnade: '20 x 13 x 13 cm' är i sig entydig, men raden 'Plast : 13 x 13 cm' motsäger den. Det är godtagbart. 'Enkelt' är utelämnat. Ingen rättning.

## 28056 (10472251195658, k_28e_utkast.json): GODKÄND

Live: en variant (431559), 49 kr. Plast, flexibel fästklämma och justerbara snabbfästen stämmer, och 'Universellt' är rätt struket. Uppmaningen att ange färg i orderkommentaren står ordagrant i källan och är nödvändig för att kunden ska kunna välja färg. Ingen lastgräns anges. Ingen rättning.

## 28057 (10472252080394, k_28e_utkast.json): RÄTTA

Live: en variant (4066S), 5269 kr. Samma fakta som 28049, och 16 tum står i egen rad. Live-titelns punkt rättas till komma. Rättningar: Märket skrivs S'cool som i 28026 (R8, versaler bara för SOKE och TRYM); skriptet känner inte märket och missade det. Dubbelt 'och' i första meningen.

- `titel` före: `Barncykel S´COOL niXe, 16 tum, Rosa`
  efter: `Barncykel S'cool niXe, 16 tum, Rosa`

- `seo_title` före: `Barncykel S´COOL niXe, Rosa`
  efter: `Barncykel S'cool niXe, Rosa`

- `meta` före: `Barncykeln S´COOL niXe i rosa väger 8,3 kg och har V-broms och fotbroms. Stödhjul, kedjeskydd och stänkskärmar medföljer.`
  efter: `Barncykeln S'cool niXe i rosa väger 8,3 kg och har V-broms och fotbroms. Stödhjul, kedjeskydd och stänkskärmar medföljer.`

- `html` före: `Barncykeln S´COOL niXe har aluminiumram och en växel och 16-tumshjul.`
  efter: `Barncykeln S'cool niXe har aluminiumram, en växel och 16-tumshjul.`

## 28059 (10472252997898, k_28e_utkast.json): GODKÄND

Live: en variant (24130732-A), 6519 kr. Aluminium 6061, 21 växlar, V-bromsar, 24-tums aluminiumhjul, 13,2 kg och '13 tum' (entydig del av den trasiga ramraden) stämmer. Shimano-modellen, stötdämparen och förarlängden är rätt utelämnade, eftersom källorna går isär. '4–5 säsonger' (utveckling), ursprung och kvalitetsord är utelämnade. Webbkoll: centrumrowerowe.pl (öppnad) gäller en annan årsmodell (EAN 5907782722753, 13 kg) och belägger inget i texten. 13 tum står ändå i den egna källan. Typordet Cykel står i live-titeln. Ingen rättning.

## 28061 (10472254996746, k_28f_utkast.json): RÄTTA

Live: en variant (59430602SC, EAN 8713249277387), 89 kr. Modellnamnet 6-60 är rätt: bike-components.de (öppnad) listar 'Axa Resolute 6-60 Cable Lock', 60 cm och 6 mm, och sökträffar hos bike24 och meinhartje kopplar 59430602SC och EAN 8713249277387 till Resolute 6-60 ice blue (sidorna gick inte att öppna, 403/404). 'Passar bäst för barncyklar', fälgskyddet och 'Säkerhetslås' är rätt utelämnade. Rättning: säkerhetsnivån stryks ur meta och specifikation. §16.5 säger inga påståenden om säkerhetsnivå för lås, och praxis sedan k_23 och k_25 (23025, 25033–25035) är att stryka nivån. Kabeltjockleken 6 mm läggs inte till, eftersom den öppnade sidan anger en annan variant (59430602KC).

- `meta` före: `Kabellåset Axa Resolute 6-60 är 60 cm långt och har automatisk låsning. Säkerhetsnivån är 2 enligt tillverkaren.`
  efter: `Kabellåset Axa Resolute 6-60 är 60 cm långt, har automatisk låsning och artikelnummer 59430602SC.`

- `html` före: `<li>Säkerhetsnivå enligt tillverkaren: 2</li>`
  efter: (raden stryks)

## 28062 (10472255684874, k_28f_utkast.json): GODKÄND

Live: en variant (59356), 49 kr. Fäste på handtagen, 4,2 cm, ca 19 cm, plast och polyester stämmer ordagrant. 'Personifiera ditt barns cykel' är utelämnat. Färgen står i live-titeln. Inga skydds- eller säkerhetsfrågor. Ingen rättning.

## 28065 (10472256143626, k_28f_utkast.json): GODKÄND

Live: en variant (59361), 99 kr. Plast, Wish-tema, 20 x 13 x 13 cm, band till styret och lila (står både i källan och titeln) stämmer. Ingen lastgräns anges eller antyds (praxis 28044/28045). Ingen rättning.

## 28066 (10472257192202, k_28f_utkast.json): GODKÄND

Live: en variant (WNT313034/37), 1719 kr, vendor Jagwire (fel i butiken, rörs inte). Det är isskridskor (blad i rostfritt stål, taggen Skridskor), inte rullskridskor. Förslipade blad, halvmjuk känga och storleksjustering med knapp stämmer. Storleksintervallen är rätt utelämnade: källan anger 34–37 och 38–41, men varianten heter Default Title, och bara SKU:n antyder 34–37 (v1.5, R2). 'Skydd för ankel, häl och tå' (skyddsfunktion) och 'pojkars' är rätt utelämnade. Färgen står i live-titeln. Ingen rättning. Butiken bör ange storleken som variant.

## 28067 (10472257257738, k_28f_utkast.json): RÄTTA

Live: en variant (24130735-A), 7049 kr. Aluminium, 24 tum, S (13 tum), 135–155 cm (enligt tillverkaren en gång) och Shimano Nexus stämmer. Antalet växlar är rätt utelämnat (3 eller 5). Pakethållaren och stänkskärmarna nämns bara som utrustning, utan last- eller bärpåstående. Ingen lastgräns finns, och ingen behövs när delen inte säljs som bärande produkt (praxis för korgar). Rättning: fram- och bakljus stryks ur meta, löptext och specifikation. Ljus är en synbarhetsfunktion (§16.2, praxis 28026 och utkastarens egen 28095), och källan kopplar dem till 'barnsäkerhet'.

- `meta` före: `Flickcykeln Romet Panda 2 har aluminiumram, Shimano Nexus-växellåda, pakethållare, stänkskärmar samt fram- och bakljus.`
  efter: `Flickcykeln Romet Panda 2 i rosa har aluminiumram, 24-tumshjul, Shimano Nexus-växellåda, pakethållare och stänkskärmar.`

- `html` före: `Pakethållare, stänkskärmar samt fram- och bakljus ingår.`
  efter: `Pakethållare och stänkskärmar ingår.`

- `html` före: `<li>Medföljer: Pakethållare, stänkskärmar samt fram- och bakljus</li>`
  efter: `<li>Medföljer: Pakethållare och stänkskärmar</li>`

## 28070 (10472280064266, k_28f_utkast.json): RÄTTA

Live: en variant (4743128000021), 149 kr. 'Maximal användarvikt 30 kg' är en ren svensk rad med etikett och enhet och står en gång med 'enligt tillverkaren' i texten (R4). Färgerna rött och blått står i källan. Källan är tunn, men har två entydiga fakta (R3). Bindningar och 41 cm står rätt nog bara i titeln. Kunden kan inte välja färg (texten utelämnar orderkommentaren och färgen beror på lagret). Rättningar: raden 'väljer mellan rött och blått' och 'Färger: Rött och blått' antyder ett val eller båda färgerna. De skrivs om till 'rött eller blått'.

- `html` före: `<li>Dig som väljer mellan rött och blått</li>`
  efter: `<li>Dig som söker skidor i rött eller blått</li>`

- `html` före: `<li>Färger: Rött och blått</li>`
  efter: `<li>Färg: Rött eller blått</li>`

## 28072 (10472282652938, k_28f_utkast.json): GODKÄND

Live: en variant (TAB25-7640), 7329 kr. Taggen säger 16 tum, men live-titeln säger 18 tum. Ramstorleken 24 cm och 110–120 cm passar 18 tum i Tabou-serien (14 tum 22 cm, 16 tum 22,5 cm), och en sökträff för velomarket.ee (leverantörens egen butik) anger 18 tum med 24 cm. 18 tum står bara i titeln och inte som specifikation. Magnesium, aluminiumdelar, 1 växel, V-bromsar, stödhjul och kedjeskydd (bara som medföljande delar) stämmer. Hjulvikt, 'maximal säkerhet' och 'ultralätt' är utelämnade. Ingen rättning. Taggen 16" bör kontrolleras av butiken.

## 28073 (10472282751242, k_28g_utkast.json): GODKÄND

Live: en variant (TAB25-7580), 7149 kr. Titeln och taggen säger 16 tum. 22,5 cm, 105–115 cm (enligt tillverkaren en gång), magnesium, 1 växel, V-bromsar, stödhjul och kedjeskydd (bara medföljande) stämmer. Säkerhets- och komfortorden och hjulvikten är utelämnade. Ingen rättning.

## 28076 (10472285536522, k_28g_utkast.json): RÄTTA

Live: en variant, 2969 kr, produkttyp Sparkcyklar. 'Lastkapacitet: upp till 70 kg' (ren svensk rad med etikett och enhet, R4) och 'Lämplig för förare i åldern 4 till 7 år' står var sin gång med 'enligt tillverkaren', alltså två gånger. Det är taket enligt R5. Meta har ingen av dem. Hopfällbar, ABEC-9, 120 mm och 3,4 kg stämmer, och komfortorden är utelämnade. Turkos är en säker översättning av 'Turquise'. Rättning: typordet blir Sparkcykel, som för syskonmodellen Rideoo 175 City (28037) och 8993 (butikens live-ord, produkttyp Sparkcyklar, R7 enhetligt i gruppen).

- `titel` före: `Scooter Rideoo 120 City, Turkos`
  efter: `Sparkcykel Rideoo 120 City, Turkos`

- `seo_title` före: `Scooter Rideoo 120 City, Turkos`
  efter: `Sparkcykel Rideoo 120 City, Turkos`

- `meta` före: `Scootern Rideoo 120 City är hopfällbar, har höjdjusterbart styre och polyuretanhjul på 120 mm samt väger 3,4 kg.`
  efter: `Sparkcykeln Rideoo 120 City är hopfällbar, har höjdjusterbart styre och polyuretanhjul på 120 mm samt väger 3,4 kg.`

- `html` före: `<p>Scootern Rideoo 120 City är hopfällbar och har höjdjusterbart styre och polyuretanhjul. Hjuldiametern är 120 mm och scootern väger 3,4 kg. Scootern är turkos.</p>`
  efter: `<p>Sparkcykeln Rideoo 120 City är hopfällbar och har höjdjusterbart styre och polyuretanhjul. Hjuldiametern är 120 mm och sparkcykeln väger 3,4 kg. Den är turkos.</p>`

- `html` före: `<li>Dig som söker en scooter som går att fälla ihop</li>`
  efter: `<li>Dig som söker en sparkcykel som går att fälla ihop</li>`

- `html` före: `<li>Dig som vill ha en scooter med höjdjusterbart styre</li>`
  efter: `<li>Dig som vill ha en sparkcykel med höjdjusterbart styre</li>`

- `html` före: `<li>Dig som söker en scooter med polyuretanhjul</li>`
  efter: `<li>Dig som söker en sparkcykel med polyuretanhjul</li>`

- `html` före: `<li>Typ: Scooter</li>`
  efter: `<li>Typ: Sparkcykel</li>`

## 28077 (10472285831434, k_28g_utkast.json): RÄTTA

Live: en variant (3078), 4909 kr. Aluminium, 1 växel, V-broms och fotbroms, 7,6 kg, 12 tum (egen rad), kedjeskydd och stänkskärmar (medföljande) samt 'stödhjul ingår ej' stämmer. Taggen Cykelbelysning är fel men rörs inte, och texten nämner ingen belysning. Rättning: Märket skrivs S'cool som i 28026 (R8, versaler bara för SOKE och TRYM); skriptet känner inte märket och missade det.

- `titel` före: `Barncykel S´COOL XXlite, 12 tum, Röd-Ljusblå`
  efter: `Barncykel S'cool XXlite, 12 tum, Röd-Ljusblå`

- `seo_title` före: `Barncykel S´COOL XXlite, Röd-Ljusblå`
  efter: `Barncykel S'cool XXlite, Röd-Ljusblå`

- `meta` före: `Barncykeln S´COOL XXlite i röd-ljusblå har aluminiumram, 1 växel samt V-broms och fotbroms. Kedjeskydd och stänkskärmar medföljer.`
  efter: `Barncykeln S'cool XXlite i röd-ljusblå har aluminiumram, 1 växel samt V-broms och fotbroms. Kedjeskydd och stänkskärmar medföljer.`

- `html` före: `Barncykeln S´COOL XXlite har`
  efter: `Barncykeln S'cool XXlite har`

## 28079 (10472286224650, k_28g_utkast.json): GODKÄND

Live: en variant (59293), 49 kr. Samma fakta som 28062. 'Färgglad' är ingen kulör och är rätt utelämnad. Ingen rättning.

## 28080 (10472286454026, k_28g_utkast.json): RÄTTA

Live: en variant (TAB22-3000), 3199 kr. Typordet Löparcykel står i källtexten (R7). Magnesiumlegering, 12 tum och 80–100 cm (enligt tillverkaren en gång) stämmer. Rättning: metan kortade källans 'den yngsta cyklisten i Tabou Mini Run-familjen' till 'avsedd för den yngsta cyklisten'. Det ändrar betydelsen till ett allmänt åldersanspråk. Ny meta med fakta.

- `meta` före: `Löparcykeln Tabou Mini Run har ram av magnesiumlegering och 12-tumshjul och är avsedd för den yngsta cyklisten.`
  efter: `Löparcykeln Tabou Mini Run har ram av magnesiumlegering och 12-tumshjul. Rekommenderad cyklistlängd är 80–100 cm.`

## 28081 (10472287207690, k_28g_utkast.json): GODKÄND

Live: en variant (59171), 49 kr. Typordet byts från 'Bicycle decorations' till Cykeldekorationer. Det är en entydig översättning, och butikens live-ord för Wish och Stitch är Cykeldekorationer (R7). Fakta som 28062. Ingen rättning.

## 28082 (10472288846090, k_28g_utkast.json): GODKÄND

Live: en variant, 1949 kr, taggen 'På beställning'. Leveranstidsmeningen står exakt som i profilen (R13), och källans egen ⏳-mening är borttagen. Bredd 44/44/44 mm, CAP, trä med luftkanaler, Nanogrip, junior-bindning och monterad bindning stämmer. Nanogrip-funktionen återges ordagrant en gång med 'enligt tillverkaren'. Det är ett funktionspåstående, inget säkerhetspåstående. 'Ingen vallning', skate-teknik, längdrådet och 110 (bara i SKU:n) är rätt utelämnade. Ingen rättning.

## 28084 (10472290746634, k_28g_utkast.json): RÄTTA

Live: en variant (24130736-B), 7329 kr. Samma fakta som 28067, och stödben står i källan ('Inkluderar ... stödben'). Rättning: fram- och bakljus stryks på samma sätt som i 28067.

- `meta` före: `Flickcykeln Romet Panda 2 i vit-beige har aluminiumram, Shimano Nexus-växellåda, pakethållare, stänkskärmar samt fram- och bakljus.`
  efter: `Flickcykeln Romet Panda 2 i vit-beige har aluminiumram, 24-tumshjul, Shimano Nexus-växellåda, pakethållare, stänkskärmar och stödben.`

- `html` före: `Pakethållare, stänkskärmar, stödben samt fram- och bakljus ingår.`
  efter: `Pakethållare, stänkskärmar och stödben ingår.`

- `html` före: `<li>Medföljer: Pakethållare, stänkskärmar, stödben samt fram- och bakljus</li>`
  efter: `<li>Medföljer: Pakethållare, stänkskärmar och stödben</li>`

## 28085 (10472290844938, k_28h_utkast.json): RÄTTA

Live: en variant (5089), 6359 kr. Aluminium, 28 cm, ca 105–120 cm (enligt tillverkaren en gång), 1 växel, bromsar, 9,5 kg, 18 tum (egen rad), stänkskärmar och kedjeskydd stämmer. 'Stöd', den trasiga raden '18.5' och 'säkerhet' är rätt utelämnade. Rättning: Märket skrivs S'cool som i 28026 (R8, versaler bara för SOKE och TRYM); skriptet känner inte märket och missade det.

- `titel` före: `Barncykel S´COOL niXe, 18 tum, Grön-Lime`
  efter: `Barncykel S'cool niXe, 18 tum, Grön-Lime`

- `seo_title` före: `Barncykel S´COOL niXe, Grön-Lime`
  efter: `Barncykel S'cool niXe, Grön-Lime`

- `meta` före: `Barncykeln S´COOL niXe i grön-lime har aluminiumram, 1 växel, 18-tumshjul samt V-broms och fotbroms. Stänkskärmar och kedjeskydd ingår.`
  efter: `Barncykeln S'cool niXe i grön-lime har aluminiumram, 1 växel, 18-tumshjul samt V-broms och fotbroms. Stänkskärmar och kedjeskydd ingår.`

- `html` före: `Barncykeln S´COOL niXe har`
  efter: `Barncykeln S'cool niXe har`

## 28086 (10472291074314, k_28h_utkast.json): RÄTTA

Live: en variant (4076), 6449 kr. 25 cm och 99–120 cm är den entydiga delen av en trasigt inledd rad (R2). Aluminium, 1 växel, bromsar, 8,6 kg, 16 tum (egen rad), kedjeskydd och stänkskärmar stämmer. Rättning: Märket skrivs S'cool som i 28026 (R8, versaler bara för SOKE och TRYM); skriptet känner inte märket och missade det.

- `titel` före: `Barncykel S´COOL XXlite, 16 tum, Svart-Orange`
  efter: `Barncykel S'cool XXlite, 16 tum, Svart-Orange`

- `seo_title` före: `Barncykel S´COOL XXlite, Svart-Orange`
  efter: `Barncykel S'cool XXlite, Svart-Orange`

- `meta` före: `Barncykeln S´COOL XXlite i svart-orange har aluminiumram, 1 växel, 16-tumshjul samt V-broms och fotbroms. Kedjeskydd och stänkskärmar ingår.`
  efter: `Barncykeln S'cool XXlite i svart-orange har aluminiumram, 1 växel, 16-tumshjul samt V-broms och fotbroms. Kedjeskydd och stänkskärmar ingår.`

- `html` före: `Barncykeln S´COOL XXlite har`
  efter: `Barncykeln S'cool XXlite har`

## 28087 (10472291139850, k_28h_utkast.json): GODKÄND

Live: en variant (1012002410), 8629 kr. Aluminium, 120–140 cm (enligt tillverkaren en gång), Shimano Altus, 8 växlar, fälgbromsar och 8,5 kg stämmer. 'Ultralätt', 'lättaste', 'stabil' och 'världens största' är rätt utelämnade, också ur titeln. Ingen rättning.

## 28090 (10472291270922, k_28h_utkast.json): GODKÄND

Live: en variant (TAB25-6690), 6079 kr. 26,5 cm och 110–120 cm (entydig del av en trasig rad), aluminium i ram, fälgar och vevparti, 1 växel, V-bromsar och kedjeskydd stämmer. 'Extra hjul' och 'skjutstång' är oklara och rätt utelämnade, liksom hjulvikten och säkerhetsorden. Ingen rättning.

## 28091 (10472291336458, k_28h_utkast.json): GODKÄND

Live: en variant (TAB25-7080), 6679 kr. 28 cm, ca 115–135 cm, Shimano Tourney, 6 växlar, V-bromsar, ca 10 kg och fästpunkter stämmer. 'Shimano Touring' och 'för flickor' är rätt utelämnade. Typordet Barncykel står i live-titeln. Ingen rättning.

## 28092 (10472292253962, k_28h_utkast.json): GODKÄND

Live: en variant (TAB26-0040), 4479 kr. Titeln och taggen säger 16 tum. Stål, 'Rammått: 24,5 cm', 105–115 cm, 1 växel och V-bromsar stämmer. Stödhjul, kedjeskydd, korg och ringklocka nämns bara som medföljande delar. Korgen har ingen lastuppgift. 'Stödstång', hjulvikten och säkerhetsorden är utelämnade. Ingen rättning.

## 28093 (10472292286730, k_28h_utkast.json): GODKÄND

Live: en variant (TAB26-0050), 4479 kr. Källan skriver 'Rammaterial: 24,5 cm'. Ram: stål står separat, och syskonet 28092 har samma värde under 'Rammått', så Ramstorlek 24,5 cm är entydigt. Övrigt som 28092. Ingen rättning.

## 28094 (10472293073162, k_28h_utkast.json): GODKÄND

Live: en variant (RB25-0020), 7169 kr. Magnesium, fälgar och vevparti i aluminium, 22 cm, ca 95–110 cm, 1 växel och V-broms stämmer. Att cykeln kan göras om till springcykel och tillbaka utan verktyg står ordagrant i källan. Det är en funktion och inget utvecklings- eller säkerhetspåstående. Det står med 'enligt tillverkaren' en gång i löptexten och en gång för längden (2, R5), och specifikationsraden upprepar faktumet utan ny formulering. Modellnamnet Royal Space Shark följer live-titeln. En sökträff på velomarket.ee visar 'Tabou Royal Space Shark' 14 tum, och SKU-prefixet RB pekar på RoyalBaby. Ingen rättning.

## 28095 (10472293892362, k_28h_utkast.json): GODKÄND

Live: en variant (TAB25-8470), 6969 kr. 'Rammaterial: 28 cm' tolkas rätt som ramstorlek. Ram: aluminium står separat, och värdet följer Tabou-mönstret med förarlängd. Webbkoll: smartech.ee, där sidan har SKU TAB25-8470 i titeln ('Children's bicycle TABOU Queen 20, white-mint (TAB25-8470)'), anger enligt sökträffen 'Frame size: 28 cm, suitable for a rider with a height of approx. 115-130 cm'. Sidan gav 403 när den öppnades. Sänkt aluminiumram, Shimano Tourney, 6 växlar, 12 kg, stänkskärmar, kedjeskydd och pakethållare (medföljande, ingen last) stämmer. Ljusen är rätt utelämnade. Ingen rättning.

## 28096 (10472294351114, k_28h_utkast.json): GODKÄND

Live: en variant (BOB-B371C), 7289 kr. Stål, läderdetaljer, 4–6 år och 105–125 cm (var sin gång 'enligt tillverkaren', 2) samt korg, stänkskärmar, kedjeskydd, klocka och stödhjul (medföljande) stämmer. Raden 'Storlek: 105 cm - 105 cm', hjulvikten och 'perfekt' är rätt utelämnade. Ingen rättning.
