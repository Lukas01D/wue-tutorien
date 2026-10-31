# -*- coding: utf-8 -*-
"""Abbildung 1 der Kaffee-Aufgabe: die zwei Varianten (Milch bei t = 0 bzw. bei t = 60 min).
Aufruf: python3 abb_t5_kaffee.py [ausgabeordner]   (ohne Angabe: ../grafik/t5_kaffee_tassen.png und .svg)"""
import sys, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyArrowPatch, Arc, Rectangle
from matplotlib import font_manager

GRAFIK = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "grafik")
out = sys.argv[1] if len(sys.argv) > 1 else GRAFIK
for f in font_manager.findSystemFonts():
    if "Carlito" in f:
        font_manager.fontManager.addfont(f)
plt.rcParams["font.family"] = "Carlito"
plt.rcParams["mathtext.fontset"] = "custom"
plt.rcParams["mathtext.rm"] = "Carlito"
plt.rcParams["mathtext.it"] = "Carlito:italic"

KAFFEE = "#8B5A2B"
GEMISCH = "#C49A6C"
MILCH = "#F4F1EA"
LINIE = "#222222"

fig, ax = plt.subplots(figsize=(7.2, 3.5))
ax.set_xlim(0, 14.4)
ax.set_ylim(0, 7.0)
ax.axis("off")


def tasse(x, y, fuell, text=None, stand=1.25):
    """Becher mit Henkel; x, y = linke untere Ecke."""
    b, h = 1.5, 1.7
    ax.add_patch(Polygon([[x + 0.06, y + 0.06], [x + b - 0.06, y + 0.06], [x + b - 0.06, y + stand], [x + 0.06, y + stand]],
                         closed=True, facecolor=fuell, edgecolor="none", zorder=1))
    ax.add_patch(Polygon([[x, y + h], [x, y], [x + b, y], [x + b, y + h]], closed=False, fill=False,
                         edgecolor=LINIE, linewidth=1.4, zorder=2))
    ax.add_patch(Arc((x + b, y + 0.85), 0.75, 0.85, theta1=-90, theta2=90, edgecolor=LINIE, linewidth=1.4, zorder=2))
    # Wärmestrom an die Umgebung
    ax.add_patch(FancyArrowPatch((x + b / 2, y + h + 0.1), (x + b / 2, y + h + 0.75), arrowstyle="-|>",
                                 mutation_scale=10, color="#B03A2E", linewidth=1.2))
    ax.text(x + b / 2 + 0.12, y + h + 0.45, r"$\dot{Q}_\mathrm{ab}$", fontsize=10, color="#B03A2E", va="center")
    # auch durch die Wand: kleine Pfeile zu beiden Seiten (gesamte Wärmeabgabe, wie Abb. L1)
    for x1, x2 in ((x - 0.08, x - 0.55), (x + b + 0.08, x + b + 0.55)):
        ax.add_patch(FancyArrowPatch((x1, y + 0.3), (x2, y + 0.3), arrowstyle="-|>",
                                     mutation_scale=9, color="#B03A2E", linewidth=1.1))
    if text:
        ax.text(x + b / 2, y - 0.3, text, ha="center", va="top", fontsize=10)


def milch(x, y):
    ax.add_patch(Polygon([[x, y], [x + 0.55, y], [x + 0.62, y + 0.75], [x - 0.07, y + 0.75]], closed=True,
                         facecolor=MILCH, edgecolor=LINIE, linewidth=1.1))
    ax.text(x + 0.27, y - 0.12, "Milch", ha="center", va="top", fontsize=9)


def pfeil(x1, x2, y, text):
    ax.add_patch(FancyArrowPatch((x1, y), (x2, y), arrowstyle="-|>", mutation_scale=12, color=LINIE, linewidth=1.2))
    ax.text((x1 + x2) / 2, y + 0.18, text, ha="center", va="bottom", fontsize=10)


# Zeitachse
ax.add_patch(FancyArrowPatch((2.3, 6.55), (13.9, 6.55), arrowstyle="-|>", mutation_scale=12, color="#555555", linewidth=1.0))
ax.text(2.95, 6.72, r"$t = 0$", ha="center", fontsize=10)
ax.text(12.15, 6.72, r"$t = 60\,\mathrm{min}$", ha="center", fontsize=10)
ax.text(13.95, 6.3, r"$t$", ha="right", fontsize=10)

# Tasse 1: Milch sofort
ax.text(0.0, 4.15, "Tasse 1", fontsize=11, fontweight="bold", va="center")
milch(1.15, 5.15)
ax.add_patch(FancyArrowPatch((1.95, 5.4), (2.45, 5.0), arrowstyle="-|>", mutation_scale=9, color=LINIE, linewidth=1.0))
tasse(2.2, 3.75, GEMISCH, r"$\vartheta_{1{,}0}$")
pfeil(4.6, 10.6, 4.6, "Abkühlen 60 min")
tasse(11.4, 3.75, GEMISCH, r"$\vartheta_{1}$ = ?")

# Tasse 2: Milch nach 60 min
ax.text(0.0, 0.85, "Tasse 2", fontsize=11, fontweight="bold", va="center")
tasse(2.2, 0.45, KAFFEE, r"$\vartheta_{\mathrm{K}{,}0}$", stand=1.05)
pfeil(4.6, 10.6, 1.3, "Abkühlen 60 min")
milch(10.3, 1.85)
ax.add_patch(FancyArrowPatch((11.1, 2.1), (11.6, 1.7), arrowstyle="-|>", mutation_scale=9, color=LINIE, linewidth=1.0))
tasse(11.4, 0.45, GEMISCH, r"$\vartheta_{2}$ = ?")

ax.text(0.0, 6.55, r"Umgebung: $\vartheta_\mathrm{u}$", ha="left", va="center", fontsize=9.5, color="#555555")

os.makedirs(out, exist_ok=True)
for ext in ("png", "svg"):
    fig.savefig(os.path.join(out, f"t5_kaffee_tassen.{ext}"), dpi=300, bbox_inches="tight")
print("ok")
