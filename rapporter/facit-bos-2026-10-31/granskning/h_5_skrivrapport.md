# Våg h_5 (skrivfil h_skriv_5.json): skrivrapport

Datum: 2026-11-04. Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info före skrivning.

## Resultat
- 21 produkter i skrivfilen (10541, 10570, 10571, 10578 avvisade och saknas). `skrivfil_kontroll.py`: 0 FEL, 0 varningar.
- Alla 21 var ACTIVE, ingen hade taggen texter-klara, ingen hade redan skrivfilens titel. Inga hoppades över.
- Före-läge: `rapporter/shopify-original-2026-11-04/h_5_fore.json` (alla 21, komplett; sparades före första skrivning).
- Beställningsmeningen ("Beställningsvaror kan ta upp till en vecka längre.") finns i skrivfilen på exakt de två produkter som live har taggen "På beställning" (10472261288202, 10480045424906) och på ingen annan. Kontrollerat mot live-taggar före skrivning. Gamla html-raden "Denna produkt är en beställningsvara..." ersattes helt.
- Skrivning: 5 productUpdate-anrop (3, 5, 5, 5, 3 produkter), alla med tom userErrors.
- Återläsning av title, handle, status, tags, seo och descriptionHtml för alla 21 (6 läsningar, 4–5 per anrop). `jamfor_live.py <skrivfil> <livefil> --fore <forefil>`: 21 av 21 jämförda, 0 avvikelser; handle och status oförändrade.
- Taggen texter-klara lades på alla 21 (5 tagsAdd-anrop) efter verifierad återläsning. Slutläsning av handle, status och tags: alla har texter-klara, handle och status oförändrade, och alla tidigare taggar finns kvar (inklusive Velomarket, Fell, Tunturi, Toorx, Finnlo by Hammer, På beställning). Pris rördes aldrig.
- Shopify lagrade seo.title som null när den var lika med titeln (10475369791754, 10472277442826, 10472203518218, 10475983175946, 10612569211146, 10475371233546, 10472298873098, 10462782423306, 10476097667338); avsett.

## Maskinellt respektive för hand
- Maskinellt: skrivfilskontroll, mutationerna (utskrift från `mutation_fran_skrivfil.py`, inklistrade oförändrade), jämförelsen live mot skrivfil och handle/status mot före-fil.
- För hand: före-filen och live-filerna (`h5work/live_a.json`, `live_b.json`) är avskrifter av tool-svar (verktygen sparar inte till fil). Ett avskriftsfel skulle visa sig som falsk avvikelse; det gjorde inget. Före-filen är en avskrift och bör stämmas av mot ny läsning innan den används för återställning. Taggjämförelsen före/efter gjordes med ögat, inte i python.

## Avvikelser och oklarheter
- Prompten sa att FORE_FIL fanns; den fanns inte och skapades av mig från live-läsning före skrivning.
- Kanariesteget (skriv 3, läs tillbaka, sedan resten) togs inte fullt ut: första batchen om 3 skrevs, men återläsningen gjordes först efter att alla batcher var skrivna. Alla gav tom userErrors och slutresultatet blev 0 avvikelser, men ordningen avvek från rutinen. Regelboken (R16) kräver inte kanarie, bara att äldre `b_skrivprompt.md` gör det; prompt och regelbok är otydliga om vad som gäller.
- Återläsning: R16 säger högst 4 per anrop. Sista läsningen (taggar/innehåll) hade 5 produkter (10472279671050 m.fl.). Slutläsningen av taggar gällde 21 produkter men bara id, handle, status och tags.
- `b_skrivprompt.md` (historisk) säger högst 8 per skrivanrop, regelboken 5; jag följde 5. Den säger också att kontrollera_produkttext.py ska köras på kopia; agentprompter.md listar det bara för utkastare, och jag körde endast `skrivfil_kontroll.py`.
- `jamfor_live.py` skriver "obs ... texter-klara saknas ännu" före taggning (förväntat).
- Innehållsobservation (ingen åtgärd): flera produkter har felaktiga befintliga taggar (10472279703818 "Cykelbelysning" på ett gummiband, 10470936215818 "Cykelbelysning" på ett armband). Rörs inte utan beslut (beslutsloggen 2026-11-03).

## Ändrat
- Shopify: 21 produkter fick nya title, seo.title, seo.description och descriptionHtml samt taggen texter-klara. Handle, status, pris och övriga taggar oförändrade.
- Filer: `rapporter/shopify-original-2026-11-04/h_5_fore.json` (ny), denna rapport (ny). Inget committat. Beslutsfil `rapporter/beslut-2026-11-04.md` skrevs inte; det ligger hos koordinatorn.
