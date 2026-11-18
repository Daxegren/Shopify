# Metabeskrivningar: prioriterad lista och 50 utkast (Workout Brands, 2026-11-18)

Gjort efter Davids ja (chatt 2026-11-18). Bara läsning och utkast i filer. Inget skrivet i Shopify, ingen spärr aktiverad eller ändrad, inga taggar rörda. Butiken kontrollerades med `get-shop-info`: workoutbrands.com.

## Prioriterad lista (`data/meta_saknas_prioriterad.csv`)
- 3 059 aktiva produkter saknar metabeskrivning. **1 499 av dem faller inom föreslagna spärrgrupper** och är utanför listan tills du beslutar om spärrlistan (`data/meta_saknas_sparrade_utanfor.csv`): prisjobb/BF26 1 138, barn 148, dubbletitlar 142, vendor som inte är märke 76, solglasögon 74, titel med storlek 57, outlet 49, Out of stock 33, mobilskal 7 (en produkt kan ha flera orsaker).
- **1 560 återstår i listan.** Rangordning: försäljning senaste 12 månaderna (ShopifyQL, brutto per produkttitel), därefter lagersaldo. Bara 17 av dem har sålt något (brutto 30 061 kr); övriga 1 543 rangordnas efter lager (1 248 med lager, 295 utan).
- Matchningen mot försäljning sker på produkttitel; titlar som ändrats sedan ordern kan ha missats. Försäljningslistan är topp 120 av 465 titlar, så produkter under cirka 450 kr brutto kan ha rankats efter lager i stället.
- Notera att den största säljaren, B Jerseyshirt Stripe Longsleeve (78 393 kr), har prisjobbstaggen och därför ligger i spärrgruppen, inte i listan. Beslutet om spärren avgör alltså var de mest säljande produkterna hamnar.

## 50 utkast (`data/meta_utkast_50.csv`)
De 50 högst rankade i listan. Kolumner: förslag på SEO-titel (utan suffixet " | Workout Brands", högst 43 tecken), metabeskrivning (70–155 tecken) och kontroll.
- Källa: endast produktens egen titel, typ, märke och beskrivningstext i butiken (R1). Första meningen har verb (R11), inga "&", inga hälso-, skydds- eller kvalitetspåståenden (R5), unika texter. Alla 50 klarar längdkontrollen (meta 70–155, SEO-titel högst 43) och unikhetskontrollen.
- **3 produkter bör granskas innan något skrivs (R3):** titeln anger en variant (storlek eller färg): rad 8 Premium 210 Fitted Cap L/XL, rad 12 UA Unstoppable Flc Jogger - Black, rad 34 FLEXFIT NU CAP darknavy S/M. Utkasten undviker storlek och färg, men produkten ska kontrolleras mot varianterna.
- **Rad 7 (B US Shield Cap):** produkttypen är Keps men texten beskriver en grovstickad vintermössa med skärm; utkastet följer texten. Typen bör rättas separat.
- Skriptet `skrivfil_kontroll.py` kördes inte: utkasten är en CSV för din bedömning, inte en skrivfil, och profilen saknar standardblock, ton och SEO-titelns maxlängd (TODO). Det ska köras på varje skrivfil före en riktig skrivning, tillsammans med regelbok och beslutslogg.
- Utkasten är mina förslag på en bedömningsbit för ton och format, inte godkända texter.

## Beslut som behövs från dig
1. Är tonen och formatet i de 50 utkasten rätt? Ändra det du vill; jag rättar och tar nästa omgång.
2. SEO-titelns mönster ("Modell typ märke" som i utkasten, eller annat) och maxlängd.
3. Spärrlistan (1 499 produkter utanför listan), särskilt prisjobbsgruppen som innehåller bästsäljarna.
4. Om några utkast ska skrivas i butiken: kräver ditt uttryckliga ja, skrivfilskontroll, en kanarie på tre produkter och återläsning enligt R16–R18.
