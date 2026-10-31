# -*- coding: utf-8 -*-
"""Tutorium 3, Abb. 1: Schnee und Meereis als Deckel zwischen Ozean und Luft (Schichten, Temperaturen, Wärmestrom).
Keine Lösung: Grenzflächentemperaturen nur als Formelzeichen, kein Ersatzschaltbild (Teil a).
Aufruf: python3 abb_t3_meereis.py   (schreibt ../grafik/t3_meereis.png und .svg)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from skizze_stil import *

fig, ax = leinwand(7.0, 3.5, xlim=(0, 14), ylim=(0, 7.0))

x0, b = 2.2, 8.4                      # Schichten von x0 bis x0 + b
y_W, y_E, y_S, y_L = 0.35, 1.75, 4.45, 5.2   # Unterkanten: Meerwasser, Eis, Schnee, Luft

# Luft (nur Fläche, oben offen)
ax.add_patch(Rectangle((x0, y_L), b, 1.55, facecolor=LUFT, edgecolor="none", zorder=0))
text(ax, x0 + 2.0, y_L + 0.85, r"Luft: $\vartheta_\mathrm{u}$, $\alpha_\mathrm{a}$", fs=10.5)
stroemungspfeil(ax, (x0 + 3.9, y_L + 0.75), (x0 + 5.7, y_L + 0.75), text="Wind", farbe=KALT, fs=9.5)

# Schnee mit Punktraster, Meereis, Meerwasser
schicht(ax, x0, y_S, b, y_L - y_S, SCHNEE)
ax.add_patch(Rectangle((x0, y_S), b, y_L - y_S, fill=False, hatch="..", edgecolor=HELLGRAU, linewidth=0, zorder=1))
text(ax, x0 + 2.4, (y_S + y_L) / 2, r"Schnee: $s_\mathrm{S}$, $\lambda_\mathrm{S}$", fs=10.5,
     bbox=dict(facecolor=SCHNEE, edgecolor="none", pad=1.0))
schicht(ax, x0, y_E, b, y_S - y_E, "#DCEAF5", text=r"Meereis: $s_\mathrm{E}$, $\lambda_\mathrm{E}$", fs=10.5)
ax.texts[-1].set_x(x0 + 2.4)
schicht(ax, x0, y_W, b, y_E - y_W, MEER, text=r"Meerwasser: $\vartheta_\mathrm{W}$", fs=10.5)
ax.texts[-1].set_x(x0 + 2.4)

# Wärmestrom vom Ozean in die Luft
waermepfeil(ax, (x0 + 6.9, y_W + 0.45), (x0 + 6.9, y_L + 1.25), text=r"$\dot{Q}$", versatz=(0.18, -0.45), fs=11.5)

# Grenzflächentemperaturen rechts
for y, s in ((y_L, r"$\vartheta_\mathrm{O}$ = ?"), (y_S, r"$\vartheta_{\mathrm{SE}}$ = ?"), (y_E, r"$\vartheta_\mathrm{W}$")):
    ax.plot([x0 + b, x0 + b + 0.35], [y, y], color=LINIE, linewidth=1.0, zorder=3)
    text(ax, x0 + b + 0.45, y, s, fs=10.5, ha="left")

# Dicken links
for y1, y2, s in ((y_S, y_L, r"$s_\mathrm{S}$"), (y_E, y_S, r"$s_\mathrm{E}$")):
    pfeil(ax, (x0 - 0.35, y1), (x0 - 0.35, y2), farbe=GRAU, breite=0.9, groesse=7, stil="<|-|>")
    text(ax, x0 - 0.5, (y1 + y2) / 2, s, fs=10.5, farbe=GRAU, ha="right")
text(ax, x0 + b, 0.08, "nicht maßstäblich", fs=8.5, farbe=GRAU, ha="right")

print(speichern(fig, "t3_meereis"))
