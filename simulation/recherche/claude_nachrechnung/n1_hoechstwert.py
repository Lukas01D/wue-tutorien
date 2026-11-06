# -*- coding: utf-8 -*-
"""Eigene Nachrechnung (Claude, Konzept Phase 1), unabhängig von kaffee_modell.py.
Höchstwert des Unterschieds der Tassen über dem Zeitpunkt der Zugabe, abhängig von kA (Deckel, Dämmung) und Becher."""
import math

K = 273.15
C_K = 200e-6 * 1000 * 4180          # J/K
C_M = 30e-6 * 1030 * 3940
TU, TK0, TM = 20.0, 80.0, 5.0       # °C genügt, da nur Differenzen und Mischungen

def kA_aus_messung(C_KT, th10=67.0, t=600.0):
    return -C_KT / t * math.log((th10 - TU) / (TK0 - TU))

def tassen(t, kA, C_T=0.0, f1=1.0):
    CKT, CGT = C_K + C_T, C_K + C_M + C_T
    T10 = (CKT * TK0 + C_M * TM) / CGT
    T1 = TU + (T10 - TU) * math.exp(-f1 * kA * t / CGT)
    T2K = TU + (TK0 - TU) * math.exp(-kA * t / CKT)
    T2 = (CKT * T2K + C_M * TM) / CGT
    return T1, T2, T2K

def maximum(kA, C_T=0.0):
    best = (-1, None)
    for i in range(1, 300 * 60 + 1):        # Sekundenraster bis 300 min
        t = float(i)
        T1, T2, T2K = tassen(t, kA, C_T)
        if T1 - T2 > best[0]:
            best = (T1 - T2, t, T2K)
    return best

print("Analytisch: Maximum genau am Schnitt (T1 = T2K), Höhe C_M (T_x - T_M) / C_G, T_x unabhängig von kA")
for C_T, name in [(0.0, "ohne Becher"), (0.3 * 850, "Becher 300 g")]:
    CKT, CGT = C_K + C_T, C_K + C_M + C_T
    kA0 = kA_aus_messung(CKT)
    T10 = (CKT * TK0 + C_M * TM) / CGT
    q = (TK0 - TU) / (T10 - TU)
    Tx = TU + (TK0 - TU) * q ** (-CGT / C_M)
    dTmax = C_M * (Tx - TM) / CGT
    print(f"{name}: kA aus Messung {kA0:.4f} W/K, T10 {T10:.2f} °C, T_x {Tx:.2f} °C, dT_max analytisch {dTmax:.3f} K")
    for f, lab in [(1.0, "kA wie gemessen"), (0.56, "Deckel: kA x 0,56"), (0.5, "kA halb"), (2.0, "kA doppelt")]:
        d, t, T2K = maximum(kA0 * f, C_T)
        print(f"   {lab:20s}: dT_max {d:.3f} K bei Zugabe nach {t/60:.1f} min, schwarzer Kaffee dann {T2K:.2f} °C")
# Standardwerte zur Kontrolle
kA0 = kA_aus_messung(C_K)
T1, T2, _ = tassen(3600, kA0)
print(f"Kontrolle Standard: kA {kA0:.4f} W/K, th1 {T1:.2f} °C, th2 {T2:.2f} °C, dT {T1-T2:.2f} K")
