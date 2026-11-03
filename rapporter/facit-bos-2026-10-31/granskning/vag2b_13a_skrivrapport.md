# Skrivrapport: vag2b_13a (29 cykellås, Best of Sports)

Datum: 2026-11-03. Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/b_skriv_13a.json`. Före-läge: `rapporter/shopify-original-2026-11-03/vag2b_13a_fore.json`. Kontrollkopia: `rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2b13a/`.

## Status: AVBRUTEN vid batch 9–15 (avvikelse)

Skrivningen stoppades enligt regel 4 vid första avvikelsen. Ingen taggning (`texter-klara`) har gjorts. 14 av 29 produkter är inte skrivna.

## Butikskontroll
- `get-shop-info`: BEST OF SPORTS, bestofsports.se. Rätt butik.

## Före (live, läst innan skrivning)
- 29 av 29 produkter ACTIVE. Ingen hoppades över.
- Ingen produkt hade taggen `texter-klara`.
- Alla 29 titlar skilde sig från skrivfilen. Alla hade `seo.title` och `seo.description` = null.
- Före-läget sparat i FORE_FIL (29 poster, filen är giltig JSON).

## Kontroll av kopian (`kontrollera_produkttext.py`, `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70`)
- Resultat: 29 produkter, 0 FEL, 29 VARNINGAR.
- Alla varningar är "saknar avsnittet 'passar dig som'". Det är den godkända varningen (rubriken heter "Passar för").

## Skrivning och återläsning
| Batch | Produkter (skrivfilens index) | Skrivning | Återläsning och jämförelse |
|---|---|---|---|
| Kanarie | 0–2 (nr 8638, 8639, 8640) | Utan userErrors | Alla fält jämförda maskinellt mot skrivfilen: 0 avvikelser |
| 2 | 3–8 (nr 8641–8646) | Utan userErrors | Alla fält jämförda maskinellt mot skrivfilen: 0 avvikelser |
| 3 | 9–14 (nr 8647, 8648, 8650, 8651, 8652, 8655) | Utan userErrors | **AVVIKELSE** (se nedan). Övriga fem lästes tillbaka men jämfördes inte maskinellt |

**Avvikelse (nr 8647, id 10472233107722):** i `descriptionHtml` står "medföljande rem­mar" med ett osynligt mjukt bindestreck (U+00AD) i live. Skrivfilen har "medföljande remmar" utan det tecknet. Jämförelsen i python bekräftar detta. Orsaken är att jag överförde utskriften till mutationen för hand och kopierade in tecknet. Skriptutskriften var korrekt. Enligt regel 2 rättas inte felet med nya handskrivna variabler. Ingen annan del av produkten är bekräftat avvikande, men fältet `descriptionHtml` är inte godkänt.

Kanarie och batch 2 är helt verifierade. Batch 3 har skrivits och lästs tillbaka, men inte godkänts.

## Efter (läge nu)
- Skrivet i Shopify: 15 av 29 produkter (0–14). Verifierat maskinellt: 9 (0–8). Avvikelse: 1 (9). Ej jämfört: 5 (10–14).
- Ej skrivet: 14 produkter (15–28, nr 8656 och framåt i skrivfilen).
- Taggen `texter-klara`: 0 produkter. Taggarna i övrigt är oförändrade i läsningen.
- Handle och status: oförändrade i alla läsningar (ACTIVE).

## Hoppade över
- Inget av skäl enligt regeln (alla ACTIVE, ingen med taggen). 14 produkter hoppade inte över utan skrevs ej, eftersom processen avbröts.

## Att göra innan fortsättning
1. Återskriv produkt 10472233107722 från skriptutskriften (en produkt, `descriptionHtml`), och läs tillbaka. Det är en beslutsfråga för David eller huvudagenten eftersom regeln förbjuder rättning med handskrivna variabler.
2. Jämför de fem olika produkterna i batch 3 maskinellt (10–14).
3. Fortsätt med resterande batcher (15–28) först efter att punkt 1 och 2 är klara.
4. Tagga först när allt är verifierat.

## Ändrat
- Shopify: productUpdate på 15 produkter (title, seo, descriptionHtml). Handle, status, pris och taggar är inte ändrade. Ingen tagg satt.
- Filer: `rapporter/shopify-original-2026-11-03/vag2b_13a_fore.json` (ny), denna rapport (ny), tre kontrollfiler under `tmp_kopia_vag2b13a/` (nya).
