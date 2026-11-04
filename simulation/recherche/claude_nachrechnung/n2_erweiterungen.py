# -*- coding: utf-8 -*-
"""Eigene Testwerte (Claude) für die vorgeschlagenen Erweiterungen, unabhängig von kaffee_modell.py.
Standardwerte der Aufgabe; Temperaturen in °C (nur Differenzen und Mischungen)."""
import math, random

C_K = 200e-6 * 1000 * 4180; C_M = 30e-6 * 1030 * 3940; C_G = C_K + C_M
TU, TK0, TM, TH10 = 20.0, 80.0, 5.0, 67.0
LN = math.log((TH10 - TU) / (TK0 - TU))

def lauf(tZ_min=60.0, C_T=0.0, fD=1.0, thM1=TM, thM2=TM, f1=1.0, t_ende_min=None):
    """Tasse 1 und 2 bis zur Zugabe tZ, optional danach weiter bis t_ende (beide Tassen als Gemisch)."""
    CKT, CGT = C_K + C_T, C_G + C_T
    kA = -CKT / 600.0 * LN * fD
    tZ = tZ_min * 60
    T10 = (CKT * TK0 + C_M * thM1) / CGT
    T1 = TU + (T10 - TU) * math.exp(-f1 * kA * tZ / CGT)
    T2K = TU + (TK0 - TU) * math.exp(-kA * tZ / CKT)
    T2 = (CKT * T2K + C_M * thM2) / CGT
    Q1, Q2 = CGT * (T10 - T1), CKT * (TK0 - T2K)
    r = dict(kA=kA, T10=T10, T1=T1, T2K=T2K, T2=T2, dT=T1 - T2, Q1=Q1 / 1e3, Q2=Q2 / 1e3)
    if t_ende_min is not None:
        dt = (t_ende_min - tZ_min) * 60
        r["T1_ende"] = TU + (T1 - TU) * math.exp(-f1 * kA * dt / CGT)
        r["T2_ende"] = TU + (T2 - TU) * math.exp(-kA * dt / CGT)
        r["dT_ende"] = r["T1_ende"] - r["T2_ende"]
    return r

def zeige(titel, r):
    print(titel + ": " + ", ".join(f"{k} {v:.4f}" if k == "kA" else f"{k} {v:.2f}" for k, v in r.items()))

zeige("Standard", lauf())
zeige("Becher 300 g", lauf(C_T=0.3 * 850))
zeige("Deckel (kA x 0,56)", lauf(fD=0.56))
zeige("Deckel und Becher", lauf(C_T=0.3 * 850, fD=0.56))
zeige("Versuch 40 min mit Becher", lauf(tZ_min=40, C_T=0.3 * 850))
zeige("Weiter bis 90 min nach Zugabe bei 60", lauf(t_ende_min=90))
zeige("Weiter bis 120 min nach Zugabe bei 60", lauf(t_ende_min=120))
r = lauf(); print(f"Energie: Q2 - Q1 = {r['Q2']-r['Q1']:.3f} kJ, C_G * dT = {C_G*r['dT']/1e3:.3f} kJ")
# Wärmestrom am Anfang und Fläche unter Qdot(t) numerisch = Q
kA = r["kA"]; n = 36000; h = 3600 / n
f1 = lambda t: kA * ((r["T10"] - TU) * math.exp(-kA * t / C_G))
f2 = lambda t: kA * ((TK0 - TU) * math.exp(-kA * t / C_K))
A1 = sum((f1(i * h) + f1((i + 1) * h)) / 2 * h for i in range(n)) / 1e3
A2 = sum((f2(i * h) + f2((i + 1) * h)) / 2 * h for i in range(n)) / 1e3
print(f"Wärmestrom am Anfang: Tasse 1 {f1(0):.2f} W, Tasse 2 {f2(0):.2f} W; Fläche bis 60 min: {A1:.3f} und {A2:.3f} kJ")

# kA aus allen Punkten: Ausgleichsgerade durch den Ursprung und mit freiem Achsenabschnitt
def ausgleich(ts_min, ths, th0, thu=TU, C=C_K):
    xs = [t * 60 for t in ts_min]; ys = [math.log((th - thu) / (th0 - thu)) for th in ths]
    b0 = sum(x * y for x, y in zip(xs, ys)) / sum(x * x for x in xs)
    n = len(xs); mx, my = sum(xs) / n, sum(ys) / n
    b1 = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs); a1 = my - b1 * mx
    return -C * b0, -C * b1, a1

ts = [10, 20, 30, 40, 50, 60]
exakt = [TU + (TK0 - TU) * math.exp(-0.340196 * t * 60 / C_K) for t in ts]
print("Synthetisch exakt:", [f"{v:.2f}" for v in exakt])
k0, k1, a = ausgleich(ts, exakt, TK0); print(f"  kA Ursprung {k0:.4f}, frei {k1:.4f} (Achsenabschnitt {a:.4f})")
# nichtlinear n = 1,25, gleiche Messung nach 10 min getroffen
n_ = 1.25
c = ((TH10 - TU) ** (1 - n_) - (TK0 - TU) ** (1 - n_)) * C_K / ((n_ - 1) * 600)
nl = [TU + ((TK0 - TU) ** (1 - n_) + (n_ - 1) * c * t * 60 / C_K) ** (1 / (1 - n_)) for t in ts]
print("Synthetisch n = 1,25:", [f"{v:.2f}" for v in nl])
k0, k1, a = ausgleich(ts, nl, TK0); print(f"  kA Ursprung {k0:.4f}, frei {k1:.4f} (Achsenabschnitt {a:.4f}); zwei Punkte (10 min) {-C_K/600*LN:.4f}")
