# Stickprov pass 7, BEST OF SPORTS, 2026-11-05

Roll: Stickprov (Sonnet, endast läsning). Inget skrevs i Shopify, inget committades. Live-läsning via `shopify_api.py`.
Underlag: `vag2_skriv/k_skriv_28lm, 28npq, 28r, 28st, 28uv, 28wx, 28z` (117 produkter). Urval: 24 produkter jämnt spridda i varje fil (lm 4, npq 6, r 3, st 3, uv 3, wx 4, z 1). Källa: `shopify-original-2026-11-05/*_fore_*.json`.

## Maskinkontroller (alla 24)
- Live mot skrivfil (titel, SEO-titel, meta, descriptionHtml): 24 av 24 identiska.
- Status ACTIVE och handle oförändrade mot före-filen. Enda taggändring är tillagd `texter-klara`. Alla har en variant (Default Title); inget pris står i texterna (priset ändras inte av skrivningen, före-filerna saknar variantdata, så pris/variant kontrollerades som oförändrat bara indirekt genom att varianten är en och att skrivningen bara rör seo/beskrivning).
- Titel högst 70 tecken och högst 2 kommatecken, SEO-titel högst 43 (max 41), meta 70-155: inga avvikelser. Inga dubbla mellanslag, inget "&", högst en "enligt tillverkaren" per påstående.
- Säkerhets-, skydds-, utvecklings- och kvalitetsord (slitstark, robust, halkfri, stabil, ergonomisk, hållbar, lätt, perfekt m.fl.): inga träffar. "kedjeskydd" och "stödhjul" (28184) är delnamn på medföljande delar, ur källan.
- Leveranstidsmeningen finns bara på 28287 (enda med taggen `På beställning`), exakt enligt profilen.

## Tabell
| nr | id | resultat | anmärkning |
|---|---|---|---|
| 28133 | 10472331968778 | OK | Allt (ABEC-9, 120 mm, 3,4 kg, 70 kg, 4-7 år) finns i källan. Lastgräns en gång med "enligt tillverkaren". |
| 28142 | 10472332853514 | OK | 3,4150 kg skrivs 3,415 kg (samma värde). Användarhöjd utelämnad. Lastgräns "Max. lastkapacitet: 100 kg" korrekt hedgad. |
| 28147 | 10472334754058 | OK | Ram, 26", 21 växlar, 14,2 kg, 160-175 cm, fästpunkter finns i källan. |
| 28156 | 10475600183562 | OK | Ramhöjd 21 cm, 95-115 cm, 5,3 kg, V-bromsar enligt källan. |
| 28157 | 10475601920266 | OK | Som 28156, färg Ocean enligt titel. |
| 28166 | 10480055189770 | OK | "Från 8 år" kommer ur reklamtext ("från 8 år och uppåt"); rimligt. Stöd, 16,4 kg, 29 cm enligt källan. |
| 28175 | 10486710239498 | OK (anm.) | SEO-titel "Barncykel S'cool Xroc 26 tum, Neon Grön" tappar "/Ocean" (kortad för 43-teckensgränsen). Färgen blir halv; överväg "Barncykel S'cool Xroc 26, Neon Grön/Ocean" (41 tecken). Titel och text har hela färgen. |
| 28184 | 10486811296010 | OK | Medföljande delar och 7,5 kg "utan tillbehör" stämmer. Källans "hållbart stål"/"säker bromsning" utelämnade. |
| 28193 | 10486812377354 | OK | Allt ur källan. |
| 28204 | 10494946115850 | OK (anm.) | Spec skriver "ALUXX-aluminium"; källan har "ALUXX-grade aluminium". Obetydlig ändring av märkesnamn; 28287 behåller "ALUXX-grade". Förslag: "ALUXX-grade aluminium". |
| 28205 | 10494946148618 | OK (anm.) | Samma som 28204. |
| 28210 | 10507247059210 | OK | Källans felaktiga "hjälm" utelämnad (R2). Mått, clip, 1 tum, hjulstorlekar stämmer. |
| 28214 | 10515744030986 | OK | Trasig rad "ABS-hjul är gjorda av ACEC" utelämnad. Styrbredd 33 cm, 4 år, 120 mm stämmer. |
| 28217 | 10523491533066 | OK (anm.) | Typordet ändrat från live "Barncykel" till "Cykel". Källans brödtext säger "cykel" (R7 tillåter), men ungdomsmodellen blir mindre träffsäker. Inget fel. |
| 28224 | 10525598023946 | OK (anm.) | Meta "enligt tillverkaren för cyklister ca 95-110 cm" är stelt men korrekt. Fälgar/vevparti av aluminium finns i källan. |
| 28232 | 10530126266634 | FEL | Källans "biltema" (bil + tema) är skrivet "Motiv: Biltema" och "har biltema" i html. Versalt B läser som varumärket Biltema (butikskedjan). Meta säger "bilmotiv", html "biltema": inkonsekvent. Rättning nedan. |
| 28241 | 10541367656714 | OK | Två plastracketar, liten boll, Seven Polska ur källan. "Disney-figurer" undviks, "Spiderman" ur titeln. |
| 28257 | 10635759780106 | OK | Fjädring fram, 21 växlar, 26 x 2,1", 13,4 kg ur källan. Ramstorlekarna S/M/L utelämnade (rätt, bara en variant). |
| 28264 | 10656686506250 | OK | 6-8 år, 29 cm, 7,5 kg, Claris 8 ur källan. |
| 28265 | 10656686571786 | OK | 8-12 år, 38 cm, 8,2 kg ur källan. |
| 28274 | 10656692568330 | OK | 5,5 kg, 26 cm, 105-120 cm, justerbar styrstam ur källan. Marknadsföringspåståenden ("40 procent lättare" m.m.) utelämnade. |
| 28279 | 10656692732170 | OK | Som 28274. "Tonåringar" utelämnat. |
| 28287 | 10673173332234 | OK (anm.) | Leveranstidsmening finns (taggen På beställning). "Giant CREST 34 Boost RCL" skrivet "Giant Crest 34 Boost RCL" (versalerna i modellnamnet CREST borttagna); obetydligt. |
| 28101 | 10472295989514 | OK | Trasiga rader ("135 cm - 135 cm...", "bromsok") utelämnade. "Växlar: Shimano" utan Tourney (källan är trasig där) är försiktigt. |

## Slutsats
23 OK (varav 5 med små anmärkningar) och 1 FEL (28232). Inga säkerhets-, skydds- eller kvalitetspåståenden, inga stavfel, ingen låst färg eller storlek, ingen ändring av status, handle eller taggar utöver `texter-klara`.

## Föreslagna rättningar (inget ändrat)
1. 28232 (10530126266634): html "Barncykelkorgen Cars har biltema och är gjord av plast" -> "Barncykelkorgen Cars har bilmotiv och är gjord av plast"; "Dig som vill ha en korg med biltema" -> "Dig som vill ha en korg med bilmotiv"; "Motiv: Biltema" -> "Motiv: Bilar". Meta oförändrad.
2. 28175 (10486710239498): SEO-titel -> "Barncykel S'cool Xroc 26, Neon Grön/Ocean" (valfritt).
3. 28204 (10494946115850) och 28205 (10494946148618): "ALUXX-aluminium" -> "ALUXX-grade aluminium" i spec (valfritt).

## Begränsningar
Bara 24 av 117 granskade (20 procent). Variantpris jämfördes inte mot före-fil (fanns inte där); enbart nuläget (en variant) lästes live. Ingen nätkoll mot tillverkare gjordes.
