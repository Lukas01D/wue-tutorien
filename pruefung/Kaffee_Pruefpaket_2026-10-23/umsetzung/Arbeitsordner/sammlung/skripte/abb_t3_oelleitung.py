# -*- coding: utf-8 -*-
"""Tutorium 3, Abb. 2: Querschnitt der gedämmten Ölleitung (Öl, Stahlrohr, Dämmung, Wind).
Keine Lösung: alpha_a und die Oberflächentemperatur werden in der Aufgabe berechnet.
Aufruf: python3 abb_t3_oelleitung.py   (schreibt ../grafik/t3_oelleitung.png und .svg)"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from skizze_stil import *

fig, ax = leinwand(7.0, 3.6, xlim=(0, 14), ylim=(0, 7.2))

cx, cy = 6.4, 3.55
r_oel, r_st, r_iso = 2.05, 2.28, 3.05          # nicht maßstäblich (Stahl dicker gezeichnet)
OEL = "#4A3B2A"

ax.add_patch(Circle((cx, cy), r_iso, facecolor=DAEMMUNG, edgecolor=LINIE, linewidth=1.2, zorder=1))
ax.add_patch(Circle((cx, cy), r_iso, fill=False, hatch="////", edgecolor="#C9A73F", linewidth=0, zorder=1))
ax.add_patch(Circle((cx, cy), r_iso, fill=False, edgecolor=LINIE, linewidth=1.2, zorder=2))
ax.add_patch(Circle((cx, cy), r_st, facecolor=METALL, edgecolor=LINIE, linewidth=1.0, zorder=2))
ax.add_patch(Circle((cx, cy), r_oel, facecolor=OEL, edgecolor=LINIE, linewidth=1.0, zorder=3))
text(ax, cx - 0.45, cy - 0.15, "Öl:", fs=11, farbe="white")
text(ax, cx - 0.45, cy - 0.75, r"$\vartheta_i$, $\alpha_i$", fs=11, farbe="white")

# Wärmestrom radial nach außen (rechts oben)
w = math.radians(38)
waermepfeil(ax, (cx + 0.55 * math.cos(w), cy + 0.55 * math.sin(w)), (cx + 3.75 * math.cos(w), cy + 3.75 * math.sin(w)))
text(ax, cx + 3.75 * math.cos(w) + 0.05, cy + 3.75 * math.sin(w) + 0.25, r"$\dot{Q}$", fs=11.5, farbe=WAERME, ha="left")

# Wind von links
for y in (1.6, 2.85, 4.1, 5.35):
    stroemungspfeil(ax, (0.35, y), (2.25, y))
text(ax, 1.3, 6.35, r"Wind: $w$", fs=10.5, farbe=KALT)
text(ax, 1.3, 0.75, r"Luft: $\vartheta_u$", fs=10.5)

# Beschriftung der Schichten rechts mit Hinweislinien
def hinweis(winkel, r, xt, yt, s):
    w = math.radians(winkel)
    xp, yp = cx + r * math.cos(w), cy + r * math.sin(w)
    ax.plot([xp, xt - 0.12], [yp, yt], color=GRAU, linewidth=0.8, zorder=6)
    ax.add_patch(Circle((xp, yp), 0.05, color=GRAU, zorder=6))
    text(ax, xt, yt, s, fs=10.5, ha="left")

hinweis(-8, (r_oel + r_st) / 2, 10.0, 3.0, r"Stahlrohr: $d_{St}$, $s_{St}$, $\lambda_{St}$")
hinweis(-32, (r_st + r_iso) / 2, 10.0, 1.75, r"Dämmung: $s_{Iso}$, $\lambda_{Iso}$")
hinweis(-58, r_iso, 10.0, 0.6, r"Außenseite: $\alpha_a$ = ?")
text(ax, 13.9, 6.9, "nicht maßstäblich", fs=8.5, farbe=GRAU, ha="right")

print(speichern(fig, "t3_oelleitung"))
