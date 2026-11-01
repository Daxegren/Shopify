# Skrivrapport våg 1b – BEST OF SPORTS (2026-11-01)

Butiken kontrollerad med get-shop-info: BEST OF SPORTS (bestofsports.se). Inget committat.

## Sammanfattning
- 18 produkter skrivna (16 ur våg 1 + 2 pilotprodukter), 0 userErrors. Kanarie: 401, därefter batch om 8, batch om 8 och 1 sista (Kettlebell).
- Statuskontroll: alla 18 har samma status som före (502 och 303 DRAFT, övriga ACTIVE). Handles oförändrade.
- Återläst alla fält (titel, SEO-titel, meta, html, status, handle) för alla 18: identiskt med filerna (Shopify lagrar seo.title som null när den är lika med titeln: 909, 702, 812, 115, 408 – OK).
- Original (före) sparade i `rapporter/shopify-original-2026-11-01/vag1b_fore.json`. Obs: för de 16 våg 1-produkterna är "före" hämtat ur skriv-filerna efter att live lästs och jämförts (live var lika med filen); pilotprodukternas före är live-texten.
- Skriv-JSON uppdaterade: `vag1_skriv/skriv_1..4.json`; pilotdata i `vag1_skriv/pilot_1b.json`.

## Produktnamn (källkontroll)
- **Nr 105 (10461917741322): INTE ändrad.** Källan säger tydligt något annat än beslutet: Tunturis egna sidor (tunturi.com, "Tunturi Fitnessmat Pro", produktkod 14TUSFU125) och Velomarket skriver "Fitnessmat Pro". Titeln står kvar som "Gymnastikmatta Tunturi Fitnessmat Pro, 140 cm, Blå". OBS: meta och brödtext på 105 säger redan "Tunturi Fitness Mat Pro" (alltså inkonsekvent mot titeln) – lämnat orört i väntan på Davids besked. Alternativ: behåll "Fitnessmat Pro" överallt (tillverkarens stavning, rekommenderas) eller gör "Fitness Mat Pro" överallt.
- **Nr 401 (10475978916106): ändrad Indiaka -> Indiaca** i titel, SEO-titel, meta och brödtext. Källor (Tunturi-återförsäljare via sökning, bl.a. Shark Fitness, Decathlon) skriver "Tunturi Indiaca Tennis"; stämmer med beslutet. Handle behåller "indiaka" (rörs aldrig).
- Webbåtkomst: WebFetch mot tunturi.com och sharkfitness.ch blockerades (host utanför tillåtna domäner), så källresultatet bygger på sökträffarnas titlar/utdrag, inte på sidläsning.

## Ändringar per produkt (före -> efter)
- **401 Tunturi Indiaca Tennis:** titel "…Indiaka Tennis, 2 Racketar och Boll" -> "…Indiaca Tennis…"; SEO "Tennisset Tunturi Indiaka Tennis" -> "…Indiaca Tennis"; meta och första meningen: "Tunturi Indiaka Tennis" -> "Tunturi Indiaca Tennis".
- **303 Gymball 90 cm Mint (DRAFT):** FAQ "166-178 cm" -> "166–178 cm", "179-190 cm" -> "179–190 cm". Sökning över alla 86 produkter (titel, SEO, meta, html, mönster siffra-bindestreck-siffra): inga fler intervall (enda andra träffen är org.nr 559500-4325).
- **106 Pro Exercise Wheel Deluxe:** meta "Hjulet väger 1 kg, är i svart och grönt syntetmaterial." -> "Hjulet väger 1 kg och är i svart och grönt syntetmaterial." (147 -> 150 tecken). Html redan korrekt.
- **909 Massagerulle kork 680 g:** meta och första meningen "Tunturi massagerulle i kork som väger 680 g." -> "Tunturi massagerulle är gjord i kork och väger 680 g." Meta: sista meningen "Material och färg: kork." utgick (annars 161 tecken); nu 136.
- **107 Handleds- och fotvikter 0,5 kg:** meta "Justerbara med kardborrefäste, i grått och svart. Mått 21 x 7 x 2,7 cm, en storlek." -> "De är grå och svarta, justerbara med kardborrefäste och mäter 21 x 7 x 2,7 cm. En storlek." (153 tecken). Specraden "Set: 2 per set" borttagen (upprepade intro och Vikt: 2 x 0,5 kg).
- **115 Silikonspray Hammer:** "Silikonspray för Hammer-löpband, 400 ml." -> "Det här är en silikonspray för Hammer-löpband, 400 ml."
- **408 Träningsmatta Toorx:** "Toorx träningsmatta på 180 x 90 x 0,6 cm." -> "Det här är en träningsmatta från Toorx som mäter 180 x 90 x 0,6 cm."
- **302 Double Exercise Wheel:** "Hjulet tränar överkropp och bål." -> "Med hjulet tränar du överkropp och bål."
- **315 Arm/Leg Weights 1,5 kg:** passar-för-punkten "Dig som vill kunna välja en annan vikt, eftersom modellen finns i andra vikter" borttagen (cirkulär; "Finns även i andra vikter" står kvar i specifikationer och meta); specraden "Set om 2" borttagen (upprepar "set om 2 x 1,5 kg" och Vikt).
- **414 Boxningshandskar 14 oz:** specrad "Storlek: L 30,5 x B 16 x H 12,5 cm" -> "Mått (L x B x H): 30,5 x 16 x 12,5 cm" (Storlek: 14 oz kvar); "Dig som söker 14 oz" -> "Dig som vill ha handskar på 14 oz".
- **502 Gymball 65 cm Röd (DRAFT):** meta "Tunturi Gymnastikboll med…" -> "Tunturi gymnastikboll med…".
- **601 Mobilhållare Toorx:** titel "Mobilhållare för Arm Toorx, Armband för Smartphone" -> "Mobilhållare Toorx för Arm, Armband för Smartphone"; SEO "Mobilhållare för Arm Toorx" -> "Mobilhållare Toorx för Arm".
- **702 Yogamatta 8 mm Svart:** "många poser" -> "många positioner"; "yin yoga" -> "yinyoga".
- **812 Yogamatta 8 mm Grå:** "yin yoga" -> "yinyoga" ("positioner" fanns redan). Texterna är nu enhetliga.
- **704 Hammer SmartLock:** titel "…SmartLock med Vrid-och-lås" -> "…SmartLock med Vrid-och-lås-mekanism" (59 tecken). SEO-titel oförändrad.
- **903 Massagebollar kork:** meta tidigare null -> "Tunturi korkmassagebollar är ett set med två bollar i kork, med diametrarna 5 och 6,5 cm. Setet väger 60 g. Material och färg: kork." (132 tecken). "Set om två" styrkt av Tunturis egen produktsida via sökträff (14TUSYO060: set of two, diameter 5 and 6,5 cm, 60 g). Orden "Massage Ball Set" undveks eftersom kontrollskriptet flaggar "Massage".
- **Pilot 10475621089546 AXA Fold 85:** SEO-titel "Vikbart Cykellås AXA Fold 85, Sold Secure Bronze | Best of Sports" (65) -> "Vikbart Cykellås AXA Fold 85, 85 cm" (35); "parkerar cykeln en kortare" -> "parkerar cykeln under en kortare"; "Hållare med fäste för flaskhållarfästen eller med två remmar" -> "Hållare som monteras på flaskhållarfästen eller med två remmar"; "(inom Sverige 179 kr)" borttagen. Titel och meta oförändrade.
- **Pilot 10588446589194 Kettlebell 16 kg:** SEO-titel "Kettlebell 16 kg Tunturi PE, PVC med Sand | Best of Sports" (58) -> "Kettlebell Tunturi PE 16 kg, PVC med Sand" (41); FAQ "Är den lika bra som gjutjärn? / Du kan göra samma övningar, den är gjord av PVC med sandfyllning." -> "Kan jag göra samma övningar som med gjutjärn? / Ja, du kan göra samma övningar. Kettlebellen är gjord av PVC med sandfyllning."; specraderna "Finns i olika vikter, produktkod 14TUSCL183" och "Vikt: 16 kg, färg: Svart" delade till egna rader (Material, Vikt, Färg, Mått, Lätt att rengöra och förvara, Produktkod, Finns i olika vikter); "(inom Sverige 179 kr)" borttagen. Meta oförändrad (kontrollantens "spretigt" om styrka/kondition/rörlighet vs FAQ lämnat; ingen faktaändring utan källa).

## Metabeskrivning som saknades
- **903:** skriven (se ovan).
- **Lämnade null (underlag räcker inte för 130–155 tecken utan påhitt):** 113 (BH löpbandsolja 500 ml), 114 (Toorx Lubetech 200 ml), 115 (Hammer silikonspray 400 ml), 402 (Toorx hand- och fotvikter 2 x 1,5 kg), 408 (Toorx matta 180 x 90 x 0,6 cm), 601 (Toorx mobilhållare). Källan har bara titel och mått; sökningen gav inga entydiga extrauppgifter (Lubetech/AHF-165 hittades men med motstridiga eller säljarspecifika uppgifter). Behöver leverantörsdata eller Davids besked.

## Lämnat orört och varför
- 105: se ovan (källan säger "Fitnessmat Pro").
- 307 (meta slutar "Storlek: En storlek.") och 810 ("squats"): inte i uppdraget; kontrollrapporten bedömde 810 som godtagbart.
- 704: saknad viktintervall i specifikationen läggs inte till (ingen källa).
- Övriga 68 våg 1-produkter: inte ändrade, inte skrivna.

## Kontroller
- `kontrollera_produkttext.py --seo-title-max 43` på alla 18 skrivna: enda FEL är "fakta_saknas" (ingen källtext angiven i filerna; förväntat), samt en träff "Massage" i 903:s meta före omskrivning – åtgärdad. Längder: titlar ≤ 63, SEO-titlar ≤ 42, meta 122–155 där meta finns (alla 130–155 utom att 115/408/601/113/114/402 är null).
- Skrivning: 18 av 18, userErrors 0. Statuskontroll: oförändrad för alla 18.
- Ej gjort: logg i ANDRINGSLOGG.md och beslutsfil (inga commits begärda).
