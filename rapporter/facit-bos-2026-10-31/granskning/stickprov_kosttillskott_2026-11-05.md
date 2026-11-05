# Stickprov kosttillskott och cykeldelar (v1.10), BEST OF SPORTS, 2026-11-05

Roll: Stickprov (Sonnet, endast läsning). Inget skrevs i Shopify, inget committades. Live-läsning via `shopify_api.py`.
Underlag: `vag2_skriv/k_skriv_32i33a` (11), `k_skriv_33b` (7), `k_skriv_33c` (7), `k_skriv_korr10` (2). Urval: ALLA 27. Före-läge: `shopify-original-2026-11-05/k_skriv_32i33a/33b/33c_fore_dry-run.json` och `korr10/k_skriv_korr10_fore_rest.json`.

## Maskinkontroller (alla 27)
- Live mot skrivfil (titel, meta, descriptionHtml): 27 av 27 identiska tecken för tecken. SEO-titel (effektiv, null = titeln): 27 av 27 lika.
- Status ACTIVE och handle oförändrade mot före-filen i alla 27. Taggar: enda skillnad är tillagd `texter-klara` i 25 (32019-33031); 32069 och 32070 hade den redan före korr10 och är oförändrade.
- SEO-titel högst 43 tecken (max 43), meta 109-154 tecken, inga dubbla mellanslag, inget '&': inga avvikelser.
- Ej känd: rad i spec plus mening i brödtext och meta i alla 5 cykel- och träningsprodukter utan lastgräns (32019, 32036, 32040, 32069, 32070; 32040 har meningen 'för modellen' i meta).  Ingen av de 22 andra har lastuppgift.
- Lastgräns 5 kg finns bara i 32037 (Basil), i meta, brödtext och spec, med 'Enligt tillverkaren'. Inga kg-värden i övriga 26.
- Hälso-/effektord (sökt: hjälp, stöd, bidra, främj, förbättr, öka, minsk, energi, uthåll, prestation, koncentration, fokus, minne, sömn, led, hud, libido, stress, immun, lever, vitalitet, hälsa, optimal, slitstark, robust, stabil, säker, hållbar): inga träffar i titel, meta, brödtext, Passar för eller spec. Ord som 'Energigel', 'Energidryck' (produkttyp, beslutat), 'sömntabletter' och 'före sänggåendet' (läkemedels- och användarvarningar) är inte påståenden. 'kroppsviktsträning' är aktivitet.
- Doser: alla dosuppgifter stämmer mot före-texterna (se tabell). Inga doser är låsta till fel portion.
- Stavfel och grammatik: inga fel hittades.

## Tabell
| nr | id | resultat | anmärkning |
|---|---|---|---|
| 32019 | 10472241168650 | OK | Ej känd-rad och mening finns i brödtext, meta och spec. Inga påståenden. |
| 32036 | 10472294940938 | OK | Ej känd-rad och mening finns. Vikt 355 g och singularform borta enligt utlåtandet. Titelns 'Dubbelsidiga' med versal efter komma är en stilfråga (SEO-titel utan). |
| 32037 | 10475424284938 | OK | Enda produkten med lastuppgift: 'Enligt tillverkaren ... 5 kg' en gång i meta och en gång i brödtext, plus spec. Ingen Ej känd-rad (rätt). 5 kg förekommer inte i någon annan av de 27. Typordet Styrstamshållare väntar fortfarande på Davids bekräftelse i profilen. |
| 32040 | 10494687805706 | OK | Ej känd-rad och mening finns. 'Slitstark', 'underhållsfria' och vikt 325 g borta. Mått 86,5 x 77,5 mm stämmer med före-texten. |
| 33002 | 10462770135306 | OK | Dos 50 ml stämmer med före-texten ('eller enligt instruktionen på flaskan'). Inga effektord. 'Konsumeras inte före sänggåendet' är en varning, inget sömnpåstående. |
| 33003 | 10462770299146 | OK | Som 33002. Dos 50 ml och 30 min före träning stämmer med före-texten. |
| 33005 | 10462777770250 | OK | 1 kapsel dagligen, helst före frukost: stämmer. Före-textens ginsengpåståenden borta. |
| 33007 | 10462778589450 | OK | 1 kapsel dagligen, rikligt med vatten: stämmer. Leverpåståenden borta. |
| 33009 | 10470944768266 | OK | 500 mg niacin per kapsel och 1 kapsel med eller efter måltid: stämmer. Energi-, trötthets- och hudpåståenden borta. |
| 33010 | 10471287783690 | OK (anm.) | Ingen dosrad. Före-texten anger 15 ml, som utelämnats (inget fel portionsvärde i texten). Samma val i 33027-33029, medan 33031 behåller 15 ml. Förvaring 2-25 C stämmer. |
| 33011 | 10472269873418 | OK | 1 kapsel 3 gånger dagligen (3 kapslar/dag), cirka 300 ml vatten, rådgör med läkare: stämmer. Prestations- och minnespåståenden borta. |
| 33012 | 10472270004490 | OK | 1 kapsel dagligen, helst före frukost eller 30 min före träning: stämmer. Titelns typord Koffein enligt utlåtandet. |
| 33014 | 10472277213450 | OK | 1 kapsel en gång dagligen cirka 30 min före måltid: stämmer. Led-, brosk- och hudpåståenden borta. |
| 33018 | 10472280719626 | OK | 1 kapsel dagligen efter måltid, 50 % bacosider: stämmer. Minnes- och koncentrationspåståenden borta. |
| 33019 | 10472280785162 | OK | 28,2 mg withanolider per kapsel (enligt tillverkaren) och 1 kapsel till måltid: stämmer. Sömn-, libido- och stresspåståenden borta. |
| 33020 | 10472297693450 | OK | Portion 60 ml, upp till 3 per dag = 180 ml: stämmer. 'Energigel' är produkttyp (beslutat). Obs-raden nämner 'före sänggåendet' som varning. |
| 33021 | 10472297824522 | OK | Upp till 1 kapsel per dag, helst till måltid, 250 ml vatten: stämmer. 'Sömntabletter' står bara i läkemedelsvarningen. |
| 33022 | 10472302018826 | OK (anm.) | Dos stämmer. Förvaring skriver '15-25 grader' (övriga '°C'), och ingredienslistan har källans stavning 'vitanolider' (övriga 'withanolider'). Båda är källtrogna och ofarliga. |
| 33023 | 10472323088650 | OK (anm.) | Ingen dosrad (före-texten anger 50 ml, inte en rimlig portion för 500 ml-flaska, så utelämnandet är rimligt). Obs-raden saknar slutpunkt. 'Energidryck' är produkttyp. |
| 33025 | 10472351203594 | OK (anm.) | 1 kapsel dagligen till måltid: stämmer. Obs-raden saknar slutpunkt. Andra Passar för-raden börjar 'Vegetarianer' i stället för 'Dig som' (källtrogen, ingen påstående). |
| 33026 | 10635764334858 | OK (anm.) | 2 kapslar dagligen med mat: stämmer. Led- och benhälsa-påståenden borta. Obs-raden saknar slutpunkt. |
| 33027 | 10656694042890 | OK (anm.) | Ingen dosrad (före-texten anger 15 ml, utelämnad). 30 min före träning stämmer. Energi-, uthållighets- och blodflödespåståenden borta. |
| 33028 | 10656694075658 | OK (anm.) | Som 33027. |
| 33029 | 10656694141194 | OK (anm.) | Som 33027. |
| 33031 | 10656694206730 | OK (anm.) | Portion 15 ml, 45 ml/dag (3 portioner) före, under eller efter träning: stämmer med före-texten och inte låst till fel portion. Obs-raden saknar slutpunkt. |
| 32069 | 10581109408010 | OK | Ej känd-rad och mening finns (beslut 2026-11-05: endast återförsäljarkälla). 120 kg från före-texten är borttaget överallt. Tagg texter-klara fanns redan före. |
| 32070 | 10581109670154 | OK | Ej känd-rad och mening finns; 140 kg/Maximal användarvikt borta. 'kroppsviktsträning' är aktivitet, inget påstående. Tagg texter-klara fanns redan före. |

## Sammanfattning
27 av 27 OK, 0 FEL. Anmärkningar (ingen kräver rättning):
1. Dosrad utelämnad i 33010, 33023 och 33027-33029 trots att före-texten har dos (15 ml respektive 50 ml), medan 33002, 33003 och 33031 har den. Rimligt val men ojämnt; beslut om enhetlig linje kan tas senare.
2. Obs-raden saknar slutpunkt i 33023, 33025, 33026 och 33031 (övriga har). Kosmetiskt.
3. 33022: '15-25 grader' mot '°C' i övriga, och 'vitanolider' (källstavning) mot 'withanolider'. Kosmetiskt.
4. Typorden 'styrstamshållare' och 'vevlager' står i profilen som 'väntar på Davids bekräftelse'.
