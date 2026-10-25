# -*- coding: utf-8 -*-
"""Abb. 2 in Tutorium 8: Schnitt vom Äquator zum Nordpol (schematisch, nicht maßstäblich).
Warme, feuchte Luft nach Norden, kalte, trockene Luft zurück, Umwälzung im Ozean, Wasserdampf als
Träger latenter Wärme; Passat und Jetstream wehen quer zur Bildebene. Ohne Wolken und Regen, denn
wo die latente Wärme frei wird, fragt Teil c. Aufruf: python3 abb_t8_pol.py"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from skizze_stil import *

fig, ax = leinwand(7.6, 3.75, xlim=(0, 15.2), ylim=(-0.4, 7.1))

x0, x1 = 1.2, 13.6                       # Äquator, Nordpol


def xb(phi):
    return x0 + phi / 90 * (x1 - x0)


yO0, yO1, yA1 = 0.85, 2.15, 5.75         # Meeresboden (schematisch), Meeresoberfläche, Oberrand (10 km)
xw = xb(40)

# Ozean und Atmosphäre
schicht(ax, x0, yO0, x1 - x0, yO1 - yO0, MEER, rand="none")
schicht(ax, x0, yO1, x1 - x0, yA1 - yO1, LUFT, rand="none")
ax.plot([x0, x1], [yO1, yO1], color=LINIE, linewidth=1.0, zorder=2)
ax.plot([x0, x1], [yO0, yO0], color=LINIE, linewidth=1.0, zorder=2)
ax.plot([x0, x1], [yA1, yA1], color=GRAU, linewidth=0.8, linestyle=(0, (5, 3)), zorder=2)
text(ax, 0.75, (yO1 + yA1) / 2, "Atmosphäre", fs=10, farbe=GRAU, rotation=90)
text(ax, 0.75, (yO0 + yO1) / 2, "Ozean", fs=10, farbe="#2B5A85", rotation=90)
pfeil(ax, (14.0, yO1), (14.0, yA1), farbe=GRAU, breite=0.9, groesse=8, stil="<|-|>")
text(ax, 14.3, (yO1 + yA1) / 2, r"$H = 10\,\mathrm{km}$", fs=9.5, farbe=GRAU, rotation=90)

# Breitenkreis 40° N als senkrechte „Wand“
ax.plot([xw, xw], [yO1, yA1], color=LINIE, linewidth=1.1, linestyle=(0, (4, 3)), zorder=4)

# Luft: warm und feucht nach Norden (oben), kalt und trocken zurück (unten)
y_w, y_k = 4.7, 3.1
stroemungspfeil(ax, (1.9, y_w), (12.4, y_w), farbe=WARM)
stroemungspfeil(ax, (12.4, y_k), (1.9, y_k), farbe=KALT)
text(ax, 1.95, y_w + 0.45, r"warm und feucht: $\vartheta + \Delta T$, $x + \Delta x$", fs=9.5, farbe=WARM, ha="left")
text(ax, 12.35, y_k - 0.42, r"kalt und trocken: $\vartheta$, $x$", fs=9.5, farbe=KALT, ha="right")
text(ax, xw + 0.15, y_w - 0.36, r"$\dot{m}_{\mathrm{L}}$", fs=10, ha="left")
text(ax, xw + 0.15, y_k + 0.36, r"$\dot{m}_{\mathrm{L}}$", fs=10, ha="left")
# Wasserdampf in der warmen Luft
random.seed(4)
for i in range(30):
    xp = 2.2 + i * 0.34 + random.uniform(-0.08, 0.08)
    yp = y_w + random.choice((-1, 1)) * random.uniform(0.12, 0.22)
    if abs(xp - xw) < 0.3 or (yp < y_w and 6.8 < xp < 7.4):
        continue
    ax.add_patch(Circle((xp, yp), 0.045, facecolor="#7FA7CF", edgecolor="none", zorder=3))
text(ax, 1.95, y_w - 0.48, "Wasserdampf", fs=9, farbe="#4F7FAF", ha="left")

# Wärmestrom der Atmosphäre über den Breitenkreis
waermepfeil(ax, (xw - 0.95, 6.2), (xw + 0.95, 6.2))
text(ax, xw, 6.62, r"$\dot{Q}_{\mathrm{A}}$", fs=10.5, farbe=WAERME)


# Passat (nach Westen, in die Bildebene) und Jetstream (nach Osten, aus der Bildebene)
def quer(x, y, aus_ebene, beschriftung):
    ax.add_patch(Circle((x, y), 0.19, facecolor="white", edgecolor=LINIE, linewidth=1.0, zorder=5))
    if aus_ebene:
        ax.add_patch(Circle((x, y), 0.05, facecolor=LINIE, edgecolor="none", zorder=6))
    else:
        d = 0.13
        ax.plot([x - d, x + d], [y - d, y + d], color=LINIE, linewidth=1.0, zorder=6)
        ax.plot([x - d, x + d], [y + d, y - d], color=LINIE, linewidth=1.0, zorder=6)
    text(ax, x + 0.3, y, beschriftung, fs=9, ha="left")


quer(xb(12), 2.55, False, "Passat (nach Westen)")
quer(xw + 0.75, 5.35, True, "Jetstream (nach Osten)")

# Ozean: warmes Oberflächenwasser nach Norden, kaltes Tiefenwasser zurück
stroemungspfeil(ax, (1.9, 1.82), (11.4, 1.82), farbe=WARM)
stroemungspfeil(ax, (11.4, 1.18), (1.9, 1.18), farbe=KALT)
text(ax, 6.65, 1.5, r"Umwälzung im Atlantik (AMOC), $\dot{V}_{\mathrm{AMOC}}$", fs=9, farbe="#1F3F66")

# Breitenangaben
for phi, name in ((0, "Äquator"), (40, "40° N"), (90, "Nordpol")):
    ax.plot([xb(phi), xb(phi)], [yO0 - 0.12, yO0], color=LINIE, linewidth=1.0)
    text(ax, xb(phi), yO0 - 0.4, name, fs=10)
text(ax, xb(16), 6.55, "Tropen: Strahlungsüberschuss", fs=9.5, farbe=GRAU)
text(ax, xb(73), 6.55, "Polargebiet: Strahlungsdefizit", fs=9.5, farbe=GRAU)
text(ax, x1, -0.3, "schematisch, nicht maßstäblich", fs=9, farbe=GRAU, ha="right", va="bottom")

speichern(fig, "t8_pol")
print("ok")
