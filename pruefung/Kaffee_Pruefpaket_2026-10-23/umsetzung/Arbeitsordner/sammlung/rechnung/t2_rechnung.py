# -*- coding: utf-8 -*-
"""Tutorium 2 (Konvektion) der Aufgabensammlung: alle Zahlen der Tabellen und Ergebniszeilen in ../teile/t2.md.

Aufgabe 1 (Offene Rinnen im Meereis): Arbeitswerte der Ideensammlung, Abschnitt 4.2, Rechnung wie in
nachrechnung_leitphaenomene.py (Ideensammlung, 17.10.2026) (Abschnitt T2). Stoffwerte der Luft mit CoolProp
(Lemmon et al. 2000, p = 1,01325 bar) bei der Filmtemperatur; gerechnet wird mit den gerundeten Tabellenwerten,
so wie die Studierenden rechnen. Die ungerundete Rechnung steht zum Vergleich daneben.
Zusatzaufgabe 1 (Windchill): quer angeströmter Zylinder, L = pi d/2, Übergangsbereich der Formelsammlung
(Nu = 0,3 + sqrt(Nu_l² + Nu_t²)), Stoffwerte der Luft bei der Lufttemperatur -10 °C (wie in der Nachrechnung).

Aufruf: python3 t2_rechnung.py
Schreibt t2_rechnung_ausgabe.txt (Name, Wert, Einheit) und prüft am Ende, ob jede Ergebniszeile und jeder Tabellenwert
genau so in ../teile/t2.md steht.
"""
import math
import os

from CoolProp.CoolProp import PropsSI
import sys as _sys, os as _os
_sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), "build"))
from indizes_aufrecht import ohne_mathrm   # Schreibweise prüfen unabhängig davon, ob Indizes aufrecht oder kursiv stehen

HIER = os.path.dirname(os.path.abspath(__file__))
TEIL = os.path.join(os.path.dirname(HIER), "teile", "t2.md")
AUSGABE = os.path.join(HIER, "t2_rechnung_ausgabe.txt")

K = 273.15
G = 9.81


def luft(th_C, p=101325.0):
    T = th_C + K
    rho = PropsSI("D", "T", T, "P", p, "Air")
    eta = PropsSI("V", "T", T, "P", p, "Air")
    lam = PropsSI("L", "T", T, "P", p, "Air")
    cp = PropsSI("C", "T", T, "P", p, "Air")
    return dict(lam=lam, nu=eta / rho, Pr=eta * cp / lam)


# ---------- Korrelationen der Formelsammlung SoSe 2026
def nu_lam(Re, Pr):                 # längs angeströmte Platte bzw. Zylinder, laminar
    return 0.664 * Re**0.5 * Pr**(1 / 3)


def nu_turb(Re, Pr):                # längs angeströmte Platte bzw. Zylinder, turbulent
    return 0.037 * Re**0.8 * Pr / (1 + 2.443 * Re**-0.1 * (Pr**(2 / 3) - 1))


def nu_platte(Re, Pr):
    """Platte: laminar für Re < 5e5, turbulent für 5e5 < Re < 1e7 (Gültigkeit wird gesondert geprüft)."""
    return nu_lam(Re, Pr) if Re < 5e5 else nu_turb(Re, Pr)


def nu_zylinder(Re, Pr):            # Übergangsbereich, 10 < Re < 1e7, L = pi d/2
    return 0.3 + math.sqrt(nu_lam(Re, Pr)**2 + nu_turb(Re, Pr)**2)


def f_waag(Pr):                     # waagerechte Platte, freie Konvektion
    return (1 + (0.322 / Pr)**(11 / 20))**(-20 / 11)


def nu_frei_waag(Gr, Pr):
    x = Gr * Pr * f_waag(Pr)
    return (0.766 * x**0.2, "laminar", x) if x <= 7e4 else (0.15 * x**(1 / 3), "turbulent", x)


# ----------------------------------------------------------------------------- Aufgabe 1: gegebene Größen
th_W, th_u = -1.8, -30.0    # °C Wasseroberfläche, Luft
w = 8.0                     # m/s Wind
b, l = 10.0, 1000.0         # m Breite in Windrichtung, Länge quer zum Wind
b1, b2 = 1.0, 100.0         # m schmale und breite Rinne (Teil f)
Re_krit = 5e5

th_m = 0.5 * (th_W + th_u)  # Filmtemperatur
ex = luft(th_m)             # CoolProp, ungerundet
# Tabellenwerte (gerundet wie in t2.md)
lam = round(ex["lam"], 5)
nu = round(ex["nu"], 8)
Pr = round(ex["Pr"], 3)
dT = th_W - th_u


def rinne(breite, s):
    Re = w * breite / s["nu"]
    Nu = nu_platte(Re, s["Pr"])
    a = Nu * s["lam"] / breite
    return dict(Re=Re, Nu=Nu, a=a, q=a * dT, gueltig=(Re < 1e7))


tab = dict(lam=lam, nu=nu, Pr=Pr)
r10, r1, r100 = rinne(b, tab), rinne(b1, tab), rinne(b2, tab)
r10x = rinne(b, ex)
x_krit = Re_krit * nu / w
Q_rinne = r10["q"] * b * l
# g) freie Konvektion, waagerechte Platte, L = A/U
L_frei = b * l / (2 * (b + l))
beta = 1 / (th_u + K)       # Formelsammlung: beta = 1/T_u (ideales Gas)
Gr = G * beta * dT * L_frei**3 / nu**2
Nu_f, form_f, x_f = nu_frei_waag(Gr, Pr)
a_frei = Nu_f * lam / L_frei
q_frei = a_frei * dT
Gr_x = G * beta * dT * L_frei**3 / ex["nu"]**2
a_frei_x = nu_frei_waag(Gr_x, ex["Pr"])[0] * ex["lam"] / L_frei

# ----------------------------------------------------------------------------- Zusatzaufgabe 1: Windchill
th_wc = -10.0
ex_wc = luft(th_wc)
lam_wc = round(ex_wc["lam"], 5)
nu_wc = round(ex_wc["nu"], 8)
Pr_wc = round(ex_wc["Pr"], 3)
w_wc, w_still = 5.0, 0.5
d_F, d_K = 0.02, 0.18


def zylinder(d, u, lam_, nu_, Pr_):
    L = math.pi * d / 2
    Re = u * L / nu_
    Nu = nu_zylinder(Re, Pr_)
    return dict(L=L, Re=Re, Nu=Nu, a=Nu * lam_ / L)


zF = zylinder(d_F, w_wc, lam_wc, nu_wc, Pr_wc)
zK = zylinder(d_K, w_wc, lam_wc, nu_wc, Pr_wc)
zK05 = zylinder(d_K, w_still, lam_wc, nu_wc, Pr_wc)
zFx = zylinder(d_F, w_wc, ex_wc["lam"], ex_wc["nu"], ex_wc["Pr"])
zKx = zylinder(d_K, w_wc, ex_wc["lam"], ex_wc["nu"], ex_wc["Pr"])


# ----------------------------------------------------------------------------- Ausgabe
def de(x, n):
    return f"{x:.{n}f}".replace(".", "{,}")


def zehner(x, n):
    """6.69e6 -> 6{,}69\\cdot 10^{6}"""
    e = int(math.floor(math.log10(abs(x))))
    m = x / 10**e
    return f"{de(m, n)}\\cdot 10^{{{e}}}"


ZEILEN = [
    ("AUFGABE 1: Offene Rinnen im Meereis, Tabelle", None, None, None, None),
    ("Rinne: Breite b in Windrichtung", b, ".0f", "m", r"b = 10\,\mathrm{m}"),
    ("Rinne: Länge l quer zum Wind", l / 1e3, ".0f", "km", r"l = 1\,\mathrm{km}"),
    ("Wasser: Temperatur theta_W", th_W, ".1f", "°C", r"\vartheta_{\mathrm{W}} = -1{,}8\,\mathrm{°C}"),
    ("Wind: Geschwindigkeit w", w, ".0f", "m/s", r"w = 8\,\mathrm{m/s}"),
    ("Wind: Lufttemperatur theta_u", th_u, ".0f", "°C", r"\vartheta_{\mathrm{u}} = -30\,\mathrm{°C}"),
    ("Luft bei Filmtemperatur: lambda (CoolProp)", ex["lam"], ".6f", "W/(m K)", None),
    ("Luft bei Filmtemperatur: lambda (Tabelle)", lam, ".5f", "W/(m K)", r"\lambda = " + de(lam, 5) + r"\,\mathrm{W/(m\,K)}"),
    ("Luft bei Filmtemperatur: nu (CoolProp)", ex["nu"], ".5e", "m²/s", None),
    ("Luft bei Filmtemperatur: nu (Tabelle)", nu, ".4e", "m²/s", r"\nu = " + zehner(nu, 3) + r"\,\mathrm{m^2/s}"),
    ("Luft bei Filmtemperatur: Pr (CoolProp)", ex["Pr"], ".5f", "-", None),
    ("Luft bei Filmtemperatur: Pr (Tabelle)", Pr, ".3f", "-", r"Pr = " + de(Pr, 3)),
    ("Weitere Rinnen: schmal b_1", b1, ".0f", "m", r"b_1 = 1\,\mathrm{m}"),
    ("Weitere Rinnen: breit b_2", b2, ".0f", "m", r"b_2 = 100\,\mathrm{m}"),
    ("AUFGABE 1: Ergebnisse (mit den Tabellenwerten)", None, None, None, None),
    ("d) Filmtemperatur theta_m", th_m, ".2f", "°C", r"\vartheta_{\mathrm{m}} = " + de(th_m, 1)),
    ("d) Reynolds-Zahl Re (b = 10 m)", r10["Re"], ".4e", "-", r"Re = " + zehner(r10["Re"], 2)),
    ("d) Umschlag laminar/turbulent nach x_krit", x_krit, ".4f", "m", r"x_{\mathrm{krit}} = " + de(x_krit, 2)),
    ("e) Nußelt-Zahl Nu (turbulent, Platte)", r10["Nu"], ".1f", "-", r"Nu = " + f"{r10['Nu']:.0f}"),
    ("e) alpha (b = 10 m)", r10["a"], ".3f", "W/(m² K)", r"\alpha = " + de(r10["a"], 1)),
    ("e) Wärmestromdichte q (b = 10 m)", r10["q"], ".2f", "W/m²", r"\dot{q} = " + f"{r10['q']:.0f}"),
    ("e) Wärmestrom der ganzen Rinne Q", Q_rinne / 1e6, ".4f", "MW", r"\dot{Q} = " + de(Q_rinne / 1e6, 2)),
    ("   ungerundet (CoolProp): alpha (b = 10 m)", r10x["a"], ".3f", "W/(m² K)", None),
    ("   ungerundet (CoolProp): q (b = 10 m)", r10x["q"], ".2f", "W/m²", None),
    ("f) Re (b_1 = 1 m)", r1["Re"], ".4e", "-", None),
    ("f) alpha_1 (b_1 = 1 m), gültig", r1["a"], ".3f", "W/(m² K)", r"\alpha_1 = " + de(r1["a"], 1)),
    ("f) q (b_1 = 1 m)", r1["q"], ".1f", "W/m²", None),
    ("f) Re_2 (b_2 = 100 m), außerhalb (Re > 1e7)", r100["Re"], ".4e", "-", r"Re_2 = " + zehner(r100["Re"], 2)),
    ("f) alpha_2 (b_2 = 100 m), nur Tendenz", r100["a"], ".3f", "W/(m² K)", r"\alpha_2 = " + de(r100["a"], 1)),
    ("f) q (b_2 = 100 m)", r100["q"], ".1f", "W/m²", None),
    ("f) alpha_1/alpha (10 m)", r1["a"] / r10["a"], ".3f", "-", None),
    ("f) alpha_1/alpha_2", r1["a"] / r100["a"], ".3f", "-", None),
    ("g) charakteristische Länge L = A/U", L_frei, ".4f", "m", r"L = " + de(L_frei, 2)),
    ("g) beta = 1/T_u", beta, ".6f", "1/K", None),
    ("g) Grashof-Zahl Gr", Gr, ".4e", "-", r"Gr = " + zehner(Gr, 2)),
    ("g) Gr Pr f(Pr) (> 7e4: turbulent)", x_f, ".4e", "-", None),
    ("g) Nu (freie Konvektion, " + form_f + ")", Nu_f, ".2f", "-", None),
    ("g) alpha (frei)", a_frei, ".4f", "W/(m² K)", r"\alpha = " + de(a_frei, 2)),
    ("g) q (frei)", q_frei, ".2f", "W/m²", r"\dot{q} = " + f"{q_frei:.0f}"),
    ("   ungerundet (CoolProp): alpha (frei)", a_frei_x, ".4f", "W/(m² K)", None),
    ("ZUSATZAUFGABE 1: Windchill", None, None, None, None),
    ("Lufttemperatur theta_u", th_wc, ".0f", "°C", r"\vartheta_{\mathrm{u}} = -10\,\mathrm{°C}"),
    ("Luft bei -10 °C: lambda (CoolProp)", ex_wc["lam"], ".6f", "W/(m K)", None),
    ("Luft bei -10 °C: lambda (Text)", lam_wc, ".5f", "W/(m K)", r"\lambda = " + de(lam_wc, 5) + r"\,\mathrm{W/(m\,K)}"),
    ("Luft bei -10 °C: nu (CoolProp)", ex_wc["nu"], ".5e", "m²/s", None),
    ("Luft bei -10 °C: nu (Text)", nu_wc, ".4e", "m²/s", r"\nu = " + zehner(nu_wc, 3) + r"\,\mathrm{m^2/s}"),
    ("Luft bei -10 °C: Pr (CoolProp)", ex_wc["Pr"], ".5f", "-", None),
    ("Luft bei -10 °C: Pr (Text)", Pr_wc, ".3f", "-", r"Pr = " + de(Pr_wc, 3)),
    ("Wind w", w_wc, ".0f", "m/s", r"w = 5\,\mathrm{m/s}"),
    ("Finger: d", d_F * 100, ".0f", "cm", r"d_{\mathrm{F}} = 2\,\mathrm{cm}"),
    ("Kopf: d", d_K * 100, ".0f", "cm", r"d_{\mathrm{K}} = 18\,\mathrm{cm}"),
    ("a) Finger: L = pi d/2", zF["L"], ".5f", "m", None),
    ("a) Finger: Re", zF["Re"], ".0f", "-", None),
    ("a) Finger: Nu", zF["Nu"], ".2f", "-", None),
    ("a) Finger: alpha_F", zF["a"], ".3f", "W/(m² K)", r"\alpha_{\mathrm{F}} = " + de(zF["a"], 1)),
    ("a) Kopf: L = pi d/2", zK["L"], ".5f", "m", None),
    ("a) Kopf: Re", zK["Re"], ".0f", "-", None),
    ("a) Kopf: Nu", zK["Nu"], ".2f", "-", None),
    ("a) Kopf: alpha_K", zK["a"], ".3f", "W/(m² K)", r"\alpha_{\mathrm{K}} = " + de(zK["a"], 1)),
    ("   ungerundet (CoolProp): alpha_F / alpha_K", zFx["a"], ".3f", "W/(m² K)", None),
    ("   ungerundet (CoolProp): alpha_K", zKx["a"], ".3f", "W/(m² K)", None),
    ("b) Verhältnis alpha_F/alpha_K", zF["a"] / zK["a"], ".3f", "-", r"\alpha_{\mathrm{F}}/\alpha_{\mathrm{K}} = " + de(zF["a"] / zK["a"], 2)),
    ("c) Kopf bei 0,5 m/s: Re", zK05["Re"], ".0f", "-", None),
    ("c) Kopf bei 0,5 m/s: alpha", zK05["a"], ".3f", "W/(m² K)", r"\alpha_{\mathrm{K}}(0{,}5\,\mathrm{m/s}) = " + de(zK05["a"], 1)),
    ("c) Faktor alpha_K(5 m/s)/alpha_K(0,5 m/s)", zK["a"] / zK05["a"], ".3f", "-", r"Faktor $" + de(zK["a"] / zK05["a"], 1)),
]


def main():
    zeilen = ["Tutorium 2: Konvektion (Zahlen für teile/t2.md, Skript t2_rechnung.py)"]
    for name, wert, fmt, einheit, _ in ZEILEN:
        if wert is None:
            zeilen.append("")
            zeilen.append(name)
            continue
        zeilen.append(f"{name:55s} {wert:>14{fmt}} {einheit}")
    zeilen.append("")
    zeilen.append("ABGLEICH mit teile/t2.md (jede Zeichenkette muss im Markdown stehen)")
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
        zeilen.append("teile/t2.md fehlt noch")
        fehlt = -1
    zeilen.append(f"Ergebnis des Abgleichs: {'alles gefunden' if fehlt == 0 else str(fehlt) + ' fehlen'}")
    text = "\n".join(zeilen) + "\n"
    with open(AUSGABE, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
