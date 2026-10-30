# -*- coding: utf-8 -*-
"""
Nachrechnung Kaffee-Aufgabe: Milch sofort oder erst nach 60 Minuten?
Tutorien Wärmeübertragung, Lehrstuhl für Fluidverfahrenstechnik (FVT), Universität Paderborn
Modell und Arbeitswerte: kaffee_modell.py (Quellen dort und in der Lösung).
Erstellt mit KI-Unterstützung (Claude, Anthropic). Ausführen: python3 nachrechnung_kaffee.py
"""
import math
from kaffee_modell import P, rechne, nichtlinear, zwei_tassen, gleichstand

K = 273.15
r = rechne(P)


def z(text, wert, einheit="", fmt=".4g"):
    print(f"{text:66s} {wert:{fmt}} {einheit}")


print("Arbeitswerte:", {k: v for k, v in P.items()})
z("m_K", r["m_K"], "kg"); z("m_M", r["m_M"], "kg")
z("C_K = m_K c_p,K", r["C_K"], "J/K"); z("C_M = m_M c_p,M", r["C_M"], "J/K"); z("C_K + C_M", r["C_G"], "J/K")
print("\na) Mischtemperatur Tasse 1")
z("T_1,0", r["T1_0"], "K", ".2f"); z("theta_1,0", r["T1_0"] - K, "°C", ".2f")
print("\nc) kA aus der Messung")
z("ln((T - T_u)/(T_K0 - T_u))", r["ln_mess"], "", ".5f")
z("kA", r["kA"], "W/K", ".4f")
z("Zeitkonstante ohne Milch", r["tau_K"] / 60, "min", ".1f"); z("Zeitkonstante mit Milch", r["tau_G"] / 60, "min", ".1f")
print("\nd) Temperaturen nach 60 min")
z("exp(-kA t/(C_K + C_M))", r["e_G"], "", ".4f"); z("T_1", r["T1"], "K", ".2f"); z("theta_1", r["T1"] - K, "°C", ".2f")
z("exp(-kA t/C_K)", r["e_K"], "", ".4f"); z("T_K(60 min)", r["T2_K"], "K", ".2f"); z("theta_K(60 min)", r["T2_K"] - K, "°C", ".2f")
z("T_2", r["T2"], "K", ".2f"); z("theta_2", r["T2"] - K, "°C", ".2f")
z("Unterschied theta_1 - theta_2", r["dT"], "K", ".2f")
print("\ne) abgegebene Wärme")
z("Q_1", r["Q1"] / 1e3, "kJ", ".2f"); z("Q_2", r["Q2"] / 1e3, "kJ", ".2f")
z("(Q_2 - Q_1)/(C_K + C_M)", (r["Q2"] - r["Q1"]) / r["C_G"], "K", ".2f")
z("Wärmestrom am Anfang Tasse 1", r["Qdot1_0"], "W", ".2f"); z("Wärmestrom am Anfang Tasse 2", r["Qdot2_0"], "W", ".2f")
z("Kaffee ohne Milch wird kälter als das Gemisch ab", r["t_schnitt"] / 60, "min", ".1f")
print("\nZusatzprüfung: temperaturabhängige Wärmeabgabe c (T - T_u)^n, an dieselbe Messung angepasst (exakt integriert)")
for n in (1.0, 4 / 3, 1.6):
    T1, T2 = nichtlinear(n)
    print(f"   n = {n:4.2f}: theta_1 = {T1-K:5.2f} °C, theta_2 = {T2-K:5.2f} °C, Unterschied {T1-T2:4.2f} K")
print("\nEmpfindlichkeit")
for name, aend in (("Milch 7 °C", dict(th_M=7.0)), ("Milch 20 °C (Raumtemperatur)", dict(th_M=20.0)),
                   ("Milch 40 ml", dict(V_M=40e-6)), ("Kaffee 85 °C", dict(th_K0=85.0)),
                   ("Messung 64 °C (schneller)", dict(th_mess=64.0)), ("Messung 70 °C (langsamer)", dict(th_mess=70.0))):
    q = dict(P); q.update(aend); s = rechne(q)
    print(f"   {name:30s}: theta_1 = {s['T1']-K:5.2f} °C, theta_2 = {s['T2']-K:5.2f} °C, Unterschied {s['dT']:4.2f} K")
# Becher mit Wärmekapazität (300 g, c = 850 J/(kg K)), immer so warm wie der Inhalt
from kaffee_modell import becher
K_ = 273.15
b = becher()
print(f"   Becher 300 g, kA neu aus derselben Messung ({b['kA']:.3f} W/K): theta_1 = {b['T1']-K_:5.2f} °C, theta_2 = {b['T2']-K_:5.2f} °C, Unterschied {b['dT']:4.2f} K")
b0 = becher(kA_neu=False)
print(f"   Becher 300 g, gleiches kA (passt nicht mehr zur Messung):  theta_1 = {b0['T1']-K_:5.2f} °C, theta_2 = {b0['T2']-K_:5.2f} °C, Unterschied {b0['dT']:4.2f} K")
z("   Anteil Becher an der Wärmekapazität des Kaffees", b["anteil"] * 100, "%", ".0f")
z("Milchtemperatur, bei der beide Tassen gleich warm wären", r["th_M_gleich"], "°C", ".1f")
s60 = rechne(dict(P, th_M=P["th_Mh"]))
print(f"   f) erwärmte Milch {P['th_Mh']:.0f} °C: theta_1 = {s60['T1']-K_:5.2f} °C, theta_2 = {s60['T2']-K_:5.2f} °C, Unterschied {s60['dT']:5.2f} K")
# allgemeine Prüfung
ok = True
for rr in (0.5, 0.8, 0.95):
    for x in (0.1, 1.0, 3.0):
        for thM in (-30.0, -10.0, 0.0):
            th0 = 60.0
            d = rr * th0 * (math.exp(-rr * x) - math.exp(-x)) + (1 - rr) * thM * (math.exp(-rr * x) - 1)
            ok = ok and d > 0
print("\nAllgemeine Prüfung (Tasse 2 immer kälter, wenn die Milch nicht wärmer als der Raum ist):", ok)

# ---------------------------------------------------------------- Ergänzungen nach der Prüfung (Oktober 2026)
C_B = P["m_B"] * P["c_B"]
print("\ng) kA als Modellparameter (Becher)")
z("kA mit Becher / kA ohne Becher", b["kA"] / r["kA"], "", ".3f")
z("Zeitkonstante mit Becher (C_K + C_B)/kA", (r["C_K"] + C_B) / b["kA"] / 60, "min", ".1f")
z("Anteil Becher an C_K", C_B / r["C_K"] * 100, "%", ".1f")
eGB = math.exp(-b["kA"] * P["t_end"] / (r["C_G"] + C_B)); eKB = math.exp(-b["kA"] * P["t_end"] / (r["C_K"] + C_B))
kaf = lambda C_T, eG, eK, thM: ((r["C_K"] + C_T) * (r["T_K0"] - r["T_U"]) * (eG - eK) / (r["C_G"] + C_T),
                                r["C_M"] * (thM + K - r["T_U"]) * (eG - 1) / (r["C_G"] + C_T))
k0, m0 = kaf(0.0, r["e_G"], r["e_K"], P["th_M"]); kB, mB = kaf(C_B, eGB, eKB, P["th_M"])
z("Kaffee-Effekt ohne / mit Becher", k0, "K", ".2f"); z("", kB, "K", ".2f")
z("Milch-Effekt ohne / mit Becher", m0, "K", ".2f"); z("", mB, "K", ".2f")
z("Milch-Effekt mit erwärmter Milch (ohne Becher)", kaf(0.0, r["e_G"], r["e_K"], P["th_Mh"])[1], "K", ".2f")
z("Typischer Fehler f: Becher nicht mitgemischt, theta_1",
  r["T_U"] - K + (r["T1_0"] - r["T_U"]) * math.exp(-b["kA"] * P["t_end"] / (r["C_G"] + C_B)), "°C", ".2f")
z("Typischer Fehler f: Becher nicht mitgemischt, theta_2", r["T2"] - K, "°C", ".2f")

print("\nc) und d) Robustheit und Plausibilität")
for tm in (66.0, 68.0):
    q = rechne(dict(P, th_mess=tm))
    print(f"   Messung {tm:.0f} °C: kA {q['kA']:.4f} W/K ({(q['kA']/r['kA']-1)*100:+.1f} %), theta_1 = {q['T1']-K:5.2f} °C, theta_2 = {q['T2']-K:5.2f} °C, Unterschied {q['dT']:4.2f} K")
z("theta nach der Zeit tau (schwarzer Kaffee)", P["th_U"] + (P["th_K0"] - P["th_U"]) * math.exp(-1), "°C", ".1f")
d_B = 0.08; h0 = P["V_K"] / (math.pi * d_B**2 / 4); hM = (P["V_K"] + P["V_M"]) / (math.pi * d_B**2 / 4)
A0 = math.pi * d_B * h0 + 2 * math.pi * d_B**2 / 4; AM = math.pi * d_B * hM + 2 * math.pi * d_B**2 / 4
z("Becher 8 cm: Füllhöhe ohne / mit Milch", h0 * 100, "cm", ".1f"); z("", hM * 100, "cm", ".1f")
z("Fläche (Wand, Boden, Oberfläche) ohne Milch", A0 * 1e4, "cm²", ".0f")
z("Zuwachs der Fläche mit Milch", (AM / A0 - 1) * 100, "%", ".1f")
z("kA/A ohne Becher", r["kA"] / A0, "W/(m² K)", ".0f")
for f in (1.03, 1.05, 1.10):
    z(f"Unterschied, wenn kA mit Milch um {(f-1)*100:.0f} % größer ist", zwei_tassen(kA1_faktor=f)["dT"], "K", ".2f")
z("kA-Faktor in Tasse 1, bei dem beide gleich warm sind (ohne Becher)", gleichstand(lambda f: zwei_tassen(kA1_faktor=f)["dT"], 1.0, 2.0), "", ".3f")
z("dto. mit Becher", gleichstand(lambda f: zwei_tassen(C_T=C_B, kA1_faktor=f)["dT"], 1.0, 2.0), "", ".3f")
z("Größter Unterschied bei Zugabe nach (min)", max(range(1, 121), key=lambda m: zwei_tassen(t_end=m * 60.0)["dT"]), "min", ".0f")

print("\nf) und Zusatzfrage: Grenzwerte")
z("f: Tasse 1 mit erwärmter Milch kA um 5,6 % kleiner (Schaumschicht), Unterschied",
  zwei_tassen(th_M1=P["th_Mh"], kA1_faktor=0.944)["dT"], "K", ".2f")
z("f: Tasse 1 mit kA um 10 % kleiner, Unterschied", zwei_tassen(th_M1=P["th_Mh"], kA1_faktor=0.90)["dT"], "K", ".2f")
z("f: späte Portion muss mindestens so warm sein", gleichstand(lambda t2: zwei_tassen(th_M1=P["th_Mh"], th_M2=t2)["dT"]), "°C", ".1f")
for f in (1.05, 0.95):
    z(f"Zusatzfrage (1): Kipppunkt bei kA in Tasse 1 x {f}", gleichstand(lambda tm: zwei_tassen(th_M1=tm, kA1_faktor=f)["dT"]), "°C", ".1f")
z("Zusatzfrage (1): Kipppunkt mit Exponent 4/3", gleichstand(lambda tm: (lambda a: a[0] - a[1])(nichtlinear(4 / 3, dict(P, th_M=tm))), 0.0, 100.0), "°C", ".1f")
z("Zusatzfrage (2): nur die späte Portion erwärmt, Gleichstand bei", gleichstand(lambda t2: zwei_tassen(th_M2=t2)["dT"]), "°C", ".1f")
z("Verdunstete Masse in Tasse 2 höchstens (Hälfte von Q_2)", 0.5 * r["Q2"] / P["dh_v"] * 1e3, "g", ".1f")
z("dto. Anteil an m_K", 0.5 * r["Q2"] / P["dh_v"] / r["m_K"] * 100, "%", ".1f")
z("Tassenwärmer: Leistung für 60 °C mit kA aus c", r["kA"] * (60.0 - P["th_U"]), "W", ".1f")
z("Tassenwärmer: Leistung für 60 °C mit kA aus g", b["kA"] * (60.0 - P["th_U"]), "W", ".1f")

print("\nVersuch: vorgewärmte Becher, Vorhersage nach 40 min")
for t_min in (30, 40, 60):
    v = zwei_tassen(C_T=C_B, t_end=t_min * 60.0); v3 = zwei_tassen(C_T=C_B, th_M2=P["th_U"], t_end=t_min * 60.0)
    print(f"   {t_min} min mit Becher: Becher 1 {v['th1']:5.2f} °C, Becher 2 {v['th2']:5.2f} °C, 1 - 2 {v['dT']:4.2f} K, 1 - 3 (Milch 20 °C) {v['T1']-v3['T2']:4.2f} K")
v = zwei_tassen(t_end=2400.0)
print(f"   40 min, Modell aus d (ohne Becher): Becher 1 - 2 {v['dT']:4.2f} K")
for f in (1.03, 1.05):
    v = zwei_tassen(C_T=C_B, t_end=2400.0, kA1_faktor=f)
    print(f"   40 min mit Becher, kA mit Milch {(f-1)*100:.0f} % größer: Becher 1 - 2 {v['dT']:4.2f} K")
z("Abkürzung: Anteil der Übertemperatur nach 40 min, (47/60)^4", ((P["th_mess"] - P["th_U"]) / (P["th_K0"] - P["th_U"])) ** 4, "", ".4f")
z("Abkühlrate bei 40 °C mit Becher (Gemisch)", b["kA"] * 20.0 / (r["C_G"] + C_B) * 60, "K/min", ".2f")

