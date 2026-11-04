# Skrivrapport f_15ok (BEST OF SPORTS, Velomarket), 2026-11-04

- Butik verifierad: BEST OF SPORTS (bestofsports.se). Skrivfil: `vag2_skriv/f_skriv_15ok.json` (9 produkter, nr 10353, 10355, 10356, 10357, 10359, 10364, 10371, 10374, 10375).
- Live före skrivning: alla ACTIVE, ingen med taggen texter-klara, titel/seo/beskrivning skilde sig från skrivfilen (original-Velomarket-text, seo null). Ingen var delvis skriven (kontrollerat för att en tidigare skrivagent stoppats); ingen hoppades över. Före-läge sparat i `rapporter/shopify-original-2026-11-04/f_15ok_fore.json` före skrivning.
- Före-filen: id-antal 9 och teckenlängd per beskrivning noterade; originalbeskrivningarna innehåller inga bildblock (Trix, inga img/figure), inget försvann. Notering: min första inklistring av före-filen tappade en rad (Hammer Force 6.0: "Max. belastningskapacitet: 250 kg"); kontrollskriptet fångade det som tal_utan_kalla, före-filen rättades mot live och kontrollen kördes om.
- Kontrollskriptet (kopia, standardblock inom [[STANDARDBLOCK]], --seo-title-max 43 --seo-suffix --meta-min 70, källtext = före-läget): 0 fel, 13 varningar (bara "Passar för", känd och godtagen). Standardblocket verifierat i python tecken för tecken lika med referensblocket (utöver På beställning-meningen).
- Skrivning: 9 produkter i 2 anrop (5 + 4).. Varje mutation utskriven av `f1415work/gen.py` (json.dumps ensure_ascii=True, vägrar osynliga tecken) och inklistrad ordagrant. Alla userErrors tomma.
- Återläsning (högst 4 per fråga) jämförd tecken för tecken i python (`cmp.py`: title, seo.title (null = titeln), seo.description, descriptionHtml samt handle, status, taggar mot före): 9 av 9 OK, inga avvikelser, ingen omskrivning. Maskinellt; inget för hand.
- 'På beställning': taggen finns bara på 10375 och endast den har meningen 'Beställningsvaror kan ta upp till en vecka längre.' (kontrollerat i python för alla 9).
- Taggen texter-klara lades sist med tagsAdd (inga userErrors); återläst: alla tidigare taggar kvar (Velomarket m.fl. orörda), status ACTIVE, handle oförändrad.
- Ändrat i Shopify: titel, seo, beskrivning och en tagg på 9 produkter. Handle, status och pris ändrades inte. Committat ingenting.
- Arbetsmapp: `/tmp/claude-0/-home-user/fbbd95a3-8b18-5096-a6b5-20df3e4eb235/scratchpad/f1415work/`.
