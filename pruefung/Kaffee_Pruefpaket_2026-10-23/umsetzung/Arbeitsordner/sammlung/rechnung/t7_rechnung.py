# -*- coding: utf-8 -*-
"""Tutorium 7, Wärmebilanzen (instationär differentiell): Zahlen für teile/t7.md.

Aufgabe 1: Temperaturwelle im Boden (gegebene Lösung T = T_m + dT_0 exp(-z/d) cos(wt - z/d), d = sqrt(2a/w)),
           Eindringtiefe sqrt(a t), Auftautiefe über Permafrost, Bohrloch als Klimaarchiv
Frage 3:   Temperaturleitfähigkeit a = lambda/(rho c) für Kupfer, Granit, feuchten Ton, Wasser, Luft
Zusatzaufgabe 1: Lord Kelvin und das Alter der Erde (halbunendlicher Körper, Gradient an der Oberfläche)

Arbeitswerte aus der Ideensammlung „Leitaufgaben aus Klima und Erde“ (17.10.2026), Abschnitt 4.7, und aus
nachrechnung_leitphaenomene.py (Abschnitt T7). Formeln nachgebaut. Stoffwerte für Frage 3: Wasser und Luft
mit CoolProp (20 °C, 1,01325 bar), Kupfer nach Datenblatt Cu-OF, Granit und feuchter Ton nach ASHRAE (2000),
Tabelle bei Sobti & Singh (2015); siehe quellen/t7_quellen.md.

Aufruf: python3 t7_rechnung.py
Schreibt t7_rechnung_ausgabe.txt und prüft, ob jede Zahl der Tabellen und Ergebniszeilen genau so in
teile/t7.md steht.
"""
import math
import os
import sys as _sys, os as _os
_sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), "build"))
from indizes_aufrecht import ohne_mathrm   # Schreibweise prüfen unabhängig davon, ob Indizes aufrecht oder kursiv stehen

HIER = os.path.dirname(os.path.abspath(__file__))
TEIL = os.path.join(os.path.dirname(HIER), "teile", "t7.md")
AUSGABE = os.path.join(HIER, "t7_rechnung_ausgabe.txt")

TAG = 86400.0
JAHR_TAGE = 365.25
JAHR = JAHR_TAGE * TAG


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
    """Zehnerpotenz: 7{,}27\\cdot 10^{-5}"""
    e = int(math.floor(math.log10(abs(x))))
    m = x / 10**e
    if round(m, n) >= 10:
        m /= 10
        e += 1
    return f"{de(m, n)}\\cdot 10^{{{e}}}"


U = lambda s: r"\,\mathrm{" + s + "}"

# ---------- Eingaben ----------
a_B = 5.0e-7          # m²/s, feuchter Boden (schwerer Ton, 15 % Wasser: 4,9 bis 7,1e-7; Arbeitswert)
t_J = JAHR            # s, Periodendauer Jahr (365,25 Tage)
t_T = TAG             # s, Periodendauer Tag
dT0 = 10.0            # K, Amplitude Jahresgang (Arbeitswert)
t_K = 14 * TAG        # s, Kälteperiode
th_mP, dT0_P, dth_P = -8.0, 15.0, 3.0   # Permafrost: Jahresmittel, Amplitude, Erwärmung
a_G = 1.0e-6          # m²/s, Gestein (Arbeitswert)
t_E = 100 * JAHR      # s, Zeit seit der Erwärmung
# Kelvin (England et al., 2007; Nachrechnung der Ideensammlung)
th_AK, th_OK = 3870.0, 0.0      # °C: Anfangstemperatur theta_A (7000 °F) und Oberfläche theta_O
G_K = 36.5e-3                    # K/m
a_K = 1.18e-6                    # m²/s
R = 6.371e6                      # m

werte = []


def neu(teil, name, wert, einheit, tex=None):
    werte.append((teil, name, wert, einheit, tex))


# ---------- Tabelle ----------
neu("Tab.", "Temperaturleitfähigkeit Boden a", a_B, "m²/s", r"a = 5\cdot 10^{-7}" + U("m^2/s"))
neu("Tab.", "Amplitude Jahresgang dT_0", dT0, "K", f"\\Delta T_0 = {de(dT0)}" + U("K"))
neu("Text", "Periodendauer Jahr t_J", JAHR_TAGE, "Tage", f"t_J = {de(JAHR_TAGE, 2)}" + U("Tage"))
neu("Text", "Periodendauer Tag t_T", t_T / 3600, "h", f"t_T = {de(t_T/3600)}" + U("h"))
neu("A1 g", "Kälteperiode t_K (im Text)", t_K / TAG, "Tage", f"t_K = {de(t_K/TAG)}" + U("Tage"))
neu("Tab.", "Permafrost: Jahresmittel theta_m,P", th_mP, "°C", f"\\vartheta_{{m,P}} = {de(th_mP)}" + U("°C"))
neu("Tab.", "Permafrost: Amplitude dT_0,P", dT0_P, "K", f"\\Delta T_{{0,P}} = {de(dT0_P)}" + U("K"))
neu("Tab.", "Permafrost: Erwärmung dtheta_P", dth_P, "K", f"\\Delta\\vartheta_P = {de(dth_P)}" + U("K"))
neu("Tab.", "Gestein: Temperaturleitfähigkeit a_G", a_G, "m²/s", r"a_G = 1\cdot 10^{-6}" + U("m^2/s"))
neu("A1 i", "Zeit seit der Erwärmung t_E (im Text)", t_E / JAHR, "Jahre", f"t_E = {de(t_E/JAHR)}" + U("Jahre"))

# ---------- Aufgabe 1 ----------
om_T, om_J = 2 * math.pi / t_T, 2 * math.pi / t_J
d_T, d_J = math.sqrt(2 * a_B / om_T), math.sqrt(2 * a_B / om_J)
neu("A1 d", "Kreisfrequenz Tag omega_T", om_T, "1/s", f"\\omega_T = {zehn(om_T)}" + U("1/s"))
# d_T mit drei Ziffern: mit dem gerundeten Wert 0,12 m ergäbe Teil e 1,6 % statt 1,4 %
neu("A1 d", "Dämpfungstiefe Tag d_T (drei Ziffern, siehe Teil e)", d_T, "m", f"d_T = {de(d_T, 3)}" + U("m"))
neu("A1 d", "  Kontrolle: Tagesgang in 0,5 m mit d_T = 0,12 m", math.exp(-0.5 / 0.12) * 100, "%")
neu("A1 d", "  Kontrolle: Tagesgang in 0,5 m mit d_T = 0,117 m", math.exp(-0.5 / 0.117) * 100, "%")
neu("A1 d", "Kreisfrequenz Jahr omega_J", om_J, "1/s", f"\\omega_J = {zehn(om_J)}" + U("1/s"))
neu("A1 d", "Dämpfungstiefe Jahr d_J", d_J, "m", f"d_J = {de(d_J, 2)}" + U("m"))
for z, n in ((1.0, 0), (5.0, 0), (10.0, 1)):
    anteil = math.exp(-z / d_J) * 100
    neu("A1 e", f"Jahresgang: Anteil der Amplitude in {z:.0f} m", anteil, "%", f"{de(anteil, n)}" + r"\,\%")
dT10 = dT0 * math.exp(-10.0 / d_J)
neu("A1 e", "Jahresgang: Amplitude in 10 m", dT10, "K", f"\\Delta T(10" + U("m") + f") = {de(dT10, 2)}" + U("K"))
anteil_T = math.exp(-0.5 / d_T) * 100
neu("A1 e", "Tagesgang: Anteil der Amplitude in 0,5 m", anteil_T, "%", f"{de(anteil_T, 1)}" + r"\,\%")
for z in (0.05, 0.10, 0.20, 0.50):
    neu("A1 e", f"  Tagesgang: Anteil in {z*100:.0f} cm (Messtiefen des DWD)", math.exp(-z / d_T) * 100, "%")
for z in (2.0, 3.0, 5.0):
    dt = z / (d_J * om_J) / TAG
    neu("A1 f", f"Verzögerung des Jahresmaximums in {z:.0f} m", dt, "Tage", f"{de(dt)}" + U("Tage"))
neu("A1 f", "  Verzögerung des Tagesmaximums in 20 cm", 0.20 / (d_T * om_T) / 3600, "h")
delta_K = math.sqrt(a_B * t_K)
neu("A1 g", "Eindringtiefe sqrt(a t_K)", delta_K, "m", f"\\sqrt{{a\\,t_K}} = {de(delta_K, 2)}" + U("m"))
for th_m in (th_mP, th_mP + dth_P):
    z0 = d_J * math.log(dT0_P / abs(th_m))
    neu("A1 h", f"Auftautiefe bei Jahresmittel {th_m:.0f} °C", z0, "m", f"z_0 = {de(z0, 2)}" + U("m"))
delta_E = math.sqrt(a_G * t_E)
neu("A1 i", "Eindringtiefe der Erwärmung sqrt(a_G t_E)", delta_E, "m", f"\\sqrt{{a_G\\,t_E}} = {de(delta_E)}" + U("m"))

# ---------- Frage 3: Temperaturleitfähigkeiten ----------
try:
    from CoolProp.CoolProp import PropsSI
    T20, p0 = 293.15, 101325.0
    coolprop = {f: (PropsSI("L", "T", T20, "P", p0, f), PropsSI("D", "T", T20, "P", p0, f),
                    PropsSI("C", "T", T20, "P", p0, f)) for f in ("Water", "Air")}
except ImportError:      # Werte aus CoolProp 8.0, notiert am 21.10.2026
    coolprop = {"Water": (0.598012, 998.207, 4184.05), "Air": (0.0258738, 1.20458, 1006.14)}
# Werte wie in der Frage (gerundet), a mit den gerundeten Werten
stoffe = [("Kupfer (Cu-OF, 20 °C)", 394.0, 8940.0, 386.0, (0, 0, 0)),
          ("Wasser (20 °C)", round(coolprop["Water"][0], 3), round(coolprop["Water"][1]), round(coolprop["Water"][2]), (3, 0, 0)),
          ("Luft (20 °C, 1,013 bar)", round(coolprop["Air"][0], 4), round(coolprop["Air"][1], 2), round(coolprop["Air"][2]), (4, 2, 0))]
for name, lam, rho, c, (nl, nr, nc) in stoffe:
    a = lam / (rho * c)
    neu("Frage 3", f"{name}: lambda", lam, "W/(m K)", f"\\lambda = {de(lam, nl)}" + U(r"W/(m\,K)"))
    neu("Frage 3", f"{name}: rho", rho, "kg/m³", f"\\rho = {de(rho, nr)}" + U("kg/m^3"))
    neu("Frage 3", f"{name}: c", c, "J/(kg K)", f"c = {de(c, nc)}" + U(r"J/(kg\,K)"))
    neu("Frage 3", f"{name}: a = lambda/(rho c)", a, "m²/s")
neu("Frage 3", "  CoolProp Wasser lambda, rho, c (ungerundet)", coolprop["Water"][0], "W/(m K)")
neu("Frage 3", "  CoolProp Luft lambda, rho, c (ungerundet)", coolprop["Air"][0], "W/(m K)")
neu("Frage 3", "  a Luft ungerundet", coolprop["Air"][0] / (coolprop["Air"][1] * coolprop["Air"][2]), "m²/s")
neu("Frage 3", "  a Wasser ungerundet", coolprop["Water"][0] / (coolprop["Water"][1] * coolprop["Water"][2]), "m²/s")
# ASHRAE (2000), Tabelle bei Sobti & Singh (2015): a in m²/Tag
for name, (l1, l2), (a1, a2), tex_l, tex_a in (
        ("Granit", (2.3, 3.7), (0.084, 0.13), r"\lambda = 2{,}3", r"1{,}5\cdot 10^{-6}"),
        ("feuchter Ton (schwer, 15 % Wasser)", (1.4, 1.9), (0.042, 0.061), r"\lambda = 1{,}4", r"7{,}1\cdot 10^{-7}")):
    neu("Frage 3", f"{name}: lambda von", l1, "W/(m K)", tex_l)
    neu("Frage 3", f"{name}: lambda bis", l2, "W/(m K)")
    neu("Frage 3", f"{name}: a von", a1 / TAG, "m²/s")
    neu("Frage 3", f"{name}: a bis", a2 / TAG, "m²/s", tex_a + U("m^2/s"))
    neu("Frage 3", f"  {name}: rho c = lambda/a (untere Werte)", l1 / (a1 / TAG) / 1e6, "MJ/(m³ K)")
neu("Frage 3", "  Verhältnis lambda Wasser/Luft", stoffe[1][1] / stoffe[2][1], "-")
neu("Frage 3", "  Verhältnis a Luft/Wasser", (stoffe[2][1] / (stoffe[2][2] * stoffe[2][3])) /
    (stoffe[1][1] / (stoffe[1][2] * stoffe[1][3])), "-")
neu("Frage 3", "  Verhältnis rho c Wasser/Luft", (stoffe[1][2] * stoffe[1][3]) / (stoffe[2][2] * stoffe[2][3]), "-")

# ---------- Zusatzaufgabe 1: Kelvin ----------
t_Kelvin = (th_AK - th_OK) ** 2 / (math.pi * a_K * G_K**2)
neu("Z1", "Anfangstemperatur theta_A", th_AK, "°C", f"\\vartheta_A = {de(th_AK)}" + U("°C"))
neu("Z1", "Gradient", G_K * 1e3, "K/km", f"{de(G_K*1e3, 1)}" + U("K/km"))
neu("Z1", "Temperaturleitfähigkeit a", a_K, "m²/s", f"a = {zehn(a_K)}" + U("m^2/s"))
neu("Z1 a", "Alter der Erde nach Kelvin", t_Kelvin / JAHR, "Jahre", f"t = {zehn(t_Kelvin / JAHR, 1)}" + U("Jahre"))
neu("Z1 a", "  in Millionen Jahren", t_Kelvin / JAHR / 1e6, "Mio. Jahre")
delta_Kelvin = math.sqrt(a_K * t_Kelvin)
neu("Z1 b", "Eindringtiefe der Abkühlung sqrt(a t)", delta_Kelvin / 1e3, "km", f"\\sqrt{{a\\,t}} = {de(delta_Kelvin/1e3, 1)}" + U("km"))
neu("Z1 b", "  Anteil am Erdradius", delta_Kelvin / R * 100, "%")
neu("Z1 b", "Erdradius R", R / 1e3, "km", f"R = {de(R/1e3)}" + U("km"))

# ---------- Kernzahlen der Ideensammlung (Abschnitt 4.7) zum Abgleich ----------
KERN = [("d Tag m", d_T, 0.12), ("d Jahr m", d_J, 2.24), ("Amplitude 1 m %", math.exp(-1 / d_J) * 100, 64),
        ("Amplitude 5 m %", math.exp(-5 / d_J) * 100, 11), ("Amplitude 10 m %", math.exp(-10 / d_J) * 100, 1.2),
        ("Verzögerung 2 m Tage", 2 / (d_J * om_J) / TAG, 52), ("Verzögerung 3 m Tage", 3 / (d_J * om_J) / TAG, 78),
        ("Verzögerung 5 m Tage", 5 / (d_J * om_J) / TAG, 130), ("Tagesgang 0,5 m %", anteil_T, 1.4),
        ("sqrt(a t) 14 Tage m", delta_K, 0.78), ("Auftautiefe -8 °C m", d_J * math.log(15 / 8), 1.4),
        ("Auftautiefe -5 °C m", d_J * math.log(15 / 5), 2.5), ("Bohrloch 100 a m", delta_E, 56),
        ("Kelvin Mio. Jahre", t_Kelvin / JAHR / 1e6, 96)]

zeilen = ["Tutorium 7: Wärmebilanzen (instationär differentiell), Zahlen für teile/t7.md (Skript t7_rechnung.py)", "",
          f"{'Teil':9s} {'Größe':58s} {'Wert':>14s}  Einheit    | Schreibweise im Markdown"]
for teil, name, wert, einheit, tex in werte:
    zeilen.append(f"{teil:9s} {name:58s} {wert:14.5g}  {einheit:10s} | {tex or ''}")
zeilen += ["", "Abgleich mit den Kernzahlen der Ideensammlung (Abschnitt 4.7, gerundet):"]
for name, ist, soll in KERN:
    ok = abs(ist - soll) <= max(0.05 * abs(soll), 0.006)
    zeilen.append(f"  {name:22s} Skript {ist:10.4g}  Ideensammlung {soll:>7g}  {'ok' if ok else 'ABWEICHUNG'}")

fehlend = []
if os.path.exists(TEIL):
    md = ohne_mathrm(open(TEIL, encoding="utf-8").read())
    for teil, name, wert, einheit, tex in werte:
        if tex and ohne_mathrm(tex) not in md:
            fehlend.append(f"{teil}: {name}: {tex}")
    zeilen += ["", f"Abgleich mit {os.path.relpath(TEIL, os.path.dirname(HIER))}: "
               + ("alle Werte gefunden" if not fehlend else f"{len(fehlend)} Werte fehlen")]
    zeilen += ["  FEHLT " + f for f in fehlend]
else:
    zeilen += ["", "teile/t7.md noch nicht vorhanden, kein Abgleich"]

text = "\n".join(zeilen) + "\n"
with open(AUSGABE, "w", encoding="utf-8") as f:
    f.write(text)
print(text)
