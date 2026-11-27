# Underlag: dubbletter bland jack- och vinterklädeskollektioner (Workout Brands), 2026-11-27

Bara läsning. Ingenting ändrat. Siffror för produktantal ur tagg-sökningar kan avvika något (några enheter) från kollektionernas egna antal.

## 1. Jackor, herr och dam

| Kollektion | Regel | Produkter | Text | Lager-filter | Länkad i menyn | Google (sedan 2025-07) |
|---|---|---|---|---|---|---|
| `jacka-herr` | taggarna `Jacket` + `men` | 134 | ja (med länkar) | ja, lager > 1 | ja (Streetwear – Man) | 165 visningar, 7 klick, CTR 4,2 %, plats 17 |
| `jackor-herr` | taggarna `jacka` + `Herr` | 325 | nej | nej | nej | 62 visningar, 1 klick, plats 21 |
| `jacka-dam` | taggarna `Jacket` + `Women` | 100 | ja (med länkar) | ja, lager > 1 | ja (Streetwear – Kvinna) | 284 visningar, 17 klick, CTR 6,0 %, plats 17,5 |
| `jackor-dam` | taggarna `jacka` + `Dam` | 256 | nej | nej | nej | 27 visningar, 1 klick, plats 11 |
| `jackor-herr-dam` | taggen `HÖST JACKA` | 208 | nej | nej | nej | 4 visningar |

**Det viktiga:** de två paren är inte samma lista. Taggsökning (aktiva och i lager räknas separat):
- Herr: `jacka`+`Herr` ger cirka 341 produkter (175 aktiva och i lager). Av dem har 179 också taggarna `Jacket`+`men`. 153 saknar taggen `Jacket`, varav cirka 64 i lager. Alltså saknar `jacka-herr` cirka 64 jackor i lager som `jackor-herr` har.
- Dam: `jacka`+`Dam` ger cirka 258 (163 aktiva och i lager); `Jacket`+`Women` ger 145 (100 i lager). `jacka-dam` saknar alltså cirka 60 jackor i lager som `jackor-dam` har.
- `jackor-herr-dam` bygger på taggen `HÖST JACKA`: det är höstjackor, inte alla jackor, trots namnet. Cirka 156 aktiva och i lager.
- Interna länkar i beskrivningarna av `vinterklader-herr`/`-dam` pekar på `jacka-herr`/`jacka-dam`.

### Alternativ för herr och dam
**A (rekommenderas). Behåll `jacka-herr` och `jacka-dam` som huvudsidor, byt deras regel till den bredare** (taggen `jacka` + `Herr`/`Dam` + lager > 1), omdirigera `jackor-herr` och `jackor-dam` dit och avpublicera dem. Skäl: huvudsidorna är redan länkade i menyn, har text och alla klick. Följd: `jacka-herr` går från 134 till cirka 175 produkter, `jacka-dam` från 100 till cirka 160; ingen jacka i lager försvinner. Risk: regeln på menysidorna ändras (får fler produkter, inklusive sådana utan taggen `Jacket`, till exempel västar eller kappor); texten bör ses över efteråt. Ångra: återställ regeln.
**B. Behåll `jackor-*` som huvudsidor** och omdirigera `jacka-*`. Kräver ändring i menyn (menylänkar till `jacka-*`) och förlorar sidorna med text och klick. Rekommenderas inte.
**C. Låt vara.** Två sidor per sökord fortsätter konkurrera.

### `jackor-herr-dam` (höstjackor)
Alternativ: (i) byt namn till "Höstjackor – Herr & Dam" (ny SEO-titel, handle oförändrad eller ändras med omdirigering), (ii) omdirigera till en av huvudsidorna ovan och avpublicera. Rekommenderas: (i), eftersom det är en egen och riktig sökavsikt (höstjacka) med 156 köpbara produkter.

## 2. Vinterkläder

| Kollektion | Regel | Produkter | Text | Google |
|---|---|---|---|---|
| `vinterklader-herr` | ingen regel (manuell lista) | 241 | lång text, länkar | 80 visningar, 3 klick, plats 17,6 |
| `vinterklader-herr-1` | ingen regel (manuell lista) | 94 | lång text | 67 visningar, 0 klick |
| `vinterklader-dam` | ingen regel (manuell lista) | 210 | lång text, länkar | 4 visningar |
| `vinterklader-herr-dam` | någon av taggarna vinterjacka, dunjacka, parka, kappa, fleece, mössa, Handskar, halsduk | 483 | lång text | 134 visningar, 2 klick, plats 41,5 |

- Ingen av vinterklädeskollektionerna är länkad i menyn.
- `vinterklader-herr` och `vinterklader-herr-1` har samma namn ("Vinterkläder - Herr") och bygger på handplockade listor. Hur mycket de överlappar går inte att läsa ur reglerna: det kräver en jämförelse av produkt-id:n, som jag inte har gjort.
- Alternativ: välj en huvudsida per kön (`vinterklader-herr`, `vinterklader-dam`), flytta in produkter som bara finns i dubbletten, omdirigera dubbletten. `vinterklader-herr-dam` är en egen regelstyrd sida och kan stå kvar.

## 3. Övrigt jag såg
- **Vinterjackorna är inte länkade i någon meny**, trots att jackorna har många köpbara produkter och sökningar på "vinterjacka" finns. Det begränsar hur lätt Google och kunderna hittar dem.
- Alla kollektioner ovan är publicerade och har produkter; ingen är tom.

## Beslut som behövs
1. Herr och dam: A, B eller C?
2. `jackor-herr-dam`: byta namn eller omdirigera?
3. Vinterkläder: ska jag göra en id-jämförelse av de två "Vinterkläder - Herr" innan vi bestämmer?
4. Ska vinterjackorna länkas i menyn (görs i admin, eller av mig efter ditt ja)?
