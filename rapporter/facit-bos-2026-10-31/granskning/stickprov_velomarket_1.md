# Stickprov Velomarket 1: oberoende kontroll, 2026-11-03

Butik bekräftad: BEST OF SPORTS (bestofsports.se). Endast läsning. Live hämtat via nodes(ids) för 20 produkter. Jämfört mot `vag2_skriv/b_stickprov_1.json`; handle, status och taggar mot före-filerna `vag2b_1_fore.json` och `vag2b_2_fore.json`.

Leveransblocket ("Leverans, retur och garanti") är tecken för tecken identiskt i alla 20 live-svar och i stickprovet. Det finns också i `c_1_utkast.json`. Radbrytning mellan `<li>` räknades som lika.

## Matchning (ja = exakt)

| nr | titel | seo.title | seo.description | descriptionHtml | handle | status ACTIVE | tagg texter-klara + övriga kvar |
|---|---|---|---|---|---|---|---|
| 5009 | ja | ja | ja (null) | ja | ja | ja | ja |
| 5032 | ja | ja | ja (null) | ja | ja | ja | ja |
| 5039 | ja | ja | ja (null) | ja | ja | ja | ja |
| 5040 | ja | ja | ja (null) | ja | ja | ja | ja |
| 5059 | ja | ja | ja (null) | ja | ja | ja | ja |
| 5016 | ja | ja | ja | ja | ja | ja | ja |
| 5018 | ja | ja | ja | ja | ja | ja | ja |
| 5022 | ja | ja | ja | ja | ja | ja | ja |
| 5026 | ja | ja | ja | ja | ja | ja | ja |
| 5063 | ja | ja (null, lika med titel) | ja | ja | ja | ja | ja |
| 5060 | ja | ja | ja | ja | ja | ja | ja |
| 5064 | ja | ja (null, lika med titel) | ja | ja | ja | ja | ja |
| 5019 | ja | ja | ja | ja | ja | ja | ja |
| 5011 | ja | ja | ja | ja | ja | ja | ja |
| 5030 | ja | ja | ja | ja | ja | ja | ja |
| 5031 | ja | ja | ja | ja | ja | ja | ja |
| 5069 | ja | ja | ja | ja | ja | ja | ja |
| 5043 | ja | ja | ja | ja | ja | ja | ja |
| 5065 | ja | ja | ja | ja | ja | ja | ja |
| 5015 | ja | ja | ja | ja | ja | ja | ja |

Resultat: 20 av 20 matchar exakt på alla fält. Inga avvikelser. Taggarna är före-filens taggar plus `texter-klara`, inget saknas eller är extra. Före-filens handle och status (ACTIVE) är oförändrade.

## Fakta mot leverantörens original

Alla siffror och kompatibilitetsuppgifter stämmer med före-filerna. Inget påhittat fakta hittades. Kontrollerat särskilt:
- 5060: 18 x 1 1/4 till 18 x 1,9 tum, ETRTO 32-355 till 47-400, autoventil 40 mm, 115 g.
- 5015: ETRTO 47/62-622 (från originalets titel), 28/29 x 1,90/2,40, Presta 42 mm, UNI och EAN.
- 5069 och 5065: 700c x 23–28 mm (Caliper) och 23–25 mm (skiva), Defy, Contend, Avail.
- Hebie-skärmarna: längder, bredder och vikter. De garblade originalraderna ("borrmaskin", "bakre plattform") är rättade till skärm.
- Basil-korgarna: mått, styrstamsfäste 22–25,4 mm, korgfäste ingår inte (Bremen).

"Enligt tillverkaren" förekommer högst en gång per text. Brödtexten har högst en, och metan räknas separat. Inga arbetstermer (TBC, leverantörsnoter) har läckt in i kundtext.

## Språkfynd (inga fel som blockerar, bara polish)

| nr | fynd | före | efter (förslag) | vikt |
|---|---|---|---|---|
| 5009 | Cirkulär och upprepande: ingressen, "Passar för" och "Användning" säger samma sak tre gånger. | `Dig som vill kunna reparera en innerslang med gummiplåster` | `Dig som vill ha ett litet kit för att laga en punktering på en innerslang` (förutsätter att "punktering" godkänns som tolkning, annars stryk punkten) | låg |
| 5009 | Versal i mitten av SEO-titeln. | `Däcklagningskit Giant för Innerslangar` | `Däcklagningskit Giant för innerslangar` | låg, stilfråga: övriga titlar använder versaler |
| 5032 | "Passar för" upprepar ingressen ordagrant (silverfärgad, 60 mm). | `Dig som söker en silverfärgad cykelklocka` / `Dig som vill ha en klocka med diametern 60 mm` | Kan strykas eller göras till användning ("Dig som vill ha en ringklocka till cykeln"). Det är dock inte fel. | låg |
| 5043 | Trefaldig upprepning av "ta loss från fästet" (ingress, Passar för, specifikation). | `Dig som vill kunna ta loss cykelkorgen från fästet` | `Dig som vill kunna lyfta av korgen när du parkerar` (kräver tolkning) eller behåll | låg |
| 5018, 5022, 5019 | Upprepning av samma uppgift i ingress, "Passar för" och specifikation (adaptrar, sadelstolpe, fäste). | t.ex. 5022: `Montering: Fästs på sadelstolpen` | Acceptabelt i strukturen. Inget måste ändras. | mycket låg |
| 5015 | Etiketten "Modell" används för däckbredd, och "Storlek" för 29 tum. Ingressen kallar samma värde "storleken". Det blir inkonsekvent. | `Modell: 28/29 x 1,90/2,40` | `Däckbredd: 28/29 x 1,90–2,40` (originalets etikett "Modell" är ett leverantörsfel) | låg till medel (kundförvirring) |
| 5063 | "skruvmejselbits" och "sexkantsnycklar" är en liten tolkning av originalets "PH2, T25, SL5" och "sexkant". Rimligt men inte ordagrant i källan. | `sexkantsnycklar, skruvmejselbits` | `sexkantsnycklar, bits (PH2, T25, SL5)` | låg |

Stavning, grammatik och verb i första metameningen: inga fel. Alla metor börjar med "X är/har/..." (verb finns). Längd 130–154 tecken (≤160). SEO-titlar 22–41 tecken.

## Slutsats

- Exakt matchning: 20/20. Inga avvikelser mot live. Inga faktafel. Inga blockerande språkfel.
- Språkfynden ovan är kosmetiska, och 5015 (etiketten "Modell") är det enda som bör rättas.
- Rekommendation: full kontroll av batchen = nej för automatisk jämförelse (stickprovet är rent). Kör i stället samma programmatiska jämförelse (live mot skrivfil) över hela batchen, eftersom den är billig. Ingen manuell språkgranskning av hela batchen behövs. Rätta etiketten "Modell" där innerslangar med däckbredd återkommer: sök efter `Modell:` i övriga innerslangstexter.
