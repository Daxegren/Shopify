# Våg 2c kanarie (Gymstick, 3 produkter) – skrivrapport 2026-11-02

Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info före skrivning. Skrivfil: `vag2_skriv/c_skriv_kanarie.json`. Före-läge: `rapporter/shopify-original-2026-11-02/vag2c_kanarie_fore.json` (sparat före skrivning).

## Före
Alla tre ACTIVE. SEO-titel och SEO-beskrivning tomma (null) på alla tre. Beskrivningen var leverantörens marknadsföringstext (till exempel "din perfekta partner", "optimal träningsupplevelse").

| Nr | Id | Titel före | Titel efter |
|---|---|---|---|
| 3006 | 10581095743754 | Aktiv 2-toners träningsmatta, blå-svart | Träningsmatta Gymstick Aktiv, 2-toners, Blå och Svart |
| 3038 | 10581101084938 | Court Proshot Dartboard | Dartskiva Gymstick Court Proshot |
| 3103 | 10581106622730 | Golvskyddsmatta 160 x 80 x 0,6 cm | Golvskyddsmatta Gymstick, 160 x 80 x 0,6 cm |

## Kontrollskriptet (kopia, html mappad till beskrivning, standardblock markerat, --seo-title-max 43 --seo-suffix " – BEST OF SPORTS", källtext = före-läget)
Resultat: 3 produkter, 0 FEL, 3 VARNINGAR. Varningarna: "saknar avsnittet 'passar dig som'" på alla tre. Texterna använder rubriken "Passar för", i enlighet med skrivfilen; ingen åtgärd gjord, bedöms av granskare.

## Skrivning
productUpdate(product: ProductUpdateInput) med title, seo{title, description}, descriptionHtml. userErrors: inga för alla tre. Handle och status skickades inte.
- 3006 och 3103: seo.title och seo.description skickades båda.
- 3038: meta är null i filen och live hade ingen beskrivning, så bara seo.title skickades (identisk med titeln).

## Återläsning (alla fält: title, handle, status, seo.title, seo.description, descriptionHtml)
Jämfört för hand, tecken för tecken, mot filen. Ingen maskinell diff (MCP-utdata kan inte diffas i bash).
- title: lika med filen på alla tre.
- handle: oförändrade (aktiv-2-toners-traningsmatta-bla-svart, court-proshot-dartboard, golvskyddsmatta-160-x-80-x-0-6-cm).
- status: ACTIVE på alla tre.
- seo.title: 3006 och 3103 lika med filen. 3038: null, avsett (Shopify lagrar tomt när SEO-titeln är lika med titeln).
- seo.description: 3006 och 3103 lika med filen. 3038: null, lika med filens meta (null).
- descriptionHtml: lika med filen på alla tre, inklusive radbrytning mellan `<li>` (avsett, Shopify lägger dit den; filen har samma), standardblocket och säljaruppgifterna.

## Avvikelser
Inga. Reservation: jämförelsen är gjord för hand. Titelns synk-risk (LARDOMAR 2026-10-30): läs tillbaka titlarna igen efter nästa nattsynk av Velomarket/Gymstick-produkter.
