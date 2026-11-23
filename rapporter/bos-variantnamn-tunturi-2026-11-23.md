# Tunturi: förslag på variantnamn (2026-11-23)

Del av Davids beslut att variantnamn ska skilja varianterna åt (färg, storlek, vikt, längd eller modell) och inte vara SKU. **Förslag; inget är ändrat i Shopify och inget är lagt i koden.** Namnen kommer från Velomarkets produktnamn per SKU (läst ur `product_syncs.product_name` i synkens databas, bara läsning). Filen `rapporter/bos-variantnamn-tunturi-forslag-2026-11-23.csv` har 56 förslag (produkt, SKU, nuvarande namn, föreslaget namn, pris, lager). Underlag: `rapporter/bos-variantnamn-tunturi-2026-11-23.json`.

## Exempel

| Produkt | SKU | Nu | Förslag |
|---|---|---|---|
| Styrketräningsset TUNTURI Hantel- & Skivstångsset 20 kg | 14TUSCL454 / 14TUSCL455 | 14TUSCL454 / 14TUSCL455 | **20 kg / 28 kg** (Velomarket: Set 20 kg och 28 kg) |
| Viktplatta TUNTURI Platinum Bumper Plate, svart, 50mm, 5 kg | 25TUPLA001 m.fl. | SKU | Svart / 5 kg, Svart / 20 kg, Grå / 5 kg, Grön / 10 kg, Gul / 15 kg |
| Kettlebell TUNTURI Platinum gjutjärn 8 kg | 25TUPLA070–075 | SKU | 6, 8, 10, 12, 16 och 20 kg |
| Gymnastikmatta Fitnessmat Pro | 14TUSFU125 / 126 | 14TUSFU125 / blue | 140 cm / Blå, 180 cm / Blå |
| Träningshandskar Pro Gel | 14TUSFU222–225 | M, L, XL, XXL (redan rätt) | oförändrade |

## Två slutsatser om produktstrukturen

1. **Produkttitlarna stämmer ofta inte med varianterna.** Varianterna är olika produkter som synken slagit ihop på SKU-prefix. Exempel: setet heter "20 kg" men har en 28 kg-variant, bumper plate-produkten heter "5 kg" men har 5 till 20 kg, Wall Ball-produkten heter "6 kg, Röd" men har en 8 kg blå-variant. Variantnamnen räddar bara delvis: titlarna bör bli neutrala (till exempel "Viktplatta Tunturi Platinum Bumper Plate, 50 mm") när varianterna skiljer sig i vikt. Det är ett separat förslag (textändring, kräver ditt ja).
2. **Sju produkter har trasiga varianter** som inte går att rädda med namn (14 rader): en variant heter "Default Title" bredvid andra, och i sex av fallen delar den SKU med en annan variant, i fem av dem med olika pris. Namn per SKU skulle ge två varianter samma namn. De behöver strukturåtgärd i synken eller manuell städning efter beslut:

| Produkt | Problem |
|---|---|
| Gymnastikboll Gymball 65 cm, Anti-Burst, Blå | "Default Title" 189 kr och "blue (U345)" 219 kr har samma SKU 14TUSFU345; Velomarket kallar SKU:n Gymball 75 cm och den är borttagen hos Velomarket (`not_found`) |
| Träningsboll Gymball 90 cm | "Default Title" 179 kr och "black" 139 kr har samma SKU 14TUSFU285 (Velomarket: 75 cm svart) |
| Träningshandskar Pro Gel | "Default Title" 169 kr och XXL 149 kr har samma SKU 14TUSFU225 |
| Treadmill Cardio Fit T30 | "Default Title" 8 135,10 kr och "must" **0,00 kr** har samma SKU 24TCFT3000 |
| Medicinboll Wall Ball 6 kg, Röd | "Default Title" 719 kr och "14TUSCF011" 659 kr har samma SKU (Velomarket: 8 kg, blå) |
| Viktväska Strengthbag 5 kg | "Default Title" 729 kr och "yellow" 799 kr har samma SKU 14TUSCL362 (Velomarket: 10 kg, gul) |
| Hantlar Platinum Hex med Gummiöverdrag | "Default Title" bredvid 25TUPLA013 |
| TUNTURI Platinum Slam Ball 6 kg | "Default Title" bredvid 25TUPLA096/097 |

Prisfrågan: samma SKU med två priser betyder att kunden ser ett pris men en av varianterna kan vara fel pris (särskilt 0,00 kr på löpbandet).

## Beslut som behövs

1. **Godkänn namnförslagen** i CSV-filen (56 st) så lägger jag in dem i `SKU_VARIANT_NAMES` på branchen `claude/variantnamn-svenska-farger-och-override` (och uppdaterar testerna). De 14 trasiga raderna är inte med.
2. **De trasiga varianterna:** ska jag ta fram ett städförslag per produkt (ta bort den döda "Default Title"-varianten eller flytta SKU:n)? Det är ändringar av varianter i butiken och kräver ditt ja per produkt. Löpbandets 0-kronorsvariant bör prioriteras.
3. **Produkttitlar** som inte stämmer med sina varianter: ska jag föreslå neutrala titlar för de berörda produkterna?
