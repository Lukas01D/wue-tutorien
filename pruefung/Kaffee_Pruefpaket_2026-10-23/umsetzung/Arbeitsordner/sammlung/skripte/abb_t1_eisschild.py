# -*- coding: utf-8 -*-
"""Tutorium 1, Abb. 1: Querschnitt durch den Eisschild (Firn oben, Eis, Gestein unten), z nach unten,
Dicke H, Oberflächentemperatur, Wärmestromdichte aus dem Erdinneren. Keine Lösung (kein Temperaturprofil).
Aufruf: python3 abb_t1_eisschild.py  (schreibt ../grafik/t1_eisschild.png und .svg)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from skizze_stil import *

fig, ax = leinwand(7.0, 3.55, xlim=(0, 14), ylim=(0.2, 7.3))

x0, x1 = 2.0, 11.0           # Breite des gezeichneten Ausschnitts
y_O, y_F, y_B, y_G = 6.0, 5.2, 1.75, 0.55   # Oberfläche, Grenze Firn/Eis, Basis, Unterkante Gestein

# Schichten (Schraffur getrennt, damit die Punkte hell bleiben)
ax.add_patch(Rectangle((x0, y_F), x1 - x0, y_O - y_F, facecolor=FIRN, edgecolor="none", zorder=1))
ax.add_patch(Rectangle((x0, y_F), x1 - x0, y_O - y_F, fill=False, hatch="...", edgecolor="#9FB3C4", linewidth=0, zorder=1))
ax.add_patch(Rectangle((x0, y_B), x1 - x0, y_F - y_B, facecolor=EIS, edgecolor="none", zorder=1))
ax.add_patch(Rectangle((x0, y_G), x1 - x0, y_B - y_G, facecolor=GESTEIN, edgecolor="none", zorder=1))
ax.add_patch(Rectangle((x0, y_G), x1 - x0, y_B - y_G, fill=False, hatch="//", edgecolor="#8A8073", linewidth=0, zorder=1))
for y in (y_O, y_F, y_B):
    ax.plot([x0, x1], [y, y], color=LINIE, lw=1.2 if y != y_F else 0.8, zorder=3)
for x in (x0, x1):           # seitliche Ränder gestrichelt: der Eisschild geht weiter
    ax.plot([x, x], [y_G, y_O], color=GRAU, lw=0.8, ls=(0, (3, 3)), zorder=2)

# Beschriftung der Schichten
text(ax, 6.5, (y_O + y_F) / 2, r"Firn, $\lambda_\mathrm{F}$", fs=10,
     bbox=dict(boxstyle="square,pad=0.15", facecolor=FIRN, edgecolor="none"), zorder=4)
text(ax, 6.5, 3.75, r"Eis, $\lambda(T)$", fs=11)
text(ax, 5.05, (y_B + y_G) / 2, "Gestein", fs=10, farbe="#2B2620",
     bbox=dict(boxstyle="square,pad=0.15", facecolor=GESTEIN, edgecolor="none"), zorder=4)
text(ax, x0 + 0.12, y_B + 0.22, "Basis", fs=9, farbe=GRAU, ha="left")

# Oberfläche mit Temperatur
text(ax, 6.5, y_O + 0.45, r"Oberfläche, Jahresmittel $\vartheta_\mathrm{O}$", fs=10)
text(ax, 13.9, 7.1, "nicht maßstäblich", fs=8.5, farbe=GRAU, ha="right")

# Koordinate z nach unten
xz = 1.1
pfeil(ax, (xz, y_O), (xz, y_B - 0.75), farbe=LINIE, breite=1.1, groesse=10)
ax.plot([xz - 0.12, xz + 0.12], [y_O, y_O], color=LINIE, lw=1.1)
ax.plot([xz - 0.12, xz + 0.12], [y_B, y_B], color=LINIE, lw=1.1)
text(ax, xz - 0.2, y_O, r"$z = 0$", fs=9.5, ha="right")
text(ax, xz - 0.2, y_B, r"$z = H$", fs=9.5, ha="right")
text(ax, xz + 0.25, y_B - 0.7, r"$z$", fs=11, ha="left")
ax.plot([xz + 0.12, x0], [y_O, y_O], color=HELLGRAU, lw=0.7, ls=(0, (2, 2)))
ax.plot([xz + 0.12, x0], [y_B, y_B], color=HELLGRAU, lw=0.7, ls=(0, (2, 2)))

# Maße rechts: Firndicke und Eisdicke
def mass_senkrecht(x, y1, y2, s):
    pfeil(ax, (x, y1), (x, y2), farbe=GRAU, breite=0.9, groesse=8, stil="<|-|>")
    text(ax, x + 0.15, (y1 + y2) / 2, s, fs=10, farbe=GRAU, ha="left")

ax.plot([x1, 12.75], [y_O, y_O], color=HELLGRAU, lw=0.7)
ax.plot([x1, 11.85], [y_F, y_F], color=HELLGRAU, lw=0.7)
ax.plot([x1, 12.75], [y_B, y_B], color=HELLGRAU, lw=0.7)
mass_senkrecht(11.65, y_O, y_F, r"$s_\mathrm{F}$")
mass_senkrecht(12.55, y_O, y_B, r"$H$")

# Wärmestromdichte aus dem Erdinneren (von unten in die Basis)
for xa in (3.6, 6.5, 9.4):
    pfeil(ax, (xa, y_G + 0.2), (xa, y_B + 0.75), farbe=WAERME, breite=1.5, groesse=12)
text(ax, 11.2, (y_B + y_G) / 2 - 0.05, "$\\dot{q}_\\mathrm{E}$ aus dem\nErdinneren", fs=10, farbe=WAERME, ha="left",
     linespacing=1.15)

print(speichern(fig, "t1_eisschild"))
