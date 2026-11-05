# Granskningsutlåtande k_13a + k_13b (omprövning), version 2

Datum: 2026-11-04. Granskare: Opus, endast läsning mot Shopify. Källa hämtad live via `shopify_api` (produkter och varianter) för alla tio utkast, dubbletten 10665228173578, Nebula 1 (10462124835082) och stickprov bland de avvisade (10101, 10113).
Maskinläsbart utlåtande: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_13v2.json`.

Den ofullständiga filen `k_utlatande_13.json` från den avbrutna granskningen lästes först efter den självständiga granskningen. Den har samma domar som den här. En skillnad: där stod att skiandbikes.de lästs, men sidan gav 403 nu, så Claris-uppgiften stöds här bara av sökträffar. Uppgiften står ändå i produktens egen källa.

## Resultat

| nr | id | Produkt | Dom |
|---|---|---|---|
| 10103 | 10487987142922 | Kona Rove | GODKÄND |
| 10105 | 10676720173322 | Leader Fox Cody | GODKÄND |
| 10106 | 10471092093194 | Romet Aspre 1 | GODKÄND |
| 10107 | 10468705665290 | 6KU Nebula 2 | GODKÄND |
| 10118 | 10472227209482 | M-Wave Cobra | GODKÄND |
| 10119 | 10471174668554 | Bookman reflexklistermärken | UNDERKÄND (standard §12) |
| 10120 | 10665228075274 | Bookman flammönster | UNDERKÄND (standard §12) |
| 10124 | 10480054534410 | Kettlebell Christopeit 2 kg | RÄTTA (R5, R11) |
| 10126 | 10581111243018 | Viktskiva Gymstick 1,25–25 kg | RÄTTA (R7) |
| 10134 | 10581105672458 | Core Roller Gymstick | GODKÄND |

Sammanlagt: 6 godkända, 2 att rätta och 2 underkända.

## Fokuspunkter

- **Texten stämmer för alla varianter:** ingen godkänd titel låser färg, storlek eller vikt. 10106 tar bort "silver-red" (alla varianter är silver), 10119 och 10120 tar bort färg och mönster, 10126 anger viktintervallet och 10134 båda längderna.
- **10105:** "Shimano Claris" och "7 växlar" står ordagrant i egen källa. Sökträffar hos återförsäljare för Cody 20 anger bakväxeln Claris RD-R2000 och ett 7-växlat HG41-frihjul, så källan motsäger sig inte. Claris finns bara mekanisk, så den obeslutade frågan om elektronisk växling berörs inte. Räckvidden "upp till 120 km" står en gång "enligt tillverkaren", som standard §16 kräver. Elcyklar är frisläppta enligt §16.
- **10106:** typordet "Gravelbike" kommer från produktens egen live-titel (R7). 10103 behåller sitt eget ord "Gravelcykel", vilket regeln tillåter.
- **10107:** M / black kostar 9 129 kr, de andra storlekarna 7 939 kr. Varianten har en egen SKU (CB62N1032, en annan än Nebula 1:s CB62N1007) och hör alltså till Nebula 2. Texten nämner inget pris, så det här är en prisfråga och inget textfel.
- **10120:** dubbletten 10665228173578 är identisk och spärrad i `sparr_titeldubbletter.csv`. 10120 är den äldsta annonsen och därmed rätt id att skriva. Produkten underkänns ändå, eftersom reflexdekaler enligt standard §12 bara får skrivas med Davids ja per produkt. Säger David ja behöver metan ett verb i huvudsatsen.
- **10126:** håldiametern är rätt utelämnad, eftersom webbkällorna anger olika mått. Typordet ska stå först. Rättningen har bara två kommatecken, eftersom skriptet räknar decimalkommat.
- **10134:** EVA bekräftades av granskaren mot skorpionas.lt (538GY6111045, 45 cm) och ox.ee (538GY6111090, 90 cm, EAN 6430016904384). Båda källorna gäller exakt modellen 61110.
- **10124:** källan är tunn men räcker, med två entydiga fakta utöver titeln. Rättningen gäller dubbel "enligt tillverkaren" i html och en meta utan verb.

## Rättningar (exakt före och efter)

**10124**
- meta. Före: `Christopeit Kettlebell på 2 kg med ergonomiskt utformat handtag, enligt tillverkaren. Kan användas hemma, på gymmet eller utomhus.` Efter: `Christopeits kettlebell väger 2 kg och har enligt tillverkaren ett ergonomiskt utformat handtag. Den kan användas hemma, på gymmet eller utomhus.`
- html. Före: `<li>Handtag: Ergonomiskt utformat, enligt tillverkaren</li>` Efter: `<li>Handtag: Ergonomiskt utformat</li>`

**10126**
- titel. Före: `Gummerad Viktskiva Gymstick, 1,25–25 kg` Efter: `Viktskiva Gymstick Gummerad, 1,25–25 kg`
- seo_title. Före: `Gummerad Viktskiva Gymstick 1,25–25 kg` Efter: `Viktskiva Gymstick Gummerad 1,25–25 kg`

## Avvisningarna (k_13a_avvisade, k_13b_avvisade)

- Alla 30 avvisningar är motiverade enligt R2, R3, R4 och R12a, så som reglerna lyder nu. Stickproven 10101 (EP8/EP800, 180/178 mm, S och M båda 38 cm) och 10113 stämmer mot live.
- **10113 Romet Vintage Eco D är troligen för strikt.** Default Title och L / valge har samma SKU (28200712-B). Beslut 3 i k_utlatande_02d väntar fortfarande på David, och samma mönster godkändes tidigare (6089, 6101, 6113). Om David säger ja kan produkten skrivas utan färg i titeln. Den trasiga växelraden och "Hjulvikt" ska då utelämnas.
- 10111, 10112, 10116 och 10117 har också samma SKU på Default Title, men där motsäger färg eller storlek titeln eller källan. De avvisningarna står sig därför även med ett ja till beslut 3.

## Frågor till David (påverkar inte domarna)

1. Reflexerna 10119 och 10120: får de skrivas för hand (standard §12)? Ska dubbletten 10665228173578 slås ihop eller arkiveras?
2. Prisfrågor: 10107 M / black (9 129 kr mot 7 939 kr). 10103 L / black finns två gånger med samma SKU till 21 369 kr och 18 619 kr.
3. 10118: färgen väljs i kassans kommentarsfält. Finns det fältet?
4. Beslut 3 (Default Title med samma SKU): ett ja gör att 10113 kan skrivas.
