# Granskning väg 2, cyklar k_02b (2026-11-04)

Oberoende granskning (Opus). Shopify bara läst, inget ändrat. Underlag: `vag2_skriv/k_02b_utkast.json` (17 utkast) och `k_02b_avvisade.json` (8 avvisade). Regler: regelbok v1.5, BESLUTSLOGG, butiksprofilen, produkttexter-standard §10, §14 och §16, LARDOMAR (cyklar 2026-11-03). Jag hämtade alla 25 produkter live på nytt via Admin API (`shopify_api.hamta_produkter` och en fråga om varianter). Dessutom hämtade jag alla 867 produkter från Kona och Giant för att leta dubbletter. Alla 25 är ACTIVE och saknar SEO-titel och meta.

**Resultat:** 12 GODKÄND, 5 RÄTTA, 0 UNDERKÄND. Rättningarna (före och efter) står i `vag2_skriv/k_utlatande_02b.json`. Varje före-text förekommer exakt en gång i sitt fält (kontrollerat i python). Jag körde `skrivfil_kontroll.py` på en rättad kopia: 0 fel, 0 varningar. Leveranstidsmeningen finns på exakt de 13 produkter som har taggen "På beställning" (R13). Titel, SEO-titel och meta krockar inte med någon Kona- eller Giant-produkt i butiken.

| nr | id | dom | kort skäl |
|---|---|---|---|
| 9126 | 10472281964810 | GODKÄND | Spårbart, en variant |
| 9127 | 10474079060234 | RÄTTA | Lägg till raden "Ingår" (estniska raden går att översätta säkert) |
| 9128 | 10676719288586 | RÄTTA | Källan motsäger sig (105 / 105 Di2), så antalet växlar ska också bort enligt §14 |
| 9129 | 10676717846794 | GODKÄND | "Ultegra Di2 elektronisk" står i källan; se beslut om elektronik |
| 9130 | 10676718665994 | GODKÄND | Ramstorlekarna M och M/L är de varianter som säljs |
| 9132 | 10676718174474 | GODKÄND | Spårbart; "enligt tillverkaren" 1 gång |
| 9136 | 10682105561354 | GODKÄND | Översättningen stämmer; S, M och L säljs |
| 9137 | 10682105626890 | GODKÄND | Som 9136 |
| 9138 | 10588452880650 | GODKÄND | Hjulstorleken är utelämnad, vilket är säkert (29 tum hade gått för L/XL) |
| 9140 | 10650208862474 | GODKÄND | Spårbart |
| 9143 | 10472349368586 | GODKÄND | Spårbart |
| 9144 | 10472297988362 | RÄTTA | Typordet ändras till "Dirt jump-cykel" (butikens eget ord och källans "dirt jump-cyklist") |
| 9146 | 10469244600586 | GODKÄND | Bakdäcksraden med villkor är sann, eftersom storleken är okänd |
| 9147 | 10650208796938 | GODKÄND | Spårbart |
| 9148 | 10472256635146 | GODKÄND | Spårbart |
| 9149 | 10476262981898 | RÄTTA | Bara S säljs, så bakdäcket är 27,5 x 2,4 tum |
| 9150 | 10476260458762 | RÄTTA | Bakdäcket är 27,5 tum; "(Grå)" tas bort (titeln säger Grey, varianten white) |

## Kontroll av utkastarens att_bekrafta
- **9128, 105 mot 105 Di2:** utkastaren utelämnade växelgruppen, och det är rätt. Men §14 (Davids beslut 2026-11-03) säger "utan växelgrupp **och antal växlar**". Därför tas "24 växlar" bort i meta, löptext och specifikation. Tvillingen 7137 avvisades i k_15 av samma skäl. Med rättningen följer 9128 regeln.
- **9149 och 9150, GX Eagle:** för 9149 säger källan "SRAM GX cable-controlled drivetrain". Det är entydigt kabelstyrt, alltså mekaniskt, och namnet får stå. För 9150 säger källan bara "SRAM GX-Eagle". Namnet är rätt utelämnat (§14, praxis 9046). Inget behöver beslutas för de här två.
- **9127, estniska raden:** "Komplektis kuuluvad porilauad, seisujalg, pakiraam, Cateye laetav tuli" betyder "I setet ingår stänkskärmar, stöd, pakethållare och laddningsbar Cateye-lampa". Översättningen är säker, så raden får användas (R2). Jag lägger därför till raden som en rättning. Det var också säkert att utelämna raden.
- **9144, Dirt Jump Bike:** källan är svensk och skriver "dirt jump-cyklist". Butiken använder redan ordet "Dirt jump-cykel" live (10650208993546 Giant STP 26, som ligger i batch k_02a). Engelska "Dirt Jump Bike" byts därför ut i alla fält. Batch k_02a ska använda samma ord.
- **9138, trasig däckrad:** raden "x2.25" (S=27,5", M-XL=29")" går att förstå för storlekarna som säljs (L och XL har 29 tum). Att utelämna är ändå säkert och godtas.
- **Hjulstorlek (9146, 9149, 9150):** 9146 har bara en variant med okänd storlek. Raden "29 x 2,4 (27,5 i storlek S)" är sann oavsett storlek och får stå. 9149 och 9150 säljs bara i storlek S. Enligt R3 v1.5 får bara storlekar som säljs nämnas, så bakdäcket blir 27,5 x 2,4 tum. Det är rätt att titeln saknar hjulstorlek (29 fram, 27,5 bak).
- **9150, Grey mot white:** titeln "Concrete (Grey)" säger emot variantfärgen "white". Rättningen tar bort "(Grå)" och behåller kulörnamnet "Gloss Concrete", på samma nivå som 9029/9030 (Mars Dust mot Red).

## Granskning av avvisningarna (k_02b_avvisade.json)
| nr | id | bedömning |
|---|---|---|
| 9131 Propel Adv Pro 0 AXS | 10676721189130 | **Svagt motiverad.** Titeln anger färgen Obsidian Pulse, och alla fyra varianter är "black". Prisskillnaden på 210 kr gäller storleken, som titeln inte anger. Produkten går att skriva med ramstorlekarna M, M/L, L och XL utan att nämna pris. Rekommendation: gör ett utkast, om elektronikfrågan nedan får ja. |
| 9133 = 8068 Giant Road Pro | 10515737542922 | **Rätt utfall, fel skäl.** 8068 skrevs aldrig. Den blev UNDERKÄND i b_utlatande_22_23 eftersom källan motsäger sig: titeln säger "sadlar", men texten beskriver pedaler (Look KEO, tätade lager). Live-källan är oförändrad, så produkten kan inte skrivas nu heller. |
| 9134 = 7080 Anthem Advanced 29 1 | 10476257116426 | **Kan skrivas nu.** 7080 blev UNDERKÄND i k_13 av två skäl: GX Eagle utan typ, och färgen Dark Irisdescent mot varianten "L / gray". Enligt dagens praxis (§14, 9046, 9150) skrivs den utan växelgruppens namn med "12 växlar". Färgen motsägs inte (samma nivå som 9029/9030). Bara L (46,5 cm) säljs. Produkten finns inte i spärrlistan. Rekommendation: nytt utkast med växelgruppen utelämnad. Källan stavar "Irisdescent", och färgen ska skrivas "Dark Iridescent". |
| 9135 = 7083 Defy Advanced 2 (2026) Abyss Black | 10476279496970 | **Rätt utfall, fel skäl.** 7083 blev UNDERKÄND i k_13 som trolig dubblett av 6054 (10476166217994). Den är skriven och har taggen texter-klara, och SKU:erna är i samma serie (…144 mot …146/…147). Dubbletten finns kvar, så produkten kan inte skrivas förrän David har beslutat om sammanslagning eller märkning. (Källan har här "Shimano 105 hydraulic" utan Di2, så den motsäger sig inte.) |
| 9139 Kona Dew Niagra | 10472335212810 | Motiverad. Samma modell och färg som 7114 (10541372113162), som är skriven och har taggen texter-klara (R12a). |
| 9141 Fire Mountain Peridot | 10565633540362 | Motiverad. Samma modell och färg som 7081 (10476262064394), som är skriven. Varianten XS har dessutom 26/27,5 tum. |
| 9142 Lava Dome Prism Dragonfly | 10487969939722 | Motiverad. Samma modell och färg som 7122 (10565633736970), som är skriven. |
| 9145 Kona Wo Matte Plum | 10462190567690 | Motiverad. Källan säger "Färg: orange", men titeln säger plommon och varianterna "purple". Priserna skiljer sig också. |

## Fynd och beslut för David
1. **Elektronisk växling på vanliga cyklar (9129, 9130, 9132, och 9131 om den skrivs).** I k_15 och k_17 avvisades tvillingarna 7136, 7138, 7140, 7141 och 7179 med skälet "elektroniskt växelsystem (batteri)". De står nu i spärrlistan som tidigare avvisade. I den här batchen godkänns samma modeller. Skälen: profilens `utanfor_tills_vidare` utesluter inte elektronisk växling, elcyklarna är frisläppta (§16), och 9028 skrevs med "elektronisk" ur källan. Standard §10 nämner däremot "allt med batteri" som säkerhetsprodukt. Rekommendation: David bekräftar att elektronisk växling får skrivas som ren fakta ur källan. Då gäller samma regel för tvillingarna. Om inget beslutas bör 9129, 9130 och 9132 hållas tillbaka.
2. **Dubbletter i butiken.** Samma titel finns på 4 produkter för Defy Advanced 2 Pearl White, 4 för Pro 0 Luminous Lagoon och 5 för Pro 1 Midnight Moon, och några har identisk SKU (t.ex. 1031030144 två gånger). Utkasten är den äldsta som inte är spärrad, och övriga är spärrade (titeldubbletter eller tidigare avvisade). Sammanslagningen behöver ändå ett beslut.
3. **Batch k_02a ska skriva "Dirt jump-cykel"**, samma ord som 9144.
