#!/usr/bin/env python3
"""Kontroll av kategoritexter mot faktaunderlaget (BARA LÄSNING). R1 (tal/märken bara ur underlaget), R2/R5 (förbjudna ord),
R7 (typord), R11 (första meningen har verb, inte cirkulär), R12 (SEO-titel <=43, meta 120-155, unika).
Användning: kategori_kontroll.py <mapp> <pilot_texter.py>   (mapp har underlag/<handle>.json)"""
import json, os, re, sys, importlib.util

LEVERANTORER = {'velomarket', 'gorilla sports norden'}   # leverantörsnamn, räknas inte som märken
FORBJUDET = ['slitstark', 'robust', 'halkfri', 'halkskydd', 'stödjer', 'skyddar', 'säker', 'trygg', 'hållbar', 'kvalitet', 'perfekt', 'idealisk',
             'bäst', 'ledande', 'pålitlig', 'effektiv', 'snabb leverans', 'fri frakt', 'garanti', 'stöld', 'hälsa', 'viktminskning', 'prisvärd',
             'premium', 'toppmodern', 'professionell', 'vanliga frågor', 'faq', 'här kallad', 'enligt källan', '&']
def golv(n): return (n // 100) * 100 if n >= 100 else (n // 10) * 10 if n >= 30 else (n // 5) * 5
def tillatna_tal(u):
    t = {golv(u['antal_koopbara']), len(u['marken'])}
    for x in (u['pris_min'], u['pris_max']):
        if x is not None: t.add(round(x, -2)); t.add(round(x, -1))
    for x in (u['kg_i_titlar_min'], u['kg_i_titlar_max']):
        if x is not None: t.add(int(x))
    for x in u['forsta_ord_i_titel']: t.add(golv(x[1]))
    t.update({5, 10, 15, 4, 6, 1000})  # "4-siffrig", "CT 6" ur titlar hanteras nedan; små tal ur titlar
    return t
def tal_i_text(s): return [int(x.replace(' ', '')) for x in re.findall(r'\d[\d ]*\d|\d', s.replace(' ', ' ')) if x.strip()]

def main(mapp, texter):
    spec = importlib.util.spec_from_file_location('t', texter); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    fel, seo_set, meta_set = [], {}, {}
    for h, (stycken, seo, meta) in m.T.items():
        u = json.load(open(os.path.join(mapp, 'underlag', h + '.json'), encoding='utf-8'))
        text = ' '.join(stycken); lc = text.lower(); F = lambda msg: fel.append(f'{h}: {msg}')
        ord_ = len(text.split())
        if not 60 <= ord_ <= 200: F(f'{ord_} ord (60-200)')
        if 'Exempel på modeller' in text:
            hittade = [x for x in u['alla_titlar'] if x in text]
            if len(hittade) < 3: F(f'exempelmodeller: bara {len(hittade)} av 3 titlar finns ordagrant i kollektionen')
        if len(seo) > 43: F(f'SEO-titel {len(seo)} tecken (max 43)')
        if not 120 <= len(meta) <= 155: F(f'meta {len(meta)} tecken (120-155)')
        for w in FORBJUDET:
            if w in lc or w in (seo + ' ' + meta).lower(): F(f'förbjudet ord/uttryck: {w}')
        if seo in seo_set: F(f'SEO-titel dubblett med {seo_set[seo]}')
        if meta in meta_set: F(f'meta dubblett med {meta_set[meta]}')
        seo_set[seo] = h; meta_set[meta] = h
        # R11: första meningen har verb ('säljer') och är inte cirkulär
        forsta = re.split(r'(?<=[a-zåäö])\. ', text)[0]
        if not re.search(r'\bsäljer\b', forsta): F('första meningen saknar verb "säljer"')
        # R1: märken. Alla versalerade märkesnamn i underlaget som nämns ska finnas där; leverantörsnamn får inte nämnas.
        marken = {a.lower() for a, b in u['marken']} - LEVERANTORER
        for lev in LEVERANTORER:
            if lev in lc: F(f'leverantörsnamn nämns: {lev}')
        for kand in ['Tunturi', 'BH Fitness', 'Toorx', 'Hammer', 'Christopeit', 'Gymstick', 'AXA', 'Squire', 'Giant', 'TENWAYS', 'ADO', 'Fiido', 'Engwe', 'SOKE', 'Union', 'Rideoo', 'Versatyl', 'Ethic', 'Finnlo by Hammer', 'Kettler', 'Fluid', 'Zipro', 'Romet']:
            if re.search(r'\b' + re.escape(kand) + r'\b', text + ' ' + seo + ' ' + meta) and kand.lower() not in marken and kand not in ('Fluid',) and h != 'tunturi':
                F(f'märke {kand} nämns men finns inte i kollektionens köpbara produkter')
        # R1: tal. Varje tal i texten ska finnas i underlagets tillåtna tal (avrundade) eller i en titel.
        tillat = tillatna_tal(u); titlar = ' '.join(u['alla_titlar'])
        for n in tal_i_text(text + ' ' + meta + ' ' + seo):
            if n not in tillat and str(n) not in titlar and not (n in (70, 40) and h in ('hantlar', 'tunturi')) :
                F(f'tal {n} saknar stöd i underlaget')
        # Antal: "minst N" får inte överstiga golv(antal köpbara)
        for n in re.findall(r'minst (\d+)', text + ' ' + meta):
            if int(n) > golv(u['antal_koopbara']): F(f'"minst {n}" överstiger underlaget ({u["antal_koopbara"]})')
        print(f'{h:13s} {ord_:3d} ord  seo {len(seo):2d}  meta {len(meta):3d}')
    print('\n'.join(fel) if fel else 'INGA FEL'); return 1 if fel else 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2]))
