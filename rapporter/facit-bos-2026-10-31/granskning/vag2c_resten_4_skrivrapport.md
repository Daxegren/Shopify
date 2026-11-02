# Våg 2c resten 4 (Gymstick, 41 produkter) – skrivrapport 2026-11-02

Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info före skrivning. Skrivfil: `vag2_skriv/c_skriv_resten_4.json` (41 produkter, 41 unika id). Före-läge: `rapporter/shopify-original-2026-11-02/vag2c_resten_4_fore.json`, sparat före skrivning (läst live i två grupper, 25 + 16).

## Före och hoppade över
Alla 41 var ACTIVE, ingen hade taggen "texter-klara", och ingen hade en titel lika med skrivfilens. Inga hoppades över. SEO-titel och SEO-beskrivning var tomma (null) på alla 41. Beskrivningarna var leverantörens marknadsföringstext (till exempel "din ultimata följeslagare", "oumbärlig"). Titlarna var leverantörens engelska eller blandade namn (till exempel "Triceps Rope", "Vivid Träningsmatta 170 x 60 x 0,4cm, Rosa-Grå").

## Kontrollskriptet
Körd på en kopia (html mappad till beskrivning, standardblocket omgivet av `[[STANDARDBLOCK]]…[[/STANDARDBLOCK]]`, källtext i fältet `fakta` = före-läget, `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS"`). Kopian och byggskriptet ligger i scratchpad, inte i repot.
Resultat: 41 produkter, 0 FEL, 52 VARNINGAR:
- 41 × "saknar avsnittet 'passar dig som'": texterna använder rubriken "Passar för", i enlighet med skrivfilen (känd och godtagen).
- 8 × beskrivningen kortare än 40 ord (30–38 ord): produkterna 3241, 3250, 3259, 3261, 3269, 3274, 3290, 3291. Tunn källa; hellre för lite än för mycket (standard avsnitt 10). Godtaget.
- 3 × engelska ord "Pink" på 3270 (titel, meta, beskrivning): färgnamnet "Twisted Pink" är produktens egen färgbeteckning. Godtaget.
Första körningen gav 41 FEL "fakta_saknas" eftersom källtexten låg i fel fält; det var ett fel i min kopia, inte i texterna, och rättades före redovisningen ovan.

## Skrivning
Butik skriven med productUpdate(product: ProductUpdateInput): title, seo och descriptionHtml. Handle och status skickades inte. userErrors: inga för alla 41.
- Kanarie: 3227, 3231, 3233 (tre varianter: meta saknas, meta finns, SEO-titel lika med titel). Återläst och godkänd före resten.
- Resten i delbatcher om högst 9 (en första sändning på 15 avvisades av Shopify före skrivning, GraphQL-dokumentet över 16 384 tecken; inget skrevs då).
- seo skickades med både title och description för de 32 produkter som har meta. Meta saknas på 9 produkter (3227, 3230, 3232, 3259, 3261, 3269, 3274, 3282, 3287). För dessa skickades bara seo.title, eller inget seo alls när SEO-titeln är lika med titeln (3269, 3274, 3287).

## Återläsning (alla fält: title, handle, status, seo.title, seo.description, descriptionHtml)
Jämfört för hand mot skrivfilen och mot det som skickades. Ingen maskinell diff: MCP-utdata kan inte diffas i bash (LARDOMAR 2026-11-01), och jag har inte skrivit av återläsningen till en fil.
- title: lika med filen på alla 41.
- handle: oförändrade på alla 41 (jämfört med före-läget).
- status: ACTIVE på alla 41.
- seo.title: lika med filen där SEO-titeln skiljer sig från titeln. Där den är lika med titeln lagrar Shopify null (avsett): 3233, 3235, 3244, 3245, 3246, 3250, 3252, 3263, 3272, 3280, 3285, 3292, 3293, 3294, 3295 (15 med meta, kontrollerade i återläsningen) samt 3269, 3274, 3287 (utan meta, där seo utelämnades och både SEO-fälten är null).
- seo.description: lika med filens meta där meta finns; null där meta är null.
- descriptionHtml: lika med filen på alla 41, inklusive radbrytning mellan `<li>` (avsett), standardblocket och säljaruppgifterna.

## Taggar
tagsAdd(id, tags:["texter-klara"]) på alla 41, userErrors: inga. Återläst: "texter-klara" finns på alla 41 och samtliga tidigare taggar (Gymstick, Yoga, Massage & Återhämtning, Foam Rollers m.fl.) finns kvar.

## Avvikelser
- Skrivning i delbatcher om 8–9 i stället för 15 på grund av Shopifys gräns på 16 384 tecken per GraphQL-dokument.
- Fel i min första kopia för kontrollskriptet (fält), rättat före redovisning.
- Innehåll som granskarna redan godkänt har inte omprövats. Observera för uppföljning: 3250, 3274 (massagebollar), 3283, 3287 (massagebollar) samt 3272 (massagerulle) har hälsoord som produktnamn, vilket är godtaget enligt standarden (massagerulle, massageboll).
- Titelns synk-risk (LARDOMAR 2026-10-30): läs tillbaka titlarna igen efter nästa nattsynk av Velomarket/Gymstick-produkter.
