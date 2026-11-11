# -*- coding: utf-8 -*-
"""Vergleichswerte für die Regler kA und C_T der schlanken Kaffee-Simulation (Recherche vom 12.11.2026).

Rechnet aus den belegten Angaben (Quellen Q1 bis Q13 in QUELLEN_Vergleichswerte.md) kA und C_T und prüft, dass die
Bereiche in src/schlank.js (Liste VERGLEICH) die Werte abdecken. Aufruf: python3 simulation/minimal/vergleichswerte.py
Ausgabe: Tabellen in Markdown (für QUELLEN_Vergleichswerte.md) und die Prüfung.
"""
import math
import os
import re
import sys

CP_W = 4180.0          # J/(kg K), Wasser bei etwa 50 bis 90 °C
RHO_W = 1.0            # kg/l (gerundet)


def kA_aus(C, t_s, th0, th, thu):
    """kA aus einer Abkühlung von th0 auf th in t_s Sekunden bei Raumtemperatur thu (Modell des Blatts)."""
    return C / t_s * math.log((th0 - thu) / (th - thu))


def C_wasser(liter):
    return liter * RHO_W * CP_W


# ------------------------------------------------------------ kA in W/K
KA = []   # (Gegenstand, kA_min, kA_max, Quelle, Bemerkung)
KA.append(("Isolierflasche 0,5 l, Mindestwert der Norm", None, kA_aus(C_wasser(0.5), 6 * 3600, 95, 70, 20), "Q1",
           "EN 12546-1: 95 °C, 6 h, 20 °C, am Ende mindestens 70 °C; Wert ist die Obergrenze für eine Flasche, die die Norm erfüllt"))
KA.append(("Isolierflasche 1 l, Mindestwert der Norm", None, kA_aus(C_wasser(1.0), 6 * 3600, 95, 78, 20), "Q1",
           "wie oben, am Ende mindestens 78 °C"))
KA.append(("sehr gute Isolierflasche (Ikea Volym)", kA_aus(C_wasser(0.5), 6 * 3600, 95, 86, 20), kA_aus(C_wasser(0.5), 24 * 3600, 95, 64, 20), "Q3",
           "95 °C, nach 6 h 86 °C, nach 24 h fast 64 °C; Füllung 0,5 l und Raum 20 °C angenommen (nicht genannt)"))
KA.append(("guter Thermobecher (bester im Test)", kA_aus(C_wasser(0.3), 3600, 80, 76, 20), kA_aus(C_wasser(0.4), 3600, 80, 76, 20), "Q2",
           "80 °C, in der ersten Stunde 4 K weniger; Füllung 0,3 bis 0,4 l und Raum 20 °C angenommen"))
KA.append(("schwacher Thermobecher (schlechtester im Test)", kA_aus(C_wasser(0.3), 3600, 80, 61, 20), kA_aus(C_wasser(0.4), 3600, 80, 61, 20), "Q2",
           "80 °C, in der ersten Stunde 19 K weniger; Annahmen wie oben"))
C_glas = 0.140 * CP_W + 0.152 * 840
KA.append(("Trinkglas 140 ml, Seitenwand (oben und unten gedämmt)", C_glas / (49 * 60), C_glas / (49 * 60), "Q4",
           "τ = 49 min; C aus 140 cm³ Wasser und 152 g Glas"))
KA.append(("Kunststoffbecher 140 ml, Seitenwand", (0.140 * CP_W + 0.0235 * 460) / (55 * 60), (0.140 * CP_W + 0.0235 * 460) / (55 * 60), "Q4", "τ = 55 min"))
KA.append(("Styroporbecher 140 ml, Seitenwand", (0.140 * CP_W + 0.0082 * 1300) / (65 * 60), (0.140 * CP_W + 0.0082 * 1300) / (65 * 60), "Q4", "τ = 65 min"))
KA.append(("Keramiktasse 200 ml mit Deckel (Blatt, vorläufig)", 0.1994, 0.1994, "Q13", "aus 72 °C nach 10 min (Annahme der TL, Messung im Januar)"))
KA.append(("Tasse mit Deckel, Abschätzung h·A", 10 * 0.020, 12 * 0.030, "eigene Abschätzung",
           "h = 10 bis 12 W/(m²K) (freie Konvektion und Strahlung), benetzte Außenfläche 0,02 bis 0,03 m²"))
KA.append(("offene Tasse (mit Verdunstung, grob)", (C_wasser(0.2) + 255) / (22 * 60), (C_wasser(0.3) + 255) / (22 * 60), "Q5 und eigene Abschätzung",
           "τ ≈ 22 min für offenen Kaffee; Füllung 0,2 bis 0,3 l und Porzellantasse 255 J/K angenommen; Verdunstung ist im Modell nicht enthalten, der Wert ist nur ein Ersatz"))

# ------------------------------------------------------------ C_T in J/K
CT = []   # (Gegenstand, Masse in g, c in J/(kg K) von, bis, Quelle, Bemerkung)
CT.append(("Pappbecher 0,3 l mit Deckel", 11 + 3.4, 1300, 1340, "Q8, Q6", "Becher 11 g (10 bis 18 g), Deckel 3,4 g; c Papier 1340, Deckel als Kunststoff etwa 1300 angenommen"))
CT.append(("doppelwandiges Glas 0,25 l (Bodum Pavina)", 100, 750, 840, "Q12, Q6", "etwa 100 g je Glas, falls 0,6 kg für den Satz gelten (unklar); mit dem Inhalt in Kontakt ist nur die Innenwand"))
CT.append(("dünnes Trinkglas", 152, 840, 840, "Q4, Q6, Q7", "152 g; c Fensterglas 840 (Q6, Q7); Q4 nennt 500 bis 840, der untere Wert gilt für Bleiglas"))
CT.append(("Steingutbecher 30 cl (Ikea Dinera)", 300, 800, 800, "Q9, Q6", "Paket 0,32 kg, Becher also etwa 0,30 kg (geschätzt); c Steingut 800"))
CT.append(("Porzellantasse 300 g (Blatt, Experiment)", 300, 850, 850, "Q13", "werte.py: M_TASSE 0,300 kg, C_KERAMIK 850"))
CT.append(("Einmachglas 580 ml (Weck)", 306, 840, 840, "Q10, Q6", "306 g (ob mit Deckel, ist nicht angegeben)"))
CT.append(("schwerer Porzellanbecher 300 ml", 540, 850, 1070, "Q11, Q6", "540 g; c Porzellan 850 (Blatt) bis 1070 (Q6)"))


def bereiche_aus_js():
    """Liest die Bereiche aus src/schlank.js (Liste VERGLEICH), damit Recherche und Seite zusammenpassen."""
    js = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "src", "schlank.js"), encoding="utf-8").read()
    teil = js[js.index("const VERGLEICH = {"):]
    teil = teil[:teil.index("\n  };") + 4]
    erg = {}
    for gr in ("kA", "CT"):
        block = re.search(gr + r": \[(.*?)\n    \]", teil, re.S).group(1)
        erg[gr] = [(float(a), TEXTE.get(b, b)) for a, b in re.findall(r"\[\s*([0-9.]+)\s*,\s*\"([^\"]+)\"", block)]
    return erg


def texte_de():
    t, k = {}, None
    for z in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "src", "texte_schlank_de.txt"), encoding="utf-8").read().split("\n"):
        if z.startswith("@"):
            k = z[1:].strip(); t[k] = ""
        elif k and z.strip() and not z.startswith("#"):
            t[k] = (t[k] + " " + z.strip()).strip()
    return t


TEXTE = texte_de()


def label(liste, x):
    t = None
    for grenze, k in liste:
        if x >= grenze - 1e-12:
            t = k
    return t


def main():
    z = lambda x: ("%.3f" % x).replace(".", ",")
    print("### kA (W/K)\n\n| Gegenstand | kA | Quelle | Bemerkung |\n|:--|:--|:--|:--|")
    for g, a, b, q, bem in KA:
        w = ("bis " + z(b)) if a is None else (z(a) if abs(a - b) < 5e-4 else z(min(a, b)) + " bis " + z(max(a, b)))
        print("| %s | %s | %s | %s |" % (g, w, q, bem))
    print("\n### Wärmekapazität der Tasse C_T (J/K)\n\n| Gegenstand | Masse in g | C_T | Quelle | Bemerkung |\n|:--|:--|:--|:--|:--|")
    for g, m, c1, c2, q, bem in CT:
        a, b = m / 1000 * c1, m / 1000 * c2
        w = "%.0f" % a if abs(a - b) < 0.5 else "%.0f bis %.0f" % (a, b)
        print("| %s | %s | %s | %s | %s |" % (g, ("%.1f" % m).replace(".", ",").replace(",0", ""), w, q, bem))
    try:
        b = bereiche_aus_js()
    except (ValueError, AttributeError):
        print("\n(Bereiche in schlank.js noch nicht vorhanden)")
        return
    print("\n### Prüfung: Welcher Vergleich erscheint beim belegten Wert?\n\n| Regler | Gegenstand | Wert | angezeigt |\n|:--|:--|:--|:--|")
    fehler = 0
    for g, a, bb, q, bem in KA:
        x = bb if a is None else (a + bb) / 2
        print("| kA | %s | %s | %s |" % (g, z(x), label(b["kA"], x)))
    for g, m, c1, c2, q, bem in CT:
        x = m / 1000 * (c1 + c2) / 2
        print("| C_T | %s | %.0f | %s |" % (g, x, label(b["CT"], x)))
    erwartet = {"Isolierflasche": "Isolierflasche", "Thermobecher": "Thermobecher", "mit Deckel": "mit Deckel", "offene": "offene",
                "Pappbecher": "Pappbecher", "dünnes": "Trinkglas", "Porzellantasse 300": "Porzellan", "Einmachglas": "Einmachglas", "schwerer": "schwer"}
    for g, a, bb, q, bem in KA:
        x = bb if a is None else (a + bb) / 2
        for k, v in erwartet.items():
            if k in g and v not in (label(b["kA"], x) or ""):
                if not (k == "Thermobecher" and "schwacher" in g):
                    print("PRÜFEN: kA", g, "->", label(b["kA"], x)); fehler += 1
    for g, m, c1, c2, q, bem in CT:
        x = m / 1000 * (c1 + c2) / 2
        for k, v in erwartet.items():
            if k in g and v not in (label(b["CT"], x) or ""):
                print("PRÜFEN: C_T", g, "->", label(b["CT"], x)); fehler += 1
    print("\n%s" % ("Bereiche passen zu den Belegen." if not fehler else "%d Stellen prüfen." % fehler))
    sys.exit(1 if fehler else 0)


if __name__ == "__main__":
    main()
