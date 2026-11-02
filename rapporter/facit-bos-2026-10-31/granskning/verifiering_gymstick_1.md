# Verifiering Gymstick (kanarie + resten 1) – BEST OF SPORTS, 2026-11-02

Oberoende kontroll. Bara läsning: inget har ändrats i Shopify och inget har committats.

## Metod
- `get-shop-info`: BEST OF SPORTS, bestofsports.se, SEK, Basic. Det är rätt butik.
- Skrivfiler: `vag2_skriv/c_skriv_kanarie.json` (3 produkter: 3006, 3038, 3103) och `vag2_skriv/c_skriv_resten_1.json` (43 produkter). Totalt 46 unika id.
- Före-filer (handle, status och taggar före skrivningen): `shopify-original-2026-11-02/vag2c_resten_1_fore.json` (43) och, för kanarien, `shopify-original-2026-11-02/vag2c_kanarie_fore.json` (3).
- Live-läget hämtades med `graphql_query` `nodes(ids)` i tre anrop (20 + 20 + 6). Fälten var title, handle, status, tags, seo{title description} och descriptionHtml. Svaren skrevs av till en lokal kopia, där leveransblocket ersattes med en platshållare. Jämförelsen gjordes sedan med program mot skrivfilerna. Leveransblocket lästes i alla 46 live-svar och var identiskt med blocket i `c_1_utkast.json`.
- Förväntat: seo.title är null när seo_title = titel, och seo.description är null när meta är null.
- descriptionHtml matchar på tecknet. Radbrytningarna mellan `<li>` finns både live och i skrivfilen, så ingen normalisering behövdes.
- Extra kontroll: variantlistan för 3070 och 3061 lästes för att belägga "finns i flera varianter" (3070 har 10/12/14 oz, 3061 har 12/14 oz).

## Resultat per produkt
Alla 46 matchar i alla fält.

| nr | id | titel | seo.title | seo.description | html | status ACTIVE | handle | texter-klara | övriga taggar kvar |
|---|---|---|---|---|---|---|---|---|---|
| 3006 | 10581095743754 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3038 | 10581101084938 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3103 | 10581106622730 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3001 | 10411728240906 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3004 | 10472282456330 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3005 | 10472282489098 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3007 | 10581095809290 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3008 | 10581095842058 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3010 | 10581095940362 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3011 | 10581095973130 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3012 | 10581096005898 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3013 | 10581096038666 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3014 | 10581096104202 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3015 | 10581096169738 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3016 | 10581096235274 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3017 | 10581096333578 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3018 | 10581096399114 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3019 | 10581096464650 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3020 | 10581096497418 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3021 | 10581096530186 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3023 | 10581096595722 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3024 | 10581096694026 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3025 | 10581096759562 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3026 | 10581096923402 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3027 | 10581096956170 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3028 | 10581096988938 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3030 | 10581100331274 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3031 | 10581100364042 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3039 | 10581101117706 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3040 | 10581101281546 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3041 | 10581101609226 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3055 | 10581104525578 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3056 | 10581104558346 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3057 | 10581104591114 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3059 | 10581104656650 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3060 | 10581104689418 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3061 | 10581104722186 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3069 | 10581105017098 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3070 | 10581105049866 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3074 | 10581105443082 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3076 | 10581105574154 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3080 | 10581105737994 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3082 | 10581105836298 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3085 | 10581105934602 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3086 | 10581105967370 | ja | ja | ja | ja | ja | ja | ja | ja |
| 3088 | 10581106032906 | ja | ja | ja | ja | ja | ja | ja | ja |

## Avvikelser mot skrivfilen
Inga. På alla 46 produkter stämmer title, seo.title, seo.description, descriptionHtml, status ACTIVE och handle (samma som före). Taggen "texter-klara" finns och alla taggar från före-läget finns kvar.

## Gränser (steg 4)
- Titel: högst 53 tecken (3006) och högst 2 kommatecken. Decimalkommatecken (0,6 och 2,75) räknas inte. Ingen överskrider gränsen.
- SEO-titel: högst 42 tecken (3040, 3069). Alla 46 ligger på 43 tecken eller färre, också där SEO-titeln är lika med titeln.
- Meta: 24 har meta, med 131–154 tecken. 22 har meta = null. Ingen ligger utanför 130–155.
- Dubbletter: inga av titel, SEO-titel eller meta inom de 46. Inga heller mot övriga `c_skriv_*.json` (resten_2–4, c_skriv.json, c_skriv_resten.json; samma id räknas inte). Ingen dubblett heller av den SEO-titel som faktiskt visas (SEO-titeln, annars titeln) bland alla 173 produkter i c_skriv-filerna.

## Kontrollskriptet (steg 5)
Körningen: `kontrollera_produkttext.py kopia.json --seo-title-max 43 --seo-suffix " – BEST OF SPORTS"`. I kopian är html mappad till beskrivning och standardblocket omgivet av [[STANDARDBLOCK]]…[[/STANDARDBLOCK]]. Källtexten är före-filens titel plus beskrivningen som ren text.

**46 produkter, 0 FEL, 69 VARNINGAR.**
- "saknar avsnittet 'passar dig som'": 46 av 46. Rubriken är "Passar för", vilket är känt och godtaget.
- "beskrivning_langd" under 40 ord: 19 produkter (3004, 3005, 3010, 3011, 3014, 3015, 3017, 3020, 3021, 3023, 3026, 3027, 3055, 3056, 3061, 3069, 3070, 3074, 3088). Källan är tunn.
- "saknar avsnittet 'specifikationer'": 3014. Källan saknar specifikationer.
- "engelska_ord: Pink": 3074, i titel, SEO-titel och beskrivning. Färgnamnet kommer från originaltiteln.

## Språkgranskning (steg 6)
Inget fynd stoppar texterna. Alla är små förbättringar som kan tas i en senare rättningsvåg.

**Påhittade fakta:** inga hittades. Påståenden som kontrollerades mot källtexten: kontoret/stol (3001), "var du än befinner dig" (3016), "på resande fot" (3028), "hemmakvällen" (3039), "träning och lek" och "lättmonterat" (3031), idrottsövningar och justerbar höjd (3069), stötdämpning (3080), pilatesboll (3086), hemmaträning (3026), tävling (3076), halverad pumptid (3082), benspark och glute bridges (3056), marklyft och frivändningar (3013), "flera varianter" (3070, belagt via varianterna). Alla har stöd. Källans hälso- och miljöpåståenden ("miljövänlig", "lindra stress och ångest", "rehabilitering") har inte förts in. Det är rätt.
**Arbetstermer** ("enligt källan", "enligt titeln" och liknande): inga.
**FAQ:** bara 3001. Båda svaren har stöd i källan (storleksguiden 164–180 cm/65 cm, träningsguide och handpump).

| # | nr | Fält | Före | Efter (förslag) | Typ |
|---|---|---|---|---|---|
| 1 | 3006 | html, första meningen | Gymstick Aktiv 2-toners träningsmatta i blått och svart. | Gymstick Aktiv är en 2-toners träningsmatta i blått och svart. | Verb saknas |
| 2 | 3001 | html, första meningen | Gymstick träningsboll i svart PVC, 65 cm. | Gymstick träningsboll är 65 cm och gjord av svart PVC. | Verb saknas |
| 3 | 3004 | html, första meningen | Gymstick medicinboll på 4 kg med handtag. | Gymstick medicinboll väger 4 kg och har handtag. | Verb saknas |
| 4 | 3005 | html, första meningen | Gymstick hopprep i läder, 2,75 m långt, med handtag i skumgummi. | Gymstick hopprep är gjort av läder, är 2,75 m långt och har handtag i skumgummi. | Verb saknas |
| 5 | 3007 | meta, andra meningen | Enligt tillverkaren tränas händer, underarmar och greppstyrka. | Enligt tillverkaren tränar den upp händer, underarmar och grepp. | Passiv form utan subjekt; "träna greppstyrka" är en ovanlig ordförbindelse |
| 6 | 3008 | meta och html | Gymstick Aktiv är två ankel- och handledsvikter på 1 kg vardera. | Gymstick Aktiv är ett par ankel- och handledsvikter på 1 kg styck. | Otymplig konstruktion |
| 7 | 3012 | meta | Gymstick Active Finger Expander Set är två fingerexpandrar för händer och fingrar. | Gymstick Active Finger Expander Set är ett set med två fingerexpandrar för händer och fingrar. | Samma som 6 (153 tecken efter ändring, inom gränsen) |
| 8 | 3016 | meta | Gymstick Active Mini Bands är två kompakta motståndsband. | Gymstick Active Mini Bands är ett set med två kompakta motståndsband. | Samma som 6. Kontrollera längden: blir 165 tecken och måste kortas, till exempel genom att stryka "kompakta" |
| 9 | 3013 | meta | har de mjuk och greppvänlig yta | har de en mjuk och greppvänlig yta | Artikel saknas (152 tecken efter ändring) |
| 10 | 3026 | meta och html | har ergonomiskt grepp och halkfri yta | har ett ergonomiskt grepp och en halkfri yta | Artiklar saknas. Meta blir 145 tecken |
| 11 | 3006 | html, punkt | kan hjälpa dig att positionera dig under övningar | kan hjälpa dig att hitta rätt position under övningarna | Anglicism |
| 12 | 3024 | html, specifikation | Material: Slitstarkt, enligt tillverkaren | Egenskaper: Slitstarkt material, enligt tillverkaren | "Slitstarkt" är inget material |
| 13 | 3041 | html, punkt | Dig som vill träna hemma eller på resan, enligt tillverkaren | Dig som vill träna hemma eller på resor, enligt tillverkaren | Ordagrann översättning |
| 14 | 3039 | html | Setet passar för hemmakvällen och för träningspass. | Setet passar för spelkvällar hemma och för träningspass. | Ordagrann översättning |
| 15 | 3059 | html, första meningen | Gymstick Anti-Stress Ball är stressbollar som säljs tre i förpackningen. | Gymstick Anti-Stress Ball är stressbollar som säljs i förpackningar om tre. | Ordval |
| 16 | 3040 | html, punkt | både på träning och i tävling | både på träning och på tävling | Prepositionerna är inte parallella |
| 17 | 3025 | html, Passar för | Dig som vill ha en träningsmatta för yoga / Dig som vill ha en träningsmatta för styrketräning / Dig som vill ha en matta för både hemmabruk och gymmet | Dig som vill ha en matta för allt från yoga till styrketräning / Dig som tränar hemma eller på gymmet | Upprepning: tre nästan likadana punkter, och första meningen och specifikationen säger samma sak |
| 18 | 3018, 3019 | html, Passar för | Dig som vill ha en boll för pilatesövningar / Dig som vill ha en boll för styrkeövningar (3019 på samma sätt med uppvärmning och styrketräning) | Dig som vill göra pilates- eller styrkeövningar | Upprepning |
| 19 | 3013 | html, specifikation | Passform: De flesta skivstänger och hantlar, enligt tillverkaren | Passform: De flesta skivstänger och hantlar | "enligt tillverkaren" står 5 gånger i produkten (meta + html), och samma sak står redan i punkten ovanför. 3080 har också 5 förekomster |
| 20 | 3010, 3011, 3018, 3021, 3027, 3030, 3055, 3056, 3057, 3059, 3060 | html, första meningen | Till exempel "Gymstick Active Pilates Ball är en pilatesboll i storlek 20 cm" och "Gymstick Ankle/Wrist Weight är ankel- och handledsvikter, 2 x 1 kg" | Godtas, eller skrivs om så att meningen säger något mer än en översättning av det engelska namnet, till exempel "Gymstick Active Pilates Ball är 20 cm och avsedd för …" | Nästan cirkulärt: det engelska modellnamnet följs av sin svenska översättning. Källan är tunn, så det är godtagbart |
| 21 | 3010 och 3011/3086/3088 | meta och html | "kärnstyrka" (3010) och "core-träning" (övriga) | Välj ett av orden | Olika termer för samma sak |
| 22 | 3006 | titel och SEO-titel | 2-toners | (valfritt) tvåfärgad | Lån från engelska. Ordet finns i originaltiteln, så fyndet kan godtas |

Granskningen är gjord för hand av en granskare. Påståendena har stämts av mot före-filernas källtext.
