# Skrivrapport våg 2b, 14b (Best of Sports, cykelhjälmar)

Datum: 2026-11-03. Butik: BEST OF SPORTS (bestofsports.se), verifierad med get-shop-info.
Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/b_skriv_14b.json` (19 produkter).
Före-läge: `rapporter/shopify-original-2026-11-03/vag2b_14b_fore.json` (sparat före första skrivning).
Kontrollkopia: `rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2b14b/kopia_vag2b14b.json`.

## Live-läsning före skrivning
- 19 av 19 produkter ACTIVE. Ingen hade taggen `texter-klara`. Ingen hade titeln redan lika med skrivfilens titel.
- Ingen produkt hoppades över.
- Före-läget: titlar, seo.title (null på alla 19), seo.description (null på alla 19), descriptionHtml, taggar.

## Kontroll med kontrollera_produkttext.py (kopia, --meta-min 70, --seo-title-max 43, --seo-suffix " – BEST OF SPORTS")
- Resultat: 19 produkter, 0 FEL, 31 VARNINGAR. Skriptet avslutade utan fel.
- Varningar "saknar avsnittet 'passar dig som'": godkända (rubriken heter "Passar för").
- Varningar om engelska färgord i titel, SEO och text (`White`, `Blue`): 4 produkter, se nedan. Ej stoppande, men granskaren bör ta ställning.

## Skrivning
- Kanarie 3 produkter (10472291664138, 10472291762442, 10472292811018), sedan batcher om 5 (Shopify-dokument under 16 384 tecken, 877 tecken per dokument).
- Mutation och variabler skrevs ut av python-skript (ensure_ascii=True) och klistrades in oförändrade. Ingen text skrevs för hand.
- Inga userErrors i något anrop.
- Skriptet kontrollerade osynliga tecken (U+00AD m.fl.) före varje batch. Inga hittades.
- SEO skickades alltid som `seo{title, description}`, eftersom meta fanns för alla 19.

## Återläsning och jämförelse
- Varje batch lästes tillbaka (title, handle, status, seo.title, seo.description, descriptionHtml, tags).
- Jämförelsen gjordes maskinellt i python, tecken för tecken, mot skrivfilen. Handle och status jämfördes mot före-läget. Taggar jämfördes mot före-läget.
- Resultat: 0 avvikelser i alla fem återläsningar (3, 5, 5, 5, 1 produkter).
- För seo.title gäller regeln att Shopify lagrar null när SEO-titeln är identisk med produkttiteln. Det är avsett och godkänt i LARDOMAR.
- Maskinellt jämfört: alla fält i alla 19 produkter. Tecken för hand: inget. Återläsningen gjordes som API-svar som överfördes till fil och jämfördes.

## Taggar
- `texter-klara` lades på alla 19 med tagsAdd efter att allt var verifierat. Inga userErrors.
- Efterkontroll: alla befintliga taggar finns kvar på alla 19 produkter. Ingen annan tagg, status, handle eller pris ändrades.

## Före och efter
- Före: titel = leverantörens original (t.ex. "Hjälm CAIRN EON Matte Sand, beige"), seo null, descriptionHtml = leverantörstext.
- Efter: titel och SEO enligt skrivfilen, descriptionHtml enligt skrivfilen, taggen `texter-klara` tillagd.

## Avvikelser och att bekräfta
1. Engelska färgord kvar i titel/text (checkern varnar, ingen FEL): 10530129510666 (Gloss White), 10530132394250 (Gloss White), 10541106626826 (Irid Blue), 10577688363274 (Iridescent White). Standarden säger färg på svenska. Skrivfilen är skriven av granskarna och ändrades inte här.
2. Skrivfilen har 19 produkter. Det fanns inget 20:e id.

## Ändrat
- Shopify: ja, 19 produkter i butiken BEST OF SPORTS (titel, seo.title, seo.description, descriptionHtml och tagg `texter-klara`).
- Lokalt: fil `rapporter/shopify-original-2026-11-03/vag2b_14b_fore.json` (ny), kontrollkopia i `granskning/tmp_kopia_vag2b14b/` (ny), denna rapport (ny).
- Ingen commit gjord.

## Teknisk notis
- Scratchpad-mappen delades med andra körningar under passet. Skript i rotmappen skrevs över. Alla jämförelser och utskrifter gjordes med egna kopior i en egen undermapp, och varje körning kontrollerades mot skrivfilen.
