# -*- coding: utf-8 -*-
"""Tutorium 1 (Wärmeleitung) der Aufgabensammlung: alle Zahlen der Tabellen und Ergebniszeilen in ../teile/t1.md.

Aufgabe 1 (Seen unter dem Eisschild) und Aufgabe 2 (Kühlhauswand): Arbeitswerte und Formeln wie im Pilotskript
pilot_tutorium1.py (Pilotblatt Tutorium 1, 17.10.2026) (hier nachgebaut). Zusatzaufgabe 1 (Erdwärme in Deutschland): Arbeitswerte
aus der Ideensammlung, Abschnitt 4.1 (Gradient 28 K/km, lambda 2,9 W/(m K)), wie in nachrechnung_leitphaenomene.py.
Mittlere Wärmeleitfähigkeit als Integralmittel über die Temperatur (V02 F. 12).

Aufruf: python3 t1_rechnung.py
Schreibt t1_rechnung_ausgabe.txt (Name, Wert, Einheit) und prüft am Ende, ob jede Ergebniszeile und jeder Tabellenwert
genau so in ../teile/t1.md steht.
"""
import math
import os
import sys as _sys, os as _os
_sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), "build"))
from indizes_aufrecht import ohne_mathrm   # Schreibweise prüfen unabhängig davon, ob Indizes aufrecht oder kursiv stehen

HIER = os.path.dirname(os.path.abspath(__file__))
TEIL = os.path.join(os.path.dirname(HIER), "teile", "t1.md")
AUSGABE = os.path.join(HIER, "t1_rechnung_ausgabe.txt")

K = 273.15
G = 9.81                    # m/s²
JAHR = 365.25 * 86400.0     # s

# ----------------------------------------------------------------------------- Aufgabe 1: gegebene Größen
H = 3700.0                  # m Eisdicke
th_O = -55.0                # °C Oberfläche (Jahresmittel)
q_E = 0.058                 # W/m² Wärmestromdichte aus dem Erdinneren (Dome C, Talalay et al. 2020)
a_L, b_L = 9.828, 5.7e-3    # lambda(T) = a exp(-b T), T in K (Cuffey & Paterson 2010)
rho = 917.0                 # kg/m³ Eis
dh_schm = 333.5e3           # J/kg Schmelzenthalpie
k_pm = 0.0742               # K/MPa Schmelzpunktsenkung (reines Eis)
s_F, lam_F = 100.0, 1.0     # m, W/(m K) Firn
z1, th1 = 3200.0, -4.2      # m, °C Bohrloch EPICA Dome C (Augustin et al. 2007)
z2, th2 = 3270.2, -2.34     # m, °C tiefster Messpunkt


def lam(th_C):
    """Wärmeleitfähigkeit von Eis bei der Celsius-Temperatur th_C."""
    return a_L * math.exp(-b_L * (th_C + K))


def lam_m(th1_C, th2_C):
    """Integralmittel 1/(T1 - T2) * Integral lambda(T) dT von T2 bis T1."""
    T1, T2 = th1_C + K, th2_C + K
    return a_L / (b_L * (T1 - T2)) * (math.exp(-b_L * T2) - math.exp(-b_L * T1))


# d) Wärmeleitfähigkeiten
lam_O = lam(th_O)
lam_0 = lam(0.0)
lm = lam_m(0.0, th_O)
# e) Basis, wenn alles geleitet wird
th_B = th_O + q_E * H / lm
grad_e = q_E / lm                                   # K/m
# f) Druck und Druckschmelzpunkt
p = rho * G * H                                     # Pa
th_pm = -k_pm * p / 1e6
# g) Basis am Druckschmelzpunkt
q_leit = lm * (th_pm - th_O) / H
q_rest = q_E - q_leit
v_schm = q_rest / (rho * dh_schm)                   # m/s
v_schm_a = v_schm * JAHR * 1e3                      # mm/a
# h1) Mindestdicke (Schmelzpunkt aus f, lambda_m aus d)
H_krit = lm * (th_pm - th_O) / q_E
H_it = H_krit
for _ in range(40):                                 # nur Kontrolle: Schmelzpunkt in der gesuchten Tiefe
    th_pm_H = -k_pm * rho * G * H_it / 1e6
    H_it = lam_m(th_pm_H, th_O) * (th_pm_H - th_O) / q_E
# h2) Firn und Eis
faktor_firn = lm / lam_F
grad_F = q_leit / lam_F
grad_I = q_leit / lm
# h3) Dome C
grad_C = (th2 - th1) / (z2 - z1)                    # K/m
lam_m3 = lam(-3.0)
q_C = lam_m3 * grad_C
p_C = rho * G * z2
th_pm_C = -k_pm * p_C / 1e6
luecke = th_pm_C - th2
dz_C = luecke / grad_C

# ----------------------------------------------------------------------------- Aufgabe 2: Kühlhauswand
th_a, th_i = 28.0, -22.0    # °C Oberflächentemperaturen außen und innen
s_B, lam_B = 0.20, 2.3      # m, W/(m K) Stahlbeton
s_D, lam_D = 0.12, 0.025    # m, W/(m K) PUR-Hartschaum
A_W = 250.0                 # m²
q_max = 8.0                 # W/m²
R_B, R_D = s_B / lam_B, s_D / lam_D
q_W = (th_a - th_i) / (R_B + R_D)
Q_W = q_W * A_W
th_G = th_a - q_W * R_B
faktor_W = lam_B / lam_D
anteil_B = R_B / (R_B + R_D)
s_D_min = lam_D * ((th_a - th_i) / q_max - R_B)
s_D_gew = math.ceil(round(s_D_min * 100, 6)) / 100  # auf ganze Zentimeter aufgerundet
q_gew = (th_a - th_i) / (R_B + s_D_gew / lam_D)
q_2B = (th_a - th_i) / (2 * R_B + R_D)

# ----------------------------------------------------------------------------- Zusatzaufgabe 1: Erdwärme in Deutschland
grad_KTB = 0.028            # K/m (28 K/km)
lam_KTB = 2.9               # W/(m K)
z_KTB = 9101.0              # m Endteufe
q_KTB = lam_KTB * grad_KTB
v_q = q_KTB / q_E
v_lam = lam_KTB / lm
dT_KTB = grad_KTB * z_KTB


# ----------------------------------------------------------------------------- Ausgabe
def de(x, n):
    """Zahl mit Dezimalkomma im Mathe-Format der Sammlung (z. B. 2{,}43)."""
    s = f"{x:.{n}f}".replace(".", "{,}")
    return s


ZEILEN = [
    # (Bezeichnung, Wert, Format, Einheit, String in t1.md oder None)
    ("AUFGABE 1: Seen unter dem Eisschild, Tabelle", None, None, None, None),
    ("Eisdicke H", H, ".0f", "m", r"H = 3700\,\mathrm{m}"),
    ("Oberflächentemperatur theta_O", th_O, ".0f", "°C", r"\vartheta_{\mathrm{O}} = -55\,\mathrm{°C}"),
    ("Wärmestromdichte aus dem Erdinneren q_E", q_E * 1e3, ".0f", "mW/m²", r"\dot{q}_{\mathrm{E}} = 58\,\mathrm{mW/m^2}"),
    ("lambda(T) = a exp(-b T): a", a_L, ".3f", "W/(m K)", r"a = 9{,}828\,\mathrm{W/(m\,K)}"),
    ("lambda(T) = a exp(-b T): b", b_L * 1e3, ".1f", "1e-3/K", r"b = 5{,}7\cdot 10^{-3}\,\mathrm{K^{-1}}"),
    ("Dichte Eis rho", rho, ".0f", "kg/m³", r"\rho = 917\,\mathrm{kg/m^3}"),
    ("Schmelzenthalpie", dh_schm / 1e3, ".1f", "kJ/kg", r"\Delta h_{\mathrm{schm}} = 333{,}5\,\mathrm{kJ/kg}"),
    ("Schmelzpunktsenkung gamma (Absenkung je MPa)", k_pm, ".4f", "K/MPa", r"\gamma = 0{,}0742\,\mathrm{K/MPa}"),
    ("Erdbeschleunigung g", G, ".2f", "m/s²", r"g = 9{,}81\,\mathrm{m/s^2}"),
    ("Firn: Dicke s_F", s_F, ".0f", "m", r"s_{\mathrm{F}} = 100\,\mathrm{m}"),
    ("Firn: Wärmeleitfähigkeit lambda_F", lam_F, ".1f", "W/(m K)", r"\lambda_{\mathrm{F}} = 1{,}0\,\mathrm{W/(m\,K)}"),
    ("Dome C: Tiefe z_1", z1, ".0f", "m", r"z_1 = 3200\,\mathrm{m}"),
    ("Dome C: Temperatur theta_1", th1, ".1f", "°C", r"\vartheta_1 = -4{,}2\,\mathrm{°C}"),
    ("Dome C: Tiefe z_2", z2, ".1f", "m", r"z_2 = 3270{,}2\,\mathrm{m}"),
    ("Dome C: Temperatur theta_2", th2, ".2f", "°C", r"\vartheta_2 = -2{,}34\,\mathrm{°C}"),
    ("AUFGABE 1: Ergebnisse", None, None, None, None),
    ("d) lambda(theta_O = -55 °C)", lam_O, ".4f", "W/(m K)", r"\lambda(\vartheta_{\mathrm{O}}) = " + de(lam_O, 2)),
    ("d) lambda(0 °C)", lam_0, ".4f", "W/(m K)", r"\lambda(0\,\mathrm{°C}) = " + de(lam_0, 2)),
    ("d) lambda_m (Integralmittel -55 bis 0 °C)", lm, ".4f", "W/(m K)", r"\lambda_{\mathrm{m}} = " + de(lm, 2)),
    ("   zum Vergleich: Mittel der Randwerte", 0.5 * (lam_O + lam_0), ".4f", "W/(m K)", None),
    ("e) Basistemperatur theta_B (alles geleitet)", th_B, ".2f", "°C", r"\vartheta_{\mathrm{B}} = " + de(th_B, 1)),
    ("   Gradient q_E/lambda_m", grad_e * 1e3, ".2f", "K/km", None),
    ("f) Druck an der Basis p", p / 1e6, ".3f", "MPa", r"p = " + de(p / 1e6, 1)),
    ("f) Druckschmelzpunkt theta_pm", th_pm, ".3f", "°C", r"\vartheta_{\mathrm{pm}} = " + de(th_pm, 2)),
    ("f) Abstand theta_B - theta_pm", th_B - th_pm, ".2f", "K", None),
    ("g) geleitete Wärmestromdichte q_leit", q_leit * 1e3, ".3f", "mW/m²", r"\dot{q}_{\mathrm{leit}} = " + de(q_leit * 1e3, 1)),
    ("g) Rest für das Schmelzen", q_rest * 1e3, ".3f", "mW/m²", None),
    ("g) Schmelzrate v_schm", v_schm, ".4e", "m/s", None),
    ("g) Schmelzrate v_schm je Jahr", v_schm_a, ".3f", "mm/a", r"v_{\mathrm{schm}} = " + de(v_schm_a, 2)),
    ("h1) Mindestdicke H_krit (Schmelzpunkt aus f)", H_krit, ".1f", "m", r"H_{\mathrm{krit}} \approx " + f"{round(H_krit, -2):.0f}"),
    ("   Kontrolle: mit Schmelzpunkt in dieser Tiefe", H_it, ".1f", "m", None),
    ("h2) Faktor der Gradienten Firn/Eis = lambda_m/lambda_F", faktor_firn, ".4f", "-", r"zu (2): Faktor $" + de(faktor_firn, 2)),
    ("   Gradient im Firn (q_leit)", grad_F * 1e3, ".2f", "K/km", None),
    ("   Gradient im Eis (q_leit)", grad_I * 1e3, ".2f", "K/km", None),
    ("h3) Dome C: Gradient nahe der Basis", grad_C * 1e3, ".3f", "K/km", r"\mathrm{d}T/\mathrm{d}z = " + de(grad_C * 1e3, 1)),
    ("h3) lambda(-3 °C)", lam_m3, ".4f", "W/(m K)", None),
    ("h3) Wärmestromdichte q_C = lambda(-3 °C) dT/dz", q_C * 1e3, ".3f", "mW/m²", r"\dot{q}_{\mathrm{C}} = " + de(q_C * 1e3, 1)),
    ("h3) Druck in z_2", p_C / 1e6, ".3f", "MPa", None),
    ("h3) Druckschmelzpunkt in z_2", th_pm_C, ".3f", "°C", r"\vartheta_{\mathrm{pm}}(z_2) = " + de(th_pm_C, 2)),
    ("h3) Abstand Schmelzpunkt minus Messwert", luecke, ".3f", "K", None),
    ("h3) Strecke bis zum Schmelzpunkt Delta z", dz_C, ".2f", "m", r"\Delta z \approx " + f"{dz_C:.0f}"),
    ("AUFGABE 2: Kühlhauswand, Tabelle", None, None, None, None),
    ("Stahlbeton: Dicke s_B", s_B * 100, ".0f", "cm", r"s_{\mathrm{B}} = 20\,\mathrm{cm}"),
    ("Stahlbeton: lambda_B", lam_B, ".1f", "W/(m K)", r"\lambda_{\mathrm{B}} = 2{,}3\,\mathrm{W/(m\,K)}"),
    ("Hartschaum: Dicke s_D", s_D * 100, ".0f", "cm", r"s_{\mathrm{D}} = 12\,\mathrm{cm}"),
    ("Hartschaum: lambda_D", lam_D, ".3f", "W/(m K)", r"\lambda_{\mathrm{D}} = 0{,}025\,\mathrm{W/(m\,K)}"),
    ("Wand: Fläche A", A_W, ".0f", "m²", r"A = 250\,\mathrm{m^2}"),
    ("Wand: Oberflächentemperatur außen theta_a", th_a, ".0f", "°C", r"\vartheta_{\mathrm{a}} = 28\,\mathrm{°C}"),
    ("Wand: Oberflächentemperatur innen theta_i", th_i, ".0f", "°C", r"\vartheta_{\mathrm{i}} = -22\,\mathrm{°C}"),
    ("Betreiber: Grenzwert q_max", q_max, ".0f", "W/m²", r"\dot{q}_{\mathrm{max}} = 8\,\mathrm{W/m^2}"),
    ("AUFGABE 2: Ergebnisse", None, None, None, None),
    ("b) s_B/lambda_B", R_B, ".4f", "m² K/W", None),
    ("b) s_D/lambda_D", R_D, ".4f", "m² K/W", None),
    ("b) Wärmestromdichte q", q_W, ".4f", "W/m²", r"\dot{q} = " + de(q_W, 2)),
    ("b) Wärmestrom Q durch 250 m²", Q_W / 1e3, ".4f", "kW", r"\dot{Q} = " + de(Q_W / 1e3, 2)),
    ("c) Temperatur an der Grenzfläche theta_G", th_G, ".4f", "°C", r"\vartheta_{\mathrm{G}} = " + de(th_G, 2)),
    ("c) Gradient im Beton", q_W / lam_B, ".3f", "K/m", None),
    ("c) Gradient in der Dämmung", q_W / lam_D, ".2f", "K/m", None),
    ("c) Faktor der Gradienten = lambda_B/lambda_D", faktor_W, ".2f", "-", r"Faktor $" + f"{faktor_W:.0f}"),
    ("e) Anteil des Betons am Widerstand", anteil_B * 100, ".2f", "%", None),
    ("d) Mindestdicke der Dämmung s_D,min", s_D_min * 100, ".3f", "cm", r"s_{\mathrm{D,min}} = " + de(s_D_min * 100, 2)),
    ("d) gewählte Dicke (aufgerundet)", s_D_gew * 100, ".0f", "cm", r"s_{\mathrm{D}} = " + f"{s_D_gew * 100:.0f}"),
    ("d) Wärmestromdichte mit gewählter Dicke", q_gew, ".4f", "W/m²", r"\dot{q}(s_{\mathrm{D}} = 16\,\mathrm{cm}) = " + de(q_gew, 2)),
    ("e) Wärmestromdichte mit doppelter Betondicke", q_2B, ".4f", "W/m²", r"\dot{q} = " + de(q_2B, 2)),
    ("ZUSATZAUFGABE 1: Erdwärme in Deutschland", None, None, None, None),
    ("Gradient KTB", grad_KTB * 1e3, ".0f", "K/km", r"28\,\mathrm{K/km}"),
    ("Wärmeleitfähigkeit Gestein lambda_KTB", lam_KTB, ".1f", "W/(m K)", r"\lambda_{\mathrm{KTB}} = 2{,}9\,\mathrm{W/(m\,K)}"),
    ("Endteufe z_KTB", z_KTB, ".0f", "m", r"z_{\mathrm{KTB}} = 9101\,\mathrm{m}"),
    ("a) Wärmestromdichte q_KTB", q_KTB * 1e3, ".3f", "mW/m²", r"\dot{q}_{\mathrm{KTB}} = " + de(q_KTB * 1e3, 1)),
    ("b) Verhältnis q_KTB/q_E", v_q, ".4f", "-", r"\dot{q}_{\mathrm{KTB}}/\dot{q}_{\mathrm{E}} = " + de(v_q, 2)),
    ("b) Verhältnis lambda_KTB/lambda_m", v_lam, ".4f", "-", r"\lambda_{\mathrm{KTB}}/\lambda_{\mathrm{m}} = " + de(v_lam, 2)),
    ("   Gradient im Eis (Teil e) zum Vergleich", grad_e * 1e3, ".2f", "K/km", None),
    ("c) Temperaturunterschied bis z_KTB", dT_KTB, ".2f", "K", r"\Delta T = " + de(dT_KTB, 1)),
    ("VORAB-FRAGE", None, None, None, None),
    ("Gradient Firn / Gradient Eis = lambda_m/lambda_F", faktor_firn, ".2f", "-", None),
]


def main():
    zeilen = ["Tutorium 1: Wärmeleitung (Zahlen für teile/t1.md, Skript t1_rechnung.py)"]
    for name, wert, fmt, einheit, _ in ZEILEN:
        if wert is None:
            zeilen.append("")
            zeilen.append(name)
            continue
        zeilen.append(f"{name:55s} {wert:>14{fmt}} {einheit}")
    # Abgleich mit dem Markdown
    zeilen.append("")
    zeilen.append("ABGLEICH mit teile/t1.md (jede Zeichenkette muss im Markdown stehen)")
    fehlt = 0
    if os.path.exists(TEIL):
        with open(TEIL, encoding="utf-8") as f:
            md = ohne_mathrm(f.read())
        for name, wert, fmt, einheit, soll in ZEILEN:
            if soll is None:
                continue
            ok = ohne_mathrm(soll) in md
            fehlt += 0 if ok else 1
            zeilen.append(f"{'ok   ' if ok else 'FEHLT'} {soll}")
    else:
        zeilen.append("teile/t1.md fehlt noch")
        fehlt = -1
    zeilen.append(f"Ergebnis des Abgleichs: {'alles gefunden' if fehlt == 0 else str(fehlt) + ' fehlen'}")
    text = "\n".join(zeilen) + "\n"
    with open(AUSGABE, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
