# Granskningsutlåtande k_24abc (BEST OF SPORTS): bärande delar med lastgräns

Granskare: Opus, endast läsning. Datum: 2026-11-05. Butiken bekräftades via API: BEST OF SPORTS, 6f2e53-67.myshopify.com. Alla 10 produkter hämtades live på nytt med shopify_api.py. Alla är ACTIVE, ingen har taggen texter-klara eller På beställning, och ingen står på spärrlistan. Ingenting är skrivet i Shopify.

Underlag: regler-v1.md (v1.5–v1.8), BESLUTSLOGG.md (raderna 2026-11-05, bl.a. "Bärande och hängande delar: nuvarande regel gäller", Davids beslut 3), butiksprofil-bestofsports.json, agentprompter.md och utlåtandet k_23abc.

**Utfall:** GODKÄND 6, RÄTTA 4, UNDERKÄND 0 (av 10).

Rättningarna är provkörda på kopior. `skrivfil_kontroll.py` gav 0 fel och 0 varningar för alla tre filerna. Varje "före" förekommer exakt en gång i sitt fält. (⏎ = radbrytning i fältet.)

## Lastgränsen i produktens egen källa

Alla tio produkterna har lastgränsen ordagrant på svenska, med etikett och enhet, i sin egen live-beskrivning och inte bara hos återförsäljare. I texterna står den en gång "enligt tillverkaren" per fält, efter rättning. Ingen text påstår att lasten gäller något som källan inte anger.

| nr | rad i live-källan |
|---|---|
| 24061 | Lastkapacitet 25 kg |
| 24062 | Kapacitet: upp till 10 kg. (samma värde i löptexten "kan bära upp till 10 kg") |
| 24063 | Maximal lastkapacitet 5 kg. |
| 24066 | Lastkapacitet: 120 kg |
| 24070 | Lastkapacitet: 5 kg. |
| 24071 | Bärkapacitet: 2,5 kg. |
| 24072 | Bärkapacitet: 5 kg. |
| 24073 | Lastkapacitet 35 kg. (en ren rad i en i övrigt trasig källa, R4 per rad) |
| 24094 | Lastkapacitet 25 kg |
| 24096 | Lastkapacitet: 100 kg (låda) + 100 kg (förare). |

## Tabell

| nr | id | fil | dom | rättning och skäl |
|---|---|---|---|---|
| 24061 | 10411858428170 | k_24a | RÄTTA | **titel:** `, 26–28 tum, svart` → `, 26–28 tum, Svart`<br>**html:** `<li>Dig som behöver ett stödben som kan justeras för olika prismor</li>⏎` → (stryks)<br>**html:** `<li>Justering: Längd och prismor</li>` → `<li>Längd: Justerbar</li>`<br>Live-titeln har tre kommatecken. Utkastet har två och har strukit "för bakre löpare" (maskinöversatt). Färgen skrivs med stor bokstav, som i syskonet 24094 och i tidigare skrivna Hebie-titlar; skriptet missade det. "Justerbar för att passa olika prismor" är oklar svenska (R2) och är redan utelämnad i 24094, som har samma källa. "Bred ände för stabilitet" är rätt utelämnad (R5). |
| 24062 | 10461971284234 | k_24a | RÄTTA | **html:** `<li>Kan bära upp till 10 kg (enligt tillverkaren)</li>` → `<li>Kapacitet: Upp till 10 kg enligt tillverkaren</li>`<br>Specifikationsraden saknade etikett. Den får källans egen etikett. Lastvärdet är detsamma i löptext och tabell (v1.5 uppfylld). "robusta", "cykelställ" och märkesbakgrunden är rätt utelämnade. Produkten är ingen dubblett av 10472250114314 (Portland i matt svart, annan färg). |
| 24063 | 10462762664202 | k_24a | GODKÄND | –<br>Titeln ändrar bara märkets skrivsätt (BASIL → Basil). Plast, 22–31,8 mm, justerbar vinkel och de två adapterplattorna står ordagrant i källan. Passformen för "de flesta stadscyklar" och elcyklar med Bosch-display, samt "hållbart" och "stadigt", är rätt utelämnade. |
| 24066 | 10462840094986 | k_24a | GODKÄND | –<br>Bytet "Squat Stand" → Skivstångsställning är belagt av profilens `godkanda_typord`. Texten innehåller inga säkerhetspåståenden: säkerhetskrokar, "högsta säkerhetsstandarder", "hållare för 30 mm kedjor", stegpinnar och träningseffekter är strukna. Lastgränsen kopplas inte till stång eller krokar. |
| 24070 | 10470989824266 | k_24a | GODKÄND | –<br>Titelbytet till "Cykelkorg Basil Class för pakethållare" är belagt av källan: "Cykelkorgen Basil Class är gjord av stål ... fästa på pakethållaren". Basil Class är alltså korgens modellnamn. Påståenden om synlighet i mörker, "säkert" och "bekväm" är rätt utelämnade. |
| 24071 | 10472218853642 | k_24a | GODKÄND | –<br>Bytet "Handlebar bag" → Styrväska är belagt av källan ("-styre väska") och av butikens live-ord (Styrväska Basil Mali, Giant H2Pro, PRO Gravel). "Vattentätt och ljusreflekterande" står ordagrant med "enligt tillverkaren". Uttrycket står då två gånger i html, vilket är högst tillåtet. "Magnetiskt toppskydd" är rätt utelämnat. |
| 24072 | 10472222425354 | k_24a | GODKÄND | –<br>Bytet Styckväska → Handväska är belagt av egen källa ("en riktig damhandväska", två korta handtag, axelrem) och av butikens live-ord (Handväska BASIL Bloom Field). Styrväska har inget stöd i den här källan. "Slitstarkt vattentätt", synlighet och valet av fäste via meddelandefältet är rätt utelämnade. Enda varianten heter Red och färgen nämns inte, vilket godtas. |
| 24073 | 10472227340554 | k_24b | RÄTTA | **html:** ` Lastkapaciteten anges enligt tillverkaren.` → (stryks)<br>**html:** `<li>Dig som vill ha ett stöd från det italienska märket Ursus</li>⏎` → (stryks)<br>**html:** `<li>Lastkapacitet: 35 kg</li>` → `<li>Lastkapacitet enligt tillverkaren: 35 kg</li>`<br>**html:** `<li>Tillverkare: Italien</li>⏎` → (stryks)<br>Meningen om lastkapaciteten säger ingenting och stryks. Lastgränsen får i stället "enligt tillverkaren" i specifikationen. "Italien" och "italienska" är ursprungsord (R5, prejudikat 23001) och stryks. Det avkortade "16-" är rätt struket ur titeln, och storleken är utelämnad. Två entydiga fakta finns utöver titeln: aluminium och 35 kg (R3, tunn källa). Webbkällan har samma EAN och "Max 35 Kg" men behövs inte. Ingen dubblett: R78 24" (10494685479178) är arkiverad. |
| 24094 | 10472245494026 | k_24c | GODKÄND | –<br>Live-titeln har tre kommatecken, utkastet två. "för bakre löpare" är struket. Typordet Stöd är live-titelns och källans eget ord. Syskonet behåller sitt Stödben (R7). "Universellt stöd med prismadapter (lämpligt för olika ramar)" står ordagrant i källan. Stabilitetsordet och "olika prismor" är rätt utelämnade. |
| 24096 | 10472246608138 | k_24c | RÄTTA | **html:** `har lådan placerad framtill, Bafang-motor` → `har en låda, Bafang-motor`<br>**html:** `<li>Räckvidd: 20–40 km</li>` → `<li>Räckvidd: 20–40 km enligt tillverkaren</li>`<br>Att lådan sitter framtill står inte i källan, som bara säger "lådcykel" och anger lådans mått (R1). Räckvidden får "enligt tillverkaren" som i alla tidigare skrivna elcykeltexter. Uttrycket står då två gånger i html, vilket är högst tillåtet. Lastgränsen anger själv vad den gäller (låda och förare). Ingen dubblett: Classic Box (21067) har lock och andra lådmått. |

## Särskilt granskat

- **Titelbyten:** Alla begärda byten är belagda:
  - 24061 och 24094 har gått från tre till två kommatecken.
  - 24066 Skivstångsställning stöds av profilen.
  - 24071 Styrväska stöds av källan och butikens live-ord.
  - 24072 Handväska stöds av källans "damhandväska" och av butikens live-ord.
  - 24063 och 24070 ändrar bara märkets skrivsätt respektive ordföljden, och källan stöder båda.
- **Säkerhet:** 24066 innehåller ingenting om hållare, säkerhetskrokar eller säkerhetsstandard. Ingen av texterna innehåller stabilitets-, skydds- eller synlighetspåståenden.
- **Ursprung (R5):** 24073 hade "Italien" och "italienska" och de stryks. Märkesbakgrunden för Basil ("nederländska", "sedan 1976", "hög kvalitet") är rätt utelämnad överallt.
- **Möjliga beslut för David (inget krävs nu):** De två Hebie Fox I-stöden behåller var sitt live-ord, Stödben (24061) och Stöd (24094). Samma typord på båda kräver ett beslut. Magnolia (24072) skrivs som Handväska. Om David hellre vill ha Styrväska, som för den rättade Styckväskan 23016, krävs också ett beslut.
- **Leveranstid (R13):** Ingen av produkterna har taggen På beställning, och ingen text har leveranstidsmeningen. Det stämmer.
- **Spärrlista och dubbletter:** Ingen av de tio står på spärrlistan. Inga dubbletter hittades vid sökning i butiken (Portland, Fox I, King R78) eller bland skrivna filer (Classic Box).
