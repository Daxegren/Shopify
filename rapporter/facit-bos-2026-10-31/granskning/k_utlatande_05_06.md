# Granskningsutlåtande k_05a (sparkcyklar) och k_06a (lås och Gorilla-viktlås/hantelstänger), 2026-11-04

Granskare: Opus, bara läsning. Källan hämtades live via Admin API (`hamta_produkter` och varianter) för alla 37 id i `k_05a_in.json` och `k_06a_in.json`. Jag hämtade också den redan skrivna 10475621089546 (AXA Fold 85) och sökte i butiken på titel (Absolute, Foldable 1000, SOKE GO, Cosmopolitan, Erawan, Credit, Stronghold, Inigma, Curlstång, Easy Click, Fjäderlås, Stjärnlås, Hantelstång, Tricepsstång, Jaw). Inga id finns i spärrlistan eller i `fitness_hallna_spar.json`. Ingenting skrevs till Shopify.

Domarna i maskinläsbar form finns i `vag2_skriv/k_utlatande_05_06.json`. Varje före-text träffar exakt en gång i sitt fält. Rättningarna har tillämpats på en kopia, och `skrivfil_kontroll.py` gav 0 fel och 0 varningar.

**Summa: 29 utkast. 17 godkända, 9 att rätta och 3 underkända (9334, 9335, 9338). Alla 8 avvisningar är motiverade.**

## Domar

| Nr | Id | Dom | Kort |
|---|---|---|---|
| 9324 | 10515741180170 | RÄTTA | Hjulmåttet 100 x 24 mm stryks i specifikation och meta, eftersom enheten mm inte står i källan och ingen webbadress anges. Etiketten "Maximal ryttarbelastning" ändras till "Maximal belastning". |
| 9325 | 10470927958282 | RÄTTA | Samma som 9324. |
| 9326 | 10472263975178 | RÄTTA | Samma som 9324. Här ändras etiketten "Maximal förarkapacitet" till "Maximal belastning". |
| 9332 | 10572664897802 | GODKÄND | Allt finns i källan. Texten har två "enligt tillverkaren", vilket är tillåtet. Ingen dubblett: den skrivna Erawan är svart/neochrome. |
| 9333 | 10676720271626 | GODKÄND | Diameter 100 mm, 223 g, lila och "Pris per: 1 hjul" står i källan. Ingen dubblett. |
| 9334 | 10411902402826 | UNDERKÄND | Källan anger åkarlängd 130–145 cm, vilket är barn- eller juniorstorlek. R6, samma bedömning som Union Lite (9330/9331). |
| 9335 | 10486673473802 | UNDERKÄND | Samma skäl som 9334. |
| 9337 | 10472295760138 | GODKÄND | Webbkällan är tillverkarens egen sida och gäller exakt modellen 7-150. Den belägger 150 cm, härdat stål och nivå 9 (se nedan). |
| 9338 | 10494706254090 | UNDERKÄND | Dubblett (R12a). AXA Fold 85 är redan skriven och aktiv som 10475621089546, till samma pris 1 519 kr. SKU skiljer bara på SB/KB, och ingen färg anges. Samma produkt avvisades i b_38 (8672). |
| 9339 | 10494705041674 | RÄTTA | "Gångjärnsdiameter" är maskinöversatt och ändras till "Diameter", som för 8693. |
| 9340 | 10636678693130 | GODKÄND | 180 kg står lika i löptext och i en svensk etiketterad rad. Ordet "Stjärnlås" i live-titeln är rätt utelämnat. |
| 9341 | 10636632162570 | GODKÄND | Märket 2M Solutions är belagt i källan. SKU:n motsvarar tillverkarens artikel 2M-EC111SCH. Det finns tre varianter till samma pris. |
| 9342 | 10636741181706 | RÄTTA | Stängerna har enligt källan diameter 30 mm, och det rättas i inledning och meta. 31 mm är låsets mått. Specifikationsraden "30/31 mm" följer titeln och får stå. |
| 9343 | 10636739051786 | GODKÄND | Tunn källa, men den har tre fakta utöver titeln. |
| 9344 | 10636678332682 | GODKÄND | Allt finns i källan. 100 kg står i en svensk etiketterad rad. |
| 9345 | 10636756091146 | GODKÄND | Lastgränsen är rätt utelämnad. Tabellen anger 100 kg, men löptexten rekommenderar högst 2,5 kg viktskivor. Det är två olika lastvärden (R4 v1.5). |
| 9346 | 10636756451594 | GODKÄND | Allt finns i källan. 100 kg står lika i löptext och tabell. |
| 9347 | 10636755894538 | GODKÄND | Allt finns i källan. |
| 9348 | 10636687048970 | GODKÄND | Allt finns i källan. Den oklara vikten är rätt utelämnad. |
| 9349 | 10636686885130 | RÄTTA | Att handtaget är räfflat står bara hos syskonprodukterna (R1). Uppgiften stryks i inledningen. |
| 9350 | 10636661817610 | GODKÄND | Allt finns i källan. |
| 9351 | 10636648907018 | RÄTTA | Produkten är ett par, och källan säger inte om "Maximal belastning: 100kg" gäller per stång eller för paret. Raden stryks (R4). |
| 9352 | 10636711854346 | GODKÄND | Allt finns i källan. Krom och svart är två varianter till samma pris. |
| 9353 | 10636756746506 | GODKÄND | 200 kg står lika i löptext och tabell. |
| 9354 | 10636757467402 | GODKÄND | 200 kg står lika i löptext och tabell. |
| 9355 | 10636696224010 | GODKÄND | Fem varianter till 479 kr. Allt finns i källan. |
| 9356 | 10636727189770 | GODKÄND | Allt finns i källan. Säkerhetspåståendena är rätt utelämnade. |
| 9359 | 10541205291274 | RÄTTA | Typordet "Vikbart lås" godtas, eftersom tillverkarens sida belägger det (se nedan). Säkerhetsklassningen står både i meta och i specifikationen och stryks i metan, som för 8696. |
| 9360 | 10548236058890 | RÄTTA | Typordet "Vikbart lås" godtas (se nedan). Raden "Certifiering: BSI Kitemark" stryks, eftersom den certifieringen gäller appen och inte låset. |

## Kontroller som koordinatorn bad om

- **Lastgränser (R4).** Varje lastgräns står en gång, med etikett och "enligt tillverkaren". Ingen meta upprepar en lastgräns.
  - 9345 är rätt utelämnad, eftersom tabellen och löptexten anger olika värden.
  - 9351 stryks, eftersom det är oklart om 100 kg gäller per stång eller för paret.
  - 9348 och 9349 anger "per stång" och "vardera" som källan, och de står kvar.
  - SOKE-etiketterna är maskinöversatta och normaliseras till "Maximal belastning", som i k_02e.
- **Viktlåsens mått.** 9342 stämmer med källan (löptexten säger 30 mm stång, tabellen 31 mm). Avvisningen av 9357 är motiverad. Där står 30 mm bara i titeln och källan anger "Diamteter på 31mm". Att skriva 31 mm utan att det är håldiametern skulle vilseleda.
- **9337 AXA Absolute 7-150.** Jag läste https://axabikesecurity.com/product/axa-absolute-7-150/. Där står "Length 150 cm", "The 7 mm thick hardened steel links", "Safety level 9" och "2 symmetrical keys". Det är tillverkarens egen sida, och den gäller exakt modellen. Butikens skala "9/14" är rätt utelämnad.
- **9359 Squire Stronghold FL/850.** squirelocks.co.uk omdirigerar till squirebikelocks.com, så det är tillverkarens egen sida. Den kallar modellen "High-Security Folding Bike Lock" och anger bredd 24 mm, 2,18 kg och borstål. Butikens egen källa är tvetydig (Bygelås mot hänglås), och enligt v1.6 och beslutsloggen 2026-11-04 får webbkällan då avgöra typordet. Det ersätter underkännandet av 8685.
- **9360 Squire Inigma FL1.** Tillverkarens produktsida heter "Inigma™ FL1 Folding Lock" (https://squirelocks.co.uk/products/inigmafl1, enligt sökträffen). Sidan svarar nu 404, och utkastets adress …/shop/inigma-fl1.html är fel. Återförsäljare anger "smartphone operated folding lock – 800mm". Typordet godtas, men belägget är en sökträff och inte en läst sida. David kan vilja bekräfta det.
- **"Kicksparkcykel" (9334).** Det är live-titelns ord, och enligt R7 behåller varje syskonprodukt sitt eget ord. Det hade fått stå, men produkten underkänns på grund av åkarlängden.
- **Versatyl 130–145 cm.** Det är juniorstorlek. Därför underkänns både 9334 och 9335, i linje med 9330 och 9331. Släpper David juniormodeller kan utkasten skrivas. 9334 behöver då SEO-titeln "Kicksparkcykel Versatyl Cosmopolitan V2 Pro" (43 tecken). Den behåller märket före färgen, som 9211.
- **SOKE i versaler och "GO" utan utropstecken.** De behålls, i linje med cirka 20 skrivna SOKE-texter. Frågan om "SOKE" eller "Soke" är redan lyft till David i k_02e. SOKE GO säger "unga" och anger ingen förarlängd, så R6 gäller inte.
- **mm-enheten i 9324–9326.** Den är inte belagd, och ingen webbadress anges. Måttet stryks i specifikation och meta.

## Avvisade (8): alla avvisningar är motiverade

- **9327 SOKE PRO.** Live har två varianter med olika pris (3 369 och 2 319 kr), och källan anger ingen färg (R3). Påståendet om dubblettrisk mot 9020 har jag inte prövat, och det påverkar inte domen.
- **9328 och 9329 START Easy HF Quick Kick.** Det är skidgreppvalla med svamp (60 ml, temperaturintervall), inte en sparkcykel. Källan är maskinöversatt och motsägelsefull (R2, R3).
- **9330 Union Lite M och 9331 Union Lite S.** Användarlängden är 110–130 och 105–125 cm, alltså barnstorlek (R6).
- **9336 Versatyl S2S.** Titeln säger "Krom/Svart" men källan "svart-grå" (R3). Källan nämner dessutom ett säte i aluminium.
- **9357 PRO Jawlock 30 mm.** Se ovan.
- **9358 Shimano SM-RT10.** Det är en bromsskiva och inte ett lås. Källan anger två ytterdiametrar, 180 och 160 mm, mot titelns 180 mm (R3).

## Observationer till koordinatorn

- På 9341 säger `att_bekrafta` "ingen märkesangivelse", fast specifikationen har "Märke: 2M Solutions". Märket är belagt, så det är bara anteckningen som är fel. Utkastarens standardrad om Gorilla-märket har kopierats även där den inte passar.
- På 9335 säger `att_bekrafta` att "Kicksparkcykel" är behållet. Raden är kopierad från 9334 och publiceras inte.
- Fler SOKE GO-färger ligger kvar oskrivna i butiken (blå-gul aktiv, Svart/Turkos/Oövervinnerlig som utkast). Det finns också Versatyl Cosmopolitan Blå/Svart som utkast och Union Credit-hjul 110 mm. Inget av dem är en dubblett av den här batchen.
