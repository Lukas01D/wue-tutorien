# -*- coding: utf-8 -*-
"""Eigene Nachrechnung (Claude) der erwarteten Antworten zu den Fragen im Konzept."""
import math
C_K = 200e-6 * 1000 * 4180; C_M = 30e-6 * 1030 * 3940; C_G = C_K + C_M
TU, TK0, TM = 20.0, 80.0, 5.0
kA = -C_K / 600 * math.log(47 / 60)

def gleich(t_min, fD=1.0, C_T=0.0):
    CKT, CGT = C_K + C_T, C_G + C_T
    k = -CKT / 600 * math.log(47 / 60) * fD
    eG, eK = math.exp(-k * t_min * 60 / CGT), math.exp(-k * t_min * 60 / CKT)
    return TU + CKT * (TK0 - TU) * (eG - eK) / (C_M * (1 - eG))

def dT(t_min, fD=1.0, thM=TM):
    k = kA * fD; T10 = (C_K * TK0 + C_M * thM) / C_G
    T1 = TU + (T10 - TU) * math.exp(-k * t_min * 60 / C_G)
    T2K = TU + (TK0 - TU) * math.exp(-k * t_min * 60 / C_K)
    return T1 - (C_K * T2K + C_M * thM) / C_G

for t in (30, 60, 90):
    print(f"Milch gleich warm bei Zugabe nach {t} min: {gleich(t):.2f} °C; mit Deckel: {gleich(t, 0.56):.2f} °C")
print(f"Grenzwert sehr späte Zugabe: dT -> {C_M*(TU-TM)/C_G:.3f} K (20 °C gegen {(C_K*TU+C_M*TM)/C_G:.2f} °C)")
for t in (30, 40, 56, 60, 100, 120, 240):
    print(f"Zugabe {t:3d} min: dT offen {dT(t):.3f} K, mit Deckel {dT(t, 0.56):.3f} K")
# Rundung auf 0,01 K: Bereich der Zugabe mit Anzeige 3,86 K
print("Anzeige 3,86 K (offen) für Minuten:", [t for t in range(1, 121) if round(dT(t), 2) == 3.86])
print("Anzeige 3,86 K (Deckel) für Minuten:", [t for t in range(1, 181) if round(dT(t, 0.56), 2) == 3.86])
