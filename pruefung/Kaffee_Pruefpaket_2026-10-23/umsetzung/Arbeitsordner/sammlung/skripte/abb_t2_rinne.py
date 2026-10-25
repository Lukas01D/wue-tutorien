# -*- coding: utf-8 -*-
"""Tutorium 2, Abb. 1: offene Rinne im Meereis von der Seite. Wind mit w über Eis und Rinne, Luft mit theta_u,
Wasseroberfläche mit theta_W, Breite b der Rinne in Windrichtung, angedeuteter Seerauch, Wärmestrom nach oben.
Keine Grenzschichten (die zeichnen die Studierenden in Teil a ein).
Aufruf: python3 abb_t2_rinne.py  (schreibt ../grafik/t2_rinne.png und .svg)"""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from skizze_stil import *

fig, ax = leinwand(7.0, 3.3, xlim=(0, 14), ylim=(0.1, 6.7))

y_w = 2.3                    # Wasserspiegel
x_l, x_r = 4.7, 9.3          # Eiskanten (luvseitig links, leeseitig rechts)
y_eu, y_eo = 1.5, 2.6        # Unter- und Oberkante der Schollen

# Meer und Eisschollen
ax.add_patch(Rectangle((0, 0.3), 14, y_w - 0.3, facecolor=MEER, edgecolor="none", zorder=1))
ax.plot([x_l, x_r], [y_w, y_w], color=LINIE, lw=1.1, zorder=3)
for xa_, xb_ in ((0.0, x_l), (x_r, 14.0)):
    ax.add_patch(Rectangle((xa_, y_eu), xb_ - xa_, y_eo - y_eu, facecolor=EIS, edgecolor=LINIE, lw=1.1, zorder=2))
text(ax, 2.35, (y_eu + y_eo) / 2, "Meereis", fs=10)
text(ax, 11.65, (y_eu + y_eo) / 2, "Meereis", fs=10)
text(ax, 2.35, 0.75, "Meerwasser", fs=10, farbe="#24476B")
text(ax, (x_l + x_r) / 2, 1.95, r"Wasser, $\vartheta_\mathrm{W}$", fs=10, farbe="#24476B")

# Eiskante (luvseitig)
ax.annotate("Eiskante", xy=(x_l, y_eo), xytext=(3.45, 3.25), fontsize=9.5, color=GRAU, ha="center", va="center",
            arrowprops=dict(arrowstyle="-", color=GRAU, lw=0.8, shrinkA=2, shrinkB=1))

# Breite b in Windrichtung (unter der Rinne)
for x in (x_l, x_r):
    ax.plot([x, x], [y_eu, 0.95], color=GRAU, lw=0.7, zorder=3)
pfeil(ax, (x_l, 1.12), (x_r, 1.12), farbe=GRAU, breite=0.9, groesse=8, stil="<|-|>", z=4)
text(ax, (x_l + x_r) / 2, 0.78, r"$b$", fs=11, farbe=LINIE)

# Wind (Anströmung von links, gleichförmig)
for y in (3.9, 4.6, 5.3):
    stroemungspfeil(ax, (0.4, y), (2.4, y))
text(ax, 1.4, 5.85, r"Wind, $w$", fs=10.5, farbe=KALT)
text(ax, 11.9, 5.35, r"Luft, $\vartheta_\mathrm{u}$", fs=10.5)
text(ax, 13.95, 6.45, "nicht maßstäblich", fs=8.5, farbe=GRAU, ha="right")

# Seerauch: aufsteigende, mit dem Wind abtreibende Schwaden
rng = np.linspace(0, 1, 120)
for x_start, hoehe, phase in ((5.9, 1.5, 0.0), (6.8, 1.9, 1.2), (7.7, 1.6, 2.1), (8.5, 1.3, 0.7)):
    xs = x_start + 1.4 * rng**1.6 + 0.12 * np.sin(6 * np.pi * rng + phase)
    ys = y_w + 0.12 + hoehe * rng
    ax.plot(xs, ys, color="#A8B3BD", lw=1.6, alpha=0.85, solid_capstyle="round", zorder=2)
text(ax, 9.7, 4.25, "Seerauch", fs=9.5, farbe=GRAU, ha="left")

# Wärmestrom vom Wasser an die Luft
waermepfeil(ax, (5.25, y_w + 0.1), (5.25, 3.55))
text(ax, 5.05, 3.25, r"$\dot{q}$", fs=11, farbe=WAERME, ha="right")

print(speichern(fig, "t2_rinne"))
