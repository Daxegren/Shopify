# Stickprov pass 4, BEST OF SPORTS, 2026-11-05 (endast läsning)

## Omfattning och begränsningar
- Läste live via shopify_api.py (butiken verifierad: BEST OF SPORTS): title, seo.title, seo.description, descriptionHtml, tags. Inget skrevs i Shopify.
- **Antal:** uppdraget angav 70 produkter, men de åtta skrivfilerna innehåller tillsammans **60** (21b 8, 21c 1, 22a 2, 23abc 13, 23de 12, 24abc 10, 24def 10, 24i 4). Alla 60 lästes live. Ingen fil saknas; 70 verkar vara en felräkning, eller så ska ytterligare en fil ingå (k_skriv_2.json har 34 och ingick inte i listan).
- Jämförelsen mot källtexterna (R4, lastgräns ordagrann) gjordes mot före-filerna i rapporter/shopify-original-2026-11-05 för de 160 produkter som finns där (bl.a. alla lastgränsprodukter i 24abc/24def/24i). 21b, 21c och delar av 23abc/23de fanns inte där och är inte källkontrollerade.
- Språkgranskningen är en läsning av den live-lästa texten (utan leveransblocket, som är standardtext: 49 med standardblock, 11 med tillägget "Beställningsvaror kan ta upp till en vecka längre"). Jag kan inte avgöra sakuppgifter som inte står i före-filerna.

## 1. Avvikelse live mot skrivfil
**Ingen.** 60 av 60 stämmer tecken för tecken: title, seo.title (null behandlat som lika med title), seo.description och descriptionHtml. Taggen texter-klara finns på alla 60.

## 2. Maskinella kontroller (alla 60)
- Titel högst 70 tecken och högst 2 kommatecken: OK (23014 har två decimalkomman i "12,7–45,3 kg", inga fler). Ingen titel med tre eller fler kommatecken.
- SEO-titel högst 43, meta 70–155 tecken: OK. Inga dubbletter av titel, SEO-titel eller meta.
- "enligt tillverkaren": högst en gång per fält och högst två per text: OK.
- Ursprungsord (Italien, Nederländerna, Danmark m.fl.): inga. "tillverkad i" förekommer bara som material (24114 "tillverkad i stål").
- R4-lastgränser (24061, 24062, 24063, 24066, 24070, 24071, 24072, 24073, 24094, 24096, 24097, 24098, 24100, 24104, 24106, 24107, 24110, 24112, 24114, 24126, 24161, 24162, 24163, 24164): värdena stämmer med källans etiketterade rad. 23022 (Ecobike Cargo, källan hade 155 kg och 15/40 kg) har korrekt utelämnats.
- Märkesstavning Maxxis (22005), Excelsior (23058): rätt. Maxxus/Excalibur förekommer inte. "Cargobike of Sweden" är rätt i titel, meta och brödtext, men se punkt B8.

## 3. Fynd (id/nr, exakt citat)
### A. Bör rättas (språk/regel)
1. **9433** titel "Innerslang Continental MTB 27.5 tum, Presta 42 mm, 47/62-584": decimalpunkt i titeln, medan SEO-titel, meta och brödtext har "27,5".
2. **23026** titel "Presta-Ventil 60 mm": versalt V (övriga: "Presta-ventil"). Meta: "däckbredd 32-47 mm" med bindestreck, ska vara tankstreck "32–47" som i övriga filer.
3. **23009** specifikation "Lager: Tätade, underhållsfria": kvalitetsord (R5) utan "enligt tillverkaren" i specen, medan brödtexten har "som enligt tillverkaren är underhållsfria".
4. **24161** och **24162**: "Reservdel till latsdrag kabelstation" / "reservdel för latsdrag kabelstation" / "Typ: Reservdelsset, kablar för latsdrag kabelstation" är ingen korrekt svensk sammansättning (titeln har "Latsdragsstation"). Förslag: "latsdragsstation" genomgående.
5. **24071** brödtext: "Öppningen kan öppnas på styrets sida" (tautologi, otydlig) och "Dig som vill komma åt väskan från sadeln" (oklart stöd i källan).
6. **23039** meta: "är klassad IPX7" utan "enligt tillverkaren" (brödtexten har "Enligt tillverkaren är den vattentät enligt IPX7"); inkonsekvent attribution.
7. **Räckvidd utan attribution:** **23022** spec "Räckvidd: Upp till 220 km" (meta och brödtext säger "enligt tillverkaren"), **24163** "Räckvidd: Upp till 60 km" och **24164** "Räckvidd: Upp till 50 km" (inget "enligt tillverkaren" någonstans), medan **24096** ("20–40 km enligt tillverkaren") och **24098** ("Upp till 80 km enligt tillverkaren") har det. Prestandapåstående bör behandlas lika.
8. **24096**, **24163**, **24164** SEO-titel "El-lastcykel Cargobike Classic" / "...Cargobike Longtail Varia" / "...Cargobike Long Lite": märket förkortat till "Cargobike" (titel och meta har "Cargobike of Sweden"). Om 43-teckensgränsen inte tvingar fram det bör det prövas mot märkesregeln.
9. **23011** spec "Manövrering: Lättanvänd på/av-knapp" (kvalitetsord utan attribution; övriga tålighetsuppgifter har "enligt tillverkaren").

### B. Stilistiskt/småsaker
10. **20018** namnet växlar: titel och SEO-titel "Gymstick Cohesive Tape", meta och brödtext "Gymstick Cohesive Bandage Tape".
11. **23005** meta "...Steady som med steady light lyser kvar i 4 minuter efter stopp" (krångligt). **23005** spec "6 V elcykelbatteri" mot **23017** "6 V e-cykelbatteri" (olika stavning).
12. **23036** titel och meta "-5...-10" utan enhet (**23037** har "°C"); meta och spec saknar °C.
13. **23055** brödtext "fem viktlägen, 4,5, 7, 9, 11 och 13,5 kg": decimalkomma i uppräkning med kommatecken blir svårläst.
14. **23060** "Ethic Scooter Stand Pad görs av plast" (övriga: "är gjord av"/"tillverkad av").
15. **22005** spec delvis på engelska och med decimalpunkt: "ALUXX SLR-grade aluminium, thru-axle 12x148 mm", "Giant Crest XC Comp, 100 mm, 15x110, remote lockout", "Maxxis Recon Race 29x2.4". **22004** gaffel: "helt i kolfiber OverDrive-styrrör" (grammatiskt hackig).
16. **24100** brödtext "som fästs på korgens kant, och den fästs på cykeln" (upprepning). **24112** och **24114** använder "×" i mått, övriga "x". **24097** "26–28"" (tumtecken) mot "tum" i titeln. **24112** "Cykellås: Tillbehör som tillval" (pleonasm).

### C. Granskat utan anmärkning
Samtliga övriga kontrollerade punkter: inga fel med gjort/gjord (alla böjda rätt: "balansbrädan är gjord", "handlindorna är gjorda", "stödet ... tillverkat"), pluralis/singularis, grå/gråa ("grå och svart" rätt), meta utan verb (alla meta har verb), hälso-/skyddspåståenden (inga; "Enligt tillverkaren är den lätt att rengöra" 23042/23043 är attribuerat).

## 4. Sammanfattning
0 avvikelser live mot skrivfil (60/60). Inga R4/R5-brott med ursprung, tre-komma-titlar eller felstavade märken. 9 punkter i A (varav 3-4 mest värda att rätta: 9433, 23026, 24161/24162, räckviddsattributionen) och 7 stilpunkter i B. Det finns ingen automatisk spärr som fångade A1, A2 och A4.
