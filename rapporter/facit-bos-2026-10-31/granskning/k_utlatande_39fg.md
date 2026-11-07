# Granskningsutlåtande k_39f och k_39g (2026-11-07)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS). Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.10), BESLUTSLOGG till och med 2026-11-07 (återaktiverade produkter får text enligt vanliga regler), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_39bd.md` och `k_utlatande_39e.md` (cirkulära inledningar rättas) och formatet i `k_utlatande_39bd.json`.

Alla 20 utkast och alla 15 avvisade är ACTIVE med lager. Ingen spärrad produkt. `skrivfil_kontroll.py` gav 0 fel och 13 varningar på utkasten (alla om cirkulär inledning) och 0 fel och 0 varningar på de rättade texterna. Standardblocket är exakt rätt på alla 20. Leveranstidsmeningen finns på exakt de tre som har taggen På beställning (39124, 39139, 39141). Titlar, SEO-titlar och metatexter är unika mot alla andra `*utkast*.json`, `*skriv*.json` och live-titlarna (sökning på syskon i butiken). Titlar ≤70 tecken och ≤2 kommatecken, SEO ≤43, meta 70–155 med verb, även efter rättning.

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_39fg.json`. Varje rättning är ETT sammanhängande före/efter-par per fält, och varje före-text förekommer exakt en gång i utkastet (kontrollerat i python).

## Resultat: 3 GODKÄND, 17 RÄTTA, 0 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 39121 | 10472348221706 | k_39f_utkast.json | RÄTTA | titel, seo_title, meta, html |
| 39122 | 10472351105290 | k_39f_utkast.json | RÄTTA | seo_title, html |
| 39123 | 10472400486666 | k_39f_utkast.json | RÄTTA | html |
| 39124 | 10472434073866 | k_39f_utkast.json | RÄTTA | html |
| 39128 | 10475373101322 | k_39f_utkast.json | RÄTTA | html |
| 39129 | 10475373429002 | k_39f_utkast.json | GODKÄND | – |
| 39130 | 10475418485002 | k_39f_utkast.json | RÄTTA | meta, html |
| 39131 | 10475418681610 | k_39f_utkast.json | RÄTTA | meta, html |
| 39133 | 10475980226826 | k_39f_utkast.json | GODKÄND | – |
| 39134 | 10475983339786 | k_39f_utkast.json | RÄTTA | meta, html |
| 39139 | 10488246698250 | k_39f_utkast.json | RÄTTA | meta, html |
| 39141 | 10494672929034 | k_39f_utkast.json | RÄTTA | meta, html |
| 39142 | 10494685479178 | k_39f_utkast.json | RÄTTA | meta, html |
| 39143 | 10494689280266 | k_39f_utkast.json | RÄTTA | meta, html |
| 39145 | 10494691115274 | k_39g_utkast.json | GODKÄND | – |
| 39146 | 10494691410186 | k_39g_utkast.json | RÄTTA | html |
| 39148 | 10494695342346 | k_39g_utkast.json | RÄTTA | html |
| 39149 | 10494695375114 | k_39g_utkast.json | RÄTTA | meta, html |
| 39154 | 10494919180554 | k_39g_utkast.json | RÄTTA | meta, html |
| 39155 | 10494919213322 | k_39g_utkast.json | RÄTTA | meta, html |

## Skäl och rättningar per produkt

### 39121 (10472348221706): RÄTTA

Live ACTIVE, en variant 0757E, lager 64. Alla fakta i egen källa (nästan alla 20-tumshjul, fästelement och monteringsfästen ingår, bakhjulsbågen ca 72 cm, bredd ca 50 mm; svart ur live-titeln). Rättning R7/R12: de skrivna syskonen heter 'Stänkskärmset Hebie Taipan, 24 tum, Svart' och '…, 26 tum, Svart' (samma engelska källtyp 'Fender set'); typordet ska vara enhetligt, och 'Stänkskärmssetet' stavas 'Stänkskärmsetet'. Unik mot syskonen genom 20 tum.

| fält | före | efter |
|---|---|---|
| titel | Stänkskärmar Hebie Taipan 20 tum, Svart | Stänkskärmset Hebie Taipan, 20 tum, Svart |
| seo_title | Stänkskärmar Hebie Taipan 20 tum | Stänkskärmset Hebie Taipan, 20 tum |
| meta | Stänkskärmssetet Hebie Taipan är lämpligt för nästan alla 20-tums hjul. Fästelement och monteringsfästen för alla fälgar ingår. | Stänkskärmsetet Hebie Taipan är lämpligt för nästan alla 20-tums hjul. Fästelement och monteringsfästen för alla fälgar ingår. |
| html | sammanhängande bit, 377 tecken (se JSON) | samma bit med ändringen i skälet |

### 39122 (10472351105290): RÄTTA

Live ACTIVE, lager 7. Kosttillskott frisläppt 2026-11-05; magnesium/B6 hör inte till de undantagna. Bara produktfakta: ingredienslista ordagrann, dos, användning, förvaring, varningar. Källans påståenden (100 % av dagligt behov, trötthet, sömn, återhämtning, elektrolytbalans, vegetarianer) är utelämnade. Typordet Kosttillskott enligt uppdraget. 'halsa' på 'vitamin' är det kända falsklarmet. Rättning R11: inledningen var cirkulär ('X är ett kosttillskott'). Rättning R12: SEO-titeln utan '+ B6' går inte att skilja från syskonet Trec Essensey Magnesium+Zinc+B6 (10472351170826, skrivet); '+ B6' ryms (42 tecken).

| fält | före | efter |
|---|---|---|
| seo_title | Kosttillskott Trec Essensey Magnesium | Kosttillskott Trec Essensey Magnesium + B6 |
| html | <p>Trec Essensey Magnesium + B6 är ett kosttillskott med magnesium i fyra former och vitamin B6. | <p>Kosttillskottet Trec Essensey Magnesium + B6 innehåller magnesium i fyra former och vitamin B6. |

### 39123 (10472400486666): RÄTTA

Live ACTIVE, lager 1. Fakta i egen källa (6-delad, 185 x 120 x 1,2 cm, träimitation, kan demonteras och förvaras kompakt, golvmatta/bas för gymutrustning hemma). Skydds- och dämpningspåståenden utelämnade. Typordet Pusselmatta ur live-titeln. Rättning R11: cirkulär inledning ('Hammer Basic är en … pusselmatta').

| fält | före | efter |
|---|---|---|
| html | <p>Hammer Basic är en 6-delad pusselmatta som mäter 185 x 120 x 1,2 cm och har ytan i träimitation. | <p>Pusselmattan Hammer Basic består av 6 delar, mäter 185 x 120 x 1,2 cm och har ytan i träimitation. |

### 39124 (10472434073866): RÄTTA

Live ACTIVE, lager 1, tagg På beställning; leveranstidsmeningen finns. Egen källa engelsk; fakta verifierade på https://www.tunturi.com/en/pr60-power-rack.html (art.nr 25TSPR6000, EAN 8717842038321): 123 x 135 x 213,7 cm, 78 kg, 'Maximum load: 300 kg', 'Number of adjustable heights: 18' för J-hooks och spotter arms. 300 kg skrivs en gång enligt tillverkaren (v1.10). Rättning: 'Ställningens höjder kan ställas in i 18 lägen' var fel (det är J-hooks/spotterarmar som ställs i 18 höjder, inte ställningen) och inledningen var cirkulär. Till David: tillverkarens sida säger inte uttryckligen om 300 kg gäller hela ställningen eller J-hooks/spotterarmar; tillbehören dip/kabeldrag har lägre gränser. Säkerhetsarmar ('safety grips') nämns inte, korrekt.

| fält | före | efter |
|---|---|---|
| html | sammanhängande bit, 231 tecken (se JSON) | samma bit med ändringen i skälet |

### 39128 (10475373101322): RÄTTA

Live ACTIVE, lager 3. Fakta i egen källa och på https://www.tunturi.com/en/pro-pull-up-bar-wall-connect.html (149 x 38 x 41,5 cm, stål, svart/krom, monteringskit med expanderbultar, art.nr 14TUSCF085). Lastgräns: tillverkaren anger ingen; 300 kg finns bara hos återförsäljaren eleme.ee, och andra återförsäljare anger 120 kg för liknande Tunturi-stänger. 'Maximal lastgräns: Ej känd' enligt v1.10 är rätt. Typordet Pull-up-stång står i egen källa ('Pull up-stång'). Rättning R11: cirkulär inledning.

| fält | före | efter |
|---|---|---|
| html | <p>Tunturi Pro är en väggmonterad pull-up-stång i stål för pull-ups och chin-ups. | <p>Pull-up-stången Tunturi Pro monteras på vägg, är gjord i stål och används för pull-ups och chin-ups. |

### 39129 (10475373429002): GODKÄND

Live ACTIVE, en variant, lager 9. Alla fakta i egen svensk källa (35 cm stång, största skivan 16 cm, totalvikt 10 kg, 2 x 2,5 + 2 x 1,25 kg, 2 skruvpluggar per hantel, svart/krom, gjutjärn/stål). Halkfritt, säkert och skruvlåspåståendet utelämnade. Unik mot de skrivna Tunturi-hantelseten (15, 20 och 28 kg).

### 39130 (10475418485002): RÄTTA

Live ACTIVE, lager 7, SKU 480000362 (annan SKU än skrivna Liv Doublespring 600 ml Transparent och Svart, 480000278, alltså inte dubblett). Tunn källa: 600 ml och '100% BPA-fri' (ordagrant, en gång enligt tillverkaren per fält), transparent ur titeln; 'lätt att rengöra' och 'Bench' utelämnade. Rättning R11: meta och inledning var cirkulära ('Liv Doublespring är en dricksflaska'). Meta efter 109 tecken med verb.

| fält | före | efter |
|---|---|---|
| meta | Liv Doublespring är en dricksflaska som rymmer 600 ml. Enligt tillverkaren är flaskan 100 % BPA-fri. | Dricksflaskan Liv Doublespring rymmer 600 ml och är transparent. Enligt tillverkaren är flaskan 100 % BPA-fri. |
| html | <p>Liv Doublespring är en dricksflaska som rymmer 600 ml. | <p>Dricksflaskan Liv Doublespring rymmer 600 ml. |

### 39131 (10475418681610): RÄTTA

Live ACTIVE, lager 83. Fakta i egen källa (justerbart, Giant Direct Mount KSA, 20–24 tums bakhjul, aluminium, fästs på KSA18 med två bultar). Webbkoll (giant-bicycles.com, balfesbikes, ridleys med 500000038): ingen lastgräns hos tillverkaren, så 'Ej känd' enligt v1.10 är rätt. Rättning R11: meta och inledning var cirkulära.

| fält | före | efter |
|---|---|---|
| meta | Giant KSA är ett justerbart cykelstöd av aluminium för Giant Direct Mount KSA och 20–24 tums bakhjul. Det fästs med två bultar. | Cykelstödet Giant KSA är justerbart, gjort av aluminium och avsett för Giant Direct Mount KSA och 20–24 tums bakhjul. Det fästs med två bultar. |
| html | <p>Giant KSA är ett justerbart cykelstöd för Giant Direct Mount KSA och 20–24 tums bakhjul. | <p>Cykelstödet Giant KSA är justerbart och avsett för Giant Direct Mount KSA och 20–24 tums bakhjul. |

### 39133 (10475980226826): GODKÄND

Live ACTIVE, sex storleksvarianter (37–41, 43) med olika SKU men samma pris och ingen färg (v1.8); titeln låser ingen storlek och spec listar bara storlekar som säljs. Typordet Kombipjäxor står i egen källa ('kombipjäxor i TOURING-serien'). Fakta: skate och klassisk, innerfoder, snölås, vattentätt och vattenavvisande yttermaterial (en gång enligt tillverkaren), Touring Auto/Basic. Komfort- och värmelöften utelämnade. Inte samma produkt som Barnskidpjäxor Alpina T 8 JR.

### 39134 (10475983339786): RÄTTA

Live ACTIVE, lager 12. Tunn källa men två entydiga fakta (klassisk bindning för träning och tävling, manuellt fästsystem); 'säker och bekväm passform' utelämnat. Pjäxsystem inte angivet, korrekt. Rättning R11: meta och inledning var cirkulära.

| fält | före | efter |
|---|---|---|
| meta | NIS Performance CL är en klassisk skidbindning för både träning och tävling. Bindningen har ett manuellt fästsystem. | Den klassiska skidbindningen NIS Performance CL är avsedd för både träning och tävling och har ett manuellt fästsystem. |
| html | <p>NIS Performance CL är en klassisk skidbindning för både träning och tävling. | <p>Den klassiska skidbindningen NIS Performance CL är avsedd för både träning och tävling. |

### 39139 (10488246698250): RÄTTA

Live ACTIVE, lager 14, tagg På beställning; leveranstidsmeningen finns. Sju variantrader, alla svarta och 10 529 kr, storlekar M/L/XL (v1.8); titeln låser ingen storlek, svart gäller alla varianter. Fakta i egen källa (ALUXX-Grade, Shimano Altus, 8 växlar, Tektro V-bromsar, CST REACH 37-622, ramstorlekar och längder, medföljande delar). Stadscykel står i källan och matchar skrivna Attend RS 2 GTS. Rättning R11: meta och inledning var cirkulära. Till David (ej textfel): variantlistan har dubblettrader (SKU 2226011185 tre gånger för M, extra SKU 2226011187/2226011188 för L/XL utan streckkod) och bör städas i butiken.

| fält | före | efter |
|---|---|---|
| meta | Giant Attend RS 3 GTS är en stadscykel med aluminiumram, 8 växlar och V-bromsar. Stänkskärmar, pakethållare samt fram- och bakljus ingår. | Stadscykeln Giant Attend RS 3 GTS har aluminiumram, 8 växlar och V-bromsar. Stänkskärmar, pakethållare samt fram- och bakljus ingår. |
| html | <p>Giant Attend RS 3 GTS är en stadscykel med ram av aluminium (ALUXX-Grade), | <p>Stadscykeln Giant Attend RS 3 GTS har ram av aluminium (ALUXX-Grade), |

### 39141 (10494672929034): RÄTTA

Live ACTIVE, lager 2, tagg På beställning; leveranstidsmeningen finns. Material och mått utelämnade med rätta (titeln PE, egen källa PVC, webben delad PE/PVC och olika mått). 'PE' behålls bara som produktnamn (Tunturi/återförsäljare säljer den som 'Tunturi PE Kettlebell'). Fakta: 2 kg, sandfylld, svart, finns i olika vikter. Rättning R11: meta och inledning var cirkulära ('Tunturi PE Kettlebell är en … kettlebell'). Till David: skrivna syskonet 10588446589194 (16 kg) har 'PVC' i titeln; materialfrågan gäller hela serien.

| fält | före | efter |
|---|---|---|
| meta | Tunturi PE Kettlebell är en sandfylld kettlebell på 2 kg i svart. Den finns i olika vikter. Artikelnummer 14TUSCL102. | Kettlebellen Tunturi PE väger 2 kg, är fylld med sand och är svart. Den finns i olika vikter. Artikelnumret är 14TUSCL102. |
| html | <p>Tunturi PE Kettlebell är en sandfylld kettlebell på 2 kg. | <p>Kettlebellen Tunturi PE väger 2 kg och är fylld med sand. |

### 39142 (10494685479178): RÄTTA

Live ACTIVE, lager 1. Fakta i egen svensk källa (bakgaffel, 24–28 tum, 18 mm mellan bultarna, aluminium, 'Lastkapacitet 35 kg' med etikett och enhet; skrivs en gång enligt tillverkaren enligt R4/v1.10). Rättning R11: meta och inledning var cirkulära. Unik mot skrivna Mini-stöd Ursus King R78 (10472227340554).

| fält | före | efter |
|---|---|---|
| meta | Ursus King R78 är ett cykelstöd för bakgaffel till 24–28 tums hjul. Stödet är av aluminium och har 18 mm mellan de två bultarna. | Cykelstödet Ursus King R78 är avsett för bakgaffel och 24–28 tums hjul. Det är av aluminium och har 18 mm mellan de två bultarna. |
| html | <p>Ursus King R78 är ett stöd för bakgaffel till 24–28 tums hjul. | <p>Cykelstödet Ursus King R78 är avsett för bakgaffel och 24–28 tums hjul. |

### 39143 (10494689280266): RÄTTA

Live ACTIVE, lager 7. Webbkoll hos tillverkaren (https://www.lookcycle.com/by-en/products/pedals/urban/geo-city-grip): komposit, vulkaniserat gummi activ grip, platta pedaler + LOOK activ grip by VIBRAM, 'Pedal 265 g', men 'Q Factor 62 mm' och 'Platform area 100x103 mm' mot egen källas 63 mm och 107x103 mm. Motsägelse enligt R2: Q-faktor och plattformsmått tas bort ur meta, löptext och specifikation; vikten gäller per pedal enligt tillverkaren. Ingen lastgräns hos tillverkaren, 'Ej känd' enligt v1.10. Meta utan lastgränsmeningen (står i text och spec). Märket skrivs 'Look' som i skrivna syskonet Camo. Till David: skrivna syskonet Pedaler Look Geo City Grip, Camo (10494689345802) har 63 mm och 107 x 103 mm i texten, som tillverkaren inte anger.

| fält | före | efter |
|---|---|---|
| meta | Look Geo City Grip är platta pedaler i komposit med gummigrepp från Vibram. Plattformen mäter 107 x 103 mm. Maximal lastgräns är inte känd. | Pedalerna Look Geo City Grip är platta och gjorda i komposit, med grepp av vulkaniserat gummi (Look Activ Grip från Vibram). |
| html | sammanhängande bit, 571 tecken (se JSON) | samma bit med ändringen i skälet |

### 39145 (10494691115274): GODKÄND

Live ACTIVE, lager 10. Alla fakta i egen källa (golvmatta L för elliptiska tränare/crosstrainers och löpband, ca 1600 x 840 x 3 mm). Grepp- och skyddspåståenden utelämnade. Golvmatta står i källan. Enhetlig med skrivna Golvmatta Christopeit M och XL.

### 39146 (10494691410186): RÄTTA

Live ACTIVE, lager 2. Fakta i egen källa (Speed Jumper, PVC-sladd, justerbar längd upp till ca 276 cm, 0,1 kg). Effektpåståenden utelämnade. Hopprep står i källan. Rättning R11: cirkulär inledning ('… är ett hopprep').

| fält | före | efter |
|---|---|---|
| html | <p>Christopeit Speed Jumper är ett hopprep med PVC-sladd. | <p>Hopprepet Christopeit Speed Jumper har PVC-sladd. |

### 39148 (10494695342346): RÄTTA

Live ACTIVE, lager 101. Egen källa tunn och delvis trasig ('lins'); modell, material, färg och användning verifierade hos tillverkaren https://messingschlager.com/en/products/bottle-cages_t54/m-wave-ada-t90-adapter-for-bottle-cages_a340017 (M-WAVE Ada T90, art.nr 340017, EAN 887539017446 = live, aluminium, svart, 'for mounting a bottle cage'). Rättning R11: cirkulär inledning.

| fält | före | efter |
|---|---|---|
| html | <p>M-Wave ADA T90 är en adapter för flaskhållare. Adaptern är av aluminium och svart.</p> | <p>Adaptern M-Wave ADA T90 används för att montera en flaskhållare. Den är av aluminium och svart.</p> |

### 39149 (10494695375114): RÄTTA

Live ACTIVE, lager 24. Fakta i egen källa (framskärm för mountainbikes, snabb att ta bort och installera, kompatibel med de flesta gafflar; giant-bicycles.com bekräftar). 'Högkvalitativ' utelämnat. Rättning R11/R12: meta var cirkulär och fylld med 'Artikelnumret är 350703. Finns hos BEST OF SPORTS.' trots att källan räcker; ersatt med källans två fakta (en gång enligt tillverkaren). Meta efter 141 tecken.

| fält | före | efter |
|---|---|---|
| meta | Giant FSX är en framskärm för mountainbikes. Artikelnumret är 350703. Finns hos BEST OF SPORTS. | Framskärmen Giant FSX är gjord för mountainbikes. Enligt tillverkaren passar den de flesta gafflar och är snabb att ta bort och installera. |
| html | <p>Giant FSX är en framskärm för mountainbikes. | <p>Framskärmen Giant FSX är gjord för mountainbikes. |

### 39154 (10494919180554): RÄTTA

Live ACTIVE, lager 2, varianter blue och Red, samma pris 3 679 kr (v1.9); titel, SEO och text låser ingen färg. Barnprodukt frisläppt 2026-11-05, sparkcykel ej undantagen; inga säkerhets- eller utvecklingslöften. Källans maxhöjd '102 mm' är trasig; 92–102 cm och hjulen 230 x 40 mm/215 x 40 mm i mm står på tillverkarens sida enligt sökmotorns index (scool.de/en/products/s-cool-flax-8-5 med exakt EAN), men sidan är nu borttagen (404) och kunde inte läsas direkt. Godtas eftersom siffrorna stämmer med egen källa och enheten är entydig hos tillverkaren; flaggas till David. 'Maximal belastning: 100 kg' svensk rad med etikett, en gång enligt tillverkaren. Rättning R11: meta och inledning var cirkulära ('S'cool flaX 8.5 är en … sparkcykel'; skriptet missar mönstret på grund av punkten i 8.5).

| fält | före | efter |
|---|---|---|
| meta | S'cool flaX 8.5 är en hopfällbar sparkcykel med aluminiumram, fotbroms och höjdjusterbart styre mellan 92 och 102 cm. | Sparkcykeln S'cool flaX 8.5 är hopfällbar och har aluminiumram, fotbroms och höjdjusterbart styre mellan 92 och 102 cm. |
| html | <p>S'cool flaX 8.5 är en hopfällbar sparkcykel med aluminiumram, fotbroms och höjdjusterbart styre. | <p>Sparkcykeln S'cool flaX 8.5 är hopfällbar och har aluminiumram, fotbroms och höjdjusterbart styre. |

### 39155 (10494919213322): RÄTTA

Live ACTIVE, en variant, lager 3; färg vit/gul ur live-titeln. Styrhöjd 870–970 mm i egen källa (sökindex för scool.de anger 87–97 cm för EAN 4250969225174). Rättning R2: hjulmåttet '200' saknar enhet i egen källa och bekräftades inte hos tillverkaren för 8.4 (bara för 8.3 hos en återförsäljare); utelämnat i löptext och spec, PU och ABEC-7 står kvar. Rättning R11: meta och inledning var cirkulära. 'Maximal belastning: 100 kg' en gång enligt tillverkaren.

| fält | före | efter |
|---|---|---|
| meta | S'cool flaX 8.4 är en hopfällbar sparkcykel med aluminiumram, fotbroms och höjdjusterbart styre mellan 870 och 970 mm. | Sparkcykeln S'cool flaX 8.4 är hopfällbar och har aluminiumram, fotbroms och höjdjusterbart styre mellan 870 och 970 mm. |
| html | sammanhängande bit, 549 tecken (se JSON) | samma bit med ändringen i skälet |

## Avvisade (15): alla avvisningar står sig, inget lyfts

| nr | skäl i korthet | bedömning |
|---|---|---|
| 39125 | Toorx Spring Locks: tom källa, taggen 31 mm mot titelns 30 mm | Rätt (R3, tunn och motsägande) |
| 39126 | SKS Velo 47: titeln 26 tum, källan "Passar för 28\" cyklar" | Rätt (R3) |
| 39127 | Razor elsparkcykel för barn: motor och batteri | Rätt (el/batteri) |
| 39132 | AXA kedjelås | Rätt enligt hittillsvarande praxis (lås som säkerhetsprodukt) |
| 39135, 39136 | Spinningcykel och motionscykel med dator/program | Rätt (elektronik, tas för hand); 39136 har dessutom motstridiga lastrader |
| 39137 | Christopeit kettlebell: två varianter 289/489 kr, olika SKU och EAN, titeln 4 kg | Rätt (olika artiklar, v1.9) |
| 39138 | Elcykel 250 W, 696 Wh | Rätt |
| 39140 | Hjälm | Rätt |
| 39144 | Rucanor "hantel 2,25 kg": källan beskriver hantelgrepp, 35 cm mot 360 mm, trasig måttrad, vikten saknas | Rätt (R2/R3) |
| 39147, 39152, 39153 | Roddmaskin, cykeldator, crosstrainer med elektronik | Rätt |
| 39150, 39151 | Look pedalblock (Keo Grip 9 grader, X-Track): tom källa | Rätt som läget är (ingen egen källa). Kan prövas med webbkoll om David räknar pedalblock till "klosspedaler får vara med" (2026-11-05) |

## Till David (inga textfel i den här batchen)

1. 39124 Tunturi PR60: tillverkarens "Maximum load: 300 kg" anger inte om gränsen gäller hela ställningen eller J-hooks/spotterarmar. Texten skriver "Maximal belastning enligt tillverkaren: 300 kg" i specifikationen. Säg till om den hellre ska bli "Ej känd".
2. 39154 S'cool flaX 8.5: tillverkarens produktsida (styrhöjd 92–102 cm, hjul i mm) är nu borttagen och kunde bara bekräftas via sökmotorns index. Godtaget; flaggat.
3. 39143: tillverkaren LOOK anger Q-faktor 62 mm och plattform 100 x 103 mm, inte leverantörens 63 mm och 107 x 103 mm. Uppgifterna tas bort här. Det redan skrivna syskonet Pedaler Look Geo City Grip, Camo (10494689345802) har leverantörens siffror kvar.
4. 39139 Giant Attend RS 3 GTS har sju variantrader för tre storlekar (samma SKU tre gånger); bör städas i butiken.
5. 39141 Tunturi PE Kettlebell: materialet (PE eller PVC) är oklart för hela serien; skrivna 16 kg-syskonet har "PVC" i titeln.
