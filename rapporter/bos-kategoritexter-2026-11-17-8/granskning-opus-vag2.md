# Oberoende granskning av kategoritexter, våg 2, runda 3 (2026-11-17)

Granskare: Opus (oberoende, endast läsning). Inga Shopify-anrop och inga nätverksanrop. Den enda fil som har skrivits är den här rapporten.

**Underlag:**
- Texterna: `vag2_texter.py` (filtid 14:13). Jämförd mot `vag2_texter_efter_runda2_fore_rattelse.py` för att se vad som rättats.
- Faktaunderlaget: `vag2dir/underlag/<handle>.json` (filtid 14:30, gäller). `vag2/rå_<handle>.json` (13:56) är bara jämförelse.
- Standarden `kategoritexter-standard.md` avsnitt 2, 3, 4 och 8, och de fem sista posterna i `LARDOMAR.md`.
- Tidigare rundor: `granskning-opus-vag2-runda1.md` och `granskning-opus-vag2-runda2.md`.

**Metod:** Varje påstående är kontrollerat med egna `python3 -I`-skript direkt mot JSON-filerna (inte med `kategori_kontroll.py`): `alla_titlar` (huvudprodukter som räknas), `ovriga_titlar` (köpbara övriga) och `marken` (vendor med antal). Gorilla Sports Norden och Velomarket räknas som leverantörer, inte märken. Golv enligt standarden: femtal under 30, tiotal från 30. Ordantal räknas på styckena utan länkmeningen i `vag2_tillagg.json` (herrcyklar, traningsmaskin), som inte ingår i granskningen. traningsutrustning-for-hemmagym granskas inte (hålls tillbaka).

**Felklasser:**
- **FAKTAFEL** = påstående som inte stämmer med underlaget, eller en uppräkning som ser fullständig ut men inte är det och saknar "bland annat"/"till exempel". Ska rättas före skrivning.
- **ANMÄRKNING** = stil, språk, marginal, risk eller sammanhang där påståendet ändå stämmer. Valfritt att åtgärda.

## Gemensamt för alla åtta texter (kontrollerat)

- Första meningen har verb ("säljer") i alla texter. Alla metabeskrivningar börjar med "Köp".
- Inga prisuppgifter: inga belopp, inget "kr". Ordet "pris" finns bara i meningen "Öppna en produkt för att se pris, lagerstatus och produktuppgifter."
- Inga förbjudna ord i text, SEO-titel eller meta (sökt bland annat på modell, bäst, perfekt, ledande, kvalitet, säker, leverans, frakt, garanti, billig, prisvärd, tillverk, ursprung, populär, störst, enda).
- "produkter" används genomgående, aldrig "modeller".
- Alla 24 exempeltitlar finns ordagrant i `alla_titlar` (ingen ligger bara bland övriga).
- Ordantal 63–81 (inom 60–200). SEO-titlar 29–42 tecken (högst 43). Metor 120–149 tecken (inom både 70–155 och standardens 120–155).
- SEO-titlarna och metorna är unika inbördes och krockar inte med någon annan kollektions SEO-titel eller meta i `alla_kollektioner_seo_live.json`.
- Leverantörerna Gorilla Sports Norden och Velomarket nämns aldrig som märken.
- Inga max- eller min-påståenden (vikt, pris, storlek) finns i texterna, så övriga köpbara produkter kan inte motsäga något sådant (lärdomen 2026-11-17).

## Översikt

| Kategori | Huvudprodukter (underlag) | "minst N" | Golv | Marginal | Ord | SEO (tecken) | Meta (tecken) | Utfall |
|---|---|---|---|---|---|---|---|---|
| traningsmaskin | 8 | 5 | 5 | 3 | 64 | 32 | 138 | Godkänd |
| herrcyklar | 11 (10 unika titlar) | 10 | 10 | 1 (**0** på unika titlar) | 63 | 31 | 120 | Godkänd (anmärkningar) |
| hybridcykel | 27 | 25 | 25 | 2 | 78 | 29 | 127 | Godkänd (anmärkningar) |
| traningsbank | 33 | 30 | 30 | 3 | 70 | 42 | 139 | Godkänd (anmärkningar) |
| grepptraning | 11 | 10 | 10 | 1 | 72 | 42 | 136 | Godkänd (anmärkning) |
| boxning | 30 | 30 | 30 | **0** | 71 | 37 | 139 | Godkänd (anmärkningar) |
| racercykel | 24 | 20 | 20 | 4 | 81 | 39 | 127 | Godkänd (anmärkningar) |
| stankskarmar-cykel | 47 | 40 | 40 | 7 | 74 | 36 | 149 | Godkänd |

## Rättelser sedan tidigare rundor

| Runda | Fel/anmärkning | Status nu |
|---|---|---|
| 1 F1 | traningsbank-meta: märkeslista utan "bland annat" | Rättat ("från bland annat Tunturi, Hammer, BH Fitness och Christopeit") |
| 1 F2, F3 | grepptraning text och meta: typlista utan "bland annat" | Rättat ("till exempel …") |
| 1 F4 | boxning-meta: märkeslista utan "bland annat" | Rättat |
| 1 F5 | stankskarmar-meta: märkeslista utan "bland annat" | Rättat |
| 2 F1 | traningsmaskin-meta: typlista utan "till exempel" | Rättat: `Köp till exempel träningsmaskin, hemmagym eller latsdragsstation från bland annat Tunturi, Hammer och Finnlo by Hammer. Minst 5 produkter.` |
| 2 A1 | traningsmaskin: plural/singular i uppräkningen | Rättat ("en latsdragsstation, en träningsstation") |
| 2 A9 | traningsbank: "bland annat magbänk" | Rättat ("en magbänk") |
| 2 A12 | grepptraning: "justerbara i produktnamnet" | Rättat ("enligt produktnamnet") |
| 2 A13 | grepptraning: "säljer greppträning" | Rättat ("säljer redskap för greppträning", även i metan) |
| 2 A14 | grepptraning: versalisering i SEO-titeln | Inte rättat (se A6 nedan) |
| 2 A10 | dubblerad exempeltitel WB20 (traningsbank och hemmagym) | Inte rättat (se A4 nedan) |
| 2 A19 | racercykel: ordföljd "serier som … finns" | Inte rättat (se A9 nedan) |

Inga nya faktafel har tillkommit genom rättelserna. Den enda textändring som inte kom från en anmärkning är grepptraning-metan, som nu räknar upp tre typer i stället för fyra; den står efter "till exempel" och är korrekt.

---

## 1. traningsmaskin: godkänd

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 5 produkter" (text och meta) | 8 huvudprodukter (huvud_regex tomt, alla köpbara räknas), femtalsgolv 5 | Godkänd, marginal 3 |
| "träningsmaskiner och hemmagym från bland annat Tunturi, Hammer och Finnlo by Hammer" | Träningsmaskin 2, Hemmagym 2. marken: Tunturi 3, Hammer 2, Finnlo by Hammer 1 (+ leverantören Gorilla Sports Norden 2, de två sissy squat-produkterna) | Godkänd |
| "bland annat träningsmaskiner, hemmagym, en latsdragsstation, en träningsstation och sissy squat-bänkar" | forsta_ord_i_titel: sissy 2, träningsmaskin 2, hemmagym 2, latsdragsstation 1, träningsstation 1 | Godkänd |
| Exempel: Tunturi WT85 Leverage Pulley Gym; Hammer Multi-Lat Tower; Hammer Bio Force Extreme Sixpack Plus | Alla 3 ordagrant i alla_titlar | Godkänd |
| SEO "Träningsmaskin – Tunturi, Hammer" (32) | De två märken som har flest | Godkänd |
| Meta (138): "Köp till exempel träningsmaskin, hemmagym eller latsdragsstation från bland annat …" | Typer med "till exempel", märken med "bland annat" | Godkänd (runda 2 F1 rättat) |

**Anmärkningar**
- A1. Första meningen "säljer träningsmaskiner och hemmagym" nämner två av fem typer utan "bland annat", men nästa mening räknar upp alla typer, och formen följer standardens mall. Samma bedömning som runda 2 (A2): inte fel.

## 2. herrcyklar: godkänd (anmärkningar)

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 10 produkter" (text och meta) | 11 huvudprodukter, femtalsgolv 10. "Herrcykel ROMET Orkan M, grå-röd" förekommer två gånger, så 10 unika titlar | Godkänd, marginal 1 (0 på unika titlar) |
| "herrcyklar och stadscyklar" | herrcykel 8, stadscykel 3 (fullständigt för huvudprodukterna) | Godkänd |
| "från bland annat Romet, Giant och Tabou" | Romet 7, Giant 3, Tabou 1 (samma antal räknat i titlarna) | Godkänd |
| "Romet har flest produkter" | 7 mot 3 och 1 | Godkänd |
| "Några produkter anger 27 växlar eller 28 tum i produktnamnet" | "27 Växlar" 1 (Wagant 8), "28 tum" 2 (Romet Orkan M, Tabou Kinetic 1.0) | Godkänd |
| Exempel: Romet Wagant 7; Tabou Kinetic 1.0, 28 tum; Giant Attend RS 2 GTS, Svart | Alla 3 ordagrant | Godkänd |
| SEO "Herrcykel – Romet, Giant, Tabou" (31) | De tre märkena i ordning efter antal | Godkänd |
| Meta (120) | "bland annat" före märkena; "herrcykel eller stadscykel" är fullständigt | Godkänd |

**Anmärkningar**
- A2. Marginal 0 räknat på unika titlar. Säljs en cykel slut före skrivning blir "minst 10" fel. Kör om underlaget direkt före skrivning (standarden 8.1).
- A3. Kan vilseleda (taggfråga, inte textfel): kollektionen har 3 köpbara produkter som inte är cyklar: "Boxningsdocka Tunturi Slam Man", "Multivitamin för Män Trec, 90 kapslar" och "Kosttillskott Trec Essensey Multivit For Him + Maca Root, 90 kapslar". Kosttillskott ligger under `utanfor_tills_vidare`. Metan har exakt 120 tecken, standardens nedre gräns.
- Observation utanför granskningen: länkmeningen för herrcyklar i `vag2_tillagg.json` är inte en "Se även"-mening utan "Vi har även cyklar från Romet." (med länk till /collections/romet). Den är inte granskad här.

## 3. hybridcykel: godkänd (anmärkningar)

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 25 produkter" (text och meta) | 27, femtalsgolv 25 | Godkänd, marginal 2 |
| "från Romet och Giant" (text och meta) | Romet 16, Giant 11; inga andra märken bland huvudprodukterna | Godkänd (bevisat fullständig) |
| "Romet har flest produkter" | 16 mot 11 | Godkänd |
| "till exempel 11, 18 eller 21 växlar" / meta "bland annat med 11, 18 eller 21 växlar" | 11 Växlar 2, 18 Växlar 3, 21 Växlar 6 (24 Växlar 3 finns också, täcks av "till exempel"); 14 av 27 anger växlar | Godkänd |
| "även andra produkter, bland annat barnstolar, cykelväskor och sparkcyklar" | Bland 55 övriga: barnstol/barnsits 9, cykelväska/pakväska 4, sparkcykel/scooter 15 | Godkänd |
| Exempel: Giant Escape 3 Disc, 700x38c, Metallic Blue; Romet Wagant 3, 21 Växlar, Blå; Giant Roam 2, 700c, Svart | Alla 3 ordagrant | Godkänd |
| SEO "Hybridcykel – Giant och Romet" (29) | | Godkänd |

**Anmärkningar**
- A4h. Bland övriga finns andra cyklar som en kund kan uppfatta som hybridcyklar (Liv Flourish, Excelsior Swan Urban, Romet Gazela, elcyklar från Giant, Tenways och Victoria) och dessutom löpband och crosstrainers ("Hybridtränare Christopeit AX 6500"). "från Romet och Giant" stämmer enligt underlagets definition; "från bland annat Romet och Giant" vore säkrare om regeln ändras. Oförändrat sedan runda 2 (A7).
- A5h. Metan "Här finns minst 25 produkter, bland annat med 11, 18 eller 21 växlar, hos BEST OF SPORTS" är tung. Oförändrat sedan runda 1 (A6).

## 4. traningsbank: godkänd (anmärkningar)

Underlaget har växt sedan runda 1 (rå-filen 13:56: 20 köpbara, huvud_regex tomt). Det gällande underlaget (14:30) har 62 produkter i kollektionen, 34 köpbara, varav 33 huvudprodukter (huvud_regex `träningsbänk`) och 1 övrig ("Sissy Squat-bänk, Svart"). 14 nya titlar har tillkommit, bland annat BH Fitness Weight Bench/Optima Press, Hammer Force 2.0–6.0, Tunturi CT80, UB40, UB70 och två Platinum-bänkar. Texten är kontrollerad mot det nya underlaget.

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 30 produkter" (text och meta) | 33 (33 unika titlar), tiotalsgolv 30 | Godkänd, marginal 3 |
| "från bland annat Tunturi, Hammer, BH Fitness, Finnlo by Hammer och Christopeit" | marken: Tunturi 17, Hammer 5, BH Fitness 4, Finnlo by Hammer 3, Christopeit 3, Gorilla Sports Norden 1 (leverantör). Samma antal räknat i titlarna | Godkänd |
| "Tunturi har flest produkter" | 17 mot 5 | Godkänd |
| "Flera träningsbänkar är hopfällbara eller justerbara enligt produktnamnet" | Hopfällbar 3 (Tricon Flex, CT40, UB20), Justerbar 7 (+ "Weight Bench Adjustable") | Godkänd |
| "det finns bland annat en magbänk" | "Träningsbänk Tunturi AB20 Magbänk, Justerbar" | Godkänd (runda 2 A9 rättat) |
| Exempel: Tunturi Centuri UB100 Utility Bench; Christopeit AB 1000; Tunturi WB20 Basic Weight Bench | Alla 3 ordagrant | Godkänd |
| SEO "Träningsbänk – Tunturi, Hammer, BH Fitness" (42) | De tre märken som har flest (17, 5, 4) | Godkänd |
| Meta (139): "från bland annat Tunturi, Hammer, BH Fitness och Christopeit, till exempel hopfällbar eller justerbar. Minst 30 produkter." | Märken med "bland annat", egenskaper med "till exempel" | Godkänd |

**Anmärkningar**
- A4. Dubblerat innehåll: exempeltiteln "Träningsbänk Tunturi WB20 Basic Weight Bench" används också i traningsutrustning-for-hemmagym. Den texten hålls tillbaka, men om den skrivs senare bör en av titlarna bytas, till exempel till "Träningsbänk Tunturi FB20 Flat Bench" här. Oförändrat sedan runda 2 (A10).
- A5. Marginal 3 vilar på att de 21 bänkar som taggades i dag ligger kvar i kollektionen. Utan dem är antalet runt 20 och "minst 30" blir fel. Kör om underlaget direkt före skrivning.

## 5. grepptraning: godkänd (anmärkning)

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 10 produkter" (text och meta) | 11, femtalsgolv 10 | Godkänd, marginal 1 |
| "redskap för greppträning från bland annat Gymstick" | marken: Gymstick 9, Gorilla Sports Norden 2 (leverantör) | Godkänd |
| "till exempel fingerexpandrar, handtränare, greppstärkare och greppringar" | Fingerexpander 2, Handtränare 2, Greppstärkare 2, Greppringar 1 | Godkänd |
| "Några produkter anger justerbart motstånd eller är justerbara enligt produktnamnet" | "Justerbart Motstånd" 1, "Justerbar" 1 (Handtränare); totalt 2 | Godkänd |
| "även ett viktset och ett justerbart handtag" | "Viktset Gymstick Vinyl Grip Pump Set, 20 kg", "Justerbart handtag, lätt" | Godkänd |
| Exempel: Fingerexpander Gymstick Active, Set med 2 st; Handtränare Gymstick, Justerbar, med Räknare; Greppstärkare Gymstick Active Power | Alla 3 ordagrant | Godkänd |
| SEO "Greppträning – Handtränare, fingerexpander" (42) | Båda typerna finns (2 vardera) | Godkänd (se A6) |
| Meta (136): "Köp redskap för greppträning från bland annat Gymstick, till exempel handtränare, fingerexpandrar och greppstärkare. Minst 10 produkter." | | Godkänd |

**Anmärkningar**
- A6. SEO-titeln har inkonsekvent versalisering ("Handtränare" men "fingerexpander"). Förslag: "Greppträning – handtränare, fingerexpander". Oförändrat sedan runda 2 (A14).
- A7. Marginal 1. Ett viktset på 20 kg och "Extra Grepp Barbell Grips" i greppträning är en taggfråga; texten redovisar viktsetet öppet.

## 6. boxning: godkänd (anmärkningar)

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 30 produkter" (text och meta) | 30, tiotalsgolv 30 | Godkänd, **marginal 0** |
| "bland annat boxningshandskar, boxningssäckar och boxningsdockor" | Boxningshandskar 13 (Hammer X-Shock har nu svenska titlar), Boxningssäck 5, Boxningsdocka 2 | Godkänd |
| "från bland annat Tunturi, Toorx, Hammer och Gymstick" (text och meta) | Tunturi 14, Toorx 7, Hammer 3, MAXXUS 2, Gymstick 2, Zipro 1, Gorilla Sports Norden 1 (leverantör) | Godkänd |
| "Tunturi har flest produkter" | 14 mot 7 | Godkänd |
| "Boxningshandskar finns i bland annat 10, 12, 14 och 16 oz" | 10 oz 3, 12 oz 4, 14 oz 2, 16 oz 1 | Godkänd |
| Exempel: Toorx Leopard, 12 oz, Polyuretan; Tunturi Classic Boxing Bag 80 cm, inkl. kedja; Tunturi Slam Man | Alla 3 ordagrant | Godkänd |
| SEO "Boxning – Handskar, säckar och dockor" (37) | | Godkänd (se A8) |
| Meta (139): "till exempel handskar, säckar och dockor, från bland annat …" | | Godkänd |

**Anmärkningar**
- A8. Marginal 0: säljs eller avpubliceras en enda produkt före skrivning blir "minst 30" fel (golvet blir 25). Kör om underlaget direkt före skrivning.
- A8b. SEO-titeln ser ut som en fullständig typlista, men 12 av 30 produkter är andra typer (skyddshjälmar, speedbag/speedball, handlindor, innerhandskar, benskydd, stående boxboll). Standarden 4 och 43-teckengränsen gör att det inte räknas som fel. Förslag: "Boxning – handskar, säckar, dockor m.m." (39 tecken). Oförändrat sedan runda 2 (A17).

## 7. racercykel: godkänd (anmärkningar)

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 20 produkter" (text och meta) | 24, femtalsgolv 20 | Godkänd, marginal 4 |
| "landsvägscyklar och racercyklar från Giant" | Landsvägscykel 23, Racercykel 1; Giant 24 (enda märket bland huvudprodukterna) | Godkänd |
| "Flera produkter anger kolfiber eller carbon i produktnamnet" | kolfiber 1, Carbon 5 | Godkänd |
| "serier som TCR, Defy, Contend och Propel finns" / meta "bland annat serierna …" | TCR 10, Defy 5, Contend 5, Propel 4 (= alla 24) | Godkänd |
| "även andra produkter, bland annat tillbehör som pedaler och pedalblock samt motionscyklar och sparkcyklar" | Bland 32 övriga: Pedaler 3, Pedalblock 2 (+ Pedalplattor 1), Motionscykel 2 (+ Spinningcykel 2), Trick-/Stuntsparkcykel 6 | Godkänd |
| Exempel: Contend 1, 700x28c, Rosewood; Defy Advanced 2, 700x32c, Abyss Black; Propel Advanced 2, 700c, Carbon | Alla 3 ordagrant | Godkänd |
| SEO "Racercykel – Landsvägscyklar från Giant" (39), meta (127) | | Godkänd |

**Anmärkningar**
- A9. Språk: "serier som TCR, Defy, Contend och Propel finns" har ovanlig ordföljd. Förslag: "… och det finns serier som TCR, Defy, Contend och Propel." Oförändrat sedan runda 2 (A19).
- A10. "Carbon" står i fyra av fem titlar på färgens plats ("700c, Carbon") och kan vara ett färgnamn. Texten säger bara att produktnamnet anger det, vilket stämmer.
- A11. Underlaget: "Cykel Giant TCR Advanced 2 Disc-PC Hematite" ligger bland övriga trots att huvud_regex innehåller `^cykel giant tcr`. Räknas den blir antalet 25; "minst 20" stämmer ändå. Bland övriga finns också "Damcykel Liv Avail AR 2, 700x32c" (landsvägscykel från Liv), så "från Giant" gäller huvudprodukterna, inte allt i kollektionen. Oförändrat sedan runda 2 (A20).

## 8. stankskarmar-cykel: godkänd

| Påstående | Kontroll mot underlaget | Utfall |
|---|---|---|
| "minst 40 produkter" (text och meta) | 47, tiotalsgolv 40 | Godkänd, marginal 7 |
| "bland annat stänkskärmset, framskärmar och bakskärmar" / meta "till exempel …" | Stänkskärmset 14 (+ Stänkskärmsset 2), Framskärm 12, Bakskärm 10 (+ Stänkskärmar 7, Stänkskydd 2) | Godkänd |
| "från bland annat Hebie, SKS, Giant och Ass Savers" (text och meta) | Hebie 17, SKS 14, Giant 8, Ass Savers 3, Academy 1, XLC 1 (Velomarket 3 är leverantör) | Godkänd |
| "Hebie och SKS har flest produkter" | Vendor: Hebie 17, SKS 14, därefter Giant 8. I titlarna: Hebie 17, SKS 17 | Godkänd med båda räknesätten |
| "till exempel 28 tum eller 26–29 tum" | "28 tum" i 4 titlar (varav 2 som exakt storlek), "26–29 tum" i 6 | Godkänd |
| Exempel: Hebie Taipan Trekking, 28 tum, Svart; SKS Shockblade för 28–29 tum; Giant Speedshield Clip-On | Alla 3 ordagrant | Godkänd |
| SEO "Stänkskärm cykel – Hebie, SKS, Giant" (36) | De tre märken som har flest | Godkänd |

Inga anmärkningar utöver att metan (149) ligger nära övre gränsen 155.

---

## Sammanställning

### Faktafel
Inga. Alla antal stämmer med golvreglerna, alla "flest"-påståenden stämmer, alla nämnda märken, typer, egenskaper och tal finns i titlarna, varje uppräkning som inte är fullständig har "bland annat" eller "till exempel", och alla exempeltitlar finns ordagrant i `alla_titlar`. Felen från runda 1 (F1–F5) och runda 2 (F1) är rättade.

### Anmärkningar (valfria)
A6 (grepptraning, versalisering i SEO-titeln), A9 (racercykel, ordföljd), A4 (dubblerad exempeltitel WB20 om hemmagym skrivs), A5h (tung hybridmeta), A8b (boxningens SEO-titel ser fullständig ut).

### Risker inför skrivning
- boxning har marginal 0 och herrcyklar marginal 0 räknat på unika titlar.
- traningsbank bygger på 21 bänkar som taggades i dag; marginalen är 3.
- Kör om underlaget och denna kontroll direkt före skrivning (standarden 8.1, lärdomen 2026-11-17).

Antal faktafel: 0
