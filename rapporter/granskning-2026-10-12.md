# Granskning av körningen 2026-10-12 (gorillasports.se)

Underlag: `gs://gorilla-sports-data-site-audit/audits/gorillasports-se/latest/`, uppladdad 2026-10-12 03:20 UTC, hämtad till `~/audit-se`. Inget har ändrats i Shopify eller Google Cloud.

**Kontroll av ändringarna 2026-10-10:**
- Loopen på `/products/vagtstangssat-25-26mm-60kg` är borta. Sidan omdirigerar i ett hopp till `/collections/skivstang-curlstang-hantlar`.
- `/wall-ball/s/283` går i ett hopp till `/collections/wall-ball`.
- Körningen har fortfarande 106 `redirect_chain`, 59 `redirect_to_error` och 73 `redirect_target_missing`.

## 1. Inline-skriptet på cirka 285–291 KB

**App:** *SEOWILL Trust Badges & Star Rating* (utvecklare Giraffly). Så här syns det:
- Skriptet anropar `/apps/giraffly-trust/add/view?name=gs-nordic-production.myshopify.com`.
- Det letar efter element med klassen `giraffly-trust-badge-…`.
- Produktsidans app-block heter `…__seowill_trust_badges_star_rating_…`.
- De kinesiska kommentarerna kommer från apputvecklarens kod, till exempel `// 检查是否有class为shopify-design-mode的元素` ("kontrollera om det finns ett element med klassen shopify-design-mode") och `console.error("请求失败:")` ("anropet misslyckades").

**Hur skriptet hamnar på sidan:** via appens *app-embed* (block `AelBWSzVVbHFJb1VaN__5890205134905443601`). Det ligger längst ner på alla 1 562 sidor, enligt `large_inline_script_sitewide`.

**Vad de 284 KB består av** (mätt på startsidan 2026-10-12):
- Ett enda badge-id (`697a19333193d-65218145-561769609523`).
- CSS för 78 animationer (hela animate.css) och badgens HTML, inbäddade som JavaScript-strängar. Tre långa rader på cirka 60 KB och tre på cirka 29 KB, varav bara tre är unika. Samma innehåll finns alltså två gånger.
- Hämtar jQuery 3.6.0 från `ajax.googleapis.com` om jQuery saknas. Pollar med `setInterval`.

**Var badgen faktiskt visas:**

| Sida | Badge-behållare | Giraffly-skript |
|---|---|---|
| Startsidan | 0 | 284 KB, som inte används |
| Produktsida (`/products/bollpump`) | 1 | 284 KB (embed) + 93 KB (produktblocket) + 1 KB, totalt cirka 378 KB |

**Förslag på åtgärd**, i den här ordningen:
1. **Stäng av appens embed** under *Onlinebutik → Teman → Anpassa → Appinbäddningar*. Gör det först i en kopia av temat. Kontrollera sedan att badgen på produktsidan fortfarande visas, eftersom produktblocket har ett eget skript på 93 KB. Det tar bort 284 KB från alla sidor som inte är produktsidor och halverar mängden på produktsidorna.
2. **Ännu bättre: ersätt appen** med en statisk bild eller SVG med betalikoner och trygghetsmärken i temats produktmall, på 2–5 KB. Avinstallera sedan appen. Då försvinner också jQuery-hämtningen och visningsanropet till `/apps/giraffly-trust` vid varje sidvisning.
3. Om appen ska vara kvar: välj ingen animation i appens inställningar, och be Giraffly ladda CSS:en som extern fil i stället för inline.

Mät före och efter med `site-audit run --psi N` (LCP och INP) och med `html_size_stats` i nästa körning.

## 2. Titlar och beskrivningar för sidor på topp 10 med låg klickfrekvens

Fil: `rapporter/titlar-lag-ctr.csv`, 68 sidor. Titlarna är högst 60 tecken och beskrivningarna högst 155 tecken. Skriptet kontrollerar längderna.

**Att känna till innan du publicerar:**
- **Temat lägger till "\n – Gorilla Sports Nordics"** efter varje SEO-titel, alltså 25 tecken plus en radbrytning. Med det tillägget blir titlarna upp till 85 tecken och kapas i Google. Förslagen har därför sökordet först och inget varumärke, så att det bara är varumärket som kapas. Bäst vore att ändra `<title>` i temat, så att tillägget bara kommer när titeln är kort. Det ska beslutas separat.
- Några befintliga titlar har både "| Gorilla Sports" och temats tillägg, alltså varumärket två gånger.
- **H1 som inte beskriver ämnet** på sex artiklar: "Fantastiska!" (smithmaskiner), "Här är vägen ut!" (superset), "Hatkärlek" (thrusters), "Vi reder ut skillnaderna" (tyngdlyftning), "Ett inlägg i latsens ära" (lats) och "Övningar som hjälper mott axelont" (stavfel). `/pages/gorilla-sports` och `/collections/all` saknar H1 helt.
- **Ny titel löser inte allt:**
  - `/collections/all`, `/collections/alla-produkter` och `/pages/gorilla-sports` får nästan bara varumärkessökningar, och där tar startsidan klicket. För `/collections/all` föreslås noindex eller canonical i stället.
  - Artikeln om latsdrag har 915 visningar på position 3,6 med 0 klick. Där bör sökresultatet granskas, eftersom det kan domineras av videor eller frågerutor.
- **Kannibalisering:**
  - Två artiklar om magrutor, plus en om magmuskler.
  - Två artiklar om större armar.
  - Kollektionen träningsbänk och produkten MX 10z syns på samma sökord.
  - Förslagen vinklar sidorna olika, men det långsiktiga är att slå ihop artiklarna.
- **Kontrollera mot artikeln:** beskrivningarna för artiklar bygger på titel, H1 och sökfraser, inte på brödtexten. Där motiveringen säger "kontrollera" har jag lagt till ett påstående som behöver stämmas av, till exempel "7 tips", tabataprotokollet eller "inversionsbänk".

## 3. Gissade omdirigeringar

Underlag: 94 gamla URL:er från `redirects_review.csv` och `actions.csv` ("Byt mål på omdirigering").

| Fil | Innehåll |
|---|---|
| `rapporter/redirects_granskade.csv` | 81 omdirigeringar i Shopifys importformat (`Redirect from,Redirect to`) |
| `rapporter/redirects_granskade_motivering.csv` | Samma 81 med verktygets förslag och min motivering |
| `rapporter/redirects_osakra.csv` | 13 som jag är osäker på, med förslag, alternativ och skäl. Importeras inte. |

**Kontroller:**
- Alla mål svarade 200 utan omdirigering, både i nattens crawl och vid en direkt kontroll 2026-10-12, med ett anrop per sekund.
- Ingen källa pekar på en annan källa, så filen skapar inga nya kedjor. Gamla par som `/lopband-runmaxx-7-1/p/1430` → `/products/lopband-runmaxx-7-1` får samma slutmål direkt.

**Vad som skiljer sig från verktyget:** för 67 av de 81 valde jag ett annat mål än verktygets. Vanligaste orsakerna:
- **Verktygets mål fanns inte på .se.** Ungefär hälften av förslagen var danska handles som inte syns på .se, till exempel `lobeband-maxxus-m8-solv`, `gs-romaskine-vannbestandig-trae` och `stobejern-trigrip-vegtskiver-2x15kg`.
- **Danska och norska ord tolkades fel:**

  | Gammalt ord | Betyder | Verktyget gissade |
  |---|---|---|
  | boksehandske | boxningshandske | päronboll |
  | vægtslæde | viktsläde | viktväst |
  | vægbeslag rope | väggfäste för battle rope | curlstångsställ |
  | hække-sæt | häcksats | plyobox |
  | vægtskiver gummi | viktskivor gummi | hantlar |

- **`/collections/all` som reserv** byttes mot rätt kategori, till exempel löpband, roddmaskin, viktskivor och boxningspaket.
- **Exakta produktmatchningar** användes bara när namn, material och vikt stämmer: GUMMI 108 kg, IRON Feder 100 kg, GUMMI Gjutjärn 1,25–25 kg, Medicinbollspaket GS 15 kg & stativ, Step Up Bräda Stor och gjutjärnshantlar 2x10 kg. I övriga fall föll valet på kategorin, eftersom en fel produkt är värre än en rätt kategori.

**Vid import:**
- Ungefär 51 av de 81 källorna finns redan som omdirigeringar i Shopify, med mål som ger 404. Kryssa i **"Ersätt befintliga omdirigeringar som har samma sökväg"**, annars hoppas de över.
- Två rader i den osäkra listan bör tas bort i Shopify i stället för att få nya mål: `/products/test` och källan som innehåller en admin-adress (`/products/https://admin.shopify.com/…`).

**Upptäckt på vägen, inte åtgärdat:**
- Det finns två levande produkter `massagestol-mx-10-0-zero-maxxus` och `…-1`, alltså en dubblett.
- `/collections/test` är publicerad.
- I `redirects_import.csv` pekar `/wall-ball-paket-pro-55kg/p/1137` på `/products/bollpump`. Det är verktygets rensning av ett befintligt mål med spårningsparametrar, men själva målet verkar fel och bör granskas före import.
