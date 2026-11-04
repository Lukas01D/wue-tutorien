#!/usr/bin/env python3
"""Kontrast- und Farbsehschwaechen-Pruefung fuer das Kaffee-Simulationstool (Recherche R2).

Rechnet
1. das Kontrastverhaeltnis nach WCAG 2.2 (relative Luminanz, Definition im Glossar
   von WCAG 2.2: Schwelle 0,04045, Gewichte 0,2126 / 0,7152 / 0,0722) jeder Farbe
   gegen Weiss #ffffff und gegen den Seitenhintergrund #f6f5f2;
2. die simulierte Darstellung bei Protanopie, Deuteranopie und Tritanopie nach
   Machado, Oliveira und Fernandes (2009), Matrizen fuer Schweregrad 1,0
   (Tabelle auf https://www.inf.ufrgs.br/~oliveira/pubs_files/CVD_Simulation/CVD_Simulation.html),
   angewandt auf linearisierte sRGB-Werte;
3. den Farbabstand CIEDE2000 (Delta E 00) zwischen allen Paaren, normal und simuliert,
   dazu den Helligkeitsabstand Delta L* (CIELAB, D65).

Bewertung des Farbabstands (Faustregel dieses Skripts, keine Norm):
  Delta E 00 >= 20  gut unterscheidbar auch als duenne Linie
  10 <= dE < 20     unterscheidbar, Linienart zusaetzlich noetig
  dE < 10           verwechselbar
Aufruf: python3 r2_kontrast.py
"""
import itertools
import numpy as np

# ---------------------------------------------------------------- Farben
HEUTE = {
    "Tasse 1": "#8b5a2b",
    "Tasse 2": "#222222",
    "Becher 3": "#4a7fb0",
    "Akzent": "#1f4e9e",
    "Grau-Text": "#5f5f5a",
    "Rot": "#b03a2e",
    "Raumlinie": "#9a9993",
}

# Vorschlag (minimale Aenderung): Die heutige Palette trennt die Kurven schon
# ueber die Helligkeit (schwarz, mittel, hell), das bleibt bei jeder
# Farbsehschwaeche erhalten. Geaendert werden nur
#  - Becher 3: etwas dunkler, damit auch Beschriftung (Text) >= 4,5:1 erreicht,
#  - Raumlinie: dunkler, damit die Linie >= 3:1 erreicht (Beschriftung in Grau-Text),
#  - Rot: im Diagramm durch Purpurrot ersetzt, weil Rot #b03a2e bei Rot-Gruen-
#    Schwaeche mit Tasse 1 zusammenfaellt.
VORSCHLAG = {
    "Tasse 1": "#8b5a2b",
    "Tasse 2": "#222222",
    "Becher 3": "#3d70a3",
    "Akzent": "#1f4e9e",
    "Grau-Text": "#5f5f5a",
    "Rot": "#a0306a",
    "Raumlinie": "#8a8984",
}

# Zum Vergleich: Okabe-Ito-Farbtoene, abgedunkelt auf >= 4,5:1. Alle drei Kurven
# haben dann fast dieselbe Helligkeit und fallen bei Farbsehschwaeche teils
# zusammen (siehe Ausgabe), deshalb nicht empfohlen.
OKABE_ITO_DUNKEL = {
    "Tasse 1": "#a64b00",
    "Tasse 2": "#0067a6",
    "Becher 3": "#007a5a",
    "Akzent": "#1f4e9e",
    "Grau-Text": "#5f5f5a",
    "Rot": "#b03a2e",
    "Raumlinie": "#6f6e69",
}

HINTERGRUENDE = {"weiss #ffffff": "#ffffff", "hell #f6f5f2": "#f6f5f2"}

# Paare, die im Diagramm nebeneinander vorkommen und unterscheidbar sein muessen
PAARE_DIAGRAMM = [
    ("Tasse 1", "Tasse 2"), ("Tasse 1", "Becher 3"), ("Tasse 2", "Becher 3"),
    ("Tasse 1", "Raumlinie"), ("Tasse 2", "Raumlinie"), ("Becher 3", "Raumlinie"),
    ("Tasse 1", "Rot"), ("Tasse 2", "Rot"), ("Becher 3", "Rot"),
    ("Becher 3", "Akzent"), ("Tasse 2", "Akzent"), ("Tasse 1", "Akzent"),
]

# ------------------------------------------------- Machado et al. (2009), Schweregrad 1,0
MACHADO = {
    "Protanopie": np.array([[0.152286, 1.052583, -0.204868],
                            [0.114503, 0.786281, 0.099216],
                            [-0.003882, -0.048116, 1.051998]]),
    "Deuteranopie": np.array([[0.367322, 0.860646, -0.227968],
                              [0.280085, 0.672501, 0.047413],
                              [-0.011820, 0.042940, 0.968881]]),
    "Tritanopie": np.array([[1.255528, -0.076749, -0.178779],
                            [-0.078411, 0.930809, 0.147602],
                            [0.004733, 0.691367, 0.303900]]),
}


def hex2rgb(h):
    h = h.lstrip("#")
    return np.array([int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4)])


def lin(c):
    """sRGB -> linear, Definition 'relative luminance' in WCAG 2.2."""
    c = np.asarray(c, dtype=float)
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def delin(c):
    c = np.clip(np.asarray(c, dtype=float), 0.0, 1.0)
    return np.where(c <= 0.0031308, 12.92 * c, 1.055 * c ** (1 / 2.4) - 0.055)


def lum_lin(rgb_lin):
    return float(0.2126 * rgb_lin[0] + 0.7152 * rgb_lin[1] + 0.0722 * rgb_lin[2])


def luminance(hexcol):
    return lum_lin(lin(hex2rgb(hexcol)))


def kontrast(l1, l2):
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def lin2lab(rgb_lin):
    m = np.array([[0.4124564, 0.3575761, 0.1804375],
                  [0.2126729, 0.7151522, 0.0721750],
                  [0.0193339, 0.1191920, 0.9503041]])
    xyz = m @ rgb_lin
    wp = np.array([0.95047, 1.0, 1.08883])
    t = xyz / wp
    d = 6 / 29
    f = np.where(t > d ** 3, np.cbrt(t), t / (3 * d * d) + 4 / 29)
    return np.array([116 * f[1] - 16, 500 * (f[0] - f[1]), 200 * (f[1] - f[2])])


def ciede2000(lab1, lab2):
    L1, a1, b1 = lab1
    L2, a2, b2 = lab2
    C1 = np.hypot(a1, b1)
    C2 = np.hypot(a2, b2)
    Cm = (C1 + C2) / 2
    G = 0.5 * (1 - np.sqrt(Cm ** 7 / (Cm ** 7 + 25 ** 7)))
    a1p, a2p = (1 + G) * a1, (1 + G) * a2
    C1p, C2p = np.hypot(a1p, b1), np.hypot(a2p, b2)
    h1p = np.degrees(np.arctan2(b1, a1p)) % 360
    h2p = np.degrees(np.arctan2(b2, a2p)) % 360
    dLp = L2 - L1
    dCp = C2p - C1p
    if C1p * C2p == 0:
        dhp = 0.0
    else:
        dh = h2p - h1p
        if dh > 180:
            dh -= 360
        elif dh < -180:
            dh += 360
        dhp = dh
    dHp = 2 * np.sqrt(C1p * C2p) * np.sin(np.radians(dhp / 2))
    Lpm = (L1 + L2) / 2
    Cpm = (C1p + C2p) / 2
    if C1p * C2p == 0:
        hpm = h1p + h2p
    else:
        if abs(h1p - h2p) <= 180:
            hpm = (h1p + h2p) / 2
        elif h1p + h2p < 360:
            hpm = (h1p + h2p + 360) / 2
        else:
            hpm = (h1p + h2p - 360) / 2
    T = (1 - 0.17 * np.cos(np.radians(hpm - 30)) + 0.24 * np.cos(np.radians(2 * hpm))
         + 0.32 * np.cos(np.radians(3 * hpm + 6)) - 0.20 * np.cos(np.radians(4 * hpm - 63)))
    dtheta = 30 * np.exp(-((hpm - 275) / 25) ** 2)
    Rc = 2 * np.sqrt(Cpm ** 7 / (Cpm ** 7 + 25 ** 7))
    Sl = 1 + 0.015 * (Lpm - 50) ** 2 / np.sqrt(20 + (Lpm - 50) ** 2)
    Sc = 1 + 0.045 * Cpm
    Sh = 1 + 0.015 * Cpm * T
    Rt = -np.sin(np.radians(2 * dtheta)) * Rc
    return float(np.sqrt((dLp / Sl) ** 2 + (dCp / Sc) ** 2 + (dHp / Sh) ** 2
                         + Rt * (dCp / Sc) * (dHp / Sh)))


def simuliere(hexcol, art):
    """Liefert linearisierte RGB-Werte der simulierten Farbe (None = normal)."""
    rl = lin(hex2rgb(hexcol))
    if art is None:
        return rl
    return np.clip(MACHADO[art] @ rl, 0.0, 1.0)


def to_hex(rgb_lin):
    s = delin(rgb_lin)
    return "#" + "".join(f"{int(round(v * 255)):02x}" for v in s)


def urteil(de):
    if de >= 20:
        return "gut"
    if de >= 10:
        return "Linienart noetig"
    return "VERWECHSELBAR"


def bericht(name, pal):
    print(f"\n==================== {name} ====================")
    print("\n1) Kontrast nach WCAG 2.2 (Text braucht 4,5:1 nach 1.4.3, "
          "Grafik/Bedienelement 3:1 nach 1.4.11)")
    print(f"{'Farbe':<11}{'Hex':<9}{'L_rel':>7}" + "".join(f"{k:>16}" for k in HINTERGRUENDE)
          + "   Urteil")
    for k, h in pal.items():
        L = luminance(h)
        ks = [kontrast(L, luminance(b)) for b in HINTERGRUENDE.values()]
        m = min(ks)
        u = "Text ok" if m >= 4.5 else ("nur Grafik" if m >= 3 else "ZU HELL")
        print(f"{k:<11}{h:<9}{L:7.4f}" + "".join(f"{x:15.2f}:1" for x in ks) + f"   {u}")

    print("\n2) Simulierte Farben (Machado 2009, Schweregrad 1,0)")
    arten = [None, "Protanopie", "Deuteranopie", "Tritanopie"]
    print(f"{'Farbe':<11}" + "".join(f"{(a or 'normal'):>14}" for a in arten))
    for k, h in pal.items():
        print(f"{k:<11}" + "".join(f"{to_hex(simuliere(h, a)):>14}" for a in arten))

    print("\n3) Farbabstand Delta E 00 (und Delta L*) der Diagramm-Paare")
    print(f"{'Paar':<24}" + "".join(f"{(a or 'normal'):>20}" for a in arten))
    for p, q in PAARE_DIAGRAMM:
        zeile = f"{p + ' / ' + q:<24}"
        for a in arten:
            l1 = lin2lab(simuliere(pal[p], a))
            l2 = lin2lab(simuliere(pal[q], a))
            de = ciede2000(l1, l2)
            dl = abs(l1[0] - l2[0])
            zeile += f"{de:7.1f} (dL {dl:4.1f}) {urteil(de)[:4]:>4}"
        print(zeile)

    print("\n4) Kontrast der Diagramm-Paare untereinander (fuer sich beruehrende Flaechen)")
    for p, q in PAARE_DIAGRAMM[:6]:
        print(f"{p + ' / ' + q:<24}{kontrast(luminance(pal[p]), luminance(pal[q])):6.2f}:1")


def selbsttest():
    """Bekannte Werte: Schwarz/Weiss 21:1; #767676 auf Weiss 4,54:1 (gaengiger
    Grenzwert fuer 4,5:1); #777777 auf Weiss knapp darunter (4,48:1);
    CIEDE2000-Pruefpaar 1 aus Sharma, Wu und Dalal (2005): 2,0425."""
    assert abs(kontrast(luminance("#000000"), luminance("#ffffff")) - 21.0) < 1e-9
    assert round(kontrast(luminance("#767676"), 1.0), 2) == 4.54
    assert round(kontrast(luminance("#777777"), 1.0), 2) == 4.48
    de = ciede2000(np.array([50.0, 2.6772, -79.7751]), np.array([50.0, 0.0, -82.7485]))
    assert abs(de - 2.0425) < 1e-3, de
    print("Selbsttest bestanden (21:1, 4,54:1, 4,48:1, CIEDE2000 2,0425).")


if __name__ == "__main__":
    selbsttest()
    bericht("HEUTIGE FARBEN", HEUTE)
    bericht("VORSCHLAG", VORSCHLAG)
    bericht("VERGLEICH: OKABE-ITO ABGEDUNKELT", OKABE_ITO_DUNKEL)
