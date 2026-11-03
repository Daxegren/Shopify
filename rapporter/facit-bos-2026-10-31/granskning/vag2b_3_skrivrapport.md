# Skrivrapport våg 2b, batch 3 (BEST OF SPORTS, 37 Velomarket-produkter)

Datum: 2026-11-03. Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info.
Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/b_skriv_2.json` (oförändrad).
Före-läge: `rapporter/shopify-original-2026-11-03/vag2b_3_fore.json`.

## 1. Urval

- 37 produkter i skrivfilen. Alla 37 hade status ACTIVE i live, ingen hade taggen "texter-klara" och ingen hade redan skrivfilens titel.
- Hoppade över: 0 produkter.
- Handle och status ändrades inte på någon produkt.

## 2. Före-läge och kontroll före skrivning

- Före-läget (titel, SEO-titel, metabeskrivning, descriptionHtml och taggar) sparades för alla 37 innan första skrivning. Filen är kontrollerad: 37 poster, unika id, samma id som skrivfilen, status ACTIVE, SEO-fält null.
- Kontrollskriptet `kontrollera_produkttext.py` kördes på en kopia: html mappad till beskrivning, standardblocket markerat, källtext = före-läget, `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS"`.
- Resultat: 37 produkter, 0 FEL, 39 VARNINGAR. 37 av varningarna är "saknar avsnittet 'passar dig som'" (rubriken "Passar för" är godtagen). De övriga 2 är beskrivning_langd: Cykelklocka Basil Portland (27 ord) och Handskar Liv Supreme SF (35 ord).

## 3. Skrivning

| Steg | Produkter | Resultat |
|---|---|---|
| Kanarie | 3 (Styrväska Basil Mali, Ramväska Basil Navigator Storm S, Cykelklocka Basil Portland) | Inga userErrors. Återläst och jämförd före övriga. |
| Batch 2 | 8 | Inga userErrors |
| Batch 3 | 8 | Inga userErrors |
| Batch 4 | 8 | Inga userErrors |
| Batch 5 | 8 | Inga userErrors |
| Batch 6 | 2 | Inga userErrors |

Skrivningen gjordes med productUpdate(product: ...) i mutationer om högst 8 produkter. SEO skickades alltid som title och description tillsammans. Där metabeskrivning saknas skickades bara seo.title. Där SEO-titeln är lika med produkttiteln utelämnades seo, eller skickades med description, som Shopify lagrar som null.

## 4. Läsning tillbaka och jämförelse

- Kanarien lästes tillbaka separat före övriga skrivningar.
- Alla 37 lästes sedan tillbaka i två anrop (25 och 12) för titel, handle, status, tags, seo.title, seo.description och descriptionHtml.
- Jämförelsen mot skrivfilen är gjord för hand, genom läsning. Det går inte att köra en maskinell diff av MCP-svar i bash. Det som kontrollerats maskinellt är kontrollskriptet på före-kopian och JSON-kontrollen av före-filen.
- Resultat: alla 37 överensstämmer med skrivfilen i titel, metabeskrivning och descriptionHtml. Handle och status är oförändrade. Befintliga taggar finns kvar.
- Förväntade skillnader, ingen avvikelse:
  - seo.title är null för 6 produkter där SEO-titeln är lika med produkttiteln (Styrväska Basil Mali, Sadelväska Giant Shadow DX, Cykelklocka Basil Portland, Bakskärm Giant Speedshield Clip-On, Cykelskydd Oxford Aquatex, Strumpor Liv Short N Snug).
  - seo.description är null för 4 produkter där skrivfilen saknar metabeskrivning (Cykelklocka Basil Portland, Stänkskärmar SKS Fatboard, Handpump Liv Control Mini+, Handskar Liv Supreme SF).

## 5. Taggar

- "texter-klara" lades till på alla 37 med tagsAdd. Svaren visar att befintliga taggar finns kvar på varje produkt.

## 6. Resultat före och efter

| Fält | Före (37 produkter) | Efter |
|---|---|---|
| Titel | Leverantörens originaltitel, t.ex. "Väska för Basil Mali styre, 8L" | Skrivfilens titel på alla 37 |
| SEO-titel | null på alla 37 | Satt på 31. Null på 6 där den är lika med titeln. |
| Metabeskrivning | null på alla 37 | Satt på 33. Null på 4 där skrivfilen saknar den. |
| Beskrivning (descriptionHtml) | Leverantörstext, ofta med annonstext och sjok av mått och märkesbakgrund | Skrivfilens text på alla 37 |
| Taggar | Befintliga | Befintliga plus "texter-klara" |
| Handle och status | Oförändrade | Oförändrade |

## 7. Avvikelser

- Inga avvikelser i Shopify. Inga userErrors i någon mutation.
- Under förberedelsen skrev jag först en förkortad descriptionHtml för Flaskhållaradapter SKS (10475978653962) i före-filen. Det rättades innan någon skrivning gjordes. Shopify påverkades inte, och före-filen är nu komplett.

## 8. Ändrat

- Shopify: JA. 37 produkter fick nya titlar, SEO-titlar (där de skiljer sig från titeln), metabeskrivningar (där skrivfilen har dem) och descriptionHtml. Taggen "texter-klara" lades till på alla 37.
- Pris, lager, bilder, handle och status ändrades inte.
- Filer: ny fil `rapporter/shopify-original-2026-11-03/vag2b_3_fore.json`, ny denna rapport. Ingen commit.

## 9. Att göra härnäst

- Läsa tillbaka titlarna på de 37 efter nattsynken 2026-11-04 (LARDOMAR 2026-11-02 och 2026-11-03).
- Stickprov på 20 procent av batchen, minst 10 produkter, av en starkare granskare än skribenten (LARDOMAR 2026-11-03).
