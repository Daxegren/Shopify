#!/usr/bin/env python3
"""Jämför före/efter-filer för en regelrättning: kollektion_regel_jamfor.py HANDLE (läser regel_<h>_fore/efter.json). Bara läsning."""
import json, sys, os
d = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'rapporter/shopify-original-2026-11-17/')
h = sys.argv[1]
a = json.load(open(d + f'regel_{h}_fore.json')); b = json.load(open(d + f'regel_{h}_efter.json'))
fa = {m[0]: m for m in a['medlemmar']}; fb = {m[0]: m for m in b['medlemmar']}
bort = [x for x in fa if x not in fb]; ny = [x for x in fb if x not in fa]
print(h, 'medlemmar', len(fa), '->', len(fb), '| köpbara', a['antal_koepbara'], '->', b['antal_koepbara'], '| tillkomna', len(ny))
from collections import Counter
print('borta per typ:', dict(Counter(fa[x][3] for x in bort)))
print('kvarvarande med annan typ än tillåtna:', sorted({fb[x][3] for x in fb}))
print('priser oförändrade för alla kvarvarande:', all(fa[x][5] == fb[x][5] for x in fb if x in fa), '| prisjobb-taggade borta:', sum(1 for x in bort if fa[x][4]))
