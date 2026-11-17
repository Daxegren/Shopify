#!/usr/bin/env python3
"""Enhetstester utan nätverk för kategorier_vag2.py.
Körning: python3 shopify-sync/scripts/test_kategorier_vag2.py"""
import csv, json, os, sys, tempfile, unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kategorier_vag2 as v


def skriv_csv(sokvag, rubriker, rader):
    with open(sokvag, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f); w.writerow(rubriker); w.writerows(rader)


class Grund(unittest.TestCase):
    def test_tal_svenska_och_engelska(self):
        self.assertEqual(v.tal('1 234'), 1234.0)
        self.assertEqual(v.tal('1\xa0234'), 1234.0)
        self.assertEqual(v.tal('45,3'), 45.3)
        self.assertEqual(v.tal('1.234,5'), 1234.5)
        self.assertEqual(v.tal(''), 0.0)
        self.assertEqual(v.tal(None), 0.0)

    def test_handle_av_url(self):
        self.assertEqual(v.handle_av('https://bestofsports.se/collections/Kettlebell?page=2'), 'kettlebell')
        self.assertEqual(v.handle_av('/collections/hantlar/tunturi'), 'hantlar')
        self.assertEqual(v.handle_av('hantlar'), 'hantlar')

    def test_narhet(self):
        self.assertEqual(v.narhet(0), 0.0)
        self.assertEqual(v.narhet(5), 0.3)
        self.assertEqual(v.narhet(10), 1.0)
        self.assertEqual(v.narhet(30), 1.0)
        self.assertAlmostEqual(v.narhet(55), 0.5)
        self.assertEqual(v.narhet(80), 0.0)
        self.assertEqual(v.narhet(200), 0.0)

    def test_potential_foredrar_narhet(self):
        # position 26 med 1200 visningar slår position 70 med 4000 visningar
        self.assertGreater(v.potential(1200, 26), v.potential(4000, 70))


class Gsc(unittest.TestCase):
    def test_lasa_gsc_summerar_dubbletter_och_viktar_position(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, 'g.csv')
            skriv_csv(p, ['handle', 'klick', 'visningar', 'position'],
                      [['https://x.se/collections/a', '1', '100', '20'], ['a', '2', '300', '40'], ['b', '0', '10', '5,5']])
            g = v.lasa_gsc(p)
        self.assertEqual(g['a']['klick'], 3)
        self.assertEqual(g['a']['visningar'], 400)
        self.assertEqual(g['a']['position'], 35.0)   # (20*100 + 40*300) / 400
        self.assertEqual(g['b']['position'], 5.5)


PRIO = [
    {'klass': '1 pilot', 'handle': 'kettlebell', 'titel': 'Kettlebell', 'koopbara': '32'},
    {'klass': '2 våg 2 (20+ köpbara)', 'handle': 'hybridcykel', 'titel': 'Hybridcykel', 'koopbara': '53'},
    {'klass': '3 våg 3 (5-19 köpbara)', 'handle': 'traningsbank', 'titel': 'Träningsbänk', 'koopbara': '18'},
    {'klass': '3 våg 3 (5-19 köpbara)', 'handle': 'juniorcyklar', 'titel': 'Juniorcykel', 'koopbara': '14'},
    {'klass': '6 utanför tills vidare (R6/profil)', 'handle': 'pre-workout-pwo', 'titel': 'PWO', 'koopbara': '7'},
    {'klass': '4 överlappar annan kollektion: avgör struktur först', 'handle': 'skivstangsset', 'titel': 'Set', 'koopbara': '7'},
    {'klass': '5 få produkter (1-4): hantera först', 'handle': 'skivstangsstallning', 'titel': 'Ställning', 'koopbara': '3'},
    {'klass': '5 tom: hantera först (ta bort, slå ihop eller fyll)', 'handle': 'pool', 'titel': 'Pool', 'koopbara': '0'},
    {'klass': '3 våg 3 (5-19 köpbara)', 'handle': 'lagt-lage', 'titel': 'Redan högt', 'koopbara': '10'},
]
GSC = {
    'kettlebell': {'klick': 0, 'visningar': 1884, 'position': 66},
    'hybridcykel': {'klick': 0, 'visningar': 2202, 'position': 47},
    'traningsbank': {'klick': 0, 'visningar': 3432, 'position': 59},
    'juniorcyklar': {'klick': 0, 'visningar': 1154, 'position': 34},
    'pre-workout-pwo': {'klick': 0, 'visningar': 4102, 'position': 67},
    'skivstangsset': {'klick': 0, 'visningar': 1232, 'position': 39},
    'skivstangsstallning': {'klick': 0, 'visningar': 2222, 'position': 57},
    'pool': {'klick': 0, 'visningar': 900, 'position': 40},
    'lagt-lage': {'klick': 50, 'visningar': 5000, 'position': 4},
}


class Rangordning(unittest.TestCase):
    def setUp(self):
        self.ranka, self.utes = v.rangordna(PRIO, GSC)

    def test_utanfor_utrullningen_och_barn_ar_uteslutna(self):
        utes = {x['handle']: x['orsak'] for x in self.utes}
        self.assertIn('pre-workout-pwo', utes)
        self.assertIn('juniorcyklar', utes)      # klass 3 men junior: uteslutet via ordlistan
        self.assertNotIn('pre-workout-pwo', [x['handle'] for x in self.ranka])
        self.assertNotIn('juniorcyklar', [x['handle'] for x in self.ranka])

    def test_ej_koopbara_overlappande_och_pilot_ar_uteslutna(self):
        utes = {x['handle'] for x in self.utes}
        for h in ('pool', 'skivstangsset', 'skivstangsstallning', 'kettlebell'):
            self.assertIn(h, utes)

    def test_rangordning_efter_potential(self):
        # traningsbank 3432 x närhet(59)=0,42 = 1 435; hybridcykel 2202 x närhet(47)=0,66 = 1 453; lagt-lage 5000 x 0,3 = 1 500
        h = [x['handle'] for x in self.ranka]
        self.assertEqual(h, ['lagt-lage', 'hybridcykel', 'traningsbank'])
        self.assertEqual([x['rang'] for x in self.ranka], [1, 2, 3])

    def test_saknad_gsc_ger_noll_potential_men_kommer_med(self):
        prio = PRIO + [{'klass': '2 våg 2 (20+ köpbara)', 'handle': 'osynlig', 'titel': 'X', 'koopbara': '30'}]
        ranka, _ = v.rangordna(prio, GSC)
        sista = ranka[-1]
        self.assertEqual((sista['handle'], sista['potential']), ('osynlig', 0))


KOLL = [
    {'handle': 'pool', 'titel': 'Pool', 'koopbara': '0'},
    {'handle': 'gammal', 'titel': 'Gammal', 'koopbara': '0'},
    {'handle': 'tom-liten', 'titel': 'Tom liten', 'koopbara': '0'},
    {'handle': 'frontpage', 'titel': 'Home page', 'koopbara': '0'},
    {'handle': 'skivstangsstallning', 'titel': 'Ställning', 'koopbara': '3'},
    {'handle': 'fa-lite', 'titel': 'Få lite', 'koopbara': '2'},
    {'handle': 'fa-inget', 'titel': 'Få inget', 'koopbara': '1'},
    {'handle': 'skivstangspaket', 'titel': 'Paket', 'koopbara': '7'},
    {'handle': 'skivstangsset', 'titel': 'Set', 'koopbara': '7'},
    {'handle': 'stor', 'titel': 'Stor', 'koopbara': '80'},
]
SG = {
    'pool': {'klick': 0, 'visningar': 900, 'position': 40},
    'tom-liten': {'klick': 1, 'visningar': 20, 'position': 12},
    'skivstangsstallning': {'klick': 0, 'visningar': 2222, 'position': 57},
    'fa-lite': {'klick': 0, 'visningar': 40, 'position': 60},
    'skivstangspaket': {'klick': 0, 'visningar': 1209, 'position': 26},
    'skivstangsset': {'klick': 0, 'visningar': 1232, 'position': 39},
}


class Struktur(unittest.TestCase):
    def setUp(self):
        self.s = {x['handle']: x for x in v.strukturforslag(KOLL, [['skivstangspaket', 'skivstangsset']], SG)}

    def test_stora_kollektioner_utan_overlapp_tas_inte_med(self):
        self.assertNotIn('stor', self.s)

    def test_tom_med_manga_visningar_omdirigeras_inte_tas_bort(self):
        self.assertEqual(self.s['pool']['forslag'], 'omdirigera')
        self.assertIn('tas inte bort', self.s['pool']['skal'])

    def test_tom_med_litet_men_nagot_omdirigeras(self):
        self.assertEqual(self.s['tom-liten']['forslag'], 'omdirigera')

    def test_tom_utan_visningar_och_klick_tas_bort(self):
        self.assertEqual(self.s['gammal']['forslag'], 'ta bort')

    def test_systemkollektion_behalls(self):
        self.assertEqual(self.s['frontpage']['forslag'], 'behåll')

    def test_fa_produkter_med_manga_visningar_behalls_och_fylls_pa(self):
        self.assertEqual(self.s['skivstangsstallning']['forslag'], 'behåll')

    def test_fa_produkter_med_nagra_visningar_slas_ihop_utan_visningar_tas_bort(self):
        self.assertEqual(self.s['fa-lite']['forslag'], 'slå ihop')
        self.assertEqual(self.s['fa-inget']['forslag'], 'ta bort')

    def test_overlappande_starkast_behalls_andra_slas_ihop(self):
        self.assertEqual(self.s['skivstangsset']['forslag'], 'behåll')    # 1 232 > 1 209 visningar
        self.assertEqual(self.s['skivstangspaket']['forslag'], 'slå ihop')
        self.assertIn('skivstangsset', self.s['skivstangspaket']['skal'])

    def test_saknad_handle_far_varning_om_tak(self):
        s = {x['handle']: x for x in v.strukturforslag(KOLL, [], SG, tak=40)}
        self.assertIn('högst 40 visningar', s['gammal']['skal'])
        self.assertEqual(s['gammal']['i_gsc'], 'nej')
        self.assertNotIn('högst', s['pool']['skal'])     # pool finns i filen

    def test_sorterad_efter_visningar(self):
        lista = v.strukturforslag(KOLL, [['skivstangspaket', 'skivstangsset']], SG)
        vis = [x['visningar'] for x in lista]
        self.assertEqual(vis, sorted(vis, reverse=True))

    def test_inget_andras_av_funktionen(self):
        kopia = json.dumps(KOLL, sort_keys=True)
        v.strukturforslag(KOLL, [['skivstangspaket', 'skivstangsset']], SG)
        self.assertEqual(json.dumps(KOLL, sort_keys=True), kopia)


class Helkorning(unittest.TestCase):
    def test_main_skriver_fyra_filer_och_inget_annat(self):
        with tempfile.TemporaryDirectory() as d:
            mapp, ut = os.path.join(d, 'm'), os.path.join(d, 'ut'); os.makedirs(mapp)
            skriv_csv(os.path.join(mapp, 'prioritering.csv'), ['klass', 'handle', 'titel', 'koopbara'],
                      [[p['klass'], p['handle'], p['titel'], p['koopbara']] for p in PRIO])
            skriv_csv(os.path.join(mapp, 'kollektioner.csv'), ['handle', 'titel', 'koopbara'], [[k['handle'], k['titel'], k['koopbara']] for k in KOLL])
            json.dump([['skivstangspaket', 'skivstangsset']], open(os.path.join(mapp, 'overlappande.json'), 'w'))
            skriv_csv(os.path.join(d, 'g.csv'), ['handle', 'klick', 'visningar', 'position'],
                      [[h, g['klick'], g['visningar'], g['position']] for h, g in {**GSC, **SG}.items()])
            self.assertEqual(v.main(['--mapp', mapp, '--gsc', os.path.join(d, 'g.csv'), '--ut', ut]), 0)
            self.assertEqual(sorted(os.listdir(ut)), ['struktur-forslag.csv', 'struktur-forslag.md', 'vag2-prioritering.csv', 'vag2-prioritering.md'])
            self.assertEqual(sorted(os.listdir(mapp)), ['kollektioner.csv', 'overlappande.json', 'prioritering.csv'])


if __name__ == '__main__':
    unittest.main()
