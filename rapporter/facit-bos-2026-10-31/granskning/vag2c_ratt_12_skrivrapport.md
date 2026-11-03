# Våg 2c, språkrättning Gymstick (rättning 1 och 2) – skrivrapport 2026-11-03

Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info. Underlag: `verifiering_gymstick_1.md` och `verifiering_gymstick_2.md` (kontrollanternas fynd), skrivfilerna `vag2_skriv/c_skriv_kanarie.json`, `c_skriv_resten_1.json`, `c_skriv_resten_2.json` (nu uppdaterade så de stämmer med live; JSON är sanningen). Före-fil från den avbrutna körningen, `shopify-original-2026-11-02/vag2c_ratt_12_fore.json` (40 produkter, live före rättning), lämnades orörd; läget vid start av denna körning ligger i `vag2c_ratt_12_fore_2.json`.

## Läge vid omstart (läst live före skrivning)
- Den avbrutna körningen hade skrivit 3006 (html rättad i båda punkterna) och 3103 (html rättad "mäter", men metabeskrivningen fortfarande "är"). Båda hade alltså fortfarande status ACTIVE och oförändrade handle och taggar.
- 3006: live lika med nya texten, skrevs inte igen. 3103: html lämnades, bara seo (titel + beskrivning) skrevs.
- Övriga 39 produkter: live lika med skrivfilen före rättning (jämfört för hand, fält för fält) och skrevs.
- Inga produkter skilde sig från både skrivfilen och den nya texten, så inget hoppades över av det skälet.

## Resultat
41 produkter berörda: 40 skrivna i denna körning (3 kanarier först: 3001, 3148, 3016, återlästa, därefter batcher om 8; 3103 bara seo), 1 redan rättad (3006, ej skriven). userErrors: inga i någon batch. 51 rättade textställen (tabell nedan).

## Före och efter per ställe
| Nr | Fält | Före | Efter |
|---|---|---|---|
| 3001 | Text | Gymstick träningsboll i svart PVC, 65 cm. Bollen | Gymstick träningsboll är 65 cm och gjord av svart PVC. Bollen |
| 3004 | Text | Gymstick medicinboll på 4 kg med handtag. | Gymstick medicinboll väger 4 kg och har handtag. |
| 3005 | Text | Gymstick hopprep i läder, 2,75 m långt, med handtag i skumgummi. | Gymstick hopprep är gjort av läder, är 2,75 m långt och har handtag i skumgummi. |
| 3006 | Text (redan rättad live före min körning, skrevs ej igen) | Gymstick Aktiv 2-toners träningsmatta i blått och svart. | Gymstick Aktiv är en 2-toners träningsmatta i blått och svart. |
| 3006 | Text (redan rättad live före min körning, skrevs ej igen) | kan hjälpa dig att positionera dig under övningar | kan hjälpa dig att hitta rätt position under övningarna |
| 3007 | Meta | tränas händer, underarmar och greppstyrka. | tränar den upp händer, underarmar och grepp. |
| 3008 | Meta | är två ankel- och handledsvikter på 1 kg vardera. | är ett par ankel- och handledsvikter på 1 kg styck. |
| 3008 | Text | är två ankel- och handledsvikter på 1 kg vardera. | är ett par ankel- och handledsvikter på 1 kg styck. |
| 3010 | Text | Gymstick Active Exercise Ball är en träningsboll på 65 cm. | Gymstick Active Exercise Ball är en 65 cm stor träningsboll för övningar inom kärnstyrka, balans och stretching, enligt tillverkaren. |
| 3011 | Text | Gymstick Active Exercise Ball är en träningsboll med diametern 75 cm. | Gymstick Active Exercise Ball är en träningsboll med diametern 75 cm för core-träning, stretching och yoga, enligt tillverkaren. |
| 3012 | Meta | är två fingerexpandrar för händer och fingrar. | är ett set med två fingerexpandrar. |
| 3013 | Meta | har de mjuk och | har de en mjuk och |
| 3016 | Meta | är två kompakta motståndsband. | är ett set om två motståndsband. |
| 3018 | Text | Dig som vill ha en boll för pilatesövningar   Dig som vill ha en boll för styrkeövningar | Dig som vill göra pilates- eller styrkeövningar |
| 3018 | Text | Gymstick Active Pilates Ball är en pilatesboll i storlek 20 cm, avsedd för övningar | Gymstick Active Pilates Ball på 20 cm används för övningar |
| 3019 | Text | Dig som vill ha ett motståndsband för uppvärmning   Dig som vill ha ett motståndsband för styrketräning hemma eller på gymmet | Dig som vill ha ett motståndsband för uppvärmning och styrketräning hemma eller på gymmet |
| 3024 | Text | Material: Slitstarkt, enligt tillverkaren | Egenskaper: Slitstarkt material, enligt tillverkaren |
| 3025 | Text | Dig som vill ha en träningsmatta för yoga   Dig som vill ha en träningsmatta för styrketräning   Dig som vill ha en matta för både hemmabruk och gymmet | Dig som vill ha en matta för allt från yoga till styrketräning   Dig som tränar hemma eller på gymmet |
| 3026 | Meta | har ergonomiskt grepp och halkfri yta | har ett ergonomiskt grepp och en halkfri yta |
| 3026 | Text | har de ergonomiskt grepp och halkfri yta | har de ett ergonomiskt grepp och en halkfri yta |
| 3039 | Text | för hemmakvällen och för träningspass | för spelkvällar hemma och för träningspass |
| 3040 | Text | både på träning och i tävling | både på träning och på tävling |
| 3041 | Text | eller på resan, enligt | eller på resor, enligt |
| 3055 | Text | Gymstick Hand Grip är en handtränare i aluminium. | Gymstick Hand Grip används för att träna grepp och underarmar. Den är gjord av aluminium. |
| 3057 | Text | Gymstick Ankle/Wrist Weight är ankel- och handledsvikter, 2 x 1 kg. | Gymstick Ankle/Wrist Weight bärs runt anklar eller handleder. Setet består av två vikter på 1 kg vardera. |
| 3059 | Text | Gymstick Anti-Stress Ball är stressbollar som säljs tre i förpackningen. | Gymstick Anti-Stress Ball säljs i förpackningar om tre. Enligt tillverkaren är bollarna mjuka och formbara. |
| 3060 | Text | Gymstick Ankle/Wrist Weight är ankel- och handledsvikter, 2 x 2 kg. | Gymstick Ankle/Wrist Weight ger extra motstånd vid löpning, gång och styrketräning, enligt tillverkaren. Setet består av två vikter på 2 kg vardera. |
| 3091 | Meta | Två träningsbollar från Gymstick ingår, och de väger 1 kg vardera. | Två träningsbollar från Gymstick väger 1 kg vardera. |
| 3093 | Text | (mini-band) | (miniband) |
| 3096 | Meta | både för stretching och efter | för stretching och efter |
| 3097 | Meta | tre fingerexpanders | tre fingerexpandrar |
| 3097 | Text | tre fingerexpanders | tre fingerexpandrar |
| 3103 | Meta | Gymstick golvskyddsmatta är 160 x 80 x 0,6 cm. | Gymstick golvskyddsmatta mäter 160 x 80 x 0,6 cm. (html var redan rättad live) |
| 3104 | Meta | Gymstick golvskyddsmatta är 250 | Gymstick golvskyddsmatta mäter 250 |
| 3104 | Text | Gymstick golvskyddsmatta är 250 x 80 x 0,6 cm och är | Gymstick golvskyddsmatta mäter 250 x 80 x 0,6 cm och är |
| 3105 | Meta | Gymstick golvskyddsmatta är 200 | Gymstick golvskyddsmatta mäter 200 |
| 3105 | Text | Gymstick golvskyddsmatta är 200 x 100 x 0,6 cm och är | Gymstick golvskyddsmatta mäter 200 x 100 x 0,6 cm och är |
| 3110 | Text | Dig som vill träna yoga, stretching eller intensiva pass | Dig som vill ha en matta för yoga, stretching eller intensiva pass |
| 3113 | Text | eller var du behöver dricka vatten | eller var du än behöver dricka vatten |
| 3126 | Meta | mindre träningsredskap och har en fackindelning. | mindre träningsredskap. Den har fackindelning. |
| 3126 | Text | en träningsklass eller utomhuspass | en träningsklass eller ett utomhuspass |
| 3132 | Meta | är ett set sammanfogbara mattor | är ett set med sammanfogbara mattor |
| 3132 | Text | är ett set sammanfogbara mattor | är ett set med sammanfogbara mattor |
| 3135 | Text | tål belastningen från kettlebellträning. | tål belastningen från träningen. |
| 3144 | Text | Material enligt tillverkaren: Slitstarkt material (rad) + Egenskaper: Extra vaddering (rad) | Egenskaper: Extra vaddering och slitstarkt material, enligt tillverkaren (en rad) |
| 3147 | Text | efter träning enligt tillverkaren. | efter träning, enligt tillverkaren. |
| 3148 | SEO-titel | Medicinboll Gymstick Medicine Ball, Handtag | Medicinboll Gymstick med Handtag |
| 3149 | Text | Gymstick Medicine Ball är en medicinboll för kast, rotationer och styrkepass. | Gymstick Medicine Ball används till kast, rotationer och styrkepass. |
| 3150 | Text | med fyra motståndsband med olika motståndsnivåer | med fyra motståndsband i olika motståndsnivåer |
| 3150 | Meta | passar nybörjare till avancerade. | passar alla nivåer. |
| 3152 | Meta | passar det för uppvärmning och mild utmaning. | passar det för uppvärmning och som en mild utmaning. |

Utöver kontrollanternas exakta förslag: 3016 meta blev "ett set om två motståndsband" (kontrollantens "ett set med två kompakta" blev 165 tecken, "kompakta" stryks och "set om" används, 155 tecken), 3150 meta "passar alla nivåer" (kontrollantens alternativ), 3012 meta strök "för händer och fingrar" (som kontrollanten föreslog). 3144 fick en sammanslagen rad eftersom "Egenskaper:" annars hade stått två gånger. 3055 och 3103 ingick i den avbrutna körningens lista (cirkulär förstamening respektive samma "är … och är"-mönster som 3104 och 3105).

## Lämnat orört (och varför)
- Rena stilönskemål utan fel: 3013 och 3080 ("enligt tillverkaren" fem gånger), 3010/3011/3086/3088 ("kärnstyrka" mot "core-träning"), 3006 "2-toners" (ordet finns i originaltiteln), 3092 m.fl. tomma rader i listor (syns inte för kunden), meta lika med första stycket (3118, 3122, 3124, 3125, 3141, 3142, 3148), en enda punkt under "Passar för" (3089, 3141, 3146; tunn källa).
- Nästan cirkulära förstameningar som kontrollanterna själva godtog eftersom de tillför material, mått eller användning: 3021, 3027, 3030, 3056, 3141, 3142, 3145. De rättade (3001, 3010, 3011, 3018, 3055, 3057, 3059, 3060, 3149) fick bara uppgifter som redan stod i produktens text.
- Metabeskrivningarna på 3010, 3011 och 3018 börjar fortfarande "… är en träningsboll/pilatesboll …" (med mått, andra meningen bär information). Rättning hade gett meta under 130 tecken eller nya fakta.
- Typord lyfts, rättades inte: 3121 "Krita" mot "Gymtalk" (2108, 2109, 2213, 3273), 3099 "Fitnessboll" mot "Träningsboll", 3093 "Miniband" mot "Motståndsband … Mini Band" (3150–3152), 3131 "sammanfogbar" mot 3133 "sammankopplingsbar". Beslut av David behövs. Produktnamn och typ ändrades inte.

## Kontroll
Maskinellt (på kopia med html mappad till beskrivning, standardblocket i `[[STANDARDBLOCK]]`, `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS"`): 41 produkter, **0 FEL**, 52 varningar (samma kända som före: rubriken "Passar för", kort text, "with" i produktnamn). Meta 130–155 tecken eller null, SEO-titel högst 43, titel högst 70, inga dubbletter av titel, SEO-titel eller meta över alla c_skriv_*-filer och a_skriv.json (skript).
För hand: live läst före skrivning för alla 41 och jämfört mot skrivfilen; efter skrivning lästes alla 41 tillbaka (title, handle, status, tags, seo.title, seo.description, descriptionHtml) och jämfördes mot den nya texten. Resultat: titel, handle (oförändrade), status ACTIVE, taggar (inklusive texter-klara och övriga) och all text lika med nya texten. Standardblocket oförändrat. SEO-titel som blev lika med titeln (3148) lagrades som null av Shopify (avsett). Observera att jämförelsen av MCP-svar gjordes för hand (utdata kan inte diffas i bash).

## Ändrat
Shopify: 40 produkter skrivna (3103 bara seo). Handle, status och taggar ändrades inte. Filer: de tre skrivfilerna, `vag2c_ratt_12_fore_2.json` (ny), denna rapport (ny). Ingenting committat. Den ursprungliga före-filen `vag2c_ratt_12_fore.json` är orörd.
