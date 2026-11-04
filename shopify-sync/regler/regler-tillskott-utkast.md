# Regeluppsättning för kosttillskott och energidryck – UTKAST för Davids beslut

Skapad 2026-11-04 (fas 1, HYPR Nutrition). **Ej godkänd. Inget juridiskt utlåtande.** Innehållet bygger på min allmänna kännedom om regelverket och är inte kontrollerat mot gällande lagtext eller myndighetsvägledning i den här sessionen. **Uppställningen bör granskas av någon med regulatorisk kompetens** (livsmedelsjurist eller regulatorisk specialist, gärna med kontakt mot Livsmedelsverket/Konsumentverket) innan fas 2. Alla hänvisningar nedan ska verifieras. Tills dess gäller att ingen produkttext skrivs.

## 1. Regelverk som berörs (att verifiera)
- EU:s förordning 1924/2006 om närings- och hälsopåståenden: bara påståenden som finns i EU:s register över tillåtna påståenden får användas, med angivna användningsvillkor; hälsopåståenden ska hänga ihop med ett specifikt, godkänt påstående.
- Livsmedelsinformationsförordningen 1169/2011: får inte tillskriva livsmedel egenskaper att förebygga, behandla eller bota sjukdom; obligatorisk information ska finnas tillgänglig före köp vid distansförsäljning; särskild märkning för drycker med högt koffeininnehåll.
- Kosttillskottsdirektivet 2002/46/EG och svenska genomförandet (Livsmedelsverkets föreskrifter): märkning, rekommenderat dagligt intag, varning om att tillskott inte ersätter en varierad kost.
- Marknadsföringsregler (Konsumentverket): vilseledande marknadsföring, jämförelser och superlativ ska kunna styrkas.
- Läkemedelsgränsen (Läkemedelsverket): medicinska påståenden kan göra en produkt till läkemedel.

## 2. Förslag: kategorigränser
| Nivå | Produkter (HYPR idag) | Hantering |
|---|---|---|
| A. Rena fakta | Kreatin (pulver, sticks), energidryck | Endast fakta ur etikett/deklaration. Inga effektpåståenden förrän David och regulatorisk granskare godkänt ett exakt påståendeformulär |
| B. Särskild granskning | Multivitamin, Protect | Innehåller vitaminer och mineraler med godkända påståenden i registret, men varje påstående måste matcha ordalydelse och villkor (t.ex. minsta mängd per portion). Kräver granskare |
| C. Hög risk | Kollagen, PEA Boswellia Curcuminoids | Leder/hud/stelhet/"kliniskt" är typiska påståenden som inte är tillåtna om de saknas i registret (växtbaserade ämnen har dessutom många väntande påståenden). Skrivs endast som ren ingrediens- och deklarationsfakta, annars spärrade |
| D. Utanför | Allt som liknar läkemedel, produkter mot sjukdom, viktminskning, barn/gravida som målgrupp | Avvisas (R6) |

## 3. Vad som får återges ordagrant (kandidat, ska godkännas)
Uppgifter som står entydigt i produktens egen etikett eller leverantörsunderlag och är faktiska, inte värderande: produktnamn, märke, form (pulver, kapslar, sticks), nettovikt/antal, antal portioner, portionsstorlek, innehållsförteckning, näringsdeklaration (per portion/100 g), mängd av aktiv ingrediens i mg/g, smak, allergener, ursprungsland ("Producerad i Sverige" endast om det står på etiketten), vegansk märkning endast om den står på etiketten, förvaring och märkningstexter som lagen kräver (t.ex. att tillskott inte ersätter en varierad kost, dosrekommendation exakt som på etiketten, varning för koffein).

## 4. Påståenden som aldrig får skrivas (förslag, kontrolleras av skript där det går)
1. Sjukdomspåståenden: förebygga, behandla, lindra, bota eller minska risk för sjukdom/symptom (inkl. smärta, stelhet, inflammation, infektion, förkylning).
2. Hälsopåståenden som inte är ordagrant godkända med villkor: "stärker immunförsvaret", "bra för leder/hud/skelett/hjärna", "ger energi", "förbättrar återhämtning", "stimulerar kroppens egen kollagensyntes".
3. Generella hälsopåståenden utan specifikt godkänt påstående bredvid ("grunden för din hälsa", "välmående", "starkare kropp").
4. Näringspåståenden som inte uppfyller villkoren: "sockerfri", "proteinrik", "högkoncentrerad", "ren", "utan tillsatser" utan kontroll mot deklarationen. "100 % kreatin" bara om deklarationen entydigt visar det.
5. Viktminskning, fettförbränning, kroppsförändring och prestationslöften ("höjer din prestation", "bygger muskler").
6. Superlativ och oprovade jämförelser: ultimat, bäst, premium, "potent", "kliniskt relevanta mängder", "välstuderade", "maximal biotillgänglighet", "garanterat".
7. Ordagranna eller parafraserade studiehänvisningar ("forskning visar") utan källa och godkänt påstående.
8. Målgruppspåståenden för barn, gravida eller ammande; råd om att ersätta mat eller läkemedel.
9. Dosrekommendationer som inte är ordagranna från etiketten.

## 5. "Enligt tillverkaren"
Fungerar i BEST OF SPORTS (R4/R5) för tekniska uppgifter. **För hälso- och näringspåståenden ändrar det inte att säljaren marknadsför**, så frasen gör inte ett otillåtet påstående tillåtet. Förslag: "enligt tillverkaren" används bara för sakuppgifter som kan kontrolleras mot etikett (t.ex. nettovikt), aldrig för effekt. Behöver bekräftas av granskare.

## 6. Process (fas 2, först efter godkännande)
- Källa: produktens etikett/deklaration (bild eller leverantörsblad) som David eller leverantör bifogar; dagens webbtexter räknas inte som källa (de innehåller påståendena ovan).
- Nytt skripttest i `skrivfil_kontroll.py`: förbjudna uttryck (listan i §4) och obligatorisk ansvarsfras; kräver att skriptet kan peka på butikens egen spärrlista (idag BOS-specifikt).
- Granskning: Opus + mänsklig regulatorisk granskare för nivå B och C. Ingen automatisk skrivning av nivå C.

## Öppna frågor (till David)
Se `rapporter/hyprnutrition-2026-11-04/genomlysning.md`, avsnitt Frågor.
