# Granskningsutlåtande k_47b2, cykelstöd och pedalplattor (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsning med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.7–v1.11), BESLUTSLOGG till och med 2026-11-08 (aktiva produkter utan text får faktatext även i tidigare utanför-kategorier), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md`.

Alla tre utkast är ACTIVE med lager > 0, en variant var (Default Title), ingen tagg På beställning, så ingen leveranstidsmening ska finnas (finns inte). `skrivfil_kontroll.py` gav 0 fel och 0 varningar både på utkastet och på den rättade versionen. Standardblocket är exakt. Titel ≤70 tecken och ≤2 kommatecken, SEO ≤43, meta 119–129 tecken med verb, "Passar för" finns. Titel, SEO och meta är unika mot alla JSON-filer under `rapporter/` och mot butikens titlar (sökning på KSA, Kickstand, Keo, Cykelstöd, Pedalplattor, SKU och EAN). Numren 48401–48403 förekommer bara i denna batch. Varje rättning är ETT sammanhängande före/efter-par per fält och varje före-text finns exakt en gång i utkastet (kontrollerat i python).

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_47b2.json`.

## Resultat: 1 GODKÄND, 2 RÄTTA, 0 UNDERKÄND

| nr | id | fil | dom | rättade fält |
|---|---|---|---|---|
| 48401 | 10515738067210 | k_47b2_utkast.json | GODKÄND | – |
| 48402 | 10472244510986 | k_47b2_utkast.json | RÄTTA | meta, html |
| 48403 | 10554363117834 | k_47b2_utkast.json | RÄTTA | titel, seo_title, html |

## Per produkt

**48401 Cykelstöd Giant Direct Mount KSA 40 mm – GODKÄND.** SKU 500000042, EAN 4713250037448, lager 20. Giants sida bekräftar aluminium, justerbar längd för 24–29 tum, KSA40-fäste med två bultar och 40 mm avstånd på vänster kedjestag, M6-bultar ingår och längden ställs in utan verktyg. Artikelnumret bekräftas hos återförsäljare. Lastgräns saknas hos Giant och i egen källa: "Ej känd" enligt v1.10. "Stabilt", "gediget", "robust" är utelämnade. Inte dubblett av syskonen 500000012, 500000013 eller 500000038 (andra artiklar).

**48402 Cykelstöd Giant Mobility Kickstand – RÄTTA.** SKU 500000007, EAN 4718905893608, lager 36. Giants italienska sida (RIF 500000007): legering, 335 mm, passar FastRoad och ToughRoad. Rapid står bara i den egna live-raden; Velomarkets produktadress säger i stället AnyRoad och Giant nämner ingen av dem. Det är en motsägelse, så bara de två modeller som båda källorna anger står kvar (R2). "Enligt Velomarket" är en arbetsterm i kundtext (R11) och tas bort. "Fast längd" saknar stöd (R1). "Har en struktur i legering" skrivs som "gjort av legering".

- meta före: "är 335 mm långt och har en struktur i legering. Det är avsett för Giant FastRoad, ToughRoad och Rapid." efter: "är 335 mm långt och gjort av legering. Det passar Giant FastRoad och ToughRoad."
- html: ett sammanhängande stycke från inledningen till raden "Passar:" byts (inledning, båda "Passar för"-raderna och specifikationsraden "Passar"); exakt före/efter finns i JSON-filen.

**48403 Pedalplattor Look Keo Cleat – RÄTTA.** SKU och EAN 3611720061546, lager 1; den egna källan har bara "9 grader". Sweetpetes listar UPC 3611720061546 som Red/9°, MPN 8149, 68 g för par med fästelement; Excelsports: säljs i par med monteringsdetaljer, röd = 9° float. Uppgifterna gäller entydigt exakt EAN. Inga frigörings-, säkerhets- eller kompatibilitetslöften ("compatible with all pedals" rätt utelämnat). Inte dubblett av Keo Grip 9° (EAN 3611720061577, annan artikel). Inledningen var cirkulär (R11). Beskrivande ord får stor bokstav i titel och SEO (R9).

- titel: "Pedalplattor Look Keo Cleat, röd, 9 grader" → "Pedalplattor Look Keo Cleat, Röd, 9 grader"
- seo_title: "Pedalplattor Look Keo Cleat, röd" → "Pedalplattor Look Keo Cleat, Röd"
- html: "<p>Look Keo Cleat är pedalplattor i rött med 9 graders float" → "<p>Pedalplattorna Look Keo Cleat är röda och har 9 graders float"

## Löften

Alla texter genomsöktes efter hälso-, säkerhets-, skydds-, stabilitets-, hållbarhets-, prestanda- och kvalitetsord (även subtila som stabil, gedigen, robust, ultralätt, säker, pålitlig, frigöring, lätt att montera). Inget sådant finns. Lastgräns anges bara som "Ej känd" (v1.10).

## Avvisade (k_47b2_avvisade.json)

Alla elva avvisningar står sig (tunn källa, oklar produkttyp, titel som motsäger källan, exakt dubblett med lager, motsägande batteriuppgift). Ingen lyfts.

## Frågor till David

1. Live-titlarna på 48401 ("Stöd för bakre löpare") och 48402 innehåller felöversättning eller versaler. Utkasten rättar titeln; handle ändras inte.
2. Giant Mobility Kickstand: ska Rapid stå med? Velomarkets text säger Rapid, deras adress säger AnyRoad och Giant nämner ingen av dem. Utlåtandet tar med bara FastRoad och ToughRoad.
