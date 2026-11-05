# Granskningsutlåtande k_28j, k_28k och k_30e (BEST OF SPORTS), 2026-11-05

Granskaren är Opus och har bara läst. Underlaget är `vag2_skriv/k_28j_utkast.json` (10 barn- och ungdomsprodukter), `k_28k_utkast.json` (10 barn- och ungdomsprodukter) och `k_30e_utkast.json` (6 kosttillskott), alltså 26 produkter. Källtext, varianter (SKU, EAN, pris, lager), vendor, taggar och skapandedatum lästes live via Admin API (`shopify_api.py`) 2026-11-05. Butiken bekräftades som BEST OF SPORTS. Syskon och möjliga dubbletter söktes upp med titelsökning i butiken. Ingenting skrevs i Shopify. Regler: regler-v1.md v1.4–v1.8, BESLUTSLOGG 2026-11-05 och profilens `frislappta_2026_11_05`. Barn och ungdom: bara fakta ur källan. Kosttillskott: produktfakta och användning, utan hälso- och näringspåståenden (1924/2006).

**Resultat:** 16 GODKÄND, 10 RÄTTA, 0 UNDERKÄND. På rättade kopior gav `skrivfil_kontroll.py` 0 fel och 0 varningar för alla tre filerna. Varje 'före' förekommer exakt en gång i sitt fält (kontrollerat i python). Titlar, SEO-titlar och metatexter är unika inom de 26 och mot alla tidigare skrivfiler i `vag2_skriv/`. Titlarna har 31–60 tecken, SEO-titlarna 27–43 och metatexterna 78–147.

**Genomgående:**
- **Påståenden:** på de rättade kopiorna sökte jag i titel, SEO-titel, meta och html (utan standardblocket) efter skydd, säker, stöd, bygg, förbättr, snabb, minsk, immun, energi, återhämt, hälsa, effekt, muskel, kvalitet, optimal, ultral, lätt, ben, tänder, trygg, stabil, bekväm, perfekt, slitstark, robust, bidra, hjälp och normal. Träffarna är bara delnamn och ingredienser: kedjeskydd, stödhjul, stödben, cykelstöd, snabbkoppling, klumpförebyggande, 'med hjälp av en shaker' och 'skydda mot ljus'. Inget säkerhets-, skydds-, utvecklings-, hälso- eller näringspåstående finns kvar. D3 och D3+K2 nämner inte ben, tänder, immunförsvar, muskler eller kalcium.
- **Barnlinjen:** stödhjul, kedjeskydd, stödben, cykelstöd, skjutstång och ringklocka nämns bara som medföljande delar. Ingen produkt har ljus kvar, eftersom LED är utelämnat i 28130. Ålder och maxvikt står en gång vardera med 'enligt tillverkaren' där källan har svenska rader med etikett och enhet (28118, 28130, 28131, 28132), och ingen text har mer än två. Märket skrivs S'cool (28122).
- **Trasiga källrader** hanteras utan gissning: ramstorleksraderna hos Tabou och Academy, 'Shimano Touring - Shimano Touring', '22 cm - 12 cm - 1 cm - 1 cm', 'skivbro', 'MCGOLD' och magnesiumsaltet. Två fynd har utkastaren missat. Det ena är maskinöversatta delnamn i 28113 ('stödstång', 'tuta fram'). Det andra är enheten mm, som utkastaren har lagt till i 28128 och 28129 (praxis 28106).
- **Webbkoll (R1 v1.6/1.7):** Academy Grade 4 Belt (bikes.de: Nexus 7 växlar) bekräftar 7 växlar i 28123. Tabou Poison 24 (tabou.pl) stämmer med 28127. Stiga Snowracer Iconic (stigasports.com) stöder typordet rattkälke. Union Lite M och S (scootshop.net) bekräftar måtten men motsäger användarhöjd och styrmaterial, så de raderna stryks som i 28008.
- **Typord (R7):** 28118 Ratt blir Rattkälke (som 8410). 30042 Mineral blir Mineralkapslar, och 30046 och 30047 Vitamin blir Vitaminkapslar (live-orden 'Mineral Kapslar' och 'Vitamin Kapslar', rättade särskrivningar som 30027). Övriga typord är live-ord eller källans egna: Balanscykel, Barncykel, Ungdomscykel, Barnskridskor, Sparkcykel, Stuntsparkcykel/Stuntscooter (var och en sitt live-ord), Magnesium, Aminosyra och Triglycerider.
- **Versaler efter bindestreck:** finns bara i färgnamn (Rosa-Vit, Röd-Svart, Ocean-Rosa), som i skrivna 28073 och 28098. Inget typord har stor bokstav efter bindestreck. Alla metatexter har verb i första meningen, och ingen inleds 'X är en X'.
- **Leveranstid:** ingen av de 26 har taggen 'På beställning', och inget utkast har leveranstidsmeningen. Det är rätt.
- **Allergener:** i alla sex kosttillskott följer allergenerna bara ingredienslistan. Den generella raden 'kan innehålla mjölk, soja ...' är utelämnad, och varningsraderna återges.

**Beslut för David:**
1. **28117 Fila X 2.0 G Ice:** källan listar S, M och L, men produkten har en enda variant utan storlek (SKU 010424205-S). Rekommendation: skriv texten utan storlek nu, som granskat. Lägg till 'Storlek: S (29–32)' först när lagret har bekräftat storleken. Om inget beslutas står produkten utan storleksuppgift, alltså som i dag.
2. **28118 och 8410:** rättningen följer 8410 och ger typordet Rattkälke. Alternativet är originalordet 'Ratt', som på svenska betyder styrratt. Rekommendation: Rattkälke.
3. **Liv Tempt XS 27,5 tum:** 28036 är skriven och 28120 föreslås som Ungdomscykel (efter live-titeln 'Youth bike'). Systern 28121 (= 7049, Tempt 1 XS) avvisades av utkastaren med skälet 'damcykel', och Tempt 3 XS Airglow är skriven som Mountainbike. Rekommendation: skriv 28120 som granskat, så att den blir enhetlig med 28036. Ta 28121 i en senare batch med samma linje i stället för att hålla den utanför. Risken är låg, eftersom bara typordet skiljer.
4. **MSM (30042):** MSM är inget växtextrakt, och det finns inget godkänt påstående för det. Texten innehåller bara fakta. Rekommendation: skriv. Alternativet är att hålla MSM utanför tills Livsmedelsverket har kontrollerats (som för växtextrakt).


## 28110 (10472303558922, k_28j_utkast.json): GODKÄND

Live: en variant (SKU 1073001420), 4969 kr, live-titel 'GIANT Pre Push Bike löpcykel'. Typordet Balanscykel står i källtexten och är samma som de skrivna syskonen 28032 och 28107 (R7). Låg aluminiumram, 12-tumshjul, snabbkoppling för sadeln och ca 85–100 cm (entydig del av den trasiga raden 'Världens största cykeltillverkare: aluminium ...', en gång enligt tillverkaren) stämmer. 'Lätt', 'inspirerar', 'perfekt' och 'världens största' är borta. SEO-titeln: hela namnet med färg blir 44 tecken, så 'Push Bike' kortas bort och märket och modellnamnet Pre står kvar (R12). Den är unik mot 28032 ('Balanscykel Giant Pre Push Bike') och 28107 ('..., Svart'). Inga påståenden.

## 28112 (10472307130634, k_28j_utkast.json): GODKÄND

Live: en variant (TAB26-0510), 4809 kr, tagg 12". Aluminiumram, 1 växel, V-bromsar, ramstorlek 22 cm och ca 80–100 cm (entydig del av den trasiga raden, en gång enligt tillverkaren) stämmer. Skjutstång, stödhjul, främre korg, ringklocka, kedjeskydd och stänkskärmar nämns bara som medföljande delar, utan påståenden. 'Lätt', 'bekväm', 'slitstark', 'säker bromsning' och 'stabil körställning' är borta, liksom 'Hjulvikt: 6,6 kg' (felbetecknad). 12 tum står bara i titel och meta. Unik mot Miss AL 16 (28113 och utkastet 16" rosa-vit).

## 28113 (10472307327242, k_28j_utkast.json): RÄTTA

Live: en variant (TAB26-0580), 4889 kr. Taggen 12" är fel. Titeln, SKU:n och källans ram 24,5 cm för 100–120 cm stämmer med 16 tum, och 16 tum står bara i titel och meta (rätt; taggen rörs inte). Aluminiumram, 1 växel och V-bromsar stämmer. Rättning: i 12-tumssyskonet 28112 står samma uppräkning som 'skjutstång, stödhjul, främre korg', men här står det 'stödstång, stödhjul, tuta fram'. Det är maskinöversatta delnamn, och utkastaren gissar själv på 'troligen skjutstång respektive signalhorn'. R2: gissa inte, så båda stryks. Meta har 117 tecken efter rättning.

- `meta` före: `Stödhjul, tuta fram och kedjeskydd ingår.`
  efter: `Stödhjul, ringklocka och kedjeskydd ingår.`

- `html` före: `Stödstång, stödhjul, tuta fram, ringklocka, kedjeskydd och stänkskärmar ingår.</p>`
  efter: `Stödhjul, ringklocka, kedjeskydd och stänkskärmar ingår.</p>`

- `html` före: `<li>Medföljer: Stödstång, stödhjul, tuta fram, ringklocka, kedjeskydd och stänkskärmar</li>`
  efter: `<li>Medföljer: Stödhjul, ringklocka, kedjeskydd och stänkskärmar</li>`

## 28114 (10472307589386, k_28j_utkast.json): GODKÄND

Live: en variant (TAB25-6620), 4679 kr, tagg 12". Ram, fälgar och vevarmar av aluminium (löptexten), ramstorlek 22 cm, ca 80–100 cm (en gång enligt tillverkaren), 1 växel och V-bromsar (löptexten) stämmer. Raden '22 cm - 12 cm - 1 cm - 1 cm', 'Hjulvikt: 6,5 kg', 'för pojkar', 'maximal säkerhet', 'för hållbarhet' och 'stanna i alla förhållanden' är rätt utelämnade. Stödhjul och kedjeskydd nämns bara som medföljande delar. Unik mot Rocket FR 14 och 16 tum röd-gul (inte skrivna, annan tumstorlek).

## 28115 (10472308015370, k_28j_utkast.json): GODKÄND

Live: en variant (TAB25-4010), 7559 kr. Aluminiumram, M (43,2 cm, motsvarar titelns 17"), ca 150–165 cm (en gång enligt tillverkaren), Zoom 565 med 60 mm slaglängd, Shimano Altus/Tourney och V-bromsar stämmer. Det tveksamma 'Antal växlar: 12', 'Stöd ingår!' och den trasiga däckraden är rätt utelämnade, och bara den entydiga delen 27,5 tum används. Fästpunkterna för stänkskärmar står i källan. Titelformen följer det skrivna syskonet 'Ungdomscykel Tabou Venom 1.0 W 27,5 tum, Svart-Turkos', och kommat före 27,5 saknas för att hålla högst två kommatecken (R12). Inga påståenden ('högkvalitativa', 'bekväm', 'för unga pojkar' är borta).

## 28116 (10472308048138, k_28j_utkast.json): GODKÄND

Live: en variant (TAB25-7590), 6349 kr, tagg 16". Magnesiumram, gaffel, fälgar och vevar av aluminium, ramstorlek 22,5 cm, 100–120 cm (en gång enligt tillverkaren), 1 växel, V-bromsar samt medföljande stödhjul och kedjeskydd stämmer. 'Ultralätt' är borttaget ur titeln, och 'maximal säkerhet', 'för hållbarhet' och 'Hjulvikt' är rätt utelämnade. SEO-titeln 'Barncykel Tabou Rocket Lite MG, Grön-Vit' är unik mot 28073 ('..., 16 tum') och 14-tumsvarianten ('..., Blå-Vit').

## 28117 (10472308310282, k_28j_utkast.json): GODKÄND

Live: en variant, Default Title, SKU och streckkod 010424205-S, 1569 kr, lager 1. Källan listar S 29–32, M 33–36 och L 37–40. Butikens egna syskon visar att SKU-suffixet är storleken: 28034 har varianterna S och M med SKU -S och -M, och rullskridskorna X 2.0 G har -S, -M och -L. Det är ändå en slutsats och ingen entydig uppgift, och utkastet anger rätt ingen storlek (v1.5: bara sålda storlekar, R2: gissa inte). Texten påstår inget felaktigt. Isskridskor (Ice, rostfritt förslipat blad, taggen Skridskor). Snörning, ankelknapp, Power Strap, kompositbladfäste och Micro Jem (en gång enligt tillverkaren) stämmer, och 'robust', 'säker, stabil', 'andas' och 'flickmodell' är borta. Beslut för David: storlek S (29–32) kan läggas till när lagret bekräftar storleken.

## 28118 (10472308572426, k_28j_utkast.json): RÄTTA

Live: en variant (73-4211-07), 2369 kr, produkttyp Vinterutrustning, tagg Pulka. Fotbroms, stålram, dragstång, maximal användarvikt 80 kg (svensk rad med etikett och enhet) och ålder 5+ stämmer. De två sista står en gång vardera enligt tillverkaren, vilket är R5-taket, och pulklinjen tillåter dem. 'Mindre ram' och 'rak frontchassi' är rätt utelämnade. Rättning av typordet: 'ratt' ensamt betyder på svenska en styrratt. Samma fall gällde 8410 'Ratt STIGA Curve', som rättades till Rattkälke och är skriven, så butikens live-ord för Stigas rattkälkar är Rattkälke (R7, enhetligt där källorna är lika). Stiga kallar modellen Snowracer Iconic (stigasports.com, kategorin Snowracer), och återförsäljare beskriver den som rattkälke med styrratt. Alternativet att behålla 'Ratt' är en fråga för David, som för 8410.

- `titel` före: `Ratt Stiga Iconic`
  efter: `Rattkälke Stiga Iconic`

- `seo_title` före: `Ratt Stiga Iconic`
  efter: `Rattkälke Stiga Iconic`

- `meta` före: `Ratten Stiga Iconic`
  efter: `Rattkälken Stiga Iconic`

- `html` före: `<p>Ratten Stiga Iconic`
  efter: `<p>Rattkälken Stiga Iconic`

- `html` före: `<li>Dig som söker en ratt med fotbroms</li>\n<li>Dig som vill ha en ratt med stålram</li>\n<li>Dig som söker en ratt med dragstång</li>`
  efter: `<li>Dig som söker en rattkälke med fotbroms</li>\n<li>Dig som vill ha en rattkälke med stålram</li>\n<li>Dig som söker en rattkälke med dragstång</li>`

- `html` före: `<li>Typ: Ratt</li>`
  efter: `<li>Typ: Rattkälke</li>`

## 28119 (10472311259402, k_28j_utkast.json): RÄTTA

Live: en variant (1127009110), 7599 kr. ALUXX-aluminium, ramstorlek 22,5 cm, 118–138 cm (en gång enligt tillverkaren), Shimano Tourney, 7 växlar och däcket Giant Junior Sport 20 x 1,95 tum med 22 tpi stämmer. Den trasiga raden 'Shimano Touring - Shimano Touring', utvecklingspåståendena och de oklara 'stöd' och 'främre plattform' är rätt utelämnade. Ringklockan står som medföljande. Rättning: titel och SEO-titel saknade färg. Butiken har en annan Liv Tempt 20 ('Barncykel Liv Tempt 20" Mountainbike, AI Blue', 10471131250954, SKU 1126005110), som inte är skriven ännu, så titeln skulle krocka när den skrivs (R12). Övriga produkter i samma batch behåller engelska färgnamn (Golden Wheat, Snow Drift, Soap Suds, Metallic Orange), och färgen Virtual Pink tas därför med.

- `titel` före: `Barncykel Liv Tempt 20`
  efter: `Barncykel Liv Tempt 20, Virtual Pink`

- `seo_title` före: `Barncykel Liv Tempt 20`
  efter: `Barncykel Liv Tempt 20, Virtual Pink`

- `html` före: `<li>Medföljer: Ringklocka</li>`
  efter: `<li>Medföljer: Ringklocka</li>\n<li>Färg: Virtual Pink</li>`

## 28120 (10472323907850, k_28j_utkast.json): GODKÄND

Live: en variant (1101020283), 11919 kr. ALUXX-aluminium, XS (33 cm), ca 150–163 cm (en gång enligt tillverkaren), SR Suntour XCE, QR, stålrör, 80 mm slaglängd (svensk rad), Shimano Altus/Acera, 16 växlar, Tektro HDC TKD 149 hydrauliska skivbromsar och Maxxis Ikon 27,5 x 2,2 tum med trådkant stämmer. Den avkortade ramraden ('skivbro') och påståendena är rätt utelämnade. Typordet Ungdomscykel är en översättning av live-titelns 'Youth bike', samma som för den skrivna systern 28036 (Tempt 3 XS, godkänd i k_28cd). Färgen Golden Wheat som i 6078. 7049/28121 (Tempt 1 XS, samma upplägg) avvisades av utkastaren med skälet 'damcykel', och hanteringen är alltså inte enhetlig. Se beslutspunkt. Unik mot 28036 och 'Mountainbike Liv Tempt 3 XS, 27,5 tum, Airglow'.

## 28122 (10472329347338, k_28k_utkast.json): GODKÄND

Live: en variant (5067), 5559 kr. Aluminiumram, ramstorlek 28 cm för 105–120 cm (en gång enligt tillverkaren), V-broms och fotbroms, cykelvikt 9,5 kg (etikett 'Cykelvikt'), däckstorlek 18" samt medföljande stänkskärmar, stödhjul, kedjeskydd och stödben stämmer. Märket skrivs S'cool som i 28049–28085 (R8). Ocean/Pink blir Ocean-Rosa, med Pink översatt som i 28049 'Blå-Rosa'. 'Hög kvalitet och säkerhet', 'barnvänlig' och 'favorit bland föräldrar' är borta. Unik mot 28085 och utkastet niXe 18" rosa.

## 28123 (10472329511178, k_28k_utkast.json): GODKÄND

Live: en variant (8834), 10919 kr. Aluminiumram, 29 cm för 115–130 cm (entydig del av den trasiga raden, en gång enligt tillverkaren), 20 tum (löptexten), Shimano Nexus, remdrift och V-bromsar stämmer. Motsägelser: vikten (8 kg i texten och 8,1 kg i raden) är rätt utelämnad. Antalet växlar anges 7 i löptexten och i 'Antal växlar', men den trasiga raden säger '5 växlar ... växlar: 7'. Webbkoll (R1 v1.6/1.7): bikes.de (https://www.bikes.de/shop/fahrraeder/marke.academy/academy-grade-4-belt-2026/) anger Shimano Nexus SG-C3001 med 7 växlar och SL-7S31 för Grade 4 Belt. 7 växlar står alltså kvar med rätta. 'Ultralätt', '40 % lättare' och 'ergonomiska krav' är borta.

## 28124 (10472329543946, k_28k_utkast.json): GODKÄND

Live: en variant (8836), 9469 kr. Aluminiumram, 29 cm för 115–130 cm (en gång enligt tillverkaren), 20 tum, Shimano Claris med 8 växlar och V-bromsar stämmer. Vikten 7,5 kg står i både löptexten ('vikt på endast 7,5 kg') och raden 'Hjulvikt', så de två stämmer överens och den kan stå som Vikt. Raden '115 cm - 115 cm - 15 cm ...', fästpunkterna 'för skateboards' och påståendena är rätt utelämnade. Unik mot övriga Grade 4 (blå, Ocean, röd och Belt Lila).

## 28126 (10472330920202, k_28k_utkast.json): GODKÄND

Live: en variant (1127013110), 7599 kr. ALUXX-aluminium, ca 113–135 cm (en gång enligt tillverkaren), Giant Custom 30 mm, Shimano Tourney, 7 växlar, V-bromsar, Giant Junior Sport 20 x 1,95 tum med 22 tpi (den dubblerade raden återges en gång) och klockan som medföljande del stämmer. 'Trygg cykling', 'bättre stabilitet' och de oklara 'stöd' och 'liten frontplattform' är rätt utelämnade. Inga påståenden.

## 28127 (10472330952970, k_28k_utkast.json): GODKÄND

Live: en variant (TAB26-1780), 7009 kr. Aluminium, ca 125–145 cm (en gång enligt tillverkaren), Shimano Tourney, 12 växlar, V-bromsar och medföljande cykelstöd stämmer. Cykelstöd är här entydigt, till skillnad från 'stöd' i 28115 och 28119. Webbkoll: tabou.pl (Poison 24 1.0, 2025) anger Tourney fram och bak med 12 växlar, V-bromsar, 125–145 cm och 'Podpórka' (stöd). Sidan visar andra färger än röd/svart och saknar SKU, så den bekräftar bara rimligheten. Vikten 11,8 kg står i källan och på tabou.pl. Utkastaren utelämnade den av försiktighet, vilket är tillåtet. Påståendena ('klarar trottoarkanter', 'högkvalitativa komponenter') är borta. Live-ordet Barncykel behålls (R7). Systern Poison 20 är arkiverad, så det finns ingen dubblett.

## 28128 (10472331084042, k_28k_utkast.json): RÄTTA

Live: en variant (1090034180), 13079 kr. ALUXX-aluminium med 12x142 mm genomgående axel, 110–130 cm (en gång enligt tillverkaren), stel kolfibergaffel med styrrör i legering, MicroSHIFT Acolyte, 8 växlar, Tektro HD-J2820 hydrauliska och Kenda Booster 20 x 2,4 tum stämmer. 'Lerhoppning', 'självförtroende', 'små hopp' och 'Liv-sortimentet för kvinnor' är rätt utelämnade. Rättning: källan anger gaffelaxeln '15x110' utan enhet, och utkastaren har lagt till mm (praxis 28106, där en tillagd enhet ströks; R2).

- `html` före: `15 x 110 mm genomgående axel`
  efter: `15 x 110 genomgående axel`

## 28129 (10472331346186, k_28k_utkast.json): RÄTTA

Live: en variant (1090033180), 13079 kr. Samma uppbyggnad som 28128 med MicroSHIFT Advent och Kenda Amrak 20 x 2,2 tum, vilket stämmer. Unik mot 28128 och de oskrivna Giant STP 20 Sandstorm och STP 20 FS. Rättning: enheten mm är tillagd på gaffelaxeln '15x110', som i 28128.

- `html` före: `15 x 110 mm genomgående axel`
  efter: `15 x 110 genomgående axel`

## 28130 (10472331804938, k_28k_utkast.json): GODKÄND

Live: en variant, 2969 kr, live-titel 'Scooter Rideoo 120 City Scooter LED Salmon'. Hopfällbar, höjdjusterbart styre, polyuretanhjul (löptexten), 120 mm, ABEC-9 och 3,4 kg stämmer. Lastkapacitet 70 kg (svensk rad med etikett och enhet) och 4 till 7 år står en gång vardera enligt tillverkaren, vilket är R5-taket. LED är rätt utelämnat (källan nämner inget ljus, och synbarhet ligger utanför barnlinjen). Typordet Sparkcykel som de skrivna syskonen 28076 och 28097. Meta och SEO-titel är unika mot dem.

## 28131 (10472331870474, k_28k_utkast.json): RÄTTA

Live: en variant, 2969 kr, lager 1. Totalhöjd 750 mm, vikt 3,415 kg, hjul 100 mm 88A, ABEC-9, IHC och max lastkapacitet 100 kg (en gång enligt tillverkaren) stämmer. Webbkollen bekräftar dem: scootshop.net (https://www.scootshop.net/union-lite-m-scooter-lime/) anger 750 mm, 3415 g, 100 mm, 100 kg och styre 520/480 mm. Rättning enligt praxis 28008 (Union Lite XS): samma sida anger förarlängd 135–165 cm mot källans 110–130 cm och styre i stål mot källans aluminium. Användarhöjden och styrets material är alltså inte entydiga och stryks (R2). Styrmåtten stämmer och står kvar. Typordet Stuntsparkcykel är live-ordet, som i 28008 (R7).

- `html` före: `<li>Användarhöjd enligt tillverkaren: 110–130 cm</li>\n`
  efter: (tas bort)

- `html` före: `<li>Styre: 520 x 480 mm, aluminium</li>`
  efter: `<li>Styre: 520 x 480 mm</li>`

## 28132 (10472331936010, k_28k_utkast.json): RÄTTA

Live: en variant, 2969 kr, lager 1. Totalhöjd 690 mm, vikt 3,293 kg, hjul 100 mm 88A, ABEC-9, IHC och max belastning 100 kg (en gång enligt tillverkaren) stämmer. Webbkollen bekräftar dem: scootshop.net (https://www.scootshop.net/union-lite-s-scooter-lime/) anger 690 mm, 3293 g, 100 mm, 100 kg och styre 470/450 mm. Rättning som i 28131: samma sida anger förarlängd 110–145 cm mot källans 105–125 cm och styre i stål mot källans aluminium, så båda stryks (R2, praxis 28008). Typordet Stuntscooter är produktens eget live-ord (R7: syskon med olika live-ord behåller sitt eget, som 28004 'Stuntscooter SOKE GO').

- `html` före: `<li>Användarhöjd enligt tillverkaren: 105–125 cm</li>\n`
  efter: (tas bort)

- `html` före: `<li>Styre: 470 x 450 mm, aluminium</li>`
  efter: `<li>Styre: 470 x 450 mm</li>`

## 30041 (10472351170826, k_30e_utkast.json): GODKÄND

Live: en variant (21615), 119 kr. Ingredienserna följer källan. Bara den entydiga delen 'Magnesium (77 %)' av den trasiga magnesiumraden används, och saltformen gissas inte (R2). Dosen 2 kapslar, användningen och förvaringen stämmer. Varningsraden återges, och 'en varierad kost och en hälsosam livsstil är viktiga' är rätt utelämnad. Alla hälsopåståenden (immunsystem, trötthet, återhämtning, stress, minne) är borta, och jag hittade inga kvar vid sökning. Den generella allergenraden är utelämnad, eftersom ingredienslistan inte har några allergener. Typordet Magnesium är live-ordet och samma som för den skrivna 30026.

## 30042 (10588446884106, k_30e_utkast.json): RÄTTA

Live: en variant (21754), 89 kr. MSM (metylsulfonylmetan) är en svavelförening och inget växtextrakt. Den står inte bland de uteslutna grupperna i profilen (glukosamin/hyaluron gäller den andra Essensey-produkten med MSM, som inte är med här). MSM har inget godkänt hälsopåstående i EU-registret, så texten får bara ha fakta, och alla led- och smärtpåståenden är borta. 1000 mg per daglig dos, 77 %, cellulosakapsel (HPMC i ingredienslistan), dosen 2 kapslar 30 minuter före måltid och varningsraden stämmer. Rättningar: (1) 'Dig som är fysiskt aktiv eller idrottar' tas bort ur Passar för. När ledpåståendena har strukits pekar målgruppen ensam ut en användning för träning, och raden behövs inte. (2) Typordet: live-titeln är 'Mineral Kapslar', och den skrivna 30027 med samma live-form blev Mineralkapslar (R7, enhetligt). SEO-titeln kortas till 38 tecken med märket kvar.

- `titel` före: `Mineral Trec Essensey MSM Organic Sulfur, 90 kapslar`
  efter: `Mineralkapslar Trec Essensey MSM Organic Sulfur, 90 kapslar`

- `seo_title` före: `Mineral Trec Essensey MSM Organic Sulfur`
  efter: `Mineralkapslar Trec MSM Organic Sulfur`

- `html` före: `<li>Dig som är fysiskt aktiv eller idrottar och vill ha ett MSM-tillskott med fast dos om 2 kapslar per dag</li>`
  efter: `<li>Dig som vill ha ett MSM-tillskott med fast dos om 2 kapslar per dag</li>`

## 30043 (10635764236554, k_30e_utkast.json): GODKÄND

Live: en variant (14782), 229 kr. Ingredienserna, portionen 10 g (2 skopor) i 300 ml vatten, 20 g per dag och tiderna för träningsdagar och dagar utan träning stämmer. Tiderna är användning och inget påstående. 'Optimalt förhållande 2:1:1', 'muskelbyggande', 'antikatabol' och 'återhämtning' är borta, och BCAA har inget godkänt påstående. Äpple och 250 g står bara i live-titeln (en variant). Den generella allergenraden är utelämnad. Det finns ingen annan BCAA Ultra Speed i butiken, så SEO-titeln utan smak är unik. Typordet Aminosyra är live-ordet.

## 30044 (10472277934346, k_30e_utkast.json): GODKÄND

Live: en variant (861), 169 kr. MCT-olja 100 %, 15 ml (1 matsked) 3 gånger dagligen till måltid, 45 ml per dag och varningsraden stämmer. Raden 'MCGOLD (100%)' är rätt utelämnad. 'Absorberas snabbt' och 'alternativ energikälla för idrottare' är rätt utelämnade, eftersom de är energipåståenden. Typordet (R7): live-ordet Triglycerider behålls i titeln. Källan säger 'komplex av medellånga triglycerider', så ordet står i källan, och det finns ingen skriven MCT-produkt att vara enhetlig mot. Typ-raden 'MCT-olja (medellånga triglycerider)' är källans eget ingrediensord. Webbkollen gav 404 (utkastaren). Ingen kokosuppgift och inga allergener i ingredienslistan.

## 30046 (10472280686858, k_30e_utkast.json): RÄTTA

Live: en variant (21578), 89 kr. Ingredienserna med D3 (kolekalciferol) 4 %, 1 kapsel per dag med vatten med eller efter måltid, förvaringen och varningsraden stämmer. Det finns inget D-vitaminpåstående. Jag sökte efter ben, tänder, immun, muskel, kalcium och fosfor och fick inga träffar. Mängden µg per kapsel saknas i källan, så villkoret för ett påstående kan inte styrkas, vilket utkastaren också noterar. Rättning: typordet. Live-titeln är 'Vitamin Kapslar', och butikens arkiverade systrar heter 'Vitaminkapslar TREC VIT. D3 ...'. Särskrivningen rättas som Mineralkapslar i 30027 (R7).

- `titel` före: `Vitamin Trec Essensey D3, 120 kapslar`
  efter: `Vitaminkapslar Trec Essensey D3, 120 kapslar`

- `seo_title` före: `Vitamin Trec Essensey D3`
  efter: `Vitaminkapslar Trec Essensey D3`

## 30047 (10472301658378, k_30e_utkast.json): RÄTTA

Live: en variant (SKU = EAN 5902114047344), 199 kr. 'En kapsel innehåller 2000 IE vitamin D3' står ordagrant i källan. Det är en mängduppgift och inget påstående, och den står en gång enligt tillverkaren. K2-mängden saknas och utelämnas, och '100 % av dagligt behov' är rätt borttaget. Ingredienserna (MCT-olja från kokos, gelatin, glycerol, vatten, MK-7, D3), användningen och förvaringen stämmer. Warfarin-varningen och 'friska vuxna upp till 75 år' återges, och Obs-raden är den andra av högst två 'enligt tillverkaren' (R5). Alla immun-, ben-, tand-, muskel- och koagulationspåståenden är borta (kontrollerat med sökning). Rättning: typordet Vitaminkapslar som i 30046. SEO-titeln blir 43 tecken.

- `titel` före: `Vitamin Trec Essensey D3 + K2 (MK-7), 90 kapslar`
  efter: `Vitaminkapslar Trec Essensey D3 + K2 (MK-7), 90 kapslar`

- `seo_title` före: `Vitamin Trec Essensey D3 + K2 (MK-7)`
  efter: `Vitaminkapslar Trec Essensey D3 + K2 (MK-7)`
