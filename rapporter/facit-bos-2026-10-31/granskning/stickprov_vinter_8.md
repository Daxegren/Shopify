# Stickprov vinterprodukter, skrivfil b_skriv_8 (2026-11-03)

Kontrollant: Sonnet (endast läsning). Butik: BEST OF SPORTS (bestofsports.se), bekräftad med get-shop-info. Inget skrevs i Shopify.
Underlag: `vag2_skriv/b_skriv_8.json` (26 produkter), före-läge `shopify-original-2026-11-03/vag2b_8_fore.json`, live via graphql_query.

## Urval (12 av 26)
Alpina T 10 (pjäxor, 10475367760138), Peltonen Astra Skin 25 (skidor, 10462235623690), Kästle XA20 (skidor, 10471005257994), Start Track (stavar, 10472218820874), Mund City Winter 12 (strumpor, 10411725652234), Start Easy HF Glider (glidmedel, 10462169334026), Start RG Ultra Gel (glidvalla, 10471025246474), Rex Marka (handskar, 10472242643210), Start Easy Kick Wax Tar (tjärvalla, 10472242741514), Start Easy Q +5 till -10 (fästvalla, 10472244314378), Start Universal Plus (klister, 10475385061642), Rex Omega (stav, 10494685380874).

## Resultat: 0 avvikelser mot skrivfilen
| Kontroll | Resultat |
|---|---|
| Titel = filens titel | 12 av 12 lika |
| seo.title = filens seo_title (null när lika med titeln) | 12 av 12 (Start Track lagrad som null, avsett) |
| seo.description = filens meta | 12 av 12 lika |
| descriptionHtml = filens html (radbrytning mellan li, avsett) | 12 av 12 lika för allt före rubriken Leverans; standardblocket jämfört med filens genom läsning (Astra har extra mening om beställningsvaror, avsett) |
| Taggen texter-klara, status ACTIVE | 12 av 12 |
| Rex Omega saknar raden "Varianter" | Ja, saknas i specifikationen |
| Längder | Titel 22–54 (högst 70), SEO-titel 22–39 (högst 43), meta 118–147 |
| Formatregler (stor bokstav efter kolon, versaler i titel/SEO, små ord och enheter) | Inga avvikelser |
| Stavning | Inga fel funna |

Oväntade leverantörstaggar (Hybridcykel på Mund-strumporna, Sparkcykel på Kick Wax Tar) ligger kvar; taggar ändras inte enligt standarden.

## Faktakontroll mot före-filen
Alla tal och uppgifter hittades i källan (till exempel 80/15/5 %, 31–45, 60 ml, 30 ml, 55 g, 645–825 g, 60–50–55 mm, 44 mm, PRG 3600, Tour 11 mm). Inget påhittat funnet. Trasiga källuppgifter har rätt utelämnats: Start Track "skidhandske" och "Tour 10 mm", Kick Wax Tar 50 ml mot 60 ml, klistrets temperaturintervall, HF Glider "golvglidmedel". Inga hälso- eller säkerhetspåståenden; tillverkarpåståenden (varma, nybörjarvänliga, vattentätt yttermaterial, lätt att använda) står med "enligt tillverkaren".

## Anmärkningar (inte fel, för beslut av David om önskat)
1. Rex Omega: intron säger "finns i tre varianter". Butiken har tre varianter (125, 135, 160), men källtexten nämner inte antalet. Uppgiften stämmer med butiksdata; variantnamnen är oförklarade och används inte.
2. Meta för Start Easy HF Glider, Kick Wax Tar och Easy Q anger "räcker 5–10 km" utan "enligt tillverkaren" (specifikationen för HF Glider har förbehållet, de två andra saknar det). Källan anger det utan förbehåll. Prestandapåstående, inte hälsa eller säkerhet.
3. Mund City Winter 12: meta är 118 tecken, under riktvärdet 130 (tunn källa, i linje med avsnitt 14).
4. Alpina T 10: bindningen NNN är bekräftad i källans slut ("Lämplig bindning för …"); kontrollerades mot före-filen.
