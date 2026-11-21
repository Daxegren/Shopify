#!/usr/bin/env python3
"""Kontrollerad skrivning av en skrivfil med skydd för prisjobbet. Använder shopify_skriv_texter.py för själva skrivningen.
Före varje körning: läser taggar live och stoppar om någon produkt i skrivfilen bär price-change-job-active; sparar varje variants pris
och jämförpris. Efter körning: läser priserna igen och stoppar (kod 1) om något skiljer.
Användning: skriv_med_priskontroll.py SKRIVFIL (--dry-run | --kanarie | --rest) --ut KATALOG"""
import json, os, subprocess, sys
HAR = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HAR)
import shopify_api as api, butiksprofil  # noqa: E402
from shopify_beskrivning_rader import hamta_priser, SKYDDSTAGG  # noqa: E402


def main(a):
    fil, lage = a[0], a[1]
    ut = a[a.index('--ut') + 1]
    poster = json.load(open(fil, encoding='utf-8'))
    ids = [p['id'] for p in poster]
    profil, _ = butiksprofil.profil_fran_argv([])
    k = api.klient_fran_profil(profil)
    print('Butik:', api.verifiera_butik(k))
    live = api.hamta_produkter(k, ids)
    skyddade = [api.sifferid(l['id']) for l in live if l and SKYDDSTAGG in l['tags']]
    if skyddade:
        print('STOPP: skyddstagg på', skyddade); return 1
    fore = hamta_priser(k, ids)
    r = subprocess.run([sys.executable, '-I', os.path.join(HAR, 'shopify_skriv_texter.py'), fil, lage, '--ut', ut])
    efter = hamta_priser(k, ids)
    diff = [i for i in ids if fore.get(i) != efter.get(i)]
    print('PRISER:', 'OFÖRÄNDRADE för alla %d' % len(ids) if not diff else f'ÄNDRADE för {diff}')
    json.dump({'lage': lage, 'priser_fore': fore, 'priser_efter': efter}, open(os.path.join(ut, os.path.splitext(os.path.basename(fil))[0] + f'_priser_{lage.strip("-")}.json'), 'w'), indent=1)
    return 1 if diff else r.returncode


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
