# Fullständig återläsning av skrivna texter, BEST OF SPORTS, 2026-11-17

Endast läsning. Inget skrevs i Shopify eller i någon annan butik, tema, Search Console, Analytics eller Ads. Windsor.ai användes inte. Butiken verifierades före läsningen (API-svaret kom från BEST OF SPORTS, `6f2e53-67.myshopify.com`). Nycklar lästes ur miljön och sparades aldrig.

Obs: uppdraget nådde sessionen som ett automatiskt meddelande som återger Davids ja från 2026-11-12. Jag kunde inte kontrollera citatet mot något i den här konversationen; eftersom allt var läsning gjordes körningen ändå. Ja:et finns inte som rad i `BESLUTSLOGG.md`.

## 1. Underlaget

| Mängd | Antal | Hur den byggdes |
|---|---|---|
| Produkter med senast avsedd text i en skrivfil | 3 086 | Alla `*skriv*.json` i `rapporter/facit-bos-2026-10-31/vag2_skriv/` (218 filer). 705 produkter finns i fler än en fil; 287 av dem har skilda texter i filerna |
| Produkter med taggen texter-klara men utan skrivfil | 105 | Egen kategori, bedöms mot regelboken (avsnitt 4) |
| Lästa live | 3 191 | 3 086 + 105; inga saknades i butiken |

Ordningen mellan flera skrivfiler för samma produkt bestäms av resultatfilernas tidsstämplar (131 av 218 skrivfiler har sådana), rättningsfiler (`korr`) räknas som senast. Filernas ändringstid och git-datum går inte att använda (en ny kopia ger alla filer samma tid). För 252 produkter med skilda texter i flera filer saknas tidsstämpel för minst en fil; där stämmer live med den fil som bedömts som senast, men ordningen är inte bevisad. De räknas som identiska men redovisas separat.

## 2. Läsningen: tid och rate limit

- Prov: 20 produkter på 0,8 s (2 läsanrop, tio produkter per anrop, plus ett anrop som verifierar butiken). Därefter alla: 3 191 produkter i 319 anrop på 101,8 s, i snitt 0,32 s per anrop (längsta 0,98 s).
- Rate limit: 0 svar med HTTP 429, inga omförsök, ingen paus behövdes. Shopifys kostnadsbudget är 2 000 poäng med återställning 100 per sekund; lägsta kvarvarande nivå var 1 998. Gränsen 10 produkter per anrop följdes (rutinens gräns för API-vägen; "högst 4" i R16 gäller chatt-kopplingen).

## 3. Resultat för de 3 086 skrivna produkterna

Jämförelsen gäller titel, SEO-titel, SEO-beskrivning och beskrivning, tecken för tecken mot senast avsedd text.

| Klass | Antal |
|---|---|
| Identisk | 3 060 |
| Ersatt av en senare omskrivning (rensning 1: 24, kort meta: 1) | 25 |
| Ändrad efteråt av leverantörssynken eller annan automatik (återställd till leverantörens text, eller ändrad natt efter utrullningens slut) | 0 |
| Avviker utan känd orsak | 1 |

Detaljer:
- **Rensning 2** (178 produkter, "(enligt tillverkaren)" på lastgräns) räknas inte som avvikelse: dess skrivfil `k_skriv_rens2.json` är senast avsedd text och alla 178 stämmer med den. De som ligger kvar i identisk-raden har alltså rensning 2 live.
- **Rensning 1** (24 produkter): live-metan är den rensade (utan "Finns hos BEST OF SPORTS."), som beslutat 2026-11-04. **Kort meta** (1 produkt): live-metan är den senare korta metan.
- **1 produkt är identisk efter ett Shopify-undantag:** `&` i skrivfilen lagras som `&amp;` i butiken (10494701109514, Basil Keep Dry & Clean).
- **Den enda oförklarade avvikelsen:** 10507302764810 (Finnlo by Hammer Tricon Flex, nr 10348), spärrad pilotprodukt. Live är pilottexten (SEO-titel 60 tecken med " | Best of Sports", metabeskrivning 145 mot avsedda 133 tecken, beskrivning 1 527 mot 1 247). Det är samma läge som redovisades 2026-11-12: skrivfilernas text har aldrig nått butiken. Nytt sedan dess: produkten ändrades 2026-11-13 11:36 UTC (taggarna `price-change-job-active`, `sale`, `sync-skydd`); texten är densamma. Ingen känd överträdelse och ingen regression, men orsaken till ändringen 11-13 är inte styrkt.
- **Status och taggar:** 3 068 aktiva, 16 arkiverade, 2 utkast (nattkontrollen 2026-11-06 räknade 64 ej aktiva). Alla 3 086 har taggen texter-klara. Texten är identisk även på de 18 som inte är aktiva.
- **Metabeskrivning:** 120 produkter har en äldre skrivfil utan meta, så metan kunde inte jämföras. Live har 4 av dem ingen meta och 7 en meta under 70 tecken (listade i `forslag_korrigeringsfil.csv`).
- **Ändringstid utan textändring:** 1 929 av 3 086 produkter har `updatedAt` efter 2026-11-12 (1 626 den 16 november kl. 03–07 UTC, 298 den 13 november kl. 11 UTC), men ingen text skiljer sig. 1 698 produkter bär taggen `price-change-job-active`, och alla 1 698 ligger i den gruppen. Hypotes (obekräftad): ett prisjobb ändrade produkterna, inte texterna.
- **Kontroll av metoden:** skriptet jämfördes med det äldre `jamfor_live.py` på fyra skrivfiler (`k_skriv_08bcd`, `b_skriv_10`, `k_skriv_28npq`, `f_skriv_14`). De första tre gav 0 avvikelser i båda verktygen. `f_skriv_14` gav 19 avvikelser i det äldre verktyget (18 beror på rensning 2, 1 på 10348), vilket stämmer med klassningen.

## 4. Produkter med texter-klara men utan skrivfil (105)

Status i butiken: 92 aktiva, 12 utkast, 1 arkiverad. 103 bär taggen Velomarket, 17 `sync-skydd`, 13 `På beställning`. Kontrollerna är `skrivfil_kontroll.py` och `regeltester.py`, körda på live-texterna; allt redovisas som varningar. Spärrlistan nämns separat.

| Fynd | Produkter |
|---|---|
| Cirkulär inledning ("X är en X") i meta eller första meningen | 76 |
| Saknad metabeskrivning | 24 |
| Standardblocket saknas | 0 |
| På beställning utan leveranstidsmening | 9 |
| "Enligt tillverkaren" fler än två gånger | 1 |
| SEO-titel över 43 tecken | 15 |
| FAQ-avsnitt eller "Om märket" (pilotens gamla textmall) | 41 |
| Dubbla mellanslag | 24 |
| Engelskt typord, kvalitetsord utan "enligt tillverkaren" (regeltester) | 7 respektive 12 |
| Spärrad produkt (pilot-20), förväntat | 16 |

94 av 105 har minst en varning. 85 har en varning i någon av kategorierna ur uppdraget (cirkulär inledning, mer än två "enligt tillverkaren", saknad meta, standardblocket, leveranstid), varav 11 är spärrade pilotprodukter som inte ska ändras utan beslut. Förslaget till korrigeringsfil (`forslag_korrigeringsfil.csv`) har 85 rader: de 74 utan de spärrade plus de 11 produkterna ur avsnitt 3 med saknad eller för kort meta.

## 5. Tio exempel i klartext

1. **10507302764810 (Finnlo Tricon Flex), oförklarad:** live SEO-titel "Träningsbänk Finnlo Tricon Flex, Hopfällbar | Best of Sports"; avsedd "Träningsbänk Finnlo Tricon Flex Hopfällbar".
2. **10494701109514 (Basil Keep Dry & Clean), identisk efter Shopify-normalisering:** skrivfil "Basil Keep Dry & Clean är ett regnskydd…", live "Basil Keep Dry &amp; Clean är ett regnskydd…".
3. **10472328691978 (Toorx Olympic Barbell), ersatt av rensning 1:** live-meta "Toorx Olympic Barbell är en skivstång på 220 cm som väger 20 kg och används med 50 mm viktskivor."; skrivfilen hade samma mening följd av " Finns hos BEST OF SPORTS."
4. **10472253292810 (Selle Monte Grappa 156), ersatt av kort meta:** skrivfilen saknar meta; live-meta "Selle Monte Grappa 156 är en svart sadel med överdrag i polyuretan. Sadeln är 275 x 215 mm och väger 450 g."
5. **10470907412746 (ADO Air 28 PRO), rensning 2:** live stämmer med `k_skriv_rens2.json` och är därmed identisk.
6. **10411771363594 (Träningsmatta Tunturi NBR, 15 mm, Grå), utan skrivfil:** meta "Tunturi NBR är en träningsmatta i NBR-gummi…" (cirkulär inledning) och taggen `På beställning` utan leveranstidsmeningen "Beställningsvaror kan ta upp till en vecka längre."
7. **10462190240010 (Massagerulle Tunturi Yoga Grid Foam Roller), utan skrivfil:** metabeskrivning saknas (null); första meningen cirkulär.
8. **10439135691018 (Pilatesring Tunturi), utan skrivfil:** cirkulär inledning och `På beställning` utan leveranstidsmening.
9. **10472220197130 (rensning 1), ARCHIVED men text kvar:** texten är den rensade även på arkiverade produkter.
10. **10530126266634, 10581105869066, 10581109408010, 10581109670154:** live stämmer med rättningsfilerna `k_skriv_korr8–10`, inte med de äldre `k_skriv_28st`/`32cde`/`32fgh`; räknas som identiska eftersom rättningsfilerna är senast avsedda.

## 6. Filer

- `aterlasning_skrivna.csv`: 3 086 rader (produkt-id, status, avvikelsetyp, avvikande fält, senast avsedd skrivfil, status i butiken, taggen texter-klara, senast ändrad).
- `aterlasning_utan_skrivfil.csv`: 105 rader med varningar.
- `forslag_korrigeringsfil.csv`: 85 rader, förslag till åtgärd (inga nya texter; de ska utkastas ur produktens egen källa enligt rutinen).
- `siffror_klassning.json`, `siffror_utan_skrivfil.json`.
- Skript: `shopify-sync/scripts/aterlasning_bos.py` (bara läsande).

## 7. Begränsningar

- Jämförelsen avgör vad som ligger i butiken nu, inte när eller av vem något ändrats. Klassen "ändrad av synk" bygger på två tecken: texten är lika med leverantörens ursprungstext, eller produkten ändrades kl. 03–04 UTC efter 2026-11-08. Inga produkter föll i den klassen.
- 252 produkter har skilda texter i flera skrivfiler utan tidsstämpel för alla; live stämmer med en av dem (se avsnitt 1).
- De 105 produkterna utan skrivfil kan bara bedömas mot regler, inte jämföras tecken för tecken.
