# Granskning våg 2, utkast a_2 – BEST OF SPORTS (2026-11-01)

Oberoende granskning. Jag har bara läst i Shopify och inte ändrat någon utkastsfil. Butiken kontrollerades först med get-shop-info: **BEST OF SPORTS** (bestofsports.se, SEK).

**Underlag:** `vag2_skriv/a_2_utkast.json` (15 poster, nr 2201–2215, varav 2202 och 2207 handhavda med html null). Standarden (`produkttexter-standard.md`, särskilt avsnitt 10), `LARDOMAR.md` och `verifiering_vag1_rattning.md`.

**Metod:**
- **Källan live:** title, status, vendor, productType, tags, descriptionHtml och variants hämtades med graphql_query (`nodes`) i två batchar, 8 och 7 produkter. Alla 15 är ACTIVE. Fältet `fakta` stämmer med live-källan för alla 15. Två skillnader: (a) 2210 har inte meningen om beställningsvara i beskrivningen live, men taggen "På beställning" finns, så det är rätt att den står i `fakta` och i standardblocket. (b) 2214 och 2215 har live en länk till tillverkarens datablad (elite-it.com, PDF). Länken finns inte i `fakta` och inte i utkastet, så informationen försvinner.
- **Maskinellt:** längder, antal kommatecken, standardblock (två varianter: normal och med beställningsmeningen, båda utan fraktavgift i kronor, och samma text i alla utkast), dubbletter av titel och SEO-titel i alla a_1–a_5. Jag körde `kontrollera_produkttext.py --seo-title-max 43` på kontrollfilen: 0 FEL och 19 VARNINGAR. Varningarna gäller att rubriken är "Passar för" (så heter den i alla godkända facit, alltså godtagbart) och fem korta texter. Not: körs skriptet direkt på `a_2_utkast.json` blir resultatet "0 FEL" utan att något har kontrollerats, eftersom fälten heter `titel` och inte `title`. Det är kontrollfilen som räknas.
- **För hand:** varje titel, SEO-titel, meta och html lästes mot live-källan och språkgranskades.

## Resultat i korthet

| Kategori | Antal | Nr |
|---|---|---|
| GODKÄND | 2 | 2208, 2210 |
| GODKÄND MED SMÅ RÄTTNING | 7 | 2204, 2205, 2206, 2209, 2211, 2212, 2213 |
| UNDERKÄND | 4 | 2201, 2203, 2214, 2215 |
| Handhavd (rätt undantagen) | 2 | 2202, 2207 |

Totalt 2 + 7 + 4 + 2 = 15.

## Regelkontroll (alla utkast med text)
- Titlar: 31–69 tecken och högst 2 kommatecken. 2214 har 69 tecken, alltså nära gränsen.
- SEO-titlar: 30–40 tecken (≤43). 2205 och 2208 har SEO-titel som är identisk med titeln (lagras tom, avsett beteende).
- Meta: 130–150 tecken där den finns. Null på 2203 och 2208 (tunn källa, enligt avsnitt 10).
- Enheter med gemener (mm, cm, kg, g, ml, oz) överallt. Inga "Ml", "Oz", "Mm" eller "Kg". Tankstreck i "5–8 arbetsdagar". Inga intervall med bindestreck. Inga kolon i titlarna.
- Versaler på beskrivande ord i titel och SEO-titel följs ("Svart och Grön", "i Kork", "Fristående").
- Inga omdömen, priser, ursprung eller märkeshistoria. Tunturis och Spokeys standardtexter om märket och Elites "40 år" har utelämnats. Hälsopåståendena i Spokey-källorna har utelämnats.
- **Dubblett:** SEO-titeln "Träningshandskar Trec #02 Gel Shock" på 2212 är identisk med 2107 (a_1) och 2509 (a_5). Det bryter mot regeln att SEO-titeln ska vara unik (se 2212).

## Per produkt

### 2201 – 10471232602378 – UNDERKÄND
- Live: "Rullskridskor FILA Houdini Pro, Svart/Vit". Utkast: "Rullskridskor Fila Houdini Pro, 3 x 110 mm Hjul".
- **Skäl:** rullskridskor ska tas för hand (säkerhetsprodukt enligt uppdraget). Dessutom har varianterna fel: "Default Title" har samma SKU (010620078-44) som "44 / black", och 44 har ett annat pris (3 059 kr mot 3 519 kr). Utkastskrivaren har själv flaggat båda.
- Titeländringar: FILA blir Fila, och "Svart/Vit" har tagits bort (varianterna säger bara "black"). Det är rimligt, men David behöver se det.
- Fakta i övrigt spårbar. "Förformad anatomisk vaddering **runt** anklarna" är en tolkning, eftersom källan säger "för att hålla anklarna … i rätt position". Ordföljden "3 x 110 mm Hjul" läses konstigt. Bättre: "Hjul 3 x 110 mm".

### 2202 – 10471310262538 – Handhavd (rätt)
Multi Gym Hammer Autark 9.0 har viktblock 2 x 80 kg och "Maximum operating weight 150 kg", och källan är på engelska. Det är rätt att produkten inte har fått något utkast.

### 2203 – 10472208564490 – UNDERKÄND
- Live: "TUNTURI Olympic Lock Jaw Collars, 50mm". Utkast: "Hantellås Tunturi Olympic Lock Jaw Collars, 50 mm".
- **Skäl:** hantellås finns på listan över produkter som tas för hand. Skrivaren flaggar det själv i `att_bekrafta` men har ändå skrivit ett utkast. Specifikationerna i källan är trasiga ("176 176 lb (1,5 m)", "4 mm Ø 50 gauge"). Utkastet har rätt bara tagit med 50 mm och 176 g.
- Om David ändå godkänner produkten: "Material: Syntetiskt" bör bli "Material: Syntetmaterial".

### 2204 – 10472238481674 – GODKÄND MED SMÅ RÄTTNING
- Live: "Massage roller SPOKEY 33x14cm black/green". Utkast: "Massagerulle Spokey Grean, 33 x 14 cm, Svart och Grön".
- **Titeländring:** modellnamnet "GREAN" (i källan) blir "Grean". David behöver bekräfta stavningen. "Massagerulle" är tillåtet som produktnamn (avsnitt 10).
- Mått och färg kommer från originaltiteln. Inga hälsopåståenden.
- Rättning (html, Passar för): före "Användning efter träning", efter "Efter träning". Punkten innehåller ett onödigt ord, eftersom raden ovan är "Uppvärmning före träning".

### 2205 – 10472242970890 – GODKÄND MED SMÅ RÄTTNING
- Live: "Massageboll SPOKEY Double Oak, kork". Utkast: "Massageboll Spokey Double Oak i Kork". SPOKEY blir Spokey, och ordföljden har ändrats.
- "Lätt och hållbar" står som "enligt tillverkaren", vilket är rätt. Hälsopåståendena och märkestexten har utelämnats.
- Rättning (html, Passar för): punkten "Dig som vill ha en massageboll i kork" är ett cirkelresonemang och tas bort. Kvar blir "Dig som vill ha en boll som får plats i en ryggsäck eller handväska".

### 2206 – 10472243069194 – GODKÄND MED SMÅ RÄTTNING
- Live: "Gymnastikmatta SPOKEY Home Jungle, flerfärgad". Utkast: "Gymnastikmatta Spokey Home Jungle, 183 x 61 cm, Flerfärgad".
- "Halkfri" och "fysioterapi" har rätt utelämnats.
- Rättning 1 (meta och första meningen i html): före "är en gymnastikmatta på 183 x 61 cm och 4 mm tjocklek.", efter "är en gymnastikmatta som mäter 183 x 61 cm och är 4 mm tjock." Meta blir då 150 tecken.
- Rättning 2 (Vanliga frågor): före "Enligt uppgifterna rengörs mattan för hand med en fuktig trasa.", efter "Mattan rengörs för hand med en fuktig trasa." "Enligt uppgifterna" är en arbetsterm (avsnitt 10).

### 2207 – 10472243298570 – Handhavd (rätt)
Fästet i tak eller vägg bär en tung säck. Materialraderna är trasiga, taggen "Cykelväska" är fel, och produktnamnet är oklart ("Gymnastikgummiband/boxningssäcksfäste"). Det är rätt att produkten inte har fått något utkast.

### 2208 – 10472245756170 – GODKÄND
- Live: "Yoga strap ZIPRO Yoga Strap, black". Utkast: "Yogarem Zipro Yoga Strap, Svart". Tunn källa, så texten består av en mening utan meta. Det följer regeln om tunn källa. "Yogarem" finns i källan.

### 2209 – 10472254603530 – GODKÄND MED SMÅ RÄTTNING
- Live: "Boxningshandskar Tunturi Allround Boxing Gloves 16oz". Utkast: "Boxningshandskar Tunturi Allround Boxing Gloves, 16 oz".
- Rättning (titel): före "Boxningshandskar Tunturi Allround Boxing Gloves, 16 oz", efter "Boxningshandskar Tunturi Allround, 16 oz, Konstläder" (52 tecken). Skäl: "Boxing Gloves" är ett engelskt typord som upprepar "Boxningshandskar", och den godkända facit-titeln för 14 oz-modellen (nr 414) har just den formen.
- Det är bra att "Storlek"-dubbleringen från nr 414 inte upprepas (raden heter "Mått"). Skyddslöftena har utelämnats. "Kardborre … stöd åt handleden" står ordagrant i källan och godtas.

### 2210 – 10472259813642 – GODKÄND
- Live: "Tunturi Fristående Boxningssäck". Utkast: "Boxningssäck Tunturi Fristående, 69 x 69 x 170 cm, Svart".
- Allt är spårbart (mått, vikt, PVC, sandfylld bas, nybörjare/avancerade, kampsporterna). Påståendena om skador, stress och leder har utelämnats. Standardblocket har meningen om beställningsvara, vilket stämmer med taggen. FAQ-svaret "Du fyller basen med sand." är tunt men korrekt.

### 2211 – 10472267645194 – GODKÄND MED SMÅ RÄTTNING
- Live: "Träningshandskar TREC #24 / HANDSKAR DAM GRÅ XS". Utkast: "Träningshandskar Trec #24 för Dam, Grå, XS".
- Rättning (meta): före "Insidan är förstärkt med läder och multisydd, utsidan och fingergapen är sydda med elastan.", efter "Insidan är förstärkt med läder och multisydd. Utsidan och fingergapen är sydda med elastan." Det är kommatecken mellan två huvudsatser. Meta blir 149 tecken.

### 2212 – 10472267677962 – GODKÄND MED SMÅ RÄTTNING
- Live: "Träningshandskar TREC #02 / HANDSKAR GEL SHOCK SVART XL". Utkast: "Träningshandskar Trec #02 Gel Shock, Svart, XL".
- Rättning 1 (SEO-titel, dubblett med 2107 och 2509): före "Träningshandskar Trec #02 Gel Shock", efter "Träningshandskar Trec Gel Shock, Svart, XL" (42 tecken). 2107 och 2509 behöver då också unika SEO-titlar, till exempel med färg och storlek.
- Rättning 2 (meta): före "Gelkuddar finns inuti och öglor mellan fingrarna.", efter "Inuti finns gelkuddar och mellan fingrarna sitter öglor." Meningen saknar verb för öglorna. Meta blir 145 tecken.
- Skyddslöftet om gelkuddarna har rätt utelämnats.

### 2213 – 10472270954762 – GODKÄND MED SMÅ RÄTTNING
- Live: "Gym talk TREC CHALK - LIQUID 250ml". Utkast: "Gymtalk Trec Liquid Chalk, Flytande, 250 ml".
- Rättning 1 (meta): före "Det passar styrketräning.", efter "Det passar för styrketräning." Meta blir 134 tecken.
- Rättning 2 (titel, upprepning): före "Gymtalk Trec Liquid Chalk, Flytande, 250 ml", efter "Gymtalk Trec Liquid Chalk, 250 ml". "Liquid" och "Flytande" säger samma sak. Titeln blir då samma som SEO-titeln och lagras tom. Rättningen är frivillig. Om "Flytande" ska behållas för sökbarhet är det godtagbart.
- Notera: källan skriver "talket" (neutrum), och utkastet följer det ("ett flytande gymtalk"). SAOL bör kontrolleras om "talk" är en- eller ett-ord. Det är ingen rättning nu.

### 2214 – 10472277639434 – UNDERKÄND
- Live: "Cykelträningsställ Elite Trainer Qubo Fluid". Utkast: "Cykelträningsställ Elite Trainer Qubo Fluid, Vätskebaserad Belastning".
- **Skäl:** cykelträningsställ ska tas för hand. Produkten bär en cyklist, och källan saknar max användarvikt (skrivaren flaggar det själv). Länken till databladet live tas bort utan ersättning. FAQ-svaret "Ja, enligt beskrivningen kan du använda cykelns egna växlar." innehåller arbetstermen "enligt beskrivningen".
- Om David godkänner: stryk "enligt beskrivningen" och behåll eller återinför länken till databladet.

### 2215 – 10472277737738 – UNDERKÄND
- Live: "Cykelträningsställ Elite Novo Force". Utkast: "Cykelträningsställ Elite Novo Force, 8-stegs Motstånd".
- **Skäl:** cykelträningsställ ska tas för hand. Källan har tillval med elektronik (Misuro B+, Bluetooth/ANT+), saknar max användarvikt och har motsägelsefulla effektuppgifter (690 W mot 760 W). Effekterna har rätt utelämnats. Även här tas länken till databladet bort.

## Alla rättningar (för rättaren)
1. 2204 html: "Användning efter träning" → "Efter träning".
2. 2205 html: ta bort punkten "Dig som vill ha en massageboll i kork".
3. 2206 meta och html: "är en gymnastikmatta på 183 x 61 cm och 4 mm tjocklek." → "är en gymnastikmatta som mäter 183 x 61 cm och är 4 mm tjock."
4. 2206 FAQ: "Enligt uppgifterna rengörs mattan för hand med en fuktig trasa." → "Mattan rengörs för hand med en fuktig trasa."
5. 2209 titel: "Boxningshandskar Tunturi Allround Boxing Gloves, 16 oz" → "Boxningshandskar Tunturi Allround, 16 oz, Konstläder".
6. 2211 meta: "…multisydd, utsidan och fingergapen…" → "…multisydd. Utsidan och fingergapen…".
7. 2212 SEO-titel: "Träningshandskar Trec #02 Gel Shock" → "Träningshandskar Trec Gel Shock, Svart, XL" (och unika SEO-titlar för 2107 och 2509).
8. 2212 meta: "Gelkuddar finns inuti och öglor mellan fingrarna." → "Inuti finns gelkuddar och mellan fingrarna sitter öglor."
9. 2213 meta: "Det passar styrketräning." → "Det passar för styrketräning."
10. 2213 titel (frivillig): "Gymtalk Trec Liquid Chalk, Flytande, 250 ml" → "Gymtalk Trec Liquid Chalk, 250 ml".

## Titeländringar som David ska se
Alla titlar i utkastet skiljer sig från live, eftersom typordet har översatts, märket skrivs i normal skrivning och färg eller mått har lagts till. Det som ändrar själva namnet:
- 2204: "GREAN" (källan) blir "Grean".
- 2201: "FILA" blir "Fila", och "Svart/Vit" tas bort.
- 2203, 2205, 2206, 2208, 2211, 2212, 2213: TUNTURI, SPOKEY, ZIPRO och TREC skrivs med normal skrivning.
- 2213: "CHALK - LIQUID" blir "Liquid Chalk".
- 2214: "Trainer" behålls i titeln men inte i SEO-titeln eller texten.
