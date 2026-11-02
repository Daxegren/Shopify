# Skrivrapport våg 1c (rättningsrunda på våg 1b) – BEST OF SPORTS, 2026-11-02

Butik: get-shop-info gav BEST OF SPORTS (bestofsports.se). Inget committat, ingen loggpost eller beslutsfil skriven.

## Sammanfattning
- 11 produkter skrivna, 0 userErrors. Kanarie 903, 105, 107; därefter batch om 8 (315, 414, 702, 812, 704, 302, Kettlebell, AXA).
- Före-läge (live läst före skrivning, status ACTIVE, identiskt med skrivfilerna): `rapporter/shopify-original-2026-11-02/vag1c_fore.json`.
- Skrivet med `productUpdate(product:)`, `seo` alltid med både title och description. Titel, handle och status skickades inte; alla handles och status (ACTIVE) oförändrade enligt svaret.
- Skrivfilerna `vag1_skriv/skriv_1..4.json` och `pilot_1b.json` uppdaterade (JSON är sanningen; källskripten är inaktuella).
- Maskinellt: längder, kontrollskript, textersättning med exakt träff. För hand: val av formuleringar, jämförelse av svaren från Shopify mot filerna.

## Före -> efter per produkt
- **903 Massagebollar kork:** meta "…två bollar i kork, … Material och färg: kork." -> "Tunturi korkmassagebollar är ett set med två bollar med diametrarna 5 och 6,5 cm. Setet väger 60 g. Både material och färg är kork." (131; stor bokstav efter kolon borta, upprepningen av kork borta). Html: "har diametern" -> "har diametrarna"; passar-för "Dig som vill ha massagebollar i kork" (cirkulär) -> "Dig som vill ha ett set med två massagebollar".
- **105 Fitnessmat Pro:** "Fitness Mat Pro" -> "Fitnessmat Pro" i meta och html (titel och SEO-titel hade redan rätt stavning). Meta 142 tecken. Andra produkter med "Fitness Mat Pro": ingen (live-sökning gav bara Toorx "Fitness Mat 172 Pro", ett annat namn, orört).
- **107:** meta (verblös första mening, fragmentet "En storlek.") -> "Tunturi handleds- och fotvikter i neopren säljs som set om 2 x 0,5 kg. De är grå och svarta, justerbara med kardborrefäste och mäter 21 x 7 x 2,7 cm." (149). "En storlek" finns kvar i html.
- **315:** meta (fragment "Finns även i andra vikter. En storlek.") -> "…De lindas runt handlederna eller anklarna. Modellen finns även i andra vikter." (152).
- **414:** meta -> "Tunturi Allround Boxing Gloves är universella boxningshandskar i konstläder med mjuk stoppning. Handskarna har storlek 14 oz och väger 290 g." (141). Html: passar-för-punkten om bred kardborre kring handleden borttagen (kardborren nämns nu i ingress och specifikation).
- **702 / 812:** meta -> "Tunturi yogamatta på 8 mm är i TPE och tjockare än vanliga mattor (3–4 mm). Den är halkfri, lätt att rengöra och har bärväska. Finns i 7 färger, här svart/grå." (155 / 153). Html: "Yoga där du utför många positioner liggande eller sittande" -> "Yoga i liggande eller sittande positioner".
- **704:** upprepningen borttagen i html: ingressens andra mening om viktskivorna borta, specifikationsraden om vrid-och-lås-mekanismen borta (finns i ingressen). Meta oförändrad (146).
- **302:** ingressens mening "Med hjulet tränar du överkropp och bål." och passar-för-punkten om dubbelhjuldesign och breda handtag borttagna (finns i ingress och specifikation). Meta oförändrad.
- **Kettlebell:** meta (verblös, "styrka, kondition och rörlighet" motsade FAQ) -> "Tunturi PE-kettlebell väger 16 kg och är gjord i PVC fylld med sand. Den är lätt att rengöra och förvara och är ett alternativ till gjutjärn." (141). Träningsområden utelämnade i meta (osäker källa), FAQ oförändrad. Html-ingress: "är en kettlebell på 16 kg" -> "väger 16 kg och är gjord i PVC fylld med sand" (upprepningen borta). "billigare" borttaget i meta och html (kontrollskriptet flaggar prisord; ingen källa).
- **AXA:** meta (certifieringen saknade verb) -> "AXA Fold 85 är ett vikbart 85 cm cykellås med 7 mm härdade stållänkar. Det är certifierat Sold Secure Bronze och levereras med hållare och 2 nycklar." (149). SEO-titel "Vikbart Cykellås AXA Fold 85, 85 cm" -> "Vikbart Cykellås AXA Fold 85" (28; dubbleringen av 85 borta).

## Hoppade över
- **303 och 502 (DRAFT):** inte skrivna, filerna oförändrade. Kvarstående: 502:s verblösa meta och 303:s "avsedd för längd över 190 cm".
- **115, 408, 601 (saknad meta):** lämnade null. Filerna har bara titel/mått, ingen entydig källa; en meta på 130–155 tecken skulle kräva påhittade fakta. Behöver leverantörsdata eller Davids besked. **402:** null enligt uppdraget.
- Ej ändrat (stilfråga, inget språkfel): 909 "Tunturi massagerulle är…", 106, 401, 601 titel.

## Kontroll
- `kontrollera_produkttext.py --seo-title-max 43 --seo-suffix " – BEST OF SPORTS"` på en kopia (html mappad till beskrivning, "Passar för" mappat till "Passar dig som:", standardblock i [[STANDARDBLOCK]]): 11 produkter, 0 varningar. FEL kvar: "fakta_saknas" på alla (ingen källtext i kopian, förväntat) samt "halsa: Vibration" på AXA, som är falsklarm: den gamla specraden "Vibrationsdämpning" (låsets egenskap), orörd. Första körningen gav "billigare" på Kettlebell, åtgärdat.
- Längder: titlar ≤ 59, SEO-titlar ≤ 42, meta 131–155. Unika titlar/SEO/meta bland de 11. Inga intervall med bindestreck, enheter med liten bokstav, stor bokstav efter kolon.
- Återläsning: svaret från varje productUpdate (title, handle, status, seo.title, seo.description, descriptionHtml) jämfört med skrivfilen för alla 11, utan avvikelser. 702 och 812 har seo.title null i Shopify (lika med titeln, avsett). Radbrytning mellan `<li>` bevarad. Gjort för hand (utdata kan inte diffas i bash).
- Ej gjort: ny kontroll dagen efter nattsynken (titlar rördes inte, men läs tillbaka), post i ANDRINGSLOGG.md, beslutsfil.
