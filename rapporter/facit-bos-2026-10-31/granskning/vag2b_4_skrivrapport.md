# Skrivrapport: Velomarket våg 2b, batch 4 (3 produkter, kanarie)

Datum: 2026-11-03. Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info före skrivning.
Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/b_skriv_3.json`. Före-läge: `rapporter/shopify-original-2026-11-03/vag2b_4_fore.json`.

## Före och efter

| Produkt (id) | Fält | Före | Efter |
|---|---|---|---|
| 10475980161290 (nr 5275) | titel | Cykelkorg Basil Cairo Luxe för pakethållare | Cykelkorg Basil Cairo Luxe för Pakethållare |
| | seo.title | (null) | Cykelkorg Basil Cairo Luxe |
| | seo.description | (null) | (null), oförändrat |
| | beskrivning | Basil-brödtext, 4 punkter | Ny text enligt skrivfilen |
| 10470908264714 (nr 5245) | titel | Giant Connect Gel Handtagstejp, vit/röd | Handtagstejp Giant Connect Gel, Vit och Röd |
| | seo.title | (null) | Handtagstejp Giant Connect Gel |
| | seo.description | (null) | (null), oförändrat |
| | beskrivning | Giant-brödtext, en div | Ny text enligt skrivfilen |
| 10472252375306 (nr 5268) | titel | LIV Contact SL styretape, vit | Handtagstejp Liv Contact SL, Vit |
| | seo.title | (null) | Handtagstejp Liv Contact SL |
| | seo.description | (null) | Ny metabeskrivning enligt skrivfilen |
| | beskrivning | Liv-brödtext, en div | Ny text enligt skrivfilen |

Alla tre var ACTIVE före och efter. Handle är oförändrad på alla tre. Taggar: Basil, Cykelkorg, Pakethållare, Tillbehör, Velomarket (plus texter-klara); Giant, Tillbehör, Velomarket (plus texter-klara); Liv, Tillbehör, Velomarket (plus texter-klara). Befintliga taggar finns kvar.

## Hoppade över

Inga. Alla tre var ACTIVE, saknade taggen "texter-klara" och hade titlar som skiljer sig från skrivfilen.

## Kontroll före skrivning

Kontrollskriptet kördes på en kopia (html mappad till beskrivning, standardblocket inom [[STANDARDBLOCK]], fakta = före-läget, `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS"`). Resultat: 3 produkter, 0 FEL, 4 VARNINGAR.

- Tre VARNINGAR gäller att rubriken "Passar för" saknas i kontrollens lista över avsnitt ("passar dig som"). Det är den kända och godtagna varningen.
- En VARNING gäller ordantal: produkt 10475980161290 har 27 ord, under kontrollens förväntade intervall 40–450. Det är en bedömning för granskaren och ingen felaktighet. Texten är kort eftersom källan (före-texten) är kort. Den är inte stoppad.

Inga kommatecken i mått i titlarna. Inga produkter behövde lyftas till handläggning.

## Skrivning

- Ett productUpdate-anrop med alla tre produkter (aliasen a, b, c). `product:`-argumentet användes. Inga userErrors.
- seo skickades med bara title för de två produkterna där meta var null (10475980161290, 10470908264714). Meta förblev null.
- seo skickades med både title och description för 10472252375306.
- Shopify lagrar seo.title som null när den är lika med titeln. Det gäller inte här eftersom alla tre SEO-titlar skiljer sig från produkttiteln.

## Kontroll efter skrivning (läst tillbaka)

Alla fält lästes tillbaka live med en ny query: title, handle, status, tags, seo.title, seo.description, descriptionHtml.

- Titlar, seo.title och seo.description: jämförda för hand mot skrivfilen. Stämmer på alla tre.
- Handle och status: jämförda mot före-läget. Oförändrade.
- descriptionHtml: jämförd för hand mot skrivfilen, ett fält i taget. Stämmer. Shopify har lagt radbrytning mellan li-elementen och tagit bort seo.title-värdet när det är identiskt med titeln, det är avsett enligt standarden.
- Taggar: jämförda för hand. "texter-klara" finns på alla tre och befintliga taggar finns kvar.

Maskinellt: inga. Jämförelsen gjordes för hand, eftersom MCP-svar inte kan diffas i bash. Det är inte en byte-för-byte-jämförelse. Standardblocket, som är identiskt i alla tre texterna, lästes igenom i sin helhet på varje produkt.

## Taggning

"texter-klara" lades till med tagsAdd på alla tre. Inga userErrors. Verifierades i en läsning efter taggningen.

## Avvikelser

Inga avvikelser mot skrivfilen. Det enda som avviker från en ren "lika med filen" är det som standarden förutser: radbrytning mellan li-element, och seo.title som null när den är identisk med titeln (gäller inte här).

## Ändrat i Shopify

Ja: titel, seo (title, och för 10472252375306 även description), descriptionHtml och taggen "texter-klara" på tre produkter. Inget annat. Ingen handle eller status ändrades.

Ingen commit gjordes.
