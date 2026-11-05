# Stickprov pass 6, BEST OF SPORTS, 2026-11-05

Roll: Stickprov (Sonnet, endast läsning). Inget skrevs i Shopify. Läsning live via `shopify_api.py` (ShopifyKlient, `nodes(ids)`, 5 per anrop).
Underlag: `vag2_skriv/k_skriv_26a.json` (4 dubbdäck) och `vag2_skriv/k_skriv_27a.json` (10 variantprodukter). Omfattning: alla 14 produkter (100 procent).

## 1. Jämförelse live mot skrivfil (tecken för tecken)

Fält jämförda per produkt: title, seo.title (null = title), seo.description, descriptionHtml. Dessutom taggen `texter-klara` och status.

Resultat: 14 av 14 produkter har alla fyra fält identiska med skrivfilen (56 av 56 fält lika). Alla 14 är ACTIVE och har taggen `texter-klara`. Inga avvikelser mot skrivfilen.

| nr | id | titel (live) | variantpris | variantnamn |
|---|---|---|---|---|
| 26001 | 10472189788426 | Dubbdäck Schwalbe Winter 47-559 | 659 | Default Title |
| 26002 | 10472303919370 | Dubbdäck Suomi Tyres Hile W240 40-622 | 1589 | Default Title |
| 26003 | 10472304017674 | Dubbdäck Suomi Tyres Routa W126 50-622 | 1759 | Default Title |
| 26004 | 10472304050442 | Dubbdäck Suomi Tyres Porcupine W408 TT 65-622 | 2269 | Default Title |
| 27008 | 10581104427274 | Air Track Gymstick 300 x 100 x 10 cm | 2999 | BL, BLU, PI |
| 27009 | 10636616696074 | Träningsmatta Movit 183 x 60 cm | 549 | 12 färger |
| 27010 | 10636616925450 | Träningsmatta Movit 190 x 60 cm | 699 | 12 färger |
| 27011 | 10636617122058 | Träningsmatta Movit 190 x 100 cm | 699 | 12 färger |
| 27012 | 10636638224650 | Pilatesring 36 cm | 459 | Svart, Grå, Blå |
| 27013 | 10636652085514 | Yogamatta PVC 180 x 60 cm | 379 | 4 färger |
| 27014 | 10636653822218 | Träningshandduk 180 x 60 cm | 389 | 4 färger |
| 27015 | 10636676792586 | Parallettes Push Up Bars Low, 46 x 39 x 30 cm | 1039 | Röd, Svart, Blå |
| 27016 | 10636683018506 | Yogabälte i Bomull 260 cm | 239 | 10 färger |
| 27017 | 10636701303050 | Yogamatta TPE 180 x 60 cm | 579 | 8 färger |

Priserna är lika inom varje produkt (ingen prisskillnad mellan varianter). Inget pris förekommer i någon text (sökning på kr/SEK/:- gav 0 träffar).

## 2. Kontroller enligt uppdraget

- Färg- eller storleksord i titel/SEO/meta som låser en variant: inga. Storleksmått i titlarna (t.ex. 183 x 60 cm, 47-559) är produktens egna mått, inte variantval; alla varianter delar dem. Enda färgordet utanför specifikationslistor är "svart undersida" i meta för 27017 (fast egenskap hos mattan, inte variantnamn, se anm. 5).
- Färglistor mot variantnamn: stämmer för 27009, 27010, 27011, 27012, 27013, 27014, 27015, 27016, 27017 (antal och namn, inklusive "isblå/ljusblå" och "brun/beige"). 27008 anger inga färger.
- Mer än två "enligt tillverkaren" per text: ingen (högst 1 per produkt: 27009, 27010, 27011, 27015).
- Tre eller fler kommatecken i titel: ingen (27015 har ett).
- Meta utan verb: ingen. Alla har minst ett verb (har, är, mäter, används, väger, finns, tvättas, ingår).
- Mellanslagsfel, mjuka bindestreck, hårda mellanslag, nollbreddstecken: inga.
- Dubbdäck: inga prestanda-, grepp-, säkerhets- eller hälsopåståenden. Endast specifikationer (dubbantal, storlek, vikt, lufttryck). Se anm. 1 om "reflekterande".

## 3. Anmärkningar (språk och påståenden), ordnade efter vikt

Inget av nedan är en avvikelse mot skrivfilen. Det är iakttagelser om texterna själva. Ingen bedöms som blockerande, men 2 och 3 bör avgöras.

1. **26003 (10472304017674), "reflekterande sidor"** i meta ("Dubbdäck från Suomi Tyres med 126 dubbar och reflekterande sidor.") och html ("Dig som behöver ett däck med reflekterande sidor", "Sidor: Reflekterande"). Egenskapen är en synlighetsfunktion och står utan "enligt tillverkaren". Jag kan inte verifiera källan; kontrollera mot leverantörens uppgift. Påståendet är en faktauppgift, inte ett löfte om säkerhet.
2. **27010/27011 (10636616925450, 10636617122058), "Halkfri enligt tillverkaren"** (likaså 27009, 10636616696074: "Yta: Halkfri enligt tillverkaren") och 27015, "Enligt tillverkaren är maximal lastkapacitet per parallett 100 kg." Båda är grepp- respektive säkerhetsnära påståenden. De är hedgade en gång vardera, vilket stämmer med lärdomen 2026-11-04 (lastgräns får stå en gång som "enligt tillverkaren" om källan är svensk och ordagrann). Jag kan inte avgöra om källan var svensk och ordagrann; bekräfta det för 27015 och för "Halkfri".
3. **27008 (10581104427274), "både inomhus och utomhus"** (html två gånger, spec "Miljö: Inomhus och utomhus"). Obedömt bruksanspråk utan "enligt tillverkaren". Samma för 27010/27011 "Mattan går att använda utomhus" (meta, html, spec). Kontrollera mot källa. Titeln "Air Track" är produktnamn, ingen prestandaformulering finns.
4. **27017 (10636701303050), "nedvärmning"** i "Dig som vill ha en matta för nedvärmning och stretch". Ordet "nedvärmning" är inte standardsvenska; avsett ord är troligen "nedvarvning" (cool-down). "stretch" bör vara "stretching" (som i övriga texter). Språkfel.
5. **27017, meta**: "Yogamatta i TPE, 180 x 60 cm, med svart undersida och färgad ovansida med diamantmönster." Första meningen saknar verb (verbet kommer först i andra meningen: "Mattan finns i åtta färger"). Hela metan har verb, så den klarar kontrollen; stilen är dock nominal. "Svart undersida" är en fast egenskap, inte ett variantnamn. Ingen åtgärd krävs.
6. **27016 (10636683018506), titel "Yogabälte i Bomull 260 cm"**: versalt B i "Bomull" mitt i titeln. Övriga titlar i passet använder gemener efter förled ("Yogamatta PVC", men PVC/TPE är förkortningar). Troligen formatfel mot regeln för stor bokstav; kontrollera mot `format_regler.py` eller regelboken. Samma sak i seo.title.
7. **27012 (10636638224650), meta**: "Ringen har mjukt vadderad yta på både in- och utsidan." Saknar obestämd artikel ("en mjukt vadderad yta", som i html). Dessutom "ca 300 g" i meta mot "cirka 300 g" i html (förkortning i meta är OK om regelboken tillåter).
8. **27015 (10636676792586)**: (a) engelska "push ups", "Push Up Bars Low" blandat med svenska; "armhävningar" vore svenska för "push ups" i löptext, men "Push Up Bars" är produktnamn. (b) Titel och meta anger "46 x 39 x 30 cm" utan att säga om måttet gäller en parallett eller paret; i metan följer direkt "Varje parallett väger 4 kg", vilket kan läsas som att måttet gäller paret. (c) "Finns i flera färger" i meta, färglistan i html stämmer (3 st).
9. **27008 (10581104427274)**: variantnamnen är koder (BL, BLU, PI). Texten nämner inga färger, så ingen konflikt, men kunden ser kodnamn i butiken. Gäller variantdata, inte texten. Stilen "som används till" i meta är något stel men korrekt.
10. **26001 (10472189788426)**: "Lufttryck: 2,0–5,0 bar (30–70 psi)" är ett säkerhetsrelevant specifikationsvärde med omräkning (5,0 bar är ca 72 psi). Bekräfta mot leverantörens datablad. Inget "enligt tillverkaren" står där; det är redovisat som faktauppgift.
11. **27014 (10636653822218)**: "Egenskap: Absorberande material" och "av absorberande material" är en produktegenskap utan mätning; ofarligt, men något tomt. "Meta" börjar med "Träningshandduken är gjord av" (annan formulering än html "tillverkad av"): inkonsekvent men inte felaktigt.

Stavfel i övrigt: inga funna. Inga felaktiga böjningar utöver punkt 4, 6 och 7. Movit, Air Track och dubbdäck innehåller inga prestanda-, hälso- eller säkerhetslöften utöver 2 och 3 ovan.

## 4. Begränsningar (öppet)

- Jag har inte kunnat verifiera fakta mot leverantörens källor (ingen källa i uppdraget). Anmärkningarna 1, 2, 3 och 10 är därför "kontrollera", inte "fel".
- Språkbedömningen är en läsning av en AI-modell, inte en korrekturläsning av en människa. Ord som "nedvärmning" bedömdes mot min kunskap om svenska, inte mot ordlista.
- Färg- och påståendeordsökningen (regex) gav falska träffar på "Movit" (innehåller "vit"), "Uppblåsbar" (innehåller "blå") och "Greppets diameter" (mått, inte påstående); dessa är granskade för hand och avförda.
- Jämförelsen gäller läget vid läsningen 2026-11-05. Inget skrevs, inget i Shopify ändrades. `skrivfil_kontroll.py` kördes inte klart (stoppade med fel vid anrop utan argument); jag skrev inga egna jämförelseskript i repot, jämförelsen gjordes i scratchpad.
- Bilder, tema, kategorisidor och Shopify-metafält granskades inte.
