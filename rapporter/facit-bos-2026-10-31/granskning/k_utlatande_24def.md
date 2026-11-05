# Granskningsutlåtande k_24def (BEST OF SPORTS): bärande delar med lastgräns

Granskare: Opus, endast läsning. Datum: 2026-11-05. Butiken bekräftades via API: BEST OF SPORTS, 6f2e53-67.myshopify.com. Alla 10 produkter hämtades live på nytt med shopify_api.py. Alla är ACTIVE med en variant, och ingen har taggen texter-klara. Ingen står på spärrlistan eller på listan över barn- och ungdomsprodukter. Ingenting är skrivet i Shopify.

Underlag: regler-v1.md (v1.5–v1.8), BESLUTSLOGG.md (raderna 2026-11-05, bl.a. "Bärande och hängande delar: nuvarande regel gäller", Davids beslut 3), butiksprofil-bestofsports.json, agentprompter.md och utlåtandet k_24abc.

**Utfall:** GODKÄND 2, RÄTTA 8, UNDERKÄND 0 (av 10). Sex av rättningarna gäller bara format (färgens versal, tankstreck, parentes). Tre gäller innehåll: 24107 saknade leveranstidsmeningen, 24112 och 24114 hade en första mening utan verb, och i 24106 var lastgränsen ofullständig i metan.

Rättningarna är provkörda på kopior. Varje "före" förekommer exakt en gång i sitt fält. `skrivfil_kontroll.py` och `kontrollera_produkttext.py --seo-title-max 43 --meta-min 70` gav 0 fel och 0 varningar för alla tre filerna. Skriptet varnade för en cirkulär inledning ("Namn är ett typord") i en första version av rättningarna för 24112 och 24114, så de formulerades om.

## Lastgränsen i produktens egen källa

Alla tio produkterna har lastgränsen ordagrant på svenska, med etikett och enhet, i sin egen live-beskrivning. Den står högst en gång "enligt tillverkaren" per fält. Ingen text påstår att lasten gäller något som källan inte anger, till exempel förare, passagerare eller lasten per cykel.

| nr | rad i live-källan |
|---|---|
| 24097 | Maximal lastkapacitet 40 kg |
| 24098 | Lastkapacitet: 150 kg |
| 24100 | "Denna framkorg har en maximal lastkapacitet på 10 kg" (samma värde: "en maximal vikt på 10 kilo") |
| 24104 | Maxvikt: 10 kg |
| 24106 | Maxvikt: 10 kg totalt, max 5 kg per väska. |
| 24107 | Lastkapacitet: 120 kg |
| 24110 | Lastkapacitet: 10 kg. |
| 24112 | Maximal lastkapacitet: 60 kg |
| 24114 | Maximal lastkapacitet: 10 kg |
| 24126 | Maxvikt: 5 kg |

## Tabell

| nr | id | fil | dom | rättning och skäl |
|---|---|---|---|---|
| 24097 | 10472246870282 | k_24d | RÄTTA | **titel:** `eLex 26"-28", svart` → `eLex, 26–28 tum, Svart`<br>Titeln skrivs som syskonen Hebie Fox I (24061, 24094). Lastgränsen står en gång enligt tillverkaren per fält. Stabilitetspåståendet och den otydliga raden om 0699-40 är rätt utelämnade. |
| 24098 | 10472248148234 | k_24d | GODKÄND | –<br>Texten säger inte vad 150 kg omfattar. Personer och "familjer med 1–2 barn" är rätt utelämnade: det finns ingen uppgift om barnsits eller säkerhet. Produkten är en el-lastcykel och ingen barnprodukt (R6 gäller inte). Räckvidd och last står med enligt tillverkaren, två gånger i html, vilket är högst tillåtet. Taggen På beställning finns och meningen står med. Hjulvikten och den trasiga däckraden är rätt utelämnade (R2). |
| 24100 | 10472250114314 | k_24d | RÄTTA | **titel:** `, 25 l, matt svart` → `, 25 l, Matt Svart`<br>**seo_title:** `25 l, svart` → `25 l, Svart`<br>Framkorg är källans eget ord. Syskonet 24062 (SKU 50413) är en annan artikel, och titeln är fortfarande unik. |
| 24104 | 10472251228426 | k_24d | RÄTTA | **titel:** `MIK, svart` → `MIK, Svart`<br>**seo_title:** `MIK, svart` → `MIK, Svart`<br>Bytet Bagagekorg → Cykelkorg är belagt av källan ("praktisk cykelkorg"). Övriga fakta står ordagrant. |
| 24106 | 10472251851018 | k_24d | RÄTTA | **titel:** `28-32 l, brun` → `28–32 l, Brun`<br>**seo_title:** `28-32 l, brun` → `28–32 l, Brun`<br>**meta:** `Maxvikt 10 kg totalt enligt tillverkaren.` → `Maxvikt 10 kg totalt, 5 kg per väska, enligt tillverkaren.`<br>Metan utelämnade gränsen per väska och kunde läsas som 10 kg i en väska. Med rättningen blir metan 150 tecken. Html återger källraden ordagrant. "Vattentät" står ordagrant i källan. Att ordet är utelämnat är försiktigt och godtas. Bytet Pakväska → Cykelväska är belagt ("Cykelväskan är kompakt"). |
| 24107 | 10472268955914 | k_24d | RÄTTA | **html:** `Se sidan Frakt för övriga länder.</p>` → `Se sidan Frakt för övriga länder. Beställningsvaror kan ta upp till en vecka längre.</p>`<br>Produkten har taggen På beställning, men meningen saknades (R13, v1.8). Källan säger "Vuxentrecylkel", så det är en trehjuling för vuxna och ingen barnprodukt. Trehjuling är källans eget ord och ersätter Tricycle. Det skiljer sig från Eltrehjuling AM_LIGHTWEIGHT, som är en annan produkt. Amladcykler stavas som leverantörsfältet. Kvalitets-, stabilitets- och ursprungsord är rätt utelämnade. |
| 24110 | 10472294547722 | k_24e | GODKÄND | –<br>Lastgränsen står en gång enligt tillverkaren i löptexten. Specifikationsraden är samma påstående. "Tillverkad i Tyskland" är rätt utelämnat (R5). Typordet Sadelstolpsrack kommer från live-titeln. |
| 24112 | 10472296153354 | k_24e | RÄTTA | **html:** `<p>Dragkroksmonterat cykelställ för upp till fyra cyklar. Peruzzo Siena har en maximal` → `<p>Peruzzo Siena monteras på bilens dragkrok och har fästen för upp till fyra cyklar. Stället har en maximal`<br>Den första meningen saknade verb (R11). Källan har "Utrustad med fästen för en andra, tredje och fjärde cykel". "Typgodkänd" är utelämnat, vilket är försiktigt (R5). "Maximal vikt per hjul: 15 kg" är rätt utelämnad, eftersom källan säger "hjul" om cyklar (R2). Taggen På beställning finns och meningen står med. |
| 24114 | 10472522023178 | k_24e | RÄTTA | **html:** `<p>Avtagbar cykelkorg på 23 liter med bas i bambu. Basil Nordland MIK har en` → `<p>Basil Nordland MIK rymmer 23 liter och är tillverkad i stål med en bas i bambu. Den avtagbara korgen har en`<br>Den första meningen saknade verb (R11). Färgen "svart/trä" är rätt struken. "Slitstarkt", "extra säkerhet" och "snabbt och säkert" är rätt utelämnade. |
| 24126 | 10554354139402 | k_24f | RÄTTA | **html:** `<li>Maxvikt: 5 kg (enligt tillverkaren)</li>` → `<li>Maxvikt: 5 kg enligt tillverkaren</li>`<br>Parentesen tas bort, så att formen blir densamma som i övriga texter (prejudikat 24062). Metan har ingen lastgräns, vilket är tillåtet. IPX 3, "skyddade" och "nästan alla (el)cyklar" är rätt utelämnade. |

## Särskilt granskat

- **24098 Jobobike Transer:** Personer och barn är utelämnade, och texten säger inte vad 150 kg omfattar. Det är riktigt. Om David vill hålla cyklar som marknadsförs för barntransport utanför, som Svensson Family (21064), krävs ett beslut. Den här texten nämner ingen barntransport.
- **24107 trehjuling:** Det är en trehjuling för vuxna och ingen barnprodukt. Amladcykler är leverantörens namn.
- **24106:** Gränsen per väska står nu även i metan. "Vattentät" är utelämnat, vilket godtas.
- **24112:** Det är riktigt att "typgodkänd" är utelämnat. Om David vill ha med uppgiften kan den skrivas som "typgodkänd bakljuspanel enligt tillverkaren", eftersom den står ordagrant. Inget beslut krävs nu. Leveranstidsmeningen är på plats.
- **Typordsbyten:** Alla är belagda av källan eller live-titeln:
  - Cykelkorg (24104, 24114)
  - Cykelväska (24106, 24126)
  - Trehjuling (24107)
  - Framkorg (24100)
  - Sadelstolpsrack och Cykelställ (live-titeln)
- **Märken:** HEBIE, JOBOBIKE, BASIL och RACKTIME skrivs nu Hebie, Jobobike, Basil och Racktime. AMLADCYKLER skrivs Amladcykler, som i leverantörsfältet.
- **Leveranstid (R13):** Tre produkter har taggen På beställning: 24098, 24107 och 24112. 24107 saknade meningen och rättas. Ingen av de övriga texterna har meningen.
- **Dubbletter:** Inga dubbletter hittades vid sökning i butiken. Sökorden var eLex, Transer, Portland, Base, City, Amladcykler, ClipIT, Siena, Nordland och Miles.
