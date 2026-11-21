# Genomlysning av BEST OF SPORTS, 2026-11-21 (läsande)

Samma metod som för Gorilla Sports: export av butikens produkter, kollektioner och översättningar (Cloud Shell, bara läsning; token har enbart `read_`-behörigheter) och en publik skanning av 100 sidor (1,5 s mellan anrop, avbryter vid bot-kontroll). Inget ändrades i butiken. Detaljer: `export/rapport.md` (4 brister och 13 varningar), `publik/rapport.md` (1 brist och 6 varningar). Rapporterna är underlag för bedömning och varje fynd bör granskas av en människa.

## Butiken i siffror
- 5 377 produkter varav 3 923 aktiva och 1 454 utkast eller arkiverade; 350 kollektioner; språk: sv (grund), da, fi och en.
- 3 229 av de aktiva produkterna (82 %) har taggen `texter-klara`: textutrullningen är i stort sett gjord.
- **2 233 aktiva produkter (57 %) har prisjobbstaggen `price-change-job-active`.** Enligt tidigare beslut rörs de inte av skrivningar förrän prisjobbet är avslutat (tidigast efter 2026-11-30). Det begränsar vad som går att göra nu.

## Fynd per lager (se playbook avsnitt 10)
**Lager 1, site (kollektioner och sidstruktur)**
- 77 av 350 kollektioner är tomma (22 %), bland annat `hantelpaket`, `teknik`, `pool` och `basket`. Flera ligger publicerade, och två av de sex sidorna utan exakt en H1 i den publika skanningen är tomma kollektioner (`hantelset`, `hantelpaket`). Strukturförslagen finns sedan tidigare (omdirigeringar och föräldralösa kategorier, se `bos-konsolidering-2026-11-21.md`); avpublicering kräver att David gör det i admin.
- 160 kollektioner (46 %) har nästan ingen text (under 50 tecken), 46 saknar SEO-titel och 44 saknar SEO-beskrivning.
- I den publika skanningen: 21 % av sidorna har SEO-titel över 60 tecken, 17 % metabeskrivning över 160 tecken, 3 % saknar metabeskrivning, 6 % saknar exakt en H1.
- 83 aktiva produkter delar titel med en annan aktiv produkt (granska: storlekar eller riktiga dubbletter).

**Lager 2, kanaler och produktflöden**
- **3 033 av 3 923 aktiva produkter (77 %) saknar produktkategori** (480 med "Uncategorized", 2 553 helt utan). Det är långt mer än hos Gorilla Sports (210 av 885). Störst är kosttillskott, konditionsträning och fitness, cyklar och tillbehör. Det avgör flödeskvaliteten mot Google, Meta och andra köpkanaler. **Vilka kanaler BOS faktiskt säljer i har jag inte kontrollerat** (kopplingen pekar inte på BOS); kontrollera det innan kategorisering prioriteras.
- 6 aktiva produkter saknar bild.

**Lager 3, filter och attribut**
- 3 548 av 3 923 saknar fältet Avsett för (kön). Relevant bara där kön betyder något (kläder, skor, cyklar).

**Innehåll och bilder**
- **Alt-text:** 13 722 av 14 018 bilder (97,9 %) saknar alt-text i mediabiblioteket, och i den publika skanningen saknar 82 % av bilderna alt i sidans HTML. Till skillnad från Gorilla Sports (där temat fyller i själv, 2 %) är det här en verklig lucka som syns för besökare och sökmotorer. Åtgärden är densamma som för Workout Brands (`wb_alt.py`, alt = produkttitel).
- 32 aktiva produkter har beskrivning under 100 tecken.

**Språk och marknader**
- Danska: 5 016 av 5 377 produkttitlar är översatta men **3 032 av dem är föråldrade** (källtexten ändrad sedan översättningen); 4 914 beskrivningar översatta varav 3 016 föråldrade; SEO-titlar för produkter saknas nästan helt (28 av 2 152). Finska: 3 184 titlar översatta, 2 176 föråldrade, inga SEO-översättningar. Engelska: i princip ingen produkttext översatt (7 av 5 377).
- Kollektioner är bättre översatta på danska och finska (titlar 349 av 350 respektive 294 av 350); engelska saknar 305 kollektionstitlar.
- Vilka språk som ger trafik vet vi inte än; prioritera efter Search Console innan något översätts.

## Förslag på ordning (inget är godkänt, inget är skrivet)
1. **Kontrollera mål och kanaler:** vilka köpkanaler säljer BOS i, och vilka marknader ger trafik? Det avgör om kategorisering (3 033 produkter) och översättning (8 000+ föråldrade texter) är värt mest.
2. **Search Console-baslinje för BOS** (`sc-domain:bestofsports.se`, även `.dk` och `.fi` finns): läsande, tar några minuter. Mycket arbete har redan gjorts i oktober och november, så en ny baslinje visar läget nu.
3. **Alt-text** (13 722 bilder): lågrisk och störst synlig effekt här. Kräver Davids ja och en app med `write_files`; avgör också om bildbeskrivningar på produkter med prisjobbstaggen får skrivas (de rör media, inte pris eller taggar, men BOS-reglerna nämner "skrivningar av produkter med price-change-job-active").
4. **Kollektionerna:** de 77 tomma (omdirigering efter beslut om avpublicering) och 46 saknade SEO-titlar; knyts till de öppna besluten i konsolideringsrapporten.
5. **Översättningar:** först efter Search Console visar vilka språk som ger trafik.
6. **Kategorier:** efter punkt 1, och med skrivrätt (`write_products`) i en app som David godkänt. BOS-token har bara läsning.

## Begränsningar
- Den publika skanningen tittar på 100 av 4 414 sidor och räknar andelar för urvalet; sidor hämtas utan JavaScript.
- Export och skanning mäter inte försäljning, trafik eller marginaler.
- Översättningstäckningen räknas på alla produkter (även utkast och arkiverade); täckningen för aktiva produkter är sannolikt högre.
