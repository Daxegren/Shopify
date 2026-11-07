# Granskningsutlåtande k_41a, k_41b och k_41c (2026-11-07)

Granskaren har bara läst i Shopify och har inte ändrat något där eller committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient; `verifiera_butik` gav BEST OF SPORTS). Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.10), BESLUTSLOGG till och med 2026-11-07 (löpband och elcyklar släppta för faktatext), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_39fg.md` och formatet i `k_utlatande_39fg.json`.

Alla 27 utkast är ACTIVE. Ingen av dem är spärrad (undantaget för gruppen elcykel-lopband-2026-11-07 gäller). `skrivfil_kontroll.py` gav 0 fel och 0 varningar, både på utkasten och på de 12 godkända eller rättade texterna. Standardblocket är exakt rätt på alla 27. Leveranstidsmeningen finns på exakt de 22 produkter som har taggen På beställning. Titel, SEO och meta krockar inte med andra `*utkast*.json`/`*skriv*.json`. Titel ≤70 tecken och ≤2 kommatecken, SEO ≤43, meta 70–155 med verb, högst två "enligt tillverkaren" per text.

Maskinläsbar version: `vag2_skriv/k_utlatande_41.json`. Varje rättning är ETT sammanhängande före/efter-par per fält, och varje före-text förekommer exakt en gång i utkastet (kontrollerat i python).

## Resultat: 10 GODKÄND, 2 RÄTTA, 15 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 39159 | 10472250179850 | k_41a_utkast.json | GODKÄND | – |
| 39160 | 10472255979786 | k_41a_utkast.json | RÄTTA | html |
| 39162 | 10472293499146 | k_41a_utkast.json | UNDERKÄND | – |
| 39166 | 10472304935178 | k_41a_utkast.json | RÄTTA | meta, html |
| 39167 | 10472329969930 | k_41a_utkast.json | GODKÄND | – |
| 41001 | 10476275761418 | k_41b_utkast.json | UNDERKÄND | – |
| 41002 | 10486670786826 | k_41b_utkast.json | GODKÄND | – |
| 41003 | 10488326258954 | k_41b_utkast.json | UNDERKÄND | – |
| 41004 | 10502528073994 | k_41b_utkast.json | UNDERKÄND | – |
| 41005 | 10502528139530 | k_41b_utkast.json | UNDERKÄND | – |
| 41006 | 10503212138762 | k_41b_utkast.json | UNDERKÄND | – |
| 41007 | 10503235698954 | k_41b_utkast.json | GODKÄND | – |
| 41008 | 10507441537290 | k_41b_utkast.json | UNDERKÄND | – |
| 41009 | 10523486945546 | k_41b_utkast.json | UNDERKÄND | – |
| 41010 | 10561355972874 | k_41b_utkast.json | UNDERKÄND | – |
| 41011 | 10523487109386 | k_41b_utkast.json | UNDERKÄND | – |
| 41012 | 10530216378634 | k_41b_utkast.json | UNDERKÄND | – |
| 41013 | 10561355874570 | k_41b_utkast.json | GODKÄND | – |
| 41014 | 10561356103946 | k_41b_utkast.json | UNDERKÄND | – |
| 41015 | 10588451864842 | k_41b_utkast.json | GODKÄND | – |
| 41016 | 10588453142794 | k_41b_utkast.json | UNDERKÄND | – |
| 41017 | 10589711892746 | k_41b_utkast.json | GODKÄND | – |
| 41001 | 10635809325322 | k_41c_utkast.json | GODKÄND | – |
| 41002 | 10635810111754 | k_41c_utkast.json | GODKÄND | – |
| 41003 | 10673181229322 | k_41c_utkast.json | UNDERKÄND | – |
| 41004 | 10673181360394 | k_41c_utkast.json | UNDERKÄND | – |
| 41005 | 10494769529098 | k_41c_utkast.json | GODKÄND | – |

## Viktigt före bygget av skrivfilen

1. **Dubbla nr:** k_41b och k_41c använder båda nr 41001–41005. Bland de godkända har både Fiido Titan (k_41b, 10486670786826) och Giant Fathom L/XL (k_41c, 10635810111754) nr **41002**. `bygg_m_skriv.py` använder nr som nyckel, så en av dem faller bort tyst (lärdomen 2026-11-05). Numrera om k_41c (till exempel 41201–41205) i utkast och utlåtande före bygget, eller bygg per fil. Avvisade-filerna krockar också (41101–41104).
2. **Härledda ramstorlekar (uppdragets huvudfråga):** 13 utkast (11 i k_41b och 2 Leader Fox i k_41c) har en storlek i titeln som bara är härledd ur artikelnumret. Bara en gick att belägga på exakt artikelnummer hos tillverkaren: Tenways CGO600 Pro Mintgrön (081301580036 = XL på tenways.com). Giant och Liv publicerar inga artikelnummer, EAN-sökning gav inga träffar, och velomarket.ee och bike24.com svarar 403 från molnmiljön. Leader Fox-numret gav inga träffar. För alla 12 utan belägg skulle titeln utan storlek bli densamma som en redan skriven aktiv produkt med samma modell och färg. De är därför UNDERKÄNDA enligt R12a, och syskonet anges per produkt. Ingen storlek har rättats bort så att produkten släpps.
3. **Underlag för beslut:** butikens egna variantnamn i hela Giant/Liv-serien följer mönstret utan undantag (380 varianter: 3=XS, 4=S, 5=M, 6=M/L, 7=L, 8=XL). Om David utvidgar undantaget från 2026-11-07 till Giant/Liv (och Leader Fox, där …/215 motsvarar 21,5 tum) kan de 11 Giant/Liv-utkasten skrivas som de står. Det gäller inte Revolt Advanced 2 (2025): där användes slutsiffran 6, och titeln skiljer sig från syskonet bara genom '(2025)'.
4. **Avvisade som kan lyftas:** k_41c 41117 (10635810177290, Ouroboros CR/DL Gloss Concrete, B36ORCDGYSRHK48) kan beläggas hos tillverkaren som storlek 48 (cm) på https://en-eu.konaworld.com/products/ouroboros-cr-dl-36. Med storleken '48 cm' i titeln skiljer den sig från det skrivna syskonet (52/54/58). Den kan få ett nytt utkast. Övriga avvisningar är riktiga.

## Skäl och rättningar per produkt

### 39159 (10472250179850, k_41a_utkast.json): GODKÄND

Live ACTIVE, en variant TEB6P1540003, lager 1. Alla uppgifter i egen svensk källa (remdrift, Mivice M070 250 W 40 Nm, S200-momentgivare, OLED, LG 36 V 10 Ah, 28 tum, Tektro hydrauliska, stänkskärmar/stöd/ljus). Räckvidd 100 km en gång enligt tillverkaren (entydig: ett värde). Vikt utelämnad (16 mot 17 kg), storlekstabell utelämnad (en variant): rätt. Lastgräns saknas i källan: 'Ej känd' (v1.10). Till David: färgen 'Ljusgrå' står bara i live-titeln; den skrivna 10471090749706 heter 'Pebble Grey' (andra SKU-serien 0813…). Om Ljusgrå är samma kulör är det inte exakt samma artikel (annat artikelnummer) och titlarna skiljer sig, så ingen dubblett enligt beslutet 2026-11-05.

### 39160 (10472255979786, k_41a_utkast.json): RÄTTA

Live ACTIVE, varianter L/silver och XL/silver, samma pris 45249 kr, lager 6 (v1.8: storlekarna står i egna varianter). Fakta i egen svensk källa: Bafang M410 250 W 80 Nm mittmotor med momentgivare, 36 V 14 Ah, upp till 100 km, aluminium, L (50 cm)/XL (53 cm), Shimano Deore 10 växlar, hydrauliska skivbromsar, 'Lastkapacitet: 150 kg' (svensk rad med etikett och enhet, en gång enligt tillverkaren, R4), skärmar/pakethållare/stöd/ljus. 'Hjulvikt 29 kg' och trasig XL-rad utelämnade: rätt. Två 'enligt tillverkaren' (max). Rättning: färgraden ska stämma med titeln och live-titeln ('Gradient Silver', båda varianterna 'silver').

| fält | före | efter |
|---|---|---|
| html | <li>Färg: Silver</li> | <li>Färg: Gradient Silver</li> |

### 39162 (10472293499146, k_41a_utkast.json): UNDERKÄND

Produkttypen är oklar och källan motsäger titeln (R2/R3). Live-titeln säger 'Vevlager', men egen källa har bara tre rader ('särskilt lämplig för elcyklar', 'Lämplig för 24"-29" hjul', 'aluminium'); ett vevlager anges inte efter hjulstorlek. M-Waves artikelnummer 4307xx är cykelstöd (t.ex. 430734 'Adjustable Bicycle Centre Kickstand 24-29', https://www.skroutz.eu/s/32304145/M-Wave-Adjustable-Bicycle-Centre-Kickstand-24-29-430734.html), så produkten är troligen ett cykelstöd ('Strong F'). Typordet får inte bytas utan stöd i källan (R7), och ett vevlager med 'Maximal lastgräns: Ej känd' skulle beskriva fel produkt. Till David: vill du att produkten skrivs som Cykelstöd (godkänt typord) med 'Maximal lastgräns: Ej känd'?

### 39166 (10472304935178, k_41a_utkast.json): RÄTTA

Live ACTIVE, lager 0, tagg På beställning; leveranstidsmeningen finns. Tunn källa men tre entydiga fakta (vinterdäck, utformat för elcyklar, dubbar) plus storleken i live-titeln; trasiga rader '244 pounds 74.01' och alla säkerhets-/greppord utelämnade: rätt. Typordet Cykeldäck ur live-titeln (R7). Rättning R5: 'från Finland' är ett ursprungspåstående (källan: 'finskt vinterdäck') och ska bort; inledningen omformulerad så att produkten namnges. Rättning meta: grammatiken ('har dubbar, är utformat … i storleken') rättad.

| fält | före | efter |
|---|---|---|
| meta | Cykeldäcket Suomi Tyres Routa W244 E-Bike har dubbar, är utformat för elcyklar i storleken 28 x 1,38. | Cykeldäcket Suomi Tyres Routa W244 E-Bike har dubbar och är utformat för elcyklar. Storleken är 28 x 1,38. |
| html | <p>Vinterdäcket från Finland är utformat för elcyklar och har dubbar. Suomi Tyres Routa E-Bike finns i storleken 28 x 1,38.</p> | <p>Suomi Tyres Routa W244 E-Bike har dubbar och är utformat som vinterdäck för elcyklar. Storleken är 28 x 1,38.</p> |

### 39167 (10472329969930, k_41a_utkast.json): GODKÄND

Live ACTIVE, en variant 9117, lager 1. Alla uppgifter i egen svensk källa (Bafang H300 250 W bak, 378 Wh, 40–70 km, aluminium, rammått 39 cm, Shimano Altus 7 växlar, mekaniska skivbromsar, Innova IA-2126 20x2.20, låg ram, stöd/stänkskärmar/pakethållare/ljus). 'Lastkapacitet: 130 kg' är svensk rad med etikett och enhet, en gång enligt tillverkaren (R4); räckvidd en gång; totalt två. 'Hjulvikt 22,3 kg' utelämnad: rätt. Färgen Honey ur live-titeln.

### 41001 (10476275761418, k_41b_utkast.json): UNDERKÄND

Live ACTIVE, Default Title 5090000105, lager 1. Storleken är härledd ur artikelnumrets slutsiffra och står inte i produktens egen källa (Default Title). Den gick inte att belägga på exakt artikelnummer hos tillverkaren eller återförsäljare: Giant/Liv publicerar inte artikelnummer, EAN-sökning gav inga träffar, och velomarket.ee och bike24.com svarar 403 från molnmiljön (bike24 listar 5090000104/105/107/108 utan storlek). Butikens egna variantnamn i Giant/Liv-serien stämmer alltid med mönstret (380 varianter: 3=XS, 4=S, 5=M, 6=M/L, 7=L, 8=XL, inga avvikelser), men det är leverantörens data för andra artiklar, inte verifiering av exakt artikel, och Davids undantag 2026-11-07 gäller bara tre namngivna cyklar. Utan storlek blir titel, SEO och text desamma som för den redan skrivna aktiva produkten 10472326463754 ('Elcykel Giant Talon E+, 29 tum, Asphalt Green', 5090000107, texter-klara) och i praktiken 10488326193418 (5090000104). R12a: dubblett i titeln; syskon 10472326463754.

### 41002 (10486670786826, k_41b_utkast.json): GODKÄND

Live ACTIVE, en variant TITAN-2025-EU, lager 3, tagg På beställning; leveranstidsmeningen finns. Alla uppgifter i egen svensk källa (250 W 55 Nm, momentgivare, 696 Wh, aluminium, 42 cm, DSL-D310 9 växlar, hydrauliska, CST 26x4.0, ca 40 kg, stöd/stänkskärmar/pakethållare/ljus). Lastgräns: 'Lastkapacitet: 200 kg' står på svenska i egen källa och skrivs en gång enligt tillverkaren (R4/v1.10, som uppdraget anger). Räckvidd 115 km (ett batteri) en gång; 347 km med extra batterier utelämnad. Vattentät/robust/kraftfull utelämnade. Ingen syskonprodukt med text.

### 41003 (10488326258954, k_41b_utkast.json): UNDERKÄND

Live ACTIVE, Default Title 1032015183, lager 1. Storleken är härledd ur artikelnumrets slutsiffra och står inte i produktens egen källa (Default Title). Den gick inte att belägga på exakt artikelnummer hos tillverkaren eller återförsäljare: Giant/Liv publicerar inte artikelnummer, EAN-sökning gav inga träffar, och velomarket.ee och bike24.com svarar 403 från molnmiljön (bike24 listar 5090000104/105/107/108 utan storlek). Butikens egna variantnamn i Giant/Liv-serien stämmer alltid med mönstret (380 varianter: 3=XS, 4=S, 5=M, 6=M/L, 7=L, 8=XL, inga avvikelser), men det är leverantörens data för andra artiklar, inte verifiering av exakt artikel, och Davids undantag 2026-11-07 gäller bara tre namngivna cyklar. Utan storlek blir titel, SEO och text desamma som för den redan skrivna aktiva produkten 10471330349322 ('Gravelcykel Liv Devote 0, Clear Sky', varianter S och L, texter-klara). R12a: dubblett i titeln; syskon 10471330349322.

### 41004 (10502528073994, k_41b_utkast.json): UNDERKÄND

Live ACTIVE, Default Title 5700001185, lager 0. Storleken är härledd ur artikelnumrets slutsiffra och står inte i produktens egen källa (Default Title). Den gick inte att belägga på exakt artikelnummer hos tillverkaren eller återförsäljare: Giant/Liv publicerar inte artikelnummer, EAN-sökning gav inga träffar, och velomarket.ee och bike24.com svarar 403 från molnmiljön (bike24 listar 5090000104/105/107/108 utan storlek). Butikens egna variantnamn i Giant/Liv-serien stämmer alltid med mönstret (380 varianter: 3=XS, 4=S, 5=M, 6=M/L, 7=L, 8=XL, inga avvikelser), men det är leverantörens data för andra artiklar, inte verifiering av exakt artikel, och Davids undantag 2026-11-07 gäller bara tre namngivna cyklar. Utan storlek blir titel, SEO och text desamma som för den redan skrivna aktiva produkten 10472331280650 ('Elcykel Liv Lurra E+ EX, Grå Gryning', 5700001184, texter-klara). R12a: dubblett i titeln; syskon 10472331280650.

### 41005 (10502528139530, k_41b_utkast.json): UNDERKÄND

Live ACTIVE, Default Title 5700000185, lager 0. Storleken är härledd ur artikelnumrets slutsiffra och står inte i produktens egen källa (Default Title). Den gick inte att belägga på exakt artikelnummer hos tillverkaren eller återförsäljare: Giant/Liv publicerar inte artikelnummer, EAN-sökning gav inga träffar, och velomarket.ee och bike24.com svarar 403 från molnmiljön (bike24 listar 5090000104/105/107/108 utan storlek). Butikens egna variantnamn i Giant/Liv-serien stämmer alltid med mönstret (380 varianter: 3=XS, 4=S, 5=M, 6=M/L, 7=L, 8=XL, inga avvikelser), men det är leverantörens data för andra artiklar, inte verifiering av exakt artikel, och Davids undantag 2026-11-07 gäller bara tre namngivna cyklar. Utan storlek blir titel, SEO och text desamma som för den redan skrivna aktiva produkten 10469246206218 ('Elcykel Liv Lurra E+, Lunar Eclipse', 5700000184, texter-klara). R12a: dubblett i titeln; syskon 10469246206218.

### 41006 (10503212138762, k_41b_utkast.json): UNDERKÄND

Live ACTIVE, Default Title 1079015246, lager 0. Storleken M/L är härledd ur slutsiffran 6, som inte ens ingår i utkastarens egen tabell (3/4/5/7/8). Storleken är härledd ur artikelnumrets slutsiffra och står inte i produktens egen källa (Default Title). Den gick inte att belägga på exakt artikelnummer hos tillverkaren eller återförsäljare: Giant/Liv publicerar inte artikelnummer, EAN-sökning gav inga träffar, och velomarket.ee och bike24.com svarar 403 från molnmiljön (bike24 listar 5090000104/105/107/108 utan storlek). Butikens egna variantnamn i Giant/Liv-serien stämmer alltid med mönstret (380 varianter: 3=XS, 4=S, 5=M, 6=M/L, 7=L, 8=XL, inga avvikelser), men det är leverantörens data för andra artiklar, inte verifiering av exakt artikel, och Davids undantag 2026-11-07 gäller bara tre namngivna cyklar. Utan storlek blir titel, SEO och text desamma som för den redan skrivna aktiva produkten 10503202472202 ('Gravelcykel Giant Revolt Advanced 2, Solar Flare', 1079015248, texter-klara); '(2025)' skiljer bara skenbart, båda är samma 1079015-serie. R12a: dubblett i titeln; syskon 10503202472202.

### 41007 (10503235698954, k_41b_utkast.json): GODKÄND

Live ACTIVE, Default Title 081301580036, lager 0, tagg På beställning; leveranstidsmeningen finns. Storleken XL är verifierad hos tillverkaren på exakt artikelnummer: https://www.tenways.com/products/cgo600-pro (variant 'CGO600 Pro New Edition (Belt Drive) / XL / Mint Green', SKU 081301580036, EAN 8721055331797). Den skrivna 10472294220042 (081301540035) är L enligt samma sida, så titlarna skiljer korrekt. Övriga fakta i egen svensk källa (navmotor 250 W 40 Nm, momentgivare, 360 Wh integrerat, 100 km en gång enligt tillverkaren, Gates Carbon-rem, aluminium, XL 58 cm, 1 växel, Tektro hydrauliska, 17 kg utan tillbehör, Kenda 700x48C, stöd/stänkskärmar/ljus).

### 41008 (10507441537290, k_41b_utkast.json): UNDERKÄND

Live ACTIVE, Default Title 5550001107, lager 0. Storleken är härledd ur artikelnumrets slutsiffra och står inte i produktens egen källa (Default Title). Den gick inte att belägga på exakt artikelnummer hos tillverkaren eller återförsäljare: Giant/Liv publicerar inte artikelnummer, EAN-sökning gav inga träffar, och velomarket.ee och bike24.com svarar 403 från molnmiljön (bike24 listar 5090000104/105/107/108 utan storlek). Butikens egna variantnamn i Giant/Liv-serien stämmer alltid med mönstret (380 varianter: 3=XS, 4=S, 5=M, 6=M/L, 7=L, 8=XL, inga avvikelser), men det är leverantörens data för andra artiklar, inte verifiering av exakt artikel, och Davids undantag 2026-11-07 gäller bara tre namngivna cyklar. Utan storlek blir titel, SEO och text desamma som för den redan skrivna aktiva produkten 10471305838858 ('Elcykel Liv Tempt E+ EX, Sandshell', varianter XS/S/M, texter-klara). Utan storlek går inte heller däckstorleken att avgöra (27,5 tum för XS/S, 29 tum för M/L enligt källan). Belysningsmotsägelsen (framlampa mot fram- och bakljus) är korrekt utelämnad. R12a: dubblett i titeln; syskon 10471305838858.

### 41009 (10523486945546, k_41b_utkast.json): UNDERKÄND

Live ACTIVE, Default Title 5310005103, lager 0. Storleken är härledd ur artikelnumrets slutsiffra och står inte i produktens egen källa (Default Title). Den gick inte att belägga på exakt artikelnummer hos tillverkaren eller återförsäljare: Giant/Liv publicerar inte artikelnummer, EAN-sökning gav inga träffar, och velomarket.ee och bike24.com svarar 403 från molnmiljön (bike24 listar 5090000104/105/107/108 utan storlek). Butikens egna variantnamn i Giant/Liv-serien stämmer alltid med mönstret (380 varianter: 3=XS, 4=S, 5=M, 6=M/L, 7=L, 8=XL, inga avvikelser), men det är leverantörens data för andra artiklar, inte verifiering av exakt artikel, och Davids undantag 2026-11-07 gäller bara tre namngivna cyklar. Utan storlek blir titel, SEO och text desamma som för den redan skrivna aktiva produkten 10503245332746 ('Elcykel Liv Embolden E+ 1 (2027), Pale Moss/Black', M och L, texter-klara), och samma som utkastet 10561355972874. Däckstorleken (27,5 tum bara för XS) hänger också på den overifierade storleken. Räckvidden är korrekt utelämnad (245 mot cirka 120 km). R12a: dubblett i titeln; syskon 10503245332746.

### 41010 (10561355972874, k_41b_utkast.json): UNDERKÄND

Live ACTIVE, Default Title 5310005104, lager 0. Storleken är härledd ur artikelnumrets slutsiffra och står inte i produktens egen källa (Default Title). Den gick inte att belägga på exakt artikelnummer hos tillverkaren eller återförsäljare: Giant/Liv publicerar inte artikelnummer, EAN-sökning gav inga träffar, och velomarket.ee och bike24.com svarar 403 från molnmiljön (bike24 listar 5090000104/105/107/108 utan storlek). Butikens egna variantnamn i Giant/Liv-serien stämmer alltid med mönstret (380 varianter: 3=XS, 4=S, 5=M, 6=M/L, 7=L, 8=XL, inga avvikelser), men det är leverantörens data för andra artiklar, inte verifiering av exakt artikel, och Davids undantag 2026-11-07 gäller bara tre namngivna cyklar. Utan storlek blir titel, SEO och text desamma som för den redan skrivna aktiva produkten 10503245332746 ('Elcykel Liv Embolden E+ 1 (2027), Pale Moss/Black', M och L, texter-klara), och samma som utkastet 10523486945546. R12a: dubblett i titeln; syskon 10503245332746.

### 41011 (10523487109386, k_41b_utkast.json): UNDERKÄND

Live ACTIVE, Default Title 5310006103, lager 0. Storleken är härledd ur artikelnumrets slutsiffra och står inte i produktens egen källa (Default Title). Den gick inte att belägga på exakt artikelnummer hos tillverkaren eller återförsäljare: Giant/Liv publicerar inte artikelnummer, EAN-sökning gav inga träffar, och velomarket.ee och bike24.com svarar 403 från molnmiljön (bike24 listar 5090000104/105/107/108 utan storlek). Butikens egna variantnamn i Giant/Liv-serien stämmer alltid med mönstret (380 varianter: 3=XS, 4=S, 5=M, 6=M/L, 7=L, 8=XL, inga avvikelser), men det är leverantörens data för andra artiklar, inte verifiering av exakt artikel, och Davids undantag 2026-11-07 gäller bara tre namngivna cyklar. Utan storlek blir titel, SEO och text desamma som för den redan skrivna aktiva produkten 10507440226570 ('Elcykel Liv Embolden E+ 2 (2027), Slate Grey/Black', S och M, texter-klara). R12a: dubblett i titeln; syskon 10507440226570.

### 41012 (10530216378634, k_41b_utkast.json): UNDERKÄND

Live ACTIVE, Default Title 1080044104, lager 0. Storleken är härledd ur artikelnumrets slutsiffra och står inte i produktens egen källa (Default Title). Den gick inte att belägga på exakt artikelnummer hos tillverkaren eller återförsäljare: Giant/Liv publicerar inte artikelnummer, EAN-sökning gav inga träffar, och velomarket.ee och bike24.com svarar 403 från molnmiljön (bike24 listar 5090000104/105/107/108 utan storlek). Butikens egna variantnamn i Giant/Liv-serien stämmer alltid med mönstret (380 varianter: 3=XS, 4=S, 5=M, 6=M/L, 7=L, 8=XL, inga avvikelser), men det är leverantörens data för andra artiklar, inte verifiering av exakt artikel, och Davids undantag 2026-11-07 gäller bara tre namngivna cyklar. Utan storlek blir titel, SEO och text desamma som för den redan skrivna aktiva produkten 10480053321994 ('Gravelcykel Giant Revolt Advanced 0 SE (2026), Radio Spectrum', 1080044108, texter-klara). R12a: dubblett i titeln; syskon 10480053321994.

### 41013 (10561355874570, k_41b_utkast.json): GODKÄND

Live ACTIVE, variant 'XL / beige' (5300002108), lager 0, tagg På beställning; leveranstidsmeningen finns. Storleken XL står i produktens egen variant, så den behöver inget undantag. Skiljer sig från den skrivna 10561353908490 ('…Mandel/Svart', 5300002107) genom storleken. Alla tekniska rader i egen svensk källa; räckvidd 245 km bara i tabellen, en gång enligt tillverkaren. Säljfraser utelämnade.

### 41014 (10561356103946, k_41b_utkast.json): UNDERKÄND

Live ACTIVE, Default Title 5300003108, lager 0. Storleken är härledd ur artikelnumrets slutsiffra och står inte i produktens egen källa (Default Title). Den gick inte att belägga på exakt artikelnummer hos tillverkaren eller återförsäljare: Giant/Liv publicerar inte artikelnummer, EAN-sökning gav inga träffar, och velomarket.ee och bike24.com svarar 403 från molnmiljön (bike24 listar 5090000104/105/107/108 utan storlek). Butikens egna variantnamn i Giant/Liv-serien stämmer alltid med mönstret (380 varianter: 3=XS, 4=S, 5=M, 6=M/L, 7=L, 8=XL, inga avvikelser), men det är leverantörens data för andra artiklar, inte verifiering av exakt artikel, och Davids undantag 2026-11-07 gäller bara tre namngivna cyklar. Utan storlek blir titel, SEO och text desamma som för den redan skrivna aktiva produkten 10488318296330 ('Elcykel Giant Stance E+ 2 (2027), 29 tum, Desert Sage/Black', 5300003105, texter-klara). R12a: dubblett i titeln; syskon 10488318296330.

### 41015 (10588451864842, k_41b_utkast.json): GODKÄND

Live ACTIVE, varianter 'S / gray' och 'M / gray', samma pris 76309 kr, lager 0, tagg På beställning; leveranstidsmeningen finns. Storlekarna står i egna varianter (v1.8). Tekniska rader i egen svensk källa; räckvidd en gång enligt tillverkaren. Skiljer sig från den skrivna 10523491401994 (L) genom storleken. Till David (ingen rättning): syskonet är skrivet med färgen 'Kolsvart/Svart', här 'Charcoal/Black' ur live-titeln; samma kulör kan se ut som två olika.

### 41016 (10588453142794, k_41b_utkast.json): UNDERKÄND

Dubblett (R12a) och motsägelse (R2/R3). Variant 'XL / white' har SKU B36ORCDGYSRHK58, som också är XL-varianten i den redan skrivna aktiva 10588452847882 ('Gravelcykel Kona Ouroboros CR/DL, Gloss Concrete', texter-klara), men med annat pris (71319 mot 92359 kr): samma artikel i två annonser. Variant 'XS / white' har SKU …50, men Kona anger storlekar i cm (https://en-eu.konaworld.com/products/ouroboros-cr-dl-36: 48, 50, 52, 54, 56, 58), och butikens andra Ouroboros-annons (10468716478730) kallar 50 för S och 48 för XS; källans storlekstabell säger 41 cm för både XS och S. Syskon: 10588452847882.

### 41017 (10589711892746, k_41b_utkast.json): GODKÄND

Live ACTIVE, varianter S/M/L blue, samma pris, lager 0, tagg På beställning; leveranstidsmeningen finns. Storlekarna står i egna varianter och stämmer med tillverkaren på exakt artikelnummer: https://en-eu.konaworld.com/products/el-kahuna-37 (B37EKHBLBCPPMEUAJ01 = SM, …03 = MD, …05 = LG, …06 = XL). XL (…06) är den skrivna 10588453241098, så titlarna skiljer korrekt. Tekniska rader i egen svensk källa; räckvidd en gång enligt tillverkaren; säljfraser utelämnade.

### 41001 (10635809325322, k_41c_utkast.json): GODKÄND

Live ACTIVE, variant 'S / blue' (5332004184), lager 0, tagg På beställning; leveranstidsmeningen finns. Storleken S står i egen variant. Alla tekniska rader och 'hardtail' i egen svensk källa. Räckvidd (214 km) och laddtid utelämnade avsiktligt, godtagbart. Skiljer sig från den skrivna 10635807064330 (Default Title, utan storlek) och från 10635810111754 (L och XL, annat pris) genom storleken. Lastgräns 'Ej känd' (v1.10).

### 41002 (10635810111754, k_41c_utkast.json): GODKÄND

Live ACTIVE, varianter 'L / blue' och 'XL / blue', samma pris 55069 kr, lager 0, tagg På beställning; leveranstidsmeningen finns. Storlekarna står i egna varianter (v1.8). Tekniska rader i egen svensk källa ('luftfjädrad' för STL 36 Air är en rimlig översättning). Skiljer sig från 10635809325322 och den skrivna 10635807064330 genom storleken.

### 41003 (10673181229322, k_41c_utkast.json): UNDERKÄND

Live ACTIVE, Default Title K23/8/2/3/29/3/215, lager 0. Storleken XL är härledd ur artikelnumret (…/215 tolkat som 21,5 tum; källan listar L 19.5" och XL 21.5"), men den står inte i produktens egen variant och gick inte att belägga på exakt artikelnummer hos tillverkare eller återförsäljare (sökning på K23/8/2/3/29 gav inga träffar). Utan storlek blir titeln densamma som den skrivna aktiva 10673180475658 ('Elcykel Leader Fox Ayra, 29 tum, Orange', variant L/…/195, texter-klara). R12a: dubblett i titeln; syskon 10673180475658. (att_bekrafta innehåller dessutom en felkopierad rad om Giants 2027-sidor.)

### 41004 (10673181360394, k_41c_utkast.json): UNDERKÄND

Live ACTIVE, Default Title K23/8/2/3/29/2/215, lager 0. Samma skäl som 10673181229322: storleken XL är bara härledd ur artikelnumret och gick inte att belägga. Utan storlek blir titeln densamma som den skrivna aktiva 10673180508426 ('Elcykel Leader Fox Ayra, 29 tum, Blå', variant L/…/195, texter-klara). R12a: dubblett i titeln; syskon 10673180508426.

### 41005 (10494769529098, k_41c_utkast.json): GODKÄND

Live ACTIVE, en variant G6540 (EAN 8431284980429), lager 1, ingen tagg På beställning och ingen leveranstidsmening: rätt. Egen svensk källa säger 'Motor: 3,0 hk', och det skriver utkastet. Återförsäljare bekräftar 3.0 HP för G6540 (https://www.harveynorman.com.au/bh-fitness-g6540-nydo-bluetooth-treadmill.html, https://www.binglee.com.au/products/bhfitness-nydo-treadmill-g6540). Syskonets '2,0 hk (max 3,0 hk)' gäller G6541 (annan EAN 8445960097615, annan källtext med Bluetooth FTMS) och påverkar inte denna text. Lastgräns 'Maximal användarvikt: 130 kg' är svensk rad i egen källa, en gång enligt tillverkaren (R4/v1.10). 'Lutning: 12' utan enhet utelämnad: rätt. Säkerhets- och idealordet utelämnade. Inte samma artikel som 10665232335114 (annat artikelnummer och EAN), och titel/SEO skiljer sig. Till David: kunden ser två nästan lika Nydo-löpband till samma pris; om G6541 är en nyare version kan titlarna behöva skiljas tydligare.
