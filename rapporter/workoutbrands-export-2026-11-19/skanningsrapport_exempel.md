# Skanningsrapport: Workout Brands (exempel)

Datum: 2026-11-19. Källor: produkter.csv, kollektioner.csv, oversattning_sammanfattning.csv. Läsande skanning, inget har ändrats på sajten.

**Sammanfattning:** 3 brister och 15 varningar fördelade på 4 paket.

## Fynd per paket

### P1. Katalogstädning (kategorier, attribut, bilder, dubbletter)

| Fynd | Antal | Av | Andel | Allvar | Åtgärd | Enhet för insats |
|---|---|---|---|---|---|---|
| Bilder utan alt-text (aktiva produkter) | 46013 | 70475 | 65.3 % | BRIST | Sätt alt-text i bulk (wb_alt.py) | per 1 000 bilder |
| Aktiva produkter utan bild | 3 | 7380 | 0.0 % | BRIST | Lägg till bild eller avpublicera | per produkt |
| Aktiva produkter utan fältet Avsett för (kön) | 802 | 7380 | 10.9 % | VARNING | Fyll attributet efter regel (kon_fyll_target_gender.py) | per 1 000 produkter |
| Produkttitlar som används på flera aktiva produkter (antal produkter) | 354 | 7380 | 4.8 % | VARNING | Granska: samma produkt i flera storlekar eller riktiga dubbletter | per 100 produkter |
| Aktiva produkter utan produktkategori | 63 | 7380 | 0.9 % | VARNING | Sätt produktkategori (kategori_satt.py) | per 100 produkter |

### P2. Kollektioner och sidstruktur (tomma sidor, regler, omdirigeringar)

| Fynd | Antal | Av | Andel | Allvar | Åtgärd | Enhet för insats |
|---|---|---|---|---|---|---|
| Tomma kollektioner | 42 | 674 | 6.2 % | BRIST | Regelfix, avpublicera och omdirigera | per kollektion |

### P4. Innehåll och metadata (titlar, beskrivningar, rubriker, texter)

| Fynd | Antal | Av | Andel | Allvar | Åtgärd | Enhet för insats |
|---|---|---|---|---|---|---|
| Kollektioner utan SEO-titel | 524 | 674 | 77.7 % | VARNING | Skriv SEO-titel (prioritera efter visningar) | per kollektion |
| Kollektioner utan SEO-beskrivning | 328 | 674 | 48.7 % | VARNING | Skriv SEO-beskrivning | per kollektion |
| Kollektioner med nästan ingen beskrivning (under 50 tecken) | 85 | 674 | 12.6 % | VARNING | Skriv kategoritext | per kollektion |
| SEO-titlar över 60 tecken (av satta) | 34 | 383 | 8.9 % | VARNING | Korta titeln | per 100 produkter |
| SEO-beskrivningar över 160 tecken (av satta) | 141 | 4312 | 3.3 % | VARNING | Korta beskrivningen | per 100 produkter |
| Aktiva produkter med beskrivning under 100 tecken | 18 | 7380 | 0.2 % | VARNING | Skriv produkttexter | per produkt |

### P5. Språk och marknader (översättning, hreflang)

| Fynd | Antal | Av | Andel | Allvar | Åtgärd | Enhet för insats |
|---|---|---|---|---|---|---|
| Minst översatta kollektionsbeskrivningar (de tre sämsta språken: is saknar 661, tr saknar 403, sr saknar 390) | 1454 | 1995 | 72.9 % | VARNING | Översätt saknade texter per språk | per språk och 1 000 texter |
| Minst översatta kollektionstitlar (de tre sämsta språken: is saknar 670, tr saknar 356, sr saknar 347) | 1373 | 2022 | 67.9 % | VARNING | Översätt saknade texter per språk | per språk och 1 000 texter |
| Föråldrade översättningar av kollektionsbeskrivningar (alla språk) | 5393 | 8097 | 66.6 % | VARNING | Översätt om ändrade källtexter | per språk och 1 000 texter |
| Minst översatta produkttitlar (de tre sämsta språken: is saknar 8928, no saknar 7443, en saknar 7273) | 23644 | 46992 | 50.3 % | VARNING | Översätt saknade texter per språk | per språk och 1 000 texter |
| Föråldrade översättningar av produkttitlar (alla språk) | 16466 | 171029 | 9.6 % | VARNING | Översätt om ändrade källtexter | per språk och 1 000 texter |
| Föråldrade översättningar av kollektionstitlar (alla språk) | 450 | 9158 | 4.9 % | VARNING | Översätt om ändrade källtexter | per språk och 1 000 texter |

## Att veta

- Produkter i status utkast/arkiverad (av alla): 8284 av 15664

## Exempel (för att kunna kontrollera fynden)

- Tomma kollektioner: home-start-collection; collection-1; collection-3; traningsskor-kvinna; traningssko
- Produkttitlar som används på flera aktiva produkter (antal produkter): flexfit 360 omnimesh cap s/m; classic 5 panel snapback one size; low profile cap snapback one size
- Aktiva produkter utan produktkategori: Cap Washer black one size; CapRack 36 System; CapRack 18 System black one size

## Anmärkningar och begränsningar

- SEO-titel/-beskrivning tomma på en produkt betyder att Shopify använder produkttiteln/texten; det är inte i sig ett fel.
