# Skrivrapport skrivfil 2 (BOS, löpband), 2026-11-04

- Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info före skrivning.
- Skrivfil: vag2_skriv/f_skriv_2.json, 22 produkter (10034 och 10044 underkända och ej med; 10045 redan skriven). Före-läge: rapporter/shopify-original-2026-11-04/f_2_fore.json.
- Före: alla 22 ACTIVE, ingen med texter-klara, seo.title och seo.description tomma, gamla Velomarket-texter med titlar som "Treadmill ...". Inga hoppades över.
- Kontroll på kopia (kontrollera_produkttext.py, --seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70, källtext = före-läget): 0 FEL, 23 varningar (saknad rubrik "Passar dig som" = känd och godtagen; 10411839914250 har 32 ord, tunn källa).
- Skrivning: productUpdate (title, seo{title, description}, descriptionHtml), skriptutskrift klistrad ordagrant, batcher 3 (kanarie) + 5 + 5 + 5 + 4. Alla userErrors tomma.
- Återläsning: högst 4 produkter per fråga, jämförelse i python (g2_cmp.py) för title, seo.title (null när lika med titeln, avsett), seo.description, descriptionHtml (22 av 22 byte för byte lika), handle och status (oförändrade), samt osynliga tecken (U+00AD, nollbredd, U+00A0): 0 avvikelser. Allt maskinellt, inget för hand.
- Leveranstid: de 9 produkter som har taggen "På beställning" (10472261714186, 10472264630538, 10472289042698, 10598555549962, 10476097601802, 10523460337930, 10494733123850, 10561324220682, 10494829199626) har meningen "Beställningsvaror kan ta upp till en vecka längre." exakt; de 13 övriga saknar den. Stämmer 22 av 22.
- Taggar: texter-klara tillagd på alla 22 med tagsAdd; återläst, alla tidigare taggar (Velomarket, Gymstick, Fell, På beställning m.fl.) finns kvar.
- Ändrade inte: handle, status, pris, andra taggar. Inga avvikelser, inga omskrivningar.
