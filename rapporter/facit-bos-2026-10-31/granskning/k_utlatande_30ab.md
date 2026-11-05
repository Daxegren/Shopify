# Granskningsutlåtande k_30a och k_30b (BEST OF SPORTS, kosttillskott Trec), 2026-11-05

Granskaren är Opus och har bara läst. Underlaget är `vag2_skriv/k_30a_utkast.json` (30001–30010) och `vag2_skriv/k_30b_utkast.json` (30011–30019). Källtext, varianter (pris, SKU, EAN) och taggar lästes live via Admin API 2026-11-05, och butiken bekräftades som BEST OF SPORTS. Ingenting skrevs i Shopify. Regler: regler-v1.md v1.4–v1.8, BESLUTSLOGG 2026-11-05 (kosttillskott: fakta och användning nu, påståenden först när etikettens mängder och svensk registerlydelse är bekräftade) och exempeltexterna i `rapporter/kosttillskott-exempel-2026-11-05.md`.

**Resultat:** 0 GODKÄND, 19 RÄTTA, 0 UNDERKÄND. På rättade kopior gav `skrivfil_kontroll.py` 0 fel och 0 varningar; före rättning gav den 10 varningar om cirkulär inledning. `kontrollera_produkttext.py --seo-title-max 43 --meta-min 70` gav 43 'halsa'-fel. Alla gäller produktnamn och typord (Kreatin, Protein, Vitamin, Aminosyr, Energi) och är bedömda manuellt som falsklarm. Varje 'före' förekommer exakt en gång i sitt fält.

**Genomgående:**
- **Inga påståenden har smugit in.** Jag sökte i titel, SEO-titel, meta och html efter skydd, stöd, förbättr, bygg, snabb, minsk, fett, immun, energi, återhämt, antioxid, rik på, högt protein, tillsatt socker, ök, bidra, hjälp, hälsa, effekt, prestation, muskel, metabol, kvalitet och optimal. Träffarna är ingrediensnamn (fettsyror, klumpförebyggande medel), förvaringsrader ('skydda mot ljus'), produktnamn (Energigel, Fettsyra) och 'naturligt förekommande sockerarter' som fakta. Inget påstående enligt 1924/2006 finns kvar.
- **Varningsraden** återges i alla 19 som i källan: ej för barn, gravida och ammande, överskrid inte dosen och ersätter inte varierad kost, där källan har det. Där källan saknar raderna (30007, 30011, 30012) har de rätt inte lagts till. I två fall stryks en tolkning eller motsägelse (30007 '3 kapslar', 30016 'högst').
- **Allergener** följer bara ingredienslistan. Den generella raden 'kan innehålla mjölk, soja, vete ...' är utelämnad i alla texter.
- **Trasiga källrader** hanteras utan gissning: 30003 (tiamin, inbäddad bildtagg), 30011 (hakparenteser), 30013 (raden 'L-C L-Kalcium ...'), 30016 (hakparentes) och 30017 ('300 mg per dag'). För 30013 och 30017 bekräftar tillverkarens sida dagsdosen.
- **Titlar** låser ingen variant. Alla 19 har en variant (Default Title), och smak och vikt kommer ur live-titeln.
- **Typord:** Kreatin (30010, 30014), Viktökare (30015), Alfa-liponsyra (30017), Proteinbar (30011, 30012) och Vitamin- och mineralkomplex (30003) står i produktens egen källtext eller i live-titeln (R7). Live-orden 'Antioxidant' (30007, 30017) och 'Ultrarena' (30006) är rätt bortvalda.
- **Meta och första meningen:** alla tio i k_30a började 'Namn är ett typord' (skriptvarning), och 30013 hade samma form utan att skriptet varnade. Sju metatexter i k_30b saknade verb. Alla är omskrivna.
- **Faktakoll mot tillverkaren:** www.trec.com svarar med ett certifikat för en annan värd och tillhör inte tillverkaren. Kontrollen gjordes därför på trecnutrition.com (Trec Nutrition Sp. z o.o., Gdynia). Sidorna visar inte EAN eller SKU, så produkterna matchas på namn, förpackning och smak. Nya uppgifter: 60 mg Q10 per dagsdos (30007), dagsdos 1 g (30013) och 'Multivitamin' som smak (30018). Två motsägelser hittades: BCAA-förhållandet i 30019 och isomaltos i 30018. Underlag för senare påståenden (inte infört): kreatin per dagsdos är 4988 mg för CM3 (30001), 5 g för Magnum (30016) och 4166 mg per 6 kapslar för Micronized (30010, där sidan bara visar förpackningen med 400 kapslar). Omega 3 + D3 (30008) har 2000 IE per kapsel.
- **Leveranstid:** ingen produkt har taggen 'På beställning', och inget utkast har leveranstidsmeningen. Det är rätt.

**Beslut för David:** (1) 30003 innehåller ginseng- och citrusbioflavonoidextrakt. Min rekommendation är att skriva den som vitamin- och mineralpreparat utan påståenden; alternativet är att hålla den utanför enligt växtextraktsspärren. (2) 30015: typordet 'Viktökare' kan läsas som en effekt på vikten. Min rekommendation är att behålla källans ord. (3) 30019 avviker från exempeltexten 29003 eftersom förhållandet 2:1:1 stryks.

## 30001 (10411931074826, k_30a_utkast.json): RÄTTA

Live: en variant (Default Title), 209 kr, SKU = EAN 5902114017736. Typordet Kreatinkomplex är live-ordet. Ananas står bara i live-titeln; tillverkarens sida (https://trecnutrition.com/brands/trec/trec-core/cm3-powder/) listar 250 g och smaken Pineapple, så smaken stämmer. Dos 7 g, portion 3,5 g (0,5 skopa) i 250–300 ml och tiderna för tränings- och vilodagar stämmer mot källan och tillverkaren. Obs-raden återger källans varning (allergi, barn, gravida och ammande, dagsdos, varierad kost). Allergenraden 'kan innehålla mjölk, soja ...' är rätt utelämnad. Inga påståenden: 'förbättrar prestationen', 'resistent mot magsyra' och 'förhindra gaser' är borta. 'Vattenlösligt' och 'bunden till äppelsyra' är egenskaper som står i källan. Underlag för senare: tillverkaren anger 4988 mg kreatin per 7 g, alltså över villkoret 3 g, men svensk registerlydelse är inte verifierad, så inget påstående förs in. Rättning: metan och första meningen hade den cirkulära inledningen 'Namn är ett typord' (skriptvarning).

- `meta` före: `Trec CM3 är ett kreatinpulver med trikreatinmalat och smak av ananas. Burken innehåller 250 g och en portion är 3,5 g som rörs ut i vatten.`
  efter: `Kreatinpulvret Trec CM3 innehåller trikreatinmalat och har smak av ananas. Burken rymmer 250 g och en portion är 3,5 g som rörs ut i vatten.`
- `html` före: `<p>Trec CM3 är ett smaksatt, vattenlösligt kreatinpulver med trikreatinmalat, en kreatinform som är bunden till äppelsyra.`
  efter: `<p>Trec CM3 innehåller trikreatinmalat, en kreatinform som är bunden till äppelsyra, i ett smaksatt och vattenlösligt pulver.`

## 30002 (10462790844682, k_30a_utkast.json): RÄTTA

Live: en variant, 79 kr, SKU 10682, EAN 5902114018016. Produkten finns inte på trecnutrition.com och kunde inte jämföras där. Typordet Vitaminkomplex är live-ordet. Ingredienslistan och doseringen (1 kapsel med eller efter måltid, minst 300 ml vatten) stämmer ordagrant. Obs-raden stämmer med källan. Alla påståenden om energiproduktion, nervsystemet och immunsystemet är borta. 'Vitamin B4 (kolin)' står så i källan och får stå kvar. Om beteckningen ska ändras avgörs mot förpackningen, inte här. Rättning: metan och första meningen hade cirkulär inledning.

- `meta` före: `Trec Vitamin B Complex är ett vitaminkomplex med B-vitaminer, inositol, aminobensoesyra och kolin i 60 kapslar. Dosen är 1 kapsel per dag.`
  efter: `Trec Vitamin B Complex innehåller B-vitaminer, inositol, aminobensoesyra och kolin i 60 kapslar. Dosen är 1 kapsel per dag med minst 300 ml vatten.`
- `html` före: `<p>Trec Vitamin B Complex är ett kosttillskott med B-vitaminer, inositol, aminobensoesyra och kolin i kapselform.`
  efter: `<p>Trec Vitamin B Complex innehåller B-vitaminer, inositol, aminobensoesyra och kolin i kapselform.`

## 30003 (10470937755914, k_30a_utkast.json): RÄTTA

Live: en variant, 129 kr, EAN 5902114011758. Typordet 'Vitamin- och mineralkomplex' är motiverat enligt R7. Källan själv säger 'komplex av vitaminer, mineraler', och live-ordet 'Mineral komplex' stämmer inte med innehållet. Tiamin: i källan är 'tiaminmononitr<img>at' trasigt av en inbäddad bildtagg. Utkastet skriver bara 'tiamin', vilket är den entydiga delen, och gissar inte (R2). Etiketten 'metabolismaktivatorer' är rätt utelämnad. Texten nämner ginseng- och citrusbioflavonoidextrakt bara som ingredienser, utan något påstående. 'Ökar behovet', 'lättassimilerade' och 'stress' är borta. Tillverkarens sida (https://trecnutrition.com/brands/trec/vitality-lifestyle/multipack/) bekräftar 120 kapslar, 2 kapslar per dag och 'högst 3 månader'. Den anger 200 mg koreansk ginsengextrakt och 50 mg extrakt av pomerans per dagsdos. Beslut för David: produkten innehåller växtextrakt utan godkända påståenden. Min bedömning är att den får skrivas, eftersom den är ett vitamin- och mineralpreparat och texten saknar påståenden. Vill David tillämpa spärren strikt ska den hållas utanför. Rättning: metan och första meningen hade cirkulär inledning.

- `meta` före: `Trec Multipack är ett kosttillskott med vitaminer, mineraler och ginsengextrakt i 120 kapslar. Dosen är 2 kapslar per dag, 1 kapsel två gånger dagligen.`
  efter: `Trec Multipack innehåller vitaminer, mineraler, ginsengextrakt och citrusbioflavonoidextrakt i 120 kapslar. Dosen är 1 kapsel två gånger dagligen.`
- `html` före: `<p>Trec Multipack är ett kosttillskott som innehåller vitaminer, mineraler och några övriga ämnen, bland annat koreansk ginsengextrakt och citrusbioflavonoidextrakt, i kapselform.`
  efter: `<p>Trec Multipack innehåller vitaminer, mineraler och några övriga ämnen, bland annat koreansk ginsengextrakt och citrusbioflavonoidextrakt, i kapselform.`

## 30004 (10470937985290, k_30a_utkast.json): RÄTTA

Live: en variant, 1819 kr, SKU 20875, EAN 5902114044992. Produkten finns inte på trecnutrition.com (Gold Core-linjen saknas där). Jordgubbssmak, 2000 g, de tre vassleproteinerna, 30 g i 200 ml och 60–90 g per dag stämmer. Källan anger bara tider för träningsdagar, och utkastet har bara den raden, vilket är rätt. 'Bred BCAA-aminosyraprofil med glutamin', 'fettförbränning', 'minskar aptiten' och liknande är borta. Allergenraden är utelämnad, och mjölk syns i ingredienslistan. Rättning: metan och första meningen hade cirkulär inledning.

- `meta` före: `Trec Gold Core Line Whey 100 är ett proteinpulver med jordgubbssmak och tre vassleproteiner. Burken innehåller 2000 g och en portion är 30 g.`
  efter: `Proteinpulvret Trec Gold Core Line Whey 100 innehåller tre vassleproteiner och har jordgubbssmak. Burken rymmer 2000 g och en portion är 30 g.`
- `html` före: `<p>Trec Gold Core Line Whey 100 är ett proteinpulver med smak av jordgubbar som innehåller vassleproteinkoncentrat, vassleproteinisolat och vassleproteinhydrolysat.`
  efter: `<p>Trec Gold Core Line Whey 100 innehåller vassleproteinkoncentrat, vassleproteinisolat och vassleproteinhydrolysat och har smak av jordgubbar.`

## 30005 (10470943293706, k_30a_utkast.json): RÄTTA

Live: en variant, 129 kr, SKU 21764, EAN 5902114047665. Essensey finns inte på trecnutrition.com. '2000 IE D3' är en del av produktnamnet i live-titeln och får stå i titeln. Texten anger ingen mängd vitamin D per kapsel, vilket är rätt eftersom källan inte gör det. '1000 mg fiskolja per portion' står en gång 'enligt tillverkaren'. Typordet Fettsyra är live-ordet. Påståendena 'rik på omega-3', 'positiv effekt på immunitet', 'sänka triglycerider' och 'skydda synen' är borta. Obs-raden stämmer med källan. Rättning: metan och första meningen hade cirkulär inledning.

- `meta` före: `Trec Essensey Omega 3 + 2000 IE D3 är ett kosttillskott med fiskolja (18 % EPA, 12 % DHA) och vitamin D3. Förpackningen har 90 kapslar.`
  efter: `Trec Essensey Omega 3 + 2000 IE D3 innehåller fiskolja (18 % EPA, 12 % DHA) och vitamin D3. Förpackningen har 90 kapslar och dosen är 1 kapsel dagligen.`
- `html` före: `<p>Trec Essensey Omega 3 + 2000 IE D3 är ett kosttillskott som innehåller fiskolja med omega-3-fettsyrorna EPA och DHA samt vitamin D3.`
  efter: `<p>Trec Essensey Omega 3 + 2000 IE D3 innehåller fiskolja med omega-3-fettsyrorna EPA och DHA samt vitamin D3.`

## 30006 (10470943555850, k_30a_utkast.json): RÄTTA

Live: en variant, 429 kr, EAN 5902114017385. Tillverkarens sida (https://trecnutrition.com/brands/trec/trec-core/aminomax-6800/) bekräftar 320 kapslar, 8 kapslar per dag, '8 efter träning' och '4 två gånger 30 min före måltid'. 'Ultrarena' står bara i live-titeln och är rätt utelämnat ur typordet (R5/R7). 'Snabbt återställa', 'ideala aminogram' och 'bidrar till effektiv användning' är borta. Rättning: metan och första meningen hade cirkulär inledning.

- `meta` före: `Trec AminoMax 6800 är ett kosttillskott med vassleproteinhydrolysat, L-glutamin, taurin, vitamin C och B6 i 320 kapslar. Dagsdosen är 8 kapslar.`
  efter: `Trec AminoMax 6800 innehåller vassleproteinhydrolysat, L-glutamin, taurin, vitamin C och B6 i 320 kapslar. Dagsdosen är 8 kapslar.`
- `html` före: `<p>Trec AminoMax 6800 är ett kosttillskott med aminosyror och mikropeptider från hydrolysat av vassleproteinkoncentrat, med tillsats av L-glutamin och taurin samt vitamin C och B6.`
  efter: `<p>Trec AminoMax 6800 innehåller aminosyror och mikropeptider från hydrolysat av vassleproteinkoncentrat, med tillsats av L-glutamin och taurin samt vitamin C och B6.`

## 30007 (10470943916298, k_30a_utkast.json): RÄTTA

Live: en variant, 149 kr, EAN 5902114019013. Källan är tunn men har fler än två entydiga fakta: 90 kapslar, 2 kapslar per dag, 1 kapsel två gånger dagligen med 300 ml vatten efter måltid, och att burken ska användas inom tre månader efter öppnandet (R3 uppfyllt). Typordet Kosttillskott är motiverat. Live-ordet 'Antioxidant' kan läsas som ett påstående, och tillverkaren kallar själv produkten 'Food supplement'. Faktakoll enligt v1.6: tillverkarens sida (https://trecnutrition.com/brands/trec/vitality-lifestyle/coenzyme-q10/) gäller exakt Coenzyme Q10 i 90 kapslar och anger 60 mg coenzym Q10 per 2 kapslar (dagsdos). Raden läggs till. Sidan visar inget EAN, så produkten matchas på namn och förpackningsstorlek. Obs-raden: källan säger både 'överskrid inte den dagliga normen' (2 kapslar) och 'överskrid inte 3 kapslar per dag'. Uppgifterna motsäger varandra, så 3-kapselsmeningen stryks (R2). Raderna om barn och gravida och om varierad kost saknas i källan och har rätt inte lagts till. Rättningar: meta, första meningen, Obs-raden och en ny innehållsrad.

- `meta` före: `Trec Coenzyme Q10 är ett kosttillskott med coenzym Q10 i 90 kapslar. Dosen är 1 kapsel två gånger dagligen med 300 ml vatten, helst efter måltid.`
  efter: `Trec Coenzyme Q10 innehåller coenzym Q10 i 90 kapslar. Dosen är 1 kapsel två gånger dagligen med 300 ml vatten, helst efter måltid.`
- `html` före: `<p>Trec Coenzyme Q10 är ett kosttillskott med coenzym Q10 i kapselform.`
  efter: `<p>Trec Coenzyme Q10 innehåller coenzym Q10 i kapselform.`
- `html` före: `Obs: Enligt tillverkaren: Överskrid inte den dagliga normen. Överskrid inte det dagliga intaget av 3 kapslar per dag.`
  efter: `Obs: Enligt tillverkaren ska den dagliga dosen inte överskridas.`
- `html` före: `<li>Förpackning: 90 kapslar</li>\n`
  efter: `<li>Förpackning: 90 kapslar</li>\n<li>Innehåll per dagsdos (2 kapslar): 60 mg coenzym Q10</li>\n`

## 30008 (10470949880074, k_30a_utkast.json): RÄTTA

Live: en variant, 119 kr, SKU 13351, EAN 5902114040574. Texten är densamma som exempeltexten 29004 och stämmer med live-källan. Påståendena om hjärta, ögonhälsa och immunsystem är borta. Obs-raden stämmer. Notering för underlaget (inte kundtext): tillverkarens sida för Omega 3 + D3, 90 kapslar (https://trecnutrition.com/brands/trec/vitality-lifestyle/omega-3-d3-2/) anger 50 µg (2000 IE) vitamin D och 180 mg EPA plus 120 mg DHA per kapsel. Påståendet i att_bekrafta att 2000 IE bara gäller Essensey stämmer alltså inte. Påståendena ska ändå vänta på verifierad svensk registerlydelse. Rättning: metan och första meningen hade cirkulär inledning. Texten i övrigt är oförändrad från exemplet.

- `meta` före: `Trec Omega 3 + D3 är ett kosttillskott med fiskolja (18 % EPA, 12 % DHA) och vitamin D3. Förpackningen har 90 kapslar, dosen är 1 kapsel dagligen.`
  efter: `Trec Omega 3 + D3 innehåller fiskolja (18 % EPA, 12 % DHA) och vitamin D3. Förpackningen har 90 kapslar, dosen är 1 kapsel dagligen.`
- `html` före: `<p>Trec Omega 3 + D3 är ett kosttillskott som innehåller fiskolja med omega-3-fettsyrorna EPA och DHA samt vitamin D3.`
  efter: `<p>Trec Omega 3 + D3 innehåller fiskolja med omega-3-fettsyrorna EPA och DHA samt vitamin D3.`

## 30009 (10470974980362, k_30a_utkast.json): RÄTTA

Live: en variant, 529 kr, SKU 4396, EAN 5902114010966. Texten är densamma som exempeltexten 29001. Choklad, 900 g, 30 g i 200 ml, 60–90 g per dag och ingredienserna stämmer med live-källan. 'Snabb återhämtning', 'stödja metaboliska processer' och 'bekämpa övervikt' är borta. Rättning: metan och första meningen hade cirkulär inledning.

- `meta` före: `Trec Gold Core Whey 100 är ett proteinpulver med chokladsmak och vassleproteinkoncentrat. Portionen är 30 g och rörs ut i 200 ml vatten eller mjölk.`
  efter: `Proteinpulvret Trec Gold Core Whey 100 har chokladsmak och innehåller vassleproteinkoncentrat. En portion är 30 g i 200 ml vatten eller mjölk.`
- `html` före: `<p>Trec Gold Core Whey 100 är ett proteinpulver med chokladsmak som innehåller vassleproteinkoncentrat.`
  efter: `<p>Trec Gold Core Whey 100 innehåller vassleproteinkoncentrat och har chokladsmak.`

## 30010 (10471010369802, k_30a_utkast.json): RÄTTA

Live: en variant, 129 kr, SKU 17839, EAN 5902114043995. Texten är densamma som exempeltexten 29002. 120 kapslar, 6 kapslar per dag och 3 kapslar två gånger dagligen med 300 ml stämmer, liksom tiderna för tränings- och vilodagar. Azorubinvarningen är rätt utelämnad, eftersom ingredienslistan saknar azorubin. Underlag: tillverkaren (https://trecnutrition.com/brands/trec/trec-core/creatine-micronized-200-mesh/) anger 4166 mg kreatin per 6 kapslar. Sidan listar bara förpackningen med 400 kapslar och gäller därför inte entydigt 120 kapslar. Inget påstående förs in. Rättning: metan och första meningen hade cirkulär inledning.

- `meta` före: `Trec Creatine Micronized 200 Mesh är ett kreatintillskott med mikroniserat kreatinmonohydrat i 120 kapslar. Enligt tillverkaren är en portion 3 kapslar.`
  efter: `Trec Creatine Micronized 200 Mesh innehåller mikroniserat kreatinmonohydrat i 120 kapslar. Enligt tillverkaren är en portion 3 kapslar.`
- `html` före: `<p>Trec Creatine Micronized 200 Mesh är ett kosttillskott som innehåller mikroniserat kreatinmonohydrat i kapslar.`
  efter: `<p>Trec Creatine Micronized 200 Mesh innehåller mikroniserat kreatinmonohydrat i kapslar.`

## 30011 (10471010861322, k_30b_utkast.json): RÄTTA

Live: en variant, 29 kr, EAN 5902114048945. Ingredienslistan i källan har obalanserade hakparenteser. Utkastet återger inte hela listan, bara entydiga delar, och gissar inte (R2). Allergenraden ('mjölk, soja (sojalecitin) och nötsmör (hasselnötter, jordnötter)') följer bara ingredienslistan. Raden 'kan innehålla gluten, nötter, ägg och soja' i varningen är utelämnad enligt linjen. 'Högt proteininnehåll', 'utan tillsatt socker' och 'hälsosammare alternativ' är borta. 'Innehåller naturligt förekommande sockerarter' återges som fakta, utan påståendet om tillsatt socker. Typordet Proteinbar står i källtexten. Rättning: metan saknade verb.

- `meta` före: `Proteinbar på mjölkchoklad med vaniljsmakande och karamellsmakande innehåll från Trec. Baren väger 49 g och är sötad med sötningsmedel.`
  efter: `Proteinbaren Trec Vanilla och Caramel är gjord på mjölkchoklad med vanilj- och karamellsmakande innehåll. Den väger 49 g och är sötad med sötningsmedel.`

## 30012 (10471138951434, k_30b_utkast.json): RÄTTA

Live: en variant, 29 kr, SKU = EAN 5902114048938. Ingredienslistan är hel i den här källan och återges komplett. Allergenerna syns i listan, och ingen extra allergenrad är skriven. 'Palmefett' är rättat till 'palmfett', vilket är en ren stavningsrättelse. Påståendena är borta. Obs-raden återger diarrévarningen, som är källans enda varning. Rättning: metan saknade verb.

- `meta` före: `Proteinbar på mjölkchoklad med rostade kokosflingor och karamellsmakande innehåll från Trec. Baren väger 48 g och är sötad med sötningsmedel.`
  efter: `Proteinbaren Trec Kokos och Karamell är gjord på mjölkchoklad med rostade kokosflingor och karamellsmakande innehåll. Den väger 48 g.`

## 30013 (10471171227914, k_30b_utkast.json): RÄTTA

Live: en variant, 119 kr, SKU = EAN 5902114017552. Den trasiga raden 'L-C L-Kalcium L-Cosin ... 1 gram' är rätt utelämnad (R2). 'C-vitamin bidrar till immunsystemet' är borta. Faktakoll enligt v1.6: tillverkarens sida (https://trecnutrition.com/brands/trec/trec-core/vit-c-l-lysine-powder/) gäller exakt Vit. C + L-Lysine Powder 300 g och anger 'Recommended daily portion is 1 g' (800 mg vitamin C och 200 mg L-lysin HCl). Dagsdosen läggs därför till. Den trasiga raden tolkas inte. Varningen om över 500 mg C-vitamin och njursten återges ordagrant och gäller produkten. Typordet Vitaminpulver är live-ordet. Rättningar: meta (cirkulär inledning, missad av skriptet) och en ny rad med dagsdos.

- `meta` före: `Trec Vit. C + L-Lysin är ett vitaminpulver med C-vitamin (L-askorbinsyra) och L-lysin. Burken innehåller 300 g och en portion är 1 g.`
  efter: `Trec Vit. C + L-Lysin innehåller C-vitamin (L-askorbinsyra) och L-lysin i pulverform. Burken rymmer 300 g och en portion är 1 g.`
- `html` före: `<li>Portion: 1 g (1 skopa)`
  efter: `<li>Rekommenderad daglig dos: 1 g</li>\n<li>Portion: 1 g (1 skopa)`

## 30014 (10471172112650, k_30b_utkast.json): RÄTTA

Live: en variant, 129 kr, SKU = EAN 5902114044954. Ingredienserna (76 % kreatinmonohydrat, 22 % natriumcitrat och 2 % C-vitamin), 5 g per dag och tiderna stämmer. Typordet Kreatin är motiverat enligt R7. Källan säger 'kreatinmonohydratpulver', och live-ordet 'Creatine complex' är engelska. 'Förbättrar prestationen' och 'fördelarna märks' är borta. Underlaget i att_bekrafta stämmer (3,8 g kreatinmonohydrat per dag). Rättning: metan saknade verb.

- `meta` före: `Kreatinpulver från Trec med kreatinmonohydrat, natriumcitrat och C-vitamin. Burken innehåller 300 g och en portion är 5 g.`
  efter: `Trec Creatine+ innehåller kreatinmonohydrat, natriumcitrat och C-vitamin i pulverform. Burken rymmer 300 g och en portion är 5 g.`

## 30015 (10472267972874, k_30b_utkast.json): RÄTTA

Live: en variant, 239 kr, SKU 354, EAN 5901828341564. Tillverkaren (https://trecnutrition.com/brands/trec/trec-core/mass-xxl/) kallar produkten 'gainer' och listar 1000 g och smaken choklad. 70 g (3 skopor), 4 portioner och 280 g per dag stämmer. Allergenerna mjölk och korn följer ingredienslistan. Påståendena om muskelmassa och B6 är borta. Typordet Viktökare står i källtexten ('chokladsmakande viktökare') och följer R7. Ordet beskriver vad produkten är, men det kan läsas som en effekt på vikten. Beslut för David: behålla 'Viktökare' (min rekommendation, eftersom det är vedertaget kategoriord och källans ord) eller byta till ett neutralt ord. Rättning: metan saknade verb.

- `meta` före: `Chokladsmakande viktökare från Trec med vassleproteinkoncentrat och kolhydrater. Burken innehåller 1000 g och en portion är 70 g.`
  efter: `Viktökaren Trec Mass XXL har chokladsmak och innehåller vassleproteinkoncentrat och kolhydrater. Burken rymmer 1000 g och en portion är 70 g.`

## 30016 (10472268431626, k_30b_utkast.json): RÄTTA

Live: en variant, 199 kr, SKU 866, EAN 5901828345470. Ingredienslistan har en hakparentes som inte stängs efter 'Multi CARB Matrix'. Utkastet räknar upp de entydiga ingredienserna som 'urval' utan grupper och gissar inte (R2). Allergenerna mjölk och korn följer listan. 'Världens mest potenta', 'säkerställer snabb viktuppgång' och 'optimal uppsättning' är borta. Tillverkaren (https://trecnutrition.com/brands/trec/trec-core/magnum-8000/) bekräftar 1000 g, banan, 75 g (2,5 skopor) i 250 ml och 2 portioner. Typordet Näringskoncentrat är live-ordet. Rättningar: metan saknade verb. I Obs-raden stryks 'ska högst 2 portioner användas per dag', eftersom källan säger 'Använd 2 portioner per dag' och 'högst' är en tolkning.

- `meta` före: `Protein-kolhydrattillskott från Trec med banansmak, kreatin och MCT-olja. Burken innehåller 1000 g och en portion är 75 g.`
  efter: `Trec Magnum 8000 innehåller protein, kolhydrater, kreatin och MCT-olja och har banansmak. Burken rymmer 1000 g och en portion är 75 g.`
- `html` före: `Enligt tillverkaren ska högst 2 portioner användas per dag. Produkten är inte avsedd`
  efter: `Enligt tillverkaren är produkten inte avsedd`

## 30017 (10472268923146, k_30b_utkast.json): RÄTTA

Live: en variant, 109 kr, SKU 10135, EAN 5902114017101. 250 mg alfa-liponsyra per kapsel, 60 kapslar och 1 kapsel två gånger dagligen stämmer. Den lösa raden '300 mg per dag' i varningen är rätt utelämnad (R2). Tillverkaren (https://trecnutrition.com/brands/trec/vitality-lifestyle/ala-250/) anger 500 mg per 2 kapslar som dagsdos, så doseringen i utkastet stämmer, och raden med 300 mg är fel i källan. Typordet Alfa-liponsyra är motiverat enligt R7. Källan använder ordet, live-ordet 'Antioxidant' är ett egenskapsord som kan läsas som påstående, och liten bokstav efter bindestrecket är rätt. 'Höga antioxidantegenskaper' och 'neutraliserar fria radikaler' är borta. Rättning: metan saknade verb.

- `meta` före: `Kosttillskott från Trec med alfa-liponsyra i kapslar. Varje kapsel innehåller 250 mg alfa-liponsyra, förpackningen 60 kapslar.`
  efter: `Trec ALA 250 innehåller 250 mg alfa-liponsyra per kapsel. Förpackningen har 60 kapslar och dosen är 1 kapsel två gånger dagligen.`

## 30018 (10472269021450, k_30b_utkast.json): RÄTTA

Live: en variant, 29 kr, SKU 14483, EAN 5902114041731. Påståendena om B6 (trötthet) och magnesium (muskelfunktion, energiomsättning), samt 'professionell' och 'högkvalitativa', är borta. Typordet Energigel är live-ordet och produktens namn. 'Energi' är här kategoriord, inget påstående. Faktakoll (https://trecnutrition.com/brands/trec/endurance/energy-gel/): 'Multivitamin' är en av tre smaker (Orange, Multivitamin, Forest fruit). Ordet betyder alltså smak och inte vitamininnehåll, och därför läggs raden Smak: Multivitamin till, så att titeln inte kan läsas som ett vitaminpåstående. Källans 'isomaltos' är isomaltulos enligt tillverkaren ('Isomaltulose') och rättas. Obs-raden stämmer med källan. Rättningar: smakraden och isomaltulos.

- `html` före: `<li>Typ: Energigel</li>\n`
  efter: `<li>Typ: Energigel</li>\n<li>Smak: Multivitamin</li>\n`
- `html` före: `isomaltos`
  efter: `isomaltulos`

## 30019 (10472269218058, k_30b_utkast.json): RÄTTA

Live: en variant, 169 kr, SKU 10187, EAN 5902114017392. Förhållandet 2:1:1 i källan motsägs av tillverkaren (https://trecnutrition.com/brands/trec/trec-core/bcaa-g-force-1150/, förpackning 90 kapslar finns). Där anges per 12 kapslar L-leucin 6840 mg, L-valin 1920 mg och L-isoleucin 960 mg, alltså cirka 7:2:1. Förhållandet är inte entydigt och stryks i meta, första meningen och specifikationsraden (R2). Det avviker från exempeltexten 29003, som David har sett. Andelarna 60 % BCAA och 24 % glutamin stämmer med tillverkarens siffror (9720 mg och 3900 mg). 12 kapslar per dag och portionen 6 kapslar med 300 ml stämmer. 'Optimalt valt förhållande' är borta. 'Styrka, snabbhet eller uthållighet' beskriver målgruppen enligt källan. Rättningar: meta och html.

- `meta` före: `Aminosyrakomplex från Trec med L-leucin, L-isoleucin och L-valin i förhållandet 2:1:1. Förpackningen innehåller 90 kapslar.`
  efter: `Trec BCAA G-Force 1150 innehåller grenade aminosyror (L-leucin, L-isoleucin, L-valin) och L-glutamin. Förpackningen har 90 kapslar.`
- `html` före: ` i förhållandet 2:1:1. Förpackningen`
  efter: `. Förpackningen`
- `html` före: `<li>Förhållande leucin, isoleucin och valin: 2:1:1</li>\n`
  efter: (stryks)
