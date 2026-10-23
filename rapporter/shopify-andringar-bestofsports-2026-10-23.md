# Ändringar i Shopify, Best of Sports (2026-10-23)

Alla ändringar är gjorda med Davids uttryckliga ja (förslag A–E, Minibike som utkast, Melatonin bort från Shopping) i `rapporter/bestofsports-merchant-och-kategorier-2026-10-23.md`. Exakta originaltexter finns i `rapporter/shopify-original-2026-10-23/` och exakta efter-versioner i filer med prefixet `EFTER-`. Varje text är kontrollerad tecken för tecken mot förväntad text (identisk).

## Ändringar

| # | Vad | Före | Efter | Kontroll |
|---|---|---|---|---|
| A | Kategori Motionscykel, beskrivningen | "…pålitliga varumärken som TUNTURI, CHRISTOPEIT, KETTLER, HAMMER, BH Fitness, Gorilla Sports och MAXXUS." | "…pålitliga varumärken som Tunturi, BH Fitness, Toorx, Hammer och Christopeit." | Identisk med förväntad |
| B | Kategori Träningsbänk, beskrivningen | "…från ledande varumärken som TUNTURI, CHRISTOPEIT, KETTLER, HAMMER, BH Fitness, Gorilla Sports och MAXXUS." | "…från varumärken som Tunturi, Hammer, Finnlo, Christopeit och Gorilla Sports." | Identisk |
| B | Kategori Träningsbänk, metabeskrivning | "Upptäck träningsbänkar från TUNTURI, CHRISTOPEIT, KETTLER, HAMMER, BH Fitness, Gorilla Sports och MAXXUS. …" | "Upptäck träningsbänkar från Tunturi, Hammer, Finnlo, Christopeit och Gorilla Sports. …" | Identisk, SEO-titeln oförändrad |
| C | Kategori Roddmaskin, beskrivningen (varumärken) | "…TUNTURI, CHRISTOPEIT, KETTLER, HAMMER, BH Fitness, Gorilla Sports och MAXXUS." | "…Tunturi, Hammer, Christopeit, BH Fitness, Finnlo och Toorx." | Identisk |
| C | Kategori Roddmaskin, meningen om modeller | "Våra roddmaskiner finns i olika modeller, inklusive traditionella luftmotståndsmodeller, vattenbaserade roddmaskiner och roddmaskiner i trä för en mer naturlig känsla." | "Våra roddmaskiner finns i flera olika modeller och prisklasser." | Identisk |
| D | Kategori Lådcykel, stycket Kända varumärken | Beskrev Christiania Bikes, Babboe och Winther (tre meningar om märken som inte säljs) | "Hos Best Of Sports hittar du lådcyklar och elassisterade lastcyklar från bland annat Cargobike of Sweden och Amladcykler." | Identisk |
| E | Kategori Barncykel 6–8 år (20"), regel | Regel: etikett = `6-8` (0 produkter) | Regel: etikett = `barncykel-20` (13 produkter) | 13 produkter, alla aktiva med lager |
| E | Etiketten `barncykel-20` lades till på 13 produkter | – | De 13 aktiva 20-tumscyklarna med lager (Romet Rambler 20 KID 1 och 2, S´COOL Wave Steel LTD 20" och Xroc 20" ×2, LIV Tempt 20 ×2, LIV STP 20 och STP 20 FS, GIANT Talon 20, GIANT STP 20, GIANT ARX 20, TABOU Queen 20) | Alla 13 listas i kategorin |
| E | Kategori Barncykel 6–8 år (20"), texten | "…från välkända märken som Giant, Liv, Kona och Romet." | "…från märken som Romet, Liv, Giant, S´COOL och Tabou." | Identisk |
| P1 | Produkt Minibike TUNTURI Minibike Basic | Status aktiv, 8 i lager (Google: "Recalled product") | **Utkast** (inte längre till salu) | Status DRAFT bekräftad |

**Avvikelse från förslaget:** förslaget nämnde sex 20-tumscyklar att etikettera. Jag etiketterade alla 13 aktiva 20-tumscyklar med lager (fler än sex), eftersom alla hör hemma i kategorin och en kategori med bara sex hade varit missvisande. Etiketten är en vanlig produktetikett och kan tas bort per produkt.

## Inte gjort, och varför
- **Melatonin (TREC) bort från Google Shopping:** Shopify-kopplingen jag använder blockerar avpublicering (`publishableUnpublish`) av säkerhetsskäl. Produkten är därför oförändrad och ligger kvar på Google & YouTube. David gör det i Shopify admin: Produkter, TREC Melatonin, Försäljningskanaler och appar, ta bort Google & YouTube. Alternativt utesluts produkten i Merchant Center.
- **Yogamatta Movit (3 varianter) och Latexband Paket, bildbyte:** jag kan inte se bilderna härifrån (Shopifys bildserver är inte nåbar för mig), så jag kan inte avgöra vilken bild som har text eller är olämplig. Yogamattornas bilder är alla 493 px (en enda på 1 500 px, `20040302___P1.webp` på 190x100) och uppfyller därför inte storlekskraven; ny bild måste komma från Gorilla Sports Norden. Latexband har åtta bilder (725 px): vilken som ska vara huvudbild avgör David.
- **Styrlager SHIMANO FH-MC18:** produkten har ingen bild och rubriken stämmer inte med produkten (FH-MC18 är en frihjulsnav/frihjulskropp för 8–10-växlade kassetter, inte ett styrlager). Jag har inte hittat en bild som vi har rätt att använda; leverantören (Velomarket) bör lämna bild. Se [en sida om reservdelen](https://www.incycle.com/products/shimano-freehub-body-fh-mc18-3a) och [en annan](https://aroundthecycle.com/products/new-shimano-alivio-mc18-deore-m525-510-9-speed-freehub-body-with-seal-does-not-include-fixing-bolt-or-washer) för att bekräfta vad produkten är. Förslag: sätt produkten som utkast tills bild finns.
- **Roddmaskin, avsnittet om vatten- och träroddmaskiner:** står kvar oförändrat tills David avgjort beslut 3 (vattenroddmaskiner finns inte, Fluid-träroddmaskinerna är slut).
- **Merchant-rättningarna för Ab Sling (namn, etikett), titlar med "Default Title" och övriga:** inte gjorda; väntar på besked.

## Mätning
Testloggen (`site-audit test add`) körs av David i Cloud Shell. Förslag:
- A–D: `--pages /collections/motionscykel,/collections/traningsbank,/collections/roddmaskin,/collections/ladcyklar`, mått `gsc_clicks`, start 2026-10-23, 28 dagar, förväntat 5 % (en gissning; ändringarna rättar fel och flyttar sannolikt inte rankningen mycket).
- E: `--pages /collections/barncyklar-6-8-ar-20`, mått `gsc_clicks`, start 2026-10-23, 28 dagar, förväntat 20 % (en gissning; sidan har fått produkter för första gången).
Utvärdering tidigast 2026-11-24 (Search Console släpar tre dagar).
