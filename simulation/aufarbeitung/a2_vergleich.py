# -*- coding: utf-8 -*-
"""A2: Python gegen JavaScript über ein Raster aller Regler (Aufarbeitung vom 12.11.2026).

Gerechnet wird mit dem Code der GEBAUTEN Seiten (js_rechnen.js, Node) und verglichen mit
  a) der numerischen Lösung der Differentialgleichung aus a1_nachrechnung.py (unabhängig, alle Einstellungen),
  b) kaffee_modell.zwei_tassen (Python-Modell des Blatts; nur dort, wo es gilt: Q̇W = 0 und t = t_Z),
  c) der Hauptseite (auswerten) bei C_T = 0, Q̇W = 0, t = t_Z und 200 ml Kaffee (Aussage im Kopf von schlank.js),
  d) Hauptseite gegen kaffee_modell.rechne (wie test_kern.py, hier auf dem Raster).
Raster: t ∈ {1, 45, 90, 180} min mit t_Z ∈ {1, 45, t} (t_Z ≤ t), je drei Werte (Minimum, Blatt, Maximum) für Milchtemperatur,
Milchmenge, Kaffeetemperatur, Kaffeemenge, Raum, Tassenwärmer (0, 5 W, Obergrenze), kA und C_T; dazu 2000 Zufallsfälle.
Aufruf: python3 simulation/aufarbeitung/a2_vergleich.py   (Dauer etwa eine Minute; Ausgabe nach ergebnisse/a2_vergleich.txt)
"""
import itertools
import json
import math
import os
import random
import subprocess
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
SIM = os.path.dirname(HIER)
sys.path.insert(0, HIER)
from a1_nachrechnung import ode  # noqa: E402

KA_BLATT = 0.19938717547267143      # wird unten mit dem Wert der Seite verglichen


def js(auftrag):
    r = subprocess.run(["node", os.path.join(HIER, "js_rechnen.js")], input=json.dumps(auftrag), capture_output=True, text=True, check=True)
    return json.loads(r.stdout)


def obergrenze_QW(kA, thU):
    return max(0.0, min(35.0, math.floor(kA * (95 - thU) / 0.5 + 1e-9) * 0.5))


def raster():
    paare = [(1, 1), (45, 1), (45, 45), (90, 1), (90, 45), (90, 90), (180, 1), (180, 45), (180, 180)]
    werte = dict(thM=[2, 5, 95], VM_ml=[10, 100, 200], thK0=[60, 80, 95], VK_ml=[50, 200, 400], thU=[10, 20, 30],
                 QW=["0", "5", "max"], kA=[0.01, KA_BLATT, 1.0], CT=[0, 255, 600])
    faelle = []
    for (t, tZ) in paare:
        for kombi in itertools.product(*werte.values()):
            e = dict(zip(werte.keys(), kombi), t=t, tZ=tZ)
            cap = obergrenze_QW(e["kA"], e["thU"])
            e["QW"] = {"0": 0.0, "5": min(5.0, cap), "max": cap}[e["QW"]]
            faelle.append(e)
    rnd = random.Random(20261112)
    for _ in range(2000):
        t = rnd.randint(1, 180)
        e = dict(t=t, tZ=rnd.randint(1, t), thM=rnd.uniform(2, 95), VM_ml=rnd.uniform(10, 200), thK0=rnd.uniform(60, 95),
                 VK_ml=rnd.uniform(50, 400), thU=rnd.uniform(10, 30), kA=0.01 * 100 ** rnd.random(), CT=rnd.uniform(0, 600))
        e["QW"] = rnd.uniform(0, obergrenze_QW(e["kA"], e["thU"]))
        faelle.append(e)
    return faelle


def main():
    sys.path.insert(0, os.path.join(SIM, "modell"))
    import kaffee_modell as km
    zeilen = ["A2: Python gegen JavaScript (Code der gebauten Seiten)", ""]
    faelle = raster()
    # Hauptseite: Raster ihrer eigenen Regler (VK fest 200 ml, kein Wärmer, keine Tasse, t = t_Z)
    haupt = [dict(thK0=a, thM=b, thU=c, VM_ml=d, kA=k, tZ=z) for a in (60, 80, 95) for b in (2, 5, 95) for c in (10, 20, 30)
             for d in (10, 100, 200) for k in (0.01, KA_BLATT, 1.0) for z in (1, 45, 90, 180)]
    vergleich_c = [dict(t=h["tZ"], tZ=h["tZ"], thM=h["thM"], VM_ml=h["VM_ml"], thK0=h["thK0"], VK_ml=200, thU=h["thU"], QW=0, kA=h["kA"], CT=0)
                   for h in haupt]
    j = js({"schlank": faelle + vergleich_c, "haupt": haupt})
    zeilen.append("kA des Blatts: schlanke Seite %.15f, Hauptseite %.15f" % (j["KA_schlank"], j["KA_haupt"]))
    s = j["schlank"][:len(faelle)]
    sc = j["schlank"][len(faelle):]
    hp = j["haupt"]

    # a) gegen die Differentialgleichung
    o = ode(faelle)
    groesste = dict(th=0.0, Q=0.0, i_th=-1, i_Q=-1)
    for i, r in enumerate(s):
        for k in ("th1", "th2"):
            d = abs(r[k] - o[k][i])
            if d > groesste["th"]:
                groesste.update(th=d, i_th=i)
        for k in ("Q1", "Q2"):
            d = abs(r[k] - o[k][i])
            if d > groesste["Q"]:
                groesste.update(Q=d, i_Q=i)
    zeilen += ["", "a) schlanke Seite gegen Differentialgleichung (numerisch, unabhängig): %d Einstellungen" % len(faelle),
               "   größte Abweichung Temperatur %.2e K, Wärme %.2e J" % (groesste["th"], groesste["Q"]),
               "   Fall mit größter Temperaturabweichung: %s" % json.dumps({k: round(v, 4) for k, v in faelle[groesste["i_th"]].items()})]
    ok_a = groesste["th"] < 1e-6 and groesste["Q"] < 1e-3

    # b) gegen kaffee_modell.zwei_tassen (gilt nur ohne Wärmer und bei t = t_Z; dort ist kA aus der Messung mit Tasse bestimmt)
    db, dk, nb, nfehl, beispiel = 0.0, 0.0, 0, 0, None
    for i, e in enumerate(faelle):
        if e["QW"] != 0 or e["t"] != e["tZ"]:
            continue
        CK = km.P["rho_K"] * e["VK_ml"] * 1e-6 * km.P["cp_K"]
        # Messwert nach 10 min, der mit Tasse genau das kA der Einstellung ergibt
        mess = e["thU"] + (e["thK0"] - e["thU"]) * math.exp(-e["kA"] * 600 / (CK + e["CT"]))
        p = dict(km.P, V_K=e["VK_ml"] * 1e-6, V_M=e["VM_ml"] * 1e-6, th_K0=e["thK0"], th_M=e["thM"], th_U=e["thU"], th_mess=mess,
                 t_end=e["tZ"] * 60.0)
        try:
            z = km.zwei_tassen(p, C_T=e["CT"])
        except ValueError:                    # rechne() bricht ab, wenn die Mischung kälter als der Raum ist (Logarithmus in t_schnitt)
            nfehl += 1
            beispiel = beispiel or {k: round(v, 3) for k, v in e.items()}
            continue
        dk = max(dk, abs(z["kA"] - e["kA"]) / e["kA"])
        db = max(db, abs(z["th1"] - s[i]["th1"]), abs(z["th2"] - s[i]["th2"]))
        nb += 1
    zeilen += ["", "b) schlanke Seite gegen kaffee_modell.zwei_tassen: %d Einstellungen ohne Wärmer bei t = t_Z" % nb,
               "   größte Abweichung Temperatur %.2e K, kA relativ %.2e" % (db, dk),
               "   %d Einstellungen nicht vergleichbar: kaffee_modell.rechne bricht ab (Mischung kälter als der Raum), z. B. %s"
               % (nfehl, json.dumps(beispiel))]
    ok_b = db < 1e-9 and dk < 1e-12

    # c) schlanke Seite gegen Hauptseite
    dc = 0.0
    for r1, r2 in zip(sc, hp):
        dc = max(dc, abs(r1["th1"] - r2["th1"]), abs(r1["th2"] - r2["th2"]), abs(r1["th10"] - r2["th10"]), abs(r1["th2K"] - r2["th2K"]),
                 abs(r1["Q1"] - r2["Q1"]) / 1000, abs(r1["Q2"] - r2["Q2"]) / 1000)
    zeilen += ["", "c) schlanke Seite (C_T = 0, Q̇W = 0, t = t_Z, 200 ml) gegen Hauptseite: %d Einstellungen" % len(hp),
               "   größte Abweichung %.2e (K oder kJ)" % dc]
    ok_c = dc < 1e-9

    # d) Hauptseite gegen kaffee_modell.rechne
    dd = 0.0
    for h, r in zip(haupt, hp):
        p = dict(km.P, V_K=200e-6, V_M=h["VM_ml"] * 1e-6, th_K0=h["thK0"], th_M=h["thM"], th_U=h["thU"], t_end=h["tZ"] * 60.0)
        CK = p["rho_K"] * p["V_K"] * p["cp_K"]
        p["th_mess"] = h["thU"] + (h["thK0"] - h["thU"]) * math.exp(-h["kA"] * 600 / CK)
        q = km.rechne(p)
        dd = max(dd, abs(q["T1"] - 273.15 - r["th1"]), abs(q["T2"] - 273.15 - r["th2"]), abs(q["Q1"] - r["Q1"]) / 1000, abs(q["Q2"] - r["Q2"]) / 1000)
    zeilen += ["", "d) Hauptseite gegen kaffee_modell.rechne: %d Einstellungen" % len(haupt), "   größte Abweichung %.2e (K oder kJ)" % dd]
    ok_d = dd < 1e-9

    ok_ka = abs(j["KA_schlank"] - KA_BLATT) < 1e-15 and abs(j["KA_haupt"] - KA_BLATT) < 1e-15
    alle = ok_a and ok_b and ok_c and ok_d and ok_ka
    zeilen += ["", "Ergebnis: " + ("alle Vergleiche innerhalb der Grenzen (Temperatur 1e-6 K numerisch, sonst 1e-9)" if alle else
                                   "ABWEICHUNG: a %s, b %s, c %s, d %s, kA %s" % (ok_a, ok_b, ok_c, ok_d, ok_ka))]
    text = "\n".join(zeilen) + "\n"
    print(text, end="")
    open(os.path.join(HIER, "ergebnisse", "a2_vergleich.txt"), "w", encoding="utf-8").write(text)
    return 0 if alle else 1


if __name__ == "__main__":
    raise SystemExit(main())
