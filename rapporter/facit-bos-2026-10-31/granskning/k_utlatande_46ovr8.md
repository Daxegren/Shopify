# Granskningsutlåtande k_46ovr8, aktiva produkter i tidigare utanför-kategorier (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient; `verifiera_butik` gav BEST OF SPORTS). `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, BESLUTSLOGG till och med 2026-11-08 (aktiva produkter utan text får faktatext enligt strukturen, men produkter med motsägande eller tom källa och exakta dubbletter av andra aktiva annonser skrivs inte), `c_granskarprompt.md` och formatet i `k_utlatande_43.json`/`k_utlatande_46ovr6.json`. Tidigare avvisningar av tvillingannonsen 10676714111242 lästes (k_02a nr 9106, k_17l, k_46ovr7).

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_46ovr8.json` (tom lista, eftersom utkastfilen är tom).

## Resultat: 0 GODKÄND, 0 RÄTTA, 0 UNDERKÄND

`k_46ovr8_utkast.json` är tom (`[]`). Det finns inga utkast att granska. Batchen innehöll en produkt, och utkastaren avvisade den.

## Avvisad produkt: avvisningen är riktig och lyfts inte

| nr | id | titel | bedömning |
|---|---|---|---|
| 47701 | 10676714144010 | Kapellställning CARGOBIKE of SWEDEN för Flex/Delight Nova Premium | Avvisningen står kvar. Ett ytterligare skäl tillkommer: produkten är en exakt dubblett. |

Livekontroll av 10676714144010: status ACTIVE, typ "Tillbehör för lådcyklar", taggen På beställning, en variant (Default Title) med SKU 1521-100, EAN 7350097567997, 789 kr och lager 0. Handle slutar på `-1521-101`, men varianten har SKU 1521-100. Live-texten säger bara "Kapellställning för modellerna Flex Nova och Delight Nova från Cargobike of Sweden" och "Tillverkad av Cargobike of Sweden". Det är en enda uppgift utöver titeln, och ordet "Premium" i titeln har inget stöd i källan. Det saknas mått, material och vikt.

1. **Tunn och motsägande källa (R3):** utkastarens skäl stämmer. Samma bedömning gjordes tidigare för tvillingannonsen, i k_02a nr 9106, k_17l och k_46ovr7. Där gav en webbsökning ingen tillverkarsida som entydigt gäller artikel 1521-100.
2. **Exakt dubblett (R12a och beslutet 2026-11-08):** 10676714111242 är också ACTIVE och har identisk titel, identisk beskrivning, samma SKU 1521-100, samma EAN 7350097567997, samma pris (789 kr) och lager 0. Enligt beslutet skrivs exakta dubbletter av andra aktiva annonser inte förrän annonserna har slagits ihop.

## Frågor till David

1. Kapellställningen för Flex/Delight Nova Premium (SKU 1521-100) ligger aktiv två gånger: 10676714111242 och 10676714144010. En av annonserna bör tas bort ur försäljning (till exempel arkiveras) innan någon av dem får text. Samma mönster finns för Canopy Bows Long Lite: 10676713750794 och 10676713783562 är båda aktiva med SKU 1521-28, trots handles -1521-28 och -1521-29.
2. Även efter en sammanslagning räcker källan inte för en faktatext. Det behövs en tillverkaruppgift (mått, material, vad "Premium" avser) för artikel 1521-100.
