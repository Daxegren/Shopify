# Produktunderlag: produktdata-AI med kvalitetsrapport (självbetjäning)

Skapad 2026-11-04 av samordnaren. Filen fylls bara på. Inga löften om försäljningseffekt: inget är mätt än.

## 1. Vad kunden behöver för att köra systemet själv
| Del | Vad det är | Läge i praktiken (exempel) |
|---|---|---|
| Åtkomst | App per butik med läs/skriv på produkter, adress under Allowed domains, token som hemlig variabel | Svårast hittills. Shopify-verktygets koppling delas mellan sessioner och pekar på en butik; sex butikssessioner körde `switch-shop` och bröt BEST OF SPORTS. Dev Dashboard-flödet kräver manuella steg av ägaren per butik. Sex butiker väntar på detta (fråga S1). |
| Profil | Märken, typord, ton, standardblock, taggar, gränsvärden | Finns för 7 butiker som utkast; flera har TODO-fält som bara ägaren kan fylla (standardblock, ton, tilltal). |
| Spärrlista | Produkter/kategorier som aldrig skrivs | Regelverkskänsliga butiker (barn, tillskott, djurfoder) spärrar nästan hela sortimentet tills ägaren beslutat. |
| Inventering | Alla produkter inklusive utkast och arkiverade | Publik katalog räcker bara för publicerade produkter; status, SEO-fält och översättningar kräver admin. |
| Skrivväg | Skript mot Admin API med före-fil och återläsning | Inklistring för hand gav osynliga tecken och tappade meningar; API-skript tar bort det. |
| Kvalitetsrapport | Mätning av granskningsutfall per regel och typ | `mat_utbyte.py`; se avsnitt 2 i kommande mätrapport. |
| Sökdata | Search Console, GA4, Ads | Saknas i alla nya butiker; utan den kan åtgärder inte prioriteras på trafik. |

## 2. Pilotupplägg: mallgenerering mot AI (FÖRSLAG, ej godkänt, körs inte)
Bakgrund: David är öppen för att en mall genererar texten för produkter med strukturerad källdata och att AI bara används för undantag, om resultatet är minst lika bra. Beslut relaterat via bygg-sessionen 2026-11-04; inte bekräftat direkt i min chatt.

**Kategori:** kettlebells i BEST OF SPORTS (20 produkter skrivna av AI i fitnessgruppen; kontrollerat i skrivfilerna f_*). Alternativ: viktskivor (21). Kettlebell är enklast: få fält, ingen lastgräns, enkel text.

**Strukturerade fält (ur produktens egen källa):** märke, modell, vikt (kg), färg, material/överdrag (bara om entydigt i källan), "enligt tillverkaren"-rad om viktintervall för serien, avsedd användning bara om ordagrant i källan.

**Mall (en kod, inga fria formuleringar):**
- Titel: `Kettlebell {Märke} {Modell}, [{Färg}, ]{vikt} kg`
- Första meningen: `{Märke} {Modell} är en [{färg} ]kettlebell på {vikt} kg.` Därefter en mening per entydigt extrafält (serie/viktintervall, användning), alltid "enligt tillverkaren".
- Specifikationsrader: Vikt, Färg, Märke (stor bokstav efter kolon). Standardblock exakt ur profilen.
- Saknas ett fält utelämnas meningen; mallen gissar aldrig. Produkter med motsägande eller trasig källa går till AI-spåret (undantag).
- Mallen körs genom samma `skrivfil_kontroll.py` som AI-texterna.

**Blindjämförelse:** för varje produkt (A) befintlig AI-text och (B) malltext, avidentifierade och slumpad ordning. Oberoende granskare (Opus, inte samma instans som skrev AI-texterna) vet inte vilken som är vilken. Kriterier: faktakorrekthet mot live-källan, språk, tydlighet, SEO (titel/meta enligt R12). Poäng 0–2 per kriterium och en dom godkänd/rättas/underkänd. Ett stickprov om 5 produkter dubbelgranskas av en andra granskare för samstämmighet.

**Mätetal:** andel godkända direkt; antal faktafel per 100 produkter; antal rättningar per typ (samma indelning som `mat_utbyte.py`); tokens och tid per produkt (mall = 0 tokens för skrivning, plus kostnad för granskning); andel produkter som mallen måste lämna till AI.

**Gräns för när mall slår AI (föreslagen, David beslutar):** mall vinner om (1) godkända direkt är minst lika hög som AI, (2) faktafel är 0 eller färre än AI, (3) granskarna i snitt inte betygsätter språk och tydlighet lägre än 0,2 poäng under AI, och (4) mallen täcker minst 80 % av produkterna utan AI. Annars behålls AI för kategorin. Med 20 produkter är underlaget litet: ett utfall är en indikation, inte ett bevis.

**Villkor för start:** BEST OF SPORTS-sessionen är klar med sina batcher och David har godkänt upplägget. Piloten skriver inget i butiken; den jämför bara filer.

## 3. Pausläge (beslut relaterat 2026-11-04)
Övriga butiker väntar på att David installerar appen. Butikssessionerna avslutar fas 1 på publika data och vilar; inga nya agenter eller uppgifter dit. BEST OF SPORTS har företräde (gemensam användningsgräns) och får köra batcher om upp till 50 med kvalitetsvakt. Utfallet följs i mätningen.

## 4. Kvalitetsrapporten: vad som kan mätas idag (2026-11-04, tillägg)
Källa: `rapporter/matning-2026-11-04.md` (`mat_utbyte.py`, `mat_regler.py`), 2 159 granskade utkast i BEST OF SPORTS. Raden "Kvalitetsrapport" i tabellen i avsnitt 1 pekade på en kommande mätrapport; den finns nu.
- **Andel godkända direkt:** 49 % (rättas 40 %, underkänns 9 %). Per grupp 38–62 %. Det är den ärliga utgångspunkten: AI-text utan granskning hade krävt rättning i nästan hälften av fallen.
- **Typ av ändring:** 11 % format (skriptstyrt), 88 % innehåll. Störst: övrigt innehåll 34 %, metatext 17 %, titel/SEO-titel 16 %, påståendeord 7 %, uppgift struken 6 %, lastgräns 2 %.
- **Det som inte går att mäta än:** vilka regler som förebygger mest (rättningar saknade regelkod; ändras för nya batcher efter Davids ja på S13), allvarlighet, tid och kostnad per produkt, och all effekt på trafik eller försäljning.
- **Vad en kund bör få i rapporten:** antal produkter per steg (inventerade, avvisade med skäl, skrivna, verifierade), andel godkända direkt per kategori, rättningar per regelkod och allvarlighet, spärrade produkter och skälen, öppna beslut. Allt utom de två sista finns i statusfilen och mätskripten; regelkod och allvarlighet kommer med nästa batcher.

## 5. Vad som varit svårast i praktiken (exempel)
1. **Åtkomst till butikerna.** Shopify-verktygets koppling delas mellan sessioner och pekar på en butik åt gången. `switch-shop` bröt BEST OF SPORTS-sessionen i sex av nio sessioner trots lärdomsposter. Sex butiker står stilla i fas 1 på publika data tills ägaren installerat en app per butik (Dev Dashboard, Allowed domains, miljövariabler) och lämnat myshopify-adresserna. Kundflödet måste göra detta till ett enda guidat steg per butik.
2. **Ägarens beslut är flaskhalsen, inte AI:n.** Profil, spärrar, ton, standardblock och språk kan bara ägaren besluta; sex profiler har TODO-fält. En kund behöver ett kort frågeformulär, inte en dialog.
3. **Regelverkskänsliga sortiment.** Happy Parent (barn: CE och säkerhet nämns i ca 210 texter), HYPR (kosttillskott med hälsopåståenden, fel bolags köpvillkor) och Alpha Zoo (foder) kan inte köras som vanliga butiker. Systemet behöver en uttrycklig spärr och en kunnig granskare, inte bara bättre texter.
4. **Fel antaganden om butiken.** Workout Brands antogs vara träning men säljer streetwear; Mondido och To The Moon visade sig inte vara butiker (Mondido är enligt publik sida en betaltjänst). Inventering mot live-sortimentet kommer före profilen.
5. **Publika data räcker inte.** Status, SEO-fält och översättningar kräver admin; Search Console, GA4 och Ads var inte anslutna i någon ny butik, och Ahrefs-planen saknar API. Utan sökdata går åtgärderna inte att prioritera efter trafik.
6. **Skrivning för hand fungerar inte i skala.** Inklistrade mutationer gav osynliga tecken och tappade meningar (LARDOMAR 2026-11-03 och 2026-11-04); skript mot API med före-fil och återläsning tog bort felen.
7. **Samordning mellan sessioner.** Dubbelarbete (B You gjordes två gånger), tre oberoende versionsnummer i regelboken och fem grenar som gav samma filnamn åt olika filer. Kräver en samordnare som äger versioner och namn.

## 6. Minsta körbara kundflöde (förslag, ej byggt)
1. Ägaren installerar appen och lämnar butikens adress (guidat steg, ingen nyckel i chatt).
2. Inventering via API (inklusive utkast och arkiverade) och kontroll av inriktning mot sortimentet.
3. Profil ur `butiksprofil-MALL.json`, ifylld av ägaren; spärrlista med skäl; ägaren godkänner.
4. Kanariebatch om 3 produkter, återläsning, därefter batcher med granskning och stickprov.
5. Kvalitetsrapport per batch och per kategori; lättad granskning bara för kategorier som uppfyller mätbara villkor.
Delar som redan finns i repot: regelbok (`regler-v1.md`), mallprofil, kontrollskript, statusfil, mätskript, skrivrutin. Delar som saknas: guidat åtkomststeg, kundvänd rapport, kostnadsmätning, flerspråkig granskning.

## 7. Ägande och IP (flaggat, ej utrett)
- **Ecomduct:** hur det hänger ihop med den här satsningen är obekräftat (i Davids andra repon är Ecomduct en systerprodukt som ägs av Axegren Invest AB och inte får slås ihop med KANPAJ:s kodbas). Fråga S2 väntar på David. Inga kodbaser har slagits ihop.
- **Vem äger vad:** regelboken, mallarna och skripten byggs i det här repot för flera bolag (HYPR Sthlm AB är ett annat bolag än Gorilla Sports; kunddata och åtkomst ska hållas åtskilda). Innan något säljs behöver det avgöras vilket bolag som äger systemet, och om kunders produktdata får användas för att förbättra regler.
- **Juridik:** kvalitetsrapporten får inte ge intryck av att granska regelefterlevnad (CE, hälsopåståenden); den visar bara om texten följer butikens regler och källan.
