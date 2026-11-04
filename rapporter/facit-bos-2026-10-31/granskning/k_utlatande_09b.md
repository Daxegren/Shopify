# Granskningsutlåtande k_09b (Opus, endast läsning)

Datum: 2026-11-04. Butik bekräftad via API: BEST OF SPORTS (6f2e53-67.myshopify.com). Källan hämtades live på nytt för alla 31 produkter i k_09b_in och k_09c_in (beskrivning, taggar, varianter och pris). Inget ändrades i Shopify.
Utkast: `vag2_skriv/k_09b_utkast.json` (13 produkter). Utkastens nr 9626–9646 överlappar nr i k_08-filerna; identifiera via id. Domar i `vag2_skriv/k_utlatande_09b.json`.

## Domar

| Dom | Antal | Nr |
|---|---|---|
| GODKÄND | 11 | 9626, 9627, 9628, 9630, 9634, 9635, 9640, 9642, 9643, 9644, 9646 |
| RÄTTA | 2 | 9631, 9632 |
| UNDERKÄND | 0 | – |

## Rättningar

**9631 Träningsrulle Elite Roller Arion (10468721983754)** och **9632 Träningsrulle Elite Roller Quick Motion (10472281211146)**
- Källan anger "115 kg (hjul + cyklist)" respektive "115 kg (hjul + förare)". Ordet "hjul" är maskinöversatt (estniska *ratas* betyder både hjul och cykel), så det är oklart vad lasten omfattar.
- Tillverkarens egna sidor anger dessutom **110 kg** för båda modellerna:
  - Arion: https://www.elite-it.com/en/products/home-trainers/rollers/arion ("Maximum load 110 kg", framrullen i 10 lägen)
  - Quick Motion: https://www.elite-it.com/en/home-trainers/classic-rollers/quick-motion ("Load 110 kg", magnetiskt motstånd i 3 lägen, hopfällbar)
- Källan och tillverkaren säger alltså olika saker om en säkerhetsuppgift. Då får 115 kg inte stå (R2, R4). Det tidigare underkännandet av 2112 (2026-11-02) gällde att rullar bär last och behöver en lastuppgift. Därför strycks raden inte. Den ersätts med tillverkarens lägre siffra, med stöd av beslutsloggen 2026-11-04 där tillverkarens egen sida gäller först, och utan någon tolkning av vad lasten omfattar:
  - före: `Belastning enligt tillverkaren: Maximal lastkapacitet 115 kg (hjul + cyklist)` → efter: `Belastning enligt tillverkaren: Maximal last 110 kg` (9631)
  - före: `Belastning enligt tillverkaren: Maximal belastningskapacitet 115 kg (hjul + förare)` → efter: `Belastning enligt tillverkaren: Maximal last 110 kg` (9632)
- Om David hellre vill att uppgiften strycks helt är det alternativet. Det beslutet behövs inte för att skriva.

## Fokuspunkter

- **Meta med verb:** alla 13 metabeskrivningar har verb ("är", "har", "används") och ingen är cirkulär.
- **9630, etiketten Axlar:** etiketten godtas. "Trummor" är maskinöversatt (nav), men måtten är entydiga och den andra raden säger själv "genomgående axel" (R2 tillåter en entydig del). "Enligt tillverkaren" används två gånger, vilket ryms i R5.
- **Typord:** Cykelträningsställ är butikens eget ord på Elite-syskonen 9435–9437 (godkända i k_07). Träningsrulle står i Arions källtext och i Quick Motions live-titel. Sissy squat-bänk står i källtexten. Förslag till koordinatorn: lägg till de tre orden i `godkanda_typord` i profilen.
- **9635, bänk (full granskning):** mått, vikt, färg, justering och 130 kg (en ren svensk rad med etikett) stämmer med källan. Att motståndet kan ökas med vikter är medvetet utelämnat, vilket är rätt. Sissy Squat Profi är en annan produkt och ingen dubblett.
- **9626 och 9628, bänkar:** 9626 har 120 kg från en ren svensk rad. 9628 har ingen lastuppgift i källan och ingen i texten.
- **Elektronik- och hälsoord:** inga kvar. Utelämnat är skonsamhet mot lederna och "exakt pulsmätning" (9627), noggrannheten (9630 har den med "enligt tillverkaren"), säkerhet och balans (9632), rehabilitering och "explosionssäker" (9640) samt flexibilitet (9646).
- **9646, pris 9 kr:** texten godkänns. Live-priset 9 kr är troligen ett prisfel och går till David som en egen fråga. Det påverkar inte texten.
- **Leveranstidsmeningen:** den finns på exakt de produkter som har taggen "På beställning" (9626, 9627, 9630, 9631, 9632, 9642, 9646).

## Avvisade (k_09b_avvisade 12, k_09c_avvisade 6)

Alla 18 avvisningar är motiverade. Nedan granskas de som flaggats som eventuellt för strikta.

- **9636 GT1.0 och 9637 GX3.0:** motiverade. De har 10 respektive 5 varianter med priser från 5 499 till 49 999 kr. Titeln låser en enda variant, och källan innehåller ingen teknisk uppgift.
- **9638 Treadmill Lubrication:** motiverad. Två varianter har olika pris (249 och 299 kr) utan förklaring, och källan är ren marknadsföring.
- **9641 Hammer Core 2.0:** slutsatsen är motiverad, men ett av skälen är fel. Måtten 68 x 77 x 117 cm motsäger inte justeringen. De är minsta läget: bredd 77 cm och höjd 117 cm. Det som håller är att "Lastkapacitet 120 kg" har oklar etikett. Nätet kallar den både användarvikt (fitshop) och maxlast (kaufland), och ingen sida från Hammer hittades. Dessutom är "30 mm kedjor" maskinöversatt (det betyder viktskivor) och säkerhetskrokarna är ett säkerhetspåstående. Ett rack som bär last och har oklar lastetikett ska avvisas.
- **9645 Viktplatta:** motiverad. Den har fem varianter från 59 till 439 kr som bara heter artikelnummer, och källan säger 29 mm medan titeln säger 30 mm.
- **9648 Balansbräda:** avvisningen är tillåten. R3 tillåter antingen avvisning eller kort meta, och den står sig främst för att brädan bär last utan någon lastuppgift. Den är något strängare än 9644 (fotledsvikter), som skrevs med kort meta trots ännu tunnare källa. Det är godtagbart eftersom 9644 inte bär last.
- **9649 Bröstbälte:** motiverad. Den enda uppgiften, 5,3 kHz, står redan i titeln, frekvensomfånget är en trasig rad och Italien är ett ursprungspåstående.
- **9654 Surfplattehållare:** motiverad. Titeln säger "Mega", men källan säger "Apollo Pro XL" och "Platinum RW30" (R3).
- **9655 Exercise Wheel Deluxe:** motiverad. Titeln och källan anger olika modell (Deluxe och Double), typordet saknas i profilen och måttet är oklart. Kan prövas igen med webbkontroll mot tunturi.com enligt v1.6.
- **Övriga:** 9629 (vibrationsplatta, R6), 9633 (batteri, hanteras för hand), 9639, 9650, 9651, 9652 och 9653 (dubbletter) samt 9656 (kroppsanalysvåg, R6) är korrekta. Alla dubblettoriginal är kontrollerade live som aktiva och har taggen texter-klara. 9647 har redan vår egen text, och dess källa är inte tillverkarens.
