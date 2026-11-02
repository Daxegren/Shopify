# Granskning våg 2, utkast c_9–c_12 – BEST OF SPORTS (2026-11-02)

Oberoende granskning. Jag har bara läst i Shopify och inte ändrat någon utkastsfil. Butiken kontrollerades först med get-shop-info: **BEST OF SPORTS** (bestofsports.se, SEK).

**Underlag:** `vag2_skriv/c_9_utkast.json` (10), `c_10_utkast.json` (12), `c_11_utkast.json` (11) och `c_12_utkast.json` (11), alltså 44 utkast, nr 3121–3180. Avvisade: `c_9_avvisade.json`–`c_12_avvisade.json` (16 st). Standarden (`produkttexter-standard.md` avsnitt 1–11), `LARDOMAR.md` och `vag2_a_granskning_2.md` för formatet.

**Metod:**
- **Källan live:** title, handle, status, productType, vendor, tags, descriptionHtml, seo och variants hämtades med graphql_query (`nodes`) i fyra batchar om 11. Alla 44 är ACTIVE, vendor Gymstick, productType tom (utkasten ändrar den inte) och seo.title/description tomma. Fältet `fakta` stämmer med live-källan för alla 44. Några `fakta` kortar källans sista mening (till exempel 3136, 3142, 3166), men inget i utkasten bygger på den bortkortade texten utan stöd.
- **Maskinellt (skript i min scratchpad, inte kontrollskriptet):** längder, kommatecken, standardblock och dubbletter av titel och SEO-titel mot alla `c_*_utkast.json` (och för de nya SEO-titlarna även mot `a_*_utkast.json`). Standardblocket är **exakt** detsamma som i `c_1_utkast.json` i alla 44, utan fraktavgift i kronor. Ingen av produkterna har taggen "På beställning".
- **För hand:** varje titel, SEO-titel, meta och html lästes mot live-källan och språkgranskades.

## Resultat i korthet

| Kategori | Antal | Nr |
|---|---|---|
| GODKÄND | 26 | 3122, 3124, 3125, 3126, 3141, 3145, 3146, 3147, 3149, 3150, 3151, 3152, 3153, 3154, 3156, 3157, 3161, 3165, 3167, 3168, 3174, 3175, 3176, 3177, 3178, 3180 |
| RÄTTA | 13 | 3121, 3123, 3131, 3132, 3133, 3135, 3136, 3142, 3144, 3148, 3160, 3164, 3179 |
| UNDERKÄND | 5 | 3139, 3143, 3163, 3166, 3171 |

Totalt 26 + 13 + 5 = 44. De 16 avvisade är rätt avvisade (se sist). Ingen av dem kan släppas.

## Regelkontroll (alla 44)
- Titlar: 18–69 tecken. Högst 2 kommatecken som skiljetecken. 3133 har dessutom 3 decimalkomman ("102,7 x 102,7 x 2,2 cm"), och kontrollskriptet räknar dem som en VARNING. Det godtas, eftersom det är decimaltecken.
- SEO-titlar: 20–41 tecken (≤43). Dubbletter: **3142** = 3005 (c_1) och **3148** = 3004 (c_1). I övrigt unika.
- Meta: 133–153 tecken där den finns. Null på 21 tunna källor, vilket följer avsnitt 10.
- Varianter: medicinbollarna (3148: 4/6/8/10, 3149: 0–10), banden (3151, 3152, 3168, 3177, 3180) och Office Ball (3160: 65/75) har oförklarade varianter. **Inget utkast låser** vikt, styrka, färg eller längd i titel, SEO eller specifikation. Frågorna ligger under `att_bekrafta`. Det är bra.
- Hälsopåståenden (rehabilitering, lindra, återhämtning, hållning, blodcirkulation, skydda leder) och marknadsföring (ultimata, perfekt, högkvalitativ) har utelämnats överallt. Massageboll/massagebollar står bara som produktnamn (tillåtet enligt avsnitt 10). Inga ursprung, omdömen eller priser.
- "Anti-burst", maxvikt och belastningsuppgifter för gymnastikbollarna (3161, 3175, 3176) har rätt utelämnats. Gymnastikbollar har tidigare skrivits i vågorna med den regeln, så jag underkänner dem inte.
- Format: stor bokstav efter kolon och på beskrivande ord i titel och SEO ("Svart", "Grå", "med Handtag", "i Läder"). Enheter med gemener och mellanslag ("70 cm", "0,7 cm"). Inga arbetstermer ("enligt källan").

## Per produkt (RÄTTA och UNDERKÄND; GODKÄND bara när det finns något att notera)

| Nr | Id | Dom | Före → efter / skäl |
|---|---|---|---|
| 3121 | 10581107409162 | RÄTTA | Titel: "Gym Chalk Gymstick" → "Krita Gymstick Gym Chalk". SEO: "Gym Chalk Gymstick för Grepp" → "Krita Gymstick Gym Chalk för Grepp" (34). Skäl: titeln börjar med ett engelskt typord och saknar svenskt typord. "Krita" står i källan. |
| 3122 | 10581107441930 | GODKÄND | En variant, så Medium/blå får låsas. "för vattenträning" och "i aqua-träning" upprepar varandra lite, men det godtas. |
| 3123 | 10581107540234 | RÄTTA | Html: "&lt;li&gt;Dig som vill ha ett extra starkt motståndsband, enligt tillverkaren&lt;/li&gt;" → "&lt;li&gt;Dig som vill ha ett extra starkt motståndsband&lt;/li&gt;". Skäl: "enligt tillverkaren" passar inte på ett önskemål. |
| 3131 | 10581107998986 | RÄTTA | SEO: "Gymmatta Interlocking Mat Pro" → "Gymmatta Gymstick Interlocking Mat Pro" (38). Skäl: märket saknas. Notera: samma modellnamn som 3133 (399 kr mot 849 kr) utan förklaring. Utkastaren har rätt i att inte föra över 3133:s mått. |
| 3132 | 10581108031754 | RÄTTA | SEO: "Gymmatta Interlocking Mat Set" → "Gymmattor Gymstick Interlocking Mat Set" (39). Html: "&lt;li&gt;Dig som vill ha sammanfogbara mattor, enligt tillverkaren&lt;/li&gt;" → "&lt;li&gt;Dig som vill ha mattor som går att sammanfoga&lt;/li&gt;". |
| 3133 | 10581108064522 | RÄTTA | SEO: "Interlocking Mat Pro, 102,7 x 102,7 cm" → "Gymmatta Interlocking Mat Pro, 2,2 cm" (37). Skäl: svenskt typord saknas, och tjockleken skiljer den från 3131. Meta: "Enligt tillverkaren går den att koppla ihop med andra." → "Enligt tillverkaren går den att koppla ihop med andra mattor." (147). |
| 3135 | 10581108162826 | RÄTTA | Meta: "Gymstick Kettlebell Pad är en pad för kettlebellträning. Enligt tillverkaren skyddar den golv och utrustning och tål belastningen från kettlebellträning." → "Gymstick Kettlebell Pad är ett golvskydd för kettlebellträning. Enligt tillverkaren skyddar det golv och utrustning och tål belastningen från träningen." (152). Html, första meningen: "är en pad för kettlebellträning. Enligt tillverkaren skyddar den golv och utrustning" → "är ett golvskydd för kettlebellträning. Enligt tillverkaren skyddar det golv och utrustning". Skäl: "Pad är en pad" är cirkulärt. |
| 3136 | 10581108195594 | RÄTTA | Titel och SEO: "Ab Roller Gymstick Jumbo" → "Maghjul Gymstick Jumbo Ab Roller" (32, lagras tom som SEO). Meta: "är en ab roller för bålträning. Enligt tillverkaren är den robust" → "är ett maghjul för bålträning. Enligt tillverkaren är det robust" (137). Html: "är en ab roller för bålträning. Enligt tillverkaren är den robust och utformad för träning" → "är ett maghjul för bålträning. Enligt tillverkaren är det robust och utformat för träning". Html, punkt: "Dig som vill träna bålen med en ab roller" → "Dig som vill träna bålen med ett maghjul". Skäl: engelskt typord och cirkulärt "Ab Roller är en ab roller". |
| 3139 | 10581108293898 | UNDERKÄND | Oklar produkttyp och möjlig last. Källan säger inte om Lateral Curl Bar är en skivstång för viktskivor eller ett kabeltillbehör, och maxbelastning saknas (utkastaren flaggar det själv). En stång med last tas för hand. |
| 3142 | 10581108556042 | RÄTTA | SEO: "Hopprep Gymstick i Läder" → "Hopprep Gymstick Leather Jump Rope" (34). Skäl: dubblett med 3005 i c_1. |
| 3143 | 10581108588810 | UNDERKÄND | Oklar produkttyp. Källan säger bara "grepp" (handskar, dynor eller grepp med rem?), titeln står på engelska och texten blir cirkulär ("Lifting Grips är grepp"). Källan påstår också att greppen minskar risken för skador. Den är för tunn för att skriva säkert. |
| 3144 | 10581108621578 | RÄTTA | Meta: "Gymstick Lifting Straps with Padding är lyftremmar med extra vaddering. Enligt tillverkaren är de tillverkade av slitstarkt material." → "Gymstick Lifting Straps with Padding är lyftremmar med extra vaddering för styrketräning med tunga lyft. Enligt tillverkaren är materialet slitstarkt." (150). Html: "Enligt tillverkaren är de tillverkade av slitstarkt material.&lt;/p&gt;" → "Enligt tillverkaren är materialet slitstarkt.&lt;/p&gt;". Skäl: "tillverkaren … tillverkade" upprepas. |
| 3146, 3147 | 10581108687114, 10581108719882 | GODKÄND | Tunna källor. Bara märke, antal och "efter träning" finns kvar, utan meta. Alla effektpåståenden har utelämnats. |
| 3148 | 10581108883722 | RÄTTA | SEO: "Medicinboll Gymstick med Handtag" → "Medicinboll Gymstick Medicine Ball, Handtag" (43). Skäl: dubblett med 3004 i c_1 (samma serie, 4 kg). Bättre alternativ om c_1 inte är skriven: ge 3004 SEO-titeln "Medicinboll Gymstick med Handtag, 4 kg" och låt 3148 behålla sin. |
| 3149 | 10581108916490 | GODKÄND | 10 kg är inte låst. Variant "0" för 1 299 kr är oförklarad och ligger under att bekräfta. |
| 3160 | 10581109309706 | RÄTTA | Html: "&lt;li&gt;Dig som vill ha en träningsboll på kontoret&lt;/li&gt;\n&lt;li&gt;Dig som vill ha en träningsboll på hemmakontoret&lt;/li&gt;" → "&lt;li&gt;Dig som vill ha en träningsboll på kontoret eller hemmakontoret&lt;/li&gt;". Skäl: två punkter säger samma sak. 65/75 är rätt olåst. |
| 3163 | 10581109408010 | UNDERKÄND | Oklar produkttyp. "Performance Board" kan vara en balansbräda: användaren står på produkten och maxbelastning saknas. Utkastaren lyfter själv frågan. Tas för hand. |
| 3164 | 10581109440778 | RÄTTA | Meta: "Gymstick träningsmatta i grått, 140 x 60 cm och 0,7 cm tjock. Enligt tillverkaren ger mattan grepp och stötdämpning vid yoga och styrketräning." → "Gymstick träningsmatta är grå och mäter 140 x 60 cm. Den är 0,7 cm tjock och ger enligt tillverkaren grepp och stötdämpning vid yoga och styrketräning." (151). Html: "&lt;p&gt;Gymstick träningsmatta är en grå träningsmatta på 140 x 60 cm. Mattan är 0,7 cm tjock.&lt;/p&gt;" → "&lt;p&gt;Gymstick träningsmatta är grå och mäter 140 x 60 cm. Mattan är 0,7 cm tjock.&lt;/p&gt;". Html, specifikation: lägg till "&lt;li&gt;Märke: Gymstick&lt;/li&gt;" före "&lt;li&gt;Mått: 140 x 60 cm&lt;/li&gt;". Skäl: första metameningen saknar verb, "träningsmatta är en … träningsmatta" upprepar och märket saknas i specifikationen. |
| 3166 | 10581109571850 | UNDERKÄND | En hållningskorrigerare är ett stöd. Hela källan består av hälsopåståenden (hållning, minska obehag, rakare rygg) och taggen är "Rehab & Hållning". Titelns "Stor/Extra stor" motsäger dessutom varianterna S/M och L/XL. |
| 3171 | 10581109768458 | UNDERKÄND | Oklar produkttyp. Svenskt typord saknas (glidmatta?). Varianterna Default 799 kr, SL 149 kr och G 129 kr är troligen olika produkter, och användaren står och glider på produkten. |
| 3175, 3176 | 10581109932298, 10581109965066 | GODKÄND | Källans "upp till en viss viktgräns" har rätt inte skrivits vidare. Maxvikt bör ändå hämtas från leverantören innan något om belastning läggs till. |
| 3178 | 10581110063370 | GODKÄND | Frivilligt: lägg till "Märke: Gymstick" i specifikationen, som i övriga. |
| 3179 | 10581110096138 | RÄTTA | Meta: "…är en grå träningsmatta i NBR på 170 x 60 cm och 1,5 cm tjock. Mattan passar" → "…är en grå träningsmatta i NBR som mäter 170 x 60 cm och är 1,5 cm tjock. Mattan passar" (154). Html, första stycket: samma ändring ("på 170 x 60 cm och 1,5 cm tjock." → "som mäter 170 x 60 cm och är 1,5 cm tjock."). Skäl: konstruktionen haltar grammatiskt. Frivilligt: "Märke: Gymstick" i specifikationen. |

Övriga GODKÄND (3124, 3125, 3126, 3141, 3145, 3150–3157, 3161, 3165, 3167, 3168, 3174, 3177, 3180): allt i texten finns i källan, tillverkarpåståenden står som "enligt tillverkaren", och språket och formatet är rätt.

## De avvisade (16), rätt avvisade
3127 boxsäck, 3128 och 3173 parallettes, 3129 och 3134 viktskivor, 3155 dörrgym, 3169 ringar, 3170 viktväst och 3172 chinsräcke (last). 3130 varm/kall-roller, 3158 nackavslappnare, 3159 nackdragare och 3137 kinesiotejp (hälsa/behandling). 3138, 3140 och 3162 knästöd (stöd med skadeförebyggande påståenden). Ingen av dem är uppenbart en produkt utan säkerhetsprofil. **Inget att släppa.**

## Frågor till David
1. Typord: "Krita" (källan) för Gym Chalk 3121, eller "Gymtalk" som för Trec (avsnitt 11)? Och "Maghjul" för Ab Roller 3136?
2. 3131 och 3133 heter båda Interlocking Mat Pro (399 kr respektive 849 kr). Är 3131 en annan tjocklek eller en dubblett?
3. Medicinbollarna 3148/3149 och 3004 (c_1): betyder varianterna kg, och vad är variant 0 (1 299 kr) på 3149? Vilken produkt ska behålla SEO-titeln "Medicinboll Gymstick med Handtag"?
4. Ska gymnastikbollar och sittbollar (3160, 3161, 3175, 3176) räknas som produkter med last när källan saknar maxvikt? Hittills har de skrivits utan belastningsuppgift.
