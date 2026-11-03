# Våg 2b, grupp 16 (25 elcyklar och cyklar), skrivrapport

Datum: 2026-11-03. Butik: BEST OF SPORTS (bestofsports.se), verifierad med get-shop-info.
Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/b_skriv_16.json` (25 produkter).
Före-läge: `rapporter/shopify-original-2026-11-03/vag2b_16_fore.json` (25 produkter, sparat före skrivning).
Kontrollkopia: `rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2b16/` (kopia.json, kontroll.txt).

## Status: klar

Alla 25 produkter är skrivna, verifierade och taggade med texter-klara.

## Före skrivning
- Alla 25 var ACTIVE, ingen hade taggen texter-klara och ingen hade en titel lika skrivfilen.
- Inga produkter hoppades över. Inga avvikelser mot skrivfilen.

## Kontroll (kontrollera_produkttext.py)
Kopia med html mappad till beskrivning, standardblocket markerat med [[STANDARDBLOCK]], källtext = före-läget, `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70`.
Resultat: 0 FEL, 25 VARNINGAR. Alla varningar är "saknar avsnittet 'passar dig som'", den godtagna rubrikvarningen.

## Skrivning
- Kanarie 3 produkter (8747–8749), därefter batcher om 5 (8750–8754, 8755–8760, 8761–8766, 8767–8772) och 2 (8773–8774).
- Mutationen och variablerna skrevs ut av `scratchpad/bygg_b16.py` (ensure_ascii=True) och klistrades in ordagrant. Inga variabler skrevs för hand.
- Varje productUpdate sände title, seo{title, description} (båda fälten, eftersom alla 25 har meta) och descriptionHtml. Handle och status ändrades inte.
- Sex produkter har SEO-titel lika med titeln (nr 8753, 8754, 8762, 8767, 8772, 8773). Shopify lagrar seo.title som null för dem. Det är avsett, och metabeskrivningen finns kvar.

## Verifiering (maskinell, i python mot skrivfilen och före-läget)
- Efter varje batch lästes alla fält tillbaka. Svaren sparades till fil, så jämförelsen kördes i python: title, handle, status, seo.title, seo.description, descriptionHtml (två kopior per produkt) och taggar, samt kontroll av U+00AD.
- Resultat per batch: kanarie 3/3, batch 5/5, batch 5/5, batch 5/5, batch 5/5 samt batch 2/2 utan avvikelser.
- Slutläsning av alla 25 efter tagging: taggerna är före-läget plus texter-klara och inget annat har ändrats. Inga avvikelser och inget U+00AD.
- Läsningarna är gjorda med flera kopior av descriptionHtml-fältet, eftersom svaren annars visas i chatten och inte kan jämföras maskinellt. Datat är oförändrat.

## Taggar
- texter-klara lades sist med tagsAdd på alla 25. Inga userErrors. Befintliga taggar finns kvar (verifierat i slutläsningen).

## Ändrat i Shopify
Ja: title, seo (title och description), descriptionHtml och taggen texter-klara på 25 produkter (8747–8774 enligt skrivfilen). Inget annat ändrades: handle, status, pris och övriga taggar är oförändrade.

## Att notera
- Skrivningen är gjord enligt prompten. Ingen commit gjordes.
- Beslutsfilen `rapporter/beslut-2026-11-03.md` enligt CLAUDE.md skrivs av huvudagenten, inte av denna skrivning.
