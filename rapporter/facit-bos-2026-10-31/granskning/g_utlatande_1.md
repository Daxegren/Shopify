# Granskning faktatext g_1 (träningsstationer, multigym, kabeltorn och tillbehör) – BEST OF SPORTS (2026-11-04)

Oberoende granskning, bara läsning. Butiken är bekräftad med get-shop-info: **BEST OF SPORTS** (bestofsports.se, SEK).

**Underlag:** `vag2_skriv/g_1_utkast.json` (23 utkast) och `g_1_avvisade.json` (10384, 10389), totalt 25 produkter från `g_1_in.json`. Granskat i FAKTATEXTLÄGE (§14–17, `fakta_utkastprompt.md`) med meta 70–155 tecken (§17). Standardblocket är jämfört med `b_skriv_24.json`. Lastuppgifter är bedömda enligt Davids beslut alt A 2026-11-04: engelska eller maskinöversatta maxvikter utelämnas, och ordagranna svenska lastgränser med enhet får stå en gång som 'enligt tillverkaren'.

**Metod:** alla 25 produkter är hämtade live (graphql `nodes`). Alla är ACTIVE och produkttypen är oförändrad. Maskinellt kontrollerat:
- längder och kommatecken
- `format_regler.py` (titel_versaler, kolon_versal): inga avvikelser
- märket i versaler: inga
- standardblocket
- beställningsmeningen mot taggen 'På beställning'
- tal i texten mot fakta
- unikhet mot alla `*.json` i vag2_skriv och granskning, och inom filen

**Resultat:**
- Standardblocket är identiskt med b_skriv_24 på alla 23. Beställningsmeningen finns på de 20 produkter som har taggen och saknas på 10376 och 10381, som saknar taggen.
- Titlar 26–56 tecken, SEO-titlar 26–42, meta 105–154. Inga dubbletter.
- **Pilot 20:** ingen av de 25 finns i `bestofsports-pilot-20-produkter-2026-10-25.csv`. Experiment 1 hålls inte längre utanför (David 2026-11-04).

## Resultat
| Dom | Antal | Nr |
|---|---|---|
| GODKÄND | 15 | 10376, 10378, 10379, 10381, 10386, 10390, 10397, 10398, 10399, 10400, 10401, 10402, 10408, 10409, 10410 |
| RÄTTA | 7 | 10380, 10392, 10395, 10396, 10403, 10411, 10412 |
| UNDERKÄND | 1 | 10407 |
| Avvisade (bekräftade) | 2 | 10384, 10389 |

## Särskilda kontroller
- **Maxvikter som står kvar:** 10376 150 kg, 10378/10379/10380 130 kg, 10381 135 kg och 10386 150 kg. Alla står ordagrant på svenska som 'Maximal användarvikt: … kg' i just den produktens egen källa. Var och en återges en gång i specifikationen som 'enligt tillverkaren' och står inte i titel eller meta.
- **Utelämnade lastuppgifter, borta ur alla fält:**
  - 10376: 90 kg
  - 10378: 2 x 90 kg
  - 10379: 70/100 kg
  - 10395: 150 kg (engelska)
  - 10396: 125 och 135 kg
  - 10402: 150 kg (engelska)
  - 10403: 135 och 150 kg (engelska)
  - 10407: 120 kg
  - 10408: 135 kg
  - 10410: 70 och 150 kg
  - 10411: 2 x 80 och 150 kg
  - 10412: 90 och 100 kg
- **Avvisningar:** båda är riktiga. 10384 är samma Autark 5.0 som 10386 (samma mått), och källan anger Totalvikt både 80 kg och 255 kg. 10389 har bara 'Tillverkaren är Hammer' som källa.
- **10403:** produktvikten 324 kg är identisk med 10402, trots att 10402 har två viktblock om 80 kg och andra mått, och 'Dimensions' saknar värde. Vikten utelämnas (rättning). På 10402 behålls 324 kg, se fråga 2.
- **Engelska källor (10395, 10402, 10403):** bara entydiga specifikationer är översatta. 'Ceiling height' återges som 'Takhöjd' utan 'minsta'.
- **Typord:**
  - Jõujaam → Träningsstation (10376, 10396) och → Powerstation (10395): godtas.
  - Multy Gym → Träningsstation, Power station → Träningsmaskin (10381) och → Träningsstation (10410) stöds av källtexten.
  - Squat Stand → Squatställning är rimligt, men 10407 underkänns av andra skäl.
  - Rättas: brödtexten skriver engelska 'power station' (två ord) i 10380, 10395, 10411 och 10412 och ändras till 'powerstation' som i titeln. 10390 behåller 'Autark FT3 power station' som namn på den produkt den passar till.
- **SEO-titel 10396** saknade typord och rättas till 'Träningsstation Hammer Bio Force Extreme'.
- **Format:** märket står i vanlig skrivning överallt. Stor bokstav efter kolon, versaler på beskrivande ord och små bokstäver i enheter är rätt.
- **Cirkulära inledningar:** inga tomma inledningar. Varje inledning tillför mått, vikt eller funktion.
- **Säkerhets- och hälsopåståenden:** 'säker' (10410), stabilitet (10395, 10401), 'högsta säkerhetsstandarder' (10407), fettförbränning och muskelutveckling (10396) samt rehabilitering (kabeltorn) är borta. Ingen produkt har elektronik eller massage.
- **Syskonläckage:** inget. Cable Tower 4.0, Dubbel och NorsK har var sina mått och vikter ur sin egen källa, och Autark 3.0, 5.0 och 9.0 likaså.

## Per produkt
| Nr | Id | Dom | Skäl och rättning (fullständigt före/efter i g_utlatande_1.json) |
|---|---|---|---|
| 10376 | 10472307163402 | GODKÄND | Mått, 111 kg, sex förvaringsfack och fästen för gymnastikbollar står ordagrant. 'Maximal användarvikt: 150 kg' står ordagrant på svenska och återges en gång som 'enligt tillverkaren' (alt A). 'Viktkapacitet 90 kg', robust, hållbarhet och Ergoline är borta. Jõujaam → Träningsstation godtas enligt beslutet (obs: att_bekrafta säger felaktigt att källan använder ordet träningsstation, källan säger 'bur'). Ingen tagg 'På beställning' och ingen beställningsmening, vilket är rätt. |
| 10378 | 10472288813322 | GODKÄND | 17 höjder, mått 124 x 220 x 225,5 cm, 352 kg och 2 personer ('enligt tillverkaren') står ordagrant. 130 kg står ordagrant på svenska, en gång som 'enligt tillverkaren'. '2 x 90 kg' är borta. Multi Gym → Multigym. Beställningsmeningen är rätt. |
| 10379 | 10472288747786 | GODKÄND | Multy Gym → Träningsstation stöds av källans 'multifunktionell träningsstation'. Förstärkt ram, 4 personer, mått och 346 kg står ordagrant. 130 kg ordagrant på svenska, en gång. '70/100 kg' och Spanien är borta. Beställningsmeningen är rätt. |
| 10380 | 10472288715018 | RÄTTA | Vikter av metall 90 kg (viktblocket, ingen lastgräns), mått och 225 kg står ordagrant. 130 kg ordagrant på svenska, en gång. Biomekanik och Spanien är borta. Typordet i texten är engelska 'power station' (två ord), medan titeln har Powerstation. Rättas till 'powerstation' i meta och text så att det blir svenska och stämmer med titeln.<br>meta: `BH Fitness Indar är en power station med vikter av metall på 90 kg. Den är 190 x 72 x 210 cm och väger 225 kg.` → `BH Fitness Indar är en powerstation med vikter av metall på 90 kg. Den är 190 x 72 x 210 cm och väger 225 kg.`<br>html: `…<p>BH Fitness Indar är en power station med vik…` → `…<p>BH Fitness Indar är en powerstation med vik…`<br>html: `…/h2><ul> <li>Dig som söker en power station med vik…` → `…/h2><ul> <li>Dig som söker en powerstation med vik…` |
| 10381 | 10656691749130 | GODKÄND | Power station → Träningsmaskin stöds av källtexten ('träningsmaskin'). Egen kroppsvikt, hemma och på professionella gym ('enligt tillverkaren'), mått och 40 kg står ordagrant. 135 kg ordagrant på svenska, en gång. Ingen beställningstagg och ingen beställningsmening, vilket är rätt. |
| 10386 | 10589703241994 | GODKÄND | VectorLoad, 1 x 80 kg, mått, golvyta och 255 kg står ordagrant. 150 kg står ordagrant på svenska ('Maximal användarvikt'), en gång. Hållbarhet och perfekt är borta. Avvisningen av 10384 är riktig: samma modell och mått, och källan anger Totalvikt både 80 och 255 kg. |
| 10390 | 10472289435914 | GODKÄND | 30 och 50 mm och anslutning till Autark FT3 står i källan ('enligt tillverkaren'). Inga mått eller lastgränser. Tyskland och 'nästa nivå' är borta. Landmine står i live-titeln. |
| 10392 | 10605384171786 | RÄTTA | 4 x 5 kg, 20 kg och 65 → 85 kg står ordagrant i källan. Första metameningen saknar verb. Passar-punkten 'ett kabeltorn' gör kompatibiliteten bredare än titeln, som bara anger Cable Tower 4.0.<br>html: `…assar för</h2><ul> <li>Dig som har ett kabeltorn o…` → `…assar för</h2><ul> <li>Dig som har Hammer Cable Tower …`<br>html: `…ssar för</h2><ul> <li>Dig som har ett kabeltorn och …` → `… för</h2><ul> <li>Dig som har Hammer Cable Tower 4.…`<br>html: `…r för</h2><ul> <li>Dig som har ett kabeltorn och vi…` → `…ör</h2><ul> <li>Dig som har Hammer Cable Tower 4.0 …`<br>html: `…ör</h2><ul> <li>Dig som har ett kabeltorn och vill…` → `…/h2><ul> <li>Dig som har Hammer Cable Tower 4.0 och…`<br>html: `…r</h2><ul> <li>Dig som har ett kabeltorn och vill lä…` → `…2><ul> <li>Dig som har Hammer Cable Tower 4.0 och vi…`<br>html: `…h2><ul> <li>Dig som har ett kabeltorn och vill läg…` → `…ul> <li>Dig som har Hammer Cable Tower 4.0 och vill …`<br>html: `…2><ul> <li>Dig som har ett kabeltorn och vill lägga…` → `… <li>Dig som har Hammer Cable Tower 4.0 och vill lägga…`<br>meta: `Extra vikter på 20 kg i fyra viktskivor om 5 kg för Hammer Cable Tower 4.0. Enligt tillverkaren ökar motståndet från 65 kg till 85 kg.` → `Extra vikter för Hammer Cable Tower 4.0 är ett set med fyra viktskivor på 5 kg, totalt 20 kg. Enligt tillverkaren ökar motståndet från 65 kg till 85 kg.` |
| 10395 | 10471348535562 | RÄTTA | Engelsk källa. 1 x 80 kg, mått, utrymme och 225 kg är entydigt översatta. 'Maximum operating weight 150 kg' är borta ur alla fält (alt A), liksom stabilitet och låg takhöjd. Jõujaam → Powerstation godtas. Typordet i texten är engelska 'power station' (två ord), medan titeln har Powerstation. Rättas till 'powerstation' i meta och text så att det blir svenska och stämmer med titeln.<br>meta: `Hammer Autark 3.0 är en power station med vikter på 1 x 80 kg. Den är 190 x 116 x 198 cm och väger 225 kg.` → `Hammer Autark 3.0 är en powerstation med vikter på 1 x 80 kg. Den är 190 x 116 x 198 cm och väger 225 kg.`<br>html: `…<p>Hammer Autark 3.0 är en power station med vik…` → `…<p>Hammer Autark 3.0 är en powerstation med vik…`<br>html: `…/h2><ul> <li>Dig som söker en power station med vik…` → `…/h2><ul> <li>Dig som söker en powerstation med vik…` |
| 10396 | 10472298512650 | RÄTTA | Motståndsrep, magträningsbälte, två personer ('enligt tillverkaren'), mått, utrymme, 78 kg och användarlängd 205 cm står ordagrant. 125 kg och 'Maximal driftsvikt 135 kg' är borta. Fettförbränning och muskelutveckling är borta. SEO-titeln saknar typord; 'Träningsstation Hammer Bio Force Extreme' (40 tecken) är unik, eftersom den andra Bio Force-produkten i butiken är ett Power rack.<br>seo_title: `Hammer Bio Force Extreme Sixpack Plus` → `Träningsstation Hammer Bio Force Extreme` |
| 10397 | 10612594573578 | GODKÄND | 65 kg, 38 x 34 x 200 cm, 120 kg och det modulära konceptet ('enligt tillverkaren', stor bokstav efter kolon) står ordagrant. Rehabilitering och precision är borta. Ingen last. |
| 10398 | 10605384139018 | GODKÄND | 2 x 65 kg, 80 x 120 x 200 cm, 248 kg och 'små utrymmen' ('enligt tillverkaren') står ordagrant. Ingen sammanblandning med NorsK (egen källa). |
| 10399 | 10624087458058 | GODKÄND | Träfinish, skandinavisk design ('enligt tillverkaren'), 2 x 65 kg, mått och 248 kg står ordagrant. Double → Dubbel. SEO-titeln är unik. |
| 10400 | 10612594606346 | GODKÄND | Träfinish, 'skandinaviskt inspirerad' ('enligt tillverkaren'), 65 kg, mått och 120 kg står ordagrant. Inget läckage från 10399. |
| 10401 | 10605384270090 | GODKÄND | Kopplar ihop två kabeltorn, har surfplattehållare och krokar: allt står i källan. Stabilitetspåståendena är borta. Inga påhittade mått. |
| 10402 | 10471310262538 | GODKÄND | Engelsk källa, entydigt översatt: 2 x 80 kg, 5-stegs vinkeljustering, två extra kabelsystem, mått, utrymme, takhöjd 225 cm och 324 kg. 'Maximum operating weight 150 kg' och 'jaw pull' är borta. 324 kg är rimligt för två viktblock om 80 kg och behålls; samma värde på 10403 utelämnas (se där). |
| 10403 | 10471311180042 | RÄTTA | Engelsk källa. Multipress, kabelsystem, skivstång, 30/50 mm, utrymme och takhöjd är entydigt översatta. 'Support up to 135 kg' och 150 kg är borta. Produktvikten 324 kg är exakt samma som för Autark 9.0 (10402), trots att 9.0 har två viktblock om 80 kg och andra mått, och 'Dimensions' saknar värde. Troligen ett källfel, så vikten utelämnas.<br>html: `…s med viktskivor på 30 mm och 50 mm. Maskinen väger 324 kg.</p><h2>Passar…` → `…s med viktskivor på 30 mm och 50 mm.</p><h2>Passar…`<br>html: `…i> </ul><h2>Specifikationer</h2><ul> <li>Vikt: 324 kg</li> <li>Fritt utr…` → `…i> </ul><h2>Specifikationer</h2><ul> <li>Fritt utr…` |
| 10407 | 10462840094986 | UNDERKÄND | Squatställning (bär last) med motsägande och delvis maskinöversatt källa. Måtten 68 x 77 x 117 cm motsäger att hyllhöjden kan ställas till 189 cm. 'Hyllhöjd', '8-stegs justering av stegpinnarna' och '30 mm kedjor' är maskinöversatt med oklar betydelse. 'Säkerhetskrokar … högsta säkerhetsstandarder' är ett säkerhetspåstående som inte går att återge entydigt; utkastet har 'Ingår: Säkerhetskrokar'. Lastkapacitet 120 kg är korrekt utelämnad. Kan inte skrivas säkert utan bekräftade mått och komponenter. |
| 10408 | 10472280916234 | GODKÄND | Kompakt hemmagym, över 80 övningar och TNT-teknik ('enligt tillverkaren'), alla tre måtten och 83 kg står ordagrant. 'Maximal arbetsvikt 135 kg', tyst och Tyskland är borta. |
| 10409 | 10472289304842 | GODKÄND | 6 hållare och håldiameter 50 mm står i källan, och 'viktskivor' står i källans första mening, så att 'kedjor' tolkas som viktplattor är belagt. Passar Autark FT3 enligt titeln. Kort meta 109 tecken (§17). |
| 10410 | 10472288616714 | GODKÄND | Power station → Träningsstation stöds av källan. Överkroppen, polyuretanbelagda stålkablar, mått, 154 kg och tillbehören står ordagrant. 'Säker' (träningen är säker), 70 kg, 150 kg och Italien är borta. |
| 10411 | 10472288354570 | RÄTTA | Hela kroppen, mått, 294 kg och 8 paket står ordagrant. '2 x 80 kg' och 'Maximal belastningsvikt 150 kg' är borta. Typordet i texten är engelska 'power station' (två ord), medan titeln har Powerstation. Rättas till 'powerstation' i meta och text så att det blir svenska och stämmer med titeln.<br>meta: `Toorx CSX-3000 är en power station för träning av hela kroppen. Den är 200 x 95 x 218 cm och väger 294 kg.` → `Toorx CSX-3000 är en powerstation för träning av hela kroppen. Den är 200 x 95 x 218 cm och väger 294 kg.`<br>html: `…<p>Toorx CSX-3000 är en power station för trä…` → `…<p>Toorx CSX-3000 är en powerstation för trä…`<br>html: `…/h2><ul> <li>Dig som söker en power station för hel…` → `…/h2><ul> <li>Dig som söker en powerstation för hel…` |
| 10412 | 10472288387338 | RÄTTA | Triceps, rygg och axlar ('enligt tillverkaren'), mått och 140 kg står ordagrant. 90 kg och 100 kg är borta. Typordet i texten är engelska 'power station' (två ord), medan titeln har Powerstation. Rättas till 'powerstation' i meta och text så att det blir svenska och stämmer med titeln.<br>meta: `Toorx LTX-3000 är en power station som enligt tillverkaren är avsedd för träning av triceps, rygg och axlar. Den är 164 x 77 x 211,5 cm.` → `Toorx LTX-3000 är en powerstation som enligt tillverkaren är avsedd för träning av triceps, rygg och axlar. Den är 164 x 77 x 211,5 cm.`<br>html: `…<p>Toorx LTX-3000 är en power station som enl…` → `…<p>Toorx LTX-3000 är en powerstation som enl…`<br>html: `…/h2><ul> <li>Dig som söker en power station för tri…` → `…/h2><ul> <li>Dig som söker en powerstation för tri…` |
| 10384 | 10472282063114 | AVVISAD (bekräftad) | Dubblett av 10386 och källan motsäger sig själv (Totalvikt 80 och 255 kg). |
| 10389 | 10462846943498 | AVVISAD (bekräftad) | Källan består bara av 'Tillverkaren är Hammer' och en engelsk titel. Hantelställ bär last. |

## Öppna frågor till David
1. **10407 Hammer Core 2.0:** ska leverantören bekräfta mått, 'hyllhöjd', stegpinnar och säkerhetskrokar innan produkten skrivs för hand?
2. **10402 och 10403:** båda anger 324 kg. Ska leverantören tillfrågas om vilken vikt som är rätt? I dag står 324 kg kvar på 10402 och är borttagen på 10403.
3. **10384 och 10386:** samma Autark 5.0 ligger två gånger med olika SKU och pris (64 439 och 49 769 kr). Ska dubbletten hanteras i sammanslagningen?
