# Granskningsutlåtande k_49t4: tom eller tunn källa enligt v1.12 (2026-11-08)

Granskaren har bara läst i Shopify och har inte ändrat något där eller committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient; `verifiera_butik` gav BEST OF SPORTS). `mcp__Shopify__*` användes inte. Underlaget var CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.12), BESLUTSLOGG till och med 2026-11-08, LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md` och formatet i `k_utlatande_43.json`.

Granskningen omfattade 10 utkast och 3 avvisade produkter, och alla är ACTIVE. Standardblocket är exakt rätt på alla. Leveranstidsmeningen finns bara på 49305, som också är den enda produkten med taggen På beställning. Efter rättningarna gäller följande:

- Titlarna har högst 54 tecken och högst 1 kommatecken.
- SEO-titlarna har högst 40 tecken.
- Metatexterna har 84–126 tecken och innehåller verb.

Titel, SEO-titel och metatext krockar inte med någon annan fil i `vag2_skriv`. Butiken söktes på Steel, Ding, Minnie, Regnskydd, Hamax, Fiido T2, Back Support, Barbell Pad, Armbågsstöd, Kid MTB, Canopy, Träningshjul, Stödhjul och på EAN. Ingen av produkterna är en dubblett av en skriven eller aktiv produkt. Varje rättning är ett sammanhängande före/efter-par per fält, och varje före-text förekommer exakt en gång i utkastet (kontrollerat i Python).

`skrivfil_kontroll.py` kördes på de rättade texterna. Den gav 0 formatfel men 2 spärrfel (49304 och 49309, se frågorna nedan).

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_49t4.json`.

## Resultat: 8 GODKÄND, 2 RÄTTA, 0 UNDERKÄND

| nr | id | dom | rättade fält / anmärkning |
|---|---|---|---|
| 49301 | 10523491434762 | RÄTTA | titel (Träningshjul betyder ab-hjul i butiken; "till cykel" läggs till) |
| 49302 | 10523491467530 | GODKÄND | – |
| 49303 | 10530130854154 | GODKÄND | – |
| 49304 | 10554352894218 | GODKÄND | **Spärrad** (utanfor-tills-vidare-2026-11-04) |
| 49305 | 10565595726090 | GODKÄND | – |
| 49306 | 10581104754954 | GODKÄND | – |
| 49307 | 10581104918794 | GODKÄND | – |
| 49308 | 10581105901834 | GODKÄND | – |
| 49309 | 10612569112842 | GODKÄND | **Spärrad** (utanfor-tills-vidare-2026-11-04) |
| 49310 | 10502528008458 | RÄTTA | titel, seo_title, meta, html (engelska Canopy frame byts mot butikens ord Kapellställning) |

### Rättningar (före → efter)

- **49301 titel:** "Träningshjul Giant Steel för 16–20 tum" → "Träningshjul Giant Steel till cykel, 16–20 tum"
- **49310 titel:** "Canopy frame Cargobike of Sweden 2-kids för Classic" → "Kapellställning Cargobike of Sweden 2-kids för Classic"
- **49310 seo_title:** "Canopy frame Cargobike 2-kids Classic" → "Kapellställning Cargobike 2-kids Classic"
- **49310 meta:** "Canopy frame 2-kids från Cargobike of Sweden är avsedd för modellen Classic. Artikelnummer 1521-16." → "Kapellställningen 2-kids från Cargobike of Sweden är avsedd för lastcykelmodellen Classic. Artikelnummer 1521-16."
- **49310 html:** ett sammanhängande stycke från inledningen till typraden. "Canopy frame" byts mot "Kapellställningen" eller "kapellställning", och typraden blir "Typ: Kapellställning (canopy frame)". Den exakta texten finns i JSON-filen.

## Tillverkarkällor (minst en kontroll per produkt)

| nr | Kontroll | Utfall |
|---|---|---|
| 49301 | giant-bicycles.com (partnumber 910522) | "Suits 16" - 20" wheels" stämmer. Ingen lastgräns. |
| 49305 | uk.fiido.com/products/rear-pegs-for-t2 | "Rear Pegs for T2" stämmer. Ingen lastgräns. |
| 49309 | zefal.com 616 Kid MTB | Sidan gav ingen produktdata. EAN kopplas till Kid MTB Mudguard Set av återförsäljare. |
| 49304 | Webbsökning på EAN | bike-discount.de: Hamax Rain Cover för barncykelstol. Det är en återförsäljare, inte tillverkaren. |
| 49302 och 49310 | Webbsökning på namn och artikelnummer | Ingen tillverkarsida hittades. |
| 49306, 49307 och 49308 | gymstick.com | Svarar 403. Webbsökningen gav ingen träff på artikelnumren. |

Där ingen tillverkarsida finns bygger texterna bara på titeln och egen källa, vilket v1.12 tillåter.

## Löften och påståenden

Följande ord från källorna är rätt utelämnade:

- **49306:** kompression, minskad skaderisk, hållning, stabilitet, träna säkrare, högkvalitativa.
- **49307:** ultimata, säkerhet, stötdämpning, minskat tryck, bekvämlighet.
- **49308:** förbättra prestation, skydda, kompression, slitstarka.

"Skydd" och "stöd" förekommer bara som typord från källan (nackskydd, ryggstöd, armbågsstöd, regnskydd, stänkskydd), aldrig som löfte. Barnprodukterna (49303, 49304 och 49309) har inga säkerhets-, skydds- eller utvecklingspåståenden.

Lastgräns enligt v1.10: 49301 och 49305 har "Maximal lastgräns: Ej känd" och en mening om detta, vilket är rätt. 49304 (regnskydd) och 49310 (kapellställning) har ingen lastgräns, vilket också är rätt. De bär ingen last, och barntransport är undantagen.

Varianter: bara 49306 har flera varianter (S/M och L/XL, samma pris, samma artikel). Det uppfyller v1.8, och titeln låser ingen storlek.

## Avvisade (k_49t4_avvisade.json): alla tre avvisningar står fast

- **49401** Giant Airway Sport Sidepull: varianterna heter bara efter SKU, och "(L)" och "Svart/Blå" är oförklarade.
- **49402** Justerbart handtag: varianterna L och S kan vara olika motståndsklasser, alltså olika artiklar.
- **49403** Horisontell stång med remskiva: egen källa och tillverkaren motsäger varandra om 4 eller 5 stationer, och tillverkarens EAN stämmer inte med butikens.

## Frågor till David

1. 49304 (Hamax regnskydd) och 49309 (Zefal Kid MTB) står på spärrlistan `utanfor-tills-vidare-2026-11-04` (barn). Beslutet från 2026-11-08 tillåter text på aktiva barnprodukter, men spärrlistan har inte uppdaterats, så `skrivfil_kontroll.py` stoppar båda. Ska de få ett undantag? Granskaren har inte ändrat spärrlistan.
2. 49301: i butiken och i profilens `godkanda_typord` betyder "Träningshjul" ab-hjul. Cykelns hjul heter "Stödhjul" i andra produkter (Polaver, Selle Monte Grappa). Ska typordet bytas till Stödhjul? Det kräver ditt besked, eftersom live-titeln säger Träningshjul (R7).
3. 49310: ska Kapellställning läggas in som godkänt typord i profilen för canopy frame och canopy bows?
