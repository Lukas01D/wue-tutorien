# -*- coding: utf-8 -*-
"""Prüft das Simulationstool Kaffee_Simulation.html gegen das Rechenmodell kaffee_modell.py.

1. Der Modellteil des Tools (zwischen MODELL-ANFANG und MODELL-ENDE) läuft unverändert in Node.
2. Standardwerte: Das Tool trifft die Zahlen der Lösung (gerundet wie gedruckt), und jede dieser Zahlen steht in Kaffee_Loesung.md.
3. Weitere Parametersätze: Endtemperaturen, kA, Mischtemperatur, Kurvenpunkte, abgegebene Wärme und Schnittpunkt stimmen
   mit dem Python-Modell überein (relative Abweichung unter 1e-9).
Aufruf vom Repository aus: python3 ergebnisse/kaffee/simulation/test_simulation.py   (braucht node)
"""
import json, math, os, re, subprocess, sys, tempfile

HIER = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HIER)))
KAFFEE = os.path.join(REPO, "pruefung", "Kaffee_Pruefpaket_2026-10-23", "umsetzung", "Arbeitsordner", "kaffee")
sys.path.insert(0, KAFFEE)
from kaffee_modell import P, rechne, zwei_tassen   # noqa: E402

K = 273.15
html = open(os.path.join(HIER, "Kaffee_Simulation.html"), encoding="utf-8").read()
modell_js = html[html.index("// MODELL-ANFANG"):html.index("// MODELL-ENDE")]

STANDARD = dict(tEnd_min=60, thM=5, milch2Raum=False, VM_ml=30, thU=20, becher=False, thK0=80, thMess=67, VK_ml=200,
                kA1Faktor=1.0, mB_g=300)


def tool(einstellungen, zeiten_s):
    """Modell des Tools in Node auswerten; Kurven an den angegebenen Zeiten (in s)."""
    js = modell_js + """
const S = JSON.parse(process.argv[2]), Z = JSON.parse(process.argv[3]);
console.log(JSON.stringify(S.map(e => { const m = berechne(e); const o = {};
  for (const k in m) if (typeof m[k] === "number") o[k] = isFinite(m[k]) ? m[k] : null;
  o.k1 = Z.map(t => m.kurve1(t)); o.k2 = Z.map(t => m.kurve2(t)); return o; })));
"""
    with tempfile.TemporaryDirectory() as d:
        f = os.path.join(d, "modell.js")
        open(f, "w", encoding="utf-8").write(js)
        out = subprocess.run(["node", f, json.dumps(einstellungen), json.dumps(zeiten_s)], capture_output=True, text=True, check=True)
    return json.loads(out.stdout)


def python(e):
    """Dieselbe Einstellung mit kaffee_modell.py."""
    p = dict(P, V_K=e["VK_ml"] * 1e-6, V_M=e["VM_ml"] * 1e-6, th_K0=e["thK0"], th_M=e["thM"], th_U=e["thU"], th_mess=e["thMess"],
             m_B=e["mB_g"] / 1000, t_end=e["tEnd_min"] * 60.0)
    r = rechne(p)
    C_T = p["m_B"] * p["c_B"] if e["becher"] else 0.0
    th_M2 = p["th_U"] if e["milch2Raum"] else p["th_M"]
    z = zwei_tassen(p, C_T=C_T, th_M1=p["th_M"], th_M2=th_M2, kA1_faktor=e["kA1Faktor"])
    kurve = lambda t: zwei_tassen(p, C_T=C_T, th_M1=p["th_M"], th_M2=th_M2, kA1_faktor=e["kA1Faktor"], t_end=t)
    return p, r, C_T, z, kurve


def gleich(a, b, rel=1e-9):
    return abs(a - b) <= rel * max(1.0, abs(b))


fehler, zeilen = [], []


def pruefe(name, ok, info=""):
    zeilen.append(f"{'ok    ' if ok else 'FEHLER'} {name}{('  ' + info) if info else ''}")
    if not ok:
        fehler.append(name)


# ---------------------------------------------------------------- 2. Standardwerte und Zahlen der Lösung
loesung = open(os.path.join(KAFFEE, "Kaffee_Loesung.md"), encoding="utf-8").read()
de = lambda x, n: f"{x:.{n}f}".replace(".", ",")
faelle = {
    "Standard": dict(STANDARD),
    "Becher (g)": dict(STANDARD, becher=True),
    "erwärmte Milch (f)": dict(STANDARD, thM=60),
    "Milch für Tasse 2 bei Raumtemperatur (Zusatzfrage 2)": dict(STANDARD, milch2Raum=True),
    "Versuch 40 min mit Becher": dict(STANDARD, tEnd_min=40, becher=True),
    "Versuch 40 min ohne Becher": dict(STANDARD, tEnd_min=40),
}
erg = dict(zip(faelle, tool(list(faelle.values()), [0.0])))
s, b, f, h2, v40b, v40 = (erg[k] for k in faelle)
soll = [  # (Bezeichnung, Wert im Tool, Stellen, Schreibweise in der Lösung)
    ("a) Mischtemperatur", s["T1_0"] - K, 2, "70{,}47"),
    ("c) kA", s["kA"], 4, "0{,}3402"),
    ("d) Tasse 1", s["th1"], 2, "34{,}05"),
    ("d) Tasse 2", s["th2"], 2, "30{,}19"),
    ("d) Unterschied", s["dT"], 2, "3{,}85"),
    ("e) Q1 in kJ", s["Q1"] / 1e3, 2, "34{,}88"),
    ("e) Q2 in kJ", s["Q2"] / 1e3, 2, "38{,}57"),
    ("Abb. L2 Schnittpunkt in min", s["t_schnitt"] / 60, 0, "etwa 56 min"),
    ("f) Tasse 1", f["th1"], 2, "35{,}99"),
    ("f) Tasse 2", f["th2"], 2, "37{,}18"),
    ("g) kA mit Becher", b["kA"], 4, "0{,}4440"),
    ("g) Tasse 1 mit Becher", b["th1"], 2, "34{,}04"),
    ("g) Tasse 2 mit Becher", b["th2"], 2, "30{,}96"),
    ("Zusatzfrage (2): Tasse 2 mit Milch bei Raumtemperatur", h2["th2"], 2, "32{,}10"),
    ("Zusatzfrage (2): Tasse 2 mindestens kühler um", h2["dT"], 2, "1{,}95"),
    ("Versuch 40 min, Modell mit Becher", v40b["dT"], 2, "2,97 K"),
    ("Versuch 40 min, Modell aus d)", v40["dT"], 2, "3,70 K"),
]
for name, wert, n, schreib in soll:
    gerundet = de(wert, n)
    ok_wert = gerundet.replace(",", "{,}") in schreib or gerundet in schreib
    pruefe(f"Lösung: {name} = {gerundet}", ok_wert and schreib in loesung, f"(in Kaffee_Loesung.md: „{schreib}“)")

# Zusatzfrage (1): Milchtemperatur für gleich warme Tassen, mit dem Tool durch Bisektion gesucht
lo, hi = 0.0, 100.0
for _ in range(60):
    mid = (lo + hi) / 2
    d_mid = tool([dict(STANDARD, thM=mid)], [0.0])[0]["dT"]
    lo, hi = (mid, hi) if d_mid > 0 else (lo, mid)
pruefe(f"Lösung: Zusatzfrage (1) Milchtemperatur für Gleichstand = {de(lo, 1)} °C", de(lo, 1) == "47,0" and "47{,}0" in loesung)

# ---------------------------------------------------------------- 3. Vergleich mit dem Python-Modell
saetze = [
    dict(STANDARD),
    dict(STANDARD, tEnd_min=15, thM=8, VM_ml=50, thU=22),
    dict(STANDARD, tEnd_min=90, thM=45, VM_ml=20, thU=18, becher=True, mB_g=450),
    dict(STANDARD, tEnd_min=120, thM=62, milch2Raum=True, thK0=85, thMess=70),
    dict(STANDARD, tEnd_min=35, thM=3, VM_ml=100, thU=12, thK0=70, thMess=58, VK_ml=300, kA1Faktor=1.05),
    dict(STANDARD, tEnd_min=60, thM=20, VM_ml=40, thU=25, becher=True, thK0=90, thMess=80, VK_ml=150, kA1Faktor=0.95, mB_g=200),
    dict(STANDARD, tEnd_min=5, thM=5, VM_ml=5, thU=10, thK0=60, thMess=50, VK_ml=400),
    dict(STANDARD, tEnd_min=75, thM=55, milch2Raum=True, becher=True, kA1Faktor=1.10, mB_g=600),
]
for i, e in enumerate(saetze, 1):
    p, r, C_T, z, kurve = python(e)
    zeiten = [0.0, 600.0, 0.37 * p["t_end"], p["t_end"]]
    t = tool([e], zeiten)[0]
    werte = [("kA", t["kA"], z["kA"]), ("T1_0", t["T1_0"], z["T1_0"]), ("T1", t["T1"], z["T1"]), ("T2_K", t["T2_K"], z["T2_K"]),
             ("T2", t["T2"], z["T2"]), ("dT", t["dT"], z["dT"])]
    werte += [(f"Kurve Tasse 1 bei {tz:.0f} s", k1, kurve(tz)["T1"]) for tz, k1 in zip(zeiten, t["k1"])]
    werte += [(f"Kurve Tasse 2 bei {tz:.0f} s", k2, kurve(tz)["T2_K"]) for tz, k2 in zip(zeiten, t["k2"])]
    if C_T == 0.0 and not e["milch2Raum"] and e["kA1Faktor"] == 1.0:
        # ohne Becher und mit gleicher Milch: abgegebene Wärme und Schnittpunkt direkt aus rechne()
        werte += [("Q1 (rechne)", t["Q1"], r["Q1"]), ("Q2 (rechne)", t["Q2"], r["Q2"])]
        if t["t_schnitt"] is not None and math.isfinite(r["t_schnitt"]):
            werte.append(("Schnittpunkt (rechne)", t["t_schnitt"], r["t_schnitt"]))
    else:
        # mit Becher oder anderer Milch: Energiebilanz um den Bilanzraum mit den Temperaturen des Python-Modells
        werte += [("Q1 (Energiebilanz)", t["Q1"], (r["C_G"] + C_T) * (z["T1_0"] - z["T1"])),
                  ("Q2 (Energiebilanz)", t["Q2"], (r["C_K"] + C_T) * (r["T_K0"] - z["T2_K"]))]
        if t["t_schnitt"] is not None and t["t_schnitt"] > 0:
            k = kurve(t["t_schnitt"])                                       # am Schnittpunkt sind beide Kurven gleich
            werte.append(("Schnittpunkt: Kurven gleich (Python)", k["T1"], k["T2_K"]))
    abw = [(n, a, b_) for n, a, b_ in werte if not gleich(a, b_)]
    pruefe(f"Satz {i}: {len(werte)} Werte gleich dem Python-Modell", not abw,
           "; ".join(f"{n}: Tool {a:.10g}, Python {b_:.10g}" for n, a, b_ in abw[:3]) if abw else
           ", ".join(f"{k}={v}" for k, v in e.items() if STANDARD.get(k) != v) or "Standardwerte")

text = "\n".join(["Test des Simulationstools gegen kaffee_modell.py", ""] + zeilen +
                 ["", f"Ergebnis: {len(zeilen) - len(fehler)} von {len(zeilen)} Prüfungen bestanden."])
open(os.path.join(HIER, "test_ergebnis.txt"), "w", encoding="utf-8").write(text + "\n")
print(text)
sys.exit(1 if fehler else 0)
