# Granskning våg 2, utkast c_13, c_16 och c_18 – BEST OF SPORTS (2026-11-02)

Oberoende granskning. Jag har bara läst i Shopify och har inte ändrat någon utkastsfil. Butiken kontrollerades först med get-shop-info: **BEST OF SPORTS** (bestofsports.se, SEK).

**Underlag:** `vag2_skriv/c_13_utkast.json` (13 poster), `c_16_utkast.json` (14) och `c_18_utkast.json` (9), sammanlagt 36 utkast, samt `c_13/16/18_avvisade.json` (2 + 1 + 6). Standarden (`produkttexter-standard.md`, avsnitt 1–11), `LARDOMAR.md`, `handhavd_ids.txt` och formatet i `vag2_a_granskning_2.md`.

**Metod:**
- **Källan live:** title, handle, status, productType, vendor, tags, descriptionHtml, seo och variants hämtades med graphql_query (`nodes`) i tre batchar (13, 14 och 9). Alla 36 är ACTIVE, productType är tom och vendor är Gymstick, oförändrat. Ingen har taggen "På beställning". Fältet `fakta` stämmer med live, med tre undantag: 3258 (fakta kopierad från den rosa mattan, se nedan), 3183 (live 28 varianter, fakta 20) och 3194 (live 23 varianter och 6 utan pris, fakta 20 och 8).
- **Maskinellt:** längder och antal kommatecken (titlar 19–62 tecken, högst 2 kommatecken; SEO-titlar 20–43; meta 132–155 eller null), standardblocket jämfört tecken för tecken mot `c_1_utkast.json` (alla 36 identiska, utan fraktavgift i kronor), dubbletter av titel och SEO-titel mot alla `c_*_utkast.json` (inga dubbletter som rör de här filerna), och att varje "före"-text nedan förekommer exakt en gång i utkastet. Kontrollskriptet kördes inte av mig.
- **För hand:** varje titel, SEO-titel, meta och html lästes mot live-källan och språkgranskades.

## Resultat i korthet

| Kategori | Antal | Nr |
|---|---|---|
| GODKÄND | 12 | 3227, 3230, 3232, 3233, 3235, 3236, 3237, 3238, 3263, 3270, 3257, 3261 |
| RÄTTA | 18 | 3181, 3182, 3183, 3185, 3188, 3189, 3190, 3191, 3192, 3193, 3194, 3226, 3231, 3240, 3256, 3258, 3259, 3269 |
| UNDERKÄND | 6 | 3186, 3187, 3228, 3229, 3234, 3260 |

Totalt 36. Avvisade av utkastaren (9): alla avvisningar är rätt; inget kan släppas.

**Huvudfynd:** alla 13 utkast i `c_13` har samma FAQ, "Går bandet att tvätta? Ja, bandet tål maskintvätt i 30 grader …", som inte har något stöd i källan och inte hör till produkterna (hjul, hantlar, golv, stepbrädor). Det är en påhittad uppgift och hela avsnittet "Vanliga frågor" ska bort. `c_16` och `c_18` har inga FAQ.

## Tabell

| Nr | Id | Dom | Rättning (före → efter) eller skäl |
|---|---|---|---|
| 3181 | 10581110161674 | RÄTTA | **html:** "<h2>Vanliga frågor</h2><h3>Går bandet att tvätta?</h3><p>Ja, bandet tål maskintvätt i 30 grader. Använd inte torktumlare eller torkskåp.</p>" → (tas bort)<br>**html:** "Enligt tillverkaren passar det både hemmaträning och gym." → "Enligt tillverkaren passar det för både hemmaträning och gym."<br>FAQ om att tvätta ett band är felkopierad och hör inte till produkten (påhittad uppgift); hela avsnittet Vanliga frågor tas bort. Prepositionen "för" saknas. |
| 3182 | 10581110194442 | RÄTTA | **html:** "<h2>Vanliga frågor</h2><h3>Går bandet att tvätta?</h3><p>Ja, bandet tål maskintvätt i 30 grader. Använd inte torktumlare eller torkskåp.</p>" → (tas bort)<br>**html:** "Enligt tillverkaren passar det både intervallträning och uppvärmning." → "Enligt tillverkaren passar det för både intervallträning och uppvärmning."<br>FAQ om att tvätta ett band är felkopierad och hör inte till produkten (påhittad uppgift); hela avsnittet Vanliga frågor tas bort. Prepositionen "för" saknas. |
| 3183 | 10581110227210 | RÄTTA | **html:** "<h2>Vanliga frågor</h2><h3>Går bandet att tvätta?</h3><p>Ja, bandet tål maskintvätt i 30 grader. Använd inte torktumlare eller torkskåp.</p>" → (tas bort)<br>**html:** "Gymstick Pro Hex Hantel är en hexhantel med sexkantig form." → "Gymstick Pro Hex Hantel är en hantel med sexkantig form."<br>**meta:** "Gymstick Pro Hex Hantel är en hexhantel med sexkantig form." → "Gymstick Pro Hex Hantel är en hantel med sexkantig form."<br>FAQ om att tvätta ett band är felkopierad och hör inte till produkten (påhittad uppgift); hela avsnittet Vanliga frågor tas bort. "Hexhantel med sexkantig form" säger samma sak två gånger (meta blir 141 tecken). Live har 28 varianter (1–60), inte 20 som i fakta; vikten är rätt olåst. |
| 3185 | 10581110292746 | RÄTTA | **html:** "<h2>Vanliga frågor</h2><h3>Går bandet att tvätta?</h3><p>Ja, bandet tål maskintvätt i 30 grader. Använd inte torktumlare eller torkskåp.</p>" → (tas bort)<br>**html:** "Enligt tillverkaren passar den både hemmagym och gym." → "Enligt tillverkaren passar den för både hemmagym och gym."<br>FAQ om att tvätta ett band är felkopierad och hör inte till produkten (påhittad uppgift); hela avsnittet Vanliga frågor tas bort. Prepositionen "för" saknas. |
| 3186 | 10581110358282 | UNDERKÄND | Viktplattor är produkter med last (Davids beslut 2026-11-02 om 2310/2314; c_18 har avvisat viktskivorna 3264 av samma skäl). Hålets diameter saknas i källan, och 7 varianter (1,25–25) med olika pris. Utkastet har också den felkopierade FAQ:n om tvätt av band. |
| 3187 | 10581110391050 | UNDERKÄND | Viktset med okänt innehåll (stång, vikter, lås, antal anges inte) = produkt med last, och källan är för tunn för att skriva säkert. Om 20 kg avser setet framgår inte. Felkopierad FAQ om tvätt av band. Samma bedömning som 3234. |
| 3188 | 10581110423818 | RÄTTA | **html:** "<h2>Vanliga frågor</h2><h3>Går bandet att tvätta?</h3><p>Ja, bandet tål maskintvätt i 30 grader. Använd inte torktumlare eller torkskåp.</p>" → (tas bort)<br>FAQ om att tvätta ett band är felkopierad och hör inte till produkten (påhittad uppgift); hela avsnittet Vanliga frågor tas bort. |
| 3189 | 10581110456586 | RÄTTA | **html:** "<h2>Vanliga frågor</h2><h3>Går bandet att tvätta?</h3><p>Ja, bandet tål maskintvätt i 30 grader. Använd inte torktumlare eller torkskåp.</p>" → (tas bort)<br>FAQ om att tvätta ett band är felkopierad och hör inte till produkten (påhittad uppgift); hela avsnittet Vanliga frågor tas bort. |
| 3190 | 10581110522122 | RÄTTA | **html:** "<h2>Vanliga frågor</h2><h3>Går bandet att tvätta?</h3><p>Ja, bandet tål maskintvätt i 30 grader. Använd inte torktumlare eller torkskåp.</p>" → (tas bort)<br>**html:** "Gymstick Pro Gummi Golv är ett gummigolv i golvplattor på 50 x 100 cm." → "Gymstick Pro Gummi Golv består av gummiplattor på 50 x 100 cm."<br>**meta:** "Gymstick Pro Gummi Golv är ett gummigolv på 50 x 100 cm. Enligt tillverkaren ger det stötdämpning och ljudisolering. Finns i flera varianter." → "Gymstick Pro Gummi Golv består av gummiplattor på 50 x 100 cm. Enligt tillverkaren ger plattorna stötdämpning och ljudisolering. Finns i flera varianter."<br>FAQ om att tvätta ett band är felkopierad och hör inte till produkten (påhittad uppgift); hela avsnittet Vanliga frågor tas bort. "Gummi Golv är ett gummigolv" är cirkulärt och "ett gummigolv i golvplattor" haltar; källan säger golvplattor (meta blir 153 tecken). Tjockleken 3 cm (titel/text) mot varianterna 30/40 är rätt olåst. |
| 3191 | 10581110554890 | RÄTTA | **html:** "<h2>Vanliga frågor</h2><h3>Går bandet att tvätta?</h3><p>Ja, bandet tål maskintvätt i 30 grader. Använd inte torktumlare eller torkskåp.</p>" → (tas bort)<br>**html:** "Enligt tillverkaren passar den både hemmagym och gym." → "Enligt tillverkaren passar den för både hemmagym och gym."<br>FAQ om att tvätta ett band är felkopierad och hör inte till produkten (påhittad uppgift); hela avsnittet Vanliga frågor tas bort. Prepositionen "för" saknas. Öppen fråga: stepbräda bär kroppsvikt och källan saknar maxbelastning (se slutet). |
| 3192 | 10581110587658 | RÄTTA | **html:** "<h2>Vanliga frågor</h2><h3>Går bandet att tvätta?</h3><p>Ja, bandet tål maskintvätt i 30 grader. Använd inte torktumlare eller torkskåp.</p>" → (tas bort)<br>FAQ om att tvätta ett band är felkopierad och hör inte till produkten (påhittad uppgift); hela avsnittet Vanliga frågor tas bort. Öppen fråga om stepbrädor (maxbelastning saknas, justerbar höjd). |
| 3193 | 10581110620426 | RÄTTA | **html:** "<h2>Vanliga frågor</h2><h3>Går bandet att tvätta?</h3><p>Ja, bandet tål maskintvätt i 30 grader. Använd inte torktumlare eller torkskåp.</p>" → (tas bort)<br>**meta:** "är en hantel med slitstark vinylbeläggning." → "är en hantel med vinylbeläggning."<br>FAQ om att tvätta ett band är felkopierad och hör inte till produkten (påhittad uppgift); hela avsnittet Vanliga frågor tas bort. "Slitstark" är tillverkarens påstående utan "enligt tillverkaren" i meta (meta blir 136 tecken). |
| 3194 | 10581110653194 | RÄTTA | **html:** "<h2>Vanliga frågor</h2><h3>Går bandet att tvätta?</h3><p>Ja, bandet tål maskintvätt i 30 grader. Använd inte torktumlare eller torkskåp.</p>" → (tas bort)<br>FAQ om att tvätta ett band är felkopierad och hör inte till produkten (påhittad uppgift); hela avsnittet Vanliga frågor tas bort. Live har 23 varianter (5–60), varav 6 med pris 0 kr (42,5, 47,5, 52,5, 55, 57,5, 60); fakta säger 20 varianter och 8 utan pris. Texten låser ingen vikt, men prisfelen bör ses av David. |
| 3226 | 10581112193290 | RÄTTA | **html:** "Enligt tillverkaren passar den både för hemmabruk och på gymmet." → "Enligt tillverkaren passar den för både hemmabruk och gym."<br>Ordföljd och parallellitet. Varianter 33/60 rätt olåsta. |
| 3227 | 10581112226058 | GODKÄND | Varianterna Default/90 (olika pris) är rätt olåsta. |
| 3228 | 10581112258826 | UNDERKÄND | Oklar produkttyp: källan säger inte vad Universal Paw är; titeln saknar typord ("Universal Paw Gymstick") och texten kallar den bara "träningsutrustning". Utkastaren flaggar själv. |
| 3229 | 10581112324362 | UNDERKÄND | Oklar produkttyp: källan säger inte vad Universal Spike är; titeln saknar typord och källan bygger på "kontroll och säkerhet". Utkastaren flaggar själv. |
| 3230 | 10581112357130 | GODKÄND | "V-Bar" är engelskt typord utan svenskt typord i titeln; godtagbart (V-bar används i svensk handel), men David kan välja t.ex. "Kabelhandtag Gymstick V-Bar" för enhetlighet med 3232. |
| 3231 | 10581112389898 | RÄTTA | **html:** "<li>Vikt: 15 kg (set)</li>" → "<li>Vikt: 15 kg</li>"<br>"(set)" är en tolkning; källan säger bara "Set 15kg" och utkastaren vet inte om vikten är total eller per hantel. |
| 3232 | 10581112422666 | GODKÄND |  |
| 3233 | 10581112455434 | GODKÄND | Vikt och antal (2 x 1 kg mot fem varianter 1–5) rätt olåsta. |
| 3234 | 10581112488202 | UNDERKÄND | Viktset med okänt innehåll (skivor, stång, grepp anges inte); typen "viktset" kommer bara från taggen. Produkt med last enligt utkastarens egen flagga; samma bedömning som 3187. |
| 3235 | 10581112553738 | GODKÄND | Varianter 4–12 rätt olåsta. |
| 3236 | 10581112586506 | GODKÄND | Varianter 3–12 rätt olåsta. "Medicinboll" från taggen Medicinbollar. |
| 3237 | 10581112619274 | GODKÄND | Färgvarianterna BL/LI/PI/TU är rätt olåsta (originaltiteln säger Svart). |
| 3238 | 10581112652042 | GODKÄND | Färgvarianterna G/LI/PI/TU är rätt olåsta (originaltiteln säger grå). |
| 3240 | 10581112750346 | RÄTTA | **html:** "<li>Material: Trä (enligt produktnamnet)</li>" → "<li>Material: Trä</li>"<br>**seo_title:** "Balansbräde i Trä Gymstick Wooden" → "Balansbräde Gymstick i Trä"<br>"(enligt produktnamnet)" är en arbetsterm i kundtext (avsnitt 10). SEO-titeln har engelskt "Wooden" som upprepar "i Trä"; ny SEO-titel = titeln och lagras tom. Öppen fråga: balansbräde i trä har fallrisk och saknar maxbelastning (utkastaren flaggar). |
| 3256 | 10581119303946 | RÄTTA | **meta:** "Gymstick Vivid är en träningsmatta på 170 x 60 cm och 0,4 cm tjock, avsedd för övningar som yoga, stretching och styrketräning. Färg: Rosa och grå." → "Gymstick Vivid är en träningsmatta som mäter 170 x 60 cm och är 0,4 cm tjock. Den är avsedd för yoga, stretching och styrketräning. Färg: Rosa och grå."<br>"En träningsmatta på 170 x 60 cm och 0,4 cm tjock" är grammatiskt fel (jfr rättning 2206). Meta blir 151 tecken. |
| 3257 | 10581119336714 | GODKÄND | Tunn källa, kort text utan meta, följer regeln. Öppen fråga om stepbrädor (maxbelastning saknas). Frivilligt: titeln upprepar typordet på engelska ("Stepbräda … Step Board"). |
| 3258 | 10581119369482 | RÄTTA | **meta:** "Gymstick Vivid är en träningsmatta på 170 x 60 cm och 0,4 cm tjock, avsedd för övningar som yoga, stretching och styrketräning. Färg: Turkos och grå." → "Gymstick Vivid är en träningsmatta som mäter 170 x 60 cm och är 0,4 cm tjock, avsedd för yoga, stretching och mer intensiva pass. Färg: Turkos och grå."<br>**html:** "avsedd för övningar som yoga, stretching och styrketräning.</p>" → "avsedd för övningar som yoga, stretching och mer intensiva pass.</p>"<br>**html:** "<li>Dig som vill ha en matta att använda vid styrketräning</li>" → "<li>Dig som vill ha en matta till mer intensiva pass</li>"<br>Faktafel: live-källan för turkos säger "allt från yoga och stretching till mer intensiva pass", inte styrketräning. Fältet fakta i utkastet är kopierat från den rosa mattan (3256) och stämmer inte med live. Dessutom samma grammatikfel i meta som 3256. Meta blir 151 tecken. |
| 3259 | 10581119402250 | RÄTTA | **html:** "<li>Längd: 33 cm</li>" → "<li>Mått: 33 cm</li>"<br>Källan anger 33 cm bara i titeln utan att säga att det är längden (utkastaren flaggar själv); "Mått" påstår inte vilken dimension. |
| 3260 | 10581119435018 | UNDERKÄND | Oklar produkttyp: källan säger bara "tube trainer" (inte om det är motståndsband, handtag eller motstånd); utkastet använder det neutrala "Träningsredskap" som titel och SEO-titel. Dessutom står "styrketräning" i intro, medan källan säger uppvärmning, konditionsträning och rehabilitering. Samma skäl som 3228/3229. |
| 3261 | 10581119467786 | GODKÄND |  |
| 3263 | 10593397408010 | GODKÄND |  |
| 3269 | 10593407566090 | RÄTTA | **html:** "är ett balanskudde" → "är en balanskudde"<br>Genusfel (en kudde). Typordet "balanskudde" är översatt från "Balance Pad"; i våg 1 blev Tunturis Balance Pad "balansplatta". David bör välja ett ord. |
| 3270 | 10593407729930 | GODKÄND |  |

## Avvisade av utkastaren (kontrollerade)
- 3184 Pro Knee Straps, 3195 Pro Wrist Straps: skydd/stöd med skadeförebyggande påståenden och oklar typ. Rätt avvisade.
- 3239 Lyftbälte: skydd vid tunga lyft, oförklarade varianter. Rätt.
- 3262 Aktiv Hantelstång (tagg Pull-up, oklar typ), 3264 viktskivor 2 x 10 kg, 3265 2 kg hantelstång: last. Rätt.
- 3266 Ab Straps (hängande, bär kroppsvikt), 3267 Fotledsstöd 2.0, 3268 Ryggstöd 1.0: last eller stöd med skadepåståenden. Rätt.

## Gränsdragning som David bör bekräfta
- **Hantlar och kettlebells** (3183, 3185, 3193, 3194, 3231, 3233, 3235, 3236) har jag inte räknat som last, i linje med våg 1 där hantlar, kettlebells och viktskivor skrevs. **Viktplattor och viktset** (3186, 3187, 3234) har jag underkänt, i linje med Davids beslut 2026-11-02 (2310, 2314) och utkastarens avvisning av 3264. Det blir då olika regler för viktskivor i våg 1 och våg 2.
- **Stepbrädor och balansbräde** (3191, 3192, 3257, 3240) bär kroppsvikt och källan saknar maxbelastning. 3192 har justerbar höjd. Inget av utkasten lovar något om belastning, så jag har inte underkänt dem, men utkastarna flaggar själva risken. Om David räknar dem som säkerhetsprodukter blir de fyra underkända.
- **3194:** sex varianter har priset 0 kr i butiken. Det gäller inte texten men bör rättas.

## Mönster
- En felkopierad FAQ i en hel fil (c_13). Kontrollskriptet upptäcker inte detta, eftersom det inte jämför FAQ mot källan.
- "passar det både X och Y" utan "för" (5 utkast).
- Arbetstermer och tolkningar i specifikationen: "(enligt produktnamnet)", "(set)", "Längd" där källan bara anger ett mått.
- Engelskt typord upprepat efter det svenska i titeln ("Stepbräda … Step Board", "Yogarem … Yoga Strap", "Träningshjul … Exercise Wheel"). Godtaget som modellnamn, i linje med 2208 i våg 2a. Inte rättat.
