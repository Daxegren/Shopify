# Rensning 2 – underlag: "enligt tillverkaren" på lastgränser (BEST OF SPORTS, 2026-11-06)

**Status: underlag och lista. Ingenting är skrivet till Shopify eller till någon butik.** Listan bygger på repots egna skrivfiler och utkast (`rapporter/facit-bos-2026-10-31/vag2_skriv/`), inte på live-läsning. Live kan avvika (nattsynken, manuella ändringar, arkivering). Ett live-klassningssteg (som i rensning 1: live-texten måste vara lika med "före"-texten, annars hoppas produkten över) krävs därför före all skrivning.

Frågan som underlaget hör till är F2 i `shopify-sync/status/oppna_fragor.json`: ska "enligt tillverkaren" stå på alla maxviktsuppgifter? Svaret antas inte här; beslutsfilen `rapporter/beslut-2026-11-06.md` ställer frågan.

## 1. Resultat i siffror

| Mått | Antal |
|---|---|
| Skrivna texter i skrivfilerna (senaste version per produkt, metarensning 1 och 3 påförda) | 2614 |
| Texter med maxvikt-/belastningsuppgift (lastgräns) | 482 |
| Lastgränsuppgifter (påståenden) i dessa texter | 487 |
| – nivå 0: frasen "enligt tillverkaren" finns på minst en förekomst av påståendet (uppfyller R5 "en gång per påstående") | 321 |
| – nivå 2: frasen finns på en förekomst, men uppgiften upprepas utan frasen (oftast i metabeskrivningen, "Passar för" eller löptext) | 156 |
| – nivå 1: frasen saknas helt, på alla förekomster | 10 |
| Förekomster (rader/meningar) med lastgräns som saknar frasen | 242 av 786 |
| Produkter där alla påståenden är på nivå 0 | 316 |
| Produkter med nivå 2 som högsta nivå | 156 |
| Produkter med nivå 1 (frasen saknas helt på minst ett påstående) | 10 |
| **Förslag enligt gällande regler (lista 1)** | **4 produkter, 4 rader** |
| **Osäkra, kräver Davids beslut (lista 2)** | **7 produkter, 8 rader** |
| Spärrade eller arkiverade, ändras inte (lista 3) | 7 produkter |
| Alternativ B (lista 4): alla övriga förekomster utan frasen | 154 produkter, 216 rader |

**Läsning av siffrorna.** Rensning 2 den 4 november lade till frasen på specifikationsraderna i 178 texter, och texterna som skrevs efter det har frasen från start. Därför är den ursprungliga uppskattningen i F2 ("2 av 24 texter") inte längre rättvisande: i repots data saknar bara 10 av 482 texter frasen helt. Det som återstår i stor skala är att uppgiften upprepas utan frasen i metabeskrivning, "Passar för" och löptext. Det är tillåtet enligt R5 (en gång per påstående) men är exakt vad F2 egentligen frågar om.

**Bakgrund: vad rensning 2 hoppade över den 4 november** (`rapporter/rensning2-lastgranser-2026-11-04/underlag.md`): 8797 och 10104 (skulle ge fler än två "enligt tillverkaren"), 3001 och 10349 (ingen specifikationsrad som kunde ändras automatiskt), 10348 (inte aktiv) och viktvästen 10604 (tillagd vikt, ingen lastgräns). Av dem är 8797 fortfarande öppen och redovisas i lista 1 (en rad i stället för två, så att R5 hålls). 10104 och 3001 redovisas i lista 2 (R5). 10349 har frasen i löptexten och saknar den bara på specifikationsraden (alt B). 10348 är spärrad. 10604 är ingen lastgräns.

## 2. Metod, nivåer och källklasser

- **Detektering:** för varje titel, SEO-titel, metabeskrivning, punkt i specifikation/"Passar för", löptextmening och FAQ-svar söks en lastetikett (användarvikt, maxlast, lastkapacitet, maximal belastning, lastgräns, maxvikt, bärförmåga, driftsvikt m.fl.) med ett kg-värde i samma mening. Inte lastgränser (enligt R4): viktväst med tillagd vikt, plug-in-vikter, motstånd, svänghjul, produktvikt, fyllnadsmängd. Kontrollerat med en andra sökning på "max", "upp till", "ton", "kilo": inga ytterligare lastgränser hittades.
- **Nivå:** per påstående (kg-värde): 0 = frasen finns på minst en förekomst; 1 = frasen saknas överallt; 2 = frasen finns på någon förekomst men inte alla.
- **Källklass A+:** produktens källtext säger själv "enligt tillverkaren" vid värdet. **A:** svensk ordagrann etikett och enhet i leverantörens källtext (regelbokens R4 och Davids beslut 2026-11-04, "Alt A"; samma grund som rensning 2 den 4 november använde). **B (osäker, kräver Davids beslut):** engelsk eller maskinöversatt källa, etiketten är en tolkning ("driftsvikt"), värdet står inte i sparad källtext, eller uppgiften kommer från en webbkälla som inte styrker att den är tillverkarens. För B föreslås ingen ändring.
- **Viktig tolkning att bekräfta:** ingen leverantörskälla säger ordagrant att uppgiften kommer från tillverkaren (utom A+). Jag har behandlat regelbokens definition (svensk ordagrann uppgift med etikett och enhet = tillverkarens uppgift) som tillräcklig för klass A. Läser David uppdraget strängare flyttas alla klass A till "osäker".
- **Förslagens utformning:** minsta ändring, frasen direkt efter måttet. Specifikationsrad: `(enligt tillverkaren)` i parentes (som i rensning 2). Metabeskrivning och löptext: ` enligt tillverkaren`. Punkt i "Passar för": `, enligt tillverkaren`. Inga utfyllnadsord.
- **Gällande regler (lista 1):** högst en förekomst per påstående (R5), högst två "enligt tillverkaren" per text, meta 70–155 tecken. Lastgräns i titel/SEO-titel föreslås inte (titeln är högst 70 tecken; kräver omformulering).
- **Alternativ B (lista 4):** frasen på varje återstående förekomst. Det strider mot R5 ("en gång per påstående", högst två per text) och kräver både ett ja på F2 i den formen och en ändring av R5. För metabeskrivningar anges om den nya metan ryms inom 155 tecken.

## 3. Antal per produkttyp

| Produkttyp | Texter med lastgräns | Förslag (lista 1) | Osäkra (lista 2) | Bara alt B (lista 4) | Spärrade/arkiverade |
|---|---|---|---|---|---|
| Elcyklar och eltrehjulingar | 67 | 1 | 0 | 0 | 0 |
| Motionscyklar (inkl. spinning) | 64 | 3 | 3 | 49 | 5 |
| Stänger, handtag och tillbehör | 53 | 0 | 0 | 12 | 0 |
| Löpband | 50 | 0 | 0 | 44 | 0 |
| Sparkcyklar | 43 | 0 | 0 | 0 | 0 |
| Crosstrainers och roddmaskiner | 41 | 0 | 0 | 29 | 1 |
| Cykelbärare, korgar och stödben | 40 | 0 | 3 | 2 | 0 |
| Hemmaträning, stöd och handtag | 38 | 0 | 0 | 1 | 0 |
| Bänkar, stationer och multigym | 28 | 0 | 0 | 2 | 1 |
| Styrkemaskiner, ställ och racks | 25 | 0 | 0 | 2 | 0 |
| Bollar, balans och plyo | 18 | 0 | 1 | 0 | 0 |
| Övrigt | 15 | 0 | 0 | 7 | 0 |

Produkttyp = typordet först i titeln (gruppering enligt skriptet `shopify-sync/scripts/rensning2_underlag.py`).

## 4. Lista 1 – förslag enligt gällande regler (före och efter)

Bara nivå 1 (frasen saknas helt), klass A eller A+, en förekomst per påstående. Längdgränser kontrollerade nedan.

| Nr | Titel | Rad | Före | Efter | Risk |
|---|---|---|---|---|---|
| 8797 | Elcykel ADO Air 28, 28 tum, Ljusgul | li | Maxvikt: 120 kg | Maxvikt: 120 kg (enligt tillverkaren) | Låg: svensk ordagrann etikett och enhet i källan; ändrar bara raden |
| 10071 | Motionscykel BH Fitness TFR Ergo med Ryggstöd och… | li | Maximal driftsvikt: 130 kg | Maximal driftsvikt: 130 kg (enligt tillverkaren) | Låg: svensk ordagrann etikett och enhet i källan; ändrar bara raden |
| 10074 | Liggande Motionscykel BH Fitness i.TFR MED med Ry… | li | Maximal driftsvikt: 180 kg | Maximal driftsvikt: 180 kg (enligt tillverkaren) | Låg: svensk ordagrann etikett och enhet i källan; ändrar bara raden |
| 10090 | Spinningcykel BH Fitness Xcalibur Multimedia med… | li | Maximal driftsvikt: 130 kg | Maximal driftsvikt: 130 kg (enligt tillverkaren) | Låg: svensk ordagrann etikett och enhet i källan; ändrar bara raden |

## 5. Lista 2 – osäkra: kräver Davids beslut (ingen ändring föreslås)

| Nr | Titel | Rad | Text | Skäl |
|---|---|---|---|---|
| 3001 | Träningsboll Gymstick, 65 cm, Svart | li | Maxbelastning: 120 kg | R5: texten har redan 3 "enligt tillverkaren" och skulle få 4 (högst 2); en annan förekomst måste tas bort först |
| 10069 | Liggande Motionscykel BH Fitness Inertia med… | li | Maximal driftsvikt: 180 kg | källan är engelsk eller maskinöversatt; översättning av etikett (R4: utelämna eller osäker) |
| 10069 | Liggande Motionscykel BH Fitness Inertia med… | meta | BH Fitness Inertia är en liggande motionscykel med ryggstöd och 16-tums pekskärm. Bromssystemet är EMS, induk… | källan är engelsk eller maskinöversatt; översättning av etikett (R4: utelämna eller osäker) |
| 10083 | Motionscykel BH Fitness XTB MED, Maximal Anv… | titel | Motionscykel BH Fitness XTB MED, Maximal Användarvikt 180 kg | lastgräns i titel/SEO-titel; kräver omformulering (titeln är högst 70 tecken) |
| 10104 | Spinningcykel Hammer Speed Race X med 20 kg… | li | Maximal användarvikt: 130 kg | R5: texten har redan 2 "enligt tillverkaren" och skulle få 3 (högst 2); en annan förekomst måste tas bort först |
| 32027 | Stödben Hebie Abstellheld 18 | li | Maximal lastgräns: 25 kg | bara återförsäljarkälla (t.ex. bike-components, Rose Bikes); beslutet 2026-11-05 gör sådan lastgräns till "Ej känd" |
| 32028 | Stödben Hebie Fox Uni, 26–28 tum, Svart | li | Maximal lastgräns: 25 kg | bara återförsäljarkälla (t.ex. bike-components, Rose Bikes); beslutet 2026-11-05 gör sådan lastgräns till "Ej känd" |
| 32029 | Stödben Hebie Abstellheld 40, Svart | li | Maximal lastgräns: 25 kg | bara återförsäljarkälla (t.ex. bike-components, Rose Bikes); beslutet 2026-11-05 gör sådan lastgräns till "Ej känd" |

Särskilt om etiketten "driftsvikt": BH Fitness 10071, 10074 och 10090 har "Maximal driftsvikt" ordagrant på svenska i källan och ligger därför i lista 1/alt B som klass A (R4: etiketten får stå, men får inte tolkas som användarvikt). 10069 har bara engelsk källa ("Maximum operating weight"); beslutsloggen 2026-11-04 ("Alt A") säger att driftsvikt utelämnas då. Texten kan alltså redan strida mot R4; det är ett separat fynd att ta ställning till, inte något som löses genom att lägga till frasen.

Särskilt om Hebie-stödbenen 32027–32029: texterna har redan "enligt tillverkaren" på lastgränsen 25 kg, men uppgiften bygger på återförsäljarsidor (bike-components, Rose Bikes) eftersom Hebies egen sida inte gick att läsa. Beslutet 2026-11-05 (Gymstick Performance Board och Power Rings) gjorde sådan lastgräns till "Ej känd". Det är ett separat fynd: samma princip kan kräva att de tre texterna ändras, inte kompletteras.

## 6. Lista 3 – spärrade och arkiverade (ändras inte)

| Nr | Titel | Skäl | Rader som annars hade berörts |
|---|---|---|---|
| 10073 | Hopfällbar Motionscykel BH Fitness X-Tri 2 med Ry… | arkiverad av leverantörssynken (Velomarket3) | 2 |
| 10092 | Motionscykel Hammer Cardio T3 med 8 Nivåer | arkiverad av leverantörssynken (Velomarket3) | 2 |
| 10103 | Spinningcykel Hammer Speed Race SR med 10,1-tums… | spärrad: pilot-20 | 3 |
| 10110 | Motionscykel Toorx BRX 65 Comfort med Ryggstöd | spärrad: pilot-20 | 3 |
| 10148 | Minicykel Tunturi Mini Bike Pro Chair Bike | arkiverad av leverantörssynken (Velomarket3) | 2 |
| 10162 | Crosstrainer BH Fitness Super Khronos | arkiverad av leverantörssynken (Velomarket3) | 1 |
| 10348 | Träningsbänk Finnlo by Hammer Tricon Flex, Hopfäl… | spärrad: pilot-20 | 1 |

## 7. Lista 4 – alternativ B: frasen på alla återstående förekomster (före och efter)

Gäller bara om David svarar ja på F2 i den vidaste formen och beslutar att R5 ändras. Kolumnen "Ryms" visar om ny meta blir högst 155 tecken. Efter ändring ger flera texter fler än två "enligt tillverkaren" (R5), se avsnitt 8.

### Motionscyklar (inkl. spinning) (54 produkter)

| Nr | Titel | Rad | Före | Efter | Ryms |
|---|---|---|---|---|---|
| 9422 | Motionscykel Christopeit Active | li | Dig som behöver en motionscykel med maximal användarvikt 110 kg | Dig som behöver en motionscykel med maximal användarvikt 110 kg, enligt tillverkaren |  |
| 9424 | Hopfällbar Motionscykel Christopeit S-B… | li | Dig som behöver en motionscykel med maximal användarvikt 120 kg | Dig som behöver en motionscykel med maximal användarvikt 120 kg, enligt tillverkaren |  |
| 9425 | Motionscykel Christopeit ET 5.1, Svart | li | Dig som behöver en motionscykel med maximal användarvikt 120 kg | Dig som behöver en motionscykel med maximal användarvikt 120 kg, enligt tillverkaren |  |
| 10070 | Liggande Motionscykel BH Fitness Movemi… | meta | BH Fitness Movemia BR1000R LED är en liggande motionscykel med ryggstöd, LED-display och 25 motståndsnivåer. Maximal användarvikt är 190 kg. | BH Fitness Movemia BR1000R LED är en liggande motionscykel med ryggstöd, LED-display och 25 motståndsnivåer. Maximal användarvikt är 190 kg enligt tillverkaren. | nej (160) |
| 10071 | Motionscykel BH Fitness TFR Ergo med Ry… | meta | BH Fitness TFR Ergo är en motionscykel med ryggstöd, LED-display, 30 träningsprogram och 24 nivåer. Maximal driftsvikt är 130 kg. | BH Fitness TFR Ergo är en motionscykel med ryggstöd, LED-display, 30 träningsprogram och 24 nivåer. Maximal driftsvikt är 130 kg enligt tillverkaren. | ja (149) |
| 10072 | Motionscykel BH Fitness Arctic med 8 Mo… | meta | BH Fitness Arctic är en motionscykel med LCD-display, 8 motståndsnivåer och magnetiskt bromssystem. Svänghjul 8 kg, maximal användarvikt 90 kg. | BH Fitness Arctic är en motionscykel med LCD-display, 8 motståndsnivåer och magnetiskt bromssystem. Svänghjul 8 kg, maximal användarvikt 90 kg enligt tillverkaren. | nej (163) |
| 10074 | Liggande Motionscykel BH Fitness i.TFR… | meta | BH Fitness i.TFR MED är en liggande motionscykel med ryggstöd, sidohandtag och magnetiskt bromssystem. Maximal driftsvikt är 180 kg. | BH Fitness i.TFR MED är en liggande motionscykel med ryggstöd, sidohandtag och magnetiskt bromssystem. Maximal driftsvikt är 180 kg enligt tillverkaren. | ja (152) |
| 10076 | Motionscykel BH Fitness Carbon Bike RS… | meta | BH Fitness Carbon Bike RS är en motionscykel med 10-tums pekskärm, 16 träningsprogram och 24 nivåer. Maximal användarvikt är 130 kg. | BH Fitness Carbon Bike RS är en motionscykel med 10-tums pekskärm, 16 träningsprogram och 24 nivåer. Maximal användarvikt är 130 kg enligt tillverkaren. | ja (152) |
| 10076 | Motionscykel BH Fitness Carbon Bike RS… | li | Dig som behöver en motionscykel med maximal användarvikt 130 kg | Dig som behöver en motionscykel med maximal användarvikt 130 kg, enligt tillverkaren |  |
| 10077 | Motionscykel BH Fitness EC01 Exercycle… | meta | BH Fitness EC01 Exercycle är en motionscykel med svänghjul på 11 kg och maximal effekt 1500 W. Maximal användarvikt är 150 kg. | BH Fitness EC01 Exercycle är en motionscykel med svänghjul på 11 kg och maximal effekt 1500 W. Maximal användarvikt är 150 kg enligt tillverkaren. | ja (146) |
| 10077 | Motionscykel BH Fitness EC01 Exercycle… | li | Dig som behöver en motionscykel med maximal användarvikt 150 kg | Dig som behöver en motionscykel med maximal användarvikt 150 kg, enligt tillverkaren |  |
| 10078 | Motionscykel BH Fitness Ergo EMS med 12… | meta | BH Fitness Ergo EMS är en motionscykel med LCD-display, 12 träningsprogram och 24 motståndsnivåer. Maximal användarvikt är 150 kg. | BH Fitness Ergo EMS är en motionscykel med LCD-display, 12 träningsprogram och 24 motståndsnivåer. Maximal användarvikt är 150 kg enligt tillverkaren. | ja (150) |
| 10078 | Motionscykel BH Fitness Ergo EMS med 12… | li | Dig som behöver en motionscykel med maximal användarvikt 150 kg | Dig som behöver en motionscykel med maximal användarvikt 150 kg, enligt tillverkaren |  |
| 10079 | Motionscykel BH Fitness Lyon Climber me… | li | Dig som behöver en motionscykel med maximal användarvikt 110 kg | Dig som behöver en motionscykel med maximal användarvikt 110 kg, enligt tillverkaren |  |
| 10080 | Motionscykel BH Fitness Lyon Climber Mu… | li | Dig som behöver en motionscykel med maximal användarvikt 110 kg | Dig som behöver en motionscykel med maximal användarvikt 110 kg, enligt tillverkaren |  |
| 10081 | Motionscykel BH Fitness Osaka med 32 Mo… | meta | BH Fitness Osaka är en motionscykel med LCD-display, 32 motståndsnivåer och magnetiskt bromssystem. Maximal användarvikt är 110 kg. | BH Fitness Osaka är en motionscykel med LCD-display, 32 motståndsnivåer och magnetiskt bromssystem. Maximal användarvikt är 110 kg enligt tillverkaren. | ja (151) |
| 10081 | Motionscykel BH Fitness Osaka med 32 Mo… | li | Dig som behöver en motionscykel med maximal användarvikt 110 kg | Dig som behöver en motionscykel med maximal användarvikt 110 kg, enligt tillverkaren |  |
| 10082 | Motionscykel BH Fitness XTB med 30 Trän… | meta | BH Fitness XTB är en motionscykel med LCD-display, 30 träningsprogram och 24 motståndsnivåer. Maximal användarvikt är 130 kg. | BH Fitness XTB är en motionscykel med LCD-display, 30 träningsprogram och 24 motståndsnivåer. Maximal användarvikt är 130 kg enligt tillverkaren. | ja (145) |
| 10082 | Motionscykel BH Fitness XTB med 30 Trän… | li | Dig som behöver en motionscykel med maximal användarvikt 130 kg | Dig som behöver en motionscykel med maximal användarvikt 130 kg, enligt tillverkaren |  |
| 10083 | Motionscykel BH Fitness XTB MED, Maxima… | meta | BH Fitness XTB MED är en motionscykel med LCD-display, 30 träningsprogram och 24 motståndsnivåer. Maximal användarvikt är 180 kg. | BH Fitness XTB MED är en motionscykel med LCD-display, 30 träningsprogram och 24 motståndsnivåer. Maximal användarvikt är 180 kg enligt tillverkaren. | ja (149) |
| 10083 | Motionscykel BH Fitness XTB MED, Maxima… | li | Dig som söker en motionscykel med maximal användarvikt 180 kg | Dig som söker en motionscykel med maximal användarvikt 180 kg, enligt tillverkaren |  |
| 10084 | Motionscykel BH Fitness XTB Multimedia… | li | Dig som behöver en motionscykel med maximal användarvikt 130 kg | Dig som behöver en motionscykel med maximal användarvikt 130 kg, enligt tillverkaren |  |
| 10086 | Spinningcykel BH Fitness i.Rhone med 32… | meta | BH Fitness i.Rhone är en spinningcykel med LED-display, 32 nivåer och svänghjul på 8 kg. Maximal användarvikt är 120 kg. | BH Fitness i.Rhone är en spinningcykel med LED-display, 32 nivåer och svänghjul på 8 kg. Maximal användarvikt är 120 kg enligt tillverkaren. | ja (140) |
| 10086 | Spinningcykel BH Fitness i.Rhone med 32… | li | Dig som behöver en spinningcykel med maximal användarvikt 120 kg | Dig som behöver en spinningcykel med maximal användarvikt 120 kg, enligt tillverkaren |  |
| 10088 | Spinningcykel BH Fitness Stratos med 22… | meta | BH Fitness Stratos är en spinningcykel med LCD-display, friktionsbroms och svänghjul på 22 kg. Maximal användarvikt är 130 kg. | BH Fitness Stratos är en spinningcykel med LCD-display, friktionsbroms och svänghjul på 22 kg. Maximal användarvikt är 130 kg enligt tillverkaren. | ja (146) |
| 10088 | Spinningcykel BH Fitness Stratos med 22… | li | Dig som behöver en spinningcykel med maximal användarvikt 130 kg | Dig som behöver en spinningcykel med maximal användarvikt 130 kg, enligt tillverkaren |  |
| 10089 | Spinningcykel BH Fitness Tokyo med 20 k… | meta | BH Fitness Tokyo är en spinningcykel med LCD-skärm, svänghjul på 20 kg och Poly-V-rem. Maximal användarvikt är 130 kg. | BH Fitness Tokyo är en spinningcykel med LCD-skärm, svänghjul på 20 kg och Poly-V-rem. Maximal användarvikt är 130 kg enligt tillverkaren. | ja (138) |
| 10089 | Spinningcykel BH Fitness Tokyo med 20 k… | li | Dig som behöver en spinningcykel med maximal användarvikt 130 kg | Dig som behöver en spinningcykel med maximal användarvikt 130 kg, enligt tillverkaren |  |
| 10090 | Spinningcykel BH Fitness Xcalibur Multi… | li | Dig som behöver en spinningcykel med maximal driftsvikt 130 kg | Dig som behöver en spinningcykel med maximal driftsvikt 130 kg, enligt tillverkaren |  |
| 10095 | Motionscykel Hammer Cardio Motion BT me… | meta | Hammer Cardio Motion BT är en motionscykel med LCD-display, 22 träningsprogram och 16 motståndsnivåer. Maximal användarvikt är 130 kg. | Hammer Cardio Motion BT är en motionscykel med LCD-display, 22 träningsprogram och 16 motståndsnivåer. Maximal användarvikt är 130 kg enligt tillverkaren. | ja (154) |
| 10095 | Motionscykel Hammer Cardio Motion BT me… | li | Dig som behöver en motionscykel med maximal användarvikt 130 kg | Dig som behöver en motionscykel med maximal användarvikt 130 kg, enligt tillverkaren |  |
| 10096 | Motionscykel Hammer Cardio XT7 med 24 T… | meta | Hammer Cardio XT7 är en motionscykel med LCD-display, 24 träningsprogram och 16 motståndsnivåer. Maximal användarvikt är 130 kg. | Hammer Cardio XT7 är en motionscykel med LCD-display, 24 träningsprogram och 16 motståndsnivåer. Maximal användarvikt är 130 kg enligt tillverkaren. | ja (148) |
| 10096 | Motionscykel Hammer Cardio XT7 med 24 T… | li | Dig som behöver en motionscykel med maximal användarvikt 130 kg | Dig som behöver en motionscykel med maximal användarvikt 130 kg, enligt tillverkaren |  |
| 10097 | Motionscykel Hammer CardioPace 5.0 Nors… | li | Dig som behöver en motionscykel med maximal användarvikt 130 kg | Dig som behöver en motionscykel med maximal användarvikt 130 kg, enligt tillverkaren |  |
| 10098 | Motionscykel Hammer Maximum Presidio me… | meta | Hammer Maximum Presidio är en motionscykel med LCD-display, 16 träningsprogram och 41 motståndsnivåer. Maximal användarvikt är 180 kg. | Hammer Maximum Presidio är en motionscykel med LCD-display, 16 träningsprogram och 41 motståndsnivåer. Maximal användarvikt är 180 kg enligt tillverkaren. | ja (154) |
| 10098 | Motionscykel Hammer Maximum Presidio me… | li | Dig som behöver en motionscykel med maximal användarvikt 180 kg | Dig som behöver en motionscykel med maximal användarvikt 180 kg, enligt tillverkaren |  |
| 10099 | Motionscykel Hammer Speed Race med 16 k… | meta | Hammer Speed Race är en motionscykel med LCD-display, manuellt bromssystem och svänghjul på 16 kg. Maximal användarvikt är 130 kg. | Hammer Speed Race är en motionscykel med LCD-display, manuellt bromssystem och svänghjul på 16 kg. Maximal användarvikt är 130 kg enligt tillverkaren. | ja (150) |
| 10099 | Motionscykel Hammer Speed Race med 16 k… | li | Dig som behöver en motionscykel med maximal användarvikt 130 kg | Dig som behöver en motionscykel med maximal användarvikt 130 kg, enligt tillverkaren |  |
| 10101 | Spinningcykel Hammer HyRace SR med Peks… | meta | Hammer HyRace SR är en spinningcykel med pekskärm, 17 träningsprogram och 32 motståndsnivåer. Svänghjulet väger 20 kg och maximal användarvikt är 135 kg. | Hammer HyRace SR är en spinningcykel med pekskärm, 17 träningsprogram och 32 motståndsnivåer. Svänghjulet väger 20 kg och maximal användarvikt är 135 kg enligt tillverkaren. | nej (173) |
| 10101 | Spinningcykel Hammer HyRace SR med Peks… | li | Dig som behöver en spinningcykel med maximal användarvikt 135 kg | Dig som behöver en spinningcykel med maximal användarvikt 135 kg, enligt tillverkaren |  |
| 10102 | Spinningcykel Hammer Speed PRO med 36 N… | meta | Hammer Speed PRO är en spinningcykel med LCD-skärm, 36 nivåer och svänghjul på 22 kg. Maximal användarvikt är 150 kg. | Hammer Speed PRO är en spinningcykel med LCD-skärm, 36 nivåer och svänghjul på 22 kg. Maximal användarvikt är 150 kg enligt tillverkaren. | ja (137) |
| 10102 | Spinningcykel Hammer Speed PRO med 36 N… | li | Dig som behöver en spinningcykel med maximal användarvikt 150 kg | Dig som behöver en spinningcykel med maximal användarvikt 150 kg, enligt tillverkaren |  |
| 10104 | Spinningcykel Hammer Speed Race X med 2… | meta | Hammer Speed Race X är en spinningcykel med LCD-display och svänghjul på 20 kg. Maximal användarvikt är 130 kg. | Hammer Speed Race X är en spinningcykel med LCD-display och svänghjul på 20 kg. Maximal användarvikt är 130 kg enligt tillverkaren. | ja (131) |
| 10104 | Spinningcykel Hammer Speed Race X med 2… | li | Dig som behöver en spinningcykel med maximal användarvikt 130 kg | Dig som behöver en spinningcykel med maximal användarvikt 130 kg, enligt tillverkaren |  |
| 10105 | Motionscykel Toorx BRX-100 med 12 kg Sv… | meta | Toorx BRX-100 är en motionscykel med LCD-display, 16 nivåer och svänghjul på 12 kg. Maximal användarvikt är 150 kg. | Toorx BRX-100 är en motionscykel med LCD-display, 16 nivåer och svänghjul på 12 kg. Maximal användarvikt är 150 kg enligt tillverkaren. | ja (135) |
| 10105 | Motionscykel Toorx BRX-100 med 12 kg Sv… | li | Dig som behöver en motionscykel med maximal användarvikt 150 kg | Dig som behöver en motionscykel med maximal användarvikt 150 kg, enligt tillverkaren |  |
| 10106 | Motionscykel Toorx BRX-100 Ergo med 32… | meta | Toorx BRX-100 Ergo är en motionscykel med LCD-skärm, 32 nivåer och svänghjul på 14 kg. Maximal användarvikt är 150 kg. | Toorx BRX-100 Ergo är en motionscykel med LCD-skärm, 32 nivåer och svänghjul på 14 kg. Maximal användarvikt är 150 kg enligt tillverkaren. | ja (138) |
| 10106 | Motionscykel Toorx BRX-100 Ergo med 32… | li | Dig som behöver en motionscykel med maximal användarvikt 150 kg | Dig som behöver en motionscykel med maximal användarvikt 150 kg, enligt tillverkaren |  |
| 10107 | Motionscykel Toorx BRX-300 med 14 kg Sv… | meta | Toorx BRX-300 är en motionscykel med LCD-skärm, 32 nivåer och svänghjul på 14 kg. Maximal användarvikt är 150 kg. | Toorx BRX-300 är en motionscykel med LCD-skärm, 32 nivåer och svänghjul på 14 kg. Maximal användarvikt är 150 kg enligt tillverkaren. | ja (133) |
| 10107 | Motionscykel Toorx BRX-300 med 14 kg Sv… | li | Dig som behöver en motionscykel med maximal användarvikt 150 kg | Dig som behöver en motionscykel med maximal användarvikt 150 kg, enligt tillverkaren |  |
| 10108 | Hopfällbar Motionscykel Toorx BRX Compa… | meta | Toorx BRX Compact är en hopfällbar motionscykel med LCD-display, 8 nivåer och svänghjul på 6 kg. Maximal användarvikt är 100 kg. | Toorx BRX Compact är en hopfällbar motionscykel med LCD-display, 8 nivåer och svänghjul på 6 kg. Maximal användarvikt är 100 kg enligt tillverkaren. | ja (148) |
| 10108 | Hopfällbar Motionscykel Toorx BRX Compa… | li | Dig som behöver en motionscykel med maximal användarvikt 100 kg | Dig som behöver en motionscykel med maximal användarvikt 100 kg, enligt tillverkaren |  |
| 10109 | Hopfällbar Motionscykel Toorx Compact M… | meta | Toorx Compact MultiFit är en hopfällbar motionscykel med LCD-skärm, 8 nivåer och svänghjul på 6 kg. Maximal användarvikt är 100 kg. | Toorx Compact MultiFit är en hopfällbar motionscykel med LCD-skärm, 8 nivåer och svänghjul på 6 kg. Maximal användarvikt är 100 kg enligt tillverkaren. | ja (151) |
| 10109 | Hopfällbar Motionscykel Toorx Compact M… | li | Dig som behöver en motionscykel med maximal användarvikt 100 kg | Dig som behöver en motionscykel med maximal användarvikt 100 kg, enligt tillverkaren |  |
| 10112 | Spinningcykel Toorx SRX-50S med 20 kg S… | meta | Toorx SRX-50S är en spinningcykel med LCD-skärm, manuellt bromssystem och svänghjul på 20 kg. Maximal användarvikt är 125 kg. | Toorx SRX-50S är en spinningcykel med LCD-skärm, manuellt bromssystem och svänghjul på 20 kg. Maximal användarvikt är 125 kg enligt tillverkaren. | ja (145) |
| 10112 | Spinningcykel Toorx SRX-50S med 20 kg S… | li | Dig som behöver en spinningcykel med maximal användarvikt 125 kg | Dig som behöver en spinningcykel med maximal användarvikt 125 kg, enligt tillverkaren |  |
| 10113 | Spinningcykel Toorx SRX-70S med 22 kg S… | meta | Toorx SRX-70S är en spinningcykel med LCD-skärm, manuellt bromssystem och svänghjul på 22 kg. Maximal användarvikt är 125 kg. | Toorx SRX-70S är en spinningcykel med LCD-skärm, manuellt bromssystem och svänghjul på 22 kg. Maximal användarvikt är 125 kg enligt tillverkaren. | ja (145) |
| 10113 | Spinningcykel Toorx SRX-70S med 22 kg S… | li | Dig som behöver en spinningcykel med maximal användarvikt 125 kg | Dig som behöver en spinningcykel med maximal användarvikt 125 kg, enligt tillverkaren |  |
| 10114 | Spinningcykel Toorx SRX-EVOLVE med 22 k… | meta | Toorx SRX-EVOLVE är en spinningcykel med LCD-display, 12 träningsprogram och 24 motståndsnivåer. Maximal användarvikt är 150 kg. | Toorx SRX-EVOLVE är en spinningcykel med LCD-display, 12 träningsprogram och 24 motståndsnivåer. Maximal användarvikt är 150 kg enligt tillverkaren. | ja (148) |
| 10114 | Spinningcykel Toorx SRX-EVOLVE med 22 k… | li | Dig som behöver en spinningcykel med maximal användarvikt 150 kg | Dig som behöver en spinningcykel med maximal användarvikt 150 kg, enligt tillverkaren |  |
| 10116 | Motionscykel Toorx BRX R100 Ergo med Ry… | meta | Toorx BRX R100 Ergo är en motionscykel med ryggstöd, LCD-skärm och 32 nivåer. Svänghjulet väger 14 kg och maximal användarvikt är 130 kg. | Toorx BRX R100 Ergo är en motionscykel med ryggstöd, LCD-skärm och 32 nivåer. Svänghjulet väger 14 kg och maximal användarvikt är 130 kg enligt tillverkaren. | nej (157) |
| 10116 | Motionscykel Toorx BRX R100 Ergo med Ry… | li | Dig som behöver en motionscykel med maximal användarvikt 130 kg | Dig som behöver en motionscykel med maximal användarvikt 130 kg, enligt tillverkaren |  |
| 10117 | Liggande Motionscykel Toorx BRX R3000 m… | meta | Toorx BRX R3000 är en liggande motionscykel med LCD-skärm, 12 träningsprogram och 32 nivåer. Maximal användarvikt är 160 kg. | Toorx BRX R3000 är en liggande motionscykel med LCD-skärm, 12 träningsprogram och 32 nivåer. Maximal användarvikt är 160 kg enligt tillverkaren. | ja (144) |
| 10117 | Liggande Motionscykel Toorx BRX R3000 m… | li | Dig som behöver en motionscykel med maximal användarvikt 160 kg | Dig som behöver en motionscykel med maximal användarvikt 160 kg, enligt tillverkaren |  |
| 10118 | Motionscykel Toorx BRX95 Comfort med Ry… | meta | Toorx BRX95 Comfort är en motionscykel med ryggstöd, LCD-skärm, 21 träningsprogram och 24 nivåer. Maximal användarvikt är 130 kg. | Toorx BRX95 Comfort är en motionscykel med ryggstöd, LCD-skärm, 21 träningsprogram och 24 nivåer. Maximal användarvikt är 130 kg enligt tillverkaren. | ja (149) |
| 10118 | Motionscykel Toorx BRX95 Comfort med Ry… | li | Dig som behöver en motionscykel med maximal användarvikt 130 kg | Dig som behöver en motionscykel med maximal användarvikt 130 kg, enligt tillverkaren |  |
| 10119 | Motionscykel Tunturi Competence F20 med… | meta | Tunturi Competence F20 är en motionscykel med 3 träningsprogram och manuellt bromssystem. Maximal användarvikt är 135 kg. | Tunturi Competence F20 är en motionscykel med 3 träningsprogram och manuellt bromssystem. Maximal användarvikt är 135 kg enligt tillverkaren. | ja (141) |
| 10119 | Motionscykel Tunturi Competence F20 med… | li | Dig som behöver en motionscykel med maximal användarvikt 135 kg | Dig som behöver en motionscykel med maximal användarvikt 135 kg, enligt tillverkaren |  |
| 10120 | Motionscykel Tunturi FitCycle 20 med 8… | meta | Tunturi FitCycle 20 är en motionscykel med LCD-skärm, 1 program och 8 svårighetsgrader. Maximal användarvikt är 100 kg. | Tunturi FitCycle 20 är en motionscykel med LCD-skärm, 1 program och 8 svårighetsgrader. Maximal användarvikt är 100 kg enligt tillverkaren. | ja (139) |
| 10120 | Motionscykel Tunturi FitCycle 20 med 8… | li | Dig som behöver en motionscykel med maximal användarvikt 100 kg | Dig som behöver en motionscykel med maximal användarvikt 100 kg, enligt tillverkaren |  |
| 10121 | Motionscykel Tunturi FitCycle 30 med 4… | meta | Tunturi FitCycle 30 är en motionscykel med LCD-skärm, 4 träningsprogram och 8 svårighetsnivåer. Maximal användarvikt är 110 kg. | Tunturi FitCycle 30 är en motionscykel med LCD-skärm, 4 träningsprogram och 8 svårighetsnivåer. Maximal användarvikt är 110 kg enligt tillverkaren. | ja (147) |
| 10121 | Motionscykel Tunturi FitCycle 30 med 4… | li | Dig som behöver en motionscykel med maximal användarvikt 110 kg | Dig som behöver en motionscykel med maximal användarvikt 110 kg, enligt tillverkaren |  |
| 10123 | Motionscykel Tunturi Cardio Fit B30 med… | meta | Tunturi Cardio Fit B30 är en motionscykel med LCD-skärm, 4 träningsprogram och 8 svårighetsnivåer. Maximal användarvikt är 110 kg. | Tunturi Cardio Fit B30 är en motionscykel med LCD-skärm, 4 träningsprogram och 8 svårighetsnivåer. Maximal användarvikt är 110 kg enligt tillverkaren. | ja (150) |
| 10123 | Motionscykel Tunturi Cardio Fit B30 med… | li | Dig som behöver en motionscykel med maximal användarvikt 110 kg | Dig som behöver en motionscykel med maximal användarvikt 110 kg, enligt tillverkaren |  |
| 10124 | Motionscykel Tunturi Cardio Fit B40 med… | meta | Tunturi Cardio Fit B40 är en motionscykel med 4 träningsprogram och 8 träningsnivåer. Maximal användarvikt är 110 kg. | Tunturi Cardio Fit B40 är en motionscykel med 4 träningsprogram och 8 träningsnivåer. Maximal användarvikt är 110 kg enligt tillverkaren. | ja (137) |
| 10124 | Motionscykel Tunturi Cardio Fit B40 med… | li | Dig som behöver en motionscykel med maximal användarvikt 110 kg | Dig som behöver en motionscykel med maximal användarvikt 110 kg, enligt tillverkaren |  |
| 10128 | Motionscykel Tunturi Fitcycle 40i | meta | Tunturi FitCycle 40i är en motionscykel med 23 träningsprogram, 16 svårighetsgrader och Bluetooth-anslutning. Maximal användarvikt är 110 kg. | Tunturi FitCycle 40i är en motionscykel med 23 träningsprogram, 16 svårighetsgrader och Bluetooth-anslutning. Maximal användarvikt är 110 kg enligt tillverkaren. | nej (161) |
| 10128 | Motionscykel Tunturi Fitcycle 40i | li | Dig som behöver en motionscykel med maximal användarvikt 110 kg | Dig som behöver en motionscykel med maximal användarvikt 110 kg, enligt tillverkaren |  |
| 10133 | Motionscykel Tunturi Signature E40 | meta | Tunturi Signature E40 är en motionscykel med 26 träningsprogram, 32 motståndsnivåer och svänghjul på 9 kg. Maximal användarvikt är 150 kg. | Tunturi Signature E40 är en motionscykel med 26 träningsprogram, 32 motståndsnivåer och svänghjul på 9 kg. Maximal användarvikt är 150 kg enligt tillverkaren. | nej (158) |
| 10133 | Motionscykel Tunturi Signature E40 | li | Dig som behöver en motionscykel med maximal användarvikt 150 kg | Dig som behöver en motionscykel med maximal användarvikt 150 kg, enligt tillverkaren |  |
| 10135 | Liggande Motionscykel Tunturi Signature… | meta | Tunturi Signature E60R är en liggande motionscykel med 7-tums LED/LCD-skärm och 26 träningsprogram. Maximal användarvikt är 150 kg. | Tunturi Signature E60R är en liggande motionscykel med 7-tums LED/LCD-skärm och 26 träningsprogram. Maximal användarvikt är 150 kg enligt tillverkaren. | ja (151) |
| 10135 | Liggande Motionscykel Tunturi Signature… | li | Dig som behöver en motionscykel med maximal användarvikt 150 kg | Dig som behöver en motionscykel med maximal användarvikt 150 kg, enligt tillverkaren |  |
| 10136 | Motionscykel Tunturi Signature E80 | li | Dig som behöver en motionscykel med maximal användarvikt 150 kg | Dig som behöver en motionscykel med maximal användarvikt 150 kg, enligt tillverkaren |  |
| 10137 | Motionscykel Tunturi Star Fit B100 Bike | meta | Tunturi Star Fit B100 är en motionscykel med 21 träningsprogram och 16 svårighetsgrader. Maximal användarvikt är 110 kg. | Tunturi Star Fit B100 är en motionscykel med 21 träningsprogram och 16 svårighetsgrader. Maximal användarvikt är 110 kg enligt tillverkaren. | ja (140) |
| 10137 | Motionscykel Tunturi Star Fit B100 Bike | li | Dig som behöver en motionscykel med maximal användarvikt 110 kg | Dig som behöver en motionscykel med maximal användarvikt 110 kg, enligt tillverkaren |  |
| 10138 | Motionscykel Tunturi Star Fit E100 HR I+ | meta | Tunturi Star Fit E100 HR I+ är en motionscykel med 22 träningsprogram och 16 svårighetsgrader. Maximal användarvikt är 120 kg. | Tunturi Star Fit E100 HR I+ är en motionscykel med 22 träningsprogram och 16 svårighetsgrader. Maximal användarvikt är 120 kg enligt tillverkaren. | ja (146) |
| 10138 | Motionscykel Tunturi Star Fit E100 HR I+ | li | Dig som behöver en motionscykel med maximal användarvikt 120 kg | Dig som behöver en motionscykel med maximal användarvikt 120 kg, enligt tillverkaren |  |
| 10139 | Motionscykel Tunturi Star Fit X100 X-Bi… | meta | Tunturi Star Fit X100 är en motionscykel av typen X-Bike med 8 svårighetsgrader. Maximal användarvikt är 110 kg. | Tunturi Star Fit X100 är en motionscykel av typen X-Bike med 8 svårighetsgrader. Maximal användarvikt är 110 kg enligt tillverkaren. | ja (132) |
| 10139 | Motionscykel Tunturi Star Fit X100 X-Bi… | li | Dig som behöver en motionscykel med maximal användarvikt 110 kg | Dig som behöver en motionscykel med maximal användarvikt 110 kg, enligt tillverkaren |  |
| 10140 | Spinningcykel Tunturi Cardio Fit S20 Sp… | meta | Tunturi Cardio Fit S20 är en spinningcykel med 3 träningsprogram och friktionsbroms. Maximal användarvikt är 100 kg. | Tunturi Cardio Fit S20 är en spinningcykel med 3 träningsprogram och friktionsbroms. Maximal användarvikt är 100 kg enligt tillverkaren. | ja (136) |
| 10140 | Spinningcykel Tunturi Cardio Fit S20 Sp… | li | Dig som behöver en spinningcykel med maximal användarvikt 100 kg | Dig som behöver en spinningcykel med maximal användarvikt 100 kg, enligt tillverkaren |  |
| 10149 | Minicykel Tunturi Cardio Fit M40 Mini B… | meta | Tunturi Cardio Fit M40 är en minicykel med 8 motståndsnivåer och Bluetooth-anslutning. Maximal användarvikt är 100 kg. | Tunturi Cardio Fit M40 är en minicykel med 8 motståndsnivåer och Bluetooth-anslutning. Maximal användarvikt är 100 kg enligt tillverkaren. | ja (138) |
| 10149 | Minicykel Tunturi Cardio Fit M40 Mini B… | li | Dig som behöver en minicykel med maximal användarvikt 100 kg | Dig som behöver en minicykel med maximal användarvikt 100 kg, enligt tillverkaren |  |
| 10155 | Motionscykel Tunturi Cardio Fit D20 Des… | p | Maximal användarvikt är 110 kg och måtten hopfälld är 46 x 59 x 106,5 cm. | Maximal användarvikt är 110 kg enligt tillverkaren och måtten hopfälld är 46 x 59 x 106,5 cm. |  |
| 10155 | Motionscykel Tunturi Cardio Fit D20 Des… | meta | Tunturi Cardio Fit D20 Deskbike är en motionscykel med manuellt PMS-bromssystem och 3,6 kg svänghjul. Maximal användarvikt är 110 kg. | Tunturi Cardio Fit D20 Deskbike är en motionscykel med manuellt PMS-bromssystem och 3,6 kg svänghjul. Maximal användarvikt är 110 kg enligt tillverkaren. | ja (153) |

### Löpband (44 produkter)

| Nr | Titel | Rad | Före | Efter | Ryms |
|---|---|---|---|---|---|
| 10001 | Löpband BH Fitness Inertia G588, 19-tum… | meta | Löpbandet BH Fitness Inertia G588 har 3,5 hk motor, hastighet 0,5–22 km/h, löpyta 155 x 55 cm och 19-tums pekskärm. Maximal användarvikt är 150 kg. | Löpbandet BH Fitness Inertia G588 har 3,5 hk motor, hastighet 0,5–22 km/h, löpyta 155 x 55 cm och 19-tums pekskärm. Maximal användarvikt är 150 kg enligt tillverkaren. | nej (167) |
| 10002 | Löpband BH Fitness Inertia G688 LED | meta | Löpbandet BH Fitness Inertia G688 LED har 4,5 hk motor, hastighet 0,8–24 km/h och löpyta 160 x 58 cm. Maximal användarvikt är 182 kg. | Löpbandet BH Fitness Inertia G688 LED har 4,5 hk motor, hastighet 0,8–24 km/h och löpyta 160 x 58 cm. Maximal användarvikt är 182 kg enligt tillverkaren. | ja (153) |
| 10003 | Löpband BH Fitness Inertia G788, 19-tum… | meta | Löpbandet BH Fitness Inertia G788 har 5,0 hk motor, hastighet 0,8–25 km/h, löpyta 160 x 58 cm och 19-tums pekskärm. Maximal användarvikt är 182 kg. | Löpbandet BH Fitness Inertia G788 har 5,0 hk motor, hastighet 0,8–25 km/h, löpyta 160 x 58 cm och 19-tums pekskärm. Maximal användarvikt är 182 kg enligt tillverkaren. | nej (167) |
| 10004 | Löpband BH Fitness Inertia G788, 22-tum… | meta | Löpbandet BH Fitness Inertia G788 har 5,0 hk motor, hastighet 0,8–25 km/h, löpyta 160 x 58 cm och 22-tums pekskärm. Maximal användarvikt är 182 kg. | Löpbandet BH Fitness Inertia G788 har 5,0 hk motor, hastighet 0,8–25 km/h, löpyta 160 x 58 cm och 22-tums pekskärm. Maximal användarvikt är 182 kg enligt tillverkaren. | nej (167) |
| 10006 | Löpband BH Fitness LX50 Multimedia, 22-… | meta | Löpbandet BH Fitness LX50 Multimedia har 22-tums pekskärm, 25 träningsprogram, hastighet 1–22 km/h och löpyta 154 x 55 cm. Maximal användarvikt är 150 kg. | Löpbandet BH Fitness LX50 Multimedia har 22-tums pekskärm, 25 träningsprogram, hastighet 1–22 km/h och löpyta 154 x 55 cm. Maximal användarvikt är 150 kg enligt tillverkaren. | nej (174) |
| 10007 | Löpband BH Fitness LX90 Multimedia, 22-… | meta | Löpbandet BH Fitness LX90 Multimedia har 3,5 AC-motor, 22-tums pekskärm, hastighet 1–22 km/h och löpyta 154 x 55 cm. Maximal användarvikt är 150 kg. | Löpbandet BH Fitness LX90 Multimedia har 3,5 AC-motor, 22-tums pekskärm, hastighet 1–22 km/h och löpyta 154 x 55 cm. Maximal användarvikt är 150 kg enligt tillverkaren. | nej (168) |
| 10008 | Löpband BH Fitness Movemia TR1000, 22-t… | meta | Löpbandet BH Fitness Movemia TR1000 har 6,0 hk motor, 22-tums pekskärm, hastighet 0,5–26 km/h och löpyta 160 x 58 cm. Maximal användarvikt är 195 kg. | Löpbandet BH Fitness Movemia TR1000 har 6,0 hk motor, 22-tums pekskärm, hastighet 0,5–26 km/h och löpyta 160 x 58 cm. Maximal användarvikt är 195 kg enligt tillverkaren. | nej (169) |
| 10009 | Löpband BH Fitness Movemia TR800 LED | meta | Löpbandet BH Fitness Movemia TR800 LED har 5,0 hk motor, LED-display, hastighet 0,8–22 km/h och löpyta 160 x 58 cm. Maximal användarvikt är 190 kg. | Löpbandet BH Fitness Movemia TR800 LED har 5,0 hk motor, LED-display, hastighet 0,8–22 km/h och löpyta 160 x 58 cm. Maximal användarvikt är 190 kg enligt tillverkaren. | nej (167) |
| 10010 | Löpband BH Fitness RCM Pro, LED-display | meta | Löpbandet BH Fitness RCM Pro har 3,5 AC-motor, LED dot matrix-display, 36 träningsprogram och hastighet 0,8–22 km/h. Maximal användarvikt är 180 kg. | Löpbandet BH Fitness RCM Pro har 3,5 AC-motor, LED dot matrix-display, 36 träningsprogram och hastighet 0,8–22 km/h. Maximal användarvikt är 180 kg enligt tillverkaren. | nej (168) |
| 10011 | Löpband BH Fitness RCM Pro TFT, 16-tums… | meta | Löpbandet BH Fitness RCM Pro TFT har 16-tums pekskärm, 3,5 AC-motor, 25 träningsprogram och hastighet 0,8–22 km/h. Maximal användarvikt är 180 kg. | Löpbandet BH Fitness RCM Pro TFT har 16-tums pekskärm, 3,5 AC-motor, 25 träningsprogram och hastighet 0,8–22 km/h. Maximal användarvikt är 180 kg enligt tillverkaren. | nej (166) |
| 10012 | Löpband BH Fitness RS1000 TFT, 16 tum | meta | Löpbandet BH Fitness RS1000 TFT har 16-tums TFT-skärm, 3,5 hk motor, 25 träningsprogram och hastighet 1–22 km/h. Maximal användarvikt är 150 kg. | Löpbandet BH Fitness RS1000 TFT har 16-tums TFT-skärm, 3,5 hk motor, 25 träningsprogram och hastighet 1–22 km/h. Maximal användarvikt är 150 kg enligt tillverkaren. | nej (164) |
| 10013 | Löpband BH Fitness i.F2W | meta | Löpbandet BH Fitness i.F2W har 6,8-tums LCD-skärm, 1,5 hk motor, hastighet 1–18 km/h och löpyta 135 x 51 cm. Maximal användarvikt är 115 kg. | Löpbandet BH Fitness i.F2W har 6,8-tums LCD-skärm, 1,5 hk motor, hastighet 1–18 km/h och löpyta 135 x 51 cm. Maximal användarvikt är 115 kg enligt tillverkaren. | nej (160) |
| 10014 | Löpband BH Fitness i.RC12 | meta | Löpbandet BH Fitness i.RC12 har LED-skärm, 14 träningsprogram, 4,5 hk motor och hastighet 1–22 km/h. Maximal användarvikt är 150 kg. | Löpbandet BH Fitness i.RC12 har LED-skärm, 14 träningsprogram, 4,5 hk motor och hastighet 1–22 km/h. Maximal användarvikt är 150 kg enligt tillverkaren. | ja (152) |
| 10015 | Löpband BH Fitness LX50, LCD-display | meta | Löpbandet BH Fitness LX50 har LCD-display, 8 träningsprogram, hastighet 1–22 km/h och löpyta 154 x 55 cm. Maximal användarvikt är 150 kg. | Löpbandet BH Fitness LX50 har LCD-display, 8 träningsprogram, hastighet 1–22 km/h och löpyta 154 x 55 cm. Maximal användarvikt är 150 kg enligt tillverkaren. | nej (157) |
| 10016 | Löpband BH Fitness LX90, LED-display | meta | Löpbandet BH Fitness LX90 har 3,5 AC-motor, LED-display, 8 träningsprogram, hastighet 1–22 km/h och löpyta 154 x 55 cm. Maximal användarvikt är 150 kg. | Löpbandet BH Fitness LX90 har 3,5 AC-motor, LED-display, 8 träningsprogram, hastighet 1–22 km/h och löpyta 154 x 55 cm. Maximal användarvikt är 150 kg enligt tillverkaren. | nej (171) |
| 10018 | Löpband BH Fitness Nydo, Hopfällbart | meta | Löpbandet BH Fitness Nydo har LED-display, 36 träningsprogram, hastighet 1–18 km/h och löpyta 140 x 50 cm. Maximal användarvikt är 130 kg. | Löpbandet BH Fitness Nydo har LED-display, 36 träningsprogram, hastighet 1–18 km/h och löpyta 140 x 50 cm. Maximal användarvikt är 130 kg enligt tillverkaren. | nej (158) |
| 10019 | Löpband BH Fitness Nyman Plus, Infällba… | meta | Löpbandet BH Fitness Nyman Plus är infällbart och har LCD-display, 36 träningsprogram och löpyta 125 x 45 cm. Maximal användarvikt är 115 kg. | Löpbandet BH Fitness Nyman Plus är infällbart och har LCD-display, 36 träningsprogram och löpyta 125 x 45 cm. Maximal användarvikt är 115 kg enligt tillverkaren. | nej (161) |
| 10020 | Löpband BH Fitness Pioneer Senior | meta | Löpbandet BH Fitness Pioneer Senior har LCD-skärm, 2,0 hk motor, hastighet 1–13 km/h, handstöd och låg ram. Maximal användarvikt är 100 kg. | Löpbandet BH Fitness Pioneer Senior har LCD-skärm, 2,0 hk motor, hastighet 1–13 km/h, handstöd och låg ram. Maximal användarvikt är 100 kg enligt tillverkaren. | nej (159) |
| 10023 | Löpband BH Fitness RS1200 Multimedia, 1… | meta | Löpbandet BH Fitness RS1200 Multimedia har 16-tums pekskärm, 3,5 hk motor, hastighet 1–22 km/h och löpyta 155 x 55 cm. Maximal användarvikt är 150 kg. | Löpbandet BH Fitness RS1200 Multimedia har 16-tums pekskärm, 3,5 hk motor, hastighet 1–22 km/h och löpyta 155 x 55 cm. Maximal användarvikt är 150 kg enligt tillverkaren. | nej (170) |
| 10026 | Löpband BH Fitness RS800, Hopfällbart | meta | BH Fitness RS800 är ett hopfällbart löpband med 3,5 hk motor och hastighet 1–20 km/h. Löpytan är 150 x 51 cm och maximal användarvikt är 130 kg. | BH Fitness RS800 är ett hopfällbart löpband med 3,5 hk motor och hastighet 1–20 km/h. Löpytan är 150 x 51 cm och maximal användarvikt är 130 kg enligt tillverkaren. | nej (164) |
| 10027 | Löpband BH Fitness RS800 Multimedia | meta | BH Fitness RS800 Multimedia är ett löpband med 10-tums pekskärm och 32 träningsprogram. Hastigheten är 1–20 km/h och maximal användarvikt är 130 kg. | BH Fitness RS800 Multimedia är ett löpband med 10-tums pekskärm och 32 träningsprogram. Hastigheten är 1–20 km/h och maximal användarvikt är 130 kg enligt tillverkaren. | nej (168) |
| 10027 | Löpband BH Fitness RS800 Multimedia | li | Dig som söker ett löpband med maximal användarvikt 130 kg | Dig som söker ett löpband med maximal användarvikt 130 kg, enligt tillverkaren |  |
| 10028 | Löpband BH Fitness RS900TFT, Hopfällbart | meta | BH Fitness RS900TFT är ett hopfällbart löpband med 15-tums TFT-skärm och 32 träningsprogram. Hastigheten är 1–22 km/h och maxvikt för användaren är 150 kg. | BH Fitness RS900TFT är ett hopfällbart löpband med 15-tums TFT-skärm och 32 träningsprogram. Hastigheten är 1–22 km/h och maxvikt för användaren är 150 kg enligt tillverkaren. | nej (175) |
| 10028 | Löpband BH Fitness RS900TFT, Hopfällbart | li | Dig som söker ett löpband med maximal användarvikt 150 kg | Dig som söker ett löpband med maximal användarvikt 150 kg, enligt tillverkaren |  |
| 10029 | Löpband BH Fitness Runlab Plus | meta | BH Fitness Runlab Plus är ett kompakt löpband med LED-display och Bluetooth-anslutning. Hastigheten är 1–15 km/h och maximal användarvikt är 110 kg. | BH Fitness Runlab Plus är ett kompakt löpband med LED-display och Bluetooth-anslutning. Hastigheten är 1–15 km/h och maximal användarvikt är 110 kg enligt tillverkaren. | nej (168) |
| 10029 | Löpband BH Fitness Runlab Plus | li | Dig som söker ett löpband med maximal användarvikt 110 kg | Dig som söker ett löpband med maximal användarvikt 110 kg, enligt tillverkaren |  |
| 10030 | Löpband BH Fitness RX3 | meta | BH Fitness RX3 är ett löpband med LED-display och 36 träningsprogram. Hastigheten är 1–15 km/h och maximal användarvikt är 110 kg. | BH Fitness RX3 är ett löpband med LED-display och 36 träningsprogram. Hastigheten är 1–15 km/h och maximal användarvikt är 110 kg enligt tillverkaren. | ja (150) |
| 10030 | Löpband BH Fitness RX3 | li | Dig som söker ett löpband med maximal användarvikt 110 kg | Dig som söker ett löpband med maximal användarvikt 110 kg, enligt tillverkaren |  |
| 10031 | Löpband BH Fitness Sherpa Run | meta | BH Fitness Sherpa Run är ett vikbart löpband med LED-skärm och 12 träningsprogram. Hastigheten är 0,8–14 km/h och maximal användarvikt är 110 kg. | BH Fitness Sherpa Run är ett vikbart löpband med LED-skärm och 12 träningsprogram. Hastigheten är 0,8–14 km/h och maximal användarvikt är 110 kg enligt tillverkaren. | nej (165) |
| 10031 | Löpband BH Fitness Sherpa Run | li | Dig som söker ett löpband med maximal användarvikt 110 kg | Dig som söker ett löpband med maximal användarvikt 110 kg, enligt tillverkaren |  |
| 10033 | Löpband Finnlo by Hammer Endurance TFT | meta | Finnlo by Hammer Endurance TFT är ett löpband med 15-tums pekskärm och 41 träningsprogram. Hastigheten är 1–24 km/h och maximal användarvikt är 160 kg. | Finnlo by Hammer Endurance TFT är ett löpband med 15-tums pekskärm och 41 träningsprogram. Hastigheten är 1–24 km/h och maximal användarvikt är 160 kg enligt tillverkaren. | nej (171) |
| 10033 | Löpband Finnlo by Hammer Endurance TFT | li | Dig som söker ett löpband med maximal användarvikt 160 kg | Dig som söker ett löpband med maximal användarvikt 160 kg, enligt tillverkaren |  |
| 10035 | Löpband Hammer Q. VADIS 10.0 | meta | Hammer Q. VADIS 10.0 är ett löpband med 15,6-tums pekskärm och 44 träningsprogram. Hastigheten är 0,3–22 km/h och maximal användarvikt är 150 kg. | Hammer Q. VADIS 10.0 är ett löpband med 15,6-tums pekskärm och 44 träningsprogram. Hastigheten är 0,3–22 km/h och maximal användarvikt är 150 kg enligt tillverkaren. | nej (165) |
| 10035 | Löpband Hammer Q. VADIS 10.0 | li | Dig som söker ett löpband med maximal användarvikt 150 kg | Dig som söker ett löpband med maximal användarvikt 150 kg, enligt tillverkaren |  |
| 10036 | Löpband Hammer Q. VADIS 3.0 | meta | Hammer Q. VADIS 3.0 är ett hopfällbart löpband med LCD-display och 14 träningsprogram. Hastigheten är 1–18 km/h och maximal användarvikt är 130 kg. | Hammer Q. VADIS 3.0 är ett hopfällbart löpband med LCD-display och 14 träningsprogram. Hastigheten är 1–18 km/h och maximal användarvikt är 130 kg enligt tillverkaren. | nej (167) |
| 10036 | Löpband Hammer Q. VADIS 3.0 | li | Dig som söker ett löpband med maximal användarvikt 130 kg | Dig som söker ett löpband med maximal användarvikt 130 kg, enligt tillverkaren |  |
| 10038 | Löpband Toorx City Compact, Pure Bronze | meta | Toorx City Compact i Pure Bronze är ett ultrakompakt löpband med 1,75 hk motor och hastighet 1–14 km/h. Maximal användarvikt är 100 kg. | Toorx City Compact i Pure Bronze är ett ultrakompakt löpband med 1,75 hk motor och hastighet 1–14 km/h. Maximal användarvikt är 100 kg enligt tillverkaren. | ja (155) |
| 10038 | Löpband Toorx City Compact, Pure Bronze | li | Dig som söker ett löpband med maximal användarvikt 100 kg | Dig som söker ett löpband med maximal användarvikt 100 kg, enligt tillverkaren |  |
| 10039 | Löpband Toorx City Compact, Rose Gold | meta | Toorx City Compact i Rose Gold är ett ultrakompakt löpband med 1,75 hk motor och hastighet 1–14 km/h. Maximal användarvikt är 100 kg. | Toorx City Compact i Rose Gold är ett ultrakompakt löpband med 1,75 hk motor och hastighet 1–14 km/h. Maximal användarvikt är 100 kg enligt tillverkaren. | ja (153) |
| 10039 | Löpband Toorx City Compact, Rose Gold | li | Dig som söker ett löpband med maximal användarvikt 100 kg | Dig som söker ett löpband med maximal användarvikt 100 kg, enligt tillverkaren |  |
| 10042 | Löpband Toorx Mirage S80 | meta | Toorx Mirage S80 är ett löpband med 4,5 hk motor och 24 träningsprogram. Hastigheten är 1–22 km/h, pulsbälte ingår och maxvikt är 160 kg. | Toorx Mirage S80 är ett löpband med 4,5 hk motor och 24 träningsprogram. Hastigheten är 1–22 km/h, pulsbälte ingår och maxvikt är 160 kg enligt tillverkaren. | nej (157) |
| 10042 | Löpband Toorx Mirage S80 | li | Dig som söker ett löpband med maximal användarvikt 160 kg | Dig som söker ett löpband med maximal användarvikt 160 kg, enligt tillverkaren |  |
| 10043 | Löpband Toorx Voyager | meta | Toorx Voyager är ett löpband med 2,75 hk motor och 24 träningsprogram. Hastigheten är 1–18 km/h och maximal användarvikt är 120 kg. | Toorx Voyager är ett löpband med 2,75 hk motor och 24 träningsprogram. Hastigheten är 1–18 km/h och maximal användarvikt är 120 kg enligt tillverkaren. | ja (151) |
| 10043 | Löpband Toorx Voyager | li | Dig som söker ett löpband med maximal användarvikt 120 kg | Dig som söker ett löpband med maximal användarvikt 120 kg, enligt tillverkaren |  |
| 10046 | Löpband Tunturi Centuri Performance T100 | meta | Tunturi Centuri Performance T100 är ett löpband med 10-tums LCD-skärm och 47 träningsprogram. Hastigheten är 0,8–20 km/h och maxvikt är 135 kg. | Tunturi Centuri Performance T100 är ett löpband med 10-tums LCD-skärm och 47 träningsprogram. Hastigheten är 0,8–20 km/h och maxvikt är 135 kg enligt tillverkaren. | nej (163) |
| 10046 | Löpband Tunturi Centuri Performance T100 | li | Dig som söker ett löpband med maximal användarvikt 135 kg | Dig som söker ett löpband med maximal användarvikt 135 kg, enligt tillverkaren |  |
| 10047 | Löpband Tunturi FitRun 90i PRO | meta | Tunturi FitRun 90i PRO är ett löpband med 7-tums LCD-display och 16 träningsprogram. Hastigheten är 0,8–20 km/h och maximal användarvikt är 130 kg. | Tunturi FitRun 90i PRO är ett löpband med 7-tums LCD-display och 16 träningsprogram. Hastigheten är 0,8–20 km/h och maximal användarvikt är 130 kg enligt tillverkaren. | nej (167) |
| 10047 | Löpband Tunturi FitRun 90i PRO | li | Dig som söker ett löpband med maximal användarvikt 130 kg | Dig som söker ett löpband med maximal användarvikt 130 kg, enligt tillverkaren |  |
| 10048 | Löpband Tunturi Platinum Core | meta | Tunturi Platinum Core är ett löpband med LED-skärm och 57 träningsprogram. Maximal användarvikt är 150 kg och produktvikten är 142 kg. | Tunturi Platinum Core är ett löpband med LED-skärm och 57 träningsprogram. Maximal användarvikt är 150 kg enligt tillverkaren och produktvikten är 142 kg. | ja (154) |
| 10048 | Löpband Tunturi Platinum Core | li | Dig som söker ett löpband med maximal användarvikt 150 kg | Dig som söker ett löpband med maximal användarvikt 150 kg, enligt tillverkaren |  |
| 10049 | Löpband Tunturi Platinum TR20 | meta | Tunturi Platinum TR20 är ett löpband med 10-tums skärm och 47 träningsprogram. Löpytan är 150 x 56 cm och maximal användarvikt är 165 kg. | Tunturi Platinum TR20 är ett löpband med 10-tums skärm och 47 träningsprogram. Löpytan är 150 x 56 cm och maximal användarvikt är 165 kg enligt tillverkaren. | nej (157) |
| 10049 | Löpband Tunturi Platinum TR20 | li | Dig som söker ett löpband med maximal användarvikt 165 kg | Dig som söker ett löpband med maximal användarvikt 165 kg, enligt tillverkaren |  |
| 10050 | Löpband Tunturi Signature T20 | meta | Tunturi Signature T20 är ett löpband med 44 träningsprogram. Hastigheten är 1–16 km/h och maximal användarvikt är 120 kg. | Tunturi Signature T20 är ett löpband med 44 träningsprogram. Hastigheten är 1–16 km/h och maximal användarvikt är 120 kg enligt tillverkaren. | ja (141) |
| 10050 | Löpband Tunturi Signature T20 | li | Dig som söker ett löpband med maximal användarvikt 120 kg | Dig som söker ett löpband med maximal användarvikt 120 kg, enligt tillverkaren |  |
| 10051 | Löpband Tunturi Signature T40 med 10-tu… | meta | Tunturi Signature T40 är ett löpband med 10-tums LCD-display, 44 träningsprogram, 3,5 hk motor och hastighet 1–16 km/h. Maximal användarvikt är 120 kg. | Tunturi Signature T40 är ett löpband med 10-tums LCD-display, 44 träningsprogram, 3,5 hk motor och hastighet 1–16 km/h. Maximal användarvikt är 120 kg enligt tillverkaren. | nej (171) |
| 10052 | Löpband Tunturi T50 med 44 Träningsprog… | meta | Tunturi T50 är ett löpband med 44 träningsprogram, 4,5 hk motor och hastighet 1–20 km/h. Löpytan är 140 x 50 cm och maximal användarvikt är 135 kg. | Tunturi T50 är ett löpband med 44 träningsprogram, 4,5 hk motor och hastighet 1–20 km/h. Löpytan är 140 x 50 cm och maximal användarvikt är 135 kg enligt tillverkaren. | nej (167) |
| 10054 | Löpband Tunturi Signature T80 med 10-tu… | meta | Tunturi Signature T80 är ett löpband med 10-tums LED-skärm, 47 träningsprogram och 5,5 hk motor. Hastigheten är 0,8–22 km/h och maxvikten 150 kg. | Tunturi Signature T80 är ett löpband med 10-tums LED-skärm, 47 träningsprogram och 5,5 hk motor. Hastigheten är 0,8–22 km/h och maxvikten 150 kg enligt tillverkaren. | nej (165) |
| 10055 | Löpband Tunturi Signature T90 med AC-mo… | meta | Tunturi Signature T90 är ett löpband med 5,0 HP AC-motor, 47 träningsprogram och hastighet 0,8–24 km/h. Maximal användarvikt är 150 kg. | Tunturi Signature T90 är ett löpband med 5,0 HP AC-motor, 47 träningsprogram och hastighet 0,8–24 km/h. Maximal användarvikt är 150 kg enligt tillverkaren. | ja (155) |
| 10056 | Löpband Tunturi Cardio Fit T10 med Blue… | meta | Tunturi Cardio Fit T10 är ett löpband med Bluetooth-anslutning, 2,25 hk motor och hastighet 1–12 km/h. Maximal användarvikt är 100 kg. | Tunturi Cardio Fit T10 är ett löpband med Bluetooth-anslutning, 2,25 hk motor och hastighet 1–12 km/h. Maximal användarvikt är 100 kg enligt tillverkaren. | ja (154) |
| 10057 | Löpband Tunturi Cardio Fit T25 med 19 P… | meta | Tunturi Cardio Fit T25 är ett löpband med LED-display, 19 träningsprogram och Bluetooth. Hastigheten är 0,8–14 km/h och maximal användarvikt är 110 kg. | Tunturi Cardio Fit T25 är ett löpband med LED-display, 19 träningsprogram och Bluetooth. Hastigheten är 0,8–14 km/h och maximal användarvikt är 110 kg enligt tillverkaren. | nej (171) |
| 10058 | Löpband Tunturi Cardio Fit T35 med 5-tu… | meta | Tunturi Cardio Fit T35 är ett löpband med 5-tums LCD-skärm, 41 träningsprogram och 1,5 hk motor. Hastigheten är 1–16 km/h och maximal användarvikt 100 kg. | Tunturi Cardio Fit T35 är ett löpband med 5-tums LCD-skärm, 41 träningsprogram och 1,5 hk motor. Hastigheten är 1–16 km/h och maximal användarvikt 100 kg enligt tillverkaren. | nej (174) |

### Crosstrainers och roddmaskiner (29 produkter)

| Nr | Titel | Rad | Före | Efter | Ryms |
|---|---|---|---|---|---|
| 9421 | Crosstrainer Christopeit CT 5 | li | Dig som behöver en crosstrainer med maximal användarvikt 110 kg | Dig som behöver en crosstrainer med maximal användarvikt 110 kg, enligt tillverkaren |  |
| 10156 | Crosstrainer BH Fitness Crystal 2.0 | p | Maximal användarvikt är 150 kg. | Maximal användarvikt är 150 kg enligt tillverkaren. |  |
| 10157 | Crosstrainer BH Fitness Crystal 2.0 Mul… | p | Steglängden är 43,5 cm och maximal användarvikt 150 kg. | Steglängden är 43,5 cm och maximal användarvikt 150 kg enligt tillverkaren. |  |
| 10160 | Crosstrainer BH Fitness Altai | p | Maximal användarvikt är 150 kg. | Maximal användarvikt är 150 kg enligt tillverkaren. |  |
| 10161 | Crosstrainer BH Fitness Easy Flex | p | Maximal användarvikt är 130 kg. | Maximal användarvikt är 130 kg enligt tillverkaren. |  |
| 10161 | Crosstrainer BH Fitness Easy Flex | meta | BH Fitness Easy Flex är en vikbar crosstrainer med 24 motståndsnivåer och 20 kg svänghjul. Maximal användarvikt är 130 kg. | BH Fitness Easy Flex är en vikbar crosstrainer med 24 motståndsnivåer och 20 kg svänghjul. Maximal användarvikt är 130 kg enligt tillverkaren. | ja (142) |
| 10163 | Crosstrainer BH Fitness FDC Studio | p | Steglängden är 51 cm och maximal användarvikt 130 kg. | Steglängden är 51 cm och maximal användarvikt 130 kg enligt tillverkaren. |  |
| 10164 | Crosstrainer BH Fitness Movemia EC1000 | p | Steglängden är 52 cm och maximal användarvikt 190 kg. | Steglängden är 52 cm och maximal användarvikt 190 kg enligt tillverkaren. |  |
| 10166 | Crosstrainer BH Fitness Movemia ERV1000… | p | Svänghjulet sitter baktill, steglängden är 52–55 cm och maximal användarvikt är 181 kg. | Svänghjulet sitter baktill, steglängden är 52–55 cm och maximal användarvikt är 181 kg enligt tillverkaren. |  |
| 10167 | Crosstrainer BH Fitness Movemia EV1000… | p | Maximal användarvikt är 190 kg. | Maximal användarvikt är 190 kg enligt tillverkaren. |  |
| 10169 | Crosstrainer Hammer Crossfly BT | p | Maximal användarvikt är 130 kg. | Maximal användarvikt är 130 kg enligt tillverkaren. |  |
| 10170 | Crosstrainer Hammer Loxon XTR | p | Maximal användarvikt är 150 kg. | Maximal användarvikt är 150 kg enligt tillverkaren. |  |
| 10171 | Crosstrainer Hammer SpeedMotion II | p | Svänghjulet väger 18 kg, steglängden är 50 cm och maximal användarvikt är 130 kg. | Svänghjulet väger 18 kg, steglängden är 50 cm och maximal användarvikt är 130 kg enligt tillverkaren. |  |
| 10172 | Crosstrainer Hammer CrossPace 5.0 NorsK | p | Svänghjulet väger 20 kg, steglängden är 50 cm och maximal användarvikt är 130 kg. | Svänghjulet väger 20 kg, steglängden är 50 cm och maximal användarvikt är 130 kg enligt tillverkaren. |  |
| 10173 | Crosstrainer Hammer CrossPace 7.0 NorsK | p | Steglängden är 52 cm, steghöjden 50 cm och maximal användarvikt 130 kg. | Steglängden är 52 cm, steghöjden 50 cm och maximal användarvikt 130 kg enligt tillverkaren. |  |
| 10174 | Crosstrainer Hammer Crosstech XTR BT | p | Steglängden är 32 cm och maximal användarvikt 130 kg. | Steglängden är 32 cm och maximal användarvikt 130 kg enligt tillverkaren. |  |
| 10175 | Crosstrainer Hammer Ellypsis E3500 | p | Steglängden är 32 cm och maximal användarvikt 150 kg. | Steglängden är 32 cm och maximal användarvikt 150 kg enligt tillverkaren. |  |
| 10178 | Crosstrainer Tunturi FitCross 50i | meta | Tunturi FitCross 50i är en crosstrainer med 5,5-tums LCD-skärm, 22 träningsprogram och 32 svårighetsgrader. Maximal användarvikt är 150 kg. | Tunturi FitCross 50i är en crosstrainer med 5,5-tums LCD-skärm, 22 träningsprogram och 32 svårighetsgrader. Maximal användarvikt är 150 kg enligt tillverkaren. | nej (159) |
| 10179 | Crosstrainer Tunturi Platinum CT20 | meta | Tunturi Platinum CT20 är en crosstrainer med 7-tums skärm, 26 träningsprogram och 48 svårighetsnivåer. Maximal användarvikt är 180 kg. | Tunturi Platinum CT20 är en crosstrainer med 7-tums skärm, 26 träningsprogram och 48 svårighetsnivåer. Maximal användarvikt är 180 kg enligt tillverkaren. | ja (154) |
| 10185 | Roddmaskin BH Fitness Kingston | meta | BH Fitness Kingston är en roddmaskin med dynamiskt luftmotstånd och LCD-skärm. Måtten är 244 x 51 x 114 cm och maximal användarvikt är 140 kg. | BH Fitness Kingston är en roddmaskin med dynamiskt luftmotstånd och LCD-skärm. Måtten är 244 x 51 x 114 cm och maximal användarvikt är 140 kg enligt tillverkaren. | nej (162) |
| 10187 | Roddmaskin Hammer Cobra XTR Plus | p | Rullängden är 118 cm och maximal användarvikt är 130 kg. | Rullängden är 118 cm och maximal användarvikt är 130 kg enligt tillverkaren. |  |
| 10187 | Roddmaskin Hammer Cobra XTR Plus | meta | Hammer Cobra XTR Plus är en roddmaskin med LCD-skärm, 20 träningsprogram och 16 svårighetsgrader. Maximal användarvikt är 130 kg. | Hammer Cobra XTR Plus är en roddmaskin med LCD-skärm, 20 träningsprogram och 16 svårighetsgrader. Maximal användarvikt är 130 kg enligt tillverkaren. | ja (149) |
| 10189 | Roddmaskin Hammer Maximum SpeedROW Comp… | p | Maximal användarvikt är 180 kg. | Maximal användarvikt är 180 kg enligt tillverkaren. |  |
| 10194 | Roddmaskin Toorx Rower Master | meta | Toorx Rower Master är en roddmaskin med LCD-konsol, 12 motståndsnivåer och manuell motståndsjustering. Maximal användarvikt är 130 kg. | Toorx Rower Master är en roddmaskin med LCD-konsol, 12 motståndsnivåer och manuell motståndsjustering. Maximal användarvikt är 130 kg enligt tillverkaren. | ja (154) |
| 10198 | Roddmaskin Fluid Viking 3 XL, Trä | meta | Fluid Viking 3 XL är en roddmaskin av amerikanskt askträ med Bluetooth-monitor. Maximal användarvikt är 150 kg. | Fluid Viking 3 XL är en roddmaskin av amerikanskt askträ med Bluetooth-monitor. Maximal användarvikt är 150 kg enligt tillverkaren. | ja (131) |
| 10199 | Roddmaskin Fluid Viking Pro XL, Trä | meta | Fluid Viking Pro XL är en vattenbaserad roddmaskin av amerikanskt askträ. Måtten är 213 x 54 x 56 cm och maximal användarvikt är 150 kg. | Fluid Viking Pro XL är en vattenbaserad roddmaskin av amerikanskt askträ. Måtten är 213 x 54 x 56 cm och maximal användarvikt är 150 kg enligt tillverkaren. | nej (156) |
| 10199 | Roddmaskin Fluid Viking Pro XL, Trä | li | Dig som söker en roddmaskin med maximal användarvikt 150 kg | Dig som söker en roddmaskin med maximal användarvikt 150 kg, enligt tillverkaren |  |
| 10200 | Roddmaskin Tunturi Cardio Fit R20 | meta | Tunturi Cardio Fit R20 är en hopfällbar roddmaskin med LCD-skärm och 4 motståndsnivåer. Maximal användarvikt är 100 kg. | Tunturi Cardio Fit R20 är en hopfällbar roddmaskin med LCD-skärm och 4 motståndsnivåer. Maximal användarvikt är 100 kg enligt tillverkaren. | ja (139) |
| 10202 | Roddmaskin Tunturi FitRow 50 | meta | Tunturi FitRow 50 är en hopfällbar roddmaskin med 5,5-tums LCD-skärm, 21 träningsprogram och 16 motståndsnivåer. Maximal användarvikt är 120 kg. | Tunturi FitRow 50 är en hopfällbar roddmaskin med 5,5-tums LCD-skärm, 21 träningsprogram och 16 motståndsnivåer. Maximal användarvikt är 120 kg enligt tillverkaren. | nej (164) |
| 10205 | Roddmaskin Tunturi Fluid Rower Apollo P… | meta | Tunturi Fluid Rower Apollo Plus är en roddmaskin med vattenmotstånd, Bluetooth-anslutning och 4 motståndsnivåer. Maximal användarvikt är 150 kg. | Tunturi Fluid Rower Apollo Plus är en roddmaskin med vattenmotstånd, Bluetooth-anslutning och 4 motståndsnivåer. Maximal användarvikt är 150 kg enligt tillverkaren. | nej (164) |
| 10207 | Roddmaskin Tunturi Fluid Rower Apollo P… | meta | Tunturi Fluid Rower Apollo Pro XL är en roddmaskin med 10 motståndsnivåer. Måtten är 213 x 54 x 56 cm och maximal användarvikt är 150 kg. | Tunturi Fluid Rower Apollo Pro XL är en roddmaskin med 10 motståndsnivåer. Måtten är 213 x 54 x 56 cm och maximal användarvikt är 150 kg enligt tillverkaren. | nej (157) |
| 10207 | Roddmaskin Tunturi Fluid Rower Apollo P… | li | Dig som vill ha en roddmaskin med maximal användarvikt 150 kg | Dig som vill ha en roddmaskin med maximal användarvikt 150 kg, enligt tillverkaren |  |
| 10210 | Roddmaskin Tunturi Signature R20 | meta | Tunturi Signature R20 är en hopfällbar roddmaskin med LCD-skärm, 6 träningsprogram och 16 motståndsnivåer. Maximal användarvikt är 120 kg. | Tunturi Signature R20 är en hopfällbar roddmaskin med LCD-skärm, 6 träningsprogram och 16 motståndsnivåer. Maximal användarvikt är 120 kg enligt tillverkaren. | nej (158) |

### Stänger, handtag och tillbehör (12 produkter)

| Nr | Titel | Rad | Före | Efter | Ryms |
|---|---|---|---|---|---|
| 9527 | Kabelhandtag Enhands Kort | meta | Kort enhands kabelhandtag i krom för kabelmaskin. Roterande, handtagets diameter är 2,5 cm och maximal belastning 200 kg. | Kort enhands kabelhandtag i krom för kabelmaskin. Roterande, handtagets diameter är 2,5 cm och maximal belastning 200 kg enligt tillverkaren. | ja (141) |
| 9528 | Kabelhandtag Enhands Kort, Par | meta | Två korta enhands kabelhandtag i krom som säljs som par. Roterande grepp, handtagets diameter 2,5 cm och maximal belastning 200 kg vardera. | Två korta enhands kabelhandtag i krom som säljs som par. Roterande grepp, handtagets diameter 2,5 cm och maximal belastning 200 kg vardera enligt tillverkaren. | nej (159) |
| 9529 | Kabelhandtag Enhands Lång | meta | Långt enhands kabelhandtag i krom för kabelstation. Roterande, handtagets diameter är 2,5 cm och maximal belastning 200 kg. | Långt enhands kabelhandtag i krom för kabelstation. Roterande, handtagets diameter är 2,5 cm och maximal belastning 200 kg enligt tillverkaren. | ja (143) |
| 9530 | Kabelhandtag Enhandsgrepp Bygel | meta | Kabelhandtag Enhandsgrepp Bygel i krom med roterande grepp. Handtagets diameter är 2,5 cm och maximal belastning 200 kg. | Kabelhandtag Enhandsgrepp Bygel i krom med roterande grepp. Handtagets diameter är 2,5 cm och maximal belastning 200 kg enligt tillverkaren. | ja (140) |
| 9534 | Roddhandtag Parallellt, 33 cm, Krom | meta | Det parallella roddhandtaget i krom har 33 cm mellan handtagen och räfflad greppyta. Diameter 2,6 cm och maximal belastning 200 kg. | Det parallella roddhandtaget i krom har 33 cm mellan handtagen och räfflad greppyta. Diameter 2,6 cm och maximal belastning 200 kg enligt tillverkaren. | ja (151) |
| 9536 | Kabelstång Rak och Roterande, 50 cm | meta | Rak och roterande kabelstång i krom, 50 cm lång med räfflade handtag. Stångens diameter är 2,5 cm och maximal belastning 200 kg. | Rak och roterande kabelstång i krom, 50 cm lång med räfflade handtag. Stångens diameter är 2,5 cm och maximal belastning 200 kg enligt tillverkaren. | ja (148) |
| 9541 | Kabelstång för Latsdrag, 118 cm, Krom | meta | Kabelstången för latsdrag i krom är 118 cm lång och väger 5 kg. Roterande med räfflad yta, diameter 2,5 cm och maximal belastning 200 kg. | Kabelstången för latsdrag i krom är 118 cm lång och väger 5 kg. Roterande med räfflad yta, diameter 2,5 cm och maximal belastning 200 kg enligt tillverkaren. | nej (157) |
| 9547 | Roddhandtag Parallell, 12 cm, Krom | meta | Det parallella roddhandtaget i krom har 12 cm mellan handtagen och räfflad greppyta på 12,5 cm. Maximal belastning 200 kg. | Det parallella roddhandtaget i krom har 12 cm mellan handtagen och räfflad greppyta på 12,5 cm. Maximal belastning 200 kg enligt tillverkaren. | ja (142) |
| 9548 | Roddhandtag Parallell Roterande med Gån… | meta | Parallellt roddhandtag med gångjärn och 12 cm mellan handtagen. Handtagets diameter är 2,5 cm och maximal belastning 200 kg. | Parallellt roddhandtag med gångjärn och 12 cm mellan handtagen. Handtagets diameter är 2,5 cm och maximal belastning 200 kg enligt tillverkaren. | ja (144) |
| 9549 | Roddhandtag Parallell Smal, 10 cm, Krom | meta | Smalt parallellt roddhandtag i krom med 10 cm mellan handtagen. Handtagets diameter är 2,5 cm och maximal belastning 200 kg. | Smalt parallellt roddhandtag i krom med 10 cm mellan handtagen. Handtagets diameter är 2,5 cm och maximal belastning 200 kg enligt tillverkaren. | ja (144) |
| 9550 | Roddhandtag Parallellt med Uppdelad Gre… | meta | Det parallella roddhandtaget i krom har uppdelad och centrerad räfflad greppyta, 12 cm bredd och maximal belastning 200 kg. | Det parallella roddhandtaget i krom har uppdelad och centrerad räfflad greppyta, 12 cm bredd och maximal belastning 200 kg enligt tillverkaren. | ja (143) |
| 34017 | Hantelstång Gymstick 35 cm, 2 kg, 30 mm | li | Maximal lastgräns: 100 kg | Maximal lastgräns: 100 kg (enligt tillverkaren) |  |

### Övrigt (7 produkter)

| Nr | Titel | Rad | Före | Efter | Ryms |
|---|---|---|---|---|---|
| 24110 | Sadelstolpsrack Racktime ClipIT 2.0, 20… | li | Lastkapacitet: 10 kg | Lastkapacitet: 10 kg (enligt tillverkaren) |  |
| 24112 | Cykelställ Peruzzo Siena för dragkrok,… | li | Maximal lastkapacitet: 60 kg | Maximal lastkapacitet: 60 kg (enligt tillverkaren) |  |
| 32037 | Styrstamshållare Basil Fixed Mounted, 2… | li | Maximal lastgräns: 5 kg | Maximal lastgräns: 5 kg (enligt tillverkaren) |  |
| 32039 | Stänkskärmset Hebie Alumee, 40 mm | li | Maximal lastgräns bakre stänkskärm: 8 kg per sida | Maximal lastgräns bakre stänkskärm: 8 kg per sida (enligt tillverkaren) |  |
| 32060 | Chinsstång Gymstick Door Gym Bar, för D… | li | Maximal användarvikt: 130 kg | Maximal användarvikt: 130 kg (enligt tillverkaren) |  |
| 32084 | Bälte Gymstick Dip Belt | li | Rekommenderad maximal belastning: 80 kg | Rekommenderad maximal belastning: 80 kg (enligt tillverkaren) |  |
| 32090 | Yogablock GS i EVA-skum, 23,5 x 15 x 8… | li | Maximal lastgräns: 150 kg | Maximal lastgräns: 150 kg (enligt tillverkaren) |  |

### Styrkemaskiner, ställ och racks (2 produkter)

| Nr | Titel | Rad | Före | Efter | Ryms |
|---|---|---|---|---|---|
| 10176 | Stegmaskin Toorx Everfit Step Twist | meta | Toorx Everfit Step Twist är en stegmaskin med display för stegantal, kalorier och tid samt justerbara handtag. Maximal användarvikt är 100 kg. | Toorx Everfit Step Twist är en stegmaskin med display för stegantal, kalorier och tid samt justerbara handtag. Maximal användarvikt är 100 kg enligt tillverkaren. | nej (162) |
| 10193 | Skiergometer Hammer Maximum SpeedSKI Co… | p | Maximal användarvikt är 180 kg. | Maximal användarvikt är 180 kg enligt tillverkaren. |  |

### Bänkar, stationer och multigym (2 produkter)

| Nr | Titel | Rad | Före | Efter | Ryms |
|---|---|---|---|---|---|
| 10349 | Träningsbänk Hammer Force 6.0 | li | Max. belastningskapacitet: 250 kg | Max. belastningskapacitet: 250 kg (enligt tillverkaren) |  |
| 32068 | Träningsstation för Dörröppning Gymstic… | li | Maximal lastgräns: 100 kg | Maximal lastgräns: 100 kg (enligt tillverkaren) |  |

### Cykelbärare, korgar och stödben (2 produkter)

| Nr | Titel | Rad | Före | Efter | Ryms |
|---|---|---|---|---|---|
| 24114 | Cykelkorg Basil Nordland MIK | li | Maximal lastkapacitet: 10 kg | Maximal lastkapacitet: 10 kg (enligt tillverkaren) |  |
| 32033 | Handväska Basil Bloom Field, 8–11 liter… | li | Bärkapacitet: Upp till 5 kg | Bärkapacitet: Upp till 5 kg (enligt tillverkaren) |  |

### Elcyklar och eltrehjulingar (1 produkter)

| Nr | Titel | Rad | Före | Efter | Ryms |
|---|---|---|---|---|---|
| 8797 | Elcykel ADO Air 28, 28 tum, Ljusgul | li | Lastkapacitet: 120 kg | Lastkapacitet: 120 kg (enligt tillverkaren) |  |

### Hemmaträning, stöd och handtag (1 produkter)

| Nr | Titel | Rad | Före | Efter | Ryms |
|---|---|---|---|---|---|
| 32065 | Parallettes Gymstick Hi-Rise | li | Maximal lastgräns: 150 kg | Maximal lastgräns: 150 kg (enligt tillverkaren) |  |

## 8. Kontroller (`skrivfil_kontroll.py`, läsläge på kopior; inga filer i repot ändrades)

Kontrollerna kördes på en temporär skrivfil med "före"- och "efter"-text per produkt. Jämförelsen visar bara nya fel som förslaget orsakar.

| Förslag | Produkter | Fel före | Fel efter | Nya fel | Nya varningar |
|---|---|---|---|---|---|
| Lista 1 | 4 | 0 | 0 | 0 | 0 |
| Lista 1 + lista 4 | 154 | 0 | 101 | 101 | 0 |

- Lista 1: nya fel 0. Fel som redan fanns före ändringen räknas inte som förslagets.
- Lista 4: 101 nya fel: 50 metabeskrivningar över 155 tecken och 51 texter med fler än två "enligt tillverkaren" (R5). Av 114 metaändringar ryms 64 inom 155 tecken; 50 kräver att annan text i metan kortas (inte föreslaget här). Totalt 51 texter skulle få fler än två "enligt tillverkaren" i beskrivningen.

## 9. Risk

- **Källrisk:** frasen sätter tillverkarens namn på en uppgift. För klass A bygger det på regelbokens definition, inte på att leverantören skriver "tillverkaren". För klass B finns inget stöd, därför inga förslag.
- **Regelrisk (alt B):** frasen på varje förekomst bryter R5 och gör metabeskrivningar längre än 155 tecken; texten blir mer upprepande utan att bli mer informativ för kunden.
- **Läsbarhetsrisk:** "Maximal användarvikt är 130 kg enligt tillverkaren" i en metabeskrivning tar 20 tecken av 155 och pressar bort annat innehåll.
- **Datarisk:** listan bygger på repots filer. Texter kan ha ändrats live; därför live-klassning (live-raden måste vara exakt "före") och återläsning tecken för tecken efter skrivning, som i rensning 1 och 2.
- **Teknisk risk:** rensning 1:s skript (`shopify_meta_rensning.py`) hanterar bara `seo.description`. Radändringar i beskrivningen kräver samma väg som rensning 2 den 4 november (`shopify_skriv_texter.py` med skrivfil). Indatafilen innehåller raderna före/efter för exakt strängbyte (varje rad måste finnas exakt en gång).

## 10. Filer

- Indata (körs inte): `rapporter/facit-bos-2026-10-31/vag2_skriv/rensning2_forslag.json` – lista med rensning 1:s fält (`id`, `nr`, `fil`, `titel`, `seo_title`, `meta_gammal`, `meta_ny`) och utökade fält `typ`, `status`, `kor` (alltid false), `forslag`, `alt_b`, `osakra`, `meta_ny_alt_b`, `notering`. `meta_ny` är bara ändrad där en lista 1-ändring gäller metan; annars lika med `meta_gammal`.
- Skript som tar fram listan: `shopify-sync/scripts/rensning2_underlag.py` (läser bara repots filer; inget nätverk).
