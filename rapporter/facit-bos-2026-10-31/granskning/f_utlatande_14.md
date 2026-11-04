# Granskning faktatext f_14 (kettlebells och träningsbänkar) – BEST OF SPORTS (2026-11-04)

Oberoende granskning, endast läsning. Butiken bekräftad med get-shop-info: **BEST OF SPORTS** (bestofsports.se, SEK).

**Underlag:** `vag2_skriv/f_14_utkast.json` (19 poster), `f_14_avvisade.json` (10329, 10331, 10335, 10338, 10339, 10340). FAKTATEXTLÄGE (§14–17, `fakta_utkastprompt.md`); meta 70–155 (§17); standardblocket jämfört med `b_skriv_24.json`; Davids beslut alt A 2026-11-04.

**Metod:** alla 25 hämtade live (graphql `nodes`), alla ACTIVE, productType oförändrad (Konditionsträning & Fitness). Maskinellt: längder, kommatecken, `format_regler.py` (titel_versaler, kolon_versal – inga avvikelser), '&', bindestreck i intervall, standardblock, beställningsmening, unikhet mot alla övriga `*.json` i vag2_skriv och inom filen. Standardblocket identiskt på alla 19; beställningsmeningen står exakt bara på 10336 (enda med taggen 'På beställning'). Titlar 29–57 tecken (högst 2 kommatecken), SEO 29–42, meta 79–154. Inga dubbletter, inga id-krockar med skrivfiler (10349 finns bara i a_4_in.json som nr 2401, inte i något utkast).

## Resultat
| Dom | Antal | Nr |
|---|---|---|
| GODKÄND | 13 | 10326, 10327, 10332, 10334, 10336, 10337, 10342, 10343, 10344, 10346, 10348, 10349, 10350 |
| RÄTTA | 5 | 10328, 10330, 10341, 10345, 10347 |
| UNDERKÄND | 7 | 10333 (utkast) samt avvisningarna 10329, 10331, 10335, 10338, 10339, 10340 (bekräftade) |

## Särskilda kontroller
- **Lastgränser (alt A):** 10341 140 kg, 10343 100 kg, 10344 100 kg, 10345 140 kg ('Maximal användarvikt'); 10347 130 kg, 10348 130 kg, 10350 200 kg ('Maximal belastning'); 10349 250 kg ('Max. belastningskapacitet') – alla står ordagrant på svenska med enhet i just den produktens live-källa, återges en gång i text som 'enligt tillverkaren' plus specifikationsraden (som i f_9/f_10). Ingen står i titel eller meta. Godtas.
- **Utan maxvikt:** 10342 och 10346 saknar maxvikt i källan och ingen återges – rätt.
- **'Säkerhetsrem' (10342):** ordagrant i källan ('Inkluderar säkerhetsrem och armstöd'), återges bara som det som ingår ('Ingår: Säkerhetsrem och armstöd'), inget säkerhetslöfte. Godtas.
- **Vikt samma tal överallt:** kettlebells 10326–10337 har samma vikt och enhet (kg, liten bokstav) i titel, SEO-titel, meta, text och specifikation; vikten stöds av SKU (handle-suffix +2 på Olympic EVO/Vinyl följs inte, samma mönster i alla). 10333 har ingen vikt (underkänd).
- **Typord:** Kettlebell, Träningsbänk, Inversionsbänk enhetligt; 'Treeningpink' (estniska) och 'Weight Bench' ersatta med Träningsbänk.
- **Cirkulära inledningar:** inga ('X är en kettlebell/träningsbänk' med modellnamn, inte engelskt typord).
- **Syskonläckage:** inget; Vinyl 12/20 kg och Olympic EVO lila/gul har egna tal; Tricon och Tricon Flex har egna mått.

## Per produkt
| Nr | Id | Dom | Skäl och rättning (fullständigt före/efter i f_utlatande_14.json) |
|---|---|---|---|
| 10326 | 10472327905546 | GODKÄND | Stål, 20 kg (titel, SKU AKCA-20, en variant) och hemmabruk/sportklubbar ('enligt tillverkaren') ur källan; kvalitets-, grepp- och livslängdspåståenden borta. |
| 10327 | 10472328790282 | GODKÄND | Lila och 20 kg ur titeln, SKU KCAE-20 stöder vikten (handle -22 följs inte, samma mönster som 10332). Gym/hemmaträning 'enligt tillverkaren'; maskinöversatt 'spännbomber', material och ergonomi utelämnade. |
| 10328 | 10472299561226 | RÄTTA | Data rätt (12 kg, vinylbelagd yta). Rättning: meta-ordföljden 'yta på 12 kg' blir som i inledningen.<br>meta: `Toorx Vinyl är en kettlebell med vinylbelagd yta på 12 kg. Enligt tillverkaren finns kettlebellsen i flera vikter. Finns hos BEST OF SPORTS.` → `Toorx Vinyl är en kettlebell på 12 kg med vinylbelagd yta. Enligt tillverkaren finns kettlebellsen i flera vikter. Finns hos BEST OF SPORTS.` |
| 10329 | 10472300052746 | UNDERKÄND | Avvisningen bekräftas live: Titeln anger 10 kg, men produkten har tre varianter (KRV-10 till 649 kr, KRV-16 och KRV-14 till 789 kr) med oförklarade namn. Titeln stämmer inte med produkten och vikten går inte att låsa. Kan skrivas när varianterna är uppdelade. |
| 10330 | 10472329380106 | RÄTTA | Som 10328 (20 kg, SKU KRV-20). Rättning: meta-ordföljden.<br>meta: `Toorx Vinyl är en kettlebell med vinylbelagd yta på 20 kg. Enligt tillverkaren finns kettlebellsen i flera vikter. Finns hos BEST OF SPORTS.` → `Toorx Vinyl är en kettlebell på 20 kg med vinylbelagd yta. Enligt tillverkaren finns kettlebellsen i flera vikter. Finns hos BEST OF SPORTS.` |
| 10331 | 10430254809354 | UNDERKÄND | Avvisningen bekräftas live: Titeln anger blå och 12 kg, men SKU är KCAE-14 medan övriga Olympic EVO har SKU som motsvarar vikten (KCAE-16 = 16 kg, KCAE-18 = 18 kg, KCAE-20 = 20 kg). Källan säger varken vikt eller färg. Motsägande uppgift om vikten; kan skrivas när leverantören bekräftat 12 eller 14 kg. |
| 10332 | 10472328462602 | GODKÄND | Gul, 16 kg, SKU KCAE-16. Som 10327. |
| 10333 | 10588451635466 | UNDERKÄND | Fyra varianter (25TUPLA100–103, 1599/1619 kr) med oförklarade namn, handle anger 12 kg. Texten 'Finns i flera vikter' gör att kunden tror varianterna är vikter utan att veta vilken. Live-texten är en tidigare genererad text (FAQ, 'Om märket'), inte leverantörens; 'internationell tävlingsstandard' går inte att belägga. Samma mönster som 10254/10257/10335. Skrivs när varianterna fått namn. |
| 10334 | 10548292649226 | GODKÄND | Gjutjärn och 4 kg (titel, SKU, en variant). Kort meta 79 tecken. 'Avancerade atleter'/tung styrketräning borta. |
| 10335 | 10541372801290 | UNDERKÄND | Avvisningen bekräftas live: Titeln anger 8 kg, men produkten har sex varianter (25TUPLA071 till 389 kr och 25TUPLA070, 072–075 till 679 kr) med oförklarade namn. Källan nämner ingen vikt. Titeln stämmer inte med produkten. |
| 10336 | 10472315126026 | GODKÄND | Svart (enda variant 'black'), 4 kg, gummiöverdrag, stålhandtag ordagrant. Beställningsmeningen står exakt (tagg 'På beställning'); fettförbränning, golvskydd, rostskydd borta. |
| 10337 | 10475372642570 | GODKÄND | 8 kg, svart, stål ordagrant; oklara rader 'Handtagets diameter: 21 cm'/'8,5 kg: 21 cm', hälso- och viktminskningstext borta. |
| 10338 | 10548235862282 | UNDERKÄND | Avvisningen bekräftas live: Titeln anger PE, men källtexten anger genomgående PVC med sandfyllning ("PVC-kettle"). Motsägande materialuppgift mellan titel och källa; källan innehåller dessutom garblad text. Går inte att skriva säkert utan besked om PE eller PVC. |
| 10339 | 10548235403530 | UNDERKÄND | Avvisningen bekräftas live: Titeln anger PE, men källtexten anger genomgående PVC med sandfyllning. Motsägande materialuppgift mellan titel och källa; källan innehåller dessutom en oklar rad ("Iga"). Går inte att skriva säkert utan besked om PE eller PVC. Samma sak som 10338. |
| 10340 | 10462836490506 | UNDERKÄND | Avvisningen bekräftas live: Vikten 3,5 kg står bara i produktnamnet; källan anger inte om den avser handtaget eller en största vikt för en justerbar kettlebell, och tillbehöret (skruv för att fästa vikter, Add-On Kit) bär last. Källan har dessutom en tom rad ("Mått"). Kan skrivas när vikten och kompatibiliteten bekräftats. |
| 10341 | 10589705568522 | RÄTTA | Maximal användarvikt 140 kg ordagrant svenska med enhet, en gång 'enligt tillverkaren' (+ spec, som f_9/f_10). Rättning: källan ('Det justerbara ryggstödet och fotstöden') säger inte entydigt att fotstöden är justerbara; punkten och specen görs neutrala.<br>html: `<li>Dig som söker en träningsbänk med justerbara fotstöd</li>` → `<li>Dig som söker en träningsbänk med fotstöd</li>`; `<li>Fotstöd: Justerbara</li>` → `<li>Fotstöd: Ja</li>` |
| 10342 | 10472323711242 | GODKÄND | Ingen maxvikt i källan och ingen återges. 'Säkerhetsrem' står ordagrant ('Inkluderar säkerhetsrem och armstöd') och återges bara som det som ingår, inget löfte. 'Sträcka ryggraden' borta. 92 grader, mått, vikt ordagrant. Handle -2 men ingen annan Zero i butiken. |
| 10343 | 10472323514634 | GODKÄND | Maximal användarvikt 100 kg ordagrant svenska. Justerbart ryggstöd, sits med lutning, mått, vikt ordagrant. 'Treeningpink' → Träningsbänk (taggen träningsbänk). |
| 10344 | 10565602410762 | GODKÄND | Maximal användarvikt 100 kg ordagrant svenska. Stålkonstruktion, ryggstöd med flera positioner, skivförvaring, mått, 46 kg ordagrant; 'förstärkt', stabilitet, säkerhet borta. Typord från live-titeln. |
| 10345 | 10472323481866 | RÄTTA | Maximal användarvikt 140 kg ordagrant svenska. Rättning: stavfel 'sitlägen' → 'sitslägen'; SEO-titeln 'Weight Adjustable' är inget modellnamn – live-titeln är 'Weight Bench BH FITNESS Adjustable', modellen är Adjustable.<br>html: `ryggstöds- och sitlägen` → `ryggstöds- och sitslägen`<br>seo_title: `Träningsbänk BH Fitness Weight Adjustable` → `Träningsbänk BH Fitness Adjustable` |
| 10346 | 10472264597770 | GODKÄND | Tunn källa; inga mått/maxvikt och ingen återges. 'Designad för att ... träna mag- och ryggmuskulatur' står ordagrant och återges 'enligt tillverkaren' utan 'effektivt'; stabil/ergonomisk borta. 'Ab&Back' → 'Ab och Back' godtas (inga '&'), se fråga. |
| 10347 | 10472264892682 | RÄTTA | Maximal belastning 130 kg ordagrant svenska med enhet, en gång 'enligt tillverkaren'. Rättning: 'för rygg- och magträning' omskriver källans effektpåstående ('för att stärka rygg- och magmusklerna') utan att vara ordagrant – stryks; 'hemma' står i källan. Tyskland borta (rätt).<br>html: `<p>Finnlo by Hammer Tricon är en justerbar och hopfällbar träningsbänk för rygg- och magträning hemma.` → `<p>Finnlo by Hammer Tricon är en justerbar och hopfällbar träningsbänk för träning hemma.` |
| 10348 | 10507302764810 | GODKÄND | Maximal belastning 130 kg ordagrant svenska i egen källa. 'Ryggträning, hyperextensions och stretching/stretchfunktioner' ordagrant. Mått, yta, hopfälld, 17 kg ordagrant; FAQ 'medicinsk produkt' borta. |
| 10349 | 10472298840330 | GODKÄND | 'Max. belastningskapacitet: 250 kg' står ordagrant på svenska med enhet i egen källa och godtas en gång 'enligt tillverkaren' (alt A). 7-/3-stegs justering, avsmalnande sittdyna, extra negativ position, mått med tankstreck, 24 kg ordagrant. |
| 10350 | 10507303354634 | GODKÄND | Maximal belastning 200 kg ordagrant svenska. 40 mm stoppning, två hjul och handtag, mått, 15,5 kg ordagrant; 'studiokvalitet', 'små lägenheter' borta. |

## Öppna frågor till David
1. **10346:** godtas modellnamnet 'Ab och Back Trainer' (i stället för 'Ab&Back') i titel och text, eller ska '&' behållas/skrivas 'Ab/Back'?
2. **10333 och 10335, 10329:** varianterna har bara SKU som namn (25TUPLA100–103, 25TUPLA070–075, KRV-10/14/16). Kan Velomarket eller vi namnge varianterna med vikt? Då kan de skrivas.
3. **10338/10339:** PE (titel) eller PVC med sand (källan)? **10331:** 12 eller 14 kg (SKU KCAE-14)? **10340:** avser 3,5 kg handtaget?
4. **10342 (inversionsbänk):** källan anger ingen maximal användarvikt. Texten skriver ingen, men vill du att leverantören tillfrågas innan en inversionsbänk säljs med ny text?
