# Granskningsutlåtande k_08e (viktprodukter) och k_09a (Christopeit fitness)

Granskare: Opus. Endast läsning, inga ändringar i Shopify. Datum 2026-11-04. 51 produkter (36 utkast och 15 avvisade) hämtades live via Admin API, med varianter och priser via GraphQL. Dessutom lästes 12 redan skrivna dubblettreferenser live. Underlag: regelbok v1.6, beslutslogg, butiksprofil, LARDOMAR och k_08bcd. Maskinläsbart utlåtande: `vag2_skriv/k_utlatande_08e_09a.json`.

## Sammanfattning

- 36 utkast gav **32 GODKÄND, 4 RÄTTA och 0 UNDERKÄND**. Rättningarna lades in i kopior av utkastfilerna och kördes genom `skrivfil_kontroll.py`. Resultat: 0 fel och 0 varningar i båda filerna.
- **Meta:** alla 36 metabeskrivningar har verb, och ingen inledning är cirkulär. Undantaget är 9623 i k_08e, där metan särskriver "Pull-up baren". Den rättas.
- **Diametrar (30/31 och 50/51 mm):** alla stämmer med källan. Där källan saknar stångdiameter (9602, 9606, 9607) har utkastet utelämnat den.
- **Totalvikter mot delarnas summa:** alla stämmer (9601, 9602, 9605, 9606, 9607, 9619 och SP 5000 med 12 x 5 = 60 kg).
- **Prisvarianter:** 9604 har sju vikter och 9608 tre färger. Titlarna anger inget enskilt alternativ och texten gäller för alla varianter. Båda godkänns.
- **Lastgränser (R4):** alla som står kvar är svenska etiketterade rader med enhet, och var och en står "enligt tillverkaren" en gång. Följande är rätt utelämnade: "driftvikt" och löptext utan etikett (9623 k_08e), "Maximal viktkapacitet" (9619 k_09a) och "Belastning: 5/8 kg" (9609 och 9623 k_09a).
- **Golvmattor (9608, 9613, 9614 i k_09a):** varje produkts egen källa säger "Golvmatta", så typordet följer godkanda_typord. Skyddsordet står ordagrant i källan och återges en gång "enligt tillverkaren".
- **Elektronik- och hälsoord:** "ledvänlig", träningseffekter, "halkfri", "robust" och liknande är strukna överallt.
- **Märkning (nr):** k_08e och k_09a använder samma nr för olika produkter (9608, 9610–9619, 9623, 9625). Skript som slår upp på nr kan blanda ihop produkterna. Använd id eller fil+nr när skrivfilen byggs.

## Rättningar (före → efter)

| Fil | Nr | Fält | Före | Efter | Skäl |
|---|---|---|---|---|---|
| k_08e | 9623 | meta | `Pull-up baren fästs` | `Hammer Multigrip Pull-up Bar fästs` | Särskrivning. Typordet Pull-Up Bar är annars rätt: det står i källan och används i butiken |
| k_08e | 9625 | titel | `Hantel Tunturi Rapid Justerbar` | `Hantel Tunturi Rapid Justerbar, 20 kg` | Se nedan |
| k_08e | 9625 | seo_title | `Hantel Tunturi Rapid Justerbar` | `Hantel Tunturi Rapid Justerbar 20 kg` | Se nedan |
| k_08e | 9625 | html | `<li>Material: Järn</li>` | `<li>Totalvikt: 20 kg</li>` + `<li>Material: Järn</li>` | Se nedan |
| k_09a | 9617 | html | `Motor: 1 HP` | `Motor: 1 hk` | Svensk enhet med liten bokstav (R9). Samma linje som "5,0 hk" (TR800) och "1,2 hk" (9615) |
| k_09a | 9622 | html | `Räckvidd: 1 m (enligt tillverkaren)` | `Räckvidd: 1 m` | Räckvidden stod två gånger med "enligt tillverkaren" (R5: en gång per påstående) |

**9625 Tunturi Rapid (20 kg):** utkastaren strök 20 kg i onödan. Uppgiften står i produktens egen live-titel och motsägs inte, eftersom källan inte anger handtagets vikt (jämför 9532 i k_08bcd). Webbkontrollen enligt R1 v1.6 stöder den. Tunturis egna sidor för set som bygger på 14TUSCL464 anger handtaget till 4 kg och två skruvar till 1 kg vardera:
- https://www.tunturi.com/en/go/product/159135978
- https://www.tunturi.com/en/go/product/159135977
- https://www.tunturi.com/en/go/product/159135973

Det ger 4 + 2 + 2 + 12 = 20 kg. Decathlon listar exakt 14TUSCL464 som 20 kg (4–20 kg): https://www.decathlon.ie/p/1100158998-758974-rapid-adjustable-dumbbell-single-set-20kg-adjustable-4-20kg-9-in-one.html. Skriv in adresserna i `att_bekrafta`. Taggen "På beställning" finns, och leveranstidsmeningen ingår.

## Punkter som koordinatorn särskilt bad om

- **9623 (k_08e):** typbytet från Hantelstång till Pull-Up Bar är motiverat (R7). Ordet står i källtexten, och den aktiva produkten "Pull-Up Bar Tunturi Door-Way Chinning Bar" använder det. Det var rätt att utelämna lastgränsen (150 kg i löptext och "Maximal driftvikt").
- **9617 (k_09a):** "1 HP" rättas till "1 hk".
- **9622 (k_09a):** räckvidden 1 m får stå. Den är en entydig del av en annars trasig rad (R2).
- **9610/9612/9619 (k_09a):** utelämnandena är motiverade. Det gäller programantal som motsäger varandra (12 mot 23 respektive 21 mot 12 + 5), den trasiga etiketten "Bruksanvisning: 12 kg" och "viktkapacitet" utan angivet objekt. **9610/9612/9619 (k_08e):** inga viktiga uppgifter saknas. 9610 utelämnar märket Gorilla Sports, vilket är försiktigt och godtagbart.
- **9618 (k_08e):** SKU:n är GYM61068-1 medan handtaget (adressdelen) slutar på -3. Det motsäger inte titeln (3 kg) entydigt. Godkänd, men värd en kontroll vid stickprovet.

## Avvisade produkter

| Fil | Nr | Avvisningen | Bedömning |
|---|---|---|---|
| k_08e | 9603 | Redan skriven (Trigrip 51 mm 6 x 5 kg) | **Formellt rätt, men produkten bör skrivas om.** Live har vår text med en kvarlämnad sektion "Vanliga frågor" efter standardblocket (strider mot R15) och saknar taggen texter-klara. Skriv om den i en senare batch med originalet i `rapporter/shopify-original-2026-10-31/facit30-original.json` som källa (samma linje som 9570 i k_08bcd): ta bort FAQ-sektionen och sätt taggen sist |
| k_08e | 9609 | Dubblett av 10636691013898 (ankelband 34 cm) | Motiverad i sak: samma modell, färg och data. **Notera:** olika SKU (…-0001 mot …-0137) och olika pris (449 mot 949 kr). Den skrivna produkten säger "säljs i par", vilket kan betyda att 9609 är ett enstaka band. Fråga till David, se nedan |
| k_08e | 9617 | Tunn källa (Gymstick-hantel, tom beskrivning) | Motiverad |
| k_08e | 9620, 9621 | Tunn källa (kettlebellrack och hantelrack) | Motiverad. Källan innehåller bara marknadsföring och kvalitetsord |
| k_08e | 9622 | R3: titeln säger 1,25 kg men produkten har sju varianter (89–1 329 kr) | **Motiverad men strikt.** R3 kräver avvisning ordagrant. Dessutom ger källan utöver titeln bara märket och "gummerade", så den vore tunn även med en intervalltitel. Den kan skrivas senare som "Viktskivor Gymstick Gummi, 1,25–25 kg", på samma sätt som 9604, om en webbkälla för exakt RWP-serien ger minst håldiameter eller material |
| k_08e | 9624 | Dubblett (Platinum Hex 37,5 kg) | Motiverad. Den skrivna 10656688275722 och den oskrivna 10656688341258 har samma SKU (25TUPLA033) |
| k_08f | 9626 | Tunn källa (Zipro HEX 2,5 kg) | Motiverad |
| k_09a | 9601, 9603–9607 | Dubbletter av skrivna 10164, 10166, 10009, 10010, 10011 och 10381 | Motiverade. Samma SKU (EC1000R19, ERV1000LED, TR800RLED, G6515B, G6515BTFT, G340) och samma data. Alla referenser är aktiva och har taggen texter-klara |
| k_09a | 9602 | Movemia ER1000R: titeln säger elliptisk, texten säger roddmaskin | **Motiverad, och typfrågan kan i stort sett besvaras.** Måtten 225 x 62 x 161 cm och steglängden 46 cm passar inte en roddmaskin. Webbkällor beskriver ER1000R som en elliptisk tränare (crosstrainer): Kübler Sport (https://www.kuebler-sport.com/bh-fitness-movemia-elliptical-trainer-er100r-vg-003756.html) anger 46 cm, 225 x 62 x 161 cm och 190 kg. Ordet "roddmaskin" i källan är alltså fel (R2). Webbkällorna motsäger dock produktvikten (139 mot 125 kg) och svänghjulets placering (fram eller bak), och ingen tillverkarsida hittades. Butiken har tre listningar med samma SKU ER1000R19: 10656691257610, 10656691290378 och 10656691323146 |

## Frågor till David (påverkar inte domarna)

1. **ER1000R (tre listningar med samma SKU):** vilken listning ska behållas? Rekommendation: skriv den som "Crosstrainer BH Fitness Movemia ER1000R" med bara de uppgifter som stämmer överens (19-tums pekskärm, 25 nivåer, EMS/induktion, steglängd 46 cm, mått, 190 kg). Utelämna "roddmaskin", produktvikten och svänghjulets placering. Behandla de andra två som dubbletter.
2. **9609 och den skrivna 10636691013898 (ankelband):** är det samma produkt, eller är den ena ett par och den andra ett enstaka band? SKU och pris skiljer sig. Om det är olika säljenheter är 9609 inte en dubblett.
3. **9603:** ska omskrivningen med borttagen FAQ-sektion ingå i nästa viktbatch?
