# Skrivrapport våg 2b-7 (BEST OF SPORTS, tillbehör), 2026-11-03

Butik: BEST OF SPORTS (bestofsports.se). Verifierad med get-shop-info före skrivning.
Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/b_skriv_7.json` (43 produkter).
Före-läge (live, sparat före skrivning): `rapporter/shopify-original-2026-11-03/vag2b_7_fore.json` (43 produkter).
Kontrollkopia: `rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2b7/kopia_vag2b_7.json`.

## 1. Före
- Alla 43 produkter ACTIVE. Ingen hade taggen `texter-klara`. Ingen hade titel lika med skrivfilens titel. Ingen hoppades över.
- seo.title och seo.description var null på alla 43.

## 2. Kontroll före skrivning
- `kontrollera_produkttext.py` kördes på kopian (html mappad till beskrivning, standardblocket inom `[[STANDARDBLOCK]]`, fakta = före-läget, `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS"`).
- Resultat: 0 FEL, 68 VARNINGAR.
  - 43 st "passar dig som": avsiktlig varning (rubriken heter "Passar för"), godtagen.
  - 10 st beskrivning_langd (35 ord, tunn källa), godtagen.
  - 15 st engelska_ord ("Blue", "Green" i färg- och modellnamn från källan, t.ex. Aruba Blue, Ash Blue, Green Life), godtagen.

## 3. Skrivning
- 6 batcher: kanarie 8207–8209 (3 produkter), sedan 5 batcher à 8 produkter. Högst 8 produkter per productUpdate-anrop.
- Mutationer och variabler byggdes av skriptet `bygg_batcher.py` (i scratchpad) ur skrivfilen. Ingen text skrevs för hand i mutationen.
- Avvikelse från utskriften: kanariebatchens variabler klistrades in med \uXXXX-escapes i stället för råa UTF-8-tecken. JSON-innehållet är identiskt, och återläsningen av kanarien jämfördes ändå tecken för tecken.
- SEO-regel: meta finns → `seo{title, description}` med båda fälten. Meta null och SEO-titel skild från titeln → `seo{title}`. Meta null och SEO-titel lika med titeln → inget seo-objekt.
- Ändrades inte: handle, status, pris.
- Taggen `texter-klara` lades sist per batch (tagsAdd) efter att batchen verifierats. Inga userErrors. Befintliga taggar kvar (kontrollerat i jämförelsen: före-taggarna ingår i efter-taggarna).

## 4. Återläsning och jämförelse
- Efter varje batch lästes fälten tillbaka: title, handle, status, seo.title, seo.description, descriptionHtml, tags. Läsningen är svaret från productUpdate, som visar det Shopify lagrat.
- Jämförelsen gjordes maskinellt i python mot skrivfilen och före-läget (exakt likhet, tecken för tecken). Svaren överfördes till readback-filer i kopiamappen; överföringen gjordes för hand, och det är den som jämförs.
- Resultat: 43 av 43 produkter utan avvikelse. Ingen avbrottsorsak uppstod.
- Inte gjort: en separat slutläsning av alla 43 via graphql_query efter batch 5. Det är en möjlig extra kontroll.

## 5. Ändrat i Shopify
- JA. 43 produkter: title, seo (title och description), descriptionHtml och tagg `texter-klara` tillagd. Inget annat.

## 6. Övrigt
- En butikssökning på `tag:texter-klara` visade att fler produkter från tidigare vågor har taggen. Två av dem (10462782554378 och 10462856806666) har status DRAFT. De ingår inte i denna våg och ändrades inte. Det bör kontrolleras separat.
- Ingen commit gjord (uppdraget säger "Committa inte"). Beslutsfilen `rapporter/beslut-2026-11-03.md` enligt projektets CLAUDE.md skrevs inte; den bör göras av ansvarig.
