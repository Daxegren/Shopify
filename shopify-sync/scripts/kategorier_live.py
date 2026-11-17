#!/usr/bin/env python3
"""Läser kollektionens live-fält (BARA LÄSNING): titel, handle, SEO, beskrivning, regler, sortering, bild, mall, publicering.
Används av kategorier_skriv.py för före-fil och återläsning."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shopify_api as s

FALT = '''id handle title updatedAt descriptionHtml sortOrder templateSuffix
  seo{title description} image{url altText}
  ruleSet{appliedDisjunctively rules{column relation condition}}
  productsCount{count}'''

def las(k, ids):
    q = 'query($ids:[ID!]!){nodes(ids:$ids){... on Collection{' + FALT + '}}}'
    return k.graphql(q, {'ids': ids})['nodes']

def ovriga_falt(c):
    """Fält som INTE får ändras av en textskrivning."""
    return {'id': c['id'], 'handle': c['handle'], 'title': c['title'], 'sortOrder': c['sortOrder'], 'templateSuffix': c['templateSuffix'],
            'image': c['image'], 'ruleSet': c['ruleSet'], 'productsCount': c['productsCount']}
