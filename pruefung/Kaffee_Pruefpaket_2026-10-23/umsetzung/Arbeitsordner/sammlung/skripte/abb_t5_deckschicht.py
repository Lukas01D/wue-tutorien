# -*- coding: utf-8 -*-
"""Abb. 3 in Tutorium 5 (Aufgabe 3, Ozean als Wärmespeicher): Küste mit Boden (Vergleich) und Ozean mit
durchmischter Deckschicht der Tiefe h über der Tiefsee; zusätzliche Strahlungsflussdichte q_F von oben.
Kein Bilanzraum und keine abgeführte Wärme (beides zeichnen die Studierenden in Teil a ein).
Aufruf: python3 abb_t5_deckschicht.py   (schreibt ../grafik/t5_deckschicht.png und .svg)"""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from skizze_stil import *

TIEFSEE = "#B7D3EC"

fig, ax = leinwand(6.6, 3.3, xlim=(0, 13.2), ylim=(0, 6.6))

Y_LAND, Y_MEER, Y_SPRUNG, Y_GRUND = 4.15, 3.95, 2.1, 0.55
X_KUESTE = 3.4

# Atmosphäre
ax.add_patch(Rectangle((0.0, 5.45), 13.2, 0.75, facecolor="#E9EEF3", edgecolor="none", zorder=0))
text(ax, 6.6, 5.83, "Atmosphäre mit doppeltem CO₂-Gehalt", fs=9.5, farbe=GRAU)
text(ax, 0.0, 6.45, "nicht maßstäblich", fs=8.5, farbe=GRAU, ha="left")

# Land: Boden (Vergleich) über Gestein
ax.add_patch(Polygon([(0, Y_GRUND), (X_KUESTE + 1.6, Y_GRUND), (X_KUESTE + 0.2, Y_MEER - 0.35), (X_KUESTE, Y_LAND),
                      (0, Y_LAND)], closed=True, facecolor=GESTEIN, edgecolor="none", zorder=1))
ax.add_patch(Polygon([(0, Y_LAND - 0.62), (X_KUESTE - 0.22, Y_LAND - 0.62), (X_KUESTE, Y_LAND), (0, Y_LAND)],
                     closed=True, facecolor=BODEN, edgecolor="none", zorder=2))
ax.plot([0, X_KUESTE, X_KUESTE + 0.2, X_KUESTE + 1.6], [Y_LAND, Y_LAND, Y_MEER - 0.35, Y_GRUND], color=LINIE, lw=1.0, zorder=3)
text(ax, 1.15, Y_LAND - 0.31, "Boden", fs=9)
masslinie(ax, (2.55, Y_LAND - 0.62), (2.55, Y_LAND), r"$h_\mathrm{B}$", fs=9.5, versatz=(0.1, 0.0))
text(ax, 1.4, 1.6, "Land", fs=9.5, farbe=LINIE)

# Ozean: Deckschicht und Tiefsee
xs = np.linspace(X_KUESTE + 0.07, 13.2, 300)
welle = Y_MEER + 0.05 * np.sin(xs * 5.0)
ax.fill_between(xs, np.full_like(xs, Y_SPRUNG), welle, color=WASSER, zorder=0, lw=0)
ax.add_patch(Rectangle((X_KUESTE, Y_GRUND), 13.2 - X_KUESTE, Y_SPRUNG - Y_GRUND, facecolor=TIEFSEE, edgecolor="none", zorder=0))
ax.plot(xs, welle, color=KALT, lw=1.1, zorder=3)
ax.plot([X_KUESTE + 0.89, 13.2], [Y_SPRUNG, Y_SPRUNG], color=KALT, lw=0.9, ls=(0, (5, 3)), zorder=3)
ax.plot([X_KUESTE + 1.6, 13.2], [Y_GRUND, Y_GRUND], color=LINIE, lw=1.0, zorder=3)
text(ax, 8.3, 1.3, "Tiefsee (kälter, kaum durchmischt)", fs=9.5, farbe=LINIE)

# Durchmischung durch Wind und Wellen
for xm, ym in ((6.0, 3.05), (8.0, 2.8), (10.0, 3.1)):
    a, b, th = 0.475, 0.35, np.radians(330.0)
    ax.add_patch(Arc((xm, ym), 2 * a, 2 * b, theta1=20, theta2=330, edgecolor=KALT, lw=1.1, zorder=4))
    p_end = (xm + a * np.cos(th), ym + b * np.sin(th))          # Ende des Bogens, Pfeil tangential
    t = np.array([-a * np.sin(th), b * np.cos(th)])
    t = 0.12 * t / np.hypot(*t)
    pfeil(ax, (p_end[0] - t[0], p_end[1] - t[1]), (p_end[0] + t[0], p_end[1] + t[1]), farbe=KALT, breite=1.1, groesse=8, z=4)
text(ax, 8.0, 3.55, r"Deckschicht, durchmischt: Erwärmung $\Delta T(t)$", fs=9.5, farbe=LINIE)
pfeil(ax, (8.6, 4.45), (10.4, 4.45), farbe=GRAU, breite=1.2, groesse=10)
text(ax, 9.5, 4.62, "Wind", fs=9, farbe=GRAU, va="bottom")
masslinie(ax, (12.6, Y_SPRUNG), (12.6, Y_MEER - 0.05), r"$h$", fs=10, versatz=(0.1, 0.0))

# zusätzliche Strahlungsflussdichte
for xq in (1.4, 5.3, 7.0):
    waermepfeil(ax, (xq, 5.4), (xq, Y_LAND + 0.12 if xq < X_KUESTE else Y_MEER + 0.15))
text(ax, 1.55, 4.8, r"$\dot{q}_\mathrm{F}$", fs=10.5, farbe=WAERME, ha="left")
text(ax, 7.15, 4.75, r"$\dot{q}_\mathrm{F}$", fs=10.5, farbe=WAERME, ha="left")

if __name__ == "__main__":
    print(speichern(fig, "t5_deckschicht"))
