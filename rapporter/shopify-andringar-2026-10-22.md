# Ändringar i Shopify 2026-10-22 (före och efter)

Godkända av David 2026-10-22: A (bloggartikeln), B (rensa spårningsparametrar i länkar), C (länka spinningcykel och motionscykel till varandra). Shopify har ingen ångra-funktion för kollektionstexter; "före"-texterna nedan är därför den enda återställningskällan. Alla ändringar görs med Shopify Admin API (articleUpdate och collectionUpdate) och bekräftas av David i verktygsprompten. Inget i temat ändras.

## A. Bloggartikeln `motionscyklar-eller-spinningcyklar-vi-forklarar-skillnaden` (Article 999686799745)
Före → efter:
1. Efter inledningsstycket (som slutar "…hur du vill använda cykeln.") läggs till: `<p style="text-align: left;"><strong>Hitta rätt cykel:</strong> Vill du ha jämn konditionsträning hemma, se våra <a href="https://www.gorillasports.se/collections/motionscykel-kondition">motionscyklar</a>. Vill du träna intervaller och högre intensitet, se våra <a href="https://www.gorillasports.se/collections/spinningcykel">spinningcyklar</a>.</p>`
2. Rubriken "FÖRDELAR OCH UTMANINGAR" (första, ovanför "Motionscyklar är perfekta…") → "MOTIONSCYKLAR: FÖRDELAR OCH UTMANINGAR".
3. Rubriken "FÖRDELAR OCH UTMANINGAR" (andra, ovanför "Spinningcyklar är byggda…") → "SPINNINGCYKLAR: FÖRDELAR OCH UTMANINGAR".
4. Sist i artikeln läggs samma länkblock som i punkt 1 till (efter stycket "Motionscyklar passar bäst… skonsam.").
Övrig text oförändrad.

## B. Spårningsparametrar i länkar (bara adressen ändras; länktext och mål är desamma)
Kollektionen `crosstrainer-kondition`:
- `…/collections/traningscykel-motionscykel-crosstrainer?_pos=1&_psq=kond&_ss=e&_v=1.0` → `…/collections/traningscykel-motionscykel-crosstrainer`
- `…/collections/kettlebell?_pos=2&_psq=kettle&_ss=e&_v=1.0` → `…/collections/kettlebell`

Kollektionen `motionscykel-kondition`:
- `…/products/motionscykel-x-frame-svart?_pos=1&_sid=9483fb7c1&_ss=r&shpxid=7e61fefc-2b97-4aba-85e1-300f7089224e` → `…/products/motionscykel-x-frame-svart`
- `…/products/motionscykel-spinning-spinningcykel-f25x50?_pos=1&_sid=fab878949&_ss=r&shpxid=f87eb789-5478-49e8-895d-1d7bd25eed23` → `…/products/motionscykel-spinning-spinningcykel-f25x50`
- `…/products/ergometer-motionscykel-90pro?_pos=21&_sid=20823dc7e&_ss=r` → `…/products/ergometer-motionscykel-90pro`
- `…/products/motionscykel-maxxus-recumbentcykel-4-2r?_pos=1&_sid=69f843a1f&_ss=r` → `…/products/motionscykel-maxxus-recumbentcykel-4-2r`

Kollektionen `stallbara-hantlar`:
- `…/collections/hantelstang?_pos=1&_psq=hantelst%C3%A4ng&_ss=e&_v=1.0` → `…/collections/hantelstang`

## C. Länkar mellan motionscykel och spinningcykel (bara tillägg, inget tas bort)
- Kollektionen `motionscykel-kondition`: i stycket "Spinningcyklar" (under "Olika typer av träningscyklar") läggs efter meningen "…intervaller och längre konditionspass." tillägget ` <a href="https://www.gorillasports.se/collections/spinningcykel">Se alla spinningcyklar</a>.` Den befintliga länken till enskild produkt behålls (utan parametrar, se B).
- Kollektionen `spinningcykel`: första stycket (slutar "…för både korta pass och längre intervaller.") får tillägget ` Vill du hellre ha jämn och skonsam konditionsträning? Se våra <a href="https://www.gorillasports.se/collections/motionscykel-kondition">motionscyklar</a>.`

## Utfört och kontrollerat (2026-10-22)
- **A** (artikeln), **B** och **C** är genomförda med Shopify Admin API (`articleUpdate` och `collectionUpdate`), efter Davids ja. Fyra kollektioner och en artikel uppdaterades. Tidpunkter (UTC): artikeln 06:38, crosstrainer 06:41, motionscykel 06:41 (rättad 06:59), spinningcykel 06:45 (rättad 06:49), ställbara hantlar 06:47 (rättad 06:48).
- **Fel som uppstod och rättades:** vid den första skrivningen av motionscykel, spinningcykel och ställbara hantlar skrev jag av texten med små avvikelser från originalet (bland annat "kvalitéer" blev "kvaléteter", "hantelstången" blev "hantelstangen", "viktskivorna" blev "viktskivor", "benträning" blev "bensträning", samt några hårda mellanslag blev vanliga). Jag upptäckte det genom en teckenvis jämförelse mot originalet, skrev om de tre sidorna med originaltexten och jämförde igen.
- **Slutkontroll** (teckenvis jämförelse av original och nuläge): bara de ändringar som godkänts finns kvar. Titel och metabeskrivning (SEO) är oförändrade på alla fyra kollektioner. Artikeln skiljer sig från originalet bara genom de två länkblocken och de två nya rubriknamnen.
- **Inte gjort (kräver Davids ja):** motionscykelns text säger "Fri frakt ingår på alla våra gym produkter" och crosstrainers text "Fri frakt på alla crosstrainers!"; gällande policy är fri frakt över 800 kr (David 2026-10-22), och all konditionsutrustning kostar mer än så. Förslag D: ändra motionscykelns mening till "Fri frakt gäller på alla ordrar över 800 kr." Metabeskrivningarnas "Gratis hemleverans" stämmer för dessa produkter och lämnas.
