import json,re
D='/home/user/Shopify/rapporter/facit-bos-2026-10-31/vag2_skriv/'
b24=json.load(open(D+'b_24_utkast.json'))[0]['html']
STD=b24[b24.index('<h2>Leverans, retur och garanti</h2>'):]
LT=' Beställningsvaror kan ta upp till en vecka längre.'
def ul(items): return '<ul>\n'+'\n'.join('<li>%s</li>'%i for i in items)+'\n</ul>'
def html(intro,passar,spec,extra=''):
    return '<p>%s</p><h2>Passar för</h2>%s<h2>Specifikationer</h2>%s%s%s'%(intro,ul(passar),ul(spec),extra,STD)
old={x['id']:x for x in json.load(open(D+'k_02a_utkast.json'))}
step=[x for x in json.load(open(D+'c_18_utkast.json')) if x['id']=='10581119336714'][0]
U=[]
g=dict(old['10581606629642']); g['nr']=20024; g['att_bekrafta']=g['att_bekrafta']+["Faktakoll på nätet (Giants egen sida, https://www.giant-bicycles.com/ee/anytour-cs-2-gb): Gates remdrift, Shimano Nexus 8 och hydrauliska MT200-bromsar stämmer med källan; inget tillkom. Tillverkarens sida anger Nexus 8 Revo-växelreglage men retailers anger annat, så ingen reglagemodell nämns.","Frame-storlekar M/L/XL utelämnade (bara en variant, Default Title). Reflexrand på däcken återges som delbeskrivning av däcket, inte som reflexprodukt."]
U.append(g)
s=dict(step); s['nr']=20023
s['meta']='Gymstick Vivid Step Board är en stepbräda från Gymstick för träning, till exempel aerobiska övningar och styrketräning.'
s['att_bekrafta']=step['att_bekrafta']+["Ingen faktakoll på nätet gav entydiga mått för exakt modellen; inget tillkom. Meta är kort och sann (standard §14)."]
U.append(s)
# bag 150
U.append(dict(id='10636601458954',nr=20025,
 titel='Boxningssäck MAXXUS, Vatten och Luft, 150 cm',
 seo_title='Boxningssäck MAXXUS Vatten och Luft',
 meta='Boxningssäcken MAXXUS Vatten och Luft fylls med vatten och luft och är gjord av PVC med 7 mm tjocklek. Längd 150 cm, diameter 30 cm.',
 html=html('MAXXUS Vatten och Luft är en boxningssäck i PVC med 7 mm materialtjocklek. Säcken fylls med både vatten och luft, så att du kan justera hårdheten. Pump ingår inte.',
  ['Dig som vill ha en boxningssäck där hårdheten kan justeras med lufttrycket','Dig som vill träna slag och sparkar hemma'],
  ['Märke: MAXXUS','Material: PVC, 7 mm tjocklek','Fyllning: Vatten och luft','Diameter: 30 cm','Längd: 150 cm','Pump: Ingår inte']),
 fakta='Boxningssäck MAXXUS Vatten & Luft 150cm/ca 30kg. PVC 7mm, fyllning vatten och luft, diameter 30cm, längd 150cm, pump ingår ej. Säcken fylls med vatten och lufttrycket avgör hårdheten. SKU GSMX-600427-00019-0002, en variant, 1299 kr. Tag boxning, boxningssäck, Maxxus.',
 att_bekrafta=['Titelns 30 kg utelämnat: källan skriver "ca 30kg" i rubriken utan förklaring (sannolikt fylld vikt, som är fyllnadsmängd, R4).','"Slitstark", "tåla upprepad belastning" och "stabilitet" utelämnade (R5).','Syskonprodukten 100 cm (20026) avvisad; 150 cm-versionen har konsekventa mått (längd 150 cm).','Ingen faktakoll på nätet gjord; källan är entydig.']))
# stabilitet
U.append(dict(id='10636602802442',nr=20027,
 titel='Stabilitetspaket med Gummiband och Balansredskap',
 seo_title='Stabilitetspaket med Gummiband',
 meta='Stabilitetspaketet innehåller justerbart gummiband, fem korta gummiband, balanskudde och balansplatta för balansövningar och träning med gummiband.',
 html=html('Stabilitetspaketet samlar gummiband och balansredskap. Det innehåller justerbart gummiband, fem korta gummiband, en balanskudde och en balansplatta.',
  ['Dig som vill träna balans med balanskudde och balansplatta','Dig som vill ha gummiband med olika motstånd i samma paket'],
  ['Ingår: Gummiband Justerbara Tre färger, Gummibandspaket Korta 50 cm, Balanskudde Balansdyna 33 cm, Balansplatta Handtag 39,5 cm',
   'Justerbart gummiband: Tre motståndsnivåer, längd 117 cm, förvaringspåse medföljer',
   'Justerbart gummiband, motstånd: Blå 1,4–2,5 kg, röd 2,2–3,4 kg, grön 2,8–5,3 kg',
   'Korta gummiband: Fem band, 500x50 mm, motstånd rosa 4,5 kg, gul 9 kg, blå 11,3 kg, röd 13,6 kg, svart 15,8 kg',
   'Balanskudde: Diameter 33 cm, material PVC, pump ingår, maxbelastning 220 kg enligt tillverkaren',
   'Balansplatta: Diameter 39,5 cm, höjd 9 cm, vikt 3 kg, material plast, maxbelastning 120 kg enligt tillverkaren']),
 fakta='Stabilitetspaket: gummiband justerbara tre färger (117cm, tre nivåer, blå 1,4-2,5kg, röd 2,2-3,4kg, grön 2,8-5,3kg, förvaringspåse), gummibandspaket korta 50cm (500x50mm, rosa 10lb/4,5kg, gul 20lb/9kg, blå 25lb/11,3kg, röd 30lb/13,6kg, svart 35lb/15,8kg), balanskudde 33cm (maxbelastning 220kg, PVC halkfritt, pump ingår), balansplatta handtag 39,5cm (höjd 9cm, maxbelastning 120kg, vikt 3kg, plast, halkfri yta). Ingen SKU, en variant, 1399 kr. Tag balans, bundle, paket.',
 att_bekrafta=['Rehab-, skadeförebyggande- och förbättrar-påståenden utelämnade (R5). "Halkfritt/halkfri yta" utelämnat (R5).','Maxbelastning 220 kg och 120 kg återges ordagrant (svenska, enhet, etikett), en gång vardera: två "enligt tillverkaren".','Uppgifter i lb (10–35 lb) utelämnade, kg behålls.','Ingen SKU (null). Bundle: delprodukterna har inga egna SKU i källan.','Ingen faktakoll på nätet gjord; källan är entydig.']))
# yogapaket
U.append(dict(id='10636620398858',nr=20032,
 titel='Yogapaket med Yogamatta, Yogablock och Yogaboll',
 seo_title='Yogapaket med Matta, Block och Boll',
 meta='Yogapaket med yogamatta 190x60 cm, yogablock i EVA-skum och yogaboll med 65 cm diameter. Pump medföljer. Färg rosa på matta och block.',
 html=html('Yogapaketet innehåller en yogamatta, ett yogablock och en yogaboll. Matta och block är rosa, och bollen levereras med pump.',
  ['Dig som vill ha matta, block och boll i samma paket','Dig som vill kombinera yoga med övningar på yogaboll'],
  ['Ingår: Träningsmatta Deluxe Yogamatta 190x60 cm, Yogablock GS, Fitnessboll Yogaboll Pilatesboll',
   'Yogamatta: Material ftalatfritt skum av nitrilgummi och PVC, mått 190x60x1,5 cm, vikt 1,2 kg, bärsele ingår, färg rosa',
   'Yogablock: Material EVA-skum, mått 23,5x15x8 cm, maxbelastning 150 kg enligt tillverkaren, färg rosa',
   'Yogaboll: Diameter 65 cm, maxbelastning 500 kg enligt tillverkaren, pump ingår']),
 fakta='Yogapaket: Träningsmatta Deluxe Yogamatta 190x60cm (ftalatfritt hudvänligt skum av nitrilgummi och PVC, 190x60x1,5cm, bärsele, rosa, 1,2kg), Yogablock GS (EVA, maximal belastning 150kg, 23,5x15x8cm, rosa), Fitnessboll Yogaboll Pilatesboll (maximal belastning 500kg, pump, diameter 65cm). SKU 121017-10016-0001, en variant, 799 kr. Tag bundles, Yoga, yogapaket, yogaset.',
 att_bekrafta=['Yogabollens färg ligger i en avkortad rad i källan; färgen utelämnad för bollen.','Maxbelastning 150 kg (block) och 500 kg (boll) ordagrant på svenska med enhet och etikett: två "enligt tillverkaren".','"Mjuk och slitstark", "stödjande" och förbättra-påståenden utelämnade (R5).','Ingen faktakoll på nätet gjord; källan är entydig.']))
# pilates
U.append(dict(id='10636624167178',nr=20033,
 titel='Pilatesset med Pilatesstång och Motståndsband',
 seo_title='Pilatesset med Pilatesstång',
 meta='Pilatesset med justerbar pilatesstång 90–100 cm, motståndsband på 13, 18 och 23 kg, hand- och fotremmar, dörrankare och bärväska.',
 html=html('Pilatessetet innehåller en pilatesstång som kan justeras från 90 till 100 cm och motståndsband med tre olika motstånd. Dörrankare, hand- och fotremmar och en bärväska ingår.',
  ['Dig som vill ha pilatesstång och motståndsband i samma set','Dig som vill ha en stång som kan delas i tre delar för förvaring och transport'],
  ['Stång: Justerbar längd 90–100 cm, kan delas i tre delar','Motståndsband: Grå 13 kg, svart 18 kg, röd 23 kg','Ingår: Hand- och fotremmar (2 st), dörrankare, bärväska','Vikt: 1,5 kg']),
 fakta='Pilatesset Pilatesstång. Tre motståndsnivåer grå 13kg, svart 18kg, röd 23kg. Stången kan justeras 90-100cm och delas i tre delar. 2 hand- och fotremmar, 1 dörrankare, 1 bärväska, vikt 1,5kg. SKU 101304-00001-0001, en variant, 779 kr. Tag pilates, Pilatesband, Pilatesstång.',
 att_bekrafta=['Antalet band är motsägelsefullt i källan ("tre par motståndsband", "3 justerbara pilates band", "3 motståndsband"); antal utelämnat (R2).','Färgen på 18 kg (svart) och 23 kg (röd) står i brödtexten; listan anger bara siffrorna. Motstånd i kg är inte lastgräns.','Ingen faktakoll på nätet gjord; källan är entydig.']))
for u in U: u.setdefault('fakta','')
json.dump(U,open(D+'k_19c_utkast.json','w'),ensure_ascii=False,indent=1)
IN={x['id']:x for x in json.load(open(D+'k_19c_in.json'))}
sk={
'10636601655562':'R3: titeln anger 100 cm men specifikationen i källan anger längd 120 cm (motsägelse mellan titel och källa); kan inte skrivas utan att gissa. Möjlig dubblett av 9720 "Boxningssäck Excalibur Workout 100, 26 kg" (10636659687690, redan skriven).',
'10636609224970':'Hängande/bärande produkt (suspensionstränare, kroppsvikten hänger i banden): v1.7/R4 kräver ordagrann svensk lastgräns; källan anger ingen och webbsökning gav ingen entydig uppgift för exakt TRYM-modellen. Kräver Davids ja per produkt.',
'10636616696074':'R3/v1.7: 12 färgvarianter med olika SKU (20040605–20040616); olika SKU på riktiga varianter avvisas.',
'10636616925450':'R3/v1.7: 12 färgvarianter med olika SKU (20040319–20040478); olika SKU på riktiga varianter avvisas.',
'10636617122058':'R3/v1.7: 12 färgvarianter med olika SKU (20040300–20040475); olika SKU på riktiga varianter avvisas.'}
A=[{'id':i,'nr':IN[i]['nr'],'titel':IN[i]['titel_nu'],'skäl':s} for i,s in sk.items()]
json.dump(A,open(D+'k_19c_avvisade.json','w'),ensure_ascii=False,indent=1)
