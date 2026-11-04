# Granskning väg 2, cyklar k_02d (Romet) (2026-11-04)

Oberoende granskning (Opus). Shopify bara läst, inget ändrat. Underlag: `vag2_skriv/k_02d_utkast.json` (22 utkast) och `k_02d_avvisade.json` (3 avvisade). Regler: regelbok v1.6, BESLUTSLOGG, butiksprofilen, produkttexter-standard §14 och §16, LARDOMAR (cyklar 2026-11-03). Jag hämtade alla 25 produkter live på nytt via Admin API (`shopify_api.hamta_produkter` och en fråga om varianter). För att hitta dubbletter hämtade jag också alla 172 Romet-produkter i butiken och jämförde modell, färg, pris och artikelkod i SKU (siffrorna efter hjul- och ramstorlek). Alla 25 är ACTIVE, saknar SEO-titel och meta och har inte taggen "På beställning". Därför ska ingen text ha leveranstidsmeningen, och ingen har den (R13).

**Resultat:** 20 GODKÄND, 0 RÄTTA, 2 UNDERKÄND (9196 och 9200). Domarna står i `vag2_skriv/k_utlatande_02d.json`. `skrivfil_kontroll.py` på utkastfilen gav 0 fel och 0 varningar. Titel, SEO-titel och meta krockar inte med andra batchers utkast eller skrivfiler, och inte med någon live-titel eller SEO-titel för Romet. Inget utkast använder webbkällor (R1 v1.6), och inget behövde det.

| nr | id | dom | kort skäl |
|---|---|---|---|
| 9176 | 10472515567882 | GODKÄND | Spårbart; 27,5 tum står bara i live-titeln och är rätt utelämnat |
| 9177 | 10471091568906 | GODKÄND | Den motsägande växelraden (3 mot 5) är utelämnad |
| 9178 | 10472332460298 | GODKÄND | Stadscykel är källans ord; syskonet Vit heter Damcykel (beslut 2) |
| 9179 | 10472291467530 | GODKÄND | M och L säljs; ingen dubblett mot Orkan D Rosa |
| 9180 | 10507278024970 | GODKÄND | Spårbart; bromsar och ursprung är utelämnade |
| 9181 | 10507289755914 | GODKÄND | "Hybridcykel för herrar" står i källan |
| 9182 | 10472332394762 | GODKÄND | Herrcykel är källans ord |
| 9183 | 10526097801482 | GODKÄND | Annan SKU än både D Lite Lila/Rosa och Orkan D Vit och Lila |
| 9184 | 10472294613258 | GODKÄND | Spårbart; "unga" är utelämnat (beslut 1) |
| 9185 | 10471004438794 | GODKÄND | Terrängcykel är källans ord; färgen står i källan |
| 9186 | 10472306540810 | GODKÄND | De trasiga raderna är utelämnade; bromsarna tas från specifikationsraden |
| 9187 | 10523487273226 | GODKÄND | Mountainbike är källans ord |
| 9189 | 10526100193546 | GODKÄND | Källan stämmer med titeln (2.0 M) |
| 9190 | 10472295104778 | GODKÄND | Cykel är live-ordet; källan har inget typord |
| 9191 | 10472288878858 | GODKÄND | Damcykel är källans ord |
| 9192 | 10494855807242 | GODKÄND | Cykel är källans ord; de trasiga Nexus-raderna är utelämnade |
| 9193 | 10471076266250 | GODKÄND | Stadscykel är källans ord (beslut 2) |
| 9195 | 10472290713866 | GODKÄND | Cykel är kvar; källan har inget svenskt typord |
| 9196 | 10523488321802 | UNDERKÄND | Trolig dubblett av den skrivna Vintage Eco D Turkos |
| 9198 | 10526098129162 | GODKÄND | Trekkingcykel, samma ord som den skrivna Wagant 2 Grå |
| 9199 | 10472334459146 | GODKÄND | Den enda varianten är M / black |
| 9200 | 10472334360842 | UNDERKÄND | Källan säger "mountainbike för ungdomar" (R6, beslut 1) |

## Särskilda kontroller
- **Typord.** 9178 (Stadscykel), 9181 (Hybridcykel), 9182 (Herrcykel), 9185 (Terrängcykel), 9187 (Mountainbike), 9191 (Damcykel), 9193 (Stadscykel) och 9198 (Trekkingcykel) använder alla ordet i produktens egen källa (R7). 9190, 9192, 9195 och 9196 behåller live-titelns "Cykel". Det är rätt eftersom källan inte har något eget svenskt typord ("cykeln", "en cykel med karaktär", "mångsidig specialist", "allroundcykel"). För 9190 hade det varit fel enligt R1 att låna "damcykel" från syskonet 9191. 9176 och 9200 säger "Damcykel" i titeln och "mountainbike för damer/kvinnor" i texten, precis som de redan skrivna Jolene-cyklarna.
- **Färg i titeln.** I alla 22 utkast kommer färgen i titeln från live-titeln. Varje produkt har en enda variant, eller varianter i samma färg (9179 pink, 9199 black), så R3 bryts inte. Färgen står bara i texten där källan eller varianten styrker den (9179, 9185, 9199).
- **Kortade SEO-titlar** (9183, 9185, 9186, 9187, 9200) är unika och har märke och modell kvar.
- **Trasiga rader** är utelämnade överallt: Luiza Classics rader om Nexus och 145 cm, "6061 Aluminiumlegering" under ramstorlek, "Kedjebromsar" och "Suntour XCE framnav", raden "Nexus: 175 x 175 mm", "Shimano Touring – Shimano Touring" och "Hjulvikt". Där det står "Hjulvikt" är vikten rätt utelämnad: 9177, 9179, 9184, 9192 och 9193.
- **Dubbletter mot redan skrivna Romet-produkter.** 9179 (Orkan 1 D, rosa, SKU 28190885/28170883) är inte samma modell som Orkan D Rosa (10526097899786, SKU 2328554, V-bromsar och 63 mm gaffel). 9183 (D Lite vit-lila, SKU 2328540) är inte samma produkt som D Lite Lila och Rosa (2328542) eller Orkan D Vit och Lila (28190089-A, 8 239 kr). Övriga syskon har annan färg och annan artikelkod (Luiza Legend, Orkan 2 M, Orkan 5 D, Orkan 6 M, Wagant 2 och Vintage Classic M). Det enda fyndet är 9196, se nedan.

## Underkända
- **9196 Vintage Eco M, turkos.** SKU 28181056-B har samma artikelkod (1056, 28 tum, 18-tumsram) som den skrivna "Damcykel Romet Vintage Eco D, Turkos" (10472291008778, SKU 28181056-A). Priset är också detsamma, 6 789 kr. Inget annat utkast i batchen delar artikelkod med en annan Romet-produkt. Den ena annonsen säger M (herr) och den andra D (dam), och källorna räcker inte för att avgöra vilken som stämmer. Det är samma bedömning som för 7083 i k_02b. Produkten kan inte skrivas förrän David har beslutat.
- **9200 Jolene 6.2, 26 tum, L.** Källan säger två gånger att cykeln är för ungdomar: "mountainbike designad för kvinnor och ungdomar" och "som sig bör för en mountainbike för ungdomar". Den kallar den också "nybörjarcykel". Utkastaren strök ordet "ungdomar" och flaggade det. Ungdomscyklar avvisas tills David har beslutat (k_5, k_10, k_12, 9163, 9215–9222). Storleken L (165–180 cm) och live-typordet Damcykel talar för vuxen. Om David säger ja kan utkastet skrivas som det är.

## Granskning av avvisningarna (k_02d_avvisade.json)
| nr | id | bedömning |
|---|---|---|
| 9188 Vintage Classic 2.0 M grön | 10472333279498 | **Motiverad (R3).** Titeln säger 2.0 M, men källan beskriver "Vintage Classic 1.0 M". Det finns också redan en skriven "Stadscykel Romet Vintage Classic 1.0 M, Grön" (10472335900938). Om källan har rätt är produkten alltså dessutom en dubblett. |
| 9194 Vintage Eco D vit | 10471064273162 | **Motiverad enligt R3 som regeln lyder nu** (Default Title 6 749 kr och L / valge 5 869 kr). Båda varianterna har samma SKU, 28200712-B, så Default Title är troligen en överbliven variant. Tidigare godkändes samma mönster: 6089, 6101 och 6113 i k_4/k_5, bland annat Orkan D Lite Lila och Rosa. Se beslut 3. |
| 9197 Vintage LTD D gul | 10472297300234 | **Motiverad (R3).** Varianterna har olika SKU (28201899-A för 20-tumsram och 28181898-A för M / yellow) och olika pris (9 979 och 8 679 kr). Det är två verkliga storlekar med olika pris. |

## Beslut för David
1. **Ungdom kontra vuxen.** 9200 hålls tillbaka eftersom källan säger "för ungdomar". 9184 (Rambler R7.1) godkänns. Källan säger "för unga och män", men storlekarna är 150–180 cm, och texten nämner inte unga. Rekommendation: vuxenstorlekar (cirka 150 cm och uppåt) med dam- eller herrtypord får skrivas utan ungdomsord. Då kan 9200 skrivas som den är. Om inget beslutas hålls 9200 kvar, och 9184 skrivs.
2. **Typord inom samma modell.** 9178 Luiza Legend svart heter Stadscykel (källans ord). Den redan skrivna Luiza Legend Vit har samma källtext men heter Damcykel. 9193 Vintage Eco D röd heter Stadscykel, medan de skrivna Eco D Grafit och Turkos heter Damcykel (deras källtext skiljer sig). Båda följer R7. Rekommendation: låt dem stå. Om David vill ha samma typord per modell gäller det de redan skrivna produkterna och kräver ett beslut.
3. **Default Title med annat pris.** Rekommendation: om båda varianterna har samma SKU och samma färg (9194) behandlas Default Title som överbliven, och produkten skrivs. Har varianterna olika SKU (9197) avvisas produkten som nu. Om inget beslutas förblir 9194 avvisad.
4. **Dubbletten 9196 och 10472291008778** (samma artikelkod och pris, M kontra D). Det behöver beslutas om annonserna ska slås ihop eller märkas.
