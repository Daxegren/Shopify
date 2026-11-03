# Granskning våg 2b, utkast b_22 och b_23 (tillbehör) – BEST OF SPORTS (2026-11-03)

Oberoende granskning (Opus). Bara läsning i Shopify, inget ändrat i butiken eller i utkastfilerna, inget committat. Butiken kontrollerad med get-shop-info: **BEST OF SPORTS** (bestofsports.se, SEK).

**Underlag:** `vag2_skriv/b_22_utkast.json` (21 utkast, 8049–8069) och `b_23_utkast.json` (15 utkast, 8070–8096), totalt 36. Standarden (`produkttexter-standard.md` avsnitt 1–13), `LARDOMAR.md`, `handhavd_ids.txt`, tidigare utlåtande `b_utlatande_7_9.json` / `vag2_b_granskning_7_9.md` och granskarprompten `c_granskarprompt.md`. Maskinläsbart utlåtande: `vag2_skriv/b_utlatande_22_23.json`.

## Metod
- **Källan live:** title, handle, status, productType, vendor, tags, descriptionHtml, seo och varianter hämtade med graphql_query (`nodes`) i tre omgångar om 12. Alla 36 är ACTIVE, productType Tillbehör, seo tomt. Inget id finns i `handhavd_ids.txt`.
- **Maskinellt:** längder och kommatecken, standardblocket jämfört tecken för tecken med `c_1_utkast.json` (30 exakt lika, 6 med beställningsmeningen), taggen "På beställning" mot beställningsmeningen (8052, 8055, 8057, 8067, 8075, 8080 har både tagg och mening; inga andra), dubbletter av titel och SEO-titel inom batchen och mot alla övriga `*_utkast.json`. Varje rättnings "före" kontrollerad att förekomma exakt en gång i sitt fält; nya metalängder räknade.
- **För hand:** varje titel, SEO-titel, meta och html läst mot live-källan och språkgranskad.
- **5256** (Giant ARX orange) är *inte* skriven: den underkändes i b_7–b_9 som barnprodukt och live-titeln är fortfarande "Dricksflaska GIANT ARX 400ML ORANGE". Det finns alltså inget skrivet mönster för 8070–8072, som därför underkänns på samma grund.

## Resultat i korthet

| Dom | Antal | Nr |
|---|---|---|
| GODKÄND | 9 | 8051, 8055, 8057, 8060, 8064, 8067, 8069, 8088, 8095 |
| RÄTTA | 19 | 8049, 8050, 8054, 8058, 8061, 8063, 8065, 8066, 8073, 8074, 8075, 8079, 8080, 8086, 8089, 8091, 8092, 8094, 8096 |
| UNDERKÄND | 8 | 8052, 8056, 8068, 8070, 8071, 8072, 8076, 8093 |

Totalt 9 + 19 + 8 = 36.

## Mönster
- **Säkerhet:** två stödben (8052, 8056) bär cykelns vikt; tre ARX-flaskor (8070–8072) är "designade för barncyklar" med tagg Barncykel; solglasögonen (8076) lovar ögonskydd. 8068 är troligen en pedal (Look KEO, lager) under titeln "sadlar".
- **Motsägande källa:** färgen i 8074 (SVART/GRÅ, svart), "55 mm" i 8075, "7 delar" mot ett multiverktyg i 8080, "impellerhållare" i 8086, oförklarade varianter i 8093.
- **Språk:** cirkulära första meningar (8050, 8089), märket som subjekt (8054, 8058), upprepningar (8066, 8091), omvänd ordning i SEO-titeln (8080, 8096), "bara" i metan (8073), säkerhetslöfte "säkert grepp" (8092), "tryckavlastning" (8063).
- **Kan släppas:** inget av de 12 avvisade (`b_22_avvisade.json`, `b_23_avvisade.json`) är uppenbart ofarligt; alla avvisningar står sig.
- **Följdfynd utanför batchen:** 8102 i b_24 (SKS Bluemels Basic 45 mm) får samma titel som 8075 om måtten stryks; båda bör skiljas åt med däckbredden (32–47 mm respektive 28–37 mm).

## Per produkt

| Nr | Id | Dom | Fält | Före | Efter | Skäl |
|---|---|---|---|---|---|---|
| 8049 | 10472293531914 | RÄTTA | html | för montering på styret. Diametern är 22–26 mm.&lt;/p&gt; | för montering på styret.&lt;/p&gt; | Källan anger 'Diameter: 22-26 mm' utan att säga om det är hållarens eller styrets mått, och nästa rad är felöversatt ('montering på en lins'). Måttet får stå som specifikation ordagrant men inte förklaras i inledningen. Övrigt stämmer (aluminium, för styre, svart i titeln). |
| 8050 | 10472294088970 | RÄTTA | html | &lt;p&gt;Giant Valve Extender är en ventilförlängare på 50 mm.&lt;/p&gt; | &lt;p&gt;Det här är en ventilförlängare från Giant på 50 mm.&lt;/p&gt; | Cirkulär första mening ('Valve Extender är en ventilförlängare'). Tunn källa (bara titel) rätt hanterad, ingen meta. SEO lika med titeln lagras tom (avsett). |
| 8051 | 10472294154506 | GODKÄND | | | | Stämmer mot källan. 'Passar 21-26mm linser' rätt utelämnad (felöversättning). Typordet stöds av titeln och taggen ringklocka. SEO lika med titeln lagras tom (avsett). |
| 8052 | 10472294842634 | UNDERKÄND | | | | UNDERKÄND. Stödben (taggen stödben, källan 'Stand'/'Stativ') bär cykelns vikt, här till elcykeln ADO Air Carbon; samma bedömning som 5003/5010. Källan är dessutom för tunn och motsägande (Stand/Stativ/stödben) för att typordet ska vara entydigt. |
| 8054 | 10472486109450 | RÄTTA | html | &lt;p&gt;Start skidskrapa är tillverkad av metall | &lt;p&gt;Skidskrapan från Start är tillverkad av metall | Typordet Skidskrapa stöds av källan ('rengöra ... skidornas belag'); den trasiga 'Startkabeln' och 'gammalt fett' är rätt utelämnade. Inledningen 'Start skidskrapa är' är ogrammatisk (Start är märket). |
| 8055 | 10475355570442 | GODKÄND | | | | Stämmer: plast, 45 g, 317 mm, buntband, 26–29 tum och 1,95–2,6 tum enligt tillverkaren. Trasig mening om 'enkel kabel' rätt utelämnad. Taggen På beställning finns och standardblocket har beställningsmeningen. |
| 8056 | 10475361206538 | UNDERKÄND | | | | UNDERKÄND. Centrerat cykelstöd (taggen stödben) bär cykelns vikt och är avsett för 16–20 tums cyklar, alltså troligen barncyklar; både last och barn. Samma linje som 5003/5010. Titeln 'Cykelstöd för Cyklar' är dessutom cirkulär. |
| 8057 | 10475361894666 | GODKÄND | | | | Stämmer: tvåkomponentsplast, 29 tum, 2,0–3,0 tum, 620 mm, max sadelstolpe 35 mm, Powerstraps, 2-pivot enligt tillverkaren. '27.5 plus' rätt utelämnat ur titeln (specifikationen säger bara 29). 'Tillverkad i Tyskland' och 'okrossbar' utelämnade. Beställningsmeningen finns (tagg På beställning). |
| 8058 | 10475385356554 | RÄTTA | meta | Start mässingsborste för skidor används för | Mässingsborsten från Start används för | Start är märket, inte produkten: 'Start är en mässingsborste' och 'Start mässingsborste ... används' är fel/ogrammatiskt. Innehållet stämmer mot källan (paraffin, struktur, polering, en riktning). Ny meta se längd i tabellen. |
|  |  |  | html | &lt;p&gt;Start är en mässingsborste för skidor. Den används | &lt;p&gt;Det här är en mässingsborste för skidor från Start. Den används |  |
| 8060 | 10475621646602 | GODKÄND | | | | Tunn källa rätt hanterad (bara titel och 'Tillverkaren är Liv'), ingen meta. En variant; färgen från titeln. |
| 8061 | 10475981930762 | RÄTTA | html | Sadeln har en ergonomisk design och en optimerad form. | Sadeln har enligt tillverkaren en ergonomisk design och en optimerad form. | Ergonomisk design och optimerad form är tillverkarens påstående (metan markerar det, inledningen inte). 'Rammaterial: chromoly' och Giants standardtext rätt utelämnade. 400 g stämmer. |
| 8063 | 10494689313034 | RÄTTA | meta | M-Wave Comp VI är en svart racingsadel med V-design och ventilationshål. Enligt tillverkaren har den O-Zone i hel längd för tryckavlastning. | null | 'För tryckavlastning' är ett kroppsligt effektpåstående (jfr 8074 där 'avlasta' utelämnats) och tas bort; utan det räcker källan (tre punkter i kvarlämnad chattkod) inte till en meta om 130–155 tecken utan utfyllnad, så meta blir null (tunn källa). Html har redan bara 'O-Zone i hel längd'. Handtaget slutar på 251014 men SKU är 251013 (att bekräfta). |
| 8064 | 10494696587530 | GODKÄND | | | | Stämmer: polypropen, 50 g, 23–35 mm enligt tillverkaren, utan verktyg, vikbar, 3M-klistermärken. Trasigt stycke om 'borrdäcket' och 'perfekta valet' rätt utelämnade. |
| 8065 | 10494699274506 | RÄTTA | html | Färgen är matt svart med blank blå. | Färgen är matt svart och blank blå. | Språk: 'matt svart med blank blå' blir 'matt svart och blank blå' som i titel och specifikation. Kolfiber och 14 g stämmer. SKU 490000082 mot handtag ...083 (att bekräfta). |
| 8066 | 10494706417930 | RÄTTA | html | &lt;p&gt;Unior 1781/2HX är en 3-armad sexkantnyckel från Unior.&lt;/p&gt; | &lt;p&gt;1781/2HX är en 3-armad sexkantnyckel från Unior.&lt;/p&gt; | Upprepning av märket i samma mening. Tunn källa rätt hanterad, inga storlekar påhittade. |
| 8067 | 10494944018698 | GODKÄND | | | | Framkorg utan lastuppgift i källan och ingen lastgräns i texten (tillåtet enligt Davids beslut 2026-11-03). Korgen har ingen elektronik. Beställningsmeningen finns (tagg På beställning). |
| 8068 | 10515737542922 | UNDERKÄND | | | | UNDERKÄND. Motsägande källa: originaltiteln säger 'Landsvägscykelsadlar' men punkterna beskriver pedaler ('lämpliga för Look KEO-systemet', 'tätade lager, underhållsfria'). Vikten 257 g och 'Mått 82 x 92 mm' kan lika gärna vara pedalens. Giant Road Pro kan vara en pedal; pedaler är säkerhetsprodukter. Produkttypen är oklar och inget mått kan användas säkert. |
| 8069 | 10515737805066 | GODKÄND | | | | Stämmer: H2Tex, M, 43 x 6 x 11,5 cm, 3 liter, täckt öppning, vattentät enligt tillverkaren. Ingen lastgräns i källan och ingen i texten (kapacitet i liter är ingen lastuppgift). 'Säker förvaring' rätt utelämnat. |
| 8070 | 10515738001674 | UNDERKÄND | | | | UNDERKÄND. Källan säger 'designad för barncyklar' och taggen är Barncykel; dessutom hygienpåstående (antimikrobiell). 5256 (samma flaska, orange) underkändes av samma skäl i b_7–b_9 och är inte skriven (live-titeln är fortfarande originalet), så det finns inget skrivet mönster att följa. |
| 8071 | 10515738034442 | UNDERKÄND | | | | UNDERKÄND. Som 8070 och 5256: 'designad för barns cyklar', tagg Barncykel, antimikrobiellt påstående. |
| 8072 | 10515739476234 | UNDERKÄND | | | | UNDERKÄND. Som 8070 och 5256: 'designad för barncyklar', tagg Barncykel, antimikrobiellt påstående. |
| 8073 | 10515745833226 | RÄTTA | meta | och väger bara 60 g. | och väger 60 g. | 'Bara' är en värdering utan stöd (html skriver rätt 'väger 60 g'). Övrigt stämmer: 100 PSI / 6,9 bar, 60 g, endast Presta. |
| 8074 | 10523464368394 | RÄTTA | titel | Handtag Giant Ergo Max Lockon Grip, Svart | Handtag Giant Ergo Max Lockon Grip | Färgen är motsägande i källan ('SVART/GRÅ, svart'); Svart är inte entydigt hela färgen och stryks ur titel och specifikation. SEO-titeln blir då lika med titeln och lagras tom (avsett). Vibrations- och avlastningspåståenden rätt utelämnade. |
|  |  |  | html | &lt;li&gt;Färg: Svart&lt;/li&gt; | (tas bort) |  |
| 8075 | 10523466498314 | RÄTTA | titel | Stänkskärmar SKS Bluemels Basic, 28 tum, 55 mm | Stänkskärmar SKS Bluemels Basic, 28 tum, Däckbredd 32–47 mm | '55 mm' förklaras inte i källan och stryks ur titeln. Utan det blir titeln identisk med systerprodukten 8102 i b_24 (45 mm-versionen, 28–37 mm), så däckbredden ur källan skiljer dem åt i titel och SEO-titel (8102 bör få 'Däckbredd 28–37 mm' på samma sätt). Däckbredden är kompatibilitet och skrivs enligt tillverkaren även i metan (som i html). ASR-säkerhetssystem och 'Tillverkad i Tyskland' rätt utelämnade. Beställningsmeningen finns. |
|  |  |  | seo_title | Stänkskärmar SKS Bluemels Basic 28 tum | Stänkskärmar SKS Bluemels Basic, 32–47 mm |  |
|  |  |  | meta | SKS Bluemels Basic är stänkskärmar i aluminium och plast för 28 tum och däckbredd 32–47 mm. Framskärmen är 680 mm och bakskärmen 1185 mm lång. | SKS Bluemels Basic är stänkskärmar i aluminium och plast för 28 tum, enligt tillverkaren för däckbredd 32–47 mm. Framskärmen är 680 mm lång. |  |
| 8076 | 10523474592010 | UNDERKÄND | | | | UNDERKÄND. Solglasögon är ögonskydd: källan lovar 'maximalt skydd för dina ögon' och 'säkerhet', och 'Kat. 3' är en filterkategori med användningsbegränsningar som källan inte förklarar. Utkastaren flaggade själv frågan. Tas för hand med Davids ja. |
| 8079 | 10523491500298 | RÄTTA | seo_title | Cykelklocka Giant Ding-A-Ling Svart | Cykelklocka Giant Ding-A-Ling, Svart | SEO-titeln saknar kommatecknet före färgen (formatet i övriga). Rättad SEO-titel blir lika med titeln och lagras tom (avsett). Tom källa rätt hanterad: kort intro, ingen meta, ingen påhittad text. |
| 8080 | 10525550510346 | RÄTTA | titel | Verktygsset SKS Tom 7 | Multiverktyg SKS Tom 7 | Titeltypen stöds inte av källan: originaltiteln säger 'Verktygsset ... 7 delar' men texten beskriver ett enda multifunktionsverktyg med 7 integrerade funktioner (motsägelse). Typordet tas från texten ('multifunktionsverktyg', här Multiverktyg), produkttypen Tillbehör ändras inte. SEO-titeln hade omvänd ordning; blir lika med titeln och lagras tom. 'Från Sale' och 'I lager: från rostfritt stål' rätt utelämnade. Beställningsmeningen finns. |
|  |  |  | seo_title | SKS Tom 7 Verktygsset | Multiverktyg SKS Tom 7 |  |
| 8086 | 10541100499210 | RÄTTA | meta | Bladet är av polypropen, impellerhållaren av polyamid och remmen av TPU. | Bladet är av 0,9 mm polypropen och remmen av termoplastisk polyuretan. | 'Impellerhållare' är maskinöversatt (som 'borrningsplatta') och det är oklart vilken del som avses; stryks i meta och specifikation. Mått 375 x 85 mm, 64 g, PP 0,9 mm och TPU stämmer. Ny meta se längd i tabellen. |
|  |  |  | html | &lt;li&gt;Material, impellerhållare: Polyamid (PA) förstärkt med glasfiber&lt;/li&gt; | (tas bort) |  |
| 8088 | 10541328367882 | GODKÄND | | | | Stämmer: damhandskar, förformad tumdesign, förlängd manschett som ersätter kardborrefästet. 'Sitter säkert' och 'slitstark' rätt utelämnade. Cykelhandskar för vuxna är ingen säkerhetsprodukt (jfr 5270). |
| 8089 | 10541366640906 | RÄTTA | meta | Giant Chain Cleaner är en kedjerengöring med integrerad | Giant Chain Cleaner är ett verktyg med integrerad | Cirkulär första mening ('Chain Cleaner är en kedjerengöring'). Användningen stämmer mot källan. Ny meta se längd i tabellen. |
|  |  |  | html | &lt;p&gt;Giant Chain Cleaner är en kedjerengöring med integrerad | &lt;p&gt;Giant Chain Cleaner är ett verktyg för kedjan med integrerad |  |
| 8091 | 10541367755018 | RÄTTA | html |  Handtagen har en slip-on-design och en offset-design.&lt;/p&gt; |  Handtagen har en offset-design.&lt;/p&gt; | Upprepning: 'slip-on-handtag' står redan i meningen före. Övrigt stämmer (silikon, 32 mm, 130 mm, 80 g för 32 mm, 6/5 mm). Stötdämpning och vibrationsreducering rätt utelämnade. |
| 8092 | 10541368606986 | RÄTTA | html |  Enligt tillverkaren ger de ett säkert grepp även i regn.&lt;/p&gt; | &lt;/p&gt; | 'Säkert grepp även i regn' är ett säkerhetslöfte och tas bort även med 'enligt tillverkaren' (jfr 'halkfri' i 3080). 'Världens största cykeltillverkare' rätt utelämnat. Tunn källa, ingen meta. |
| 8093 | 10541369098506 | UNDERKÄND | | | | UNDERKÄND. Två varianter med oförklarade namn (490000099 och 490000095, samma pris); titeln och handtaget säger Svart/Blå men det framgår inte vad 490000095 är (troligen en annan färg). Efter att färgen strukits återstår bara '500–750 ml' – för lite för en säker text, och titeln skiljer sig inte från systerprodukterna. David/leverantören avgör varianterna. |
| 8094 | 10541369393418 | RÄTTA | html | &lt;li&gt;Färg: Svart och Röd&lt;/li&gt; | &lt;li&gt;Färg: Svart och röd&lt;/li&gt; | Stor bokstav gäller bara direkt efter kolon (jfr 'Svart och orange' i 8060). En variant, färg från titeln, 500–750 ml stämmer. Tunn källa, ingen meta. |
| 8095 | 10541370016010 | GODKÄND | | | | Stämmer: UniClip, snabbkopplat, aerodynamisk, kompatibel med Giant Uniclip-sadlar, innerslang/verktyg/reparationskit. Ingen lastgräns i källan och ingen i texten. SEO lika med titeln lagras tom. |
| 8096 | 10548232618250 | RÄTTA | seo_title | Giant Cleanspring Dricksflaska 600 ml | Dricksflaska Giant Cleanspring 600 ml | SEO-titeln har omvänd ordning (märke före typord, jfr 5208); blir lika med titeln och lagras tom. 'Antibakteriell plast' rätt utelämnat, BPA-fri enligt tillverkaren. |

## Öppna frågor till David
1. Stödben/cykelstöd utan lastuppgift (8052, 8056): fortsatt för hand, som 5003/5010?
2. Solglasögon (8076): ska solglasögon generellt räknas som skydd och tas för hand?
3. Giant ARX-flaskorna (5256, 8070–8072): får "enligt tillverkaren designad för barncyklar" stå, eller tas de för hand som barnprodukter?
4. 8093: vad är varianten 490000095 (färg)? 8068: är Giant Road Pro en sadel eller en pedal?
5. 8080: godtas typordet "Multiverktyg" (källans text) i stället för originaltitelns "Verktygsset ... 7 delar"?
