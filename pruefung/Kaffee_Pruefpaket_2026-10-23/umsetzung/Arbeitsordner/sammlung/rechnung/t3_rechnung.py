# -*- coding: utf-8 -*-
"""Tutorium 3 (Wärmedurchgang) der Aufgabensammlung: alle Zahlen der Tabellen und Ergebniszeilen.

Aufgabe 1: Meereis und Schnee als Deckel (Ideensammlung 4.3, Teile a bis f)
Aufgabe 2: Ölleitung im Permafrost (Ideensammlung 4.3, Teile g bis i)
Zusatzaufgabe 1: schneefreie Stellen (Parallelschaltung)

Eingabewerte wie im Aufgabenblatt (teile/t3.md); Arbeitswerte aus der Ideensammlung
„Leitaufgaben aus Klima und Erde“ (17.10.2026) und aus nachrechnung_leitphaenomene.py.
Stahlwand 14,3 mm (0,562 Zoll), Außendurchmesser 1,22 m (48 Zoll) und Dämmung 9,5 cm (3,75 Zoll)
nach dem TAPS Factbook (Alyeska, 2024); alpha_i = 500 W/(m² K) ist ein Arbeitswert des Skripts.
Korrelationen: Formelsammlung Wärmeübertragung SoSe 2026 (querumströmter Zylinder, L = pi d / 2).

Aufruf: python3 t3_rechnung.py   (schreibt t3_rechnung_ausgabe.txt in diesen Ordner und prüft am Ende,
ob jeder Tabellenwert und jede Ergebniszahl genau so in ../teile/t3.md steht)
"""
import math
import os
import sys as _sys, os as _os
_sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), "build"))
from indizes_aufrecht import ohne_mathrm   # Schreibweise prüfen unabhängig davon, ob Indizes aufrecht oder kursiv stehen

HIER = os.path.dirname(os.path.abspath(__file__))
AUS = []                                   # (Name, Wert, Einheit, Anzeige im Blatt)


def de(x, n=2):
    """Zahl mit Dezimalkomma wie im Blatt."""
    return f"{x:.{n}f}".replace(".", ",")


def merke(name, wert, einheit, n):
    AUS.append((name, wert, einheit, de(wert, n)))
    return wert


def kopf(text):
    AUS.append((None, text, None, None))


# Korrelationen nach Formelsammlung SoSe 2026
def nu_lam(Re, Pr):
    return 0.664 * Re**0.5 * Pr**(1 / 3)


def nu_turb(Re, Pr):
    return 0.037 * Re**0.8 * Pr / (1 + 2.443 * Re**-0.1 * (Pr**(2 / 3) - 1))


def nu_zyl(Re, Pr):                         # querumströmter Zylinder, Übergangsbereich, 10 < Re < 1e7
    return 0.3 + math.sqrt(nu_lam(Re, Pr)**2 + nu_turb(Re, Pr)**2)


# =====================================================================================
# Aufgabe 1: Meereis und Schnee als Deckel
# =====================================================================================
th_L, th_W, alpha_a = -30.0, -1.8, 15.0      # °C, °C, W/(m² K)
s_S, lam_S = 0.20, 0.20                      # m, W/(m K)
s_E, lam_E = 1.40, 2.10                      # m, W/(m K)
rho_E, dh_schm = 917.0, 333.5e3              # kg/m³, J/kg
A = 1.0                                      # m²
s_J = 0.10                                   # m, Jungeis (Teil f)
lam_S_min, lam_S_max = 0.14, 0.30            # W/(m K), Spannbreite Schnee (Teil c)
dT = th_W - th_L

kopf("Aufgabe 1: Meereis und Schnee als Deckel (A = 1 m²)")
R_a = merke("c) R_th,alpha = 1/(alpha_a A)", 1 / (alpha_a * A), "K/W", 4)
R_S = merke("c) R_th,S = s_S/(lambda_S A)", s_S / (lam_S * A), "K/W", 2)
R_E = merke("c) R_th,E = s_E/(lambda_E A)", s_E / (lam_E * A), "K/W", 3)
merke("c) R_th,S mit lambda_S = 0,3 W/(m K)", s_S / (lam_S_max * A), "K/W", 3)
merke("c) R_th,S mit lambda_S = 0,14 W/(m K)", s_S / (lam_S_min * A), "K/W", 2)
R_ges = merke("d) R_th,ges", R_a + R_S + R_E, "K/W", 2)
kA = merke("d) kA = 1/R_th,ges", 1 / R_ges, "W/K", 3)
Q = merke("d) Wärmestrom Q", dT / R_ges, "W", 1)
th_O = merke("d) theta_O (Schneeoberfläche)", th_L + Q * R_a, "°C", 1)
th_SE = merke("d) theta_SE (Grenze Schnee/Eis)", th_O + Q * R_S, "°C", 1)
assert abs((th_W - Q * R_E) - th_SE) < 1e-9          # Kontrolle von unten
merke("e) Delta T über alpha_a", Q * R_a, "K", 2)
merke("e) Delta T über dem Schnee", Q * R_S, "K", 1)
merke("e) Delta T über dem Eis", Q * R_E, "K", 1)
merke("e) Summe der Teildifferenzen", Q * (R_a + R_S + R_E), "K", 1)
q_W = merke("e) offenes Wasser q_W = alpha_a (theta_W - theta_u)", alpha_a * dT, "W/m²", 0)
merke("e) Faktor offenes Wasser / mit Eis und Schnee", q_W * A / Q, "-", 0)

# Vergleichswert aus Tutorium 2 (10 m breite Rinne, 8 m/s, Platte turbulent, Luft bei der Filmtemperatur)
try:
    from CoolProp.CoolProp import PropsSI
    T_film2 = 0.5 * (th_W + th_L) + 273.15
    nu2 = PropsSI("V", "T", T_film2, "P", 101325.0, "Air") / PropsSI("D", "T", T_film2, "P", 101325.0, "Air")
    lam2 = PropsSI("L", "T", T_film2, "P", 101325.0, "Air")
    Pr2 = PropsSI("V", "T", T_film2, "P", 101325.0, "Air") * PropsSI("C", "T", T_film2, "P", 101325.0, "Air") / lam2
    alpha_R = nu_turb(8.0 * 10.0 / nu2, Pr2) * lam2 / 10.0
    quelle_R = "CoolProp, wie nachrechnung_leitphaenomene.py"
except ImportError:                                  # Wert aus nachrechnung_ausgabe.txt
    alpha_R = 19.645
    quelle_R = "ohne CoolProp: Wert aus nachrechnung_ausgabe.txt"
merke(f"e) Tutorium 2: alpha der Rinne ({quelle_R})", alpha_R, "W/(m² K)", 1)
merke("e) Tutorium 2: q der Rinne (offenes Wasser)", alpha_R * dT, "W/m²", 0)
alpha_R_blatt = 19.6                                 # im Blatt genannter, gerundeter Wert
merke("e) Q mit alpha = 19,6 W/(m² K) (Eis und Schnee)", dT / (1 / (alpha_R_blatt * A) + R_S + R_E), "W", 1)
merke("e) Anteil des äußeren Widerstands an R_th,ges", R_a / R_ges * 100, "%", 1)

dhdt = merke("f) Eiswachstum dh/dt = q/(rho_E dh_schm)", Q / A / (rho_E * dh_schm) * 86400 * 100, "cm/d", 2)
R_J = 1 / alpha_a + s_J / lam_E                      # m² K/W, Jungeis ohne Schnee
q_J = merke("f) Jungeis 10 cm ohne Schnee: q", dT / R_J, "W/m²", 0)
merke("f) Jungeis 10 cm ohne Schnee: dh/dt", q_J / (rho_E * dh_schm) * 86400 * 100, "cm/d", 2)
merke("f) Verhältnis q Jungeis / q mit Schnee", q_J * A / Q, "-", 1)

# Nur zur Information (Ideensammlung, nicht im Blatt): Spannbreite des Schnees
for lam in (lam_S_max, lam_S_min):
    merke(f"Info: Q mit lambda_S = {de(lam, 2)} W/(m K)", dT / (R_a + s_S / (lam * A) + R_E), "W", 1)

# =====================================================================================
# Aufgabe 2: Ölleitung im Permafrost (L = 1 m)
# =====================================================================================
th_Oel, th_L2, w = 30.0, -30.0, 5.0           # °C (Öl, Blatt: theta_i), °C (Luft, Blatt: theta_u), m/s
alpha_i = 500.0                               # W/(m² K), Arbeitswert Ölseite
d_St, s_St, lam_St = 1.22, 0.0143, 45.0       # m, m, W/(m K)
s_Iso, lam_Iso = 0.095, 0.04                  # m, W/(m K)
L = 1.0                                       # m
th_m_ann = -29.0                              # °C, angenommene Filmtemperatur theta_m
nu_L, lam_L, Pr_L = 1.087e-5, 0.0221, 0.716   # Luft bei -29 °C (Tabelle, gerundet)

kopf("Aufgabe 2: Ölleitung im Permafrost (L = 1 m)")
try:
    from CoolProp.CoolProp import PropsSI
    T = th_m_ann + 273.15
    rho = PropsSI("D", "T", T, "P", 101325.0, "Air")
    eta = PropsSI("V", "T", T, "P", 101325.0, "Air")
    lam = PropsSI("L", "T", T, "P", 101325.0, "Air")
    cp = PropsSI("C", "T", T, "P", 101325.0, "Air")
    AUS.append(("Tabelle: Luft bei -29 °C (CoolProp) nu", eta / rho * 1e5, "1e-5 m²/s", de(eta / rho * 1e5, 3)))
    AUS.append(("Tabelle: Luft bei -29 °C (CoolProp) lambda", lam, "W/(m K)", de(lam, 4)))
    AUS.append(("Tabelle: Luft bei -29 °C (CoolProp) Pr", eta * cp / lam, "-", de(eta * cp / lam, 3)))
except ImportError:
    pass

r_St = d_St / 2                               # Außenradius Stahl = Innenradius Dämmung
r_i = r_St - s_St
r_a = r_St + s_Iso
d_a = 2 * r_a
merke("a) Innenradius Stahlrohr r_i", r_i, "m", 4)
merke("a) Außendurchmesser der Dämmung d_a", d_a, "m", 2)
L_ch = merke("a) charakteristische Länge pi d_a/2", math.pi * d_a / 2, "m", 3)
Re = merke("a) Re", w * L_ch / nu_L, "-", 0)
merke("a) Re / 1e6", Re / 1e6, "1e6", 2)
merke("a) Nu_lam", nu_lam(Re, Pr_L), "-", 0)
merke("a) Nu_turb", nu_turb(Re, Pr_L), "-", 0)
Nu_m = merke("a) Nu_m", nu_zyl(Re, Pr_L), "-", 0)
alpha_a2 = merke("a) alpha_a", Nu_m * lam_L / L_ch, "W/(m² K)", 1)
assert 5e5 < Re < 1e7

R_i = merke("b) R_th,i = 1/(alpha_i 2 pi r_i L)", 1 / (alpha_i * 2 * math.pi * r_i * L), "K/W", 6)
R_St = merke("b) R_th,St = ln(r_St/r_i)/(2 pi lambda_St L)", math.log(r_St / r_i) / (2 * math.pi * lam_St * L), "K/W", 7)
R_Iso = merke("b) R_th,Iso = ln(r_a/r_St)/(2 pi lambda_Iso L)", math.log(r_a / r_St) / (2 * math.pi * lam_Iso * L), "K/W", 3)
R_aa = merke("b) R_th,a = 1/(alpha_a 2 pi r_a L)", 1 / (alpha_a2 * 2 * math.pi * r_a * L), "K/W", 4)
R2 = merke("b) R_th,ges", R_i + R_St + R_Iso + R_aa, "K/W", 3)
merke("b) Anteil der Dämmung an R_th,ges", R_Iso / R2 * 100, "%", 1)
Q2 = merke("b) Wärmestrom Q (L = 1 m) = Q/L", (th_Oel - th_L2) / R2, "W", 0)
merke("b) Q/L mit einer Nachkommastelle", Q2, "W/m", 1)
th_O2 = merke("c) theta_O (Oberfläche der Dämmung)", th_L2 + Q2 * R_aa, "°C", 1)
merke("c) Filmtemperatur theta_m = (theta_O + theta_u)/2", 0.5 * (th_O2 + th_L2), "°C", 1)
k_i = merke("d) k_i = kA/(2 pi r_i L)", 1 / (R2 * 2 * math.pi * r_i * L), "W/(m² K)", 3)
k_a = merke("d) k_a = kA/(2 pi r_a L)", 1 / (R2 * 2 * math.pi * r_a * L), "W/(m² K)", 3)
merke("d) k_i A_i", k_i * 2 * math.pi * r_i * L, "W/K", 2)
merke("d) k_a A_a", k_a * 2 * math.pi * r_a * L, "W/K", 2)
r_krit = merke("e) r_krit = lambda_Iso/alpha_a in mm", lam_Iso / alpha_a2 * 1e3, "mm", 2)
merke("e) Außenradius der Dämmung r_a in mm", r_a * 1e3, "mm", 0)

# Kernzahlen der Ideensammlung (Abschnitt 4.3) zur Kontrolle
assert abs(R_ges - 1.733) < 1e-3 and abs(Q - 16.3) < 0.05 and abs(th_O + 28.9) < 0.05 and abs(th_SE + 12.6) < 0.05
assert abs(q_W - 423) < 0.5 and abs(dhdt - 0.46) < 0.005 and abs(q_J - 247) < 0.5
assert abs(alpha_a2 - 20.2) < 0.05 and abs(Q2 - 102) < 0.5 and abs(k_i - 0.455) < 5e-4 and abs(k_a - 0.384) < 5e-4
assert abs(r_krit - 2.0) < 0.05

# =====================================================================================
# Zusatzaufgabe 1: schneefreie Stellen (Parallelschaltung), A = 1 m², 10 % ohne Schnee
# =====================================================================================
kopf("Zusatzaufgabe 1: schneefreie Stellen (10 % der Fläche ohne Schnee)")
f_frei = 0.10
R_mit = (1 / alpha_a + s_S / lam_S + s_E / lam_E) / ((1 - f_frei) * A)   # K/W, Pfad mit Schnee
R_ohne = (1 / alpha_a + s_E / lam_E) / (f_frei * A)                     # K/W, Pfad ohne Schnee
merke("a) R_th mit Schnee (0,9 m²)", R_mit, "K/W", 2)
merke("a) R_th ohne Schnee (0,1 m²)", R_ohne, "K/W", 2)
R_par = merke("a) R_th,ges parallel", 1 / (1 / R_mit + 1 / R_ohne), "K/W", 2)
Q_par = merke("b) Wärmestrom Q", dT / R_par, "W", 1)
merke("b) Zunahme gegenüber geschlossener Schneedecke", (Q_par / Q - 1) * 100, "%", 1)
merke("c) Anteil durch die schneefreie Fläche", dT / R_ohne / Q_par * 100, "%", 1)
assert abs((Q_par / Q - 1) * 100 - 14) < 0.5

# =====================================================================================
# Abgleich mit teile/t3.md (wie in t1_rechnung.py und t2_rechnung.py): jede Zeichenkette
# (Tabellenwert oder Ergebnis, aus den Variablen oben formatiert) muss genau so im Blatt stehen.
# =====================================================================================
W = {name: wert for name, wert, _, _ in AUS if name is not None}


def m(x, n):
    """Zahl im Mathe-Format des Blatts (Dezimalkomma als {,})."""
    return f"{x:.{n}f}".replace(".", "{,}")


def mz(x, n):
    """Zahl in Zehnerpotenz-Schreibweise des Blatts, z. B. 5{,}34\\cdot 10^{-4}."""
    e = int(math.floor(math.log10(abs(x))))
    return m(x / 10**e, n) + r"\cdot 10^{" + str(e) + "}"


SOLL = [
    # Aufgabe 1, Tabelle
    r"\vartheta_u = " + m(th_L, 0) + r"\,\mathrm{°C}",
    r"\vartheta_W = " + m(th_W, 1) + r"\,\mathrm{°C}",
    r"\alpha_a = " + m(alpha_a, 0) + r"\,\mathrm{W/(m^2\,K)}",
    r"s_S = " + m(s_S, 1) + r"\,\mathrm{m}",
    r"\lambda_S = " + m(lam_S, 1) + r"\,\mathrm{W/(m\,K)}",
    r"s_E = " + m(s_E, 1) + r"\,\mathrm{m}",
    r"\lambda_E = " + m(lam_E, 1) + r"\,\mathrm{W/(m\,K)}",
    r"\rho_E = " + m(rho_E, 0) + r"\,\mathrm{kg/m^3}",
    r"\Delta h_{schm} = " + m(dh_schm / 1e3, 1) + r"\,\mathrm{kJ/kg}",
    r"A = " + m(A, 0) + r"\,\mathrm{m^2}",
    r"s_J = " + m(s_J, 1) + r"\,\mathrm{m}",
    # Aufgabe 1, Ergebnisse
    r"zwischen $" + m(lam_S_min, 2) + r"$ und $" + m(lam_S_max, 1) + r"\,\mathrm{W/(m\,K)}$",
    r"R_{th,\alpha} = " + m(R_a, 4) + r"\,\mathrm{K/W}",
    r"R_{th,S} = " + m(R_S, 2) + r"\,\mathrm{K/W}",
    r"R_{th,E} = " + m(R_E, 3) + r"\,\mathrm{K/W}",
    r"R_{th,S} = " + m(s_S / (lam_S_max * A), 3) + r"$ bis $" + m(s_S / (lam_S_min * A), 2) + r"\,\mathrm{K/W}",
    r"R_{th,ges} = " + m(R_ges, 2) + r"\,\mathrm{K/W}",
    r"kA = " + m(kA, 3) + r"\,\mathrm{W/K}",
    r"\dot{Q} = " + m(Q, 1) + r"\,\mathrm{W}",
    r"\vartheta_O = " + m(th_O, 1) + r"\,\mathrm{°C}",
    r"\vartheta_{SE} = " + m(th_SE, 1) + r"\,\mathrm{°C}",
    r"\Delta T_S = " + m(Q * R_S, 1) + r"\,\mathrm{K}",
    m(Q * R_a, 2) + r"\,\mathrm{K} + " + m(Q * R_S, 1) + r"\,\mathrm{K} + " + m(Q * R_E, 1) + r"\,\mathrm{K} = "
    + m(Q * (R_a + R_S + R_E), 1) + r"\,\mathrm{K}",
    r"\dot{q}_W = " + m(q_W, 0) + r"\,\mathrm{W/m^2}$, Faktor " + m(q_W * A / Q, 0),
    r"\alpha = " + m(alpha_R, 1) + r"\,\mathrm{W/(m^2\,K)}$ und $\dot{q} = " + m(alpha_R * dT, 0) + r"\,\mathrm{W/m^2}",
    r"zu (3): $\dot{Q} = " + m(W["e) Q mit alpha = 19,6 W/(m² K) (Eis und Schnee)"], 1) + r"\,\mathrm{W}",
    r"\mathrm{d}s_E/\mathrm{d}t = " + m(dhdt, 2) + r"\,\mathrm{cm/d}",
    r"\dot{q}_J = " + m(q_J, 0) + r"\,\mathrm{W/m^2}",
    r"\mathrm{d}s_J/\mathrm{d}t = " + m(W["f) Jungeis 10 cm ohne Schnee: dh/dt"], 2) + r"\,\mathrm{cm/d}",
    # Aufgabe 2, Tabelle und Annahme
    r"\vartheta_i = " + m(th_Oel, 0) + r"\,\mathrm{°C}",
    r"\alpha_i = " + m(alpha_i, 0) + r"\,\mathrm{W/(m^2\,K)}",
    r"w = " + m(w, 0) + r"\,\mathrm{m/s}",
    r"\nu_L = " + m(nu_L * 1e5, 3) + r"\cdot 10^{-5}\,\mathrm{m^2/s}",
    r"\lambda_L = " + m(lam_L, 4) + r"\,\mathrm{W/(m\,K)}",
    r"Pr = " + m(Pr_L, 3),
    r"d_{St} = " + m(d_St, 2) + r"\,\mathrm{m}",
    r"s_{St} = " + m(s_St * 1e3, 1) + r"\,\mathrm{mm}",
    r"\lambda_{St} = " + m(lam_St, 0) + r"\,\mathrm{W/(m\,K)}",
    r"s_{Iso} = " + m(s_Iso * 100, 1) + r"\,\mathrm{cm}",
    r"\lambda_{Iso} = " + m(lam_Iso, 2) + r"\,\mathrm{W/(m\,K)}",
    r"L = " + m(L, 0) + r"\,\mathrm{m}",
    r"\vartheta_m = " + m(th_m_ann, 0) + r"\,\mathrm{°C}",
    # Aufgabe 2, Ergebnisse
    r"Re = " + m(Re / 1e6, 2) + r"\cdot 10^{6}",
    r"Nu_m = " + m(Nu_m, 0),
    r"\alpha_a = " + m(alpha_a2, 1) + r"\,\mathrm{W/(m^2\,K)}",
    r"R_{th,i} = " + mz(R_i, 2) + r"\,\mathrm{K/W}",
    r"R_{th,St} = " + mz(R_St, 2) + r"\,\mathrm{K/W}",
    r"R_{th,Iso} = " + m(R_Iso, 3) + r"\,\mathrm{K/W}",
    r"R_{th,a} = " + m(R_aa, 4) + r"\,\mathrm{K/W}",
    r"R_{th,ges} = " + m(R2, 3) + r"\,\mathrm{K/W}",
    r"\dot{Q} = " + m(Q2, 0) + r"\,\mathrm{W}",
    r"\vartheta_O = " + m(th_O2, 1) + r"\,\mathrm{°C}",
    r"\vartheta_m = " + m(W["c) Filmtemperatur theta_m = (theta_O + theta_u)/2"], 1) + r"\,\mathrm{°C}",
    r"k_i = " + m(k_i, 3) + r"\,\mathrm{W/(m^2\,K)}",
    r"k_a = " + m(k_a, 3) + r"\,\mathrm{W/(m^2\,K)}",
    r"k_i A_i = k_a A_a = " + m(W["d) k_i A_i"], 2) + r"\,\mathrm{W/K}",
    r"r_{krit} = \lambda_{Iso}/\alpha_a = " + m(r_krit, 2) + r"\,\mathrm{mm}",
    # Zusatzaufgabe 1
    r"R_{th,ges} = " + m(R_par, 2) + r"\,\mathrm{K/W}",
    r"\dot{Q} = " + m(Q_par, 1) + r"\,\mathrm{W}",
    r"Zunahme: $" + m((Q_par / Q - 1) * 100, 1) + r"\,\%",
    r"Anteil: $" + m(dT / R_ohne / Q_par * 100, 1) + r"\,\%",
]

TEIL = os.path.join(os.path.dirname(HIER), "teile", "t3.md")
abgleich = ["", "ABGLEICH mit teile/t3.md (jede Zeichenkette muss im Markdown stehen)"]
fehlt = 0
if os.path.exists(TEIL):
    with open(TEIL, encoding="utf-8") as f:
        md = ohne_mathrm(f.read())
    for soll in SOLL:
        ok = ohne_mathrm(soll) in md
        fehlt += 0 if ok else 1
        abgleich.append(f"{'ok   ' if ok else 'FEHLT'} {soll}")
else:
    abgleich.append("teile/t3.md fehlt noch")
    fehlt = -1
abgleich.append(f"Ergebnis des Abgleichs: {'alles gefunden' if fehlt == 0 else str(fehlt) + ' fehlen'}")

with open(os.path.join(HIER, "t3_rechnung_ausgabe.txt"), "w", encoding="utf-8") as f:
    f.write("Tutorium 3: Wärmedurchgang (Zahlen der Tabellen und Ergebniszeilen; Spalte „Blatt“ = Anzeige im Blatt)\n")
    for name, wert, einheit, blatt in AUS:
        if name is None:
            f.write(f"\n{wert}\n")
        else:
            f.write(f"{name:76s} {wert:16.6f} {einheit:10s} Blatt: {blatt}\n")
    f.write("\n".join(abgleich) + "\n")
print(open(os.path.join(HIER, "t3_rechnung_ausgabe.txt"), encoding="utf-8").read())
