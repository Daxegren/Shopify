# Granskningsutlåtande k_45a och k_45b, omprövade produkter under v1.8/v1.9 (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (slutsiffra = ramstorlek för Giant/Liv; aktiva produkter får text enligt strukturen), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md` och formatet i `k_utlatande_43.json`.

Alla sju produkter är ACTIVE med totalInventory > 0. `skrivfil_kontroll.py` gav 0 fel och 0 varningar både på utkasten och på de rättade texterna. Standardblocket är exakt som i `b_skriv_24.json`; leveranstidsmeningen finns på exakt de tre produkter som har taggen På beställning (45002, 45104, 45105). Titel ≤70 tecken och ≤2 kommatecken, SEO ≤43, meta 116–136 tecken med verb, 'Passar för' på alla, högst två 'enligt tillverkaren'. Titlar, SEO och meta är unika mot alla skrivfiler och utkast i `rapporter/` och mot butikens titlar (sökning på Union Lite, Versatyl, Pinner, Attend, Avail, Astra, Peltonen). Varje rättning är ETT sammanhängande före/efter-par per fält, och före-texten förekommer exakt en gång i utkastet (kontrollerat i python). Avvisningarna i `k_45a_avvisade.json` och `k_45b_avvisade.json` har lästs; ingen är uppenbart fel.

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_45.json`.

## Resultat: 3 GODKÄND, 4 RÄTTA, 0 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 45001 | 10471009026314 | k_45a_utkast.json | RÄTTA | meta, html |
| 45002 | 10470929334538 | k_45a_utkast.json | GODKÄND | – |
| 45101 | 10472332493066 | k_45b_utkast.json | RÄTTA | html |
| 45102 | 10472332820746 | k_45b_utkast.json | RÄTTA | html |
| 45103 | 10515745636618 | k_45b_utkast.json | RÄTTA | titel, seo_title, html |
| 45104 | 10488246632714 | k_45b_utkast.json | GODKÄND | – |
| 45105 | 10488246796554 | k_45b_utkast.json | GODKÄND | – |

## Mönster

- Varianter (v1.9): alla flervariantsprodukter är samma artikel i olika storlek eller färg: Astra Wax tre längder, Pinner Comp svart/blå (bekräftat på ebike24.com och bikesandbeyond.ca), Attend RS 1 GTS M/L (slutsiffra enligt Davids beslut), Avail AR 2 överbliven Default Title med samma SKU/EAN. Ingen titel låser storlek, färg eller pris som skiljer mellan varianter.
- Användarhöjd/åkarlängd på sparkcyklar: leverantörens egna värden motsägs för exakt EAN av återförsäljare (Union Lite S 105–125 mot 110–145 cm, Lite M 110–130 mot 135–165 cm, Versatyl S2S 160–170 mot 140–170 och 135–165 cm). Uppgiften stryks (R2), vilket också är hur de redan skrivna Union Lite-syskonen ser ut. Lastkapaciteten 100 kg stämmer överallt och står kvar en gång.
- Typord: Klassiska Skidor (Astra Wax) stöds av egen källa och syskonen. Versatyl S2S byts tillbaka till live-ordet Tricksparkcykel (R7; källan säger trick, inte stunt).
- Lastgräns v1.10: bara pedalerna är en bärande del; ingen lastgräns hittades, 'Ej känd' står i spec och text. Cyklarna får ingen lastuppgift (saknas i källan).

## Frågor till David

1. Giant Attend RS 1 GTS: M (Default Title) kostar 12 469 kr och L 5 229 kr. Ett av priserna är troligen fel; Default Title borde också heta M / black. Texten påverkas inte.
2. Liv Avail AR 2 (S): Default Title 26 209 kr och S / white 22 789 kr har samma SKU/EAN; den överblivna varianten bör tas bort. Pinner Comp: svart 629 kr och blå 489 kr för samma pedal.
3. Leverantörens användarhöjder för Union Lite och Versatyl stämmer inte med återförsäljarnas för samma EAN. Utlåtandet stryker dem. Vill du hellre ha tillverkarens egen storleksguide (unionscooters.com saknar cm-uppgift) eller ingen uppgift alls som nu?
4. Peltonen Astra Wax: live-titeln säger pjäxor och taggen Klassiska pjäxor finns kvar (taggar rörs inte). Titeln blir Klassiska Skidor. Taggen kan ge fel filtrering i butiken.

## Skäl och rättningar per produkt

### 45001 (10471009026314, k_45a_utkast.json): RÄTTA

Live ACTIVE, lager 4 (180: 1, 190: 2, 200: 1), tre längder av samma skida (SKU 21AN925100180/190/200, pris 3 499/3 499/3 489 kr): samma artikel i olika storlek, v1.9 uppfylld; titel, SEO och text låser ingen längd. Egen källtext säger 'Klassiska skidor Peltonen ASTRA' med monterade Rottefella NIS Touring Basic-bindningar och 'vallningsbara skidor (Astra Wax)'; live-titelns 'pjäxor' motsägs av källan och produkttypen 'Klassiska skidor Peltonen', så typordsbytet till Klassiska Skidor stöds (R7) och följer syskonen Astra Skin 25. Alla specifikationsrader stämmer med källan. Längdenheten cm är en tolkning av variantvärdena (skidlängd i cm är entydigt för klassiska skidor 180–200). Ingen tillverkarsida hittades för SKU 21AN925100 (webben visar bara Astra Step/Skin/G-Grip), så inget hämtat därifrån. Rättning: första meningen var nära cirkulär ('Klassiska skidor ... är vallningsbara skidor', R11) och metan saknade artikel ('Klassiska skidorna ...' ska vara 'De klassiska skidorna'); båda omformulerade utan nya fakta. Meta 136 tecken.

**meta** före:
```
Klassiska skidorna Peltonen Astra Wax är vallningsbara och har Rottefella NIS Touring Basic-bindningar monterade. Längder 180, 190 och 200 cm.
```
**meta** efter:
```
Peltonen Astra Wax är vallningsbara klassiska skidor med monterade Rottefella NIS Touring Basic-bindningar. Längder 180, 190 och 200 cm.
```

**html** före:
```
<p>Klassiska skidor Peltonen Astra Wax är vallningsbara skidor med kärna av trä med luftkanaler.
```
**html** efter:
```
<p>Peltonen Astra Wax är vallningsbara klassiska skidor med kärna av trä med luftkanaler.
```

### 45002 (10470929334538, k_45a_utkast.json): GODKÄND

Live ACTIVE, lager 10 (3+7), tagg På beställning, leveranstidsmeningen finns. Varianterna 230000103 (EAN 4713250020471, 629 kr) och 230000104 'sinine' (EAN 4713250020488, 489 kr) är samma pedal i svart respektive blå enligt ebike24.com (black 230000103, blue 230000104, purple 105, red 106) och bikesandbeyond.ca (Blue 04713250020488 230000104): v1.9 uppfylld, inga färger eller priser låsta. Mått, kontaktyta, profil 16/17,1 mm, 9 pinnar per sida, tätade lager och stålaxel stämmer med källan (webben: Cr-Mo-axel, 117x110 mm, 350 g). Vikten rätt utelämnad. v1.10: ingen lastgräns i egen källa eller på webben (Giants maxvikter gäller cyklar, inte pedaler), därför 'Maximal lastgräns: Ej känd' i spec och mening i texten. Inga kvalitetsord. Ingen dubblett: Pinner Comp Röd (230000106, skriven) och Lila (230000105, DRAFT) är andra artiklar.

### 45101 (10472332493066, k_45b_utkast.json): RÄTTA

Live ACTIVE, en variant EAN 2902506587840, lager 1. Uppgifterna stämmer med egen källa; typordet Stuntsparkcykel följer de skrivna Union Lite-syskonen och 'trike' är maskinöversättning. Ingen dubblett: Lite S finns skriven i Svart och Neochrome, inte Lime. Rättning (R2): egen källa anger användarhöjd 105–125 cm, men scootshop.net för exakt EAN 2902506587840 anger 'For rider height: 110-145 cm'. Uppgiften är motsägande och stryks; de skrivna syskonen (Lite XS/S/M) saknar också användarhöjd. Kvar finns en 'enligt tillverkaren' (lastkapacitet 100 kg, ren svensk rad, bekräftad av scootshop). Inga säkerhets- eller utvecklingslöften.

**html** före:
```
<li>Vikt: 3,293 kg</li>
<li>Användarhöjd enligt tillverkaren: 105–125 cm</li>
```
**html** efter:
```
<li>Vikt: 3,293 kg</li>
```

### 45102 (10472332820746, k_45b_utkast.json): RÄTTA

Live ACTIVE, en variant EAN 2906869937854, lager 3. Uppgifterna stämmer med egen källa (källans 'Styrning: 520 x 480 mm' återgivet som Styre, som syskonen). Ingen dubblett: Lite M finns skriven i Svart, Lime och Neochrome, inte Blå. Rättning (R2): egen källa anger användarhöjd 110–130 cm, men scootshop.net för exakt EAN 2906869937854 anger 'Rider height: 135-165 cm' (vikt 3 415 g, styre 520/480 mm och 100 kg stämmer där). Uppgiften stryks som för syskonen.

**html** före:
```
<li>Vikt: 3,415 kg</li>
<li>Användarhöjd enligt tillverkaren: 110–130 cm</li>
```
**html** efter:
```
<li>Vikt: 3,415 kg</li>
```

### 45103 (10515745636618, k_45b_utkast.json): RÄTTA

Live ACTIVE, en variant SKU 3760004845294 (EAN enligt scootshop.net och veloplus.ee), lager 2. Färgen rätt utelämnad (live-titeln Krom/Svart mot källans svart-grå; webben säger Chrome/Black respektive 'black, silver'), liksom sätet i aluminium och färdighetsnivån. Mått och material stämmer med källan och med veloplus.ee (däck 508x118 mm, styre 600x540 mm, 110 mm hjul, 100 kg). Rättning 1 (R7): live-ordet är Tricksparkcykel och egen källa talar om trickelement, inte stunt; praxis (vag2b_utlatande_49_50, k_utlatande_02e) behåller Tricksparkcykel där live-titeln säger det. Rättning 2 (R2): åkarlängden 160–170 cm i egen källa motsägs för exakt artikeln av veloplus.ee ('Riders 140–170 cm') och scootshop.net ('135-165 cm'); stryks i 'Passar för' och specifikationen, och 'Passar för' får i stället källans användning (trick och skatepark). Vikt 2,9 kg behålls ur egen källa (webben 2,95–2,99 kg). En 'enligt tillverkaren' kvar (lastkapacitet).

**titel** före:
```
Stuntsparkcykel Versatyl S2S Edition Pro
```
**titel** efter:
```
Tricksparkcykel Versatyl S2S Edition Pro
```

**seo_title** före:
```
Stuntsparkcykel Versatyl S2S Edition Pro
```
**seo_title** efter:
```
Tricksparkcykel Versatyl S2S Edition Pro
```

**html** före:
```
<p>Stuntsparkcykeln Versatyl S2S Edition Pro har ståplattform och styre i aluminium, styrsystemet IHC och ABEC-9-lager. Hjulen är 110 mm och sparkcykeln väger 2,9 kg.</p><h2>Passar för</h2><ul>
<li>Dig som söker en stuntsparkcykel med plattform och styre i aluminium</li>
<li>Dig som är mellan 160 och 170 cm lång, enligt tillverkaren</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Stuntsparkcykel</li>
<li>Märke: Versatyl</li>
<li>Modell: S2S Edition Pro</li>
<li>Plattformens längd: 508 mm</li>
<li>Plattformens bredd: 118 mm</li>
<li>Plattformens material: Aluminium</li>
<li>Styrmaterial: Aluminium</li>
<li>Styrsystem: IHC</li>
<li>Styrarmens längd: 600 mm</li>
<li>Styrbredd: 540 mm</li>
<li>Lager: ABEC-9</li>
<li>Hjulstorlek: 110 mm</li>
<li>Vikt: 2,9 kg</li>
<li>Åkarlängd: 160–170 cm</li>
```
**html** efter:
```
<p>Tricksparkcykeln Versatyl S2S Edition Pro har ståplattform och styre i aluminium, styrsystemet IHC och ABEC-9-lager. Hjulen är 110 mm och sparkcykeln väger 2,9 kg.</p><h2>Passar för</h2><ul>
<li>Dig som söker en tricksparkcykel med plattform och styre i aluminium</li>
<li>Dig som vill köra trick och åka i skatepark</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Tricksparkcykel</li>
<li>Märke: Versatyl</li>
<li>Modell: S2S Edition Pro</li>
<li>Plattformens längd: 508 mm</li>
<li>Plattformens bredd: 118 mm</li>
<li>Plattformens material: Aluminium</li>
<li>Styrmaterial: Aluminium</li>
<li>Styrsystem: IHC</li>
<li>Styrarmens längd: 600 mm</li>
<li>Styrbredd: 540 mm</li>
<li>Lager: ABEC-9</li>
<li>Hjulstorlek: 110 mm</li>
<li>Vikt: 2,9 kg</li>
```

### 45104 (10488246632714, k_45b_utkast.json): GODKÄND

Live ACTIVE, lager 3 (Default Title SKU 2206041185, EAN 4712878765702, 12 469 kr, lager 3; L / black SKU 2206041187, EAN 4712878765719, 5 229 kr, lager 0). Enligt Davids beslut 2026-11-08 är slutsiffra 5 = M och 7 = L för Giant, och Attend RS 3 GTS i butiken följer samma mönster (2226011185 M, 1187 L); velomarket.ee visar Attend RS 1 GTS, Black, med ram M (50 cm) för 168–178 cm. Varianterna är alltså samma cykel i M och L; v1.9 uppfylld trots den orimliga prisskillnaden, och texten låser varken storlek eller pris. Bara M och L nämns (XL säljs inte). Färg Svart: L-varianten och live-titeln, ingen variant anger annan kulör (v1.8). Alla tekniska uppgifter och medföljande delar stämmer med källan; 'pålitlig', 'hållbarhet', 'utmärkt hantering' rätt utelämnade. Ramlås och belysning bara som medföljande delar. Tagg På beställning, leveranstidsmeningen finns. Prisfelet bör rättas av David/leverantören (påverkar inte texten).

### 45105 (10488246796554, k_45b_utkast.json): GODKÄND

Live ACTIVE, lager 1 (S / white). Default Title och S / white delar SKU 1017035184 och EAN 4711291218024: överbliven Default Title (v1.7), ignoreras; prisskillnaden låses inte. Slutsiffra 4 = S (Davids beslut 2026-11-08) stämmer med variantnamnet S. Ingen dubblett enligt dubblettbeslutet 2026-11-05: 10502528205066 är SKU 1017035185 (M). Titeln skiljer produkterna med 'storlek S' (två kommatecken, samma form som skrivna Liv-titlar). Färgen rätt utelämnad (white mot Lavender Blush). Ramstorlek S 46,5 cm för 158–169 cm, ALUXX, gaffel, Shimano Cues 20 växlar, BR-U6030, S-R2 Disc, Gavia Fondo 2 700x32c och fästpunkter stämmer med källan; stabilitets-, komfort- och bromskraftlöften rätt utelämnade. Ingen webbträff på EAN, men uppgifterna kommer ur produktens egen källa. Tagg På beställning, leveranstidsmeningen finns.
