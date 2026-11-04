# Textutrullning BEST OF SPORTS – status

Genereras av `shopify-sync/scripts/status_uppdatera.py` (2026-11-04). Redigera inte för hand; öppna frågor ligger i `oppna_fragor.json`.
Regler: `shopify-sync/regler/regler-v1.md`. Beslut: `shopify-sync/docs/BESLUTSLOGG.md`. Profil: `shopify-sync/config/butiksprofil-bestofsports.json`.

**Fitnessgruppen:** 498 produkter skrivna och verifierade i batcherna nedan (utöver tidigare vågor). Avvisade i batcherna: 66.

| Batch | Inventerade | Utkast | Avvisade | Dom (godk/rättas/underk) | Skrivfil | Steg |
|---|---|---|---|---|---|---|
| f_1 | 25 | 24 | 1 | 17/7/0 | 24 | skriven |
| f_2 | 25 | 24 | 1 | 6/16/2 | 22 | skriven |
| f_3 | 25 | 25 | 0 | 11/14/0 | 25 | skriven |
| f_4 | 25 | 24 | 1 | 13/6/5 | 19 | skriven |
| f_5 | 25 | 25 | 0 | 15/10/0 | 25 | skriven |
| f_6 | 25 | 24 | 1 | 9/15/0 | 24 | skriven |
| f_7 | 25 | 23 | 2 | 16/7/2 | 23 | skriven |
| f_8 | 25 | 25 | 0 | 22/3/0 | 25 | skriven |
| f_9 | 25 | 23 | 2 | 17/6/2 | 23 | skriven |
| f_10 | 25 | 23 | 2 | 1/22/2 | 23 | skriven |
| f_11 | 25 | 21 | 4 | 15/6/4 | 21 | skriven |
| f_12 | 25 | 21 | 4 | 7/13/5 | 20 | skriven |
| f_13 | 25 | 18 | 7 | 9/9/7 | 18 | skriven |
| f_14 | 25 | 19 | 6 | 13/5/7 | 17 | skriven |
| f_15 | 25 | 25 | 0 | 4/20/1 | 24 | skriven |
| f_x1 | 7 | 7 | 0 | 4/3/0 | 7 | skriven |
| g_1 | 25 | 23 | 2 | 15/7/1 | 22 | skriven |
| g_2 | 25 | 22 | 3 | 11/11/3 | 22 | skriven |
| g_3 | 25 | 11 | 14 | 4/2/5 | 6 | skriven |
| g_4 | 12 | 7 | 5 | 5/2/0 | 7 | skriven |
| h_1 | 25 | 25 | 0 | 20/5/0 | 25 | skriven |
| h_2 | 25 | 25 | 0 | 16/9/0 | 25 | skriven |
| h_3 | 25 | 24 | 1 | 11/12/1 | 23 | skriven |
| h_4 | 25 | 23 | 2 | 15/8/0 | 23 | skriven |
| h_5 | 25 | 21 | 4 | 17/4/0 | 21 | skrivfil |
| h_6 | 25 | 21 | 4 | 15/6/0 | 21 | skrivfil |
| h_7 | 5 | 5 | 0 | 2/3/0 | 5 | skriven |

Steg: in → utkast → granskad → skrivfil → skriven (skrivrapport finns). f_x1 och fix-filer (f_*fix) ingår i huvudbatcherna.

## Öppna frågor till David
- F1 (2026-11-04): Pilotens 20 produkter: fortsätt hålla dem utanför (nu), eller räkna dem som avslutade? Två skrevs av misstag (10103, 10110)
- F2 (2026-11-04): Ska 'enligt tillverkaren' stå på alla lastgränser? Idag på 2 av 24 texter med maxvikt i f_1–f_15
- F3 (2026-11-04): Golvmatta eller Träningsmatta som typord för mattor under maskiner?
- F4 (2026-11-04): Dubbletter i butiken (Autark 5.0 10384/10386, Centuri E100 10126/10142, Lyon Climber H9117, 10158/10165): ta med i sammanslagningsplanen?
- F5 (2026-11-04): Avvisade produkter med flera varianter (10254, 10257, 10258, 10264, 10276, 10278, 10307, 10317, 10321–10323, 10329, 10333, 10335): dela upp varianter i butiken eller be leverantören rätta?
- F6 (2026-11-04): Märket 'FLUID' i versaler på tre roddtillbehör (10061, 10065, 10067): rätta till 'Fluid'?
- F7 (2026-11-04): API-vägen: tillåt myshopify-adressen, skapa app (read/write_products) och lägg token som hemlig variabel
- F8 (2026-11-04): CLAUDE.md: ok att lägga in en kort rad som pekar på regelbok, beslutslogg och profil så de läses vid start?
- F9 (2026-11-04): Elektronik som pulsband och vågar: tillåtet som ren teknisk fakta, eller utanför? Kroppsanalysvågar (hälsoparametrar) ligger nu utanför. Typordet Träningshjul (10502 live, Exercise wheel) är inte godkänt i profilen: godkänn eller byt
- F10 (2026-11-04): Cirka 30 skrivna fitnessprodukter har meta som slutar med utfyllnaden 'Finns hos BEST OF SPORTS.' fast metan redan är över 70 tecken. Rensa den i ett svep när API-vägen finns (enkel textersättning)?
- F11 (2026-11-04): Svettdräkter (t.ex. Sauna Smoke 10599): skrivs idag som ren fakta utan löften om svettning/viktminskning. Okej, eller utanför? Även: produkter som bär kroppsvikt men saknar lastgräns (speedball, balansredskap): säkerhetsprodukter eller inte?
- F12 (2026-11-04): Tunturi Allround Boxing Gloves 16 oz har live 'ger stöd åt handleden' i metan utan 'enligt tillverkaren'. Prövas separat (stödpåstående, R5)
