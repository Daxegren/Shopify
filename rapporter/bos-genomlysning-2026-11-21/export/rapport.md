# Skanningsrapport: BEST OF SPORTS

Datum: 2026-11-21. Källor: produkter.csv, kollektioner.csv, oversattning_sammanfattning.csv. Läsande skanning, inget har ändrats på sajten.

**Sammanfattning:** 4 brister och 13 varningar fördelade på 4 paket.

## Fynd per paket

### P1. Katalogstädning (kategorier, attribut, bilder, dubbletter)

| Fynd | Antal | Av | Andel | Allvar | Åtgärd | Enhet för insats |
|---|---|---|---|---|---|---|
| Bilder utan alt-text (aktiva produkter) | 13722 | 14018 | 97.9 % | BRIST | Sätt alt-text i bulk (wb_alt.py) | per 1 000 bilder |
| Aktiva produkter utan produktkategori | 3033 | 3923 | 77.3 % | BRIST | Sätt produktkategori (kategori_satt.py) | per 100 produkter |
| Aktiva produkter utan bild | 6 | 3923 | 0.2 % | BRIST | Lägg till bild eller avpublicera | per produkt |
| Aktiva produkter utan fältet Avsett för (kön) | 3548 | 3923 | 90.4 % | VARNING | Fyll attributet efter regel (kon_fyll_target_gender.py) | per 1 000 produkter |
| Produkttitlar som används på flera aktiva produkter (antal produkter) | 83 | 3923 | 2.1 % | VARNING | Granska: samma produkt i flera storlekar eller riktiga dubbletter | per 100 produkter |

### P2. Kollektioner och sidstruktur (tomma sidor, regler, omdirigeringar)

| Fynd | Antal | Av | Andel | Allvar | Åtgärd | Enhet för insats |
|---|---|---|---|---|---|---|
| Tomma kollektioner | 77 | 350 | 22.0 % | BRIST | Regelfix, avpublicera och omdirigera | per kollektion |

### P4. Innehåll och metadata (titlar, beskrivningar, rubriker, texter)

| Fynd | Antal | Av | Andel | Allvar | Åtgärd | Enhet för insats |
|---|---|---|---|---|---|---|
| Kollektioner med nästan ingen beskrivning (under 50 tecken) | 160 | 350 | 45.7 % | VARNING | Skriv kategoritext | per kollektion |
| Kollektioner utan SEO-titel | 46 | 350 | 13.1 % | VARNING | Skriv SEO-titel (prioritera efter visningar) | per kollektion |
| Kollektioner utan SEO-beskrivning | 44 | 350 | 12.6 % | VARNING | Skriv SEO-beskrivning | per kollektion |
| Aktiva produkter med beskrivning under 100 tecken | 32 | 3923 | 0.8 % | VARNING | Skriv produkttexter | per produkt |
| SEO-titlar över 60 tecken (av satta) | 3 | 2108 | 0.1 % | VARNING | Korta titeln | per 100 produkter |

### P5. Språk och marknader (översättning, hreflang)

| Fynd | Antal | Av | Andel | Allvar | Åtgärd | Enhet för insats |
|---|---|---|---|---|---|---|
| Föråldrade översättningar av produkttitlar (alla språk) | 5214 | 8207 | 63.5 % | VARNING | Översätt om ändrade källtexter | per språk och 1 000 texter |
| Minst översatta kollektionsbeskrivningar (de tre sämsta språken: en saknar 297, fi saknar 118, da saknar 111) | 526 | 924 | 56.9 % | VARNING | Översätt saknade texter per språk | per språk och 1 000 texter |
| Minst översatta produkttitlar (de tre sämsta språken: en saknar 5370, fi saknar 2193, da saknar 361) | 7924 | 16131 | 49.1 % | VARNING | Översätt saknade texter per språk | per språk och 1 000 texter |
| Minst översatta kollektionstitlar (de tre sämsta språken: en saknar 305, fi saknar 56, da saknar 1) | 362 | 1050 | 34.5 % | VARNING | Översätt saknade texter per språk | per språk och 1 000 texter |
| Föråldrade översättningar av kollektionsbeskrivningar (alla språk) | 115 | 398 | 28.9 % | VARNING | Översätt om ändrade källtexter | per språk och 1 000 texter |
| Föråldrade översättningar av kollektionstitlar (alla språk) | 15 | 688 | 2.2 % | VARNING | Översätt om ändrade källtexter | per språk och 1 000 texter |

## Att veta

- Produkter i status utkast/arkiverad (av alla): 1454 av 5377

## Exempel (för att kunna kontrollera fynden)

- Aktiva produkter utan produktkategori: Sadel Selle Monte Grappa Venice, Brun; Skruvlås Tunturi, 30 mm; Isskor ANTi SKid Sole Double, 41–46
- Tomma kollektioner: frontpage; hantelpaket; teknik; pool; basket
- Produkttitlar som används på flera aktiva produkter (antal produkter): liv rove 3 damcykel, pulp gray; cykel excelsior cracker, guld matt; landsvägscykel giant defy advanced 1, charcoal/milky way

## Anmärkningar och begränsningar

- SEO-titel/-beskrivning tomma på en produkt betyder att Shopify använder produkttiteln/texten; det är inte i sig ett fel.
- Översättningstäckningen räknas på alla produkter i exporten, även utkast och arkiverade; täckningen för aktiva produkter är sannolikt högre.
