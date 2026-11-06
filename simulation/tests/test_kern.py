# -*- coding: utf-8 -*-
"""Tests des Rechenkerns der Kaffee-Simulation (BAU_AUFTRAG.md, Teil 2.2).

Aufruf vom Repository aus:  python3 simulation/tests/test_kern.py [--html simulation/site/index.html]
Ohne --html werden die Quellen in simulation/site/src/ geprüft, mit --html die Blöcke der fertigen Seite.

TOLERANZEN (festgelegt am 05.11.2026 vor der ersten Auswertung, nie geweitet):
  JavaScript gegen Python (gleiche Gleichungen, Gleitkomma):
    Temperaturen und Unterschiede (°C, K):        |d| <= 1e-9
    Wärmen (kJ):                                    |d| <= 1e-9
    Wärmeströme (W):                                |d| <= 1e-9
    kA (W/K):                                       |d| <= 1e-12
    Zeiten (min):                                   |d| <= 1e-7 oder relativ <= 1e-10
  Feste Testfälle gegen Konzept und f2_testfaelle.txt: halbe Einheit der letzten angegebenen Stelle
    (z. B. 34,05 °C: |d| <= 0,005 K; 0,3402 W/K: |d| <= 0,00005 W/K).
  Physik: Energiebilanz |Rest| <= 1e-9 kJ; Monotonie ohne Toleranz (strikt); größter Unterschied:
    analytisch gegen Raster 1e-4 K und 0,05 min, über kA gleich auf 1e-9 K.
ZUFALLSTESTS: 10 000 Sätze, Startwert 20261105, Verteilung siehe zufallssatz().
Fehlerfälle werden reproduzierbar nach simulation/tests/fehlerfaelle/ geschrieben.
"""
import hashlib, json, math, os, random, subprocess, sys, tempfile

HIER = os.path.dirname(os.path.abspath(__file__))
SIM = os.path.dirname(HIER)
REPO = os.path.dirname(SIM)
sys.path.insert(0, os.path.join(SIM, "modell"))
import kaffee_erweitert as ke  # noqa: E402

HTML = None
if "--html" in sys.argv:
    HTML = os.path.join(REPO, sys.argv[sys.argv.index("--html") + 1]) if not os.path.isabs(sys.argv[sys.argv.index("--html") + 1]) else sys.argv[sys.argv.index("--html") + 1]

ERG = []
FEHLER_DIR = os.path.join(HIER, "fehlerfaelle")


def pruefe(name, ok, info=""):
    ERG.append((ok, name, info))
    print(("ok    " if ok else "FEHLT ") + name + (("  " + info) if info else ""))


def js(faelle, extra=None):
    auftrag = {"faelle": faelle}
    if HTML:
        auftrag["html"] = HTML
    if extra:
        auftrag.update(extra)
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
        json.dump(auftrag, f)
        name = f.name
    out = subprocess.run(["node", os.path.join(HIER, "kern_laden.js"), name], capture_output=True, text=True, check=True)
    os.unlink(name)
    return json.loads(out.stdout)


def E(**abw):
    return ke.einstellung(**abw)


def nah(a, b, tol):
    return abs(a - b) <= tol


# ---------------------------------------------------------------- 0 Identität des Kerns
def test_identitaet():
    soll = "b32e3f9db9f82b09bfc0e300388ffbef72f875cec65540da668d765389f97d24"
    src = open(os.path.join(SIM, "site", "src", "modell.js"), "rb").read()
    pruefe("MODELL-Block der Quellen bytegleich dem geprüften Werkzeug (SHA-256 b32e3f9…)", hashlib.sha256(src).hexdigest() == soll)
    py = open(os.path.join(SIM, "modell", "kaffee_modell.py"), "rb").read()
    pruefe("kaffee_modell.py bytegleich der Quelle (SHA-256 eb7efc1d…)",
           hashlib.sha256(py).hexdigest() == "eb7efc1d5322b629e1e11494f7c70fa8d8d54ec60e555874326fa491a31757a1")
    if HTML:
        h = open(HTML, encoding="utf-8").read()
        block = h[h.index("// MODELL-ANFANG"):h.index("// MODELL-ENDE") + len("// MODELL-ENDE")]
        pruefe("MODELL-Block in der fertigen Seite bytegleich", block == src.decode("utf-8").rstrip("\n").rstrip(),
               "" if block == src.decode("utf-8").rstrip("\n").rstrip() else "abweichend")


# ---------------------------------------------------------------- 1 Feste Testfälle
FEST = [
    # (Name, Einstellung, Größe, Sollwert, Toleranz)
    ("Standard kA", E(), "kA", 0.3402, 5e-5),
    ("Standard Mischtemperatur", E(), "th10", 70.47, 0.005),
    ("Standard theta1", E(), "th1", 34.05, 0.005),
    ("Standard theta2", E(), "th2", 30.19, 0.005),
    ("Standard Unterschied", E(), "dT", 3.85, 0.005),
    ("Standard Q1", E(), "Q1", 34.88, 0.005),
    ("Standard Q2", E(), "Q2", 38.57, 0.005),
    ("Standard Schnitt", E(), "tSchnitt", 55.7, 0.05),
    ("Standard schwarz nach 30 min", E(), "schwarz30", 48.84, 0.005),
    ("Standard Zeitkonstante", E(), "tauMin", 41.0, 0.05),
    ("Standard Wärmestrom 0 Tasse 1", E(), "q1_0", 17.17, 0.005),
    ("Standard Wärmestrom 0 Tasse 2", E(), "q2_0", 20.41, 0.005),
    ("Standard Wärmestrom 60 Tasse 1", E(), "q1_60", 4.78, 0.005),
    ("Standard Wärmestrom 60 Tasse 2", E(), "q2_60", 4.72, 0.005),
    ("Teilfläche vor dem Schnitt, Zugabe 60", E(), "flaecheVor", 3.6987, 5e-5),
    ("Teilfläche nach dem Schnitt, Zugabe 60", E(), "flaecheNach", -0.0083, 5e-5),
    ("Teilfläche vor, Zugabe 120", E(tEnd_min=120), "flaecheVor", 3.6987, 5e-5),
    ("Teilfläche nach, Zugabe 120", E(tEnd_min=120), "flaecheNach", -0.8055, 5e-5),
    ("Becher (Teil g) kA", E(kAQuelle="messung", becher=True), "kA", 0.4440, 5e-5),
    ("Becher (Teil g) theta1", E(kAQuelle="messung", becher=True), "th1", 34.04, 0.005),
    ("Becher (Teil g) theta2", E(kAQuelle="messung", becher=True), "th2", 30.96, 0.005),
    ("Becher (Teil g) Q1", E(kAQuelle="messung", becher=True), "Q1", 46.60, 0.005),
    ("Becher (Teil g) Q2", E(kAQuelle="messung", becher=True), "Q2", 50.34, 0.005),
    ("Becher (Teil g) Q2-Q1 ungerundet", E(kAQuelle="messung", becher=True), "dQ", 3.73, 0.005),
    ("Versuch 40 min, Becher theta1", E(kAQuelle="messung", becher=True, tEnd_min=40), "th1", 41.79, 0.005),
    ("Versuch 40 min, Becher theta2", E(kAQuelle="messung", becher=True, tEnd_min=40), "th2", 38.82, 0.005),
    ("Milch für Tasse 2 bei 20 °C: theta2", E(milch2Raum=True), "th2", 32.10, 0.005),
    ("Milch für Tasse 2 bei 20 °C: Unterschied", E(milch2Raum=True), "dT", 1.95, 0.005),
    ("Milch für Tasse 2 bei 20 °C: Milchbeitrag", E(milch2Raum=True), "milch", -1.83, 0.005),
    ("Milch 60 °C (Teil f) theta1", E(thM=60.0), "th1", 35.99, 0.005),
    ("Milch 60 °C (Teil f) theta2", E(thM=60.0), "th2", 37.18, 0.005),
    ("kA Tasse 1 relativ 1,05: theta1", E(kA1Faktor=1.05), "th1", 33.18, 0.005),
    ("kA Tasse 1 relativ 1,05: Unterschied", E(kA1Faktor=1.05), "dT", 2.98, 0.005),
    ("kA Tasse 1 relativ 1,10: Unterschied", E(kA1Faktor=1.10), "dT", 2.17, 0.005),
    ("kA beider 0,9: Unterschied", E(kA=0.9 * ke.kA_aufgabe()), "dT", 3.860, 0.0005),
    ("kA beider 1,1: Unterschied", E(kA=1.1 * ke.kA_aufgabe()), "dT", 3.816, 0.0005),
    # Tabelle 8.2.1 Voreinstellungen
    ("Keramik mit Deckel kA", E(kA=0.56 * ke.kA_aufgabe()), "kA", 0.1905, 5e-5),
    ("Keramik mit Deckel theta1", E(kA=0.56 * ke.kA_aufgabe()), "th1", 44.66, 0.005),
    ("Keramik mit Deckel theta2", E(kA=0.56 * ke.kA_aufgabe()), "th2", 41.15, 0.005),
    ("Keramik mit Deckel Unterschied", E(kA=0.56 * ke.kA_aufgabe()), "dT", 3.51, 0.005),
    ("Keramik mit Deckel Q1", E(kA=0.56 * ke.kA_aufgabe()), "Q1", 24.72, 0.005),
    ("Keramik mit Deckel Q2", E(kA=0.56 * ke.kA_aufgabe()), "Q2", 28.08, 0.005),
    ("Keramik mit Deckel 30 min", E(kA=0.56 * ke.kA_aufgabe()), "schwarz30", 59.81, 0.005),
    ("Keramik mit Deckel Zeitkonstante", E(kA=0.56 * ke.kA_aufgabe()), "tauMin", 73.1, 0.05),
    ("Edelstahl kA", E(kA=0.90 * ke.kA_aufgabe()), "kA", 0.3062, 5e-5),
    ("Edelstahl 30 min", E(kA=0.90 * ke.kA_aufgabe()), "schwarz30", 51.03, 0.005),
    ("Edelstahl Zeitkonstante", E(kA=0.90 * ke.kA_aufgabe()), "tauMin", 45.5, 0.05),
    ("Edelstahl Unterschied", E(kA=0.90 * ke.kA_aufgabe()), "dT", 3.86, 0.005),
    ("Thermobecher offen kA", E(kA=0.44 * ke.kA_aufgabe()), "kA", 0.1497, 5e-5),
    ("Thermobecher offen 30 min", E(kA=0.44 * ke.kA_aufgabe()), "schwarz30", 63.47, 0.005),
    ("Thermobecher offen Zeitkonstante", E(kA=0.44 * ke.kA_aufgabe()), "tauMin", 93.1, 0.05),
    ("Thermobecher offen Unterschied", E(kA=0.44 * ke.kA_aufgabe()), "dT", 3.17, 0.005),
    # T2: kA festgehalten mit Becher
    ("kA fest 0,3402 mit Becher theta1", E(becher=True), "th1", 39.11, 0.005),
    ("kA fest 0,3402 mit Becher theta2", E(becher=True), "th2", 36.06, 0.005),
    ("kA fest 0,3402 mit Becher Unterschied", E(becher=True), "dT", 3.05, 0.005),
    ("kA fest 0,3402 mit Becher Q1", E(becher=True), "Q1", 40.46, 0.005),
    ("kA fest 0,3402 mit Becher Q2", E(becher=True), "Q2", 44.16, 0.005),
    ("kA fest 0,3402 mit Becher 30 min", E(becher=True), "schwarz30", 54.23, 0.005),
    ("Deckel und Becher, kA fest: theta1", E(becher=True, kA=0.56 * ke.kA_aufgabe()), "th1", 49.80, 0.005),
    ("Deckel und Becher, kA fest: theta2", E(becher=True, kA=0.56 * ke.kA_aufgabe()), "th2", 47.28, 0.005),
    ("Deckel und Becher, kA fest: Unterschied", E(becher=True, kA=0.56 * ke.kA_aufgabe()), "dT", 2.53, 0.005),
    # T4 und T9 (Abschnitt 8.5)
    ("8.5 300/50 ml, 90/10/25 °C, kA 0,25: theta1", E(VK_ml=300, VM_ml=50, thK0=90, thM=10, thU=25, kA=0.25), "th1", 54.04, 0.005),
    ("8.5 300/50 ml, 90/10/25 °C, kA 0,25: theta2", E(VK_ml=300, VM_ml=50, thK0=90, thM=10, thU=25, kA=0.25), "th2", 50.21, 0.005),
    ("8.5 300/50 ml, 90/10/25 °C, kA 0,25: Q1", E(VK_ml=300, VM_ml=50, thK0=90, thM=10, thU=25, kA=0.25), "Q1", 36.16, 0.005),
    ("8.5 300/50 ml, 90/10/25 °C, kA 0,25: Q2", E(VK_ml=300, VM_ml=50, thK0=90, thM=10, thU=25, kA=0.25), "Q2", 41.74, 0.005),
    ("8.5 kA 0,05: theta1", E(kA=0.05), "th1", 61.82, 0.005),
    ("8.5 kA 0,05: theta2", E(kA=0.05), "th2", 60.32, 0.005),
    ("8.5 kA 1,00: theta1", E(kA=1.0), "th1", 21.18, 0.005),
    ("8.5 kA 1,00: theta2", E(kA=1.0), "th2", 18.80, 0.005),
    ("8.5 fest, Kaffee 95 °C: theta1", E(thK0=95.0), "th1", 37.69, 0.005),
    ("8.5 fest, Kaffee 95 °C: theta2", E(thK0=95.0), "th2", 33.22, 0.005),
    ("8.5 Messung, Kaffee 95 °C: kA", E(thK0=95.0, kAQuelle="messung"), "kA", 0.6512, 5e-5),
    ("8.5 Messung, Kaffee 95 °C: theta1", E(thK0=95.0, kAQuelle="messung"), "th1", 25.50, 0.005),
    ("8.5 Messung, Kaffee 95 °C: theta2", E(thK0=95.0, kAQuelle="messung"), "th2", 22.06, 0.005),
    ("8.5 fest, Kaffee 100 ml: theta1", E(VK_ml=100), "th1", 24.45, 0.005),
    ("8.5 fest, Kaffee 100 ml: theta2", E(VK_ml=100), "th2", 19.10, 0.005),
    ("8.5 Messung, Kaffee 100 ml: kA", E(VK_ml=100, kAQuelle="messung"), "kA", 0.1701, 5e-5),
    ("8.5 Messung, Kaffee 100 ml: theta1", E(VK_ml=100, kAQuelle="messung"), "th1", 33.85, 0.005),
    ("8.5 Messung, Kaffee 100 ml: theta2", E(VK_ml=100, kAQuelle="messung"), "th2", 27.35, 0.005),
    ("8.5 fest, Kaffee 400 ml: theta1", E(VK_ml=400), "th1", 47.74, 0.005),
    ("8.5 fest, Kaffee 400 ml: theta2", E(VK_ml=400), "th2", 45.86, 0.005),
    ("8.5 Messung, Kaffee 400 ml: kA", E(VK_ml=400, kAQuelle="messung"), "kA", 0.6805, 5e-5),
    ("8.5 fest, Raum 30 °C: theta1", E(thU=30.0), "th1", 41.26, 0.005),
    ("8.5 fest, Raum 30 °C: theta2", E(thU=30.0), "th2", 36.91, 0.005),
    ("8.5 Messung, Raum 30 °C: kA", E(thU=30.0, kAQuelle="messung"), "kA", 0.4195, 5e-5),
    ("8.5 fest, Raum 10 °C: theta1", E(thU=10.0), "th1", 26.83, 0.005),
    ("8.5 fest, Raum 10 °C: theta2", E(thU=10.0), "th2", 23.48, 0.005),
    ("8.5 Messung, Raum 10 °C: kA", E(thU=10.0, kAQuelle="messung"), "kA", 0.2863, 5e-5),
    ("8.5 fest, Kaffee 60 °C: theta1", E(thK0=60.0), "th1", 29.19, 0.005),
    ("8.5 fest, Kaffee 60 °C: theta2", E(thK0=60.0), "th2", 26.16, 0.005),
    ("8.5 Milch 100 ml: theta1", E(VM_ml=100), "th1", 33.24, 0.005),
    ("8.5 Milch 100 ml: theta2", E(VM_ml=100), "th2", 24.43, 0.005),
]


def groesse(r, name):
    if name == "dQ":
        return r["Q2"] - r["Q1"]
    if name == "q1_0":
        return r["q1"][0]
    if name == "q2_0":
        return r["q2"][0]
    if name == "q1_60":
        return r["q1"][1]
    if name == "q2_60":
        return r["q2"][1]
    return r[name]


def py_als_js(e, zeiten):
    """Python-Referenz in den Namen der JS-Ausgabe."""
    r = ke.auswerten(e)
    o = dict(kA=r["kA"], th10=r["th10"], th1=r["th1"], th2=r["th2"], th2K=r["th2K"], th2Raum=r["th2_raum"], dT=r["dT"],
             Q1=r["Q1"], Q2=r["Q2"], milch=r["milch"], energieRest=r["energie_rest"], tSchnitt=r["t_schnitt"],
             tWaermestrom=r["t_waermestrom"], flaecheVor=r["flaeche_vor"], flaecheNach=r["flaeche_nach"],
             schwarz30=r["schwarz30"], tauMin=r["tau_min"], thMessModell=r["thMess_modell"])
    o["k1"] = [r["kurve1"](t) for t in zeiten]
    o["k2"] = [r["kurve2"](t) for t in zeiten]
    kA, U = r["kA"], e["thU"]
    o["q1"] = [e["kA1Faktor"] * kA * (r["kurve1"](t) - U) for t in zeiten]
    o["q2"] = [kA * (r["kurve2"](t) - U) for t in zeiten]
    return o


def test_fest():
    faelle = [{"e": e, "zeiten": [0, e["tEnd_min"]]} for _, e, _, _, _ in FEST]
    out = js(faelle)["faelle"]
    for (name, e, g, soll, tol), j in zip(FEST, out):
        p = py_als_js(e, [0, e["tEnd_min"]])
        vp, vj = groesse(p, g), groesse(j, g)
        pruefe("fest: " + name, nah(vp, soll, tol) and nah(vj, soll, tol), "Python %.6f, JS %.6f, Soll %s" % (vp, vj, soll))
    # M4, M9, M10, Ausgleich, größter Unterschied
    extra = {"ausgleich": [
        {"punkte": [[t, ke.auswerten(E())["kurve2"](t)] for t in (10, 20, 30, 40, 50, 60)], "th0": 80.0, "thU": 20.0, "C_KB": 836.0},
        {"punkte": [[10, 67.3], [20, 56.9], [30, 49.1], [40, 42.7], [50, 37.4], [60, 33.7]], "th0": 80.1, "thU": 20.0, "C_KB": 836.0},
        {"punkte": [[10, 67.00], [20, 57.34], [30, 50.04], [40, 44.43]], "th0": 80.0, "thU": 20.0, "C_KB": 836.0}]}
    sonder = [{"e": E(), "tV": 90}, {"e": E(), "tV": 120}, {"e": E(kA1Faktor=1.05), "tV": 90},
              {"e": E(becher=True, kAQuelle="messung"), "tV": 90},
              {"e": E(becher=True, kA=0.444031473), "kalt": True},
              {"e": E(), "trink": 60}, {"e": E(kA=0.56 * ke.kA_aufgabe()), "trink": 60},
              {"e": E(becher=True, kAQuelle="messung"), "trink": 60},
              {"e": E(), "gu": True}, {"e": E(becher=True, kAQuelle="messung"), "gu": True}]
    d = js(sonder, extra)
    s = d["faelle"]
    pruefe("M4 Zugabe 60, Vergleich 90: 27,41 / 25,38 / 2,03", nah(s[0]["nach"]["th1"], 27.41, .005) and nah(s[0]["nach"]["th2"], 25.38, .005) and nah(s[0]["nach"]["dT"], 2.03, .005))
    pruefe("M4 Vergleich 120: 1,07 K", nah(s[1]["nach"]["dT"], 1.07, .005))
    pruefe("M4 kA Tasse 1 · 1,05, Vergleich 90: 1,35506 K (nicht 1,57380)", nah(s[2]["nach"]["dT"], 1.35506, 5e-6), "%.6f" % s[2]["nach"]["dT"])
    pruefe("M4 mit Becher (Teil g), Vergleich 90: 1,59 K", nah(s[3]["nach"]["dT"], 1.59, .005))
    k = s[4]["kalt"]
    pruefe("M9 Becher kalt: 59,85 / 65,98 / 30,67 / 28,05 / 2,62", nah(k["th1_0"], 59.85, .005) and nah(k["thK_0"], 65.98, .005)
           and nah(k["th1"], 30.67, .005) and nah(k["th2"], 28.05, .005) and nah(k["dT"], 2.62, .005))
    pruefe("M10 Trinkzeit Standard 10,90 / 16,60 min", nah(s[5]["trink"]["tasse1"], 10.90, .005) and nah(s[5]["trink"]["schwarz"], 16.60, .005))
    pruefe("M10 Trinkzeit Deckel 19,47 / 29,65 min", nah(s[6]["trink"]["tasse1"], 19.47, .005) and nah(s[6]["trink"]["schwarz"], 29.65, .005))
    pruefe("M10 Trinkzeit Becher (Teil g) 12,35 / 16,60 min", nah(s[7]["trink"]["tasse1"], 12.35, .005) and nah(s[7]["trink"]["schwarz"], 16.60, .005))
    g0, gb = s[8]["gu"], s[9]["gu"]
    pruefe("größter Unterschied ohne Becher 3,862 K bei 35,38 °C, 55,7 min", nah(g0["dT_max"], 3.862, 5e-4) and nah(g0["th_x"], 35.38, .005) and nah(g0["t_min"], 55.7, .05))
    pruefe("größter Unterschied mit Becher 3,090 K bei 35,78 °C, 54,7 min", nah(gb["dT_max"], 3.090, 5e-4) and nah(gb["th_x"], 35.78, .005) and nah(gb["t_min"], 54.7, .05))
    a = d["extra"]["ausgleich"]
    pruefe("M2 T09 exakte (ungerundete) Modellreihe 10 bis 60 min: alle 0,3402 W/K", nah(a[0]["kA_ursprung"], 0.3402, 5e-5) and nah(a[0]["kA_frei"], 0.3402, 5e-5))
    pruefe("M2 T10: Ursprung 0,3423, frei 0,3444, Abschnitt +0,007", nah(a[1]["kA_ursprung"], 0.3423, 5e-5) and nah(a[1]["kA_frei"], 0.3444, 5e-5) and nah(a[1]["achsenabschnitt"], 0.007, 5e-4))
    pruefe("M2 gekrümmte Reihe 10 bis 40 min: 0,3187 W/K", nah(a[2]["kA_ursprung"], 0.3187, 5e-5))
    py = [ke.ausgleich([tuple(p) for p in x["punkte"]], x["th0"], x["thU"], x["C_KB"]) for x in extra["ausgleich"]]
    pruefe("M2 JS gleich Python (drei Reihen)", all(nah(py[i][k2], a[i][k2], 1e-12) for i in range(3) for k2 in ["kA_ursprung", "kA_frei", "achsenabschnitt"]))
    pruefe("KA_AUFGABE gleich Python", nah(d["extra"]["KA_AUFGABE"], ke.kA_aufgabe(), 1e-15))
    pruefe("Voreinstellungen gleich Tabelle 8.2.1", [(v["id"], v["faktor"]) for v in d["extra"]["VOREINSTELLUNGEN"]] == [(i, f) for i, f, _ in ke.VOREINSTELLUNGEN])


# ---------------------------------------------------------------- 2 Zufallstests JS gegen Python
TOL = dict(temp=1e-9, kJ=1e-9, W=1e-9, kA=1e-12, min_abs=1e-7, min_rel=1e-10)
GROESSEN = [("kA", "kA"), ("th10", "temp"), ("th1", "temp"), ("th2", "temp"), ("th2K", "temp"), ("th2Raum", "temp"), ("dT", "temp"),
            ("Q1", "kJ"), ("Q2", "kJ"), ("milch", "kJ"), ("flaecheVor", "kJ"), ("flaecheNach", "kJ"), ("schwarz30", "temp"),
            ("tauMin", "min"), ("tSchnitt", "min"), ("tWaermestrom", "min"), ("thMessModell", "temp")]


def zufallssatz(rng):
    """Gleichverteilt über die Reglerbereiche der Vertiefung (Konzept A.4):
    VK 100..400 ml, VM 5..100 ml, thK0 60..95 °C, thM 2..65 °C, thU 10..30 °C, tZ 1..180 min, Becher je zur Hälfte (Masse 100..600 g),
    Milch für Tasse 2 bei Raumtemperatur in 30 %, kA Tasse 1 relativ: zur Hälfte genau 1, sonst 0,90..1,10;
    kA-Quelle zur Hälfte "fest" (kA 0,05..1,00 W/K), sonst "messung" (Messwert gleichverteilt zwischen max(thU, 30) und min(thK0, 90), Ränder ausgenommen)."""
    e = dict(VK_ml=rng.uniform(100, 400), VM_ml=rng.uniform(5, 100), thK0=rng.uniform(60, 95), thM=rng.uniform(2, 65),
             thU=rng.uniform(10, 30), tEnd_min=rng.uniform(1, 180), becher=rng.random() < 0.5, mB_g=rng.uniform(100, 600),
             milch2Raum=rng.random() < 0.3, kA1Faktor=1.0 if rng.random() < 0.5 else rng.uniform(0.9, 1.1))
    if rng.random() < 0.5:
        e.update(kAQuelle="fest", kA=rng.uniform(0.05, 1.0), thMess=67.0)
    else:
        lo, hi = max(e["thU"], 30.0), min(e["thK0"], 90.0)
        e.update(kAQuelle="messung", kA=None, thMess=rng.uniform(lo + 0.01, hi - 0.01))
    return e


def test_zufall(n=10000):
    rng = random.Random(20261105)
    saetze = [zufallssatz(rng) for _ in range(n)]
    faelle = []
    for e in saetze:
        tz = e["tEnd_min"]
        zeiten = [0.0, tz * rng.random(), tz * (1 - 1e-9), tz]      # Anfang, zufällig, unmittelbar vor und bei der Zugabe
        faelle.append({"e": e, "zeiten": zeiten, "tV": tz + 10.0})
    out = js(faelle)["faelle"]
    fehler = []
    for f, j in zip(faelle, out):
        e = f["e"]
        if ke.fehler(e) or j.get("fehler"):
            if ke.fehler(e) != j.get("fehler", ""):
                fehler.append(dict(e=e, grund="Gültigkeit verschieden", py=ke.fehler(e), js=j.get("fehler")))
            continue
        p = py_als_js(e, f["zeiten"])
        for g, art in GROESSEN:
            a, b = p[g], j[g]
            if isinstance(b, str) or isinstance(a, float) and math.isinf(a):
                if not (isinstance(b, str) and math.isinf(a) and (b == "inf") == (a > 0)):
                    fehler.append(dict(e=e, groesse=g, py=str(a), js=b))
                continue
            if art == "min":
                ok = abs(a - b) <= TOL["min_abs"] or abs(a - b) <= TOL["min_rel"] * abs(a)
            else:
                ok = abs(a - b) <= TOL[art]
            if not ok:
                fehler.append(dict(e=e, groesse=g, py=a, js=b))
        for key, art in [("k1", "temp"), ("k2", "temp"), ("q1", "W"), ("q2", "W")]:
            for a, b in zip(p[key], j[key]):
                if abs(a - b) > TOL[art]:
                    fehler.append(dict(e=e, groesse=key, py=a, js=b))
        nz = ke.nach_zugabe(e, f["tV"])
        for k2 in ["th1", "th2", "dT"]:
            if abs(nz[k2] - j["nach"][k2]) > TOL["temp"]:
                fehler.append(dict(e=e, groesse="nach." + k2, py=nz[k2], js=j["nach"][k2]))
    os.makedirs(FEHLER_DIR, exist_ok=True)
    pfad = os.path.join(FEHLER_DIR, "zufall_20261105.json")
    if fehler:
        json.dump(fehler[:200], open(pfad, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    elif os.path.exists(pfad):
        os.remove(pfad)
    pruefe("Zufall: %d Sätze, JS gegen Python an 4 Zeitpunkten je Satz (0, zufällig, unmittelbar vor und bei der Zugabe) und 10 min danach" % n,
           not fehler, "%d Abweichungen über der Toleranz%s" % (len(fehler), (" (" + pfad + ")") if fehler else ""))
    return saetze


# ---------------------------------------------------------------- 3 Physik
def test_physik(saetze):
    rest = max(abs(ke.auswerten(e)["energie_rest"]) for e in saetze[:2000] if not ke.fehler(e))
    pruefe("Energiebilanz mit Milchbeitrag: C_GB dT = Q2 - Q1 + C_M (thM1 - thM2), 2000 Sätze", rest <= 1e-9, "größter Rest %.2e kJ" % rest)
    # Mischtemperaturen aus den Wärmekapazitäten
    mx = 0.0
    for e in saetze[:2000]:
        if ke.fehler(e):
            continue
        r = ke.auswerten(e)
        soll1 = (r["C_KB"] * e["thK0"] + r["C_M"] * e["thM"]) / r["C_GB"]
        thM2 = e["thU"] if e["milch2Raum"] else e["thM"]
        soll2 = (r["C_KB"] * r["th2K"] + r["C_M"] * thM2) / r["C_GB"]
        mx = max(mx, abs(soll1 - r["th10"]), abs(soll2 - r["th2"]))
    pruefe("Mischtemperaturen folgen aus den Wärmekapazitäten (Tasse 1 bei 0, Tasse 2 bei der Zugabe)", mx <= 1e-9, "%.1e K" % mx)
    # Monotonie zwischen den Mischereignissen
    schlecht = 0
    for e in saetze[:500]:
        if ke.fehler(e):
            continue
        r = ke.auswerten(e)
        ts = [e["tEnd_min"] * i / 50 for i in range(51)]
        for kurve in (r["kurve1"], r["kurve2"]):
            w = [kurve(t) - e["thU"] for t in ts]
            # Abstand zur Raumtemperatur nimmt strikt ab und wechselt nicht das Vorzeichen. Gültigkeitsbereich: Abstand über 1e-9 K;
            # darunter liegt der Unterschied unter der Gleitkomma-Auflösung einer Temperatur in K (etwa 6e-14 K bei 300 K).
            if not all(abs(w[i + 1]) < abs(w[i]) and w[i + 1] * w[i] > 0 for i in range(50) if abs(w[i + 1]) > 1e-9):
                schlecht += 1
    pruefe("Zwischen den Mischereignissen nähert sich jede Temperatur monoton der Raumtemperatur (500 Sätze, Abstand über 1e-9 K)", schlecht == 0, "%d Verstöße" % schlecht)
    # Größter Unterschied über einen Bereich von kA
    werte0 = [ke.groesster_unterschied(E(kA=k)) for k in [0.05 + 0.05 * i for i in range(20)]]
    werteb = [ke.groesster_unterschied(E(kA=k, becher=True)) for k in [0.05 + 0.05 * i for i in range(20)]]
    pruefe("größter Unterschied ohne Becher für kA 0,05 bis 1,00 W/K gleich 3,862 K", all(nah(w["dT_max"], werte0[0]["dT_max"], 1e-9) for w in werte0) and nah(werte0[0]["dT_max"], 3.862, 5e-4))
    pruefe("größter Unterschied mit Becher für kA 0,05 bis 1,00 W/K gleich 3,090 K", all(nah(w["dT_max"], werteb[0]["dT_max"], 1e-9) for w in werteb) and nah(werteb[0]["dT_max"], 3.090, 5e-4))
    t_ = ke.groesster_unterschied(E(kA=0.56 * ke.kA_aufgabe()))["t_min"]
    pruefe("Zeitpunkt des größten Unterschieds mit kA · 0,56: 99,5 min", nah(t_, 99.5, 0.05), "%.3f min" % t_)
    for lab, e in [("ohne Becher", E()), ("mit Becher (Teil g)", E(becher=True, kAQuelle="messung")), ("Deckel", E(kA=0.56 * ke.kA_aufgabe()))]:
        a, n = ke.groesster_unterschied(e), ke.groesster_unterschied_numerisch(e, t_max_min=200.0, schritte=40000)
        pruefe("größter Unterschied analytisch gleich Raster (%s)" % lab, nah(a["dT_max"], n["dT_max"], 1e-4) and nah(a["t_min"], n["t_min"], 0.05),
               "%.5f K bei %.2f min gegen %.5f K bei %.2f min" % (a["dT_max"], a["t_min"], n["dT_max"], n["t_min"]))
    d60 = ke.auswerten(E(kA=0.56 * ke.kA_aufgabe()))["dT"]
    pruefe("Unterschied nach festen 60 min mit Deckel (3,51 K) ist eine andere Größe als der größte Unterschied (3,86 K)", nah(d60, 3.51, 0.005))
    # kA festhalten gegen kA aus der Messung (F2-15, 8.5)
    a, b = ke.auswerten(E(thK0=95.0)), ke.auswerten(E(thK0=95.0, kAQuelle="messung"))
    pruefe("kA festhalten: kA bleibt bei Kaffee 95 °C gleich (0,3402 W/K)", nah(a["kA"], ke.kA_aufgabe(), 1e-12))
    pruefe("kA aus der Messung: kA wird bei Kaffee 95 °C neu bestimmt (0,6512 W/K)", nah(b["kA"], 0.6512, 5e-5))
    a = ke.auswerten(E(becher=True))
    pruefe("kA festhalten mit Becher: kA bleibt 0,3402 W/K, Becher speichert zusätzlich", nah(a["kA"], ke.kA_aufgabe(), 1e-12) and a["th1"] > 34.05)
    # gleichwertiger Messwert reproduziert kA (M8) für alle festen Sätze
    mx = max(abs(ke.auswerten(e)["kA"] - e["kA"]) / e["kA"] for e in saetze if e["kAQuelle"] == "fest" and not ke.fehler(e))
    pruefe("M8: Grundmodell rechnet aus dem gleichwertigen Messwert genau das festgehaltene kA", mx <= 1e-12, "relativ %.1e" % mx)


# ---------------------------------------------------------------- 4 Ungültige und extreme Eingaben
def test_ungueltig():
    faelle = [
        ("Anfang gleich Raum", E(thK0=20.0, thU=20.0), "anfang_ueber_raum"),
        ("Anfang unter Raum", E(thK0=60.0, thU=70.0), "anfang_ueber_raum"),
        ("Messung über Anfang", E(kAQuelle="messung", thMess=85.0), "messung_zwischen"),
        ("Messung gleich Raum", E(kAQuelle="messung", thMess=20.0), "messung_zwischen"),
        ("kA null", E(kA=0.0), "kA_positiv"),
        ("kA negativ", E(kA=-0.1), "kA_positiv"),
        ("kA leer (keine Zahl; in JSON als null)", E(kA=None), "kA_positiv"),
        ("Anfang leer (keine Zahl; in JSON als null)", E(thK0=None), "anfang_ueber_raum"),
    ]
    out = js([{"e": e} for _, e, _ in faelle])["faelle"]
    for (name, e, soll), j in zip(faelle, out):
        pruefe("ungültig: %s meldet %s (Python und JS)" % (name, soll), ke.fehler(e) == soll and j.get("fehler") == soll, "Python %s, JS %s" % (ke.fehler(e), j.get("fehler")))
    extrem = [E(VK_ml=100, VM_ml=100, thK0=95, thM=2, thU=10, tEnd_min=180, kA=1.0), E(VK_ml=400, VM_ml=5, thK0=60, thM=65, thU=30, tEnd_min=1, kA=0.05),
              E(kAQuelle="messung", thMess=79.99), E(kAQuelle="messung", thMess=20.01), E(tEnd_min=180, becher=True, mB_g=600, kA1Faktor=1.1)]
    out = js([{"e": e, "zeiten": [0, e["tEnd_min"]]} for e in extrem])["faelle"]
    endlich = all(all(isinstance(j[g], (int, float)) and math.isfinite(j[g]) for g in ["kA", "th1", "th2", "Q1", "Q2", "dT"]) for j in out)
    pruefe("extreme Ränder der Regler: alle Ergebnisse endlich, JS gleich Python", endlich and all(
        nah(py_als_js(e, [0])["th2"], j["th2"], 1e-9) for e, j in zip(extrem, out)))


if __name__ == "__main__":
    test_identitaet()
    test_fest()
    s = test_zufall()
    test_physik(s)
    test_ungueltig()
    n_ok = sum(1 for ok, _, _ in ERG if ok)
    print("\nErgebnis: %d von %d Prüfungen bestanden." % (n_ok, len(ERG)))
    sys.exit(0 if n_ok == len(ERG) else 1)
