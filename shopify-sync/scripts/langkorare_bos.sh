#!/usr/bin/env bash
# Långkörare för Cloud Shell (egen flik). Kör sex läsande kontroller mot Best of Sports efter varandra och sparar allt i en mapp.
# Tar ungefär 45–90 minuter. Skriver ingenting i Shopify, Google Ads eller Merchant Center.
#
#   cd ~/Shopify/shopify-sync && git pull origin claude/zealous-johnson-0ywddr
#   nohup bash scripts/langkorare_bos.sh > ~/langkorare.log 2>&1 &
#   tail -f ~/langkorare.log          # följ förloppet; Ctrl+C stoppar bara tail, inte körningen
#
# Steg: 1) indexeringsstatus (Search Console URL Inspection) för .se .dk .fi, 2) renderande kategorikontroll .se .dk .fi,
#       3) samtycke och spårning, 4) köpflöde mobil och desktop, 5) tillgänglighet (axe-core).
# Steg 1 kräver att du är inloggad med tjänstekontots behörighet till Search Console (samma som vid backfill); misslyckas det
# hoppas steget över och resten körs ändå.
set -uo pipefail
cd "$(dirname "$0")/.."
OUT="${OUT:-$HOME/langkorare-$(date +%Y%m%d-%H%M)}"
mkdir -p "$OUT"
COLL="${COLL:-/collections/motionscykel}"
log() { printf '\n== %s  %s\n' "$(date +%H:%M:%S)" "$*"; }

log "Förberedelser (pip, Playwright)"
pip install -q -e . 2>&1 | tail -n 2
pip install -q playwright axe-playwright-python 2>&1 | tail -n 2
python3 -m playwright install --with-deps chromium 2>&1 | tail -n 3

for s in se dk fi; do
  log "1. Indexeringsstatus bestofsports-$s"
  site-audit --config sites.toml inspect --site "bestofsports-$s" --per-type 30 --out "$OUT/inspektion-$s" 2>&1 | tail -n 25
done
for s in se dk fi; do
  log "2. Renderande kategorikontroll bestofsports.$s"
  python3 scripts/rendera_kategorier.py --base-url "https://bestofsports.$s" --sample 40 --out "$OUT/kategorier-$s" 2>&1 | tail -n 12
done
log "3. Samtycke och spårning bestofsports.se (mobil)"
python3 scripts/samtycke_test.py --base-url https://bestofsports.se --out "$OUT/samtycke-se" 2>&1 | tail -n 40
log "4. Köpflöde bestofsports.se (mobil, desktop)"
python3 scripts/kopflode_test.py --base-url https://bestofsports.se --collection "$COLL" --viewport mobile --out "$OUT/kopflode-mobil" 2>&1 | tail -n 30
python3 scripts/kopflode_test.py --base-url https://bestofsports.se --collection "$COLL" --viewport desktop --out "$OUT/kopflode-desktop" 2>&1 | tail -n 30
log "5. Tillgänglighet bestofsports.se (mobil)"
python3 scripts/tillganglighet_test.py --base-url https://bestofsports.se --collection "$COLL" --out "$OUT/tillganglighet" 2>&1 | tail -n 20
log "KLART. Resultat i $OUT"
ls -R "$OUT" | head -n 60
