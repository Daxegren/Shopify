# Skrivrapport f_8 (2026-11-04)

Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info. Skrivfil: vag2_skriv/f_skriv_8.json (25 Velomarket-produkter: steppers, crosstrainers, roddmaskiner, skiergometer).

## Före/efter
- Före-läge: rapporter/shopify-original-2026-11-04/f_8_fore.json (titel, handle, status, taggar, seo, descriptionHtml). Alla 25 var ACTIVE, ingen hade texter-klara, ingen hade redan skrivfilens titel. Ingen hoppades över.
- Före: samtliga hade seo.title och seo.description null; titlarna var leverantörens (t.ex. "Stepper TOORX Everfit Step Twist", "Rowing ergometer BH FITNESS i.Thames"). Efter: titel, SEO-titel, metabeskrivning och beskrivning enligt skrivfilen.
- Notering: före-filens descriptionHtml kommer från inklistring av live-läsningen (fyra långa texter lästes om och sparades exakt).

## Kontroll före skrivning
kontrollera_produkttext.py (--seo-title-max 43 --seo-suffix " – BEST OF SPORTS" --meta-min 70, källa = före-text + handle): 0 FEL efter att produktkoden 20TCFR2050 (10411898339594) verifierats som variantens SKU; 25 VARNINGAR "saknar avsnittet 'passar dig som'" (kända, rubriken heter "Passar för"). Utan --meta-min 70 gav 9 produkter meta under 130 tecken (111-129), godtaget enligt standard avsnitt 14/17 (kort meta, ingen utfyllnad).
På beställning: alla 9 produkter med taggen har leveranstidsmeningen, och ingen utan tagg har den (kontrollerat maskinellt).

## Skrivning
productUpdate via skriptutskrift (json.dumps ensure_ascii=True) inklistrad ordagrant: kanarie 3, därefter 5+5+5+5+2. seo skickades alltid med title och description. 0 userErrors. Handle, status och pris orörda.

## Återläsning
Alla 25 återlästa i grupper om högst 4 och jämförda i python tecken för tecken mot skrivfilen: titel, handle (oförändrad), status (ACTIVE), seo.title (null accepteras när lika med titeln), seo.description, descriptionHtml, samt osynliga tecken (Cf, mjukt bindestreck, nbsp, zero-width). Avvikelser: 0. Förstahandsläsning av radbrytningar mellan <li>: skrivfilen hade redan \n, ingen skillnad. Inget kontrollerades bara för hand.

## Taggar
tagsAdd "texter-klara" på alla 25, 0 userErrors. Efterläsning: övriga taggar kvar (inkl. Velomarket, Gymstick på 10472298381578, På beställning på 9 produkter).

## Avvikelser
Inga i Shopify. Process: ett första försök att spara före-läget i fil hade förkortade texter på fyra produkter; upptäcktes före skrivning och rättades med ny läsning av just de fyra. Före-filen är alltså komplett.
Anm. Handlingsbar notering: 10411898339594 hade i före-läget kodstaket "```html" som text; ersatt av ny text.
