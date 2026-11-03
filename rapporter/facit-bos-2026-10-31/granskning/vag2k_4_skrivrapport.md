# Våg 2k4 (cyklar, skrivfil k_skriv_4.json): skrivrapport

Datum: 2026-11-03. Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info före skrivning.

## Resultat
- 12 produkter i skrivfilen. Alla var ACTIVE, ingen hade taggen texter-klara och ingen hade titeln redan skriven. Inga hoppades över.
- Före-läge sparat: `rapporter/shopify-original-2026-11-03/vag2k_4_fore.json` (sparades före första skrivning).
- Kontrollskript (`kontrollera_produkttext.py`, på kopia `rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2k4/vag2k4_kopia.json`, html mappad till beskrivning, standardblocket inom `[[STANDARDBLOCK]]`, `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS"`, källtext = före-läget): 0 FEL, 16 VARNINGAR. Varningarna: "passar dig som" (rubriken heter "Passar för", godtaget) på 12 produkter, och "White" som engelskt ord i titel, SEO och text för 10476124012810 (Illusion White, en färgbeteckning från tillverkaren). Den sistnämnda är inte en av de godtagna varningarna och redovisas här för beslut. Den skrevs ändå, eftersom den är en varning och inget FEL.
- Skrivning i tre batcher: kanarie 3 (10471017414922, 10471335461130, 10471336116490), sedan 6 (10472322138378 t.o.m. 10476128403722), sedan 3 (10487987667210, 10565633507594, 10624088572170). Alla productUpdate gav tom userErrors.
- Tillbakaläsning av title, handle, status, seo.title, seo.description och descriptionHtml för alla 12, jämförd maskinellt (python) mot skrivfilen och före-läget: 0 avvikelser i alla tre batcher. Handle och status oförändrade.
- Taggen texter-klara lades på alla 12 efter verifiering av respektive batch. En sista läsning av taggar visar att alla 12 har texter-klara och att befintliga taggar finns kvar.

## Vad som kontrollerats maskinellt och vad som inte gjorts för hand
- Maskinellt: kontrollskriptet; jämförelse av tillbakaläsning mot skrivfil och före-läge (python); att alla före-taggar finns kvar.
- Mutationerna genererades av `/tmp/claude-0/-home-user/fbbd95a3-8b18-5096-a6b5-20df3e4eb235/scratchpad/vag2k4/bygg.py` från skrivfilen. Utskriften klistrades in ordagrant.
- För hand: före-filen och tillbakaläsningsfilerna (`aterlas_1..3.json` i scratchpad) skrevs av mig från tool-svar, eftersom verktygen inte sparar svaren till fil. Jämförelsen är maskinell, men själva filerna är en avskrift. Eventuella tecken-fel i avskriften skulle synas som avvikelse i jämförelsen, men inte i själva Shopify-svaret. Före-filen är därför en avskrift, och den bör stämmas av mot en ny läsning innan den används för återställning.

## Avvikelser och noteringar
- Prompten kallar produkterna "Gymstick", men skrivfilen innehåller cyklar (Kona, Giant, Liv). Arbetet följde skrivfilen.
- Produkten 10476124012810 har "Illusion White" i titeln och SEO-titeln ("White" är engelska). Se varningen ovan.
- Shopify returnerade inga radbrytningsskillnader i descriptionHtml. Ingen seo.title blev null.

## Ändrat
- Shopify: 12 produkter fick nya title, seo.title, seo.description och descriptionHtml. Taggen texter-klara lades till. Handle, status, pris och övriga taggar är oförändrade.
- Filer: `rapporter/shopify-original-2026-11-03/vag2k_4_fore.json` (ny), `rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2k4/vag2k4_kopia.json` (ny), denna rapport (ny). Inget committat.

## Öppet
- Beslutsfilen `rapporter/beslut-2026-11-03.md` enligt CLAUDE.md har inte skrivits. Instruktionen var "committa inte", och CLAUDE.md säger att filen committas och pushas. Det behöver avgöras.
- Varningen "White" (se ovan) behöver beslut från David.
