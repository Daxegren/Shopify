# Granskningsutlåtande k_28a och k_28b (BEST OF SPORTS), 2026-11-05

Granskaren är Opus och har bara läst. Underlaget är `vag2_skriv/k_28a_utkast.json` (9 produkter) och `vag2_skriv/k_28b_utkast.json` (5 produkter). Källtext, varianter (pris, SKU, färg) och taggar lästes live via Admin API 2026-11-05, och butiken bekräftades som BEST OF SPORTS. Ingenting skrevs i Shopify. Regler: regler-v1.md v1.4–v1.8 och BESLUTSLOGG 2026-11-05. Enligt loggen får barn- och ungdomsprodukter skrivas med bara fakta. Barnhjälmar, stolar och säten, bälten, babyprodukter och produkter med skyddsfunktion är fortfarande utanför.

**Resultat:** 4 GODKÄND, 10 RÄTTA, 0 UNDERKÄND. `skrivfil_kontroll.py` på en rättad kopia gav 0 fel och 0 varningar.

**Genomgående:**
- **Inget är underkänt på barnregeln.** Ringklockor (28012, 28013, 28015) är signalutrustning, inte skydd, och alla säkerhetspåståenden är utelämnade. Stödhjul, kedjeskydd, skjutstång och korg (28003, 28017, 28019) nämns bara som medföljande delar, utan påstående om skydd eller last. Kedjeskyddet gör inte cykeln till en skyddsprodukt. Stödhjulen säljs inte som en bärande del, och ingen lastgräns påstås. Enligt min tolkning gäller v1.7 inte här. Vill David ha det strängare, stryks de i 28003, 28017 och 28019.
- **Ålder och längd.** Ingen ålder skrivs. 14+ år i 28006 står bara i live-titeln och är utelämnat, vilket är tillåtet. Förar- eller åkarlängd står högst en gång per text 'enligt tillverkaren', och ingen text har mer än två sådana förekomster.
- **Skidor med flera varianter.** 28002 och 28011 har två längder (140 och 150) till samma pris och samma färg (eller ingen färg). Titlarna låser ingen längd (v1.8).
- **Färger.** Alla övriga har en variant, och färgen står i live-titeln eller källan. Bindestrecksfärger i titlar skrivs med versal efter bindestrecket, som i tidigare skrivna titlar ('Svart-Röd', 'Rosa-Lila'). Därför rättas Blå-vit, Blå-gul och Svart-turkos.
- **Hjulstorlek.** En hjulstorlek som bara står i live-titeln (14 och 27,5 tum) får stå i titeln men inte som specifikationsrad (praxis 8774).
- **Meta.** Sju metatexter inledde utan verb och rättas: 28003, 28004, 28005, 28007, 28012, 28013 och 28015.
- **Leveranstid.** Ingen produkt har taggen 'På beställning', och inget utkast har leveranstidsmeningen. Det är rätt.

## 28002 (10411721916682, k_28a_utkast.json): GODKÄND

Live: två varianter (140 / green och 150 / green), båda 2509 kr, med olika SKU. Enligt v1.8 skrivs produkten. Titel, SEO, meta och text låser ingen längd. Färgen utelämnas, vilket är tillåtet. Bredd 54-48-52 mm, polyeten, UL1, 838-1034 g per par, universal och NNN (NIS) står ordagrant. Fiskbensmönstret under foten står i källan; påståendena om glid och smörjning är rätt utelämnade, liksom längdrådet och märkeshistoriken. 'JR' finns bara i modellnamnet, och texten påstår inget om ålder, säkerhet eller utveckling. Kästle skrivs rätt med gemener (R8).


## 28003 (10411852333322, k_28a_utkast.json): RÄTTA

Live: en variant (Default Title), 6969 kr. Magnesiumram, aluminium i gaffel, fälgar och vevarmar, 22 cm, 95-110 cm (enligt tillverkaren en gång), 1 växel och V-bromsar stämmer. Stödhjul och kedjeskydd: källan säger bara 'Inkluderar stödhjul och kedjeskydd'. Utkastet anger dem som delar som följer med, utan påstående om skydd eller last. Ett kedjeskydd gör inte cykeln till en produkt med skyddsfunktion, och stödhjulen är en medföljande del, inte en bärande produkt med lastgräns. v1.7 gäller produkter som säljs som bärande delar och påståenden om last; så tolkar jag det. Rättningar: (1) 14 tum står bara i live-titeln. Enligt praxis (8774) får måttet stå i titeln men inte som specifikationsrad, så raden stryks. (2) Metan inleddes utan verb. (3) Färgen skrivs Blå-Vit i titel och SEO-titel, som Svart-Röd och Rosa-Lila i skrivna titlar. 'Ultralätt', 'maximal säkerhet', 'för pojkar' och 'Hjulvikt' är rätt utelämnade.

- `titel` före: `Blå-vit`
  efter: `Blå-Vit`
- `seo_title` före: `Blå-vit`
  efter: `Blå-Vit`
- `meta` före: `Barncykel med magnesiumram, 1 växel och V-bromsar. Tabou Rocket Lite MG har stödhjul och kedjeskydd som ingår.`
  efter: `Barncykeln Tabou Rocket Lite MG har magnesiumram, 1 växel och V-bromsar. Stödhjul och kedjeskydd ingår.`
- `html` före: `<li>Hjulstorlek: 14 tum</li>\n`
  efter: `(stryks)`

## 28004 (10411859181834, k_28a_utkast.json): RÄTTA

Live: en variant, 2289 kr. Höjd 82 cm, bas och klämma i aluminium, bromsar i stål och 88A stämmer. 'Maximal ryttarbelastning: 100 kg.' är en ren svensk rad med etikett och enhet och återges en gång enligt tillverkaren (R4). 'linser - järnstål', '100x24' och '48,5 cm bred lins' är rätt utelämnade (R2). SOKE får skrivas med versaler (beslut 2026-11-04). Rättningar: metan inleddes utan verb, och färgen skrivs Blå-Gul i titel och SEO-titel för enhetlighet. Målgruppen 'unga som börjar' är rätt utelämnad.

- `titel` före: `Blå-gul`
  efter: `Blå-Gul`
- `seo_title` före: `Blå-gul`
  efter: `Blå-Gul`
- `meta` före: `Blå-gul stuntscooter med aluminiumbas,`
  efter: `Den blå-gula stuntscootern SOKE GO har aluminiumbas,`

## 28005 (10411902402826, k_28a_utkast.json): RÄTTA

Live: en variant, 2969 kr, 'Färg: svart' ordagrant. 'Lämplig för ryttare som är 130-145 cm långa' återges som åkarlängd 130–145 cm enligt tillverkaren. Det är en ren återgivning utan tolkning. Lastkapacitet upp till 100 kg är en svensk rad med etikett och står enligt tillverkaren. Två förekomster är max och tillåtet (R5). Färdighetsnivå, plattform 490 x 118 mm i aluminium, IHC, 560/540 mm, ABEC-9, 110 mm och 3,38 kg stämmer. Typordet Kicksparkcykel kommer från live-titeln. Rättning: metan inleddes utan verb ('Svart sparkcykel med ...').

- `meta` före: `Svart sparkcykel med aluminiumplattform, IHC-styrsystem, ABEC-9-lager och 110 mm hjul. Versatyl Cosmopolitan V2 Pro väger 3,38 kg.`
  efter: `Sparkcykeln Versatyl Cosmopolitan V2 Pro har aluminiumplattform, IHC-styrsystem, ABEC-9-lager och 110 mm hjul. Den är svart och väger 3,38 kg.`

## 28006 (10439143981322, k_28a_utkast.json): RÄTTA

Live: en variant, 6259 kr. Aluminium, M (17 tum) för 150-165 cm (enligt tillverkaren en gång), Shimano Tourney, V-bromsar och fästpunkter stämmer. Åldern '14+ år' står bara i live-titeln och är utelämnad. Det är tillåtet och säkrast, eftersom åldern inte står i källtexten. 'Antal växlar: 12', 'Shimano Touring - 12 bromsok', 'Hjulvikt' och 'Stöd ingår' är rätt utelämnade (R2). Rättningar: (1) 27,5 tum står bara i live-titeln. Måttet får stå kvar i titel och SEO-titel (praxis 8774), men specifikationsraden och metameningen 'Hjulstorleken är 27,5 tum' stryks. (2) Färgen skrivs Svart-Turkos i titeln. Metan skrivs om så att den börjar med vad cykeln har.

- `titel` före: `Svart-turkos`
  efter: `Svart-Turkos`
- `meta` före: `Tabou Venom 1.0 W är en ungdomscykel med aluminiumram, Shimano Tourney-växel och V-bromsar. Hjulstorleken är 27,5 tum.`
  efter: `Ungdomscykeln Tabou Venom 1.0 W har aluminiumram, Shimano Tourney-växel, V-bromsar och fästpunkter för stänkskärmar.`
- `html` före: `<li>Hjulstorlek: 27,5 tum</li>\n`
  efter: `(stryks)`

## 28007 (10460946465034, k_28a_utkast.json): RÄTTA

Live: en variant, 8339 kr. ALUXX-aluminium, 27 cm för 130-150 cm (enligt tillverkaren en gång), 7 växlar och Giant Junior Sport 24 x 1,95 tum, 22 tpi stämmer. Ringklockan står i 'Inkluderar stöd, ringklocka och främre plattform' och nämns bara som medföljande. En ringklocka är ingen skyddsprodukt, och säkerhetspåståenden saknas. 'Stöd' och 'främre plattform' är rätt utelämnade. Det gäller också raderna med 130/150 och Touring samt 'självförtroende/utveckla terrängfärdigheter'. Dusty Blue är live-titelns färg (en variant). Rättning: metan inleddes utan verb.

- `meta` före: `Barncykel med ram av ALUXX-aluminium, 7 växlar och däck på 24 x 1,95 tum. Liv Tempt 24 har en ringklocka som ingår.`
  efter: `Barncykeln Liv Tempt 24 har ram av ALUXX-aluminium, 7 växlar och däck på 24 x 1,95 tum. En ringklocka ingår.`

## 28008 (10460950003978, k_28a_utkast.json): RÄTTA

Live: en variant, 2969 kr. Totalhöjd 630 mm, vikt 3,1440 kg (skrivs 3,144 kg), hjul 100 mm 88A, ABEC-9, IHC och 'Max. lastkapacitet: 100 kg' (en gång enligt tillverkaren) stämmer. Den trasiga raden '14,1495 kg - 120-120 cm Styrning: 400 x 420 mm, aluminium' delar ut en andra höjd (120-120 cm) direkt efter raden 'Användarhöjd: 100-120 cm'. Webbkoll: https://www.scootshop.net/union-lite-xs-scooter-lime/ (Union Lite XS) anger förarlängd 110–145 cm och styre 420 x 430 mm i stål. Användarhöjden är alltså inte entydig, och styrmåttet kommer ur den trasiga raden och motsägs på nätet. Båda specifikationsraderna stryks (R2). Övriga rader är rena i den egna källan och står kvar (R1). Kvalitetsorden och nybörjarorden är rätt utelämnade.

- `html` före: `<li>Användarhöjd enligt tillverkaren: 100–120 cm</li>\n`
  efter: `(stryks)`
- `html` före: `<li>Styrning: 400 x 420 mm, aluminium</li>\n`
  efter: `(stryks)`

## 28011 (10462231167242, k_28a_utkast.json): GODKÄND

Live: två varianter (150 och 140), båda 1929 kr, utan färg. Enligt v1.8 skrivs produkten, och titeln låser ingen längd. 'Universella skidor för barn', Rottefella NNN Touring Basic (set), 45/45/45 (utan enhet, som i källan), CAP, trä med luftkanaler och extrudering stämmer. Råden om skidlängd är rätt utelämnade. Det finns inga ålders-, säkerhets- eller utvecklingspåståenden. Taggen 'Barncykel' är fel men rörs inte (R18).


## 28012 (10462768988426, k_28a_utkast.json): RÄTTA

Live: en variant, 69 kr. Minnie-tema, metall, diameter 80 mm och höjd 55 mm stämmer. En ringklocka är ingen produkt med skyddsfunktion, och 'säkerställer cyklistens säkerhet' och 'behagliga ljud' är utelämnade. Därmed ligger produkten inom frisläppningen 2026-11-05. Färgen står bara i live-titeln och produkten har en variant, så den får stå. Rättning: metan inleddes utan verb.

- `meta` före: `Cykelklocka med Minnie-tema i metall, rosa. Klockan har diametern 80 mm och höjden 55 mm.`
  efter: `Cykelklockan Minnie är rosa, har Minnie-tema och är gjord av metall. Diametern är 80 mm och höjden 55 mm.`

## 28013 (10462805721354, k_28b_utkast.json): RÄTTA

Live: en variant, 69 kr. Frost-tema för barn, metall, 80 mm och 55 mm stämmer. Säkerhets- och ljudpåståendena är utelämnade, och en ringklocka är inget skydd. Färgen står bara i live-titeln och produkten har en variant, så den får stå. Rättning: metan inleddes utan verb.

- `meta` före: `Cykelklocka med Frost-tema för barn. Klockan är av metall`
  efter: `Cykelklockan Frost 2 har Frost-tema för barn. Klockan är av metall`

## 28015 (10462806409482, k_28b_utkast.json): RÄTTA

Live: en variant, 69 kr. Källan är tunn: Avengers-tema, barncykelklocka, metall och 'Linsdiameter: 22 mm'. Det oklara måttet är rätt utelämnat (R2). Metall och barncykelklocka är två entydiga fakta utöver titeln, och metan är kort men sann (§14). Inget skydd påstås. Färgen står bara i live-titeln och produkten har en variant, så den får stå. Rättning: metan inleddes utan verb.

- `meta` före: `Barncykelklocka med Avengers-tema i metall. Klockan finns i färgen mörkblå.`
  efter: `Den här barncykelklockan har Avengers-tema och är gjord av metall. Färgen är mörkblå.`

## 28016 (10462812176650, k_28b_utkast.json): RÄTTA

Live: en variant, 5769 kr. Aluminium, S (10 tum) för ca 110-130 cm (ur raden felmärkt 'Tillverkare:', entydig del, enligt tillverkaren en gång), Shimano Tourney, 6 växlar, däck 20 x 1.9 och fästpunkter stämmer. 'Shimano Touring: 6 hjul', 'Hjulvikt' och marknadsföringen är rätt utelämnade. Färgen står bara i live-titeln och produkten har en variant, så den får stå. Rättning: decimalpunkt till decimalkomma ('20 x 1,9') i meta, inledning och specifikation, som 28007 ('24 x 1,95'). Ingen enhet läggs till, eftersom källan inte anger någon.

- `meta` före: `20 x 1.9.`
  efter: `20 x 1,9.`
- `html` före: `däck i 20 x 1.9 och`
  efter: `däck i 20 x 1,9 och`
- `html` före: `<li>Däck: 20 x 1.9</li>`
  efter: `<li>Däck: 20 x 1,9</li>`

## 28017 (10462813225226, k_28b_utkast.json): GODKÄND

Live: en variant, 6079 kr. Aluminium i ram, hjul och vevparti, 1 växel, V-bromsar, 26,5 cm (entydig del av en trasig rad) för 110-120 cm (enligt tillverkaren en gång) och 'Extra hjul, kedjeskydd och skjutstång ingår' stämmer ordagrant. 'Extra hjul' tolkas inte som stödhjul, vilket är rätt. Kedjeskyddet och skjutstången nämns utan skydds- eller lastpåstående. 18 tum är utelämnat helt, vilket är tillåtet. 'Maximal säkerhet', 'för flickor', ursprung och 'Hjulvikt' är rätt utelämnade. Färgen står bara i live-titeln och produkten har en variant, så den får stå.


## 28019 (10462836130058, k_28b_utkast.json): GODKÄND

Live: en variant, 4929 kr. Aluminium, 28 cm för 110-125 cm (entydig del, enligt tillverkaren en gång), 1 växel och V-bromsar stämmer. Källan säger 'Inkluderar kedjeskydd, stödhjul, skjutstång, ringklocka och korg fram' samt 'avtagbara stödhjul'. Stödhjulen, kedjeskyddet och korgen nämns bara som utrustning, utan lastgräns eller skyddspåstående. Det är tillåtet: inget i texten påstår bärförmåga, och v1.7 kräver lastgräns bara för påståenden om last och för bärande produkter. 'Utmärkt för att lära sig cykla', 'perfekt som första cykel', 'mjuka handtag' och den trasiga raden med huven är rätt utelämnade. 18 tum är utelämnat. Färgen står bara i live-titeln och produkten har en variant, så den får stå.

