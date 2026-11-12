# -*- coding: utf-8 -*-
"""A1: Unabhängige Nachrechnung der Kaffee-Aufgabe (Aufarbeitung vom 12.11.2026).

Importiert weder kaffee_modell.py noch werte.py noch den Code der Seite. Grundlage sind nur die Angaben und Gleichungen
des Blatts (Tabelle „Gegeben“, Tutorium 5): C dθ/dt = −kA (θ − θu) + Q̇W, Mischung ohne Verlust, kA aus der Messung nach
10 min. Zwei unabhängige Wege:
  1. geschlossene Formeln des Blatts (nur für den Fall des Blatts: Q̇W = 0, C_T = 0, t = t_Z),
  2. numerische Lösung der Differentialgleichung (Runge-Kutta 4. Ordnung, Schritt 1 s) für jede Einstellung der Seite,
     abgegebene Wärme als Integral ∫ kA (θ − θu) dt (nicht aus der Energiebilanz).
Aufruf: python3 simulation/aufarbeitung/a1_nachrechnung.py   (Ausgabe nach ergebnisse/a1_nachrechnung.txt)
Import: from a1_nachrechnung import blatt_formeln, ode   (für A2 und A3)
"""
import math
import os
import numpy as np

# Angaben des Blatts (Tabelle „Gegeben“)
RHO_K, CP_K = 1000.0, 4180.0       # kg/m³, J/(kg K), Kaffee wie Wasser
RHO_M, CP_M = 1030.0, 3940.0       # Milch
BLATT = dict(VK_ml=200.0, VM_ml=100.0, thK0=80.0, thM=5.0, thU=20.0, mess10=72.0, tZ=45.0)
# Ergebnisse, wie sie auf dem Blatt und in der Lösung stehen (gerundet)
SOLL = dict(kA=0.1994, CG=1241.8, th10=55.49, th1=43.01, th2K=51.51, th2=36.31, dT=6.69, Q1=15.50, Q2=23.82, dQ=8.31)


def blatt_formeln(VK_ml, VM_ml, thK0, thM, thU, tZ, mess10=None, kA=None):
    """Weg 1: Formeln des Blatts. kA entweder aus dem Messwert nach 10 min oder vorgegeben. Zeiten in min."""
    CK = RHO_K * VK_ml * 1e-6 * CP_K
    CM = RHO_M * VM_ml * 1e-6 * CP_M
    CG = CK + CM
    if kA is None:
        kA = CK / 600.0 * math.log((thK0 - thU) / (mess10 - thU))          # aus θ(10 min) = θu + (θK0 − θu) e^(−kA·600/CK)
    th10 = (CK * thK0 + CM * thM) / CG                                     # Mischtemperatur Tasse 1
    th1 = thU + (th10 - thU) * math.exp(-kA * tZ * 60 / CG)               # Tasse 1 nach t_Z
    th2K = thU + (thK0 - thU) * math.exp(-kA * tZ * 60 / CK)              # schwarzer Kaffee nach t_Z
    th2 = (CK * th2K + CM * thM) / CG                                      # Tasse 2 nach der Milch
    Q1 = CG * (th10 - th1)                                                 # abgegebene Wärme = Abnahme der inneren Energie
    Q2 = CK * (thK0 - th2K)
    return dict(CK=CK, CM=CM, CG=CG, kA=kA, th10=th10, th1=th1, th2K=th2K, th2=th2, dT=th1 - th2, Q1=Q1, Q2=Q2, dQ=Q2 - Q1)


def ode(faelle, dt=1.0):
    """Weg 2: numerische Lösung für viele Einstellungen zugleich (Felder wie die schlanke Seite, Zeiten in min).
    Zustand je Tasse: Temperatur θ und abgegebene Wärme Q; dθ/dt = (Q̇W − kA(θ − θu))/C, dQ/dt = kA(θ − θu).
    Tasse 1: Mischung bei t = 0, C = C_G + C_T. Tasse 2: C = C_K + C_T bis t_Z, dann Mischung und C = C_G + C_T.
    Die Tasse ist immer so warm wie ihr Inhalt (wie kaffee_modell.zwei_tassen)."""
    n = len(faelle)
    g = {k: np.array([float(f[k]) for f in faelle]) for k in faelle[0]}
    CK = RHO_K * g["VK_ml"] * 1e-6 * CP_K + g["CT"]
    CM = RHO_M * g["VM_ml"] * 1e-6 * CP_M
    CG = CK + CM
    kA, u, QW = g["kA"], g["thU"], g["QW"]
    nZ = np.rint(g["tZ"] * 60 / dt).astype(int)
    nE = np.rint(g["t"] * 60 / dt).astype(int)
    th1 = (CK * g["thK0"] + CM * g["thM"]) / CG
    th2 = g["thK0"].copy()
    C2 = CK.copy()
    Q1 = np.zeros(n); Q2 = np.zeros(n)
    max1, max2, min1, min2 = th1.copy(), th2.copy(), th1.copy(), th2.copy()
    aus = {k: np.full(n, np.nan) for k in ("th1", "th2", "Q1", "Q2", "th2K", "th2Z")}
    zugabe = {}
    ende = {}
    for i in range(n):
        zugabe.setdefault(nZ[i], []).append(i)
        ende.setdefault(nE[i], []).append(i)
    zugabe = {k: np.array(v) for k, v in zugabe.items()}
    ende = {k: np.array(v) for k, v in ende.items()}

    def f(th, C):
        return (QW - kA * (th - u)) / C, kA * (th - u)

    for s in range(0, int(nE.max()) + 1):
        if s in zugabe:                       # Milch in Tasse 2 (vor dem Schritt ab diesem Zeitpunkt)
            j = zugabe[s]
            aus["th2K"][j] = th2[j]
            th2[j] = (CK[j] * th2[j] + CM[j] * g["thM"][j]) / CG[j]
            C2[j] = CG[j]
            aus["th2Z"][j] = th2[j]
            max2[j] = np.maximum(max2[j], th2[j]); min2[j] = np.minimum(min2[j], th2[j])
        if s in ende:
            j = ende[s]
            for k, v in (("th1", th1), ("th2", th2), ("Q1", Q1), ("Q2", Q2)):
                aus[k][j] = v[j]
        if s == nE.max():
            break
        for th, Q, C in ((th1, Q1, CG), (th2, Q2, C2)):
            a1, b1 = f(th, C)
            a2, b2 = f(th + 0.5 * dt * a1, C)
            a3, b3 = f(th + 0.5 * dt * a2, C)
            a4, b4 = f(th + dt * a3, C)
            th += dt / 6 * (a1 + 2 * a2 + 2 * a3 + a4)
            Q += dt / 6 * (b1 + 2 * b2 + 2 * b3 + b4)
        lauf = s + 1 <= nE                    # nur bis t zählt für Größt- und Kleinstwerte
        max1 = np.where(lauf, np.maximum(max1, th1), max1); min1 = np.where(lauf, np.minimum(min1, th1), min1)
        max2 = np.where(lauf, np.maximum(max2, th2), max2); min2 = np.where(lauf, np.minimum(min2, th2), min2)
    aus.update(max1=max1, max2=max2, min1=min1, min2=min2, CG=CG, CK=CK)
    return aus


def main():
    zeilen = ["A1: Unabhängige Nachrechnung (ohne kaffee_modell.py, ohne Code der Seite)", ""]
    b = blatt_formeln(**BLATT)
    zeilen.append("Weg 1, Formeln des Blatts, Werte des Blatts:")
    fehler = 0
    for k, soll in SOLL.items():
        ist = b[k] / 1000 if k in ("Q1", "Q2", "dQ") else b[k]
        n = 4 if k == "kA" else (1 if k == "CG" else 2)
        ok = ("%.*f" % (n, ist)) == ("%.*f" % (n, soll))
        fehler += not ok
        zeilen.append("  %-5s gerechnet %12.6f  Blatt %s  %s" % (k, ist, ("%.*f" % (n, soll)).replace(".", ","), "gleich" if ok else "ABWEICHUNG"))
    zeilen.append("  Energiebilanz Q2 − Q1 − C_G (θ1 − θ2) = %.3e J" % (b["dQ"] - b["CG"] * b["dT"]))
    # Weg 2 mit denselben Werten, dazu Fälle, die die Seite zeigt
    faelle = [dict(t=45, tZ=45, thM=5, VM_ml=100, thK0=80, VK_ml=200, thU=20, QW=0, kA=b["kA"], CT=0),
              dict(t=90, tZ=45, thM=5, VM_ml=100, thK0=80, VK_ml=200, thU=20, QW=0, kA=b["kA"], CT=0),
              dict(t=45, tZ=45, thM=95, VM_ml=100, thK0=80, VK_ml=200, thU=20, QW=0, kA=b["kA"], CT=0),
              dict(t=45, tZ=45, thM=5, VM_ml=100, thK0=80, VK_ml=200, thU=20, QW=5, kA=b["kA"], CT=0),
              dict(t=180, tZ=45, thM=5, VM_ml=100, thK0=80, VK_ml=200, thU=20, QW=14.5, kA=b["kA"], CT=0),
              dict(t=45, tZ=45, thM=5, VM_ml=100, thK0=80, VK_ml=200, thU=20, QW=0, kA=b["kA"], CT=255)]
    o = ode(faelle)
    zeilen += ["", "Weg 2, Differentialgleichung numerisch (Runge-Kutta, 1 s):"]
    namen = ["Blatt (45 min)", "t = 90 min", "Milch 95 °C", "Tassenwärmer 5 W", "Wärmer 14,5 W, t = 180 min", "Tasse 255 J/K"]
    for i, nm in enumerate(namen):
        zeilen.append("  %-27s θ1 %8.4f °C  θ2 %8.4f °C  Δθ %7.4f K  Q1 %7.3f kJ  Q2 %7.3f kJ  Q2−Q1 %6.3f kJ  höchstens %6.2f °C"
                      % (nm, o["th1"][i], o["th2"][i], o["th1"][i] - o["th2"][i], o["Q1"][i] / 1e3, o["Q2"][i] / 1e3,
                         (o["Q2"][i] - o["Q1"][i]) / 1e3, max(o["max1"][i], o["max2"][i])))
    d = max(abs(o["th1"][0] - b["th1"]), abs(o["th2"][0] - b["th2"]), abs(o["Q1"][0] - b["Q1"]) / 1e3, abs(o["Q2"][0] - b["Q2"]) / 1e3)
    zeilen.append("  Weg 1 gegen Weg 2 beim Blatt: größte Abweichung %.2e (K oder kJ)" % d)
    zeilen.append("")
    zeilen.append("Ergebnis: " + ("alle Werte des Blatts bestätigt" if fehler == 0 and d < 1e-6 else "%d Abweichungen" % fehler))
    text = "\n".join(zeilen) + "\n"
    print(text, end="")
    os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ergebnisse"), exist_ok=True)
    open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ergebnisse", "a1_nachrechnung.txt"), "w", encoding="utf-8").write(text)
    return 0 if fehler == 0 and d < 1e-6 else 1


if __name__ == "__main__":
    raise SystemExit(main())
