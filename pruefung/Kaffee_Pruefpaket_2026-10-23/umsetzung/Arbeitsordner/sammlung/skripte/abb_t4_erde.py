# -*- coding: utf-8 -*-
"""Tutorium 4, Abb. 1: Die Erde im Sonnenlicht. Einstrahlung auf den Querschnitt pi R^2, Abstrahlung über die
Oberfläche 4 pi R^2, dünne Atmosphärenschicht. Keine Lösung (kein S0/4, keine Bilanzgleichung).
Aufruf: python3 abb_t4_erde.py   (schreibt ../grafik/t4_erde.png und .svg)"""
import sys, os, math
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from skizze_stil import *

fig, ax = leinwand(7.2, 3.8, xlim=(0, 14.4), ylim=(0, 7.6))

cx, cy, R, R_atm = 8.0, 3.7, 2.15, 2.55
SONNE_TEXT = "#8A6A00"

# Strahlenbündel, das die Erde trifft: Querschnitt pi R^2 (gestrichelte Scheibe bei x_q)
x_q = 4.3
for s in (+1, -1):
    ax.plot([x_q, cx], [cy + s * R, cy + s * R], color=HELLGRAU, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
ax.add_patch(Ellipse((x_q, cy), 0.6, 2 * R, fill=False, edgecolor=GRAU, linewidth=1.1, linestyle=(0, (4, 3)), zorder=4))
text(ax, x_q, cy - R - 0.45, r"Querschnitt $\pi R^2$", fs=10.5, farbe=GRAU)

# Erde und Atmosphärenschicht
ax.add_patch(Circle((cx, cy), R_atm, facecolor="#E6EFF8", edgecolor="#8FA9C4", linewidth=1.0, zorder=2))
ax.add_patch(Circle((cx, cy), R, facecolor=MEER, edgecolor=LINIE, linewidth=1.2, zorder=3))
text(ax, cx + 0.55, cy, r"Erde: $T_\mathrm{O}$", fs=11)

# Sonnenstrahlen (parallel, bis zur Oberfläche, die Schicht ist für Sonnenlicht durchlässig)
for dy in (-1.7, -0.85, 0.0, 0.85, 1.7):
    x_end = cx - math.sqrt(R**2 - dy**2) - 0.05
    pfeil(ax, (0.3, cy + dy), (x_end, cy + dy), farbe=SONNE, breite=1.6, groesse=11, z=5)
text(ax, 0.3, cy + R + 0.3, r"Sonnenstrahlung: $S_0$", fs=10.5, farbe=SONNE_TEXT, ha="left")

# Reflexion (planetare Albedo)
x_r = cx - math.sqrt(R_atm**2 - 1.7**2)
pfeil(ax, (x_r, cy + 1.75), (x_r - 1.0, cy + 2.85), farbe=SONNE, breite=1.4, groesse=10, z=5)
text(ax, x_r - 1.05, cy + 3.05, r"reflektiert: $\rho_\mathrm{p}$", fs=10, farbe=SONNE_TEXT, ha="right")


# Wärmestrahlung nach allen Seiten (gewellte rote Pfeile)
def wellenpfeil(winkel, r1=R_atm + 0.1, r2=R_atm + 1.25, amp=0.09, wl=0.38):
    w = math.radians(winkel)
    ux, uy = math.cos(w), math.sin(w)
    nx, ny = -uy, ux
    t = np.linspace(0, (r2 - r1) - 0.3, 200)
    x = cx + (r1 + t) * ux + amp * np.sin(2 * np.pi * t / wl) * nx
    y = cy + (r1 + t) * uy + amp * np.sin(2 * np.pi * t / wl) * ny
    ax.plot(x, y, color=WAERME, linewidth=1.4, zorder=5)
    pfeil(ax, (x[-1], y[-1]), (cx + r2 * ux, cy + r2 * uy), farbe=WAERME, breite=1.4, groesse=10)


for winkel in (110, 70, 30, -10, -50, -90):
    wellenpfeil(winkel)
text(ax, 10.35, 7.25, r"Wärmestrahlung über $4\pi R^2$", fs=10.5, farbe=WAERME, ha="left")

# Atmosphärenschicht beschriften
w = math.radians(10)
xp, yp = cx + (R + R_atm) / 2 * math.cos(w), cy + (R + R_atm) / 2 * math.sin(w)
ax.plot([xp, 11.05], [yp, 4.3], color=GRAU, linewidth=0.8, zorder=6)
ax.add_patch(Circle((xp, yp), 0.05, color=GRAU, zorder=6))
text(ax, 11.15, 4.55, "Atmosphärenschicht:", fs=10.5, ha="left")
text(ax, 11.15, 4.0, r"$T_\mathrm{A}$, $\varepsilon_\mathrm{A}$", fs=10.5, ha="left")
text(ax, 14.3, 0.3, r"Weltall: $T \approx 0\,\mathrm{K}$", fs=10, farbe=GRAU, ha="right")
text(ax, 0.3, 0.3, "nicht maßstäblich", fs=8.5, farbe=GRAU, ha="left")
text(ax, 14.3, 7.6 - 0.05, "", fs=1)

print(speichern(fig, "t4_erde"))
