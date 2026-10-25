# -*- coding: utf-8 -*-
"""Tutorium 7, Abb. 1: Bodensäule mit z nach unten; die Oberflächentemperatur schwankt periodisch.
In den Tiefen z_1 und z_2 stehen nur leere Zeitachsen mit Fragezeichen, damit die Skizze die
Antwort auf die Vorab-Frage (Dämpfung und Verzögerung) nicht vorwegnimmt (Vorgabe der Koordination).
Aufruf: python3 abb_t7_boden.py   (schreibt ../grafik/t7_boden.png und .svg)"""
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from skizze_stil import *  # noqa: E402,F401,F403

fig, ax = leinwand(7.2, 3.7, xlim=(0, 14.4), ylim=(0, 7.4))

# ---------------- Bodensäule ----------------
bx0, bx1 = 1.2, 3.6
y_O, y_U = 6.3, 0.35
schicht(ax, bx0, y_U, bx1 - bx0, y_O - y_U, BODEN, rand="none")
ax.plot([bx0, bx0], [y_O, y_U], color=LINIE, lw=1.1)
ax.plot([bx1, bx1], [y_O, y_U], color=LINIE, lw=1.1)
ax.plot([bx0, bx1], [y_O, y_O], color=LINIE, lw=1.4)
# nach unten offen (halbunendlich): Wellenlinie als Abbruch
xs = np.linspace(bx0, bx1, 60)
ax.plot(xs, y_U + 0.06 * np.sin((xs - bx0) * 9), color=LINIE, lw=1.0)
for xg in np.arange(bx0 + 0.1, bx1 - 0.05, 0.28):
    ax.plot([xg, xg + 0.07], [y_O, y_O + 0.13], color="#6B8E4E", lw=0.9)
text(ax, (bx0 + bx1) / 2, y_O + 0.55, "Oberfläche", fs=9.5)
text(ax, (bx0 + bx1) / 2, 1.05, r"Boden: $a$", fs=9.5)

# z-Achse
pfeil(ax, (0.7, y_O), (0.7, y_U + 0.1), farbe=LINIE, breite=1.1, groesse=10)
ax.plot([0.6, 0.8], [y_O, y_O], color=LINIE, lw=1.0)
text(ax, 0.48, y_O, "0", fs=9.5, ha="right")
text(ax, 0.48, y_U + 0.25, r"$z$", fs=10.5, ha="right")

# Messstellen in z_1 und z_2
tiefen = [(y_O, None), (4.15, r"$z_1$"), (2.15, r"$z_2$")]
for y, lab in tiefen[1:]:
    ax.plot([0.6, 0.8], [y, y], color=LINIE, lw=1.0)
    text(ax, 0.48, y, lab, fs=10, ha="right")
    ax.add_patch(Circle((bx1 - 0.35, y), 0.09, facecolor=LINIE, edgecolor=LINIE, zorder=5))

# ---------------- Temperaturverläufe über der Zeit ----------------
px0, px1 = 4.9, 13.9          # Zeitachse
amp0 = 0.62                   # Amplitude an der Oberfläche (Zeichnungseinheiten)
perioden = 1.6
labels = [r"$T(0,t)$", r"$T(z_1,t)$", r"$T(z_2,t)$"]
for (y, _), lab in zip(tiefen, labels):
    # Verbindung von der Messstelle zum Diagramm
    if y != y_O:
        ax.plot([bx1 - 0.25, px0 - 0.15], [y, y], color=GRAU, lw=0.7, ls=(0, (3, 3)))
    else:
        ax.plot([bx1 + 0.05, px0 - 0.15], [y, y], color=GRAU, lw=0.7, ls=(0, (3, 3)))
    # Achsen
    pfeil(ax, (px0, y), (px1 + 0.25, y), farbe=GRAU, breite=0.9, groesse=8)
    ax.plot([px0, px0], [y - 0.75, y + 0.75], color=GRAU, lw=0.9)
    text(ax, px1 + 0.3, y - 0.22, r"$t$", fs=10, ha="left", farbe=GRAU)
    text(ax, px0 + 0.08, y + 0.92, lab, fs=9.5, ha="left")
    if y == y_O:
        # Welle an der Oberfläche (Mittelwert T_m liegt auf der Zeitachse)
        t = np.linspace(0, perioden * 2 * math.pi, 400)
        xw = px0 + 0.2 + (px1 - px0 - 0.5) * t / t[-1]
        ax.plot(xw, y + amp0 * np.cos(t), color=WAERME, lw=1.6, zorder=4)
    else:
        # in der Tiefe: leere Zeitachse, der Verlauf ist gesucht
        text(ax, (px0 + px1) / 2, y + 0.38, "?", fs=15, farbe=LINIE)

# Beschriftung der oberen Welle: T_m, Amplitude, Periodendauer
y0 = tiefen[0][0]
text(ax, px0 - 0.1, y0 + 0.02, r"$T_m$", fs=9.5, ha="right", va="bottom", farbe=GRAU)
x_max2 = px0 + 0.2 + (px1 - px0 - 0.5) * (2 * math.pi) / (perioden * 2 * math.pi)
masslinie(ax, (x_max2, y0), (x_max2, y0 + amp0), "")
text(ax, x_max2 + 0.12, y0 + 0.17, r"$\Delta T_0$", fs=9.5, ha="left", farbe=GRAU)
x_min1 = px0 + 0.2 + (px1 - px0 - 0.5) * math.pi / (perioden * 2 * math.pi)
x_min2 = px0 + 0.2 + (px1 - px0 - 0.5) * 3 * math.pi / (perioden * 2 * math.pi)
pfeil(ax, (x_min1, y0 - amp0 - 0.12), (x_min2, y0 - amp0 - 0.12), farbe=GRAU, breite=0.8, groesse=7, stil="<|-|>")
text(ax, (x_min1 + x_min2) / 2, y0 - amp0 - 0.32, r"$2\pi/\omega$", fs=9.5, farbe=GRAU)

print(speichern(fig, "t7_boden"))
