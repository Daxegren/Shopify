#!/usr/bin/env bash
# Långkörare för Cloud Shell (egen flik): läsande kontroller mot Gorilla Sports (.se och .dk) efter varandra, sparade i en mapp.
# Tar ungefär 45–90 minuter. Skriver ingenting i Shopify, Google Ads eller Merchant Center.
#
#   cd ~/Shopify/shopify-sync && git pull origin claude/zealous-johnson-0ywddr
#   nohup bash scripts/langkorare_gorilla.sh > ~/langkorare-gorilla.log 2>&1 &
#   tail -f ~/langkorare-gorilla.log     # Ctrl+C stoppar bara tail, inte körningen
#
# Steg: 0) läget (gorilla_lage.sh), 1) indexeringsstatus (Search Console) .se .dk, 2) renderande kategorikontroll .se .dk,
#       3) samtycke och spårning .se .dk, 4) köpflöde mobil på .se och .dk, desktop på .se, 5) tillgänglighet .se.
# Steg 1 kräver Search Console-behörighet; saknas den hoppas steget över och resten körs ändå.
# Kategori som testas kan ändras: COLL=/collections/annat bash scripts/langkorare_gorilla.sh
set -uo pipefail
cd "$(dirname "$0")/.."
OUT="${OUT:-$HOME/langkorare-gorilla-$(date +%Y%m%d-%H%M)}"
mkdir -p "$OUT"
COLL="${COLL:-/collections/kettlebell}"
log() { printf '\n== %s  %s\n' "$(date +%H:%M:%S)" "$*"; }

log "Förberedelser (pip, Playwright)"
pip install -q -e . 2>&1 | tail -n 2
pip install -q playwright axe-playwright-python 2>&1 | tail -n 2
python3 -m playwright install --with-deps chromium 2>&1 | tail -n 3

log "0. Läget (jobb, fynd, omdirigeringar, omsättning, annonser)"
bash scripts/gorilla_lage.sh > "$OUT/lage.txt" 2>&1; tail -n 8 "$OUT/lage.txt"

for s in se dk; do
  log "1. Indexeringsstatus gorillasports-$s"
  site-audit --config sites.toml inspect --site "gorillasports-$s" --per-type 30 --out "$OUT/inspektion-$s" 2>&1 | tail -n 25
done
for s in se dk; do
  log "2. Renderande kategorikontroll www.gorillasports.$s"
  python3 scripts/rendera_kategorier.py --base-url "https://www.gorillasports.$s" --sample 40 --out "$OUT/kategorier-$s" 2>&1 | tail -n 12
done
for s in se dk; do
  log "3. Samtycke och spårning www.gorillasports.$s (mobil)"
  python3 scripts/samtycke_test.py --base-url "https://www.gorillasports.$s" --out "$OUT/samtycke-$s" 2>&1 | tail -n 40
done
for s in se dk; do
  log "4. Köpflöde www.gorillasports.$s (mobil)"
  python3 scripts/kopflode_test.py --base-url "https://www.gorillasports.$s" --collection "$COLL" --viewport mobile --out "$OUT/kopflode-$s-mobil" 2>&1 | tail -n 30
done
log "4b. Köpflöde www.gorillasports.se (desktop)"
python3 scripts/kopflode_test.py --base-url https://www.gorillasports.se --collection "$COLL" --viewport desktop --out "$OUT/kopflode-se-desktop" 2>&1 | tail -n 30
log "5. Tillgänglighet www.gorillasports.se (mobil)"
python3 scripts/tillganglighet_test.py --base-url https://www.gorillasports.se --collection "$COLL" --out "$OUT/tillganglighet-se" 2>&1 | tail -n 20
log "KLART. Resultat i $OUT"
ls -R "$OUT" | head -n 60
