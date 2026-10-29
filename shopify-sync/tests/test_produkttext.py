import argparse
import importlib.util
import pathlib
import sys

_spec = importlib.util.spec_from_file_location("kpt", pathlib.Path(__file__).resolve().parent.parent / "scripts" / "kontrollera_produkttext.py")
kpt = importlib.util.module_from_spec(_spec)
sys.modules['kpt'] = kpt
_spec.loader.exec_module(kpt)

OPT = argparse.Namespace(title_max=70, seo_title_max=60, seo_suffix="", meta_min=130, meta_max=155)
FAKTA = "Tunturi Mini Resistance Band Set, 5 st. 5 band: 4,8 / 6,5 / 9,5 / 13 / 14 kg. Mått 25 x 5 x 0,8 cm. Förvaringspåse. Tillverkare: Tunturi."
OK = {
    "id": "a", "fakta": FAKTA, "titel": "Motståndsband Tunturi Mini, set med 5 band",
    "seo_title": "Motståndsband Tunturi Mini, set med 5 band",
    "meta": "Tunturi Mini Resistance Band Set har fem motståndsband i olika färger, från 4,8 till 14 kg. Förvaringspåse ingår. Varje band är 25 x 5 x 0,8 cm.",
}


def regler(p, opt=OPT):
    return {(x.nivå, x.regel) for x in kpt.kontrollera_produkt(p, opt)}


def test_godkant_utkast_ger_inga_fel():
    assert not [r for r in regler(OK) if r[0] == "FEL"]


def test_tal_utan_kalla_fångas():
    p = dict(OK, meta=OK["meta"].replace("14 kg", "15 kg"))
    assert ("FEL", "tal_utan_kalla") in regler(p)


def test_komma_och_punkt_i_tal_ar_samma():
    assert not kpt.tal_i("0,8 cm") ^ kpt.tal_i("0.8 cm")
    assert kpt.tal_i("1 000 kg") == {"1000"}


def test_ursprung_utan_kalla_ar_fel():
    p = dict(OK, beskrivning="Tillverkat av Tunturi i Italien. Passar dig som tränar hemma. Specifikationer: fem band. Leverans enligt standard.")
    assert ("FEL", "ursprung") in regler(p)
    assert ("FEL", "nationalitet_utan_kalla") not in regler(dict(p, fakta=FAKTA + " Italien italiensk"))


def test_halsoord_superlativ_och_pris():
    assert ("FEL", "halsa") in regler(dict(OK, meta=OK["meta"] + " Dämpar vibrationer."))
    assert ("FEL", "superlativ") in regler(dict(OK, meta=OK["meta"] + " Marknadens bästa."))
    assert ("FEL", "pris_eller_kampanj") in regler(dict(OK, meta=OK["meta"] + " Nu på rea!"))


def test_langdgranser():
    assert ("FEL", "titel_lang") in regler(dict(OK, titel="x" * 71))
    assert ("FEL", "seo_titel_lang") in regler(dict(OK, seo_title="x" * 61))
    assert ("FEL", "meta_langd") in regler(dict(OK, meta="kort"))


def test_varumarke_dubbelt_med_suffix():
    opt = argparse.Namespace(**{**vars(OPT), "seo_suffix": " – BEST OF SPORTS"})
    assert ("FEL", "varumarke_dubbelt") in regler(dict(OK, seo_title="Band | Best of Sports"), opt)


def test_standardblock_raknas_inte():
    body = ("Ett motståndsband. Passar dig som tränar hemma.\nSpecifikationer: 5 band.\n"
            "[[STANDARDBLOCK]]Leverans 5–8 arbetsdagar, 30 dagars öppet köp.[[/STANDARDBLOCK]]")
    assert ("FEL", "tal_utan_kalla") not in regler(dict(OK, beskrivning=body))


def test_dubbletter_i_batch():
    fynd = kpt.kontrollera_batch([OK, dict(OK, id="b")], OPT)
    assert any(x.regel == "dubblett_titel" for x in fynd)


def test_saknad_fakta_ar_fel():
    assert ("FEL", "fakta_saknas") in regler({k: v for k, v in OK.items() if k != "fakta"})
