# BEST OF SPORTS: status för produkttexterna 2026-11-12

**Bara läsning.** Siffrorna kommer från en ny läsning av alla produkter i butiken 2026-11-12 (inventering, 5 354 produkter, 109 anrop, ca 50 sekunder) och är kontrollräknade i `rapporter/inventering-bos-2026-11-12/siffror.json`. Ingenting skrevs i Shopify. Den gamla planen `shopify-sync/status/bestofsports-plan-kvarvarande.md` (inventering 2026-11-04) är inaktuell och lämnades orörd.

Förklaringar: **texter-klara** är taggen som markerar att en produkt har fått vår text och verifierats. **Spärrlistan** (`shopify-sync/config/sparrlista.json`) är listan över produkter som textutrullningen inte får skriva. **Standardblocket** är den fasta delen med leverans, retur, reklamation och säljare. **Meta** är metabeskrivningen som visas i Googles träfflista.

## 1. Produkter per status

| Status | Totalt | Med texter-klara | Utan texter-klara |
|---|---|---|---|
| Aktiva | 3 891 | 3 160 | 731 |
| Utkast | 1 167 | 14 | 1 153 |
| Arkiverade | 296 | 17 | 279 |
| **Alla** | **5 354** | **3 191** | **2 163** |

Förändring sedan inventeringen 2026-11-04 (5 315 produkter): 39 nya produkter (alla aktiva, ingen med text), 454 utkast blev aktiva, 150 arkiverade blev aktiva, 116 aktiva blev arkiverade, 15 utkast arkiverades och 1 aktiv blev utkast. Det är den främsta förklaringen till att antalet aktiva produkter utan text har ökat från 281 (mätning 2026-11-08) till 731.

## 2. De 731 aktiva produkterna utan text

| Grupp | Antal | Vad det är |
|---|---|---|
| A. Aktiv spärr: utanför tills vidare | 10 | Kvar i spärrlistan efter undantagsfilen |
| B. Aktiv spärr: titeldubblett | 2 | Samma titel som en annan produkt |
| C. Aktiv spärr: tidigare avvisad | 30 | Avvisad i en tidigare omgång, väntar på beslut eller källa |
| D. Avvisad i en batch, men inte i spärrlistan | 198 | Se nedan |
| F. Aldrig bearbetad | 491 | Aktiverades eller skapades efter 2026-11-04 |
| **Summa** | **731** | |

**D uppdelad efter avvisningsskäl** (sorterat på ord i motiveringen, därför ungefärligt): olika pris eller artiklar i samma annons 73, dubbletter 52, tunn eller motsägande källa 25, säkerhetsprodukter 18, övrigt 16, barn 9, kosttillskott 4, elektronik 1.

**F uppdelad** (alla 491 har taggen Velomarket, 156 är beställningsvaror): kandidater för ny omgång 244 (lager, ingen titelträff mot skriven produkt, inga riskord), riskord i titel eller typ (hjälm, lås, broms, barn, kosttillskott, massage m.fl.) 123, lager 0 118, titel lika med en redan skriven aktiv produkt 6.

Listan per produkt finns i `rapporter/inventering-bos-2026-11-12/aktiva_utan_text.csv`.

## 3. Spärrlistan: antal och varför

| Spärr | Poster i filen | Gäller efter undantagsfilen | Skäl |
|---|---|---|---|
| pilot-20 | 20 | 19 (alla aktiva, alla med text) | Pilotens 20 produkter mäts runt 2026-11-22 och ändras inte; David 2026-11-04 |
| utanför tills vidare | 333 | 13 (10 aktiva, 3 arkiverade) | Kategorier som ägaren inte släppt; inventering 2026-11-04 |
| tidigare avvisade | 567 | 77 (30 aktiva, 47 arkiverade) | Avvisade i tidigare batcher, väntar på beslut eller källa |
| titeldubbletter | 26 | 12 (2 aktiva, 10 arkiverade) | Samma titel; den äldsta skrivs, övriga spärras (R12a) |

Undantagsfilen (David 2026-11-05) frisläpper 1 234 produkter ur spärrarna. Ingen spärrad produkt har fått text utom pilotens 19 (de har pilottexten) och inga andra överträdelser hittades i dag.

## 4. Utanför tills vidare, per kategori

Butiksprofilen listar: isbroddar, rullskridskor, akupressur, vibrationsplattor, kroppsanalysvågar och massagestolar. David beslutade 2026-11-08 att **aktiva** produkter i tidigare utanför-kategorier får text (utom blandade annonser, dubbletter med lager och produkter med tom eller motsägande källa). Profilens lista är därför mer sträng än verkligheten. Nyckelordsträffar i titel, produkttyp och taggar (ungefärliga):

| Kategori | Alla | Aktiva med text | Aktiva utan text | Utkast / arkiverade |
|---|---|---|---|---|
| Isbroddar | 0 | 0 | 0 | 0 |
| Rullskridskor | 34 | 13 | 21 | 0 |
| Akupressur | 13 | 7 | 1 | 4 / 1 |
| Vibrationsplattor | 12 | 6 | 1 | 5 / 0 |
| Kroppsanalysvågar | 1 | 1 | 0 | 0 |
| Massagestolar | 8 | 0 | 0 | 6 / 2 |
| Barn (brett nyckelord) | 323 | 203 | 87 | resten |
| Kosttillskott | 153 | 89 | 15 | resten |

## 5. Titeldubbletter

Exakt lika titel: 81 grupper med 179 produkter i hela butiken. Bland aktiva produkter 36 grupper med 75 produkter, varav 10 har text och 65 saknar. Spärrlistan täcker bara 12 av dem.

## 6. Luckor i SEO, meta och standardblock

| Mått | Aktiva med text (3 160) | Aktiva utan text (731) | Alla (5 354) |
|---|---|---|---|
| Meta saknas | 27 | 722 | 2 063 |
| Meta under 70 tecken | 7 | 0 | 8 |
| Meta över 155 tecken | 1 | 0 | 14 |
| SEO-titel ej satt (titeln används) | 1 106 | 728 | 3 259 |
| SEO-titel över 60 tecken | 4 | 0 | 6 |
| Titel över 70 tecken | 0 | 37 | 55 |
| Standardblock saknas | 0 | 726 | 2 157 |
| Beskrivning under 50 tecken | 0 | 10 | 45 |
| Beställningsvara utan leveranstidsmening | 13 | 207 | 444 |

"SEO-titel ej satt" är inte ett fel: Shopify lagrar tom SEO-titel när den är lika med titeln. Räknat över alla 3 191 produkter med texter-klara (oavsett status) har 54 minst en lucka; bland de aktiva är det 27 utan meta, 7 med för kort meta, 1 med för lång, 4 med lång SEO-titel och 13 beställningsvaror utan leveranstidsmening (en produkt kan ha flera). Lista i `rapporter/inventering-bos-2026-11-12/luckor_skrivna.csv`.

## 7. Vad som återstår för att produkttexterna ska vara klara

| Grupp | Antal | Beslut som saknas |
|---|---|---|
| Nya eller aktiverade produkter, kandidater för ny omgång | 244 | Ja till en ny skrivomgång (samma rutin som tidigare) |
| Nya eller aktiverade med riskord | 123 | Behandlas en och en enligt beslutet 2026-11-08; ja till omgången? |
| Nya eller aktiverade utan lager | 118 | Ska produkter med lager 0 få text? |
| Nya eller aktiverade, titel lika med skriven produkt | 6 | Dubbletter: arkivera eller lämna |
| Avvisade: olika pris eller artiklar | 73 | Dela annonsen per artikel eller lämna (beslut från 2026-11-08 öppet) |
| Avvisade: dubbletter | 52 | Flytta lager och arkivera; kräver lagerbehörighet i appen |
| Avvisade: tunn eller motsägande källa, övrigt | 41 | Lämna tills leverantören ger uppgifter |
| Avvisade: säkerhet, barn, kosttillskott, elektronik | 32 | Fall för fall |
| Aktiva spärrar A–C | 42 | Häva eller behålla |
| Rättningar på skrivna texter (meta, leveranstid) | 54 | Ja till små rättningar (kräver skrivning) |
| F2: "enligt tillverkaren" på maxvikt | 4 | Ja till före/efter i `beslut-2026-11-12-2.md` |
| Utkast och arkiverade utan text | 1 153 + 279 | Ingen åtgärd tills de blir aktiva; en löpande kontroll behövs |

**Statusfilen** `shopify-sync/status/bestofsports-textutrullning.md` uppdaterades inte: generatorn räknar bara batcherna f, g och h (540 produkter) och skulle bara byta datumet i en rad. Den ger därför ingen rättvisande bild av läget; denna rapport ersätter den tills generatorn kan läsa alla batchprefix.
