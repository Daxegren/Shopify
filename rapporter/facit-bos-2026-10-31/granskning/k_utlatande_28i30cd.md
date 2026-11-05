# Granskningsutlåtande k_28i, k_30c och k_30d (BEST OF SPORTS), 2026-11-05

Granskaren är Opus och har bara läst. Underlaget är `vag2_skriv/k_28i_utkast.json` (8 barn- och ungdomsprodukter), `k_30c_utkast.json` (8 kosttillskott) och `k_30d_utkast.json` (8 kosttillskott), alltså 24 produkter. Källtext, varianter (pris, SKU, EAN), vendor och taggar lästes live via Admin API 2026-11-05. Butiken bekräftades som BEST OF SPORTS (6f2e53-67.myshopify.com). Ingenting skrevs i Shopify. Regler: regler-v1.md v1.4–v1.8, BESLUTSLOGG 2026-11-05 och profilens `frislappta_2026_11_05`. Kosttillskott följer Davids linje: produktfakta och användning, inga hälso- eller näringspåståenden (1924/2006).

**Resultat:** 9 GODKÄND, 15 RÄTTA, 0 UNDERKÄND. På rättade kopior gav `skrivfil_kontroll.py` 0 fel och 0 varningar för alla tre filerna. Varje 'före' förekommer exakt en gång i sitt fält (kontrollerat i python). Titlar, SEO-titlar och metatexter är unika inom de 24, och metatexterna har 117–151 tecken efter rättning.

**Genomgående:**
- **Påståenden:** jag sökte i titel, SEO-titel, meta och html (utan standardblocket) på de rättade kopiorna efter skydd, stöd, bygg, förbättr, snabb, minsk, fett, immun, energi, återhämt, antioxid, högt protein, tillsatt, ök, bidra, hjälp, hälsa, effekt, prestation, muskel, säker, kvalitet, optimal, ultral och lätt. Träffarna är delnamn och ingredienser (kedjeskydd, stödhjul, stöd, snabbspännesadel, fettsyror, klumpförebyggande) och förvaringsraden 'skydda mot ljus'. Inget påstående finns kvar. Det enda som smugit in var 'med tillsatt kalcium, zink, vitamin B6 och vitamin D' i 30037. Formuleringen är näringspåståendet 'Med tillsatt [näringsämne]' i bilagan till 1924/2006, och den stryks.
- **Varningsraden** återges som i källan i alla 16 kosttillskott (barn, gravida och ammande, eller under 18 år, dagsdos och varierad kost där källan har dem). 'En hälsosam kost och en aktiv livsstil är avgörande för god hälsa' är rätt utelämnad. Två Obs-rader (30036, 30037) var grammatiskt fel ('produkten ska inte överskrida') och skrivs om.
- **Allergener** följer bara ingredienslistan. Den generella raden 'kan innehålla mjölk, soja ...' är utelämnad överallt.
- **Trasiga källrader** hanteras utan gissning (28100, 28104, 28106, 28107, 30029, 30030, 30033, 30036). Två tillägg av utkastaren stryks: tum på däcket i 28106 och 3000 mg fiskolja per portion i 30023 (går inte ihop med ingredienslistan).
- **Motsägelser mot tillverkaren** stryks enligt praxis 30019: procentsatserna i 30021, vattenmängden i 30031 (200 eller 250 ml) och antalet kreatinformer i 30033 (tre eller fyra).
- **Typord (R7):** Kreatinkomplex (30031–30033, 30035), Proteinisolat (30036, rättar 'Proteinisolaat'), Proteinpulver (30037, 30038, 30040), Proteinbar (30021, 30022, ur källtexten mot live-titelns 'Proteingel') och Kreatin (30029, 30030) är belagda. 28097 rättas från Scooter till Sparkcykel, som de skrivna syskonen 28076 och 28037. 30027:s särskrivning 'Mineral kapslar' blir Mineralkapslar.
- **Smaker** står bara i live-titeln i alla smaksatta produkter. Där tillverkarens sida finns stämmer de (Green apple, Raspberry, Watermelon, Creamy-blueberry, Creamy strawberry, Vanilla). Saltkaramell (30038) är på tillverkarens sida 'Chocolate Salted Caramel'. Det noteras, men live-titeln får gälla.
- **30040 (koncentrat mot isolat):** proteinkällan är rätt skriven neutralt som 'vassleprotein'. **30035:** det finns en tillverkarsida (CM3 1250, 180 kapslar) som bekräftar doseringen. **30033:** det finns en egen pulversida (Crea Xtreme Powder, 180 g), så kapselsidan gäller inte. Doseringen stämmer med förpackningen enligt källan och tillverkaren i alla 16 kosttillskott, utom vattenmängden i 30031.
- **Meta och första meningen:** fem metatexter saknade verb i första meningen (30021, 30022, 30029, 30030, 30033). 30024 började 'Namn är ett kosttillskott', och den inledningen rättas. Ingen annan har formen 'Namn är ett typord'.
- **Barnregeln:** 28097–28107 har inga säkerhets-, skydds- eller utvecklingspåståenden. Stödhjul, kedjeskydd och pakethållare nämns bara som medföljande delar. Ljus som medföljande del stryks i 28105 (praxis k_28efgh). Märket skrivs S'cool (28098).
- **Faktakoll:** trecnutrition.com (Trec Nutrition Sp. z o.o., Gdynia) hade sidor för 30021, 30022, 30026, 30031–30033, 30035–30038 och 30040. Det saknas sidor för Essensey (30023, 30027), Vit. C 1000 (30024) och Boogie Creatine (30029, 30030). Sidorna visar inte EAN, så produkterna matchas på namn, förpackning och smak.
- **Leveranstid:** ingen av de 24 har taggen 'På beställning', och inget utkast har leveranstidsmeningen. Det är rätt.

**Beslut för David:** (1) 30024: löptexten gäller 'Vit. C Strong 1000' (tablett med bioflavonoider och zink), medan titel, ingredienser och 90 kapslar gäller Vit. C 1000. Rekommendation: skriv med rättningen (bara titelns namn och den egna ingredienslistan, utan 1000 mg-raden). Alternativet är att avvisa enligt R3. (2) 28105 har en yngre möjlig dubblett, 10589703373066 (samma titel, annat SKU och EAN, 10 kr dyrare). Den ska in i sammanslagningsplanen och får inte skrivas med samma text.


## 28097 (10472294449418, k_28i_utkast.json): RÄTTA

Live: en variant, 2969 kr, produkttyp Sparkcyklar. Hopfällbar, höjdjusterbart styre, polyuretanhjul 120 mm, ABEC-9 och 3,4 kg stämmer. 'Lastkapacitet: upp till 70 kg' (svensk rad med etikett och enhet) och åldern 4 till 7 år står en gång vardera med 'enligt tillverkaren', alltså två gånger (R5-taket); barnlinjen tillåter ålder och maxvikt. LED är rätt utelämnat (källan nämner ingen belysning) och komfortorden är borta. Färgen svart står i live-titeln. Rättning: typordet blir Sparkcykel, som för syskonen 28076 (rättad i k_28efgh och skriven) och 28037 (R7, enhetligt där källorna är lika).

- `titel` före: `Scooter Rideoo 120 City, Svart`
  efter: `Sparkcykel Rideoo 120 City, Svart`

- `seo_title` före: `Scooter Rideoo 120 City, Svart`
  efter: `Sparkcykel Rideoo 120 City, Svart`

- `meta` före: `Scootern Rideoo 120 City i svart är hopfällbar`
  efter: `Sparkcykeln Rideoo 120 City i svart är hopfällbar`

- `html` före: `<p>Scootern Rideoo 120 City är hopfällbar och har höjdjusterbart styre. Hjulen är av polyuretan med en diameter på 120 mm och lagren är av typen ABEC-9. Scootern väger 3,4 kg. Den är svart.</p>`
  efter: `<p>Sparkcykeln Rideoo 120 City är hopfällbar och har höjdjusterbart styre. Hjulen är av polyuretan med en diameter på 120 mm och lagren är av typen ABEC-9. Sparkcykeln väger 3,4 kg. Den är svart.</p>`

- `html` före: `<li>Dig som söker en hopfällbar scooter</li>\n<li>Dig som vill ha en scooter med höjdjusterbart styre</li>\n<li>Dig som söker en scooter med 120 mm polyuretanhjul</li>`
  efter: `<li>Dig som söker en hopfällbar sparkcykel</li>\n<li>Dig som vill ha en sparkcykel med höjdjusterbart styre</li>\n<li>Dig som söker en sparkcykel med 120 mm polyuretanhjul</li>`

- `html` före: `<li>Typ: Scooter</li>`
  efter: `<li>Typ: Sparkcykel</li>`


## 28098 (10472294777098, k_28i_utkast.json): RÄTTA

Live: en variant, 6099 kr, SKU 3076. Aluminiumram, 85–100 cm (en gång enligt tillverkaren), 1 växel, V-broms och fotbroms, 7,6 kg, kedjeskydd och stänkskärmar som medföljande delar och 'stödhjul ingår ej' stämmer. 'Idealisk', 'barnvänlig geometri' och 'kvalitet' är borta. 12 tum står bara i live-titeln och tas bara med i titeln, vilket är rätt. Inget säkerhetspåstående. Rättning: märket skrivs S'cool som i 28026 och k_28efgh (R8), inte S´COOL.

- `titel` före: `Barncykel S´COOL XXlite, 12 tum, Svart-Orange`
  efter: `Barncykel S'cool XXlite, 12 tum, Svart-Orange`

- `seo_title` före: `Barncykel S´COOL XXlite, Svart-Orange`
  efter: `Barncykel S'cool XXlite, Svart-Orange`

- `meta` före: `Barncykeln S´COOL XXlite`
  efter: `Barncykeln S'cool XXlite`

- `html` före: `<p>Barncykeln S´COOL XXlite`
  efter: `<p>Barncykeln S'cool XXlite`


## 28100 (10472295399690, k_28i_utkast.json): GODKÄND

Live: en variant, 9619 kr. Aluminiumram, 8 växlar, Shimano Claris (ur löptexten), V-bromsar och 7,8 kg stämmer. Ramstorlek 10 tum och 120–140 cm är den entydiga delen av den trasiga raden 'Aluminium::: 10" - lämplig ...' (R2). De trasiga raderna '120 cm - 120 cm ...' och 'Shimano Claris: 8 bromsar' är rätt utelämnade, liksom 'Ultralätt', 'effektiva' och pulkfästena. 20 står bara i live-titeln och bara i titeln. Inga påståenden.


## 28103 (10472297005322, k_28i_utkast.json): GODKÄND

Live: en variant, 2219 kr. Alla åtta rader stämmer: 3–5 år, 3 hjul, styrstång av aluminium, styrhöjd 490/580/670 mm, maxvikt 50 kg och 2,1 kg. Maxvikt (svensk etikett och enhet) och ålder står en gång vardera med 'enligt tillverkaren' (två, R5-taket), vilket barnlinjen tillåter. Typordet Barnsparkcykel är butikens live-ord på systerprodukten Aest Barnsparkcykel (R7). Inga påståenden.


## 28104 (10472297365770, k_28i_utkast.json): GODKÄND

Live: en variant, 6969 kr. Magnesiumram, gaffel, fälgar och vevar av aluminium, ramstorlek 22 cm för 95–110 cm, 1 växel, V-bromsar och medföljande stödhjul och kedjeskydd stämmer. 'Maximal säkerhet och komfort', 'hållbarhet', 'under alla förhållanden', 'ultralätt' och den felbetecknade raden 'Hjulvikt: 6 kg' är rätt utelämnade. Stödhjul och kedjeskydd nämns bara som medföljande delar. 14 tum står bara i live-titeln och bara i titeln.


## 28105 (10472297398538, k_28i_utkast.json): RÄTTA

Live: en variant, 7209 kr, SKU 24130063-B, EAN 5904803259052. Aluminiumram, 24 x 1,75 tum, S (13 tum) för 125–155 cm, Shimano Tourney, 21 växlar, Revoshift, V-bromsar och 14,4 kg stämmer. Pakethållaren nämns utan lastgräns. Rättning: fram- och bakljus stryks som medföljande delar (synbarhetsfunktion, praxis 28067 och 28084 i k_28efgh). Dubblett: 10589703373066 har samma titel men annat SKU (24130063-C), EAN 5904803263615, pris 7219 kr, en bild och är skapad 2026-08-11; denna (2026-04-11, en bild) är äldst och skrivs enligt dubblettbeslutet. Den yngre ska hanteras i sammanslagningsplanen och får inte skrivas med samma text.

- `html` före: `Pakethållare, stöd, stänkskärmar samt fram- och bakljus ingår.`
  efter: `Pakethållare, stöd och stänkskärmar ingår.`

- `html` före: `<li>Medföljer: Pakethållare, stöd, stänkskärmar samt fram- och bakljus</li>`
  efter: `<li>Medföljer: Pakethållare, stöd och stänkskärmar</li>`


## 28106 (10472297431306, k_28i_utkast.json): RÄTTA

Live: en variant, 6959 kr. Aluminiumram, S (13 tum) för 130–150 cm (entydig del av trasig rad), 21 växlar från Shimano, skivbromsar och främre stänkskärm stämmer med löptexten. Säkerhetsorden, 'kraftfulla', 'stoppar omedelbart', livstidsgarantin och 'Shimano Tourney' (bara på trasig bromsrad) är rätt utelämnade. Obs: utkastets anteckning säger 'Hjulvikt: 13,4 kg' men källan säger 14,3 kg; raden är ändå rätt utelämnad (felbetecknad). Rättning: källan anger däcket '24×1.90' utan enhet, och enheten tum är tillagd av utkastaren (R2, gissa inte); enheten stryks.

- `html` före: `<li>Däck: 24 × 1,90 tum</li>`
  efter: `<li>Däck: 24 × 1,90</li>`


## 28107 (10472302969098, k_28i_utkast.json): GODKÄND

Live: en variant, 4969 kr, inget EAN. Låg aluminiumram, 12-tumshjul, justerbar snabbspännesadel och ca 85–100 cm (entydig del av den trasiga raden, en gång enligt tillverkaren) stämmer. 'Världens största cykeltillverkare', 'inspirerar' och 'perfekt' är borta. Typordet Balanscykel står i källan. 'Snabbspänne' är en sadelfunktion och inget påstående.


## 30021 (10472270856458, k_30c_utkast.json): RÄTTA

Live: en variant, 29 kr, SKU 13049, EAN 5902114040598. Typordet Proteinbar står i källtexten (live-titelns 'Proteingel' är fel), som 30011/30012. Tillverkaren (https://trecnutrition.com/brands/trec/better-food/protein-bar-nougat-caramel/) bekräftar 46 g, maltitol och 1–2 barer per dag med vatten. Den anger 'nougat-flavoured filling (45 %)' och 'caramel filling (15 %)', medan live-källan anger choklad 45 % och krispigt innehåll 15 %. Procentsatserna motsäger varandra och stryks (R2, praxis 30019). 'Utan tillsatt socker', 'högt proteininnehåll' och 'hälsosammare alternativ' är borta. Allergener följer ingredienslistan, och diarrévarningen återges som i källan. Underlag för senare (inte infört): 30 g protein och 515 kcal per 100 g. Rättningar: meta saknade verb i första meningen (praxis 30011), samt procentsatserna.

- `meta` före: `Proteinbar från Trec med chokladöverdrag och karamellfyllning. Baren väger 46 g och innehåller sötningsmedlet maltitol.`
  efter: `Proteinbaren Trec Nougat och Caramel har chokladöverdrag och karamellfyllning. Den väger 46 g och innehåller sötningsmedlet maltitol.`

- `html` före: `har ett överdrag av choklad (45 %), smaksatt krispigt innehåll (15 %) och karamellfyllning.`
  efter: `har ett överdrag av choklad och karamellfyllning.`

- `html` före: `<li>Bas: Choklad (45 %), mjölkchoklad med kakaohalt minst 32 %</li>\n<li>Innehåll: Smaksatt krispigt innehåll 15 % med karamellfyllning</li>`
  efter: `<li>Bas: Mjölkchoklad med kakaohalt minst 32 %</li>\n<li>Fyllning: Karamellfyllning</li>`


## 30022 (10472270921994, k_30c_utkast.json): RÄTTA

Live: en variant, 29 kr, SKU 13050, EAN 5902114040604. Tillverkaren (https://trecnutrition.com/brands/trec/better-food/protein-bar-peanut-caramel/) bekräftar 49 g, maltitol, karamellfyllning 20 % och 1–2 barer per dag. Jordnötsandelarna (30 %, 10 % och 9 %) går isär och är rätt utelämnade. Inga påståenden. Allergener enligt ingredienslistan. Underlag: 27 g protein och 500 kcal per 100 g. Rättning: meta saknade verb i första meningen.

- `meta` före: `Proteinbar från Trec av mjölkchoklad med karamellfyllning och jordnötter. Baren väger 49 g och innehåller sötningsmedlet maltitol.`
  efter: `Proteinbaren Trec Peanut och Caramel är gjord av mjölkchoklad med karamellfyllning och jordnötter. Den väger 49 g och är sötad med maltitol.`


## 30023 (10472277672202, k_30c_utkast.json): RÄTTA

Live: en variant, 109 kr, SKU 21154. Typordet Fettsyra är live-ordet (praxis 30005). Alla hälsopåståenden (hjärta, hjärna, syn, oxidativ stress, 'potent') är borta. Varningsraden återges som källan, och allergenraden är rätt utelämnad. Tillverkarens sida (https://trecnutrition.com/brands/trec/vitality-lifestyle/omega-3-6-9/) gäller Omega 3-6-9 utan Essensey (3 kapslar per dag, 225 mg fiskolja) och alltså inte entydigt den här produkten; Essensey finns inte på trecnutrition.com. Rättning: raden '3 000 mg fiskolja, 360 mg DHA och 540 mg EPA per portion' stryks. Portionen är odefinierad, och mängden går inte ihop med ingredienslistan: gurkörtolja står före fiskoljan, så 2 kapslar skulle innehålla över 6 g olja (R2). Kvar är ett 'enligt tillverkaren'.

- `html` före: `<li>Innehåll per portion enligt tillverkaren: 3 000 mg fiskolja, med 360 mg DHA och 540 mg EPA</li>\n`
  efter: `(tomt, raden stryks)`


## 30024 (10472280359178, k_30c_utkast.json): RÄTTA

Live: en variant, 109 kr, SKU 11664, EAN 5902114018443. Källan blandar två produkter. Löptexten beskriver 'Vit. C Strong 1000' (tablett, bioflavonoider och zink), medan titeln, ingredienslistan (C-vitamin och kapselhölje av HPMC) och 90 kapslar gäller Vit. C 1000 i kapslar. En webbsökning på EAN:et ger detaljhandlare med 'Trec Vit. C 1000 90 caps', men sidorna gick inte att öppna, så inget hämtas därifrån. trecnutrition.com har ingen sida för produkten. Utkastet utelämnar rätt bioflavonoider, zink, azorubinraden och 'ökad mängd'. Rättningar: produktnamnet följer titeln ('Vit. C 1000', inte 'Strong'), den cirkulära inledningen 'är ett kosttillskott' tas bort och '1000 mg' utan bas (per kapsel eller per dag framgår inte) stryks ur meta, text och specifikation (R2). 1000 står kvar som del av namnet. Beslut för David: alternativet är att avvisa enligt R3 (källtexten gäller en annan variant).

- `meta` före: `Trec Vit. C Strong 1000 är ett kosttillskott med C-vitamin (1000 mg). Förpackningen innehåller 90 kapslar och dosen är 1 st dagligen med 300 ml vatten.`
  efter: `Trec Vit. C 1000 innehåller C-vitamin i 90 kapslar. Dosen är 1 st dagligen med 300 ml vatten, helst efter en huvudmåltid.`

- `html` före: `<p>Trec Vit. C Strong 1000 är ett kosttillskott med C-vitamin (1000 mg).`
  efter: `<p>Trec Vit. C 1000 innehåller C-vitamin.`

- `html` före: `<li>Dig som vill ha ett C-vitamintillskott med 1000 mg C-vitamin</li>`
  efter: `<li>Dig som vill ha ett C-vitamintillskott som tas en gång om dagen</li>`

- `html` före: `<li>Innehåll: C-vitamin 1000 mg</li>\n`
  efter: `(tomt, raden stryks)`


## 30026 (10472280523018, k_30c_utkast.json): GODKÄND

Live: en variant, 129 kr, SKU 14625. Tillverkaren (https://trecnutrition.com/brands/trec/vitality-lifestyle/triple-magnesium-complex/) bekräftar 120 kapslar, 4 kapslar per dag, 2 kapslar med 300 ml och 2 portioner per dag, i samband med måltid. 'Lättupptagliga' och alla påståenden (energiomsättning, trötthet, proteinsyntes, ben) är borta. Varningsraden återges som källan, och allergenraden är rätt utelämnad. Underlag för senare (inte infört): 261,2 mg magnesium per 4 kapslar.


## 30027 (10472280654090, k_30c_utkast.json): RÄTTA

Live: en variant, 109 kr, SKU 21339. 15 mg zink per dag (en gång enligt tillverkaren), 1 kapsel dagligen med mycket vatten efter måltid, ingredienserna och varningen stämmer. Alla påståenden om immunförsvar, hud, hår, naglar, celler och ben är borta. trecnutrition.com har bara 'Zinc' i 90 kapslar (en annan linje än Essensey), så sidan används inte. 'Organic' är en del av produktnamnet. Rättning: live-ordet 'Mineral kapslar' är särskrivet och skrivs Mineralkapslar i titel och SEO-titel. Det är samma ord, som 'Vitaminkapslar' i 30024 (R7).

- `titel` före: `Mineral kapslar Trec Essensey Zinc Organic, 120 kapslar`
  efter: `Mineralkapslar Trec Essensey Zinc Organic, 120 kapslar`

- `seo_title` före: `Mineral kapslar Trec Essensey Zinc Organic`
  efter: `Mineralkapslar Trec Essensey Zinc Organic`


## 30029 (10472297890058, k_30c_utkast.json): RÄTTA

Live: en variant, 179 kr, SKU = EAN 5902114049409. Kreatinmonohydrat 87,5 %, 3,9 g (3/4 skopa) i 150 ml, högst 1 portion per dag, tiderna och varningen (under 18 år, gravida och ammande, dagsdos, varierad kost) stämmer. 'Förbättrar den fysiska prestationen' och 'önskad effekt' är borta. Allergenraden och den trasiga raden om hållbarhet efter öppnande är rätt utelämnade. Boogie Creatine finns inte på trecnutrition.com (sökningen ger bara Boogie Whey, Bar och Oat Gainer), så smak och 300 g bygger på live-titeln. Typordet Kreatin följer praxis 30010/30014. Rättning: meta saknade verb i första meningen.

- `meta` före: `Kreatinpulver från Trec med kreatinmonohydrat och smaken Bubble Gum. Burken innehåller 300 g och en portion är 3,9 g som löses upp i 150 ml vatten.`
  efter: `Kreatinpulvret Trec Boogie Creatine innehåller kreatinmonohydrat och har smaken Bubble Gum. Burken rymmer 300 g, en portion är 3,9 g i 150 ml vatten.`


## 30030 (10472298709258, k_30c_utkast.json): RÄTTA

Live: en variant, 169 kr, SKU = EAN 5902114049416. Som 30029, med aromer och svart morotskoncentrat enligt den egna ingredienslistan, och smaken Candy ur live-titeln. Inga påståenden. Ingen tillverkarsida finns. Rättning: meta saknade verb i första meningen.

- `meta` före: `Kreatinpulver från Trec med kreatinmonohydrat och smaken Candy. Burken innehåller 300 g och en portion är 3,9 g som löses upp i 150 ml vatten.`
  efter: `Kreatinpulvret Trec Boogie Creatine innehåller kreatinmonohydrat och har smaken Candy. Burken rymmer 300 g, en portion är 3,9 g i 150 ml vatten.`


## 30031 (10472301756682, k_30d_utkast.json): RÄTTA

Live: en variant, 129 kr, SKU = EAN 5902114045807. Tillverkaren (https://trecnutrition.com/brands/trec/trec-core/creatine-mono/) bekräftar 300 g, smaken Green apple, 4,1 g (1 skopa) och tiderna. Den anger 3,00 g kreatin och 80 mg vitamin C per 4,1 g (underlag, inte infört). Påståendena om prestation och trötthet är borta. Typordet Kreatinkomplex är live-ordet. Rättning: tillverkaren anger '250 ml vatten eller juice' och live-källan '200 ml vatten'. Vattenmängden motsäger sig och stryks (R2, praxis 30019).

- `meta` före: `en portion är 4,1 g i 200 ml vatten.`
  efter: `en portion är 4,1 g (1 skopa).`

- `html` före: `som löses upp i 200 ml vatten.</p>`
  efter: `som löses upp i vatten.</p>`

- `html` före: `<li>Portion: 4,1 g (1 skopa) i 200 ml vatten</li>`
  efter: `<li>Portion: 4,1 g (1 skopa) i vatten</li>`


## 30032 (10472301789450, k_30d_utkast.json): GODKÄND

Live: en variant, 129 kr, SKU = EAN 5902114040130. Tillverkaren (https://trecnutrition.com/brands/trec/endurance/creatine-sport/; utkastets adress under trec-core är fel) bekräftar 300 g, smaken Raspberry, 5 g (1 skopa) i 250 ml med shaker eller mixer och tiderna. Per 5 g anges 3000 mg kreatinmonohydrat, 1000 mg dextros och 250 mg taurin, vilket stämmer med 60, 20 och 5 %. Kreatinkomplex är en entydig översättning av 'Creatine complex' och butikens live-ord (R7). 'Högkvalitativt' och 'uthållighetssporter' är borta. Varningen återges som källan.


## 30033 (10472301887754, k_30d_utkast.json): RÄTTA

Live: en variant, 179 kr, SKU = EAN 5902114018986. Kapslar mot pulver är löst. Tillverkaren har en egen pulversida (https://trecnutrition.com/brands/trec/trec-core/crea-xtreme-powder/) med 180 g, smaken Watermelon, 3 g (0,5 skopa) i 300 ml, 2 portioner och 6 g per dag. Den stämmer med live-källan. Kapselsidan som utkastaren hittade gäller en annan förpackning. Prestationspåståendena och 'biotillgänglighet' är borta, och 'Kreatinhypersmältning' är rätt utelämnat. Underlag (inte infört): 3696 mg kreatin per 6 g. Rättning: tillverkaren anger fyra kreatinformer (även trikreatinmalat), medan live-källan anger tre. Antalet 'tre' stryks i meta, första meningen och Passar för (R2). Ämnena från den egna ingredienslistan står kvar.

- `meta` före: `Trec Crea Xtreme innehåller tre former av kreatin: monohydrat, hydroklorid och citrat. Burken rymmer 180 g pulver med smak av vattenmelon.`
  efter: `Kreatinpulvret Trec Crea Xtreme innehåller kreatinmonohydrat, kreatinhydroklorid och kreatincitrat. Burken rymmer 180 g med smak av vattenmelon.`

- `html` före: `<p>Trec Crea Xtreme innehåller tre former av kreatin, kreatinmonohydrat, kreatinhydroklorid och kreatincitrat, i pulverform.`
  efter: `<p>Trec Crea Xtreme innehåller kreatinmonohydrat, kreatinhydroklorid och kreatincitrat i pulverform.`

- `html` före: `<li>Dig som vill ta kreatin i pulverform med tre kreatinformer</li>`
  efter: `<li>Dig som vill ta kreatin i pulverform</li>`


## 30035 (10472301986058, k_30d_utkast.json): GODKÄND

Live: en variant, 209 kr, SKU = EAN 5902114044671. Utkastet säger att tillverkarsida saknas, men trecnutrition.com har CM3 1250 (https://trecnutrition.com/brands/trec/trec-core/cm3-1250/) med 180 kapslar, 3 kapslar med cirka 300 ml och 2 portioner per dag (6 kapslar). Det stämmer med texten. Sidans tabell 'per 4 capsules' motsäger dagsdosen 6 och används inte. Alla påståenden om ATP, muskler, återhämtning och 'sur miljö' är borta. Typordet Kreatinkomplex är live-ordet. SEO-titeln 'Kreatinkomplex Trec CM3 Kapslar' är unik mot 30001 ('... Pulver Ananas').


## 30036 (10472302084362, k_30d_utkast.json): RÄTTA

Live: en variant, 639 kr, SKU = EAN 5902114046217. Tillverkaren (https://trecnutrition.com/brands/trec/trec-core/isolate-100/) bekräftar 700 g, smaken Creamy-blueberry, 30 g (1,5 skopa) i 200 ml och 90 g per dag. BV 159, 'snabb absorption', muskelpåståendet och 'fett- och sockerfritt' är borta. Typordet Proteinisolat rättar live-ordets felstavning 'Proteinisolaat' (R7). Den tomma vilodagsraden och den obegripliga varningsmeningen är rätt utelämnade (R2). Mjölk är den enda allergenen enligt listan. Underlag: 77 g protein per 90 g. Rättning: Obs-raden sa att produkten 'ska inte överskrida' mängden; det skrivs om.

- `html` före: `och den ska inte överskrida den rekommenderade dagliga mängden.`
  efter: `och den rekommenderade dagliga mängden ska inte överskridas.`


## 30037 (10472302149898, k_30d_utkast.json): RÄTTA

Live: en variant, 369 kr, SKU = EAN 5902114019853. Tillverkaren (https://trecnutrition.com/brands/trec/trec-core/whey-100-new-formula/) bekräftar 700 g, Creamy strawberry, 30 g (2 skopor) i 200 ml och 3 portioner per dag. Rättningar: 'med tillsatt kalcium, zink, vitamin B6 och vitamin D' och 'Tillsatta vitaminer och mineraler' är formuleringen av näringspåståendet 'Med tillsatt [näringsämne]' enligt bilagan till 1924/2006. Enligt Davids linje stryks det och ersätts med en uppräkning av innehållet. Mängderna per 90 g (198 mg kalcium, 2,52 mg zink, 0,36 mg B6, 1,35 µg D) är underlag för senare. Obs-raden skrivs om som i 30036.

- `html` före: `och den ska inte överskrida den rekommenderade dagliga mängden.`
  efter: `och den rekommenderade dagliga mängden ska inte överskridas.`

- `html` före: `innehåller vassleproteinkoncentrat (WPC) med tillsatt kalcium, zink, vitamin B6 och vitamin D, i ett pulver med jordgubbssmak.`
  efter: `innehåller vassleproteinkoncentrat (WPC), kalcium, zink, vitamin B6 och vitamin D i ett pulver med jordgubbssmak.`

- `html` före: `<li>Tillsatta vitaminer och mineraler: Kalcium, zink, vitamin B6 och vitamin D</li>`
  efter: `<li>Vitaminer och mineraler: Kalcium, zink, vitamin B6 och vitamin D</li>`

- `meta` före: `innehåller vassleproteinkoncentrat med tillsatt kalcium, zink, vitamin B6 och vitamin D.`
  efter: `innehåller vassleproteinkoncentrat, kalcium, zink, vitamin B6 och vitamin D.`


## 30038 (10472302346506, k_30d_utkast.json): GODKÄND

Live: en variant, 519 kr, SKU = EAN 5902114044541. Ingredienserna, 30 g i 200 ml, 3 portioner och tiderna stämmer. Påståendena om muskelmassa, 'snabbt upptag' och 'högkvalitativt' är borta. Smaken Saltkaramell står bara i live-titeln. Tillverkaren (https://trecnutrition.com/brands/trec/trec-core/whey-100/) listar 900 g men bara 'Chocolate Salted Caramel'. Kakaopulvret i listan talar för samma smak, men det är inte entydigt, så live-titeln får gälla och ingen webbfakta förs in (rätt bedömt). Att notera för butiken: smaknamnet kan behöva kontrolleras mot förpackningen.


## 30040 (10472350187786, k_30d_utkast.json): GODKÄND

Live: en variant, 1789 kr, SKU 20898, EAN 5902114045739. Koncentrat mot isolat är rätt hanterat. Löptexten och tillverkaren (https://trecnutrition.com/brands/trec/trec-core/whey-100/: 85,19 g vassleproteinkoncentrat per 90 g, 2000 g, Vanilla) anger koncentrat, men live-källans ingredienslista är Isolate 100:s ('91,7 % CFM vassleproteinisolat'). Ingredienslistan är därför utelämnad och proteinkällan skriven neutralt som 'vassleprotein (från mjölk)' (R2). Tillverkarens uppgift skulle kunna föras in enligt v1.6, men den egna källan säger emot, så den neutrala formen är säkrast. 30 g i 200 ml, 3 portioner och tiderna stämmer. Påståendena om muskelmassa och upptag är borta.
