# Granskningsutlåtande k_11a (blandat: fitnesstillbehör, solglasögon, GPS-spårare, bänk, remmar)

Granskare: Opus. Endast läsning, inga ändringar i Shopify. Datum 2026-11-04. Butiken bekräftades (BEST OF SPORTS). Alla 25 produkter (21 utkast och 4 avvisade) hämtades live via Admin API (`shopify_api.hamta_produkter`), och varianter, priser, status och produkttyp hämtades via GraphQL. Underlag: regelbok v1.6, beslutslogg, butiksprofil, standard §12 och §16, LARDOMAR och utlåtandena k_10, k_09b och k_08e_09a. Det maskinläsbara utlåtandet finns i `vag2_skriv/k_utlatande_11a.json`. Varje post där har nr, id och fil, eftersom nr-serien kan krocka med andra batcher.

## Sammanfattning

- 21 utkast gav **8 GODKÄND, 13 RÄTTA och 0 UNDERKÄND**. Godkända: 9805, 9807, 9813, 9814, 9817, 9818, 9820 och 9824.
- Rättningarna lades in i en kopia av utkastet och kördes genom `skrivfil_kontroll.py`. Resultat: 0 fel och 0 varningar. Meta ligger mellan 101 och 141 tecken, och ingen text har fler än två "enligt tillverkaren". Varje före-text förekommer exakt en gång i sitt fält, vilket kontrollerades med skript.
- Alla siffror i utkasten (mått, vikter, längder, priser via varianter) finns i produktens egen live-källa. Inga uppgifter är lånade från syskonprodukter.
- **De fyra avvisningarna står sig.** 9801 är ett bärande stödben med en enda källmening. För 9802 Alpina T40 säger titeln "Skridskor", men källan beskriver en pjäxa; David avgör typordet. 9808 kallbadtunna bygger på hälsopåståenden och en läkarvarning. 9816 har tunn källa (bara anatomi och skaderisk).

## Huvudfynd

1. **Cirkulära inledningar (R11), 11 produkter.** Mönstret "Namn är en/ett [typord]" förekommer i meta och ofta i första meningen: 9803, 9804, 9809, 9810, 9811, 9812, 9819, 9821, 9822, 9823 och 9825. Inledningarna skrivs om med verb och typordet först, till exempel "Träningsrepet Battle Rope fixeras runt …" och "Situpskudden Ab Mat GS är gjord av …". Skriptets test hittar inte mönstret när orden skiljer sig ("Battle Rope är ett träningsrep", "Situpskudde … är en kudde"). Det bör bli en varning: meta eller första mening som börjar med ett egennamn följt av "är en/ett".
2. **9819 Anchor Straps, motsägande antal karbinhakar.** Källan säger både "inklusive två karbinhakar" och "inkluderar även en karbinhake". Utkastet flaggade motsägelsen men skrev ändå "Karbinhakar medföljer" (plural) i meta, löptext och specifikation, vilket tar ställning för två. Antalet stryks överallt enligt R2. Bara användningen ("fäst handtaget i karbinhaken") står kvar.
3. **9806 typordet "Träningsremmar" saknar stöd (R7).** Live-titeln är "Training belts", och källans första rad ("Träningsgrupp") är maskinöversatt. Ordet "träningsremmar" står inte i källan, inte i profilens `godkanda_typord` och inte i någon live-titel i butiken (titlarna söktes på "remmar" och "Träningsrem"). Titeln rättas tillbaka till "Training Belts". **Alternativ (beslut av koordinatorn eller David):** om "träningsremmar" läggs i `godkanda_typord` kan utkastet användas oförändrat. Butikens närmaste live-ord, "Suspensionstränare", används inte, eftersom källan inte säger "suspension".
4. **9803 GPS-spårare.** Raden "Vid stöld: BikeFinder-teamet guidar … genom återvinningsprocessen" stryks. Den är ett tjänstelöfte och dessutom felöversatt ("återvinning" ska vara "återställning", engelska *recovery*), se R2. Månadsavgiften nämns som sakuppgift utan belopp och utan löften, och det är rätt. Stöldskyddslöftena ("praktiskt taget omöjlig att ta bort", "alla typer av cyklar") är utelämnade. Det ingår inga batteri-, räckvidds- eller täckningslöften.
5. **9815 sakfel i meta.** "Paret är 23 cm långt" ändras till "Varje adapter är 23 cm lång".
6. **9812 lastgränsens etikett.** Lastgränsen ska stå ordagrant: källans etikett "Max belastning" ska stå i stället för utkastets "Maximal belastning".

## Punkter som koordinatorn särskilt bad om

- **9804 solglasögon:** "Kat. 3" återges som "kategori 3", vilket bara skriver ut förkortningen. Texten förklarar inte vad kategorin betyder, och den har inga UV-, ögonskydds- eller säkerhetsord (§16 punkt 2). Källans "maximalt skydd för dina ögon" är utelämnat. "Reptålig beläggning" står med "enligt tillverkaren". Bara den cirkulära inledningen rättas.
- **Hängande och bärande redskap med lastuppgift (R4):** 9806 har "Maximal användarvikt: 100 kg", 9812 "Max belastning: 300kg", 9819 "Maximal dragkraft(totalt): 400kg" och 9820 "Maxbelastning sittplats: 250kg". Alla fyra är rena svenska rader med etikett och enhet i produktens egen källa, och var och en står en gång med "enligt tillverkaren". Löptexten i 9820 anger samma värde (250 kg), så det finns ingen konflikt enligt R4 v1.5. 9805 (armhävningsstöd, 100 kg) uppfyller också R4. Inga lastgränser skrivs där källan saknar dem: 9811, 9814, 9815 och stativet i 9818.
- **9814:** "4mm insektsnyckel" återges som "4 mm nyckel (ingår ej)". Felöversättningen är borta, och texten tolkar inte ordet till insexnyckel. Godkänt.
- **9813 färg:** färgraden ("Svart, silver/grå och röd") är rätt utelämnad. Produkten har en enda variant, och det går inte att avgöra om raden beskriver färgval eller en flerfärgad produkt. Godkänt.
- **Prisvarianter (R3):** 9807 har 3 färger till samma pris, 9817 har 10 vikter (429–1 099 kr), 9822 har 6 kombinationer av längd och diameter (1 129–2 669 kr), 9823 har 2 diametrar (1 299 och 2 179 kr) och 9825 har 5 vikter (1 099–1 549 kr). Variantnamnen live stämmer med texterna. Ingen titel låser en variant, och mått och vikter anges per variant där de skiljer sig.
- **"Enligt tillverkaren" högst två per text:** högst två i alla 21 texter (två i 9805 och 9806), även efter rättningarna.

## Rättningar (före → efter)

| Nr | Fält | Före | Efter |
|---|---|---|---|
| 9803 | meta | `BikeFinder Gen2 är en GPS-spårare för cyklar med GPS, GSM och Bluetooth.` | `GPS-spåraren BikeFinder Gen2 för cyklar bygger på GPS, GSM och Bluetooth.` |
| 9803 | html | `<p>BikeFinder Gen2 är en GPS-spårare för cyklar baserad på GPS-, GSM- och Bluetooth-teknik.` | `<p>GPS-spåraren BikeFinder Gen2 för cyklar bygger på GPS-, GSM- och Bluetooth-teknik.` |
| 9803 | html | `<li>Vid stöld: BikeFinder-teamet guidar enligt tillverkaren ägaren genom återvinningsprocessen</li>` | (struken) |
| 9804 | meta / html | `Cairn Flake är solglasögon i kategori 3.` / `…i kategori 3 för sport.` | `Solglasögonen Cairn Flake tillhör kategori 3.` / `…tillhör kategori 3 och är avsedda för sport.` |
| 9806 | titel, seo_title, meta, html | `Träningsremmar` / `träningsremmar` | `Training Belts` (samt "Dig som söker Training Belts med dörrankare och medföljande väska") |
| 9809 | meta / html | `Ab Mat Situpskudde GS är en (svart) kudde i konstläder …` | `Situpskudden Ab Mat GS är gjord av svart konstläder, mäter …` / `Situpskudden Ab Mat GS i konstläder placeras under svanken …` |
| 9810 | meta / html | `Ab Mat Situpskudde Ryggstöd är en (svart) kudde i …` | `Situpskudden Ab Mat Ryggstöd i svart konstläder och skumplast mäter …` / `… används vid sit-ups.` |
| 9811 | meta / html | `Ab Roller är en magtränare som mäter …` / `… med skumvadderade grepp` | `Magtränaren Ab Roller mäter …` / `Magtränaren Ab Roller har skumvadderade grepp och nackstöd.` |
| 9812 | meta / html | `Ab Sling är ett redskap för magträning …` | `Ab Sling för magträning har bred, vadderad rem …` |
| 9812 | html | `Maximal belastning enligt tillverkaren: 300 kg` | `Max belastning enligt tillverkaren: 300 kg` |
| 9815 | meta | `Paret är 23 cm långt.` | `Varje adapter är 23 cm lång.` |
| 9819 | meta / html | `Anchor Straps är ett par (nylon)slingor … Karbinhakar medföljer …` | `Slingorna Anchor Straps i nylon säljs parvis och placeras …` (karbinhakar som medföljande stryks) |
| 9819 | html | `<li>Karbinhakar: Medföljer</li>` | (struken) |
| 9821 | meta / html | `Barbell Grips är ett par svarta grepp …` / `Barbell Grips är extra grepp i silikon som sveps runt` | `De svarta greppen Barbell Grips i silikon säljs i par och sveps runt …` / `De extra greppen Barbell Grips i silikon sveps runt` |
| 9822 | meta / html | `Battle Rope är ett träningsrep med medföljande fäste. Det finns` / `… som fixeras runt` | `Träningsrepet Battle Rope levereras med fäste och finns` / `Träningsrepet Battle Rope fixeras runt` |
| 9823 | meta / html | `Battle Rope är ett träningsrep på 15 m i (100 procent) nylon …` | `Träningsrepet Battle Rope är 15 m långt, tillverkat i (100 procent) nylon och finns …` |
| 9825 | meta / html | `Bulgarian Bag är en (svart) viktsäck i konstläder med sandfyllning och tre handtag.` | `Viktsäcken Bulgarian Bag i svart konstläder har sandfyllning …` / `Viktsäcken Bulgarian Bag är gjord av konstläder och har sandfyllning och tre handtag.` |

Tabellen är förkortad. Den exakta före-texten per fält står i JSON-filen.

## Förslag till regelboken och skriptet

- Lägg till en R11-varning i `skrivfil_kontroll.py` för meta eller första mening som har formen "[Egennamn] är en/ett …" (11 av 21 i den här batchen, och samma mönster i k_10).
- R2-förtydligande: när utkastaren själv flaggar en motsägelse i `att_bekrafta` ska uppgiften strykas i alla fält, inte bara i specifikationen (9819).
