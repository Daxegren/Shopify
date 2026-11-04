# Skrivrapport f_skriv_3 (BEST OF SPORTS, 2026-11-04)

- Butik bekräftad: BEST OF SPORTS (bestofsports.se). Skrivfil: vag2_skriv/f_skriv_3.json, 25 produkter (nr 10051–10075).
- Före-läge: rapporter/shopify-original-2026-11-04/f_3_fore.json (25 produkter, alla ACTIVE, ingen med texter-klara, alla hade seo null).
- Hoppade över: 0 (titlarna skilde sig från skrivfilen på alla 25).
- Kontrollskriptet (kopia, html mappad till beskrivning, standardblock markerat, --seo-title-max 43, suffix): 5 FEL, alla meta_langd (105–129 tecken, kort meta enligt standard avsnitt 14), 26 VARNINGAR (Passar för-rubriken, känd; en produkt 39 ord). Inga andra fel.
- Skrivning: kanarie 3 + batcher om 5 (en mutation med alias per batch), variabler utskrivna av skript med ensure_ascii=True och inklistrade ordagrant. seo skickades med title och description. Inga userErrors.
- Återläsning: högst 4 per fråga, jämförd i python mot skrivfilen (titel, seo.title, seo.description, descriptionHtml, handle, status, taggar, osynliga tecken Cf/Cc): 25 av 25 OK, 0 avvikelser. Kontrollerat maskinellt; inga fält jämförda för hand.
- Leveranstid: "Beställningsvaror kan ta upp till en vecka längre" finns på exakt de 11 produkter som har taggen "På beställning" (kontrollerat före skrivning och i återläsningen).
- Tagg: texter-klara tillagd på alla 25 med tagsAdd; befintliga taggar (inkl. Velomarket, Gymstick, På beställning) kvar.
- Handle, status och pris ändrades inte.
- Anmärkning: återläsningssvaren överfördes till python genom inklistring (transkription), inte direkt från verktyget; alla matchade, så ingen felkälla syntes.
