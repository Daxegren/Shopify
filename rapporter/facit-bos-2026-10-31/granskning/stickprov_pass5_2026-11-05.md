# Stickprov pass 5, BEST OF SPORTS, 2026-11-05

Roll: Stickprov (Sonnet, endast läsning). Inget skrevs i Shopify. Butiken bekräftad via `verifiera_butik` (BEST OF SPORTS). Läst live via `shopify_api.py`: 40 av 40 produkter i `vag2_skriv/k_skriv_25abcf.json` (23) och `k_skriv_25de.json` (17).

## 1. Jämförelse live mot skrivfil (tecken för tecken)
- title, effektiv seo.title (null räknat som lika med title), seo.description och descriptionHtml: **0 avvikelser på 40 av 40**.
- Taggen `texter-klara` finns på alla 40. Status ACTIVE på alla 40.
- Leveranstidsmeningen ("Beställningsvaror kan ta upp till en vecka längre.") finns på ingen produkt, och ingen av de 40 har taggen "På beställning". Standardblocket är identiskt på alla 40 och lika med `b_skriv_24.json`.
- Dubbletter av meta eller SEO-titel inom de 40: inga. Meta 98-147 tecken, SEO-titel högst 43, titel högst 70.

## 2. Regelkontroller (live-texterna)
- Tre eller fler kommatecken i titel: ingen (högst två).
- Barnuppgifter: ordet "barn" förekommer inte i någon text. El-lastcyklarna 25014 (Delight) och 25036 (Vogue Avenger) nämner varken barn eller familj.
- Lås (25019, 25033, 25034, 25035): inga säkerhetsnivå- eller stöldpåståenden.
- Belysning (25009, 25010, 25023, 25051, 25052, 25056, 25059, 25060, 25061, 25072, 25073): inga lagkrav- eller synlighetspåståenden.
- Ursprungsord: inga. "Sweden" förekommer bara i märkesnamnet Cargobike of Sweden (25014).
- Märkesstavning: Axa överallt (ingen versal-AXA i texterna), Maxxus förekommer inte.
- Färger skrivs med liten bokstav i löptext (röda, rött, orange, grå); versal bara i titel och som listvärde efter "Färg:".
- "Enligt tillverkaren": högst två i brödtexten på alla. **Gränsfall:** 25024, 25025 och 25026 har två i brödtexten plus en i meta (tre om meta räknas som del av texten). 25027 har två i brödtexten och ingen i meta.

## 3. Avvikelser och fel (sorterade efter vikt)

**A. Faktafel i meta, 25022 (Curlbar Tunturi Olympic SpringCol, 10472259584266)**
- Live meta: "Curlbar av metall i krom från Tunturi, 120 cm lång med 50 mm diameter."
- Granskningen k_utlatande_25abcf rättade just detta i brödtexten: 50 mm gäller viktskivorna, inte stången (brödtexten säger nu "passar viktskivor för 50 mm"). Metan säger fortfarande "50 mm diameter" och strider mot brödtexten.

**B. Meta utan verb**
- 25072 (Giant Numen HL600): "Cykellampa Giant Numen HL600 för cykelns framsida med 600 lumen, fem ljuslägen och USB-C-laddning." Hela metan saknar verb.
- 25073 (Bookman Volume 1500), gränsfall: "Cykellampa Bookman Volume 1500 med 1500 lumen, batteri på 4000 mAh, aluminiumkropp och Garmin-fäste. GoPro-adapter ingår." Första meningen saknar verb, andra har "ingår".

**C. Genus i "ramöra" (25024, 25025, 25026, 25027)**
- Brödtexten: "Ramörat är av aluminium" (25027: "Ramörat är tillverkat i aluminium"), men "Passar för": "Dig som söker en ramöra av aluminium" (25027: "en ramöra i aluminium"). Öra är ett ord, så "en ramöra" är inkonsekvent med "Ramörat". Frågan om ramöra eller växelöra är redan öppen i utlåtandet.

**D. Singularis mot pluralis (25053 Alloy Röd, 25054 Alloy Orange)**
- "Kona Wah Wah 2 Alloy är fullstora platta pedaler i aluminium. Enligt tillverkaren är pedalen fullt servicebar." (pedaler, sedan pedalen). Samma mening i meta. Specifikationen har dessutom "Tillverkare: Kona" där övriga texter har "Märke:".

**E. 25034 (Axa Fold Lite 100)**
- "…på flaskhållaren eller, i avsaknad av detta, på en annan del av cykelramen med hjälp av speciella fästen." "detta" syftar på flaskhållaren, ett en-ord (borde vara "denna"); "speciella fästen" är vagt.
- Meta: "Vikbart lås på 100 cm med stålstänger på 5 mm." Ordet "stänger" finns inte i brödtexten eller specifikationen (där står "Material: Stål", "Tjocklek: 5 mm").
- Positivt: texten innehåller inga säkerhetsnivå- eller stöldpåståenden. "avsett för dagligt bruk" står i källan.

**F. Ordval**
- 25058 (Axact 9W Vit): "sträckdistans" (brödtext, passar för, spec och meta) är dubblerat ord; "sträcka" eller "distans" räcker.
- 25057 (Look Geo Trekking Grip) meta: "Andra sidan är platt." Artikel saknas ("Den andra sidan"). Brödtexten är en enda mening.
- Axact-serien använder tre termer för samma funktion: "automatisk skanning" (25048), "scanning" (25049), "Auto SCAN" (25058).
- 25047 (Giant Original MTB Sport): "Vikten är 385 g." utan att ange per pedal eller per par.
- 25060/25061 skriver "Driftstid", 25072 skriver "Drifttid".
- 25073 (Bookman): "Dig som vill kunna bära extra batterier" och "extra batterier kan bäras med" är oklara (källan: "möjlighet att bära extra batterier").
- 25036 (Vogue Avenger): "Sittdynor ingår." / "Sittdynor: Ingår" utan förklaring; källan nämner "familjeanvändning". Texten nämner inget om barn.

**G. Påståenden i meta utan "enligt tillverkaren" där brödtexten har det**
- 25027 meta: "Ramöra i aluminium för olika modeller från bland annat Haibike, Hercules, Staiger, Wheeler och Winora." (passformspåstående utan attribution; brödtexten har det och listar 15 märken).
- 25062 meta: "Setet är avsett för hemmaträning, till exempel marklyft och knäböj."
- 25065 meta: "Stången används till bicepscurls, triceps extensions och axelövningar."
- 25067 meta: "…mjuk yta för box jumps och step-ups."
- Brödtexten attribuerar i alla fyra fall. Ingen regelbrytande träningseffekt, men skiljer sig från hur t.ex. 25031 och 25053 gör.

**H. Kontroll av källa mot text (stickprov)**
- 25066 (Gymstick Vinyl): brödtexten säger "med vinylyta", specifikationen "Material: HDPE, cement, sand, järnmalm" (vinyl nämns inte i materialraden). Källan säger "slitstark vinylyta" (utelämnat i texten, rätt).
- 25022: "utformad för att träna triceps" står i källan ("utformad för att träna triceps snabbt och enkelt") och är attribuerat.

## 4. Inga fynd (kontrollerat)
- "gjort/gjord": en träff, 25002 "är gjord av metall" (korrekt).
- Stavfel och mojibake: inga funna. Dubbla mellanslag: inga.
- Cargobike Delight 25014: lastkapacitet och bromsar står "enligt tillverkaren" (två); inga barnuppgifter.

## 5. Begränsningar
- Jämförelsen gäller title, seo.title, seo.description, descriptionHtml, tags och status. Bilder, varianter, pris, metafält och kollektioner lästes inte.
- Språkgranskningen är en manuell läsning av en modell, stödd av enkla mönsterkontroller (regex). Den är inte en stavningskontroll med ordlista.
- Källjämförelse mot ursprungstexten gjordes bara som stickprov (25014, 25022, 25034, 25036, 25066, 25073). Övriga produkters fakta kontrollerades inte mot källa eller webben.
- "Mer än två enligt tillverkaren" räknades både i brödtext och brödtext plus meta; vilken tolkning som gäller avgör regelboken (R5 säger "per text").
- "På beställning" bedömdes enbart via taggar; ingen leveransdata lästes.
- Jag har inte rättat något. Alla fynd är rapporterade, inte åtgärdade, och inget fynd är registrerat i beslutsloggen.
