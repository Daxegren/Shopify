# Stickprov läsning grupp 13 (cykellås), 2026-11-03

Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info. Endast läsning, inget skrivet.
Urval: 20 av 57. 13a: nr 8638, 8641, 8644, 8647, 8648, 8651, 8655, 8660, 8664, 8668 (index 0,3,6,9,10,12,14,18,22,26). 13b: nr 8671, 8675, 8679, 8682, 8686, 8690, 8693, 8695, 8697, 8701 (index 0,3,6,9,12,15,18,20,22,26).
Metod: live via graphql_query (nodes, 2-4 produkter per anrop), jämfört i python mot skrivfilen: titel, SEO-titel (null godtagen när lika med titeln), meta, descriptionHtml före standardblocket (teckenvis). Standardblocket (Leverans, retur, garanti, Säljare) jämfört med ögat, det var identiskt i alla 20 (13b nr 8671 har meningen om beställningsvaror, avsett). Tal i meta och html kontrollerade mot före-filerna.

## Resultat
- Titel, SEO-titel, meta, html (före standardblocket): 20 av 20 identiska med skrivfilen. Inga handtranskriberingsfel. Status ACTIVE på alla 20. Ingen SEO-titel över 43 tecken, meta 85-155 tecken (ingen över 155).
- Tal och fakta: alla tal finns i före-filerna. Säkerhetsnivåer och certifieringar står en gång per text och som "enligt tillverkaren" (8644, 8647, 8655, 8660, 8664, 8668, 8671, 8675, 8697, 8701). Kontrollerade uppgifter (zinkkapslar, M-nyckellås, polyesterhölje, Sold Secure m.fl. på 8668, anodiserad klämma, Kraton, neopren, hjälmar, skyddslock, inomhus/utomhus) finns i källan. Inga påhittade uppgifter hittades. Stavning: inga fel. Nr 8693 har "neoprenskydd" rättat.
- Nr 8701: SEO-titel lagras som null (lika med titeln), avsett. Meta finns.

## Avvikelser
1. **Osynligt tecken, nr 8647 (Vikbart Lås AXA Fold Lite 80, id 10472233107722).** Live innehåller descriptionHtml ett mjukt bindestreck (U+00AD) i ordet "remmar" på två ställen. Skrivfilen har ingen U+00AD (0 träffar i alla b_skriv_13*-filer och före-filerna).
   - Före (live): `...eller med medföljande rem­mar</li>` och `<li>Hållare: För cykelramen, medföljande rem­mar ingår</li>` (med U+00AD mellan "rem" och "mar")
   - Efter (skrivfil): `...medföljande remmar` och `medföljande remmar ingår`
   Sågs vid två separata läsningar. Verktygsutdata går inte att tecken-testa i kod, så fyndet bör bekräftas med ett skript som läser live och räknar U+00AD. Åtgärd: skriv om descriptionHtml för 8647 från skrivfilen och läs tillbaka. Övriga 19 inga osynliga tecken (bedömt på läsningen).
2. **Taggen texter-klara saknas på 6 av 10 i 13a:** 8648, 8651, 8655, 8660, 8664, 8668. De första fyra stickprovsprodukterna (8638, 8641, 8644, 8647) och alla 10 i 13b har taggen. Texterna är redan skrivna och rätt, bara taggen saknas, så sannolikt är taggningssteget inte klart för 13a (övriga ej taggade är ej kontrollerade). Rekommenderad åtgärd: tagga alla skrivna 13a-produkter, kontrollera resten av 13a med fråga på taggen.

Inga andra avvikelser.
