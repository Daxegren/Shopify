# Skrivrapport vågb 13b (28 cykellås), 2026-11-03

**Status: KLAR. Alla 28 skrivna, verifierade och taggade "texter-klara".**

Historik: skrivningen avbröts först efter batch 4 på grund av ett fel i 10635764269322 (min handtranskription, "neoprenöverdrag" i stället för "neoprenskydd"). Efter koordinatorns ja rättades 10635764269322 med skriptutskrift (mutation_13b.py 18 19), sedan skrevs batch 5 (8696–8701) och batch 6 (8702) med skriptutskrift, och alla återlästes.

## Slutverifiering (28 av 28)
- Python mot skrivfilen: title, status, seo.title, seo.description, descriptionHtml. 0 avvikelser.
- Undantag: seo.title är null för 8701 (10665232269578) eftersom SEO-titeln är lika med produkttiteln. Det är avsett enligt standarden.
- Osynliga tecken: inga hittades i skrivfilen eller i de återlästa texterna.
- Taggen "texter-klara" lades sist (tagsAdd, 28 av 28 utan userErrors). Återläsning: alla 28 ACTIVE, taggen finns och befintliga taggar är kvar.

## Ändrat i den historiska delen nedan
Avsnittet "Skrivning" och "Jämförelse" nedan beskriver läget efter batch 4. Det som står där om avbrott gäller inte längre.

## Före skrivning
- Butik: BEST OF SPORTS (bestofsports.se), verifierad med get-shop-info.
- Live-läge för alla 28 produkter lästes. Alla 28 var ACTIVE, ingen hade taggen "texter-klara" och ingen hade titeln från skrivfilen. Alla 28 skulle skrivas.
- Före-läget sparat i `rapporter/shopify-original-2026-11-03/vag2b_13b_fore.json` innan skrivning (28 poster, verifierat att filen läser in och innehåller 28 ACTIVE).

## Kontroll (kontrollera_produkttext.py, kopia)
- Kopia: `rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2b13b/kontroll_13b.json`. Standardblocket inslaget i [[STANDARDBLOCK]]. Källtext = före-läget (titel + beskrivning).
- Körning med `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70`.
- Resultat: 0 FEL, 28 VARNINGAR. Alla varningar är "saknar avsnittet 'passar dig som'", vilket är avsiktligt (rubriken heter "Passar för").
- Första körningen gav 12 FEL "tal_utan_kalla" (16, 230). Orsak: källfältet hade bara beskrivningen, inte originaltiteln. Kopian rättades så att källtexten innehåller originaltiteln. Därefter 0 FEL.

## Skrivning
- Mutation och variabler genererades av skript (`scratchpad/mutation_13b.py`) och klistrades in. Alla variabler i batch 1–3 och 4 är samma som skriptets utskrift, förutom att JSON-escapes (å o.s.v.) användes i stället för tecknen. Semantiskt identiskt.
- Kanarie (batch 1, 3 produkter): skrivna, userErrors tomma, återläst och jämfört.
- Batch 2 (6 produkter): skriven, userErrors tomma, återläst och jämförd. 0 avvikelser.
- Batch 3 (6 produkter): skriven, userErrors tomma, återläst och jämförd. 0 avvikelser.
- Batch 4 (6 produkter, index 15–20): skriven, userErrors tomma. Återläsning jämförd mot skrivfilen:
  - 5 av 6 utan avvikelse.
  - **10635764269322 (Kedjelås Squire Chainlok 10):** `seo.description` och `descriptionHtml` avviker. Skrivfilen: "neoprenskydd". Det som skrevs in: "neoprenöverdrag". Felet kom från min handtranskription av mutationen (skriptets utskrift hade "neoprenskydd"). Shopify har den felaktiga texten nu.
- Enligt reglerna rättas inte fel med nya handskrivna variabler. Skrivningen avbröts därför här.

## Jämförelse
- Maskinellt jämfört (python, `scratchpad/jamför_13b.py`): title, status, seo.title, seo.description, descriptionHtml för varje återläst produkt. Handle och övriga taggar har lästs men inte ändrats (kontrollerade i utskriften).
- Batch 5 (21–26) och batch 6 (27) är inte skrivna och inte återlästa.

## Taggar
- "texter-klara" är inte lagd på någon produkt. Av regel 5 följer att ingen tagg ska läggas förrän allt är verifierat. Befintliga taggar (t.ex. Velomarket, Cykellås) är kvar på alla skrivna produkter enligt återläsningen.

## Skrivna produkter (21 av 28, varav 20 OK)
| nr | id | status |
|---|---|---|
| 8671, 8673, 8674 | 10475619746058, 10475621155082, 10494701175050 | OK (kanarie) |
| 8675, 8676, 8678, 8679, 8680, 8681 | 10494702747914, 10494702911754, 10494704681226, 10530183414026, 10541139394826, 10541139919114 | OK |
| 8682, 8683, 8684, 8686, 8687 | 10541140279562, 10541168853258, 10541168951562, 10541368803594, 10541368934666 | OK |
| 8689 | 10548282196234 | OK |
| 8690 | 10572666175754 | OK |
| 8691 | 10572666208522 | OK |
| 8692 | 10635749064970 | OK |
| 8693 | 10635764269322 | **AVVIKELSE** (seo.description, descriptionHtml) |
| 8694, 8695 | 10635764400394, 10635764859146 | OK |

Ej skrivna: nr 8696–8702 (id 10656693846282, 10656693879050, 10656693911818, 10656693944586, 10656693977354, 10665232269578, 10665232302346).

## Beslut och nästa steg
1. **Rätta 10635764269322:** regenerera mutationen med skriptet (`mutation_13b.py 18 19`) och klistra in utskriften ordagrant. Verifiera sedan återläsningen. Kräver ditt ja, eftersom det är ett manuellt ingrepp i en avbruten batch.
2. **Fortsätt med batch 5 och 6** efter punkt 1. Gör en ny återläsning av batch 4 efter rättningen.
3. **Taggning** "texter-klara" först när alla 28 är verifierade.
4. **Orsak:** avbrottet beror på min handtranskription av en lång mutation. Lärdomen bör in i LARDOMAR.md (den filen rör jag inte utan ditt ja i den här sessionen).

## Ändrat
- Shopify: ja. 21 produkter skrivna (titel, seo, descriptionHtml). 1 av dem har felaktig text (se ovan). Inga taggar, handle eller status ändrade.
- Filer: före-fil, kontrollkopia, skrivrapport (denna fil), mutationsskript och jämförelseskript i scratchpad.
- Inget committat (enligt skrivprompten).
