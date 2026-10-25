# -*- coding: utf-8 -*-
"""Tutorium 4 (Strahlung) der Aufgabensammlung: alle Zahlen der Tabellen und Ergebniszeilen.

Aufgabe 1: Die Strahlungsbilanz der Erde (Ideensammlung 4.4, Teile a bis i)
Zusatzaufgabe 1: Eis aus der Nacht (Ideensammlung 4.4, Zusatzaufgaben)
Zusatzaufgabe 2: Autoscheibe und Reif (bisherige Vorab-Frage als Kurzrechnung; -5 °C und Glas mit
                 epsilon = 0,95 wie in V08 Teil g; die -5 °C gelten als wirksame Temperatur der Umgebung
                 aus klarem Himmel, Häusern und Bäumen, die die schräge Scheibe sieht)

Eingabewerte wie im Aufgabenblatt (teile/t4.md). Arbeitswerte aus der Ideensammlung „Leitaufgaben
aus Klima und Erde“ (17.10.2026) und aus nachrechnung_leitphaenomene.py; Messwerte der globalen
Energiebilanz nach Forster et al. (2021), Abb. 7.2. sigma wie in V04 F. 10.

Aufruf: python3 t4_rechnung.py   (schreibt t4_rechnung_ausgabe.txt in diesen Ordner)
"""
import os

HIER = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(os.path.dirname(HIER), "teile", "t4.md")
AUS = []                                   # (Name, Wert, Einheit, Anzeige im Blatt, im Text?)
K = 273.15
SIGMA = 5.6705e-8                          # W/(m² K⁴), V04 F. 10


def de(x, n=2):
    return f"{x:.{n}f}".replace(".", ",")


def merke(name, wert, einheit, n, im_text=True):
    """im_text=False: nur Info oder Kontrolle, steht nicht im Blatt."""
    AUS.append((name, wert, einheit, de(wert, n), im_text))
    return wert


def kopf(text):
    AUS.append((None, text, None, None, False))


def gleichgewicht(eps, th_H, th_L, alpha, lo=-60.0, hi=None):
    """Temperatur (°C) einer Oberfläche, die nur Strahlung mit dem Himmel (schwarz, th_H) und
    Konvektion mit der Luft (th_L, alpha) austauscht: eps sigma (T^4 - T_H^4) = alpha (T_L - T)."""
    hi = th_L if hi is None else hi
    for _ in range(200):                   # Bisektion
        m = 0.5 * (lo + hi)
        f = eps * SIGMA * ((m + K)**4 - (th_H + K)**4) - alpha * (th_L - m)
        lo, hi = (lo, m) if f > 0 else (m, hi)
    return 0.5 * (lo + hi)


# =====================================================================================
# Aufgabe 1: Die Strahlungsbilanz der Erde
# =====================================================================================
S0, rho_p, T_O, q_E = 1361.0, 0.30, 288.0, 0.09      # W/m², -, K, W/m²
dq_CO2 = 3.93                                        # W/m², Verdopplung von CO2 (Forster et al., 2021)
q_G_mess, q_O_mess, q_konv, q_verd = 342.0, 398.0, 21.0, 82.0   # W/m², Forster et al. (2021), Abb. 7.2

kopf("Aufgabe 1: Die Strahlungsbilanz der Erde (Tabellenwerte)")
merke("Solarkonstante S0", S0, "W/m²", 0)
merke("planetare Albedo rho_p", rho_p, "-", 2)
merke("Mitteltemperatur der Oberfläche T_O", T_O, "K", 0)
merke("Erdwärme q_E", q_E, "W/m²", 2)
merke("Strahlungsantrieb bei Verdopplung von CO2", dq_CO2, "W/m²", 2)
merke("Stefan-Boltzmann-Konstante (Anzeige 5,6705e-8)", SIGMA * 1e8, "1e-8 W/(m² K⁴)", 4)
kopf("Aufgabe 1: Ergebnisse")
merke("a) S0/4", S0 / 4, "W/m²", 0)
q_abs = merke("c) absorbiert q_abs = S0 (1 - rho_p)/4", S0 * (1 - rho_p) / 4, "W/m²", 0)
T_e = merke("d) T_e = (q_abs/sigma)^(1/4)", (q_abs / SIGMA)**0.25, "K", 1)
merke("d) T_e in °C", T_e - K, "°C", 1)
T_E = merke("d) nur Erdwärme 0,09 W/m²: T", (q_E / SIGMA)**0.25, "K", 1)
merke("d) nur Erdwärme in °C", T_E - K, "°C", 0, im_text=False)
merke("d) Verhältnis q_abs / q_E", q_abs / q_E, "-", 0, im_text=False)
eps_A = merke("f) eps_A für T_O = 288 K: 2 (1 - (T_e/T_O)^4)", 2 * (1 - (T_e / T_O)**4), "-", 2)
T_A = merke("f) T_A = T_O / 2^(1/4)", T_O / 2**0.25, "K", 1)
merke("f) Kontrolle: T_O mit eps_A = 0,78", T_e * (2 / (2 - 0.78))**0.25, "K", 1, im_text=False)
merke("g) Grenzfall eps_A = 0: T_O", T_e * (2 / (2 - 0.0))**0.25, "K", 1)
merke("g) Grenzfall eps_A = 1: T_O", T_e * (2 / (2 - 1.0))**0.25, "K", 1)
q_G = merke("g) Gegenstrahlung im Modell eps_A sigma T_A^4", eps_A * SIGMA * T_A**4, "W/m²", 0)
merke("g) Gegenstrahlung mit eps_A = 0,78 (gerundet)", 0.78 * SIGMA * T_A**4, "W/m²", 0)
merke("g) Abstrahlung der Oberfläche im Modell sigma T_O^4", SIGMA * T_O**4, "W/m²", 0, im_text=False)
merke("g) Anteil (Konvektion + Verdunstung)/Abstrahlung (gemessen)", (q_konv + q_verd) / q_O_mess * 100, "%", 0)
q_S_atm = 80.0                                       # W/m², von der Atmosphäre absorbierte Sonnenstrahlung (Forster)
merke("g) Info: Sonne an der Oberfläche q_abs - 80", q_abs - q_S_atm, "W/m²", 0, im_text=False)
merke("g) Info: Oberflächenbilanz mit Messwerten (q_abs - 80) + 342 - 398 - 21 - 82",
      q_abs - q_S_atm + q_G_mess - q_O_mess - q_konv - q_verd, "W/m²", 0, im_text=False)
merke("g) Info: Lücke gemessen - Modell, 342 - q_G", q_G_mess - q_G, "W/m²", 0, im_text=False)
merke("g) Info: Erklärung 80 + 21 + 82 + (398 - sigma T_O^4)", q_S_atm + q_konv + q_verd + (q_O_mess - SIGMA * T_O**4),
      "W/m²", 0, im_text=False)
lam_P = merke("h) 4 sigma T_e^3", 4 * SIGMA * T_e**3, "W/(m² K)", 2)
dT_2x = merke("h) Delta T = Delta q / (4 sigma T_e^3)", dq_CO2 / lam_P, "K", 2)

# Kernzahlen der Ideensammlung (Abschnitt 4.4) zur Kontrolle
assert round(S0 / 4) == 340 and round(q_abs) == 238 and abs(T_e - 254.6) < 0.05 and abs(T_e - K + 18.6) < 0.05
assert abs(eps_A - 0.78) < 0.005 and round(T_A) == 242 and abs(T_e * 2**0.25 - 302.7) < 0.05
assert abs(lam_P - 3.74) < 0.005 and abs(dT_2x - 1.05) < 0.005

# =====================================================================================
# Zusatzaufgabe 1: Eis aus der Nacht (Wasser eps = 0,96 wie in nachrechnung_leitphaenomene.py)
# =====================================================================================
kopf("Zusatzaufgabe 1: Eis aus der Nacht (Luft 5 °C, Himmel -20 °C, eps = 0,96)")
for a in (2.0, 5.0):
    th = merke(f"b) Gleichgewicht für alpha_L = {de(a, 0)} W/(m² K)", gleichgewicht(0.96, -20.0, 5.0, a), "°C", 1)
    assert th < 0
q_str0 = merke("Info: Nettoabstrahlung bei 0 °C", 0.96 * SIGMA * (K**4 - (K - 20.0)**4), "W/m²", 0, im_text=False)

# =====================================================================================
# Zusatzaufgabe 2: Autoscheibe und Reif (Glas eps = 0,95, Umgebung -5 °C wie in V08 Teil g)
# =====================================================================================
kopf("Zusatzaufgabe 2: Autoscheibe und Reif (Scheibe 0 °C, Umgebung aus Himmel, Häusern, Bäumen -5 °C, eps = 0,95)")
q_S = merke("a) Nettoabstrahlung der Scheibe bei 0 °C", 0.95 * SIGMA * (K**4 - (K - 5.0)**4), "W/m²", 1, im_text=False)
for a in (5.0, 10.0):
    th_grenz = merke(f"a/b) Grenz-Lufttemperatur für alpha_L = {de(a, 0)} W/(m² K)", 0.0 + q_S / a, "°C", 2)
    # Kontrolle: bei dieser Lufttemperatur hat die Scheibe genau 0 °C
    assert abs(gleichgewicht(0.95, -5.0, th_grenz, a)) < 1e-6

# =====================================================================================
with open(os.path.join(HIER, "t4_rechnung_ausgabe.txt"), "w", encoding="utf-8") as f:
    f.write("Tutorium 4: Strahlung (Zahlen der Tabellen und Ergebniszeilen; Spalte „Blatt“ = Anzeige im Blatt,\n"
            "„nur Info“ = Kontrolle oder Hilfswert, steht nicht im Blatt)\n")
    for name, wert, einheit, blatt, im_text in AUS:
        if name is None:
            f.write(f"\n{wert}\n")
        else:
            f.write(f"{name:66s} {wert:12.4f} {einheit:10s} {'Blatt: ' + blatt if im_text else 'nur Info'}\n")
print(open(os.path.join(HIER, "t4_rechnung_ausgabe.txt"), encoding="utf-8").read())

# Abgleich mit dem Blatt: jede Anzeige (Dezimalkomma als {,}) muss in teile/t4.md vorkommen
if os.path.exists(MD):
    text = open(MD, encoding="utf-8").read()
    fehlt = [f"{name}: {blatt}" for name, _, _, blatt, im_text in AUS
             if name is not None and im_text and blatt.replace(",", "{,}") not in text]
    print("Prüfung Markdown:", "alle Anzeigen gefunden" if not fehlt else "\nfehlt: " + "\nfehlt: ".join(fehlt))
    assert not fehlt
