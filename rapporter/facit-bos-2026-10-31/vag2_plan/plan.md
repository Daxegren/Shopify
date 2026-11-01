# Våg 2: avgränsning inför Black Month (planeringsunderlag, 2026-11-01)

Bara läsning. Inget är skrivet till Shopify och inget är committat. Butiken bekräftad med `get-shop-info`: BEST OF SPORTS (bestofsports.se).

## Underlag och metod
- **Snapshot:** `rapporter/bos-produkter-titlar-beskrivningar-2026-10-25.csv` (3 250 aktiva produkter den 25 oktober, kolumnen `velo` = Velomarket; 2 583 Velomarket, 369 Gymstick, 285+8+8 Gorilla Norden, 4 Maxxus, 1 Azimut). Titlarna i CSV-filerna är alltså från 25 oktober.
- **Status nu:** snapshoten innehåller bara produkter som var aktiva 25/10. Jag har läst live från Shopify alla produkter med status DRAFT (409) och ARCHIVED (126) som uppdaterats sedan 24/10 och lagt dem mot snapshoten. 110 snapshot-produkter är nu DRAFT och 50 ARKIVERADE (160 av 3 250, 4,9 % på sex dagar). Kolumnen `status_live` i CSV-filerna bygger på detta. Kolumnen visar ACTIVE för det som inte påträffats i de två listorna.
- **Undantagslistor:** experiment 1 = `forslag-bos-experiment-1-2026-10-27/kohorter.csv` (432), pilot 20 = id i `13_kontroll_skrivna_titlar.sql`, facit 30 = `shopify-original-2026-10-31/facit30-original.json`, våg 1 = `vag1_klara_ids.json` och `vag1_skriv/skriv_*.json` (86), handhavd = `handhavd_ids.txt` (27 unika id). Listorna överlappar inte varandra.
- **Gruppindelning:** (c) tillverkare Gymstick (369); (a) övriga Velomarket med fitness-produkttyp (Konditionsträning & Fitness, Professionell utrustning, Crosstrainers, Yoga-/gymnastikmattor, Boxning, Stretchband, Träningsbollar, vikter, Massage, Utomhusträning) eller tillverkare Tunturi/Toorx/Hammer/BH Fitness/Christopeit/Finnlo; (b) resten av Velomarket. Gränsen mellan a och b är min tolkning.
- **Säkerhetsflaggor** är grova regler på titel, handle och produkttyp (ingen läsning av beskrivningar) och är **försiktiga**: de fångar hellre för mycket än för lite. Kända falska träffar finns (till exempel "Treadmill Lubrication" som batteri/motor, "Balansbräda" som barnprodukt, "Massage Hook/Stick" som massage). Flaggade produkter ska inte släppas till vågen utan att David eller en granskare tittat på dem.
- **BigQuery:** `bq` nekades ("Invalid Credentials"), så ingen trafikprioritering (fråga 12) och ingen trafikdata är körd.

## Kolumner i CSV-filerna
`id, nr (löpnummer i filen, inte vågens nr), titel (25/10), status_live, vendor, typ, kategori, skal, lager_2026_10_25, beskr_ord`

`kategori`:
- `ingar` = aktiv, ingen flagga, ingår i våg 2.
- `ingar_ej_aktiv` = ingen flagga men DRAFT/ARKIVERAD nu: skrivs inte förrän produkten är aktiv igen.
- `granska` / `granska_ej_aktiv` = mjuk flagga: professionell utrustning/roddmaskiner (grupp a, b) eller sparkcyklar/skridskor/skidor som troligen är barnprodukter (grupp b). Tas separat efter en titt, ingår inte i batcharna.
- `sakerhet` = hård flagga enligt Davids lista (hjälm, lås, barn, last, elcykel, kosttillskott, batteri/motor/elektronik, vibration, massagepistol, akupressur): tas för hand med Davids ja.
- `handhavd` = finns i `handhavd_ids.txt`.
- `undantag` = experiment 1, pilot 20, facit 30 eller våg 1. Kolumnen `skal` visar även eventuell säkerhetsflagga som ligger bakom.

## Antal per grupp
| | Totalt i gruppen | **Ingår, aktiva** | Ingår men DRAFT/ARKIV | Mjuk flagga (granska) | Hård säkerhetsflagga | Handhavd | Undantag (exp1, pilot, facit, våg 1) |
|---|---|---|---|---|---|---|---|
| (a) Fitness Velomarket | 867 | **75** | 5 | 52 + 6 | 170 | 27 | 532 (429 exp1, 86 våg 1, 10 pilot, 7 facit) |
| (b) Övriga Velomarket | 1 708 | **879** | 26 | 80 + 5 | 694 | 0 | 24 (16 facit, 8 pilot) |
| (c) Gymstick | 369 | **295** | 36 | 0 + 1 | 33 | 0 | 4 (3 exp1, 1 facit) |
| Summa | 2 944 | **1 249** | 67 | 132 + 12 | 897 | 27 | 560 |

(a)+(b) = 2 575 Velomarket-produkter; Gymstick-märkta Velomarket-produkter (8) räknas i (c). Tal i parentes i uppdraget (cirka 79 för a) stämmer med min siffra 75 aktiva + 5 DRAFT/ARKIV = 80.

Avvikelser mot uppdraget: (c) är 369 i snapshoten, men live finns 333 aktiva Gymstick-produkter och 372 i DRAFT; (a)+(b) = 2 575, inte 2 583: skillnaden är 8 Velomarket-produkter med tillverkare Gymstick, som ligger i (c).

## Föreslagen batchstorlek (enligt processen: utkast högst 15 per agent, skrivbatch högst 25, kanarie 3)
| Grupp | Utkast | Skrivbatchar | Kommentar |
|---|---|---|---|
| (a) 75 | 5 agenter à 15 | 3 batchar à 25 | Liten grupp, ta den först. Beskrivningarna är i snitt 88 ord; 19 av 75 har under 30 ord. |
| (c) 295 | 20 agenter à ~15 | 12 batchar à ≤25 | Eget varumärke/leverantör, kort text (snitt 55 ord). Gör en kanariebatch på 3 och vänta ett dygn (se risk 2) innan resten. |
| (b) 879 | 59 agenter à ~15 | 36 batchar à ≤25 | Delas i transcher (se nedan). 74 har under 10 ord (tunn källa: kort intro, ingen metabeskrivning) och 191 under 30. |

Förslag på ordning i (b): (1) prioritera efter trafik/annonskostnad med `12_produkter_prioritet_texter.sql` när BigQuery-inloggningen fungerar; (2) lägg produkter med lager 0 eller lägre sist (223 av 879 hade lager ≤ 0 den 25/10, de går inte att köpa); (3) börja med typer utan variantproblem (tillbehör, delar) och spara cyklar med många färgvarianter till sist (113 rader delar titel med en annan, 446 titlar har oklart språk). Hela (b) bedöms för stort för att nå före Black Month med processen som den är (utkast + oberoende granskning + rättning + stickprov); räkna med att en tranch på 200–300 produkter hinner.

## Vilka som är DRAFT eller ARKIVERADE (och därför inte ska skrivas)
Fullständig lista: kolumnen `status_live` i de tre CSV-filerna (filtrera på DRAFT/ARCHIVED).
- (a): 50 DRAFT + 22 ARKIVERADE av 867. Bland de som annars ingått: 5 (4 DRAFT, 1 ARKIV), plus 6 mjuka.
- (b): 22 DRAFT + 28 ARKIVERADE av 1 708. Bland de som annars ingått: 26.
- (c): 38 DRAFT av 369 (inga ARKIVERADE). 36 av dem hade annars ingått.
- Andra grupper: experiment 1 har 15 ARKIVERADE; pilot 20 har AL 1 (10462768038154) arkiverad; facit 30 har 2 DRAFT (10472298971402 Treadmill TOORX Street Compact, 10411721261322 Träningshandskar TUNTURI Fitness Gloves Pro Gel).
- **Våg 1: 13 av 86 är redan inte aktiva** (12 DRAFT, 1 ARKIVERAD, alla Tunturi/Toorx, mest gymbollar, viktplattor och mattor). Id: 10515748487434, 10462782554378, 10588447342858, 10472299266314, 10472303689994, 10462856806666, 10472311062794, 10472308506890, 10470942114058, 10472279965962, 10472311030026, 10472277803274 (DRAFT) och 10470934544650 (ARKIV, Roddmaskin Signature R90W). Skrivdata för dessa ska inte köras förrän de är aktiva igen.
- Nya aktiva produkter sedan 25/10 (13 st, alla cyklar från 2027-modellen med engelska titlar, Giant/Liv/Kona) finns inte i snapshoten och ingår inte i listorna.

## Risker
1. **Leverantörssynken (Velomarket3) ändrar status.** 4,9 % av snapshoten blev DRAFT/ARKIVERAD på sex dagar, och 15 % av våg 1:s utkast. Läs status direkt före varje skrivbatch och ta bort allt som inte är ACTIVE. Skriv inte till produkter som ligger i DRAFT (de kan återaktiveras av synken med leverantörens text).
2. **Synken kan återställa titlar.** 12 av pilotens 20 titlar gick tillbaka till leverantörens original dygnet efter skrivning (orsak ej fastställd; Velomarket3 ska enligt produkthändelserna inte ändra titlar). Följ processen: kanariebatch, återläsning direkt, ny kontroll efter nästa nattsynk (`13_kontroll_skrivna_titlar.sql`, byggd på pilotens id och behöver utökas med varje vågs id) och läs tillbaka titel, SEO-titel, metabeskrivning och beskrivning för alla produkter. Skicka alltid `seo:{title, description}` tillsammans (se LARDOMAR 2026-11-01). Vänta med nästa batch tills dygnskontrollen är grön.
3. **Titlarna i CSV är från 25/10.** Skriv aldrig utifrån dem: hämta källan på nytt vid utkastet (processens steg 1). 
4. **Hårda flaggor är grova.** 897 produkter är flaggade, 27 handhavda. Flaggorna kan ha falska träffar åt båda håll: en produkt utan flagga kan ändå vara en säkerhetsprodukt (till exempel cykel med motor i beskrivningen men inte i titeln, eller sparkcykel/barncykel utan barnord i titeln). Granskarna ska därför fortsätta avvisa batteri/motor/last/barn som de gjorde i våg 1.
5. **Tunn och trasig källa.** I (b) har 74 aktiva ingående produkter under 10 ord. Hellre för lite än för mycket; ingen påhittad text.
6. **Titelduplicering och varianter.** I (b) delar 113 rader titel med en annan produkt (färgvarianter som egna produkter). Titel, SEO och specifikation får inte låsa färg/storlek som inte styrs av produkten.
7. **Kvarvarande stickprov och öppna beslut från David** (stickprovstabellen för våg 1, pullbuoy, bärförmåga 220 kg på gymbollar) blockerar att mönster i våg 2 är rättade. Rätta mönstren i `fix_4.py` först.
8. **Experiment 1 (432) ska vara kvar utanför.** 3 av dem är Gymstick-produkter och ligger i (c) som `undantag`.
9. **Black Month stör mätningen** av pilotens effekt (ingen kontrollgrupp), vilket inte påverkar urvalet men bör sägas till David.

## Filer
- `a_fitness_velomarket.csv`, `b_ovriga_velomarket.csv`, `c_gymstick.csv` (alla produkter i gruppen med kategori och skäl).
- Skript för att återskapa: ligger i sessionens scratchpad (`build.py`, `sets.py`), inte incheckat.
