# Våg 2c resten 1 (Gymstick, 43 produkter) – skrivrapport 2026-11-02

Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info före skrivning. Skrivfil: `vag2_skriv/c_skriv_resten_1.json` (43 produkter, 43 unika id). Före-läge sparat före skrivning: `rapporter/shopify-original-2026-11-02/vag2c_resten_1_fore.json` (id, titel, handle, status, taggar, SEO, beskrivning som HTML).

## Före
Alla 43 var ACTIVE, ingen hade taggen "texter-klara", ingen hade en titel lika med skrivfilens. SEO-titel och SEO-beskrivning var null på alla 43. Beskrivningarna var leverantörens marknadsföringstext eller (3 Velomarket-produkter) korta tekniska rader. Inga hoppades över.

## Kontrollskriptet
Kört på en kopia (html mappad till beskrivning, standardblocket omgivet av [[STANDARDBLOCK]], `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS"`, källtext = före-läget: originaltitel + beskrivning som ren text). Resultat: 43 produkter, **0 FEL**, 66 VARNINGAR:
- "saknar avsnittet 'passar dig som'" på 43 av 43: texterna använder rubriken "Passar för" (känt och godtaget).
- "beskrivning_langd" (under 40 ord) på 19 produkter: tunn källa, hellre kort än påhittad text (standard avsnitt 10).
- "saknar avsnittet 'specifikationer'" på 3014 (Greppringar): källan har inga specifikationer.
- "engelska_ord: Pink" på 3074 (titel, SEO-titel, beskrivning): färgnamnet "Twisted Pink" kommer från originaltiteln.
Inget stoppade skrivningen.

## Skrivning
`productUpdate(product: ProductUpdateInput)` med title, descriptionHtml och seo. Handle och status skickades aldrig.
- Kanarie (3 produkter, en av varje SEO-variant): 3001, 3014, 3025. userErrors: inga. Återläst och jämförd före resten.
- Därefter 15 + 15 + 10 produkter. userErrors: inga i någon batch.
- SEO-regeln: meta finns, seo och meta skickas båda (22 produkter). Meta saknas och SEO-titeln skiljer sig från titeln: bara seo.title (5 produkter; live seo.description var null). Meta saknas och SEO-titeln är lika med titeln: seo utelämnad (16 produkter).

## Återläsning (title, handle, status, seo.title, seo.description, descriptionHtml)
Alla 43 lästes tillbaka efter skrivning (kanarien separat, 40 i två frågor). Jämfört **för hand**, tecken för tecken mot filen; ingen maskinell diff (MCP-svar kan inte diffas i bash).
- title: lika med filen på alla 43.
- handle: oförändrade på alla 43 (jämfört mot före-läget). status: ACTIVE på alla 43.
- seo.title: lika med filen där den skiljer sig från titeln; null där den är lika med titeln (avsett Shopify-beteende), på 22 produkter.
- seo.description: lika med filen där meta finns (22); null där meta är null i filen (21), lika med före-läget.
- descriptionHtml: lika med filen på alla 43, inklusive radbrytning mellan `<li>` (avsett), standardblocket och säljaruppgifterna.

## Taggar
`tagsAdd(id, tags:["texter-klara"])` på alla 43, userErrors inga. I svaret fanns alla befintliga taggar kvar (till exempel Gymstick, Velomarket, Träningsbollar, Greppträning, Boxning, Kettlebells) tillsammans med "texter-klara". Jämfört mot före-lägets taggar för hand.

## Avvikelser
Inga avvikelser mot skrivfilen. Reservationer:
- Jämförelsen är gjord för hand (se ovan).
- Språk- och faktagranskning av texterna ingick inte i skrivsteget; den gjordes av de oberoende granskarna före skrivfilen.
- Synk-risk (LARDOMAR 2026-10-30 och 2026-11-02): tre av produkterna (3001, 3004, 3005) är Velomarket-produkter. Läs tillbaka titlar, SEO och beskrivning efter nästa nattsynk och jämför mot skrivfilen. Hela batchen bör kontrolleras via `updatedAt` efter natten.
- Inget ändrades i Shopify utöver title, seo, descriptionHtml och taggen "texter-klara" på de 43 produkterna.
