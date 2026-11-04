# Skrivrapport g_1 (BH Fitness / Hammer / Toorx träningsstationer, Velomarket), 2026-11-04

Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info.
Skrivfil: vag2_skriv/g_skriv_1.json (22 produkter; 10384, 10389, 10407 saknas i filen och skrevs inte). Före-läge: rapporter/shopify-original-2026-11-04/g_1_fore.json (22 av 22 id, sparat före skrivning).

## Före / efter
- Före: alla 22 ACTIVE, ingen med texter-klara, SEO-titel och meta null, titlar på formen "Jõujaam/Multi Gym/Power station ...", flera beskrivningar på engelska (10395, 10471310262538 m.fl.) eller med brutna specifikationer. Alla titlar skilde sig från skrivfilen; ingen produkt hoppades över.
- Efter: titel, seo.title, seo.description och descriptionHtml identiska med skrivfilen på 22 av 22. handle och status (ACTIVE) orörda, pris rördes inte.
- Bildblock (Trix/figure/img) i originalbeskrivningarna: inga hittades i någon av de 22.

## Före-fil
Skriven från de råa API-svaren (inklistrade ordagrant som JSON och inläst med python, inte omskrivna). 22 id, descriptionHtml 393-1449 tecken per produkt. Teckenlängd jämfördes inte oberoende mot ett andra läsning; risken är därför begränsad till inklistringsfel i före-filen, inte i skrivningen.

## Kontrollskript (kopia, standardblock markerat, fakta = före-titel + före-text)
Med --seo-title-max 43 --seo-suffix " – BEST OF SPORTS": 12 FEL, alla meta_langd (105-129 tecken, krav 130-155). Med --meta-min 70 (rutinen, kort sann meta godtagen): 0 FEL, 22 VARNINGAR (bara "passar dig som", känd och godtagen).

## Skrivning
Kanarie 3 (0-3), därefter 5+5+5+4. Varje mutation skrevs ut av python-skript (json.dumps ensure_ascii=True) och klistrades in. userErrors tomma i alla anrop. Seo skickades alltid med title och description.

## Återläsning
Alla 22 återlästa (högst 4 åt gången) och jämförda i python (titel, seo.title, seo.description, descriptionHtml, handle mot före, status, osynliga tecken Cf/Zs): 22 av 22 identiska, 0 osynliga tecken. Återläsningen klistrades in i filer för hand (MCP-svar nås inte från bash); en felkopiering skulle ge falsk avvikelse, inte falsk överensstämmelse. Ingen omskrivning behövdes. Handtaggar jämfördes mot före-filen.

## Taggar
texter-klara tillagd på alla 22 med tagsAdd, inga userErrors. Svaret visar att övriga taggar (BH Fitness, Hammer, Toorx, Velomarket, På beställning m.fl.) finns kvar.
"På beställning": 20 produkter har taggen och 20 har meningen "Beställningsvaror kan ta upp till en vecka längre"; 10376 och 10381 saknar både tagg och mening. Matchar exakt (kontrollerat i python mot före-taggarna).

## Avvikelser
Inga. Notering: Velomarket-handles innehåller gamla ord (t.ex. "j-ujaam-...", "multi-gym-...") och rördes inte, enligt regeln.
