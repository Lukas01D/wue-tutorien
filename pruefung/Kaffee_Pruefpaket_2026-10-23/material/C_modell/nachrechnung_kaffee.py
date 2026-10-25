# -*- coding: utf-8 -*-
"""
Nachrechnung Kaffee-Aufgabe: Milch sofort oder erst nach 60 Minuten?
Tutorien Wärmeübertragung, Lehrstuhl für Fluidverfahrenstechnik (FVT), Universität Paderborn
Modell und Arbeitswerte: kaffee_modell.py (Quellen dort und in der Lösung).
Erstellt mit KI-Unterstützung (Claude, Anthropic). Ausführen: python3 nachrechnung_kaffee.py
"""
import math
from kaffee_modell import P, rechne, nichtlinear

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
print("\nf) nichtlineare Wärmeabgabe, angepasst an dieselbe Messung")
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
s60 = rechne(dict(P, th_M=60.0))
print(f"   Milch 60 °C (warmer Milchschaum): theta_1 = {s60['T1']-K_:5.2f} °C, theta_2 = {s60['T2']-K_:5.2f} °C, Unterschied {s60['dT']:5.2f} K")
# allgemeine Prüfung
ok = True
for rr in (0.5, 0.8, 0.95):
    for x in (0.1, 1.0, 3.0):
        for thM in (-30.0, -10.0, 0.0):
            th0 = 60.0
            d = rr * th0 * (math.exp(-rr * x) - math.exp(-x)) + (1 - rr) * thM * (math.exp(-rr * x) - 1)
            ok = ok and d > 0
print("\nAllgemeine Prüfung (Tasse 2 immer kälter, wenn die Milch nicht wärmer als der Raum ist):", ok)
