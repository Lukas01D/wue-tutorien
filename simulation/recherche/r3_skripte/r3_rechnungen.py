# -*- coding: utf-8 -*-
"""R3 Fach und Modell: Nachrechnungen zu den Erweiterungen des Kaffee-Modells (Tutorium 5).

Aufruf (aus dem Repository):
    python3 simulation/recherche/r3_skripte/r3_rechnungen.py > simulation/recherche/r3_skripte/r3_rechnungen_ausgabe.txt

Alle Rechnungen mit eigenen Gleichungen (Temperaturen in °C, Differenzen in K, Zeiten in s).
Wo kaffee_modell.py eine Funktion hat, wird verglichen. Das Modell wird aus dem Zweig der
Kaffee-Prüfung gelesen (git show); fehlt der Zweig, entfallen nur die Vergleiche.
Abschnitte: 0 Grundwerte, 1 Deckel, 2 Bechermaterial, 3 Verdunstung, 4 nichtlinear,
5 Ausgleichsrechnung, 6 Energie, 7 größter Unterschied, 8 Abkühlen nach dem Zugießen, 9 Sonstiges.
Nur Standardbibliothek und numpy.
"""
import math
import os
import subprocess
import types

import numpy as np

HIER = os.path.dirname(os.path.abspath(__file__))
REF = "origin/claude/kaffee-pruefung-sgvo1r"
PFAD = "pruefung/Kaffee_Pruefpaket_2026-10-23/umsetzung/Arbeitsordner/kaffee/kaffee_modell.py"


def lade_modell():
    try:
        src = subprocess.run(["git", "-C", HIER, "show", f"{REF}:{PFAD}"],
                             capture_output=True, text=True, check=True).stdout
    except Exception:
        return None
    mod = types.ModuleType("kaffee_modell")
    exec(compile(src, "kaffee_modell.py", "exec"), mod.__dict__)
    return mod


M = lade_modell()
K0 = 273.15


def kopf(text):
    print()
    print("=" * 78)
    print(text)
    print("=" * 78)


def z(name, wert, einheit="", fmt="{:.4f}"):
    print(f"  {name:<58s} {fmt.format(wert):>12s} {einheit}")


# ---------------------------------------------------------------------------
# Arbeitswerte der Aufgabe (unabhängig eingetragen, nicht aus dem Modell übernommen)
# ---------------------------------------------------------------------------
V_K, RHO_K, CP_K = 200e-6, 1000.0, 4180.0
V_M, RHO_M, CP_M = 30e-6, 1030.0, 3940.0
TH_K0, TH_M, TH_U = 80.0, 5.0, 20.0
T_MESS, TH_MESS = 600.0, 67.0
T_END = 3600.0
M_B, C_B = 0.300, 850.0

M_K = RHO_K * V_K
M_M = RHO_M * V_M
C_K = M_K * CP_K
C_M = M_M * CP_M
C_G = C_K + C_M


def kA_aus_messung(C_T=0.0, th0=TH_K0, thm=TH_MESS, tm=T_MESS, thu=TH_U):
    """kA aus zwei Punkten (Teil c), Becher mit C_T eingeschlossen."""
    return -(C_K + C_T) / tm * math.log((thm - thu) / (th0 - thu))


def zwei(kA1, kA2=None, C_T=0.0, thM1=TH_M, thM2=None, t=T_END, th0=TH_K0, thu=TH_U):
    """Beide Tassen linear, eigene Rechnung. Tasse 1: Milch bei t = 0; Tasse 2: Milch bei t."""
    kA2 = kA1 if kA2 is None else kA2
    thM2 = thM1 if thM2 is None else thM2
    CKT, CGT = C_K + C_T, C_G + C_T
    th10 = (CKT * th0 + C_M * thM1) / CGT
    th1 = thu + (th10 - thu) * math.exp(-kA1 * t / CGT)
    thK = thu + (th0 - thu) * math.exp(-kA2 * t / CKT)
    th2 = (CKT * thK + C_M * thM2) / CGT
    Q1 = CGT * (th10 - th1)
    Q2 = CKT * (th0 - thK)
    return dict(th10=th10, th1=th1, thK=thK, th2=th2, d=th1 - th2, Q1=Q1, Q2=Q2)


def maximum_analytisch(kA, C_T=0.0, thM=TH_M, th0=TH_K0, thu=TH_U):
    """Größter Unterschied über den Zeitpunkt der Zugabe (Vergleich direkt nach dem Zugießen).
    dDelta/dt_z = 0  <=>  Kaffee schwarz so warm wie Tasse 1 (Schnittpunkt).
    theta_K* = theta_K0 (theta_10/theta_K0)^(C_GT/C_M),  Delta_max = C_M (th_K* - th_M) / C_GT."""
    CKT, CGT = C_K + C_T, C_G + C_T
    thK0e = th0 - thu
    th10e = (CKT * thK0e + C_M * (thM - thu)) / CGT
    thKs_e = thK0e * (th10e / thK0e) ** (CGT / C_M)
    ts = math.log(thK0e / th10e) / (kA * (1.0 / CKT - 1.0 / CGT))
    dmax = C_M * (thKs_e + thu - thM) / CGT
    return dict(t_stern=ts, thK_stern=thKs_e + thu, dmax=dmax)


def rk4(f, y0, t0, t1, dt):
    """Klassisches Runge-Kutta-Verfahren 4. Ordnung für Listen-Zustände."""
    y = list(y0)
    t = t0
    n = max(1, int(round((t1 - t0) / dt)))
    h = (t1 - t0) / n
    for _ in range(n):
        k1 = f(t, y)
        k2 = f(t + h / 2, [a + h / 2 * b for a, b in zip(y, k1)])
        k3 = f(t + h / 2, [a + h / 2 * b for a, b in zip(y, k2)])
        k4 = f(t + h, [a + h * b for a, b in zip(y, k3)])
        y = [a + h / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(y, k1, k2, k3, k4)]
        t += h
    return y


def bisektion(f, lo, hi, n=80):
    flo = f(lo)
    for _ in range(n):
        mid = 0.5 * (lo + hi)
        fm = f(mid)
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return 0.5 * (lo + hi)


kA0 = kA_aus_messung()
C_T0 = M_B * C_B
kAB = kA_aus_messung(C_T0)
testfaelle = []


def test(name, eingabe, ausgabe):
    testfaelle.append((name, eingabe, ausgabe))


# ===========================================================================
kopf("0  Grundwerte (eigene Rechnung) und Vergleich mit kaffee_modell.py")
r0 = zwei(kA0)
z("m_K c_p,K", C_K, "J/K", "{:.2f}")
z("m_M c_p,M", C_M, "J/K", "{:.3f}")
z("C_G = Summe", C_G, "J/K", "{:.3f}")
z("kA aus Messung (ohne Becher)", kA0, "W/K", "{:.5f}")
z("tau_K = m_K c_p,K / kA", C_K / kA0 / 60, "min", "{:.2f}")
z("tau_G = C_G / kA", C_G / kA0 / 60, "min", "{:.2f}")
z("theta_1,0", r0["th10"], "°C", "{:.3f}")
z("theta_1 (60 min)", r0["th1"], "°C", "{:.3f}")
z("theta_2 (60 min, direkt nach dem Zugießen)", r0["th2"], "°C", "{:.3f}")
z("Unterschied theta_1 - theta_2", r0["d"], "K", "{:.3f}")
z("Q_1", r0["Q1"] / 1000, "kJ", "{:.3f}")
z("Q_2", r0["Q2"] / 1000, "kJ", "{:.3f}")
rB = zwei(kAB, C_T=C_T0)
z("Becher: C_B = m_B c_B", C_T0, "J/K", "{:.1f}")
z("Becher: kA aus derselben Messung", kAB, "W/K", "{:.5f}")
z("Becher: theta_1", rB["th1"], "°C", "{:.3f}")
z("Becher: theta_2", rB["th2"], "°C", "{:.3f}")
z("Becher: Unterschied", rB["d"], "K", "{:.3f}")
z("Becher: Q_1 (Inhalt und Becher)", rB["Q1"] / 1000, "kJ", "{:.3f}")
z("Becher: Q_2 (Inhalt und Becher)", rB["Q2"] / 1000, "kJ", "{:.3f}")
if M is not None:
    r = M.rechne()
    b = M.becher()
    print("  Vergleich mit kaffee_modell.py (Abweichung eigene Rechnung minus Modell):")
    z("kA", kA0 - r["kA"], "W/K", "{:.2e}")
    z("theta_1", r0["th1"] - (r["T1"] - K0), "K", "{:.2e}")
    z("theta_2", r0["th2"] - (r["T2"] - K0), "K", "{:.2e}")
    z("Q_1", r0["Q1"] - r["Q1"], "J", "{:.2e}")
    z("Q_2", r0["Q2"] - r["Q2"], "J", "{:.2e}")
    z("Becher theta_1", rB["th1"] - (b["T1"] - K0), "K", "{:.2e}")
    z("Becher theta_2", rB["th2"] - (b["T2"] - K0), "K", "{:.2e}")
else:
    print("  kaffee_modell.py nicht gefunden: Vergleich entfällt.")
test("Grundfall", "Standardwerte, 60 min", f"theta_1 = {r0['th1']:.2f} °C, theta_2 = {r0['th2']:.2f} °C, "
     f"Delta = {r0['d']:.2f} K, Q_1 = {r0['Q1']/1000:.2f} kJ, Q_2 = {r0['Q2']/1000:.2f} kJ")
test("Becher (Teil g)", "m_B 300 g, c_B 850 J/(kg K), kA neu aus Messung",
     f"kA = {kAB:.4f} W/K, theta_1 = {rB['th1']:.2f} °C, theta_2 = {rB['th2']:.2f} °C, "
     f"Q_1 = {rB['Q1']/1000:.2f} kJ, Q_2 = {rB['Q2']/1000:.2f} kJ")

# ===========================================================================
kopf("1  Deckel (Ferreira 2025, Abb. 6: Steigungen von ln(T_w - T_a) über t)")
s_off, s_D = 0.0241, 0.0135   # 1/min, abgelesen aus den Regressionsgleichungen in Abb. 6
f_D = s_D / s_off
z("Steigung offen (y = -0,0241x + 4,1422, R² = 0,99)", s_off, "1/min")
z("Steigung mit Styropordeckel (y = -0,0135x + 4,2152)", s_D, "1/min")
z("Faktor kA_Deckel / kA_offen", f_D, "", "{:.4f}")
z("Abnahme des scheinbaren kA", 100 * (1 - f_D), "%", "{:.2f}")
z("tau offen = 1/Steigung", 1 / s_off, "min", "{:.2f}")
z("tau mit Deckel", 1 / s_D, "min", "{:.2f}")
z("Kontrolle über h aus Tab. 1: 1 - 9,9/18", 100 * (1 - 9.9 / 18), "%", "{:.2f}")
kAD = f_D * kA0
fall = {
    "A beide offen": zwei(kA0),
    "B beide mit Deckel": zwei(kAD),
    "C nur Tasse 2 (schwarz) mit Deckel": zwei(kA0, kAD),
    "D nur Tasse 1 (Milch sofort) mit Deckel": zwei(kAD, kA0),
}
print(f"  kA mit Deckel = {f_D:.4f} * {kA0:.5f} = {kAD:.5f} W/K")
print(f"  {'Fall (60 min)':<42s}{'theta_1':>9s}{'theta_2':>9s}{'Delta':>8s}")
for k, v in fall.items():
    print(f"  {k:<42s}{v['th1']:9.2f}{v['th2']:9.2f}{v['d']:8.2f}")
for k, kk in (("A beide offen", (kA0, kA0)), ("B beide mit Deckel", (kAD, kAD))):
    v = zwei(*kk, t=2400.0)
    print(f"  {k + ' (40 min, Versuch)':<42s}{v['th1']:9.2f}{v['th2']:9.2f}{v['d']:8.2f}")
th10_D = TH_U + (TH_K0 - TH_U) * math.exp(-kAD * T_MESS / C_K)
z("gleichwertige Messung mit Deckel: theta(10 min)", th10_D, "°C", "{:.2f}")
mxD = maximum_analytisch(kAD)
mx0 = maximum_analytisch(kA0)
z("größter Unterschied offen: Zeitpunkt", mx0["t_stern"] / 60, "min", "{:.2f}")
z("größter Unterschied mit Deckel (beide): Zeitpunkt", mxD["t_stern"] / 60, "min", "{:.2f}")
z("größter Unterschied mit Deckel (beide): Wert", mxD["dmax"], "K", "{:.3f}")
if M is not None:
    zt = M.zwei_tassen(kA1_faktor=f_D)
    z("Vergleich Fall D mit zwei_tassen(kA1_faktor): theta_1 Abw.", fall["D nur Tasse 1 (Milch sofort) mit Deckel"]["th1"] - zt["th1"], "K", "{:.2e}")
    z("Vergleich Fall D mit zwei_tassen(kA1_faktor): theta_2 Abw.", fall["D nur Tasse 1 (Milch sofort) mit Deckel"]["th2"] - zt["th2"], "K", "{:.2e}")
vB = fall["B beide mit Deckel"]
test("Deckel auf beiden Tassen", f"kA = 0,5602 * 0,3402 = {kAD:.4f} W/K (oder Messung {th10_D:.2f} °C nach 10 min), 60 min",
     f"theta_1 = {vB['th1']:.2f} °C, theta_2 = {vB['th2']:.2f} °C, Delta = {vB['d']:.2f} K; "
     f"Maximum {mxD['dmax']:.2f} K bei {mxD['t_stern']/60:.1f} min")
vC = fall["C nur Tasse 2 (schwarz) mit Deckel"]
test("Deckel nur auf Tasse 2", f"kA_1 = {kA0:.4f}, kA_2 = {kAD:.4f} W/K, 60 min",
     f"theta_1 = {vC['th1']:.2f} °C, theta_2 = {vC['th2']:.2f} °C, Delta = {vC['d']:.2f} K")

# ===========================================================================
kopf("2  Bechermaterial: Wärmekapazität C_T und (geschätztes) kA")
# (Name, Masse kg, c J/(kg K), kA-Schätzfaktor gegenüber Keramik offen, Herkunft)
becher = [
    ("Keramik, Arbeitswert Aufgabe", 0.300, 850.0, 1.00, "Aufgabe"),
    ("Porzellan 310 g, c 1070", 0.310, 1070.0, 1.00, "openLCA-Masse, c ETB"),
    ("Steinzeug 310 g, c 800", 0.310, 800.0, 1.00, "openLCA-Masse, c ETB"),
    ("Glas 250 g (Beispiel), c 840", 0.250, 840.0, 1.00, "Masse Beispiel, c ETB"),
    ("Edelstahl einwandig 150 g, c 500", 0.150, 500.0, 0.85, "Masse Beispiel, c 1.4301"),
    ("Edelstahl Vakuum, Innenwand 70 g", 0.070, 500.0, 0.45, "Schätzung"),
    ("Pappbecher 8,3 g, c 1340", 0.0083, 1340.0, 1.00, "openLCA-Masse, c ETB"),
]
print("  (i) gleiche Messung (67 °C nach 10 min), kA neu mit C_T (Funktion becher):")
print(f"  {'Becher':<36s}{'C_T J/K':>8s}{'C_T/C_K':>8s}{'kA W/K':>8s}{'th_1':>7s}{'th_2':>7s}{'Delta':>7s}{'D_max':>7s}{'t* min':>7s}")
for name, m, c, f, q in becher:
    CT = m * c
    kk = kA_aus_messung(CT)
    v = zwei(kk, C_T=CT)
    mx = maximum_analytisch(kk, C_T=CT)
    print(f"  {name:<36s}{CT:8.1f}{CT / C_K:8.3f}{kk:8.4f}{v['th1']:7.2f}{v['th2']:7.2f}{v['d']:7.2f}{mx['dmax']:7.2f}{mx['t_stern'] / 60:7.1f}")
    if M is not None and name.startswith("Keramik"):
        bb = M.becher(m, c)
        z("    Vergleich becher(): Abw. theta_1, theta_2", max(abs(v['th1'] - (bb['T1'] - K0)), abs(v['th2'] - (bb['T2'] - K0))), "K", "{:.1e}")
print("  (ii) Schätzung: kA = Faktor * kA des Keramikbechers (0,4440 W/K, Becher eingeschlossen):")
print(f"  {'Becher':<36s}{'Faktor':>7s}{'kA W/K':>8s}{'th(10)':>8s}{'th_1':>7s}{'th_2':>7s}{'Delta':>7s}{'t* min':>7s}")
for name, m, c, f, q in becher:
    CT = m * c
    kk = f * kAB
    v = zwei(kk, C_T=CT)
    th10 = TH_U + (TH_K0 - TH_U) * math.exp(-kk * T_MESS / (C_K + CT))
    mx = maximum_analytisch(kk, C_T=CT)
    print(f"  {name:<36s}{f:7.2f}{kk:8.4f}{th10:8.2f}{v['th1']:7.2f}{v['th2']:7.2f}{v['d']:7.2f}{mx['t_stern'] / 60:7.1f}")
print("  Herleitung der Faktoren (Ferreira 2025a/b, Steigungen mit Deckel, also ohne Verdunstung):")
f_al = 0.00983 / 0.0135
f_gl = 0.0100 / 0.0142
z("Aluminiumbecher / Keramik (Radiation, Abb. 5)", f_al, "", "{:.3f}")
z("Glas mit Alufolie / Glas (Radiation, Abb. 8)", f_gl, "", "{:.3f}")
z("Edelstahl blank offen: 0,44 + 0,56 * 0,728", 0.44 + 0.56 * f_al, "", "{:.3f}")
z("Vakuum doppelwandig offen: nur Oberseite, rund 0,44", 0.44, "", "{:.2f}")
CTp = 0.0083 * 1340.0
test("Pappbecher", f"C_T = 8,3 g * 1340 J/(kg K) = {CTp:.1f} J/K, gleiche Messung",
     f"kA = {kA_aus_messung(CTp):.4f} W/K, theta_1 = {zwei(kA_aus_messung(CTp), C_T=CTp)['th1']:.2f} °C, "
     f"theta_2 = {zwei(kA_aus_messung(CTp), C_T=CTp)['th2']:.2f} °C")
CTs = 0.150 * 500.0
vS = zwei(kA_aus_messung(CTs), C_T=CTs)
test("Edelstahl einwandig, gleiche Messung", f"C_T = 150 g * 500 J/(kg K) = {CTs:.1f} J/K",
     f"kA = {kA_aus_messung(CTs):.4f} W/K, theta_1 = {vS['th1']:.2f} °C, theta_2 = {vS['th2']:.2f} °C, Delta = {vS['d']:.2f} K")

# ===========================================================================
kopf("3  Verdunstung als eigener Term")
# Sättigungsdampfdruck nach IAPWS-IF97 (Region 4), Kontrolle gegen NIST WebBook
N4 = [0.11670521452767e4, -0.72421316703206e6, -0.17073846940092e2, 0.12020824702470e5,
      -0.32325550322333e7, 0.14915108613530e2, -0.48232657361591e4, 0.40511340542057e6,
      -0.23855557567849, 0.65017534844798e3]


def p_s(th):
    T = th + K0
    v = T + N4[8] / (T - N4[9])
    A = v * v + N4[0] * v + N4[1]
    B = N4[2] * v * v + N4[3] * v + N4[4]
    C = N4[5] * v * v + N4[6] * v + N4[7]
    return (2 * C / (-B + math.sqrt(B * B - 4 * A * C))) ** 4 * 1e6


NIST = {20: (2.3393, 83.914, 2537.4), 30: (4.2470, 125.73, 2555.5), 40: (7.3849, 167.53, 2573.5),
        50: (12.352, 209.34, 2591.3), 60: (19.946, 251.18, 2608.8), 70: (31.201, 293.07, 2626.1),
        80: (47.414, 335.01, 2643.0), 90: (70.182, 377.04, 2659.5), 100: (101.42, 419.17, 2675.6)}
print("  Kontrolle Dampfdruck: theta, p_s IF97 (eigene Umsetzung), p_s NIST, Abweichung")
for th, (p, hl, hv) in NIST.items():
    print(f"    {th:4d} °C  {p_s(th) / 1000:9.4f} kPa  {p:9.4f} kPa  {100 * (p_s(th) / 1000 / p - 1):+.3f} %")
TS = sorted(NIST)


def dh_v(th):
    """Verdampfungsenthalpie h'' - h' aus der NIST-Tabelle, linear interpoliert (J/kg)."""
    th = min(max(th, 20.0), 100.0)
    for a, b in zip(TS[:-1], TS[1:]):
        if a <= th <= b:
            ha = NIST[a][2] - NIST[a][1]
            hb = NIST[b][2] - NIST[b][1]
            return 1000 * (ha + (hb - ha) * (th - a) / (b - a))
    return 1000 * (NIST[100][2] - NIST[100][1])


z("Delta h_v bei 50 °C (NIST)", dh_v(50) / 1000, "kJ/kg", "{:.1f}")
z("Delta h_v bei 80 °C (NIST)", dh_v(80) / 1000, "kJ/kg", "{:.1f}")
MW, RU = 0.018015, 8.314462618


def rho_v(th):
    return p_s(th) * MW / (RU * (th + K0))


def sim_verd(th0, C_fest, m_w, kA_tr, betaA, phi, t_end=None, th_stop=None, dt=1.0, thu=TH_U,
             kurve=False, grad=False, cw=CP_K):
    """C dT/dt = -kA_tr (T - T_u) - mdot Delta h_v(T),  mdot = betaA (rho_v,s(T) - phi rho_v,s(T_u)),
    dm/dt = -mdot, C = C_fest + m_w c_w (C_fest: Milch, Becher; verdunstet wird nur Wasser).
    kurve: Punkte jede Minute; grad: Zeitpunkte jedes Übergangs um 1 K (wie bei Ferreira gemessen)."""
    rv_u = phi * rho_v(thu)
    t = 0.0
    pts = [(0.0, th0, m_w)] if (kurve or grad) else None

    def f(_t, y):
        T, mm = y[0], y[1]
        md = betaA * (rho_v(T) - rv_u)
        qtr = kA_tr * (T - thu)
        qv = md * dh_v(T)
        C = C_fest + mm * cw
        return [-(qtr + qv) / C, -md, qtr, qv]

    y = [th0, m_w, 0.0, 0.0]
    while True:
        if t_end is not None and t >= t_end - 1e-9:
            break
        h = dt if t_end is None else min(dt, t_end - t)
        yn = rk4(f, y, t, t + h, h)
        if grad:
            k = math.floor(y[0])
            while k > yn[0] and k >= (th_stop if th_stop is not None else -1e9):
                fr = (y[0] - k) / (y[0] - yn[0])
                if k < th0 - 1e-9:
                    pts.append((t + fr * h, float(k), y[1] + fr * (yn[1] - y[1])))
                k -= 1
        if th_stop is not None and yn[0] <= th_stop:
            frac = (y[0] - th_stop) / (y[0] - yn[0])
            y = [a + frac * (b - a) for a, b in zip(y, yn)]
            t += frac * h
            if kurve:
                pts.append((t, y[0], y[1]))
            break
        y, t = yn, t + h
        if kurve and abs(t / 60 - round(t / 60)) < 1e-6:
            pts.append((t, y[0], y[1]))
    return dict(th=y[0], dm=m_w - y[1], Qtr=y[2], Qv=y[3], t=t, kurve=pts, m=y[1])


def steigung_frei(pts, thu=TH_U):
    t = np.array([p[0] / 60 for p in pts])
    y = np.log(np.array([p[1] - thu for p in pts]))
    A = np.vstack([t, np.ones_like(t)]).T
    (a, b) = np.linalg.lstsq(A, y, rcond=None)[0]
    r2 = 1 - np.sum((y - (a * t + b)) ** 2) / np.sum((y - y.mean()) ** 2)
    return -a, b, r2


# Kalibrierung am offenen Lauf von Ferreira (2025a): Abb. 6 offen y = -0,0241x + 4,1422 (Punkte je 1 K von 90 bis 40 °C),
# ohne Rühren 90 -> 40 °C in rund 55 min (Abb. 7), 11 g verdunstet. Mit Deckel Steigung 0,0135 1/min.
C_F = 9.9 * 0.0232 * (60 / 0.0135)          # J/K, aus h = 9,9 W/(m² K), A = 232 cm², tau = 1/0,0135 min (abgeleitet)
m_F = C_F / CP_K
z("Ferreira-Becher: m_w c_w aus h A tau (abgeleitet)", C_F, "J/K", "{:.1f}")
z("Ferreira-Becher: Wassermasse (abgeleitet)", 1000 * m_F, "g", "{:.0f}")
z("Ferreira-Becher: kA mit Deckel ohne Becher-C", C_F * 0.0135 / 60, "W/K", "{:.4f}")


def ferreira_lauf(betaA, kA_tr, phi, C_bech):
    return sim_verd(90.0, C_bech, m_F, kA_tr, betaA, phi, th_stop=40.0, dt=2.0, grad=True)


print("  Kalibrierung beta*A (m³/s) am offenen Lauf, phi 0,5; kA_tr = (m_w c_w + C_Becher) * 0,0135/min:")
print(f"  {'Variante':<40s}{'betaA':>10s}{'Zeit min':>9s}{'dm g':>7s}{'Steig.':>8s}{'Achse':>8s}{'R²':>8s}")
kal = {}
for C_bech in (0.0, 300.0):
    kA_tr = (C_F + C_bech) * 0.0135 / 60
    for ziel in ("Steigung 0,0241", "11 g"):
        if ziel == "11 g":
            bA = bisektion(lambda b: ferreira_lauf(b, kA_tr, 0.5, C_bech)["dm"] - 0.011, 1e-7, 2e-4, 40)
        else:
            bA = bisektion(lambda b: steigung_frei(ferreira_lauf(b, kA_tr, 0.5, C_bech)["kurve"])[0] - 0.0241, 1e-7, 2e-4, 40)
        rr = ferreira_lauf(bA, kA_tr, 0.5, C_bech)
        sl, b0, r2 = steigung_frei(rr["kurve"])
        lab = f"C_Becher {C_bech:.0f} J/K, Ziel {ziel}"
        print(f"  {lab:<40s}{bA:10.3e}{rr['t'] / 60:9.1f}{1000 * rr['dm']:7.1f}{sl:8.4f}{b0:8.4f}{r2:8.4f}")
        kal[(C_bech, ziel)] = (bA, kA_tr)
bA_F, kAtr_F = kal[(300.0, "Steigung 0,0241")]
C_tot_F = C_F + 300.0
# Kontrolle: mit diesem beta*A, aber Deckel (beta*A = 0) -> Steigung 0,0135 nach Konstruktion
z("Kontrolle offen/Deckel-Verhältnis im kalibrierten Modell (Zielwert 0,56)", 0.0135 / 0.0241, "", "{:.3f}")

# Theoretische Abschätzung beta über die Lewis-Analogie (Größenordnung)
D_i = 0.082 - 2 * 0.0052          # m, Innendurchmesser aus Außendurchmesser (2025a) und Wandstärke (2025b)
A_s = math.pi * D_i ** 2 / 4
L_c = D_i / 4                      # A/P für eine Kreisfläche
rho_a, k_a, nu_a, Pr_a = 1.118, 0.02680, 1.726e-5, 0.7248   # Luft bei 42,5 °C (Ferreira 2025a)
alpha_a = nu_a / Pr_a
cp_a = Pr_a * k_a / (nu_a * rho_a)
Le = 0.85


def rho_feucht(th, pv, p=101325.0):
    return ((p - pv) * 0.028965 + pv * MW) / (RU * (th + K0))


z("Wasseroberfläche Ferreira-Becher A_s (randvoll)", A_s * 1e4, "cm²", "{:.1f}")
print("  Abschätzung beta aus freier Konvektion über der Oberfläche (Nu = 0,54 Ra^(1/4), L = D/4) und")
print("  Lewis-Analogie beta = h/(rho c_p) Le^(-2/3), Auftrieb aus Temperatur und Wasserdampf:")
for th in (80.0, 60.0, 40.0):
    rs_ = rho_feucht(th, p_s(th))
    ru_ = rho_feucht(TH_U, 0.5 * p_s(TH_U))
    Ra = 9.81 * (ru_ - rs_) / (0.5 * (ru_ + rs_)) * L_c ** 3 / (nu_a * alpha_a)
    h = 0.54 * Ra ** 0.25 * k_a / L_c
    beta = h / (rho_a * cp_a) * Le ** (-2 / 3)
    print(f"    {th:4.0f} °C: Ra = {Ra:9.3e}, h = {h:5.2f} W/(m² K), beta = {beta:.4f} m/s, beta*A = {beta * A_s:.3e} m³/s"
          f"  (kalibriert/theoretisch = {bA_F / (beta * A_s):.2f})")
z("kalibriertes beta*A (Referenz: C_Becher 300 J/K, Steigung)", bA_F, "m³/s", "{:.3e}")
z("  entspricht beta bei randvoller Öffnung", bA_F / A_s, "m/s", "{:.4f}")

# Übertragung auf die Tasse der Aufgabe, kA_tr jeweils aus der Messung (67 °C nach 10 min)
print("  Übertragung auf die Aufgabe (kA_tr so, dass 67 °C nach 10 min; Milch verdunstet nicht, Wasser schon):")
print(f"  {'Variante':<36s}{'betaA':>10s}{'kA_tr':>8s}{'th_1':>7s}{'th_2':>7s}{'Delta':>7s}{'dm1 g':>7s}{'dm2 g':>7s}{'Ant.80':>7s}{'Ant.60':>7s}{'Qv79':>6s}{'Qg79':>6s}")
verd_ergebnis = {}


def verd_fall(lab, bA, phi, C_T):
    def fehler(k):
        return sim_verd(TH_K0, C_T, M_K, k, bA, phi, t_end=T_MESS, dt=2.0)["th"] - TH_MESS
    kk = bisektion(fehler, -0.5, 1.0, 50)
    r2 = sim_verd(TH_K0, C_T, M_K, kk, bA, phi, t_end=T_END, dt=2.0)
    th10 = ((C_K + C_T) * TH_K0 + C_M * TH_M) / (C_G + C_T)
    r1 = sim_verd(th10, C_M + C_T, M_K, kk, bA, phi, t_end=T_END, dt=2.0)
    C2 = r2["m"] * CP_K + C_T
    th2 = (C2 * r2["th"] + C_M * TH_M) / (C2 + C_M)
    qv0 = bA * (rho_v(80.0) - phi * rho_v(TH_U)) * dh_v(80.0)
    qtr0 = kk * 60.0
    qv79 = bA * (rho_v(79.0) - phi * rho_v(TH_U)) * dh_v(79.0)
    ant60 = r2["Qv"] / (r2["Qv"] + r2["Qtr"])
    e = dict(kA_tr=kk, th1=r1["th"], th2=th2, d=r1["th"] - th2, dm1=r1["dm"], dm2=r2["dm"], bA=bA, phi=phi, C_T=C_T,
             ant0=qv0 / (qv0 + qtr0), ant60=ant60, qv79=qv79, qtot79=qv79 + kk * 59.0)
    verd_ergebnis[lab] = e
    warn = "  (kA_tr < 0: unverträglich)" if kk < 0 else ""
    print(f"  {lab:<36s}{bA:10.3e}{kk:8.4f}{e['th1']:7.2f}{e['th2']:7.2f}{e['d']:7.2f}{1000 * e['dm1']:7.2f}{1000 * e['dm2']:7.2f}"
          f"{100 * e['ant0']:6.1f}%{100 * ant60:6.1f}%{qv79:6.2f}{e['qtot79']:6.2f}{warn}")
    return e


bA_prop = bA_F * C_K / C_tot_F
verd_fall("R ohne Becher, proportional, phi 0,5", bA_prop, 0.5, 0.0)
verd_fall("ohne Becher, proportional, phi 0,3", bA_F * C_K / C_tot_F, 0.3, 0.0)
verd_fall("ohne Becher, proportional, phi 0,7", bA_F * C_K / C_tot_F, 0.7, 0.0)
verd_fall("ohne Becher, gleiche Öffnung, phi 0,5", bA_F, 0.5, 0.0)
verd_fall("ohne Becher, prop. aus Ziel 11 g", kal[(300.0, "11 g")][0] * C_K / C_tot_F, 0.5, 0.0)
verd_fall("Becher 255 J/K, proportional, phi 0,5", bA_F * (C_K + C_T0) / C_tot_F, 0.5, C_T0)
verd_fall("Becher 255 J/K, gleiche Öffnung", bA_F, 0.5, C_T0)
ref = verd_ergebnis["R ohne Becher, proportional, phi 0,5"]
# scheinbares kA im Referenzmodell (zwei Punkte) offen gegen ohne Verdunstung
th10_ohne = sim_verd(TH_K0, 0.0, M_K, ref["kA_tr"], 0.0, 0.5, t_end=T_MESS, dt=2.0)["th"]
kA_ohne = -C_K / T_MESS * math.log((th10_ohne - TH_U) / (TH_K0 - TH_U))
z("Referenz: kA_tr / kA (Anteil trocken im 10-min-Wert)", ref["kA_tr"] / kA0, "", "{:.3f}")
z("Referenz: Deckel im Modell (beta*A = 0): theta(10 min)", th10_ohne, "°C", "{:.2f}")
z("Referenz: Qdot_v bei 79 °C", ref["qv79"], "W", "{:.2f}")
z("Referenz: Qdot gesamt bei 79 °C", ref["qtot79"], "W", "{:.2f}")
z("Condoret (2007, Tab. 2, Sekundärquelle): 12,0 / 22,7", 100 * 12.0 / 22.7, "%", "{:.1f}")
print("  Referenz: Wärmeströme über der Temperatur (Verdunstung, trocken, Anteil, scheinbares kA = Qdot/(theta - theta_u)):")
for th in (80.0, 70.0, 60.0, 50.0, 40.0, 30.0):
    qv = ref["bA"] * (rho_v(th) - 0.5 * rho_v(TH_U)) * dh_v(th)
    qt = ref["kA_tr"] * (th - TH_U)
    print(f"    {th:4.0f} °C: Qdot_v = {qv:6.2f} W, Qdot_tr = {qt:6.2f} W, Anteil {100 * qv / (qv + qt):5.1f} %, kA_schein = {(qv + qt) / (th - TH_U):.4f} W/K")
print("  Stefan-Faktor ln((1 - w_u)/(1 - w_s)) / (w_s - w_u) (hohe Stoffübergangsraten, nicht im Modell):")
for th in (80.0, 60.0, 40.0):
    def w(thx, pv):
        return pv * MW / ((101325.0 - pv) * 0.028965 + pv * MW)
    ws, wu = w(th, p_s(th)), w(TH_U, 0.5 * p_s(TH_U))
    print(f"    {th:4.0f} °C: w_s = {ws:.4f}, w_u = {wu:.4f}, Faktor {math.log((1 - wu) / (1 - ws)) / (ws - wu):.3f}")
z("Obergrenze der Masse: Q_2 / Delta h_v(50 °C), alle Wärme verdunstet", r0["Q2"] / dh_v(50) * 1000, "g", "{:.1f}")
test("Verdunstung, Referenzvariante (nur Größenordnung, nicht gegen Messung getestet)",
     f"beta*A = {ref['bA']:.3e} m³/s, phi = 0,5, kA_tr = {ref['kA_tr']:.4f} W/K (aus 67 °C nach 10 min), RK4 2 s",
     f"theta_1 = {ref['th1']:.2f} °C, theta_2 = {ref['th2']:.2f} °C, Delta = {ref['d']:.2f} K, "
     f"verdunstet {1000 * ref['dm1']:.2f} g und {1000 * ref['dm2']:.2f} g")

# ===========================================================================
kopf("4  Nichtlineare Wärmeabgabe")


def c_aus_messung(n):
    th0, thm = TH_K0 - TH_U, TH_MESS - TH_U
    if n == 1:
        return -C_K / T_MESS * math.log(thm / th0)
    return (thm ** (1 - n) - th0 ** (1 - n)) * C_K / ((n - 1) * T_MESS)


def ende_pot(th0e, C, t, c, n):
    if n == 1:
        return th0e * math.exp(-c * t / C)
    return (th0e ** (1 - n) + (n - 1) * c * t / C) ** (1 / (1 - n))


def pot_tassen(n, t=T_END, cfak=1.0):
    c = c_aus_messung(n) * cfak
    th10e = (C_K * (TH_K0 - TH_U) + C_M * (TH_M - TH_U)) / C_G
    th1 = TH_U + ende_pot(th10e, C_G, t, c, n)
    thK = TH_U + ende_pot(TH_K0 - TH_U, C_K, t, c, n)
    th2 = (C_K * thK + C_M * TH_M) / C_G
    return th1, th2, c, thK


print(f"  {'Exponent n':<14s}{'c':>12s}{'th_1':>8s}{'th_2':>8s}{'Delta':>8s}{'RK4-Abw. th_2':>16s}{'Modell-Abw.':>13s}")
nl = {}
for n in (1.0, 1.25, 4 / 3):
    th1, th2, c, thK = pot_tassen(n)
    yK = rk4(lambda _t, y: [-c * max(y[0], 0) ** n / C_K], [TH_K0 - TH_U], 0, T_END, 0.5)[0]
    th2_rk = (C_K * (TH_U + yK) + C_M * TH_M) / C_G
    dm = float("nan")
    if M is not None:
        T1m, T2m = M.nichtlinear(n)
        dm = max(abs(th1 - (T1m - K0)), abs(th2 - (T2m - K0)))
    nl[n] = (th1, th2)
    print(f"  {n:<14.4f}{c:12.5e}{th1:8.3f}{th2:8.3f}{th1 - th2:8.3f}{th2 - th2_rk:16.2e}{dm:13.2e}")
# physikalische Variante: laminare freie Konvektion (5/4) plus Strahlung, Anteil Strahlung 33 % bei 65 °C (Ferreira 2025a)
SIG = 5.670e-8


def g_kr(th, r=0.33, thr=65.0):
    T, Tu, Tr = th + K0, TH_U + K0, thr + K0
    konv = (th - TH_U) ** 1.25 / (thr - TH_U) ** 1.25
    strl = (T ** 4 - Tu ** 4) / (Tr ** 4 - Tu ** 4)
    return (1 - r) * konv + r * strl     # = 1 bei thr; Wärmestrom = a * g


def sim_g(th0, C, a, t):
    return rk4(lambda _t, y: [-a * g_kr(y[0]) / C], [th0], 0, t, 1.0)[0]


a_kr = bisektion(lambda a: sim_g(TH_K0, C_K, a, T_MESS) - TH_MESS, 1.0, 60.0, 60)
th10 = (C_K * TH_K0 + C_M * TH_M) / C_G
th1_kr = sim_g(th10, C_G, a_kr, T_END)
thK_kr = sim_g(TH_K0, C_K, a_kr, T_END)
th2_kr = (C_K * thK_kr + C_M * TH_M) / C_G
z("Konvektion 5/4 + Strahlung (33 % bei 65 °C): Wärmestrom bei 65 °C", a_kr, "W", "{:.3f}")
z("  theta_1", th1_kr, "°C", "{:.3f}")
z("  theta_2", th2_kr, "°C", "{:.3f}")
z("  Delta", th1_kr - th2_kr, "K", "{:.3f}")
z("lineares h_r = eps sigma (T^4 - T_u^4)/(T - T_u), eps 0,93, T 90 °C", 0.93 * SIG * ((90 + K0) ** 4 - (20 + K0) ** 4) / 70, "W/(m² K)", "{:.2f}")
z("lineares h_r, T 40 °C", 0.93 * SIG * ((40 + K0) ** 4 - (20 + K0) ** 4) / 20, "W/(m² K)", "{:.2f}")
print("  Zusammenstellung (60 min):")
print(f"  {'Modell':<46s}{'th_1':>8s}{'th_2':>8s}{'Delta':>8s}")
print(f"  {'linear (Aufgabe)':<46s}{r0['th1']:8.2f}{r0['th2']:8.2f}{r0['d']:8.2f}")
print(f"  {'Potenz n = 5/4':<46s}{nl[1.25][0]:8.2f}{nl[1.25][1]:8.2f}{nl[1.25][0] - nl[1.25][1]:8.2f}")
print(f"  {'Potenz n = 4/3':<46s}{nl[4/3][0]:8.2f}{nl[4/3][1]:8.2f}{nl[4/3][0] - nl[4/3][1]:8.2f}")
print(f"  {'Konvektion 5/4 + Strahlung':<46s}{th1_kr:8.2f}{th2_kr:8.2f}{th1_kr - th2_kr:8.2f}")
print(f"  {'Verdunstung (Referenzvariante Abschnitt 3)':<46s}{ref['th1']:8.2f}{ref['th2']:8.2f}{ref['d']:8.2f}")
th1n, th2n, cn, _ = pot_tassen(1.25)
test("nichtlinear n = 5/4", f"c aus der Messung = {cn:.5e} W/K^1,25, 60 min",
     f"theta_1 = {th1n:.2f} °C, theta_2 = {th2n:.2f} °C, Delta = {th1n - th2n:.2f} K")

# ===========================================================================
kopf("5  kA aus allen Messpunkten (synthetische Datensätze)")
t_p = np.arange(0, 61, 10) * 60.0


def daten(n, rng, rausch=0.3, runden=True):
    if n == 1:
        th = TH_U + (TH_K0 - TH_U) * np.exp(-kA0 * t_p / C_K)
    else:
        c = c_aus_messung(n)
        th = TH_U + np.array([ende_pot(TH_K0 - TH_U, C_K, t, c, n) for t in t_p])
    th_m = th + rng.uniform(-rausch, rausch, size=th.size)
    return th, (np.round(th_m, 1) if runden else th_m)


def auswertung(th_m):
    th_e = th_m - TH_U
    t = t_p
    erg = {}
    # (a) zwei Punkte (0 und 10 min)
    erg["2 Punkte"] = (-C_K * math.log(th_e[1] / th_e[0]) / T_MESS, float("nan"), float("nan"))
    # (b) Ursprungsgerade: y = ln(theta/theta_0) = -a t
    y = np.log(th_e[1:] / th_e[0])
    tt = t[1:]
    a = -np.sum(tt * y) / np.sum(tt * tt)
    s = math.sqrt(np.sum((y + a * tt) ** 2) / (len(tt) - 1))
    erg["Ursprungsgerade"] = (a * C_K, s / math.sqrt(np.sum(tt * tt)) * C_K, 0.0)
    # (c) freier Achsenabschnitt: ln(theta) = b - a t
    Y = np.log(th_e)
    A = np.vstack([t, np.ones_like(t)]).T
    (sl, b), res, _, _ = np.linalg.lstsq(A, Y, rcond=None)
    s2 = math.sqrt(np.sum((Y - (sl * t + b)) ** 2) / (len(t) - 2))
    sa = s2 / math.sqrt(np.sum((t - t.mean()) ** 2))
    erg["freier Achsenabschnitt"] = (-sl * C_K, sa * C_K, b - math.log(th_e[0]))
    # (d) gewichtet (w = theta², weil sigma_ln = sigma_theta/theta), freier Achsenabschnitt
    w = th_e ** 2
    W = np.sqrt(w)
    (slw, bw), _, _, _ = np.linalg.lstsq(A * W[:, None], Y * W, rcond=None)
    erg["gewichtet, frei"] = (-slw * C_K, float("nan"), bw - math.log(th_e[0]))
    return erg


rng = np.random.default_rng(20261104)
for n in (1.0, 1.25):
    th_w, th_m = daten(n, rng)
    print(f"  Datensatz n = {n} (Rauschen gleichverteilt +-0,3 K, dann auf 0,1 K gerundet), Samen 20261104:")
    print("    t/min  " + "".join(f"{int(x / 60):7d}" for x in t_p))
    print("    wahr   " + "".join(f"{x:7.2f}" for x in th_w))
    print("    Messung" + "".join(f"{x:7.1f}" for x in th_m))
    kA_int = [-C_K * math.log((th_m[i + 1] - TH_U) / (th_m[i] - TH_U)) / 600 for i in range(len(t_p) - 1)]
    print("    kA je Intervall (W/K): " + ", ".join(f"{k:.3f}" for k in kA_int))
    erg = auswertung(th_m)
    for k, (kk, s, b0) in erg.items():
        v = zwei(kk)
        thK60 = v["thK"]
        print(f"    {k:<24s} kA = {kk:.4f} W/K" + (f" +- {s:.4f}" if not math.isnan(s) else "          ")
              + (f", Achsenabschnitt-ln(theta_0) = {b0:+.4f}" if not math.isnan(b0) else "") +
              f"; Vorhersage th_K(60) = {thK60:.2f} °C, Delta = {v['d']:.2f} K")
    if n == 1.25:
        fit = erg["freier Achsenabschnitt"]
        Y = np.log(th_m - TH_U)
        res = Y - (np.log(th_m[0] - TH_U) + fit[2] - fit[0] / C_K * t_p)
        print("    Residuen der freien Geraden (ln): " + ", ".join(f"{x:+.4f}" for x in res))
    print(f"    wahres th_K(60) = {th_w[-1]:.2f} °C")
# Monte-Carlo
print("  Monte-Carlo (20 000 Reihen je Fall, Rauschen gleichverteilt +-0,3 K, ohne Runden):")
for n in (1.0, 1.25):
    rng = np.random.default_rng(7)
    samml = {}
    for _ in range(20000):
        _, th_m = daten(n, rng, runden=False)
        for k, (kk, s, b0) in auswertung(th_m).items():
            samml.setdefault(k, []).append(kk)
    for k, v in samml.items():
        v = np.array(v)
        print(f"    n = {n:<5}{k:<24s} Mittel {v.mean():.4f} W/K, Streuung {v.std(ddof=1):.4f} W/K ({100 * v.std(ddof=1) / v.mean():.2f} %)")
dthK = -(TH_K0 - TH_U) * T_END / C_K * math.exp(-kA0 * T_END / C_K)
z("Ableitung d theta_K(60 min) / d kA", dthK, "K/(W/K)", "{:.1f}")
for lab, s_ in (("2 Punkte", 0.0065), ("Ursprungsgerade", 0.0018), ("frei", 0.0022)):
    z(f"  Streuung theta_K(60 min) aus sigma_kA ({lab}, {s_} W/K)", abs(dthK) * s_, "K", "{:.2f}")
print("  Empfindlichkeit von Delta(60 min) gegen kA (linear):")
for fk in (0.9, 0.95, 1.0, 1.05, 1.1):
    v = zwei(fk * kA0)
    print(f"    kA = {fk:.2f} * kA0: theta_1 = {v['th1']:.2f}, theta_2 = {v['th2']:.2f}, Delta = {v['d']:.3f} K")
th_exakt = TH_U + (TH_K0 - TH_U) * np.exp(-kA0 * t_p / C_K)
e_ex = auswertung(th_exakt)
test("Ausgleich, exakte Daten (n = 1, alle 10 min)", "theta = " + "; ".join(f"{x:.2f}" for x in th_exakt) + " °C",
     f"kA = {e_ex['Ursprungsgerade'][0]:.4f} W/K (Ursprungsgerade) = {e_ex['freier Achsenabschnitt'][0]:.4f} W/K (frei) = 2 Punkte")
_, th_m_test = daten(1.0, np.random.default_rng(20261104))
e_t = auswertung(th_m_test)
test("Ausgleich, verrauschte Reihe n = 1 (Samen 20261104, gerundet auf 0,1 K)", "theta = " + "; ".join(f"{x:.1f}" for x in th_m_test) + " °C",
     f"kA = {e_t['2 Punkte'][0]:.4f} (2 Punkte), {e_t['Ursprungsgerade'][0]:.4f} +- {e_t['Ursprungsgerade'][1]:.4f} (Ursprung), "
     f"{e_t['freier Achsenabschnitt'][0]:.4f} +- {e_t['freier Achsenabschnitt'][1]:.4f} W/K (frei)")

# ===========================================================================
kopf("6  Energie sichtbar machen")
dtq = 1.0
ts = np.arange(0, T_END + dtq / 2, dtq)
qd1 = kA0 * (r0["th10"] - TH_U) * np.exp(-kA0 * ts / C_G)
qd2 = kA0 * (TH_K0 - TH_U) * np.exp(-kA0 * ts / C_K)
Q1n = np.trapezoid(qd1, ts) if hasattr(np, "trapezoid") else np.trapz(qd1, ts)
Q2n = np.trapezoid(qd2, ts) if hasattr(np, "trapezoid") else np.trapz(qd2, ts)
z("Q_1 geschlossen", r0["Q1"] / 1000, "kJ", "{:.4f}")
z("Q_1 als Fläche unter Qdot_1(t) (Trapez, 1 s)", Q1n / 1000, "kJ", "{:.4f}")
z("Q_2 geschlossen", r0["Q2"] / 1000, "kJ", "{:.4f}")
z("Q_2 als Fläche unter Qdot_2(t)", Q2n / 1000, "kJ", "{:.4f}")
z("Qdot_1(0)", qd1[0], "W", "{:.2f}")
z("Qdot_2(0)", qd2[0], "W", "{:.2f}")
z("Qdot_1(60 min)", qd1[-1], "W", "{:.2f}")
z("Qdot_2(60 min, vor dem Zugießen)", qd2[-1], "W", "{:.2f}")
z("Q_2 - Q_1", (r0["Q2"] - r0["Q1"]) / 1000, "kJ", "{:.4f}")
z("C_G (theta_1 - theta_2)", C_G * r0["d"] / 1000, "kJ", "{:.4f}")
eG = math.exp(-kA0 * T_END / C_G)
eK = math.exp(-kA0 * T_END / C_K)
for thm_ in (TH_M, 60.0):
    kaf = C_K * (TH_K0 - TH_U) * (eG - eK) / C_G
    mil = C_M * (thm_ - TH_U) * (eG - 1) / C_G
    z(f"Zerlegung (Milch {thm_:.0f} °C): Kaffee-Effekt", kaf, "K", "{:.3f}")
    z(f"Zerlegung (Milch {thm_:.0f} °C): Milch-Effekt", mil, "K", "{:.3f}")
    z(f"  Summe / direkt", kaf + mil, "K", "{:.3f}")
    z(f"  direkt aus zwei()", zwei(kA0, thM1=thm_)["d"], "K", "{:.3f}")
# Energie in Wärme umgerechnet: Kaffee-Effekt und Milch-Effekt in kJ (mal C_G)
z("Kaffee-Effekt * C_G", C_G * C_K * (TH_K0 - TH_U) * (eG - eK) / C_G / 1000, "kJ", "{:.3f}")
z("Milch-Effekt * C_G (kalte Milch)", C_M * (TH_M - TH_U) * (eG - 1) / 1000, "kJ", "{:.3f}")
z("Becher: Q_1, Q_2 und C_GT Delta", rB["Q1"] / 1000, "kJ", "{:.3f}")
z("  ", rB["Q2"] / 1000, "kJ", "{:.3f}")
z("  ", (C_G + C_T0) * rB["d"] / 1000, "kJ", "{:.3f}")
z("Becher: davon gibt der Becher in Tasse 2 ab: C_B (80 - th_K)", C_T0 * (TH_K0 - rB["thK"]) / 1000, "kJ", "{:.3f}")
test("Energie", "Standardwerte, 60 min", f"Q_1 = {r0['Q1']/1000:.2f} kJ, Q_2 = {r0['Q2']/1000:.2f} kJ, Q_2 - Q_1 = "
     f"{(r0['Q2']-r0['Q1'])/1000:.2f} kJ = C_G * {r0['d']:.2f} K; Qdot(0) = {qd1[0]:.2f} W und {qd2[0]:.2f} W")

# ===========================================================================
kopf("7  Größter Unterschied über dem Zeitpunkt der Zugabe")


def scan_linear(kA, C_T=0.0, thM=TH_M, tmax=400 * 60.0, dt=1.0):
    best = (-1e9, 0.0)
    t = 0.0
    while t <= tmax:
        v = zwei(kA, C_T=C_T, thM1=thM, t=t)
        if v["d"] > best[0]:
            best = (v["d"], t)
        t += dt
    return best


print(f"  {'Fall':<44s}{'t* ana':>8s}{'t* num':>8s}{'th_K*':>8s}{'D_max ana':>10s}{'D_max num':>10s}")
for lab, kk, CT in (("ohne Becher, kA0", kA0, 0.0), ("ohne Becher, 0,5 kA0", 0.5 * kA0, 0.0),
                    ("ohne Becher, 2 kA0", 2 * kA0, 0.0), ("ohne Becher, Deckel 0,56 kA0", kAD, 0.0),
                    ("Becher 255 J/K, kA 0,4440", kAB, C_T0), ("Becher 255 J/K, 0,5 * 0,4440", 0.5 * kAB, C_T0),
                    ("Vakuumbecher 35 J/K, 0,45 * 0,4440", 0.45 * kAB, 35.0), ("Pappbecher 11,1 J/K", kA_aus_messung(CTp), CTp)):
    a = maximum_analytisch(kk, C_T=CT)
    dnum, tnum = scan_linear(kk, C_T=CT)
    print(f"  {lab:<44s}{a['t_stern'] / 60:8.2f}{tnum / 60:8.2f}{a['thK_stern']:8.2f}{a['dmax']:10.4f}{dnum:10.4f}")
a = maximum_analytisch(kA0, thM=60.0)
dnum, tnum = scan_linear(kA0, thM=60.0)
print(f"  {'erwärmte Milch 60 °C (Maximum für sofort)':<44s}{a['t_stern'] / 60:8.2f}{tnum / 60:8.2f}{a['thK_stern']:8.2f}{a['dmax']:10.4f}{dnum:10.4f}")
for thm_ in (0.0, 10.0, 20.0):
    a = maximum_analytisch(kA0, thM=thm_)
    print(f"  {'Milch ' + str(thm_) + ' °C':<44s}{a['t_stern'] / 60:8.2f}{'':>8s}{a['thK_stern']:8.2f}{a['dmax']:10.4f}")
for th0_ in (70.0, 90.0):
    a = maximum_analytisch(kA0, th0=th0_)
    print(f"  {'Kaffee ' + str(th0_) + ' °C am Anfang':<44s}{a['t_stern'] / 60:8.2f}{'':>8s}{a['thK_stern']:8.2f}{a['dmax']:10.4f}")
# nichtlinear: gleicher Verlauf bei c*t, also gleicher Höchstwert
print("  nichtlinear (n = 5/4), c skaliert: Höchstwert bleibt, Zeitpunkt skaliert mit 1/c:")
for nn in (1.25, 4 / 3):
    for cf in (0.5, 1.0, 2.0):
        best = (-1, 0)
        for tz in np.arange(0, 400 * 60, 1.0):
            th1, th2, _, _ = pot_tassen(nn, t=tz, cfak=cf)
            if th1 - th2 > best[0]:
                best = (th1 - th2, tz)
        # Schnittpunkt theta_1 = theta_K genau (Bisektion)
        ts_ = bisektion(lambda tz: pot_tassen(nn, t=tz, cfak=cf)[0] - pot_tassen(nn, t=tz, cfak=cf)[3], 1.0, 400 * 60.0, 80)
        th1, th2, _, thK = pot_tassen(nn, t=ts_, cfak=cf)
        print(f"    n = {nn:.4f}, c-Faktor {cf}: D_max (Raster 1 s) = {best[0]:.4f} K bei {best[1] / 60:.2f} min;"
              f" Schnittpunkt {ts_ / 60:.2f} min, th_K = th_1 = {thK:.3f} °C, C_M (th_K - th_M)/C_G = {C_M * (thK - TH_M) / C_G:.4f} K")
# Verdunstungsmodell: kA_tr allein halbiert (Dämmung der Wand) und beide Terme halbiert
print("  Verdunstungsmodell (Referenz): Kurven bis 300 min, Unterschied über dem Zugabezeitpunkt:")
for lab, fk_tr, fk_v in (("Referenz", 1.0, 1.0), ("nur Wand gedämmt (kA_tr * 0,5)", 0.5, 1.0), ("Verdunstung aus (beta*A = 0)", 1.0, 0.0)):
    th10 = (C_K * TH_K0 + C_M * TH_M) / C_G
    k1 = sim_verd(th10, C_M, M_K, ref["kA_tr"] * fk_tr, ref["bA"] * fk_v, 0.5, t_end=300 * 60, dt=2.0, kurve=True)["kurve"]
    k2 = sim_verd(TH_K0, 0.0, M_K, ref["kA_tr"] * fk_tr, ref["bA"] * fk_v, 0.5, t_end=300 * 60, dt=2.0, kurve=True)["kurve"]
    best = (-1, 0, 0)
    for (t1, a1, m1), (t2, a2, m2) in zip(k1, k2):
        C2 = m2 * CP_K
        th2 = (C2 * a2 + C_M * TH_M) / (C2 + C_M)
        if a1 - th2 > best[0]:
            best = (a1 - th2, t1, a2)
    print(f"    {lab:<34s} D_max = {best[0]:.3f} K bei {best[1] / 60:.0f} min, th_K dort {best[2]:.2f} °C")
ts_nl = bisektion(lambda tz: pot_tassen(1.25, t=tz)[0] - pot_tassen(1.25, t=tz)[3], 1.0, 400 * 60.0, 80)
_a, _b, _, _thK = pot_tassen(1.25, t=ts_nl)
test("Maximum nichtlinear n = 5/4", "c aus der Messung, Zugabezeitpunkt frei",
     f"Delta_max = {_a - _b:.2f} K bei theta_K* = {_thK:.2f} °C, t* = {ts_nl / 60:.2f} min (Schnittpunkt)")
mw = maximum_analytisch(kA0, thM=60.0)
test("Extremum bei erwärmter Milch 60 °C", "Standardwerte, Milch 60 °C, Zugabezeitpunkt frei",
     f"Delta_max = +{mw['dmax']:.2f} K (sofort wärmer) bei t* = {mw['t_stern']/60:.2f} min, theta_K* = {mw['thK_stern']:.2f} °C; "
     f"bei 60 min Delta = {zwei(kA0, thM1=60.0)['d']:.2f} K")
mx = maximum_analytisch(kA0)
test("Maximum ohne Becher", "Standardwerte, beliebiges kA",
     f"Delta_max = {mx['dmax']:.2f} K bei theta_K* = {mx['thK_stern']:.2f} °C, t* = {mx['t_stern']/60:.2f} min * (0,3402 W/K / kA)")
mxb = maximum_analytisch(kAB, C_T=C_T0)
test("Maximum mit Becher", "C_B = 255 J/K, beliebiges kA",
     f"Delta_max = {mxb['dmax']:.2f} K bei theta_K* = {mxb['thK_stern']:.2f} °C, t* = {mxb['t_stern']/60:.2f} min bei kA = 0,4440 W/K")

# ===========================================================================
kopf("8  Beide Tassen kühlen nach dem Zugießen weiter ab")
aG = kA0 / C_G
for tz, tv in ((60, 60), (60, 70), (60, 90), (60, 120), (40, 40), (40, 50), (40, 60)):
    dz = zwei(kA0, t=tz * 60.0)["d"]
    ana = dz * math.exp(-aG * (tv - tz) * 60)
    # numerisch: Tasse 1 bis tv, Tasse 2 bis tz schwarz, dann gemischt bis tv
    v = zwei(kA0, t=tz * 60.0)
    th2v = TH_U + (v["th2"] - TH_U) * math.exp(-aG * (tv - tz) * 60)
    th1v = TH_U + (v["th10"] - TH_U) * math.exp(-aG * tv * 60)
    print(f"  Zugabe {tz:3d} min, Vergleich {tv:3d} min: Delta = {ana:.3f} K (direkt {th1v - th2v:.3f} K), th_1 = {th1v:.2f}, th_2 = {th2v:.2f} °C")
z("Abklingzeit des Unterschieds tau_G", C_G / kA0 / 60, "min", "{:.2f}")
z("Halbwertszeit tau_G ln 2", C_G / kA0 / 60 * math.log(2), "min", "{:.2f}")
z("mit Becher: tau_GT = (C_G + C_B) / kA_B", (C_G + C_T0) / kAB / 60, "min", "{:.2f}")
vB60 = zwei(kAB, C_T=C_T0)
z("mit Becher: Delta(90 min) bei Zugabe 60 min", vB60["d"] * math.exp(-kAB / (C_G + C_T0) * 1800), "K", "{:.3f}")
print("  Fester Vergleich bei 60 min, Zugabe früher (lineares Modell):")
for tz in (0, 10, 20, 30, 40, 50, 60):
    dz = zwei(kA0, t=tz * 60.0)["d"]
    print(f"    Zugabe {tz:2d} min: Delta(60 min) = {dz * math.exp(-aG * (60 - tz) * 60):.3f} K")
print("  nichtlinear n = 5/4: Unterschied nach Zugabe bei 60 min, Vergleich später (numerisch):")
c125 = c_aus_messung(1.25)
th1z, th2z, _, _ = pot_tassen(1.25, t=3600.0)
for tv in (60, 70, 90, 120):
    a1 = TH_U + ende_pot(th1z - TH_U, C_G, (tv - 60) * 60, c125, 1.25)
    a2 = TH_U + ende_pot(th2z - TH_U, C_G, (tv - 60) * 60, c125, 1.25)
    lin = (th1z - th2z) * math.exp(-aG * (tv - 60) * 60)
    print(f"    {tv:3d} min: Delta = {a1 - a2:.3f} K (Exponentialansatz mit tau_G: {lin:.3f} K)")
v90 = zwei(kA0)
test("Abkühlen nach der Zugabe", "Zugabe 60 min, Vergleich 90 min",
     f"Delta = {v90['d'] * math.exp(-aG * 1800):.2f} K = {v90['d']:.2f} K * exp(-30 min/{C_G / kA0 / 60:.2f} min)")

# ===========================================================================
kopf("9  Sonstiges: Füllhöhe, Biot-Zahl, nicht vorgewärmter Becher")
print("  Füllhöhe (kA von Tasse 1 um Faktor größer):")
for fk in (1.0, 1.05, 1.10, 1.15):
    v = zwei(fk * kA0, kA0)
    s = ""
    if M is not None:
        zt = M.zwei_tassen(kA1_faktor=fk)
        s = f"  (zwei_tassen: {zt['th1']:.2f}, Abw. {v['th1'] - zt['th1']:.1e})"
    mxf = None
    print(f"    Faktor {fk:.2f}: theta_1 = {v['th1']:.2f} °C, theta_2 = {v['th2']:.2f} °C, Delta = {v['d']:.2f} K{s}")
# Biot
h_a = 10.0
z("Bi Wand Keramik = h e / k (h 10, e 5,2 mm, k 1,5)", h_a * 0.0052 / 1.5, "", "{:.3f}")
z("Bi Kaffee nur Wärmeleitung = h (V/A) / k_w (V/A ~ 1 cm, k 0,6)", h_a * 0.01 / 0.6, "", "{:.3f}")
q_aussen = h_a * (90 - 3.5 - 20)
z("innerer Wärmeübergang aus Ferreira (3,5 K Abstand bei 90 °C)", q_aussen / 3.5, "W/(m² K)", "{:.0f}")
z("wirksame Biot-Zahl h_a / h_i", h_a / (q_aussen / 3.5), "", "{:.3f}")
# nicht vorgewärmter Becher
for CT in (C_T0, 0.310 * 1070.0):
    th_gl = (C_K * TH_K0 + CT * TH_U) / (C_K + CT)
    z(f"nicht vorgewärmt, C_T = {CT:.0f} J/K: Ausgleichstemperatur", th_gl, "°C", "{:.2f}")
# Fehler des Zwei-Punkte-kA, wenn der Becher nicht vorgewärmt ist (Ausgleich schnell, Uhr ab Eingießen, theta_0 = 80 °C)
kk_true = kAB
th_gl = (C_K * TH_K0 + C_T0 * TH_U) / (C_K + C_T0)
th10_nv = TH_U + (th_gl - TH_U) * math.exp(-kk_true * T_MESS / (C_K + C_T0))
kA_falsch = -C_K / T_MESS * math.log((th10_nv - TH_U) / (TH_K0 - TH_U))
z("  dann nach 10 min (Becher eingeschlossen, kA 0,4440)", th10_nv, "°C", "{:.2f}")
z("  Zwei-Punkte-kA ohne Becher aus 80 °C und diesem Wert", kA_falsch, "W/K", "{:.4f}")
z("  Verhältnis zum richtigen kA ohne Becher (0,3402)", kA_falsch / kA0, "", "{:.2f}")
test("Nicht vorgewärmter Becher", "C_B = 255 J/K bei 20 °C, Kaffee 80 °C",
     f"Ausgleich auf {th_gl:.2f} °C (Absenkung {TH_K0 - th_gl:.2f} K)")
test("Füllhöhe", "kA_1 = 1,05 * kA0, kA_2 = kA0", f"theta_1 = {zwei(1.05 * kA0, kA0)['th1']:.2f} °C, Delta = {zwei(1.05 * kA0, kA0)['d']:.2f} K")

# ===========================================================================
kopf("Testfälle (Eingabe und erwartete Ausgabe)")
for i, (n, e, a) in enumerate(testfaelle, 1):
    print(f"  T{i:02d} {n}")
    print(f"      Eingabe: {e}")
    print(f"      erwartet: {a}")
