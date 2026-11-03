# Skrivrapport: vinterprodukter, skrivfil b_skriv_9 (2026-11-03)

Butik: BEST OF SPORTS (bestofsports.se), kontrollerad med get-shop-info innan skrivning.

## Före och efter

| Nr | Produkt-id | Live före (titel) | Skriven titel | Status | Tagg |
|---|---|---|---|---|---|
| 8401 | 10411476615434 | Kälke STIGA Pacer med bromsar, svart | Kälke Stiga Pacer med Bromsar | ACTIVE | texter-klara |
| 8402 | 10470970392842 | Kälke "Salvo" mix | Kälke Uniplast Salvo | ACTIVE | texter-klara |
| 8405 | 10470954238218 | Eretic Snowscoot Slope | Snowscoot Eretic Slope | ACTIVE | texter-klara |
| 8409 | 10472281899274 | Styrkälke STIGA SnowPower, svart/grön | Styrkälke Stiga SnowPower, Svart och Grön | ACTIVE | texter-klara |
| 8410 | 10472285274378 | Ratt STIGA Curve grafitgrå/blå | Rattkälke Stiga Curve, Grafitgrå och Blå | ACTIVE | texter-klara |
| 8425 | 10472323875082 | Hockeyskridskor FILA Viper Hc PLUS, Black/Red | Hockeyskridskor Fila Viper HC Plus, Svart och Röd | ACTIVE | texter-klara |

Före-läget (titel, handle, status, tags, seo, descriptionHtml) ligger i `rapporter/shopify-original-2026-11-03/vag2b_9_fore.json`. Före skrivning var seo.title och seo.description null på alla sex.

Hoppade över: inga. Alla sex var ACTIVE, hade inte taggen "texter-klara" och hade annan titel än skrivfilen.

## Kontroll före skrivning

- Kontrollskriptet kördes på kopia (`tmp_kopia_vag2b9/kontroll_b9.json`), html mappad till beskrivning, standardblocket markerat, källtext = före-läget, `--seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70`.
- Resultat: 0 FEL, 8 VARNINGAR.
- Varning "saknar avsnittet 'passar dig som'" (6 st): avsiktlig, rubriken heter "Passar för".
- Varning "tillverkad i Estland" (8402): står i källtexten ("Tillverkad i Estland."), godtas.
- Meta-längder 94–152 tecken, alla över 70.

## Skrivning

- Kanarie: 8401, 8402, 8405 i en mutation (productUpdate, seo{title, description} med båda fälten). Inga userErrors.
- Resten: 8409, 8410, 8425 i en mutation. Inga userErrors. Mutationstexten (537 tecken) och variablerna (ca 4 700 tecken) genererades av skript och klistrades in ordagrant.
- Inga handskrivna rättningar gjordes. Inga fel uppstod.

## Verifiering

- Återläsning av alla sex med graphql_query (title, handle, status, seo.title, seo.description, descriptionHtml, tags).
- Jämförelse mot skrivfilen och före-läget i python: 36 av 36 kontroller stämmer (title, handle, status, seo.title, seo.description, descriptionHtml). Inga avvikelser. Shopify lagrade inga null-värden för seo.title (ingen seo_title var lika med titeln).
- Taggar efter tagsAdd: "texter-klara" finns på alla sex, och alla före-taggar finns kvar.
- Obs: återläsningen klistrades in av mig i en fil och jämfördes sedan maskinellt. Det som jämförts maskinellt är alltså den inklistrade återläsningen mot skrivfilen. Den direkta läsningen från Shopify är kontrollerad visuellt mot det inklistrade.
- Obs: före-filen är inklistrad från live-läsningen, inte maskinellt hämtad.

## Ändrat i Shopify

Ja: title, seo (title och description) och descriptionHtml på sex produkter, plus taggen "texter-klara". Handle, status och pris ändrades inte.

## Att bekräfta

- Ingen. Alla sex är klara enligt standarden.
- Varning "tillverkad i Estland" för 8402 är godkänd enligt källtexten, men David kan vilja bekräfta den.

## Filer

- Skrivfil: `rapporter/facit-bos-2026-10-31/vag2_skriv/b_skriv_9.json`
- Före-läge: `rapporter/shopify-original-2026-11-03/vag2b_9_fore.json`
- Kontrollkopia: `rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2b9/kontroll_b9.json`
- Återläsningar: `/tmp/claude-0/-home-user/fbbd95a3-8b18-5096-a6b5-20df3e4eb235/scratchpad/readback_a.json` och `readback_b.json`
- Inget har committats.
