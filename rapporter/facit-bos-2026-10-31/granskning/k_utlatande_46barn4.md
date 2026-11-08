# Granskningsutlåtande k_46barn4, skyddsram för barnstol (2026-11-08)

Granskaren har bara läst i Shopify och inte ändrat något där, och har inte committat något. Live-läsningen gjordes med `shopify_api.py` (ShopifyKlient, `verifiera_butik` gav BEST OF SPORTS); `mcp__Shopify__*` användes inte. Underlag: CLAUDE.md, `regler-v1.md` (R1–R19, v1.5–v1.11), BESLUTSLOGG till och med 2026-11-08 (aktiva produkter utan text får faktatext även i tidigare utanför-kategorier; exakta dubbletter av andra aktiva annonser skrivs inte), LARDOMAR, butiksprofilen, `c_granskarprompt.md`, praxis i `k_utlatande_43.md`/`k_utlatande_46barn1.md` och formatet i `k_utlatande_43.json`. Avvisade-filen är tom.

Maskinläsbar version: `rapporter/facit-bos-2026-10-31/vag2_skriv/k_utlatande_46barn4.json`.

## Resultat: 0 GODKÄND, 0 RÄTTA, 1 UNDERKÄND

| nr | id | fil | dom | skäl |
|---|---|---|---|---|
| 46901 | 10676715553034 | k_46barn4_utkast.json | UNDERKÄND | Exakt dubblett av aktiv annons 10676715487498 (samma SKU 1580-5 och EAN 7350097561254) |

## 46901 (10676715553034): UNDERKÄND

**Skäl (R12a, BESLUTSLOGG 2026-11-05 och 2026-11-08):** butiken har två aktiva annonser för samma artikel:

- 10676715553034 "Skyddsram för barnstol till CARGOBIKE of SWEDEN Longtail Varia" (detta utkast)
- 10676715487498 "Skyddsram för barnstol CARGOBIKE of SWEDEN Longtail Varia"

Båda har SKU 1580-5, EAN 7350097561254, lager 0 och taggen På beställning. Beslutet 2026-11-08 säger att exakta dubbletter av andra aktiva annonser inte skrivs förrän lagret flyttats. Tvillingen avvisades i k_46barn3 (nr 46824) med säkerhetsskäl, så de två annonserna har också fått olika bedömning. David behöver välja vilken annons som ska vara kvar.

**Texten i sig håller:** live ACTIVE, en variant (Default Title, 1580-5, 1749 kr). Artikelnummer och EAN bekräftade på tillverkarens sida https://cargobikeofsweden.com/sv/articles/2.8.409/skyddsram-for-barnsate-longtail. Alla uppgifter finns i egen källa (pakethållare, två barn, dubbla räcken, stål, svart lack). Löftena "tryggt", "säkert" och "skydda barnens händer" är utelämnade; "Skyddsram" står bara som produktnamn. Inga hälso-, utvecklings-, prestanda- eller kvalitetslöften. "Maximal lastgräns: Ej känd" är tillåtet enligt v1.10, även om barntransport egentligen inte omfattas. Titel 57 tecken och 0 kommatecken, SEO 41, meta 128 med verb, "Passar för" finns, ingen cirkulär inledning. Standardblocket är exakt som i `b_skriv_24.json`, och leveranstidsmeningen finns eftersom produkten har taggen På beställning. Titel, SEO och meta finns inte i andra utkast. `skrivfil_kontroll.py` ger 1 FEL: produkten står i spärrlistan (utanfor-tills-vidare-2026-11-04) och behöver undantag. Utkastet kan återanvändas utan ändring för den annons David väljer att behålla.

## Fråga till David

Två aktiva annonser säljer samma skyddsram (1580-5). Vilken ska vara kvar? Rekommendation: behåll 10676715553034, arkivera 10676715487498 (lager 0 på båda, så inget lager behöver flyttas) och skriv sedan detta utkast efter undantag i spärrlistan. Kontrollera först enligt LARDOMAR 2026-11-06 att Velomarket-synken inte återaktiverar den arkiverade annonsen.
