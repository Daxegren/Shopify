# Kategoritextstandard (kollektioner), utkast 2026-11-04

Utkast för Davids godkännande. Gäller kollektionens `descriptionHtml`, SEO-titel och metabeskrivning. Gäller inte produkter, taggar, navigation, tema eller villkor. Bygger på produkttextstandarden (`produkttexter-standard.md`) och regelboken (`shopify-sync/regler/regler-v1.md`). Butiksspecifikt (märken, spärrar) står i butikens profil. Filen fylls bara på efter godkännande.

## 1. Princip: fakta med kod, text med modell
1. **Faktaunderlaget tas fram med kod** ur kollektionens egna produkter (`shopify-sync/scripts/kategorier_underlag.py`): antal köpbara huvudprodukter, märken med antal, avrundat prisspann, vikter som står i titlarna, titlarna själva. Språkmodellen får bara skriva text av de uppgifterna.
2. **Huvudprodukter**: kollektionerna innehåller tillbehör (löpbandsolja, sparkcykelhjul, cykelsadlar). Underlaget räknar bara produkter vars typord står först (i de två första orden) i titeln. Prisspann, antal och märken räknas på dem.
3. **Köpbar** = status aktiv och lager över noll (eller utan lagerspårning). Utkast, arkiverade och slutsålda räknas inte.
4. **Leverantörsnamn är inte märken** (Velomarket, Gorilla Sports Norden). Märken som profilen eller vendor-fältet visar får nämnas bara om de finns bland kollektionens köpbara huvudprodukter.
5. **Kontroll**: `shopify-sync/scripts/kategori_kontroll.py` (tal, märken, längder, förbjudna ord, verb i första meningen, unikhet). Därefter **oberoende Opus-granskare** som kontrollerar varje påstående mot underlaget. Skrivning först efter 0 fel och godkänd granskning.

## 2. Innehåll i texten
- **Första meningen** (GEO): "BEST OF SPORTS säljer X, Y och Z från märke A, B och C. Här finns minst N modeller i prisklassen cirka P1–P2 kr." Har verb, är inte cirkulär, kan citeras av en AI-sökmotor.
- **Hjälp att välja** bara av härledd fakta: vilka märken som har flest modeller, vilka typer som finns, vikter som står i titlarna, funktioner som står i titlarna (hopfällbar, antal nivåer). Ingen allmän köpguide utan källa.
- **Exempelmodeller** med titlar ordagrant ur underlaget (minst tre).
- **Tal**: antal anges som "minst N" (golvat: tiotal från 30, femtal under, hundratal från 100). Pris avrundat till hundratal och med "cirka". Tal får inte skrivas utan stöd i underlaget.
- **Förbjudet**: kvalitets-, säkerhets-, effekt- och hälsolöften, superlativ ("bäst", "perfekt", "ledande"), nyckelordsfyllning, FAQ utan stöd i butikens egna villkor, leveranstider och frakt (kategoritext nämner inte villkor; de ligger i butikens standardtext), uppgifter om märken som inte finns i kollektionen, ursprungsuppgifter. Ordlistan ligger i `kategori_kontroll.py`.
- **Språk**: bara svenska i denna omgång. Danska och finska kräver granskning av modersmålstalare och tas upp separat. Befintliga da/fi-översättningar ändras inte.

## 3. Längd och placering
- **60–200 ord.** Förslag: lägre gräns 60 (inte 80) eftersom underlaget ofta bara bär 60–90 ord utan utfyllnad. Fyll aldrig ut för att nå ordantal. Smalt underlag ger kort text.
- **Placering**: dagens tema lägger all kategoritext ovanför produktlistan (mätt på `/collections/lopband`: texten börjar ca 44 000 tecken före första produktlänk). Därför ska texten tills vidare vara kort. En längre text under listan kräver ett nytt textfält i temat (beslut, se beslutsfilen).
- **HTML**: bara `<p>`-stycken, ingen rubrik i texten (sidans H1 är kollektionens titel), inga länkar tills intern länkning är beslutad.

## 4. SEO-titel och meta
- **SEO-titel högst 43 tecken**, utan butiksnamn (temat lägger till "– BEST OF SPORTS"). Typordet först, därefter de tre vanligaste märkena eller en tydlig avgränsare. Unik mot alla andra kollektioners SEO-titlar (kontrolleras av byggskriptet) och mot produkters SEO-titlar via nyckelordssökning före skrivning.
- **Meta 120–155 tecken**, första meningen har verb ("Köp ..."), nämner typ, märken och lägsta pris eller antal. Unik. Ingen utfyllnad, inga löften.

## 5. Vilka kollektioner som får text
Hoppa över: tomma kollektioner (0 köpbara), kollektioner med 1–4 köpbara (struktur först), dubbletter och kollektioner med samma innehåll som en annan (avgör struktur först), samt kategorier under `utanfor_tills_vidare` i profilen (kosttillskott, barn, akupressur, vibration m.fl.). Se `rapporter/bos-kategorier-2026-11-04/prioritering.csv`.

## 6. Skrivning (efter Davids ja)
Samma rutin som produkttexter: före-fil i `rapporter/shopify-original-<datum>/`, dry-run, kanarie på 3, återläsning och tecken-för-tecken-jämförelse, skript mot Admin API (aldrig handskrivna variabler). Ändrar bara `descriptionHtml` och `seo{title, description}` (båda fälten alltid tillsammans). Logg i `ANDRINGSLOGG.md`, status i `shopify-sync/status/bestofsports-kategorier.md`.

## 7. Godkännande (tillägg 2026-11-17, ändrar ingen text ovan)
David har godkänt standarden: bekräftat 2026-11-12 (standarden godkänd, textlängd 60–200 ord, kort text ovanför listan tills vidare) och den 2026-11-17 genom sessionen Översikt (alternativet "markering längst ned"; se `BESLUTSLOGG.md`). Rubriken och inledningen ovan säger fortfarande "utkast": *Inaktuellt sedan 2026-11-12, se ändringsloggen.* Godkännandet av standarden är inte ett godkännande av några texter; pilottexterna godkänns först efter granskning av nytt underlag (se avsnitt 8) och skrivs tidigast 2026-12-01 (Black Week).

## 8. Kontroll av underlaget (tillägg 2026-11-17: förslag till arbetsrutin, ännu inte beslutat av David; bygger på granskningarna 2026-11-05 och 2026-11-12)
1. Kör om underlaget direkt före varje text eller skrivning. Sortimentet och priserna ändras (inom två veckor ändrades antal, titlar och märkesstavning i flera kategorier), och exempelmodeller kan ha bytt namn eller försvunnit.
2. Granska underlaget separat: billigaste och dyraste titel, intervall i vikter ("1–10 kg"), produkter bland "övriga" (engelska titlar som Dumbbell, Treadmill, Electric bike), tillbehör som räknas som huvudprodukter (hantelställ, hantellås, löpbandsolja).
3. Skriv inte priser eller prisspann medan en prisjobbstagg (`price-change-job-active`) är aktiv på produkterna i kollektionen. Rabattpriset är inte ordinarie pris.
4. Skriv "bland annat" före varje uppräkning som inte är bevisat fullständig. Märken stavas som i produkttitlarna (inte versaler, R8). Skriv "produkter" om inte unika modeller är räknade.
