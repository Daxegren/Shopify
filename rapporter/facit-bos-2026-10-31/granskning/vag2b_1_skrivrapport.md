# Våg 2b-1: skrivning av 30 Best of Sports-produkter (2026-11-03)

Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/b_skriv.json`. Före-läge (live före skrivning): `rapporter/shopify-original-2026-11-03/vag2b_1_fore.json`. Butik: BEST OF SPORTS (bestofsports.se), bekräftat med `get-shop-info`.

## Sammanfattning

- **Skrivet:** 30 av 30 produkter (titel, SEO-titel, metabeskrivning och beskrivning). Alla 30 var ACTIVE, ingen hoppades över, ingen hade taggen "texter-klara" eller en titel som redan var skriven.
- **Kanarie:** 3 produkter (nr 5007, 5009, 5013) skrevs först, lästes tillbaka och jämfördes mot filen innan resten skrevs.
- **Kontroll före skrivning:** `kontrollera_produkttext.py` på en kopia gav **0 FEL** och 34 VARNINGAR (30 st "saknar avsnittet 'passar dig som'", som är den kända och godtagna "Passar för"-varningen, och 4 st korta beskrivningar, se avvikelser).
- **Taggen "texter-klara"** lades på alla 30 med `tagsAdd`. Befintliga taggar finns kvar (kontrollerat per produkt).
- **Ändrat i Shopify:** ja, titel, SEO-titel, metabeskrivning, beskrivning (`descriptionHtml`) och taggen "texter-klara" på 30 produkter. Handle och status är oförändrade. Pris, lager, bilder och övriga taggar är oförändrade.

## Kontroll

**Maskinellt:**
- Antal produkter i skrivfil (30) och före-fil (30), och att id-mängderna är identiska.
- Status för alla 30 före skrivning och efter (ACTIVE).
- Att ingen produkt hade taggen "texter-klara" eller titel som redan var skriven före skrivning.
- Kontrollskriptet (0 FEL). Skriptet kördes på en kopia där `html` mappats till `beskrivning`, standardblocket (från `<h2>Leverans, retur och garanti</h2>` till slutet) är markerat med `[[STANDARDBLOCK]]`, och källtexten `fakta` = före-läget (titel + beskrivning).
- Att `userErrors` var tomma i varje mutation-svar (alla anrop).
- Att tags efter taggning innehåller "texter-klara" för alla 30 och att status och handle är oförändrade (läst i en fråga).

**För hand (läst ur svar och jämförd mot filen, ingen maskinell diff):**
- Kanarie (5007, 5009, 5013): titel, handle, status, tags, SEO-titel, metabeskrivning och hela `descriptionHtml` lästes tillbaka och jämfördes mot filen. Inga avvikelser.
- Övriga 27: titel, SEO-titel, metabeskrivning och `descriptionHtml` lästes tillbaka och jämfördes mot filen. Jämförelsen är gjord genom läsning, inte med diff, så en tecken-för-tecken-kontroll av hela beskrivningarna är inte maskinellt bevisad.

## Hoppade över

Inga. Alla 30 var ACTIVE och hade varken taggen "texter-klara" eller en titel som redan var skriven.

## Avvikelser

1. **SEO-titel lagrad som tom** för två produkter där SEO-titeln är lika med produkttiteln: 5045 (Multiverktyg Giant ToolShed 6) och 5063 (Verktygssats Giant Toolshed 12). Shopify lagrar då `seo.title` som null. Det är avsett enligt standarden (avsnitt 10), inte ett fel. Metabeskrivningen lagrades.
2. **Metabeskrivning saknas** för 5009, 5032, 5039, 5040 och 5059 (inga metabeskrivningar i skrivfilen). Enligt instruktionen skickades bara `seo.title`. Live-läget hade `seo.description = null` för dem, så inget raderades.
3. **Kontrollskriptets varningar som godtagits:** "saknar avsnittet 'passar dig som'" för alla 30 (vi använder "Passar för", känd och godtagen varning), och `beskrivning_langd` för fyra korta beskrivningar: 5009 (35 ord), 5035 (36 ord), 5039 (15 ord) och 5040 (15 ord). Det är VARNINGAR, inte FEL, och de skrevs. Granskaren bör titta på de fyra korta texterna.
4. **Titlar med fler än 2 kommatecken** (decimalkomma i mått) godtogs, enligt instruktionen.

Inga avvikelser i kanariepassen.

## Före och efter

Kolumnerna: nr, live-titel före, ny titel, SEO-titel före (tom = null), ny SEO-titel, metabeskrivning efter (ja/nej).

| Nr | Titel före | Titel efter | SEO-titel före | SEO-titel efter | Metabeskrivning |
|---|---|---|---|---|---|
| 5007 | Flaskhållare GIANT GATEWAY 5MM, svart | Flaskhållare Giant Gateway | (tom) | Flaskhållare Giant Gateway, Aluminium | ja |
| 5009 | GIANT TIRE PATCH KIT | Däcklagningskit Giant | (tom) | Däcklagningskit Giant för Innerslangar | nej (tom) |
| 5013 | Skirt protector SELLE MONTE GRAPPA, black, plastic | Kjolskydd Selle Monte Grappa, Svart, Plast | (tom) | Kjolskydd Selle Monte Grappa, Svart | ja |
| 5016 | Fender set HEBIE Taipan 24", black | Stänkskärmset Hebie Taipan, 24 tum, Svart | (tom) | Stänkskärmset Hebie Taipan, 24 tum | ja |
| 5017 | Fender set HEBIE Viper 26"-29" black | Stänkskärmset Hebie Viper, 26–29 tum, Svart | (tom) | Stänkskärmset Hebie Viper, 26–29 tum | ja |
| 5018 | Fender set HEBIE Viper X, 24"-28", MTB, black | Stänkskärmset Hebie Viper X MTB, 24–28 tum, Svart | (tom) | Stänkskärmset Hebie Viper X, 24–28 tum | ja |
| 5022 | Bakskärm HEBIE Viper X, 26"- | Bakskärm Hebie Viper X för Sadelstolpe | (tom) | Bakskärm Hebie Viper X | ja |
| 5026 | Stänkskärmset HEBIE Taipan Trekking 28", svart | Stänkskärmset Hebie Taipan Trekking, 28 tum, Svart | (tom) | Stänkskärmset Hebie Taipan Trekking | ja |
| 5027 | Fender set HEBIE Viper S, 26"-29", black | Stänkskärmset Hebie Viper S, 26–29 tum, Svart | (tom) | Stänkskärmset Hebie Viper S, 26–29 tum | ja |
| 5029 | Fender set HEBIE Viper x Stealth, 26"-29", MTB | Stänkskärmset Hebie Viper X Stealth, 26–29 tum, MTB | (tom) | Stänkskärmset Hebie Viper X Stealth | ja |
| 5032 | Bicycle watch Basil Noir | Cykelklocka Basil Noir, Silverfärgad | (tom) | Cykelklocka Basil Noir | nej (tom) |
| 5035 | Saddle cover Basil GO | Sadelöverdrag Basil GO | (tom) | Sadelöverdrag för Cykel Basil GO | ja |
| 5036 | Sadel SELLE MONTE GRAPPA Feliz, grå | Sadel Selle Monte Grappa Feliz, Grå | (tom) | Sadel Selle Monte Grappa Feliz | ja |
| 5039 | Flaskhållare GIANT AIRWAY SPORT Vit/Gloss Blue, vit-blå | Flaskhållare Giant Airway Sport, Vit och Blå | (tom) | Flaskhållare Giant Airway Sport, Blå | nej (tom) |
| 5040 | Flaskhållare GIANT AIRWAY SPORT Vit/Gloss Red, vit-röd | Flaskhållare Giant Airway Sport, Vit och Röd | (tom) | Flaskhållare Giant Airway Sport, Röd | nej (tom) |
| 5044 | Cykelväska regnskydd Basil Keep Dry & Clean | Regnskydd för Cykelväska Basil Keep Dry & Clean | (tom) | Regnskydd Cykelväska Basil Keep Dry & Clean | ja |
| 5045 | GIANT Toolshed 6 verktygssats | Multiverktyg Giant ToolShed 6 | (tom) | Multiverktyg Giant ToolShed 6 | ja |
| 5047 | Saddle cover Basil Noir | Sadelöverdrag Basil Noir | (tom) | Sadelöverdrag Basil Noir, Polyester | ja |
| 5050 | Flaskhållare GIANT AIRWAY SPORT Röd/Gloss Black, röd/blanksvart | Flaskhållare Giant Airway Sport, Röd och Blanksvart | (tom) | Flaskhållare Giant Airway Sport i Nylon | ja |
| 5051 | Pakväska BASIL KAVAN ECO CLASSIC, 68 l, dubbelsidig, svart | Packväska Basil Kavan Eco Classic, 68 l, Svart | (tom) | Packväska Basil Kavan Eco Classic | ja |
| 5052 | Sadel SELLE MONTE GRAPPA Venice, svart | Sadel Selle Monte Grappa Venice i Retrostil | (tom) | Sadel Selle Monte Grappa Venice | ja |
| 5059 | Flaskhållare Giant AirWay Lite | Flaskhållare Giant AirWay Lite i Kolfiber, Svart | (tom) | Flaskhållare Giant AirWay Lite, Svart | nej (tom) |
| 5061 | Flaskhållare GIANT AIRWAY SPORT Blå/Gloss Black, blå/blanksvart | Flaskhållare Giant Airway Sport, Blå och Blanksvart | (tom) | Flaskhållare Giant Airway Sport | ja |
| 5062 | Cykelklocka GIANT DING-A-LING Silver | Cykelklocka Giant Ding-a-Ling, Silver | (tom) | Cykelklocka Giant Ding-a-Ling | ja |
| 5063 | Giant Toolshed 12 Tool Kit | Verktygssats Giant Toolshed 12 | (tom) | Verktygssats Giant Toolshed 12 | ja |
| 5075 | Flaskhållare GIANT Proway, Svart/Neongul | Flaskhållare Giant Proway, Svart och Neongul | (tom) | Flaskhållare Giant Proway Neongul | ja |
| 5082 | Giant Toolshed 13 Tool Kit | Verktygssats Giant Toolshed 13, 13 Delar | (tom) | Verktygssats Giant Toolshed 13 | ja |
| 5084 | Sadelväska BASIL DISCOVERY 365D, M - 1 l, grå | Sadelväska Basil Discovery 365D, M, 1 l | (tom) | Sadelväska Basil Discovery 365D, 1 l | ja |
| 5085 | Golvpump GIANT Control Tower Pro 2 Stage | Golvpump Giant Control Tower Pro 2 Stage | (tom) | Golvpump Giant Control Tower Pro 2 | ja |
| 5086 | Saddlebag Basil Mada, 1L | Sadelväska Basil Mada, 1–1,5 l | (tom) | Sadelväska Basil Mada | ja |

Före-läget för beskrivningarna finns i `rapporter/shopify-original-2026-11-03/vag2b_1_fore.json` (fältet `descriptionHtml`), för återställning vid behov.

## Ändrat

- **Shopify (bestofsports.se):** 30 produkter: `title`, `seo.title`, `seo.description` (där metabeskrivning finns), `descriptionHtml`, och tagg "texter-klara" tillagd. Ingen handle eller status ändrad. Ingen annan produktdata ändrad.
- **Filer:** ny fil `rapporter/shopify-original-2026-11-03/vag2b_1_fore.json` (före-läge). Ny rapport `rapporter/facit-bos-2026-10-31/granskning/vag2b_1_skrivrapport.md`. Ingen commit, enligt instruktionen.
- **Ingen kod, ingen mall eller standard ändrad.**

## Nästa steg

- Granskaren (oberoende) bör läsa de fyra korta beskrivningarna (5009, 5035, 5039, 5040) och ta ställning.
- Stickprov efter nattsynken enligt `produkttexter-standard.md` avsnitt 10 och LARDOMAR (2026-11-02): kontrollera att titlar och beskrivningar ligger kvar för de 30, mot skrivfilen.
