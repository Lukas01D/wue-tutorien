# -*- coding: utf-8 -*-
"""Nachrechnung (Claude) der Zahlen aus dem Prüfbericht X4 (Codex), eigene Rechnung ohne kaffee_modell.py und ohne x4_skripte."""
import math, random
C_K = 200e-6 * 1000 * 4180; C_M = 30e-6 * 1030 * 3940; C_G = C_K + C_M
TU, TK0 = 20.0, 80.0
kA = -C_K / 600 * math.log(47 / 60)

def lauf(tZ, f1=1.0, thM1=5.0, thM2=5.0, C_B=0.0, fD=1.0):
    CKT, CGT = C_K + C_B, C_G + C_B
    k = -CKT / 600 * math.log(47 / 60) * fD
    T10 = (CKT * TK0 + C_M * thM1) / CGT
    T1 = TU + (T10 - TU) * math.exp(-f1 * k * tZ * 60 / CGT)
    T2K = TU + (TK0 - TU) * math.exp(-k * tZ * 60 / CKT)
    T2 = (CKT * T2K + C_M * thM2) / CGT
    Q1, Q2 = CGT * (T10 - T1), CKT * (TK0 - T2K)
    return dict(k=k, T10=T10, T1=T1, T2K=T2K, T2=T2, dT=T1 - T2, Q1=Q1, Q2=Q2, CGT=CGT)

print("== Konzept 2: Milch für Tasse 2 bei Raumtemperatur")
r = lauf(60, thM2=20.0)
print("th2 %.5f, dT %.5f K; (Q2-Q1)/C_G = %.5f K; (Q2-Q1 + C_M (thM1-thM2))/C_G = %.5f K" % (r["T2"], r["dT"], (r["Q2"] - r["Q1"]) / C_G, (r["Q2"] - r["Q1"] + C_M * (5 - 20)) / C_G))

print("== Konzept 3: ungleiches kA (f1 = 1,05)")
r = lauf(60, f1=1.05); d = 1800
T1_90 = TU + (r["T1"] - TU) * math.exp(-1.05 * kA * d / C_G); T2_90 = TU + (r["T2"] - TU) * math.exp(-kA * d / C_G)
print("dT(60) %.5f K, dT(90) richtig %.5f K, mit gemeinsamem Abklingfaktor %.5f K" % (r["dT"], T1_90 - T2_90, r["dT"] * math.exp(-kA * d / C_G)))
# Extremum über t_Z bei f1 = 1,05: gleiche Wärmeströme statt gleicher Temperaturen?
best = max((lauf(t / 60.0, f1=1.05)["dT"], t / 60.0) for t in range(60, 150 * 60))
r = lauf(best[1], f1=1.05)
print("Maximum %.4f K bei %.2f min: Tasse 1 %.3f °C, schwarz %.3f °C; Wärmeströme %.4f und %.4f W" % (best[0], best[1], r["T1"], r["T2K"], 1.05 * kA * (r["T1"] - TU), kA * (r["T2K"] - TU)))
# spätere Reihenfolge?
for tv in (120, 240, 480):
    a = TU + (lauf(60, f1=1.05)["T1"] - TU) * math.exp(-1.05 * kA * (tv - 60) * 60 / C_G); b = TU + (lauf(60, f1=1.05)["T2"] - TU) * math.exp(-kA * (tv - 60) * 60 / C_G)
    print("  Vergleich nach %d min: dT %.4f K" % (tv, a - b))

print("== Konzept 1: Vorzeichen von Qdot2 - Qdot1 und Teilflächen")
for tZ in (30, 60, 120):
    r = lauf(tZ); n = int(tZ * 60); pos = neg = 0.0
    for i in range(n):
        t = i + 0.5
        q1 = kA * (r["T10"] - TU) * math.exp(-kA * t / C_G); q2 = kA * (TK0 - TU) * math.exp(-kA * t / C_K)
        dq = q2 - q1
        if dq > 0: pos += dq
        else: neg += dq
    print("Zugabe %3d min: Fläche positiv %.4f kJ, negativ %.4f kJ, Summe %.4f kJ, Q2-Q1 %.4f kJ" % (tZ, pos / 1e3, neg / 1e3, (pos + neg) / 1e3, (r["Q2"] - r["Q1"]) / 1e3))

print("== Konzept 4: formaler Standardfehler der Ursprungsgeraden gegen tatsächliche Streuung")
random.seed(4)
ts = [10, 20, 30, 40, 50, 60]
wahr = [TK0] + [TU + (TK0 - TU) * math.exp(-kA * t * 60 / C_K) for t in ts]
ks, ses = [], []
for _ in range(10000):
    m = [v + random.uniform(-0.3, 0.3) for v in wahr]
    x = [t * 60 for t in ts]; y = [math.log((v - TU) / (m[0] - TU)) for v in m[1:]]
    sxx = sum(a * a for a in x); b = sum(a * c for a, c in zip(x, y)) / sxx
    s = math.sqrt(sum((c - b * a) ** 2 for a, c in zip(x, y)) / (len(x) - 1))
    ks.append(-C_K * b); ses.append(C_K * s / math.sqrt(sxx))
mk = sum(ks) / len(ks); sd = math.sqrt(sum((k - mk) ** 2 for k in ks) / (len(ks) - 1))
print("Mittel kA %.5f W/K, tatsächliche Streuung %.5f W/K, mittlerer formaler Standardfehler %.5f W/K" % (mk, sd, sum(ses) / len(ses)))

print("== Kontrolle der Tabelle in X4")
for lab, r in [("Standard", lauf(60)), ("Keramik 60", lauf(60, C_B=255)), ("Keramik 40", lauf(40, C_B=255)), ("Deckel", lauf(60, fD=0.56)), ("Deckel Keramik", lauf(60, C_B=255, fD=0.56))]:
    print("%-15s th1 %.5f th2 %.5f dT %.5f kA %.6f" % (lab, r["T1"], r["T2"], r["dT"], r["k"]))
