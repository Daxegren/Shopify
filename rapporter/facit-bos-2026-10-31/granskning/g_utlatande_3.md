# Granskning faktatext g_3 (bollar, balans, puls, simning, våg) – BEST OF SPORTS (2026-11-04)

Oberoende granskning, bara läsning, enligt regelbok v1.1. Butiken är bekräftad med get-shop-info: **BEST OF SPORTS** (bestofsports.se, SEK).

**Underlag:** `vag2_skriv/g_3_utkast.json` (11 utkast) och `g_3_avvisade.json` (14). Alla 25 är hämtade live (graphql `nodes`). Alla är ACTIVE och har en variant var. Ingen av dem finns i pilotens 20 (`bestofsports-pilot-20-produkter-2026-10-25.csv`). Formatreglerna är redan testade av skript. Granskningen gäller fakta och risk (R1–R7, R11, R15). Varje före-sträng är kontrollerad: den finns exakt en gång i sitt fält.

## Resultat
| Dom | Antal | Nr |
|---|---|---|
| GODKÄND | 4 | 10511, 10543, 10549, 10554 |
| RÄTTA | 2 | 10493, 10526 |
| UNDERKÄND | 5 | 10501, 10539, 10546, 10547, 10561 |

## Per produkt
| Nr | Id | Dom | Före → efter / skäl |
|---|---|---|---|
| 10493 | 10470945816842 | RÄTTA | html: `Steget är avtagbart och täckt med en halkskyddsbeläggning.` → `Steget är avtagbart och enligt tillverkaren täckt med en halkskyddsbeläggning.`; html: `<li>Extra steg: Roterande, avtagbart och med halkskyddsbeläggning</li>` → `<li>Extra steg: Roterande och avtagbart</li>`. Halkskydd är ett halkord (R5). Mått-raderna och 98 cm är rätt utelämnade. Max 150 kg står ordagrant ("Maximal användarvikt: 150 kg") och återges en gång (R4). a_1 (nr 2115) har inte återanvänts. |
| 10501 | 10472300937482 | UNDERKÄND | Tunn källa (R3): bara diametern. Färgen står bara i titeln. Kort meta (§14) eller vänta. |
| 10511 | 10472284684554 | GODKÄND | Alla uppgifter finns i live. Rullar-iväg-påståendet står en gång som enligt tillverkaren. |
| 10526 | 10461962764554 | RÄTTA | meta: `träningsboll av vinyl med diametern` → `träningsboll med diametern`; html: `träningsboll av vinyl med diametern` → `träningsboll med diametern`; html: `<li>Material: Vinyl</li>\n` → (tomt). Live säger både vinyl och "tillverkad av nylon", så materialet utelämnas (R2). Det är rätt enligt R4 v1.1 att sprängsäker och 350 kg är utelämnade. |
| 10539 | 10411857641738 | UNDERKÄND | Källan säger "Double Exercise Wheel" men titeln säger "Deluxe" (R3). Typordet Träningshjul finns varken i källan eller i godkanda_typord (R7). Det är oklart vad måttet gäller. |
| 10543 | 10472296677642 | GODKÄND | Pullbuoy är titelns eget ord och källan säger Pull Buoy (R7 tillåter att titelns ord behålls). Ujumispoi är borttaget. Träningseffekten står en gång som enligt tillverkaren. |
| 10546 | 10472299004170 | UNDERKÄND | Live-texten är vår egen tidigare enmeningstext (facit 30). Utkastet har inga fakta utöver titeln (R3). Live har redan standardblock och SEO-titel, så texten ska lämnas som den är (R15). |
| 10547 | 10475517772042 | UNDERKÄND | Den enda uppgiften är frekvensen, som redan står i titeln. Frekvensomfångsraden är trasig och Italien är en ursprungsuppgift. Det finns noll fakta utöver titeln (R3). Det är en annan produkt än 10546 (annan SKU och annat pris). |
| 10549 | 10472218263818 | GODKÄND | Anmärkning: batteriuppgiften (2 x CR2032, utbytbara) kommer från den delvis trasiga raden. Den delen är entydig och godtas. |
| 10554 | 10472218984714 | GODKÄND | Alla uppgifter finns i live. Produkttypen Crosstrainers är fel i Shopify, men den rörs inte. Flaggas till David. |
| 10561 | 10462778392842 | UNDERKÄND | Produkten är en kroppsanalysvåg (fett, muskelmassa, BMR, kroppsålder). Kategorin står under `utanfor_tills_vidare` (R6). |

## Avvisningarna (14)
Alla 14 avvisningar är kontrollerade live. Alla är riktiga, och ingen kan släppas:
- 10550, 10551, 10552 och 10560 är massagepistoler.
- 10553 är ett värme- och kylhuvud till massagepistol, med ett påstående om smärtlindring.
- 10556–10559 är akupressurmattor.
- 10562 är en vibrerande massagerulle.
- 10563 och 10564 är vibrationsplattor. 10564 säger dessutom V10 i texten men V20 i titeln.
- 10545 är en kroppsanalysvåg.
- 10520 tillhör ingen spärrad kategori, men live-texten är bara vår egen enmeningstext, så det finns ingen faktagrund (R3).

## Oklart i regelbok och prompt
1. R2 säger inte om en entydig del av en delvis trasig rad får användas (10549).
2. R3 säger inte om vår egen tidigare text räknas som källa (10546, 10520).
3. R5 räknar upp "halkfri" men inte "halkskydd". Gäller det också beskrivande materialord?
4. Profilen saknar ett beslut om pulsband och bröstbälten, alltså elektronik. Den äldre c_granskarprompt räknar elektronik som säkerhetsprodukt, men R6 säger att profilen är facit.
5. Typord som andra utkast har använt (h_3 10502 Träningshjul) har ingen status. De bör antingen föras in i `godkanda_typord` eller förbjudas.
