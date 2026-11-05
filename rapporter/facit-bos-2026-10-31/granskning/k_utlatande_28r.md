# Granskning k_28r (barn och ungdom, 9 utkast och 3 avvisade)

Granskare: oberoende Opus, bara läsning. Datum 2026-11-05. Butik bekräftad via Admin API (`shop`): BEST OF SPORTS, 6f2e53-67.myshopify.com. Shopify-verktyget (MCP) var frånkopplat; källan lästes live med `shopify-sync/scripts/shopify_api.py` (title, handle, status, productType, vendor, tags, descriptionHtml, seo, variants). Inget ändrades i Shopify.

Underlag: regelbok v1.8, beslutsloggen (barn frisläppt 2026-11-05, endast fakta), profilens `frislappta_2026_11_05`, LARDOMAR.md, granskarmallen `c_granskarprompt.md`. Maskinellt: `skrivfil_kontroll.py` 0 fel och 0 varningar (även på en rättad kopia); titel ≤70 tecken och ≤2 kommatecken, SEO-titel ≤43, meta 95–151 tecken med verb, standardblock exakt som `b_skriv_24.json`, "Passar för" finns, högst två "enligt tillverkaren", ingen tagg "På beställning", titel/SEO/meta unika mot alla andra JSON-filer i `vag2_skriv/` (inklusive `k_skriv_*.json` och övriga utkast). Butiken söktes efter syskon (Sidepull, Spencer, flaX, Retro Runner, Jolene 20): inga dubbletter.

**Resultat: 7 GODKÄND, 2 RÄTTA, 0 UNDERKÄND.**

| nr | id | dom | skäl |
|---|---|---|---|
| 28205 | 10494946148618 | GODKÄND | Live (API 2026-11-05): ACTIVE, 'Ultralätt barncykel GIANT ARX 16, Cobalt', variant Default Title/1011002210/7769 kr. ALUXX-grade aluminium (skrivs ALUXX-aluminium som 28203), ramstorlek 38 cm, ca 105–125 cm (en gång enligt tillverkaren), 1 växel, V-bromsar och ca 7 kg stämmer. 'Ultralätt', 'lättaste i sin klass', 'stabil ramgeometri', däckpåståendet och 'världens största' är borta. 16 och Cobalt ur live-titeln. Unik mot 28181/28203/28204/28206. |
| 28206 | 10494946214154 | GODKÄND | Live (API 2026-11-05): ACTIVE, 'Ultralätt barncykel GIANT ARX 16, Lime Punch', variant Default Title/1011002410/7769 kr. Samma källdata som 28205 (källan stavar 'Rammstorlek', 38 cm entydigt). Alla uppgifter stämmer, marknadsord borta, färg ur live-titeln. Unik. |
| 28207 | 10494946279690 | GODKÄND | Live (API 2026-11-05): ACTIVE, "Scooter S'COOL flaX 8.3, Mörkgrå/Gul", variant Default Title/2514/2649 kr. Hopfällbar, höjdjusterbart styre, styrhöjd 870–970 mm, aluminiumram, hjul PU 200x40 och ABEC-7 stämmer. 'Maximal belastning: 100 kg' är svensk ordagrann rad med etikett och enhet (R4), en gång enligt tillverkaren. Fotbromsen nämns inte i titel, meta eller html (kontrollerat). 'Utvecklats för aktiva barn', 'anpassar sig perfekt' och 'praktiskt transportmedel' borta. Sparkcykel är källans eget ord (R7). Ingen dubblett: flaX 8.4/8.5 arkiverade, 8.6 annan modell. |
| 28209 | 10503204208906 | GODKÄND | Live (API 2026-11-05): ACTIVE, 'Balanscykel EXCELSIOR Retro Runner, 12" blå', variant Default Title/02130226/3499 kr. Stålram, saknar pedaler, justerbart styre och sadelhöjd, ca 90–110 cm och 3,2 kg stämmer. 'Lastkapacitet: 45 kg' är svensk ordagrann rad (R4); två 'enligt tillverkaren' totalt (R5). Utvecklingspåståenden ('lära sig cykla', 'öva balans', 'växer med barnet') och ursprunget '(Tyskland)' borta. 12 tum och blå ur live-titeln. Cream-utförandet (10502526238986) är DRAFT och annan färg: ingen dubblett. |
| 28210 | 10507247059210 | RÄTTA | Live (API 2026-11-05): ACTIVE, 'Främre korg för barncykel SPENCER 16-24″, metall, vit', variant Default Title/EK-SP029-V/159 kr, productType Tillbehör, tagg Cykelkorg. 'Hjälm fram' är en felöversättning: live-titeln ('Främre korg'), taggen, nästa mening ('Cykelkorgen fästs med ett clip'), måtten 25 x 17 x 18 cm, priset och syskonen (Röd, Rosa, Svart) visar alla en korg. Det är ingen hjälm; raden är rätt utelämnad (R2). Hjulstorlekar, clip, 1 tums gaffelrör, alla delar ingår, metall och vit stämmer; 'mellan styrkronorna' rätt utelämnad. Rättning: '1 tums gaffelrör' blir '1-tums gaffelrör' på två ställen i html (R10, som skrivna syskonet 28044). '24 tums hjul' lämnas som i 28044/28045. |
| 28211 | 10507291820298 | GODKÄND | Live (API 2026-11-05): ACTIVE, 'Barncykel ROMET Jolene 20 KID 2, vit-blå-rosa', variant Default Title/20100748-A/5899 kr. Aluminiumram, S (10"), ca 115–135 cm, 6 växlar Shimano, V-bromsar och fästpunkter stämmer. Vikten är rätt utelämnad: egen källa säger bara 'Hjulvikt: 10,3 kg' (otydlig etikett, praxis 28159/28170/28173); syskonet 28212:s 'Cykelns vikt' får inte lånas (R1). 'Shimano Touring' rätt reducerad till Shimano. Säkerhets-, komfort- och 'för flickor'-påståenden borta. Anm.: SEO-titeln kortar färgen till Vit-Blå (Rosa ryms inte); godtas enligt praxis 28165 (färg kortad i SEO), unik mot 28212. |
| 28212 | 10507294474506 | GODKÄND | Live (API 2026-11-05): ACTIVE, 'Barncykel ROMET Jolene 20 KID 2, grå-rosa', variant Default Title/20100749-A/5899 kr. Aluminiumram, S (10"), ca 115–135 cm, 6 växlar, V-bromsar, 'Cykelns vikt: 10,3 kg' och fästpunkter stämmer. Shimano Tourney står ordagrant i inledningen och på egen rad; 'Shimano Touring' är en trasig rad och Tourney den entydiga delen (R2). Den trasiga måttraden och 'främre stänkskärm' rätt utelämnade. Marknadsord borta. |
| 28213 | 10515742064906 | RÄTTA | Live (API 2026-11-05): ACTIVE, 'Flaskhållare GIANT ARX SIDEBULL (R), svart', variant Default Title/490000145/89 kr. Sidepull är rätt: källtexten och handle (...-sidepull-r-svart-...) säger Sidepull; SIDEBULL är stavfel i live-titeln. Nylon, 27 g och 'för ARX-serien av barncyklar' stämmer; trasiga '27X'-raden och Giant-texten rätt utelämnade. Rättningar: (1) '(R)' ska stå kvar i titel, SEO och Modell: butiken har Giant/Liv Airway Sidepull i både (R)- och (L)-utförande och skrivna texter behåller beteckningen (8094 'Sidepull (L)', 'Giant Airway Sport Sidepull (R)'); (2) meta saknar typordet och börjar 'Giant ARX Sidepull i svart' i stället för 'Flaskhållaren ...'. Ny titel/SEO 42 tecken, meta 117. |
| 28214 | 10515744030986 | GODKÄND | Live (API 2026-11-05): ACTIVE, 'Scooter RIDEOO 120 City Scooter Lila', variant Default Title/4751036030740/2969 kr. Hopfällbar, höjdjusterbart styre, polyuretanhjul, 120 mm, ABEC-9, styrbredd 33 cm, 3,4 kg och från 4 år (en gång enligt tillverkaren) stämmer. 'Dämpar åkturen' och 'ABS-hjul ... ACEC-hjul' rätt utelämnade. Typord Sparkcykel som skrivna syskon 28076/28097/28130/28133. Unik. |

## Rättningar (exakt)

**28210** html: `Korgen fästs med ett clip och passar 1 tums gaffelrör.` → `Korgen fästs med ett clip och passar 1-tums gaffelrör.` samt `<li>Cyklar med 1 tums gaffelrör</li>` → `<li>Cyklar med 1-tums gaffelrör</li>`.

**28213**
- titel: `Flaskhållare Giant ARX Sidepull, Svart` → `Flaskhållare Giant ARX Sidepull (R), Svart`
- seo_title: `Flaskhållare Giant ARX Sidepull, Svart` → `Flaskhållare Giant ARX Sidepull (R), Svart`
- meta: `Giant ARX Sidepull i svart är gjord av nylon, väger 27 g och är avsedd för barncyklar i ARX-serien.` → `Flaskhållaren Giant ARX Sidepull (R) i svart är gjord av nylon, väger 27 g och är avsedd för barncyklar i ARX-serien.`
- html: `<li>Modell: Giant ARX Sidepull</li>` → `<li>Modell: Giant ARX Sidepull (R)</li>`

Fullständiga före/efter-strängar (hela html) finns i `vag2_skriv/k_utlatande_28r.json`.

## Avvisade (k_28r_avvisade.json): alla tre rätt avvisade, inget lyfts ur

| nr | id | bedömning |
|---|---|---|
| 28208 | 10502528008458 | Live: 'Canopy frame CARGOBIKE Canopy Framework 2-kids för Classic', tom beskrivning. Tunn källa (R3) och barntransport (ram till kalesch för två barn på lastcykel, som Svensson Family). Rätt avvisad. |
| 28215 | 10515754516746 | Live: 'Scooter Rideoo 120 City Scooter med LED-belysning'. Källan har fakta (ABEC-9, 120 mm, 3,4 kg, 4–7 år, 'upp till 70 kg') men nämner varken LED eller färg; titelns särdrag saknar stöd (R3) och belysning ligger fortfarande utanför. Rätt avvisad. |
| 28216 | 10523491434762 | Live: 'Träningshjul GIANT Steel Träningshjul, 16"-', tom beskrivning. Tunn källa (R3); stödhjul är dessutom en bärande del utan lastgräns. Rätt avvisad. |

## Särskilda punkter
- 28207: fotbromsen nämns ingenstans i utkastet.
- 28210: "hjälm fram" är en felöversättning; produkten är en korg (live-titel, tagg, nästa mening, mått, pris och syskon).
- 28213: Sidepull är rätt (källtext och handle); "(R)" ska behållas som i butikens övriga Sidepull-hållare.
- 28211: den utelämnade vikten är rätt ("Hjulvikt" är en otydlig etikett, och syskonets vikt får inte lånas).

## Öppna frågor till David
Inga nya.
