# Skanningsrapport: Gorilla Sports Nordics

Datum: 2026-11-20. Källor: produkter.csv, kollektioner.csv, oversattning_sammanfattning.csv. Läsande skanning, inget har ändrats på sajten.

**Sammanfattning:** 2 brister och 12 varningar fördelade på 4 paket.

## Fynd per paket

### P1. Katalogstädning (kategorier, attribut, bilder, dubbletter)

| Fynd | Antal | Av | Andel | Allvar | Åtgärd | Enhet för insats |
|---|---|---|---|---|---|---|
| Bilder utan alt-text (aktiva produkter) | 7854 | 8228 | 95.5 % | BRIST | Sätt alt-text i bulk (wb_alt.py) | per 1 000 bilder |
| Aktiva produkter utan produktkategori | 210 | 885 | 23.7 % | BRIST | Sätt produktkategori (kategori_satt.py) | per 100 produkter |
| Aktiva produkter utan fältet Avsett för (kön) | 879 | 885 | 99.3 % | VARNING | Fyll attributet efter regel (kon_fyll_target_gender.py) | per 1 000 produkter |
| Produkttitlar som används på flera aktiva produkter (antal produkter) | 27 | 885 | 3.1 % | VARNING | Granska: samma produkt i flera storlekar eller riktiga dubbletter | per 100 produkter |

### P2. Kollektioner och sidstruktur (tomma sidor, regler, omdirigeringar)

| Fynd | Antal | Av | Andel | Allvar | Åtgärd | Enhet för insats |
|---|---|---|---|---|---|---|
| Tomma kollektioner | 5 | 216 | 2.3 % | VARNING | Regelfix, avpublicera och omdirigera | per kollektion |

### P4. Innehåll och metadata (titlar, beskrivningar, rubriker, texter)

| Fynd | Antal | Av | Andel | Allvar | Åtgärd | Enhet för insats |
|---|---|---|---|---|---|---|
| Kollektioner utan SEO-titel | 31 | 216 | 14.4 % | VARNING | Skriv SEO-titel (prioritera efter visningar) | per kollektion |
| Kollektioner med nästan ingen beskrivning (under 50 tecken) | 28 | 216 | 13.0 % | VARNING | Skriv kategoritext | per kollektion |
| Kollektioner utan SEO-beskrivning | 17 | 216 | 7.9 % | VARNING | Skriv SEO-beskrivning | per kollektion |

### P5. Språk och marknader (översättning, hreflang)

| Fynd | Antal | Av | Andel | Allvar | Åtgärd | Enhet för insats |
|---|---|---|---|---|---|---|
| Föråldrade översättningar av kollektionsbeskrivningar (alla språk) | 77 | 370 | 20.8 % | VARNING | Översätt om ändrade källtexter | per språk och 1 000 texter |
| Föråldrade översättningar av produkttitlar (alla språk) | 446 | 2464 | 18.1 % | VARNING | Översätt om ändrade källtexter | per språk och 1 000 texter |
| Minst översatta kollektionsbeskrivningar (de tre sämsta språken: no saknar 32, da saknar 20) | 52 | 633 | 8.2 % | VARNING | Översätt saknade texter per språk | per språk och 1 000 texter |
| Föråldrade översättningar av kollektionstitlar (alla språk) | 26 | 408 | 6.4 % | VARNING | Översätt om ändrade källtexter | per språk och 1 000 texter |
| Minst översatta produkttitlar (de tre sämsta språken: no saknar 154, da saknar 0) | 154 | 3927 | 3.9 % | VARNING | Översätt saknade texter per språk | per språk och 1 000 texter |
| Minst översatta kollektionstitlar (de tre sämsta språken: no saknar 24, da saknar 0) | 24 | 648 | 3.7 % | VARNING | Översätt saknade texter per språk | per språk och 1 000 texter |

## Att veta

- Produkter i status utkast/arkiverad (av alla): 424 av 1309

## Exempel (för att kunna kontrollera fynden)

- Aktiva produkter utan produktkategori: Curlstång CHROME 35kg; Hantlar IRON Gjutjärn 2x15kg; Curlstång IRON 35kg
- Produkttitlar som används på flera aktiva produkter (antal produkter): skivstång 170cm stjärnlås 30mm; skivstång curlstång hantlar iron 108kg; skivstångsset fjäderlås 30mm
- Tomma kollektioner: frontpage; kinesiologi-kinesiotejp; traningsutrustning-for-seniorer-och-aldre; gyronetics; showroom

## Anmärkningar och begränsningar

- SEO-titel/-beskrivning tomma på en produkt betyder att Shopify använder produkttiteln/texten; det är inte i sig ett fel.
- Översättningstäckningen räknas på alla produkter i exporten, även utkast och arkiverade; täckningen för aktiva produkter är sannolikt högre.
