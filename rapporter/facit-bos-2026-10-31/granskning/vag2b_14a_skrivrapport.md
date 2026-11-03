# Våg 2b, grupp 14a (hjälmar, 19 produkter): skrivrapport

Datum: 2026-11-03. Butik: BEST OF SPORTS (bestofsports.se), verifierad med get-shop-info före skrivning.
Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/b_skriv_14a.json`. Före-läge: `rapporter/shopify-original-2026-11-03/vag2b_14a_fore.json`. Kontrollkopia: `rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2b14a/` (`kopia.json`, `kontroll.txt`).

## Urval
- 19 produkter i skrivfilen (nr 8703–8726, ids i skrivfilen). Alla 19 var ACTIVE och hade inte taggen `texter-klara`. Inga hoppades över. Ingen hade redan skrivna titlar.
- Live-läget ("före") lästes och sparades i FORE_FIL innan någon skrivning.

## Kontroll före skrivning
`kontrollera_produkttext.py` på kopia (html som beskrivning, standardblock inom `[[STANDARDBLOCK]]`, `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70`, källtext = före-läget):
- **0 FEL.** Körningen godkänd.
- **32 VARNINGAR**, alla kända eller godtagna:
  - 19 st "saknar avsnittet 'passar dig som'". Rubriken heter "Passar för", avsiktligt enligt standarden.
  - 12 st `engelska_ord` (Blue, Black, Pink; titel, SEO, meta, beskrivning) för färg- och modellnamn ur källan, t.ex. "Matt Steel Blue", "Black Ice", "Shiny Powder Pink".
  - 1 st `beskrivning_langd` för 10472238973194 (Kamerafäste Lazer Impala): 34 ord, under förväntade 40. Källan är tunn; texten är kort och påstår inget extra. Godtagen.

## Skrivning
- Kanarie 3 produkter (8703–8705), sedan batcher om 5 (8708–8713 med 5, 8714–8720 med 5, 8721–8725 med 5) och sist 8726 ensam.
- Mutation och variabler skrevs ut av `skriv_batch.py` (ensure_ascii=True, inga osynliga tecken, under 16 384 tecken). Utskriften klistrades in ordagrant. Ingen text skrevs för hand.
- `productUpdate(product: ...)` med `title`, `seo{title, description}` och `descriptionHtml`. Samtliga 19 hade meta, så seo skickades med båda fälten, även där seo-titeln var lika med titeln (8726).
- Handle och status skickades inte. Inga fel i userErrors.

## Återläsning och jämförelse
- Efter varje batch lästes title, handle, status, seo.title, seo.description, descriptionHtml och tags tillbaka med `nodes(ids:)`.
- Jämförelse i python (`jamfor.py`) mot skrivfilen och före-filen: title, handle, status, seo.title (null där seo-titeln är lika med titeln, annars skrivfilens värde), seo.description, descriptionHtml (exakt, tecken för tecken), tags (före-taggarna kvar), osynliga tecken (U+00AD, nollbreddstecken).
- **Resultat: 19 av 19 OK, inga avvikelser.** Inga avbrott.
- Begränsning: återläsningens svar fördes över till filer för jämförelsen. Jämförelsen är alltså maskinell mot den kopian, men kopian skrevs för hand av det svar som kom tillbaka. Tecken-för-tecken-kontrollen mot skrivfilen gjordes i python, inte av ögat.

## Taggen texter-klara
- `tagsAdd(texter-klara)` lades sist, på alla 19, först efter att allt var verifierat.
- Efter taggningen lästes taggarna tillbaka. Alla 19 har `texter-klara`. Övriga taggar finns kvar (kontrollerat för alla 19).

## Före och efter (titel)
| nr | id | före (titel) | efter (titel) |
|---|---|---|---|
| 8703 | 10461421207818 | Hjälm CAIRN EON, Matt Svart Agatgrå | Hjälm Cairn EON, Matt Svart Agatgrå |
| 8704 | 10462126604554 | Bicycle helmet LIMAR 778 | Cykelhjälm Limar 778, Blå |
| 8705 | 10462190731530 | Hjälm LAZER ONE+, Matt Vit | Hjälm Lazer One+, Matt Vit |
| 8708 | 10462231429386 | Hjälm LIMAR Pora, Matt Svart Titan | Hjälm Limar Pora, Matt Svart Titan |
| 8710 | 10462761484554 | Winter content for MELON helmets | Vinterkit Melon för Hjälmar, Öronlappar och Nackskydd |
| 8711 | 10462818500874 | Hjälm LIMAR Urbe, Matt Svart | Hjälm Limar Urbe, Matt Svart |
| 8712 | 10470913900810 | Hjälm LIMAR Scrambler, Blå Svart 21 | Hjälm Limar Scrambler, Blå och Svart |
| 8713 | 10471004700938 | Cykelhjälm LIMAR Berg-Em, Matt Steel Blue | Cykelhjälm Limar Berg-Em, Matt Steel Blue |
| 8714 | 10471008272650 | Hjälm MELON E-Series, Black Ice | Hjälm Melon E-Series, Black Ice |
| 8715 | 10472233959690 | Bicycle helmet LIMAR 848DR | Cykelhjälm Limar 848DR, Matt Ljusgrön |
| 8717 | 10472237138186 | Cykelhjälm LIMAR Berg-Em, Matt Mörk Röd | Cykelhjälm Limar Berg-Em, Matt Mörk Röd |
| 8719 | 10472238973194 | Kammarfäste för hjälm LAZER Part Impala Action Camera mount set | Kamerafäste för Hjälm Lazer Impala, Set för Actionkamera |
| 8720 | 10472258601226 | Hjälm CAIRN EON Shiny Powder Pink, rosa | Hjälm Cairn EON, Shiny Powder Pink, Rosa |
| 8721 | 10472261255434 | Helmet MELON Real Melon | Hjälm Melon Real Melon |
| 8722 | 10472262140170 | Helmet MELON Paris | Hjälm Melon Paris |
| 8723 | 10472262172938 | Helmet MELON Rio | Hjälm Melon Rio |
| 8724 | 10472266006794 | Bicycle helmet LIMAR 888 | Cykelhjälm Limar 888, Matt Vit |
| 8725 | 10472267383050 | Bakljus för GIANT Numen Alumbra-hjälm | Bakljus Giant Numen Alumbra med Magnetfäste |
| 8726 | 10472288092426 | Hjälm LIMAR Air Star, Matt Svart | Cykelhjälm Limar Air Star, Matt Svart |

Handle är oförändrat för alla 19 (kontrollerat).

## Hoppade över
Inga.

## Avvikelser
Inga. Ingen återläsning avvek från skrivfilen. Ingen rättning gjordes. Inga produkter avbröts.

## Att notera
- SEO-titeln för 8726 lagras som null i Shopify, eftersom den är lika med produkttiteln. Det är avsett.
- Återläsningen gav descriptionHtml identisk med det som skickades, för alla 19 (inga tillagda radbrytningar i denna batch).
- Helmerna och övriga säkerhetsprodukter i gruppen är frisläppta i faktatextläge (standarden avsnitt 16). Texterna innehåller inga säkerhets- eller skyddspåståenden utan "enligt tillverkaren".

## Ändrat
- Shopify: ja. `productUpdate` (title, seo, descriptionHtml) på 19 produkter, `tagsAdd` med `texter-klara` på samma 19. Ingen handle, status, pris eller annan tagg ändrades.
- Lokalt: `rapporter/shopify-original-2026-11-03/vag2b_14a_fore.json` (ny fil), `rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2b14a/` (ny kontrollkopia), denna rapport. Ingen commit.
