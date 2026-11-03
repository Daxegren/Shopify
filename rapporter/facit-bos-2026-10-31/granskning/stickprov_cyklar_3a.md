# Stickprov cyklar 3a (k_skriv_3a.json), 2026-11-03

Kontrollant: Sonnet (endast läsning, inget skrivet i Shopify). Butik bekräftad med get-shop-info: BEST OF SPORTS, bestofsports.se.

## Resultat
Kontrollerade: 10 av 28. Avvikelser mellan live och skrivfil: 0. Sakfel mot källan: 0. Formatavvikelser: 0.

| Nr | Produkt | Anledning till urval | Resultat |
|---|---|---|---|
| 7005 | Giant Roam 1 | första produkten | OK |
| 7025 | Giant Reign Advanced 2 | rättat utlåtande (meta: "29-tumshjul") | OK, rättningen finns live |
| 7032 | Liv Tempt 1 GE | rättat utlåtande (titel och SEO: komma före hjulstorlek) | OK, rättningen finns live |
| 7045 | Kona Unit | spridning | OK |
| 7050 | Liv Rove 2 | rättat utlåtande ("med låsning") | OK, rättningen finns live |
| 7059 | Giant Defy Advanced 2 | landsväg | OK |
| 7060 | 6KU Troy | rättat utlåtande (tillbehörspunkten) och tunn källa | OK, rättningen finns live |
| 7081 | Kona Fire Mountain | däckbredd struken, rättat utlåtande ("XS: WTB Ranger") | OK, ingen däckbredd, rättningen finns live |
| 7085 | Kona Rove LTD | gravel | OK |
| 7088 | Liv Avail AR 1 | damcykel, landsväg | OK (se observation) |

## Metod
- Live hämtat med graphql_query (title, handle, status, tags, seo, descriptionHtml) och jämfört tecken för tecken mot titel, seo_title, meta och html i skrivfilen (script i scratchpad, jämförelsen utfördes maskinellt). Hela standardblocket (leverans, retur, reklamation, säljare) är identiskt med skrivfilen för alla tio.
- seo.title: 7060 lagras null (SEO-titel lika med titeln, avsett). Övriga nio har seo.title lika med skrivfilen.
- Alla tio: status ACTIVE, taggen `texter-klara` finns, övriga taggar oförändrade (Velomarket, På beställning med flera).
- Längder: titel 21-59 tecken (max 70), SEO-titel 21-42 (max 43; 7081 är högst med 42), meta 137-149 (130-155). Högst två kommatecken i titlarna. Unika titlar i urvalet.
- Format: stor bokstav efter kolon i alla specifikationsrader, enheter (tum, mm) med liten bokstav, "Växlar" med stor bokstav i titeln 7005. Inga utropstecken, superlativ, köpuppmaningar, priser eller arbetstermer. Stavning kontrollerad, inga fel funna.
- Fakta: varje uppgift (ramar, gafflar, växelsystem, antal växlar, bromsar, däck, hjulstorlek, fästpunkter) spårad mot före-filen `rapporter/shopify-original-2026-11-03/vag2k_3a_fore.json`. Inga påhittade fakta. Ursprung/märkesbakgrund, "världens största", "grundat 1972", rolltexter (Kona Unit), "punkteringsskydd", 6KU:s "Kalifornien"/"Del Rey"/"Fixiede" är rätt utelämnade. "Designat för kvinnor" (7088) står som "enligt tillverkaren".
- 7081 Kona Fire Mountain: däckbredden (2,25) saknas som avsett. Live: "Däck: WTB Trail Boss (XS: WTB Ranger)"; hjulstorlek "26, 27,5 eller 29 tum, beroende på ramstorlek" stämmer med källan.
- Elektronisk växling/batteri: ingen text nämner eller antyder Di2, AXS, motor eller batteri. Samtliga tio är cyklar utan motor.

## Avvikelser
Inga.

## Observation (ingen avvikelse, för David att veta)
- 7088 Liv Avail AR 1 och 7085 Kona Rove LTD har 24 växlar (2x12). Källan säger "Shimano 105" respektive "Shimano GRX" utan Di2. Utlåtandet för 7085 resonerar att det är mekaniskt; utlåtandet för 7088 tar inte upp frågan, och utlåtandet för 7059 noterar att 105 med 12 växlar kan vara Di2. Texten påstår ingenting om mekanisk eller elektronisk växling, så regeln är uppfylld, men om leverantörens uppgift "Shimano 105" i själva verket är Di2 saknas det i texten (utelämnande, inte felaktigt påstående). Kan bekräftas hos leverantören om David vill.
- 7032: utlåtandets "efter" för SEO-titeln är "Liv Tempt 1 GE, 27,5 tum" men skrivfilen och live har "Liv Tempt 1 GE, 27,5 tum, Milky Way" (före var "Liv Tempt 1 GE 27,5 tum, Milky Way"; utlåtandet förkortade bara ändringen). Korrekt.
