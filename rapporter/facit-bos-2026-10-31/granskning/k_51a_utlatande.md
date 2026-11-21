# Granskning k_51a (8 utkast), Opus, 2026-11-17

Källa: live-läsning 2026-11-17 (`rapporter/shopify-original-2026-11-17/k_51a_kalla_live_granskning.json`) och webbkoll mot tillverkare och återförsäljare. Utlåtandet i JSON-form finns i `vag2_skriv/k_utlatande_51a.json`. Varje ändring (före → efter) är kontrollerad i python: texten som ändras finns exakt en gång i sitt fält. Efter ändringarna är titeln högst 61 tecken, SEO-titeln (titeln som visas i sökmotorer) högst 37 tecken och metabeskrivningen (texten under länken i sökresultaten) 71–130 tecken. Ingenting har ändrats i Shopify. De avvisade utkasten (`k_51a_avvisade.json`) är tomma. Ingen produkt har taggen "På beställning".

**Resultat:** 5 GODKÄND, 3 RÄTTA, 0 UNDERKÄND.

| nr | Produkt | Dom | Kort skäl |
|---|---|---|---|
| 51001 | Träningshandskar Spokey Lava, svart, XL | GODKÄND | Kort text med bara titelns uppgifter och artikelnummer (v1.12, Davids beslut). Den motsägande meningen är rätt utelämnad. |
| 51002 | Cykelskydd Oxford Aquatex (03-CC100) | RÄTTA | Måtten tas bort. Källan anger 192 x 72 x 110 cm, men tillverkaren och flera återförsäljare anger 200 x 80 x 110 cm (R2). |
| 51003 | Set med cykellampor AXA Niteline 44 | GODKÄND | Brinntid och synlighet står ordagrant i källan och har ett "enligt tillverkaren". |
| 51004 | Cykellyktset AXA Niteline T1 | GODKÄND | Synligheten 2000 m bekräftas av AXA:s egen produktsida. |
| 51005 | Baklykta Giant Recon TL 100 | GODKÄND | Uppgifterna från webben (IPX7, batteri, vikt, mått) gäller exakt artikel 400000169. Hjälmraden är källans egen rad och bekräftas av Giant. |
| 51006 | Ramlås AXA Imenso Large | RÄTTA | 75 mm är låsets öppningsbredd, inte låsets bredd. Orden "än standardutförandet" står inte i källan. Säkerhetsnivå 12 får stå. |
| 51007 | Solglasögon Giant Stratos Lite kat. 3 | GODKÄND | Allt står i källan. Inga UV- eller skyddslöften. |
| 51008 | Glasögon Cairn Flake, Matte Black Fire | RÄTTA | Produkten är solglasögon, men källan säger bara "glasögon". Därför behålls typordet "Glasögon" (R7). |

## Viktigaste fynden
1. **51006, säkerhetsnivå:** Raden "Säkerhetsnivå 12 (skala 1–15)" står ordagrant i källan och är AXA:s egen klassning. Den återges en gång med "enligt tillverkaren", på samma sätt som i det redan skrivna Ramlås AXA Defender Retractable. Det är ingen egen rekommendation (§16.5), och texten lovar inget stöldskydd. Raden godkänns. Rättningen gäller 75 mm: en återförsäljare anger "opening of 75 mm", och med ordet "bredd" krockade siffran med måtten 160 x 170 x 35 mm.
2. **51002, Oxford:** Utkastaren hänvisade till ett beslut av David om att använda källans mått. Något sådant beslut finns inte i beslutsloggen. Beslutet 2026-11-17 gäller bara att produkten skrivs. Måtten går isär mellan källorna (192/200/190 x 72/80), så de utelämnas enligt R2. Kvar blir en kort text med typ, märke, modell, en cykel, artikelnummer och EAN (streckkoden).
3. **51008, Cairn Flake:** Produkten är solglasögon i kategori 3 (hardloop.fr säljer den som "lunettes de soleil" i färgen Mat Black Fire) och hör alltså till en tillåten kategori. Typordet byts ändå inte, eftersom produktens egen källa bara säger "glasögon" (R7). Syskonet Matt Aqua Grafit hette "Solglasögon" redan i butiken. Galaxus anger tillverkningsland Frankrike, men det står inte i källan och tas inte med.
4. **51004, synlighet 2000 m:** AXA:s produktsida anger "To be seen 2000 m". Raden får stå kvar med "enligt tillverkaren".
5. **51005:** Handle (den del av webbadressen som pekar på produkten) slutar på 400000170, men varianten har artikelnumret 400000169. Det numret är Recon TL 100 enligt Giant och återförsäljare. Handle ändras inte.
6. Det finns inga ursprungs-, kvalitets-, hälso- eller stöldpåståenden. Märkestexterna om säkerhet ("115 år", "världsledande") är utelämnade i alla utkast. Titlar och SEO-titlar är unika mot butikens titlar.

## Beslut för David
- **51002, två annonser för samma cykelskydd.** 03-CC100 (EAN 5030009319648) och den redan skrivna 10635765743882 (OXFCC100, EAN 5030009347726) är troligen samma Oxford Aquatex-skydd för en cykel i två utgåvor. Rekommendation: skriv enligt beslutet 2026-11-17 och ta med paret i planen för att slå ihop dubbletter. Risk: två nästan likadana annonser konkurrerar i sökningar. Om inget beslutas skrivs texten utan mått.
- **51008, typord.** Alternativ A (rekommenderas): behåll "Glasögon" enligt R7. Alternativ B: tillåt "Solglasögon" så att namnet blir enhetligt med syskonet. Då blir domen GODKÄND utan ändring. Om inget beslutas gäller A.

## Webbkällor
- https://www.oxfordproducts.com/oxford-aquatex-single-bicycle-cover-cc100.html
- https://www.cycle-technology.co.uk/shop/accessories/sub/bike-covers/oxford-aquatex-single-bicycle-cover-212109810/option/
- https://www.edinburghbicycle.com/accessories/bike-storage-transport/oxford-aquatex-single-bicycle-cover-in-black__615
- https://axabikesecurity.com/?p=18024 (Niteline T1, enligt sökresultat)
- https://www.giant-bicycles.com/fr-ch/recon-tl-100-2020
- https://ekkip-sports.com/en/collections/lumieres-velos/products/recon-tl100
- https://www.bike-components.de/en/Axa/Imenso-Large-Frame-Lock-p88860
- https://www.bikeinn.com/bikeinn/en/axa-imenso-large-75-mm-frame-lock/140390580/p
- https://www.hardloop.fr/produit/78606-cairn-flake-cat-3-lunettes-de-soleil-homme
- https://www.galaxus.ch/en/s8/product/cairn-flake-sunglasses-61043424
