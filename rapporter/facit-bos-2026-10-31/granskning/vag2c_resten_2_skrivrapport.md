# Våg 2c resten 2 (Gymstick, 43 produkter) – skrivrapport 2026-11-02

Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info före skrivning. Skrivfil: `vag2_skriv/c_skriv_resten_2.json`. Före-läge: `rapporter/shopify-original-2026-11-02/vag2c_resten_2_fore.json` (sparat före skrivning, alla 43 med title, handle, status, tags, seo, descriptionHtml).

## Före
Alla 43 lästes live (2 läsningar, 25 + 18). Alla ACTIVE. Ingen hade taggen "texter-klara", ingen hade titel lika med skrivfilens. Inga produkter hoppades över. SEO-titel och SEO-beskrivning var tomma (null) på alla. Beskrivningarna var leverantörens marknadsföringstext (till exempel "din ultimata följeslagare", "perfekta partner"); fyra hade ren text utan HTML.

## Kontrollskriptet (kopia, html mappad till beskrivning, standardblock markerat, --seo-title-max 43 --seo-suffix " – BEST OF SPORTS", källtext = före-läget)
Resultat: 43 produkter, 0 FEL, 51 VARNINGAR. Varningarna är kända eller godtagna:
- 43 st "saknar avsnittet 'passar dig som'": texterna använder rubriken "Passar för" (känd, godtagen).
- 1 st titel_kommatecken (3133, mått i titeln, känd, godtagen).
- 3 st beskrivning_langd (3089 36 ord, 3096 33 ord, 3146 25 ord): tunn källa, kort intro enligt standarden.
- 2 st engelska_ord "with" (3144 och 3148): kommer från produktnamnen "Lifting Straps with Padding" och "Medicine Ball with Handles" som tillverkaren anger på engelska.

## Skrivning
productUpdate(product: ProductUpdateInput) med title, seo och descriptionHtml. Handle och status skickades inte. Kanarie först (3 produkter: 3089, 3090, 3091), återläst och kontrollerad, därefter resten. Batcher: 3 + 8 + 8 + 8 + 8 + 8 = 43. Batcherna blev högst 8 eftersom Shopifys verktyg avvisar dokument över 16 384 tecken (ett försök med 15 produkter avvisades före körning, inget skrevs). userErrors: inga i någon batch.
- seo skickades med både title och description för 38 produkter.
- Meta är null i filen för 3089, 3146, 3147, 3153, 3154. För 3089, 3147 och 3154 skickades bara seo.title (SEO-titeln skiljer sig från titeln). För 3146 och 3153 är SEO-titeln lika med titeln, så seo utelämnades (Shopify lagrar null).

## Återläsning (title, handle, status, seo.title, seo.description, descriptionHtml)
Alla 43 återlästes (kanarie 3 i eget steg, övriga 40 i två läsningar).
- **Maskinellt (python mot skrivfilen):** title och seo.title för alla 43. 0 avvikelser. seo.title null accepterades där SEO-titeln är lika med titeln (avsett).
- **För hand (läst mot filen):** seo.description, descriptionHtml (inklusive standardblock och säljaruppgifter, radbrytning mellan `<li>` som Shopify lägger dit), handle (oförändrade mot före-läget, bland annat `tyg-mini-band-latt`, `fascia-ball-cork`, `vikbar-gymmatta-300-x-120-x-5-cm-svart`) och status (ACTIVE på alla). Ingen maskinell diff av beskrivningstext, eftersom MCP-utdata inte kan diffas i bash. Ingen avvikelse hittades.
- seo.description null som väntat på 3146, 3147, 3153 och 3154 (och 3089, lika med filens meta null).

## Taggar
tagsAdd(id, tags:["texter-klara"]) på alla 43, inga userErrors. Återläst: alla 43 har "texter-klara" och alla tidigare taggar finns kvar (jämfört mot före-läget, till exempel Gymstick, Träningsmattor, Motståndsband, Massage & Återhämtning, Greppträning, Gymstick Stänger). Status ACTIVE på alla.

## Avvikelser
- Batchstorleken (8 i stället för upp till 15) på grund av dokumentgränsen på 16 384 tecken. Ingen påverkan på resultatet.
- Beskrivningstexten jämfördes för hand, inte maskinellt (se ovan).
- Titelns synk-risk (LARDOMAR 2026-10-30): läs tillbaka titlar, SEO och beskrivning igen efter nästa nattsynk av Gymstick-produkter (`updatedAt` mot skrivtidpunkt 2026-11-02).
