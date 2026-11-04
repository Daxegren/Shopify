# Granskning väg 2, elcyklar och cyklar k_01d (2026-11-04)

Oberoende granskning (Opus), endast läsning mot Shopify. Underlag: `vag2_skriv/k_01d_utkast.json` (4 utkast: 9017, 9029, 9030, 9034), `k_01d_avvisade.json` (tom). Regelbok v1.5, BESLUTSLOGG, butiksprofil BEST OF SPORTS, standard §16 och Davids beslut för 9017, 9029/9030 och 9034. Alla fyra hämtades live på nytt via Admin API (`shopify_api.hamta_produkter` + variantfråga), plus 9026, 9027, den arkiverade 10472335638794 och alla 3 365 aktiva produkter (titel, SEO-titel, meta) för R12. Alla fyra är ACTIVE och saknar SEO-titel och meta. Inget ändrat i Shopify.

**Resultat:** 4 GODKÄND, 0 RÄTTA, 0 UNDERKÄND.

| nr | id | dom | skäl |
|---|---|---|---|
| 9017 | 10494946312458 | GODKÄND | Allt spårbart i egen svensk källa. Lastkapacitet 150 kg är en ren svensk rad (R4). Färgen utelämnad enligt Davids beslut (Gem Blue mot SKU GREEN). Ingen tagg "På beställning", ingen leveranstidsmening. |
| 9029 | 10682105299210 | GODKÄND | Spårbart. Bara M, L och XL nämns (säljs som varianter, samma pris); S rätt utelämnad (R3 v1.5). Mars Dust mot variantfärgen Red: ingen motsägelse, praxis 9024. Taggen finns, meningen med. |
| 9030 | 10682105331978 | GODKÄND | Som 9029. Moonstone mot blue: ingen motsägelse (ljust blågrått kulörnamn); godtas som färg som bara finns i titeln. |
| 9034 | 10676719714570 | GODKÄND | Spårbart; en variant, ramstorlekar rätt utelämnade. Titelkrocken mot den arkiverade 10472335638794 är avsedd. Se fynd 1 om en aktiv dubblett. |

## Kontroll av att_bekrafta och Davids beslut
- **9017 utan färg:** följer beslutet. Titel och SEO "Elcykel Engwe E26" är unika (9018 heter "…, Svart").
- **9029/9030 färg från live-titeln:** godtas. Varianterna (Red/blue) säger inte emot Mars Dust/Moonstone, och färgen bekräftas inte heller av SKU. Samma nivå som 9026/9027 och 9024.
- **9029/9030 titel avviker från 9026/9027:** avsett. SEO-titlarna skiljer sig genom ", M–XL" och metan är olika, så R12 håller. 9026 och 9027 är fortfarande ACTIVE med texter-klara (en variant var, SKU …204/…104). Två aktiva produkter av samma modell och färg med text kvarstår tills 9026/9027 hanteras.
- **Storlek S utelämnad (9029/9030), ramstorlekar utelämnade (9034):** rätt enligt R3 v1.5.
- **9034 "Växlar: Shimano Cues" och "nedre ramrör" för underrör:** godtagbara omskrivningar, inget nytt påstående.
- **R13:** leveranstidsmeningen finns på exakt de tre som har taggen "På beställning" (9029, 9030, 9034), inte på 9017.
- **R12:** inga lika titlar, SEO-titlar eller metor mot aktiva produkter eller mot andra batchfiler, utom 9034:s titel (se fynd 1 och den avsedda krocken mot b_skriv_17/8824).

## Fynd
1. **Aktiv dubblett av 9034 som inte finns i någon batch:** 10676719812874 "Gravelcykel GIANT Revolt Advanced 3, Aquarium" (ACTIVE, skapad 2026-10-22, handle slutar på -1080022145) har samma SKU 1080022144, samma källa och en variant, men priset 44 609 kr mot 9034:s 44 529 kr. Titeln krockar redan live (bara GIANT/Giant skiljer). Skrivningen av 9034 skapar ingen ny krock, men produkten bör inte skrivas med samma titel senare.

## Öppna frågor till David
1. **Revolt Advanced 3 Aquarium:** två aktiva produkter med samma SKU och olika pris (9034 44 529 kr, 10676719812874 44 609 kr). Vilken ska finnas kvar, och ska den andra arkiveras?
2. **9026/9027:** ska de arkiveras nu när 9029/9030 får texten, så att samma modell och färg inte visas två gånger?
