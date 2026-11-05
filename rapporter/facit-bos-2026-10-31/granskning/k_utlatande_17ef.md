# Granskning väg 2, k_17e och k_17f (2026-11-05)

Oberoende granskning (Opus, endast läsning) av 2 utkast: `vag2_skriv/k_17e_utkast.json` (10111 Liv Tempt 2 GE) och `vag2_skriv/k_17f_utkast.json` (9016 Engwe E26 ST), enligt regelboken v1.4–v1.7. Butiken bekräftades live: BEST OF SPORTS (6f2e53-67.myshopify.com). Källorna hämtades live på nytt via `shopify_api.py`. Båda produkterna är ACTIVE, saknar SEO och saknar taggen "På beställning" (därför ingen leveranstidsmening, vilket är rätt). Jag öppnade nätkällorna själv. Sökning i butiken på Tempt, E26 och SKU gav inga dubbletter. Inget ändrat i Shopify.

**Resultat:** 1 GODKÄND, 1 RÄTTA, 0 UNDERKÄND.

## Särskilda frågor
- **10111, Default Title enligt v1.7:** Default Title (13 339 kr) och M / green (11 599 kr) har samma SKU 2201135185 och samma EAN. Default Title saknar färg. Det är samma mönster som i 10113 och 10117, så v1.7 gäller. Titeln låser varken färg eller pris.
- **9016, räcker återförsäljarkällor?** Frågan behöver inte avgöras. Engwes egen E26-sida har en gemensam specifikationstabell för High-Step och Step-Thru (ST). Batteri 48V 16Ah (= 768 Wh), aluminium, Shimano 7 växlar, hydrauliska bromsar, 26 x 4.0 och max last 150 kg gäller därför båda. Bara vikten skiljer. Återförsäljarsidorna ensamma hade inte räckt:
  - decathlon.ie svarade 404 och ypc.co.uk svarade 403.
  - electrotraveller säger emot sig själv om lasten (120 kg mot 150 kg).
- **9016, lastkapacitet:** får stå. Raden "Lastkapacitet: 150 kg" i live-källan är svensk, ordagrann och har etikett och enhet. Tillverkaren anger samma maxlast. Uppgiften skrivs en gång med "enligt tillverkaren" (R4). Det är samma bedömning som för 9017 (k_utlatande_01d).
- **9016, rättning:** längdintervallet 165–195 cm stryks. Källan beskriver E26 i allmänhet, och uppgiften motsägs av tillverkaren (170–200 cm) och electrotraveller (168–195 cm). Enligt R2 utelämnas uppgifter som motsägs.

| nr | id | dom | före → efter / skäl |
|---|---|---|---|
| 10111 | 10474079518986 | GODKÄND | **Varianter:** samma SKU och samma EAN på båda varianterna, och Default Title saknar färg. Därför gäller v1.7 och prejudikaten 10113 och 10117. Det är rätt att stryka "Ocean Wave" (varianten heter green). **Fakta:** allt står ordagrant i live-källan: ALUXX-Grade aluminium, Suntour SF22-X1-Coil RLR DS 100 mm, Alivio M3120, Deore M592, Deore BR-MT200 med hydrauliska skivbromsar, Kenda Booster 27,5 x 2,2 (max 2,4) och fästpunkter. Livs egen sida (Tempt 2 (GE) MY22, Ocean Wave) bekräftar komponenterna och att storlek M finns i 27,5 tum. **Utelämnat, och rätt så:** ramstorlekar, antal växlar och reklamord (perfekt, lätt, bekväm). **Dubbletter:** inga. Tempt 2 (SKU 2201115285) och Tempt 2 GE 29 tum (SKU 2201134185) är andra modeller. |
| 9016 | 10502527877386 | RÄTTA | **Rättningar i html:** (1) "&lt;li&gt;Dig som vill ha 7 växlar med Shimano&lt;/li&gt;\n&lt;li&gt;Dig som är ca 165–195 cm lång&lt;/li&gt;" → "&lt;li&gt;Dig som vill ha 7 växlar med Shimano&lt;/li&gt;". (2) "\n&lt;li&gt;Lämplig för längder: Ca 165–195 cm&lt;/li&gt;" → "" (tas bort). **Skäl:** längdintervallet går isär mellan källorna (R2). **Övrigt:** alla andra fakta stöds av egen källa och Engwes gemensamma E26-tabell. Lastkapaciteten får stå (se ovan). Vikt (34,5 kg är High-Step-värdet), motor och räckvidd är korrekt utelämnade. "Svart" stöds av SKU:n ENGWE_E26ST-BLACK. **Dubbletter:** inga, eftersom 9017 och 9018 är E26 utan ST. |

## Till koordinatorn
- Tillämpa de två html-rättningarna för 9016 innan skrivfilen byggs. 10111 kan skrivas som den är.
- Byt i `att_bekrafta` för 9016 till tillverkarens adress: https://engwe-bikes.com/collections/on-sale/products/engwe-e26 (omdirigeras till us.engwe.com). Två av utkastets tre adresser gick inte att öppna.
- 9017 och 9018 är redan skrivna med "Ca 165–195 cm" från samma källtext, och tillverkaren anger 170–200 cm. Det är kandidat för en lärdom eller rättning, men kräver Davids beslut.
- Till David (data, inte text): 10111 har en Default Title-rad med lager och 1 740 kr högre pris än M / green. Handle slutar dessutom på 2201135184, som inte är variantens SKU.
