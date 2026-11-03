# Våg 2b, batch 11: skrivrapport (längdskidor Peltonen och solglasögon Limar)

Datum: 2026-11-03. Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info.
Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/b_skriv_11.json` (14 produkter).
Före-läge: `rapporter/shopify-original-2026-11-03/vag2b_11_fore.json` (sparat före första skrivning).

## Före och efter
- Antal produkter i filen: 14. Alla ACTIVE. Ingen hade taggen "texter-klara" och ingen hade titeln redan skriven. Ingen hoppades över.
- Efter skrivning: titel, SEO-titel, metabeskrivning och beskrivning är ändrade på alla 14. Handle, status och övriga taggar är oförändrade.
- Taggen "texter-klara" lades sist på alla 14 (tagsAdd), och befintliga taggar finns kvar.

## Kontroll
- Kontrollskript (`kontrollera_produkttext.py`, kopia med standardblock markerat, `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70`, källtext = före-läget): 0 FEL, 46 VARNINGAR. Varningarna är "passar dig som" (rubriken heter "Passar för", känd och godtagen) och engelska färgord (Black, Gray, Blue) som ingår i källans produktnamn. Inget fel stoppade skrivningen.
- Kanarie: 3 produkter, därefter batcher om 6 och 5. Samtliga mutationer gav tomma userErrors.
- Återläsning av alla 14 (titel, handle, status, seo.title, seo.description, descriptionHtml, tags): jämförd maskinellt i python mot skrivfilen och före-läget. 0 avvikelser.
- Taggarna kontrollerade med läsfråga efter tagsAdd: alla 14 har texter-klara och övriga taggar kvar.
- Skriptet bygger mutation och variabler ur skrivfilen; ingen text skrevs för hand. Skrivningarna kom från skriptets utskrift, och återläsningen verifierar lagrade värden mot filen.
- Fältet `seo.title` är null på de produkter där SEO-titeln är lika med produkttiteln. Det är Shopifys avsedda beteende. `seo.description` är satt på alla 14.

## Avvikelser
- Inga avvikelser i återläsningen.
- Peltonen-produkterna har bytt "Skridskor" till "Längdskidor" i titeln, enligt standardens avsnitt 16. Det är avsikten, inte en avvikelse.

## Att granska (ändrat inte, ligger i skrivfilen)
- Acadia SK 21 Medium (10472226685194) säger "Skidorna finns i två varianter" och Acadia SK 25 Stiff (10471008534794) säger "Skidorna finns i tre varianter" i metabeskrivningen. Standardens avsnitt 10 kräver att varianter inte låser vikt eller antal utan underlag. Frågan bör bekräftas innan den sprids.
- Solglasögontexterna innehåller UV- och skyddsuppgifter (till exempel "100 % UV-skydd upp till 400 nm" i Caos, "omslutande lins skyddar"). Jag har inte granskat dem mot faktatextlägets regler i avsnitt 16 på nytt; det är gjort i granskningssteget. Skrivningen har inte lagt till några påståenden utöver skrivfilen.

## Ändrat i Shopify
Ja. Titel, SEO-titel, metabeskrivning och beskrivning ändrades på 14 produkter med productUpdate. Taggen texter-klara lades till med tagsAdd på samma 14. Handle, status och pris ändrades inte.
