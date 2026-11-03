# Stickprov Velomarket 2 (b_stickprov_2.json, 10 produkter)

Kontrollerad 2026-11-03, endast läsning. Butik: BEST OF SPORTS (bestofsports.se) bekräftad via get-shop-info.
Live hämtat med nodes(ids) (title, handle, status, tags, seo, descriptionHtml). Leveransblocket läst i live-svaret och identiskt med blocket i stickprovet för alla tio (5239 har tillägget "Beställningsvaror kan ta upp till en vecka längre." i både live och stickprov).

## Matchning live mot stickprov

| nr | title | seo.title | seo.description | descriptionHtml | status/handle | tagg texter-klara + övriga kvar |
|---|---|---|---|---|---|---|
| 5203 | ja | ja (null) | ja (null) | ja | ja | ja |
| 5239 | ja | ja | ja (null) | ja | ja | ja |
| 5266 | ja | ja | ja (null) | ja | ja | ja |
| 5270 | ja | ja | ja (null) | ja | ja | ja |
| 5222 | ja | ja | ja | ja | ja | ja |
| 5240 | ja | ja (null, lika med titeln) | ja | ja | ja | ja |
| 5219 | ja | ja | ja | ja | ja | ja |
| 5226 | ja | ja (null) | ja | ja | ja | ja |
| 5235 | ja | ja (null) | ja | ja | ja | ja |
| 5201 | ja | ja (null) | ja | ja | ja | ja |

Resultat: 10 av 10 matchar exakt. Alla ACTIVE, handle oförändrad mot före-filen, alla taggar ur före-filen finns kvar plus texter-klara.

## Språkfynd (svenska, kompatibilitet mot leverantörens original)

Inga stavfel, grammatikfel, saknade verb i första metameningen, påhittade fakta eller arbetstermer hittades. "enligt tillverkaren" förekommer högst en gång per text (5239 html, 5226 html, 5201 html, 5240 meta). Kompatibilitetsuppgifter stämmer med leverantören (5226 mountainbikes och hybridcyklar, sadelstolpe, justerbar vinkel; 5222 Schrader och Presta, 1,5 tum; 5235 inomhus/utomhus, 1 cykel, 200 x 80 x 110 cm; 5219 mått och vikt).

Mindre fynd:

| nr | fält | före | förslag | kommentar |
|---|---|---|---|---|
| 5226 | html, målgruppspunkt 1 | "Dig som har en mountainbike eller hybridcykel och vill ha en bakskärm, enligt tillverkaren" | "Dig som har en mountainbike eller hybridcykel och vill ha en bakskärm" | Hängande "enligt tillverkaren" i slutet av punkten är krångligt; uppgiften är en ren produktuppgift. |
| 5226 | materialterm | html "flexibelt PP-material"; spec och meta "PP-plast" | enhetligt "PP-material" eller "PP-plast" | Inkonsekvent, leverantören skriver PP-material. Låg prioritet. |
| 5235 | meta | "ett cykelskydd för en cykel som kan användas både inomhus och utomhus" | "ett cykelskydd för en cykel, avsett för både inomhus- och utomhusbruk" | "som" kan läsas som att cykeln används inomhus/utomhus. |
| 5240 | html mot meta | html: "ett stretchigt och lätt material" (utan förbehåll); meta: "som enligt tillverkaren är stretchigt, ventilerande och lätt" | Medvetet eller samordna | Leverantören anger även "mycket ventilerande"; utelämnat i html. Storlek XS/S (34-37) i leverantörstexten finns inte med någonstans (rimligt om titeln saknar storlek, men värt ett beslut). |
| 5219 | spec | "Fjädring: Fjädrar" | "Fjädring: Ja" eller "Fjädring: Spiralfjädrar" (bara om belagt) | Cirkulärt. Låg prioritet. |

## Rekommendation

Full manuell kontroll av hela batchen: nej. Tekniskt utfall är 10/10 exakt och språket är rent; fynden ovan är kosmetiska (ev. en liten rättning av 5226 punkt 1 och 5235 meta). Kör i stället automatisk avstämning live mot b_skriv_2.json för resten av batchen (title, seo, descriptionHtml, status, handle, taggar).
