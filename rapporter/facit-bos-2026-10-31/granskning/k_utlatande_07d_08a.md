# Granskningsutlåtande k_07d och k_08a (Opus, endast läsning)

Datum: 2026-11-04. Källan hämtades på nytt via Admin API (produkter och varianter, 39 id). Inget ändrades i Shopify. Utlåtandet i maskinläsbar form finns i `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_07d_08a.json` (varje före-text finns exakt en gång i sitt fält; kontrollerat med skript).

## Sammanfattning
- **Utkast (23):** 13 GODKÄND, 10 RÄTTA, 0 UNDERKÄND.
- **Sakfel:** 9481 (stabilitetspåstående "låg tyngdpunkt" ur en maskinöversatt mening), 9486 ("hänga upp" är en tolkning), 9510 (höjdinställningen tillskrevs sits och armkudde). Övriga rättningar gäller metabeskrivningar utan verb (7 st) och en meta med utfyllnad (9477).
- **Avvisningar:** 11 av 16 är motiverade. 5 i k_08a är för strikta (se nedan).

## Punkter som skulle kontrolleras särskilt
- **9477 Shimano-glasögon:** godkänd med rättad meta. Produkten underkändes som 8031 i b_21, eftersom källan lovar skydd mot solen och god synlighet. Sedan dess har David frisläppt solglasögon i faktatextläge (standard §16). Utkastet har inga löften om skydd, UV eller synlighet, alltså samma linje som Limar 8626/8630.
- **9489 NIS-skidbindning:** inte R6. Kategorin står inte under `utanfor_tills_vidare`. En längdskidbindning har ingen utlösningsfunktion, och texten saknar säkerhetsord. Vill David behandla skidbindningar som säkerhetsprodukter behövs ett nytt beslut.
- **9478 viktväska:** live-priset är 9 kr (troligen ett prisfel). Texten påverkas inte, men frågan bör gå till David.
- **9488 Ethic-hjul:** 240 g står i produktens egen källa ("Vikt (g): 240") och 115 mm i live-titeln. Återförsäljare anger 260–289 g, men för standardversionen V2 och inte entydigt för Pro-modellen. Enligt v1.6 används webben bara när uppgiften saknas, så den egna källan gäller.
- **9483–9485 BH Fitness XTR:** användarvikten står som svensk etiketterad rad och återges en gång som "enligt tillverkaren" (R4). För 9483 är värdet detsamma i löptexten. Att rehabilitering är utelämnad är rätt och tillåtet.
- **Totalvikter k_08a:** att 70 kg utelämnas i 9518/9519 (delarna blir 68 kg trots att källan säger att stängerna ingår) och 30 kg i 9525 (skivorna blir 25 kg) är riktigt enligt R2. För 35 kg mot 35,5 kg (9520–9523) och 20 kg mot 19,5 kg (9511) är utelämnandet strikt men säkert. **9501:** 20 kg står i titeln och i löptexten. Skivorna väger 19 kg och handtagen och stången saknar vikt, så uppgiften motsägs inte och får stå. **9510:** 40 kg motsägs inte heller (stångens vikt saknas), men att utelämna det är säkert. Om "cirka" eller avrundade totalvikter ska tillåtas är en fråga för David.
- **9510 SZ-stång:** källtexten säger SZ-stång, live-titeln Z-stång. Det godtas att utkastet följer källtexten.
- **Lastgränser (R4):** alla som står med är svenska etiketterade rader ("Maximal belastning: …") och förekommer en gång. Ingen lastgräns kommer från löptext eller webb.

## Utkast
| nr | id | dom | skäl / rättning |
|---|---|---|---|
| 9477 | 10472252866826 | RÄTTA | meta: ` De väger 27,6 g och har en svart färg.` → ` De väger 27,6 g.` (utfyllnad). Inga skyddslöften; §16 gäller. |
| 9478 | 10472251064586 | GODKÄND | Ordagrant. Träningseffekter strukna. Priset 9 kr flaggas. |
| 9481 | 10468714021130 | RÄTTA | html: ` Enligt tillverkaren ger hållaren en låg tyngdpunkt.` → (tomt). Stabilitetspåstående ur en maskinöversatt mening, inte ordagrant (R2, R5). |
| 9483 | 10605381583114 | GODKÄND | 180 kg lika i löptext och rad, en gång (R4). Inte dubblett av XTB MED. |
| 9484 | 10605381615882 | GODKÄND | Ordagrant. Två "enligt tillverkaren". 130 kg från etiketterad rad. |
| 9485 | 10612594311434 | GODKÄND | Ordagrant (128 cm). Säkerhets- och åldersord strukna. |
| 9486 | 10589704618250 | RÄTTA | html: `Dig som vill hänga upp en cykel med däck upp till 3,5 tum` → `Dig som har en cykel med däck upp till 3,5 tum`. Tunn källa, kort meta godtas. |
| 9488 | 10472278327562 | GODKÄND | Egen källa gäller (R1). Webbens vikter är inte entydiga för Pro-modellen. |
| 9489 | 10475980947722 | GODKÄND | Inte R6, inga säkerhetsord, två entydiga fakta. |
| 9501 | 10480054501642 | GODKÄND | 20 kg motsägs inte. Säkerhets- och slitageord strukna. |
| 9507 | 10472296546570 | RÄTTA | meta utan verb: `Två viktskivor på cirka 5,6 kg vardera, avsedda` → `Det här är två viktskivor på cirka 5,6 kg vardera, avsedda`. Inte handhavd (det är 9506/SP 5000). |
| 9509 | 10636691013898 | GODKÄND | 120 kg från etiketterad rad. Rehab struket. |
| 9510 | 10636740231434 | RÄTTA | html: `har sits och armkudde med fem höjdinställningar` → `har sits, armkudde och fem höjdinställningar`. meta: `Bicepscurlbänk med fem höjdinställningar,` → `Bicepscurlbänken har fem höjdinställningar,`. |
| 9511 | 10636706545930 | GODKÄND | Ordagrant. 60 kg under Stång. 20 kg rätt utelämnat. |
| 9516 | 10636721717514 | GODKÄND | Ordagrant. 200 kg en gång. |
| 9517 | 10636750487818 | GODKÄND | Ordagrant. Maskinöversatta ord inte använda. |
| 9518 | 10636756320522 | RÄTTA | meta: `Skivstångspaket med curlstång på 120 cm,` → `Skivstångspaket BASIC har en curlstång på 120 cm,`. 70 kg mot 68 kg rätt utelämnat. |
| 9519 | 10636757238026 | RÄTTA | meta: `Skivstångspaket med curlstång på 120 cm och två` → `Skivstångspaket IRON har en curlstång på 120 cm och två`. |
| 9520 | 10636757369098 | RÄTTA | meta: `Curlstång IRON på 120 cm med` → `Curlstång IRON har en stång på 120 cm med`. |
| 9521 | 10636755796234 | GODKÄND | Ordagrant. Gjutjärn ur live-titeln. |
| 9522 | 10636728467722 | GODKÄND | Ordagrant. |
| 9523 | 10636728664330 | RÄTTA | meta: `Curlstång Trigrip S med stång på 120 cm,` → `Curlstång Trigrip S har en stång på 120 cm,`. |
| 9525 | 10636650938634 | RÄTTA | meta: `Curlstångspaket E Series med curlstång på 120 cm,` → `Curlstångspaket E Series har en curlstång på 120 cm,`. 30 kg rätt utelämnat. |

## Avvisningar
| nr | id | bedömning |
|---|---|---|
| 9476 | 10472242446602 | Motiverad. Bromsskiva, säkerhetskritisk cykeldel. |
| 9479, 9480 | 10472304050442, 10472304017674 | Motiverade. Dubbdäck, avklippta titlar, trasig källa. |
| 9482 | 10665225945354 | Motiverad. Dubblett av 10665225912586 (aktiv, texter-klara, kontrollerat live). |
| 9487 | 10462785896714 | Motiverad. Trasig och maskinöversatt källa (R2). |
| 9502 | 10472278163722 | Motiverad. Varianterna heter bara 30-1872/30-1873 (439/589 kr). Det går inte att se vad den andra varianten är, och titeln låser 2 x 3 kg (R3). |
| 9505 | 10480054599946 | Motiverad. Samma sak: 21-2547/21-2548 (289/489 kr), titeln låser 4 kg. |
| 9503, 9504 | 10480054567178, 10480054534410 | Motiverade. Bara reklamtext och vikten i titeln (R3, tunn källa). |
| 9506 | 10472296808714 | Motiverad. Står i handhavd_ids.txt (rad 46). |
| 9524 | 10636758286602 | Motiverad, redan skriven (facit30). Obs: live saknar taggen `texter-klara`. Koordinatorn bör avgöra om taggen ska läggas till. |
| **9508** | 10636630622474 | **För strikt.** Titeln anger hela intervallet (1,25–25 kg) och låser ingen variant. Källan har data per vikt (diameter och bredd), 31 mm, gummi 4 mm och "säljs styckvis". Utelämna "åtta olika vikter" (det finns 7 varianter, R2). |
| **9512** | 10636690718986 | **För strikt.** Intervalltitel. Källan har per vikt bredd och 45 cm diameter, 51 mm hål och "säljs en och en". |
| **9513** | 10636672631050 | **För strikt.** Intervalltitel. Par, 51 mm hål, passar 50 mm-stänger, data per vikt. |
| **9514** | 10636735283466 | **För strikt.** Intervalltitel. 51 mm i titeln och "Passar 50mm-stänger" motsäger inte varandra (samma par som i 9513). Däremot saknas hålmått i texten: skriv bara "passar 50 mm-stänger". |
| **9515** | 10636632621322 | **För strikt.** Intervalltitel (2 x 10–25 kg), källan har data per vikt. "IWF-standard" får bara stå som "enligt tillverkaren". "Proffsen använder" och slitagelöftet ska strykas. |

R3 avser titlar som pekar ut en variant. När titeln anger hela intervallet och källan beskriver alla varianter går produkten att skriva utan att låsa någon variant och utan priser. Det är samma linje som skidlängderna i 8303/8306 (varianter med olika pris, olåsta). De fem produkterna bör skrivas som utkast i en ny batch.

## Källor (webb)
- [Broadway Pro Scooters, Incube V2 12STD 115 mm](https://broadwayproscooters.com/parts/scooter-wheels/ethic-incube-v2-12-std-115mm-wheel.html)
- [Versus Pro Shop, Incube V2 12STD 115x30 mm par](https://versusproshop.com/products/ethic-dtc-incube-v2-12std-115x30mm-pair-scooter-wheels)
- [Scooter-Lab, Incube V2 115 mm svart](https://www.scooter-lab.com/scooterlab_en/ethic-dtc-wheel-12-std-incube-v2-115-mm-couleur-noir)
