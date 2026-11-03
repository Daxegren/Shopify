# Våg 2b, grupp 13a (cykellås), skrivrapport 2

Datum: 2026-11-03. Butik: BEST OF SPORTS (bestofsports.se, verifierad med get-shop-info).
Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/b_skriv_13a.json` (29 produkter).
Före-läge: `rapporter/shopify-original-2026-11-03/vag2b_13a_fore.json` (inte ändrat).

## Status: avbrutet före skrivning

Ingen productUpdate har körts och ingen tagg har lagts till. Index 0–28 är oförändrade i butiken av denna körning.

## Kontroll (kontrollera_produkttext.py)

Körningen gjordes på en kopia av index 10–28 (19 produkter). Html mappades till beskrivning, standardblocket (från "Leverans, retur och garanti" till slutet) markerades med [[STANDARDBLOCK]], källtext var före-läget. Kopian ligger i `/tmp/claude-0/-home-user/fbbd95a3-8b18-5096-a6b5-20df3e4eb235/scratchpad/kontroll_10_28.json`.

Resultat: 14 FEL och 19 VARNINGAR.

FEL, alla `meta_langd` (kravet är 130–155 tecken):

| Nr | Tecken |
|---|---|
| 8651 | 122 |
| 8652 | 126 |
| 8655 | 105 |
| 8657 | 113 |
| 8658 | 121 |
| 8659 | 102 |
| 8661 | 120 |
| 8663 | 116 |
| 8664 | 122 |
| 8665 | 116 |
| 8666 | 126 |
| 8667 | 129 |
| 8668 | 128 |
| 8669 | 124 |

VARNINGAR: "saknar avsnittet 'passar dig som'" på alla 19. Det är rubrikvarningen som skrivprompten godtar.

Övriga 5 produkter (8648, 8650, 8660, 8662, 8670) klarar metakravet.

## Avvikelse som inte är rättad

Skrivfilens metabeskrivningar för de 14 produkterna är för korta enligt standarden (avsnitt 3 och 14). Standarden anger "kort meta" bara för produkter med tunn källa, och dessa har specifikationer i källan. Det är alltså inte ett undantag. Enligt skrivprompten och lärdomarna rättas inte detta med handskrivna variabler. Skrivningen avbröts därför.

## Andra fynd

- Nr 8638 (index 0, redan verifierad i den tidigare omgången) har meta på 124 tecken i skrivfilen. Den är inte med i kontrollen ovan. Samma regel gäller, så den bör granskas.
- Live-läsningen (`nodes`) gjordes för index 0–24. Index 25–28 är inte lästa live.

## Beslut som behövs

1. **Metalängden för de 14 produkterna.** Alternativ A: en ny skrivfil där metan blir 130–155 tecken, skriven av skribent och granskad på nytt. Alternativ B: David godkänner de kortare metorna som undantag från standarden. Rekommendation: A. Om inget beslutas står alla 19 kvar i butiken i sin nuvarande text (ingen skrivning sker).
2. **Index 0 (8638) med 124 tecken.** Samma beslut gäller.

## Nästa steg

När beslutet är taget: skriv om med en uppdaterad skrivfil (eller godkänt undantag), kör checkern på kopian, och skriv i batcher om högst 5 med skriptutskrift. Läs sedan tillbaka alla fält maskinellt och lägg taggen texter-klara först efter godkänd återläsning.
