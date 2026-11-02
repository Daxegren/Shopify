# Verifiering våg 2c, resten_2 (Gymstick) – BEST OF SPORTS (2026-11-02)

Oberoende kontroll, endast läsning. Inget ändrat i Shopify, inget committat.

## Metod
- `get-shop-info`: **BEST OF SPORTS**, bestofsports.se, SEK. Rätt butik.
- Sanningen: `vag2_skriv/c_skriv_resten_2.json` (43 produkter, nr 3089–3154). Före-läge: `shopify-original-2026-11-02/vag2c_resten_2_fore.json` (handle, status, taggar).
- Live hämtat med `graphql_query` (`nodes(ids)`, fyra anrop: 15 + 15 + 7 + 6): title, handle, status, tags, seo{title description}, descriptionHtml.
- Leveransblocket ersattes vid avskrift av live-svaret med en platshållare. Blocket lästes i varje live-svar och var identiskt med blocket i `c_1_utkast.json` (Leverans … Säljare, utan FAQ-delen). Alla 43 i skrivfilen har samma block.
- Jämförelse i skript: seo.title förväntas null när seo_title = titel; seo.description null när meta är null. descriptionHtml matchar **tecken för tecken** på alla 43 (även utan normalisering av radbrytningar).
- Taggar: "texter-klara" finns på alla 43; alla taggar från före-filen finns kvar och inga andra har tillkommit.

## Resultat per produkt
Kolumner: titel, seo.title, meta (seo.description), html, status ACTIVE, handle = före, taggen texter-klara finns (och övriga kvar).

| Nr | Id | Titel | SEO-titel | Meta | Html | ACTIVE | Handle | Tagg |
|---|---|---|---|---|---|---|---|---|
| 3089 | 10581106065674 | ja | ja | ja | ja | ja | ja | ja |
| 3090 | 10581106098442 | ja | ja | ja | ja | ja | ja | ja |
| 3091 | 10581106131210 | ja | ja | ja | ja | ja | ja | ja |
| 3092 | 10581106163978 | ja | ja | ja | ja | ja | ja | ja |
| 3093 | 10581106196746 | ja | ja | ja | ja | ja | ja | ja |
| 3096 | 10581106360586 | ja | ja | ja | ja | ja | ja | ja |
| 3097 | 10581106393354 | ja | ja | ja | ja | ja | ja | ja |
| 3099 | 10581106458890 | ja | ja | ja | ja | ja | ja | ja |
| 3104 | 10581106655498 | ja | ja | ja | ja | ja | ja | ja |
| 3105 | 10581106688266 | ja | ja | ja | ja | ja | ja | ja |
| 3106 | 10581106753802 | ja | ja | ja | ja | ja | ja | ja |
| 3107 | 10581106786570 | ja | ja | ja | ja | ja | ja | ja |
| 3108 | 10581106819338 | ja | ja | ja | ja | ja | ja | ja |
| 3109 | 10581106852106 | ja | ja | ja | ja | ja | ja | ja |
| 3110 | 10581106884874 | ja | ja | ja | ja | ja | ja | ja |
| 3113 | 10581107015946 | ja | ja | ja | ja | ja | ja | ja |
| 3118 | 10581107245322 | ja | ja | ja | ja | ja | ja | ja |
| 3119 | 10581107278090 | ja | ja | ja | ja | ja | ja | ja |
| 3120 | 10581107310858 | ja | ja | ja | ja | ja | ja | ja |
| 3121 | 10581107409162 | ja | ja | ja | ja | ja | ja | ja |
| 3122 | 10581107441930 | ja | ja | ja | ja | ja | ja | ja |
| 3123 | 10581107540234 | ja | ja | ja | ja | ja | ja | ja |
| 3124 | 10581107671306 | ja | ja | ja | ja | ja | ja | ja |
| 3125 | 10581107704074 | ja | ja | ja | ja | ja | ja | ja |
| 3126 | 10581107769610 | ja | ja | ja | ja | ja | ja | ja |
| 3131 | 10581107998986 | ja | ja | ja | ja | ja | ja | ja |
| 3132 | 10581108031754 | ja | ja | ja | ja | ja | ja | ja |
| 3133 | 10581108064522 | ja | ja | ja | ja | ja | ja | ja |
| 3135 | 10581108162826 | ja | ja | ja | ja | ja | ja | ja |
| 3136 | 10581108195594 | ja | ja | ja | ja | ja | ja | ja |
| 3141 | 10581108490506 | ja | ja | ja | ja | ja | ja | ja |
| 3142 | 10581108556042 | ja | ja | ja | ja | ja | ja | ja |
| 3144 | 10581108621578 | ja | ja | ja | ja | ja | ja | ja |
| 3145 | 10581108654346 | ja | ja | ja | ja | ja | ja | ja |
| 3146 | 10581108687114 | ja | ja | ja | ja | ja | ja | ja |
| 3147 | 10581108719882 | ja | ja | ja | ja | ja | ja | ja |
| 3148 | 10581108883722 | ja | ja | ja | ja | ja | ja | ja |
| 3149 | 10581108916490 | ja | ja | ja | ja | ja | ja | ja |
| 3150 | 10581108949258 | ja | ja | ja | ja | ja | ja | ja |
| 3151 | 10581108982026 | ja | ja | ja | ja | ja | ja | ja |
| 3152 | 10581109014794 | ja | ja | ja | ja | ja | ja | ja |
| 3153 | 10581109047562 | ja | ja | ja | ja | ja | ja | ja |
| 3154 | 10581109080330 | ja | ja | ja | ja | ja | ja | ja |

**43 av 43 matchar exakt. Inga avvikelser mellan skrivfil och live.**

## Gränser
- Titel: 20–69 tecken (≤70). Kommatecken högst 2 i alla. 3133 "Gymmatta Gymstick Interlocking Mat Pro, 102,7 x 102,7 x 2,2 cm, Svart" (69 tecken) har 5 kommatecken enligt skriptet, varav 3 är decimalkomman i mått, alltså 2 avskiljare. Godkänt enligt undantaget.
- SEO-titel: 20–43 tecken (≤43). Längst: 3148 "Medicinboll Gymstick Medicine Ball, Handtag" (43, på gränsen).
- Meta: 130–155 tecken där den finns (3099 = 130 och 3092/3106 = 155, på gränserna). Null på 3089, 3146, 3147, 3153, 3154.
- Dubbletter: inga av titel, SEO-titel eller meta inom filen eller mot övriga `c_skriv_*.json` (samma produkt i flera filer räknas inte).

## Kontrollskriptet
`kontrollera_produkttext.py --seo-title-max 43 --seo-suffix " – BEST OF SPORTS"` på en kopia (html → beskrivning, leveransblocket i `[[STANDARDBLOCK]]…[[/STANDARDBLOCK]]`). Kördes två gånger: med före-filens text (titel, taggar, beskrivning) som källa och med `fakta` från `c_*_utkast.json`.

- **0 FEL** i båda körningarna, 51 varningar.
- Varningar: 43 × rubriken heter "Passar för" och inte "Passar dig som" (samma i hela våg 2, känt); kort text 3089 (36 ord), 3096 (33), 3146 (25); titelkomma 3133 (decimalkomman, se ovan); engelska ordet "with" i 3144 och 3148 (del av produktnamnet, godtas).

## Språkgranskning
Inga hälso-, miljö- eller ursprungspåståenden, inga priser, inga arbetstermer ("enligt källan/titeln"), ingen FAQ. Alla rehab-, återhämtnings-, blodcirkulations- och miljöpåståenden i källan är utelämnade. Varje första metamening har verb. Inga stavfel hittades. Fynden nedan är förbättringar, inga fel som kräver omskrivning i butiken. Ändringar i live-texten kräver Davids beslut.

| Nr | Fält | Fynd | Före | Efter (förslag) |
|---|---|---|---|---|
| 3091 | meta | Onödigt kommatecken och omvänd ordföljd i första meningen | Två träningsbollar från Gymstick ingår, och de väger 1 kg vardera. | Förpackningen innehåller två träningsbollar från Gymstick som väger 1 kg vardera. |
| 3093 | html spec | Olika stavning mot titeln ("Miniband") | Typ: Motståndsband (mini-band) | Typ: Motståndsband (miniband) |
| 3096 | meta | Ojämn samordning ("både för … och efter …") | Enligt tillverkaren används rullen både för stretching och efter träningspasset. | Enligt tillverkaren används rullen för stretching och efter träningspasset. |
| 3097 | meta + html | Engelsk pluralform | tre fingerexpanders | tre fingerexpandrar |
| 3104 | html intro | Dubbelt "är" | Gymstick golvskyddsmatta är 250 x 80 x 0,6 cm och är avsedd att skydda … | Gymstick golvskyddsmatta mäter 250 x 80 x 0,6 cm och är avsedd att skydda … |
| 3105 | html intro | Dubbelt "är" | Gymstick golvskyddsmatta är 200 x 100 x 0,6 cm och är avsedd att skydda … | Gymstick golvskyddsmatta mäter 200 x 100 x 0,6 cm och är avsedd att skydda … |
| 3110 | html passar 1 | "träna stretching/intensiva pass" haltar | Dig som vill träna yoga, stretching eller intensiva pass, enligt tillverkaren | Dig som vill ha en matta för yoga, stretching eller intensiva pass, enligt tillverkaren |
| 3113 | html intro | "var" behöver "än" i betydelsen överallt | … löprundan eller var du behöver dricka vatten. | … löprundan eller var du än behöver dricka vatten. |
| 3126 | meta | Två "och" i rad | … mindre träningsredskap och har en fackindelning. | … mindre träningsredskap. Den har fackindelning. (meta blir 141 tecken) |
| 3126 | html passar 1 | Saknar artikel | Dig som ska till gymmet, en träningsklass eller utomhuspass, enligt tillverkaren | Dig som ska till gymmet, en träningsklass eller ett utomhuspass, enligt tillverkaren |
| 3132 | meta + html intro | Saknar "med" | … är ett set sammanfogbara mattor. | … är ett set med sammanfogbara mattor. |
| 3135 | html intro | Upprepning av "kettlebellträning" i två meningar | … och tål belastningen från kettlebellträning. | … och tål belastningen från träningen. (som i meta) |
| 3144 | html spec | Raden anger en egenskap, inte ett material (samma mönster som i c_19/c_20) | Material enligt tillverkaren: Slitstarkt material | Egenskaper: Slitstarkt material, enligt tillverkaren |
| 3147 | html intro | Saknar kommatecken före tillskrivningen | … avsedda för användning efter träning enligt tillverkaren. | … avsedda för användning efter träning, enligt tillverkaren. |
| 3148 | seo_title | "Medicinboll … Medicine Ball, Handtag" dubblerar typordet och kommat haltar | Medicinboll Gymstick Medicine Ball, Handtag | Medicinboll Gymstick med Handtag (= titeln, lagras då tom) |
| 3150 | html intro | Dubbelt "med" och "motstånd" | … ett set med fyra motståndsband med olika motståndsnivåer. | … ett set med fyra motståndsband i olika motståndsnivåer. |
| 3150 | meta | Saknar "allt från" | … och passar nybörjare till avancerade. | … och passar allt från nybörjare till avancerade. (meta blir 158 tecken, över 155; alternativt "passar alla nivåer") |
| 3152 | meta | "passar för … mild utmaning" haltar | Enligt tillverkaren passar det för uppvärmning och mild utmaning. | Enligt tillverkaren passar det för uppvärmning och som en mild utmaning. (150 tecken) |

**Mönster (ingen ändring krävs, men värt att ta ställning till):**
1. **Nästan cirkulära förstameningar** där det engelska namnet följs av sin översättning: 3141 "Leather Ankle Strap är en ankelrem i äkta läder", 3142 "Leather Jump Rope är ett hopprep i läder", 3145 "Lifting Straps Leather är lyftremmar i läder", 3148/3149 "Medicine Ball … är en medicinboll". De tillför material eller användning och är därför inte rent cirkulära. Förslag om skärpning, till exempel 3149: "Gymstick Medicine Ball är en medicinboll för kast, rotationer och styrkepass." → "Gymstick Medicine Ball används till kast, rotationer och styrkepass."
2. **Typord som avviker från resten av vågen:** 3121 "Krita Gymstick Gym Chalk" medan 2108, 2109, 2213 och 3273 använder "Gymtalk" (standarden avsnitt 11); 3099 "Fitnessboll" medan alla andra bollar och specraden i 3099 själv heter "Träningsboll"; 3093 "Miniband" medan 3150–3152 heter "Motståndsband … Mini Band"; 3131 "sammanfogbar" och 3133 "sammankopplingsbar" om samma matta.
3. **Endast en punkt under "Passar för"** (standarden 2–3): 3089, 3141, 3146. Tunna källor, godtas.
4. **Tomma rader i listor** (`<ul>\n\n<li>` eller `</li>\n\n</ul>`) i 3089, 3092, 3093, 3096, spår av borttagna punkter. Syns inte för kunden.
5. **Meta = första stycket ordagrant** i 3118, 3122, 3124, 3125, 3141, 3142, 3148. Tillåtet, men ger inget extra i sökresultatet.

## Ändrat
Inget. Bara läsning i Shopify; rapporten är den enda nya filen. Hjälpfiler (live-avskrift, kopior för skriptet) ligger i scratchpad och är inte en del av repot.
