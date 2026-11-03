# Stickprov tillbehör grupp 6 (b_skriv_6.json), 2026-11-03

Kontrollant: Sonnet, endast läsning. Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info.

## Urval (10 av 40)
8098, 8099, 8107, 8118, 8130, 8135, 8138, 8147, 8151, 8155.
- Titel lika med SEO-titel: 8118, 8135, 8138, 8147, 8155.
- Rättade utlåtanden (b_utlatande_24_25.json, dom RÄTTA): 8099, 8118, 8130, 8138, 8147, 8151.
- Utan meta i filen: 8098. Beställningsvaror (standardblock med längre leveranstid): 8099, 8147, 8151, 8155.

## Resultat: inga avvikelser
Jämfört tecken för tecken i python mot skrivfilen: titel, SEO-titel (live null där filen har SEO-titel lika med titeln; 8118, 8135, 8138, 8147, 8155 bekräftade), seo.description lika med filens meta (8098: null som i filen), beskrivning före standardblocket. Standardblockets text och beställningsvarumeningen kontrollerades mot filen.

| nr | titel | SEO live | meta (tecken) | taggen texter-klara | status |
|---|---|---|---|---|---|
| 8098 | lika | lika | null = null | ja | ACTIVE |
| 8099 | lika | lika | lika (150) | ja | ACTIVE |
| 8107 | lika | lika | lika (149) | ja | ACTIVE |
| 8118 | lika | null (= titel) | lika (151) | ja | ACTIVE |
| 8130 | lika | lika | lika (146) | ja | ACTIVE |
| 8135 | lika | null (= titel) | lika (153) | ja | ACTIVE |
| 8138 | lika | null (= titel) | lika (138) | ja | ACTIVE |
| 8147 | lika | null (= titel) | lika (130) | ja | ACTIVE |
| 8151 | lika | lika | lika (148) | ja | ACTIVE |
| 8155 | lika | null (= titel) | lika (136) | ja | ACTIVE |

Längder: titlar 34-50 tecken (max 70), SEO-titlar 31-42 (max 43), metor 130-153 (130-155). Handle oförändrade, övriga taggar bevarade.

## Faktakontroll mot före-filen (vag2b_6_fore.json)
Alla tal, mått, material och funktionspåståenden finns i före-texten. Leverantörens förstärkningar är utelämnade ("världens största cykeltillverkare", "tillverkad i Tyskland" för 8151, "toppklass", "utmärkt skydd", "stilren och högkvalitativ"). Trasig data (155.15 x 15.15 mm i 8155) är inte använd. Osäkra uppgifter har "enligt tillverkaren" (8099 däckbredd, 8130 smakfri, 8135 kvinnas hand, 8138 lufttät anslutning, 8147 kompatibilitet, 8155 vattentät). Inga arbetstermer, utropstecken, superlativ, priser eller hälsopåståenden. "Handtagstejp" (inte Styrlinda) enligt avsnitt 12. Stor bokstav efter kolon och i titlar följs.

## Observationer (ingen åtgärd krävs)
- 8135: "Handskarna finns i storlek M och L" saknas i leverantörstexten men stöds av varianterna (M / blue, L / blue). Varianternas färgnamn "blue" stämmer inte med "Soap Suds" i titeln; texten påstår inte blått.
- 8099 har sedan före en tagg "Skidor" som inte passar en stänkskärm (finns i före-filen, ändrades inte av skrivningen).
- 8099 har en tom rad mellan två listpunkter i beskrivningen; den finns även i skrivfilen (Shopify-radbrytning), avsett.
