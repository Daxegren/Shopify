# Oberoende granskning av kategoritexter, våg 2, runda 2 (2026-11-17)

Granskare: Opus (oberoende, endast läsning). Inga Shopify-anrop och inga nätverksanrop. Den enda fil som har skrivits är den här rapporten.

**Underlag:** `vag2_texter.py` (texterna, filtid 14:05), `vag2dir/underlag/<handle>.json` (faktaunderlaget, filtid 14:05, gäller), `vag2/rå_<handle>.json` (äldre körning, bara jämförelse), `shopify-sync/docs/kategoritexter-standard.md` (avsnitt 2, 3, 4 och 8) och de fem sista posterna i `LARDOMAR.md` (2026-11-05, 2026-11-12 ×2, 2026-11-17, 2026-11-13).

**Metod:** Varje påstående är kontrollerat mot `alla_titlar` (huvudprodukter som räknas), `ovriga_titlar` (köpbara övriga) och `marken` (vendor med antal), med egna `python3 -I`-skript direkt mot JSON-filerna, inte med `kategori_kontroll.py`. Gorilla Sports Norden och Velomarket räknas som leverantörer, inte märken. Ordantalet räknas på styckena utan den separata "Se även"-meningen (herrcyklar, traningsmaskin). Golv enligt standarden 2: femtal under 30, tiotal från 30, hundratal från 100.

**Felklasser:**
- **FAKTAFEL** = påstående som inte stämmer med underlaget, eller en uppräkning som ser fullständig ut men inte är det och saknar "bland annat"/"till exempel" (standarden 8.4, lärdomen 2026-11-12). Ska rättas före skrivning.
- **ANMÄRKNING** = språk, numerus, marginal, risk eller sammanhang där påståendet ändå är sant. Valfritt att åtgärda, men språkfelen bör rättas.

## Gemensamt för alla nio texter (kontrollerat)

- Första meningen har verb ("säljer") i alla texter, och alla metabeskrivningar börjar med "Köp".
- Inga prisuppgifter: ordet "pris" förekommer bara i meningen "Öppna en produkt för att se pris, lagerstatus och produktuppgifter." Inga belopp, inget "kr".
- Inga förbjudna ord: ingen träff på modell, bäst, perfekt, ledande, kvalitet, säker, leverans, frakt, tillverkning/ursprung, garanti, billig eller prisvärd (sökt i text, SEO-titel och meta).
- "produkter" används genomgående, aldrig "modeller".
- Alla 27 exempeltitlar finns ordagrant i `alla_titlar` (ingen ligger bara bland övriga).
- Ordantal 61–81 (inom 60–200). SEO-titlar 29–42 tecken (högst 43). Metor 120–149 tecken (inom både uppdragets 70–155 och standardens 120–155).
- SEO-titlarna är unika inbördes och krockar inte med någon annan kollektions SEO-titel i `alla_kollektioner_seo_live.json`. Metorna är unika.
- Leverantörerna Gorilla Sports Norden och Velomarket nämns aldrig som märken.

## Översikt

| Kategori | Huvudprodukter (underlag) | "minst N" | Golv | Marginal | Ord | SEO (tecken) | Meta (tecken) | Utfall |
|---|---|---|---|---|---|---|---|---|
| traningsmaskin | 8 | 5 | 5 | 3 | 62 | 32 | 144 | **FEL** (1 faktafel) |
| herrcyklar | 11 (10 unika titlar) | 10 | 10 | 1 (0 på unika titlar) | 63 | 31 | 120 | Godkänd (anmärkningar) |
| hybridcykel | 27 | 25 | 25 | 2 | 78 | 29 | 127 | Godkänd (anmärkningar) |
| traningsbank | 33 | 30 | 30 | 3 | 69 | 42 | 139 | Godkänd (språkanmärkning) |
| grepptraning | 11 | 10 | 10 | 1 | 70 | 42 | 147 | Godkänd (språkanmärkningar) |
| boxning | 30 | 30 | 30 | **0** | 71 | 37 | 139 | Godkänd (anmärkningar) |
| racercykel | 24 | 20 | 20 | 4 | 81 | 39 | 127 | Godkänd (anmärkningar) |
| stankskarmar-cykel | 47 | 40 | 40 | 7 | 74 | 36 | 149 | Godkänd |
| traningsutrustning-for-hemmagym | 714 (709 unika titlar) | 700 | 700 | 14 | 61 | 31 | 139 | Godkänd (anmärkningar) |

De fem faktafelen från runda 1 (F1 traningsbank-meta, F2 och F3 grepptraning, F4 boxning-meta, F5 stankskarmar-meta) är rättade i den nya texten: alla märkeslistor i dessa metor har nu "bland annat" och typlistorna "till exempel".

---

## 1. traningsmaskin: FEL (1 faktafel)

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 5 produkter" (text och meta) | 8 huvudprodukter (huvud_regex tomt), femtalsgolv 5 | Godkänd |
| "träningsmaskiner och hemmagym från bland annat Tunturi, Hammer och Finnlo by Hammer" | Träningsmaskin 2, Hemmagym 2. marken: Tunturi 3, Hammer 2, Finnlo by Hammer 1 (+ leverantören Gorilla Sports Norden 2, de två sissy squat-produkterna) | Godkänd |
| "bland annat träningsmaskiner, hemmagym, latsdragsstation, träningsstation och sissy squat-bänkar" | Latsdragsstation 1, Träningsstation 1, Sissy Squat 2 ("Sissy Squat Profi, Svart, med Justerbara Kuddar", "Sissy Squat-bänk, Svart") | Godkänd i sak (språk, se A1) |
| Exempel: WT85 Leverage Pulley Gym; Hammer Multi-Lat Tower; Hammer Bio Force Extreme Sixpack Plus | Alla 3 ordagrant i alla_titlar | Godkänd |
| SEO "Träningsmaskin – Tunturi, Hammer" (32) | De två märken som har flest | Godkänd |
| **Meta: "Köp träningsmaskin, hemmagym eller latsdragsstation från bland annat …"** | Typlistan saknar "bland annat"/"till exempel". Kollektionen har även **träningsstation (1)** och **sissy squat (2)**, alltså 3 av 8 huvudprodukter som inte ryms i listan | **FAKTAFEL** |

**FAKTAFEL F1 (meta)**
- Före: `Köp träningsmaskin, hemmagym eller latsdragsstation från bland annat Tunturi, Hammer och Finnlo by Hammer. Minst 5 produkter hos BEST OF SPORTS.` (144)
- Efter: `Köp till exempel träningsmaskin, hemmagym eller latsdragsstation från bland annat Tunturi, Hammer och Finnlo by Hammer. Minst 5 produkter.` (138 tecken)
- Belägg: `traningsmaskin.json` → `forsta_ord_i_titel` = sissy 2, träningsmaskin 2, hemmagym 2, latsdragsstation 1, träningsstation 1. `alla_titlar` innehåller "Träningsstation Hammer Bio Force Extreme Sixpack Plus", "Sissy Squat Profi, Svart, med Justerbara Kuddar" och "Sissy Squat-bänk, Svart".
- Not: runda 1 (A2) bedömde samma mening som anmärkning med motiveringen att "Köp X, Y eller Z" är en uppmaning. Jag gör en annan bedömning: standarden 8.4 gäller "varje uppräkning som inte är bevisat fullständig", metan står ensam i sökresultatet utan brödtextens "bland annat"-mening, och listan utelämnar 3 av 8 produkter. Det är samma typ av fel som lärdomen 2026-11-12 beskriver. Om David hellre följer runda 1:s tolkning sjunker antalet faktafel till 0.

**Anmärkningar**
- A1. Språk: uppräkningen blandar plural och singular ("träningsmaskiner, hemmagym, latsdragsstation, träningsstation och sissy squat-bänkar"). Förslag: "Kategorin omfattar bland annat träningsmaskiner, hemmagym, en latsdragsstation, en träningsstation och sissy squat-bänkar." (texten får 64 ord)
- A2. Första meningen "säljer träningsmaskiner och hemmagym" nämner bara två av fem typer utan "bland annat". Andra meningen räknar upp alla med "bland annat", och standardens mall för första meningen ser ut så här, så det räknas inte som fel.
- A3. Texten har 62 ord, nära gränsen 60.

## 2. herrcyklar: godkänd

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 10 produkter" (text och meta) | 11 huvudprodukter, femtalsgolv 10. "Herrcykel ROMET Orkan M, grå-röd" förekommer två gånger: 10 unika titlar | Godkänd, marginal 1 (0 på unika titlar) |
| "herrcyklar och stadscyklar" | herrcykel 8, stadscykel 3 (fullständigt för huvudprodukterna) | Godkänd |
| "från bland annat Romet, Giant och Tabou" | Romet 7, Giant 3, Tabou 1 | Godkänd |
| "Romet har flest produkter" | 7 mot 3 och 1 | Godkänd |
| "Några produkter anger 27 växlar eller 28 tum" | 27 Växlar: 1 (Wagant 8). 28 tum: 2 (Romet Orkan M, Tabou Kinetic 1.0) | Godkänd |
| Exempel: Romet Wagant 7; Tabou Kinetic 1.0, 28 tum; Giant Attend RS 2 GTS, Svart | Alla 3 ordagrant | Godkänd |
| SEO "Herrcykel – Romet, Giant, Tabou" (31) | De tre märkena i ordning efter antal | Godkänd |
| Meta (120) | "bland annat" före märkena; "herrcykel eller stadscykel" är fullständigt | Godkänd |

**Anmärkningar**
- A4. Marginal 0 räknat på unika titlar. Säljs en cykel slut före skrivning blir "minst 10" fel. Kör om underlaget direkt före skrivning (standarden 8.1).
- A5. Kan vilseleda: kollektionen har också 3 köpbara produkter som inte är cyklar ("Boxningsdocka Tunturi Slam Man", "Multivitamin för Män Trec, 90 kapslar", "Kosttillskott Trec Essensey Multivit For Him + Maca Root, 90 kapslar"). Texten påstår inget om dem; det är en taggfråga. Kosttillskott ligger under `utanfor_tills_vidare`.
- A6. Metan har exakt 120 tecken, standardens nedre gräns.

## 3. hybridcykel: godkänd

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 25 produkter" (text och meta) | 27, femtalsgolv 25 | Godkänd, marginal 2 |
| "från Romet och Giant" (text och meta) | Romet 16, Giant 11, inga andra märken bland huvudprodukterna | Godkänd (bevisat fullständig) |
| "Romet har flest produkter" | 16 mot 11 | Godkänd |
| "till exempel 11, 18 eller 21 växlar" / meta "bland annat med 11, 18 eller 21 växlar" | 11: 2, 18: 3, 21: 6 (24: 3 finns också, täcks av "till exempel"/"bland annat") | Godkänd |
| "även andra produkter, bland annat barnstolar, cykelväskor och sparkcyklar" | Bland 55 övriga: barnstol/barnsits 9, cykelväska 4, sparkcykel 11 | Godkänd |
| Exempel: Giant Escape 3 Disc …; Romet Wagant 3, 21 Växlar, Blå; Giant Roam 2, 700c, Svart | Alla 3 ordagrant | Godkänd |
| SEO "Hybridcykel – Giant och Romet" (29) | | Godkänd |

**Anmärkningar**
- A7. Bland övriga finns andra cyklar (Liv Flourish, Excelsior Swan Urban, Romet Gazela, elcyklar från Giant, Tenways och Victoria). "från Romet och Giant" stämmer enligt underlagets definition; "från bland annat Romet och Giant" vore säkrare om underlagets regel ändras.
- A8. Meta: "Här finns minst 25 produkter, bland annat med 11, 18 eller 21 växlar" är lite tungt (oförändrat sedan runda 1, A6).

## 4. traningsbank: godkänd (språkanmärkning)

Underlaget har ändrats sedan runda 1: kollektionen har nu 62 produkter (tidigare 41) och 33 köpbara huvudprodukter (tidigare 19–20), med 14 nya titlar (bland annat BH Fitness Weight Bench, Hammer Force 2.0/4.0/5.0/6.0, Tunturi CT80, UB40, UB70). Texten är anpassad till det nya underlaget.

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 30 produkter" (text och meta) | 33, tiotalsgolv 30 | Godkänd, marginal 3 |
| "från bland annat Tunturi, Hammer, BH Fitness, Finnlo by Hammer och Christopeit" | Tunturi 17, Hammer 5, BH Fitness 4, Finnlo by Hammer 3, Christopeit 3 (+ leverantören Gorilla Sports Norden 1) | Godkänd |
| "Tunturi har flest produkter" | 17 (även räknat i titlarna, inkl. "TUNTURI") mot 5 | Godkänd |
| "Flera träningsbänkar är hopfällbara eller justerbara enligt produktnamnet" | Hopfällbar 3, Justerbar 7 | Godkänd |
| "det finns bland annat magbänk" | 1 titel: "Träningsbänk Tunturi AB20 Magbänk, Justerbar" | Godkänd i sak (språk, se A9) |
| Exempel: Centuri UB100 Utility Bench; Christopeit AB 1000; WB20 Basic Weight Bench | Alla 3 ordagrant | Godkänd |
| SEO "Träningsbänk – Tunturi, Hammer, BH Fitness" (42) | De tre märken som har flest | Godkänd |
| Meta (139): "från bland annat Tunturi, Hammer, BH Fitness och Christopeit, till exempel hopfällbar eller justerbar" | Märken med "bland annat", egenskaper med "till exempel" | Godkänd |

**Anmärkningar**
- A9. Språk: "det finns bland annat magbänk" saknar artikel. Förslag: "… och det finns bland annat en magbänk." (70 ord)
- A10. Dubblerat innehåll: exempeltiteln "Träningsbänk Tunturi WB20 Basic Weight Bench" används också i traningsutrustning-for-hemmagym. Byt i en av texterna, till exempel till "Träningsbänk Tunturi FB20 Flat Bench" här.
- A11. Underlaget ändrades kraftigt mellan körningarna samma dag (41 → 62 produkter i kollektionen). Kör om underlaget direkt före skrivning och kontrollera att de nya bänkarna är avsiktligt taggade.

## 5. grepptraning: godkänd (språkanmärkningar)

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 10 produkter" (text och meta) | 11, femtalsgolv 10 | Godkänd, marginal 1 |
| "från bland annat Gymstick" | Gymstick 9 (+ leverantören Gorilla Sports Norden 2) | Godkänd |
| "till exempel fingerexpandrar, handtränare, greppstärkare och greppringar" (text och meta) | Fingerexpander 2, Handtränare 2, Greppstärkare 2, Greppringar 1 | Godkänd (runda 1 F2/F3 rättade) |
| "justerbart motstånd eller är justerbara i produktnamnet" | "Justerbart Motstånd" 1, "Justerbar" 1 (Handtränare), "Justerbart handtag" 1 | Godkänd i sak (språk, se A12) |
| "även ett viktset och ett justerbart handtag" | "Viktset Gymstick Vinyl Grip Pump Set, 20 kg", "Justerbart handtag, lätt" | Godkänd |
| Exempel: Fingerexpander Gymstick Active, Set med 2 st; Handtränare Gymstick, Justerbar, med Räknare; Greppstärkare Gymstick Active Power | Alla 3 ordagrant | Godkänd |
| SEO "Greppträning – Handtränare, fingerexpander" (42) | | Godkänd (se A14) |

**Anmärkningar**
- A12. Språk: "Några produkter anger justerbart motstånd eller är justerbara i produktnamnet" säger att produkterna är justerbara "i produktnamnet". Förslag: "Några produkter är justerbara enligt produktnamnet, till exempel med justerbart motstånd, och kategorin omfattar även ett viktset och ett justerbart handtag." (72 ord)
- A13. "säljer greppträning" beskriver en aktivitet, inte en vara. Förslag: "säljer produkter för greppträning".
- A14. SEO-titeln har inkonsekvent versalisering ("Handtränare" men "fingerexpander"). Förslag: "Greppträning – handtränare, fingerexpander".
- A15. Ett viktset på 20 kg och "Extra Grepp Barbell Grips" i greppträning är en taggfråga; texten redovisar viktsetet öppet.

## 6. boxning: godkänd (anmärkningar)

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 30 produkter" (text och meta) | 30, tiotalsgolv 30 | Godkänd, **marginal 0** |
| "bland annat boxningshandskar, boxningssäckar och boxningsdockor" | Boxningshandskar 11 (+ 2 "Boxing gloves HAMMER"), Boxningssäck 5, Boxningsdocka 2 | Godkänd |
| "från bland annat Tunturi, Toorx, Hammer och Gymstick" (text och meta) | Tunturi 14, Toorx 7, Hammer 3, MAXXUS 2, Gymstick 2, Zipro 1 | Godkänd (runda 1 F4 rättat) |
| "Tunturi har flest produkter" | 14 mot 7 | Godkänd |
| "bland annat 10, 12, 14 och 16 oz" | 10 oz 3, 12 oz 4, 14 oz 2, 16 oz 1 | Godkänd |
| Exempel: Toorx Leopard, 12 oz, Polyuretan; Tunturi Classic Boxing Bag 80 cm, inkl. kedja; Tunturi Slam Man | Alla 3 ordagrant | Godkänd |
| Meta (139): "till exempel handskar, säckar och dockor" | | Godkänd |

**Anmärkningar**
- A16. Marginal 0: säljs en produkt slut före skrivning blir "minst 30" fel (golvet blir 25). Kör om underlaget direkt före skrivning.
- A17. SEO-titeln "Boxning – Handskar, säckar och dockor" ser ut som en fullständig typlista, men kollektionen har också skyddshjälmar (2), speedbag/speedball, handlindor, innerhandskar, benskydd och en stående boxboll (12 av 30 produkter). Standarden 4 tillåter att SEO-titeln räknar upp de vanligaste märkena utan "bland annat", och 43-teckengränsen ger inte plats; därför anmärkning, inte faktafel. Förslag om man vill: "Boxning – handskar, säckar, dockor m.m." (39 tecken).

## 7. racercykel: godkänd (anmärkningar)

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 20 produkter" (text och meta) | 24, femtalsgolv 20 | Godkänd, marginal 4 |
| "landsvägscyklar och racercyklar från Giant" | Landsvägscykel 23, Racercykel 1; Giant 24 (enda märket) | Godkänd |
| "kolfiber eller carbon i produktnamnet" | kolfiber 1, Carbon 5 | Godkänd (se A18) |
| "serier som TCR, Defy, Contend och Propel" / meta "bland annat serierna …" | TCR 10, Defy 5, Contend 5, Propel 4 | Godkänd |
| "även andra produkter, bland annat tillbehör som pedaler och pedalblock samt motionscyklar och sparkcyklar" | Bland 32 övriga: Pedaler 3, Pedalblock 2 (+ Pedalplattor 1), Motionscykel 2, Spinningcykel 2, trick-/stuntsparkcyklar 6 | Godkänd |
| Exempel: Contend 1, 700x28c, Rosewood; Defy Advanced 2, 700x32c, Abyss Black; Propel Advanced 2, 700c, Carbon | Alla 3 ordagrant | Godkänd |
| SEO (39), meta (127) | | Godkänd |

**Anmärkningar**
- A18. "Carbon" står i fyra av fem titlar på färgens plats ("700c, Carbon") och kan vara ett färgnamn. Texten säger bara att produktnamnet anger det, vilket stämmer.
- A19. Språk (smärre): "serier som TCR, Defy, Contend och Propel finns" har omvänd ordföljd. Förslag: "… och det finns serier som TCR, Defy, Contend och Propel."
- A20. Underlaget: "Cykel Giant TCR Advanced 2 Disc-PC Hematite" ligger bland övriga trots att huvud_regex innehåller `^cykel giant tcr`. Räknas den blir antalet 25; "minst 20" är ändå sant. Kontrollera regeln i `kategorier_underlag.py` (oförändrat sedan runda 1, A16).

## 8. stankskarmar-cykel: godkänd

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 40 produkter" (text och meta) | 47, tiotalsgolv 40 | Godkänd, marginal 7 |
| "bland annat stänkskärmset, framskärmar och bakskärmar" / meta "till exempel …" | Stänkskärmset 14 (+ Stänkskärmsset 2), Framskärm 12, Bakskärm 10 | Godkänd |
| "från bland annat Hebie, SKS, Giant och Ass Savers" (text och meta) | Hebie 17, SKS 14, Giant 8, Ass Savers 3, Academy 1, XLC 1 (Velomarket 3 är leverantör) | Godkänd (runda 1 F5 rättat) |
| "Hebie och SKS har flest produkter" | Vendor: Hebie 17, SKS 14, nästa Giant 8. I titlarna: Hebie 17, SKS 17 | Godkänd med båda räknesätten |
| "till exempel 28 tum eller 26–29 tum" | "28 tum" i 2 titlar, "26–29 tum" i 6 | Godkänd |
| Exempel: Hebie Taipan Trekking, 28 tum, Svart; SKS Shockblade för 28–29 tum; Giant Speedshield Clip-On | Alla 3 ordagrant | Godkänd |
| SEO "Stänkskärm cykel – Hebie, SKS, Giant" (36) | De tre märken som har flest | Godkänd |

Inga anmärkningar utöver att metan (149) ligger nära övre gränsen 155.

## 9. traningsutrustning-for-hemmagym: godkänd (anmärkningar)

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 700 produkter" (text och meta) | 714, hundratalsgolv 700; 709 unika titlar | Godkänd, marginal 14 (9 på unika titlar) |
| "från bland annat Tunturi, Toorx, Hammer, BH Fitness och Christopeit" | De fem största i marken: 295, 141, 80, 55, 54 | Godkänd |
| "bland annat motionscyklar, löpband, roddmaskiner, träningsbänkar, kettlebells och viktskivor" (text) och motsvarande i meta | Titlar som börjar med typordet: motionscykel 58, löpband 45, roddmaskin 21, träningsbänk 30, kettlebell 28, viktskiv- 59 | Godkänd |
| Exempel: Motionscykel Tunturi Signature E60; Träningsbänk Tunturi WB20 Basic Weight Bench; Kettlebell Tunturi Competition, 8 kg | Alla 3 ordagrant | Godkänd |
| SEO "Träningsutrustning för hemmagym" (31) | Typord, ingen märkeslista | Godkänd |

**Anmärkningar**
- A21. Texten har 61 ord, en mening från att hamna under 60.
- A22. Exempeltiteln "Träningsbänk Tunturi WB20 Basic Weight Bench" dubbleras med traningsbank (se A10).
- A23. Vendor Trec (14) är här träningshandskar, flaskor och krita, inte kosttillskott. Kollektionen innehåller också produkter från kategorier under `utanfor_tills_vidare` (till exempel akupressurmattor och vibrationsplattor), men texten påstår inget om dem.

---

## Sammanställning

### Faktafel

| Nr | Kategori | Fält | Fel | Belägg i underlaget |
|---|---|---|---|---|
| F1 | traningsmaskin | meta | Typlistan "träningsmaskin, hemmagym eller latsdragsstation" ser fullständig ut men saknar "bland annat"/"till exempel"; träningsstation (1) och sissy squat (2) saknas | `forsta_ord_i_titel`, `alla_titlar` i `traningsmaskin.json` |

### Anmärkningar som bör rättas före skrivning (språk)
A1 (traningsmaskin, numerus), A9 (traningsbank, "en magbänk"), A12 och A13 (grepptraning, "justerbara i produktnamnet", "säljer greppträning"), A14 (grepptraning, versalisering i SEO-titeln), A10/A22 (dubblerad exempeltitel WB20).

### Risker inför skrivning
Boxning har marginal 0 och herrcyklar marginal 0 räknat på unika titlar. Traningsbank ändrades kraftigt mellan körningarna samma dag. Kör om underlaget och denna kontroll direkt före skrivning (standarden 8.1, lärdomen 2026-11-17).

Inga antal är fel, alla "flest"-påståenden stämmer, alla nämnda typer, egenskaper och tal finns i titlarna, och alla exempeltitlar finns ordagrant. Inget i texterna rör priser, villkor eller ursprung.

Antal faktafel: 1
