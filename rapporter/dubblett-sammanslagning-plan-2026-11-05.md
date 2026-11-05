# Sammanslagning av dubbletter: underlag (2026-11-05)

David beslutade "Slå ihop". Inget har ändrats i butiken. Underlaget är läst direkt från Shopify.

## Vad läsningen visar
- **De flesta är inga riktiga dubbletter utan storleksuppdelade annonser.** Giant Propel Advanced 1 (7057, 6057, 7089, 7123) har fyra annonser med varsitt artikelnummer (…104 till …108) och samma pris 67 389 kr. Det är sannolikt samma cykel i olika storlekar. Men storleken framgår bara av två av dem (S och M på 7089). Jag gissar inte vilka storlekar de andra är.
- **Priserna skiljer** på 7069 (217 359 kr) mot 7084 (186 389 kr) och på 7127 (184 889 kr) mot 7110 (192 349 kr). Det kan vara olika årsmodell eller färg, inte dubbletter.
- **9433 mot 10472239333642** är en riktig dubblett (samma EAN, med och utan förpackning), båda med lager (106 och 92 st).
- **7061 mot 7062 och 7064 mot 7065** har samma artikelnummer på flera varianter men olika pris; Default Title är sannolikt överblivna.

## Förslag till sammanslagning (utförs först efter ditt ja på varje rad)
Ett riktigt sammanslag kräver att varianterna flyttas till en annons och att den andra arkiveras med omdirigering. Det går att göra via API:t, men ändrar produktstruktur, länkar och lager.

| Grupp | Behåll | Arkivera | Förutsättning |
|---|---|---|---|
| 9433 | den med flest i lager (10470898827530, 106 st) | 10472239333642 | Du bekräftar att de två slangarna är samma artikel |
| 7061 + 7062, 7064 + 7065 | 7062 respektive 7065 (skrivna) | 7061 respektive 7064 | Du bekräftar att Default Title/olika pris är fel i butiken |
| 7127 + 7110 | 7110 (skriven) | 7127 | Du bekräftar att priserna 184 889 och 192 349 kr avser samma cykel |
| 7069 + 7084 | 7084 (skriven) | 7069 | Du bekräftar att priset 217 359 kr mot 186 389 kr avser samma cykel |
| 10676718174474 + 7179 | 7179 (äldst, skriven) | 10676718174474 | Samma pris 116 209 kr, annan artikelkod: du bekräftar att de är samma |
| Propel Advanced 1 (7057, 6057, 7089, 7123) | 6057 (skriven) som storleksannons | de övriga som varianter | Du anger vilken storlek varje artikelnummer har |

## Detaljer per produkt
| Id | Handle | Skapad | texter-klara | Varianter (titel / artikelnr / pris / lager) |
|---|---|---|---|---|
| 10472435024138 | road-bike-giant-propel-advanced-1-2027-c | 2026-04-11 | nej | Default Title / 1074029107 / 67 389 kr / lager 0 |
| 10486710305034 | landsv-gscykel-giant-propel-advanced-1-2 | 2026-04-24 | ja | Default Title / 1074029106 / 67 389 kr / lager 2 |
| 10488318329098 | landsv-gscykel-giant-propel-advanced-1-2 | 2026-04-25 | nej | S / gray / 1074029104 / 67 389 kr / lager 0; M / gray / 1074029105 / 67 389 kr / lager 0 |
| 10565633769738 | landsv-gscykel-giant-propel-advanced-1-2 | 2026-07-13 | nej | Default Title / 1074029108 / 67 389 kr / lager 0 |
| 10476145213706 | road-bike-giant-trinity-advanced-sl-0-ca | 2026-04-15 | nej | Default Title / 1138005105 / 217 359 kr / lager 0 |
| 10480050110730 | landsv-gscykel-giant-trinity-advanced-sl | 2026-04-20 | ja | Default Title / 1138005107 / 186 389 kr / lager 0 |
| 10588451832074 | landsv-gscykel-giant-propel-advanced-sl- | 2026-08-10 | nej | Default Title / 1074048105 / 184 889 kr / lager 0 |
| 10526098850058 | landsv-gscykel-giant-propel-advanced-sl- | 2026-06-03 | ja | Default Title / 1074048106 / 192 349 kr / lager 0 |
| 10476044845322 | landsv-gscykel-giant-tcr-advanced-1-pc-2 | 2026-04-15 | nej | Default Title / 1096023146 / 50 029 kr / lager 0; M/L / green / 1096023146 / 43 509 kr / lager 0 |
| 10476066701578 | landsv-gscykel-giant-tcr-advanced-1-pc-2 | 2026-04-15 | ja | XS / green / 1096023143 / 50 029 kr / lager 0; L / green / 1096023147 / 50 029 kr / lager 0; XL / green / 1096023148 / 50 029 kr / lager 0 |
| 10476107497738 | bicycle-giant-tcr-advanced-pro-1-di2-car | 2026-04-15 | nej | Default Title / 1096028143 / 59 229 kr / lager 0; XS / gray / 1096028143 / 59 229 kr / lager 0 |
| 10476123521290 | cykel-giant-tcr-advanced-pro-1-di2-carbo | 2026-04-15 | ja | Default Title / 1096028148 / 68 119 kr / lager 0 |
| 10470898827530 | innerd-ck-continental-27-5-pv-47-60-584- | 2026-04-10 | nej | Default Title / VMCO0182351 / 99 kr / lager 106 |
| 10472239333642 | inner-tube-mtb-27-5-presta-s-42mm-47-584 | 2026-04-10 | nej | Default Title / VMCO0182311 / 99 kr / lager 92 |
| 10676718174474 | landsv-gscykel-giant-trinity-advanced-sl | 2026-10-22 | nej | Default Title / 1138008103 / 116 209 kr / lager 0 |
| 10665232138506 | landsv-gscykel-giant-trinity-advanced-sl | 2026-10-12 | ja | M / black / 1138008105 / 116 209 kr / lager 0 |
