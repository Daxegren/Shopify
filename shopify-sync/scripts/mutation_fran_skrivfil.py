#!/usr/bin/env python3
"""Skriver ut en färdig productUpdate-mutation (ASCII-säker, ensure_ascii) för produkter i en skrivfil.

Används tills skrivning går via API-skript. Klistra in UTSKRIFTEN oförändrad i graphql_mutation; skriv aldrig text för hand (R16).
Användning: mutation_fran_skrivfil.py <skrivfil> <start> <antal>   (antal högst 5)
Efteråt kan taggen läggas med: mutation_fran_skrivfil.py <skrivfil> <start> <antal> --tagga
"""
import json, sys

def q(s):
    return json.dumps(s, ensure_ascii=True)

def main():
    a = sys.argv[1:]
    tagga = '--tagga' in a
    a = [x for x in a if x != '--tagga']
    fil, start, antal = a[0], int(a[1]), int(a[2])
    if antal > 5:
        sys.exit('högst 5 produkter per anrop (R16)')
    d = json.load(open(fil, encoding='utf-8'))[start:start + antal]
    delar = []
    for i, x in enumerate(d):
        gid = f'gid://shopify/Product/{x["id"]}'
        if tagga:
            delar.append(f'a{i}: tagsAdd(id:"{gid}", tags:["texter-klara"]){{userErrors{{field message}}}}')
        else:
            seo = f'seo:{{title:{q(x["seo_title"] or x["titel"])}, description:{q(x["meta"])}}}' if x.get('meta') else f'seo:{{title:{q(x["seo_title"] or x["titel"])}}}'
            delar.append(f'p{i}: productUpdate(product:{{id:"{gid}", title:{q(x["titel"])}, {seo}, descriptionHtml:{q(x["html"])}}}){{product{{id}} userErrors{{field message}}}}')
    print('mutation { ' + ' '.join(delar) + ' }')

if __name__ == '__main__':
    main()
