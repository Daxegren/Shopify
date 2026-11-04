# Grupp g_2 (Tunturi/Toorx, fitness): skrivrapport

Datum: 2026-11-04. Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info före skrivning. Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/g_skriv_2.json` (22 produkter; 10477, 10478 och 10491 är avvisade och ingår inte). Före-fil: `rapporter/shopify-original-2026-11-04/g_2_fore.json`.

## Resultat
- 22 av 22 skrivna. Alla var ACTIVE, ingen hade taggen texter-klara. Inga hoppades över.
- R15: tre produkter hade redan rätt titel (10472299069706, 10472265154826, 10462775771402). Beskrivning och meta skilde sig mot skrivfilen på alla tre (och SEO-titeln var redan lika), så de skrevs. 10462775771402 hade dessutom gammal FAQ ("Vanliga frågor") och "Om märket" som nu är ersatta helt.
- Beställningsmeningen ("Beställningsvaror kan ta upp till en vecka längre.") finns på alla 19 produkter med taggen "På beställning" och på ingen av de 3 utan taggen. Kontrollerat maskinellt före skrivning och i återläsningen.
- `skrivfil_kontroll.py` på skrivfilen: 0 FEL, 0 varningar.
- `kontrollera_produkttext.py` på kopia (`g2work/g2_kopia.json`, standardblocket inom `[[STANDARDBLOCK]]`, källtext = före-läget, `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70`): 0 FEL, 24 VARNINGAR. 22 är "saknar avsnittet 'passar dig som'" (rubriken heter "Passar för", godtaget). 2 är `beskrivning_langd` för 10472289141002 (38 ord) och 10472299069706 (32 ord): produkterna har så lite källtext att beskrivningen blir kort; godtaget, inget utfyllnad.
- Skrivning i fem anrop: kanarie 3 (10472288551178, 10472288583946, 10494913347850), sedan 5, 5, 5 och 4. Alla productUpdate gav tom userErrors.
- Återläsning av title, handle, status, tags, seo.title, seo.description och descriptionHtml för alla 22, högst 4 per fråga, jämförd i python mot skrivfilen och före-läget: 0 avvikelser (title, seo.description och descriptionHtml tecken för tecken; seo.title där den är lika med titeln lagras som null, vilket är avsett; handle och status oförändrade; taggar oförändrade). Återläsningsfilerna `aterlas_1..5.json` ligger i `g2work/`.
- Tagg texter-klara lades till sist på alla 22 efter att alla batcher var verifierade (två anrop med tagsAdd, tom userErrors). Svaren visar att alla tidigare taggar, inklusive Velomarket och Gymstick, finns kvar (jämfört i python mot före-filen: 22 av 22).

## Vad som kontrollerats maskinellt och vad för hand
- Maskinellt: de två kontrollskripten; jämförelse av återläsning mot skrivfil, handle, status och taggar (python); osynliga tecken (U+00AD, nollbreddstecken) i alla fält före varje mutation (skriptet `bygg.py` avbryter om sådana finns).
- Mutationerna genererades av `g2work/bygg.py` (ensure_ascii) och klistrades in ordagrant. Inga handskrivna variabler.
- För hand: före-filen och återläsningsfilerna är avskrifter av verktygssvar (verktyget sparar inte svar till fil). Ett tecken-fel i avskriften skulle ha synts som falsk avvikelse, men inte i själva Shopify-svaret. Före-filen bör stämmas av mot en ny läsning om den används för återställning. Före-filen innehåller inte metafält (seo) som null-skillnad utöver det som visas.

## Avvikelser och noteringar
- Batchstorlek: skrivprompten säger högst 8 produkter per anrop, regelboken R16 säger högst 5. Jag följde R16 (3, 5, 5, 5, 4).
- Meta-minimum: `kontrollera_produkttext.py` har standard `--meta-min 130`, regelboken R12 säger 70–155. Med standardvärdet blir 14 produkter FEL på metalängd. Jag körde med `--meta-min 70`. 
- Meta för 10472299069706 (Toorx-mattan) slutar med "Finns hos BEST OF SPORTS." Det är utfyllnad i meta och strider mot R12 ("meta utan utfyllnad"). Skrivfilen passerade ändå skripten. Skrevs som den är (inte mitt att ändra); granskare/koordinator bör avgöra om den ska rättas.
- Tre produkter (10472299069706, 10472265154826, 10462775771402) hade redan en tidigare skriven text (pilotens eller våg 1:s), inte tillverkarens ursprungstext, som live-"källa". Skrivfilens fakta hämtades alltså från en text som i sin tur var skriven. Den sista, 10462775771402, får "Enligt tillverkaren är mattan halkfri" (R5) med grund bara i den tidigare skrivna texten. Koordinatorn bör bekräfta att originalkällan stöder det.
- 10472288551178 (MSX-3000): källan hade "Maximal vikt: 90 kg" och "Maximal driftsvikt: 150 kg"; båda är utelämnade i skrivfilen enligt Alt A/R4. Likaså engelska lastgränser på 10472330068234 (SS60). Skrivfilen följer det.
- 10673174741258 (SM70): källan hade "2 x J-hooks" två gånger; skrivfilen anger "J-hooks" utan antal. Avsett enligt R2.
- Produktnamn: Toorx-titlarna ändrades från "Power station" till "Powerstation", och "Half Rack" till "Halvställ", "Squat stand" till "Skivstångsställning". R7 säger byt typord bara om produktens egen källtext använder det nya ordet; "Powerstation", "halvställ" (HR60) och "skivstångsställning" finns i källtexten eller taggar ("Skivstångsställning" som tagg på SS60). "Halvställ" finns i källan ("halvstället"). Jag har inte ändrat dessa, bara noterat dem.
- Inget ändrat i Shopify utöver title, seo.title, seo.description, descriptionHtml och taggen texter-klara. Handle, status, pris, övriga taggar och varianter är orörda.

## Ändrat
- Shopify: 22 produkter fick nya title, seo, descriptionHtml och taggen texter-klara.
- Filer: `rapporter/shopify-original-2026-11-04/g_2_fore.json` (ny), denna rapport (ny), arbetsfiler i `/tmp/claude-0/-home-user/fbbd95a3-8b18-5096-a6b5-20df3e4eb235/scratchpad/g2work/`. Inget committat.

## Förbättringsförslag till regelboken och prompten
1. Prompten (`b_skrivprompt.md`) och R16 säger olika om batchstorlek (8 respektive 5). Ange ett tal, helst i regelboken, och hänvisa dit från prompten.
2. `kontrollera_produkttext.py` har meta-min 130 som standard, regelboken säger 70. Sätt 70 som standard (eller läs värdet ur butiksprofilens `gransvarden`) så att FEL inte uppstår av fel inställning. Samma sak för `--seo-title-max 43 --seo-suffix`: läs dem ur profilen.
3. `b_skrivprompt.md` hänvisar till `CLAUDE.md`, `produkttexter-standard.md` och `LARDOMAR.md`, medan agentprompter.md hänvisar till regelboken. Prompten bör peka på regler-v1.md och agentprompter.md (rollen Skrivare) i stället, annars läser skrivaren föråldrade regler.
4. Prompten gäller "Velomarket-produkter" och Gymstick i andra körningar; gör den butiks- och gruppneutral (variabler `SKRIVFIL`, `FORE_FIL`, `RAPPORT`).
5. Det saknas ett skript som bygger "kopia för kontrollscript" ur skrivfil och före-fil (standardblock inom markörer, fakta = före-läget). Jag skrev det för hand. Lägg det i `shopify-sync/scripts/`.
6. Det saknas ett skript som skriver mutationen (som `bygg.py`) och en maskinell jämförelse av återläsning (som `jamfor.py`). Båda bör ligga i repot (R16 hänvisar till "skript" utan att peka på ett). Mutationen i ensure_ascii blir ca 2,5 gånger längre än texten och måste ändå klistras in; ett API-skript (när token finns) tar bort den manuella avskriften helt.
7. Före-filen och återläsningen måste i dag skrivas av från verktygssvar. R17 bör säga att före-filen är en avskrift tills API-token finns, och att den stäms av mot en ny läsning vid behov.
8. Saknas regel om meta som slutar med varumärkesfras ("Finns hos BEST OF SPORTS."): lägg till ett test i `skrivfil_kontroll.py` (R12 utfyllnad) som flaggar meta som avslutas med butiksnamnet.
9. Saknas regel för produkter där live-källan är en tidigare skriven text (pilot/våg 1): R1 bör säga att skrivfilens fakta då ska ha stöd i den ursprungliga tillverkartexten (finns i Före-filerna för pilot/våg 1), annars utelämnas påståendet.
10. Taggning sker enligt R18 "sist", men det är oklart om det avser sist per batch eller efter hela filen. Jag taggade efter att alla batcher var verifierade. Förtydliga.
