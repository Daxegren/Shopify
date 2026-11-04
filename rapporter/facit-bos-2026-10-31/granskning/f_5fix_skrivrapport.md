# Skrivrapport f_5fix (2026-11-04)

Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info. Skrivfil: vag2_skriv/f_skriv_5fix.json. Före-läge: shopify-original-2026-11-04/f_5fix_fore.json.

| Nr | Produkt-id | Resultat |
|---|---|---|
| 10103 | 10411848532234 | Skriven. Titel, seo.title, seo.description och descriptionHtml lika skrivfilen tecken för tecken (python). |
| 10110 | 10541370114314 | Skriven. Samma kontroll, alla fyra lika. |

- Orsak: tidigare agent hoppade över på lika titel; livetexten var pilotens gamla med "Vanliga frågor" och "Om märket" (LARDOMAR 2026-11-03). Hela posten ersattes.
- Skrivning: ett productUpdate-anrop med två alias, mutationen utskriven av python med json.dumps(ensure_ascii=True), inga osynliga tecken (kontrollerat), inga userErrors.
- Återläsning: "Vanliga frågor" och "Om märket" finns inte kvar. Leveranstidsmeningen ("Beställningsvaror kan ta upp till en vecka längre") finns i 10103 (har taggen På beställning) och saknas i 10110 (saknar taggen).
- Orört: handle, status, pris, tidigare taggar (identiska före och efter).
- Tagg: texter-klara tillagd med tagsAdd på båda (saknades). Övriga taggar kvar.
- Ändrat i Shopify: ja, bara dessa två produkter.
