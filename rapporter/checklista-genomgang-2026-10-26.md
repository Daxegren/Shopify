# Checklista: genomgång av nattens genomlysningar (2026-10-26)

Mål: se om de fem jobben gick igenom och om rättningarna fungerade. Allt är läsning.

## 1. Ett kommando (Cloud Shell)
```bash
cd ~/Shopify/shopify-sync && git pull origin claude/zealous-johnson-0ywddr && bash scripts/audit_status.sh
```
Klistra in hela utdata till Claude.

## 2. Vad som ska stå där
| Sajt | Förväntat |
|---|---|
| Alla fem jobb | `COMPLETE 1/1`, ingen avbruten körning. Gorilla SE och DK ska lyckas för första gången sedan 13 oktober |
| bestofsports-* | `canonical_offsite` 0, `broken_internal_link` 0, `malformed_link_href` 0, `product_schema_no_image` nära 0 |
| bestofsports-* | `collections_rendered_by_js` 1 fynd i stället för hundratals kategorifynd |
| gorillasports-* | Samma kontroller. Eventuella nya fynd är verkliga och går igenom en i taget |

## 3. Om något avviker
- **Jobb misslyckat:** be Claude läsa loggen: `gcloud run jobs executions describe <körning> --region europe-north1` och klistra in raderna med `status`.
- **Tidsgräns nådd (jobb avbrutet efter 4 h eller 3 h):** höj `TASK_TIMEOUT` för det jobbet och kör om.
- **Fortfarande trasiga länkar:** kontrollera att Translate & Adapt inte skrivit om temats texter efter 25 oktober.

## 4. Verifiera kategorierna (en gång)
```bash
python3 scripts/rendera_kategorier.py --base-url https://bestofsports.fi --sample 30 --out rendera-bos-fi
```
Klistra in sammanfattningsraden. Siffran för `byggs_med_js` och `utan_h1` avgör om det finns verkliga kategoriproblem.

## 5. Beslut som väntar på David
- Omdömesappen: egen kod eller app? (`grep` i produktsidans HTML, se chatten.)
- Översättningsappen Translate & Adapt: stäng av auto-översättning av temats standardtext.
- Manuellt i Shopify: Melatonin bort från Google & YouTube, bilder för yogamattan och latexbandspaketet.
