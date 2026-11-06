# Granskningsutlåtande k_37a (frisläppta kosttillskott och Romet-cyklar, BEST OF SPORTS)

**Granskare:** Opus, oberoende. Datum: 2026-11-06. Granskningen var bara läsning. Källan lästes live via Admin API (`shopify_api.py`), och butiken bekräftades som BEST OF SPORTS (bestofsports.se). Inget ändrades i Shopify och inget committades.

**Underlag:** CLAUDE.md, regelbok v1.4–v1.10 (R1, R2, R3, R4, R7, R12, R13, v1.9), BESLUTSLOGG till och med 2026-11-06 (frisläppning av hållna grupper: varunamnen får stå kvar, bara fakta), LARDOMAR, butiksprofilen, kosttillskott-exempel-2026-11-05.md och praxis i k_utlatande_32i33a, 33b och 36ab.

**Domen gäller bara textens kvalitet.** Enligt Davids beslut 2026-11-06 underkänns ingen produkt på grund av namn eller läkemedelsklassning. Riskerna med namn och klassning redovisas i skälen.

## Resultat

- GODKÄND: 8 (37001–37008)
- RÄTTA: 0
- UNDERKÄND: 0

## Kontroller som gjorts på alla

- **Källa (R1, R2):** varje mängd, halt, dos, tid, temperatur och däck- och växeluppgift jämfördes mot live-texten. Inga avvikelser hittades.
- **Motsägelser rätt utelämnade:**
  - källornas generella allergenrader (alla sex kosttillskott)
  - intagstiden för Herbal Energy ("helst efter frukost" mot "ta inte ... efter frukost")
  - OA-extrakt och L-karnitin i Appetite Control (står i löptexten men inte i ingredienslistan)
  - Wagants växelgrupp (Alivio i specifikationen, Alivio/Altus i löptexten; bara "Shimano" återges)
  - dessutom Romets hjulvikt och cykelvikt, Wagants gaffel och den trasiga raden "Shimano Reverse"
- **Påståenden:** effektord söktes i titel, SEO, meta, Passar för, typ och specifikation (energi, vikt, fett, aptit, led, rörlighet, libido, sömn, minne, prestation, stöd, bidrar, hjälper, kan, främjar, förbättrar, naturlig, hälsa, stress, trötthet, kvalitet m.fl.). Alla träffar är oskyldiga: "kapselform", "fettsyror", "pulverform", tokoferoler som antioxidant och "stöd" i betydelsen cykelstöd. Inga påståenden har kommit in indirekt, inte heller i Passar för.
- **Typord:** Kosttillskott står i alla sex kosttillskott. Det ersätter live-orden Vitamin kapslar, Adaptogen, Viktminskningskapslar, Mineral Kapslar, Mineralpulver och Naturliga energikapslar. Romet följer live-orden Cykel och Herrcykel (R7).
- **Romet (v1.9):** båda produkterna har två varianter med olika pris och SKU. Titel, SEO, meta och text låser varken färg, storlek, vikt, årsmodell eller pris och nämner inga varianter.
- **Format:**
  - titel 24–68 tecken, högst 2 kommatecken
  - SEO 24–42 tecken
  - meta 138–153 tecken, med verb och utan cirkulär inledning
  - Passar för finns i alla
  - "enligt tillverkaren" högst två gånger per text
  - standardblocket är tecken för tecken likt `b_skriv_24.json`
  - ingen har taggen På beställning, och ingen har leveranstidsmeningen
  - alla är ACTIVE och har lager och bild
  - `skrivfil_kontroll.py` ger 0 fel och 0 varningar
- **Unikhet:** titel, SEO och meta jämfördes mot alla `*utkast*.json` och `*skriv*.json`. De enda träffarna är äldre, oskrivna utkast för samma produkt-id (k_31b: 31013 och 31015; k_33a: 33004, 33006 och 33008; k_33b: 33013), så det är ingen krock. Mot butiken söktes Vintage LTD och alla 20 Wagant-titlar: inga krockar.

## Domar

| nr | id | produkt | dom | anmärkning |
|---|---|---|---|---|
| 37001 | 10462773641482 | Trec TBL Beauty Body Shaper | GODKÄND | Utkastet stänger källans öppna hakparentes efter vitamin B12. Det är en tolkning som inte ändrar någon mängd och som redovisas, så den godtas. Risk: namnet är ett viktlöfte, och produkten har synefrin och koffein utan angiven synefrinmängd. |
| 37002 | 10462778458378 | Trec Essensey Tribido Max Tribulus | GODKÄND | Alla påståenden om libido, organ och immunförsvar är borta. Risk: namnet anspelar på libido. |
| 37003 | 10462791991562 | Trec TBL Appetite Control | GODKÄND | Bara ingredienslistan används. Källan har ingen varning för barn eller gravida, och utkastet lägger rätt inte till någon. Risk: namnet är ett viktlöfte, och Garcinia har varningar i andra EU-länder. |
| 37004 | 10472277180682 | Trec Essensey Glucosamine+Chondroitin+MSM | GODKÄND | Halterna 31,3/31,3/18,8 % och dosen 2 x 2 kapslar stämmer. Risk: Läkemedelsverkets klassning av glukosamin (2001) och möjlig skaldjursallergen. |
| 37005 | 10472277311754 | Trec TBL Flexi Move, Vanilj och Jordgubb | GODKÄND | Det finns en enda smakvariant, så smaken låser ingenting. Metan är något omständlig men korrekt. Risk: samma glukosaminklassning som 37004; fisk och gelatin står i ingredienslistan. |
| 37006 | 10472323219722 | Trec Herbal Energy | GODKÄND | Den motsägande intagstiden är utelämnad. "Energy" finns bara i varunamnet. |
| 37007 | 10472297300234 | Romet Vintage LTD D | GODKÄND | Titeln är neutral. Stålram, Nexus med 7 växlar, V-bromsar och 700x35C står i källan. Risk: uppgifterna kan inte knytas till en viss variant eller årsmodell. |
| 37008 | 10472332099850 | Romet Wagant 7 | GODKÄND | Titeln är neutral, och växelgruppen är reducerad till "Shimano". Pakethållaren nämns utan lastuppgift. Samma variantrisk som 37007. |

Fullständiga skäl per produkt finns i `vag2_skriv/k_utlatande_37a.json`. Inga rättningar behövs, så `rattningar` är tomt för alla.

## Att känna till (påverkar inte domen)

1. **Namn som påståenden:** Beauty Body Shaper, Appetite Control, Tribido Max och Herbal Energy kan ses som hälsopåståenden i namnet (förordning 1924/2006 art. 1.3). Vår text lägger inte till något påstående.
2. **Glukosamin (37004, 37005):** Läkemedelsverkets beslut från 2001 att klassa glukosamin som läkemedel har inte kontrollerats mot dagens praxis.
3. **Romet (37007, 37008):** varianterna har olika pris och SKU och är troligen olika årsmodeller. Specifikationen kommer från en enda källtext. Kunden ser samma text för båda varianterna.
