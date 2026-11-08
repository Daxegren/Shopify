# Granskningsutlåtande k_47b8 (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS). `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (aktiva produkter utan text får faktatext även i tidigare utanför-kategorier), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md` och formatet i `k_utlatande_43.json`.

Båda utkasten bygger på vår egen tidigare facit 30-text. Enligt R3 räknas den inte som källa. Granskaren har därför kontrollerat varje uppgift mot leverantörens originaltext i `rapporter/shopify-original-2026-10-31/facit30-original.json`. Där stod allt som utkasten innehåller.

Kontroller: `skrivfil_kontroll.py` gav 0 fel och 0 varningar, både på utkastet och på den rättade versionen. Standardblocket är tecken för tecken lika det kanoniska blocket i `b_skriv_24.json`. Ingen av produkterna har taggen På beställning, så ingen leveranstidsmening behövs. Titlarna har 54 och 49 tecken och två kommatecken var. SEO-titlarna har 31 och 34 tecken. Metatexterna har 154 och 141 tecken efter rättning. Titel, SEO-titel och meta krockar inte med någon annan utkast- eller skrivfil. I butiken finns inga dubbletter: sökningen gällde SKU, EAN, Spencer-korgar och alla Tabou Rocket-produkter. Varje rättning är ett sammanhängande före/efter-par per fält, och före-texten förekommer exakt en gång i utkastet (kontrollerat i Python).

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_47b8.json`.

## Resultat: 0 GODKÄND, 2 RÄTTA, 0 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 49001 | 10472248115466 | k_47b8_utkast.json | RÄTTA | html, meta |
| 49002 | 10526099210506 | k_47b8_utkast.json | RÄTTA | html, meta |

### 49001 Frontkorg för Barncykel Spencer, 16–24 tum, Svart Stål

Produkten är ACTIVE med en variant, EK-SP027-M (streckkoden är samma som SKU, ingen EAN), 159 kr och lager 15. Leverantörens text bekräftar:
- hjulstorlekarna 16, 18, 20 och 24 tum
- svartlackerat stålnät
- en klämma mellan styrkronorna för 1 tums (25,4 mm) gaffelrör
- måtten 25 x 17 x 18 cm
- att monteringsplatta, bultar, muttrar och brickor medföljer

Källans felrad "Cykelhjälm för barn Spencer" och ordet "starkt" är rätt utelämnade. Texten innehåller inga säkerhets-, skydds- eller kvalitetslöften. Produkten är ingen dubblett: den röda (EK-SP020-P) och den rosa (EK-SP028-R) Spencer-korgen är andra artiklar. Korgar skrivs utan rad om lastgräns, enligt praxis (24070, 28044, 28210). Den gamla FAQ-delen är borttagen (R15).

Rättningen gäller R11: den första meningen i html och i meta saknade verb.

- html före: `<p>Spencer frontkorg för barncykel i svartlackerat stålnät, lämplig för cyklar med 16, 18, 20 och 24 tums hjul.</p>`
- html efter: `<p>Spencer frontkorg för barncykel är gjord av svartlackerat stålnät och passar cyklar med 16, 18, 20 och 24 tums hjul.</p>`
- meta före: `Spencer frontkorg i svartlackerat stålnät för barncyklar med 16–24 tums hjul.`
- meta efter: `Spencer frontkorg i svartlackerat stålnät som passar barncyklar med 16–24 tums hjul.`

### 49002 Barncykel Tabou Rocket Alu, 14 tum, Svart och Röd

Produkten är ACTIVE med en variant, TAB27-0340 (EAN 5904257320209), 4 779 kr och lager 7. Leverantörens text bekräftar:
- aluminiumram
- ramstorlek 24 cm
- 1 växel
- V-broms och fotbroms
- vikten 8,2 kg utan tillbehör
- avtagbara stödhjul, skjutstång och korg fram
- listan över vad som ingår

Utkastaren flaggade fotbroms, vikt och ramstorlek som obekräftade, men alla tre står i leverantörens text. Hjulstorleken 14 tum kommer från leverantörens titel. "Lätt" och "utmärkt första cykel" är rätt borttagna. Längdintervallet 95–110 cm står i källan; att det utelämnas är inget fel. Produkten är ingen dubblett: Rocket Alu i svart-blått (TAB26-0320) och Rocket Alu 16 tum i svart-rött (TAB27-0370) är andra artiklar.

Rättningarna:
- "Lära sig cykla" är ett utvecklingslöfte. Raden ersätts på samma sätt som i 28219.
- Den första meningen i meta saknade verb (R11).

- html före: `<li>Barn som ska lära sig cykla (avtagbara stödhjul och skjutstång för föräldern)</li>`
- html efter: `<li>Dig som vill ha en barncykel med avtagbara stödhjul och skjutstång</li>`
- meta före: `Barncykel med aluminiumram och 14-tums hjul.`
- meta efter: `Barncykeln Tabou Rocket Alu har aluminiumram och 14-tums hjul.`

## Prövning av avvisningarna (k_47b8_avvisade.json)

Granskaren läste alla 12 produkterna live. Ingen avvisning är uppenbart fel, och **ingen produkt lyfts ur**.

| nr | id | bedömning |
|---|---|---|
| 49101 | 10472286126346 | Avvisningen står. Källan säger "stödben … med bakre fjädring. Avstånd 40mm". Produkttypen är oklar. |
| 49102 | 10472302444810 | Avvisningen står. Beskrivningen är tom (R3). |
| 49103 | 10494698881290 | Avvisningen står. Källan består bara av "Maximal användarvikt 60 kg." Det är en svensk rad med etikett, så skälet "utan etikett" är fel i detalj. Men raden är det enda faktumet utöver titeln, så källan är för tunn (R3). |
| 49104 | 10502528008458 | Avvisningen står. Beskrivningen är tom, och produkten är en lastcykeldel för barntransport. |
| 49105, 49106 | 10676715258122, 10676715323658 | Avvisningen står. Båda är aktiva och har samma SKU 1521-22 och EAN 7350097561209, så de är exakta dubbletter (R12a). Lager 0. |
| 49107 | 10472238678282 | Avvisningen står. Beskrivningen är tom. |
| 49108 | 10472240382218 | Avvisningen står. Källan är marknadsföringstext ("säkerställer … stabil infästning") och saknar EAN. Vad adaptern gör framgår inte entydigt. |
| 49109 | 10472245330186 | Avvisningen står. Titeln säger stödhjul, men källan anger hålavstånd 18 mm och "Robust och stark". Produkttypen är oklar. |
| 49110 | 10470943621386 | Avvisningen står. Källan beskriver ett pre-workout-pulver med koffein, men ingredienslistan anger bara kreatin, natriumcitrat och vitamin C. Källan motsäger sig själv. |
| 49111 | 10472285569290 | Avvisningen står. Beskrivningen är tom. |
| 49112 | 10472300085514 | Avvisningen står. Källan innehåller bara hälso- och säkerhetsfraser. Utöver titeln finns inga fakta. |

## Öppna frågor till David

1. 49105 och 49106 (sittdynor till Cargobike, samma SKU och EAN) ligger båda aktiva. Lagret måste flyttas och en av dem avpubliceras innan någon av dem kan få text.
