# Granskningsutlåtande k_46sak6: aktiva produkter i tidigare utanför-kategorier (2026-11-08)

Granskaren har bara läst i Shopify och har inte ändrat något där. Inget har committats. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient; `verifiera_butik` gav BEST OF SPORTS). `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08, LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md` och `k_utlatande_46sak4.md`, samt formatet i `k_utlatande_43.json`. Enligt beslutet 2026-11-08 får aktiva produkter utan texter-klara faktatext, även trampoliner och belysning.

Alla 3 utkast är ACTIVE och har lager > 0. Bara 46603 har taggen På beställning, och bara den har leveranstidsmeningen. Standardblocket är rätt på alla. Titlarna är 28–53 tecken med högst 1 kommatecken, SEO-titlarna 27–42 tecken och metatexterna 125–139 tecken med verb. "Passar för" finns på alla, och ingen text har fler än två "enligt tillverkaren". Butiken söktes på Propel, Studsmatta, trampolin och Eclipse, på Bookman-lampor och på EAN 7350051865756 och 4260438738586. Ingen exakt dubblett hittades (R12a), och inga SEO-krockar mot butiken eller mot andra utkast i `rapporter/`. `skrivfil_kontroll.py` ger 0 fel och 0 varningar, både på utkasten och på de rättade texterna. Varje rättning är ETT sammanhängande före/efter-par per fält, och varje före-text förekommer exakt en gång i fältet (kontrollerat i python).

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_46sak6.json`.

## Resultat: 1 GODKÄND, 2 RÄTTA, 0 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 46601 | 10636696518922 | k_46sak6_utkast.json | RÄTTA | meta |
| 46602 | 10665226830090 | k_46sak6_utkast.json | RÄTTA | titel, seo_title |
| 46603 | 10676721189130 | k_46sak6_utkast.json | GODKÄND | – |

## Rättningar (före → efter)

- **46601 meta:** "Studsmattan har sex fötter, 48 gummiband i fjädringssystemet och ett justerbart handtag. Maximal belastning är 150 kg enligt tillverkaren." → "Studsmattan har sex fötter, 48 gummiband i fjädringssystemet och ett handtag som justeras i sex steg. Den kan användas inomhus och utomhus."
- **46602 titel:** "Ljus Bookman Eclipse bärbar lampa" → "Ljus Bookman Eclipse Bärbar Lampa"
- **46602 seo_title:** "Ljus Bookman Eclipse bärbar lampa" → "Ljus Bookman Eclipse Bärbar Lampa"

## Motivering per produkt

- **46601 Studsmatta Trampolin 100 cm (RÄTTA):**
  - Underlag: produkten är ACTIVE och har tre färgvarianter med olika pris (SKU 100974-00043/-00077/-00042-0001) och lager 96. Det är samma artikel i olika färg, så v1.9 är uppfylld.
  - Källa: alla uppgifter står ordagrant i produktens svenska källa.
  - Lastgräns: "Maximal belastning: 150kg" står på en egen rad med etikett och enhet. Den får därför stå en gång som "enligt tillverkaren" (R4, v1.10). Den tidigare avvisningen kallade uppgiften "löptext utan etikett", vilket inte stämmer.
  - Utelämnat, med rätta: källans påståenden om leder, balans, koordination och kondition samt orden "högkvalitativt" och "skonsamt".
  - Rättning: lastgränsen stod både i meta och i specifikationen. Den tas bort ur meta.
- **46602 Bookman Eclipse (RÄTTA):**
  - Underlag: SKU 575, EAN 7350051865756, lager 1.
  - Källa: varje uppgift finns i produktens egen källa.
  - Utelämnat, med rätta: säkerhet, synlighet, "kraftfull", "robust", "breda ljuskäglan" och kombinationen med reflexkläder. Uppgiften om laddning finns bara hos återförsäljare och är också rätt utelämnad.
  - Rättning: de beskrivande orden i titel och SEO-titel ska ha stor bokstav (R9, `format_regler.titel_versaler`).
  - Övrigt: det finns ett äldre, oskrivet utkast för samma id i b_51. Det är inte en dubblett.
- **46603 Giant Propel Advanced Pro 0 AXS (2027) (GODKÄND):**
  - Varianter: storlekarna M, M/L, L och XL har två olika priser och totalt lager 1 (v1.9). Storlek S säljs inte och är utelämnad (v1.5).
  - Källa: alla specifikationer stämmer med produktens egen källa och med tillverkarsidan https://www.giant-bicycles.com/ee/propel-advanced-pro-0-axs-2027 (färg Obsidian Pulse, ram, gaffel, SRAM Force AXS E1, bromsar, hjul, däck, största däckbredd 32 mm och cyklistlängder).
  - Utelämnat: inga prestanda- eller komfortlöften finns kvar.

## Löften (hälsa, säkerhet, skydd, utveckling, prestanda, kvalitet)

Alla tre texterna söktes igenom efter både tydliga och subtila löften: säker, synlig, skydd, stabil, robust, hållbar, kvalitet, skonsam, leder, balans, kondition, snabb, styv, aerodynamisk, komfort, prestanda, perfekt och idealisk. Inget av detta finns kvar.

## Avvisade (k_46sak6_avvisade.json)

Ingen avvisning är uppenbart fel, och ingen lyfts ur:

- **Exakta dubbletter:** Giant AnyTour ×2 och BH Lyon Climber.
- **Olika artiklar:** Wall Ball-paketet och kettlebell 4 kg.
- **Titeln motsäger källan:** viktlåset (30 mm i titeln, 31 mm i källan).
- **Oklara varianter:** Bookman-klistermärkena.
- **Redan skrivna:** tre produkter.
- **Motsägande batteriuppgift och inget lager:** Fathom E+ 2 EX.
