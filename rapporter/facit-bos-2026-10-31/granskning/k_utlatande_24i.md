# Granskningsutlåtande k_24i (BEST OF SPORTS): kablar och lastcyklar med lastgräns

Granskare: Opus, endast läsning. Datum: 2026-11-05. Butiken bekräftades via API: BEST OF SPORTS, 6f2e53-67.myshopify.com. Alla fyra produkterna och dubbletten 24165 hämtades live på nytt med shopify_api.py. Alla fem är ACTIVE, ingen har taggen texter-klara och ingen står på spärrlistan. Ingenting är skrivet i Shopify.

Underlag: regler-v1.md (v1.5–v1.8), BESLUTSLOGG.md (raderna 2026-11-05, bl.a. "Bärande och hängande delar: nuvarande regel gäller", Davids beslut 3, samt dubblettbeslutet "den äldsta annonsen behålls så länge den har all info och alla bilder"), butiksprofil-bestofsports.json, agentprompter.md och utlåtandet k_24abc.

**Utfall:** GODKÄND 4, RÄTTA 0, UNDERKÄND 0 (av 4).

`skrivfil_kontroll.py` på en kopia av utkastfilen gav 0 fel och 0 varningar. "enligt tillverkaren" står exakt en gång per text (i html, inte i titel, SEO-titel eller meta).

## Lastgränsen i produktens egen källa

| nr | rad i live-källan | i utkastet |
|---|---|---|
| 24161 | Maximal belastning: 280kg (under "Lång Kabel:") | Maximal belastning: 280 kg enligt tillverkaren |
| 24162 | Maximal belastning: 280kg (två gånger, under "Kort Kabel:" och "Lång Kabel:") | Maximal belastning: 280 kg per kabel enligt tillverkaren |
| 24163 | Lastkapacitet: 110 kg | Lastkapacitet: 110 kg enligt tillverkaren |
| 24164 | Lastkapacitet: 180 kg | Lastkapacitet: 180 kg enligt tillverkaren |

Alla fyra raderna är svenska, har etikett och enhet och står i produktens egen live-beskrivning. Det finns inget annat lastvärde i löptexten (v1.5 uppfylld). "per kabel" i 24162 återger källan troget, eftersom samma värde står under varje kabel.

## Tabell

| nr | id | dom | skäl |
|---|---|---|---|
| 24161 | 10636628066570 | GODKÄND | Stålkabel med plastbeläggning, 241,5 cm och "säljs en och en" står ordagrant i källan. Källan säger bara "Reservdel för Latsdrag Kabelstation" och länkar till gorillasports.se. Butiken har ingen produkt med det namnet; de närmaste är två utkast (DRAFT), "Universal bänkpress med Kabelhiss för latsdrag". Utkastet nämner ingen maskinmodell och påstår ingen passform eller hållfasthet. Länken till leverantörens sajt och leverantörsnamnet är rätt utelämnade. En variant (SKU 101137-00001-0001). Ingen tagg "På beställning" och därför ingen leveranstidsmening. Ingen dubblett (sökning på SKU). |
| 24162 | 10636670894346 | GODKÄND | Kort kabel 182 cm, lång kabel 241,5 cm, stålkabel med plastbeläggning och "säljs endast i paket" står i källan. Ingen passform mot en maskin påstås. "Dig som vill byta båda kablarna samtidigt" följer av paketförsäljningen och lovar inget om passformen. En variant (SKU 101138-00001-0001). Ingen leveranstidstagg. Ingen dubblett. |
| 24163 | 10665232367882 | GODKÄND | Alla tolv specifikationsrader stämmer med källan (motor 250 W/110 Nm Ananda, 20 Ah, upp till 60 km, aluminium, Shimano Nexus, 8 växlar, hydrauliska bromsar, 24 x 3,0 tum, 37 kg, 110 kg). Taggen "På beställning" finns och leveranstidsmeningen står i standardblocket (R13, v1.8). Källans "familjeäventyr" och marknadsorden ("hållbar", "kraftfulla prestanda", "högkvalitativa komponenter") är utelämnade. Texten nämner inga barn och inga säkerhetsord. Den säger inget om vem eller vad lasten avser, alltså inga uppgifter om förare eller passagerare. Butiken säljer "Skyddsram för barnstol" till Longtail Varia, men den uppgiften finns inte i cykelns källa och ska inte in. Märket skrivs "Cargobike of Sweden" som i tidigare skrivna Cargobike-titlar (Classic, Flex m.fl.). Taggarna Velomarket och Cargobike of Sweden rörs inte. |
| 24164 | 10676713586954 | GODKÄND | Alla specifikationsrader stämmer med källan (250 W/110 Nm Ananda, 19,6 Ah, upp till 50 km, aluminium, Shimano Altus, 8 växlar, Tektro hydrauliska, 26/20 x 1,95 tum, 48 kg, 260 x 65 x 120 cm, 180 kg). "tvåhjulig" och "omdesignad lastlåda" står i källan. "kundfavorit" och "tillbaka i ny tappning" är rätt utelämnade. Inga barn-, säkerhets- eller lastinnehållspåståenden. Taggen "På beställning" finns och leveranstidsmeningen står med. **Rätt annons att skriva:** 24164 skapades 2026-10-22 12:49:37 och dubbletten 24165 (10676713652490) två sekunder senare. Båda har SKU 1240, 9 bilder och tecken för tecken identisk beskrivning. Den äldsta annonsen har alltså all info och alla bilder, och enligt Davids beslut 2026-11-05 behålls den. 24165 hålls (avvisad i k_24i_avvisade.json). Prisskillnaden (75 999 kr mot 76 149 kr) rörs inte av textutrullningen. Bara de två Long Lite-annonserna har SKU 1240. |

## Att notera (inget fel i utkastet)

- 24164 och 24165 får olika titlar när 24164 har skrivits. Det är avsett tills dubbletterna slås ihop enligt den plan David ska godkänna.
- I kabeltexterna står "latsdrag kabelstation" med gemener, som en allmän beskrivning. Det är källans nivå utan leverantörslänken. Om David vill att kablarna knyts till en viss maskin i butiken krävs ett eget beslut, eftersom källan inte namnger någon modell som BOS säljer.
