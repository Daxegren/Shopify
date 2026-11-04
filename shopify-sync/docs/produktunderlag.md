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
