# -*- coding: utf-8 -*-
"""Eigene Testwerte (Claude): kA aus allen Punkten und gleichwertiger Messwert nach 10 min (M2)."""
import math
C_K = 200e-6 * 1000 * 4180; C_T = 0.3 * 850; TU, TK0 = 20.0, 80.0
def kA_ursprung(ts_min, ths, th0, C, thu=TU):
    xs = [t * 60 for t in ts_min]; ys = [math.log((th - thu) / (th0 - thu)) for th in ths]
    b = sum(x * y for x, y in zip(xs, ys)) / sum(x * x for x in xs)
    n = len(xs); res = [y - b * x for x, y in zip(xs, ys)]
    s_b = math.sqrt(sum(r * r for r in res) / (n - 1) / sum(x * x for x in xs)) if n > 1 else float('nan')
    return -C * b, C * s_b
def aequivalent(kA, C, th0=TK0, thu=TU):
    return thu + (th0 - thu) * math.exp(-kA * 600 / C)
ts = [10, 20, 30, 40]
for C, name in [(C_K, "ohne Becher"), (C_K + C_T, "mit Becher 300 g")]:
    kA0 = -C / 600 * math.log(47 / 60)
    exakt = [TU + (TK0 - TU) * math.exp(-kA0 * t * 60 / C) for t in ts]
    n_ = 1.25; c = ((67 - TU) ** (1 - n_) - (TK0 - TU) ** (1 - n_)) * C / ((n_ - 1) * 600)
    nl = [TU + ((TK0 - TU) ** (1 - n_) + (n_ - 1) * c * t * 60 / C) ** (1 / (1 - n_)) for t in ts]
    for lab, d in [("exakt", exakt), ("n = 1,25", nl)]:
        k, s = kA_ursprung(ts, d, TK0, C)
        print(f"{name}, {lab}: Punkte {[round(v, 2) for v in d]} -> kA {k:.4f} W/K (s {s:.4f}), gleichwertiger Messwert nach 10 min {aequivalent(k, C):.2f} °C")
