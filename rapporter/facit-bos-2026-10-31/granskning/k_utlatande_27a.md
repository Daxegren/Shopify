# Granskningsutlåtande k_27a (BEST OF SPORTS), 2026-11-05

Granskare: Opus, endast läsning. Underlag: `vag2_skriv/k_27a_utkast.json` (10 produkter). Källan och varianterna (pris, SKU, färg, taggar) lästes live via Admin API 2026-11-05. Butiken bekräftades som BEST OF SPORTS. Ingenting skrevs i Shopify. Regler: regler-v1.md v1.4–v1.8 och BESLUTSLOGG 2026-11-05 (färg- och storleksneutral titel när alla varianter har samma pris).

**Resultat:** 7 GODKÄND, 3 RÄTTA (27012, 27013, 27015), 0 UNDERKÄND. `skrivfil_kontroll.py` på en rättad kopia: 0 fel, 0 varningar.

**Genomgående:** Alla 10 har samma pris på alla varianter. Variantnamnen är färger, utom 27008 där BL/BLU/PI är oförklarade. Ingen titel, SEO-titel, meta eller specifikation låser en färg eller storlek. Alla färglistor stämmer exakt med variantnamnen, och ingen färg är påhittad. Ingen produkt har taggen "På beställning", och inget utkast har leveranstidsmeningen. Det är rätt. Standardblocket är oförändrat.

## 27009 (10636616696074): GODKÄND

Live: 12 färgvarianter, alla 549 kr; variantnamnen stämmer exakt med färglistan. Mått 183x60x1cm, NBR-skum, spänne och 'Halkfri yta' står ordagrant. 'Halkfri enligt tillverkaren' en gång är tillåtet enligt R5 (ordet står ordagrant i källan) och är ingen säkerhets- eller skyddsformulering. Rehab, hudvänligt, tungmetaller och 'extra tjock' rätt utelämnade. 'Utomhus' saknas i denna källa och skrivs rätt inte. Titel, SEO och meta skiljer sig från 27010/27011. Ingen tagg På beställning.

## 27010 (10636616925450): GODKÄND

Live: 12 färgvarianter, alla 699 kr; färglistan stämmer med variantnamnen. 190x60x1,5cm, utomhus, NBR, spänne och 'Halkfri yta' ordagrant; 'enligt tillverkaren' en gång. Titel, SEO, meta och html skiljer sig från 27011 (måttet 60 resp. 100 cm) och från 27009. Ingen tagg På beställning.

## 27011 (10636617122058): GODKÄND

Live: 12 färgvarianter, alla 699 kr; färglistan stämmer. 190x100x1,5cm, utomhus, NBR, spänne och 'Halkfri yta' ordagrant; 'enligt tillverkaren' en gång. Alla fält unika mot 27009/27010. Ingen tagg På beställning.

## 27012 (10636638224650): RÄTTA

Live: 3 färgvarianter (Svart, Grå, Blå), alla 459 kr. R2: löptexten säger 'tillverkad i gummi' men materiallistan anger PP, TPR, NBR och EVA (PP och EVA är inte gummi). Uppgiften går isär och lyfts i titel, SEO-titel och meta; därför tas 'gummi' bort och materiallistan får stå. Diameter 36 cm, ca 300 g och vadderad in- och utsida ordagrant. Träningseffekt, rehab och 'maximal komfort' rätt utelämnade. 'Pilatesring 36 cm' krockar inte med Tunturi-, Gymstick- eller GS-ringen. Ingen tagg På beställning.

- `titel` före: `Pilatesring 36 cm i Gummi`
  efter: `Pilatesring 36 cm`
- `seo_title` före: `Pilatesring 36 cm i Gummi`
  efter: `Pilatesring 36 cm`
- `meta` före: `Pilatesring i gummi med diametern 36 cm`
  efter: `Pilatesring med diametern 36 cm`
- `html` före: `Pilatesringen är tillverkad i gummi, har en diameter på 36 cm och väger cirka 300 g.`
  efter: `Pilatesringen har en diameter på 36 cm och väger cirka 300 g.`

## 27013 (10636652085514): RÄTTA

Live: 4 färgvarianter, alla 379 kr; färglistan stämmer. Löptexten säger att mattan 'levereras med en praktisk axelrem' och beskriver hur den rullas ihop och hålls med axelremmen; bara listan nämner även en bärväska. Webbsökning på Gorilla Sports 180x60x0,5 cm PVC (Galaxus, Kaufland) anger matta och bärrem, ingen väska (sidorna gick inte att öppna, exakt artikel 101167 bekräftades inte). Uppgiften om väska är osäker och tas bort (R2); bärremmen står kvar. Mått, 1,07 kg, PVC, går att vika dubbelt och går att torka av ordagrant. Ingen tagg På beställning.

- `meta` före: `Bärväska och bärrem ingår, och mattan`
  efter: `En bärrem ingår, och mattan`
- `html` före: `Bärväska och bärrem ingår, och materialet`
  efter: `En bärrem ingår, och materialet`
- `html` före: `<li>Dig som vill ha bärväska och bärrem för transport</li>`
  efter: `<li>Dig som vill ha en bärrem för transport</li>`
- `html` före: `<li>Ingår: Yogamatta, bärväska och bärrem</li>`
  efter: `<li>Ingår: Yogamatta och bärrem</li>`

## 27014 (10636653822218): GODKÄND

Live: 4 färgvarianter, alla 389 kr; färglistan stämmer. 80/20 polyester/polyamid, 180x60 cm, 400 g, absorberande material och skötselråden står ordagrant. 'Absorberande' är en materialegenskap i källan, inget R5-ord. Yogahandduk i Passar för har stöd i källan. Ingen tagg På beställning.

## 27015 (10636676792586): RÄTTA

Live: 3 färgvarianter (Röd, Svart, Blå), alla 1039 kr. Lastgränsen 'Maximal lastkapacitet per parallette: 100kg' är svensk, ordagrann och har etikett och enhet, och löptexten säger detsamma ('100kg vardera'). Den återges rätt en gång som 'enligt tillverkaren' (R4, v1.7). Måttet 'Dimension(LxBxH): 46x39x30cm' saknar 'per parallette', till skillnad från vikten och lasten. Webbkällan (guenstiger.de, 101128-00019-0001) skriver '2er Set, 46 x 39 x 30cm, bis 200kg' och avgör inte frågan. Tolkningen 'per parallett' tas därför bort ur specifikationen och metan (R1/R2). 4 kg per parallett och greppet 4 cm står ordagrant. Ingen tagg På beställning.

- `meta` före: `Låga parallettes som säljs parvis, 46 x 39 x 30 cm och 4 kg per parallett.`
  efter: `Låga parallettes som säljs parvis och mäter 46 x 39 x 30 cm. Varje parallett väger 4 kg.`
- `html` före: `<li>Mått per parallett (L x B x H): 46 x 39 x 30 cm</li>`
  efter: `<li>Mått (L x B x H): 46 x 39 x 30 cm</li>`

## 27016 (10636683018506): GODKÄND

Live: 10 färgvarianter, alla 239 kr; färglistan följer variantnamnen (Brun/Beige). 100 % bomull, maskintvätt, 260x3,8 cm, 120 g och 'förlängning i positioner där du inte når hela vägen' står ordagrant. 'GS' rätt borttaget. Hudvänligt och hjälp att orka hålla positioner rätt utelämnade (R5). 'Tio färger' stämmer med varianterna. Ingen tagg På beställning.

## 27017 (10636701303050): GODKÄND

Live: 8 färgvarianter, alla 579 kr; färglistan stämmer med variantnamnen. Tjockleken går isär (0,8 cm i löptexten, 0,6 cm i Mått och Tjocklek), så den utelämnas rätt (R2). 'Motverka att den glider' och 'optimala ytan' rätt utelämnade (R5). TPE, 180x60 cm, svart undersida, färgad ovansida med diamantmönster, yoga/pilates och nedvärmning står ordagrant. Ingen tagg På beställning.

## 27008 (10581104427274): GODKÄND

Live: 3 varianter BL/BLU/PI (SKU 61200-BL/-BLU/-PI), alla 2999 kr; källan säger 'svart och rött'. Webbkoll: Gymstick Air Track 300 x 100 x 10 cm säljs i blå-vit och svart-röd (gigantti.fi via sökning), så variantkoderna är troligen färger som inte går att styrka; att färg utelämnas helt är rätt och måttet är detsamma för alla varianter. Inga hälso-, skade- eller skyddspåståenden: stötdämpning/leder, 'hållbara', 'högsta kvalitet', 'idealisk investering' rätt utelämnade (beslut 2026-11-05 och R5). Pump, väska och reparationssats nämns inte (ingen sida kopplad till SKU 61200). Ingen dubblett: Gymnastikmatta AirTrack 300/500 cm är Gorilla Sports 101161. Ingen tagg På beställning, ingen leveranstidsmening. Taggen Gymstick får inte röras vid skrivning (R18).

## Källor (webb)
- https://www.gigantti.fi/yrityksille/product/urheilu-ja-vapaa-aika/urheilu-ja-fitness/liikuntavalineet-ja-tarvikkeet/gymstick-air-track-urheilu-ja-vapaa-aika/257600 (enligt sökresultatet; sidan gav 404 vid öppning)
- https://www.guenstiger.de/Produkt/Gorilla_Sports/Push_Up_Parallettes.html (enligt sökresultatet; 403 vid öppning)
- https://www.galaxus.ch/en/s3/product/gorilla-sports-yoga-mat-5-mm-yoga-mats-15526207 och https://www.kaufland.de/product/301861367/ (enligt sökresultatet; 503/403 vid öppning)

Webbuppgifterna har bara använts för att stödja försiktighet, alltså att utelämna. Ingen ny uppgift har lagts till från dem.
