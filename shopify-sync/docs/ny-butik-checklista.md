# Checklista: ny butik i textutrullningen (Alpha Zoo och B You Underwear)

Skapad 2026-11-06 av Claude på Davids uppdrag. Filen fylls bara på. Den bygger på `textutrullning-rutin.md`, `regler/regler-v1.md`, `BESLUTSLOGG.md`, `LARDOMAR.md` och BOS-profilen `config/butiksprofil-bestofsports.json`.

**Status:** tomma profiler och spärrlistor finns, ingenting är inventerat och ingen åtkomst är ordnad. Inget får skrivas till någon butik förrän David fyllt i profilen och satt `klar_for_skrivning` till `true` i `_meta`.

Filer:

| Butik | Profil | Spärrlista |
|---|---|---|
| Alpha Zoo (alphazoo.se, .dk, .fi) | `config/butiksprofil-alphazoo.json` | `config/sparrlista-alphazoo.json` |
| B You Underwear (byouunderwear.se) | `config/butiksprofil-byou.json` | `config/sparrlista-byou.json` |

Obesvarade fält i profilerna har formen `"FYLLS_I_AV_DAVID": "fråga"`. Det som redan är ifyllt (butiksnamn, domäner, regelbokens gränser, sökvägar) står med källa under `_meta.kallor` och ska bekräftas av David.

## 1. Ordning (gäller båda butikerna)

| Steg | Vad | Vem | Klart när |
|---|---|---|---|
| 1 | Besvara frågorna för butiken nedan | David | Alla frågor har ett svar eller ett uttryckligt "avvakta" |
| 2 | Åtkomst enligt `textutrullning-rutin.md` §3: tillåt butikens myshopify-adress, skapa app med `read_products` och `write_products`, lägg nyckeln som hemlig miljövariabel. Aldrig nyckel i chatten eller repot. Aldrig `switch-shop` (LARDOMAR 2026-11-04) | David | Claude kan läsa en produkt i en ny session |
| 3 | Fyll i grunduppgifter i profilen: myshopify, språk, ton | Claude efter Davids svar | Fälten saknar `FYLLS_I_AV_DAVID` |
| 4 | Inventering (bara läsning): antal produkter, kategorier, märken, taggar, leverantörsappar som skriver produktdata | Claude | Inventeringsfil i `rapporter/inventering-<butik>-<datum>/` |
| 5 | Märken, taggar som inte får röras, standardblock, leveranstidstagg, SEO-suffix och längder i profilen | Claude föreslår, David godkänner | Fälten ifyllda |
| 6 | Riskkategorier: David bekräftar eller ändrar förslagen i avsnitt 4 och 5 | David | `faktatextlage_kategorier` och `utanfor_tills_vidare` ifyllda |
| 7 | Spärrlista: en inventeringsfil (CSV med kolumnen `produkt_id`) per spärr, och en post i spärrlistan. Format nedan | Claude | Alla produkter i kategorier under `utanfor_tills_vidare` ligger i en aktiv spärr |
| 8 | Torrkörning: `skrivfil_kontroll.py` mot en provskrivfil (när skripten är profilstyrda) och dry-run mot API:et | Claude | 0 fel |
| 9 | Pilot: kanarie på 3 produkter, återläsning tecken för tecken, därefter små batcher enligt rutinen | Claude, David godkänner | Återläsning utan avvikelse |
| 10 | Davids godkännande: `klar_for_skrivning` till `true` och beslutet in i `BESLUTSLOGG.md` | David | Skrivning får börja |

Ordningen är viktig: spärrlistan (steg 7) ska finnas före första skrivfilen. Det var så pilot- och experimentprodukterna i BOS skrevs över av misstag (LARDOMAR 2026-11-04).

### Format på en post i spärrlistan

```json
{
  "namn": "utanfor-tills-vidare-ÅÅÅÅ-MM-DD",
  "aktiv": true,
  "idfil": "rapporter/inventering-<butik>-<datum>/sparr_utanfor_tills_vidare.csv",
  "idkolumn": "produkt_id",
  "skal": "Kategorier under utanfor_tills_vidare i butiksprofilen.",
  "beslut": "David ÅÅÅÅ-MM-DD, hänvisning till svaret.",
  "kanda_overtradelser": []
}
```

## 2. Frågor till David: Alpha Zoo

Svara gärna med nummer och ja/nej eller en kort rad (till exempel "A1 en butik, A3 bara svenska först").

| Nr | Fråga |
|---|---|
| A1 | Är alphazoo.se, .dk och .fi en Shopify-butik med tre marknader, eller tre separata butiker? (Avgör om vi behöver en eller tre profiler och spärrlistor.) |
| A2 | Vilken är butikens myshopify-adress (eller adresser)? |
| A3 | Vilka språk ska texterna skrivas på: bara svenska först, eller också danska och finska? Vem kan granska dansk och finsk text? (Regelboken är skriven för svenska.) |
| A4 | Har du skapat appen och lagt nyckeln i miljön enligt rutinens §3? Om inte: ska vi börja med det? |
| A5 | Ska tonen vara samma som i BOS (saklig, bara uppgifter ur källan, inga löften)? |
| A6 | Finns en leverantörssynk eller app som skriver produkttexter eller arkiverar produkter (som Velomarket3 i BOS)? Vilka taggar får aldrig ändras? |
| A7 | Standardblock: finns en färdig text för leverans, retur, garanti, säljare och kontakt? Skiljer villkoren mellan Sverige, Danmark och Finland? |
| A8 | Finns beställningsvaror med längre leveranstid? Vilken tagg och vilken mening ska i så fall användas? |
| A9 | SEO-titel: ska den ha suffix (BOS: " – BEST OF SPORTS") och hur lång får den vara? Gränserna för titel (70 tecken, högst två kommatecken) och meta (70–155) kommer från regelboken R12. Godkänner du dem? |
| A10 | Är "Alpha Zoo" rätt skrivning av butiksnamnet i texterna? |
| A11 | Riskkategorier: bekräfta eller ändra förslaget i avsnitt 4 (särskilt foder, loppmedel och avmaskning, veterinära preparat). |
| A12 | Ska några produkter hållas utanför som mätgrupp eller pilot, som pilot-20 i BOS? |
| A13 | Omfattning: alla produkter, eller vissa kategorier först? |
| A14 | Finns levande djur, eller livsmedel av animaliskt ursprung, i sortimentet? |

## 3. Frågor till David: B You Underwear

| Nr | Fråga |
|---|---|
| B1 | Vilken är butikens myshopify-adress? |
| B2 | Är svenska det enda språket? (Utkastet `sites.portfolio.draft.toml` anger sv och profilen har det ifyllt, men det är inte bekräftat av dig.) |
| B3 | Har du skapat appen och lagt nyckeln i miljön enligt rutinens §3? Om inte: ska vi börja med det? |
| B4 | Är "B You" butikens eget märke? Finns andra märken som ska skrivas rätt? |
| B5 | Ska tonen vara saklig faktatext som i BOS, eller mer varumärkesnära? Vilka ord får aldrig användas om kroppen (förslag i avsnitt 5)? |
| B6 | Finns en leverantörssynk eller app som skriver produkttexter eller arkiverar produkter? Vilka taggar får aldrig ändras? |
| B7 | Standardblock: finns en färdig text för leverans, retur, garanti, säljare och kontakt? Gäller någon särskild returregel för underkläder av hygienskäl? |
| B8 | Får certifieringar (till exempel Oeko-Tex, GOTS) och uttrycket "ekologisk bomull" nämnas, och i så fall bara om det står ordagrant i produktens egen källa? |
| B9 | Ingår barn- eller tonårsmodeller i sortimentet? |
| B10 | Ingår mensskydd, inkontinens- eller andra absorberande underkläder? |
| B11 | Ingår formande underkläder (shapewear) eller kompressionsprodukter? |
| B12 | Säljs flerpack (2-pack, 3-pack) med olika pris eller innehåll under samma produkt? Hur ska varianter hanteras (jämför regelbok v1.8–v1.9)? |
| B13 | SEO-titel: suffix och längd? Godkänner du regelbokens gränser för titel (70) och meta (70–155)? |
| B14 | Riskkategorier: bekräfta eller ändra förslaget i avsnitt 5. |
| B15 | Ska några produkter hållas utanför som mätgrupp eller pilot? Vilka? |
| B16 | Omfattning: alla produkter eller vissa kategorier först? |

## 4. Förslag på riskkategorier: Alpha Zoo (för bekräftelse, inte beslut)

BOS-reglerna om faktatextläge, lastgräns (R4) och "enligt tillverkaren" (R5) är utgångspunkten. Förslaget gäller vad som bör prövas. Lagkrav ska kontrolleras mot myndighetens egna sidor innan en kategori släpps; listan är inget juridiskt underlag.

| Kategori | Risk | Förslag |
|---|---|---|
| Foder och godis (hund, katt, smådjur, fågel, fisk) | Näringsmässiga och hälsomässiga påståenden ("stärker lederna", "minskar allergi", "komplett"); sammansättning och analytiska halter måste stämma med etiketten | Faktatextläge. Bara etikettens uppgifter. Inga hälsopåståenden. Foderdeklaration återges ordagrant eller utelämnas |
| Specialfoder (diet, njure, allergi, veterinärfoder) | Texten kan läsas som behandlingsråd | Utanför tills vidare |
| Loppmedel, fästingmedel, avmaskning, öron- och ögonpreparat, vitaminer och kosttillskott för djur | Kan vara läkemedel eller biocid. Påståenden om att behandla, förebygga eller bota är riskabla | Utanför tills vidare |
| Halsband, koppel, selar, bilsäkerhet för hund, transportburar | Produktsäkerhet: bärande delar, brytlås, viktgräns. Motsvarar BOS "bärande delar" (R4, v1.10) | Faktatextläge. Viktgräns bara ordagrann svensk eller "Ej känd" enligt v1.10. Inga säkerhetslöften |
| Leksaker och tuggprodukter (tuggben, rawhide, bollar) | Kvävnings- eller tarmstoppsrisk, storlek mot djurets storlek | Faktatextläge. Inga "säker"-påståenden. Storleksvägledning bara ur källan |
| Burar, hägn, grindar, terrarier, akvarier | Produktsäkerhet, djurvälfärd (minimistorlek), fastklämning | Faktatextläge. Mått och lastgräns bara ur källan |
| Värme och el (värmelampor, värmemattor, akvarievärmare, pumpar, belysning) | Elsäkerhet, brand, överhettning | Faktatextläge. Effekt och spänning bara ur källan. Inga säkerhetslöften |
| Hygien och rengöring (schampo, tassvård, tandvård, rengöringsmedel) | Kan göra kosmetiska eller medicinska påståenden; kemikalier | Faktatextläge. Bara bruksanvisning ur källan |
| Påståenden om djuret ("passar valpar", "för äldre hundar", "hypoallergen", "veterinärrekommenderad", rasspecifika) | Ålders-, vikt- och rasuppgifter är oftast bara tillverkarens egen indelning | Bara med "enligt tillverkaren" och ordagrant ur källan |
| Levande djur och livsmedel av animaliskt ursprung (om de finns) | Särskild reglering | Utanför tills vidare tills fråga A14 besvarats |

## 5. Förslag på riskkategorier: B You Underwear (för bekräftelse, inte beslut)

| Kategori | Risk | Förslag |
|---|---|---|
| Kroppspåståenden ("formande", "bantande", "motverkar celluliter", "korrigerar hållning", "lyfter", "slimmar") | Påståenden om kroppens utseende eller hälsa som produkten inte kan styrka; kan vara skadligt för läsaren | Utanför som påståenden. Formande och kompressionsprodukter (fråga B11) skrivs med bara fakta ur källan (material, passform, mått), utan resultatpåståenden |
| Hälsopåståenden ("medicinsk", "ortopedisk", "stödjer ryggen", "förebygger svampinfektion", "antibakteriell", "motverkar svett och lukt") | Hälso- och hygienlöften utan underlag | Bara om det står ordagrant i källan, då "enligt tillverkaren". Annars utelämna |
| Material och fiber ("bambu", "naturligt", "andas", "temperaturreglerande", "mjuk som siden") | Fibernamn och procentandelar ska stämma med produktens märkning. Bambu är ofta viskos; "andas" och "temperaturreglerande" är egenskapspåståenden | Fibersammansättning ordagrant ur källan. Egenskapsord bara om de står i källan |
| Certifieringar och miljö (Oeko-Tex, GOTS, "ekologisk", "hållbar", "klimatsmart") | Certifierings- och miljöpåståenden kräver dokumentation | Bara om certifieringen står ordagrant i källan (fråga B8). Inga egna hållbarhetsord |
| Mensskydds-, inkontinens- och absorberande underkläder (om de finns) | Påståenden om absorption och läckagesäkerhet; kan vara medicinteknik | Utanför tills vidare tills fråga B10 besvarats |
| Barn- och tonårsmodeller (om de finns) | Åldersanpassad ton, ingen sexualiserande beskrivning; hänsyn till små delar | Utanför tills vidare tills fråga B9 besvarats. Därefter bara fakta (storlek, material, ålder enligt tillverkaren) |
| Produktsäkerhet: kemikalier och detaljer (metalldetaljer och nickel, färgämnen, prydnadsdetaljer och små delar, snören) | Allergi och kemikaliekrav; små delar | Faktatextläge. Inga "hudvänlig", "allergivänlig" eller "ofarlig" utan ordagrann källa |
| Storlek och passform ("sitter som en storlek mindre", storlekstabeller) | Felaktig storleksvägledning ger returer och missnöje | Storlekar ordagrant ur källan; ingen egen passformsbedömning (R3, v1.8) |
| Flerpack och varianter (2-pack, 3-pack, färgmix) | Olika artiklar under samma produkt; priset avgör inte vad som ingår | Titel och text låser inte antal om varianterna har olika innehåll; jämför v1.8–v1.9 |
| Hygien och retur (förseglade produkter) | Returvillkor kan skilja sig för underkläder av hygienskäl | Standardblocket ska ha rätt returtext (fråga B7). Texten kontrolleras mot gällande konsumentregler innan butiken släpps |

## 6. Vad som skiljer från BOS, att ta hänsyn till

- BOS är på svenska och regelbokens format (R9, R10) är skrivna för svenska. Alpha Zoo på dansk och finsk marknad behöver egna formatregler eller ett beslut att bara skriva svenska (A3).
- BOS-kategorierna (barn, kosttillskott, skydd) har inga direkta motsvarigheter. Motsvarande riskpunkter är foder och läkemedel för djur (Alpha Zoo) samt kropps-, hälso- och hygienpåståenden (B You).
- Typord (`godkanda_typord`) och märken (`marken`) fylls först efter inventeringen. Gissa dem inte.
- Spärrlistan är tom tills inventeringen är gjord. En tom spärrlista är ingen kontroll av att kategorierna är säkra.
