# -*- coding: utf-8 -*-
"""Tutorium 1, Abb. 3: Schnitt durch die Kühlhauswand (außen Stahlbeton, innen Hartschaum aus Polyurethan)
mit den beiden Oberflächentemperaturen. Kein Temperaturverlauf (den skizzieren die Studierenden in Teil a).
Aufruf: python3 abb_t1_kuehlhaus.py  (schreibt ../grafik/t1_kuehlhaus.png und .svg)"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from skizze_stil import *

fig, ax = leinwand(7.0, 3.0, xlim=(0, 14), ylim=(0, 6.0))

xa, xg, xi = 4.7, 7.2, 8.7   # äußere Oberfläche, Grenzfläche, innere Oberfläche (20 cm : 12 cm)
yu, yo = 1.1, 5.0

# Schichten
ax.add_patch(Rectangle((xa, yu), xg - xa, yo - yu, facecolor=BETON, edgecolor="none", zorder=1))
ax.add_patch(Rectangle((xa, yu), xg - xa, yo - yu, fill=False, hatch="//", edgecolor="#9C9C9C", linewidth=0, zorder=1))
ax.add_patch(Rectangle((xg, yu), xi - xg, yo - yu, facecolor=DAEMMUNG, edgecolor="none", zorder=1))
ax.add_patch(Rectangle((xg, yu), xi - xg, yo - yu, fill=False, hatch="xx", edgecolor="#D9B640", linewidth=0, zorder=1))
for x in (xa, xg, xi):
    ax.plot([x, x], [yu, yo], color=LINIE, lw=1.2 if x != xg else 0.9, zorder=3)
for y in (yu, yo):            # Wand oben und unten abgeschnitten
    ax.plot([xa, xi], [y, y], color=GRAU, lw=0.8, ls=(0, (3, 3)), zorder=2)

kasten = dict(boxstyle="square,pad=0.15", edgecolor="none")
text(ax, (xa + xg) / 2, 5.38, "Stahlbeton", fs=10)
text(ax, (xa + xg) / 2, 4.0, r"$\lambda_\mathrm{B}$", fs=11, bbox=dict(kasten, facecolor=BETON), zorder=4)
text(ax, (xg + xi) / 2 + 0.12, 5.38, "Dämmung", fs=10)
text(ax, (xg + xi) / 2, 4.0, r"$\lambda_\mathrm{D}$", fs=11, bbox=dict(kasten, facecolor=DAEMMUNG), zorder=4)

# außen: Sommer, Sonne
text(ax, 2.6, 5.38, "außen", fs=10.5, farbe=GRAU)
cx, cy, r = 1.0, 4.45, 0.38
ax.add_patch(Circle((cx, cy), r, facecolor=SONNE, edgecolor="#C99A00", lw=0.8, zorder=2))
for k in range(8):
    phi = k * math.pi / 4
    ax.plot([cx + 1.45 * r * math.cos(phi), cx + 2.0 * r * math.cos(phi)],
            [cy + 1.45 * r * math.sin(phi), cy + 2.0 * r * math.sin(phi)], color="#C99A00", lw=1.0)
# innen: Kühlraum
text(ax, 11.5, 5.38, "innen: Kühlraum", fs=10.5, farbe=GRAU)

# Oberflächentemperaturen
for x, s, ha, dx in ((xa, r"$\vartheta_\mathrm{a}$", "right", -0.18), (xi, r"$\vartheta_\mathrm{i}$", "left", 0.18)):
    ax.plot([x], [3.0], "o", ms=4.5, color=LINIE, zorder=5)
    text(ax, x + dx, 3.0, s, fs=11, ha=ha)

# Wärmestrom von außen nach innen
waermepfeil(ax, (2.2, 1.9), (11.6, 1.9))
text(ax, 2.35, 2.25, r"$\dot{q}$", fs=11, farbe=WAERME, ha="left")

# Maße
def mass_waagerecht(x1, x2, y, s):
    pfeil(ax, (x1, y), (x2, y), farbe=GRAU, breite=0.9, groesse=8, stil="<|-|>")
    text(ax, (x1 + x2) / 2, y - 0.32, s, fs=10, farbe=GRAU)

for x in (xa, xg, xi):
    ax.plot([x, x], [yu, 0.45], color=HELLGRAU, lw=0.7, zorder=0)
mass_waagerecht(xa, xg, 0.62, r"$s_\mathrm{B}$")
mass_waagerecht(xg, xi, 0.62, r"$s_\mathrm{D}$")

print(speichern(fig, "t1_kuehlhaus"))
