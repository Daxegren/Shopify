# Granskning väg 2, cyklar k_01b – BEST OF SPORTS (2026-11-04)

Oberoende granskning, endast läsning. Underlag: `vag2_skriv/k_01b_utkast.json` (18 utkast) och `vag2_skriv/k_01b_avvisade.json` (7 avvisade), regelboken v1.4, BESLUTSLOGG, butiksprofilen och standarden §14 och §16. Alla 25 produkter, plus 10472335638794, hämtades live på nytt via Admin API (`shopify_api.hamta_produkter`, varianter och pris via GraphQL). Butiken söktes dessutom på varje modellnamn för att hitta dubbletter (R12a). Inget ändrat i Shopify.

**Kontroller med skript:** standardblocket är identiskt med det kanoniska (`b_skriv_24.json`) i alla 18 utkast. Leveranstidsmeningen är fel på ett av dem (9035, se nedan). Titlar ≤70 tecken, SEO-titlar ≤43, metor 116–140 tecken. Titel, SEO-titel och meta krockar inte med något i andra filer i `vag2_skriv/`. Högst två "enligt tillverkaren" per text. Ingen av produkterna har taggen `texter-klara` eller egen SEO, så det finns ingen gammal text att jämföra med (R15). Byggskriptet `bygg_m_skriv.py` provkördes med detta utlåtande: 18 skrivbara, inga problem, och varje "före" träffar exakt en gång.

**Resultat:** 14 GODKÄND, 4 RÄTTA, 0 UNDERKÄND. Avvisningarna: 6 är motiverade, och 1 (9034) bör prövas om eftersom förutsättningen har ändrats.

| nr | id | dom | före → efter / skäl |
|---|---|---|---|
| 9026 | 10676720697610 | GODKÄND | Allt finns i den egna svenska källan (centermotor = mittmotor, 430 Wh, 115 km "enligt tillverkaren", XCM32, Cues 10, MT200, Rekon 29x2.4). Produkten har en variant och ramstorleken är rätt utelämnad. Färgen kommer bara från titeln. Om valet mellan den här produkten och 9029, se nedan. |
| 9027 | 10676721549578 | GODKÄND | Som 9026. |
| 9028 | 10682105397514 | GODKÄND | Översättningen från engelska stämmer: Maestro 170 mm, Fox 38 Factory 180 mm, Float X2 205x65, TRP EVO Pro 4-kolvs, 29/27,5 tum, vikbara däck och tillvalsbatteri 280 Wh. Källan säger "electronic SRAM XO Eagle Transmission AXS", så "elektroniskt" får stå (§14). 800 W är rätt utelämnat. 171 km står på specraden och återges med "enligt tillverkaren". Källan stavar "Assagai"; utkastets "Assegai" är Maxxis rätta namn och godtas. |
| 9031 | 10682105463050 | GODKÄND | Specifikationen står i produktens egen källa och är inte lånad från Talon E+ 2. Utrustningen (stöd, stänkskärmar, pakethållare, ljus) gäller EX-produkten. S/M/L kostar lika mycket. |
| 9032 | 10682106118410 | RÄTTA | **html:** `<li>Dig som vill ha en elcykel med navväxel och hydrauliska bromsar</li>` → `<li>Dig som vill ha en elcykel med Shimano Nexus och hydrauliska bromsar</li>`. Källan säger bara "Shimano Nexus", inte navväxel (R1). Övrigt stämmer mot den engelska källan. Att tum utelämnas (källan anger bara 622x55) är rätt. |
| 9033 | 10469208916234 | GODKÄND | Motorns märke är rätt utelämnat: löptexten säger Yamaha, specraden Giant SyncDrive Core. 250 W och 50 Nm är entydiga på specraden (R2). Den estniska raden är rätt översatt: seisujalg = stöd, ketikaitse = kedjeskydd, pakiraam = pakethållare, porilauad = stänkskärmar, esi- ja tagatuli = fram- och baklampa. 180 km står på två ställen i källan. L (55 cm) är källans enda storlek. |
| 9035 | 10472241299722 | RÄTTA | **seo_title:** `Elcykel Italwin K2 XL, Vit` → `Hopfällbar Elcykel Italwin K2 XL, Vit` (samma typord som titeln, R7).<br>**meta:** `Italwin K2 XL i vit har` → `Italwin K2 XL i vitt har`.<br>**html:** `övriga länder. Beställningsvaror kan ta upp till en vecka längre.</p>` → `övriga länder.</p>`. Produkten saknar taggen "På beställning", så leveranstidsmeningen ska bort (R13; skriptet fångade inte detta).<br>Ah-motsägelsen är rätt hanterad: 378 Wh / 36 V = 10,5 Ah som i titeln, men källraden säger 14,5 Ah, så Ah utelämnas helt. "Maxvikt: 90 kg" säger inte om vikten gäller cyklisten, lasten eller totalen, så det är rätt att utelämna den (R4). "Made in Italy", EU-standarden och 25 km/h är rätt utelämnade. |
| 9036 | 10470900957450 | RÄTTA | **meta:** `Robin ST i grön har` → `Robin ST i grönt har` (språkfel). Fakta stämmer. 26 x 4,0 tum är rätt tolkat ur `CST 26 "X4.0"`. "Lastkapacitet: 120 kg" är en svensk rad med etikett och står en gång med "enligt tillverkaren". |
| 9037 | 10470903087370 | GODKÄND | Allt finns i den egna svenska källan. BMS och "stabil prestanda" är rätt utelämnade (R5). |
| 9038 | 10472249819402 | GODKÄND | Allt finns i källan (XOFO baknavsmotor, 36 V 10,4 Ah, 29 kg, lastkapacitet 120 kg med etikett). 28 tum och blå kommer från titeln. "Lättaste" och "robust" är rätt utelämnade. |
| 9039 | 10682105528586 | GODKÄND | Coco är ingen elcykel trots taggen (taggen rörs inte). Typordet "Cykel" är en entydig översättning av live-titelns "Bicycle" (R7), och "stadscykel" står i källan ("city bike"). Damcykel används med rätta inte, eftersom bara den äldre Coco-produkten säger det (R1). Punkteringsskyddet är rätt utelämnat. |
| 9040 | 10472282620170 | GODKÄND | Allt finns i den egna svenska källan. Ramstorlek S (13 tum) är källans enda storlek och produkten har en variant, så raden får stå. Det finns ingen dubblett i butiken. |
| 9042 | 10469226283274 | RÄTTA | **html:** `<li>Räckvidd: Upp till 150 km enligt tillverkaren</li>\n` → (tas bort). Källan är maskinöversatt och delvis trasig ("Amort", "supports you in the sharpness", "Deere Deere", modellen jämförs med sig själv). 150 km med E7000 och 504 Wh är dessutom nästan dubbelt mot Konas egen uppgift för samma motor och batteri (80 km, 9040). Syskonet används inte som källa, bara som skäl att inte lita på raden. Räckvidd är ett löfte som kräver en säker källa (§16.2). Däckraden används rätt, bara i sina entydiga delar. |
| 9043 | 10682105594122 | GODKÄND | Allt finns i källan (Bosch CX 250 W/120 Nm, 800 Wh, 180 km, Zeb 170 mm, Maven Base). Växelgruppen "SRAM Eagle 90 Transmission" får utelämnas eftersom källan inte anger typen. §14 hade också tillåtit namnet ordagrant, utan ordet mekanisk eller elektronisk. |
| 9044 | 10470987694346 | GODKÄND | "Elektronisk växelreglering" och "dropper post" står ordagrant i källan, så "elektronisk" får stå (till skillnad från 9043 och 9046). Bytet Gravelbike → Gravelcykel godtas: det är en entydig motsvarighet som också är butikens live-ord (taggen, syskonet 9046), och samma bedömning gjordes för 7121 i vag2k_utlatande_13_15. Kolfiberfälgarna ("Check!") är rätt utelämnade. |
| 9046 | 10494941659402 | GODKÄND | Allt finns i källan. Att "SRAM Apex XPLR AXS" utelämnas är tillåtet (§14). Alla varianter kostar lika mycket. |
| 9047 | 10471129153802 | GODKÄND | Allt finns i källan. Produkten har en variant (L). "Lätt" och prisvärdheten är rätt utelämnade. |
| 9048 | 10530213429514 | GODKÄND | Allt finns i källan ("Shimano Sora mekaniska" står ordagrant). OBS: 10565633638666 "Gravelcykel KONA Rove AL/DL, Gloss Aragorn" (ACTIVE, Default Title, SKU …52) är samma modell och färg och finns inte i någon batch. Den ska avvisas som dubblett när den kommer upp. |

## Avvisningarna (k_01b_avvisade.json)

| nr | id | bedömning |
|---|---|---|
| 9034 | 10676719714570 | **Bör prövas om.** Avvisningen följer R12a på pappret, men produkten den jämförs med, 10472335638794 (skriven i b_skriv_17, taggen `texter-klara`), är nu **ARCHIVED**. 9034 är den produkt som är ACTIVE och syns för kunderna, och den har ingen text. De två skiljer sig också åt: SKU 1080022144 / Default Title / 44 529 kr mot SKU 1080022145 / M / 44 609 kr. Rekommendation: koordinatorn eller David bestämmer om 9034 ska få en egen text. Byggskriptet stoppar annars samma titel som den arkiverade produkten, så titel, SEO-titel och meta måste skilja sig, eller så måste den arkiverade produkten uttryckligen undantas. |
| 9029 | 10682105299210 | Avvisningen är motiverad (R12a, samma modell och färg som 9026). Men: 9029 har varianterna M/L/XL (SKU …205/207/208), medan 9026 bara har en variant (SKU …204, troligen S). Att skriva texten på 9026 och avvisa 9029 betyder att produkten med flest storlekar blir utan text. Eftersom texten inte nämner ramstorlek passar den lika bra på 9029. Andra skälet i avvisningen ("M/L/XL medan källan listar S–XL") räcker inte enligt R3: alla varianter kostar lika mycket och storlekarna ingår i källans lista. |
| 9030 | 10682105331978 | Som 9029 (dubblett av 9027, M/L/XL mot en variant). |
| 9041 | 10468744397066 | Motiverad: XL kostar 111 239 kr, övriga 111 449 kr (R3), och källan motsäger sig (EP8/EP800, 180/178 mm, S och M båda 38 cm). |
| 9045 | 10488282251530 | Motiverad: 38 019 kr mot 33 059 kr (R3), och XL finns i två färger. |
| 9049 | 10487987142922 | Motiverad: 21 419, 21 369 och 18 619 kr (R3). |
| 9050 | 10474079322378 | Motiverad: 18 719 kr mot 16 279 kr (R3), och XL/gray stämmer inte med titelns färg. |

## Utkastarens att_bekrafta-punkter

- **9035 Italwin (Ah):** rätt hanterad. Ah utelämnas, 378 Wh och 36 V står kvar och stämmer med titelns 10,5 Ah. Maxvikt 90 kg är också rätt utelämnad (det framgår inte vad vikten gäller).
- **9033 Liv Allure E+ 2:** motormärket är rätt utelämnat och den estniska raden rätt översatt.
- **9042 Kona Remote 130:** däckraden är rätt hanterad, men räckvidden 150 km ska bort (RÄTTA).
- **9043 och 9046 jämfört med 9028 och 9044:** konsekvent hanterade. "Elektronisk" står bara där källan säger det ordagrant (9028 "electronic … AXS", 9044 "Elektronisk växelreglering"). Där källan inte anger typen utelämnas växelgruppen, vilket §14 tillåter.
- **9039 Kona Coco:** typordet "Cykel" och "stadscykel" är rätt. Damcykel används inte.
- **9044:** Gravelbike → Gravelcykel godtas (se tabellen).
- **9028 och 9032 (engelska källor):** översättningarna stämmer. Enda tillägget utanför källan var "navväxel" i 9032 (rättat).

## Återkommande fynd

1. **Dubbletter där storlekarna är separata produkter.** Velomarket lägger ofta en storlek som egen produkt (Talon E+ 2 S kontra M/L/XL, Rove AL/DL Aragorn M/L kontra M, Revolt Advanced 3 Default kontra M). R12a säger vilken som ska avvisas när den andra redan är skriven, men inte vilken av två oskrivna som ska få texten. Förslag till regel: skriv den aktiva produkten med flest varianter, och kontrollera att den redan skrivna fortfarande är ACTIVE innan en avvisning görs.
2. **Leveranstidsmeningen på produkt utan taggen "På beställning"** (9035) slank igenom. Det kan testas med skript (R13 är T): jämför html med taggen i live-läsningen.
3. **Räckvidd från trasiga, maskinöversatta källor.** En ren rad i en i övrigt opålitlig källa kan ändå vara fel. Förslag: räckvidd (och batteri) utelämnas när källan har trasiga rader på andra ställen, på samma sätt som R4 gör för lastgräns.
4. **Grammatik för färg i meta:** "i grön" och "i vit" ska vara "i grönt" och "i vitt". Svenska färgord i formen "i <färg>" kan fångas av ett enkelt test.
5. **Kunskap utanför källan i "Passar för"** (navväxel). Små, sanna tillägg smyger in där.
