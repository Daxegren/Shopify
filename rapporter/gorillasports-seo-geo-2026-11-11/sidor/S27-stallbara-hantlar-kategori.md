# S27: Ställbara hantlar (kategori)

| Fält | Värde |
|---|---|
| Typ | Kategori |
| URL (komplett) | (saknas, fylls i) |
| URL i rapporten (kan vara avkortad) | https://www.gorillasports.se/collections/stallbara-hant… |
| Källa | Growth Audit (Etals, 2026-10-18) |
| Prioritet i rapporten | ej angiven (– rekommendationer) |
| Målnyckelord | ställbara hantlar (880/mån, pos. 21) |
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

**URL:** https://www.gorillasports.se/collections/stallbara-hantlar (200, canonical till sig själv)

| Mätpunkt | Värde |
|---|---|
| Titel | "Justerbara hantlar – Ställbara hantlar för flexibel träning – Gorilla Sports Nordics" |
| Metabeskrivning | "Ställbara hantlar som hantelset med viktskivor och hantelstänger. Välj färdiga set eller bygg ditt eget och ändra vikten efter övning. Snabb leverans." |
| H1 | Justerbara Hantlar (innehåller inte ordet "ställbara") |
| Synliga ord | cirka 503 |
| H2 | Ställbara/Justerbar hantlar, Köp justerbara hantlar |
| Produkter | 42 |
| Strukturerad data | ItemList |

**Iakttagelser:** sökordet *ställbara hantlar* (880/mån, pos. 21) finns i titeln och i en H2, men H1 säger "Justerbara Hantlar". Sidan är omfattande (42 produkter, 503 ord) men har bara två rubriker i texten.

**Förslag (beslut av David krävs):** 1) Gör H1 och H2 konsekventa mot sökordet, t.ex. "Ställbara hantlar" (Google förstår synonymen justerbara, men sidan bör vara tydlig). 2) Lägg till köpguide under produkterna (typer: hantelset, skivstångs-hantlar, viktskivor; vad som skiljer 30 mm/50 mm enligt tillverkaren). Rankingen ligger nära sida 1, så det här är en av de snabbaste vinsterna enligt rapporten. Verifiera med Search Console.
