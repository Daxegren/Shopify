# Granskning våg 2, utkast a_1 och a_5 – BEST OF SPORTS (2026-11-01)

Oberoende granskning. Inget har skrivits till Shopify och inga utkastfiler har ändrats. Butiken kontrollerades först med get-shop-info: **BEST OF SPORTS** (bestofsports.se, SEK).

**Underlag:** `vag2_skriv/a_1_utkast.json` (15 produkter, nr 2101–2115) och `vag2_skriv/a_5_utkast.json` (12 produkter, nr 2501–2515 utom 2507, 2510 och 2512). Läst: `CLAUDE.md`, `produkttexter-standard.md` (särskilt avsnitt 10), `LARDOMAR.md` och `verifiering_vag1_rattning.md`.

**Metod:**
- Källan lästes live med `graphql_query` (`nodes`: title, status, vendor, productType, tags, descriptionHtml, variants) i fyra batchar (8 + 8 + 8 + 3). Alla 27 är ACTIVE.
- Fältet `fakta` jämfördes för hand mot live-texten. Det stämmer för alla 27: inget i `fakta` saknas live, och inget live-innehåll som påverkar texten saknas i `fakta`. I `fakta` är vissa trasiga eller reklamartade stycken förkortade (märkestexter för Spokey och Zipro), men ingen uppgift som används i utkasten kommer från något som inte finns live.
- Med skript kontrollerades längder, kommatecken, enheter, tankstreck, stor bokstav efter kolon, dubbletter i alla fem a-filerna och standardblocket. Faktaspårbarhet, språk och säkerhet bedömdes för hand.

## Sammanfattning

| Bedömning | Antal | Nr |
|---|---|---|
| GODKÄND | 9 | 2101, 2102, 2103, 2104, 2106, 2113, 2114, 2508, 2511 |
| GODKÄND MED SMÅ RÄTTNING | 6 | 2107, 2108, 2109, 2110, 2111, 2509 |
| UNDERKÄND | 12 | 2105, 2112, 2115, 2501, 2502, 2503, 2504, 2505, 2506, 2513, 2514, 2515 |

Inget påhittat tal, ursprung, material eller hälsopåstående hittades. Hälso-, kalori-, skade- och rehabpåståenden i källorna (2101, 2102, 2113, 2114, 2115, 2502, 2514) är utelämnade som de ska. Alla 12 underkännanden gäller säkerhet, barnprodukter, belastning, låsta varianter eller oklar produkttyp. Inget av dem beror på påhittad fakta.

## Fynd som gäller hela leveransen

1. **Kontrollskriptet har aldrig läst beskrivningarna.** `kontrollera_produkttext.py` läser brödtexten bara från fälten `beskrivning`, `body` eller `beskrivning_efter`. Utkasten använder `html`. "0 FEL, 0 VARNINGAR" gäller därför bara titel, SEO-titel och meta. Jag körde om skriptet med fältet döpt till `beskrivning` på en kopia i scratchpad:
   - **Med standardblocket:** 147 FEL (a_1) och 118 FEL (a_5). Alla kommer från standardblocket (org.nr, postnummer, "30 dagar", "godkänd reklamation"), eftersom blocket saknar markeringen `[[STANDARDBLOCK]] … [[/STANDARDBLOCK]]` som skriptet använder för att hoppa över det.
   - **Utan standardblocket:** 0 FEL i båda filerna. Varningarna gäller bara att rubriken heter "Passar för" och inte "Passar dig som", korta texter (2108, 2109, 2110, 2111, 2505, 2515) och att 2515 saknar specifikationer.
   - **Slutsats:** alla tal i beskrivningarna går att spåra. Byggskriptet bör dock mappa `html` → `beskrivning` och lägga in markeringen för standardblocket, annars kontrolleras aldrig brödtexten automatiskt.
2. **Standardblocket** är samma text som i våg 1 (114 förekomster i `vag1_skriv`), har ingen fraktavgift i kronor och har meningen om beställningsvara på 2112 (taggen "På beställning"). Korrekt.
3. **Dubbla SEO-titlar mellan filerna** (missas när varje fil kontrolleras för sig):
   - "Träningshandskar Trec #02 Gel Shock" används av 2107 (a_1), 2212 (a_2) och 2509 (a_5).
   - "Rullskridskor Fila Legacy Pro 80" används av 2415 (a_4) och 2502 (a_5).
4. **Formregler:** alla titlar har högst 70 tecken och högst 2 kommatecken. Alla SEO-titlar har högst 43 tecken. Meta är 133–154 tecken eller null (2110, 2111, 2508, 2511, 2515: tunn källa). Enheterna står med gemener (ml, oz, cm, mm, kg, g). Intervallen har tankstreck (11–14 kg, 21,5–24 cm). Det är stor bokstav efter kolon i alla specifikationer. Beskrivande ord har versal i titlar och SEO-titlar, och småorden (i, för, och) står med gemen.

## Titeländringar (live → utkast)

| Nr | Live-titel | Utkastets titel |
|---|---|---|
| 2101 | Stretch rubber TUNTURI Textile blue | Stretchband Tunturi i Textil, Latexfritt, Blå |
| 2102 | Sensorisk träningsmatta SPOKEY Rose Eco, beige | Sensorisk Träningsmatta Spokey Rose Eco, Beige |
| 2103 | Yogamatta SPOKEY Mandala, lila | Yogamatta Spokey Mandala, 183 x 61 cm, Lila |
| 2104 | Gymnastikboll ZIPRO Anti-Burst Gymnastics Ball 65cm, svart | Gymnastikboll Zipro, 65 cm, Svart |
| 2105 | 4in1 (rullskridskor) NILS EXTREME NH18192, rosa-mint, L | Rullskridskor Nils Extreme NH18192 4in1, Rosa och Mint, L |
| 2106 | Träningshandskar TREC #06 / GLOVES YELLOW (Power Max) XL | Träningshandskar Trec #06 Power Max, Gul, XL |
| 2107 | Träningshandskar TREC #02 / GLOVES GEL SHOCK RED XL | Träningshandskar Trec #02 Gel Shock, Röd, XL |
| 2108 | Gym talk TREC CHALK - LIQUID, 100ml | Gymtalk Trec Liquid Chalk, 100 ml |
| 2109 | Gym talk TREC CHALK - BLOCK 57g | Gymtalk Trec Chalk Block, 57 g |
| 2110 | Boxningshandskar TOORX Leopard Boxing Gloves 12oz | Boxningshandskar Toorx Leopard, 12 oz, Polyuretan |
| 2111 | Boxningshandskar TOORX Panther Boxing Gloves 12oz | Boxningshandskar Toorx Panther, 12 oz, Polyuretan |
| 2112 | Training stand ELITE Roller Arion | Träningsrulle för Cykel Elite Arion, Hopfällbar |
| 2113 | Gymnastikboll ZIPRO Peanut 45cm, grön | Gymnastikboll Zipro Peanut, 45 cm, Grön |
| 2114 | Massage roller SPOKEY Tausa, kork | Massagerulle Spokey Tausa, Kork |
| 2115 | Trampoline HAMMER JumpStep | Trampolin Hammer JumpStep |
| 2501 | Rullskridskor LEGACY PRO 84 LADY, svart-blå | Rullskridskor Fila Legacy Pro 84 Lady, Svart och Blå |
| 2502 | Rullskridskor LEGACY PRO 80 | Rullskridskor Fila Legacy Pro 80 för Vuxna |
| 2503 | Rullskridskor LEGACY PRO 84, svart-grå | Rullskridskor Fila Legacy Pro 84, Svart och Grå |
| 2504 | Beach rackets Frozen, purple | Strandracketar Seven Polska Frozen, Lila |
| 2505 | Flying saucer Frozen, purple | Flygande Disc Seven Polska Frozen, Lila |
| 2506 | Beach rackets Spiderman | Strandracketar Seven Polska Spiderman |
| 2508 | Träningshandskar TREC #24 / DAMHANDSKAR GRÅ S | Träningshandskar Trec #24 för Dam, Grå, Storlek S |
| 2509 | Träningshandskar TREC #02 GLOVES GEL SHOCK SVART L | Träningshandskar Trec #02 Gel Shock, Svart, Storlek L |
| 2511 | Träningshandskar TREC #23 / Damhandskar VIT XS | Träningshandskar Trec #23 för Dam, Vit, Storlek XS |
| 2513 | Rullskridskor FILA Argon 84 Lady, Svart/Magenta | Rullskridskor Fila Argon 84 Lady, Svart och Magenta |
| 2514 | Rullskridskor FILA Legacy Pro 80 Lady, Svart/Violett | Rullskridskor Fila Legacy Pro 80 Lady, Svart och Violett |
| 2515 | Boxningssäck TOORX Fastball för WBX-70 | Boxningssäck Toorx Fastball för WBX-70 |

Ändringar som är mer än versaler och översättning:
- **2101:** modellnamnet "Textile" har blivit materialet "i Textil". Skribenten är själv osäker (`att_bekrafta`).
- **2104:** "Anti-Burst" är borttaget. Det följer avsnitt 10 (säkerhetslöfte utan entydig källa) men ändrar produktnamnet.
- **2102, 2103, 2110, 2111, 2112:** "Eco" behålls. Mått, material och "Hopfällbar" är tillagda ur källan.
- **2502:** "för Vuxna" är tillagt ur källan.
- **2508, 2509, 2511:** "Storlek" är tillagt framför storleken. 2106 och 2107 skriver bara "XL", så formatet är inte enhetligt. Det är inget fel, men det bör bestämmas.

Ingen agent har bytt produkttyp för att komma förbi en kontroll. "Massagerulle" (2114) är tillåtet som produktnamn enligt avsnitt 10.

## Per produkt

### GODKÄND

**2101 Stretchband Tunturi i Textil, Latexfritt, Blå** (10411606081802)
- Alla uppgifter finns i källan: mått, motstånd 11–14 kg, 40 g, 70/30 polyester/bomull, silikonribbor och tvätt i 30 grader. "Mindre muskler" står som "enligt tillverkaren". Påståendena om hållning och skaderisk är utelämnade.
- Notering: "Tunturi Textile är ett blått stretchband i textil" upprepar ordet. Måttet 32 cm och frågan om modellnamnet ligger redan under "att bekräfta".

**2102 Sensorisk Träningsmatta Spokey Rose Eco, Beige** (10411669750026)
- Spårbart. Den motstridiga tjockleken, "riskli" och påståendena om massage och cirkulation är utelämnade.
- Notering: punkterna under "Passar för" upprepar bara specifikationerna ("Dig som vill ha en vikbar matta"). Det är tunt, men inget fel.

**2103 Yogamatta Spokey Mandala, 183 x 61 cm, Lila** (10411858362634)
- Spårbart. Egenskaperna står som "enligt tillverkaren", och den trasiga upprepningen i källan är utelämnad.

**2104 Gymnastikboll Zipro, 65 cm, Svart** (10461406232842)
- Spårbart. Den trasiga raden i källan ("Färg: 65 cm") är ignorerad, och färgen stämmer med varianten "black".
- Notering: "träna balans, koordination och styrka …, enligt tillverkaren" är ett prestandapåstående. Det är godtagbart med "enligt tillverkaren". Att "Anti-Burst" tagits bort ur namnet går till David via "att bekräfta".

**2106 Träningshandskar Trec #06 Power Max, Gul, XL** (10462769840394)
- Spårbart. "Maximalt skydd" och "extra robusta" är utelämnade. "Extra vaddering vid handleden" står i källan.

**2113 Gymnastikboll Zipro Peanut, 45 cm, Grön** (10470898860298)
- Spårbart. Alla påståenden om rehab, skador, smärta och "fri från skadliga ämnen" är utelämnade. Texten riktar sig inte till barn.

**2114 Massagerulle Spokey Tausa, Kork** (10470907805962)
- Spårbart. Påståendena om effekt och allergi är utelämnade, och de trasiga raderna om material är utelämnade.
- Notering: "håller sig ren längre" är en jämförelse utan referens, men den står ordagrant i källan och som "enligt tillverkaren".

**2508 Träningshandskar Trec #24 för Dam, Grå, Storlek S** (10588446523658)
- Spårbart. Ingen meta (tunn källa), vilket är korrekt.
- Notering: samma SKU (2876) som nr 2510 ligger redan under "att bekräfta". Punkten under "Passar för" upprepar specifikationen.

**2511 Träningshandskar Trec #23 för Dam, Vit, Storlek XS** (10588446687498)
- Spårbart. Ingen meta.
- Notering: 2508 stryker "multisydd" som obegripligt, medan 2511 behåller "multisömmar". Det är begripligt, men de två texterna är inte enhetliga.

### GODKÄND MED SMÅ RÄTTNING

**2107 Träningshandskar Trec #02 Gel Shock, Röd, XL** (10462769905930)
- SEO-titeln är densamma som för 2212 och 2509.
  - Före: `Träningshandskar Trec #02 Gel Shock`
  - Efter: `Träningshandskar Trec #02 Gel Shock, Röd` (40 tecken)
- I övrigt är texten spårbar. Skyddspåståendet ("skydda händerna från skador") är utelämnat.

**2108 Gymtalk Trec Liquid Chalk, 100 ml** (10462775017738)
- Genus: SAOL böjer "talk" som en-ord (talken). "Ett flytande gymtalk" bör därför vara "en flytande gymtalk". Behåller David ordet "gymtalk" rättas artiklarna:
  - Meta före: `Trec Liquid Chalk är ett flytande gymtalk på 100 ml i en förpackning som är lätt att dosera. Enligt tillverkaren torkar det snabbt och absorberar fukt.`
  - Meta efter: `Trec Liquid Chalk är en flytande gymtalk på 100 ml i en förpackning som är lätt att dosera. Enligt tillverkaren torkar den snabbt och absorberar fukt.` (150 tecken)
  - Html före: `Trec Liquid Chalk är ett flytande gymtalk i en förpackning på 100 ml.`
  - Html efter: `Trec Liquid Chalk är en flytande gymtalk i en förpackning på 100 ml.`
- Ordval: `<li>Förpackning: Enkel att dosera</li>` säger att förpackningen doseras. Efter: `<li>Förpackning: Gör produkten enkel att dosera</li>`.
- Den svenska benämningen (gymtalk, magnesium eller krita) ligger redan under "att bekräfta".

**2109 Gymtalk Trec Chalk Block, 57 g** (10462775116042)
- Samma genus som för 2108, för att texterna ska vara enhetliga. Källan skriver själv "talket", så David kan välja form, men de två produkterna bör skrivas lika.
  - Meta före: `… Enligt tillverkaren torkar talket snabbt mot huden …`
  - Meta efter: `… Enligt tillverkaren torkar talken snabbt mot huden …`
  - Html före: `Enligt tillverkaren torkar talket snabbt vid kontakt med huden`
  - Html efter: `Enligt tillverkaren torkar talken snabbt vid kontakt med huden`

**2110 Boxningshandskar Toorx Leopard, 12 oz, Polyuretan** (10468720378122)
- Den engelska modellbeteckningen ger en cirkulär mening ("Boxing Gloves är boxningshandskar"), och punkten under "Passar för" upprepar meningen. Vid tunn källa gäller kort intro.
  - Före: `<p>Toorx Leopard Boxing Gloves är boxningshandskar i polyuretan, storlek 12 oz.</p><h2>Passar för</h2><ul><li>Dig som vill ha boxningshandskar i polyuretan i storlek 12 oz</li></ul>`
  - Efter: `<p>Toorx Leopard är boxningshandskar i polyuretan, storlek 12 oz.</p>`
  - Specifikationerna och standardblocket behålls.

**2111 Boxningshandskar Toorx Panther, 12 oz, Polyuretan** (10468720476426)
- Samma rättning som för 2110.
  - Före: `<p>Toorx Panther Boxing Gloves är boxningshandskar i polyuretan, storlek 12 oz.</p><h2>Passar för</h2><ul><li>Dig som vill ha boxningshandskar i polyuretan i storlek 12 oz</li></ul>`
  - Efter: `<p>Toorx Panther är boxningshandskar i polyuretan, storlek 12 oz.</p>`

**2509 Träningshandskar Trec #02 Gel Shock, Svart, Storlek L** (10588446556426)
- SEO-titeln är densamma som för 2107 och 2212. 2212 är Svart XL, så färgen räcker inte för att skilja dem åt.
  - Före: `Träningshandskar Trec #02 Gel Shock`
  - Efter: `Träningshandskar Trec #02 Gel Shock Svart L` (43 tecken)
  - Rekommendation utanför uppdraget: 2212 får `Träningshandskar Trec #02 Gel Shock, XL` (39 tecken) eller motsvarande.
- Notering: punkten "Träning med hantlar och kettlebells" saknar "enligt tillverkaren", vilket 2107 har för samma källtext. Det är inget fel, men texterna är inte enhetliga.

### UNDERKÄND

**2105 Rullskridskor Nils Extreme NH18192 4in1** (10462176936202)
- **Skäl:** rullskridskor (säkerhet) och en motsägelse om vad som säljs.
  - Källan beskriver ett 4-i-1-set med skridskoblad i rostfritt stål och tre hjulkonfigurationer. Utkastet beskriver bara rullskridskor och säger inget om bladet.
  - Det är oklart om "L" och "innerdiameter 21,5–24 cm" anger storleken.
  - "Stövel: Halvmjuk, EVA och tät skumplast" kopplar källans rad "Innehåll" till stöveln, vilket är en tolkning.
- Tas för hand.

**2112 Träningsrulle för Cykel Elite Arion, Hopfällbar** (10468721983754)
- **Skäl:** produkten bär belastning. Källan anger maximal last 115 kg (hjul plus cyklist), och utkastet har strukit uppgiften. Rullar är en fallrisk, så uppgiften behövs, och den ska bekräftas av en människa.
- **Felöversättning i meta:** `… och har ett justerbart framhjul.` Rullen har inget framhjul. Källan säger att framhjulet (cykelns hjulplats på rullen) kan justeras i 10 lägen. Förslag vid handläggning: `Elite Arion är en hopfällbar träningsrulle för cykelträning hemma. Rullen passar landsvägs- och mountainbikes, och framhjulet kan justeras i 10 lägen.` (150 tecken)
- Specifikationen "Tillägg: Sensorn Misuro B+ …" kan läsas som att sensorn ingår, vilket inte framgår av källan.
- Produkten kostar 5 439 kr och är en beställningsvara. Tas för hand.

**2115 Trampolin Hammer JumpStep** (10470945816842)
- **Skäl:** belastning (maximal användarvikt 150 kg, struken) och fyra motstridiga mått i källan. Utkastet utelämnar korrekt måtten, men en trampolin utan uppgift om användarvikt bör inte publiceras utan beslut.
- Tas för hand.

**2501 Rullskridskor Fila Legacy Pro 84 Lady, Svart och Blå** (10494939627786)
- **Skäl:** rullskridskor (säkerhet, broms). Dessutom låser titeln färgen "Svart och Blå", medan den enda varianten heter "38 / black". Det strider mot variantregeln i avsnitt 10. Skribenten skriver att färgen inte är med, men den står i titeln.
- **Språk och fakta:**
  - Specifikationen "Hjul och lager: Robusta" är ett omdöme, inte en uppgift.
  - "Dig som vill ha rullskridskor som anpassar sig efter fotens form" är ett påstående från tillverkaren utan "enligt tillverkaren".
  - Meta säger "justerbara" utan att säga vad som justeras.

**2502 Rullskridskor Fila Legacy Pro 80 för Vuxna** (10494939660554)
- **Skäl:** rullskridskor (säkerhet). SEO-titeln är densamma som för 2415. Föreslagen SEO-titel: `Rullskridskor Fila Legacy Pro 80 för Vuxna` (42 tecken).
- **Språk och fakta:**
  - "Skal: Lätt men hållbart" och "Hjul och lager: Robusta" är omdömen.
  - "Dig som är vuxen och vill ha rullskridskor i unisexmodell" är klumpigt.
  - Källans "Färg: Svart, Blå" och "Svarta Rullskridskor" motsäger varandra. Det ligger redan under "att bekräfta".

**2503 Rullskridskor Fila Legacy Pro 84, Svart och Grå** (10494941495562)
- **Skäl:** rullskridskor (säkerhet). Två varianter med olika pris ("Default Title" 2 589 kr och "44 / black" 2 249 kr), och titeln låser färgen "Svart och Grå" mot varianten "black". Det strider mot avsnitt 10.
- Brödtexten är nästan identisk med 2501.

**2504 Strandracketar Seven Polska Frozen, Lila** (10541367263498)
- **Skäl:** barnprodukt (Disney-motiv), som ska tas för hand enligt avsnitt 10. Uppgift om ålder och leksaksmärkning saknas i källan.
- **Språk:**
  - "ett set med strandracketar med Disney-figurer" har dubbla "med".
  - Meta "två plastracketar och en liten boll med Disney-figurer" kan läsas som att bara bollen har motiv.
  - "SevenPolska" (butikens märke) skrivs "Seven Polska". Det ligger redan under "att bekräfta".

**2505 Flygande Disc Seven Polska Frozen, Lila** (10541367492874)
- **Skäl:** barnprodukt. Typordet "Disc" är engelska (standarden förbjuder engelska typord). En svensk benämning (kastdisc, frisbee eller flygande tallrik) behöver beslutas.

**2506 Strandracketar Seven Polska Spiderman** (10541367656714)
- **Skäl:** barnprodukt. Källan kallar Spider-Man en Disney-figur, och texten skriver det vidare ("Motiv: Disney-figurer"). Det är en tveksam uppgift om ett licensierat varumärke, och den officiella stavningen är "Spider-Man".

**2513 Rullskridskor Fila Argon 84 Lady, Svart och Magenta** (10588451897610)
- **Skäl:** rullskridskor (säkerhet, broms). Åtta varianter med två priser (2 669 och 2 319 kr), två varianter delar SKU 010621215-37-5, och titeln låser färgen "Svart och Magenta" mot varianterna "black". Det strider mot avsnitt 10.
- **Språk:** "medelgoda åkare" är ett ovanligt ordval. Förslag: "medelvana åkare".

**2514 Rullskridskor Fila Legacy Pro 80 Lady, Svart och Violett** (10588451930378)
- **Skäl:** rullskridskor (säkerhet). Fyra storleksvarianter "black", och titeln låser färgen "Svart och Violett".
- **Språk:**
  - "lätta promenader" är en felöversättning. Man promenerar inte på rullskridskor. Förslag: "lugn åkning".
  - "lätta … lätta … lätt" upprepas i meta och första stycket.
  - Meta säger "aluminiumram", medan specifikationen säger "Ram: 6000-serie aluminium". Det är förenligt.

**2515 Boxningssäck Toorx Fastball för WBX-70** (10624084148490)
- **Skäl:** produkttypen är oklar.
  - SKU:n KIT-PALLAWBX-70 tyder på ett bollkit ("palla" = boll) till WBX-70, inte en boxningssäck. Ändå påstår texten att produkten "är en boxningssäck för WBX-70".
  - Källan är bara titeln, och texten är cirkulär (7 ord).
- Samma behandling som stepbrädan i `handhavd_ids.txt` ("produkttyp oklar"). Produkten kostar 1 709 kr. Tas för hand efter datablad.

## Rekommendationer till nästa steg (inget är genomfört)
1. Låt byggskriptet skicka `html` som `beskrivning` till `kontrollera_produkttext.py` och lägga in markeringen för standardblocket. Annars kontrolleras aldrig brödtexten.
2. Kör dubblettkontrollen på hela vågen (a_1–a_5 tillsammans), inte per fil.
3. Lägg till de 12 underkända i `handhavd_ids.txt` (rullskridskor, barnprodukter, belastning och oklar typ) efter Davids beslut.
4. Rullskridskor finns inte uttryckligen i listan över säkerhetsprodukter i avsnitt 10. David bör avgöra om de ska läggas till som ett nytt stycke i standarden. Befintlig text ändras inte.
