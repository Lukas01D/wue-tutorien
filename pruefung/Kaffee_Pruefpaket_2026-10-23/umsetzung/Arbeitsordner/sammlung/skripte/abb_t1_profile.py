# -*- coding: utf-8 -*-
"""Tutorium 1, Abb. 2 (Frage 3): angeblich stationäre Temperaturprofile in drei Wänden aus zwei Schichten.
Logik wie pilot_t1_grafiken.py (Pilotblatt Tutorium 1), Funktion profile_lesen (A: Schicht 1 steil,
B: Schicht 1 flach, C: Maximum an der Grenzfläche); Gestaltung im gemeinsamen Stil (skizze_stil.py).
Aufruf: python3 abb_t1_profile.py  (schreibt ../grafik/t1_profile.png und .svg)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from skizze_stil import *

SCHICHT1 = FIRN
SCHICHT2 = "#EFE3CB"

fig, ax = leinwand(7.0, 2.45, xlim=(0, 16), ylim=(0, 5.6))

faelle = {
    "A": [(0.0, 0.92), (0.5, 0.42), (1.0, 0.22)],   # Schicht 1 steil, Schicht 2 flach
    "B": [(0.0, 0.92), (0.5, 0.80), (1.0, 0.22)],   # Schicht 1 flach, Schicht 2 steil
    "C": [(0.0, 0.55), (0.5, 0.88), (1.0, 0.25)],   # Maximum an der Grenzfläche
}
breite, hoehe = 3.9, 3.3
x0s = [0.9, 6.15, 11.4]
y0 = 1.1
for (name, pkt), x0 in zip(faelle.items(), x0s):
    ax.add_patch(Rectangle((x0, y0), breite / 2, hoehe, facecolor=SCHICHT1, edgecolor=GRAU, lw=0.8, zorder=1))
    ax.add_patch(Rectangle((x0 + breite / 2, y0), breite / 2, hoehe, facecolor=SCHICHT2, edgecolor=GRAU, lw=0.8, zorder=1))
    text(ax, x0 + breite / 4, y0 - 0.36, "Schicht 1", fs=10.5, farbe=GRAU)
    text(ax, x0 + 3 * breite / 4, y0 - 0.36, "Schicht 2", fs=10.5, farbe=GRAU)
    # Achsen
    pfeil(ax, (x0 - 0.35, y0), (x0 - 0.35, y0 + hoehe + 0.4), farbe=LINIE, breite=0.9, groesse=8)
    text(ax, x0 - 0.35, y0 + hoehe + 0.62, r"$T$", fs=12)
    pfeil(ax, (x0, y0 - 0.7), (x0 + breite + 0.4, y0 - 0.7), farbe=LINIE, breite=0.9, groesse=8)
    text(ax, x0 + breite + 0.6, y0 - 0.7, r"$x$", fs=12)
    # Profil
    xs = [x0 + p[0] * breite for p in pkt]
    ys = [y0 + p[1] * hoehe for p in pkt]
    ax.plot(xs, ys, color=LINIE, lw=2.0, solid_capstyle="round", solid_joinstyle="round", zorder=3)
    text(ax, x0 + breite / 2, y0 + hoehe + 0.45, name, fs=13, fontweight="bold")

print(speichern(fig, "t1_profile"))
