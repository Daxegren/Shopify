# Verifiering Gymstick del 3 (c_skriv_resten_3) – BEST OF SPORTS (2026-11-02)

Oberoende kontroll, endast läsning. Inget ändrat i Shopify, inget committat.

## Metod
- `get-shop-info`: BEST OF SPORTS, bestofsports.se, SEK, Basic. Rätt butik.
- Skrivfil: `vag2_skriv/c_skriv_resten_3.json` (43 produkter, nr 3156–3226). Före-fil: `shopify-original-2026-11-02/vag2c_resten_3_fore.json` (43, alla ACTIVE).
- Live hämtat med `graphql_query` `nodes(ids)` i tre anrop (20 + 20 + 3): title, handle, status, tags, seo{title description}, descriptionHtml.
- Leveransblocket skrevs som platshållare vid avskrift av live-svaret. Blocket lästes i live-svaret för alla 43 och var identiskt med skrivfilens enda block (samma i alla 43), som i sin tur är identiskt med ett av blocken i `c_1_utkast.json`. Ingen produkt har varianten med "Beställningsvaror ...".
- Jämförelse programmatiskt: seo.title förväntas null när seo_title = titel; seo.description null när meta är null; html jämförd med normaliserade radbrytningar mellan taggar (matchade även utan normalisering). Taggar: före-taggarna ska finnas kvar och enda nya taggen ska vara `texter-klara`.

## Resultat: 43 av 43 matchar exakt
| nr | id | titel | seo.title | meta | html | ACTIVE | handle | tagg texter-klara | övriga taggar kvar | titel/SEO/meta tecken |
|---|---|---|---|---|---|---|---|---|---|---|
| 3156 | 10581109145866 | ja | ja | ja | ja | ja | ja | ja | ja | 41/41/null |
| 3157 | 10581109178634 | ja | ja | ja | ja | ja | ja | ja | ja | 40/40/null |
| 3160 | 10581109309706 | ja | ja | ja | ja | ja | ja | ja | ja | 33/33/null |
| 3161 | 10581109342474 | ja | ja | ja | ja | ja | ja | ja | ja | 35/35/null |
| 3164 | 10581109440778 | ja | ja | ja | ja | ja | ja | ja | ja | 45/35/151 |
| 3165 | 10581109473546 | ja | ja | ja | ja | ja | ja | ja | ja | 40/40/null |
| 3167 | 10581109604618 | ja | ja | ja | ja | ja | ja | ja | ja | 34/34/143 |
| 3168 | 10581109637386 | ja | ja | ja | ja | ja | ja | ja | ja | 33/33/null |
| 3174 | 10581109866762 | ja | ja | ja | ja | ja | ja | ja | ja | 42/35/148 |
| 3175 | 10581109932298 | ja | ja | ja | ja | ja | ja | ja | ja | 47/33/null |
| 3176 | 10581109965066 | ja | ja | ja | ja | ja | ja | ja | ja | 47/33/null |
| 3177 | 10581110030602 | ja | ja | ja | ja | ja | ja | ja | ja | 39/39/null |
| 3178 | 10581110063370 | ja | ja | ja | ja | ja | ja | ja | ja | 55/37/148 |
| 3179 | 10581110096138 | ja | ja | ja | ja | ja | ja | ja | ja | 53/35/154 |
| 3180 | 10581110128906 | ja | ja | ja | ja | ja | ja | ja | ja | 25/25/null |
| 3181 | 10581110161674 | ja | ja | ja | ja | ja | ja | ja | ja | 40/25/null |
| 3182 | 10581110194442 | ja | ja | ja | ja | ja | ja | ja | ja | 20/20/null |
| 3183 | 10581110227210 | ja | ja | ja | ja | ja | ja | ja | ja | 22/22/141 |
| 3185 | 10581110292746 | ja | ja | ja | ja | ja | ja | ja | ja | 23/23/null |
| 3188 | 10581110423818 | ja | ja | ja | ja | ja | ja | ja | ja | 36/36/null |
| 3189 | 10581110456586 | ja | ja | ja | ja | ja | ja | ja | ja | 51/32/148 |
| 3190 | 10581110522122 | ja | ja | ja | ja | ja | ja | ja | ja | 35/35/153 |
| 3193 | 10581110620426 | ja | ja | ja | ja | ja | ja | ja | ja | 24/24/136 |
| 3194 | 10581110653194 | ja | ja | ja | ja | ja | ja | ja | ja | 23/23/146 |
| 3196 | 10581110817034 | ja | ja | ja | ja | ja | ja | ja | ja | 34/31/141 |
| 3197 | 10581110882570 | ja | ja | ja | ja | ja | ja | ja | ja | 38/38/145 |
| 3198 | 10581110915338 | ja | ja | ja | ja | ja | ja | ja | ja | 40/40/133 |
| 3199 | 10581110948106 | ja | ja | ja | ja | ja | ja | ja | ja | 38/38/147 |
| 3203 | 10581111144714 | ja | ja | ja | ja | ja | ja | ja | ja | 42/28/154 |
| 3205 | 10581111210250 | ja | ja | ja | ja | ja | ja | ja | ja | 39/39/137 |
| 3207 | 10581111275786 | ja | ja | ja | ja | ja | ja | ja | ja | 30/30/143 |
| 3209 | 10581111374090 | ja | ja | ja | ja | ja | ja | ja | ja | 31/31/146 |
| 3210 | 10581111406858 | ja | ja | ja | ja | ja | ja | ja | ja | 41/41/154 |
| 3211 | 10581111439626 | ja | ja | ja | ja | ja | ja | ja | ja | 27/27/146 |
| 3212 | 10581111472394 | ja | ja | ja | ja | ja | ja | ja | ja | 31/31/145 |
| 3214 | 10581111570698 | ja | ja | ja | ja | ja | ja | ja | ja | 38/38/151 |
| 3215 | 10581111603466 | ja | ja | ja | ja | ja | ja | ja | ja | 38/38/144 |
| 3217 | 10581111701770 | ja | ja | ja | ja | ja | ja | ja | ja | 43/43/144 |
| 3219 | 10581111767306 | ja | ja | ja | ja | ja | ja | ja | ja | 38/38/141 |
| 3221 | 10581111931146 | ja | ja | ja | ja | ja | ja | ja | ja | 36/36/150 |
| 3223 | 10581111996682 | ja | ja | ja | ja | ja | ja | ja | ja | 40/40/151 |
| 3224 | 10581112029450 | ja | ja | ja | ja | ja | ja | ja | ja | 37/37/152 |
| 3226 | 10581112193290 | ja | ja | ja | ja | ja | ja | ja | ja | 34/34/null |
Tecken = längd på titel / SEO-titel (seo_title-fältet; lika med titeln när seo.title är null) / meta.

## Gränser
- Titel ≤ 70 tecken: alla (längst 55). Högst 2 kommatecken (decimalkomma i mått undantaget): alla.
- SEO-titel ≤ 43: alla (även där seo.title är null och titeln används; längst 43, på gränsen).
- Meta 130–155 eller null: alla. 28 har meta, 15 null.
- Dubbletter: inga dubbletter av titel, SEO-titel eller meta inom filen, och inga mot övriga `c_skriv_*.json` (produkter med samma id i samlingsfilerna räknades inte).

## kontrollera_produkttext.py
Kört på en kopia (html → beskrivning, leveransblocket inom `[[STANDARDBLOCK]]…[[/STANDARDBLOCK]]`, `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS"`).
- Med före-filen (titel + descriptionHtml) som källtext: **2 FEL**, `tal_utan_kalla` för artikelnumren 61260 (3181 Träningshjul) och 62018 (3182 Hopprep). Före-texten saknar SKU, men SKU finns i utkastets källfakta (`c_13_utkast.json`: "SKU 61260", "SKU 62018"). Felen är alltså falsklarm från källvalet, inte påhittade tal.
- Med före-filen + utkastens källfakta: **0 FEL**, 48 VARNINGAR: 43 × "saknar avsnittet 'passar dig som'" (rubriken heter "Passar för", samma mall som tidigare godkända vågor) och 5 × kort text under 40 ord (3160: 31, 3168: 36, 3165, 3174, 3217: 39). Tunn källa, redan flaggad i utkasten.

## Avvikelser live mot skrivfil
Inga. Titel, SEO-titel, meta, html, status ACTIVE, handle och taggar stämmer för alla 43; `texter-klara` finns på alla och inga befintliga taggar har försvunnit.

## Språkfynd (förslag, inget ändrat)
Inga stavfel, inga arbetstermer ("enligt källan/titeln"), inga FAQ och inga påhittade hälso-, miljö- eller ursprungspåståenden hittades. Hälsopåståenden i källan (rehabilitering, triggerpunktsterapi, blodcirkulation, hållning, "miljövänligt" om korkmattan) är utelämnade. Fynden nedan är grammatik och stil.

### Bör rättas
1. **3221 meta, första meningen saknar verb.**
   Före: "Träningshandskar från Gymstick i svart-grå färg, i storlekarna XS, S, M och L. Enligt tillverkaren är de designade för komfort och förbättrar greppet."
   Efter: "Gymstick träningshandskar finns i svart-grå färg och i storlekarna XS, S, M och L. Enligt tillverkaren är de designade för komfort och förbättrar greppet." (154 tecken)
2. **3224 meta, första meningen saknar verb.**
   Före: "Träningshandskar från Gymstick i rosa-svart färg, i storlekarna S, M och L. Enligt tillverkaren är de designade för komfort och stöd under träningspass."
   Efter: "Gymstick träningshandskar finns i rosa-svart färg i storlekarna S, M och L. Enligt tillverkaren är de designade för komfort och stöd under träningspass." (152 tecken)
3. **3221 och 3224, första meningen i beskrivningen saknar verb.**
   Före: "Gymstick träningshandskar i svart-grå färg." / "Gymstick träningshandskar i rosa-svart färg."
   Efter: "Gymstick träningshandskar finns i svart-grå färg." / "Gymstick träningshandskar finns i rosa-svart färg."
4. **3207, fel possessivpronomen.**
   Före: "Dig som vill komplettera sin befintliga träningsutrustning, enligt tillverkaren"
   Efter: "Dig som vill komplettera din befintliga träningsutrustning, enligt tillverkaren" (jämför 3214 "ditt vanliga träningsprogram")
5. **3193, adjektiv utan substantiv.**
   Före: "Nybörjare och erfarna, enligt tillverkaren"
   Efter: "Nybörjare och erfarna utövare, enligt tillverkaren" (samma formulering som 3212)
6. **3212 meta, samma sak.**
   Före: "... för både nybörjare och erfarna."
   Efter: "... för både nybörjare och erfarna utövare." (153 tecken)
7. **3205 meta, upprepning tillverkaren/tillverkad.**
   Före: "Enligt tillverkaren är den tillverkad av slitstarkt material."
   Efter: "Enligt tillverkaren är den gjord av slitstarkt material." (132 tecken)

### Stil, kan rättas (cirkulära inledningar "X är en X")
Samma ord står i produktnamnet och i typordet direkt efter "är". Förslagen behåller samma fakta.
8. 3178 Före: "Gymstick Pro Träningsmatta NBR är en svart träningsmatta på 140 x 60 x 1,0 cm." Efter: "Gymstick Pro Träningsmatta NBR är svart och mäter 140 x 60 x 1,0 cm." (gäller även meta, första meningen)
9. 3179 Före: "Gymstick Pro Träningsmatta NBR är en grå träningsmatta i NBR som mäter 170 x 60 cm och är 1,5 cm tjock." Efter: "Gymstick Pro Träningsmatta NBR är grå, mäter 170 x 60 cm och är 1,5 cm tjock." (NBR står också två gånger; gäller även meta)
10. 3180 Före: "Gymstick Pro Träningsband är ett träningsband för styrka, flexibilitet och dynamisk uppvärmning." Efter: "Gymstick Pro Träningsband används för styrka, flexibilitet och dynamisk uppvärmning."
11. 3183 Före: "Gymstick Pro Hex Hantel är en hantel med sexkantig form." Efter: "Gymstick Pro Hex Hantel har sexkantig form." (gäller även meta)
12. 3185 Före: "Gymstick Pro Kettlebell är en kettlebell för styrke- och konditionsträning." Efter: "Gymstick Pro Kettlebell används för styrke- och konditionsträning."
13. 3188 Före: "Gymstick Pro Gummigolv är ett gummigolv på 100 x 100 cm." Efter: "Gymstick Pro Gummigolv mäter 100 x 100 cm."
14. 3189 Före: "Gymstick Pro Gummigolv är ett svartgrått gummigolv på 100 x 100 cm med tjockleken 0,8 cm." Efter: "Gymstick Pro Gummigolv är svartgrått, mäter 100 x 100 cm och är 0,8 cm tjockt." (gäller även meta)
15. 3193 Före: "Gymstick Pro Vinyl Hantel är en hantel med vinylbeläggning." Efter: "Gymstick Pro Vinyl Hantel har vinylbeläggning." (gäller även meta)
16. 3194 Före: "Gymstick Pro TPU Hantel är en hantel med TPU-beläggning." Efter: "Gymstick Pro TPU Hantel har TPU-beläggning." (gäller även meta)
17. 3219 Före: "Gymstick Tatamimatta är en matta på 105 x 105 x 2 cm." Efter: "Gymstick Tatamimatta mäter 105 x 105 x 2 cm." (gäller även meta)

Om meta ändras enligt 8, 9, 11, 14–17 ska längden (130–155) kontrolleras på nytt.

### Övrigt att notera
- 3215: meta kallar produkten "träningsyta", beskrivning och titel "balanskudde". Förslag på meta: "Gymstick Stability Air Pad är en balanskudde för balans och bålstyrka. Enligt tillverkaren passar den för grundläggande och avancerade övningar." (144 tecken). Typen balanskudde är en tolkning (flaggad i utkastet).
- 3165: "Bollen är 20 cm." är vagt; källan säger "20 cm stora boll". Förslag: "Bollen är 20 cm stor."
- 3179 meta: "Mattan passar för yoga, pilates och styrketräning." står utan "enligt tillverkaren", till skillnad från de flesta andra metatexter. Har stöd i källan, så det är ett val av ton.
- 3224: "crossfit" är ett varumärke (CrossFit). Det kommer från källan och kan stå kvar eller bytas mot "funktionell träning".
