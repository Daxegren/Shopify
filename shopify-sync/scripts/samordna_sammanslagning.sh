#!/usr/bin/env bash
# Slår ihop butiksgrenar in i en testgren utan att pusha (samordnaren, 2026-11-04).
# Användning: samordna_sammanslagning.sh TESTGREN GREN [GREN ...]   (GREN utan origin/claude/-prefix)
# Regler: docs/ (append-only) behåller båda sidors rader; filer med samma namn från olika grenar
# (rapporter/beslut-*.md, scripts/*.py) behåller första versionen och sparar övriga som <namn>-<butik>.<ändelse>.
# Pushar aldrig. Skapar ingen pull request. Originalen på butiksgrenarna ändras inte.
set -u
test=$1; shift
cd "$(git rev-parse --show-toplevel)"
git fetch -q origin
git checkout -q -B "$test" "$(git rev-parse --abbrev-ref HEAD)"
union() { python3 - "$@" <<'PY'
import sys
for p in sys.argv[1:]:
    out=[];mode=0
    for l in open(p,encoding='utf-8').read().split('\n'):
        if l.startswith('<<<<<<< '): mode=1; continue
        if l.startswith('=======') and mode==1: mode=2; continue
        if l.startswith('>>>>>>> ') and mode==2: mode=0; continue
        out.append(l)
    open(p,'w',encoding='utf-8').write('\n'.join(out))
PY
}
for b in "$@"; do
  k=${b%%-*}; echo "== $b"
  git merge --no-commit --no-ff "origin/claude/$b" >/dev/null 2>&1
  for f in $(git diff --name-only --diff-filter=U); do
    ext=${f##*.}; n=$(basename "$f" ".$ext"); d=$(dirname "$f")
    case $f in
      shopify-sync/docs/*) union "$f"; git add "$f"; echo "   union: $f";;
      rapporter/beslut-*|shopify-sync/scripts/*) git show "origin/claude/$b:$f" > "$d/$n-$k.$ext"; git checkout -q --ours "$f"; git add "$f" "$d/$n-$k.$ext"; echo "   omdöpt: $d/$n-$k.$ext";;
      *) echo "   OLÖST: $f";;
    esac
  done
  if git diff --name-only --diff-filter=U | grep -q .; then echo "   STOPP: olösta konflikter, avbryter"; git merge --abort; exit 1; fi
  git commit -q -m "Sammanslagning (test): $b" && echo "   ok"
done
