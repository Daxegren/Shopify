# Skrivrapport f_4 (2026-11-04)

Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info. Skrivfil: vag2_skriv/f_skriv_4.json (19 produkter, nr 10076-10099 utom 10085, 10087, 10093, 10094, 10100). Före-läge: rapporter/shopify-original-2026-11-04/f_4_fore.json.

- Skrivna: 19 av 19. Hoppade över: 0 (alla ACTIVE, ingen tagg texter-klara, alla titlar skilde sig från skrivfilen).
- Före: seo.title och seo.description var null på alla 19. Efter: titel, SEO-titel, meta och beskrivning enligt skrivfilen.
- Kontrollskript på kopia (html mappad till beskrivning, standardblock markerat, --seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70): 0 FEL, 19 VARNINGAR (rubriken "Passar för", känd och godtagen). Med standardgränsen meta-min 130 gav 13 produkter metalängd 106-129 tecken; godtaget enligt beslut om kort sann meta.
- Skrivning: kanarie 3, därefter 5+5+5+1 (högst 5 per productUpdate), mutationer utskrivna av skript med ensure_ascii=True.
- Avvikelse: 10078 (Ergo EMS) skrevs första gången med en tappad mening i Retur-stycket ("Vid ångrat köp står du för returfrakten") när jag klistrade in kanariemutationen. Upptäcktes vid återläsning, skrevs om med skriptets utskrift och verifierades OK. Övriga 18: 0 avvikelser.
- Återläsning: alla 19 (högst 4 åt gången) jämförda maskinellt i python mot skrivfilen: titel, seo.title (null tillåtet endast om lika med titeln), seo.description, descriptionHtml tecken för tecken, status ACTIVE, kontroll av osynliga tecken (Cf/Zs/styrtecken). Alla 19 OK. Handle oförändrad. (Återläsningstexten fördes till python genom inklistring; skillnad hade synts som avvikelse.)
- På beställning: taggen finns på 10076, 10078, 10083, 10084, 10090 och bara de har meningen "Beställningsvaror kan ta upp till en vecka längre". Kontrollerat före skrivning.
- Tagg: texter-klara tillagd på alla 19 med tagsAdd; återläst, alla befintliga taggar (inkl. Velomarket, Hammer, BH Fitness, På beställning) finns kvar.
- Ändrades inte: handle, status, pris, andra taggar. Inget committat.
