# -*- coding: utf-8 -*-
"""Nachrechnung der Prüferzahlen durch die Koordination (eigenes Skript, lineares Modell)."""
import math
from kaffee_modell import P, rechne, becher, nichtlinear

K = 273.15
r = rechne(P)
C_K, C_M, C_G, kA = r["C_K"], r["C_M"], r["C_G"], r["kA"]
Tu, TK0, TM = r["T_U"], r["T_K0"], r["T_M"]
ln_m = r["ln_mess"]


def lauf(t_end=3600.0, C_T=0.0, kA1=None, kA2=None, thM1=5.0, thM2=None, thK0=80.0,
         thmess=67.0, thU=20.0, m_M=None, kAfaktor1=1.0, kAfaktor2=1.0):
    """Tasse 1: Milch sofort; Tasse 2: Milch nach t_end. kA aus Messung (Tasse 2 ohne Milch)."""
    thM2 = thM1 if thM2 is None else thM2
    mM = r["m_M"] if m_M is None else m_M
    CM = mM * P["cp_M"]
    CKT = C_K + C_T
    CGT = CKT + CM
    T_U = thU + K
    T_K0 = thK0 + K
    lnm = math.log((thmess + K - T_U) / (T_K0 - T_U))
    kAc = -CKT / P["t_mess"] * lnm
    k1 = (kA1 if kA1 else kAc) * kAfaktor1
    k2 = (kA2 if kA2 else kAc) * kAfaktor2
    T10 = (CKT * T_K0 + CM * (thM1 + K)) / CGT
    T1 = T_U + (T10 - T_U) * math.exp(-k1 * t_end / CGT)
    T2K = T_U + (T_K0 - T_U) * math.exp(-k2 * t_end / CKT)
    T2 = (CKT * T2K + CM * (thM2 + K)) / CGT
    return T1 - K, T2 - K, T1 - T2, kAc, T2K - K


def p(txt, *v):
    print(f"{txt:60s}", "  ".join(f"{x:.3f}" if isinstance(x, float) else str(x) for x in v))


print("== Grundfall")
p("a) theta_1,0", r["T1_0"] - K)
p("c) kA, tau_K, tau_G [min]", kA, r["tau_K"] / 60, r["tau_G"] / 60)
p("d) th1, th2, diff", *lauf()[:3])
p("e) Q1, Q2 [kJ], (Q2-Q1)/C_G", r["Q1"] / 1e3, r["Q2"] / 1e3, (r["Q2"] - r["Q1"]) / C_G)
p("Wärmestrom t=0 Tasse 1/2 [W]", r["Qdot1_0"], r["Qdot2_0"])
p("Schnitt [min]", r["t_schnitt"] / 60)
b = becher()
p("f) kA, th1, th2, diff", b["kA"], b["T1"] - K, b["T2"] - K, b["dT"])
p("g) Schaum 60 °C: th1, th2, diff", *lauf(thM1=60.0)[:3])
p("Kipppunkt th_M", r["th_M_gleich"])

print("\n== Prof/Tech/Rech: kA-Faktor in Tasse 1")
for f in (0.944, 0.90, 0.80):
    p(f"g) kA1*{f}: th1, th2, diff", *lauf(thM1=60.0, kAfaktor1=f)[:3])


def kipp_faktor(**kw):
    lo, hi = 0.5, 2.0
    sgn = lambda f: lauf(kAfaktor1=f, **kw)[2]
    s_lo = sgn(lo)
    for _ in range(80):
        mid = (lo + hi) / 2
        if (sgn(mid) > 0) == (s_lo > 0):
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


p("g) kA1-Faktor für Gleichstand", kipp_faktor(thM1=60.0))
p("d) kA1-Faktor für Gleichstand ohne Becher", kipp_faktor())
p("d) kA1-Faktor für Gleichstand mit Becher", kipp_faktor(C_T=255.0))
for f in (1.03, 1.05, 1.10, 1.15):
    p(f"d) kA1*{f}: diff", lauf(kAfaktor1=f)[2])
p("d) mit Becher kA1*1.05: diff", lauf(C_T=255.0, kAfaktor1=1.05)[2])

print("\n== Kipppunkt (h1) bei kA-Faktor Tasse 1")


def kipp_thM(**kw):
    lo, hi = -50.0, 200.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if lauf(thM1=mid, **kw)[2] > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


for f in (0.95, 1.0, 1.05):
    p(f"Kipppunkt kA1*{f}", kipp_thM(kAfaktor1=f))
p("Kipppunkt mit Becher", kipp_thM(C_T=255.0))
for t in (30, 40, 60):
    p(f"Kipppunkt bei t_end={t} min", kipp_thM(t_end=t * 60.0))
for mg in (5e-3, 79e-3):
    p(f"Kipppunkt Milch {mg*1e3:.0f} g", kipp_thM(m_M=mg))

print("\n== Tech5: Empfindlichkeit")
for tm in (66.0, 68.0, 64.0, 70.0):
    o = lauf(thmess=tm)
    p(f"Messung {tm}: th1, th2, diff, kA/kA0", o[0], o[1], o[2], o[3] / kA)
for tk in (79.0, 81.0, 85.0):
    p(f"Start {tk}: diff", lauf(thK0=tk)[2])
for tu in (18.0, 22.0):
    p(f"Raum {tu}: diff", lauf(thU=tu)[2])
for ml in (25, 35, 40):
    p(f"Milch {ml} ml: diff", lauf(m_M=ml * 1.03e-3)[2])
p("Milch 7 °C: diff", lauf(thM1=7.0)[2])
p("Milch 20 °C (beide): diff", lauf(thM1=20.0)[2])
p("Rech: Milch 5 g / 79 g: diff", lauf(m_M=5e-3)[2], lauf(m_M=79e-3)[2])
p("Stud8: ±5 ml Milch -> th2 (Becher-Modell)", lauf(C_T=255.0, m_M=25*1.03e-3)[1], lauf(C_T=255.0)[1],
  lauf(C_T=255.0, m_M=35*1.03e-3)[1])
for m_B, c_B in ((0.25, 800.0), (0.40, 1080.0), (0.25, 1080.0), (0.40, 800.0)):
    p(f"Rech8: Becher {m_B} kg, {c_B}: diff", lauf(C_T=m_B * c_B)[2])
CM377 = r["m_M"] * 3770.0
# c_p Milch 3,77
T10 = (C_K * TK0 + CM377 * TM) / (C_K + CM377)
T1 = Tu + (T10 - Tu) * math.exp(-kA * 3600 / (C_K + CM377))
T2 = (C_K * (r["T2_K"]) + CM377 * TM) / (C_K + CM377)
p("Rech8: c_p,M = 3,77: diff", T1 - T2)

print("\n== Versuch (Becher 255 J/K)")
for t in (30, 40, 60):
    o12 = lauf(t_end=t * 60.0, C_T=255.0)
    o13 = lauf(t_end=t * 60.0, C_T=255.0, thM2=20.0)
    p(f"t={t}: B1, B2, B1-B2, B1-B3", o12[0], o12[1], o12[2], o12[0] - o13[1])
o = lauf(t_end=2400.0)
p("ohne Becher 40 min: th1, th2, diff", o[0], o[1], o[2])
# Abkühlrate bei 40 °C mit Becher
kAb = b["kA"]
p("Abkühlrate bei 40 °C mit Becher [K/min] Gemisch, schwarz",
  kAb * 20 / (C_G + 255) * 60, kAb * 20 / (C_K + 255) * 60)
p("Abkühlrate bei 34 °C ohne Becher, Tasse 1 [K/min]", kA * 14.05 / C_G * 60)
# Becher 1 bei 10 min
T10b = ((C_K + 255) * TK0 + C_M * TM) / (C_G + 255)
for f in (1.0, 1.15):
    p(f"Did6: Becher 1 bei 10 min, kA*{f}", Tu - K + (T10b - Tu) * math.exp(-kAb * f * 600 / (C_G + 255)))
# 50 ml Milch im Versuch
for thM3 in (13.0, 20.0):
    o12 = lauf(C_T=255.0, m_M=51.5e-3)
    o13 = lauf(C_T=255.0, m_M=51.5e-3, thM2=thM3)
    p(f"Tech4: 50 ml, B1-B2, B1-B3 (Glas {thM3})", o12[2], o12[0] - o13[1])
for thM2 in (7.0, 10.0):
    for thM3 in (13.0, 17.0):
        o12 = lauf(C_T=255.0, thM2=thM2)
        o13 = lauf(C_T=255.0, thM2=thM3)
        p(f"Tech4: Kühltasche {thM2}, Glas {thM3}: B1-B2, B1-B3, B3-B2", o12[2], o12[0] - o13[1], o13[1] - o12[1])

print("\n== Rech2: tau-Varianten (mit Becher 255 J/K)")
for tau in (20, 30, 41, 75):
    thm = 20 + 60 * math.exp(-10 / tau)
    o60 = lauf(C_T=255.0, thmess=thm)
    o30 = lauf(t_end=1800.0, C_T=255.0, thmess=thm)
    o3 = lauf(C_T=255.0, thmess=thm, thM2=20.0)
    p(f"tau={tau}: th(10), B1-B2 60, B1-B2 30, B1-B3", thm, o60[2], o30[2], o60[0] - o3[1])

print("\n== Verdunstete Masse, Tassenwärmer, Zeitkonstante")
for dh in (2400e3, 2380e3):
    p(f"m_v = 0,5 Q2 / {dh/1e3:.0f} kJ/kg [g], Anteil", 0.5 * r["Q2"] / dh * 1e3, 0.5 * r["Q2"] / dh / r["m_K"])
p("m_v Tasse 1 [g]", 0.5 * r["Q1"] / 2380e3 * 1e3)
mv = 0.5 * r["Q2"] / 2380e3
CKv = (r["m_K"] - mv) * P["cp_K"]
p("Tasse 2 mit verdunsteter Masse: th2", ((CKv * r["T2_K"] + C_M * TM) / (CKv + C_M)) - K)
p("Tassenwärmer P ohne/mit Becher [W], Verhältnis", kA * 40, kAb * 40, kA / kAb)
p("tau mit Becher [min]", (C_K + 255) / kAb / 60)
p("theta(tau)", 20 + 60 * math.exp(-1))
A = math.pi * 0.08 * 0.0398 + 2 * math.pi * 0.04 ** 2
p("Füllhöhe 200/230 ml [cm]", 200e-6 / (math.pi * 0.04 ** 2) * 100, 230e-6 / (math.pi * 0.04 ** 2) * 100)
A2 = math.pi * 0.08 * 230e-6 / (math.pi * 0.04 ** 2) + 2 * math.pi * 0.04 ** 2
p("Fläche 200/230 ml [cm²], Zuwachs", A * 1e4, A2 * 1e4, A2 / A - 1)
p("k = kA/A ohne/mit Becher [W/m²K]", kA / A, kAb / A)
p("(47/60)^6", (47 / 60) ** 6)

print("\n== Zerlegung (Kaffee-Effekt, Milch-Effekt)")


def zerlegen(C_T=0.0, thM=5.0):
    CKT, CGT = C_K + C_T, C_G + C_T
    kAx = -CKT / P["t_mess"] * ln_m
    eG, eK = math.exp(-kAx * 3600 / CGT), math.exp(-kAx * 3600 / CKT)
    T_M = thM + K
    kaffee = CKT / CGT * (TK0 - Tu) * (eG - eK)
    milch = C_M / CGT * (T_M - Tu) * (eG - 1)
    return kaffee, milch, kaffee + milch, eG


p("ohne Becher: Kaffee, Milch, Summe", *zerlegen()[:3])
p("ohne Becher Schaum: Kaffee, Milch, Summe", *zerlegen(thM=60.0)[:3])
p("mit Becher: Kaffee, Milch, Summe, e_G", *zerlegen(C_T=255.0))

print("\n== Stud5: f ohne Becher im Mischen")
CKT = C_K + 255.0
T10 = r["T1_0"]
CGT_Becher = C_G + 255.0
# Tasse 1: Mischtemperatur aus a) übernommen, dann mit Becher abkühlen
T1 = Tu + (T10 - Tu) * math.exp(-kAb * 3600 / CGT_Becher)
# Tasse 2: Kaffee mit Becher abkühlen, dann nur Kaffee mit Milch mischen
T2 = (C_K * r["T2_K"] + C_M * TM) / C_G
p("th1, th2 (Becher nicht mitgemischt)", T1 - K, T2 - K)
p("th1,0 mit Becher", ((CKT * TK0 + C_M * TM) / CGT_Becher) - K)
p("Stud12: Q2 mit Kaffee+Milch [kJ]", C_G * (TK0 - r["T2_K"]) / 1e3)
p("Stud12: kA mit t in min", -C_K / 10 * ln_m)

print("\n== h(2)")
p("Milch nimmt höchstens auf [kJ]", C_M * 15 / 1e3)
p("Q2-Q1 [kJ]", (r["Q2"] - r["Q1"]) / 1e3)
p("Mindestunterschied (3,69-1,83)/C_G", (r["Q2"] - r["Q1"] - C_M * 15) / C_G)

print("\n== Did11: Unterschied bei Zugabe zum Zeitpunkt t (Maximum)")
best = (0, -1)
for tm in range(1, 121):
    o = lauf(t_end=tm * 60.0)
    if o[2] > best[1]:
        best = (tm, o[2])
p("Maximum bei min, Wert", best[0], best[1])

print("\n== nichtlinear n = 4/3")
T1, T2 = nichtlinear(4 / 3)
p("n=4/3 ohne Becher: th1, th2", T1 - K, T2 - K)
