# Skrivrapport: rättningar våg 2a (BEST OF SPORTS, 2026-11-02)

Butik verifierad med get-shop-info: BEST OF SPORTS, bestofsports.se, SEK. Skrivning med `productUpdate(product:)`, seo alltid med title och description. Status ACTIVE kontrollerades live före varje skrivning (alla ACTIVE). Handle och status ändrades aldrig. Före-läge: `rapporter/shopify-original-2026-11-02/vag2a_ratt_fore.json`. Kanarie: 2209, återläst, därefter övriga. Sanningen för texterna är `vag2_skriv/a_skriv.json`, som är uppdaterad så att den stämmer med live.

## Ändrat (före/efter)
| nr | Fält | Före | Efter |
|---|---|---|---|
| 2209 | html | Tunturi Allround Boxing Gloves är boxningshandskar i konstläder, 16 oz. ... | Tunturi Allround är boxningshandskar i konstläder, 16 oz. ... |
| 2209 | meta (142 → 137) | Tunturi Allround Boxing Gloves är boxningshandskar i konstläder, 16 oz. De har ... | Tunturi Allround är boxningshandskar i konstläder i storlek 16 oz. De har mjuk stoppning och en bred kardborre som ger stöd åt handleden. (Storlek 16 oz står i specifikationen och titeln: entydigt.) |
| 2213 | titel | Gymtalk Trec Liquid Chalk, Flytande, 250 ml | Gymtalk Trec Liquid Chalk, 250 ml |
| 2213 | seo.title | Gymtalk Trec Liquid Chalk, 250 ml | samma (lagras nu som null, eftersom den är lika med titeln; avsett beteende) |
| 2213 | html | ett flytande gymtalk. Talket torkar | en flytande gymtalk. Talken torkar |
| 2213 | meta (134 → 133) | ... ett flytande gymtalk ... Talket ... Det passar | ... en flytande gymtalk ... Talken ... Den passar för styrketräning. |
| 2210 | meta (150 → 153) | Tunturi fristående boxningssäck i svart PVC, 69 x 69 x 170 cm och 9,6 kg. Basen fylls med sand. Säcken passar både nybörjare och avancerade användare. | Tunturi fristående boxningssäck i svart PVC väger 9,6 kg och mäter 69 x 69 x 170 cm. Basen fylls med sand. Den passar nybörjare och avancerade användare. (Verifieringsrapportens förslag hade "är i svart PVC", vilket låter fel; "väger/mäter" ger verb och stämmer med html och specifikation.) |
| 2108 | meta (150 → 155) | ... i en förpackning som är lätt att dosera. ... | ... i en förpackning som gör den lätt att dosera. Enligt tillverkaren torkar den snabbt och absorberar fukt. |
| 2104 | html | Passar för hade två punkter; den andra: "Dig som vill ha en boll att använda hemma, på jobbet eller utomhus" | Punkten borttagen. Frasen står kvar en gång, i inledningen (där den har förbehållet "enligt tillverkaren"). Meta och SEO oförändrade. |
| 2410 | titel | Reservfjädrar Tunturi Indiaka | Reservfjädrar Tunturi Indiaca |
| 2410 | html | Tunturi Indiaka reservfjädrar ... | Tunturi Indiaca reservfjädrar ... |
| 2410 | seo | title null (= titeln), description null | title = titeln (lagras null), description null. Meta fanns inte och skrevs inte. |

Beslut redovisade:
- **2213 titel:** "Flytande" upprepar "Liquid". Jag förenklade titeln (systerprodukten 2108 har redan formen "Gymtalk Trec Liquid Chalk, 100 ml"). "Gymtalk" behålls som produktord. Specifikationen "Typ: Flytande talk" behölls. Titeln är unik.
- **2109:** meta och html innehåller inte formuleringen om förpackning/dosering. Ingen ändring. (Meningen "och passar för styrketräning" är grammatiskt godtagbar.)
- **2204 Grean:** källorna är entydiga. Leverantörstexten skriver "Spokey GREAN" (versaler som modellnamn), och återförsäljare (fitnessmarket.ee, sportisimo, morele.net, gemini.pl) skriver GREAN/Grean. Ingen splittring, ingen alternativ stavning. Befintlig stavning "Grean" i titel, SEO och text är konsekvent och behålls. Ingen skrivning.
- **2410 Indiaca:** originaltitelns "Indiaka" följde tillverkarens artikelnummer/handle. Källtexten och produkt 401 skriver "Indiaca". Handle `...indiaka...` ändrades inte (instruktion).

## Taggar (tagsRemove, status ACTIVE kontrollerad)
Sökt: alla produkter i våg 2a (32) och våg 1/1b (88 id ur vag1_skriv/*.json), live-läsning av tags. Bort tagit bara uppenbart fel för produkttypen. Före och efter finns i före-filen och i mutationssvaret.
| id | nr/produkt | Borttaget | Tags efter |
|---|---|---|---|
| 10588446523658 | 2508 handske dam | Damcykel | Konditionsträning & Fitness, Trec, Velomarket |
| 10588446687498 | 2511 handske dam | Damcykel | samma |
| 10472267645194 | 2211 handske dam | Damcykel | samma |
| 10472259813642 | 2210 boxningssäck | Cykelväska | Boxning, boxningssäck, Boxningsutrustning, Fell, Gymstick, På beställning, Tunturi, Velomarket |
| 10472283898122 | 2309 stretchband | Cykelbelysning | Fell, gummiband, På beställning, Stretchband, Tunturi, Velomarket |
| 10470927433994 | Stretchband Tubing Set (våg 1) | Cykelbelysning | Stretchband, Tunturi, Velomarket |
| 10470947324170 | Stretchband Power Band Extra Light (våg 1) | Cykelbelysning | gummiband, Stretchband, Tunturi, Velomarket |
| 10588446851338 | Massagerulle Yoga Grid ljusblå (våg 1) | Cykelbelysning | Konditionsträning & Fitness, Massage, Tunturi, Velomarket, Yoga |
| 10472505868554 | Yogamatta 8 mm ljusblå (våg 1) | Cykelbelysning | Fell, Tunturi, Velomarket, Yoga, yogamatta, Yogamattor |
| 10472213250314 | Viktväska Strengthbag (våg 1) | Cykelväska, Cykelväskor | Fell, Tunturi, Velomarket |
| 10462758469898 | Boxningsdocka Slam Man (våg 1) | Herrcykel | Boxing equipment, Boxning, Fell, Tunturi, Velomarket |

Cykellås: ingen produkt i våg 1/2a hade felaktig Cykellås (10475621089546 är ett riktigt cykellås).

Osäkra, ändrades inte:
- **Fell** (på ca 40 Tunturi-produkter i vågorna): troligen leverantörens produktlinje/etikett, betydelsen okänd.
- **Gymstick** på 2210 (Tunturi boxningssäck) och Minicykel Tunturi (10472277606666): kan vara leverantörens koncerntillhörighet.
- **Pump** på Lyftstångsset Tunturi Pro Aerobic Pump Set (10471042646282): produkttypen "pump" (kroppspump) kan vara avsedd.
- **Vikbar cykel** på Minicykel Tunturi Mini Bike Foldable Easy: möjligen avsett (vikbar minicykel).
- **Pedals** på Pedaler Tunturi Reha för motionscykel: stämmer.
- Fler taggfel finns troligen utanför våg 1/2a (till exempel Cykelväska på boxningssäckar, viktväskor och Tunturi Bulgarian Bag, samt Damcykel på rullskridskor, multivitaminer och damhandskar). Dessa ingick inte i uppdraget och rördes inte. Rullskridskorna är säkerhetsprodukter.
- Obs: tagg-rensningen kan skrivas över av Velomarket-synken. Kontrollfråga efter nattsynken.

## 2201 (Rullskridskor FILA Houdini Pro, id 10471232602378): bara undersökt, inget skrivet
Live: ACTIVE, handle `rullskridskor-fila-houdini-pro-svart-vit-010620078-39`, option "Variant" med sju varianter:
| Variant | SKU | Pris | Lager |
|---|---|---|---|
| Default Title | 010620078-44 | 3 519 | 1 |
| 40 / black | 010620078-40 | 3 519 | 1 |
| 40.5 / black | 010620078-40-5 | 3 519 | 1 |
| 41 / black | 010620078-41 | 3 519 | 1 |
| 42.5 / black | 010620078-42-5 | 3 519 | 1 |
| 43 / black | 010620078-43 | 3 519 | 1 |
| 44 / black | 010620078-44 | **3 059** | 1 |
Fynd: (1) varianten "Default Title" har samma SKU (-44) som "44 / black", så den är troligen en kvarleva från produktskapandet (en extra variant utan egen storlek); (2) storlek 44 kostar 3 059 kr medan alla andra storlekar kostar 3 519 kr, och spannet visas som 3 059–3 519 kr; (3) båda varianterna med SKU -44 har lager 1, så lagret för 44 kan vara dubbelräknat. Mina antaganden: leverantörens pris för 44 kan vara ett kampanj-/utförsäljningspris, eller felet ligger i synken. Detta är inte fastställt. Ändra inget utan Davids beslut och leverantörens prislista; kontrollera också om "Default Title" ska tas bort av Velomarket-synken. Priser, varianter och produkten rördes inte.

## Punkt 8: storleksformat i handsktitlarna (endast rapport)
| nr | Titel | SEO-titel |
|---|---|---|
| 2106 | ..., Gul, XL | utan storlek och färg |
| 2107 | ..., Röd, XL | ..., Röd (ingen storlek) |
| 2212 | ..., Svart, XL | "Trec Gel Shock, Svart, XL" (saknar #02) |
| 2211 | ..., Grå, XS | "Trec #24, Dam, XS" (komma före Dam, "för" saknas) |
| 2508 | ..., Grå, Storlek S | utan storlek |
| 2511 | ..., Vit, Storlek XS | utan storlek |
| 2509 | ..., Svart, Storlek L | "Gel Shock Svart L" (inga kommatecken) |
Skillnaden: "Storlek S/XS/L" (2508, 2511, 2509) mot bara "XL"/"XS" (2106, 2107, 2212, 2211). Inget ändrat.

## Kontroll
- **Maskinellt:** `kontrollera_produkttext.py --seo-title-max 43 --seo-suffix " – BEST OF SPORTS"` på kopia (html till beskrivning, standardblock inom [[STANDARDBLOCK]]…[[/STANDARDBLOCK]], fakta = originaltitel + original-html ur `vag2a_fore.json`), 32 produkter från den uppdaterade `a_skriv.json`: **0 FEL, 49 varningar** (struktur: avsnittet "Passar dig som"/specifikationer saknas; beskrivning_langd på tunna källor, bland annat 2108 37 ord, 2213 30 ord, 2410 12 ord). Samma 49 som före rättningen enligt verifieringsrapporten. Titlar unika, längsta titel 58, längsta SEO-titel 43, SEO-titlar unika. Metalängder 2209 137, 2213 133, 2210 153, 2108 155.
- **Återläsning efter skrivning (för hand):** alla fält (title, handle, status, tags, seo.title, seo.description, descriptionHtml) lästes tillbaka för 2209, 2213, 2210, 2108, 2104, 2410 och jämfördes med avsett värde: inga avvikelser. Handle och status oförändrade. seo.title är null för 2213 och 2410 (lika med titeln). 2204 och 2109 lästes (oförändrade). Radbrytningen mellan `<li>` bevarades. Taggar lästes tillbaka i svaret från tagsRemove (inga userErrors).
- **Begränsning:** jämförelsen är gjord för hand (MCP-svar kan inte diffas i bash). Före-filens descriptionHtml är hämtad från `a_skriv.json`, som verifieringen 2026-11-02 visade identisk med live; live-texten lästes också på nytt före skrivning för de sex produkterna och stämde. För tagg-produkterna i före-filen sparades inte descriptionHtml (rördes inte). Texterna är inte granskade av en oberoende språkgranskare; det bör göras enligt lärdomen 2026-11-01. Titlar bör läsas tillbaka efter nattsynken (lärdomen 2026-10-30).
