# -*- coding: utf-8 -*-
"""Abb. 1 in Tutorium 8: Sole-Wasser-Wärmepumpe mit Erdwärmesonde (Kreislauf mit Temperaturen).
Ohne Bilanzraum und ohne Wärmeströme (beides tragen die Studierenden in Teil b ein); der Verdampfer
zeigt keine Stromführung (Frage 1). Aufruf: python3 abb_t8_waermepumpe.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from skizze_stil import *

KM = "#4D4D4D"   # Kältemittel (dunkelgrau)

fig, ax = leinwand(7.4, 3.85, xlim=(0, 14.8), ylim=(0.1, 7.8))


def linie(pts, farbe, lw=1.8, z=2):
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=farbe, linewidth=lw, solid_capstyle="butt", zorder=z)


def richtung(p1, p2, farbe, groesse=11):
    """kleiner Pfeil in der Mitte einer Leitung"""
    pfeil(ax, p1, p2, farbe=farbe, breite=1.6, groesse=groesse, z=6)


# ---------------- Boden mit Erdwärmesonde ----------------
y_ok, y_fuss = 4.5, 1.1                      # Geländeoberfläche, Fuß der Sonde
schicht(ax, 0.0, 0.75, 4.4, y_ok - 0.75, BODEN, rand="none")
ax.plot([0.0, 4.4], [y_ok, y_ok], color=LINIE, linewidth=1.2, zorder=2)
for xg in (0.25, 0.75, 1.25, 3.35, 3.85, 4.3):    # Gras als Andeutung der Oberfläche
    ax.plot([xg, xg - 0.08], [y_ok, y_ok + 0.16], color="#6B8E23", linewidth=0.9, zorder=2)
    ax.plot([xg, xg + 0.08], [y_ok, y_ok + 0.16], color="#6B8E23", linewidth=0.9, zorder=2)
# Bohrloch (verfüllt) und U-Rohr: links steigt die erwärmte Sole auf, rechts fließt die kalte Sole hinab
schicht(ax, 1.72, y_fuss - 0.2, 1.06, y_ok - y_fuss + 0.2, "#E6DCC8", rand="#8C7B5E", lw=0.8)
xa, xb = 1.98, 2.52
linie([(xa, y_fuss + 0.25), (xa, 6.35)], KALT)
linie([(xb, 5.25), (xb, y_fuss + 0.25)], KALT)
ax.add_patch(Arc(((xa + xb) / 2, y_fuss + 0.25), xb - xa, 0.5, theta1=180, theta2=360,
                 edgecolor=KALT, linewidth=1.8, zorder=2))
richtung((xa, 2.6), (xa, 3.2), KALT)
richtung((xb, 3.2), (xb, 2.6), KALT)
pfeil(ax, (0.45, y_fuss), (0.45, y_ok), farbe=GRAU, breite=0.9, groesse=8, stil="<|-|>")
text(ax, 0.75, (y_fuss + y_ok) / 2, r"$L = 100\,\mathrm{m}$", fs=9.5, farbe=GRAU, rotation=90)
text(ax, 3.6, 2.95, "Boden", fs=10, farbe="#5C4A2E")
text(ax, 3.6, 2.45, r"$\vartheta_{\mathrm{B}} = 11\,\mathrm{°C}$", fs=10, farbe="#5C4A2E")
text(ax, 2.2, 0.4, r"Erdwärmesonde, Rohre mit $d_{\mathrm{i}}$", fs=9.5)

# ---------------- Sole-Leitungen zum Verdampfer ----------------
xV0, xV1, yV0, yV1 = 5.15, 6.75, 4.35, 7.05   # Verdampfer
y_warm, y_kalt = 6.35, 5.25                   # Sole aus der Sonde zum Verdampfer (oben), zurück zur Sonde (unten)
linie([(xa, y_warm), (xV0, y_warm)], KALT)
linie([(xV0, y_kalt), (xb, y_kalt)], KALT)
richtung((3.7, y_warm), (4.3, y_warm), KALT)
richtung((4.3, y_kalt), (3.7, y_kalt), KALT)
text(ax, 3.85, y_warm + 0.33, r"$\vartheta_{\mathrm{S{,}aus}} = 2\,\mathrm{°C}$", fs=9.5, farbe=KALT)
text(ax, 3.85, y_kalt - 0.33, r"$\vartheta_{\mathrm{S{,}ein}} = -1\,\mathrm{°C}$", fs=9.5, farbe=KALT)
text(ax, 0.95, 6.35, "Sole", fs=10, farbe=KALT, fontweight="bold")

# ---------------- Wärmepumpe ----------------
# Verdampfer: zwei Kanäle (Sole links, Kältemittel rechts), keine Pfeile im Inneren
ax.add_patch(FancyBboxPatch((xV0, yV0), xV1 - xV0, yV1 - yV0, boxstyle="round,pad=0,rounding_size=0.12",
                            facecolor="#EEF3F8", edgecolor=LINIE, linewidth=1.3, zorder=3))
ax.plot([(xV0 + xV1) / 2] * 2, [yV0 + 0.12, yV1 - 0.12], color=LINIE, linewidth=0.9, linestyle=(0, (3, 2)), zorder=4)
text(ax, (xV0 + xV1) / 2, yV1 + 0.3, "Verdampfer", fs=10.5, fontweight="bold")
text(ax, xV0 + 0.4, (yV0 + yV1) / 2, "Sole", fs=9, farbe=KALT, rotation=90)
text(ax, xV1 - 0.4, (yV0 + yV1) / 2, "Kältemittel", fs=9, farbe=KM, rotation=90)
text(ax, (xV0 + xV1) / 2, yV0 - 0.32, r"$\vartheta_{\mathrm{V}} = -6\,\mathrm{°C}$", fs=10)

# Kondensator
xK0, xK1 = 10.05, 11.65
ax.add_patch(FancyBboxPatch((xK0, yV0), xK1 - xK0, yV1 - yV0, boxstyle="round,pad=0,rounding_size=0.12",
                            facecolor="#FBEFEA", edgecolor=LINIE, linewidth=1.3, zorder=3))
ax.plot([(xK0 + xK1) / 2] * 2, [yV0 + 0.12, yV1 - 0.12], color=LINIE, linewidth=0.9, linestyle=(0, (3, 2)), zorder=4)
text(ax, (xK0 + xK1) / 2, yV1 + 0.3, "Kondensator", fs=10.5, fontweight="bold")
text(ax, xK0 + 0.4, (yV0 + yV1) / 2, "Kältemittel", fs=9, farbe=KM, rotation=90)
text(ax, xK1 - 0.4, (yV0 + yV1) / 2, "Heizwasser", fs=9, farbe=WARM, rotation=90)
text(ax, (xK0 + xK1) / 2, yV0 - 0.32, r"$\vartheta_{\mathrm{K}} = 40\,\mathrm{°C}$", fs=10)

# Verdichter (Kreis mit Trapez) oben, Expansionsventil (Doppeldreieck) unten
xm, yD, yE = (xV1 + xK0) / 2, 6.6, 4.75
r = 0.42
ax.add_patch(Circle((xm, yD), r, facecolor="white", edgecolor=LINIE, linewidth=1.3, zorder=5))
ax.plot([xm - r * 0.75, xm + r * 0.75], [yD - r * 0.66 + 0.18, yD - r * 0.25 + 0.05], color=LINIE, linewidth=1.0, zorder=6)
ax.plot([xm - r * 0.75, xm + r * 0.75], [yD + r * 0.66 - 0.18, yD + r * 0.25 - 0.05], color=LINIE, linewidth=1.0, zorder=6)
text(ax, xm, yD + r + 0.28, "Verdichter", fs=10)
ax.add_patch(Polygon([[xm - 0.32, yE - 0.22], [xm - 0.32, yE + 0.22], [xm + 0.32, yE - 0.22], [xm + 0.32, yE + 0.22]],
                     closed=True, facecolor="white", edgecolor=LINIE, linewidth=1.2, zorder=5))
text(ax, xm, yE - 0.5, "Expansionsventil", fs=9.5)

# Kältemittelkreis
linie([(xV1, yD), (xm - r, yD)], KM)
linie([(xm + r, yD), (xK0, yD)], KM)
linie([(xK0, yE), (xm + 0.32, yE)], KM)
linie([(xm - 0.32, yE), (xV1, yE)], KM)
richtung((7.15, yD), (7.55, yD), KM, groesse=10)
richtung((9.25, yD), (9.65, yD), KM, groesse=10)
richtung((9.65, yE), (9.25, yE), KM, groesse=10)
richtung((7.55, yE), (7.15, yE), KM, groesse=10)
text(ax, xm, 5.68, "Kältemittel", fs=9, farbe=KM)

# Heizkreis mit Fußbodenheizung
xH0, xH1 = 12.75, 14.65
y_vl, y_rl = 6.35, 5.25
linie([(xK1, y_vl), (xH0 + 0.1, y_vl)], WARM)
linie([(xH0 + 0.1, y_rl), (xK1, y_rl)], WARM)
richtung((11.95, y_vl), (12.4, y_vl), WARM, groesse=10)
richtung((12.4, y_rl), (11.95, y_rl), WARM, groesse=10)
# Schlange der Fußbodenheizung
xs, ys = [xH0 + 0.1], [y_vl]
yy = y_vl
for i in range(5):
    x_re = xH1 - 0.12 if i % 2 == 0 else xH0 + 0.45
    xs += [x_re, x_re]
    yy2 = yy - 0.22
    ys += [yy, yy2]
    yy = yy2
xs += [xH0 + 0.1]
ys += [y_rl]
ax.plot(xs, ys, color=WARM, linewidth=1.3, zorder=2)
ax.add_patch(Rectangle((xH0, y_rl - 0.2), xH1 - xH0, y_vl - y_rl + 0.4, fill=False, edgecolor=GRAU, linewidth=0.9, zorder=1))
text(ax, (xH0 + xH1) / 2, y_vl + 0.55, "Heizkreis", fs=10.5, fontweight="bold")
text(ax, (xH0 + xH1) / 2, y_rl - 0.55, "Fußbodenheizung", fs=9.5)

speichern(fig, "t8_waermepumpe")
print("ok")
