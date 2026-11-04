# Skrivrapport 14rest (BEST OF SPORTS, Velomarket), 2026-11-04

- Butik verifierad: BEST OF SPORTS (bestofsports.se). Skrivfil: `vag2_skriv/f_skriv_14rest.json` (13 produkter). Före-läge: `rapporter/shopify-original-2026-11-04/f_14rest_fore.json` (sparat före skrivning).
- Före-filen: id-antal och teckenlängd per beskrivning noterade vid läsning; inga bildblock (Trix, img, figure) i originalen, inget försvann. 
- Live före: alla ACTIVE, ingen med texter-klara. 10326, 10327, 10328 hade redan exakt skrivfilens titel, seo och beskrivning (kontrollerat i python, alla tre fälten lika, ev. pilotens text som är identisk): ingen ny skrivning, endast tagg. Övriga 10 skilde sig.
- Kontrollskript (kopia, standardblock i [[STANDARDBLOCK]], --seo-title-max 43 --seo-suffix --meta-min 70): 0 fel; varningar bara "Passar för" (känd) samt kort beskrivning (35 resp. 39 ord) på 10334 och 10337 (tunna produkter, godtaget). Standardblocket tecken för tecken lika med referensen (utom På beställning-meningen).
- Skrivning: 10 produkter i 3 anrop (kanarie 3 + 5 + 2 med 15rest-batchar delade); 3 redan lika. Mutationer utskrivna av gen.py (json.dumps ensure_ascii=True) och inklistrade ordagrant, userErrors tomma.
- Återläsning (högst 4 per fråga), jämförd maskinellt tecken för tecken i python (title, seo.title, seo.description, descriptionHtml, handle, status, taggar mot före): alla OK, inga avvikelser, ingen omskrivning.
- På beställning: sats och tagg sammanfaller på alla (assert i skript).
- texter-klara lades sist med tagsAdd på alla 13; taggarna återlästa: alla tidigare taggar kvar (Velomarket/Gymstick orörda), status ACTIVE, handle oförändrad.
- Ändrat i Shopify: titel, seo, beskrivning och en tagg. Handle, status och pris orörda. Committat ingenting.
- Arbetsmapp: /tmp/claude-0/-home-user/fbbd95a3-8b18-5096-a6b5-20df3e4eb235/scratchpad/frest/
