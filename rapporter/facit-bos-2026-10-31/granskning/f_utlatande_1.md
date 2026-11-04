# Granskning f_1 – löpband BH Fitness, faktatextläge (2026-11-04)

Oberoende granskning. Jag har bara läst i Shopify och inte ändrat någon utkastsfil. Butiken kontrollerades först med get-shop-info: **BEST OF SPORTS** (bestofsports.se, SEK).

**Underlag:** `vag2_skriv/f_1_utkast.json` (24 löpband, nr 10001–10025; 10017 avvisad av utkastaren som dubblett av 10018). Regler: `produkttexter-standard.md` avsnitt 1–17 (faktatextläge §16, kort meta §17), `fakta_utkastprompt.md`, `LARDOMAR.md`. Uppdragets avvikelse: löpband underkänns inte för att de har motor eller elektronik när texten bara återger live-källan.

**Metod:**
- **Källan live:** title, status, productType, vendor, tags, descriptionHtml, seo och variants hämtades med graphql_query (`nodes`) i tre batchar om 8. Alla 24 är ACTIVE, har en variant (Default Title), och SEO-fälten är tomma i dag.
- **Maskinellt:** titel 24–54 tecken med högst 1 kommatecken, SEO-titel 24–40 tecken (≤43), meta 132–154 tecken (inom 70–155 och även inom 130–155). Inga dubbletter av titel, SEO-titel eller meta inom filen eller mot övriga `*_utkast.json` och `*skriv*.json`. Standardblocket är identiskt med `b_skriv_24.json`. Produkter med taggen "På beställning" (18 st) har dessutom meningen "Beställningsvaror kan ta upp till en vecka längre." Den varianten finns i redan godkända skrivfiler och följer §10. De 6 utan taggen (10005, 10013, 10014, 10018, 10019, 10020) har grundblocket.
- **För hand:** varje tal och varje uppgift lästes mot live-källan.

## Resultat i korthet

| Dom | Antal | Nr |
|---|---|---|
| GODKÄND | 17 | 10003, 10004, 10005, 10006, 10007, 10008, 10009, 10011, 10013, 10014, 10015, 10016, 10018, 10019, 10021, 10023, 10024 |
| RÄTTA | 7 | 10001, 10002, 10010, 10012, 10020, 10022, 10025 |
| UNDERKÄND | 0 | – |

## Särskilda kontroller
- **10003/10004 (G788):** 10003 (10650209976586, SKU G788-19) har "19-tum, pekskärm" i källan och 19-tums i utkastet. 10004 (10656692404490, SKU G78822) har "22-tum, pekskärm" i källan och 22-tums i utkastet. Båda stämmer, och titlarna skiljs åt av skärmstorleken. 10004 saknar produktmått i källan, och utkastet tar inte med några.
- **"Maximum operating weight" → "maximal användarvikt" (10021, 10024, 10025):** källan anger produktvikt separat (125 kg och 130 kg), så 180 kg kan inte vara maskinens vikt. Systermodellen RCM Pro (10010, svensk källa) anger "Maximal användarvikt: 180 kg". Jag godtar översättningen, men den är en tolkning och inte ett ordagrant citat. Därför ligger den som fråga till David (se nedan).
- **Lutning och hastighet med enhet:** % eller procent står bara där källan anger enheten i listan eller i löptexten (10001, 10002, 10003, 10004, 10007, 10009, 10010, 10016, 10018, 10022, 10023, 10024, 10025). Där källan bara har ett tal utan enhet har talet utelämnats (10005, 10006, 10011, 10012, 10013, 10014, 10015, 10019 [10 lägen], 10020, 10021). 10008 har ett orimligt intervall i källan ("-3 till -16 procent") och det är rätt utelämnat. Hastighet står alltid i km/h som i källan. Den trasiga hastigheten för 10021 ("0.3 - 18 km/h. 3.5 HP: 3.5 mph") är rätt utelämnad.
- **Läckage från syskonprodukter:** inget hittat. 10002 tar inte med 19-tumsskärmen eller ANT+ (konsolalternativ). 10006 och 10011 saknar Bluetooth i källan och har det inte i texten. 10012 och 10022 (RS1000 TFT och LED) har var sitt antal program (25 och 8) och var sin motoruppgift (3,5 hk och 3,5 AC) enligt sin egen källa.
- **Påståenden:** inga uppgifter om säkerhet, stabilitet, leder, rehabilitering, hälsa, kroppsfett eller hållbarhet (timmar per vecka). Pioneer Senior har inga ålders- eller ledpåståenden. "MED" förklaras inte. Inget ursprungsland (Spanien) står med. Produkttyp och märke är oförändrade, och "Treadmill" i originaltiteln har blivit "Löpband".

## Rättningar (exakt före → efter; ersättning av delsträng i angivet fält)

| Nr | Id | Fält | Före | Efter | Skäl |
|---|---|---|---|---|---|
| 10001 | 10656691945738 | html | `<li>Reglage: Easy Toolbar i det främre handstödet för hastighet, lutning och puls</li>` | `<li>Reglage: Easy Toolbar i det främre handstödet för hastighet och lutning samt pulsövervakning</li>` | Källan säger att man justerar hastighet och lutning och övervakar pulsen, inte att man reglerar pulsen. |
| 10002 | 10656692470026 | html | `<li>Dig som vill ha pulssensorer, snabbjusteringsknappar och nödstoppsknapp på löpbandet</li>` | `<li>Dig som vill ha pulssensorer och snabbjusteringsknappar för hastighet och lutning</li>` | Nödstoppsknappen ska inte användas som köpskäl i "Passar för", eftersom det är en säkerhetsfunktion. Den står kvar som faktarad under Specifikationer. |
| 10010 | 10656690897162 | html | `<li>Träningsprogram: 36, varav 3 pulsstyrda</li>` | `<li>Träningsprogram: 36 förinställda, 3 pulsstyrda</li>` | Källan räknar upp 36 förinställda och 3 pulsstyrda program var för sig. "Varav" är en tolkning. |
| 10012 | 10612574191882 | meta | `16 tums TFT-skärm` | `16-tums TFT-skärm` | Sammansättning med bindestreck, som i övriga utkast. Meta blir 144 tecken. |
| 10012 | 10612574191882 | html | `med 16 tums TFT-skärm` | `med 16-tums TFT-skärm` | Samma som ovan. |
| 10020 | 10470935593226 | html | `<li>Ram: Handstöd och låg ram</li>` | `<li>Utformning: Handstöd och låg ram</li>` | Handstöd är inte en del av ramen. |
| 10022 | 10650208633098 | html | `<li>Dig som söker ett hopfällbart löpband med löpyta 150 x 55 cm</li>` | `<li>Dig som söker ett löpband med löpyta 150 x 55 cm</li>` | Punkten upprepar hopfällningen från nästa punkt. |
| 10025 | 10471307411722 | html | `<li>Skärmfunktioner: Förinstallerade appar, Screen Mirroring</li>` | `<li>Skärmfunktioner: Förinstallerade appar, skärmspegling (Screen Mirroring)</li>` | Engelsk term i kundtexten. Punkten ovan säger redan "skärmspegling". |

## Öppna frågor till David
1. Godkänner du att "Maximum operating weight" i de engelska källorna (10021, 10024, 10025) återges som "Maximal användarvikt"?
2. Motorn anges som "3,5 AC" utan hk i källan (10007, 10010, 10011, 10016, 10022). Den återges så, till exempel "3,5 AC-motor". Ska det stå så, eller ska talet utelämnas?
3. 10017 (SKU G6540) avvisades som dubblett av 10018 (Nydo, G6541) trots att motorn skiljer sig (3,0 hk). Är det två olika varianter som var för sig ska få text?
4. 10002 (G688 LED): Easy Toolbar, pulssensorer, nödstopp och flaskhållare står i källan efter meningen om konsolalternativ. Jag har läst dem som utrustning på själva löpbandet. Stämmer det?
