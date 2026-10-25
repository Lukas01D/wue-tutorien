# -*- coding: utf-8 -*-
"""Tutorium 6, Wärmebilanzen (stationär differentiell): Zahlen für teile/t6.md.

Aufgabe 1: Erdkruste mit radioaktiver Wärmequelle (Bilanz am Element dz, z nach unten)
Aufgabe 2: Erde als Kugel mit gleichmäßig verteilter Wärmequelle (Bilanz an der Kugelschale dr)
Zusatzaufgabe 1: Wie warm wäre die Erde ohne Sonne?

Arbeitswerte aus der Ideensammlung „Leitaufgaben aus Klima und Erde“ (17.10.2026), Abschnitt 4.6,
und aus nachrechnung_leitphaenomene.py (Abschnitte T4 und T6). Formeln nachgebaut, nicht importiert,
weil das Ausgangsskript beim Import alle Tutorien rechnet und CoolProp braucht.

Aufruf: python3 t6_rechnung.py
Schreibt t6_rechnung_ausgabe.txt (Name, Wert, Einheit, Schreibweise im Markdown) und prüft, ob jede
Zahl der Tabellen und Ergebniszeilen genau so in teile/t6.md steht.
"""
import math
import os

HIER = os.path.dirname(os.path.abspath(__file__))
TEIL = os.path.join(os.path.dirname(HIER), "teile", "t6.md")
AUSGABE = os.path.join(HIER, "t6_rechnung_ausgabe.txt")


# ---------- Schreibweise wie im Markdown (Dezimalkomma {,}, schmaler Abstand ab fünf Stellen) ----------
def de(x, n=0):
    """Zahl mit n Nachkommastellen, Dezimalkomma als {,}, ab fünf Vorkommastellen mit \\, gruppiert."""
    s = f"{abs(x):.{n}f}"
    ganz, _, rest = s.partition(".")
    if len(ganz) >= 5:
        gruppen = []
        while ganz:
            gruppen.insert(0, ganz[-3:])
            ganz = ganz[:-3]
        ganz = r"\,".join(gruppen)
    s = ganz + ("{,}" + rest if rest else "")
    return ("-" if x < 0 else "") + s


def zehn(x, n=2):
    """Zehnerpotenz: 4{,}34\\cdot 10^{-8}"""
    e = int(math.floor(math.log10(abs(x))))
    m = x / 10**e
    if round(m, n) >= 10:
        m /= 10
        e += 1
    return f"{de(m, n)}\\cdot 10^{{{e}}}"


U = lambda s: r"\,\mathrm{" + s + "}"

# ---------- Eingaben ----------
# Aufgabe 1: Erdkruste (Ideensammlung 4.6, Arbeitswerte)
s = 30e3            # m, Krustendicke
lam = 2.5           # W/(m K)
th_O = 10.0         # °C, Oberfläche
q_O = 0.065         # W/m², Wärmestromdichte an der Oberfläche (nach oben), Mittel der Kontinente
q_KV = 1.0e-6       # W/m³, Wärmequelle (Arbeitswert)
q_KV_G = 2.5e-6     # W/m³, typisch für Granit (Arbeitswert)
z_B = 9.1e3         # m, Kontinentale Tiefbohrung (9101 m, gerundet)
th_B = 265.0        # °C, Temperatur in dieser Tiefe (GFZ)
# Aufgabe 2: Erde als Kugel
R = 6.371e6         # m
Q_ges = 47e12       # W, Davies & Davies (2010)
lam_Kugel = (3.0, 4.0)
th_Kern = 6000.0    # °C, am inneren Kern (ESRF zu Anzellini et al., 2013)
S0, rho_p = 1361.0, 0.30   # wie Tutorium 4
q_S = S0 * (1 - rho_p) / 4  # absorbierte Sonnenstrahlung, W/m²
# Zusatzaufgabe
SIGMA = 5.6705e-8   # W/(m² K⁴), V04 F. 10
q_alt = 0.087       # W/m², Pollack et al. (1993), gehört zu 44,2 TW


def theta(z, qkv):
    """Profil mit z nach unten: T(z) = T_O + q_O/lam z - qkv/(2 lam) z²; Randbedingungen T(0) = T_O,
    dT/dz(0) = q_O/lam (Wärme strömt nach oben, Fourier: q_z = -lam dT/dz = -q_O)."""
    return th_O + q_O / lam * z - qkv / (2 * lam) * z**2


def q_basis(qkv):
    """Wärmestromdichte nach oben an der Krustenbasis: q_M = lam dT/dz(s) = q_O - qkv s."""
    return lam * (q_O / lam - qkv / lam * s)


werte = []   # (Teil, Name, Wert, Einheit, Schreibweise im Markdown oder None)


def neu(teil, name, wert, einheit, tex=None):
    werte.append((teil, name, wert, einheit, tex))


# ---------- Tabellen ----------
neu("Tab. A1", "Krustendicke s", s / 1e3, "km", f"s = {de(s/1e3)}" + U("km"))
neu("Tab. A1", "Wärmeleitfähigkeit lambda", lam, "W/(m K)", f"\\lambda = {de(lam, 1)}" + U(r"W/(m\,K)"))
neu("Tab. A1", "Wärmequelle q_KV", q_KV * 1e6, "µW/m³", f"\\dot{{q}}_{{KV}} = {de(q_KV*1e6)}" + U("µW/m^3"))
neu("Tab. A1", "Oberflächentemperatur theta_O", th_O, "°C", f"\\vartheta_O = {de(th_O)}" + U("°C"))
neu("Tab. A1", "Wärmestromdichte Oberfläche q_O", q_O * 1e3, "mW/m²", f"\\dot{{q}}_O = {de(q_O*1e3)}" + U("mW/m^2"))
neu("Tab. A1", "Wärmequelle Granit q_KV,G", q_KV_G * 1e6, "µW/m³", f"\\dot{{q}}_{{KV,G}} = {de(q_KV_G*1e6, 1)}" + U("µW/m^3"))
neu("Tab. A1", "Tiefe Tiefbohrung z_B", z_B / 1e3, "km", f"z_B = {de(z_B/1e3, 1)}" + U("km"))
neu("Tab. A1", "Temperatur Tiefbohrung theta_B", th_B, "°C", f"\\vartheta_B = {de(th_B)}" + U("°C"))
neu("Tab. A2", "Erdradius R", R / 1e3, "km", f"R = {de(R/1e3)}" + U("km"))
neu("Tab. A2", "Wärmestrom aus dem Erdinneren", Q_ges / 1e12, "TW", f"\\dot{{Q}} = {de(Q_ges/1e12)}" + U("TW"))
neu("Tab. A2", "Wärmeleitfähigkeit Kugel (unten)", lam_Kugel[0], "W/(m K)", f"\\lambda = {de(lam_Kugel[0])}")
neu("Tab. A2", "Wärmeleitfähigkeit Kugel (oben)", lam_Kugel[1], "W/(m K)", f"{de(lam_Kugel[1])}" + U(r"W/(m\,K)"))
neu("Tab. A2", "Temperatur am inneren Kern", th_Kern, "°C", f"\\vartheta_K = {de(th_Kern)}" + U("°C"))
neu("Tab. A2", "absorbierte Sonnenstrahlung q_S = S0 (1 - rho_p)/4", q_S, "W/m²", f"\\dot{{q}}_S = {de(q_S)}" + U("W/m^2"))

# ---------- Aufgabe 1 ----------
for z in (10e3, 20e3, 30e3):
    t_mit, t_ohne = theta(z, q_KV), theta(z, 0.0)
    neu("A1 e", f"theta({z/1e3:.0f} km) mit Quelle", t_mit, "°C",
        f"\\vartheta({de(z/1e3)}" + U("km") + f") = {de(t_mit)}" + U("°C"))
    neu("A1 e", f"theta({z/1e3:.0f} km) ohne Quelle", t_ohne, "°C",
        f"\\vartheta({de(z/1e3)}" + U("km") + f") = {de(t_ohne)}" + U("°C"))
t_KTB = theta(z_B, q_KV)
neu("A1 f", "theta(z_B) aus dem Profil", t_KTB, "°C", f"\\vartheta(z_B) = {de(t_KTB)}" + U("°C"))
neu("A1 f", "  Abstand zum Wert der Bohrung", th_B - t_KTB, "K")
neu("A1 f", "  Wärmestromdichte, die mit dem Profil 265 °C in z_B ergäbe", (th_B - th_O + q_KV / (2 * lam) * z_B**2) * lam / z_B * 1e3, "mW/m²")
q_M = q_basis(q_KV)
neu("A1 g", "q_M aus dem Profil (lam dT/dz bei z = s)", q_M * 1e3, "mW/m²", f"\\dot{{q}}_M = {de(q_M*1e3)}" + U("mW/m^2"))
neu("A1 g", "q_M aus der globalen Bilanz q_O - q_KV s", (q_O - q_KV * s) * 1e3, "mW/m²")
neu("A1 g", "  Anteil der Kruste an q_O (q_KV s / q_O)", q_KV * s / q_O * 100, "%")
z_max = q_O / q_KV_G
q_M_G = q_basis(q_KV_G)
neu("A1 h", "Granit: Tiefe des Maximums z_max = q_O/q_KV,G", z_max / 1e3, "km", f"z_{{max}} = {de(z_max/1e3)}" + U("km"))
neu("A1 h", "Granit: Wärmestromdichte an der Basis q_M", q_M_G * 1e3, "mW/m²", f"\\dot{{q}}_M = {de(q_M_G*1e3)}" + U("mW/m^2"))
neu("A1 h", "  Granit: Temperatur im Maximum", theta(z_max, q_KV_G), "°C")
neu("A1 h", "  Granit: Temperatur an der Basis (30 km)", theta(s, q_KV_G), "°C")
neu("A1 Prüfung", "  Abweichung der Parabel von der Geraden in 100 m Tiefe", q_KV / (2 * lam) * 100.0**2, "K")
neu("A1 Prüfung", "  Gradient an der Oberfläche q_O/lambda", q_O / lam * 1e3, "K/km")

# ---------- Aufgabe 2 ----------
V = 4 / 3 * math.pi * R**3
A = 4 * math.pi * R**2
q_KV_E = Q_ges / V
neu("A2 c", "q_KV der Erde (47 TW gleichmäßig)", q_KV_E, "W/m³", f"\\dot{{q}}_{{KV}} = {zehn(q_KV_E, 2)}" + U("W/m^3"))
for lam_k in lam_Kugel:
    dT = q_KV_E * R**2 / (6 * lam_k)
    neu("A2 c", f"T_Mitte - T_O für lambda = {lam_k:.0f}", dT, "K", f"{de(round(dT, -2))}" + U("K"))
q_O_E = q_KV_E * R / 3
neu("A2 d", "q_O = q_KV R/3 (aus dem Profil)", q_O_E * 1e3, "mW/m²", f"\\dot{{q}}_O = {de(q_O_E*1e3, 1)}" + U("mW/m^2"))
neu("A2 d", "q_O = Q/(4 pi R²) (globale Bilanz)", Q_ges / A * 1e3, "mW/m²")
neu("A2 f", "q_S / q_O", q_S / q_O_E, "-", None)
neu("A2 f", "q_S / q_O, gerundet auf zwei gültige Ziffern", round(q_S / q_O_E, -2), "-",
    f"\\dot{{q}}_S/\\dot{{q}}_O \\approx {de(round(q_S / q_O_E, -2))}")
neu("A2 f", "  absorbierte Sonnenstrahlung gesamt", q_S * A / 1e12, "TW")

# ---------- Zusatzaufgabe 1 ----------
T_ohne = (q_O_E / SIGMA) ** 0.25
T_alt = (q_alt / SIGMA) ** 0.25
neu("Z1 a", "Oberflächentemperatur ohne Sonne mit q_O aus A2", T_ohne, "K", f"T = {de(T_ohne, 1)}" + U("K"))
neu("Z1 a", "  in °C", T_ohne - 273.15, "°C")
neu("Z1 a", "  zum Vergleich mit 92 mW/m² (gerundet)", (0.092 / SIGMA) ** 0.25, "K")
neu("Z1 b", "Oberflächentemperatur mit 87 mW/m²", T_alt, "K", f"T = {de(T_alt, 1)}" + U("K"))
neu("Z1 b", "  Änderung der Temperatur in %", (T_alt / T_ohne - 1) * 100, "%")
neu("Z1 b", "  Änderung der Wärmestromdichte in %", (q_alt / q_O_E - 1) * 100, "%")
neu("Z1 b", "  Tabellenwert 87 mW/m²", q_alt * 1e3, "mW/m²", f"{de(q_alt*1e3)}" + U("mW/m^2"))

# ---------- Kernzahlen der Ideensammlung (Abschnitt 4.6) zum Abgleich ----------
KERN = [("theta(10 km)", theta(10e3, q_KV), 250), ("theta(20 km)", theta(20e3, q_KV), 450),
        ("theta(30 km)", theta(30e3, q_KV), 610), ("ohne Quelle 10 km", theta(10e3, 0), 270),
        ("ohne Quelle 20 km", theta(20e3, 0), 530), ("ohne Quelle 30 km", theta(30e3, 0), 790),
        ("Mantel mW/m²", q_M * 1e3, 35), ("z_max km", z_max / 1e3, 26), ("Mantel Granit", q_M_G * 1e3, -10),
        ("KTB °C", t_KTB, 230), ("q_KV Erde 1e-8", q_KV_E * 1e8, 4.3), ("dT lambda 4", q_KV_E * R**2 / 24, 73000),
        ("dT lambda 3", q_KV_E * R**2 / 18, 98000), ("q_O Kugel mW/m²", q_O_E * 1e3, 92),
        ("ohne Sonne K", T_ohne, 35)]

zeilen = ["Tutorium 6: Wärmebilanzen (stationär differentiell), Zahlen für teile/t6.md (Skript t6_rechnung.py)", "",
          f"{'Teil':11s} {'Größe':62s} {'Wert':>14s}  Einheit   | Schreibweise im Markdown"]
for teil, name, wert, einheit, tex in werte:
    zeilen.append(f"{teil:11s} {name:62s} {wert:14.5g}  {einheit:9s} | {tex or ''}")
zeilen += ["", "Abgleich mit den Kernzahlen der Ideensammlung (Abschnitt 4.6, gerundet):"]
for name, ist, soll in KERN:
    ok = abs(ist - soll) <= max(0.06 * abs(soll), 0.6)
    zeilen.append(f"  {name:22s} Skript {ist:12.4g}  Ideensammlung {soll:>8g}  {'ok' if ok else 'ABWEICHUNG'}")

# ---------- Abgleich mit dem Markdown ----------
fehlend = []
if os.path.exists(TEIL):
    md = open(TEIL, encoding="utf-8").read()
    for teil, name, wert, einheit, tex in werte:
        if tex and tex not in md:
            fehlend.append(f"{teil}: {name}: {tex}")
    zeilen += ["", f"Abgleich mit {os.path.relpath(TEIL, os.path.dirname(HIER))}: "
               + ("alle Werte gefunden" if not fehlend else f"{len(fehlend)} Werte fehlen")]
    zeilen += ["  FEHLT " + f for f in fehlend]
else:
    zeilen += ["", "teile/t6.md noch nicht vorhanden, kein Abgleich"]

text = "\n".join(zeilen) + "\n"
with open(AUSGABE, "w", encoding="utf-8") as f:
    f.write(text)
print(text)
