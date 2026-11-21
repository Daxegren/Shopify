# Regelförslag för barn- och föräldraprodukter (Happy Parent) – FÖR DAVIDS BESLUT

Skapad 2026-11-04. **Förslag, inte gällande regler.** Läggs som tillägg till `regler-v1.md` (R1–R19) först när David godkänt. Koder: T = skript, G = granskare, M = mänskligt beslut. Bakgrund: i BEST OF SPORTS ligger barn under `utanfor_tills_vidare`; i Happy Parent är barn hela sortimentet, så en särskild uppsättning behövs. Den skarpa risken är att en text ger ett säkerhets-, ålders- eller standardlöfte som butiken inte kan styrka. Inte juridisk rådgivning: B3 och B4 bör ses av någon med kunskap om leksakssäkerhet (EU:s leksaksregler, CE-märkning, EN 71) innan de beslutas.

## Säkerhet och standarder
- B1 (G/T) **Inget säkerhetslöfte som egen slutsats.** Ord som "säker", "helt säker", "trygg", "ofarlig", "barnsäker", "giftfri", "testad", "godkänd" får bara stå om produktens egen leverantörskälla säger det ordagrant, och då som "enligt tillverkaren". Idag finns det på minst 41 produkter ("helt säker för ditt barn att bita på").
- B2 (T/G) **Material** (BPA-fri, ftalatfri, silikon, ekologisk bomull) får anges bara ordagrant ur källan, med "enligt tillverkaren". "Organic/ekologisk" kräver att källan anger certifiering (t.ex. GOTS); annars utelämna.
- B3 (M) **CE-märkning och standarder (EN 71, CCC m.fl.).** Förslag: texten får nämna CE bara om (a) leverantörens egen källa anger det och (b) David bekräftat att leverantörens försäkran om överensstämmelse finns arkiverad för produkten. Annars tas påståendet bort ur nya texter. Aldrig "CE-märkt" som egen slutsats; aldrig EN-nummer som inte står i källan. Idag nämner ca 210 produkter CE eller certifiering och ingen nämner EN 71. CCC-certifikat (kinesiskt) är inte ett europeiskt säkerhetsbevis och ska inte lyftas fram.
- B4 (M) **Ansvarig aktör.** För varje varumärke ska det vara känt vem som är tillverkare/importör. För etiketten "Happy Parent" (367 produkter) avgör det vem som bär ansvaret för CE och märkning. David anger det; ingen produkttext skrivs om säkerhet innan det är känt.

## Ålder
- B5 (T/G) **Åldersuppgift** (t.ex. "0–12 månader", "3+") får skrivas bara om den står entydigt i produktens egen källa, och alltid med tillverkarens ordalydelse. Gissa aldrig ålder från titel, tagg ("2 år") eller syskonprodukt. Taggarna `0 år`–`6 år` är butikens egna sorteringstaggar, inte en säkerhetsuppgift.
- B6 (T) **Varning för små delar** ("Innehåller små delar: ej lämplig för barn under 3 år") ska bevaras om den finns i källan, och får aldrig strykas av en omskrivning. Saknas åldersgräns men produkten har små delar eller batterier: markera som spärrad, skriv inte.
- B7 (G) Motsägelse mellan ålder i titel, tagg och beskrivning → avvisa med skäl (R2).

## Tillsyn, sömn och hälsa
- B8 (T/G) **Batterier, knappceller och magneter** (83 produkter nämner batteri): batterityp, att batterier ingår/inte ingår och varningar får återges bara ur källan. Inga ord om att produkten är "trygg" med batterier.
- B9 (M) **Spädbarns sömn och position** (sovkuddar, babynest, nackkuddar, babymobil över spjälsäng, filtar): produkterna är spärrade tills David beslutat. Inga påståenden om sömnkvalitet, att barnet "kommer till ro" eller om lutande läge. Exempel idag: en sovkudde med påståendet att den "förebygger halsbränna".
- B10 (T/G) **Hälso- och utvecklingspåståenden.** Förbjudna utan ordagrann källa och "enligt tillverkaren": lindra tandning/kolik, förebygga, behandla, underlätta matsmältning, antibakteriell, allergivänlig. Utvecklingsord ("tränar finmotorik", "främjar inlärning", "stimulerar hjärnan", "Montessori") beskrivs som vad leksaken *innehåller eller gör* (t.ex. "pusslet har 9 bitar med siffror"), inte som effekt på barnet. Idag nämner ca 250 produkter motorik/utveckling och 153 Montessori/pedagogisk.
- B11 (M) **Tillsynsersättande produkter** (lekhage, barnstol, gåstol, skyddsbälte, hjälm): spärrade. Ingen text får antyda att barnet kan lämnas utan tillsyn. Om de skrivs sker det i faktatextläge med tillverkarens varningar ordagrant.

## Format
- B12 (G) **Faktatextläge är standard** för hela sortimentet (standard §16): bara uppgifter ur produktens egen källa, inga "perfekt present", "trygg", "hållbar", "slitstark", "mjuk som" utan "enligt tillverkaren". Kläder får beskrivas med material och passform ur källan; "ekologisk", "OEKO-TEX" följer B2.

## Hantering av "enligt tillverkaren" (utöver R5)
Högst två per text gäller inte för B1–B3: varje säkerhets-, material- eller standardpåstående får sin egen markering. Hellre färre påståenden än ett obelagt.

## Vad som kan automatiseras (T) när David godkänt
Skriptet `skrivfil_kontroll.py` kan få en lista över förbjudna ord (B1, B10), kräva "enligt tillverkaren" intill CE/BPA/giftfri, stoppa EN-nummer och åldersuppgifter som saknas i en källfil, och stoppa produkter i spärrlistan. Mätning: andel utkast med noll träffar mot B1–B11.
