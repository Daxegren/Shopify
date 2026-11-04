# Skrivrapport f_6 (Tunturi/Toorx motions- och minicyklar), 2026-11-04

Butik: BEST OF SPORTS (bestofsports.se), verifierad med get-shop-info. Skrivfil: vag2_skriv/f_skriv_6.json (24 produkter, nr 10126-10150 utom 10142). Före-läge: rapporter/shopify-original-2026-11-04/f_6_fore.json (sparat före skrivning).

- Hoppade över: 0. Alla 24 var ACTIVE, ingen hade texter-klara, ingen hade redan skrivfilens titel.
- Kontrollskript (kopia, --seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70): 0 fel, 25 varningar (rubriken "Passar för" saknar "passar dig som" = känd och godtagen; 10472298250506 saknar Specifikationer = tunn källa). Med standardens meta-min 130 gav 14 meta-längdfel; korta, sanna metabeskrivningar är beslutade (LARDOMAR 2026-11-03).
- Skrivning: productUpdate (title, seo{title,description}, descriptionHtml), mutationerna utskrivna av skript med ensure_ascii=True och inklistrade ordagrant. Kanarie 3, därefter 5+5+5+5+1. userErrors: inga.
- Återläsning av alla 24 (4 per fråga), maskinell jämförelse i python mot skrivfilen: titel, handle (oförändrad), status (ACTIVE), seo.description, descriptionHtml tecken för tecken, seo.title (null när lika med titeln, annars exakt), osynliga tecken (mjukt bindestreck, nollbredd, NBSP) och dubbla mellanslag. 24 av 24 utan avvikelse. För hand: inget.
- På beställning: 12 produkter har taggen och exakt meningen "Beställningsvaror kan ta upp till en vecka längre."; 12 utan tagg saknar meningen (kontrollerat i python mot före-taggar).
- Taggar: texter-klara tillagd på alla 24 med tagsAdd; övriga taggar (inkl. Velomarket, Gymstick, Fell, På beställning) kvar.
- Handle, status och pris: oförändrade (pris rördes aldrig).
- Avvikelser: inga. Notering: 10471002931466 har titeln "Liggande Motionscykel Tunturi Signature E60R" men SEO-titel "Motionscykel Tunturi Signature E60R" (enligt skrivfilen).
- Arbetsfiler (scratchpad): .../scratchpad/f6work/ (mkfore.py, chk.py, mut.py, cmp.py, rb1-7.json).
