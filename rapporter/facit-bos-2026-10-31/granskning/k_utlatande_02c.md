# Granskning väg 2, cyklar k_02c (2026-11-04)

Oberoende granskning (Opus). Shopify bara läst, inget ändrat. Underlag: `vag2_skriv/k_02c_utkast.json` (13 utkast) och `k_02c_avvisade.json` (12 avvisade). Regler: regelbok v1.6 (inklusive faktakoll på nätet), BESLUTSLOGG, butiksprofilen, produkttexter-standard, LARDOMAR (cyklar 2026-11-03). Alla 25 produkter hämtades live på nytt via Admin API (`shopify_api.hamta_produkter` plus en variantfråga), liksom tvillingarna 10472269840650, 10472256831754, 10502528205066, 10476230541578, 10472332329226 och 10474077847818. Alla 13 utkastprodukter är ACTIVE och saknar SEO-titel och meta, och ingen av dem står i spärrlistan.

**Resultat:** 10 GODKÄND, 3 RÄTTA, 0 UNDERKÄND. Rättningarna (före och efter) står i `vag2_skriv/k_utlatande_02c.json`. Varje före-text förekommer exakt en gång i sitt fält (kontrollerat i python). `skrivfil_kontroll.py` på en rättad kopia gav 0 fel och 0 varningar. Leveranstidsmeningen finns på exakt de fem produkter som har taggen "På beställning" (9151, 9154, 9155, 9158, 9161), R13.

| nr | id | dom | kort skäl |
|---|---|---|---|
| 9151 | 10469226316042 | RÄTTA | Lägg till "Växelreglage: SRAM NX Eagle" (egen källa; NX Eagle är bara mekanisk, webbkälla) |
| 9152 | 10411716837642 | GODKÄND | Spårbart, en variant |
| 9154 | 10589713531146 | RÄTTA | "Vivid Coil Base R" (R:et tappat) och "Växelsystem: SRAM GX DH" (bara mekanisk, webbkälla) |
| 9155 | 10588448030986 | GODKÄND | Spårbart |
| 9156 | 10507441963274 | GODKÄND | Spårbart; färgen bara i titeln, en variant |
| 9158 | 10470937002250 | GODKÄND | Spårbart; tvillingen 10472269840650 är spärrad och oskriven |
| 9160 | 10462752669962 | GODKÄND | Damcykel är live-ordet och står i källan |
| 9161 | 10462752833802 | GODKÄND | Som 9160 |
| 9165 | 10494689345802 | GODKÄND | Vikten är rätt utelämnad (oklart om det gäller en pedal eller paret) |
| 9166 | 10461951197450 | GODKÄND | "Pedaler" är butikens ord |
| 9173 | 10523488289034 | RÄTTA | Ta bort "Shimano BR-MT200" ur bromsraden (modellen tar ställning i en motsägelse) |
| 9174 | 10472332787978 | GODKÄND | Spårbart |
| 9175 | 10472334393610 | GODKÄND | Ramstorlek M motsägs inte (en variant, källan har bara M) |

## Särskilda kontroller
- **Växelsystem 9151 och 9154 (R1 v1.6).** Källan anger "SRAM NX-Eagle" respektive "SRAM GX DH". Båda finns bara som kabelstyrda (mekaniska) delar. NX Eagle-reglaget levereras med växelvajer (https://www.bike-components.de/en/SRAM/NX-Eagle-Shifter-12-Speed-p65010/), och modellens spec anger NX Eagle-reglage och GX Eagle-bakväxel utan AXS (https://www.vitalmtb.com/product/guide/bikes/kona/process-153-56176). GX DH 7 växlar har X-Actuation och ingen AXS-version (https://www.rosebikes.com/p/sram-gx-dh-7-speed-rear-derailleur-2700008), och Process X med GX DH 7 växlar och DB6 finns i https://www.vitalmtb.com/product/guide/bikes/kona/process-x-77461. Därför får namnen stå, som 9149 i k_02b. Det var också säkert att utelämna dem, så rättningarna är en förbättring och inte ett fel.
- **9153, Eagle 90 Transmission:** avvisningens påstående "troligen elektroniskt (AXS)" är **fel**. Eagle 90 och Eagle 70 Transmission är de mekaniska versionerna av Transmission ("the mechanical versions of the electronic AXS Transmission drivetrain", https://www.singletracks.com/mtb-gear/upgrade-kit-makes-mechanical-sram-transmission-derailleur-electronic/). Modellens spec (Process 134 DL 2026) anger Eagle 90-bakväxel och Eagle 70-reglage (https://www.vitalmtb.com/product/guide/bikes/kona/process-134-76781).
- **Färg som bara står i titeln (9152, 9154–9156, 9158, 9161, 9165, 9166):** alla har en variant, eller varianter med samma färg, och ingenting i källan motsäger färgen. Det godtas på samma nivå som i tidigare batcher. Där live-titeln har en svensk färg i parentes (9152 Grön, 9154 Grå, 9155 Guld) är det godtagbart att den utelämnas.
- **9165, vikt:** "Vikt: 265g" säger inte om det gäller en pedal eller paret. Att 9166 anger "pedal 265g, par 530g" är syskondata (R1). Rätt utelämnad.
- **9173, broms:** löptexten säger mekaniska och specifikationen säger hydrauliska. Utkastet tog bort ordet för typen men behöll modellen BR-MT200, som är hydraulisk. Modellen tar alltså ställning i motsägelsen, och därför ska raden bara säga "Skivbromsar" (R2). Webbkollen gav inget entydigt svar: centrumrowerowe.pl anger hydrauliska, men samma sida anger en 9-växlad kassett mot källans 21 växlar, alltså troligen en annan årsmodell.
- **9175, ramstorlek:** live-titeln har '17" M', källan listar bara M (17") och produkten har en enda variant. M motsägs alltså inte, och ingen storlek som inte säljs nämns (R3 v1.5).
- **Damcykel, 9160 och 9161:** båda har "Damcykel" i live-titeln, och 9160:s källa säger "damcykel". Varje produkt behåller sitt eget live-ord, även om Tempt 3 skrevs som Mountainbike (R7). Titelformen "Tempt 2 i Ocean Wave, 27,5 tum" avviker från batchens mönster men behövs. Med mönstret "Tempt 2, 27,5 tum, Ocean Wave" blir det 3 kommatecken (decimalkommat räknas), och det ger en R12-varning (testat).
- **Dubbletten 9158 mot 10472269840650:** samma titel, modell, färg och pris, men SKU …113 mot …114. 10472269840650 är inte skriven (ingen SEO, ingen texter-klara) och står i spärren `titeldubbletter`. 9158 är alltså rätt produkt att skriva. Bara 9158 har taggen "På beställning".

## Granskning av avvisningarna (k_02c_avvisade.json)
| nr | id | bedömning |
|---|---|---|
| 9153 Process 134 DL Sage | 10588453404938 | **Svagt motiverad.** Alla fem varianter är green. Prisskillnaden (77 269 mot 77 119 kr) gäller storleken, som titeln inte anger. Det är samma läge som 9131 i k_02b. Elektronikskälet är fel (se ovan). Om en ny version skrivs: växelsystemet får stå. Källans ramstorleksrader är trasiga (S och M båda 38 cm), och XS har 27,5-tumshjul fram och bak. |
| 9157 Flourish 3 Gunmetal Black | 10462773838090 | Motiverad. Det är en dubblett av 10472256831754, som är skriven med texter-klara (SKU …113 mot …114). Källan säger "Flourish FS 3" och nämner stötdämpande sadelstolpe, medan titeln säger "Flourish 3" (R3). Samma tvetydighet kan finnas i den redan skrivna tvillingens källa; se beslut 2. |
| 9159 Tempt 2 GE | 10474079518986 | Motiverad. Två varianter med olika pris (13 339 mot 11 599 kr) och samma SKU. |
| 9162 Avail AR 2 | 10488246796554 | Motiverad. Dubblett av 10502528205066 (skriven). Variantfärgen white motsäger dessutom Lavender Blush. |
| 9163 STP 26 | 10673173332234 | Motiverad. "Ungdomscykel", designad för unga (R6, barn). |
| 9164 Tempt 3 Tyrian Purple | 10476252692746 | Motiverad. Dubblett av 10476230541578 (skriven). |
| 9167–9170 Rideoo-sparkcyklar | 10472294449418, 10472331804938, 10472332001546, 10472332886282 | Motiverade. Källan anger 4–7 år eller "barn" (R6). |
| 9171 Art Deco Lux blå | 10471075381514 | Motiverad. Dubblett av 10472332329226 (skriven). |
| 9172 Art Deco Lux svart | 10462795202826 | Motiverad. Två varianter med olika pris och samma SKU. Svart finns också som DRAFT 10474077847818. |

## Beslut för David
1. **9153 och liknande (pris skiljer bara mellan storlekar, färgen är samma):** ska sådana produkter skrivas utan pris, med de ramstorlekar som säljs? Rekommendation: ja, eftersom titeln inte låser någon storlek (samma fråga som 9131 i k_02b). Om inget beslutas fortsätter de att avvisas.
2. **Flourish 3 mot Flourish FS 3:** källan för 9157 kallar modellen FS 3. Den skrivna tvillingen 10472256831754 heter "Flourish 3". Rekommendation: kontrollera tvillingens källa i före-filen innan fler Flourish-produkter skrivs. Ingen åtgärd utan beslut.
3. **9175 Jolene 6.2 "för unga och kvinnor":** ramen är för 155–170 cm, så den räknas inte som barncykel och godkänns. Om David vill att "unga" ska räknas som ungdom (som 9163) ska produkten hållas tillbaka.
