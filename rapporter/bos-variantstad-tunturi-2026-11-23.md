# Tunturi: orsak, städförslag för trasiga varianter och neutrala titlar (2026-11-23)

**Förslag; inget är ändrat i Shopify.** Läst: Shopify (varianter) och synkens databas (`product_syncs`, Velomarkets uppgifter per SKU), samt synkkoden i `velo-market-api`.

## 1. Orsaken (kod läst)

`shopify-bulk-sync` (rad ~1131–1146) uppdaterar befintliga varianter **efter position, inte efter SKU**: för varje önskad variant `i` skrivs SKU, streckkod, namn, pris och lagerpolicy till Shopifys `variants[i]`. Ändras ordningen, tillkommer eller försvinner en variant hos Velomarket, hamnar SKU:n på fel variant. Det ger exakt de fel vi ser: en variant ("Default Title", den första) som fått en annan variants SKU, två varianter med samma SKU, och priser som tillhör en annan SKU. Namnen, priset och SKU:n följer nu inte samma variant som lagret och ordrarna.

**Konsekvens för branchen:** SKU-namnen (56) skrivs till den variant som synken råkar uppdatera för just den SKU:n, så de rättar bara sin egen rad. De ger rätt resultat först när varianterna matchas på SKU. **Förslag:** ändra uppdateringen så att varje önskad variant matchas på SKU mot befintliga varianter (reserv: position bara om SKU saknas och antalet är lika), med test. Det är ett ingrepp i synkens kärna och kräver ditt ja; det ligger inte i branchen än.

## 2. De åtta produkterna: nuläge och förslag (SKU, namn, pris enligt Velomarket/databasen)

| Produkt | Nu i Shopify | Rätt enligt Velomarket | Förslag |
|---|---|---|---|
| Gymball 65 cm, Anti-Burst, Blå (10462784880906) | "Default Title" SKU 14TUSFU345 189 kr; "blue (U345)" SKU 14TUSFU345 219 kr | 14TUSFU344 = 65 cm blå, 199 kr; 14TUSFU345 = 75 cm blå, 219 kr (**borttagen hos Velomarket**) | Default → SKU 14TUSFU344, namn "65 cm / Blå"; andra → "75 cm / Blå"; överväg att ta bort 75 cm-varianten (borttagen hos leverantören). Pris sätts efter 2026-12-01 |
| Gymball 90 cm (10472214921482) | "Default Title" SKU 14TUSFU285 179 kr; "black" SKU 14TUSFU285 139 kr | 14TUSFU283 = 90 cm röd, 169 kr (arkiverad i databasen); 14TUSFU285 = 75 cm svart, 179 kr | Default → 14TUSFU283 "90 cm / Röd"; andra → 14TUSFU285 "75 cm / Svart"; titel till "Träningsboll Tunturi Gymball" |
| Fitness Gloves Pro Gel (10411721261322) | "Default Title" SKU 14TUSFU225; M, L, XL, XXL (XXL har samma SKU) | 14TUSFU221 = S, 222 M, 223 L, 224 XL, 225 XXL (alla 169 kr) | Default → SKU 14TUSFU221, namn "S". Priserna: M–XXL står på 149 kr, databasen säger 169 (prisfråga, efter 2026-12-01) |
| Treadmill Cardio Fit T30 (10472221802762) | "Default Title" SKU 24TCFT3000 8 135,10 kr; "must" SKU 24TCFT3000 **0,00 kr** | 16TCFT3000 (8 409 kr) och 24TCFT3000 (9 109 kr); samma produktnamn hos Velomarket | Default → SKU 16TCFT3000. **Vad som skiljer 16 och 24 vet vi inte** (modellår?), fråga Velomarket/Tunturi innan namn sätts. Variant med 0 kr: ta bort eller sätt rätt pris |
| Wall Ball 6 kg, Röd (10475982651658) | "Default Title" SKU 14TUSCF011 719 kr; "14TUSCF011" 659 kr | 14TUSCF010 = 6 kg röd, 719 kr; 14TUSCF011 = 8 kg blå, 759 kr | Default → SKU 14TUSCF010 "6 kg / Röd"; andra → "8 kg / Blå" |
| Strengthbag 5 kg (10472213250314) | "Default Title" SKU 14TUSCL362 729 kr; "yellow" SKU 14TUSCL362 799 kr | 14TUSCL361 = 5 kg orange, 729 kr; 14TUSCL362 = 10 kg gul, 799 kr | Default → SKU 14TUSCL361 "5 kg / Orange"; yellow → "10 kg / Gul" |
| Hantlar Platinum Hex med Gummiöverdrag (10468752720138) | "Default Title" SKU 25TUPLA014 449 kr; "25TUPLA013" 139 kr | 011 = 2×1 kg 139; 012 = 2×2 kg 239; 013 = 2×3 kg 339; 014 = 2×4 kg 449 | Default behåller 014 ("2 x 4 kg"); andra variantens SKU 013 men pris 139 (011:s pris). Bara 2 av 4 varianter finns; kontrollera lager och lägg till 011/012 efter beslut |
| Platinum Slam Ball 6 kg (10588451602698) | "Default Title" SKU 25TUPLA095 369 kr; 096 319 kr; 097 319 kr | 095 6 kg 279; 096 8 kg 359; 097 10 kg 419 | Byt "Default Title" till "6 kg" (SKU stämmer). Priserna avviker från databasen (prisfråga efter 2026-12-01) |

Alla SKU-, namn- och variantändringar görs med före-fil, återläsning och per produkt ditt ja. **Pris rörs inte före 2026-12-01.**

## 3. Neutrala produkttitlar (Tunturi, där varianterna skiljer sig i vikt, längd eller färg)

| Nu | Förslag |
|---|---|
| Styrketräningsset TUNTURI Hantel- & Skivstångsset 20 kg | Styrketräningsset Tunturi Hantel- & Skivstångsset |
| Viktplatta TUNTURI Platinum Bumper Plate, svart, 50mm, 5 kg | Viktplatta Tunturi Platinum Bumper Plate, 50 mm |
| Viktplatta TUNTURI Rubber Plate, 30 mm, 5 kg | Viktplatta Tunturi Rubber Plate, 30 mm |
| Viktplatta TUNTURI Training Bumper Plate, 50 mm, 15 kg | Viktplatta Tunturi Training Bumper Plate, 50 mm |
| Viktskivor TUNTURI Aerobic Plates 0.50kg, orange | Viktskivor Tunturi Aerobic Plates |
| Viktskivor TUNTURI Plates Black, 30 mm, 0.5kg | Viktskivor Tunturi Plates Black, 30 mm |
| Viktskivor TUNTURI Platinum Fractional Plates, Blå, 50mm, 2 x 2 kg | Viktskivor Tunturi Platinum Fractional Plates, 50 mm |
| Kettlebell TUNTURI Platinum gjutjärn 8 kg | Kettlebell Tunturi Platinum gjutjärn |
| Viktväska TUNTURI Platinum Bulgarian Bag, 10 kg (5 och 10 kg) | Viktväska Tunturi Platinum Bulgarian Bag, 5 och 10 kg |
| Heavy bag TUNTURI Platinum Bulgarian Bag, 15 kg (15 och 20 kg) | Viktväska Tunturi Platinum Bulgarian Bag, 15 och 20 kg |
| Boxningssäck Tunturi Classic Boxing Bag 80 cm, inkl. kedja | Boxningssäck Tunturi Classic Boxing Bag, inkl. kedja |
| Lyftstång TUNTURI Aerobic Pump Bar, 30 mm, 130 cm | Lyftstång Tunturi Aerobic Pump Bar, 30 mm |
| Massagerulle Tunturi Yoga Massage Roller 90 cm | Massagerulle Tunturi Yoga Massage Roller |
| Trampoline TUNTURI Funhop Trampoline 125cm | Trampolin Tunturi Funhop |
| Handledsskydd Tunturi, Bomull, Vit | Handledsskydd Tunturi, Bomull |
| Gymnastikmatta Tunturi Fitnessmat Pro, 140 cm, Blå | Gymnastikmatta Tunturi Fitnessmat Pro, Blå |
| Hantlar TUNTURI Vinyl Dumbbells 3.0kg, red | Hantlar Tunturi Vinyl Dumbbells |
| Viktväska Tunturi Strengthbag 5 kg | Viktväska Tunturi Strengthbag |
| Medicinboll Tunturi Wall Ball, 6 kg, Röd | Medicinboll Tunturi Wall Ball |
| TUNTURI Platinum Slam Ball, 6 kg | Slam Ball Tunturi Platinum |
| Träningsboll Tunturi Gymball 90 cm | Träningsboll Tunturi Gymball |

Många av dessa har taggen `texter-klara`. Titeländringar kräver ditt ja (en ändring i taget eller som grupp), och SEO-titel, handle och omdirigeringar (handle ska **inte** ändras) bör kontrolleras innan. Synken skriver inte om titlar på befintliga produkter (regel 16).

## 4. Beslut som behövs

1. **Matchning på SKU i synken** (avsnitt 1): ja till att jag lägger det i branchen med tester? Rekommendation: ja, före deploy av variantnamnen.
2. **Städningen** (avsnitt 2) produkt för produkt: godkänn per rad, eller ge ett generellt ja för SKU- och namnändringar (utan pris).
3. **Titlarna** (avsnitt 3): godkänn alla, några eller ändra.
4. **Löpbandet:** vilken skillnad finns mellan 16TCFT3000 och 24TCFT3000? Och 0-kronorsvarianten: ta bort eller prissätt (efter 2026-12-01)?
