import json, sys
base = '/home/user/Shopify/rapporter/facit-bos-2026-10-31/'
tmp = base + 'granskning/tmp_kopia_vag2b6/'
n = sys.argv[1]
fore = {p['id']: p for p in json.load(open('/home/user/Shopify/rapporter/shopify-original-2026-11-03/vag2b_6_fore.json'))}
exp = json.load(open(f'{tmp}forvantat_{n}.json'))
rb = json.load(open(f'{tmp}readback_{n}.json'))
rbm = {p['id']: p for p in rb}
avv = []
if len(rb) != len(exp): avv.append(f'antal {len(rb)} != {len(exp)}')
for e in exp:
    r = rbm.get('gid://shopify/Product/' + e['id'])
    if r is None: avv.append(f"{e['id']} saknas i återläsning"); continue
    f = fore['gid://shopify/Product/' + e['id']]
    if r['title'] != e['titel']: avv.append(f"{e['id']} title")
    exp_seo_t = None if e['seo_title'] == e['titel'] else e['seo_title']
    if r['seo']['title'] != exp_seo_t: avv.append(f"{e['id']} seo.title {r['seo']['title']!r} != {exp_seo_t!r}")
    if r['seo']['description'] != e['meta']: avv.append(f"{e['id']} seo.description")
    if r['descriptionHtml'] != e['html']: avv.append(f"{e['id']} descriptionHtml (tecken {len(r['descriptionHtml'])} vs {len(e['html'])})")
    if r['handle'] != f['handle']: avv.append(f"{e['id']} handle ändrad")
    if r['status'] != 'ACTIVE': avv.append(f"{e['id']} status {r['status']}")
    if r['tags'] != f['tags']: avv.append(f"{e['id']} tags {r['tags']} != {f['tags']}")
print(f'batch {n}: {len(exp)} produkter, avvikelser: {len(avv)}')
for a in avv: print('  ', a)
