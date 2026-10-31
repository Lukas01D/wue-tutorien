# -*- coding: utf-8 -*-
"""Tutorium 8 (Wärmeübertrager und Verdampfer): Nachrechnung aller Zahlen aus teile/t8.md.

Arbeitswerte aus der Ideensammlung „Leitaufgaben aus Klima und Erde“ (Abschnitt 4.8, Skript
nachrechnung_leitphaenomene.py, Abschnitt T8) und aus „Aufgabenideen Ozean und Atmosphäre“
(Aufgabe C, Skript nachrechnung_ozean_atmosphaere.py). Die Formeln sind hier nachgebaut, weil die
beiden Ausgangsskripte beim Import alles ausgeben; die Kernzahlen der Ausgangsskripte stehen zum
Vergleich in der Ausgabe.

Aufruf: python3 t8_rechnung.py
Ergebnis: t8_rechnung_ausgabe.txt (Name, Wert, Einheit, Schreibweise im Aufgabentext) und eine
Prüfung, ob jede Ergebniszahl in genau dieser Schreibweise in ../teile/t8.md steht.
"""
import math
import os
import sys as _sys, os as _os
_sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), "build"))
from indizes_aufrecht import ohne_mathrm   # Schreibweise prüfen unabhängig davon, ob Indizes aufrecht oder kursiv stehen

HIER = os.path.dirname(os.path.abspath(__file__))
TEIL = os.path.join(os.path.dirname(HIER), "teile", "t8.md")
K0 = 273.15

ZEILEN = []      # (Name, Wert, Einheit, Schreibweise im Markdown oder None)
ABWEICHUNG = []  # Vergleich mit den Ausgangsskripten


def de(x, n=2):
    """Zahl mit Dezimalkomma für Mathe im Markdown: 0{,}526"""
    return f"{x:.{n}f}".replace(".", "{,}")


def aus(name, wert, einheit="", md=None):
    ZEILEN.append((name, wert, einheit, md))
    return wert


def vergleich(name, neu, quelle, text_quelle):
    ABWEICHUNG.append((name, neu, quelle, text_quelle))


# =============================================================================
# Aufgabe 1: Sole-Wasser-Wärmepumpe mit Erdwärmesonde (Ideensammlung 4.8)
# =============================================================================
Q_H = 8000.0          # W Heizleistung
COP = 4.0             # Leistungszahl
JAZ = 4.3             # Jahresarbeitszahl erdgekoppelter Wärmepumpen (Fraunhofer ISE, 2025)
c_S = 3800.0          # J/(kg K) Sole (Wasser-Glykol)
rho_S = 1040.0        # kg/m³
nu_S = 4.0e-6         # m²/s
th_ein, th_aus = -1.0, 2.0   # °C Sole in die Sonde / aus der Sonde (= Verdampfer aus / ein)
th_B = 11.0           # °C Boden
th_V, th_K = -6.0, 40.0      # °C Verdampfung, Kondensation
L = 100.0             # m Sondenlänge
d_i = 0.026           # m Rohrinnendurchmesser
k1, k2 = 1000.0, 2000.0      # W/(m² K) Verdampfer
q_E = 0.065           # W/m² Wärmestromdichte aus dem Erdinneren (Kontinente, Pollack et al. 1993)
e_el = 344.0          # g/kWh Strommix 2025 (UBA, 23.03.2026), ohne Vorketten
e_gas = 202.0         # g/kWh Erdgas, Brennstoff (UBA 2024, Tabelle 4)
eta_G = 0.95          # Wirkungsgrad Gasheizung
q_richt = 60.0        # W/m Richtwert normales Festgestein (VDI 4640 Blatt 2, 2001)

# b) Energiebilanz und Solemassenstrom
P_el = aus("b) elektrische Leistung P_el = Q_H/COP", Q_H / COP / 1e3, "kW", r"P_{\mathrm{el}} = " + de(Q_H / COP / 1e3) + r"\,\mathrm{kW}")
Q_V = Q_H - Q_H / COP
aus("b) Wärmestrom aus der Sole Q_V = Q_H - P_el", Q_V / 1e3, "kW", r"\dot{Q}_{\mathrm{V}} = " + de(Q_V / 1e3) + r"\,\mathrm{kW}")
m_S = Q_V / (c_S * (th_aus - th_ein))
aus("b) Solemassenstrom m_S", m_S, "kg/s", r"\dot{m}_{\mathrm{S}} = " + de(m_S, 3) + r"\,\mathrm{kg/s}")
aus("   (Volumenstrom, nur zur Information)", m_S / rho_S * 3600, "m³/h")
C_S = m_S * c_S
aus("   Wärmekapazitätsstrom der Sole C_S", C_S, "W/K")
vergleich("Solemassenstrom", m_S, 0.526, "0,526 kg/s (1,82 m³/h)")

# c) Strömung im Sondenrohr
A_R = math.pi / 4 * d_i**2
w1 = m_S / (rho_S * A_R)
w2 = w1 / 2
Re1, Re2 = w1 * d_i / nu_S, w2 * d_i / nu_S
aus("c) (1) ein Rohrkreis: w", w1, "m/s", r"w = " + de(w1) + r"\,\mathrm{m/s}")
aus("c) (1) Re (Schreibweise auf 100 gerundet)", Re1, "", r"Re = " + f"{round(Re1, -2):.0f}")
aus("c) (2) zwei Rohrkreise: w", w2, "m/s", r"w = " + de(w2) + r"\,\mathrm{m/s}")
aus("c) (2) Re (Schreibweise auf 100 gerundet)", Re2, "", r"Re = " + f"{round(Re2, -2):.0f}")
vergleich("Re ein Kreis / zwei Kreise", Re1, 6196, "6196 / 3098")

# d) Verdampfer mit Delta T_ln
dT1, dT2 = th_aus - th_V, th_ein - th_V
dT_ln = (dT1 - dT2) / math.log(dT1 / dT2)
kA_V = Q_V / dT_ln
aus("d) Delta T_ln Verdampfer", dT_ln, "K", r"\Delta T_{\mathrm{ln}} = " + de(dT_ln) + r"\,\mathrm{K}")
aus("d) (kA)_V = Q_V/Delta T_ln (Schreibweise ganzzahlig)", kA_V, "W/K", r"(kA)_{\mathrm{V}} = " + f"{kA_V:.0f}" + r"\,\mathrm{W/K}")
aus("d) Fläche bei k1 = 1000 W/(m² K)", kA_V / k1, "m²", r"A_{\mathrm{V}} = " + de(kA_V / k1) + r"\,\mathrm{m^2}")
aus("d) Fläche bei k2 = 2000 W/(m² K)", kA_V / k2, "m²", r"bzw. $" + de(kA_V / k2) + r"\,\mathrm{m^2}$")
vergleich("kA Verdampfer (Delta T_ln)", kA_V, 940, "940 W/K bei Delta T_ln = 6,38 K")

# e) Verdampfer mit eps-NTU, C* = 0
eps_V = (th_aus - th_ein) / (th_aus - th_V)
NTU_V = -math.log(1 - eps_V)
kA_V2 = NTU_V * C_S
aus("e) C* = C_min/C_max (Kältemittel siedet, C_max -> unendlich)", 0.0, "", r"C^* = 0")
aus("e) eps_V", eps_V, "", r"\varepsilon_{\mathrm{V}} = " + de(eps_V, 3))
aus("e) NTU_V", NTU_V, "", r"NTU_{\mathrm{V}} = " + de(NTU_V, 3))
aus("e) (kA)_V = NTU_V C_S", kA_V2, "W/K", r"(kA)_{\mathrm{V}} = " + f"{kA_V2:.0f}" + r"\,\mathrm{W/K}")
assert abs(kA_V2 - kA_V) < 1e-9, "beide Wege müssen dasselbe kA liefern"
aus("   Kontrolle: Unterschied der beiden Wege", kA_V2 - kA_V, "W/K")

# f) Erdwärmesonde als Wärmeübertrager, C* = 0
eps_So = (th_aus - th_ein) / (th_B - th_ein)
NTU_So = -math.log(1 - eps_So)
kA_So = NTU_So * C_S
aus("f) eps_Sonde", eps_So, "", r"\varepsilon_{\mathrm{Sonde}} = " + de(eps_So, 3))
aus("f) NTU_Sonde", NTU_So, "", r"NTU_{\mathrm{Sonde}} = " + de(NTU_So, 3))
aus("f) (kA)_Sonde (Schreibweise ganzzahlig)", kA_So, "W/K", r"(kA)_{\mathrm{Sonde}} = " + f"{kA_So:.0f}" + r"\,\mathrm{W/K}")
eps_halb = 1 - math.exp(-NTU_So / 2)          # nach der Hälfte des Strömungswegs (tiefster Punkt)
th_unten = th_ein + eps_halb * (th_B - th_ein)
anteil = (th_unten - th_ein) / (th_aus - th_ein)
aus("f) eps nach halbem Weg = 1 - exp(-NTU/2) = 1 - sqrt(1 - eps)", eps_halb, "")
aus("f) Soletemperatur am tiefsten Punkt", th_unten, "°C", r"\vartheta_{\mathrm{S,unten}} = " + de(th_unten) + r"\,\mathrm{°C}")
aus("f) Anteil von Q_V auf dem Weg nach unten", anteil * 100, "%",
    r"\dot{Q}_{\mathrm{unten}}/\dot{Q}_{\mathrm{V}} = " + de(anteil * 100, 1) + r"\,\%")
vergleich("kA Sonde", kA_So, 575, "eps 0,250, NTU 0,288, kA 575 W/K")

# g) Prüfen
q_L = Q_V / L
aus("g) (1) Entzugsleistung je Meter Q_V/L", q_L, "W/m", r"\dot{Q}_{\mathrm{V}}/L = " + f"{q_L:.0f}" + r"\,\mathrm{W/m}")
aus("   Richtwert VDI 4640 Blatt 2 (2001), normales Festgestein", q_richt, "W/m")
COP_C = (th_K + K0) / (th_K - th_V)
aus("g) (2) Carnot-Leistungszahl T_K/(T_K - T_V)", COP_C, "", r"COP_{\mathrm{C}} = " + de(COP_C))
aus("g) (2) COP/COP_C", COP / COP_C * 100, "%", r"COP/COP_{\mathrm{C}} = " + f"{COP / COP_C * 100:.0f}" + r"\,\%")
vergleich("Carnot-COP", COP_C, 6.8, "6,8; COP 4 sind 59 % davon")

# h) Reflektieren
A_geo = Q_V / q_E
aus("h) (1) Fläche für Q_V aus dem Erdwärmestrom", A_geo, "m²")
aus("h) (1) dieselbe Fläche in Hektar", A_geo / 1e4, "ha", r"A = " + de(A_geo / 1e4) + r"\,\mathrm{ha}")
e_WP = e_el / COP
e_WP_JAZ = e_el / JAZ
e_G = e_gas / eta_G
aus("h) (2) CO2 je kWh Wärme, Wärmepumpe mit COP 4", e_WP, "g/kWh", r"e_{\mathrm{WP}} = " + f"{e_WP:.0f}" + r"\,\mathrm{g/kWh}")
aus("h) (2) CO2 je kWh Wärme, Wärmepumpe mit JAZ 4,3", e_WP_JAZ, "g/kWh", r"(mit $JAZ$: $" + f"{e_WP_JAZ:.0f}" + r"\,\mathrm{g/kWh}$)")
aus("h) (2) CO2 je kWh Wärme, Gasheizung (eta 0,95)", e_G, "g/kWh", r"e_{\mathrm{Gas}} = " + f"{e_G:.0f}" + r"\,\mathrm{g/kWh}")
vergleich("CO2 Wärmepumpe / Gas", e_WP, 86, "86 g gegen 213 g (JAZ 4,3: 80 g)")
vergleich("Fläche Erdwärmestrom", A_geo / 1e4, 9.2, "9,2 ha")

# =============================================================================
# Aufgabe 2: Wer bringt die Wärme zum Pol? (Aufgabe C, Teile C1 bis C4)
# =============================================================================
rho_W, c_W = 1025.0, 3990.0        # Meerwasser
rho_L, c_L = 1.2, 1005.0           # Luft am Boden
p0, g = 101325.0, 9.81             # Pa, m/s² (das Ausgangsskript rechnet mit 9,80665)
f_Ozean = 0.71                     # Anteil des Ozeans an der Erdoberfläche
SV = 1e6                           # m³/s je Sverdrup
V_AMOC = 17.0 * SV                 # AMOC bei 26,5° N (Johns et al., 2023: 16,9 Sv)
Q_AMOC = 1.2e15                    # W, Wärmestrom der AMOC bei 26,5° N (Johns et al., 2023: 1,20 PW; wie Tutorium 5)
Q_A = 5.0e15                       # W, Atmosphäre bei 40° N (Fasullo & Trenberth, 2008: 5,1 PW bei 41° N)
dT_A = 20.0                        # K, warme Luft nach Norden, kältere zurück
dx = 0.005                         # kg/kg, mehr Wasserdampf in der warmen Luft
dh_v = 2.43e6                      # J/kg (NIST, 30 °C)
m_Hadley = 0.8e11                  # kg/s Hadley-Zelle Nordhalbkugel (Aufgabentext Aufgabe C)
U40 = 30700e3                      # m Umfang des 40. Breitengrads (gerundet wie im Aufgabentext)
H = 10e3                           # m Höhe der „Wand“
rho_m = 0.76                       # kg/m³ mittlere Dichte der unteren 10 km (gerundet wie im Aufgabentext)

# Tabellenwerte, die nach der Prüfung ergänzt wurden (Schreibweise wird gegen den Text geprüft)
aus("Tab. A2: Wärmestrom der AMOC (Tutorium 5)", Q_AMOC / 1e15, "PW", r"\dot{Q}_{\mathrm{AMOC}} = 1{,}2\,\mathrm{PW}")
aus("Tab. A2: Erdbeschleunigung g (damit rechnet Teil a)", g, "m/s²", r"g = " + de(g) + r"\,\mathrm{m/s^2}")

# a) C1
rc_W, rc_L = rho_W * c_W, rho_L * c_L
aus("a) rho c_p Meerwasser", rc_W / 1e6, "MJ/(m³ K)")
aus("a) rho c_p Luft", rc_L / 1e3, "kJ/(m³ K)")
aus("a) Verhältnis (Schreibweise auf 10 gerundet)", rc_W / rc_L, "",
    r"(\rho\,c_p)_{\mathrm{W}}/(\rho\,c_p)_{\mathrm{L}} = " + f"{round(rc_W / rc_L, -1):.0f}")
m_saeule = p0 / g
h_1 = m_saeule * c_L / rc_W
h_2 = h_1 / f_Ozean
aus("a) Masse der Luftsäule p0/g", m_saeule, "kg/m²")
aus("a) Wasserschicht mit derselben Wärmekapazität wie die Luftsäule", h_1, "m", r"h_{\mathrm{W}} = " + de(h_1) + r"\,\mathrm{m}")
aus("a) Ozeanschicht für die ganze Atmosphäre (71 % Ozean)", h_2, "m", r"h_{\mathrm{O}} = " + de(h_2) + r"\,\mathrm{m}")
aus("a) 3 m Ozean im Verhältnis zur ganzen Atmosphäre", 3.0 / h_2 * 100, "%", r"3 m Ozean: $" + f"{3.0 / h_2 * 100:.0f}" + r"\,\%")
aus("   (nur zur Information) h_O mit g = 9,80665 m/s²", p0 / 9.80665 * c_L / rc_W / f_Ozean, "m")
vergleich("Ozeanschicht ganze Atmosphäre", h_2, 3.58, "3,58 m (mit g = 9,80665; Kernzahl 3,6 m)")

# b) C2
m_L = Q_A / (c_L * dT_A)
V_L = m_L / rho_L
m_AMOC = rho_W * V_AMOC
aus("b) Luftmassenstrom nur fühlbar", m_L, "kg/s", r"\dot{m}_{\mathrm{L}} = " + de(m_L / 1e11) + r"\cdot 10^{11}\,\mathrm{kg/s}")
aus("b) Volumenstrom (rho 1,2) in Sv", V_L / SV, "Sv", r"\dot{V}_{\mathrm{L}} = " + de(V_L / SV / 1e5) + r"\cdot 10^{5}\,\mathrm{Sv}")
aus("b) Massenstrom der AMOC", m_AMOC, "kg/s")
aus("b) Volumenstrom Luft / AMOC (Schreibweise auf 100 gerundet)", V_L / V_AMOC, "",
    r"\dot{V}_{\mathrm{L}}/\dot{V}_{\mathrm{AMOC}} = " + f"{round(V_L / V_AMOC, -2):.0f}".replace("12200", r"12\,200"))
aus("b) Massenstrom Luft / AMOC", m_L / m_AMOC, "", r"\dot{m}_{\mathrm{L}}/\dot{m}_{\mathrm{AMOC}} = " + de(m_L / m_AMOC, 1))
aus("b) Wärmestrom Atmosphäre / AMOC", Q_A / Q_AMOC, "", r"\dot{Q}_{\mathrm{A}}/\dot{Q}_{\mathrm{AMOC}} = " + de(Q_A / Q_AMOC, 1))
vergleich("Luftmassenstrom fühlbar", m_L, 2.488e11, "2,488e11 kg/s, 2,07e5 Sv, 12194-fach, 14,3-fach")

# c) C3
q_lat = dx * dh_v
dT_lat = q_lat / c_L
m_L2 = Q_A / (c_L * dT_A + q_lat)
anteil_lat = q_lat / (c_L * dT_A + q_lat)
aus("c) latente Wärme je kg Luft", q_lat / 1e3, "kJ/kg")
aus("c) entspricht einer Erwärmung um", dT_lat, "K", r"\Delta T_{\mathrm{lat}} = " + de(dT_lat, 1) + r"\,\mathrm{K}")
aus("c) Luftmassenstrom fühlbar und latent", m_L2, "kg/s", r"\dot{m}_{\mathrm{L}} = " + de(m_L2 / 1e11) + r"\cdot 10^{11}\,\mathrm{kg/s}")
aus("c) latenter Anteil", anteil_lat * 100, "%", r"latenter Anteil $" + f"{anteil_lat * 100:.0f}" + r"\,\%")
vergleich("latenter Anteil", anteil_lat * 100, 38, "12,2 kJ/kg, 12 K, 1,55e11 kg/s, 38 %")

# d) C4
aus("d) (1) Hadley-Zelle / Ergebnis aus c)", m_Hadley / m_L2, "", r"\dot{m}_{\mathrm{H}}/\dot{m}_{\mathrm{L}} = " + de(m_Hadley / m_L2))
aus("d) (1) Faktor", m_L2 / m_Hadley, "")
w_N = m_L2 / (rho_m * 0.5 * U40 * H)
aus("d) (2) mittlere Nordwärts-Geschwindigkeit (halbe Wand)", w_N, "m/s", r"w_{\mathrm{N}} = " + de(w_N) + r"\,\mathrm{m/s}")
vergleich("Hadley / C3", m_Hadley / m_L2, 0.54, "0,54 mit 0,84e11 kg/s (Aufgabentext: rund 0,8e11, Faktor 2)")
vergleich("Nordwärts-Geschwindigkeit", w_N, 1.32, "1,32 m/s mit rho 0,764 und U 30 665 km")

# =============================================================================
# Zusatzaufgabe 1: Gegenstrom im Entenfuß (C* = 1)
# =============================================================================
NTU_E = 4.0                       # Arbeitswert (gewählt)
eps_gg = NTU_E / (1 + NTU_E)
eps_gl = (1 - math.exp(-2 * NTU_E)) / 2
aus("Z1 a) eps Gegenstrom, NTU = 4", eps_gg, "", r"\varepsilon_{\mathrm{Gegen}} = " + de(eps_gg))
aus("Z1 a) eps Gleichstrom, NTU = 4", eps_gl, "", r"\varepsilon_{\mathrm{Gleich}} = " + de(eps_gl))
for n in (0.5, 1.0, 2.0, 4.0, 10.0, 100.0):
    aus(f"   NTU = {n:5.1f}: eps Gegenstrom / Gleichstrom", n / (1 + n), f"/ {(1 - math.exp(-2 * n)) / 2:.4f}")
aus("Z1 b) Grenzwert Gegenstrom (NTU -> unendlich)", 1.0, "", r"\varepsilon_{\mathrm{Gegen}} \to 1")
aus("Z1 b) Grenzwert Gleichstrom (NTU -> unendlich)", 0.5, "", r"\varepsilon_{\mathrm{Gleich}} \to 0{,}5")
# Fuß gibt (1 - eps) C (theta_Körper - theta_Wasser) ab, wenn das Blut den Fuß mit Wassertemperatur verlässt
f_gg, f_gl = 1 - eps_gg, 1 - eps_gl
aus("Z1 c) Wärmeabgabe Gegenstrom / ohne Übertragung", f_gg, "")
aus("Z1 c) Wärmeabgabe Gleichstrom / ohne Übertragung", f_gl, "")
aus("Z1 c) Faktor Gegenstrom gegenüber Gleichstrom", f_gl / f_gg, "", r"Faktor $" + de(f_gl / f_gg, 1) + "$")
aus("Z1 c) Faktor Gegenstrom gegenüber ohne Übertragung", 1 / f_gg, "", r"bzw. $" + de(1 / f_gg, 0) + "$")
aus("Z1 c) gemessen 3 % -> ohne Übertragung (gleiche Durchblutung)", 3 / f_gg, "%", r"ohne Wärmeübertragung $" + f"{3 / f_gg:.0f}" + "$ bis")
aus("Z1 c) gemessen 7 % -> ohne Übertragung (gleiche Durchblutung)", 7 / f_gg, "%", r"bis $" + f"{7 / f_gg:.0f}" + r"\,\%$")

# =============================================================================
# Zusatzaufgabe 2: Der Rekordflug (Aufgabe C5)
# =============================================================================
s_GK = 5540e3                     # m Großkreis JFK nach LHR (Ausgangsskript: 5540 km)
w_F = 252.0                       # m/s Mach 0,85 in 10,7 km (Ausgangsskript: 252,1 m/s)
t_R = (4 + 56 / 60) * 3600        # s
w_G = s_GK / t_R
w_R = w_G - w_F
w_R3 = 1.03 * s_GK / t_R - w_F
t_0 = s_GK / w_F / 3600
aus("Z2 a) Geschwindigkeit über Grund", w_G, "m/s")
aus("Z2 a) mittlerer Rückenwind (Großkreis)", w_R, "m/s", r"w_{\mathrm{R}} = " + de(w_R, 1) + r"\,\mathrm{m/s}")
aus("Z2 a) mittlerer Rückenwind in km/h", w_R * 3.6, "km/h", r"\,\mathrm{m/s} = " + f"{w_R * 3.6:.0f}" + r"\,\mathrm{km/h}")
aus("Z2 b) mit 3 % längerem Flugweg", w_R3, "m/s", r"w_{\mathrm{R}} = " + de(w_R3, 1) + r"\,\mathrm{m/s}")
aus("   Flightradar24 rund 150 mph in m/s", 150 * 0.44704, "m/s")
aus("Z2 c) Flugzeit ohne Wind", t_0, "h", r"t = " + de(t_0) + r"\,\mathrm{h}")
aus("Z2 c) Flugzeit ohne Wind, Minuten über 6 h", (t_0 - 6) * 60, "min")
vergleich("Rückenwind 3 % länger", w_R3, 69.2, "69,2 m/s mit 252,1 m/s (hier 252 m/s wie im Aufgabentext)")
vergleich("Flugzeit ohne Wind", t_0, 6.11, "6,11 h")

# =============================================================================
# Ausgabe und Prüfung gegen teile/t8.md
# =============================================================================
md = ohne_mathrm(open(TEIL, encoding="utf-8").read()) if os.path.exists(TEIL) else ""
fehlt = []
zeilen = ["Tutorium 8: Wärmeübertrager und Verdampfer, Nachrechnung (t8_rechnung.py)",
          "Spalten: Name | Wert | Einheit | Schreibweise im Aufgabentext (Prüfung gegen teile/t8.md)", ""]
for name, wert, einheit, schreib in ZEILEN:
    s = f"{name:66s} {wert:14.6g} {einheit:10s}"
    if schreib:
        ok = ohne_mathrm(schreib) in md
        if not ok:
            fehlt.append(schreib)
        s += f"  {schreib}  [{'steht im Text' if ok else 'FEHLT im Text'}]"
    zeilen.append(s)
zeilen += ["", "Vergleich mit den Ausgangsskripten (neu | Ausgangsskript | Angabe dort):"]
for name, neu, quelle, text in ABWEICHUNG:
    zeilen.append(f"  {name:34s} {neu:12.5g} | {quelle:10.5g} | {text}")
zeilen += ["", f"Prüfung: {len([z for z in ZEILEN if z[3]])} Schreibweisen geprüft, {len(fehlt)} fehlen im Text."]
text = "\n".join(zeilen) + "\n"
with open(os.path.join(HIER, "t8_rechnung_ausgabe.txt"), "w", encoding="utf-8") as f:
    f.write(text)
print(text)
if fehlt:
    print("FEHLENDE SCHREIBWEISEN:")
    for s in fehlt:
        print("  ", s)
