# -*- coding: utf-8 -*-
"""Abbildungen der Musterlösung: L1 Bilanzraum, L2 Temperaturverlauf beider Tassen.
Aufruf: python3 abb_loesung.py <ausgabeordner>"""
import sys, os, math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyArrowPatch, Arc, Rectangle
from matplotlib import font_manager
from kaffee_modell import P, rechne

out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "grafik")
os.makedirs(out, exist_ok=True)
for f in font_manager.findSystemFonts():
    if "Carlito" in f:
        font_manager.fontManager.addfont(f)
plt.rcParams["font.family"] = "Carlito"
plt.rcParams["mathtext.fontset"] = "custom"
plt.rcParams["mathtext.rm"] = "Carlito"
plt.rcParams["mathtext.it"] = "Carlito:italic"
LINIE = "#222222"
r = rechne(P)

# ------------------------------------------------------------ L1 Bilanzraum
fig, ax = plt.subplots(figsize=(3.6, 2.7))
ax.set_xlim(0, 7.0); ax.set_ylim(-0.6, 5.2); ax.axis("off")
x, y, b, h = 1.9, 0.4, 2.6, 3.0
ROT, BLAU = "#B03A2E", "#1F4E9E"
ax.add_patch(Polygon([[x + 0.08, y + 0.08], [x + b - 0.08, y + 0.08], [x + b - 0.08, y + 2.2], [x + 0.08, y + 2.2]],
                     closed=True, facecolor="#C49A6C", edgecolor="none"))
ax.add_patch(Polygon([[x, y + h], [x, y], [x + b, y], [x + b, y + h]], closed=False, fill=False, edgecolor=LINIE, linewidth=1.6))
ax.add_patch(Arc((x + b, y + 1.5), 1.2, 1.4, theta1=-90, theta2=90, edgecolor=LINIE, linewidth=1.6))
# Bilanzraum: knapp innerhalb der Wand um den Tasseninhalt
ax.add_patch(Rectangle((x + 0.17, y + 0.17), b - 0.34, 2.2, fill=False, edgecolor=BLAU, linewidth=1.3, linestyle=(0, (4, 3))))
ax.text(x + b / 2, y + 1.2, r"$T(t),\ m,\ c_p$", ha="center", va="center", fontsize=11)
pfeil = dict(arrowstyle="-|>", mutation_scale=11, color=ROT, linewidth=1.3)
ax.add_patch(FancyArrowPatch((x + b / 2, y + 2.45), (x + b / 2, y + 3.85), **pfeil))
ax.add_patch(FancyArrowPatch((x - 0.05, y + 0.6), (x - 1.0, y + 0.6), **pfeil))
ax.add_patch(FancyArrowPatch((x + b + 0.05, y + 0.6), (x + b + 1.0, y + 0.6), **pfeil))
ax.text(x + b / 2 + 0.15, y + 3.55, r"$\dot{Q}_{ab} = kA\,(T - T_u)$", fontsize=10.5, color=ROT, va="center")
ax.text(0.05, 4.9, r"Umgebung $T_u$", fontsize=10, color="#555555", va="center")
ax.text(x + b / 2, y - 0.35, "Bilanzraum", fontsize=9.5, color=BLAU, ha="center", va="center")
for ext in ("png", "svg"):
    fig.savefig(os.path.join(out, f"AbbL1_Bilanzraum.{ext}"), dpi=300, bbox_inches="tight")
plt.close(fig)

# --------------------------------------------------- L2 Temperaturverlauf
t = [i * 10.0 for i in range(0, 361)]           # s, bis 60 min
T_U = r["T_U"]
T1 = [T_U + (r["T1_0"] - T_U) * math.exp(-r["a_G"] * ti) - 273.15 for ti in t]
T2 = [T_U + (r["T_K0"] - T_U) * math.exp(-r["a_K"] * ti) - 273.15 for ti in t]
tm = [ti / 60 for ti in t]
fig, ax = plt.subplots(figsize=(5.6, 3.1))
ax.plot(tm, T1, color="#C49A6C", linewidth=2.0, label="Tasse 1: Milch bei t = 0")
ax.plot(tm, T2, color="#8B5A2B", linewidth=2.0, label="Tasse 2: Milch bei t = 60 min")
SPRUNG = dict(linewidth=1.6, linestyle=(0, (1.6, 1.4)))   # Mischen: gestrichelt, kurz genug für den kleinen Sprung
ax.plot([60, 60], [r["T2_K"] - 273.15, r["T2"] - 273.15], color="#8B5A2B", **SPRUNG)
ax.plot([0, 0], [r["T_K0"] - 273.15, r["T1_0"] - 273.15], color="#C49A6C", **SPRUNG)
ax.plot([60], [r["T1"] - 273.15], "o", color="#C49A6C", markersize=5)
ax.plot([60], [r["T2"] - 273.15], "o", color="#8B5A2B", markersize=5)
ax.annotate(f"{r['T1'] - 273.15:.2f} °C".replace(".", ","), (60, r["T1"] - 273.15), xytext=(63.5, r["T1"] - 273.15 + 2.5),
            fontsize=10, va="center")
ax.annotate(f"{r['T2'] - 273.15:.2f} °C".replace(".", ","), (60, r["T2"] - 273.15), xytext=(63.5, r["T2"] - 273.15 - 2.5),
            fontsize=10, va="center")
ax.axhline(P["th_U"], color="#888888", linewidth=0.9, linestyle=(0, (5, 4)))
ax.text(1, P["th_U"] + 1.2, r"$\vartheta_u$", fontsize=10, color="#666666")
ax.set_xlim(-2, 72); ax.set_ylim(15, 90)
ax.set_xlabel("Zeit t in min"); ax.set_ylabel("Temperatur ϑ in °C")
ax.set_xticks([0, 10, 20, 30, 40, 50, 60])
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.legend(frameon=False, fontsize=9.5, loc="upper right")
for ext in ("png", "svg"):
    fig.savefig(os.path.join(out, f"AbbL2_Temperaturverlauf.{ext}"), dpi=300, bbox_inches="tight")
print("ok")
