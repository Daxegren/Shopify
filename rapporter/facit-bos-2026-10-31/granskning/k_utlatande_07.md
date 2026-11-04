# Granskningsutlåtande k_07a, k_07b och k_07c (tillbehör, fitness och innerslangar), 2026-11-04

Granskare: Opus, bara läsning. Jag hämtade källan live via Admin API för alla 75 id: 35 utkast och 40 avvisade. Jag använde `hamta_produkter` och en variantfråga. Alla utkastprodukter är ACTIVE och har en variant. Regler: regelbok v1.6, BESLUTSLOGG, butiksprofilen, standarden (§12 och §16) och LARDOMAR. Ingenting skrevs till Shopify.

Domarna i maskinläsbar form finns i `vag2_skriv/k_utlatande_07.json`. Varje före-text träffar exakt en gång i sitt fält (kontrollerat i python). Jag tillämpade rättningarna på en kopia med de 27 som inte är underkända och körde `skrivfil_kontroll.py` på den. Resultat: 0 fel och 0 varningar. Leveranstidsmeningen finns på exakt de tre produkter som har taggen "På beställning" (9435, 9436, 9437). Inget utkast-id är redan skrivet.

**Summa: 35 utkast. 17 godkända, 10 att rätta och 8 underkända. Av de 40 avvisningarna är 38 motiverade och 2 för strikta (pedalerna 9443 och 9444).**

## Domar

| Nr | Id | Dom | Kort |
|---|---|---|---|
| 9402 | 10411711430922 | RÄTTA | "15 Lux" ändras till "15 lux" i titeln (R9) |
| 9403 | 10472237170954 | UNDERKÄND | Titeln säger 5 mm men källan 35 mm (R3). Tunn källa och ingen webbkälla. Metan har dessutom utfyllnad. |
| 9404 | 10475361206538 | UNDERKÄND | Samma produkt som 8056: stödben för 16–20 tum (stödben och barn) |
| 9410 | 10462230970634 | RÄTTA | Säkerhetslöftet om att husdjuret inte hoppar ur stryks (jfr 5088) |
| 9411 | 10462755356938 | RÄTTA | Samma löfte stryks i meta och html. Det var skälet till att 5088 underkändes. |
| 9412 | 10472224588042 | UNDERKÄND | Väska med lastgräns 2,5 kg (§12) |
| 9413 | 10472218034442 | UNDERKÄND | Samma som 5077: väska med lastgräns 5 kg (§12) |
| 9414 | 10472293957898 | GODKÄND | Litermåttet är rätt utelämnat (17 mot 17,5 l) |
| 9415 | 10472251392266 | UNDERKÄND | Samma som 5071: väska med lastgräns 5 kg (§12) |
| 9418 | 10472303067402 | UNDERKÄND | Reflexer skrivs inte i vågor (§12) |
| 9419 | 10472303788298 | UNDERKÄND | Reflexdekaler (§12, jfr 5087) |
| 9420 | 10471174832394 | UNDERKÄND | Reflexdekaler (§12) |
| 9421 | 10471266713866 | RÄTTA | Typordet ändras från "Elliptisk Tränare" till Crosstrainer, som för 10160–10175 och syskonet 9427 |
| 9422 | 10472308867338 | GODKÄND | Allt finns i källan |
| 9423 | 10472283308298 | RÄTTA | "Maximal driftsvikt 120 kg" stryks i specifikationen och i Passar för (R4, alt A) |
| 9424 | 10480052207882 | GODKÄND | Allt finns i källan |
| 9425 | 10472311226634 | GODKÄND | Allt finns i källan |
| 9426 | 10572603130122 | GODKÄND | Allt finns i källan. Produkten hör till fitness i faktatextläge. |
| 9427 | 10472308900106 | GODKÄND | Allt finns i källan, och typordet följer källtexten |
| 9431 | 10472186380554 | GODKÄND | ETRTO-listan stämmer med titeln. De motsägande raderna är utelämnade. |
| 9432 | 10472237859082 | GODKÄND | Allt finns i källan |
| 9435 | 10472277737738 | RÄTTA | "760 W" stryks, eftersom källan också anger 690 W. Uppgiften 24–29 tum har stöd på tillverkarens sida. |
| 9436 | 10472350155018 | RÄTTA | Erbjudandet om gratis prenumeration stryks (det är ett löfte) |
| 9437 | 10472277639434 | GODKÄND | Allt finns i källan |
| 9438 | 10530129051914 | GODKÄND | Allt finns i källan. Tvillingen 9441 är avvisad. |
| 9442 | 10470892798218 | GODKÄND | Tunn källa, men den har två fakta |
| 9448 | 10636704252170 | GODKÄND | Allt finns i källan |
| 9449 | 10636703858954 | GODKÄND | Allt finns i källan |
| 9450 | 10636704055562 | GODKÄND | Allt finns i källan |
| 9455 | 10487987765514 | RÄTTA | Lastuppgiften 8 kg per sida stryks. Den står i löptexten utan etikett (R4). |
| 9456 | 10487987798282 | RÄTTA | Samma som 9455. Typordet Stänkskärmset godtas. |
| 9462 | 10548250575114 | RÄTTA | "Fullt servicebar" stod två gånger, och specifikationsraden stryks (R5) |
| 9463 | 10472285765898 | GODKÄND | Allt finns i källan |
| 9465 | 10507438948618 | GODKÄND | Allt finns i källan |
| 9470 | 10472254341386 | GODKÄND | Allt finns i källan |

## Kontroller som koordinatorn bad om

- **9423, "Maximal driftsvikt 120 kg".** Raden stryks. Regelboken (R4) räknar uttryckligen upp "driftsvikt" bland de ord som aldrig tolkas. Ordet är också översättningen av "Maximum operating weight", alltså samma fall som 10100 och alt A. Både specifikationsraden och Passar för-punkten tas bort.
- **9421, typord.** Det blir Crosstrainer. Alla tidigare "Elliptisk träningscykel" och "Elliptisk tränare" (10160–10175, bland annat 10172) har blivit Crosstrainer. Stödet är produkttypen Crosstrainers och taggen Crosstrainer, och syskonet CT 6 (9427) heter Crosstrainer.
- **9414, 17,5 mot 17 liter.** Det är rätt att utelämna litermåttet. Webbkällan gäller MIK-varianten och inte säkert artikelnumret 21110B. Varken titeln eller texten nämner någon volym.
- **9403, 35 mm mot 5 mm.** Underkänd. Titeln och källan motsäger varandra (R3). Webbsökning på Azimut BELL53 gav ingen tillverkarsida (v1.6). Det enda fakta som återstår är 35 mm och "liten".
- **9404, 16–20 tum.** Underkänd. Det är samma id som 8056, som redan är underkänd: ett stödben (taggen stödben) i barncykelstorlek. Batchen avvisar själv alla andra stödben, så 9404 måste behandlas på samma sätt.
- **9431 och 9432, innerslangar.** Båda godkänns. Titeln anger ETRTO, vilket §12 tillåter.
  - 9431: källans ETRTO-lista (47-559 till 62-559) stämmer med titelns 47/62-559. De rader som underkände 5006 (1,75 tum och 26x1.375) är nu utelämnade.
  - 9432: bredden 1,75–2,5 tum stämmer med 47/62.
- **9426, 9427, 9435 och 9436 (elektronik).** Alla fyra ingår i faktatextläget.
  - Profilen tar med motionscyklar i fitnessgruppen. Inget beslut undantar elektronik; §16.4 gäller bara elcyklar.
  - Cykelträningsställen har taggen Konditionsträning & Fitness och finns inte bland det som står utanför tills vidare.
  - David kan bekräfta att cykelträningsställ ska räknas till fitness. Det är en observation och inget hinder.
- **9435, maskinöversatt "kompatibla med pedalen".** Den entydiga delen är 24–29 tum. Den bekräftas av tillverkarens sida https://www.elite-it.com/en/home-trainers/classic-trainers/novo-force, där det står hjul från 24 till 29 tum. Effekten "upp till 760 W" motsäger källans "(690 W)", och Elites egna dokument anger 690 W vid 40 km/h. Effekten stryks därför (R2).
- **9455 och 9456, Hebie Alumee, "8 kg på varje sida".** Uppgiften stryks. Det är en lastgräns i löptext utan etikett (R4).
  - När uppgiften är borta nämner texten inga väskfästen och antyder ingen last.
  - Underkännandet av 5257 och 5258 i b_9 byggde på att produkten skulle lyftas till David i stället för att uppgiften togs bort. R4 v1.4 gör nu strykning till regeln.
  - Om David ser väskfästena på den bakre skärmen som en bärande funktion ska produkterna i stället hållas.
- **9456, typord.** "Stänkskärmset" godtas, fast live-titeln säger Stänkskärmsset. Det är samma ord i en annan stavning. Butikens skrivna Hebie-serie (Taipan, Viper, Swap Set) har genomgående Stänkskärmset.
- **Avvisade stödben och dragkroksställ.** Avvisningarna är motiverade.
  - Stödben bär cykelns vikt. Det gäller 9453, 9457 och 9458, 9459 med 25 kg, 9460, 9461 med 40 kg och 9466, liksom KSA-stöden 9445 och 9446. Linjen har hållits sedan 5003, 5010, 8052 och 8056.
  - Peruzzo Parma och Siena (9467 och 9468) hänger på bilens dragkrok med 60 kg last och typgodkännande, och källan har trasiga rader. De är bärande och säkerhetskritiska.

## Avvisningar

- **38 av 40 är motiverade.**
  - Dubbletterna 9406–9409 är redan skrivna (10070, 10079, 10080 och 10088 finns i f_skriv_3 och f_skriv_4).
  - Slangarna 9428–9430, 9433 och 9434 har motsägande mått, som tidigare.
  - 9441 är tvilling till 9438.
  - Barnprodukter: 9447, 9454, 9471 och 9472.
  - Tunna källor: 9401, 9405, 9439, 9440, 9451, 9452, 9464, 9469 och 9474.
  - Varianter som inte kan kopplas till titeln: 9416 och 9417.
  - Bromsadapter: 9473.
  - Motsägande antal växlar: 9475.
- **För strikta: 9443 och 9444 (pedaler Giant Combo Touring och Pinner Elite).** Pedaler skrivs sedan k_02c (9165 och 9166 är godkända och skrivna), och k_07c skriver tre pedaler (9462, 9463 och 9465). Underkännandena 5267 och 5273 kommer från den äldre b-omgången. Båda bör tas med i nästa utkastbatch och prövas på innehållet.

## Observationer till koordinatorn

- **Beslut för David: väskor och korgar med lastgräns.** Det gäller 9412, 9413 och 9415, och tidigare 5038, 5071 och 5077. Enligt §12 skrivs de inte. Men §16.3 och R4 tillåter en svensk etiketterad lastgräns en gång som "enligt tillverkaren". Ett ja från David släpper alla sex.
- **Reflexer (§12).** Utkastaren tog med 9418–9420, fast reflexer bara skrivs med Davids ja per produkt. Det kan bli ett test i skriptet: taggen "reflex" eller typordet Reflex/Reflexklistermärken.
- **Maxvikt i Passar för.** I 9421, 9422, 9424 och 9425 står maxvikten både i specifikationen ("enligt tillverkaren") och i en Passar för-punkt. R4 säger "en gång", men samma mönster finns i 135 redan skrivna fitnesstexter. Jag har därför inte rättat det. David eller koordinatorn bör avgöra om R4 ska tillämpas så strikt. Gör den det behövs ett skripttest och en revision.
- **Utkastarens anteckning om Hebie.** Utkastaren skriver att 5257 och 5258 underkändes "när den togs bort". Det stämmer bara delvis: skälet var att produkten skulle lyftas.

Källor (webb): https://www.elite-it.com/en/home-trainers/classic-trainers/novo-force och https://api.elite-it.com/assets/documents/NOVO-FORCE_DE.pdf (690 W vid 40 km/h, enligt sökträffen).
