# Granskningsutlåtande k_11d (spray, vattenflaskor, viktställ, viktvästar, paket och åtta Gymstick-produkter)

Granskare: Opus. Endast läsning, inga ändringar i Shopify. Datum 2026-11-04. Alla 25 produkter (15 utkast och 10 avvisade) hämtades live via Admin API (`shopify_api.hamta_produkter`). Varianter, SKU och priser hämtades via GraphQL. De åtta webbkällorna på gymstick.com hämtades och lästes. Underlag: regelbok v1.6, beslutslogg, butiksprofil, LARDOMAR och utlåtandet k_11a (som fastställer att "Namn är en/ett typord" är cirkulärt). Produkterna identifieras med id, eftersom 9887 och 9890 har samma id som äldre c-utkast. Det maskinläsbara utlåtandet finns i `vag2_skriv/k_utlatande_11d.json`.

## Sammanfattning

- 15 utkast gav **3 GODKÄND (9877, 9878, 9880), 12 RÄTTA och 0 UNDERKÄND**.
- Rättningarna lades in i en kopia av utkastet och kördes genom `skrivfil_kontroll.py` och `format_regler.py`. Resultat: 0 fel och 0 varningar. Meta ligger mellan 97 och 143 tecken, alla meta är unika, och ingen text har fler än två "enligt tillverkaren". Varje före-text förekommer exakt en gång i sitt fält, vilket kontrollerades med skript.
- **De åtta Gymstick-produkterna:** webbkällan gäller entydigt exakt modellen i alla åtta fall. Sju har samma SKU som live (61220, 61175, 61235, 61007, 63041-TU, 61126, 53135). Tunnrullen 72025-BLA är den svarta färgen på modellsidan 72025-X. Alla siffror i utkasten finns på sidorna. Engelska maxvikter (100 och 300 kg) är rätt utelämnade (R4).
- **De tio avvisningarna står sig.** En är möjligen för strikt (9889, se nedan).

## Huvudfynd

1. **Cirkulära inledningar (R11), 11 produkter.** Mönstret "Namn är en/ett typord" finns i meta och första mening på 9876, 9879, 9885, 9887, 9890, 9893, 9894, 9897, 9899 och 9900. På 9882 finns det bara i första meningen. Alla skrivs om med verb ("används för balansträning", "läggs under ryggen vid magövningar", "ersätter nätet i …"), eller med typordet först ("Tunnrullen Gymstick Aktiv är …", "Handtränaren … har …"). Skriptet hittar fortfarande inte mönstret när egennamnet står först. Det bör bli en varning (samma förslag som i k_11a).
2. **9897 bandage: tunt innehåll.** Utöver titeln hade texten bara materialet. Webbkällan anger entydigt bredd 75 mm och längd 400 cm, och de läggs till.
3. **9881:** "Vikt per vikt i …" ändras till "Varje vikt i …" (källans ordalydelse).
4. **9882:** inledningen "är ett träningspaket för funktionell träning" stryks, eftersom den är cirkulär och har marknadsföringston. Kettlebellsvikterna 4 och 8 kg läggs till.

## Punkter som koordinatorn särskilt bad om

- **9879 viktställ 400 kg (R4):** källan har "Maximal belastning: 400kg", en ren svensk rad med etikett och enhet. Löptexten anger samma värde, så det finns ingen konflikt. Uppgiften står en gång med "enligt tillverkaren", och etiketten är ordagrann. Godkänt; bara inledningen rättas.
- **9880 och 9881 viktvästar:** västens vikt (10/18 och 10/20/30 kg) och vikten per vikt är ingen lastgräns. Ingen lastgräns anges. Varianterna har olika pris, men titlarna nämner alla vikter, så R3 är uppfyllt. "Andningsbart" och "passar alla storlekar" står ordagrant i källan och har "enligt tillverkaren".
- **Hälso- och effektord:** inga finns kvar. Slitage, livslängd, återhämtning, rehab, skadeförebyggande, blodcirkulation, bantning och "högkvalitativ" är utelämnade. Läcksäker och droppsäker (9877, 9878) står med "enligt tillverkaren".
- **"Enligt tillverkaren":** högst två per text (två i 9876: ursprungsland och temperatur). 9900 har ingen efter rättningen.
- **Märket Maxxus (9876):** skrivs "Maxxus" enligt R8 (källan skriver MAXXUS). Märket finns inte i profilens `marken`. Det påverkar inte texten, men koordinatorn kan lägga till det i profilen.
- **9897 bandage, medicinteknisk produkt?** Tillverkaren placerar produkten under "Sport Supports/Recovery" och kallar materialet "medical non-wovens" och "medical grade adhesive". Utkastet gör inga skade-, stöd- eller medicinska påståenden och säger bara vad varan är, så texten är inte underkänd. **Beslut för David (frivilligt):** om bandage, tejp och stöd ska läggas under `utanfor_tills_vidare` (R6), ska 9897 tas ur skrivfilen. Annars skrivs produkten med rättningen.
- **9900 mål eller nät:** SKU 53135, live-titeln ("Goal Net") och tillverkaren ("replacement net for 183x122cm sized Court Ice Hockey Goal") säger alla nät. Bara den egna löptexten säger "mål". Utkastet följer titeln och tillverkaren och utelämnar mål-påståendena (R2). Godkänt efter rättning.
- **9899:** utkastaren skrev att webbsidan saknar SKU. Sidan anger SKU 61126, samma som live. Kundtexten påverkas inte.
- **Typord (R7):** fyra Gymstick-produkter behåller engelska typord (Ab Mat, Balance Disc, Balance Trainer, Core Twister), eftersom källan saknar svenskt ord. Bandage är en direkt översättning av Bandage Tape. Handtränare används som i 3055, Tunnrulle är live-ordet, och Målnät stöds av titeln och webbkällan.

## Avvisade (10)

Alla tio avvisningar står sig.
- **9883, 9886, 9888, 9898:** varianterna har olika pris, och titeln låser en variant eller förklarar inte varianterna (R3). 9898 Core Roller (45 cm 349 kr, 90 cm 599 kr) skulle kunna skrivas om med titeln "45 eller 90 cm", som viktvästarna, men den egna källan är bara marknadsföring. Därför står avvisningen.
- **9884, 9891, 9895, 9896:** tunn källa med skydds- och stödpåståenden, och för 9884 dessutom ett hängande redskap utan svensk lastgräns.
- **9892 Back Support:** S/M och L/XL kostar lika mycket, så avvisningen kan inte vila på R3:s prisregel. Den står ändå, eftersom källan är tunn och består av hälsopåståenden.
- **9889 Air Track (möjligen för strikt):** de tre varianterna BL, BLU och PI kostar lika mycket (2 999 kr), och titeln låser "Svart-Röd". Den kan skrivas med en titel utan färg, om gymstick.com entydigt anger mått, material och färgerna för SKU 61200. Ingen webbsökning gjordes för den. Förslag: ny utkastrunda med v1.6-faktakoll.

## Rättningar (före → efter)

Exakta före- och efter-texter finns i `vag2_skriv/k_utlatande_11d.json`. Där har varje fält en post `{fore, efter}`, och 9897 html har en samlad post för inledningen och specifikationslistan.

| nr | id | fält | ändring |
|---|---|---|---|
| 9876 | 10636646809866 | meta, html | Universalsprayen Maxxus Multi används för att smörja … / innehåller 400 ml fettfri silikonspray |
| 9879 | 10636723945738 | meta, html | Viktstället placeras liggande … / förvarar viktskivor i åtta fack … |
| 9881 | 10636758450442 | html | Vikt per vikt i → Varje vikt i (tre rader) |
| 9882 | 10636603064586 | html | Första stycket utan "är ett träningspaket för funktionell träning", med 4 och 8 kg |
| 9885 | 10581102067978 | meta, html | Ab Mat från Gymstick läggs under ryggen vid magövningar |
| 9887 | 10581102199050 | meta, html | Handtränaren Gymstick Adjustable Hand Grip har … |
| 9890 | 10581095907594 | meta, html | Tunnrullen Gymstick Aktiv är … |
| 9893 | 10581104820490 | meta, html | … används för balansträning |
| 9894 | 10581104886026 | meta, html | … används för balansträning |
| 9897 | 10581105213706 | meta, html | säljs i förpackning om två; + Bredd: 75 mm, Längd per bandage: 400 cm |
| 9899 | 10581105606922 | meta, html | … används för rotationsövningar |
| 9900 | 10581100757258 | meta, html | Målnätet Gymstick Court ersätter nätet i … (utan "enligt tillverkaren") |
