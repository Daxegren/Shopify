# Taggningslista att granska (2026-11-17)

Inget är taggat. Listan bygger på `brodsmula-sim/forslag-taggar.csv` (557 produkter, titelmatch mot kollektionernas taggregler) och är sorterad i två nivåer.

- **Nivå A (460 produkter):** taggordet är titelns huvudord och kollektionen är specifik. Förslag: granska ett stickprov per kollektion och godkänn per kollektion.
- **Nivå B (97 produkter):** bred kollektion (balans, sportutrustning, boxning, skidor), tillbehör ("för/till/med" före taggordet) eller osäker placering. Förslag: granskas rad för rad eller utelämnas.

Regler vid körning: bara `tagsAdd` med den angivna taggen (aldrig `tagsRemove`, aldrig `price-change-job-active`), säkerhetskopia av produktens taggar först, kanarie (en kollektion, 3 produkter), återläsning av taggar och kollektionsmedlemskap (`inCollection`), kontroll att pris inte ändrats, stopp vid första avvikelse. Ångra: `tagsRemove` med samma tagg på samma produkter (lista i CSV).

## Per kollektion (nivå A / nivå B)
| Kollektion | A | B | Exempel (A) |
|---|---|---|---|
| `hopfallbara-cyklar` | 90 | 17 | Cykel Tabou Venom Lite, Blå-Svart; Cykel Tabou Venom Lite, Storlek M, Röd-Svart |
| `barncyklar` | 63 | 1 | Barncykel GIANT STP 24 (2026) Svart Krom; Barncykel Kona Hula, Satin Metallic Mauve |
| `viktskivor` | 23 | 8 | Viktskivor Gymstick Vinyl, 2 x 10 kg; Curlstång IRON med Åtta Viktskivor och Stjärnlås |
| `hantlar` | 23 | 3 | Hantlar Tunturi Neoprene 2 x 0,5 kg, Rosa; Hantelstång 2x35 cm med Fjäderlås, 30 mm |
| `foam-roller-massageboll` | 25 | 0 | Foamroller Gymstick Active Compact, 30 cm; Massageboll Gymstick Active Mini |
| `cykelhjalmar` | 24 | 0 | Cykelhjälm Giant Relay MIPS, S/M 49–57 cm, Gloss White; Cykelhjälm Melon Brightest med Magnetfäste |
| `flaskhallare` | 19 | 3 | Flaskhållare Giant Airway Composite, Svart och Blå; Flaskhållare Giant Airway Composite, Svart, Orange och Rosa |
| `traningsboll` | 21 | 0 | Träningsboll Gymstick Active, 65 cm; Träningsboll Gymstick Active, 75 cm |
| `traningsbank` | 21 | 0 | Träningsbänk BH Fitness Weight Bench; Träningsbänk Tunturi UB40 Utility Bench, Justerbar |
| `skidor` | 0 | 17 | - |
| `skivstang` | 9 | 6 | Skivstång och Hantelset, 23 kg; Skivstångshållare Gymstick Alpha J-Cup, Par |
| `traningsmatta` | 13 | 1 | Träningsmatta Gymstick Aktiv, 2-toners, Blå och Svart; Träningsmatta Gymstick Aktiv |
| `balans` | 0 | 13 | - |
| `hybridcykel` | 10 | 0 | Hybridcykel Romet Orkan 1 M, Svart och Grön; Hybridcykel Romet Orkan 1 M, Svart och Röd |
| `sportutrustning` | 0 | 9 | - |
| `motionscykel` | 9 | 0 | Motionscykel Gymstick Crank Bike X4; Liggande Motionscykel BH Fitness i.TFR MED med Ryggstöd |
| `cykelbelysning` | 9 | 0 | Cykellampa AXA Classic Batteri, silver; Cykellampa AXA Nox Sport, 12 Lux, med Batterier |
| `fot-handledsvikt` | 7 | 0 | Ankel- och Handledsvikter Gymstick Aktiv, 2 x 1 kg; Ankel- och Handledsvikter Gymstick, 2 x 1 kg |
| `boxning` | 0 | 7 | - |
| `stodben-stodhjul-cykel` | 7 | 0 | Cykelstöd Azimut, Justerbart, 20–29 tum; Cykelstöd Ursus King R78 för bakgaffel, 24–28 tum |
| `pedaler-cykel` | 7 | 0 | Pedaler Giant Pinner Elite, Blå; Pedaler Kona Wah Wah 2 Alloy, Blå |
| `gummiband` | 5 | 1 | Motståndsband Gymstick Active Mini, Set om 2; Motståndsband Gymstick Active Workout, Set om 3 |
| `stankskarmar-cykel` | 6 | 0 | Stänkskärmar SKS Speedrocker för 27,5–28 tum; Stänkskärmar Zefal No-Mud |
| `juniorcyklar` | 6 | 0 | Ungdomscykel Tabou Venom 1.0 W 27,5 tum, Mint-Vit; Ungdomscykel Liv STP 26, Eukalyptus |
| `gymgolv` | 5 | 0 | Golvskyddsmatta BH Fitness, 120 x 60 x 0,5 cm; Golvskyddsmatta BH Fitness, 200 x 90 x 0,5 cm |
| `multigymspaket` | 5 | 0 | Multigym BH Fitness Plus, Svart; Multigym Hammer Ferrum TX2 |
| `vibrationsplatts` | 5 | 0 | Vibrationsplatta Christopeit Vibro 3000; Vibrationsplatta Tunturi Cardio Fit V10 |
| `skyddsutrustning-cykel` | 3 | 1 | Knäskydd Boom Basic, Rosa; Knäskydd Boom Solid Knee Pads Svart L |
| `studsmatta` | 4 | 0 | Trampolin Toorx, 97 cm; Trampolin Toorx Trampoline Pro 122 cm |
| `kabelmaskin` | 0 | 3 | - |
| `kettlebell` | 2 | 1 | Kettlebellgrepp, 30 mm, Krom; Kettlebellrack Gymstick, Svart, 60 x 120 x 75 cm |
| `cykelsadlar` | 2 | 1 | Sadelväska Basil Mada, 1–1,5 l; Sadel GIANT Grit SL, svart |
| `traningsmaskin` | 2 | 1 | Träningsmaskin BH Fitness Power Tower; Träningsmaskin Tunturi Platinum Lat Pulldown Selectorized V-Series |
| `smithmaskin` | 2 | 1 | Smithmaskin Tunturi SM60 Half Smith; Smithmaskin Tunturi SM70 Smith Machine |
| `bottenlager` | 3 | 0 | Växelreglage Shimano Rapidfire Plus SL-M2010-9R, 9 Växlar, Höger; Växelväljare Shimano SL-A050, Vänster, 2x7 |
| `elcyklar` | 0 | 2 | - |
| `yoga-pilates` | 1 | 1 | Pilatesring Tunturi, Glasfiber och Skum, Lila |
| `skivstangsset` | 2 | 0 | Skivstångspaket BASIC med Curlstång och Hantelstänger; Skivstångspaket IRON med Curlstång och Hantelstänger |
| `mountainbike` | 2 | 0 | Mountainbike Kona Cinder Cone, Gloss Bone; Mountainbike Romet Rambler R9.4, 29 tum, Grafit |
| `parallettes` | 2 | 0 | Parallettes Gymstick Hi-Rise; Premium Parallettes, Large |
| `mobilhallare-cykel` | 2 | 0 | Mobilhållare Toorx för Arm, Armband för Smartphone; Mobilhållare för Cykel SKS Compit Stem Mount |
| `funktionellt` | 2 | 0 | Plyobox Gymstick Soft 3-in-1; Trä Plyobox 50 x 45 x 40cm |
| `fasten-upphangningar` | 2 | 0 | Väggfäste Tunturi Battle Rope; Upphängning Boxningssäck Excalibur |
| `viktvast` | 2 | 0 | Viktväst Tunturi Weight Vest Pro 30 kg; Viktväst 2,5kg |
| `chins-dips` | 1 | 0 | Pull Up Bar för Ribbstol, Avtagbar, Plywood och Furu |
| `gravelcykel` | 1 | 0 | Gravelcykel Kona LBF, 29 tum, Smaragdgrön |
| `herrcyklar` | 1 | 0 | Herrcykel Romet Orkan 6 M, Silver |
| `traningsbalte` | 1 | 0 | Bälte Gymstick Dip Belt |
| `grepptraning` | 1 | 0 | Grepptränare Handgripper, 10–40 kg |
| `hopprep` | 1 | 0 | Hopprep Christopeit Pro med Vikter |
| `energi-prestation` | 1 | 0 | Koffeinsot TREC Boogieman Shot 100ml, Bubble Gum |
| `sandsack` | 1 | 0 | Powerbag Sandsäck, 5–30 kg, Nylon och Konstläder |
| `pulsmatare` | 1 | 0 | Pulsmätare Christopeit, Trådlös |
| `sparkcykel` | 1 | 0 | Sparkcykel S'cool flaX 8.3, Mörkgrå-Gul |
| `magnesium` | 1 | 0 | Springcykel S'cool X Magnesium, 12 tum, 2–4 år |
| `skivstangsstallning` | 1 | 0 | Skivstångsställning Hammer Core 2.0 |
| `roddmaskin` | 1 | 0 | TUNTURI Platinum - Sittande Roddmaskin för Styrketräning - Platladdad - V-Series |
| `magtraning` | 1 | 0 | Magträningshjul Tunturi Double Exercise Wheel, Dubbelhjul |
| `kabelhandtag` | 1 | 0 | Kabelhandtag Gymstick V-Handle |

Kolumnen `granskat_ja_nej` i CSV fylls i av granskaren; bara rader med `ja` (eller hela kollektioner David godkänner) körs.
