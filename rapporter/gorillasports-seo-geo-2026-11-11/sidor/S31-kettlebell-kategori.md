# S31: Kettlebell (kategori)

| Fält | Värde |
|---|---|
| Typ | Kategori |
| URL (komplett) | (saknas, fylls i) |
| URL i rapporten (kan vara avkortad) | https://www.gorillasports.se/collections/kettlebell |
| Källa | AI search visibility report (Etals, 2026-10-18) |
| Prioritet i rapporten | ej angiven (– rekommendationer) |
| Målnyckelord | kettlebell |
| Status | Ej påbörjad |

## 1. Undersöka (nuläge)

Fylls i innan något föreslås. Allt ska ha källa och datum.

- [ ] Hämta sidans detaljrekommendationer ur Etals (i PDF:en finns bara sidlistan, inte de – rekommendationerna per sida)
- [ ] Hämta live: titel, H1, metabeskrivning, antal ord, canonical, schema, interna länkar in/ut, svarskod
- [ ] Sökdata: visningar, klick, position och sökord (Search Console)
- [ ] AI-synlighet: nämns sidan i AI-svar? Vilka frågor? Vilken konkurrent nämns i stället?
- [ ] Konkurrentsida som rankar bäst på målnyckelordet (URL, ordantal, struktur)
- [ ] Vilka sitewide-åtgärder (se `tema/sitewide-atgarder.csv`) berör sidan?

| Mätpunkt | Värde före | Datum | Källa |
|---|---|---|---|
| Position målnyckelord | | | |
| Klick/månad | | | |
| Ordantal | | | |
| Har H1 (ja/nej) | | | |
| Nämns i AI-svar | | | |

## 2. Utveckla (förslag)

Varje förslag: vad, varför (koppla till rapportens punkt eller mätpunkt), förväntad effekt och risk.

| # | Förslag | Varför | Källa i rapport | Effekt/risk | Beslut (David) |
|---|---|---|---|---|---|
| 1 | | | | | |

Textförslag skrivs bara med belagda uppgifter (samma faktaregler som butikens texter: inga löften utan publicerade studier, uppgifter från tillverkare eller egen källa).

## 3. Presentera

Underlag för sidan i en sida-rapport (`mallar/presentation-sida.md`): läget, vad vi gör, vad det ger, vad vi behöver från er.

## 4. Genomfört och uppföljning

| Datum | Vad ändrades | Av vem | Efter 4 v: position/klick | Anmärkning |
|---|---|---|---|---|

## Live-undersökning 2026-11-11

**Metod:** egen hämtning av sidans HTML 2026-11-11 (verktyget `mallar/analys_sida.py`). Synliga ord räknas utan sidhuvud, sidfot och meny. Inga sökdata (position, klick) ingår: Search Console är inte ansluten ännu.

**URL:** https://www.gorillasports.se/collections/kettlebell (200, canonical till sig själv)

| Mätpunkt | Värde |
|---|---|
| Titel | "Kettlebell - Köp kettlebell mellan 2-40 kg till bra pris – Gorilla Sports Nordics" |
| Metabeskrivning | "Här hittar du competition kettlebells, järnkettlebells och kettlebells med gummibeläggning till de bästa priserna. Prisvärda kettlebells i vikter från 2-40kg." |
| H1 | Kettlebell |
| Synliga ord | cirka 505 |
| H2 | Våra kettlebells, Olika modeller, Välj rätt kettlebell för ditt hemmagym, Populära kettlebellövningar, Kettlebellens historia |
| Produkter | 31 |
| Strukturerad data | ItemList |

**Iakttagelser:** sidan är den mest citerade av AI-assistenter (AI-rapporten) och Gorilla Sports leder ämnet kettlebells med 13 %. Sidan är redan välstrukturerad. Det finns fler kettlebell-kategorier (`kettlebells-cement`, `kettlebells-gjutjern`, `kettlebellpaket`, `justerbara-kettlebells`, `kettlebellstall`).

**Förslag:** skydda sidan: ändra inte rubrikerna utan skäl. Lägg FAQPage-schema, och bygg ut med en kettlebellguide (AI-rapportens åtgärd 3: ni är topp 10 för 0 av 10 köpfrågor) som länkar till de fem underkategorierna. Beslut av David krävs.
