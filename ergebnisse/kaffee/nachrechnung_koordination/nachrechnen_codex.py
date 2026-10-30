# -*- coding: utf-8 -*-
"""Nachrechnung der Zahlen aus dem Codex-Bericht (Rolle X)."""
import math
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from kaffee_modell import P, rechne
from nachrechnen_koord import lauf
K = 273.15
r = rechne(P); C_K, C_M, C_G = r["C_K"], r["C_M"], r["C_G"]
print("Codex1: Becher, kA Tasse 1 *1,15 / *1,20:", round(lauf(C_T=255.0, kAfaktor1=1.15)[2], 4), round(lauf(C_T=255.0, kAfaktor1=1.20)[2], 4))
o1, o2 = lauf(C_T=255.0, thmess=66.0), lauf(C_T=255.0, thmess=68.0)
print("Codex2: Becher, Messung 66/68 °C: diff", round(o1[2], 4), round(o2[2], 4), "Endwerte", [round(x, 2) for x in o1[:2]], [round(x, 2) for x in o2[:2]])
kAb = lauf(C_T=255.0)[3]
print("Codex2: Abkühlrate Tasse 1 mit Becher bei 60 min [K/min]:", round(kAb * (34.0436 - 20) / (C_G + 255) * 60, 3))
print("Codex2: 15 ml Milch mit Becher: diff", round(lauf(C_T=255.0, m_M=15e-6 * 1030)[2], 4))
th1_60 = lauf(thM1=60.0)[0]
T2K = r["T2_K"] - K
f = lambda thM2: (C_K * T2K + C_M * thM2) / C_G - th1_60
print("Codex3: späte Portion mindestens [°C]:", round(brentq(f, 0, 100), 4), "; späte Portion 20 °C: th2", round((C_K * T2K + C_M * 20) / C_G, 4))
th1_5 = lauf()[0]
g = lambda thM2: (C_K * T2K + C_M * thM2) / C_G - th1_5
print("Codex4: nur späte Portion, Gleichstand bei [°C]:", round(brentq(g, 0, 100), 4))
print("Codex5: C_B/C_K =", round(255 / C_K * 100, 2), "%")
# Codex6: Exponent 1,6 exakt (adaptiver Integrator), an dieselbe Messung angepasst
n = 1.6
def ende(c, T0, C, t):
    s = solve_ivp(lambda t, y: [-c * max(y[0] - 20.0, 0) ** n / C], (0, t), [T0], rtol=1e-11, atol=1e-11)
    return s.y[0, -1]
c = brentq(lambda c: ende(c, 80.0, C_K, 600.0) - 67.0, 1e-5, 1.0)
th10 = (C_K * 80 + C_M * 5) / C_G
print("Codex6: n = 1,6 exakt: th1 =", round(ende(c, th10, C_G, 3600.0), 5))
