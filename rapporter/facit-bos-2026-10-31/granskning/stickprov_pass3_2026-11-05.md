# Stickprov pass 3, BEST OF SPORTS, 2026-11-05

Roll: Stickprov (Sonnet, endast läsning). Inget skrevs i Shopify.
Skrivfiler: k_skriv_18a.json (5), k_skriv_19abc.json (6), k_skriv_19de.json (8), k_skriv_19f20.json (14). Totalt 33 av 33 produkter lästa live (alla fanns, alla status ACTIVE).

## 1. Jämförelse live mot skrivfil (tecken för tecken)

Live lästes med `shopify_api.hamta_produkter` (fält: title, handle, status, tags, seo.title, seo.description, descriptionHtml) och jämfördes med `shopify-sync/scripts/jamfor_live.py` (seo.title null räknas lika med title).

| Fil | Jämförda | Avvikelser |
|---|---|---|
| k_skriv_18a | 5 av 5 | 0 |
| k_skriv_19abc | 6 av 6 | 0 |
| k_skriv_19de | 8 av 8 | 0 |
| k_skriv_19f20 | 14 av 14 | 0 |

Resultat: 33 av 33 identiska i title, seo.title, seo.description och descriptionHtml. Inga osynliga tecken. Taggen `texter-klara` finns på alla 33 (skriptet gav inget "obs"). Egen kontroll: ingen titel har tre eller fler kommatecken (högst 2, och där räknas decimalkomma, t.ex. "60,5"), ingen text har fler än två "enligt tillverkaren" (högst 2 i brödtext plus meta), inga dubbla mellanslag.

## 2. Språkgranskning och risker

Allvarlighet: A = bör rättas/avgöras före publik trafik, B = bör rättas, C = smaklig anmärkning.

### Hälso- och säkerhetspåståenden

- **20037 Upphängning Boxningssäck Excalibur (A, hängande del).** Spec: "Maximal belastning enligt tillverkaren: 75 kg" (attribuerat). Brödtexten innehåller dessutom en monteringsinstruktion utan attribuering: "Har säcken bara tre hängande öglor kan en av kedjorna lossas från den övre karbinhaken." Det är en säkerhetsrelevant anvisning som inte står som tillverkarens uppgift. Rekommendation: kontrollera mot källa eller ta bort.
- **20040 Väggfäste Upphängning Excalibur Boxningssäck (A, hängande del).** Spec: "Maximal belastning enligt tillverkaren: 75 kg". Exakt samma siffra som 20037 (kedja). Kan vara kopierat; verifiera mot källa. Texten säger inget om vilket väggmaterial fästet tål, vilket är bra (inget påstående), men "Dig som inte kan hänga en boxningssäck i taket" bör inte läsas som monteringsråd.
- **20054 Plyobox i Tall och Poppel (A).** "Maximal lastkapacitet: 500 kg (enligt tillverkaren)". 500 kg för en plywoodbox är ovanligt högt jämfört med 20057 (plywood, 200 kg) och 20055 (metall, 300 kg). Attribuerat, men verifiera siffran mot källa.
- **20057 Plyobox i plywood med handtag (B).** "Maximal lastkapacitet: 200 kg (enligt tillverkaren)". Attribuerat.
- **20055 Plyo Box Justerbar i Metall (B).** "maxbelastning 300 kg enligt tillverkaren" (i meta) och "Maxbelastning: 300 kg (enligt tillverkaren)". Attribuerat. Texten säger inget om att justerbara höjder måste låsas; bra att den inte hittar på det.
- **20041 Stående Boxningssäck Body Opponent Bag (A).** Spec: "Träningsyta: Ett område på 150 cm i alla riktningar från kanten av stativet rekommenderas" saknar attribuering (vem rekommenderar?). Säkerhetsrelaterat. Lägg till "enligt tillverkaren" eller ta bort. Dessutom: "Fylls det svarta bottenstativet ... väger säcken runt 130 kg" (färgen "svarta" syns inte i spec).
- **20027 Stabilitetspaket (B).** "maxbelastning 220 kg enligt tillverkaren" (balanskudde) och "maxbelastning 120 kg enligt tillverkaren" (balansplatta). Attribuerat; exakt två "enligt tillverkaren", ingen marginal kvar.
- **20032 Yogapaket (A).** "Material ftalatfritt skum av nitrilgummi och PVC" är ett hälso-/miljöpåstående utan attribuering och utan "enligt tillverkaren". Ta bort "ftalatfritt" eller attribuera (men det ger då tre "enligt tillverkaren"; bryter gränsen på två). Maxbelastning "150 kg" (block) och "500 kg" (boll) är attribuerade och gör redan två.
- **5256, 8070, 8071, 8072 Dricksflaska Giant ARX (B).** "Dricksflaskan har enligt tillverkaren antimikrobiell teknologi som håller vattnet fräscht." Hygienpåstående, attribuerat, men "håller vattnet fräscht" är ett effektpåstående. Överväg att stryka "som håller vattnet fräscht". Exakt två "enligt tillverkaren" per produkt.
- **20006 Gymnastikboll Spokey Fitball III (C).** "Dig som vill kunna använda bollen som stol hemma eller på kontoret enligt tillverkaren" och meta "kan enligt tillverkaren användas som stol". Ergonomi-/användningspåstående, attribuerat. Två "enligt tillverkaren" (en i brödtext, en i meta). Bruksanvisning/maxlast saknas, vilket är rätt.
- **El-lastcyklar som bär barn (21062, 21065, 21066, 21067, 21072, 18005):** inget påstående om barn, säten, barnsäkerhet eller transport av personer i någon av texterna. Detta är rätt. Två anmärkningar:
  - **21066 El-lastcykel Cargobike of Sweden Flex Box (B).** "Dig som behöver en lastcykel för företag eller familj" antyder familjetransport (barn) utan stöd i spec. Rekommendation: stryk "eller familj" eller verifiera mot källa.
  - **21065 Delight Box:** "Lådan har inga säten och högre kanter än övriga modeller" jämför mot oangivna "övriga modeller" och bör förtydligas (eller strykas). Inget barnpåstående.
- Lastcyklarnas siffror "100 kg (lastlåda) + 100 kg (förare)" (21065, 21066, 21067) och elcykel 21063/21068 "Upp till 130 km och 120 kg" är attribuerade med "enligt tillverkaren". Två "enligt tillverkaren" per produkt, men samlingsraden "Motor, batteri och bromsar: ... enligt tillverkaren" gör att attribueringen också kan läsas som att motorn/batteriet bara är påstådda; oklar räckvidd för attribueringen.
- 20058 Tower 2000: dörrkrav "Dörr: Minst 56 cm bred och 175 cm hög / Maximal dörrtjocklek: 4,5 cm" är monteringsvillkor utan attribuering (B). Verifiera mot källa.

### Stavning, grammatik och bindestreck

Kontrollerat "gjord/gjort": alla stämmer med ordets genus (20025 "gjord av PVC", 20035 "gjord av kork", 20036 "gjort av kork", 20040 "gjort av stål", 20054 och 20057 "gjord av"). Inga stavfel hittades i brödtext. Anmärkningar:

- **20037 (B), singular/plural:** "Kedjan till boxningssäcken har en vridbar krok och 13 kedjelänkar på vardera kedja." Singular "Kedjan" men "vardera kedja"/"En av kedjorna" och meta "Varje kedja". Oklart om det är en eller flera kedjor. Föreslagen riktning: "Kedjorna ... på vardera kedjan". Meta "Upphängningen till boxningssäck har" saknar artikel ("till en boxningssäck").
- **20058 (B), inkonsekvent böjning:** "grå, svarta eller röda" men spec "Motstånd, gråa band". Använd en form ("grå band" eller "gråa band" genomgående).
- **20024 (B) och 21069, 21070, 21071 (B), "i setet":** "I setet ingår stöd, stänkskärmar ..." (cykel) och "sadel med ryggstöd i setet" (trehjuliga). Ordet "set" passar inte för en cykel och är oklart; använd "Ingår" / "ingår i leveransen".
- **20061 (C), terminologi:** "vikbara tubeless-däck" i Passar-för men "slanglösa" i spec; 20060 använder "slanglösa". Använd ett ord.
- **20060 vs 20061 (C):** 20060 "stickaxlar" (Passar för), 20061 "genomgående axlar". Samma sak, två ord i syskonprodukter. Spec 20060: "stickaxel 12x142 mm", 20061: "genomgående axel 12x142 mm".
- **20060, 20061 (C), engelska kvar i spec:** "Advanced-grade composite", "Advanced SL-grade composite", "full-composite OverDrive Aero-styrrör". Passar-för-punkten "eftersom cykeln har fästpunkter för dem" (flaskhållare) saknar motsvarande specrad och kan inte styrkas av texten själv.
- **Inkonsekvent typ/stavning (C):**
  - "El-lastcykel" med bindestreck (21062, 21065, 21066, 21067, 21072) mot "Elcykel" (21063, 21068) och "Trehjulig Elcykel" (21069-21071). Ordet "elcykel" skrivs i ett, "ellastcykel" vore standardstavningen; bindestrecket i "El-lastcykel" är en variant som används av tillverkaren.
  - "Elcykel-fatbiken" / "elcykel-fatbike" (21063, 21068): ovanlig sammansättning med bindestreck; "elfatbike" eller "fatbike-elcykel" vore naturligare.
  - 20054/20057 "Plyobox" mot 20055 "Plyo Box" / "plyo boxen" / "Plyo Boxen" (versal "B" mitt i meningen: "Plyo Boxen är tillverkad av metall"). Föreslå "plyobox" överallt.
  - 20057 skriver "(poppel, tall)", 20054 "Tall och Poppel"/"tall och poppel": ordningen och versalerna skiljer.
  - 21065 "Minsta sadelhöjd", 21066 "Minsta sadelhöjd", 21067 "Lägsta sadelhöjd": olika etikett för samma mått.
  - 21063 "Räckvidd och lastkapacitet" mot 21068 "Räckvidd och maximal belastning": olika etikett i syskonprodukter.
  - Måttformat: "190x60" (20032), "22,5x15x7,5" (20036) mot "23,5 x 15 x 8 cm" (20049) och "L 23,5 x B 15 x H 8 cm"; blandat mellanslag kring "x".
- **20027 och 20032 (B), råa produktnamn i spec:** "Ingår: Gummiband Justerbara Tre färger, Gummibandspaket Korta 50 cm, Balanskudde Balansdyna 33 cm, Balansplatta Handtag 39,5 cm" och "Ingår: Träningsmatta Deluxe Yogamatta 190x60 cm, Yogablock GS, Fitnessboll Yogaboll Pilatesboll". Versaler mitt i raden och upprepade ord ("Balanskudde Balansdyna", "Fitnessboll Yogaboll Pilatesboll") ser ut som källnamn som klistrats in. Läsbarheten är låg.
- **20041 (B):** "säcken svänger ut av rekylen efter ett slag" är otydlig ("svänger ut" från vad? troligen "svänger tillbaka"). Verifiera.
- **20055 (C):** "fem höjder mellan 45 och 65 cm" upprepas två gånger med "mellan ... mellan" ("Dig som vill välja mellan fem höjder mellan 45 och 65 cm").
- **20035 (C):** metatexten är nästan identisk med brödtextens första stycke ("Den här yogamattan är gjord av kork och mäter 183x61x0,5 cm. Den väger 0,8 kg och kan användas till yoga och annan träning.") Samma mönster 20036. Det är ingen språkfel men duplicerat innehåll.
- **20036 (B, faktamisstanke):** Yogablocket i kork (22,5x15x7,5 cm) anges väga 0,8 kg, exakt samma som korkmattan 20035. Kan vara kopierat; verifiera mot källa.

### Meta utan verb

Alla 33 metatexter har minst ett verb (har, är, innehåller, rymmer, levereras, fylls, väger, mäter, används, bestäms m.fl.). Meta 20025 har en andra mening utan verb: "Längd 150 cm, diameter 30 cm." (C, fragment efter ett komplett första stycke; meta som helhet har verb). Metalängd 84 (20037) till 153 tecken, inga under 70.

### Titlar

Alla titlar har högst 2 kommatecken (decimalkomma inräknad). Titlar med 2 (inkl. decimalkomma): 5256, 8070, 8071, 8072, 20006, 20024, 20025, 20036, 20054, 21063, 21068. Ingen med 3 eller fler.

### Antal "enligt tillverkaren"

Högst 2 per produkt (brödtext plus meta). Inga som överskrider. Flera produkter står på exakt 2 och har därmed ingen marginal för att lägga till attribuering: 5256-serien, 20006, 20027, 20032, 21062-21068, 21072, 20055.

## 3. Begränsningar (öppet)

- Jag har bara jämfört live mot skrivfilen. Jag har inte jämfört mot leverantörens källor eller bilder, så faktasiffrorna (maxlaster, vikter, mått, räckvidd) är inte verifierade; jag pekar bara ut sådana jag finner misstänkta (20036 vikt, 20037/20040 identiska 75 kg, 20054 500 kg).
- Språkgranskningen är en manuell läsning av alla 33 texter (hela text före Leverans-avsnittet plus meta), inte ett stavningsprogram. Standardblocket "Leverans, retur och garanti" lästes inte för varje produkt; det jämfördes bara tecken för tecken mot skrivfilen.
- Handle och status jämfördes inte mot någon före-fil (ingen angavs). Alla status var ACTIVE vid läsningen.
- Taggar: kontrollerat endast att `texter-klara` finns, inte att övriga taggar är oförändrade.
- Tidpunkt: läst 2026-11-05; ändringar efter det syns inte.

## 4. Sammanfattning att agera på

0 avvikelser mot skrivfilen. Rättas/avgörs prioriterat: 20032 "ftalatfritt", 20041 oattribuerad träningsyta, 20037 oattribuerad monteringsanvisning, verifiera 20036 vikt, 20037/20040 75 kg, 20054 500 kg, 21066 "eller familj", 20058 grå/gråa, "i setet" (20024, 21069-21071), 20037 singular/plural.
