# -*- coding: utf-8 -*-
"""Gemeinsamer Stil für alle Skizzen der Aufgabensammlung (wie Abb. 1 der Kaffee-Aufgabe).

Verwendung in einem Skizzenskript:
    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from skizze_stil import *
    fig, ax = leinwand(7.0, 3.4, xlim=(0, 14), ylim=(0, 6.8))
    ... zeichnen ...
    speichern(fig, "t1_eisschild")      # schreibt ../grafik/t1_eisschild.png (300 dpi) und .svg

Regeln: schlicht und schematisch, keine Lösung in der Skizze (kein Bilanzraum, wenn die Studierenden
ihn einzeichnen sollen), Beschriftung deutsch, Formelzeichen wie im Text (ϑ in °C, T in K, Index u),
keine Gedankenstriche, Schriftgröße 9 bis 11.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyArrowPatch, Arc, Rectangle, Circle, Ellipse, Wedge, FancyBboxPatch
from matplotlib import font_manager

HIER = os.path.dirname(os.path.abspath(__file__))
GRAFIK = os.path.join(os.path.dirname(HIER), "grafik")

for _f in font_manager.findSystemFonts():
    if "Carlito" in _f:
        font_manager.fontManager.addfont(_f)
plt.rcParams["font.family"] = "Carlito"
plt.rcParams["mathtext.fontset"] = "custom"
plt.rcParams["mathtext.rm"] = "Carlito"
plt.rcParams["mathtext.it"] = "Carlito:italic"
plt.rcParams["mathtext.bf"] = "Carlito:bold"
plt.rcParams["svg.fonttype"] = "none"

# Farben (gedeckt, druckfreundlich)
LINIE = "#222222"      # Umrisse, Achsen
GRAU = "#555555"       # Umgebung, Nebenbeschriftung
HELLGRAU = "#BBBBBB"
WAERME = "#B03A2E"     # Wärmeströme (Pfeile, Beschriftung)
BILANZ = "#1F4E9E"     # Bilanzraum (gestrichelt), nur wenn gegeben
KALT = "#2F6DB5"       # kalte Ströme
WARM = "#C0392B"       # warme Ströme
WASSER = "#CFE3F3"
MEER = "#9EC5E6"
EIS = "#EEF5FB"
SCHNEE = "#FFFFFF"
FIRN = "#DDE7EF"
LUFT = "#F7FAFC"
BODEN = "#CDB58F"
GESTEIN = "#A99F92"
METALL = "#9AA3AD"
DAEMMUNG = "#F3D36B"
BETON = "#BDBDBD"
KAFFEE = "#8B5A2B"
GEMISCH = "#C49A6C"
MILCH = "#F4F1EA"
SONNE = "#F2B705"


def leinwand(breite=7.0, hoehe=3.4, xlim=(0, 14), ylim=(0, 6.8)):
    """Leere Zeichenfläche ohne Achsen; Koordinaten in frei gewählten Einheiten."""
    fig, ax = plt.subplots(figsize=(breite, hoehe))
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def pfeil(ax, p1, p2, farbe=LINIE, breite=1.2, groesse=11, stil="-|>", z=5, **kw):
    """Gerader Pfeil von p1 nach p2."""
    a = FancyArrowPatch(p1, p2, arrowstyle=stil, mutation_scale=groesse, color=farbe, linewidth=breite,
                        zorder=z, **kw)
    ax.add_patch(a)
    return a


def waermepfeil(ax, p1, p2, text=None, versatz=(0.12, 0.0), groesse=11, fs=10, ha="left", va="center"):
    """Roter Pfeil für einen Wärmestrom mit optionaler Beschriftung (z. B. r"$\\dot{Q}_{ab}$")."""
    pfeil(ax, p1, p2, farbe=WAERME, breite=1.4, groesse=groesse)
    if text:
        xm, ym = (p1[0] + p2[0]) / 2 + versatz[0], (p1[1] + p2[1]) / 2 + versatz[1]
        ax.text(xm, ym, text, color=WAERME, fontsize=fs, ha=ha, va=va)


def stroemungspfeil(ax, p1, p2, text=None, farbe=KALT, versatz=(0.0, 0.2), fs=10, ha="center", va="bottom"):
    """Pfeil für einen Massenstrom (Luft, Wasser, Sole)."""
    pfeil(ax, p1, p2, farbe=farbe, breite=1.6, groesse=12)
    if text:
        xm, ym = (p1[0] + p2[0]) / 2 + versatz[0], (p1[1] + p2[1]) / 2 + versatz[1]
        ax.text(xm, ym, text, color=farbe, fontsize=fs, ha=ha, va=va)


def schicht(ax, x, y, b, h, farbe, text=None, rand=LINIE, fs=10, textfarbe=LINIE, schraffur=None, lw=1.0):
    """Rechteckige Schicht (Wand, Eis, Boden) mit optionaler Beschriftung in der Mitte."""
    ax.add_patch(Rectangle((x, y), b, h, facecolor=farbe, edgecolor=rand, linewidth=lw, hatch=schraffur, zorder=1))
    if text:
        ax.text(x + b / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=textfarbe, zorder=3)


def bilanzraum(ax, x, y, b, h, text="Bilanzraum", fs=9.5, textpos="unten"):
    """Gestrichelter Bilanzraum (nur verwenden, wenn er gegeben ist und nicht gesucht wird)."""
    ax.add_patch(Rectangle((x, y), b, h, fill=False, edgecolor=BILANZ, linewidth=1.3, linestyle=(0, (4, 3)), zorder=4))
    if text:
        ty = y - 0.3 if textpos == "unten" else y + h + 0.3
        ax.text(x + b / 2, ty, text, ha="center", va="center", fontsize=fs, color=BILANZ)


def text(ax, x, y, s, fs=10, farbe=LINIE, ha="center", va="center", **kw):
    ax.text(x, y, s, fontsize=fs, color=farbe, ha=ha, va=va, **kw)


def masslinie(ax, p1, p2, s, fs=9.5, versatz=(0.15, 0.0), farbe=GRAU):
    """Maßpfeil mit Spitzen an beiden Enden und Beschriftung."""
    pfeil(ax, p1, p2, farbe=farbe, breite=0.9, groesse=8, stil="<|-|>")
    xm, ym = (p1[0] + p2[0]) / 2 + versatz[0], (p1[1] + p2[1]) / 2 + versatz[1]
    ax.text(xm, ym, s, fontsize=fs, color=farbe, ha="left", va="center")


def speichern(fig, name, ordner=None):
    """Speichert name.png (300 dpi) und name.svg im Ordner grafik der Sammlung."""
    ordner = ordner or GRAFIK
    os.makedirs(ordner, exist_ok=True)
    for ext in ("png", "svg"):
        fig.savefig(os.path.join(ordner, f"{name}.{ext}"), dpi=300, bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)
    return os.path.join(ordner, f"{name}.png")
