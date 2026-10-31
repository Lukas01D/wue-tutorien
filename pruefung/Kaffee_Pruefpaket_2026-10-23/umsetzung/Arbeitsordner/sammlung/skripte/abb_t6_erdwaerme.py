# -*- coding: utf-8 -*-
"""Tutorium 6, Abb. 1: links die Erdkruste mit z nach unten und dem Element dz (Aufgabe 1),
rechts die Erde als Kugel (Aufgabe 2, die Kugelschale dr zeichnen die Studierenden selbst ein).
Aufruf: python3 abb_t6_erdwaerme.py   (schreibt ../grafik/t6_erdwaerme.png und .svg)"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from skizze_stil import *  # noqa: E402,F401,F403

fig, ax = leinwand(7.4, 3.9, xlim=(0, 14.8), ylim=(0, 7.8))

MANTEL = "#C98E6B"
KRUSTE = "#D9CBB5"
ELEMENT = "#F4EEE4"

# ---------------- links: Erdkruste ----------------
x0, x1 = 1.5, 7.0            # Breite des Krustenblocks
y_O, y_M, y_U = 6.2, 1.5, 0.7  # Oberfläche, Krustenbasis, Unterkante Mantel
km = (y_O - y_M) / 30.0      # Maßstab: 30 km Kruste

text(ax, 0.0, 7.45, "Erdkruste (Aufgabe 1)", fs=10.5, ha="left", fontweight="bold")
# Luft und Oberfläche
schicht(ax, x0, y_O, x1 - x0, 0.45, LUFT, rand="none")
ax.plot([x0, x1], [y_O, y_O], color=LINIE, lw=1.4, zorder=3)
for xg in [x0 + 0.15 + 0.32 * i for i in range(int((x1 - x0) / 0.32))]:
    ax.plot([xg, xg + 0.08], [y_O, y_O + 0.12], color="#6B8E4E", lw=0.9, zorder=3)
text(ax, x0 + 0.05, y_O + 0.62, r"Oberfläche: $\vartheta_\mathrm{O}$", fs=9.5, ha="left")
# Kruste und Mantel
schicht(ax, x0, y_M, x1 - x0, y_O - y_M, KRUSTE)
schicht(ax, x0, y_U, x1 - x0, y_M - y_U, MANTEL)
text(ax, x0 + 0.25, y_U + 0.38, "Erdmantel", fs=9.5, ha="left")
text(ax, x0 + 1.55, y_O - 0.55, r"Kruste: $\lambda$, $\dot{q}_{\mathrm{KV}}$", fs=9.5, ha="left")
# Wärmestromdichte an der Oberfläche (nach oben, aus der Erde heraus)
waermepfeil(ax, (6.3, y_O + 0.05), (6.3, y_O + 0.85), r"$\dot{q}_\mathrm{O}$", versatz=(0.12, 0.05))
# Wärmestromdichte aus dem Mantel (gesucht)
waermepfeil(ax, (5.0, y_U + 0.2), (5.0, y_M + 0.65), None)
text(ax, 5.12, y_M + 0.35, r"$\dot{q}_\mathrm{M}$ = ?", fs=10, farbe=WAERME, ha="left")

# z-Achse nach unten
pfeil(ax, (0.85, y_O), (0.85, y_U + 0.1), farbe=LINIE, breite=1.1, groesse=10)
ax.plot([0.75, 0.95], [y_O, y_O], color=LINIE, lw=1.0)
text(ax, 0.62, y_O, "0", fs=9.5, ha="right")
text(ax, 0.62, y_U + 0.2, r"$z$", fs=10.5, ha="right")
# Krustendicke s
masslinie(ax, (7.35, y_O), (7.35, y_M), r"$s$", versatz=(0.12, 0.0))

# Tiefbohrung bis z_B
y_B = y_O - 9.1 * km
ax.plot([2.05, 2.05], [y_O, y_B], color=LINIE, lw=1.6, zorder=4)
ax.plot([1.97, 2.13], [y_B, y_B], color=LINIE, lw=1.2, zorder=4)
text(ax, 2.2, y_B - 0.02, r"Tiefbohrung: $z_\mathrm{B}$, $\vartheta_\mathrm{B}$", fs=9, ha="left", va="center")

# Element dz in der Tiefe z (dick gezeichnet)
y_z, h_dz = 3.85, 0.62
ex0, ex1 = 3.3, 6.0
ax.add_patch(Rectangle((ex0, y_z - h_dz), ex1 - ex0, h_dz, facecolor=ELEMENT, edgecolor=LINIE,
                       linewidth=1.1, zorder=4))
for y in (y_z, y_z - h_dz):
    ax.plot([0.95, ex0], [y, y], color=GRAU, lw=0.7, ls=(0, (3, 3)), zorder=2)
text(ax, ex0 - 0.08, y_z + 0.02, r"$z$", fs=9.5, ha="right", va="bottom")
text(ax, ex0 - 0.08, y_z - h_dz - 0.02, r"$z + dz$", fs=9.5, ha="right", va="top")
text(ax, (ex0 + ex1) / 2 - 0.45, y_z - h_dz / 2, r"$\dot{q}_{\mathrm{KV}}\,A\,dz$", fs=9.5, farbe=WAERME, zorder=6)
text(ax, ex1 + 0.12, y_z - h_dz / 2, r"$A$", fs=9.5, ha="left")
# Wärmeströme am Element in z-Richtung (Bilanzschreibweise: hinein bei z, hinaus bei z + dz)
waermepfeil(ax, (5.25, y_z + 0.75), (5.25, y_z + 0.02), r"$\dot{Q}_z$", versatz=(0.12, 0.05))
waermepfeil(ax, (5.25, y_z - h_dz - 0.02), (5.25, y_z - h_dz - 0.75), r"$\dot{Q}_{z+dz}$", versatz=(0.12, -0.05))

# ---------------- rechts: Erde als Kugel ----------------
cx, cy, rk = 11.45, 3.55, 2.25
text(ax, 8.9, 7.45, "Erde als Kugel (Aufgabe 2)", fs=10.5, ha="left", fontweight="bold")
ax.add_patch(Circle((cx, cy), rk, facecolor=KRUSTE, edgecolor=LINIE, linewidth=1.4, zorder=1))
ax.add_patch(Circle((cx, cy), 0.06, facecolor=LINIE, edgecolor=LINIE, zorder=5))
text(ax, cx - 0.12, cy - 0.28, "Mitte", fs=9, ha="center", va="top")
text(ax, cx, cy + 1.15, r"$\lambda$, $\dot{q}_{\mathrm{KV}}$", fs=9.5)
# Radius R (schräg) und Koordinate r (waagerecht)
import math as _m
ang = _m.radians(35)
masslinie(ax, (cx, cy), (cx + rk * _m.cos(ang), cy + rk * _m.sin(ang)), "", farbe=GRAU)
text(ax, cx + 0.95, cy + 0.98, r"$R$", fs=10, farbe=GRAU)
pfeil(ax, (cx, cy), (cx + rk + 0.85, cy), farbe=LINIE, breite=1.0, groesse=10)
text(ax, cx + rk + 0.85, cy - 0.3, r"$r$", fs=10.5, ha="center")
# Wärmestrom aus der Kugel
for winkel in (125, 215, 305):
    w = _m.radians(winkel)
    p1 = (cx + (rk + 0.05) * _m.cos(w), cy + (rk + 0.05) * _m.sin(w))
    p2 = (cx + (rk + 0.75) * _m.cos(w), cy + (rk + 0.75) * _m.sin(w))
    pfeil(ax, p1, p2, farbe=WAERME, breite=1.4, groesse=11)
w = _m.radians(125)
text(ax, cx + (rk + 0.55) * _m.cos(w) + 0.32, cy + (rk + 0.55) * _m.sin(w) + 0.12, r"$\dot{Q}$", fs=10,
     farbe=WAERME, ha="left")
text(ax, cx + 0.2, cy - rk - 0.35, r"Oberfläche: $\vartheta_\mathrm{O}$", fs=9.5, ha="left", va="top")

print(speichern(fig, "t6_erdwaerme"))
