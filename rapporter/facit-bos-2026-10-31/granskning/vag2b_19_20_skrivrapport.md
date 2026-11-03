# Skrivrapport: våg 2b, skrivfil 19 och 20 (elcyklar och cyklar, Best of Sports)

Datum: 2026-11-03. Butik: BEST OF SPORTS (bestofsports.se), verifierad med get-shop-info.
Skrivfiler: `vag2_skriv/b_skriv_19.json` (20 produkter), `vag2_skriv/b_skriv_20.json` (21 produkter).
Före-lägen: `rapporter/shopify-original-2026-11-03/vag2b_19_fore.json` och `vag2b_20_fore.json`.
Kontrollkopior: `granskning/tmp_kopia_vag2b19/` och `tmp_kopia_vag2b20/` (`kopia.json`, `kontroll.txt`, återläsningar `readback_*.json`).

## Före och efter
| Fil | Före (live) | Skrivna | Hoppade över | Taggen texter-klara | Userfel |
|---|---|---|---|---|---|
| 19 | 20 ACTIVE, ingen med texter-klara, ingen titel lika skrivfilen | 20 | 0 | 20 av 20 | 0 |
| 20 | 21 ACTIVE, ingen med texter-klara | 21 | 0 | 21 av 21 | 0 |

Före-läget för alla produkter sparades före skrivning. Titel, handle, status, seo.title, seo.description, descriptionHtml och taggar står i före-filerna.

## Avvikelse från reglerna (produkt 8912, 10589704749322)
Produkten har samma titel som skrivfilen, men seo, metabeskrivning och beskrivning var kvar i gammal form. Regeln "hoppa över när titeln är lika" bygger på att titeln lika betyder redan skriven, och det stämde inte här. Produkten skrevs därför med resten av filen. Titeln ändrades inte.

## Kontroll före skrivning
- `kontrollera_produkttext.py` på kopian (html som beskrivning, standardblock inom [[STANDARDBLOCK]], `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70`). Källtext = före-läget.
- Fil 19: 0 FEL, 43 varningar. Fil 20: 0 FEL, 29 varningar.
- Varningarna är "Passar för"-rubriken (godtagen) och engelska färgord som skriptet flaggar: Black, Grey, Red, Blue (till exempel Midnight Black, Velvet Red, Pale Moss/Black, Slate Grey/Black). Skriptet flaggar inte andra engelska färgnamn som Mars Dust, Snow Drift eller Pyrite Brown; de ingår i samma fråga. Standarden säger "färg på svenska" för titlar, men varningen är inte FEL och ingår inte i de godtagna varningarna, så den har inte stoppat skrivningen. Se "Beslut" nedan.

## Skrivning och kontroll efter skrivning
- Skrivning med `productUpdate` via variabler. Kanarie 3 produkter, därefter batcher om högst 5. Alla dokument under 16 384 tecken.
- Mutation och variabler skrevs ut av python-skript (`ensure_ascii=True`) ur skrivfilen och klistrades in ordagrant. Inga handskrivna texter. Ingen rättning av fel för hand.
- Seo skickades alltid som `{title, description}`.
- Återläsning efter varje batch, högst 4 produkter per fråga. Fälten titel, handle, status, taggar, seo.title, seo.description och descriptionHtml jämfördes tecken för tecken i python mot skrivfilen och före-läget. Resultat: 0 avvikelser i alla 41 produkter.
- Taggen texter-klara lades sist på alla 41 (tagsAdd). Återläsning av taggarna: texter-klara finns på alla, och de befintliga taggarna finns kvar.

## Begränsningar i kontrollen
- Före-filen för fil 19 är skriven för hand efter live-läsningen (för lång för att spara direkt). Den har kontrollerats på id, ordning, status och taggfrånvaro, men texten har inte jämförts maskinellt mot något annat. Om en rollback behövs bör den läsas om live först.
- Fil 20:s före-fil är skriven maskinellt ur det sparade svaret från live-läsningen.
- Återläsningarna har skrivits för hand till filer (de är klistrade svar). Jämförelsen är maskinell, men inklistringen är handarbete.
- Jämförelseskriptet `jamfor.py` och utskriftsskriptet ändrades på disken under arbetet. Fil 19 och kanarien i fil 20 gjordes med de versioner som gällde då. Det som ändrades påverkar inte resultatet, eftersom alla jämförelser gjordes med en fast version av jämförelseskriptet (`jamfor2.py`) och utskrifterna från samma skript.

## Beslut som behövs
1. Engelska färgnamn i titlar och texter. Gäller bland annat Midnight Black, Velvet Red, Pale Moss/Black, Slate Grey/Black, Mars Dust, Snow Drift och Pyrite Brown. Standarden kräver svenska färgnamn i titlar. Alternativ: (a) låta det stå och rätta i en uppföljning, (b) byta till svenska färgnamn i en ny skrivning. Rekommendation: (b) på titlar, eftersom det är standardens regel. Risk om inget beslutas: titlarna står kvar med engelska färgnamn.
2. Produkt 8912 skrevs trots titelregeln. Godkänns det? Om nej: den bör kontrolleras i butiken.

## Ändrat
- Shopify, BEST OF SPORTS: ja. Titel, SEO-titel, metabeskrivning och beskrivning på 41 produkter. Taggen texter-klara lades till på 41 produkter. Handle, status, pris och övriga taggar ändrades inte.
- Filer: före-filerna (två nya), kontrollkopior och återläsningar under `granskning/tmp_kopia_vag2b19/` och `tmp_kopia_vag2b20/`, och den här rapporten.
- Dokumentation: `shopify-sync/docs/ANDRINGSLOGG.md` och `LARDOMAR.md` (se nedan).
- Inga commits.

## Nästa steg
- Eventuellt beslut om färgnamn (se ovan).
- Nattkontroll av titlarna efter nattsynken (lärdom 2026-11-03).
- Ny skrivfil för de produkter som väntar.
