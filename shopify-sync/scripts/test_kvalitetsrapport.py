#!/usr/bin/env python3
"""Tester för kvalitetsrapport.py. Inga nätverksanrop (sockets stängs under testet), inga hemligheter.
Körs: python3 -I shopify-sync/scripts/test_kvalitetsrapport.py
"""
import json, os, socket, sys, tempfile, unittest

HAR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HAR)
import kvalitetsrapport as kr  # noqa: E402

ROT = os.path.abspath(os.path.join(HAR, '..', '..'))
BLOCK = '<h2>Leverans, retur och garanti</h2><p>Frakt och leverans. Retur: 14 dagar. Reklamation: kontakta oss. Säljare: Testbutiken AB.</p>'
PROFIL = {
    'butik': 'testbutiken.se', 'marken': ['Hammer', 'BH Fitness'], 'marken_varning_bara': [], 'marken_versaler_tillatna': {'SOKE': 'ok'},
    'gransvarden': {'titel_max': 30, 'titel_max_komma': 1, 'seo_titel_max': 20, 'meta_min': 20, 'meta_max': 60},
    'standardblock_krav': ['Leverans, retur och garanti', 'Frakt och leverans', 'Retur:', 'Reklamation:', 'Säljare:'],
    'klartagg': 'texter-klara', 'utanfor_tills_vidare': ['kategori X'],
}


def post(i, nr, titel='Hantel Hammer 5 kg', seo='Hantel Hammer 5 kg', meta='Hantel på 5 kg i gjutjärn med grepp.', html=None):
    return {'id': str(i), 'nr': nr, 'titel': titel, 'seo_title': seo, 'meta': meta,
            'html': html if html is not None else '<p>Hammer hantel väger 5 kg och har gummerat grepp.</p>' + BLOCK}


def skriv(sokvag, data):
    os.makedirs(os.path.dirname(sokvag), exist_ok=True)
    with open(sokvag, 'w', encoding='utf-8') as f:
        if isinstance(data, str):
            f.write(data)
        else:
            json.dump(data, f, ensure_ascii=False)


def oversikt(katalog):
    ut = {}
    for r, _, fs in os.walk(katalog):
        for f in fs:
            with open(os.path.join(r, f), 'rb') as fh:
                ut[os.path.join(r, f)] = fh.read()
    return ut


class Nat(unittest.TestCase):
    """Stänger alla sockets under varje test: bevisar att rapporten inte behöver nätverk."""
    def setUp(self):
        self._orig = socket.socket
        def forbjud(*a, **k):
            raise AssertionError('nätverksanrop är inte tillåtet')
        socket.socket = forbjud

    def tearDown(self):
        socket.socket = self._orig


class Hjalpfunktioner(Nat):
    def test_sifferid(self):
        self.assertEqual(kr.sifferid('gid://shopify/Product/123'), '123')
        self.assertEqual(kr.sifferid(456), '456')

    def test_proc_och_tal(self):
        self.assertEqual(kr.proc(1, 2), '50 %')
        self.assertEqual(kr.proc(0, 0), '–')
        self.assertEqual(kr.proc(1, 1000), '<1 %')
        self.assertEqual(kr.proc(1, 3, 1), '33,3 %')
        self.assertEqual(kr.tal(2614), '2 614')

    def test_rensa_tar_bort_hemligheter_och_personuppgifter(self):
        t = kr.rensa('Mejla anna.svensson@example.com eller ring 070-123 45 67. shpat_abcdef1234567890 client_secret=hemligt123 ' + 'a' * 40)
        self.assertNotIn('@', t)
        self.assertNotIn('070-123', t)
        self.assertNotIn('shpat_', t)
        self.assertNotIn('hemligt123', t)
        self.assertNotIn('a' * 40, t)

    def test_rensa_lamnar_produktdata(self):
        t = '12345678 EAN 7340012345678 Hantel 5 kg, 100 x 100 cm'
        self.assertEqual(kr.rensa(t), t)

    def test_text_ur_html_klipper_standardblock(self):
        t = kr.text_ur_html('<p>Hej &amp; hå</p>' + BLOCK, 'Leverans, retur och garanti')
        self.assertEqual(t, 'Hej & hå')

    def test_klassa_avvisad_tidigaste_ordet(self):
        self.assertEqual(kr.klassa_avvisad('Knäskydd för säkerhet; dessutom dubblett med 8129'), 'Säkerhet och skydd')
        self.assertEqual(kr.klassa_avvisad('Dubblett av 123, samma SKU'), 'Dubblett av annan annons')
        self.assertEqual(kr.klassa_avvisad('Barnprodukt med oklar typ'), 'Barn och ungdom')
        self.assertEqual(kr.klassa_avvisad('helt annat'), 'Övrigt')
        self.assertEqual(kr.klassa_avvisad(None), 'Övrigt')

    def test_rattningstyp(self):
        self.assertEqual(kr.rattningstyp('Gul Boll', 'gul boll!'), 'format')
        self.assertEqual(kr.rattningstyp('Gul boll', 'Röd boll'), 'innehåll')
        self.assertEqual(kr.rattningstyp(None, 'x'), 'innehåll')

    def test_ordning_korrigeringar_sist(self):
        filer = ['/x/k_skriv_korr1.json', '/x/k_skriv_02.json', '/x/k_skriv_01.json', '/x/f_skriv_1fix.json']
        o = [os.path.basename(f) for f in kr.ordna_skrivfiler(filer, {'k_skriv_02': '2026-11-05', 'k_skriv_01': '2026-11-04'}, ['korr', 'fix'])]
        self.assertEqual(o, ['k_skriv_01.json', 'k_skriv_02.json', 'f_skriv_1fix.json', 'k_skriv_korr1.json'])

    def test_stam_fran_resultatfil(self):
        self.assertEqual(kr.stam('/a/k_skriv_13_resultat_rest.json'), 'k_skriv_13')
        self.assertEqual(kr.stam('/a/k_skriv_01a_fore_dry-run.json'), 'k_skriv_01a')


class Kontroller(Nat):
    def kor(self, p, sparr=None, profil=None):
        return {k for k, _ in kr.kontrollera_produkt(p, profil or dict(PROFIL), sparr or {}, PROFIL['marken_versaler_tillatna'],
                                                       kr.FORBJUDNA_STANDARD, 2, 'enligt tillverkaren')}

    def test_felfri_produkt(self):
        self.assertEqual(self.kor(post(1, 1, titel='Hantel Hammer 5 kg', seo='Hantel Hammer 5 kg')), set())

    def test_langder_ur_profilen(self):
        k = self.kor(post(1, 1, titel='T' * 31, seo='S' * 21, meta='kort'))
        self.assertTrue({'TITEL_LANG', 'SEO_LANG', 'META_LANGD'} <= k)

    def test_meta_saknas_ar_egen_kontroll(self):
        self.assertIn('META_SAKNAS', self.kor(post(1, 1, meta=None)))

    def test_kommatecken_utan_decimaltal(self):
        self.assertNotIn('TITEL_KOMMA', self.kor(post(1, 1, titel='Boll 60,5 cm, svart', seo='Boll')))
        self.assertIn('TITEL_KOMMA', self.kor(post(1, 1, titel='Boll, svart, stor', seo='Boll')))

    def test_standardblock(self):
        self.assertIn('BLOCK', self.kor(post(1, 1, html='<p>Hammer hantel.</p>')))

    def test_marke_versaler_med_undantag(self):
        self.assertIn('VERSALER', self.kor(post(1, 1, titel='Hantel HAMMER 5 kg')))
        self.assertNotIn('VERSALER', self.kor(post(1, 1, titel='Hantel SOKE 5 kg')))

    def test_osynligt_tecken(self):
        self.assertIn('OSYNLIG', self.kor(post(1, 1, html='<p>ho­j</p>' + BLOCK)))

    def test_attribuering_max_tva(self):
        h = '<p>' + ' enligt tillverkaren'.join(['a'] * 4) + '</p>' + BLOCK
        self.assertIn('ATTRIBUERING', self.kor(post(1, 1, html=h)))

    def test_forbjudet_och_cirkular(self):
        self.assertIn('FORBJUDET', self.kor(post(1, 1, html='<p>Vanliga frågor</p>' + BLOCK)))
        self.assertIn('CIRKULAR', self.kor(post(1, 1, html='<p>Hammer Boll är en Hammer Boll.</p>' + BLOCK)))

    def test_sparrad_och_kand(self):
        self.assertIn('SPARRAD', self.kor(post(7, 7), {'7': [('pilot', False)]}))
        self.assertIn('SPARRAD_KAND', self.kor(post(7, 7), {'7': [('pilot', True)]}))

    def test_dubbletter(self):
        senast = {'1': (post(1, 1), 'a'), '2': (post(2, 2), 'a'), '3': (post(3, 3, titel='Annan titel', seo='Annan', meta='En helt annan meta text här.'), 'a')}
        res = kr.kontrollera_alla(senast, dict(PROFIL), {}, [], 2, 'enligt tillverkaren')
        self.assertEqual({x[0] for x in res['DUBBLETT_TITEL']}, {'1', '2'})
        self.assertEqual({x[0] for x in res['DUBBLETT_META']}, {'1', '2'})

    def test_butiksoberoende_andra_gransvarden(self):
        p2 = dict(PROFIL, gransvarden={'titel_max': 100, 'titel_max_komma': 5, 'seo_titel_max': 100, 'meta_min': 5, 'meta_max': 300})
        p = post(1, 1, titel='T' * 50, seo='S' * 50)
        a = {k for k, _ in kr.kontrollera_produkt(p, dict(PROFIL), {}, {}, [], 2, 'enligt tillverkaren')}
        b = {k for k, _ in kr.kontrollera_produkt(p, p2, {}, {}, [], 2, 'enligt tillverkaren')}
        self.assertIn('TITEL_LANG', a)
        self.assertNotIn('TITEL_LANG', b)


class Tolkning(Nat):
    def test_sammanfatta_utlatanden(self):
        u = [('f', {'id': '1', 'dom': 'GODKÄND', 'rattningar': {}, 'skal': 'ok R4'}),
             ('f', {'id': '2', 'dom': 'RÄTTA', 'rattningar': {'html 1': {'fore': 'Gul boll', 'efter': 'gul boll'}, 'meta': [{'fore': 'a', 'efter': 'b'}]}, 'skal': 'cirkulär inledning R11'}),
             ('f', {'id': '3', 'dom': 'UNDERKÄND', 'rattningar': {}, 'skal': 'R3'})]
        s = kr.sammanfatta_utlatanden(u)
        self.assertEqual(s['dom']['GODKÄN'], 1)
        self.assertEqual(s['unika'], 3)
        self.assertEqual(s['typer']['format'], 1)
        self.assertEqual(s['typer']['innehåll'], 1)
        self.assertEqual(s['falt']['html'], 1)
        self.assertEqual(s['regelref']['R4'], 1)
        self.assertEqual(s['orsaker']['Cirkulär eller svag inledning'], 1)

    def test_resultat_bada_nyckelvarianter(self):
        with tempfile.TemporaryDirectory() as d:
            skriv(d + '/a_resultat_rest.json', {'lage': '--rest', 'datum': '2026-11-05T01:00:00', 'skrivna_taggade_verifierade': ['1', '2'], 'avvikelser': [], 'redan_lika': ['3'], 'hoppade_over': [], 'anrop': 4})
            skriv(d + '/b_resultat_rest.json', {'lage': '--rest', 'datum': '2026-11-05T02:00:00', 'skrivna_och_verifierade': ['4'], 'avvikelser': ['x'], 'redan_klara': ['5'], 'hoppade_over': ['6'], 'anrop': 1})
            a = kr.tolka_resultat(d + '/a_resultat_rest.json', [])
            b = kr.tolka_resultat(d + '/b_resultat_rest.json', [])
        self.assertEqual((a['skrivna'], a['lika'], a['anrop']), (['1', '2'], ['3'], 4))
        self.assertEqual((b['skrivna'], b['lika'], b['avvikelser'], b['hoppade']), (['4'], ['5'], ['x'], ['6']))

    def test_stickprov_text_och_json(self):
        with tempfile.TemporaryDirectory() as d:
            skriv(d + '/stickprov_a.md', '# Stickprov A\nTotalt 33 av 33 produkter lästa live.\n**Ingen** avvikelse.\n- fynd (A, x) och (B)\n')
            skriv(d + '/stickprov_b.json', {'namn': 'B', 'lasta': 10, 'jamforda': 9, 'avvikelser': 1, 'skrivfiler': ['k_skriv_1']})
            a = kr.tolka_stickprov(d + '/stickprov_a.md', [])
            b = kr.tolka_stickprov(d + '/stickprov_b.json', [])
        self.assertEqual((a['jamforda'], a['lasta'], a['avvikelser']), (33, 33, 0))
        self.assertEqual(a['fynd'], {'A': 1, 'B': 1})
        self.assertFalse(a['maskinlasbar'])
        self.assertTrue(b['maskinlasbar'])
        self.assertEqual((b['jamforda'], b['lasta'], b['avvikelser']), (9, 10, 1))

    def test_skrivrapport_bada_ordningar(self):
        self.assertEqual(kr.tolka_skrivrapport('24 av 24 identiska med skrivfilen'), (24, 24))
        self.assertEqual(kr.tolka_skrivrapport('identiska med skrivfilen på 23 av 24'), (23, 24))
        self.assertIsNone(kr.tolka_skrivrapport('inget här'))

    def test_efterkontroll(self):
        e = kr.tolka_efterkontroll('- Kontrollerade produkter: 2614\n- Kända avvikelser (baslinjen): 90\n- **Nya avvikelser: 0**\n')
        self.assertEqual(list(e.values()), [2614, 90, 0])

    def test_original_filtreras(self):
        senast = {'1': (post(1, 1, titel='Ny', ), 'f'), '2': (post(2, 2), 'f')}
        fore = [('a', {'id': 'gid://shopify/Product/1', 'title': 'Gammal', 'tags': ['texter-klara'], 'descriptionHtml': 'x'}),   # efter skrivning: taggen finns
                ('b', {'id': 'gid://shopify/Product/1', 'title': 'Gammal', 'tags': [], 'descriptionHtml': 'x'}),
                ('c', {'id': 'gid://shopify/Product/2', 'title': senast['2'][0]['titel'], 'tags': [], 'descriptionHtml': senast['2'][0]['html']})]   # lika med slutlig text
        o = kr.valj_original(fore, senast, 'texter-klara')
        self.assertEqual(list(o), ['1'])
        self.assertEqual(o['1']['tags'], [])

    def test_exempelurval_ar_deterministiskt(self):
        orig = {str(i): {} for i in range(50)}
        a = kr.valj_exempel(orig, {}, 5, 'x')
        self.assertEqual(a, kr.valj_exempel(orig, {}, 5, 'x'))
        self.assertNotEqual(a, kr.valj_exempel(orig, {}, 5, 'y'))


class HTML(Nat):
    def test_md_till_html_tabell_rubrik_escape(self):
        md = '# Titel <b>\n\n| A | B |\n|---|---|\n| 1 | **x** |\n\n- punkt `kod`\n'
        h = kr.md_till_html(md, 'T')
        self.assertIn('<h1>Titel &lt;b&gt;</h1>', h)
        self.assertIn('<th>A</th>', h)
        self.assertIn('<td><strong>x</strong></td>', h)
        self.assertIn('<li>punkt <code>kod</code></li>', h)
        self.assertIn('prefers-color-scheme:dark', h)
        self.assertNotIn('<b>', h.split('</style>')[1].replace('<strong>', ''))


class EndToEnd(Nat):
    def bygg(self, d):
        v = d + '/kors'
        skriv(d + '/profil.json', PROFIL)
        skriv(d + '/regler.md', '# Regelbok\n- R1 (G) Bara uppgifter ur källan.\n- R2 (T) Längder.\n')
        with open(d + '/spar.csv', 'w', encoding='utf-8') as f:
            f.write('produkt_id\n3\n')
        skriv(d + '/sparr.json', {'sparrar': [{'namn': 'pilot', 'aktiv': True, 'idfil': 'spar.csv', 'idkolumn': 'produkt_id', 'skal': 'Mäts senare', 'beslut': 'ägaren', 'kanda_overtradelser': []}]})
        skriv(v + '/b1_in.json', [{'id': str(i), 'nr': i} for i in range(1, 7)])
        skriv(v + '/b1_utkast.json', [{'id': '1'}, {'id': '2'}, {'id': '3'}])
        skriv(v + '/b1_avvisade.json', [{'id': '5', 'nr': 5, 'skäl': 'Barnprodukt, R6'}, {'id': '6', 'nr': 6, 'avvisningsskal': 'Dubblett av 1, R12a'}])
        skriv(v + '/b1_utlatande.json', [{'id': '1', 'dom': 'GODKÄND', 'rattningar': {}, 'skal': 'ok'},
                                         {'id': '2', 'dom': 'RÄTTA', 'rattningar': {'meta': {'fore': 'a b', 'efter': 'a c'}}, 'skal': 'R5 enligt tillverkaren'},
                                         {'id': '3', 'dom': 'UNDERKÄND', 'rattningar': {}, 'skal': 'R3'}])
        skriv(v + '/b1_skriv.json', [post(1, 1), post(2, 2, titel='Matta Hammer 10 kg', seo='Matta Hammer', meta='Matta på 10 kg i gummi med grepp.'),
                                      post(3, 3, titel='Boll Hammer 1 kg', seo='Boll Hammer', meta='Boll på 1 kg i gummi med ytterst grepp.')])
        skriv(v + '/b1_skriv_korr1.json', [post(2, 2, titel='Matta Hammer 11 kg', seo='Matta Hammer', meta='Matta på 11 kg i gummi med grepp.')])
        skriv(v + '/original/b1_fore.json', [{'id': 'gid://shopify/Product/1', 'title': 'HANTEL', 'tags': [], 'seo': {'title': None, 'description': None},
                                              'descriptionHtml': '<p>Kontakta sven.larsson@example.com eller 070-123 45 67.</p>'},
                                             {'id': 'gid://shopify/Product/2', 'title': 'MATTA', 'tags': [], 'seo': {'title': None, 'description': 'gammal meta'}, 'descriptionHtml': '<p>Gammal text</p>'}])
        skriv(v + '/original/b1_resultat_rest.json', {'lage': '--rest', 'datum': '2026-11-05T01:00:00', 'skrivna_taggade_verifierade': ['1', '2'], 'avvikelser': [], 'redan_lika': [], 'hoppade_over': [], 'anrop': 3})
        skriv(v + '/stickprov_1.md', '# Stickprov 1\nLästa 3 av 3 produkter, jämförda mot b1_skriv.json.\nInga avvikelser.\n')
        skriv(d + '/fragor.json', [{'id': 'F1', 'datum': '2026-11-05', 'fraga': 'Ska pilot hävas?', 'status': 'öppen'}, {'id': 'F2', 'datum': 'x', 'fraga': 'klar', 'status': 'avklarad'}])
        manifest = {'namn': 'Testkörning', 'butik': 'Testbutiken', 'profil': 'profil.json', 'sparrlista': 'sparr.json', 'regelbok': 'regler.md',
                    'inventering': ['kors/*_in.json'], 'utkast': ['kors/*_utkast.json'], 'avvisade': ['kors/*_avvisade.json'], 'utlatanden': ['kors/*utlatande*.json'],
                    'skrivfiler': ['kors/*skriv*.json'], 'korrigeringsmonster': ['korr'], 'fore': ['kors/original/*fore*.json'], 'resultat': ['kors/original/*resultat*.json'],
                    'stickprov': ['kors/stickprov*.md'], 'oppna_fragor': 'fragor.json', 'exempel': {'antal': 2, 'fro': 'a'}}
        skriv(d + '/manifest.json', manifest)
        return d + '/manifest.json'

    def test_hela_flodet(self):
        with tempfile.TemporaryDirectory() as d:
            mf = self.bygg(d)
            md, u = kr.kor(mf, d, '2026-11-06')
            md2, _ = kr.kor(mf, d, '2026-11-06')
        self.assertEqual(md, md2, 'rapporten ska vara deterministisk')
        self.assertEqual(u['skrivna'], {'1', '2', '3'})
        self.assertEqual(set(u['kvar_avvisade']), {'5', '6'})
        self.assertEqual(u['senast']['2'][0]['titel'], 'Matta Hammer 11 kg', 'rättningsfilen väger tyngst')
        self.assertEqual(u['korr_ids'], {'2'})
        self.assertEqual(u['verifierade_skrivna'], {'1', '2'})
        self.assertEqual(u['utan_maskinresultat'], {'3'})
        self.assertEqual([k for k, v in u['kontroller'].items() if v and k != 'META_SAKNAS'], ['SPARRAD'])
        for rubrik in ('## Sammanfattning', '## 1. Omfattning', '## 2. Före och efter', '## 3. Regler som tillämpats', '## 4. Kontrollresultat',
                       '## 5. Granskning före skrivning', '## 6. Återläsning och stickprov', '## 7. Mätetal', '## 8. Avvisade produkter och varför',
                       '## 9. Vad som kräver ditt beslut', '## Svagheter och osäkerheter'):
            self.assertIn(rubrik, md)
        self.assertIn('Ska pilot hävas?', md)
        self.assertNotIn('klar', md.split('Öppna frågor')[1].split('Grupper')[0].replace('klara', ''))
        self.assertIn('R1', md)
        self.assertIn('Spärrad produkt har fått text', md)
        self.assertIn('Barn och ungdom', md)
        self.assertIn('Dubblett av annan annons', md)
        self.assertIn('Återläsning saknas i maskinläsbar form för 1 av 3', md)

    def test_inga_personuppgifter_i_rapporten(self):
        with tempfile.TemporaryDirectory() as d:
            md, _ = kr.kor(self.bygg(d), d, '2026-11-06')
        self.assertNotIn('sven.larsson', md)
        self.assertNotIn('070-123', md)
        self.assertNotIn('@example.com', md)

    def test_cli_skriver_md_och_html(self):
        with tempfile.TemporaryDirectory() as d:
            mf = self.bygg(d)
            import contextlib, io
            with contextlib.redirect_stdout(io.StringIO()):
                kr.main(['--manifest', mf, '--rot', d, '--ut', d + '/ut/rapport.md', '--html', '--datum', '2026-11-06'])
            self.assertTrue(os.path.getsize(d + '/ut/rapport.md') > 1000)
            with open(d + '/ut/rapport.html', encoding='utf-8') as fh:
                h = fh.read()
        self.assertTrue(h.startswith('<!doctype html>'))
        self.assertIn('<title>Testkörning</title>', h)

    def test_tomt_material_ger_rapport_utan_krasch(self):
        with tempfile.TemporaryDirectory() as d:
            skriv(d + '/m.json', {'namn': 'Tom', 'butik': 'Tom butik', 'skrivfiler': ['finns/inte/*.json']})
            md, u = kr.kor(d + '/m.json', d, '2026-11-06')
        self.assertIn('## Svagheter och osäkerheter', md)
        self.assertIn('Inga filer matchar', md)
        self.assertEqual(len(u['skrivna']), 0)

    def test_trasig_fil_stoppar_inte(self):
        with tempfile.TemporaryDirectory() as d:
            self.bygg(d)
            skriv(d + '/kors/trasig_skriv.json', '{ inte json')
            md, u = kr.kor(d + '/manifest.json', d, '2026-11-06')
        self.assertIn('trasig_skriv.json', md)
        self.assertEqual(len(u['skrivna']), 3)

    def test_ingen_indatafil_andras(self):
        with tempfile.TemporaryDirectory() as d:
            mf = self.bygg(d)
            fore = oversikt(d)
            kr.kor(mf, d, '2026-11-06')
            efter = oversikt(d)
        self.assertEqual(fore, efter)


class RiktigaData(Nat):
    def test_bestofsports_om_data_finns(self):
        mf = os.path.join(ROT, 'shopify-sync/config/kvalitetsrapport-bestofsports.json')
        if not (os.path.exists(mf) and os.path.isdir(os.path.join(ROT, 'rapporter/facit-bos-2026-10-31/vag2_skriv'))):
            self.skipTest('BEST OF SPORTS-data finns inte i den här kopian')
        md, u = kr.kor(mf, ROT, '2026-11-06')
        self.assertGreater(len(u['skrivna']), 2000)
        self.assertNotRegex(md, r'[\w.+-]+@[\w-]+\.[a-z]{2,}')
        self.assertNotRegex(md, r'shp[a-z]{1,3}_[A-Za-z0-9]{8,}')
        self.assertIn('Svagheter och osäkerheter', md)


if __name__ == '__main__':
    unittest.main(verbosity=1)
