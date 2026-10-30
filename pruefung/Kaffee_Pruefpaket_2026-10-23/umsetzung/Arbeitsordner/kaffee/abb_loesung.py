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
fig, ax = plt.subplots(figsize=(4.4, 2.75))
ax.set_xlim(-0.1, 8.6); ax.set_ylim(-0.75, 4.65); ax.axis("off")
x, y, b, h = 2.1, 0.4, 2.6, 3.0
ROT, BLAU = "#B03A2E", "#1F4E9E"
ax.add_patch(Polygon([[x + 0.08, y + 0.08], [x + b - 0.08, y + 0.08], [x + b - 0.08, y + 2.2], [x + 0.08, y + 2.2]],
                     closed=True, facecolor="#C49A6C", edgecolor="none"))
ax.add_patch(Polygon([[x, y + h], [x, y], [x + b, y], [x + b, y + h]], closed=False, fill=False, edgecolor=LINIE, linewidth=1.6))
ax.add_patch(Arc((x + b, y + 1.5), 1.2, 1.4, theta1=-90, theta2=90, edgecolor=LINIE, linewidth=1.6))
# Bilanzraum: knapp innerhalb der Wand um den Tasseninhalt (a bis e); in f mit Becher (äußere Linie)
ax.add_patch(Rectangle((x + 0.17, y + 0.17), b - 0.34, 2.2, fill=False, edgecolor=BLAU, linewidth=1.3, linestyle=(0, (4, 3))))
ax.add_patch(Rectangle((x - 0.22, y - 0.22), b + 1.12, 2.82, fill=False, edgecolor=BLAU, linewidth=1.0, linestyle=(0, (1.5, 2.5))))
ax.text(x + b / 2, y + 1.2, r"$T(t),\ m,\ c_p$", ha="center", va="center", fontsize=11)
pfeil = dict(arrowstyle="-|>", mutation_scale=11, color=ROT, linewidth=1.3)
ax.add_patch(FancyArrowPatch((x + b / 2, y + 2.45), (x + b / 2, y + 3.85), **pfeil))
ax.add_patch(FancyArrowPatch((x - 0.3, y + 0.75), (x - 1.25, y + 0.75), **pfeil))
ax.add_patch(FancyArrowPatch((x + b + 0.95, y + 0.75), (x + b + 1.9, y + 0.75), **pfeil))
ax.text(x + b / 2 + 0.15, y + 3.55, r"$\dot{Q}_{ab} = kA\,(T - T_u)$", fontsize=10.5, color=ROT, va="center")
ax.text(-0.05, 4.4, r"Umgebung: $T_u$", fontsize=10, color="#555555", va="center")
ax.text(x + b / 2, y - 0.5, "Bilanzraum (a bis e)", fontsize=9.5, color=BLAU, ha="center", va="center")
ax.text(x + b + 1.0, y - 0.5, "in f mit Becher", fontsize=9.5, color=BLAU, ha="left", va="center")
for ext in ("png", "svg"):
    fig.savefig(os.path.join(out, f"AbbL1_Bilanzraum.{ext}"), dpi=300, bbox_inches="tight", pad_inches=0.04)
plt.close(fig)

# --------------------------------------------------- L2 Temperaturverlauf
t = [i * 10.0 for i in range(0, 361)]           # s, bis 60 min
T_U = r["T_U"]
th1 = [T_U + (r["T1_0"] - T_U) * math.exp(-r["a_G"] * ti) - 273.15 for ti in t]
th2 = [T_U + (r["T_K0"] - T_U) * math.exp(-r["a_K"] * ti) - 273.15 for ti in t]
tm = [ti / 60 for ti in t]
TS = r["t_schnitt"] / 60
thS = T_U + (r["T1_0"] - T_U) * math.exp(-r["a_G"] * r["t_schnitt"]) - 273.15
F1, F2 = "#8B5A2B", "#222222"
L1 = dict(color=F1, linewidth=1.8)
L2 = dict(color=F2, linewidth=1.8, linestyle=(0, (6, 3)))
SPRUNG = dict(linewidth=1.4, linestyle=(0, (1.2, 1.6)))
de = lambda x: f"{x:.2f}".replace(".", ",")


def zeichne(ax, mit_text):
    ax.plot(tm, th1, **L1)
    ax.plot(tm, th2, **L2)
    ax.plot([0, 0], [r["T_K0"] - 273.15, r["T1_0"] - 273.15], color=F1, **SPRUNG)
    ax.plot([60, 60], [r["T2_K"] - 273.15, r["T2"] - 273.15], color=F2, **SPRUNG)
    ax.plot([60], [r["T1"] - 273.15], "o", color=F1, markersize=4.5)
    ax.plot([60], [r["T2"] - 273.15], "s", color=F2, markersize=4.5)
    ax.plot([TS], [thS], "o", markerfacecolor="white", markeredgecolor=LINIE, markersize=6, zorder=5)


fig, ax = plt.subplots(figsize=(6.0, 3.4))
zeichne(ax, True)
ax.axhline(P["th_U"], color="#888888", linewidth=0.9, linestyle=(0, (5, 4)))
ax.text(1, P["th_U"] + 1.2, r"$\vartheta_u$", fontsize=10, color="#666666")
ax.plot([], [], label="Tasse 1: Milch bei $t = 0$", **L1)
ax.plot([], [], label="Tasse 2: Milch bei $t = 60\\,\\mathrm{min}$", **L2)
ax.legend(frameon=False, fontsize=9, loc="lower left", bbox_to_anchor=(0.0, 0.08), handlelength=3.2)
ax.set_xlim(-2, 64); ax.set_ylim(15, 85)
ax.set_xlabel(r"Zeit $t$ in min"); ax.set_ylabel(r"Temperatur $\vartheta$ in °C")
ax.set_xticks([0, 10, 20, 30, 40, 50, 60])
for s_ in ("top", "right"):
    ax.spines[s_].set_visible(False)
# Ausschnitt 40 bis 60 min: Schnittpunkt und Mischsprung von Tasse 2
ins = ax.inset_axes([0.50, 0.50, 0.48, 0.48])
zeichne(ins, False)
ins.set_xlim(39, 67); ins.set_ylim(29, 44)
ins.set_xticks([40, 50, 60]); ins.set_yticks([30, 35, 40])
ins.tick_params(labelsize=8)
ins.annotate(f"etwa {TS:.0f} min", (TS, thS), xytext=(43.0, 31.0),
             fontsize=8, arrowprops=dict(arrowstyle="-", color="#666666", linewidth=0.8))
ins.text(60.8, r["T1"] - 273.15 + 0.6, de(r["T1"] - 273.15) + " °C", fontsize=8, color=F1, va="bottom")
ins.text(60.8, r["T2_K"] - 273.15 - 0.3, de(r["T2_K"] - 273.15) + " °C", fontsize=7.5, color=F2, va="top")
ins.text(60.8, r["T2"] - 273.15, de(r["T2"] - 273.15) + " °C", fontsize=8, color=F2, va="center")
ins.text(59.3, 31.4, "Milch", fontsize=7.5, color=F2, ha="right")
for s_ in ("top", "right"):
    ins.spines[s_].set_visible(False)
ax.indicate_inset_zoom(ins, edgecolor="#999999", linewidth=0.8)
for ext in ("png", "svg"):
    fig.savefig(os.path.join(out, f"AbbL2_Temperaturverlauf.{ext}"), dpi=300, bbox_inches="tight", pad_inches=0.04)
print("ok")
