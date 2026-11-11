# S25: Motionscykel

| Fält | Värde |
|---|---|
| Typ | Nytt innehåll |
| URL (komplett) | (saknas, fylls i) |
| URL i rapporten (kan vara avkortad) | https://gorillasports.se/motionscykel/ |
| Källa | Growth Audit (Etals, 2026-10-18) |
| Prioritet i rapporten | Låg (1 rekommendationer) |
| Målnyckelord | motionscykel (8 100/mån, pos. 25, /collections/spinningcykel) |
| Status | Ej påbörjad |

## 1. Undersöka (nuläge)

Fylls i innan något föreslås. Allt ska ha källa och datum.

- [ ] Hämta sidans detaljrekommendationer ur Etals (i PDF:en finns bara sidlistan, inte de 1 rekommendationerna per sida)
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

**Viktigt fynd:** rapporten säger att nyckelordet *motionscykel* (8 100/mån) rankar på pos. 25 med sidan `/collections/spinningcykel`. Det finns en annan kategori som bättre matchar sökordet: `/collections/motionscykel-kondition`. Det finns också `/collections/traningscykel-motionscykel-crosstrainer`. Tre kategorier kan alltså konkurrera om samma sökord (kannibalisering). Detta är en hypotes tills Search Console visar vilken sida Google väljer.

**URL:** https://www.gorillasports.se/collections/motionscykel-kondition (200, canonical till sig själv)

| Mätpunkt | Värde |
|---|---|
| Titel | "Motionscykel & Träningscykel - Leverans till dörren! – Gorilla Sports Nordics" |
| Metabeskrivning | "Upptäck prisvärda motions- och träningscyklar med stabil konstruktion och justerbara inställningar. Perfekt för träning hemma eller på gymmet." |
| H1 | Motionscykel |
| Synliga ord | cirka 356 |
| H2 | Köpa motionscykel träningscykel, Olika typer av motionscykel, Hitta rätt motionscykel för ditt hemmagym, Vanliga frågor om motionscyklar |
| Produkter | 7 |
| Strukturerad data | ItemList (ingen FAQPage trots avsnittet "Vanliga frågor") |

**Förslag (beslut av David krävs):**
1. Välj en huvudsida för *motionscykel* (föreslagen: `motionscykel-kondition`) och länka dit från spinningcykel-sidan och blogginlägg. Verifiera först med Search Console. Risk: låg.
2. Lägg FAQPage-schema på avsnittet "Vanliga frågor om motionscyklar" (rapportens punkt W10). Risk: låg, kräver tema- eller appändring.
3. Konditionsguide per maskin (AI-rapportens åtgärd 1): ni nämns i 0 % av AI-svaren om hemmakondition.
