# Mätning av regeltester mot granskningsfacit (2026-11-06)

Skapad 2026-11-06. Filen skapas av `shopify-sync/scripts/mat_regeltester.py` (kör `python3 -I shopify-sync/scripts/mat_regeltester.py`); tabellerna nedan är skriptets utskrift oförändrad. Fråga som besvaras: hur stor andel av granskarnas (Opus) rättningar hade kod kunnat fånga, och hur många godkända utkast hade koden larmat på i onödan.

## Underlag och metod

- **Underlag:** utkasten (`*_utkast.json`) och granskarutlåtandena (`*utlatande*.json`) i `rapporter/facit-bos-2026-10-31/vag2_skriv/`. Testfilen `test_sonnet_utlatande_5_8.json` (Sonnet som granskare) är inte facit och räknas inte med.
- **Antal:** 2 931 poster i utlåtandena; efter borttagning av samma utkast med samma utfall bedömt två gånger återstår **2 781 bedömningar** av 2 634 produkter: 1 387 godkända (49,9 %), 1 196 rättade (43,0 %), 198 underkända eller avvisade (7,1 %). Det ger **2 496 enskilda rättningar** (före/efter) i de 1 196 rättade produkterna. Måttet 45 / 44 / 11 % från 2026-11-04 gällde ca 1 700 utkast; fördelningen är i stort sett oförändrad med de senare batcherna.
- **Sortering av rättningar:** `shopify-sync/scripts/rattningstyper.py` sorterar varje före/efter-par efter typ med regler på texten. Granskarens motivering (`skal`) gäller hela produkten, inte varje rättning, och används därför inte för sorteringen. Sorteringen är inte validerad mot en manuell sortering; ett stickprov på 30 slumpade rättningar gav 27 rimliga placeringar (3 var gränsfall mellan "ordval" och "omskriven"). Typtabellen ska läsas som en grov kartläggning.
- **Format eller innehåll:** 359 rättningar (14,4 %) är format och 2 137 (85,6 %) är innehåll, i linje med måttet 12 / 87 % från `mat_utbyte.py` (skillnaden beror på att "N tum" och skiljetecken räknas som format här). 131 av 1 196 produkter rättades enbart på format.
- **Träningsdel och provdel:** kontrollerna utformades med hjälp av utlåtandefilerna b_, c_, f_ och g_ (träningsdel: 575 godkända, 635 rättade, 1 396 rättningar). Utlåtandefilerna h_ och k_ (provdel: 812 godkända, 561 rättade, 1 100 rättningar) användes inte när mönstren valdes. **Provdelens siffror är de som ska läsas som förväntad effekt framåt**; träningsdelens siffror är för optimistiska. Exempel: de nya testerna fångade 20,8 % av rättningarna i träningsdelen men 9,2 % i provdelen.
- **Tröskel:** en ny kontroll får stå på (läge varning) om den larmar på högst 2 % av de godkända utkasten i både träningsdelen och provdelen och fångar minst 0,3 % av rättningarna i minst en av delarna. Kontroller över tröskeln finns kvar i koden men står i läget `av` i `shopify-sync/config/regeltester.json`. Alla nya kontroller som är på står i läget **varning** och stoppar ingenting; ingen får läget fel utan Davids beslut.
- **Falsklarm betyder här:** kontrollen larmar på ett utkast som Opus godkände utan rättning. Det är en övre gräns: LARDOMAR 2026-11-04 visar att Opus ibland missar fel som ett test hittar, så en del av dessa larm kan vara riktiga fel.

## Förbehåll som påverkar hur siffrorna ska läsas

1. **Urvalet är delvis det som de gamla kontrollerna inte fångade.** Enligt `shopify-sync/regler/agentprompter.md` kör utkastarna `skrivfil_kontroll.py` på sina utkast före granskningen, och flera av kontrollerna tillkom under arbetets gång. Rättningar som de gamla kontrollerna redan fångat före granskningen finns därför inte kvar i facit, och de gamla kontrollernas täckning (särskilt i provdelen) är en underskattning. De nya kontrollernas täckning är däremot mätt på rättningar som de gamla missade.
2. **En enda batch väger tungt.** Utlåtandet `b_utlatande_49_50.json` står för 220 av 2 496 rättningar (8,8 %), varav 141 gäller samma ord (scooter → sparkcykel). Det är skälet till att `BUTIKSORD` fångar 9,1 % i träningsdelen men 1,9 % i provdelen.
3. **Granskarna är inte konsekventa på två punkter.** "N tums hjul/däck" rättas ibland till "N-tumshjul" men godkänns i 2–5 % av de godkända utkasten (`TUM_HJUL`). Metabeskrivning utan verb rättas i 114 fall men godkänns i 6,7 % av provdelens godkända utkast (`META_UTAN_VERB`). En kontroll kan inte vara skarpare än regeln; se `shopify-sync/regler/regelforslag-2026-11.md`.
4. **Det befintliga varningstestet "Namn är en/ett typord" är brusigt:** det larmar på 83 % av träningsdelens och 44 % av provdelens godkända utkast och särskiljer därför inte rätt från fel. Det räknas inte med i totalerna nedan. Det nya testet `CIRKULAR_TYPORD` är snävare (typordet måste vara samma ord som ett ord i namnet) och larmar på 0,5 % respektive 0 % av de godkända.
5. **Rättningstypen "fångad" för nya kontroller kräver att larmet ligger i samma fält och överlappar texten granskaren ändrade.** För de gamla kontrollerna (svart låda) räcker det att rättningens typ är den kontrollen avser.

## Rättningstyper (steg 1)

Antal är enskilda rättningar (ett före/efter-par); "Produkter" är antal rättade produkter som har minst en rättning av typen. Grupp F = format, I = innehåll. De två sista kolumnerna visar hur många rättningar av typen som de nya respektive gamla testerna fångar.

| Typ | Grupp | Antal | Andel | Produkter | Exempel (före → efter) | Fångas av nya tester | Fångas av gamla tester (utan brusiga) |
|---|---|---:|---:|---:|---|---:|---:|
| ordval (enstaka ord byts) | I | 468 | 18.8 % | 295 | `scooterhjul → sparkcykelhjul; power rack → träningsställ` | 96 | 0 |
| typord/ordval bytt i titel eller SEO-titel (R7) | I | 286 | 11.5 % | 175 | `Scooterhjul Union Dragon → Sparkcykelhjul Union Dragon` | 76 | 0 |
| mening omskriven | I | 217 | 8.7 % | 185 | `den ska inte överskrida den rekommenderade dagliga mängden → den rekommenderade dagliga mängden ska inte överskridas` | 23 | 0 |
| mening/led borttaget | I | 193 | 7.7 % | 152 | `Enligt tillverkaren ger de ett säkert grepp även i regn. → (borttaget)` | 4 | 0 |
| specifikationsrad borttagen | I | 165 | 6.6 % | 153 | `<li>Handtag: Bekvämt handtag</li> → (borttaget)` | 6 | 0 |
| cirkulär inledning "X är en/ett …" omskriven (R11) | I | 155 | 6.2 % | 96 | `Selle Monte Grappa är ett kjolskydd i svart läder → Kjolskyddet från Selle Monte Grappa är i svart läder` | 17 | 14 |
| bindestreck, mellanslag eller skiljetecken | F | 150 | 6.0 % | 85 | `27.5×2.2 → 27,5×2,2` | 84 | 0 |
| tal/mått/uppgift ändrat | I | 117 | 4.7 % | 93 | `lastgräns "1–10 kg" fyra gånger → en gång, "enligt tillverkaren"` | 7 | 0 |
| meta/inledning saknade verb (R11) | I | 114 | 4.6 % | 114 | `Skivstångspaket med curlstång på 120 cm → Skivstångspaket BASIC har en curlstång på 120 cm` | 1 | 39 |
| "enligt tillverkaren" tillagt (R4/R5) | I | 87 | 3.5 % | 64 | `Sadeln har en ergonomisk design → Sadeln har enligt tillverkaren en ergonomisk design` | 27 | 0 |
| böjning/stavning/grammatik (ett ord) | I | 75 | 3.0 % | 57 | `pakväska → packväska` | 1 | 0 |
| tum-form (N tum → N-tums) | F | 56 | 2.2 % | 33 | `27,5 tum → 27,5-tumshjul; 7 tum skärm → 7-tums skärm` | 23 | 0 |
| FAQ-avsnitt borttaget | I | 56 | 2.2 % | 56 | `<h2>Vanliga frågor</h2>… → (borttaget)` | 0 | 56 |
| titel/SEO-titel kompletterad (ord tillagt) | I | 46 | 1.8 % | 33 | `Sadel Liv Contact Comfort → Sadel Liv Contact Comfort Forward` | 0 | 0 |
| "enligt tillverkaren" borttaget/omformulerat (R4/R5) | I | 42 | 1.7 % | 40 | `Skydd: Mot regn, smuts och damm, enligt tillverkaren → Skydd: Regn, smuts och damm` | 10 | 0 |
| målgruppsrad ("Dig som …") borttagen | I | 41 | 1.6 % | 39 | `<li>Dig som vill ha handskar med UPF-solskydd</li> → (borttaget)` | 4 | 0 |
| versal/gemen efter kolon eller snedstreck i specifikationsrad | F | 40 | 1.6 % | 37 | `Färg: blå → Färg: Blå` | 0 | 21 |
| versal/gemen i titel eller SEO-titel | F | 37 | 1.5 % | 23 | `Skivstång, 18 mm, justerbart → …, Justerbart` | 0 | 4 |
| tal/mått/variant ändrat i titel eller SEO-titel | I | 32 | 1.3 % | 28 | `Giant TCR Advanced 2 PC, 700x25c → …, 700c` | 0 | 0 |
| versal/gemen i löptext | F | 26 | 1.0 % | 21 | `Orange → orange` | 0 | 0 |
| ord/märke i VERSALER → normal skrivning | F | 26 | 1.0 % | 20 | `Träningsbänk TUNTURI CT40 → Träningsbänk Tunturi CT40` | 1 | 20 |
| utfyllnaden "Finns hos BEST OF SPORTS." borttagen | I | 16 | 0.6 % | 16 | `… Finns hos BEST OF SPORTS. → (borttaget)` | 0 | 16 |
| ord/märke → VERSALER | F | 14 | 0.6 % | 5 | `SOKE Evo → SOKE EVO` | 0 | 0 |
| text tillagd/utökad | I | 13 | 0.5 % | 13 | `är ett kodlås av stål. → är ett vajerlås med kod, tillverkat av stål.` | 0 | 0 |
| enhet i versaler (psi, hk, kg …) | F | 10 | 0.4 % | 7 | `120 PSI → 120 psi; 3.0 HP → 3,0 hk` | 10 | 0 |
| leveranstidsmening (R13) borttagen | I | 7 | 0.3 % | 7 | ` Beställningsvaror kan ta upp till en vecka längre. → (borttaget)` | 0 | 0 |
| leveranstidsmening (R13) tillagd | I | 5 | 0.2 % | 5 | `Se sidan Frakt för övriga länder.</p> → Se sidan Frakt för övriga länder. Beställningsvaror kan` | 0 | 0 |
| titel/SEO-titel omskriven | I | 2 | 0.1 % | 2 | `Dricksflaska Liv Doublespring 750 ml Vit → Dricksflaska Liv 750 ml, Vit, Lila och Blå` | 1 | 0 |
| **Summa** | | **2496** | 100 % | 1196 | | **391** | **170** |

## Mätning (steg 3)

Bedömningar efter borttagning av dubbletter: 2781 (godkända 1387, rättade 1196, övriga underkända/avvisade 198). Träningsdel (utlåtandefiler b_, c_, f_, g_): 575 godkända, 635 rättade (1396 enskilda rättningar). Provdel (h_, k_): 812 godkända, 561 rättade (1100 enskilda rättningar).

Tröskel för att en ny kontroll får vara på: högst 2 % falsklarm bland godkända utkast i både träningsdelen och provdelen, och minst 0.3 % av rättningarna fångade i minst en av delarna.

#### Nya kontroller (regeltester.py)

| Kontroll | Regel | Läge nu | Fångar rättningar (träning) | Fångar rättningar (prov) | Falsklarm godkända (träning) | Falsklarm godkända (prov) | Larm på rättade utkast (prov) | Tröskel |
|---|---|---|---:|---:|---:|---:|---:|---|
| `DECIMALPUNKT` | R9 | varning | 17 av 1396 (1.2 %) | 31 av 1100 (2.8 %) | 2 av 575 (0.3 %) | 1 av 812 (0.1 %) | 13 av 561 (2.3 %) | klarar |
| `TUM_SKARM` | R10 | varning | 22 av 1396 (1.6 %) | 0 av 1100 (0.0 %) | 4 av 575 (0.7 %) | 1 av 812 (0.1 %) | 1 av 561 (0.2 %) | klarar |
| `TUM_HJUL` | R10 | av | 12 av 1396 (0.9 %) | 38 av 1100 (3.5 %) | 14 av 575 (2.4 %) | 37 av 812 (4.6 %) | 44 av 561 (7.8 %) | klarar inte |
| `APOSTROF` | R8 | varning | 0 av 1396 (0.0 %) | 28 av 1100 (2.5 %) | 0 av 575 (0.0 %) | 0 av 812 (0.0 %) | 7 av 561 (1.2 %) | klarar |
| `ENHET_FORM` | R9 | varning | 10 av 1396 (0.7 %) | 1 av 1100 (0.1 %) | 1 av 575 (0.2 %) | 0 av 812 (0.0 %) | 1 av 561 (0.2 %) | klarar |
| `BUTIKSORD` | R7 | varning | 127 av 1396 (9.1 %) | 21 av 1100 (1.9 %) | 0 av 575 (0.0 %) | 3 av 812 (0.4 %) | 6 av 561 (1.1 %) | klarar |
| `TYPORD_FEL_PLATS` | R7 | av | 10 av 1396 (0.7 %) | 3 av 1100 (0.3 %) | 26 av 575 (4.5 %) | 46 av 812 (5.7 %) | 37 av 561 (6.6 %) | klarar inte |
| `ENGELSKT_TYPORD` | R7 | varning | 51 av 1396 (3.7 %) | 11 av 1100 (1.0 %) | 3 av 575 (0.5 %) | 1 av 812 (0.1 %) | 5 av 561 (0.9 %) | klarar |
| `CIRKULAR_TYPORD` | R11 | varning | 16 av 1396 (1.1 %) | 5 av 1100 (0.5 %) | 3 av 575 (0.5 %) | 0 av 812 (0.0 %) | 5 av 561 (0.9 %) | klarar |
| `KVALITETSORD_UTAN_ETV` | R5 | varning | 49 av 1396 (3.5 %) | 6 av 1100 (0.5 %) | 4 av 575 (0.7 %) | 0 av 812 (0.0 %) | 7 av 561 (1.2 %) | klarar |
| `LASTGRANS_UTAN_ETV` | R4 | av | 11 av 1396 (0.8 %) | 0 av 1100 (0.0 %) | 113 av 575 (19.7 %) | 3 av 812 (0.4 %) | 0 av 561 (0.0 %) | klarar inte |
| `META_UTAN_VERB` | R11 | av | 11 av 1396 (0.8 %) | 113 av 1100 (10.3 %) | 1 av 575 (0.2 %) | 54 av 812 (6.7 %) | 137 av 561 (24.4 %) | klarar inte |

#### Befintliga kontroller i skrivfil_kontroll.py (oförändrade; svart låda)

Täckning räknas på typnivå: kontrollen larmar på utkastet och rättningen är av den typ kontrollen är avsedd för. Falsklarm = larm på godkända utkast. Obs: i de senare batcherna (k_) kördes dessa kontroller redan före granskningen, så rättningar de hade fångat finns inte kvar i facit; täckningen är därför en underskattning.

| Kontroll | Fångar rättningar (träning) | Fångar rättningar (prov) | Falsklarm godkända (träning) | Falsklarm godkända (prov) | Larm på rättade utkast (prov) |
|---|---:|---:|---:|---:|---:|
| FEL cirkulär inledning (X är en X) | 14 av 1396 (1.0 %) | 0 av 1100 (0.0 %) | 7 av 575 (1.2 %) | 0 av 812 (0.0 %) | 3 av 561 (0.5 %) |
| VARN meta/första meningen börjar "Namn är en/ett" | 57 av 1396 (4.1 %) | 141 av 1100 (12.8 %) | 479 av 575 (83.3 %) | 360 av 812 (44.3 %) | 254 av 561 (45.3 %) |
| VARN meta saknar verb (gamla) | 1 av 1396 (0.1 %) | 38 av 1100 (3.5 %) | 0 av 575 (0.0 %) | 1 av 812 (0.1 %) | 38 av 561 (6.8 %) |
| FEL liten bokstav efter kolon | 21 av 1396 (1.5 %) | 0 av 1100 (0.0 %) | 0 av 575 (0.0 %) | 0 av 812 (0.0 %) | 0 av 561 (0.0 %) |
| FEL märket i versaler | 16 av 1396 (1.1 %) | 4 av 1100 (0.4 %) | 0 av 575 (0.0 %) | 0 av 812 (0.0 %) | 1 av 561 (0.2 %) |
| FEL FAQ-avsnitt kopierat | 56 av 1396 (4.0 %) | 0 av 1100 (0.0 %) | 1 av 575 (0.2 %) | 0 av 812 (0.0 %) | 0 av 561 (0.0 %) |
| VARN utfyllnaden "Finns hos BEST OF SPORTS." | 16 av 1396 (1.1 %) | 0 av 1100 (0.0 %) | 9 av 575 (1.6 %) | 0 av 812 (0.0 %) | 0 av 561 (0.0 %) |
| FEL stor bokstav efter bindestreck | 0 av 1396 (0.0 %) | 4 av 1100 (0.4 %) | 0 av 575 (0.0 %) | 2 av 812 (0.2 %) | 2 av 561 (0.4 %) |
| VARN dubbla mellanslag | 1 av 1396 (0.1 %) | 0 av 1100 (0.0 %) | 58 av 575 (10.1 %) | 3 av 812 (0.4 %) | 1 av 561 (0.2 %) |

#### Totalt: andel av granskarnas rättningar som koden hade fångat

Nya tester = bara kontroller som är på (läge varning eller fel). Gamla tester = kontrollerna i tabellen ovan som själva klarar falsklarmströskeln (FEL FAQ-avsnitt kopierat, FEL cirkulär inledning (X är en X), FEL liten bokstav efter kolon, FEL märket i versaler, FEL stor bokstav efter bindestreck, VARN meta saknar verb (gamla), VARN utfyllnaden "Finns hos BEST OF SPORTS."); de brusiga räknas inte med. Fångat = en kontroll larmar på rätt ställe (nya) eller av rätt typ (gamla).

| Mått | Träning | Prov | Alla |
|---|---:|---:|---:|
| Rättningar fångade av nya tester | 290 av 1396 (20.8 %) | 101 av 1100 (9.2 %) | 391 av 2496 (15.7 %) |
| Rättningar fångade av gamla tester | 124 av 1396 (8.9 %) | 46 av 1100 (4.2 %) | 170 av 2496 (6.8 %) |
| Rättningar fångade av nya eller gamla | 401 av 1396 (28.7 %) | 147 av 1100 (13.4 %) | 548 av 2496 (22.0 %) |
| Rättade produkter där minst en rättning fångas (nya) | 107 av 635 (16.9 %) | 37 av 561 (6.6 %) | 144 av 1196 (12.0 %) |
| Rättade produkter där alla rättningar fångas (nya) | 66 av 635 (10.4 %) | 22 av 561 (3.9 %) | 88 av 1196 (7.4 %) |
| Rättade produkter där alla rättningar fångas (nya eller gamla) | 120 av 635 (18.9 %) | 51 av 561 (9.1 %) | 171 av 1196 (14.3 %) |
| Godkända utkast som får minst ett larm från nya tester (falsklarm) | 17 av 575 (3.0 %) | 6 av 812 (0.7 %) | 23 av 1387 (1.7 %) |

## Slutsatser

- De nya testerna hade fångat **15,7 %** av alla rättningar (20,8 % i träningsdelen, **9,2 % i provdelen**). Räknat per produkt: 12,0 % av de rättade produkterna hade fått minst ett larm och 7,4 % hade fått larm på samtliga sina rättningar (3,9 % i provdelen). Tillsammans med de gamla testerna som själva klarar tröskeln: 22,0 % av rättningarna (13,4 % i provdelen) och 14,3 % av de rättade produkterna med alla rättningar fångade.
- Falsklarmen bland godkända utkast: sammanlagt 1,7 % (23 av 1 387) har fått minst ett larm av de nya testerna, 3,0 % i träningsdelen och 0,7 % i provdelen. Varje enskild kontroll ligger på högst 0,7 % (undantaget `TUM_HJUL` m.fl. som står i läget `av`).
- **Slutsats för kostnaden:** koden kan ta bort omkring en tiondel av rättningarna, inte hälften. 85,6 % av rättningarna är innehåll som kräver jämförelse mot källan (påståenden, uppgifter, ordval), och bara ett fåtal av dem går att uttrycka som regel utan att larma på godkända utkast. Opus-granskningen minskar inte nämnvärt av testerna ensamma. Det som sparas är att utkastare och Sonnet kan få larmen i förväg och rätta innan Opus läser, vilket tar bort de upprepade fynden (scooter → sparkcykel, decimalpunkt, apostrof, kvalitetsord, engelska typord) ur Opus uppgift.
- Kontroller som provades men inte kan vara på: `TYPORD_FEL_PLATS` (4,5 % / 5,7 % falsklarm: SEO-titlar med märket först godkänns ofta), `TUM_HJUL`, `LASTGRANS_UTAN_ETV` (19,7 % falsklarm i träningsdelen, 0 träffar i provdelen) och `META_UTAN_VERB` (10,3 % av provdelens rättningar skulle fångas, men 6,7 % falsklarm). I prototyp utanför koden mättes dessutom "SEO-titeln har tappat märket" (0,5 % täckning, 1,4 % falsklarm, 0 träffar i provdelen) och bedömdes inte värd att införa.
- Förslag till nya granskarregler för det som inte går att kodifiera finns i `shopify-sync/regler/regelforslag-2026-11.md`. `regler-v1.md` är inte ändrad.

## Så här körs det

- Enhetstester (nätverksfria): `python3 -I shopify-sync/scripts/test_regeltester.py`
- Kontroll av en skrivfil: `python3 -I shopify-sync/scripts/skrivfil_kontroll.py FIL`; nya larm skrivs ut på en egen rad som börjar med `regeltester:`. Läge per kontroll: `shopify-sync/config/regeltester.json`.
- Mätningen görs om med `python3 -I shopify-sync/scripts/mat_regeltester.py > shopify-sync/status/regeltester-matning-ny.md` (skriv inte över den här filen utan beslut).
