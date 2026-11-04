# -*- coding: utf-8 -*-
"""Gegenprüfung (Claude) ausgewählter Zahlen aus R3: eigene Rechnung, dazu Vergleich mit kaffee_modell.py, wo es eine Funktion gibt.
Aufruf: python3 n5_r3_gegenpruefung.py <Ordner mit kaffee_modell.py>"""
import math, sys
C_K = 200e-6 * 1000 * 4180; C_M = 30e-6 * 1030 * 3940; C_G = C_K + C_M
TU, TK0, TM = 20.0, 80.0, 5.0
LN = math.log(47 / 60)

def tassen(tZ, C_T=0.0, f=1.0, f1=1.0, thM=TM, t_trink=None):
    CKT, CGT = C_K + C_T, C_G + C_T
    kA = -CKT / 600 * LN * f
    T10 = (CKT * TK0 + C_M * thM) / CGT
    T1 = TU + (T10 - TU) * math.exp(-f1 * kA * tZ * 60 / CGT)
    T2K = TU + (TK0 - TU) * math.exp(-kA * tZ * 60 / CKT)
    T2 = (CKT * T2K + C_M * thM) / CGT
    if t_trink is not None:
        d = (t_trink - tZ) * 60
        T1 = TU + (T1 - TU) * math.exp(-f1 * kA * d / CGT); T2 = TU + (T2 - TU) * math.exp(-kA * d / CGT)
    return T1, T2, T1 - T2

print("Becher Pappe 11 J/K:  dT %.2f K, th1 %.2f" % (tassen(60, 11.0)[2], tassen(60, 11.0)[0]))
print("Porzellan 332 J/K:    dT %.2f K, th1 %.2f" % (tassen(60, 0.310 * 1070)[2], tassen(60, 0.310 * 1070)[0]))
print("kA Tasse 1 +5 %%:     th1 %.2f, dT %.2f K" % tassen(60, f1=1.05)[0:3:2])
print("kA Tasse 1 +10 %%:    th1 %.2f, dT %.2f K" % tassen(60, f1=1.10)[0:3:2])
for f in (0.9, 1.1):
    a = tassen(60, f=f); print("kA beider x %.1f: th1 %.2f, dT %.3f K (Standard 3.853)" % (f, a[0], a[2]))
# erwärmte Milch 60 °C: Vorzeichenwechsel und größtes Plus von Tasse 1
best = max(((tassen(t, thM=60.0)[2], t) for t in range(1, 121)))
print("Milch 60 °C: größtes dT %.2f K bei Zugabe nach %d min; nach 60 min %.2f K" % (best[0], best[1], tassen(60, thM=60.0)[2]))
# fester Trinkzeitpunkt 60 min
for tZ in (10, 30, 60):
    print("Trinken nach 60 min, Zugabe nach %d min: dT %.2f K" % (tZ, tassen(tZ, t_trink=60)[2]))
# nicht vorgewärmter Becher
C_B = 255.0
th_aus = (C_K * TK0 + C_B * TU) / (C_K + C_B)
kA_b = -(C_K + C_B) / 600 * LN
th10 = TU + (th_aus - TU) * math.exp(-kA_b * 600 / (C_K + C_B))
kA_falsch = -C_K / 600 * math.log((th10 - TU) / (TK0 - TU))
print("Becher kalt: Ausgleich %.2f °C, nach 10 min %.2f °C, Zwei-Punkte-kA ohne Becher %.4f W/K (x %.2f)" % (th_aus, th10, kA_falsch, kA_falsch / (-C_K / 600 * LN)))
# Modellfunktionen zum Vergleich
sys.path.insert(0, sys.argv[1]); import kaffee_modell as km
print("Modell nichtlinear(1.25): th1 %.2f, th2 %.2f, dT %.2f K" % tuple([x - 273.15 for x in km.nichtlinear(1.25)] + [km.nichtlinear(1.25)[0] - km.nichtlinear(1.25)[1]]))
z = km.zwei_tassen(C_T=0.0, kA1_faktor=1.05); print("Modell zwei_tassen(kA1 1,05): th1 %.2f, dT %.2f" % (z["th1"], z["dT"]))
b = km.becher(0.310, 1070.0); print("Modell becher(310 g, 1070): dT %.2f" % b["dT"])
# Ergänzung: Becher, Energie und Abkühlen nach der Zugabe
C_B = 0.3 * 850
a = tassen(60, C_B); print("Becher: th1 %.4f, th2 %.4f, dT %.4f K, (C_G + C_B) dT = %.4f kJ" % (a[0], a[1], a[2], (C_G + C_B) * a[2] / 1e3))
a = tassen(60, C_B, t_trink=90); print("Becher, Zugabe 60, Vergleich 90: dT %.2f K" % a[2])
for tv in (50, 60):
    a = tassen(40, t_trink=tv); print("ohne Becher, Zugabe 40, Vergleich %d: dT %.2f K" % (tv, a[2]))
    a = tassen(40, C_B, t_trink=tv); print("mit Becher, Zugabe 40, Vergleich %d: th1 %.2f, th2 %.2f, dT %.2f K" % (tv, a[0], a[1], a[2]))
kA = -C_K / 600 * LN
print("Qdot bei 60 min: %.2f W und %.2f W" % (kA * (tassen(60)[0] - TU), kA * (TU + (TK0 - TU) * math.exp(-kA * 3600 / C_K) - TU)))
