# Skrivrapport h_2 (Velomarket, golvskydd/mattor/ställ), 2026-11-04

Butik: BEST OF SPORTS (bestofsports.se), bekräftat med get-shop-info. Skrivfil: vag2_skriv/h_skriv_2.json (25 produkter, nr 10433, 10435, 10437, 10447-10468). Före-läge: rapporter/shopify-original-2026-11-04/h_2_fore.json.

## Före
- Alla 25 lästes live, status ACTIVE, ingen hade taggen texter-klara, ingen hade titel+seo+beskrivning lika med skrivfilen. Inga produkter hoppades över.
- Före-filen: 25 av 25 id, ingen avkortad (längder på beskrivning 136-1891 tecken, hämtade ur live-svaret via skript, inte handskrivna). Originalens SEO var null överallt.
- Bildblock (Trix/<img>) i originalbeskrivningarna: inga fanns, ingenting försvinner.
- Originalen innehöll leverantörstext (Tunturi-motto, app-reklam m.m.) som ersätts; produkttitlar ändrade (t.ex. "Squat Rack" blir "Knäböjsställ").

## Kontroll på kopia
kontrollera_produkttext.py (--seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70): 25 produkter, 0 FEL, 25 varningar (alla "saknar avsnittet 'passar dig som'", dvs. rubriken "Passar för", känd och godtagen).

## Skrivning
- Skript (gen.py) skrev ut varje mutation med json.dumps(ensure_ascii=True); utskriften klistrades in oförkortad. Max 5 produkter per productUpdate-anrop. Kanarie 3 (10433, 10435, 10437), därefter 5+5+5+5+2. seo skickades alltid med både title och description. 0 userErrors.
- Handle, status och pris ej rörda. Standardblocket (inkl. Märke/Retur/Reklamation/Säljare) finns i alla 25.
- På beställning-taggen: finns på exakt 10437 och 10459, och exakt de två har meningen "Beställningsvaror kan ta upp till en vecka längre" (maskinkontroll mot taggar).

## Återläsning (högst 4 produkter per fråga) och jämförelse i python
Jämfört maskinellt (ver.py, tecken för tecken): title, seo.title (null godtogs när lika med titeln), seo.description, descriptionHtml (exakt lika, inkl. radbrytningar), handle och status oförändrade, tagglista oförändrad, inga osynliga tecken (kategori Cf/Cc, NBSP). Resultat: 25 av 25 OK, 0 avvikelser, ingen omskrivning behövdes. Ingenting jämfördes för hand.
Obs: återläsningstexten klistrades in i jämförelseskriptet, så jämförelsen fångar även eventuella inklistringsfel (inga uppstod).

## Taggning
tagsAdd texter-klara på alla 25, 0 userErrors. Kontrollläsning av taggar: alla tidigare taggar kvar (inkl. Velomarket, Gymstick på 10437, "Vikbar cykel" på 10463, På beställning), texter-klara tillagd. Inga andra taggar rörda.

## Avvikelser / att notera
- 10437 (Träningsställ Tunturi PT60, ställ med last) och 10433/10435 (knäböjs-/hantelställ) ligger under säkerhetskategorin "ställ med last" i standard §10; skrivna enligt Davids uppdrag, lastuppgifter "enligt tillverkaren".
- Token för Admin API saknas i miljön; skrivning gjordes via MCP-verktyget.
- Ingen ändring i Shopify utöver title, seo, descriptionHtml och taggen texter-klara på de 25 produkterna.
