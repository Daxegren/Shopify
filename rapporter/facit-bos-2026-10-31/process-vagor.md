# Process för produkttexter i vågor (Best of Sports), beslutad 2026-10-31

Beslut av David 2026-10-31: gå igenom alla produkttexter nu och förbättra med tiden; "ordentligt, inget stressat"; Claude bestämmer batchstorlek. Ordning: steg 1 Velomarket, steg 2 Gymstick, steg 3 Gorilla Sports (kontroll).

## Vad processen kan och inte kan garantera
- Den kan inte garantera att varje text är felfri. Källan (leverantörens text) har fel, och en text kan bara vara så rätt som källan.
- Den garanterar att varje mening går att spåra till källan, att motsägelser i källan flaggas i stället för att skrivas vidare, att allt kontrolleras av kod, att varje skrivning kan återställas och att fel upptäcks inom ett dygn.

## Per produkt
1. Läs källa direkt ur butiken (titel, beskrivning, märke, typ, varianter) samma dag som utkastet skrivs.
2. Skriv utkast enligt `docs/produkttexter-standard.md`. Allt som står i texten ska finnas i källan. Motsägelser och trasig data skrivs inte vidare utan hamnar under "att bekräfta".
3. Kör `kontrollera_produkttext.py`. 0 FEL krävs.
4. Tunn källa (bara titel, eller under cirka 10 ord): ingen påhittad text. Kort beskrivning, ingen metabeskrivning, flaggas för datablad.

## Per våg
- Utkastsbatch: högst 15 produkter åt gången. Skrivbatch: högst 25.
- Kanarie: 3 produkter skrivs först och läses tillbaka mot förväntad text innan resten.
- Stickprov: David granskar minst 5 slumpmässigt valda produkter per våg (alla i de första vågorna). Alla fem ska godkännas utan ändring, annars rättas mönstret och vågen görs om.
- Återläsning efter skrivning och ny kontroll nästa dag efter nattsynken (titlar, status, beskrivning).
- Original och återställningsfil sparas före varje skrivning.

## Tas separat och för hand (Davids godkännande per produkt)
Säkerhetsprodukter där en felaktig uppgift kan skada: hjälmar, lås, barnprodukter, bänkar och stativ med belastningsuppgift, elcyklar (batteri), kosttillskott. Hälsopåståenden skrivs aldrig.

## Ordning inom steg 1
Fitness först (Tunturi, Toorx, BH Fitness, Hammer, Gymstick), eftersom Black Month, julhandeln och januari driver träning. Därefter övriga Velomarket i prioritetsordning efter trafik och annonskostnad när `sql/analys/bos/12_produkter_prioritet_texter.sql` är körd.

## Öppet
- SEO-titel utan eller med varumärkessuffix (standarden säger att temat lägger till ` – BEST OF SPORTS`; piloten har suffixet i fältet). Måste avgöras före första skrivningen: se `bos`-läsningen av live-HTML.
- Danska och finska SEO-fält: se standarden, avsnitt 5.
