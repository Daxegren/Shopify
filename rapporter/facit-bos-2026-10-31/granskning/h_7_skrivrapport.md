# Skrivrapport h_7 (BEST OF SPORTS, bekräftad med get-shop-info), 2026-11-04

Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/h_skriv_7.json` (5 produkter: 10608, 10610, 10611, 10614, 10616). Före-fil: `rapporter/shopify-original-2026-11-04/h_7_fore.json` (5 av 5, live-läsning före skrivning; filen fanns inte och skapades av skrivaren).

## Utfall
- Alla fem ACTIVE, saknade html-struktur och SEO live (seo null/null), ingen hade taggen texter-klara. Ingen hoppades över.
- Ett anrop med 5 productUpdate (utskrift från mutation_fran_skrivfil.py, oförändrad): inga userErrors.
- Återläsning i två läsningar (3 + 2 produkter): title, handle, status, tags, seo.title, seo.description, descriptionHtml. `jamfor_live.py --fore`: 5 av 5 jämförda, 0 avvikelser (maskinellt, tecken för tecken). Handle och status oförändrade mot före-filen. Pris rördes inte.
- Tagg: tagsAdd texter-klara på alla fem sist (inga userErrors); återläsning visar att alla tidigare taggar finns kvar.

## Före/efter (titel)
| nr | före | efter |
|---|---|---|
| 10608 | Boxningshandskar TOORX Jaguar Boxningshandskar L/XL | Boxningshandskar Toorx Jaguar, L/XL |
| 10610 | Stående boxboll TOORX Stående boxboll Professional | Stående Boxboll Toorx Professional |
| 10611 | Boxningshandskar Tunturi Allround Boxing Gloves 12oz | Boxningshandskar Tunturi Allround Boxing Gloves, 12 oz |
| 10614 | Fristående boxningssäck TUNTURI | Fristående Boxningssäck Tunturi, 180 cm |
| 10616 | TUNTURI Free Stand Boxing Dummy | Boxningsdocka Tunturi Free Stand, 155/170/185 cm |

## Särskilda kontroller
- Taggen "På beställning" live: bara 10616 har den. Leveranstidsmeningen ("Beställningsvaror kan ta upp till en vecka längre.") finns i skrivfilen bara på 10616 och inte på de andra fyra: stämmer med R13.
- Felaktiga live-taggen "Cykelväska" på 10610 och 10614 rördes inte (kvar efter skrivning). Velomarket-taggar och övriga taggar oförändrade.
- 10610 och 10611: seo.title lagras som null på 10610 eftersom SEO-titeln är lika med titeln (avsett).
- 10616: live-originalet (engelska) nämner 110 kg sand / 130 kg vatten; skrivfilen utelämnar dem (R4, engelsk lastuppgift). 

## Avvikelser och oklarheter
- Före-filen h_7_fore.json fanns inte vid start; den skapades från live-läsningen före skrivning (inklistrad från verktygsutdata, kontrollerad: 5 poster, tags/handle/status används av jamförelsen). Live-läsningen för jämförelsen sparades i scratchpad (h7work/live.json) och inte i repot; resultatfiler i repot är före-filen och denna rapport.
- Inga egna jämförelseskript användes. Inga avvikelser i egna steg.
- Inget committat (instruktion saknades).
