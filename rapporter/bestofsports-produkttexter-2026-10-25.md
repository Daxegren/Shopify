# Best of Sports: produkttitlar och produktbeskrivningar (2026-10-25)

Underlag: 3 250 aktiva produkter lästa ur Shopify (titel, beskrivning, SEO-fält, märke, taggar, lager). Bara läsning, inget ändrat. Radnivådata: `rapporter/bos-produkter-titlar-beskrivningar-2026-10-25.csv`. Språk och struktur bedöms med enkla regler (ordlistor, antal rubriker och listor), så siffrorna är riktmärken och inte facit. Med "GEO" avses här att texterna ska gå att citera för AI-sökning (svar först, tydliga fakta), inte geografisk anpassning. Landsanpassning (SE, DK, FI) behandlas separat.

## 1. Det viktigaste
1. **Beskrivningarna är tunna och saknar struktur.** Median 88 ord. 375 produkter (12 %) har under 30 ord, 1 009 (31 %) under 60. Bara 242 har över 250 ord. 90 % saknar rubriker och 32 % saknar lista. Tabeller finns på 11 produkter.
2. **Inget SEO-fält är ifyllt.** 100 % saknar SEO-titel och 92 % saknar metabeskrivning, så Google och AI-tjänster får en titel och ett utdrag som butiken inte styr över.
3. **Nästan allt kommer från leverantören.** 2 583 av 3 250 (79 %) är Velomarket-produkter. Många beskrivningar innehåller samma märkestext (till exempel "Giant grundades 1972…", AXA: "115 års erfarenhet") och ibland trasig data (till exempel "1620 Loop: 1616o Loop: 1620o" i en specifikation). 108 av dem är på engelska.
4. **Titlarna har en struktur, men den följs bara delvis.** 62 % följer mönstret "Typ MÄRKE Modell". Resten blandar ordning, versaler och språk: 5 % är mest versaler, 1 337 innehåller kommatecken, 273 snedstreck, och 118 titlar används på mer än en produkt. Färger står på engelska i 420 titlar och på svenska i 733, och 118 titlar blandar båda. Cirka 40 titlar börjar med engelska produkttyper som "Treadmill".
5. **Landsanpassning och trygghetsinformation saknas.** Bara 12 % av beskrivningarna nämner frakt, garanti, retur, montering eller Sverige. Inget säger vad som gäller i Danmark eller Finland, och ingen har svar på de frågor köparen ställer (passar den mig, hur lång leverans, vad ingår).
6. **623 av de aktiva produkterna har lager 0 eller lägre.** Det är relevant eftersom annonser och sök kan skicka trafik till produkter som inte går att köpa.

Produkttitlarna slutar inte längre på "Default Title" (0 av 3 250). De 25 som syns i Merchant-listan kommer från variantnamn i flödet.

## 2. Förslag på standard (att besluta om, inget genomfört)
**Titel** (Typ, Märke, Modell, nyckelegenskap, färg; svenska; ett kommatecken; högst 70 tecken):
`Löpband Toorx Evertift TFK-155 Slim, hopfällbar, svart`
Märket i normal skrivning (inte versaler), produkttypen först, färg på svenska sist, inga engelska typord. Modellnummer behålls.

**SEO-titel** (högst 60 tecken): `{Titel} | Best of Sports`. **Metabeskrivning** (140–155 tecken): vad produkten är, en nyckelfördel och frakt/retur.

**Beskrivning** (samma ordning på alla produkter):
1. **Svar först (1–2 meningar):** vad den är, för vem, den viktigaste egenskapen. Det är det en AI-tjänst eller Google tar som citat.
2. **Passar dig som…** (2–3 punkter): användningsfall.
3. **Specifikationer:** lista eller tabell med mått, vikt, material, maxbelastning, garanti, vad som ingår. Bara uppgifter som finns hos leverantören.
4. **Leverans och retur:** en kort, gemensam text per marknad (SE, DK, FI) som kommer från en mall, så att den ändras på ett ställe.
5. **Vanliga frågor (2–3):** till exempel "Hur lång är leveransen?", "Behöver den monteras?".
6. **Om märket (max 2 meningar):** unik text i stället för leverantörens standardtext.

**Regel:** inga uppgifter uppfinns. Allt kommer ur leverantörstexten, produktdata eller dina uppgifter. Det som saknas markeras "uppgift saknas" i utkastet och beslutas av dig.

## 3. Hur vi går tillväxtvägen utan att betala för trafik som inte köper
- **Fakta:** annonserna kostade 2 588 kr på 28 dagar för 424 klick och 0 konverteringar, och 54 % gick till två barncyklar. Det är cirka 92 kr per dag.
- **Min rekommendation (beslut för dig och Rude, jag ändrar ingenting i Ads):** sänk eller pausa Shopping-kampanjen tills en testorder visar att köp registreras i både GA4 och Google Ads. Utan mätning vet vi inte om 0 betyder 0 eller "inte mätt". Spara pengarna, och lägg dem på produkttexter och mätning.
- **Prioritering av texter:** `sql/analys/bos/12_produkter_prioritet_texter.sql` rangordnar produkter efter synlighet i Google och annonskostnad utan köp. Börja där, inte i alfabetisk ordning.

## 4. Pilot, i steg (varje steg kräver ditt ja)
1. **Pilot på 20 produkter** från prioritetsfrågan, med lager och högst synlighet. Jag skriver utkast i en tabell (före, efter, vad som saknas). Du granskar. Inget ändras i Shopify före ditt ja.
2. **Genomförande** enligt vår rutin: originaltexterna sparas, ändringen görs per produkt, läses tillbaka och loggas. Mätning med klick per sida mot ändrade produkter (`gsc_clicks`) efter fyra veckor.
3. **Översättningar (fi och da):** Translate & Adapt översätter sönder länkar och variabler (vi såg det i temat). Jag föreslår att texterna översätts, kontrolleras mot mönstret `{{`/`notranslate`/tomma `href`, och sedan registreras.
4. **Skala upp** till kategorierna med mest trafik, därefter resten, med mallar där leverantörens text är tunn.

## 5. Beslut som behövs
- **Standarden i avsnitt 2:** godkänn eller ändra (titelformel, beskrivningsordning, vilka marknadsavsnitt).
- **Annonser:** sänka eller pausa Shopping-kampanjen tills mätningen är verifierad? Rekommendation: sänk till ca en fjärdedel nu, pausa helt om testordern inte syns i GA4. Risk: tappad betald trafik, som idag inte köper. Utan beslut fortsätter ca 92 kr per dag utan konvertering.
- **Pilot:** 20 produkter. Rekommendation: ja. Risk: låg, eftersom inget ändras utan ditt ja.
- **De 623 produkterna utan lager:** ska de döljas från annonser och sök tills de finns i lager? Rekommendation: ja, i första hand ur annonserna (hanteras med Rude).
