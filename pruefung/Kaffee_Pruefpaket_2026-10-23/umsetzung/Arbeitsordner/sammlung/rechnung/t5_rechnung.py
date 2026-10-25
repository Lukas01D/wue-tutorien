# -*- coding: utf-8 -*-
"""Tutorium 5 (Wärmebilanzen, instationär global): Zahlen der Ozean- und Flussaufgaben
(teile/t5b_ozean.md, Aufgaben 2 bis 4 und Zusatzaufgaben 1 und 2).

Jede Zahl der Ergebniszeilen und der Tabellen wird hier aus den Werten der Tabellen berechnet und mit
Name, Wert und Einheit nach t5_rechnung_ausgabe.txt geschrieben. Die Spalte „Anzeige“ ist die Schreibweise
im Markdown; am Ende prüft das Skript, ob jede Anzeige in teile/t5b_ozean.md vorkommt.

Herkunft der Arbeitswerte: Aufgabenideen_Ozean_Atmosphaere.md (Aufgabe A und B) mit dem Skript
nachrechnung_ozean_atmosphaere.py sowie Leitaufgaben_Klima_Erde_2026-10-17.md, Abschnitt 4.5, mit dem Skript
nachrechnung_leitphaenomene.py. Der Abschnitt „Abgleich“ vergleicht mit den Kernzahlen dieser Dokumente.
Die Kaffee-Aufgabe (Aufgabe 1) rechnet t5_kaffee_teil.py.

Aufruf: python3 t5_rechnung.py
"""
import math
import os

HIER = os.path.dirname(os.path.abspath(__file__))
SAMMLUNG = os.path.dirname(HIER)
MD = os.path.join(SAMMLUNG, "teile", "t5b_ozean.md")
AUSGABE = os.path.join(HIER, "t5_rechnung_ausgabe.txt")

JAHR = 365.25 * 86400.0          # s
SV = 1e6                         # m³/s je Sverdrup
K0 = 273.15
SIGMA = 5.6705e-8                # W/(m² K⁴), Wert aus V04 (wie Tutorium 4)

zeilen = []                      # (Abschnitt, Name, Wert, Einheit, Anzeige)


def de(x, n=2):
    """Dezimalkomma für Mathe im Markdown: 70.47 -> 70{,}47"""
    return f"{x:.{n}f}".replace(".", "{,}")


def de10(x, n=2):
    """Zehnerpotenz für Mathe im Markdown: 1.742e10 -> 1{,}74\\cdot 10^{10}"""
    e = int(math.floor(math.log10(abs(x))))
    m = x / 10**e
    if round(m, n) >= 10:
        m, e = m / 10, e + 1
    return f"{de(m, n)}\\cdot 10^{{{e}}}"


def ganz(x):
    """ganze Zahl, ab fünf Stellen mit schmalem Abstand (Mathe)"""
    s = f"{x:.0f}"
    if len(s.lstrip("-")) >= 5:
        s = s[:-3] + "\\," + s[-3:]
    return s


def neu(abschnitt):
    zeilen.append((abschnitt, None, None, None, None))


def z(name, wert, einheit, anzeige):
    zeilen.append(("", name, wert, einheit, anzeige))
    return wert


# =============================================================================
neu("Aufgabe 2: Die AMOC und Europas milde Winter (Tabellenwerte)")
V_AMOC = z("Volumenstrom der AMOC bei 26,5° N", 17.0, "Sv", r"\dot{V} = 17\,\mathrm{Sv}") * SV
Q_AMOC = z("Wärmestrom der AMOC bei 26,5° N", 1.2, "PW", r"\dot{Q}_{AMOC} = 1{,}2\,\mathrm{PW}") * 1e15
RHO_M = z("Dichte Meerwasser", 1025.0, "kg/m³", r"\rho_M = 1025\,\mathrm{kg/m^3}")
CP_M = z("spez. Wärmekapazität Meerwasser", 3990.0, "J/(kg K)", r"c_{p,M} = 3990\,\mathrm{J/(kg\,K)}")
TH_W = z("Oberflächenwasser (etwa)", 20.0, "°C", r"\vartheta_w \approx 20\,\mathrm{°C}")
TH_K = z("Tiefenwasser (etwa)", 3.0, "°C", r"\vartheta_k \approx 3\,\mathrm{°C}")
V_AMA = z("Amazonas", 0.206, "Sv", r"\dot{V}_A = 0{,}206\,\mathrm{Sv}") * SV
z("Golfstrom bei 60° W (mindestens)", 150.0, "Sv", r"\dot{V}_G \geq 150\,\mathrm{Sv}")
A_G = z("Fläche ganzer Gürtel 40° bis 70° N", 7.6e13, "m²", r"A_G = 7{,}6\cdot 10^{13}\,\mathrm{m^2}")
A_V = z("Fläche Viertel (50° W bis 40° O)", 1.9e13, "m²", r"A_V = 1{,}9\cdot 10^{13}\,\mathrm{m^2}")
Q_S = z("Sonne am Oberrand, Januarmittel 51,7° N", 93.0, "W/m²", r"\dot{q}_S = 93\,\mathrm{W/m^2}")
ALB = z("Albedo im Winter", 0.4, "-", r"\rho_p = 0{,}4")
EPS = z("Emissionsgrad der Atmosphärenschicht", 0.78, "-", r"\varepsilon_A = 0{,}78")
z("Stefan-Boltzmann-Konstante", SIGMA, "W/(m² K⁴)", r"\sigma = 5{,}6705\cdot 10^{-8}\,\mathrm{W/(m^2\,K^4)}")
TH_PB = z("Januarmittel Paderborn", 2.1, "°C", r"\vartheta_{PB} = 2{,}1\,\mathrm{°C}")
TH_GB = z("Januarmittel Goose Bay", -17.6, "°C", r"\vartheta_{GB} = -17{,}6\,\mathrm{°C}")
z("Deckschicht im Winter, untere Grenze", 100.0, "m", r"h = 100\,\mathrm{m}")
z("Deckschicht im Winter, obere Grenze", 350.0, "m", r"350\,\mathrm{m}")

neu("Aufgabe 2: Ergebnisse")
z("a) Volumenstrom", V_AMOC, "m³/s", r"\dot{V} = " + de10(V_AMOC, 1) + r"\,\mathrm{m^3/s}")
m_AMOC = z("a) Massenstrom m = rho V", RHO_M * V_AMOC, "kg/s", r"\dot{m} = " + de10(RHO_M * V_AMOC) + r"\,\mathrm{kg/s}")
z("a) AMOC / Amazonas", V_AMOC / V_AMA, "-", r"\dot{V}/\dot{V}_A = " + de(V_AMOC / V_AMA, 1))
C_AMOC = z("b) Wärmekapazitätsstrom C = m cp", m_AMOC * CP_M / 1e12, "TW/K", de(m_AMOC * CP_M / 1e12, 1) + r"\,\mathrm{TW/K}") * 1e12
dT_AMOC = z("b) Temperaturdifferenz Hin gegen Rück", Q_AMOC / C_AMOC, "K", r"\Delta T = " + de(Q_AMOC / C_AMOC, 1) + r"\,\mathrm{K}")
z("b) Kontrolle C (20 °C - 3 °C)", C_AMOC * (TH_W - TH_K) / 1e15, "PW", de(C_AMOC * (TH_W - TH_K) / 1e15) + r"\,\mathrm{PW}")
q_G = z("c) Wärmestromdichte ganzer Gürtel", Q_AMOC / A_G, "W/m²", r"\dot{q}_G = " + de(Q_AMOC / A_G, 1) + r"\,\mathrm{W/m^2}")
q_V = z("c) Wärmestromdichte Viertel", Q_AMOC / A_V, "W/m²", r"\dot{q}_V = " + de(Q_AMOC / A_V, 1) + r"\,\mathrm{W/m^2}")
q_abs = z("d) absorbierte Sonne (1 - rho_p) q_S", (1 - ALB) * Q_S, "W/m²", r"\dot{q}_{abs} = " + de((1 - ALB) * Q_S, 1) + r"\,\mathrm{W/m^2}")
T_e = (q_abs / SIGMA) ** 0.25
z("d) ohne Atmosphäre: theta_e", T_e - K0, "°C", r"\vartheta_e = " + de(T_e - K0, 1) + r"\,\mathrm{°C}")
T_O = T_e * (2 / (2 - EPS)) ** 0.25
z("d) Schichtmodell: theta_O", T_O - K0, "°C", r"\vartheta_O = " + de(T_O - K0, 1) + r"\,\mathrm{°C}")
f_atm = 1 - EPS / 2
T_PB = TH_PB + K0
E_PB = z("e) Abstrahlung bei +2,1 °C, sigma (1 - eps/2) T^4", SIGMA * f_atm * T_PB**4, "W/m²", de(SIGMA * f_atm * T_PB**4, 1) + r"\,\mathrm{W/m^2}")
q_zu = z("e) nötige zusätzliche Wärmezufuhr", E_PB - q_abs, "W/m²", r"\dot{q}_{zu} = " + de(E_PB - q_abs, 1) + r"\,\mathrm{W/m^2}")
z("e) AMOC-Anteil, Gürtel", q_G / q_zu * 100, "%", f"{q_G / q_zu * 100:.0f}" + r"\,\%")
z("e) AMOC-Anteil, Viertel", q_V / q_zu * 100, "%", f"{q_V / q_zu * 100:.0f}" + r"\,\%")
anteile = []
for a2 in (0.3, 0.5):
    qi = E_PB - (1 - a2) * Q_S
    z(f"e) nötige Zufuhr bei Albedo {a2:.1f}", qi, "W/m²", de(qi, 1))
    anteile += [q_G / qi * 100, q_V / qi * 100]
    z(f"   AMOC-Anteil bei Albedo {a2:.1f}, Gürtel", q_G / qi * 100, "%", f"{q_G / qi * 100:.0f}")
    z(f"   AMOC-Anteil bei Albedo {a2:.1f}, Viertel", q_V / qi * 100, "%", f"{q_V / qi * 100:.0f}")
z("e) Spanne der Anteile bei Albedo 0,3 bis 0,5, kleinster Wert", min(anteile), "%", f"{min(anteile):.0f}")
z("e) Spanne der Anteile bei Albedo 0,3 bis 0,5, größter Wert", max(anteile), "%", f"{max(anteile):.0f}" + r"\,\%")
z("f) Summe nach Seager et al. (2002): 54 + 11 + 53", 54 + 11 + 53, "W/m²", f"{54 + 11 + 53}" + r"\,\mathrm{W/m^2}")
a_S = z("g) alpha_S = 4 sigma T^3 (1 - eps/2) bei +2,1 °C", 4 * SIGMA * T_PB**3 * f_atm, "W/(m² K)", r"\alpha_S = " + de(4 * SIGMA * T_PB**3 * f_atm) + r"\,\mathrm{W/(m^2\,K)}")
z("g) Unterschied Paderborn gegen Goose Bay (nur Info)", TH_PB - TH_GB, "K", None)
z("g) (1) ganze AMOC-Wärme, Gürtel", q_G / a_S, "K", r"\Delta T_G = " + de(q_G / a_S, 1) + r"\,\mathrm{K}")
z("g) (1) ganze AMOC-Wärme, Viertel", q_V / a_S, "K", r"\Delta T_V = " + de(q_V / a_S, 1) + r"\,\mathrm{K}")
dQ = -0.2 * Q_AMOC
dq_G = z("g) (2) -20 %: Änderung der Zufuhr, Gürtel", dQ / A_G, "W/m²", r"\Delta\dot{q}_G = " + de(dQ / A_G, 1) + r"\,\mathrm{W/m^2}")
dq_V = z("g) (2) -20 %: Änderung der Zufuhr, Viertel", dQ / A_V, "W/m²", r"\Delta\dot{q}_V = " + de(dQ / A_V, 1) + r"\,\mathrm{W/m^2}")
z("g) (2) -20 %: Temperaturänderung, Gürtel", dq_G / a_S, "K", r"\Delta T_G = " + de(dq_G / a_S, 1) + r"\,\mathrm{K}")
z("g) (2) -20 %: Temperaturänderung, Viertel", dq_V / a_S, "K", r"\Delta T_V = " + de(dq_V / a_S, 1) + r"\,\mathrm{K}")
for h in (100.0, 350.0):
    C = z(f"h) Deckschicht {h:.0f} m: C = rho cp h", RHO_M * CP_M * h, "J/(m² K)", r"C = " + de10(RHO_M * CP_M * h) + r"\,\mathrm{J/(m^2\,K)}")
    tau = z(f"h) Deckschicht {h:.0f} m: tau = C / alpha_S", C / a_S / JAHR, "Jahre", r"\tau = " + de(C / a_S / JAHR, 1) + r"\,\mathrm{Jahre}") * JAHR
    z(f"h) Deckschicht {h:.0f} m: Anteil nach 10 Jahren", (1 - math.exp(-10 * JAHR / tau)) * 100, "%", f"{(1 - math.exp(-10 * JAHR / tau)) * 100:.0f}" + r"\,\%")

# =============================================================================
neu("Aufgabe 3: Der Ozean als Wärmespeicher (Tabellenwerte)")
h_D = z("Tiefe der Deckschicht", 70.0, "m", r"h = 70\,\mathrm{m}")
LAM_M = z("Wärmeleitfähigkeit Meerwasser", 0.6, "W/(m K)", r"\lambda_M = 0{,}6\,\mathrm{W/(m\,K)}")
q_F = z("zusätzliche Strahlungsflussdichte (CO2 verdoppelt)", 3.93, "W/m²", r"\dot{q}_F = 3{,}93\,\mathrm{W/m^2}")
a_eff = z("effektiver Abgabekoeffizient", 1.3, "W/(m² K)", r"\alpha_{eff} = 1{,}3\,\mathrm{W/(m^2\,K)}")
gam = z("Abgabe an die Tiefsee", 0.7, "W/(m² K)", r"\gamma = 0{,}7\,\mathrm{W/(m^2\,K)}")
T_e4 = z("Emissionstemperatur der Erde (Tutorium 4)", 254.6, "K", r"T_e = 254{,}6\,\mathrm{K}")
h_B = z("Bodenschicht (Vergleich)", 2.0, "m", r"h_B = 2\,\mathrm{m}")
rc_B = z("vol. Wärmekapazität Boden", 2.2, "MJ/(m³ K)", r"\rho_B c_B = 2{,}2\,\mathrm{MJ/(m^3\,K)}") * 1e6

neu("Aufgabe 3: Ergebnisse")
C_D = z("c) C = rho cp h", RHO_M * CP_M * h_D, "J/(m² K)", r"C = " + de10(RHO_M * CP_M * h_D) + r"\,\mathrm{J/(m^2\,K)}")
C_B = z("c) C_B = rho_B c_B h_B", rc_B * h_B, "J/(m² K)", r"C_B = " + de10(rc_B * h_B, 1) + r"\,\mathrm{J/(m^2\,K)}")
z("c) Verhältnis C / C_B", C_D / C_B, "-", r"C/C_B = " + f"{C_D / C_B:.0f}")
tau1 = z("e) tau = C / alpha_eff", C_D / a_eff / JAHR, "Jahre", r"\tau = " + de(C_D / a_eff / JAHR) + r"\,\mathrm{Jahre}") * JAHR
z("e) Erwärmung nach 10 Jahren", q_F / a_eff * (1 - math.exp(-10 * JAHR / tau1)), "K", r"\Delta T(10\,\mathrm{Jahre}) = " + de(q_F / a_eff * (1 - math.exp(-10 * JAHR / tau1))) + r"\,\mathrm{K}")
z("e) Endwert q_F / alpha_eff", q_F / a_eff, "K", r"\Delta T_\infty = " + de(q_F / a_eff) + r"\,\mathrm{K}")
a_S4 = z("f) alpha_S = 4 sigma T_e^3", 4 * SIGMA * T_e4**3, "W/(m² K)", r"\alpha_S = " + de(4 * SIGMA * T_e4**3) + r"\,\mathrm{W/(m^2\,K)}")
z("f) tau mit alpha_S", C_D / a_S4 / JAHR, "Jahre", r"\tau = " + de(C_D / a_S4 / JAHR) + r"\,\mathrm{Jahre}")
z("f) Endwert mit alpha_S", q_F / a_S4, "K", r"\Delta T_\infty = " + de(q_F / a_S4) + r"\,\mathrm{K}")
a_M = z("g) Temperaturleitfähigkeit a = lambda / (rho cp)", LAM_M / (RHO_M * CP_M), "m²/s", r"a = " + de10(LAM_M / (RHO_M * CP_M)) + r"\,\mathrm{m^2/s}")
t_L = z("g) Leitzeit t ~ h² / a", h_D**2 / a_M / JAHR, "Jahre", r"t \approx " + de10(h_D**2 / a_M / JAHR, 1) + r"\,\mathrm{Jahre}")
z("g) tau mit Tiefsee, C / (alpha_eff + gamma)", C_D / (a_eff + gam) / JAHR, "Jahre", r"\tau = " + de(C_D / (a_eff + gam) / JAHR) + r"\,\mathrm{Jahre}")
z("g) Endwert mit Tiefsee", q_F / (a_eff + gam), "K", r"\Delta T_\infty = " + de(q_F / (a_eff + gam)) + r"\,\mathrm{K}")

# =============================================================================
neu("Aufgabe 4: Sverdrup und der Amazonas (Tabellenwerte)")
V_P = z("Pader", 5.0, "m³/s", r"\dot{V}_P = 5\,\mathrm{m^3/s}")
V_W = z("Weser (Intschede)", 313.0, "m³/s", r"\dot{V}_W = 313\,\mathrm{m^3/s}")
V_R = z("Rhein (Rees)", 2260.0, "m³/s", r"\dot{V}_R = 2260\,\mathrm{m^3/s}")
V_A = z("Amazonas (Mündung)", 206000.0, "m³/s", r"\dot{V}_A = 206\,000\,\mathrm{m^3/s}")
z("alle Flüsse der Erde", 1.18, "Sv", r"\dot{V}_{Fl} = 1{,}18\,\mathrm{Sv}")
V_AM2 = z("AMOC", 17.0, "Sv", r"\dot{V}_{AMOC} = 17\,\mathrm{Sv}") * SV
RHO_F = z("Dichte Süßwasser", 1000.0, "kg/m³", r"\rho_W = 1000\,\mathrm{kg/m^3}")
CP_F = z("spez. Wärmekapazität Süßwasser", 4180.0, "J/(kg K)", r"c_{p,W} = 4180\,\mathrm{J/(kg\,K)}")
DH_V = z("Verdampfungsenthalpie bei 30 °C", 2.43, "MJ/kg", r"\Delta h_v = 2{,}43\,\mathrm{MJ/kg}") * 1e6
z("Temperatur Unterlauf, untere Grenze", 27.5, "°C", r"\vartheta_A = 27{,}5")
z("Temperatur Unterlauf, obere Grenze", 28.5, "°C", r"28{,}5\,\mathrm{°C}")
z("Temperatur der Flussfahne", 28.5, "°C", r"\vartheta_F = 28{,}5\,\mathrm{°C}")
A_B = z("Fläche des Beckens", 6e12, "m²", r"A_B = 6\cdot 10^{12}\,\mathrm{m^2}")
N_B = z("Niederschlag auf das Becken", 2200.0, "mm/a", r"N = 2200\,\mathrm{mm/a}") / 1000.0
Q_MEN = z("Energieumsatz der Menschheit", 19.0, "TW", r"\dot{Q}_{M} = 19\,\mathrm{TW}") * 1e12

neu("Aufgabe 4: Ergebnisse")
z("a) Pader in Sv", V_P / SV, "Sv", r"5\cdot 10^{-6}")
z("a) Weser in Sv", V_W / SV, "Sv", de10(V_W / SV))
z("a) Rhein in Sv", V_R / SV, "Sv", de10(V_R / SV))
z("a) Amazonas in Sv", V_A / SV, "Sv", de(V_A / SV, 3) + r"\,\mathrm{Sv}")
z("a) Amazonas / Rhein", V_A / V_R, "-", r"\dot{V}_A/\dot{V}_R = " + f"{V_A / V_R:.0f}")
z("a) AMOC / Amazonas", V_AM2 / V_A, "-", r"\dot{V}_{AMOC}/\dot{V}_A = " + de(V_AM2 / V_A, 1))
C_A = z("b) Wärmekapazitätsstrom Amazonas", RHO_F * V_A * CP_F / 1e12, "TW/K", r"\dot{C}_A = " + de(RHO_F * V_A * CP_F / 1e12, 3) + r"\,\mathrm{TW/K}") * 1e12
Q_max = z("b) Wärmestrom Fluss gegen Meer höchstens (1 K)", C_A * 1.0 / 1e12, "TW", r"|\dot{Q}| \leq " + de(C_A * 1.0 / 1e12, 3) + r"\,\mathrm{TW}") * 1e12
z("b) nötiger Überschuss für 19 TW", Q_MEN / C_A, "K", r"\Delta T = " + de(Q_MEN / C_A, 1) + r"\,\mathrm{K}")
V_N = z("c) Niederschlag als Volumenstrom", A_B * N_B / JAHR / SV, "Sv", r"\dot{V}_N = " + de(A_B * N_B / JAHR / SV, 3) + r"\,\mathrm{Sv}") * SV
V_ET = z("c) Verdunstung = Niederschlag - Abfluss", (V_N - V_A) / SV, "Sv", r"\dot{V}_V = " + de((V_N - V_A) / SV, 3) + r"\,\mathrm{Sv}") * SV
ET = z("c) Verdunstung je Fläche", V_ET / A_B * JAHR * 1000, "mm/a", f"{V_ET / A_B * JAHR * 1000:.0f}" + r"\,\mathrm{mm/a}") / 1000
z("c) Abweichung vom Messwert 1083 mm/a", (ET * 1000 - 1083) / 1083 * 100, "%", f"{(ET * 1000 - 1083) / 1083 * 100:.0f}" + r"\,\%")
q_lat = z("d) latente Wärmestromdichte rho (ET/Jahr) dh_v", RHO_F * ET / JAHR * DH_V, "W/m²", r"\dot{q}_V = " + f"{RHO_F * ET / JAHR * DH_V:.0f}" + r"\,\mathrm{W/m^2}")
Q_lat = z("d) latenter Wärmestrom des Beckens", q_lat * A_B / 1e12, "TW", r"\dot{Q}_V = " + f"{q_lat * A_B / 1e12:.0f}" + r"\,\mathrm{TW}") * 1e12
z("d) Vielfaches des Energieumsatzes der Menschheit", Q_lat / Q_MEN, "-", r"\dot{Q}_V/\dot{Q}_M = " + f"{Q_lat / Q_MEN:.0f}")
z("d) Vielfaches des Wärmestroms aus b)", Q_lat / Q_max, "-", r"\dot{Q}_V/|\dot{Q}| = " + f"{Q_lat / Q_max:.0f}")
z("d) Anteil an 153 W/m² Nettostrahlung", q_lat / 153 * 100, "%", f"{q_lat / 153 * 100:.0f}")
z("d) Anteil an 117 W/m² Nettostrahlung", q_lat / 117 * 100, "%", f"{q_lat / 117 * 100:.0f}" + r"\,\%")

# =============================================================================
neu("Zusatzaufgabe 1: Kraftwerk am Fluss")
Q_KW = z("Abwärme", 2.0, "GW", r"\dot{Q} = 2\,\mathrm{GW}") * 1e9
V_FL = z("Volumenstrom des Flusses", 200.0, "m³/s", r"\dot{V} = 200\,\mathrm{m^3/s}")
z("Dichte Flusswasser", 1000.0, "kg/m³", r"\rho = 1000\,\mathrm{kg/m^3}")
z("spez. Wärmekapazität Flusswasser", 4.18, "kJ/(kg K)", r"c_p = 4{,}18\,\mathrm{kJ/(kg\,K)}")
TH_FL = z("Flusstemperatur im Hitzesommer", 26.0, "°C", r"\vartheta_{ein} = 26\,\mathrm{°C}")
dT_KW = z("a) Erwärmung des Flusses", Q_KW / (1000.0 * V_FL * 4180.0), "K", r"\Delta T = " + de(Q_KW / (1000.0 * V_FL * 4180.0)) + r"\,\mathrm{K}")
z("b) Temperatur hinter dem Kraftwerk", TH_FL + dT_KW, "°C", r"\vartheta_{aus} = " + de(TH_FL + dT_KW) + r"\,\mathrm{°C}")

# =============================================================================
neu("Zusatzaufgabe 2: Eisberg")
L_E = z("Kantenlänge (Fläche 1 km²)", 1000.0, "m", r"1\,\mathrm{km}")
H_E = z("Dicke", 250.0, "m", r"H = 250\,\mathrm{m}")
RHO_E = z("Dichte Eis", 917.0, "kg/m³", r"\rho_E = 917\,\mathrm{kg/m^3}")
# Tiefgang aus dem Auftrieb mit Meerwasser aus Aufgabe 2 (rho_M); im Text als gerundeter Wert gegeben
h_T_auftrieb = z("Tiefgang aus dem Auftrieb H rho_E / rho_M (nur Info)", H_E * RHO_E / RHO_M, "m", None)
T_G = z("Tiefgang, gerundet (im Text gegeben)", float(round(h_T_auftrieb)), "m",
        r"h_T = " + f"{round(h_T_auftrieb):.0f}" + r"\,\mathrm{m}")
DH_S = z("Schmelzenthalpie", 333.5, "kJ/kg", r"\Delta h_s = 333{,}5\,\mathrm{kJ/kg}") * 1e3
m_E = z("a) Masse", RHO_E * L_E**2 * H_E, "kg", r"m_E = " + de10(RHO_E * L_E**2 * H_E) + r"\,\mathrm{kg}")
Q_E = z("a) Schmelzwärme", m_E * DH_S, "J", r"Q = " + de10(m_E * DH_S) + r"\,\mathrm{J}")
A_E = z("b) Fläche unter Wasser (Unterseite + Seiten)", L_E**2 + 4 * L_E * T_G, "m²", r"A = " + de10(L_E**2 + 4 * L_E * T_G) + r"\,\mathrm{m^2}")
t_schmelz = []
for a_W, dT, name, dativ in ((20.0, 2.0, "kleinster", "kleinsten"), (50.0, 3.0, "größter", "größten")):
    Qp = a_W * A_E * dT
    z(f"b) {name} Wärmestrom (alpha {a_W:.0f}, dT {dT:.0f} K)", Qp / 1e6, "MW", (de(Qp / 1e6, 1) if Qp < 1e8 else f"{Qp / 1e6:.0f}") + (r"\,\mathrm{MW}" if Qp > 1e8 else ""))
    t_schmelz.append(z(f"b) Schmelzzeit beim {dativ} Wärmestrom", Q_E / Qp / JAHR, "Jahre", de(Q_E / Qp / JAHR, 1) + r"\,\mathrm{Jahre}"))

# =============================================================================
# Abgleich mit den Kernzahlen der Ausgangsdokumente
abgleich = [
    ("A b) Massenstrom 1,74e10 kg/s", 1.742e10, m_AMOC),
    ("A c) Ċ 69,5 TW/K", 69.5e12, C_AMOC),
    ("A c) ΔT 17,3 K", 17.3, dT_AMOC),
    ("A d) Gürtel 15,8 W/m² (genaue Fläche 7,572e13 m²)", 15.8, q_G),
    ("A d) Viertel 63,4 W/m² (genaue Fläche 1,893e13 m²)", 63.4, q_V),
    ("A f) nötig 142,7 W/m²", 142.7, q_zu),
    ("A h) lambda 2,885 W/(m² K)", 2.885, a_S),
    ("A h) -20 %: Viertel -12,7 W/m²", -12.7, dq_V),
    ("4.5 tau 6,98 Jahre (alpha_eff 1,3)", 6.98, tau1 / JAHR),
    ("4.5 Leitzeit 1083 Jahre (Süßwasser 1000 kg/m³, 4186 J/(kg K))", 1083.0, t_L),
    ("B2 Ċ 0,86 TW/K", 0.86e12, C_A),
    ("B3 Verdunstung 1117 mm/a", 1117.0, ET * 1000),
    ("B4 86 W/m²", 86.0, q_lat),
    ("Kraftwerk 2,39 K (c_p 4186)", 2.39, dT_KW),
    ("4.5 Eisberg 32,2 a (dort Tiefgang 0,88 H = 220 m)", 32.2, t_schmelz[0]),
    ("4.5 Eisberg 8,6 a (dort Tiefgang 0,88 H = 220 m)", 8.6, t_schmelz[1]),
]


def schreiben():
    out = ["Tutorium 5, Aufgaben 2 bis 4 und Zusatzaufgaben 1 und 2 (Ozean und Fluss)",
           "Erzeugt von t5_rechnung.py. Spalten: Name, Wert, Einheit, Anzeige im Markdown.", ""]
    for abschnitt, name, wert, einheit, anzeige in zeilen:
        if name is None:
            out += ["", "== " + abschnitt + " =="]
            continue
        w = f"{wert:12.4g}" if (abs(wert) >= 1e5 or (abs(wert) < 1e-2 and wert != 0)) else f"{wert:12.4f}"
        out.append(f"{name:58s} {w} {einheit:10s} {anzeige if anzeige else '(nur Info, nicht im Text)'}")
    out += ["", "== Abgleich mit den Kernzahlen der Ausgangsdokumente (Quelle, neu, Abweichung) =="]
    for name, alt, neu_w in abgleich:
        out.append(f"{name:62s} {alt:12.4g} {neu_w:12.4g} {100 * (neu_w - alt) / alt:+6.1f} %")
    return "\n".join(out) + "\n"


def pruefe_markdown():
    """Prüft, ob jede Anzeige im Markdown vorkommt (Ergebniszeilen und Tabellen)."""
    if not os.path.exists(MD):
        return ["(teile/t5b_ozean.md fehlt noch)"]
    with open(MD, encoding="utf-8") as f:
        text = f.read()
    return [f"fehlt im Markdown: {name}: {anzeige}" for _, name, _, _, anzeige in zeilen
            if name is not None and anzeige is not None and anzeige not in text]


if __name__ == "__main__":
    txt = schreiben()
    with open(AUSGABE, "w", encoding="utf-8") as f:
        f.write(txt)
    print(txt)
    fehler = pruefe_markdown()
    print("Prüfung Markdown:", "alle Anzeigen gefunden" if not fehler else "\n" + "\n".join(fehler))
