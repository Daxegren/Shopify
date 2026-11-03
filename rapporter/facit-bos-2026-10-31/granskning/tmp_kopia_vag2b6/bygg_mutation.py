import json, sys
base = '/home/user/Shopify/rapporter/facit-bos-2026-10-31/'
skriv = json.load(open(base + 'vag2_skriv/b_skriv_6.json'))
q = lambda s: json.dumps(s, ensure_ascii=False)
# Kanarie 3 först, sedan högst 8 per dokument och max 16000 tecken per dokument
def doc(grupp):
    rader = []
    for i, p in enumerate(grupp):
        parts = [f'id: {q("gid://shopify/Product/" + p["id"])}', f'title: {q(p["titel"])}']
        if p["seo_title"] == p["titel"] and p["meta"] is None:
            pass  # seo utelämnas, Shopify lagrar null
        elif p["seo_title"] == p["titel"]:
            parts.append(f'seo: {{title: {q(p["titel"])}, description: {q(p["meta"])}}}')  # lika med titeln lagras som null; metan behålls
        elif p["meta"] is None:
            parts.append(f'seo: {{title: {q(p["seo_title"])}}}')
        else:
            parts.append(f'seo: {{title: {q(p["seo_title"])}, description: {q(p["meta"])}}}')
        parts.append(f'descriptionHtml: {q(p["html"])}')
        rader.append(f'  p{i+1}: productUpdate(product: {{{", ".join(parts)}}}) {{ product {{ id }} userErrors {{ field message }} }}')
    return 'mutation {\n' + '\n'.join(rader) + '\n}'
kanarie = skriv[:3]
resten = skriv[3:]
batcher = [kanarie]
grupp = []
for p in resten:
    kand = grupp + [p]
    if len(kand) > 8 or len(doc(kand)) > 16000:
        batcher.append(grupp); grupp = [p]
    else:
        grupp = kand
if grupp: batcher.append(grupp)
for n, g in enumerate(batcher):
    d = doc(g)
    assert len(d) <= 16384, (n, len(d))
    open(f'/home/user/Shopify/rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2b6/mut_{n}.graphql', 'w').write(d)
    json.dump([{'id': p['id'], 'titel': p['titel'], 'seo_title': p['seo_title'], 'meta': p['meta'], 'html': p['html']} for p in g],
              open(f'/home/user/Shopify/rapporter/facit-bos-2026-10-31/granskning/tmp_kopia_vag2b6/forvantat_{n}.json', 'w'), ensure_ascii=False)
    print(n, len(g), len(d), [p['nr'] for p in g])
