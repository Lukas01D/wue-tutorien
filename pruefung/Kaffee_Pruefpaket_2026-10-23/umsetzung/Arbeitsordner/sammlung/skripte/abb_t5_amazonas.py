# -*- coding: utf-8 -*-
"""Abb. 4 in Tutorium 5 (Aufgabe 4, Sverdrup und der Amazonas): Schnitt durch das Amazonasbecken von den Anden
bis zum Atlantik mit Niederschlag, Verdunstung über dem Regenwald, Abfluss des Flusses und Flussfahne im Meer.
Kein Bilanzraum (wird in Teil c gewählt).
Aufruf: python3 abb_t5_amazonas.py   (schreibt ../grafik/t5_amazonas.png und .svg)"""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from skizze_stil import *

WALD = "#7E9F6A"
STAMM = "#6B5640"
WOLKE = "#E4E8EC"
FAHNE = "#D8C9A0"

fig, ax = leinwand(6.6, 3.2, xlim=(0, 13.2), ylim=(0, 6.4))

Y_LAND, Y_MEER, Y_UNTEN = 1.95, 1.75, 0.95
X_KUESTE = 10.3

# Meer mit Flussfahne
ax.add_patch(Rectangle((X_KUESTE - 0.3, Y_UNTEN), 13.2 - X_KUESTE + 0.3, Y_MEER - Y_UNTEN, facecolor=WASSER, edgecolor="none", zorder=0))
ax.add_patch(Polygon([(X_KUESTE, Y_MEER), (12.7, Y_MEER), (12.3, Y_MEER - 0.22), (X_KUESTE, Y_MEER - 0.32)],
                     closed=True, facecolor=FAHNE, edgecolor="none", zorder=1))
ax.plot([X_KUESTE - 0.1, 13.2], [Y_MEER, Y_MEER], color=KALT, lw=1.1, zorder=3)
text(ax, 12.15, 1.22, "Atlantik", fs=9.5, farbe=LINIE)
text(ax, 11.55, 2.25, r"Flussfahne: $\vartheta_F$", fs=9.5, farbe=LINIE)

# Land mit Anden im Westen
land = [(0, Y_UNTEN), (X_KUESTE + 0.25, Y_UNTEN), (X_KUESTE + 0.25, Y_MEER - 0.1), (X_KUESTE, Y_LAND - 0.12),
        (1.9, Y_LAND), (1.2, 3.6), (0.75, 4.15), (0.35, 3.75), (0, 3.95)]
ax.add_patch(Polygon(land, closed=True, facecolor=BODEN, edgecolor=LINIE, linewidth=1.0, zorder=2))
text(ax, 0.75, 4.45, "Anden", fs=9, farbe=GRAU)

# Fluss im Bett, Abfluss ins Meer
ax.add_patch(Polygon([(2.0, Y_LAND), (X_KUESTE, Y_LAND - 0.12), (X_KUESTE, Y_LAND - 0.3), (2.0, Y_LAND - 0.14)],
                     closed=True, facecolor=KALT, edgecolor="none", zorder=3))
pfeil(ax, (X_KUESTE - 0.6, Y_LAND - 0.2), (X_KUESTE + 1.1, Y_MEER - 0.16), farbe=KALT, breite=2.2, groesse=13, z=6)
text(ax, 6.2, 1.35, r"Amazonas: Abfluss $\dot{V}_A$, Temperatur $\vartheta_A$", fs=9.5, farbe=KALT)

# Regenwald
for xb in np.arange(2.3, 9.9, 0.52):
    ax.plot([xb, xb], [Y_LAND - 0.02, Y_LAND + 0.32], color=STAMM, lw=1.4, zorder=4)
    ax.add_patch(Circle((xb, Y_LAND + 0.5), 0.29, facecolor=WALD, edgecolor="#5C7A4C", lw=0.6, zorder=5))
text(ax, 4.0, 2.88, "Regenwald", fs=9, farbe="#4A6340")

# Niederschlag aus der Wolke
WOLKEN = ((2.9, 5.25, 2.2, 0.95), (4.4, 5.55, 2.8, 1.15), (5.9, 5.25, 2.2, 0.95), (3.6, 4.98, 2.0, 0.6), (5.2, 4.98, 2.0, 0.6))
for xw, yw, bw, hw in WOLKEN:          # erst Umrisse, dann Füllung darüber: eine gemeinsame Kontur
    ax.add_patch(Ellipse((xw, yw), bw, hw, facecolor=WOLKE, edgecolor="#9AA3AD", lw=1.6, zorder=2))
for xw, yw, bw, hw in WOLKEN:
    ax.add_patch(Ellipse((xw, yw), bw, hw, facecolor=WOLKE, edgecolor="none", zorder=2.1))
for xr in np.arange(2.5, 6.5, 0.45):
    pfeil(ax, (xr, 4.75), (xr - 0.25, 3.45), farbe=KALT, breite=1.0, groesse=7, z=3)
text(ax, 4.4, 5.3, r"Niederschlag $N$", fs=9.5, farbe=LINIE, zorder=3)

# Verdunstung (wellige Pfeile nach oben)
for xv in (7.5, 8.3, 9.1):
    ys = np.linspace(2.95, 4.35, 60)
    ax.plot(xv + 0.09 * np.sin((ys - 2.95) * 9.0), ys, color="#5B8DB8", lw=1.3, zorder=4)
    pfeil(ax, (xv + 0.09 * np.sin(1.35 * 9.0), 4.33), (xv + 0.09 * np.sin(1.4 * 9.0), 4.6), farbe="#5B8DB8", breite=1.3, groesse=9, z=4)
text(ax, 8.3, 4.95, "Verdunstung", fs=9.5, farbe="#3F6E99")

# Ausdehnung des Beckens
masslinie(ax, (1.9, 0.5), (X_KUESTE, 0.5), "", fs=9)
text(ax, 6.1, 0.2, r"Becken mit der Fläche $A_B$", fs=9.5, farbe=GRAU)
text(ax, 13.2, 6.15, "nicht maßstäblich", fs=8.5, farbe=GRAU, ha="right")
text(ax, 0.0, 0.2, "Westen", fs=9, farbe=GRAU, ha="left")
text(ax, 13.2, 0.2, "Osten", fs=9, farbe=GRAU, ha="right")

if __name__ == "__main__":
    print(speichern(fig, "t5_amazonas"))
