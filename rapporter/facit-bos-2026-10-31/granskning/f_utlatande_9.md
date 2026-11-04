# Granskning faktatext f_9 (roddmaskiner, latsdrag, Hammer-lås, viktplattor, skivstänger) – BEST OF SPORTS (2026-11-04)

Oberoende granskning, endast läsning. Butiken bekräftad med get-shop-info: **BEST OF SPORTS** (bestofsports.se, SEK).

**Underlag:** `vag2_skriv/f_9_utkast.json` (23 poster, nr 10201–10225 utom 10222/10223), `f_9_avvisade.json` (10222, 10223). FAKTATEXTLÄGE (§14–17, `fakta_utkastprompt.md`); meta 70–155 (§17); standardblocket jämfört med `b_skriv_24.json`; Davids beslut alt A 2026-11-04.

**Metod:** alla 25 hämtade live (graphql `nodes`). Alla ACTIVE. Längder, kommatecken, standardblock, beställningsmening mot taggen 'På beställning' och unikhet mot alla övriga `*_utkast.json` och `*skriv*.json` kontrollerade maskinellt: titlar 24–63 tecken (högst 2 kommatecken), SEO 24–43, meta 124–152 (efter rättning högst 153), inga dubbletter. Standardblocket identiskt; beställningsmeningen finns exakt på de 11 med taggen (10201–10203, 10205–10212) och saknas på övriga. Inga '&', 'här kallad', förkortningar i SEO eller tappade modellnamn utom 10208 meta.

## Resultat
| Dom | Antal | Nr |
|---|---|---|
| GODKÄND | 17 | alla utom nedan |
| RÄTTA | 6 | 10208, 10211, 10219, 10220, 10221, 10225 |
| UNDERKÄND | 2 | 10222, 10223 (avvisningarna bekräftas) |

## Last på skivstängerna (frågan om alt A)
Alt A gäller oförklarad maxvikt/användarvikt. En skivstångs lastkapacitet är en belastningsgräns och får stå bara om den är entydig i just den produktens källa. Bedömt per produkt:
- **10219 Maximum PRO:** 800 kg i titel, brödtext och spec (entydigt) – behålls som 'enligt tillverkaren'.
- **10220 Olympic Barbell:** 700 kg i titel, spec och brödtext – behålls som 'enligt tillverkaren'. Brödtexten är Hammers gemensamma text (står även i 10222 med spec 250 kg), men titel och spec bekräftar 700 kg för just denna.
- **10221 SZ-Curl Bar:** 225 kg i titel, brödtext och spec – behålls i spec som 'enligt tillverkaren', stryks ur meta.
- **10225 Toorx:** 320 kg i titel och spec – behålls som 'enligt tillverkaren'.
- **10222:** 250 kg mot 700 kg och två varianter – underkänd (rätt avvisad).
Utkastet hade raderna utan 'enligt tillverkaren'; det läggs till på varje rad. Vill David vara strängare (all last på skivstänger stryks) är det fyra rader att ta bort, se frågor.

## Övriga kontroller
- **Typordsbyten:** Lyftstång → Skivstång (källtexterna säger 'skivstång', tagg Skivstång på 10220/10225), 'Lever locks' → Leverlås (ordagrann översättning, samma typord som 10218:s live-titel), 'Barbell Shoulder Pad' → Skivstångsskydd för axlar (står ordagrant i källtexten), 'Hammar' → Hammer (vendor och text) – alla godtas.
- **Källkonflikter:** 10220 längd (222/220) utelämnad; 10212 vikt (120/230) – bara viktmagasinet 120 kg från brödtexten; 10225 tagg '30mm' mot 50 mm i titel och text – texten följer titel/text; 10224 handle (5 kg, 17032) mot källa (2,5 kg, 17031) – texten följer källan.
- **10213/10215/10218 (identisk källtext):** titel, SEO-titel, meta och inledning skiljer sig åt; inga uppgifter utöver titlarnas (svart aluminium, Premium, Röd).
- **Maxvikt (alt A):** 'Maximal användarvikt' står ordagrant på svenska i källan för alla 7 som har den (10202, 10204, 10205, 10207, 10208, 10209, 10210). Utelämnade korrekt: Maximal driftsvikt, Max. belastning, Belastning, Belastningskapacitet och Lastkapacitet på roddmaskinerna och latsdraget.
- **Syskonläckage:** inget. 10207 och 10208 har samma mått (213 x 54 x 56 cm) men var och en i sin egen källa.

## Per produkt
| Nr | Id | Dom | Före → efter / skäl |
|---|---|---|---|
| 10201 | 10472259059978 | GODKÄND | Data ordagrant (LCD 49 x 24 mm, 5 program, 8 grader, PMS manuellt, 2 x AA, mått, hopfällt mått, 26,5 kg). Surfplattehållaren står i källan ('den medföljande hållaren'); hopfällbar följer av 'Mått hopfälld'. Belastningskapacitet, 'Maximal driftsvikt' och 'Max. belastning' utelämnade (alt A). Beställningsmening rätt. |
| 10202 | 10561337393418 | GODKÄND | Data ordagrant; 'Belastning: 5,5 kg' utelämnad; 'Maximal användarvikt: 120 kg' står ordagrant på svenska. Hopfällbar och transporthjul i källan; 'robust roddhandtag' borta. 5,5-tums skrivs rätt. Beställningsmening rätt. |
| 10203 | 10472306376970 | GODKÄND | Kedja i stället för band och två delar som snäpper ihop står i källan (enligt tillverkaren). Trasiga 'aerodynamisk löpbana' och resultatlöften borta; Lastkapacitet 4,5 kg och 'Maximal driftsvikt' utelämnade (alt A). Beställningsmening rätt. |
| 10204 | 10676602732810 | GODKÄND | Data ordagrant; 'idealisk för lågintensiv träning' borta; 'Maximal användarvikt: 150 kg' ordagrant. Ingen beställningstagg, ingen beställningsmening (rätt). |
| 10205 | 10605385056522 | GODKÄND | Data ordagrant (Fluid BT Monitor, 4 nivåer, vatten, 213 x 52 x 56 cm, 34,7 kg); stål och trä samt bokton enligt tillverkaren, 'styrka/hållbarhet' borta; 'Maximal användarvikt' ordagrant. SEO utan 'Rower' godtas. Skiljs från 10206 (annan SKU, annan källa, annan finish). |
| 10206 | 10472262729994 | GODKÄND | Källan saknar mått, vikt och maxvikt och utkastet har inga. Fluid Monitor, Twin Tank, stål/amerikanskt askträ, justerbara fotplattor och remmar samt pulsbälte står i källan; hälso-, pulssäkerhets-, hållnings- och stabilitetstext borta. 'Pedal ergometer' i bildtexten är felord; titel, tagg och text gäller roddmaskin. |
| 10207 | 10494771265802 | GODKÄND | Tunn källa, allt ordagrant (10 nivåer, 213 x 54 x 56 cm, 36,04 kg, 'Maximal användarvikt: 150 kg'). productType Professionell utrustning oförändrad. |
| 10208 | 10468716740874 | RÄTTA | meta: `Tunturi Evo E550 är en roddmaskin av aluminium med Fluid Twin-Tank XL och 10 motståndsnivåer. Måtten är 213 x 54 x 56 cm och vikten 30,84 kg.` → `Tunturi Fluid Rower Evo E550 är en roddmaskin av aluminium med Fluid Twin-Tank XL och 10 motståndsnivåer. Måtten är 213 x 54 x 56 cm och vikten 30,84 kg.`<br>Meta tappar modellnamnet ('Fluid Rower'); återställs (153 tecken). Övrigt ordagrant (aluminium, Fluid Twin-Tank XL, 10 nivåer, mått, 30,84 kg, maxvikt ordagrant). 'Silver Bronze' behålls som del av källans produktnamn. |
| 10209 | 10605385122058 | GODKÄND | Data ordagrant; Twin Tank med två separata tankar står i källan; 'suverän kvalitet' borta; 'Maximal användarvikt' ordagrant. Beställningsmening rätt. |
| 10210 | 10673180147978 | GODKÄND | Hemmabruk, kompakt och hopfällbar står i källan; 'träna hela kroppen'/'smarta funktioner' borta; data ordagrant; 'Maximal användarvikt: 120 kg' ordagrant. |
| 10211 | 10461966860554 | RÄTTA | html: `<li>Strömförsörjning: 9V adapter</li>` → `<li>Strömförsörjning: 9 V-adapter</li>`<br>Data ordagrant; 21 program följer specifikationen (brödtextens '20 förinställda ... eller skapa ditt eget' går ihop med 21). Belastningskapacitet och 'Maximal driftsvikt' utelämnade (alt A). Fotstöd med remmar, surfplatte- och flaskhållare samt transporthjul står i källan. Rättning: '9V adapter' skrivs '9 V-adapter' (enhet med mellanslag, svensk sammansättning). |
| 10212 | 10472304312586 | GODKÄND | Godkänd: bara viktmagasinet 120 kg (brödtexten) och 2,5 mm stålram återges; de motsägande 'Vikt'-raderna (120/230 kg) och 'Maximal driftsvikt' är utelämnade; 'komplett ryggträning'/'idealisk för gym' borta. Typordet Latsdrag/Rodd står i live-titeln och taggen Latsdrag. Obs: maskin med viktmagasin, se fråga till David. |
| 10213 | 10650210533642 | GODKÄND | 'Hammar' → Hammer stöds av vendor och källtext. 50 mm, Olympic-standard och snabbt byte av viktskivor enligt tillverkaren; säkerhets-/trygghetslöften borta; ingen belastning i källan. Svart aluminium bara i titeln. Titel, SEO, meta och text skiljer sig från 10215 och 10218 trots identisk källtext. |
| 10215 | 10650210566410 | GODKÄND | Som 10213 men 'Premium' från titeln; inget påstående om vad Premium innebär. Titel, SEO och meta unika mot 10213/10218. |
| 10217 | 10650210599178 | GODKÄND | 'Lever locks' → Leverlås (ordagrann översättning av källans typord, samma som 10218:s live-titel). Skjuta på/av, förstärkt nylon och härdade kulor i rostfritt stål ordagrant; 'säkert låsta', bänkpress/marklyft borta; ingen diameter påstås. |
| 10218 | 10650210500874 | GODKÄND | Leverlås står i live-titeln (källtexten säger snabblås, utkastet följer titeln). 50 mm, olympisk standard enligt tillverkaren; Röd bara i titeln, en variant. Säkerhetslöften borta. |
| 10214 | 10650210763018 | GODKÄND | 'Barbell Shoulder Pad' → Skivstångsskydd för axlar står ordagrant i källtexten. Tryck-, dämpnings- och komfortpåståenden borta; övningarna enligt tillverkaren; fästs på skivstången står i källan. Inga mått påhittade. |
| 10216 | 10472302936330 | GODKÄND | Data ordagrant (5 kg, 30 mm, 28 mm, 20,5 cm, 1 viktplatta); passar 30 mm-stänger enligt tillverkaren; drömkropp och handtag (gäller 5–20 kg, oklart) borta. |
| 10224 | 10656692076810 | GODKÄND | Data ordagrant (åttkantig, 2,5 kg, 50 mm, 23 cm, 1 viktplatta); stabilitet borta. Handle säger 5 kg och 17032 men varianten/SKU och källan säger 17031 och 2,5 kg; texten följer källan. |
| 10219 | 10673179656458 | RÄTTA | html: `<li>Lastkapacitet: 800 kg</li>` → `<li>Lastkapacitet: 800 kg (enligt tillverkaren)</li>`<br>Lastkapaciteten 800 kg står entydigt i tre led i just denna produkts källa (titel '800kg', brödtext 'maximal lastkapacitet på upp till 800 kg', specifikation 'Lastkapacitet: 800 kg') och gäller skivstången; behålls men markeras 'enligt tillverkaren' en gång. 'Lyftstång' → Skivstång stöds av källtexten ('skivstång'). Halkfritt/säkert grepp borta. |
| 10220 | 10673179721994 | RÄTTA | html: `<li>Belastningskapacitet: 700 kg</li>` → `<li>Belastningskapacitet: 700 kg (enligt tillverkaren)</li>`<br>Belastningskapaciteten 700 kg står i titel, specifikation och brödtext; behålls som 'enligt tillverkaren'. Längdkonflikten (titel 222 cm, spec 220 cm) korrekt hanterad: ingen längd i texten. Kullager enligt tillverkaren; skaderisk/grepp borta. Obs: brödtextens '700 kg' är Hammers gemensamma text (står även i 10222 där specen säger 250 kg), men här stöds den av titel och spec. |
| 10221 | 10650210730250 | RÄTTA | meta: `Hammer Premium SZ-Curl Bar är en böjd SZ-skivstång på 120 cm av stål med svart finish. Den väger 10 kg och har lastkapaciteten 225 kg.` → `Hammer Premium SZ-Curl Bar är en böjd SZ-skivstång på 120 cm av stål med svart finish. Den väger 10 kg och passar viktplattor med 50 mm håldiameter.`<br> html: `<li>Lastkapacitet: 225 kg</li>` → `<li>Lastkapacitet: 225 kg (enligt tillverkaren)</li>`<br>Lastkapaciteten 225 kg står i titel, brödtext ('tål stången belastningar upp till 225 kg') och spec; behålls i specifikationen som 'enligt tillverkaren' och stryks ur meta (meta utan maxlast, 148 tecken). Handleds-/ledpåståenden och den förvirrade kullagertexten borta. |
| 10225 | 10411923341578 | RÄTTA | html: `<li>Lastkapacitet: 320 kg</li>` → `<li>Lastkapacitet: 320 kg (enligt tillverkaren)</li>`<br>Lastkapaciteten 320 kg står i titel och spec; behålls som 'enligt tillverkaren'. Taggen 'skivstång 30mm' motsäger titel och text (50 mm); utkastet följer titel och text (rätt), taggen ändras inte av oss. 'Inte lämplig för CrossFit' återges som tillverkarens begränsning (rätt). |
| 10222 | 10650210664714 | UNDERKÄND | Avvisningen bekräftas: två varianter (17611 3039 kr, 17613 5699 kr) med oförklarade namn, längd 183/220 cm och belastning 250/700 kg motsäger varandra. |
| 10223 | 10650210369802 | UNDERKÄND | Avvisningen bekräftas: tre färgvarianter (Red/gray/yellow) med priser 379/559/2039 kr som tyder på olika vikter; titel låser Röd och 2,5 kg, handle säger grön 10 kg. |

## Öppna frågor till David
1. **Skivstängernas lastkapacitet (10219, 10220, 10221, 10225):** behålls i specifikationen som 'enligt tillverkaren' eftersom siffran är entydig i varje produkts egen källa. Godkänner du det, eller ska all last på skivstänger strykas?
2. **10212 latsdrag/rodd med 120 kg viktmagasin:** skrivs utan maxvikt och maskinvikt. Räknas maskiner med viktmagasin som säkerhetsprodukter (som bänkar och ställningar) eller får de gå i faktatextläge?
3. **10225:** taggen 'skivstång 30mm' motsäger produkten (50 mm). Leverantören eller du kan rätta taggen; vi ändrar inte taggar.
4. **10222 och 10223:** behöver delas upp per variant eller rättas av leverantören innan de kan skrivas.
