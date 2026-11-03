# Skrivrapport våg 2b, skrivfil 17 och 18 (2026-11-03). Delvis genomförd, stoppad.

## Status
- Skrivfil 17 (24 produkter): ej klar. Kanarie om 3 skrev (se nedan). Resten är inte skrivet. Ingen tagg "texter-klara" satt.
- Skrivfil 18 (17 produkter): inte påbörjad.
- Avbrott: återläsningen kan inte göras maskinellt. Shopify-verktyget returnerar resultatet inline när det är under ca 50 000 tecken, och då går det inte att jämföra i python utan att skriva av texten för hand. Den som ska jämföra tecken för tecken behöver en återläsning som sparas till fil.

## Skrivfil 17
- Live-läge före skrivning sparat: rapporter/shopify-original-2026-11-03/vag2b_17_fore.json (24 noder, alla ACTIVE, ingen med taggen texter-klara).
- Hoppade över (titel redan lika skrivfilen, enligt regeln): tre produkter: 10472298053898 (ADO Air 30 Pro, Meteor Grey), 10472298414346 (ADO Air 30 Pro, Forest Green), 10472303493386 (ADO Air One Ultra, Grå). Dessa har inte skrivits av denna körning. Deras beskrivning är inte kontrollerad mot skrivfilen.
- Kontrollkopia: rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2b17/kopia.json (21 produkter). kontrollera_produkttext.py med --seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70: 0 FEL, 48 VARNINGAR. Varningarna är "saknar avsnittet 'passar dig som'" (rubriken heter "Passar för", känd och godtagen) och engelska färgnamn (Grey, Black, Green, Blue) i produktnamn från källan.
- Kanarie (3 produkter, productUpdate med seo{title, description}): 10472291500298, 10472291729674, 10472293040394. userErrors tomma. Svaret visar handle oförändrat, status ACTIVE, seo.description som skrivfilen, titel och beskrivning enligt skrivfilen. För p0 och p1 är seo.title null eftersom den är lika med titeln (avsett beteende). Detta är visuellt kontrollerat, inte maskinellt.
- Ej gjort: återläsning sparad till fil, tecken-för-tecken-jämförelse, batcher 4–24, tagg texter-klara.

## Ändrat
- Shopify: ja, tre produkter i fil 17 (kanarie): title, seo och descriptionHtml. Inga handle-, status-, pris- eller taggändringar.
- Filer: vag2b_17_fore.json (ny), tmp_kopia_vag2b17/ (ny), denna rapport (ny).

## Nästa steg (kräver beslut)
1. Godkänn att återläsningen görs med en fråga som överstiger ca 50 000 tecken så att svaret sparas till fil, eller att återläsningen görs på annat sätt. Utan det kan skrivningen inte fortsätta enligt reglerna.
2. Avgör de tre hoppade produkterna (ADO Air 30 Pro x2, ADO Air One Ultra): om titeln redan är skriven ska beskrivning och meta kontrolleras mot skrivfilen innan de tas med.
3. Skrivfil 18 är ännu inte påbörjad och ska göras med samma process.
