# Granskningsutlåtande k_10a och k_10b (yoga, mattor, band, parallettes, småutrustning)

Granskare: Opus. Endast läsning, inga ändringar i Shopify. Datum 2026-11-04. 50 produkter (48 utkast och 2 avvisade) hämtades live via Admin API, med varianter och priser via GraphQL. Underlag: regelbok v1.6, beslutslogg, butiksprofil, LARDOMAR och facit30-originalet (`rapporter/shopify-original-2026-10-31/facit30-original.json`) för de två avvisade. Maskinläsbart utlåtande: `vag2_skriv/k_utlatande_10.json`. Där har varje post fälten nr, id och fil, eftersom nr-serien kan krocka med andra batcher.

## Sammanfattning

- 48 utkast gav **30 GODKÄND, 18 RÄTTA och 0 UNDERKÄND**. Rättningarna lades in i kopior av utkasten och kördes genom `skrivfil_kontroll.py`. Resultat: 0 fel och 0 varningar i båda filerna. Alla meta ligger mellan 107 och 150 tecken.
- **Meta utan verb (R11):** 14 metabeskrivningar började med en nominalfras utan verb, till exempel "Gymmatta på …" och "Paket med fem …". Det gäller 9726–9730, 9739–9743, 9746 och 9749. Skriptet hittar inte felet. Det bör bli ett test, till exempel som en varning när meta börjar med "Paket med", "Set med" eller "Två".
- **Cirkulär inledning (R11):** "Speed Rope är ett hopprep" (9734) och "Women's Health Speed Rope är ett hopprep" (9735) rättas. Skriptets test missar mönstret eftersom orden skiljer sig.
- **Prisvarianter:** 9702, 9707–9710, 9712, 9721, 9738, 9739, 9745, 9748 och 9750 har flera varianter. Ingen titel låser en variant, och varje påstående gäller alla varianter. Mått och längd anges per variant där de skiljer sig (300/500 cm, 120/200 cm, 55/65/75 cm).
- **Lastgränser (R4), full genomgång:** 9701 (180 kg), 9703 (300), 9706 (200), 9708/9709 (220), 9710 (100), 9711 (120), 9719 (chinsräcke 120), 9721 (500), 9730 (stativ 20), 9748 (100 per parallette), 9749 (150) och 9750 (2 x 100). Alla är svenska etiketterade rader med enhet och står en gång "enligt tillverkaren" i texten. Lastuppgifter i löptext utan etikett återges inte. Motstånd i kg på gummiband (9722, 9724, 9725, 9739, 9746) behandlas rätt som motstånd och inte som lastgräns.
- **Hälso-, effekt-, rehab- och halkord:** strukna överallt där de saknar ordagrant stöd. Halkfri, halksäker, skyddar golvet, slitstarkt, "aktiverar armar och bål" och ekologiskt ursprung står ordagrant i källan och står en gång med "enligt tillverkaren". 9744 och 9745 hade "enligt tillverkaren" två gånger för samma påstående. Det rättas.

## Rättningar (före → efter)

| Fil | Nr | Fält | Före | Efter |
|---|---|---|---|---|
| k_10a | 9704 | titel | `Ryggsträckare, Fem Nivåer` | `Ryggsträckare, Fem Stapelbara Delar` |
| k_10a | 9704 | seo_title | `Ryggsträckare, Fem Nivåer` | `Ryggsträckare, Fem Delar` |
| k_10a | 9704 | html | `Höjden kan ändras i fem nivåer.` / `Dig som vill kunna ändra höjden i fem nivåer` / `Höjd: Justerbar i fem nivåer` | `Höjden justeras genom att delarna staplas.` / `Dig som vill kunna justera höjden genom att stapla delarna` / `Höjd: Justerbar genom att delarna staplas` |
| k_10b | 9726 | meta | `Gymmatta på 101 x 60 x 1 cm med räfflad yta` | `Gymmattan på 101 x 60 x 1 cm har räfflad yta` |
| k_10b | 9727 / 9728 | meta | `Gymmatta i PVC på 120 (180) x 60 x 0,6 cm som väger` | `Gymmattan i PVC mäter 120 (180) x 60 x 0,6 cm och väger` |
| k_10b | 9729 | meta | `Två gymmattor på` | `Paret består av två gymmattor på` |
| k_10b | 9730 | meta | `Set med två gymmattor` | `Setet består av två gymmattor` |
| k_10b | 9739 | meta | `Paket med fem latexband` | `Paketet innehåller fem latexband` |
| k_10b | 9740–9743 | meta | `Paket med fem/tre/tre/tio medicinbollar` | `Paketet innehåller fem/tre/tre/tio medicinbollar` |
| k_10b | 9746 | meta | `Paket med fem miniband` | `Paketet innehåller fem miniband` |
| k_10b | 9746 | titel, seo_title, html | `Miniband Trym` / `Märke: Trym` | `Miniband TRYM` / `Märke: TRYM` |
| k_10b | 9748 | meta | `Höga parallettes som säljs parvis, har` | `Dessa höga parallettes säljs parvis, har` |
| k_10b | 9749 | meta | `Parallettes med två hängande handtag av svart pulverlackat stål.` | `Den sammansatta varianten av parallettes har två hängande handtag och är gjord av svart pulverlackat stål.` |
| k_10b | 9734 | meta, html | `Speed Rope är ett hopprep med 300 cm långt rep` | `Hopprepet Speed Rope har 300 cm långt rep` |
| k_10b | 9735 | meta, html | `Women's Health Speed Rope är ett hopprep med vikthandtag,` | `Hopprepet Women's Health Speed Rope har vikthandtag,` |
| k_10b | 9744 / 9745 | html | `Speltskal, ekologiska och från Österrike (enligt tillverkaren)` | `Speltskal, ekologiska och från Österrike` (påståendet står redan med "enligt tillverkaren" i löptexten) |
| k_10b | 9744 / 9745 | html | Färglistan med versaler (`Svart, Röd, Lila …`) | Gemener efter första ordet, "och" före sista färgen |
| k_10b | 9744 / 9745 | meta | `Meditationskudde (Half Moon) Zafu har` | `Meditationskudden (Half Moon) Zafu har` |

Den exakta före-texten per fält finns i JSON-filen. Varje före-text förekommer exakt en gång i sitt fält, vilket kontrollerades med skript.

## Punkter som koordinatorn särskilt bad om

- **9703 Stretchplatta:** typbytet är motiverat, eftersom källtexten säger "stretchplatta" tre gånger. "Trä" ur live-titeln stryks med rätta: källan anger PVC-yta och EVA-undersida. **9705 Hopprep:** källan säger "detta hopprep", och Speed Rope blir modellnamn. **9706 Maghjul:** källan säger "maghjulet", och live-titeln "Ab Wheel Träningshjul" är blandspråk. **9715 Bollstativ:** ordet behålls från live-titeln, och källans "bollhållare" står i parentes. Alla fyra typbyten är i linje med R7.
- **9704 Ryggkudde:** källan säger både "Fem nivåer" och "tre justerbara höjder". Enligt R2 utelämnas därför nivåantalet. Det entydiga "fem stapelbara delar" står kvar.
- **9728 (120 x 60 mot 180 x 60):** 180 x 60 x 0,6 cm är rätt. Live-titeln, live-SEO, den etiketterade måttraden, vikten (2,9 kg mot 1,9 kg på 9727), SKU-numret (-0002) och det högre priset (559 mot 479 kr) stämmer alla med 180 cm. Första meningen är kopierad från 9727.
- **9731 Hip Glute Band:** tre band är entydigt. Källan har tre färger med var sin styrka och var sin omkrets (76 cm), "banden" står i plural och titeln säger PAKET. Produkten är ingen dubblett av 9737 (Women's Health, SKU 4407, 299 kr). SEO-titlarna liknar varandra ("Höftband Hip Glute Band i Tyg" mot "Höftband Hip Glute Band, Set med 3 Band") men är unika.
- **Utelämnade uppgifter, som alla godtas:** 9736 utelämnar färgen ("snyggt rosa" mot "Grå/Magenta"). Det är försiktigt, och färgen kan läggas till om David vill. 9738 anger inte tjocklek per färg, eftersom tabellen säger Turkos och varianterna Blå; spannet 0,25–0,65 mm stämmer. 9746 utelämnar styrkeetiketterna (Gul = Heavy 4,5 kg står före Blå = Medium 6,8 kg) och rehab. Andra utelämnanden som godtas: vikten på 9706 och 9748 (oklart vad den gäller), måtten på 9713 (motsägelse) och diametern på 9750.
- **TRYM eller Trym (R8):** 9702 och 9705 skriver TRYM, 9746 skrev Trym. Tre redan skrivna produkter med taggen texter-klara heter "… TRYM" live (Latsdragstång 118/140 cm och Kabelhandtag V-Grepp). Jag har därför harmoniserat 9746 till TRYM. R8 säger dock "aldrig versaler", så David behöver besluta. Väljer han Trym ska 9702, 9705 och 9746 samt de tre skrivna produkterna ändras.

## Avvisade (k_10b_avvisade.json)

- **9737 (Höftband Women's Health) och 9747 (Miniband Latex):** båda avvisningarna godtas. Ingen av dem ska skrivas om. Live-texterna jämfördes med facit30-originalet, och sakuppgifterna stämmer. Det gäller 76 cm, 8 cm, 65/35 % och tre nivåer på 9737, och 4,5/6,8/9/13,5/18 kg, 60 cm och 5 cm på 9747. En omskrivning saknar ny källa (R3).
- **9747 har kvar avsnittet "Vanliga frågor" efter standardblocket.** Det bryter mot R15 och mot skriptets FORBJUDET. Koordinatorn bör ta bort det avsnittet och ingenting annat, sätta texter-klara efter återläsning och logga ändringen.
- **9737 saknar bara taggen.** Den kan få texter-klara efter återläsning. Raden "Gummerad insida för bättre grepp" saknar "enligt tillverkaren". Texten är godkänd av David i facit-30 och rörs inte utan hans beslut.
