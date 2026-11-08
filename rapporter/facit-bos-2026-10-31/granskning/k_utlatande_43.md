# Granskningsutlåtande k_43a–k_43c och k_44a, massageredskap och lyfta Gymstick-produkter (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (spärren på massageredskap hävd; fyra lyftbara Gymstick-produkter får utkast), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_42.md` och formatet i `k_utlatande_42.json`. Tillverkarsidorna lästes för alla produkter som har en (gymstick.com 17 sidor, tunturi.com 4 sidor, alla 200, SKU och EAN stämmer på samtliga). MG50 och Vibrating Duo saknar tillverkarsida (404); de bygger bara på egen live-text.

Alla 27 utkast och den avvisade dubbletten är ACTIVE med lager > 0. Inget utkast står på spärrlistan. `skrivfil_kontroll.py` gav 0 fel och 0 varningar på utkasten och på de rättade texterna (inga falsklarm för "hälsa" uppstod). Standardblocket är exakt rätt på alla; leveranstidsmeningen finns bara på 43201 (MG40), som är den enda med taggen På beställning. Titel ≤70 tecken och ≤2 kommatecken, SEO ≤43, meta 102–143 tecken med verb, "Passar för" finns på alla. Titlar, SEO-titlar och metatexter är unika inom batcherna, mot alla andra utkast-/skrivfiler och mot butikens titlar (sökning på typorden Massagepistol, Massagerulle, Massageboll/-bollar, Foamroller, Målnät, Pulley, Kabel, Spikey, Pilates). Numren 43001–43008, 43101–43108, 43201–43207 och 44001–44004 är unika. Varje rättning är ETT sammanhängande före/efter-par per fält, och varje före-text förekommer exakt en gång i utkastet (kontrollerat i python).

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_43.json`.

## Resultat: 18 GODKÄND, 9 RÄTTA, 0 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 43001 | 10581095874826 | k_43a_utkast.json | GODKÄND | – |
| 43002 | 10581105180938 | k_43a_utkast.json | GODKÄND | – |
| 43003 | 10581096136970 | k_43a_utkast.json | GODKÄND | – |
| 43004 | 10581108752650 | k_43a_utkast.json | GODKÄND | – |
| 43005 | 10581096300810 | k_43a_utkast.json | GODKÄND | – |
| 43006 | 10581108850954 | k_43a_utkast.json | GODKÄND | – |
| 43007 | 10581106295050 | k_43a_utkast.json | GODKÄND | – |
| 43008 | 10581108785418 | k_43a_utkast.json | RÄTTA | html |
| 43101 | 10581109276938 | k_43b_utkast.json | GODKÄND | – |
| 43102 | 10581119140106 | k_43b_utkast.json | RÄTTA | html |
| 43103 | 10593397178634 | k_43b_utkast.json | GODKÄND | – |
| 43104 | 10636654706954 | k_43b_utkast.json | GODKÄND | – |
| 43105 | 10636715491594 | k_43b_utkast.json | GODKÄND | – |
| 43106 | 10636715557130 | k_43b_utkast.json | RÄTTA | html |
| 43107 | 10636723159306 | k_43b_utkast.json | RÄTTA | html |
| 43108 | 10411701272842 | k_43b_utkast.json | GODKÄND | – |
| 43201 | 10471174242570 | k_43c_utkast.json | GODKÄND | – |
| 43202 | 10471317602570 | k_43c_utkast.json | GODKÄND | – |
| 43203 | 10472259191050 | k_43c_utkast.json | GODKÄND | – |
| 43204 | 10472270823690 | k_43c_utkast.json | GODKÄND | – |
| 43205 | 10472276590858 | k_43c_utkast.json | GODKÄND | – |
| 43206 | 10581106229514 | k_43c_utkast.json | GODKÄND | – |
| 43207 | 10581107900682 | k_43c_utkast.json | RÄTTA | html |
| 44001 | 10581097054474 | k_44a_utkast.json | RÄTTA | titel |
| 44002 | 10581100888330 | k_44a_utkast.json | RÄTTA | titel |
| 44003 | 10581104460042 | k_44a_utkast.json | RÄTTA | titel, html |
| 44004 | 10581105115402 | k_44a_utkast.json | RÄTTA | titel |

## Effektpåståenden (v1.11)

Alla texter genomsöktes efter både tydliga och subtila effektord (avslappnande, lindrar, stimulerar, djupvävnad, återhämtning, cirkulation, blodflöde, spänning, smärta, värk, knutar, triggerpunkter, terapi, behandling, inflammation, svullnad, rörlighet, välbefinnande). Inget sådant finns i någon titel, SEO, meta eller beskrivning. Kvar finns bara "ergonomiskt format" (ordagrant ur källan som formbeskrivning), "stöd i olika positioner" (Pilates Roller, fysiskt stöd ur egen källa) och "mjuka handtag". Värme, kyla, vibration och batteri står bara som specifikation: temperaturer, nivåer, drifttider, kapacitet och skötselanvisning (frys/varmvatten), aldrig med effekt. Elektroniska pistoler har bara tekniska uppgifter och avsedd användning ("avsedd för massage av …").

## Mönster

- Uppgifterna hör till exakt artikel: SKU och EAN kontrollerades mot tillverkarsidan för alla 21 produkter som har en. Active- och vanliga varianter (Cold Massager 72031/63051, Massage Hook 72040/63053) är olika artiklar med egna EAN och skiljs åt i titeln; inga dubbletter mellan dem eller mot skrivna produkter (Spikey Combo 63014 är annan EAN). Den avvisade 10472258699530 (Velomarket, GYM72029) delar EAN med 43005 och är rätt avvisad som dubblett.
- Motsägelser i tillverkarens egna sidor hanterades rätt i nästan alla fall (mått på Active Mini Massager, MG30 och Spikey; material och laddare på Fascia Gun; batteritid på MG50). Ett fall missades: materialet på massagehuvudena i 43008.
- Två påhittade detaljer i "Passar för" (43102 "handtag i båda ändar", 43207 "utan batteri eller sladd") byts mot källans ord (R1).
- Skivstångshållaren 44003: 500 kg står på engelska utan att det framgår om lasten gäller paret eller varje hållare; skrivs som "Maximal lastgräns: Ej känd" (v1.10, uppdragets avgränsning).
- Pilates Roller 43104: v1.9 är uppfylld (samma artikel i tre färger, lager 1 913; titel och text låser varken färg eller pris).
- Typord: Kylmassageredskap, Massagehook, Massageredskap, Massagepinne och Skivstångshållare godtas som rimliga nya ord (följer tillverkarens eller live-textens ord). Cable Pulley System behålls på engelska som syskonet Pulley Station. Foamroller och Massagerulle följer redan godkända syskon.
- Stor bokstav på beskrivande ord i titeln (R9) saknades i tre titlar på k_44a (Dörrankare, Par, Tricepsrep).

## Frågor till David

1. Butiksprofilen säger fortfarande att "massagepistoler och massagerullar med värme/vibration" ligger under `utanfor_tills_vidare`, trots v1.11 och beslutet 2026-11-08. R6 säger att profilen är facit, så raden behöver tas bort (ditt beslut finns redan) innan skrivfilen byggs. Samtidigt bör de nya typorden läggas till i `godkanda_typord`.
2. Massagehook eller Massagekrok? Live-texten använder "massagehook"; "massagekrok" är det vanliga svenska ordet. Utlåtandet godkänner Massagehook (R7); säg till om du vill byta.
3. Pilates Roller: blå kostar 539 kr, svart och rosa 349 kr. Troligen ett felaktigt pris i butiken (texten berörs inte).
4. Active Mini Massager finns aktiv två gånger (Gymstick 59 kr, lager 1 461, och Velomarket 159 kr, lager 1, samma EAN). Bara Gymstick-produkten får text. Vill du arkivera Velomarket-kopian?
5. Alpha J-Cup: vill du att 500 kg ska stå ändå ("enligt tillverkaren, för paret")? Då behövs ditt uttryckliga besked, eftersom källan inte säger om lasten gäller paret.

## Skäl och rättningar per produkt

### 43001 (10581095874826, k_43a_utkast.json): GODKÄND

Live ACTIVE, en variant 72031, EAN 6430062511383, lager 126. https://www.gymstick.com/active-cold-massager.html (SKU och EAN stämmer): handtag, rullkula av rostfritt stål med kylgel, 5 cm, frys före användning, rostfritt stål/PP, svart-krom, 18,5 x 8 x 5 cm, 0,12 kg, videolänk. Allt stämmer; inga effektpåståenden (inflammation, svullnad, lindring utelämnade). Kylan bara som specifikation (v1.11). Nytt typord Kylmassageredskap godtas (tillverkarens Cold Massager).

### 43002 (10581105180938, k_43a_utkast.json): GODKÄND

Live ACTIVE, 63051, EAN 6430062511994, lager 107. https://www.gymstick.com/cold-massager.html (SKU och EAN stämmer). Uppgifterna stämmer; ingen kylgel eller videolänk nämns, rätt utelämnat. Egen artikel, inte dubblett av 43001. Inga effektpåståenden.

### 43003 (10581096136970, k_43a_utkast.json): GODKÄND

Live ACTIVE, 72040, EAN 6430062511475, lager 255. https://www.gymstick.com/active-massage-hook.html (SKU och EAN stämmer): rulle i änden, PP 82 %/TPR 18 %, svart-blå, 35 x 7,5 x 16 cm, 0,16 kg, videolänk. 'Instant relief', 'achy muscles' utelämnade. Typord Massagehook godtas (live-texten på 63053 använder ordet); svenskt alternativ Massagekrok, se frågor.

### 43004 (10581108752650, k_43a_utkast.json): GODKÄND

Live ACTIVE, 63053, EAN 6430062510799, lager 445. https://www.gymstick.com/massage-hook.html (SKU och EAN stämmer): PP 100 %, svart-röd, samma mått/vikt. Egen artikel (annan färg, material, EAN). Inga effektpåståenden.

### 43005 (10581096300810, k_43a_utkast.json): GODKÄND

Live ACTIVE, 72029, EAN 6430062511369, 59 kr, lager 1461. https://www.gymstick.com/active-mini-massager.html (SKU och EAN stämmer): 'specifically designed for foot and forearm', TPR, blå, 0,08 kg. Motstridiga mått rätt utelämnade (R2). Velomarket-produkten 10472258699530 (GYM72029, samma EAN, 159 kr, lager 1) är rätt avvisad som dubblett (R12a); David bör veta att samma artikel ligger aktiv två gånger till olika pris.

### 43006 (10581108850954, k_43a_utkast.json): GODKÄND

Live ACTIVE, 63054, EAN 6430062513547, lager 764. https://www.gymstick.com/massage-stick.html (SKU och EAN stämmer): olika muskelgrupper, särskilt formade huvuden, nylon, helsvart, 45 x 19 x 3 cm, 0,2 kg. 'Opening muscle membranes/joints' rätt utelämnat.

### 43007 (10581106295050, k_43a_utkast.json): GODKÄND

Live ACTIVE, 61165, EAN 6430016907484, lager 407. https://www.gymstick.com/fascia-roller.html (SKU och EAN stämmer): bumps, kompakt, EVA, helsvart, 13 x 32 x 13 cm, 0,42 kg, övningsguide. Blodflöde, vävnadsflexibilitet, smärtlindring utelämnade. Inte dubblett av Massagerulle Gymstick Fascia Roll, Kork (61040).

### 43008 (10581108785418, k_43a_utkast.json): RÄTTA

Live ACTIVE, 61147, EAN 6430062514483, lager 287. https://www.gymstick.com/massage-gun.html (SKU och EAN stämmer). Tekniska data stämmer (3 hastigheter 1200/2000/2800, 2000 mAh/16,8 V, 3,5–5 h, borstlös 20 W, 8 mm, max 55 dB, 0,79 kg). Rättning (R2): materialet är motsägande på sidan (punktlistan 'abs, steel, silicone, eva' efter huvudena, tabellen 'Abs, silicone, eva' för produkten) och det framgår inte att materialet gäller huvudena; materialet stryks från raden.

**html** före:
```
<li>Massagehuvuden: 5 st, av ABS, stål, silikon och EVA</li>
```
efter:
```
<li>Massagehuvuden: 5 st</li>
```

### 43101 (10581109276938, k_43b_utkast.json): GODKÄND

Live ACTIVE, 61280, EAN 6430016909648, lager 364. https://www.gymstick.com/nexgen-massage-gun.html (SKU och EAN stämmer): 38 W borstlös, 10 mm, 5 hastigheter 1600–3000 RPM, 5 huvuden varav Heat & Cold (10–45 °C), fyra silikonbelagda, 2000 mAh upp till 6 h, USB-C, väska, 20 x 17 x 5 cm, 1,1 kg, material och färg. Värme/kyla bara som temperaturspecifikation, ingen effekt (v1.11). Stall force, 'deep tissue', inflammation m.m. utelämnade. 'Enligt tillverkaren' två gånger (R5 tillåter).

### 43102 (10581119140106, k_43b_utkast.json): RÄTTA

Live ACTIVE, 61345, EAN 6430062515497, lager 583. https://www.gymstick.com/vivid-massage-stick.html (SKU och EAN stämmer): rulle med 12 separat roterande delar, texturerade ergonomiska handtag, 45 cm, 5 cm, TPE+TPR+PP, grå-turkos, 0,3 kg. 'Trigger muscle knots' utelämnat. Rättning (R1): 'handtag i båda ändar' står inte i källan (utkastaren flaggade själv); raden i Passar för skrivs om till källans ord.

**html** före:
```
<li>Dig som vill ha en massagepinne på 45 cm med handtag i båda ändar</li>
```
efter:
```
<li>Dig som vill ha en massagepinne på 45 cm med texturerade handtag</li>
```

### 43103 (10593397178634, k_43b_utkast.json): GODKÄND

Live ACTIVE, 72033, EAN 6430062511406, lager 468. https://www.gymstick.com/active-spikey-massage-combo.html (SKU och EAN stämmer): två redskap, spikig yta, boll 7,5 cm, Black/Blue, set. Motstridiga mått på dubbelbollen och kemikaliekoder rätt utelämnade. 'Deep tissue massage', 'improve circulation' utelämnade. Inte dubblett (R12a, Davids regel 2026-11-05): redan skrivna Massagebollar Gymstick Spikey Combo har SKU 63014 och annan EAN; titeln skiljer med 'Active'.

### 43104 (10636654706954, k_43b_utkast.json): GODKÄND

Live ACTIVE, tre färgvarianter av samma artikel: Blå 539 kr (lager 726), Svart 349 kr (865), Rosa 349 kr (322), totalInventory 1913. v1.9 uppfylld: titel, SEO och text låser varken färg eller pris; färgerna räknas bara upp som tillgängliga. Alla uppgifter står i egen svensk källa (90 cm, 15 cm, EPE-skum, ca 830 g, självmassage, stöd i olika positioner). Typord Foamroller som skrivna Gymstick-syskon. Prisskillnaden på blå bör kontrolleras av David (troligen fel pris i butiken).

### 43105 (10636715491594, k_43b_utkast.json): GODKÄND

Live ACTIVE, 100912-00019-0001, EAN 4260438735905, lager 323. Egen svensk källa: längd 16 cm, diameter 8,2 cm, mellandel 5,3 cm, svart, ryggraden får plats mellan bollarna (formbeskrivning, inget effektpåstående). Hållning, smärta och 'lösa knölar' utelämnade. Titel skiljer sig från Dubbel Massageboll Gymstick Active Recovery.

### 43106 (10636715557130, k_43b_utkast.json): RÄTTA

Live ACTIVE, 100911-00019-0001, EAN 4260438735899, lager 481. Egen källa: ca 10 cm, räfflad yta, svart, kläm fast bollen mellan kroppen och väggen/golvet. Knutar, smärtsamma ställen utelämnade. Rättning (språk): 'genom att bollen klämmas fast' ska vara 'kläms'.

**html** före:
```
genom att bollen klämmas fast mellan kroppen
```
efter:
```
genom att bollen kläms fast mellan kroppen
```

### 43107 (10636723159306, k_43b_utkast.json): RÄTTA

Live ACTIVE, 100849-00019-0156, EAN 4260438733796, lager 78. Egen källa: riktad självmassage, 6 cm, 140 g, svart med Gorilla Sports-logga. Blodgenomströmning, återhämtning, smärta utelämnade. Rättning (språk): 'klämmas' ska vara 'kläms'.

**html** före:
```
genom att bollen klämmas fast mellan kropp
```
efter:
```
genom att bollen kläms fast mellan kropp
```

### 43108 (10411701272842, k_43b_utkast.json): GODKÄND

Live ACTIVE, 14TUSYO067, EAN 8717842034255, lager 2, ingen På beställning-tagg. https://www.tunturi.com/en/massage-gun-mini.html (SKU och EAN stämmer): 6 hastigheter, 4 munstycken, LED, 1400–2800 RPM, 'brushless, 15W, 45-50 db', 2–3 h, USB-C, väska, 460 g. Motstridiga mått rätt utelämnade. Stimulerar blodcirkulation, avkoppling, 'tyst' utelämnade.

### 43201 (10471174242570, k_43c_utkast.json): GODKÄND

Live ACTIVE, 14TUSYO082, EAN 8717842035450, lager 1, tagg På beställning; leveranstidsmeningen finns och standardblocket är annars exakt. https://www.tunturi.com/en/mg40-massage-gun.html (SKU och EAN stämmer): 20 hastigheter, 6 huvuden, LED, 8 mm, 1800–2800, 15 W 50 dB, laddtid 3 h, USB-A till USB-C, väska och manual, 635 g, svart. Driftstid 2–3,5 h står både i tillverkarens lista, beskrivningstext och egen live-text ('upp till 3,5 timmar'); tabellens 5–11 h avviker men tre källor är samstämmiga, så raden godtas. Stall force utelämnad.

### 43202 (10471317602570, k_43c_utkast.json): GODKÄND

Live ACTIVE, 14TUSYO071, EAN 8717842035283, lager 3. https://www.tunturi.com/en/head-for-massage-gun-heat-cold.html (SKU och EAN stämmer): nivåer 40/45 °C och 20/15 °C, drifttider, USB-C 2,5 h, ABS, 4,5 x 4,5 x 9,1 cm, 120 g, tre gummiringar, kompatibla märken. Värme och kyla bara som specifikation; tillverkarens effektlöften (smärta, svullnad, inflammation) utelämnade (v1.11).

### 43203 (10472259191050, k_43c_utkast.json): GODKÄND

Live ACTIVE, 14TUSYO059, EAN 8717842033005, lager 1. Tillverkarsidan finns inte längre (404, kontrollerat). Bara entydiga tekniska uppgifter ur egen live-text: 20 hastigheter 1200–3300 varv/min, fyra huvuden (boll, gaffel, boll, platt), tre program och manuellt läge, LED-pekskärm med batterivisning, litiumjon, bärväska. Maskinöversatta fördelar och motstridig batteritid utelämnade (R2).

### 43204 (10472270823690, k_43c_utkast.json): GODKÄND

Live ACTIVE, 14TUSYO081, EAN 8717842035443, lager 3. https://www.tunturi.com/en/mg70-massage-gun-pro.html (SKU och EAN stämmer): 5 hastigheter 1300–2500, 6 huvuden, vridbart huvud 5 lägen, 3+1 program, 12 mm, 25 W 45–55 dB, 3 h/3 h, 26,6 x 17,8 x 8,3 cm, 1,9 kg, svart, väska med USB-C-kabel och adapter. 'Djup avslappning', 'muskelåterhämtning', stall force utelämnade.

### 43205 (10472276590858, k_43c_utkast.json): GODKÄND

Live ACTIVE, 14TUSYO072, EAN 8717842035306, lager 1. Tillverkarsidan saknas; egen live-text har entydig specifikation (16 x 9 x 9 cm, 700 g, ABS/silikon, 3 vibrationshastigheter, 1 program, LED, litiumjon 1800 mAh, laddning 3 h, batteritid 2 h). Vibration bara som specifikation utan effekt (v1.11). Stress, muskelvärk, 'maximal avslappning och lindring' utelämnade.

### 43206 (10581106229514, k_43c_utkast.json): GODKÄND

Live ACTIVE, 61185, EAN 6430062515176, lager 1696. https://www.gymstick.com/fascia-gun.html (SKU och EAN stämmer; sidan kallar den Mini Massage Gun): 6 nivåer 1400–2800, 4 huvuden, 1500 mAh/12,6 V, 2–3 h, 12 W, 6 mm, USB-C, max 55 dB, 9,6 x 4,7 x 15,4 cm, 0,63 kg, svart-krom. Motstridigt material och laddare rätt utelämnade. Huvudenas användning (triggerpunkter, djupa muskler) rätt utelämnad. Egen artikel, inte dubblett av 43008; DRAFT-produkten 'Massagepistol, Silver' (61185S) berörs inte.

### 43207 (10581107900682, k_43c_utkast.json): RÄTTA

Live ACTIVE, 63052, EAN 6430062511918, lager 339. https://www.gymstick.com/hot-cold-roller.html (SKU och EAN stämmer, kategori Massage Tools): PVC och gel, helsvart, 8 x 19 x 8 cm, 0,51 kg, värms i varmt vatten (ej kokande, ej mikrovågsugn), frys högst 5 timmar per gång. Värme/kyla bara som skötselspecifikation, ingen effekt. Rättning (R1): 'utan batteri eller sladd' står inte i källan; Passar för-raden byts mot källans material.

**html** före:
```
<li>Dig som vill ha en massagerulle utan batteri eller sladd</li>
```
efter:
```
<li>Dig som vill ha en massagerulle av PVC och gel</li>
```

### 44001 (10581097054474, k_44a_utkast.json): RÄTTA

Live ACTIVE, 72009, EAN 6430062511123, lager 160. https://www.gymstick.com/active-workout-tube-with-door-anchor.html (SKU och EAN stämmer): slang med mjuka handtag, dörrankare, videolänk, TPR+PP+skum, blå-svart, produktmått 140 x 12,5 x 3 cm (förpackningen anges separat, så 140 cm är slangens längd), 0,26 kg. Toning, nybörjare och 'non-slip' utelämnade. Rättning (R9, syskonpraxis och live-titeln): 'med Dörrankare' med stor bokstav.

**titel** före:
```
Träningsslang Gymstick Active Workout med dörrankare
```
efter:
```
Träningsslang Gymstick Active Workout med Dörrankare
```

### 44002 (10581100888330, k_44a_utkast.json): RÄTTA

Live ACTIVE, 53155, EAN 6430016902809, lager 7. https://www.gymstick.com/court-mini-goal-net.html (SKU och EAN stämmer): ersättningsnät för Court Mini Goal i storleken 79 x 53 cm, polyester. Tunn men entydig källa (tre fakta, v1.6). Rättning (R1/R3): titeln '..., 79 x 53 cm' ser ut som nätets mått; tillverkaren anger målets storlek. Titeln skrivs så att måttet hör till målet.

**titel** före:
```
Målnät Gymstick Court Mini Goal Net, 79 x 53 cm
```
efter:
```
Målnät Gymstick Court Mini Goal Net för Mål 79 x 53 cm
```

### 44003 (10581104460042, k_44a_utkast.json): RÄTTA

Live ACTIVE, SP-PRO-APR-8, EAN 6430062515756, lager 41. https://www.gymstick.com/alpha-j-cup.html (SKU och EAN stämmer): J-formade stålhållare för Alpha Power Rack och Alpha Cage Rack, avtagbara, parvis (enhet PR), helsvart. Rättning (R4/v1.10): 'The maximum distributed load on the brackets is 500 kg. Sold in pairs.' anger inte entydigt om lasten gäller paret eller varje hållare, så lastgränsen skrivs som 'Ej känd' i text och specifikation. Rättning (R9): ', Par' med stor bokstav som syskon ('Kabelhandtag Enhands Kort, Par'). Nytt typord Skivstångshållare godtas (barbell holders).

**titel** före:
```
Skivstångshållare Gymstick Alpha J-Cup, par
```
efter:
```
Skivstångshållare Gymstick Alpha J-Cup, Par
```

**html** före:
```
Enligt tillverkaren är den maximala fördelade belastningen på fästena 500 kg.</p><h2>Passar för</h2><ul>
<li>Dig som har en Alpha Power Rack eller Alpha Cage Rack</li>
<li>Dig som söker skivstångshållare av stål</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Skivstångshållare (J-hooks)</li>
<li>Märke: Gymstick</li>
<li>Modell: Alpha J-Cup</li>
<li>Material: Stål</li>
<li>Färg: Svart</li>
<li>Säljs: Parvis</li>
<li>Passar till: Alpha Power Rack och Alpha Cage Rack</li>
<li>Maximal fördelad belastning på fästena enligt tillverkaren: 500 kg</li>
```
efter:
```
Maximal lastgräns är inte känd.</p><h2>Passar för</h2><ul>
<li>Dig som har en Alpha Power Rack eller Alpha Cage Rack</li>
<li>Dig som söker skivstångshållare av stål</li>
</ul><h2>Specifikationer</h2><ul>
<li>Typ: Skivstångshållare (J-hooks)</li>
<li>Märke: Gymstick</li>
<li>Modell: Alpha J-Cup</li>
<li>Material: Stål</li>
<li>Färg: Svart</li>
<li>Säljs: Parvis</li>
<li>Passar till: Alpha Power Rack och Alpha Cage Rack</li>
<li>Maximal lastgräns: Ej känd</li>
```

### 44004 (10581105115402, k_44a_utkast.json): RÄTTA

Live ACTIVE, 61241, EAN 6430016901000, lager 63. https://www.gymstick.com/cable-pulley-system.html (SKU och EAN stämmer): kabelträning hemma eller lätt gymanvändning, drag/tryck vertikalt, horisontellt, i vinkel; skivhållare 33 cm, kabel 200 cm/6 mm, ståltalja med 48 cm rem, 3 karbinhakar, tricepsrep 70 cm, svart-stål, 2,1 kg, material. Ingen lastgräns hos tillverkaren: 'Ej känd' i text och specifikation (v1.10). Typord Cable Pulley System behålls som syskonet Pulley Station Gymstick. Rättning (R9): 'med Tricepsrep' med stor bokstav.

**titel** före:
```
Cable Pulley System Gymstick med tricepsrep
```
efter:
```
Cable Pulley System Gymstick med Tricepsrep
```
