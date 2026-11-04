#!/usr/bin/env python3
"""Skriver ut en ASCII-säker productUpdate-mutation som bara ändrar SEO-beskrivningen (meta).

Indata: JSON-lista med id, seo_title (eller titel) och meta_ny. SEO-titeln skickas alltid med (annars tappas metan).
Användning: mutation_meta.py <fil> <start> <antal>   (antal högst 10)
"""
import json, sys

def q(s): return json.dumps(s, ensure_ascii=True)

def main():
    fil, start, antal = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    if antal > 10: sys.exit('högst 10 per anrop')
    d = json.load(open(fil, encoding='utf-8'))[start:start + antal]
    delar = [f'p{i}: productUpdate(product:{{id:"gid://shopify/Product/{x["id"]}", seo:{{title:{q(x["seo_title"])}, description:{q(x["meta_ny"])}}}}}){{product{{id}} userErrors{{field message}}}}' for i, x in enumerate(d)]
    print('mutation { ' + ' '.join(delar) + ' }')

if __name__ == '__main__':
    main()
