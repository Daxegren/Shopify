# S01: Avlastningsstativ

| Fält | Värde |
|---|---|
| Typ | Kategori |
| URL (komplett) | (saknas, fylls i) |
| URL i rapporten (kan vara avkortad) | https://www.gorillasports.se/collections/avlastni… |
| Källa | Growth Audit (Etals, 2026-10-18) |
| Prioritet i rapporten | Hög (4 rekommendationer) |
| Målnyckelord | (fylls i) |
| Status | Ej påbörjad |

## 1. Undersöka (nuläge)

Fylls i innan något föreslås. Allt ska ha källa och datum.

- [ ] Hämta sidans detaljrekommendationer ur Etals (i PDF:en finns bara sidlistan, inte de 4 rekommendationerna per sida)
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

**URL:** https://www.gorillasports.se/collections/avlastningsstativ (svarar 200, canonical pekar på sig själv)

| Mätpunkt | Värde |
|---|---|
| Titel | "Avlastningsstativ 🏋️‍♂️ - Stabil – Gorilla Sports Nordics" (emoji, radbrytning i titeln) |
| Metabeskrivning | "Prisvärda avlastningsstativ för säker skivstångsförvaring ✅ Hållbarhet ✅ Funktionalitet ✅ Kvalitet från Gorilla Sports!" (emoji, tre allmänna kvalitetsord) |
| H1 | Avlastningsstativ (en H1) |
| Synliga ord | cirka 298 |
| Rubriker (H2) | Avlastningsstativ för Styrketräning, Varför välja våra avlastningsstativ?, Fördelar med avlastningsstativ, Vårt sortiment av avlastningsstativ |
| Antal produkter på sidan | 2 |
| Strukturerad data | ItemList (ingen BreadcrumbList, ingen FAQPage) |

**Iakttagelser:** sidan är hög prioritet i Etals-rapporten. Den har bara 2 produkter och cirka 300 ord. Titel och metabeskrivning bygger på emoji och allmänna ord ("Stabil", "Kvalitet", "Hållbarhet"), som inte säger vad som skiljer produkterna.

**Förslag (inget är genomfört, beslut av David krävs):**
1. Skriv om titel och metabeskrivning utan emoji, med typ, antal modeller och faktiska uppgifter (material, bärförmåga enligt tillverkaren, mått). Effekt: tydligare träffbild; risk: låg.
2. Utöka texten enligt rapportens tvådelade modell (kort intro ovanför produkterna, köpguide under), med belagda uppgifter om skillnaden mellan avlastningsstativ och rack. Risk: låg.
3. Länka till närliggande kategorier (rack, skivstång 30 mm) så att sidan får interna länkar. Bekräfta först i Search Console om sidan har trafik; med bara 2 produkter kan en sammanslagning med rack-kategorin vara bättre. Beslutspunkt.
