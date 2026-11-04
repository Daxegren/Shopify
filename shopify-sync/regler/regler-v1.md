# Regelbok v1.2 – produkttexter (butiksoberoende)

Version 1.2, 2026-11-04 (v1.1 och v1.2 efter återkoppling från utkastare och granskare i g_3: R2, R3, R4, R5, R6, R7 förtydligade). Max ~60 rader; blir den längre har vi gjort fel. Varje regel har en kod: **T** = kontrolleras av skript (`shopify-sync/scripts/skrivfil_kontroll.py`), **G** = granskare, **M** = mänskligt beslut. Butiksspecifikt (märken, spärrar, standardblock, taggar) står i butikens profil (`shopify-sync/config/butiksprofil-*.json`) och i `shopify-sync/docs/BESLUTSLOGG.md`. Nytt granskningsfynd = ny regel här eller ett nytt test i skriptet, aldrig bara en lärdomspost.

## Källa och påståenden
- R1 (G) Bara uppgifter som står entydigt i produktens EGEN live-källa. Aldrig från syskonprodukt eller minne.
- R2 (G) Motsägelse, trasig eller maskinöversatt rad → utelämna. Gissa aldrig. En entydig del av en annars trasig rad får användas. Estniska/finska ord: översätt bara om du är säker.
- R3 (G) Titeln anger en variant (färg/vikt/storlek) men produkten har flera varianter med olika pris, eller källan stämmer inte med titeln → avvisa med skäl. Vår egen tidigare text räknas inte som källa; bara leverantörens originaltext. Tunn källa: minst två entydiga fakta utöver titeln, annars avvisa eller kort meta enligt standard §14.
- R4 (T/G) Lastgräns/maxvikt: svensk ordagrann uppgift med enhet och etikett → en gång som "enligt tillverkaren". Engelsk, maskinöversatt, oklar → utelämna helt. Tolka aldrig ("Load range", "nivåer", "driftsvikt"). Lastgräns i löptext utan etikett ("klarar upp till 350 kg", "sprängsäker") → utelämna.
- R5 (G) "Enligt tillverkaren": en gång per påstående, högst två per text. Inga säkerhets-, hälso-, stabilitets-, träningseffekt-, rehab-, ursprungs- eller kvalitetsord (slitstark, robust, halkfri, halkskydd) om det inte står ordagrant i källan; då "enligt tillverkaren".
- R6 (M) Kategorier som står under `utanfor_tills_vidare` i profilen (akupressur, massagepistoler, vibrationsplattor, kroppsanalysvågar, barn, kosttillskott m.fl.) avvisas tills ägaren beslutat. Profilen är facit; äldre prompter som säger emot gäller inte.

## Språk och format
- R7 (G) Typordet först i titel och SEO-titel, enhetligt i batchen. Byt typord bara om produktens egen källtext använder det nya ordet. Saknar källan svenskt ord (engelsk eller estnisk live-titel): använd butikens godkända typord (profilen, `godkanda_typord`) eller behåll titelns ord; hitta inte på.
- R8 (T) Märket med stor första bokstav och resten gemener ("Hammer", "BH Fitness"), aldrig versaler.
- R9 (T) Stor bokstav efter kolon i specifikationsrader; stora bokstäver på beskrivande ord i titel/SEO-titel; enheter (cm, mm, kg, g, tum) med liten bokstav.
- R10 (T/G) "N-tums skärm" i löptext, inte "N tum skärm". Skriv "och", aldrig "&".
- R11 (G) Första meningen har verb och är inte cirkulär ("X är en X"). Inga arbetstermer i kundtext ("här kallad", "enligt källan").
- R12 (T) Titel ≤70 tecken och ≤2 kommatecken; SEO-titel ≤43 (märket kvar om det ryms, behåll småord som "till"); meta 70–155 utan utfyllnad; titel, SEO och meta unika.
- R13 (T) Standardblocket exakt som i profilen. Leveranstidsmeningen bara på produkter med taggen "På beställning". seo skickas alltid med både title och description.

## Process
- R14 (T) Spärrlistan och beslutsloggen läses före varje batch; spärrade produkter får inte hamna i en skrivfil.
- R15 (G) "Lika titel" bevisar inte att texten är skriven: jämför titel, seo och beskrivning. Gammal FAQ/"Om märket" ersätts helt.
- R16 (M) Skriv via skript (API, eller json.dumps ensure_ascii vid MCP), högst 5 produkter per anrop, återläs högst 4, jämför tecken för tecken i python. Aldrig text för hand.
- R17 (G) Före-filen sparas komplett före skrivning (id-antal och teckenlängd mot live). Notera bildblock som försvinner.
- R18 (T) Taggen texter-klara sist, först efter verifierad återläsning. Butikens egna taggar (Velomarket, Gymstick m.fl.) rörs aldrig.
- R19 (G) Sonnet-stickprov på minst 10 produkter eller 20 procent per grupp, bara läsning.

## Att automatisera härnäst (de vanligaste fynden som ännu är G)
Cirkulära inledningar (R11), meta utan verb, typord som byts utan stöd i källan (R7), "enligt tillverkaren" på alla lastgränser (R4).
