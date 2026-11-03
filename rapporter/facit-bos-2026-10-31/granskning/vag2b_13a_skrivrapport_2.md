# Våg 2b, grupp 13a (cykellås), skrivrapport 2

Datum: 2026-11-03. Butik: BEST OF SPORTS (bestofsports.se, verifierad med get-shop-info).
Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/b_skriv_13a.json` (29 produkter).
Före-läge: `rapporter/shopify-original-2026-11-03/vag2b_13a_fore.json` (inte ändrat).

## Status: klart

Index 10–28 (19 produkter) är skrivna och verifierade. Taggen "texter-klara" är lagd på alla 29 produkter. Index 0–9 skrevs inte om i denna körning.

Den första körningen avbröts på grund av checkerns meta-kontroll (se nedan). Koordinatorn bekräftade därefter att avsnitt 17 i `shopify-sync/docs/produkttexter-standard.md` gäller: en metabeskrivning på minst 70 tecken godkänns när utfyllnad annars skulle krävas. Kontrollen kördes om med `--meta-min 70` och gav 0 FEL.

## Kontroll före skrivning (kontrollera_produkttext.py)

Kopia av index 10–28, html mappad till beskrivning, standardblocket markerat med [[STANDARDBLOCK]], källtext = före-läget. Kopian: `/tmp/claude-0/-home-user/fbbd95a3-8b18-5096-a6b5-20df3e4eb235/scratchpad/kontroll_10_28.json`. Utdata: `.../scratchpad/kontroll_10_28_out.txt`.

- Med standardkravet 130–155 tecken: 14 FEL (meta_langd) på 8651, 8652, 8655, 8657, 8658, 8659, 8661, 8663, 8664, 8665, 8666, 8667, 8668, 8669.
- Med `--meta-min 70` (avsnitt 17): 0 FEL, 19 VARNINGAR "saknar avsnittet 'passar dig som'". Det är rubrikvarningen som skrivprompten godtar.

## Skrivning (productUpdate, batcher om 5)

- Mutation och variabler skrevs ut av `scratchpad/skriv_mut.py` (ensure_ascii=True) och klistrades in oförändrade. Ingen text skrevs för hand.
- Batcher: [10, 11, 12] (kanarie), [13–17], [18–22], [23–27], [28].
- Alla anrop gav `userErrors: []`.
- Titel, seo{title, description} och descriptionHtml skickades för varje produkt. `seo.title` är null där SEO-titeln är lika med titeln, vilket är avsett.
- Handle och status ändrades inte. Status är ACTIVE för alla.

## Återläsning och jämförelse

- Svaren från productUpdate (titel, handle, status, seo, descriptionHtml, tags) jämfördes maskinellt mot skrivfilen i Python, för varje batch, med skriptet `scratchpad/aterlas_check.py`.
- Resultat: 0 avvikelser i alla fem batcher. Inga osynliga tecken (U+00AD eller nollbreddstecken) i någon descriptionHtml.
- Det som jämförts maskinellt: title, seo.title, seo.description, descriptionHtml, status och osynliga tecken. Det som jämförts för hand: taggarna för varje produkt.

## Taggning (tagsAdd "texter-klara")

- Taggen lades på alla 29 produkter, i batcher om 5 (sista batchen 4). Alla anrop gav `userErrors: []`.
- Befintliga taggar finns kvar i svaren. Exempel: 8670 har fortfarande "På beställning", som inte hör till skrivningen och inte ändrades.
- Ingen av de 29 hade taggen före körningen, enligt live-läsningen för index 0–24 och svaren för 25–28.

## Avvikelser och noteringar

- Index 25–28 lästes inte live innan skrivning. Före-läget för dem är skrivfilens "före"-värden från den första körningen, inte en live-läsning. Det påverkar bara jämförelsen av före-läge, inte kontrollen av efter-läget.
- Index 0–9 (8638–8647) är inte skrivna i denna körning. Nr 8638 har meta på 124 tecken i skrivfilen. Det är över 70, så det godkänns enligt avsnitt 17.
- Live-läsningen för index 0–24 gjordes före skrivning. För 10–24 visade den befintliga titlar och texter som redan liknade skrivfilen, och samma titlar fanns kvar efter skrivning.

## Ändrat

- Shopify: ja. productUpdate på 19 produkter (8648–8670), tagsAdd "texter-klara" på 29 produkter (8638–8670).
- Filer: denna rapport. Scratchpad-filerna ligger utanför repot.
- Ingen annan fil i repot ändrades. Ingen commit.
