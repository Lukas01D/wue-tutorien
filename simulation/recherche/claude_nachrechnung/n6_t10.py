# -*- coding: utf-8 -*-
"""Gegenprüfung (Claude) von R3-Testfall T10 (Ausgleichsgeraden an einer verrauschten Reihe) und der Versuchswerte nach der Zugabe."""
import math
C_K = 200e-6 * 1000 * 4180; TU = 20.0
t = [0, 10, 20, 30, 40, 50, 60]; th = [80.1, 67.3, 56.9, 49.1, 42.7, 37.4, 33.7]
x = [ti * 60 for ti in t[1:]]; y = [math.log((v - TU) / (th[0] - TU)) for v in th[1:]]
b0 = sum(a * c for a, c in zip(x, y)) / sum(a * a for a in x)
s0 = math.sqrt(sum((c - b0 * a) ** 2 for a, c in zip(x, y)) / (len(x) - 1) / sum(a * a for a in x))
X = [ti * 60 for ti in t]; Y = [math.log(v - TU) for v in th]; n = len(X); mx, my = sum(X) / n, sum(Y) / n
Sxx = sum((a - mx) ** 2 for a in X); b1 = sum((a - mx) * (c - my) for a, c in zip(X, Y)) / Sxx; a1 = my - b1 * mx
s1 = math.sqrt(sum((c - a1 - b1 * a) ** 2 for a, c in zip(X, Y)) / (n - 2) / Sxx)
print("zwei Punkte %.4f W/K" % (-C_K / 600 * math.log((th[1] - TU) / (th[0] - TU))))
print("Ursprungsgerade %.4f +- %.4f W/K" % (-C_K * b0, C_K * s0))
print("frei %.4f +- %.4f W/K, Achsenabschnitt minus ln(th0 - thu): %.3f" % (-C_K * b1, C_K * s1, a1 - math.log(th[0] - TU)))
