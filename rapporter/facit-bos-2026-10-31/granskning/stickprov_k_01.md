# Stickprov k_01 (elcyklar), 2026-11-04

Roll: stickprovare, endast läsning. Inget skrevs i Shopify.

## Urval
Alla 45 produkter i k_skriv_01a (20), k_skriv_01b (18) och k_skriv_01c (7) hämtades live och jämfördes, alltså 100 procent (kravet var minst 12 / 20 procent). Samtliga 10 prioriterade (nr 9014, 9015, 9021, 9024, 9032, 9035, 9036, 9042, 9054, 9061) ingår.

## Metod
Live-hämtning med shopify_api.hamta_produkter, 4 id per anrop. Jämförelse tecken för tecken i Python:
titel, seo.title (null jämfört som titeln), seo.description mot meta, descriptionHtml mot html, taggen texter-klara, handle och status, samt osynliga tecken (U+00AD, U+200B, U+200C, U+200D, U+2060, U+FEFF) i titel, SEO-fält, html och handle.

## Resultat
| Fält | Jämförda | Avvikelser |
|---|---|---|
| titel | 45 | 0 |
| seo.title | 45 | 0 |
| seo.description | 45 | 0 |
| descriptionHtml | 45 | 0 |
| tagg texter-klara | 45 | 0 saknas |
| osynliga tecken | 45 | 0 |
| status | 45 | alla ACTIVE |

Alla 45 hade updatedAt 2026-11-04, i linje med att de nyss skrivits.

## Begränsningar
- Bara fälten ovan jämfördes. Varianter, bilder, pris, lager, produkttyp, kollektioner och metafält kontrollerades inte.
- Handle kontrollerades bara för att vara icke-tom och utan blanksteg i kanterna. Handlarna saknar å/ä/ö (till exempel "elcykel-hopf-llbar-ado-a20-air-pro-bl-..."). Det är Shopifys äldre slugifiering och inte en effekt av skrivningen. Ändrades inte.
- "Rimlig status" tolkades som ACTIVE; om några produkter avsiktligen skulle ha varit utkast har det inte kontrollerats mot någon källa.
- Jämförelsen visar läget vid hämtningen och säger inget om senare ändringar.
- Ingen språk- eller regelgranskning av innehållet (det är granskarens uppgift).
