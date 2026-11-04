# Skrivrapport h_6 (BEST OF SPORTS, bestofsports.se), 2026-11-04

Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/h_skriv_6.json` (21 produkter, `skrivfil_kontroll.py`: 0 fel, 0 varningar)
Före-fil: `rapporter/shopify-original-2026-11-04/h_6_fore.json` (21 av 21 produkter, 22 535 tecken beskrivning, sparad före skrivning)
Live efter skrivning: `rapporter/facit-bos-2026-10-31/granskning/h_6_efter_live.json`

## Resultat
- Butik bekräftad med get-shop-info: BEST OF SPORTS, bestofsports.se.
- Alla 21 var ACTIVE och saknade taggen texter-klara före skrivning; ingen hoppades över. Före: SEO-titel och meta saknades på 20 av 21 produkter, 10598 hade SEO-titel och meta live (se nedan).
- Skrivet med skriptets utskrift oförändrad: kanarie 3 (10581, 10582, 10583), därefter 5 + 5 + 5 + 3 produkter. Alla anrop utan userErrors.
- Återläsning: kanarien lästes tillbaka separat, därefter alla 21 i grupper om högst 4 (title, handle, status, tags, seo.title, seo.description, descriptionHtml).
- Jämförelse med `jamfor_live.py <skrivfil> <livefil> --fore <forefil>`: **21 av 21 jämförda, 0 avvikelser** (title, SEO, meta, descriptionHtml tecken för tecken; handle och status oförändrade mot före-filen). Enda anmärkning från skriptet var "texter-klara saknas ännu", vilket gällde före taggningen.
- Beställningsmeningen kontrollerad maskinellt: finns på exakt 10587, 10590, 10592, 10597, 10598 och på ingen annan; alla fem har taggen "På beställning" live.
- Tagg texter-klara lades sist (tagsAdd, 5 + 5 + 5 + 5 + 1, inga userErrors). Slutkontroll: alla 21 har texter-klara, alla övriga taggar (Velomarket, Tunturi, Fell, Toorx, Hammer, På beställning m.fl.) finns kvar, handle och status oförändrade. Pris rördes inte.
- 10598: den tidigare SEO-titeln ("Motståndsband Tunturi Mini, set med 5 band") och metan ("... från 4,8 till 14 kg ...") ersattes helt av nya värden ("... Set med 5 Band" / ny meta utan kg-intervall).
- Jämförelse före/efter per produkt: titel, SEO och beskrivning finns i före-fil och live-fil ovan. Bildblock: inga bilder låg i beskrivningarna; däremot togs gammal "Om Tunturi"-text (10584, 10586, 10588, 10594, 10601 m.fl.), FAQ-liknande säljtext och produktkoder/EAN bort i beskrivningarna enligt skrivfilen. Handle som innehåller gamla ord (t.ex. "belt-" på 10583/10584) är oförändrade enligt regeln.

## Avvikelser
- Inga avvikelser i skrivningen eller jämförelsen.
- Före-filen fanns inte i repot vid start (sökvägen i uppdraget saknades). Jag hämtade live före skrivning och skrev filen. Eftersom MCP-verktyget inte kan spara till fil skrevs före- och efter-filerna ut av mig från verktygets svar (kopierade, inte omskrivna); jämförelsen mot skrivfilen visar 0 avvikelser, vilket också styrker att efter-filen är korrekt kopierad. Före-filen kan inte bevisas tecken för tecken mot live på samma sätt; den är endast kontrollerad på antal (21) och tecken-summa.

## Oklarheter i regler, prompt och skript
1. R16 säger "återläs högst 4", men uppdraget kräver att alla 21 jämförs; jag återläste alla i 6 anrop om högst 4. Regeln bör förtydligas till "högst 4 per anrop, alla ska återläsas".
2. `agentprompter.md` anger att resultatfiler ligger under `vag2_skriv/` eller `granskning/`, men före-filens plats (`rapporter/shopify-original-2026-11-04/`) står bara i uppdraget. Bör stå i prompten.
3. Det finns inget skript som sparar live-läsning direkt till fil; med MCP måste före- och efter-filerna skrivas för hand ur verktygssvaret (R16 förbjuder "text för hand" men det går inte att undvika här). Ett skript som kör nodes()-frågan via API och skriver JSON skulle ta bort den risken och göra före-filen verifierbar.
4. `b_skrivprompt.md` (historisk) säger 8 produkter per anrop och kanarie om 3; regelboken säger 5. Jag följde 3 + 5 enligt regelboken.
5. Live-handles som 10583 "belt-tunturi-arm-blaster" och 10593 "stretching-rubber-set..." stämmer inte med nya titlar. Handle ändrades inte (regel), men kan vara ett separat beslut om omdirigeringar.
