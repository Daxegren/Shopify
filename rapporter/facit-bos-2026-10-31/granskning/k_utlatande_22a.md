# Granskningsutlåtande k_22a (BEST OF SPORTS)

Granskare: Opus, endast läsning. Datum: 2026-11-05. Butiken är bekräftad via API (BEST OF SPORTS, 6f2e53-67.myshopify.com). Båda produkterna är hämtade live på nytt: båda är ACTIVE, ingen har texter-klara och ingen står på spärrlistan. Ingenting är skrivet i Shopify. Underlag: regler-v1.md (v1.5–v1.7), BESLUTSLOGG.md (raderna 2026-11-05), butiksprofil-bestofsports.json, agentprompter.md, k_utlatande_19f20, k_utlatande_02b/01d (färgprejudikat) och sammanslagningsplan.md.

**Utfall:** GODKÄND 0, RÄTTA 2, UNDERKÄND 0 (av 2).

Rättningen är provkörd på en kopia. `skrivfil_kontroll.py` gav 0 fel och 0 varningar. Varje "före" förekommer exakt en gång i sitt fält.

## Tabell

| nr | id | fil | dom | rättning och skäl |
|---|---|---|---|---|
| 22004 | 10624088637706 | k_22a | RÄTTA | **html:** "Se sidan Frakt för övriga länder.</p>" → "Se sidan Frakt för övriga länder. Beställningsvaror kan ta upp till en vecka längre.</p>"<br>Taggen På beställning finns, men leveranstidsmeningen saknas (R13). Färgen Shell White får stå (se nedan). 'Shimano 105 Di2' står ordagrant i källan, och texten säger varken elektronisk eller mekanisk (v1.7). 24 växlar står ordagrant i källan (2x12 hos Liv). Ram, gaffel, fälgar, däck och fästpunkter stämmer med live. Ingen ramstorlek nämns, och det är rätt. |
| 22005 | 10676720501002 | k_22a | RÄTTA | **html:** samma rättning som för 22004 (taggen På beställning finns).<br>"29 2" i källan är ett skrivfel (se nedan). Storlekarna S, M, L och XL i specifikationen är exakt de fyra varianterna (alla purple, 24 669 kr), och det stämmer med R3 v1.5. Övriga fakta stämmer med live och med Giants sida. |

## Särskilt granskat

- **22004, färgen Shell White mot varianten "M / gray":** Färgen får stå i titel, SEO, meta och specifikation. Källan länkar själv till Livs sida för exakt modellen (liv-cycling.com/ee/avail-advanced-1-2027), och där är Shell White den enda färgen. Det är alltså en entydig uppgift från tillverkaren om exakt modellen (v1.6/v1.7). "gray" i varianten är leverantörens färgfamilj och inget eget kulörnamn. Samma nivå gäller för 20061 (Midnight Moon mot gray) och 9029 (Mars Dust mot Red). Default Title har ingen färg. Skillnaden mot 9150: där stod en svensk grundfärg, "(Grå)", som varianten sa emot, och den togs bort. Här står bara tillverkarens kulörnamn. Ingen variant anger en annan kulör, så färgen låses inte fel.
- **22004, varianterna:** Default Title (SKU 1017039143) och M / gray (SKU 1017039145) har olika SKU men samma pris, 52 139 kr. Varianterna skrivs enligt Davids bekräftade tolkning 2026-11-05. Obs: ordalydelsen i v1.7 ("Varianter med olika SKU avvisas som förut") och beslutsloggens rad 34 pekar åt olika håll. Regelboken bör förtydligas så att den följer rad 34.
- **22004, dubblett:** 10635810046218 har samma titel och SKU 1017039143 men skapades senare (2026-09-21) och har ett annat pris (45 339 kr). Sammanslagningsplanen (rad 39) har redan denna produkt som behållare, så den skrivs (R12a, äldst).
- **22005, "29 2" mot titelns "29 1":** Granskaren har själv öppnat Giants sidor. På giant-bicycles.com/ee/xtc-slr-29-1-2027 har XTC SLR 29 1 (2027) exakt källans komponenter: ALUXX SLR 12x148, Crest XC Comp 100 mm 15x110 remote lockout, Deore RD-M6200, Tektro Orion, Maxxis Recon Race 29x2.4 och XCA 2 29 med 25 mm innerbredd. Färgerna är Tempest Purple och Cyber Lime, och storlekarna är S–XL. XTC SLR 29 2 har andra delar: Crest 34 RRL, Deore M-6100, Shimano MT200 och XCT 29. Adressen giant-bicycles.com/ee/xtc-slr-29-2-2027 visar 2025-modellen. Källans "29 2" är alltså ett skrivfel, och det är rätt att utkastet inte återger det.
- **22005, storlekar:** Alla fyra ramstorlekarna i källan (S 38, M 43,1, L 47,5, XL 52,5 cm) säljs som varianter. Längdrekommendationerna är rätt utelämnade.
- **Elektronisk växling (v1.7):** 22004 skriver "Shimano 105 Di2" utan ordet "elektronisk" och utan batteri, och det godtas. 22005 påstår inget om växlingstypen.
- **Leveranstidsmeningen:** Båda utkasten saknade meningen trots taggen. Skriptet ser inte taggen (v1.5), så felet fångas bara av granskaren. Förslag: låt bygg- eller kontrollskriptet läsa taggen ur live-filen.

## Webbkällor öppnade av granskaren (2026-11-05)

- liv-cycling.com/ee/avail-advanced-1-2027: Shell White (enda färgen), XXS–L, Shimano 105 Di2, 12 speed, Gavia Fondo 0 700x32c.
- giant-bicycles.com/ee/xtc-slr-29-1-2027: komponenter och färger enligt ovan.
- giant-bicycles.com/ee/xtc-slr-29-2-2027: visar XTC SLR 29 2 (2025) med andra komponenter.
