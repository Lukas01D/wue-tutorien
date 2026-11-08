# -*- coding: utf-8 -*-
"""Rechenkern der Kaffee-Seite Fassung 3 gegen kaffee_modell.py (unverändert) mit den Eingaben aus werte.py.

Aufruf: python3 simulation/tests/test_kern.py   (prüft simulation/site/index.html; Ergebnis nach test_kern_ergebnis.txt)
Geprüft wird der Skriptteil der gebauten Seite vor den Texten (Block MODELL, STANDARD, BEISPIEL, parameter, kABlatt, auswerten),
ausgeführt in Node. Abnahmekriterium: relative Abweichung unter 1e-9 (KONZEPT_F3.md, Auftrag Abschnitt 4).
"""
import hashlib
import json
import math
import os
import random
import subprocess
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
SIM = os.path.dirname(HIER)
sys.path.insert(0, os.path.join(SIM, "modell"))
sys.path.insert(0, os.path.join(SIM, "site"))
import kaffee_modell as km  # noqa: E402
import werte as wt  # noqa: E402
import zahlen  # noqa: E402

GRENZE = 1e-9
RECHNE_SHA = "6fded445f7007f475f7fd012e51947b345aac3bcb9a6298fb322cc3bd1a62f9a"   # rechne() wie auf main (Fassung 2, von Codex geprüft)
K = 273.15
ergebnisse = []


def pruefe(name, ok, info=""):
    ergebnisse.append((name, bool(ok), info))


def rel(a, b):
    return abs(a - b) / max(abs(b), 1e-12)


def kern_aus_seite():
    html = open(os.path.join(SIM, "site", "index.html"), encoding="utf-8").read()
    a = html.index("<script>") + len("<script>")
    b = html.index("const TEXTE = ", a)
    return html[a:b]


def node(kern, auftrag):
    prog = kern + "\nconst AUFTRAG = " + json.dumps(auftrag) + ";\n" + r"""
const aus = AUFTRAG.faelle.map(e => { const r = auswerten(e); const o = {}; for (const k in r) if (typeof r[k] === 'number') o[k] = r[k];
  o.k1 = [0, 600, 1800, e.tZ * 60].map(t => r.kurve1(t)); o.k2 = [0, 600, 1800, e.tZ * 60].map(t => r.kurve2(t)); return o; });
process.stdout.write(JSON.stringify({ aus: aus, STANDARD: STANDARD, BEISPIEL: BEISPIEL, KA: kABlatt() }));
"""
    r = subprocess.run(["node", "-"], input=prog, capture_output=True, text=True, check=True)
    return json.loads(r.stdout)


def referenz(e):
    """Unabhängig vom Skript: kaffee_modell.rechne mit dem gleichwertigen Messwert nach 10 min für das eingestellte kA."""
    p = dict(km.P, V_K=wt.V_KAFFEE, V_M=e["VM_ml"] * 1e-6, th_K0=e["thK0"], th_M=e["thM"], th_U=e["thU"], t_end=e["tZ"] * 60.0)
    C_K = p["rho_K"] * p["V_K"] * p["cp_K"]
    p["th_mess"] = wt.MESSWERT if e["kA"] is None else e["thU"] + (e["thK0"] - e["thU"]) * math.exp(-e["kA"] * p["t_mess"] / C_K)
    r = km.rechne(p)
    kurve1 = lambda t: e["thU"] + (r["T1_0"] - r["T_U"]) * math.exp(-r["a_G"] * t)
    kurve2 = lambda t: e["thU"] + (r["T_K0"] - r["T_U"]) * math.exp(-r["a_K"] * t)
    return dict(kA=r["kA"], th10=r["T1_0"] - K, th1=r["T1"] - K, th2K=r["T2_K"] - K, th2=r["T2"] - K, dT=r["dT"], Q1=r["Q1"],
                Q2=r["Q2"], t_schnitt=r["t_schnitt"], k1=[kurve1(t) for t in (0, 600, 1800, e["tZ"] * 60)],
                k2=[kurve2(t) for t in (0, 600, 1800, e["tZ"] * 60)])


def main():
    kern = kern_aus_seite()
    a = kern.index("function rechne(p) {")
    b = kern.index("\n}\n", a) + 2
    pruefe("rechne() unverändert (SHA-256 wie auf main)", hashlib.sha256(kern[a:b].encode()).hexdigest() == RECHNE_SHA)
    pruefe("Block MODELL vorhanden", "// MODELL-ANFANG" in kern and "// MODELL-ENDE" in kern)
    pruefe("keine Verdunstung im Rechenkern", "verdunst" not in kern.lower() and "dh_v" not in kern)

    w = wt.werte()
    ka = w["kA"]
    blatt = dict(thK0=wt.KAFFEE_START, thM=wt.MILCH_KALT, thU=wt.RAUM, VM_ml=wt.V_MILCH * 1e6, kA=None, tZ=60)
    faelle = [blatt, dict(blatt, kA=ka)]
    zufall = random.Random(20261108)
    for _ in range(2000):
        faelle.append(dict(thK0=round(zufall.uniform(60, 95) * 2) / 2, thM=round(zufall.uniform(2, 80) * 2) / 2,
                           thU=round(zufall.uniform(10, 30) * 2) / 2, VM_ml=float(zufall.choice(range(10, 105, 5))),
                           kA=zufall.uniform(0.05, 0.8), tZ=float(zufall.randint(1, 180))))
    for kA_rand in (0.05, 0.8):
        for tz in (1, 180):
            faelle.append(dict(blatt, kA=kA_rand, tZ=float(tz), thK0=95.0, thU=10.0, thM=80.0, VM_ml=100.0))
    js = node(kern, {"faelle": faelle})

    # Standardwerte an einer Stelle, gleich werte.py (SE6)
    st = js["STANDARD"]
    pruefe("STANDARD gleich werte.py", st["thK0"] == wt.KAFFEE_START and st["thM"] == wt.MILCH_KALT and st["thU"] == wt.RAUM and
           st["VK_ml"] == round(wt.V_KAFFEE * 1e6) and st["VM_ml"] == round(wt.V_MILCH * 1e6) and st["thMess"] == wt.MESSWERT and
           st["thMh"] == wt.MILCH_HEISS and st["trink"] == wt.TRINK, json.dumps(st))
    pruefe("kA des Blatts", rel(js["KA"], ka) < GRENZE, "%.12f gegen %.12f" % (js["KA"], ka))
    kA_b, b1, b2, b2m = w["V_becher"]
    bsp = js["BEISPIEL"]
    pruefe("Beispielwerte gleich werte.py (gerundet wie das Blatt)", bsp["t1"] == [round(x, 1) for x in b1] and
           bsp["t2"] == [round(x, 1) for x in b2] and bsp["t2Milch"] == round(b2m, 1), json.dumps(bsp))

    # Prüfwerte des Blatts (Abschnitt 1 des Auftrags) über den Weg der Seite (kA fest = kA des Blatts)
    for nr, e in enumerate(faelle[:2]):
        o = js["aus"][nr]
        art = "Messwert 72 °C" if e["kA"] is None else "kA fest"
        for name, soll in (("kA", w["kA"]), ("th10", w["th10"]), ("th1", w["th1"]), ("th2K", w["th2K"]), ("th2", w["th2"]),
                           ("dT", w["dT"]), ("Q1", w["Q1"]), ("Q2", w["Q2"]), ("t_schnitt", w["t_schnitt_min"] * 60)):
            pruefe("Prüfwert %s (%s)" % (name, art), rel(o[name], soll) < GRENZE, "%.10g gegen %.10g" % (o[name], soll))
    o = std = js["aus"][1]
    pruefe("Prüfwerte gerundet wie im Auftrag", "%.2f %.2f %.2f %.2f %.2f %.2f %.0f" % (o["th10"], o["th1"], o["th2K"], o["th2"], o["dT"],
           o["Q1"] / 1000, o["t_schnitt"] / 60) == "70.47 43.85 45.43 40.29 3.56 25.49 95" and "%.2f" % (o["Q2"] / 1000) == "28.90")

    # Zufallssätze und Ränder
    schlecht = []
    for e, o in zip(faelle, js["aus"]):
        r = referenz(e)
        for k in ("kA", "th10", "th1", "th2K", "th2", "Q1", "Q2"):
            if rel(o[k], r[k]) >= GRENZE:
                schlecht.append((k, e, o[k], r[k]))
        if abs(o["dT"] - r["dT"]) >= GRENZE * max(1.0, abs(r["th1"])):
            schlecht.append(("dT", e, o["dT"], r["dT"]))
        # Schnittzeit: relativ; nahe 0 s (Milch so warm wie der Kaffee, Schnitt beim Start) absolut auf 1 µs
        if math.isfinite(r["t_schnitt"]) and (abs(o["t_schnitt"] - r["t_schnitt"]) > 1e-6 if abs(r["t_schnitt"]) < 1e-3 else rel(o["t_schnitt"], r["t_schnitt"]) >= GRENZE):
            schlecht.append(("t_schnitt", e, o["t_schnitt"], r["t_schnitt"]))
        for i in range(4):
            if rel(o["k1"][i], r["k1"][i]) >= GRENZE or rel(o["k2"][i], r["k2"][i]) >= GRENZE:
                schlecht.append(("Kurve", e, o["k1"][i], r["k1"][i]))
        if e["kA"] is not None and rel(o["kA"], e["kA"]) >= GRENZE:
            schlecht.append(("kA fest", e, o["kA"], e["kA"]))
        # Energiebilanz ohne Verdunstung: C_G (th1 - th2) = Q2 - Q1 (gleiche Milch in beiden Tassen)
        if abs(o["C_G"] * o["dT"] - (o["Q2"] - o["Q1"])) > 1e-9 * max(abs(o["Q2"]), 1.0):
            schlecht.append(("Energiebilanz", e, o["C_G"] * o["dT"], o["Q2"] - o["Q1"]))
    pruefe("%d Parametersätze (Blatt, 2000 Zufall, Ränder) gegen kaffee_modell.py" % len(faelle), not schlecht,
           "; ".join("%s %s: %r gegen %r" % s for s in schlecht[:3]))

    # Zahlen der Texte (zahlen.py) gegen die Seite: Auftrag 1, 2, 3 und Rückmeldungen
    z = zahlen.modellzahlen()
    extra = [dict(blatt, kA=ka, thM=wt.RAUM), dict(blatt, kA=ka, tZ=std["t_schnitt"] / 60), dict(blatt, kA=ka, tZ=1e5)]
    for t in (30, 60, 90):
        extra.append(dict(blatt, kA=ka, tZ=float(t), thM=z["kipp%d" % t][0]))
    jx = node(kern, {"faelle": extra})["aus"]
    pruefe("Auftrag 1: Milch 20 °C", abs(jx[0]["dT"] - z["a1_dT"][0]) < 1e-9 and "%.2f" % jx[0]["dT"] == "2.56", "%.6f" % jx[0]["dT"])
    pruefe("Auftrag 2: größter Unterschied am Schnittpunkt", abs(jx[1]["dT"] - z["dTmax"][0]) < 1e-9 and "%.2f" % jx[1]["dT"] == "3.86"
           and "%.0f" % (std["t_schnitt"] / 60) == "%.0f" % z["tmax"][0], "%.6f" % jx[1]["dT"])
    pruefe("Auftrag 2: Rest bei sehr später Zugabe", abs(jx[2]["dT"] - z["grenz"][0]) < 1e-9, "%.6f gegen %.6f" % (jx[2]["dT"], z["grenz"][0]))
    pruefe("Auftrag 3: Kipppunkte 30, 60, 90 min (Unterschied 0)", all(abs(x["dT"]) < 1e-9 for x in jx[3:6]),
           ", ".join("%.2e" % x["dT"] for x in jx[3:6]))
    pruefe("Kipppunkt 60 min wie werte.py", rel(z["kipp60"][0], w["kipp"]) < GRENZE)
    hz = node(kern, {"faelle": [dict(blatt, kA=ka, thM=wt.MILCH_HEISS)]})["aus"][0]
    pruefe("Erwärmte Milch 70 °C (Teil g)", rel(hz["th1"], w["th1h"]) < GRENZE and rel(hz["th2"], w["th2h"]) < GRENZE,
           "%.4f %.4f" % (hz["th1"], hz["th2"]))
    pruefe("Zeit bis 60 °C (Teil d2)", "%.1f" % z["t_tr"][0] == "18.6" and rel(z["t_tr"][0], w["t_tr_min"]) < GRENZE)
    pruefe("Sprünge beim Zugießen (Rückmeldung b)", "%.1f %.1f" % (z["sprung1"][0], z["sprung2"][0]) == "9.5 5.1"
           and abs(z["sprung2"][0] - (std["th2K"] - std["th2"])) < 1e-9 and abs(z["sprung1"][0] - (80 - std["th10"])) < 1e-9)

    zeilen = ["Rechenkern Fassung 3 gegen kaffee_modell.py mit werte.py (Grenze relativ %g)" % GRENZE, ""]
    for n, ok, info in ergebnisse:
        zeilen.append(("bestanden   " if ok else "FEHLGESCHLAGEN ") + n + ("  [" + info + "]" if info and not ok else ""))
    gut = sum(1 for _, ok, _ in ergebnisse if ok)
    zeilen += ["", "%d von %d bestanden" % (gut, len(ergebnisse))]
    text = "\n".join(zeilen) + "\n"
    open(os.path.join(HIER, "test_kern_ergebnis.txt"), "w", encoding="utf-8").write(text)
    print(text)
    sys.exit(0 if gut == len(ergebnisse) else 1)


if __name__ == "__main__":
    main()
