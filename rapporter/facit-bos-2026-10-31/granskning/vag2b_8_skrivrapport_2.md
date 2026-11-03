# Skrivrapport Velomarket vinter, våg 2b, grupp 8, omstart (26 produkter)

Status: **STOPPAD före skrivning.** Ingen produkt skrevs i Shopify. Inga taggar lades till. Ingen produkt ändrad.

## Kontroller
- Butik: BEST OF SPORTS (bestofsports.se), bekräftad via get-shop-info.
- Live-läsning: alla 26 lästa (nodes, 2 anrop). Alla ACTIVE. Ingen har taggen `texter-klara`.
- Originalet före skrivning finns kvar: `rapporter/shopify-original-2026-11-03/vag2b_8_fore.json` (26 poster). Det används som före-läge.
- Skrivfilen `b_skriv_8.json` är ändrad sedan förra skrivrapporten: produkt 10494685380874 (8344) innehåller nu inga varianttal (125/135/160). Det FEL som stoppade förra försöket är alltså åtgärdat i filen. Kontrollskriptet kördes inte om i denna omgång.

## Klassning från live-läsning (titel, SEO-titel, handtag, status)
- **Klass B, oskriven (11 produkter):** 8325, 8326, 8327, 8328, 8330, 8331, 8333, 8334, 8340, 8343, 8344. Live-titlar är kvar på engelska eller i leverantörens form, och SEO-titel är null.
- **Troligen skriven, men ej verifierad (15 produkter):** 8302, 8303, 8305, 8306, 8308, 8311, 8313, 8315, 8316, 8317, 8318, 8320, 8321, 8322, 8323. Live-titel och SEO-titel är lika med skrivfilen. Beskrivning (descriptionHtml) och seo.description är inte jämförda fält för fält. Klass A (bara tagg) eller B (skriv om) kan därför inte avgöras säkert.

## Varför stoppad
Steg 3 och 5 i uppdraget kräver att alla fält jämförs tecken för tecken i python mot skrivfilen. Live-texten finns bara i svarsdata i agentens kontext och kan inte skickas till python utan att kopieras för hand. Den handkopieringen av ~40 000 tecken per läsning har redan gett fel i denna omgång, och en hand-kopierad jämförelse skulle inte räcka som verifiering. Mutationer för klass B skulle dessutom skrivas med ett utskriftsskript som klistras in, och återläsningen skulle behöva samma handkopiering. Därför skrevs inget.

## Nästa steg (kräver beslut)
1. Hämta live-data för 26 produkter till en fil via ett verktyg som kan skriva filer (exempelvis en export av nodes-svaret till JSON), så att jämförelsen kan göras maskinellt.
2. Därefter: klassning A/B för de 15, skrivning av 11 (klass B) i batcher om högst 6 med kanarie om 3, återläsning, tagg sist.
3. Alternativt: David godkänner att de 15 får taggen utan full jämförelse, vilket inte är verifierat.
