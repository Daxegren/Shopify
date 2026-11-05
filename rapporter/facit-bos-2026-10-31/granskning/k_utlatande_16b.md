# Granskningsutlåtande k_16b

Datum: 2026-11-05. Granskaren är Opus och har bara läst i Shopify. Butiken bekräftades som BEST OF SPORTS (6f2e53-67.myshopify.com). Källan, varianterna, taggarna och syskonprodukterna hämtades live via `shopify_api`. Dessutom gjordes en titelsökning i butiken per modell.
Utkastfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_16b_utkast.json`. Det maskinläsbara utlåtandet finns i `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_16b.json`.
Förutsättningar: v1.7 gäller. Elektronisk växling får skrivas när källan anger modellen ordagrant. Enligt R3 ignoreras en överbliven variant som heter Default Title och har samma SKU och färg. Faktakoll på nätet är tillåten.

## Resultat

| nr | id | Produkt | Dom |
|---|---|---|---|
| 6052 | 10472294285578 | Giant Defy Advanced 1, Charcoal/Milky Way | RÄTTA |
| 7047 | 10472321024266 | Liv Langma Advanced SL 1, Cosmic Dust | GODKÄND |
| 7052 | 10472331575562 | Liv Devote Advanced 0 SE (2026), Tropical Collage | RÄTTA |
| 7055 | 10472335376650 | Giant Trinity Advanced SL 1, Carbon/Matte Carbon | RÄTTA |
| 6060 | 10472335671562 | Giant TCR Advanced 1 PC, Dreamy Blue | GODKÄND |
| 7057 | 10472435024138 | Giant Propel Advanced 1 (2027), Carbon | GODKÄND (villkor: dubblett) |
| 7062 | 10476066701578 | Giant TCR Advanced 1 PC, Asphalt Green | GODKÄND |
| 7065 | 10476123521290 | Giant TCR Advanced Pro 1-Di2, Carbon | GODKÄND |
| 7069 | 10476145213706 | Giant Trinity Advanced SL 0, Carbon/Prismatic Haze | RÄTTA (villkor: dubblett) |

`skrivfil_kontroll.py` gav 0 fel och 0 varningar, både på en kopia av utkastet och på en kopia där rättningarna var införda. Standardblocket är identiskt med `b_skriv_24.json`. Leveranstidsmeningen finns på exakt de sju produkter som har taggen "På beställning". Den saknas på 6052 och 6060, och det är rätt eftersom de saknar taggen.

## Fokuspunkter

- **7052, Shimano GRX RX-820.** Utkastaren har rätt. RX-820 är Shimanos mekaniska grupp med 12 växlar per kassett, och den elektroniska Di2-versionen heter RX-825 ([Cycling Weekly](https://www.cyclingweekly.com/products/shimano-grx-12-speed-goes-electronic-with-2x12-speed-di2-shifting), [Cycle Tech Review](https://cycletechreview.com/2023/components-reviews/shimano-grx-rx820-12-speed-mechanical-gravel-groupset/)). För exakt den här modellen och färgen anger [Pushys](https://www.pushys.com.au/liv-devote-advanced-0-se-tropical-collage/) RX-820 med 2x12 växlar. Texten påstår varken mekanisk eller elektronisk växling. Det följer uppdraget och kan stå kvar. Avvisningen i k_12, som kallade RX-820 för Di2, var fel. En sak rättas: "(max 53 mm)" i däckraden stryks. Det framgår inte om siffran gäller däcket eller hur brett däck ramen rymmer, och då ska uppgiften utelämnas enligt R2.
- **6052, "22 växlar".** Källan skriver "Shimano 105 Di2 22 växlar". Shimano 105 Di2 finns bara med 12 växlar på kassetten. Defy Advanced 1 i Charcoal/Milky Way är 2024 års modell och säljs med 105 Di2 2x12, alltså 24 växlar ([bike-room](https://bike-room.com/products/giant-defy-advanced-1-2024-giant-pr2-shimano-105-di2-2x12sp), [Ivanhoe Cycles](https://ivanhoecycles.com.au/products/giant-defy-advanced-1-2024-charcoal-milky-way)). Källans siffra är alltså fel, och därför stryks växelantalet på alla fyra ställen (R2). Att i stället skriva 24 vore tillåtet enligt v1.6, men det kräver att man litar på en återförsäljares specifikation. Jag har valt att stryka siffran. Det finns också ett utkast (status DRAFT) med samma titel, id 10468706812170. Det är inte skrivet och räknas inte som dubblett.
- **Storlekar, färger och priser i titlar.** Ingen text nämner ramstorlekar eller passande kroppslängd. Ingen titel innehåller pris eller storlek. Där färgen står i titeln har produkten bara en färg. 7062 har tre storleksvarianter (XS, L och XL) med olika SKU men samma färg och pris, så titeln låser ingen variant. Ett observandum: produkterna med varianten Default Title är i praktiken en enda storlek var. SKU-numrets sista siffror visar storleken. Därför är det rätt att texten inte nämner någon storlek.
- **7069, SRAM RED AXS E1 med 12 växlar.** Uppgiften stämmer, eftersom Trinity Advanced SL 0 har en klinga fram och 12 drev bak ([99spokes](https://99spokes.com/bikes/giant/2025/trinity-advanced-sl-0), [Giant](https://www.giant-bicycles.com/gb/bikes-trinity-advanced-sl-2027)). En sak rättas: gaffelns "helt kompositstyrrör" kommer från syskonprodukten 7084. Produktens egen källa säger "full carbon styrrör" (R1).
- **7055.** SEO-titeln förkortar färgen till "Carbon/Matte", som inte är någon färg. Den ändras till "Matte Carbon", som är en del av det riktiga färgnamnet (41 tecken).
- **Elektronisk växling (v1.7).** Utkasten anger Di2, AXS (D2) och RED AXS E1 ordagrant som i källan. Ingen text påstår mekanisk växling, och batteri och räckvidd nämns inte.

## Dubblettrisk (R12a, R12)

| Grupp | Produkter (SKU, pris) | Bedömning |
|---|---|---|
| Propel Advanced 1 (2027), Carbon | **7057** (…107, 67 389 kr), 6057 (…106, 67 389 kr), 7089 (S/M, …104/105, 67 389 kr), 7123 (…108, 67 389 kr) | Alla är aktiva och ingen är skriven. Källtexten är densamma, på engelska eller svenska. Bara en av de fyra får skrivas, eftersom titel, SEO och meta måste vara unika. 7057 godkänns på villkor att den är den som väljs. Annars hålls den kvar. |
| Trinity Advanced SL 0, Carbon/Prismatic Haze | **7069** (…105, 217 359 kr), 7084 (…107, 186 389 kr) | Ingen av dem är skriven. Bara en får skrivas. Priserna skiljer sig med 30 970 kr, vilket David bör titta på. Det är inget textfel. |
| TCR Advanced 1 PC, Asphalt Green | **7062**, 7061 | 7061 är rätt avvisad. Den har en Default Title och en M/L-variant med samma SKU men olika pris. |
| TCR Advanced Pro 1-Di2, Carbon | **7065** (68 119 kr), 7064 (59 229 kr) | 7064 är rätt avvisad som dubblett, men utkastarens skäl är oprecist. 7064:s egna två varianter har samma SKU och samma pris, så den hade varit skrivbar enligt v1.7. Prisskillnaden är en fråga för David. |

## Rättningar (exakt före → efter)

**6052**
- meta: `Shimano 105 Di2 med 22 växlar och` → `Shimano 105 Di2 och`
- html: `Shimano 105 Di2 med 22 växlar, hydrauliska` → `Shimano 105 Di2, hydrauliska`
- html: `<li>Dig som vill ha Shimano 105 Di2 med 22 växlar</li>` → `<li>Dig som vill ha växelsystemet Shimano 105 Di2</li>`
- html: `<li>Växelsystem: Shimano 105 Di2, 22 växlar</li>` → `<li>Växelsystem: Shimano 105 Di2</li>`

**7052**
- html: `<li>Däck: Cadex GX, tubeless, 700x40C (max 53 mm)</li>` → `<li>Däck: Cadex GX, tubeless, 700x40C</li>`

**7055**
- seo_title: `Giant Trinity Advanced SL 1, Carbon/Matte` → `Giant Trinity Advanced SL 1, Matte Carbon`

**7069**
- html: `helt kompositstyrrör, genomgående axel 12x100 mm` → `styrrör helt i kolfiber, genomgående axel 12x100 mm`

Varje "före" förekommer exakt en gång i sitt fält. Det kontrollerades med python på en kopia i scratchpad.

## Övrigt (R7, R11, R15)

Typordet "Landsvägscykel" eller "Gravelcykel" stöds av taggarna Racercykel och Gravelcykel och av butikens egna ord. Ingen första mening är cirkulär. Live-produkterna saknar SEO-titel, och de gamla beskrivningarna ersätts helt. Ingenting har ändrats i Shopify.
