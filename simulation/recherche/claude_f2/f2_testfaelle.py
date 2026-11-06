# -*- coding: utf-8 -*-
"""Testfälle (Claude) für Fassung 2 des Konzepts: kA direkt mit Voreinstellungen, Vertiefungsregler, Kann-Ideen.
Eigene Rechnung aus den Gleichungen der Aufgabe; Gegenprobe mit kaffee_modell.py über den gleichwertigen Messwert.
Aufruf: python3 f2_testfaelle.py <Ordner mit kaffee_modell.py>"""
import math, sys

def rechne(VK=200, VM=30, thK0=80.0, thM1=5.0, thM2=None, thU=20.0, tZ=60.0, kA=None, th10=67.0, C_B=0.0, kalt=False, f1=1.0):
    """kA=None: kA aus der Messung nach 10 min (Teil c/g); sonst kA direkt (W/K).
    kalt=True: Becher hat beim Eingießen Raumtemperatur und gleicht sich sofort mit dem Inhalt aus."""
    thM2 = thM1 if thM2 is None else thM2
    C_K = VK * 1e-6 * 1000 * 4180; C_M = VM * 1e-6 * 1030 * 3940
    CKB, CGB = C_K + C_B, C_K + C_M + C_B
    if kA is None:
        kA = -CKB / 600 * math.log((th10 - thU) / (thK0 - thU))
    thB0 = thU if kalt else thK0                      # Bechertemperatur beim Eingießen
    th10_1 = (C_K * thK0 + C_M * thM1 + C_B * thB0) / CGB   # Tasse 1 nach dem Mischen bei t = 0
    thK_start = (C_K * thK0 + C_B * thB0) / CKB              # Tasse 2 (schwarz) nach dem Ausgleich bei t = 0
    t = tZ * 60
    th1 = thU + (th10_1 - thU) * math.exp(-f1 * kA * t / CGB)
    thK = thU + (thK_start - thU) * math.exp(-kA * t / CKB)
    th2 = (CKB * thK + C_M * thM2) / CGB
    Q1 = CGB * (th10_1 - th1); Q2 = CKB * (thK_start - thK)
    # größter Unterschied über der Zugabe (gleiches kA)
    q = (thK_start - thU) / (th10_1 - thU)
    a2, a1 = kA / CKB, f1 * kA / CGB
    tS = math.log(q) / (a2 - a1) if q > 0 and a2 != a1 else float('nan')
    return dict(kA=kA, C_K=C_K, C_M=C_M, CKB=CKB, CGB=CGB, th10_1=th10_1, thK_start=thK_start, th1=th1, thK=thK, th2=th2, dT=th1 - th2,
                Q1=Q1 / 1e3, Q2=Q2 / 1e3, tS=tS / 60,
                th30=thU + (thK_start - thU) * math.exp(-kA * 1800 / CKB), tau=CKB / kA / 60,
                aeq=thU + (thK0 - thU) * math.exp(-kA * 600 / CKB))

def dmax(**kw):
    best = (-1e9, 0)
    for i in range(1, 1500 * 6):
        t = i / 6
        d = rechne(tZ=t, **kw)["dT"]
        if d > best[0]: best = (d, t)
    return best

K0 = rechne()["kA"]
print("Arbeitswert Keramik offen kA = %.4f W/K (Aufgabe, Teil c)" % K0)
VOR = [("Keramik offen", 1.00, "Arbeitswert der Aufgabe (tau 41 min, Ferreira 2025a)"),
       ("Keramik mit Deckel", 0.56, "Ferreira 2025a, Abb. 6 (gemessen)"),
       ("Glas offen", 1.00, "Schätzung: Emissivität wie Keramik (Ferreira 2025b, R3)"),
       ("Pappbecher offen", 1.00, "Schätzung: Emissivität etwa 0,93, Wand kein großer Widerstand (R3)"),
       ("Edelstahl einwandig offen", 0.90, "Schätzung 0,85 bis 1 über die Emissivität (Ferreira 2025b: Aluminium h 13,7 gegen Keramik 16,8 W/(m2 K))"),
       ("Thermobecher offen", 0.44, "Schätzung: nur die offene Oberseite gibt ab (Deckelversuch Ferreira 2025a umgekehrt gelesen)")]
print("\n== T1 Voreinstellungen, kA direkt, ohne Becher, Standardwerte (Zugabe 60 min)")
print("%-26s %6s %8s %7s %9s %7s %7s %6s %7s %7s %8s %8s" % ("Becher", "Faktor", "kA W/K", "tau min", "80->30min", "th1", "th2", "dT", "Q1 kJ", "Q2 kJ", "dTmax", "bei min"))
for n, f, q in VOR:
    r = rechne(kA=f * K0); m = dmax(kA=f * K0)
    print("%-26s %6.2f %8.4f %7.1f %9.2f %7.2f %7.2f %6.2f %7.2f %7.2f %8.3f %8.1f" % (n, f, r["kA"], r["tau"], r["th30"], r["th1"], r["th2"], r["dT"], r["Q1"], r["Q2"], m[0], m[1]))
print("\n== T2 kA direkt mit Becher (C_B 255 J/K): kA bleibt, Inhalt kühlt langsamer")
for n, f in [("Keramik offen", 1.0), ("Keramik mit Deckel", 0.56)]:
    r = rechne(kA=f * K0, C_B=255.0)
    print("%-20s kA %.4f, 80->%.2f °C in 30 min, th1 %.2f, th2 %.2f, dT %.2f K, Q1 %.2f, Q2 %.2f kJ" % (n, r["kA"], r["th30"], r["th1"], r["th2"], r["dT"], r["Q1"], r["Q2"]))
r = rechne(C_B=255.0); print("Vergleich Messung mit Becher (Teil g): kA %.4f, th1 %.2f, th2 %.2f, dT %.2f" % (r["kA"], r["th1"], r["th2"], r["dT"]))

print("\n== T3 gleichwertiger Messwert (kA direkt -> Messung nach 10 min) und Gegenprobe mit kaffee_modell.py")
sys.path.insert(0, sys.argv[1]); import kaffee_modell as km
for kAd, CB in [(0.3402, 0.0), (0.1905, 0.0), (0.1905, 255.0), (0.25, 0.0)]:
    r = rechne(kA=kAd, C_B=CB)
    p = dict(km.P); p["th_mess"] = r["aeq"]
    z = km.zwei_tassen(p, C_T=CB)
    print("kA %.4f, C_B %5.1f: gleichwertig %.4f °C -> Modell kA %.6f, th1 %.4f/%.4f, th2 %.4f/%.4f" % (kAd, CB, r["aeq"], z["kA"], r["th1"], z["th1"], r["th2"], z["th2"]))

print("\n== T4 Vertiefungsregler")
fall = dict(VK=300, VM=50, thK0=90.0, thM1=10.0, thU=25.0, kA=0.25)
r = rechne(**fall); m = dmax(**fall)
print("300 ml, 50 ml, 90 °C, Milch 10 °C, Raum 25 °C, kA 0,25: th10_1 %.2f, th1 %.2f, th2 %.2f, dT %.2f, Q1 %.2f, Q2 %.2f, Schnitt %.1f min, dTmax %.3f bei %.1f min" % (r["th10_1"], r["th1"], r["th2"], r["dT"], r["Q1"], r["Q2"], r["tS"], m[0], m[1]))
fall = dict(VK=300, VM=50, thK0=90.0, thM1=10.0, thU=25.0)
r = rechne(**fall); print("dieselben Größen, kA aus Messung 67 °C nach 10 min: kA %.4f, th1 %.2f, th2 %.2f, dT %.2f" % (r["kA"], r["th1"], r["th2"], r["dT"]))
for lab, kw in [("Milch 60 °C", dict(thM1=60.0)), ("Milch = Raum 20 °C", dict(thM1=20.0)), ("Milch 100 ml", dict(VM=100)), ("Milch 5 ml", dict(VM=5)),
                ("Kaffee 100 ml", dict(VK=100)), ("Kaffee 400 ml", dict(VK=400)), ("Raum 30 °C", dict(thU=30.0)), ("Kaffee 95 °C", dict(thK0=95.0)),
                ("kA direkt 0,05", dict(kA=0.05)), ("kA direkt 1,0", dict(kA=1.0))]:
    r = rechne(**kw); print("  %-20s kA %.4f th1 %.2f th2 %.2f dT %+.2f K" % (lab, r["kA"], r["th1"], r["th2"], r["dT"]))

print("\n== T5 Versuch bis 60 min (Messung mit Übernahme aus 0 und 10 min): schwarzer Kaffee unabhängig vom Becher")
for CB in (0.0, 255.0):
    r0 = rechne(C_B=CB)
    print("C_B %5.1f:" % CB, ", ".join("%d min %.2f" % (t, 20 + 60 * math.exp(-r0["kA"] * t * 60 / r0["CKB"])) for t in (10, 20, 30, 40, 50, 60)),
          "| Tasse 1:", ", ".join("%d min %.2f" % (t, 20 + (r0["th10_1"] - 20) * math.exp(-r0["kA"] * t * 60 / r0["CGB"])) for t in (0, 30, 60)))

print("\n== T6 Kann: Trinkzeit bis 60 °C")
for lab, kw in [("Standard", {}), ("Keramik mit Deckel", dict(kA=0.56 * K0)), ("mit Becher (Teil g)", dict(C_B=255.0))]:
    r = rechne(**kw)
    t1 = r["CGB"] / r["kA"] * math.log((r["th10_1"] - 20) / 40) / 60
    tk = r["CKB"] / r["kA"] * math.log((r["thK_start"] - 20) / 40) / 60
    print("  %-20s Tasse 1 erreicht 60 °C nach %.2f min, schwarzer Kaffee nach %.2f min" % (lab, t1, tk))

print("\n== T7 Kann: Becher kalt (20 °C) statt vorgewärmt, kA direkt 0,4440 W/K, C_B 255 J/K")
for kalt in (False, True):
    r = rechne(kA=0.444031, C_B=255.0, kalt=kalt)
    print("  kalt=%s: Start Tasse 1 %.2f °C, schwarz %.2f °C; nach 60 min th1 %.2f, th2 %.2f, dT %.2f K" % (kalt, r["th10_1"], r["thK_start"], r["th1"], r["th2"], r["dT"]))

print("\n== T8 Kann: CSV (Standard), erste Zeilen")
r = rechne()
print("t_min;Tasse_1_degC;Tasse_2_degC")
for t in (0, 1, 2, 10):
    print("%d;%s;%s" % (t, ("%.2f" % (20 + (r["th10_1"] - 20) * math.exp(-r["kA"] * t * 60 / r["CGB"]))).replace(".", ","), ("%.2f" % (20 + 60 * math.exp(-r["kA"] * t * 60 / r["CKB"]))).replace(".", ",")))

print("\n== T9 Vertiefungsregler mit festgehaltenem kA (0,3402 W/K) statt kA aus derselben Messung")
for lab, kw in [("Kaffee 95 °C", dict(thK0=95.0)), ("Kaffee 60 °C", dict(thK0=60.0)), ("Kaffee 100 ml", dict(VK=100)), ("Kaffee 400 ml", dict(VK=400)),
                ("Raum 30 °C", dict(thU=30.0)), ("Raum 10 °C", dict(thU=10.0)), ("Milch 100 ml", dict(VM=100))]:
    a = rechne(**kw); b = rechne(kA=K0, **kw)
    print("  %-14s aus Messung: kA %.4f th1 %.2f th2 %.2f dT %+.2f | festgehalten: kA %.4f th1 %.2f th2 %.2f dT %+.2f K, 80->%.2f in 30 min" % (
        lab, a["kA"], a["th1"], a["th2"], a["dT"], b["kA"], b["th1"], b["th2"], b["dT"], b["th30"]))
