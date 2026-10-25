# -*- coding: utf-8 -*-
"""Abb. 2 in Tutorium 5 (Aufgabe 2, AMOC): Schnitt durch den Atlantik von Süd nach Nord mit warmem
Oberflächenstrom nach Norden, kaltem Rückstrom in der Tiefe und Wärmeabgabe an die Luft; darüber Paderborn
und Goose Bay auf fast derselben Breite. Kein Bilanzraum (wird in Teil a eingezeichnet).
Aufruf: python3 abb_t5_amoc.py   (schreibt ../grafik/t5_amoc.png und .svg)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from skizze_stil import *

WARMSCHICHT = "#F4DCD5"          # warmes Oberflächenwasser (Fläche)

fig, ax = leinwand(6.8, 3.75, xlim=(0, 13.6), ylim=(0, 7.5))


def x(phi):
    """geographische Breite in Grad Nord -> x-Koordinate (nicht maßstäblich zur Tiefe)"""
    return 1.0 + (phi - 15.0) * 0.2


Y_BODEN, Y_OBEN, Y_LUFT = 1.0, 3.8, 5.5

# Ozean (Süden offen, im Norden Schelf und Land)
ozean = [(0.5, Y_BODEN), (x(66.5), Y_BODEN), (x(70.0) + 0.3, Y_OBEN), (0.5, Y_OBEN)]
ax.add_patch(Polygon(ozean, closed=True, facecolor=WASSER, edgecolor="none", zorder=0))
warm = [(0.5, 2.95), (x(40), 3.1), (x(55), 3.35), (x(64), 3.6), (x(66), Y_OBEN), (0.5, Y_OBEN)]
ax.add_patch(Polygon(warm, closed=True, facecolor=WARMSCHICHT, edgecolor="none", zorder=0))
land = [(x(66.5), Y_BODEN), (13.4, Y_BODEN), (13.4, 4.15), (x(70.0) + 0.9, 4.0), (x(70.0) + 0.3, Y_OBEN)]
ax.add_patch(Polygon(land, closed=True, facecolor=BODEN, edgecolor=LINIE, linewidth=1.0, zorder=1))
ax.add_patch(Rectangle((0.5, Y_BODEN - 0.22), x(66.5) - 0.5, 0.22, facecolor=GESTEIN, edgecolor="none", zorder=1))
ax.plot([0.5, x(66.5)], [Y_BODEN, Y_BODEN], color=LINIE, lw=1.0, zorder=2)
ax.plot([0.5, x(70.0) + 0.3], [Y_OBEN, Y_OBEN], color=KALT, lw=1.2, zorder=2)

# Strömungen
pfeil(ax, (0.9, 3.4), (x(63.5), 3.4), farbe=WARM, breite=2.0, groesse=13)
text(ax, x(30), 3.12, r"warmes Oberflächenwasser: $\dot{V}$, $\vartheta_w$", fs=9.5, farbe=WARM, ha="left")
pfeil(ax, (x(64.2), 3.35), (x(64.2), 1.75), farbe=KALT, breite=2.0, groesse=13, connectionstyle="arc3,rad=-0.55")
text(ax, x(64.2) - 0.2, 2.55, "Absinken", fs=9, farbe=KALT, ha="right")
pfeil(ax, (x(63.0), 1.55), (0.9, 1.55), farbe=KALT, breite=2.0, groesse=13)
text(ax, x(30), 1.83, r"kaltes Tiefenwasser: $\dot{V}$, $\vartheta_k$", fs=9.5, farbe=KALT, ha="left")

# Messlinie bei 26,5° N
ax.plot([x(26.5), x(26.5)], [Y_BODEN - 0.22, Y_LUFT - 0.35], color=GRAU, lw=1.0, ls=(0, (4, 3)), zorder=3)
text(ax, x(26.5), Y_LUFT - 0.1, r"26,5° N: $\dot{V}$ und $\dot{Q}_{AMOC}$", fs=9.5, farbe=LINIE)

# Wärmeabgabe an die Luft zwischen 40° und 70° N
for phi in (42.0, 46.5, 57.5, 62.0, 66.5):
    waermepfeil(ax, (x(phi), Y_OBEN + 0.12), (x(phi), Y_OBEN + 0.95))
text(ax, x(57.0) + 0.6, Y_OBEN + 1.25, "Wärmeabgabe an die Luft", fs=9.5, farbe=WAERME)
text(ax, 0.62, Y_OBEN + 0.55, "Luft", fs=9, farbe=GRAU, ha="left")

# Breitenachse
pfeil(ax, (0.5, 0.42), (13.5, 0.42), farbe=GRAU, breite=0.9, groesse=9)
for phi, s in ((26.5, "26,5° N"), (40.0, "40° N"), (70.0, "70° N")):
    ax.plot([x(phi), x(phi)], [0.32, 0.52], color=GRAU, lw=0.9)
    text(ax, x(phi), 0.08, s, fs=9, farbe=GRAU)
text(ax, 0.5, 0.08, "Süden", fs=9, farbe=GRAU, ha="left")
text(ax, 12.6, 0.08, "Norden", fs=9, farbe=GRAU, ha="left")

# Paderborn und Goose Bay
Y_ORT = 6.75
for phi in (51.7, 53.3):
    ax.add_patch(Circle((x(phi), Y_ORT), 0.09, facecolor=LINIE, edgecolor="none", zorder=5))
    ax.plot([x(phi), x(phi)], [Y_ORT - 0.12, Y_ORT - 0.55], color=GRAU, lw=0.8)
text(ax, x(51.7) - 0.25, Y_ORT + 0.12, "Paderborn, 51,7° N", fs=9.5, ha="right")
text(ax, x(51.7) - 0.25, Y_ORT - 0.3, "(Europa, Ostseite)", fs=8.5, farbe=GRAU, ha="right")
text(ax, x(53.3) + 0.25, Y_ORT + 0.12, "Goose Bay, 53,3° N", fs=9.5, ha="left")
text(ax, x(53.3) + 0.25, Y_ORT - 0.3, "(Labrador, Westseite)", fs=8.5, farbe=GRAU, ha="left")
text(ax, 0.5, 7.25, "Schnitt durch den Atlantik, nicht maßstäblich", fs=8.5, farbe=GRAU, ha="left")

if __name__ == "__main__":
    print(speichern(fig, "t5_amoc"))
