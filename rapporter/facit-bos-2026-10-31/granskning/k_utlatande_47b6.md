# Granskningsutlåtande k_47b6 (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08, LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md` och formatet i `k_utlatande_43.json`.

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_47b6.json` (tom lista, eftersom inget utkast fanns att döma).

## Resultat: 0 GODKÄND, 0 RÄTTA, 0 UNDERKÄND

`k_47b6_utkast.json` är tom (`[]`). Alla 14 produkter i `k_47b6_in.json` står i `k_47b6_avvisade.json`. Granskaren har läst var och en live och prövat om avvisningen är uppenbart fel. Ingen avvisning är uppenbart fel. **Ingen produkt lyfts ur.**

## Prövning av avvisningarna

| nr | id | titel (live) | bedömning |
|---|---|---|---|
| 48801 | 10472235663626 | Ljussats AXA Greenline Set 15 Lux | Avvisningen står. Källan säger "Compactline" och har två block med olika brinntid (6 mot 4 timmar) och laddningstid (mindre än 2 mot 1,5 timmar), alltså motsägande källa (R2/R3, 2026-11-08). |
| 48802 | 10472242184458 | Bromsskiva SHIMANO 180 mm Center Lock SM-RT10 | Avvisningen står. Källan anger både 180 och 160 mm samt både smal och bred blockform. Ingen EAN, och taggen Cykellås är fel. |
| 48803 | 10472334491914 | Fälgskydd M-Wave Ringlock 29-33 | Avvisningen står. Källan består bara av titeln. Pris 6 779 kr och taggen Romet tyder på en felkopplad produkt. |
| 48804 | 10472239956234 | Adapter Shimano SM-MA90-R160 Post/Standard, 160 mm | Avvisningen står. Egen källa är bara titeln. På nätet bekräftar återförsäljare EAN 4524667430513 (bike-discount.de), men de är oense om adaptern gäller fram- eller bakhjul (Excelsports: bak; SL-Sport: fram). Tillverkarsidan kunde inte läsas. Bromsdel med tvetydig källa. Obs: live-beskrivningen har redan standardblocket men ingen texter-klara-tagg, så den tidigare skrivningen bör kontrolleras. |
| 48805 | 10472294842634 | Stand ADO Air Carbon | Avvisningen står. Källan säger bara "Stativ för ADO Air Carbon-modellen". Lager 0 och taggen På beställning. Tunn källa (R3). |
| 48806 | 10472346190090 | Stöd med bakre fäste för 26-29" cykel | Avvisningen står. Priset är 0,00 kr (ofärdig produkt), EAN:et är internt och källan är bara en mening. Taggen Gymstick ser också fel ut. |
| 48807 | 10523491467530 | Cykelklocka GIANT DING-A-LING Flick, Svart | Avvisningen står. Beskrivningen är tom och ingen sida bekräftar exakt modellen. |
| 48808 | 10541369098506 | Flaskhållare GIANT Airway Sport Sidepull (L), Svart/Blå | Avvisningen står. Produkten har två varianter (490000099/490000095, samma pris, varianter namngivna bara med SKU), och vad som skiljer dem är okänt. Källan ger bara 500–750 ml. |
| 48809 | 10523491434762 | Träningshjul GIANT Steel Träningshjul, 16" | Avvisningen står. Beskrivningen är tom, och produkten är en barn-/bärande del utan uppgifter. |
| 48810 | 10480054567178 | Sangpomm CHRISTOPEIT Kettlebell 12kg | Avvisningen står. Live-texten består nästan bara av löften (bålstyrka, stabilitet, "säkert grepp"). Granskarens egen sökning på 21-3567 gav ingen Christopeit-träff. Vikten 12 kg är den enda fakta utöver titeln, så källan är för tunn (R3). Den estniska titeln ("Sangpomm") bör ses över separat. |
| 48811 | 10462785896714 | Kork Start NATURAL | Avvisningen står. Källan är maskinöversatt och produkttypen oklar (vallakork). |
| 48812 | 10472262959370 | Battery set for Fiido Titan | Avvisningen står. Elbatteri utan specifikation, lager 0 och pris 16 859 kr. Källan säger bara vad satsen innehåller. |
| 48813 | 10475517772042 | TOORX Bröstbälte 5.3 kHz | Avvisningen står. Elektronik där den enda uppgiften utöver titeln är en trasig rad om frekvensomfång. |
| 48814 | 10636716376330 | Adduktor Tränare | Avvisningen står. Källan beskriver anatomi och skaderisk men inte produkten. Den enda webbträffen har ett annat namn. Obs: säljaren är Gorilla Sports Norden och produkten saknar taggen Velomarket/Gymstick (annan källa, jfr F20). |

## Öppna frågor till David

1. 48804: live-beskrivningen har redan vårt standardblock men saknar texter-klara-taggen. Ska den skrivningen kontrolleras och märkas, eller göras om?
2. 48803, 48806 och 48812 har orimliga priser (6 779 kr för ett fälgskydd, 0 kr och 16 859 kr) eller felaktiga taggar. Det är en prisfråga, inte en textfråga.
