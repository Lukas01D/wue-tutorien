# -*- coding: utf-8 -*-
"""Zahlen in den Texten der Kaffee-Seite, Fassung 3.

- {{z:name}}: Ergebniszahl aus ungerundeten Werten von kaffee_modell.py (unverändert) mit den Eingaben aus werte.py,
  gerundet auf die Stellen in modellzahlen(); Deutsch mit Dezimalkomma, Englisch mit Dezimalpunkt.
- {{e:name}}: Wert des Blatts (werte.py).
Jede Zahl wird in simulation/tests/test_kern.py gegen dieselbe Rechnung geprüft.
"""
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HIER), "modell"))
import kaffee_modell as km  # noqa: E402
import werte as wt  # noqa: E402

K = 273.15


def blatt():
    """Eingaben des Blatts als Parameter für kaffee_modell.rechne (wie werte.werte())."""
    return dict(km.P, th_mess=wt.MESSWERT, th_Mh=wt.MILCH_HEISS, th_K0=wt.KAFFEE_START, th_M=wt.MILCH_KALT,
                th_U=wt.RAUM, V_K=wt.V_KAFFEE, V_M=wt.V_MILCH, t_end=wt.DAUER_MIN * 60.0)


def modellzahlen():
    """Name -> (ungerundeter Wert, Nachkommastellen)."""
    w = wt.werte()
    p = blatt()
    r = km.rechne(p)
    z = dict(th1=(w["th1"], 2), th2=(w["th2"], 2), th2K=(w["th2K"], 2), dT=(w["dT"], 2), Q1=(w["Q1"] / 1000, 2),
             Q2=(w["Q2"] / 1000, 2), dQ=(w["dQ"] / 1000, 2), CG=(w["CG"], 1), th10=(w["th10"], 2), kA=(w["kA"], 4),
             t_tr=(w["t_tr_min"], 1), tmax=(r["t_schnitt"] / 60, 0))
    z["sprung1"] = (p["th_K0"] - (r["T1_0"] - K), 1)
    z["sprung2"] = (r["T2_K"] - r["T2"], 1)
    z["a1_dT"] = (km.zwei_tassen(p, th_M1=p["th_U"])["dT"], 2)
    z["dTmax"] = (km.zwei_tassen(p, t_end=r["t_schnitt"])["dT"], 2)
    # Grenzwert bei sehr später Zugabe: Tasse 1 und schwarzer Kaffee auf Raumtemperatur, dann Milch in Tasse 2
    th2_grenz = (r["C_K"] * p["th_U"] + r["C_M"] * p["th_M"]) / r["C_G"]
    z["grenz"] = (p["th_U"] - th2_grenz, 2)
    for t in (30, int(wt.DAUER_MIN), 90):
        z["kipp%d" % t] = (km.rechne(dict(p, t_end=t * 60.0))["th_M_gleich"], 1)
    return z


def eingaben():
    return dict(thK0=(wt.KAFFEE_START, 0), thM=(wt.MILCH_KALT, 0), thU=(wt.RAUM, 0), VK=(wt.V_KAFFEE * 1e6, 0),
                VM=(wt.V_MILCH * 1e6, 0), thMess=(wt.MESSWERT, 0), tZ=(wt.DAUER_MIN, 0), trink=(wt.TRINK, 0))


def zahl(x, n, sprache):
    s = "%.*f" % (n, x)
    if s.startswith("-"):
        s = "−" + s[1:]
    return s.replace(".", ",") if sprache == "de" else s


def alle(sprache):
    out = {}
    for k, (x, n) in modellzahlen().items():
        out["z:" + k] = zahl(x, n, sprache)
    for k, (x, n) in eingaben().items():
        out["e:" + k] = zahl(x, n, sprache)
    return out


if __name__ == "__main__":
    for k, v in sorted(alle("de").items()):
        print(k, v)
