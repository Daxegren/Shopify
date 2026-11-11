# Gorilla Sports: SEO- och GEO-arbete per sida

Skapad 2026-11-11 utifrån två rapporter från Etals daterade 2026-10-18:

1. **Growth Audit for gorillasports.se** (organisk sökning: synlighet, nyckelord, sidnivå, prestanda, teknik, länkar).
2. **AI search visibility report for Gorilla Sports** (hur ChatGPT, Perplexity, Gemini, Claude och Google AI Overviews svarar på 120 frågor).

Syftet är att varje enskild sida ska kunna **undersökas, utvecklas och presenteras** på samma sätt, och att arbetet går att följa upp med siffror.

## Så är mappen uppbyggd

| Fil/mapp | Innehåll |
|---|---|
| `ARBETSGANG.md` | De tre stegen, statusvärden och när något räknas som klart |
| `sidregister.csv` | En rad per sida (35 st): typ, URL, prioritet, målnyckelord, status per steg |
| `sidor/Sxx-*.md` | Ett dokument per sida enligt mallen: undersöka, utveckla, presentera, uppföljning |
| `mallar/sidmall.md` | Tom mall för nya sidor |
| `mallar/presentation-sida.md` | Mall för en enkel sidrapport till beslutsfattare |
| `tema/sitewide-atgarder.csv` | De 13 åtgärder som gäller flera sidor (H1, 404, JavaScript, FAQ-schema m.m.) |
| `tema/nyckelord.csv` | Nyckelorden som syns i PDF:en, kopplade till sida |
| `tema/ai-synlighet.md` | AI-rapportens resultat: ämnen, konkurrenter, frågor, källor, fem åtgärder |
| `tema/matning.md` | Startvärden (baslinje) och uppföljningsplan |

## Vad som saknas i PDF:erna (måste hämtas innan sidorna kan undersökas på riktigt)

- **Kompletta URL:er.** PDF:en avkortar många adresser med "…". Kolumnen `url_komplett` i registret är därför tom.
- **Sidornas egna rekommendationer.** Sidlistan visar "4–6 rekommendationer" per sida, men själva texterna finns bara i Etals webbvy, inte i PDF:en. Exempel som syns i PDF:en: ändra H1 på mitten "Mits GS" till "Slagmits / Sparkmits GS Svart - 40x20x15cm", länka `latsdrag` till ren kategori-URL, ta bort ChatGPT-HTML-omslag.
- **Alla 132 sidor och 263 nyckelord.** PDF:en visar 25 sidor och 11 nyckelord. Resten finns i Etals. Registret är byggt för att kunna växa: lägg en rad per ny sida.
- **Egen mätdata.** Search Console, Shopify och analysdata finns inte i den här mappen. Baslinjen i `tema/matning.md` kommer bara från rapporterna.

## Regler för arbetet

- Inget skrivs i butiken utan Davids besked. Ändringar i en butik följer samma rutin som övriga textutrullningar (`shopify-sync/docs/textutrullning-rutin.md`) och loggas i `shopify-sync/docs/ANDRINGSLOGG.md`.
- Texter bygger på belagda uppgifter. Inga löften om hälsa, prestanda eller resultat utan publicerade studier.
- Rapporternas siffror är Etals uppskattningar. Prognoser för intäkter (t.ex. SEK 154–570k på 12 månader) används inte som mål förrän vi har egen mätdata.

## Tidigare underlag i repot som hör ihop med detta
`rapporter/gorillasports-se-genomlysning.md` (genomlysning 2026-10-09, utan trafikdata), `rapporter/titlar-lag-ctr.csv` (förslag på nya titlar och beskrivningar för blogginlägg med låg klickfrekvens), `rapporter/kategorisidor-underlag-2026-10-20.md` och `rapporter/kategoritexter-utkast-2026-10-20.md`. Gå igenom dem när en sida undersöks så att redan gjorda förslag inte görs om. Kolumnen `url_komplett` är ifylld för 13 av 35 sidor (de som inte var avkortade samt en som kunde matchas mot filerna ovan). S17 har flera möjliga träffar och ska bekräftas.
