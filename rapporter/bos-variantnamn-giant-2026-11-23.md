# Giant: förslag på variantnamn och SKU-rättning (2026-11-23)

Samma mönster som Tunturi, i större skala. **Förslag; inget är ändrat i Shopify.** Underlag: Shopify (varianter), synkens databas (`product_syncs`: vilka SKU:er varje produkt ska ha och deras storlekar) och synkens egen namnregel (`storlek / färg`, färgord översatta till svenska enligt `variant-names.ts`).

Filer: `rapporter/bos-variantnamn-giant-forslag-2026-11-23.csv` (128 rader), `rapporter/bos-variantstad-giant-2026-11-23/plan.json` (körbar plan, 46 produkter), `rapporter/bos-variantnamn-giant-2026-11-23.json` (Shopify-läget).

## Vad som är fel

- **32 av 51 produkter** har en variant som heter "Default Title" bredvid riktiga varianter ("XL / gray"), och i de flesta fallen har den samma SKU som en annan variant (positionsmatchningen i synken, nu rättad). Den döda varianten ska i stället bli den SKU som saknas, med storlek och färg.
- **Engelska och estniska färgord** i namnen ("XL / gray", "L / sinine"). Synken skriver om dem till svenska vid nästa uppdatering, men vi sätter dem direkt så att namnen stämmer före nästa synk.
- Storleken (S, M, M/L, L, XL, XXL) tas ur databasens produktnamn; färgen ur syskonvarianternas namn.

## Förslaget

| | Antal |
|---|---|
| Rader med nytt namn | 117 |
| varav SKU-rättning av "Default Title"-varianten | 29 |
| Produkter i planen | 46 |
| Rader som kräver manuellt besked | 11 |

Exempel: Roam 4 (Svart): "Default Title" med SKU 1082012184 blir SKU 1082012185 och "M / Svart", "XL / black" blir "XL / Svart". Talon 1 GE: "Default Title" 2201130288 blir 2201130285 "M / Brun". Handskar Wisp SF: "Default Title" blir den saknade storleken.

## Manuella fall (11 rader)

- **Talon 2 (2027), Eclipse:** produkten saknas i databasen under det id den har i Shopify (databasen grupperar den under ett annat id), så SKU:er kan inte avgöras.
- **Flaskhållare Giant Gateway, Airway Sport Sidepull, pedaler Pinner Comp, strumpor Liv Short N Snug:** databasen anger ingen storlek/modell (flaskhållare R/L, strumpor XS/S och M/L, pedaler), så namnen kräver Velomarkets attribut.
- **TCR Advanced 0 PC (Frost Silver):** en "Default Title"-variant med SKU 1096021146 saknar entydig saknad SKU.

## Pris

Variantpriserna är inte med. Flera varianter står på olika priser som troligen hör till en annan SKU (till exempel Roam 4: M 11 303 kr men S 9 917 kr). Det tas efter 2026-12-01.

## Beslut som behövs

1. **Godkänn de 117 namnen och 29 SKU-rättningarna** (kanarie på en produkt, sedan resten, med före-fil och återläsning som för Tunturi). Jag kör inget före ditt ja.
2. **De 11 manuella raderna:** ska jag be dig fråga Velomarket om flaskhållarna, strumporna och pedalerna, eller lämna dem som de är?
3. **Förbättra SKU-matchningen** (uppföljnings-PR i `velo-market-api`): vid dubbel SKU ska synken föredra varianten som *inte* heter "Default Title", så att den döda varianten aldrig råkar få en riktig variants namn. Efter städningen finns inga dubbla SKU:er kvar, så det är en säkerhetsåtgärd.
