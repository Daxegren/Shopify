# Granskning faktatext f_4 (motions- och spinningcyklar) – BEST OF SPORTS (2026-11-04)

Oberoende granskning, endast läsning. Butiken bekräftad med get-shop-info: **BEST OF SPORTS** (bestofsports.se, SEK).

**Underlag:** `vag2_skriv/f_4_utkast.json` (24 poster, nr 10076–10100 utom 10091), `f_4_avvisade.json` (10091). Läge: FAKTATEXTLÄGE (standarden §14–17, `fakta_utkastprompt.md`); meta 70–155 tecken (§17); standardblocket jämfört med `b_skriv_24.json`.

**Metod:** alla 24 hämtade live (graphql `nodes`: title, status, productType, vendor, tags, descriptionHtml, seo, variants). Alla ACTIVE, en variant var (Default Title). Varje titel, SEO-titel, meta och html lästes mot live-källan. Maskinellt: längder, kommatecken, gemen efter kolon, unikhet mot alla övriga `*_utkast.json`/`*_skriv*.json`, standardblocket.

## Resultat
| Dom | Antal | Nr |
|---|---|---|
| GODKÄND | 13 | 10077, 10078, 10079, 10082, 10083, 10084, 10086, 10092, 10095, 10096, 10097, 10098, 10099 |
| RÄTTA | 6 | 10076, 10080, 10081, 10088, 10089, 10090 |
| UNDERKÄND | 5 | 10085, 10087, 10093, 10094, 10100 |

## Regelkontroll
- Titlar 29–65 tecken (70 efter rättning av 10076), högst 1 kommatecken. SEO-titlar 27–40 tecken, unika. Meta 106–134 tecken (inom 70–155), unika. Inga dubbletter mot övriga filer.
- Standardblocket identiskt med `b_skriv_24.json`; meningen om beställningsvara finns exakt på de 9 produkter som har taggen "På beställning" live och saknas på övriga.
- 'Belastning 14 kg' (10076), 'Load capacity' (10087, 10093, 10094, 10100) och 'Q-faktor 190' (10090) finns inte kvar i någon text.
- Inga säkerhets-, stabilitets-, rehab-, hälso- eller träningseffektpåståenden kvar; tillverkningsland (Spanien, Tyskland) utelämnat. Tillverkarpåståenden (appar, FTMS, Poly-V-rem, ZeroFriction, pulssensorer, träoptik) står med "enligt tillverkaren".
- 'Maximal driftsvikt': i 10085, 10087, 10093, 10094 och 10100 är det en egen översättning av engelska 'Maximum operating weight' och står inte ordagrant i källan → underkänt. I 10090 står 'Maximal driftsvikt: 130 kg' ordagrant på svenska i live-källan och godtas.
- Titeltyper: Motionscykel/Spinningcykel följer live-titlarna (engelska 'Exercise bike'/'Spinning bike' översatta). 10080 kallas spinningcykel i källans brödtext men Motionscykel i titeln; titelns typ behålls.
- Läckage från syskonprodukter: inget hittat (Lyon Climber/Multimedia, XTB/MED/Multimedia, Duke/Duke Magnetic, Spheris/NorsK jämförda rad för rad). 10091 korrekt avvisad som dubblett av 10079 (samma SKU H9117); även 10656691683594 (H9117) och 10656691585290/10656691618058 (H9117TFT) är dubbletter i butiken och utanför batchen.

## Per produkt
| Nr | Id | Dom | Före → efter / skäl |
|---|---|---|---|
| 10076 | 10612581990666 | RÄTTA | titel: "Motionscykel BH Fitness Carbon Bike RS med 10-tums Pekskärm" → "Motionscykel BH Fitness Carbon Bike RS Multimedia med 10-tums Pekskärm" Modellnamnet Multimedia (live-titel, handle, SKU H8705BTFT) får inte strykas ur titeln (70 tecken, inom gränsen). Belastning 14 kg korrekt borta. |
| 10077 | 10472262041866 | GODKÄND |  |
| 10078 | 10650208370954 | GODKÄND |  |
| 10079 | 10656691650826 | GODKÄND |  |
| 10080 | 10656691552522 | RÄTTA | seo_title: "Motionscykel BH Fitness Lyon Climber MM" → "BH Fitness Lyon Climber Multimedia" Förkortningen MM finns inte i källan. Not: källans brödtext kallar den spinningcykel, titeln Motionscykel; titelns typ behålls. |
| 10081 | 10635764138250 | RÄTTA | html: "<li>Bromssystem: magnetiskt</li>" → "<li>Bromssystem: Magnetiskt</li>" Stor bokstav efter kolon. |
| 10082 | 10589715104010 | GODKÄND |  |
| 10083 | 10605381550346 | GODKÄND |  |
| 10084 | 10612594344202 | GODKÄND |  |
| 10085 | 10468768284938 | UNDERKÄND | Engelsk källa. 'Maximal driftsvikt 115 kg' är en egen översättning av 'Maximum operating weight' (inte ordagrant, och driftsvikt betyder på svenska maskinens egen vikt i drift, inte användarvikt). Bromssystemet motsägelsefullt (friction brake/hydraulic brake). Utan maxvikt återstår bara mått och vikt. |
| 10086 | 10472305164554 | GODKÄND |  |
| 10087 | 10472323383562 | UNDERKÄND | Engelsk källa. 'Maximal driftsvikt 150 kg' är översättning av 'Maximum operating weight' (inte ordagrant, tvetydig). 'Load capacity 20 kg' oförklarad (korrekt borta). Brödtexten är Duke-modellens, inte Magnetic. |
| 10088 | 10656691454218 | RÄTTA | html: "<li>Bromssystem: friktionsbroms</li>" → "<li>Bromssystem: Friktionsbroms</li>" Stor bokstav efter kolon. |
| 10089 | 10472305099018 | RÄTTA | html: "svänghjul på 20 kg och bromssystemet PMS, manuell." → "svänghjul på 20 kg och bromssystem av typen PMS, manuell." Grammatik i inledningen. |
| 10090 | 10472308113674 | RÄTTA | seo_title: "Spinningcykel BH Fitness Xcalibur MM" → "BH Fitness Xcalibur Multimedia"; html: "<li>Skärm: 16-tums, pekkänslig</li>" → "<li>Skärm: 16 tum, pekkänslig</li>" MM är påhittad förkortning; 16-tums följt av kommatecken är ogrammatiskt (källan: 16-tum, pekkänslig). Q-faktor 190 korrekt borta. Maximal driftsvikt 130 kg står ordagrant på svenska i live-källan och får stå. Källan kallar modellen XCalibur Magnetic i brödtexten; titel och SKU H9340TFT stödjer Multimedia. |
| 10092 | 10471040188682 | GODKÄND |  |
| 10093 | 10472325513482 | UNDERKÄND | Engelsk källa. 'Maximal driftsvikt 180 kg' (översättning av 'Maximum operating weight') och '40 nivåer' (av 'Load range: 40') är tolkningar. Svänghjulet 10 kg står entydigt i brödtexten ('10 kg flywheel') och stämmer med 'Load capacity: 10 kg', så den uppgiften i sig håller. Källan kallar modellen Sphere 4.0; handle slutar 10015 men SKU är 10014. |
| 10094 | 10471334084874 | UNDERKÄND | Engelsk källa. 'Maximal driftsvikt 180 kg' är översättning av 'Maximum operating weight'. Källan har dubbla skärmrader och oförklarad 'Load capacity 10 kg' (korrekt borta). |
| 10095 | 10650166690058 | GODKÄND |  |
| 10096 | 10656692011274 | GODKÄND |  |
| 10097 | 10472268267786 | GODKÄND |  |
| 10098 | 10656691978506 | GODKÄND |  |
| 10099 | 10624086507786 | GODKÄND |  |
| 10100 | 10472324595978 | UNDERKÄND | Engelsk och maskinöversatt källa ('backpack pedal trance'), '10 workout levels' motsäger, 'Load capacity 14 kg' oförklarad (korrekt borta). 'Maximal driftsvikt 150 kg' är översättning av 'Maximum operating weight'. §16.6. Typen 'Liggande Motionscykel' (Recumbent bike) är i sig rimlig. |

## Öppna frågor till David
1. Engelska källor med 'Maximum operating weight' (5 cyklar): ska det översättas till 'maximal användarvikt', eller ska maxvikten strykas och produkterna skrivas med bara mått/skärm/program? Tills dess underkända.
2. Dubbletterna av Lyon Climber (H9117 ×3, H9117TFT ×3) i butiken bör hanteras i sammanslagningsplanen.
