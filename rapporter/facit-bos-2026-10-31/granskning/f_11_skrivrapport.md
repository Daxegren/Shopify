# Skrivrapport f_11 (Velomarket, Tunturi viktskivor och Hammer hantlar), 2026-11-04

Skrivfil: `vag2_skriv/f_skriv_11.json` (21 produkter). Före-läge: `rapporter/shopify-original-2026-11-04/f_11_fore.json`. Butik bekräftad: BEST OF SPORTS (bestofsports.se).

- Hoppade över: 0. Alla 21 var ACTIVE, saknade taggen texter-klara och hade annan titel än skrivfilen. (10254, 10257, 10258, 10264 avvisade, ej i filen.)
- Kontrollskriptet (--seo-title-max 43, suffix " – BEST OF SPORTS"): 24 FEL, 29 varningar, alla kända/godtagna: meta kortare än 130 tecken (kort sann meta, Davids beslut 2026-11-03), 2 x "tal_utan_kalla" ("2" kommer från "två" i källan, 10262 och 10266), kommatecken i mått i titeln, saknad rubrik "Passar för"-varning, engelska ordet "Black" (produktnamn).
- "På beställning": taggen finns på 8 produkter (10265, 10266, 10270-10275) och exakt de har meningen "Beställningsvaror kan ta upp till en vecka längre." i skrivfilen; övriga 13 saknar både tagg och mening (maskinellt kontrollerat).
- Skrivet: kanarie 3, därefter 5+5+5+3 (högst 5 per productUpdate), mutationer skrivna ut av skript (ensure_ascii=True) och inklistrade ordagrant. Inga userErrors.
- Återläsning: alla 21 lästes tillbaka (högst 4 åt gången) och jämfördes maskinellt tecken för tecken mot skrivfilen (titel, seo.title, seo.description, descriptionHtml) samt handle/status mot före-läget och osynliga tecken. 0 avvikelser. Ingen manuell jämförelse utöver att återläsningen klistrades in i jämförelseskriptet.
- Tagg: texter-klara tillagd på alla 21 med tagsAdd; befintliga taggar (inkl. Velomarket, Tunturi, Hammer, På beställning) finns kvar. Handle, status och pris ändrades inte.
- Före/efter: alla 21 hade tom SEO (title/description null) och leverantörens översatta text (delvis med trasiga siffror, engelsk text på Hammer Compact, tom "Tillverkare ."); efter: ny titel, SEO-titel och meta, beskrivning enligt standarden med standardblock.
- Observation: Shopify lagrade seo.title som skrivet (inte null) eftersom den skiljer sig från titeln.
- Avvikelser: inga.
