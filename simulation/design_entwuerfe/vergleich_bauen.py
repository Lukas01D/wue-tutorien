# -*- coding: utf-8 -*-
"""Baut simulation/design_entwuerfe/VERGLEICH.html: alle vier Fassungen nebeneinander je Zustand, Bilder eingebettet (offline lesbar).

Quelle der Bilder: <fassung>/bilder/*.jpg aus bilder_entwurf.js (Gerätefaktor 2). Für die Vergleichsseite werden sie verkleinert
(Handy 585 px, Laptop und Beamer 1366 px breit) und als WebP (Qualität 78) eingebettet; die Originale bleiben in bilder/.
Aufruf: python3 simulation/design_entwuerfe/vergleich_bauen.py
"""
import base64
import html
import io
import os

from PIL import Image

HIER = os.path.dirname(os.path.abspath(__file__))
FASSUNGEN = [
    ("variante_0", "Variante 0: heutiger Stand", "Stand da7deb1, wie gebaut (Fira Sans, Fira Math)."),
    ("messprotokoll", "A Messprotokoll", "Papier, Tinte, Millimeterraster, nummerierte Schritte; IBM Plex Sans, Plex Mono, Plex Math."),
    ("kaffeehaus", "B Kaffeehaus", "Milchschaum, Crema, Espresso, große weiche Karten, Mittelspalte; Fraunces, Source Sans 3, STIX Two Math."),
    ("hoersaal", "C Hörsaal", "Weiß, Schwarz, Signalblau, große Schrift und Ziele, Schrittleiste; Atkinson Hyperlegible Next, Fira Math."),
]
ZUSTAENDE = [
    ("1_startkarte", "Startkarte"),
    ("2_nach_vorhersage", "Nach der Vorhersage, mit Diagramm"),
    ("3_frage1_regler", "Frage 1 mit Regler (Vorhersage 50 min, Zugabe 56 min)"),
    ("4_vertiefung", "Vertiefung geöffnet"),
    ("5_startkarte_en", "Englische Startkarte"),
]


def einbetten(pfad, breite):
    if not os.path.exists(pfad):
        return None
    b = Image.open(pfad).convert("RGB")
    if b.width > breite:
        b = b.resize((breite, round(b.height * breite / b.width)), Image.LANCZOS)
    puf = io.BytesIO()
    b.save(puf, "WEBP", quality=78, method=6)
    return "data:image/webp;base64," + base64.b64encode(puf.getvalue()).decode("ascii"), b.width, b.height


def bild(fassung, datei, breite, alt):
    r = einbetten(os.path.join(HIER, fassung, "bilder", datei), breite)
    if r is None:
        return '<p class="fehlt">Bild fehlt: %s</p>' % html.escape(datei)
    src, w, h = r
    return '<img src="%s" width="%d" height="%d" alt="%s" loading="lazy">' % (src, w, h, html.escape(alt))


def reihe(zustand_datei, titel, breite, art):
    zellen = []
    for ordner, name, _ in FASSUNGEN:
        zellen.append('<figure>%s<figcaption>%s</figcaption></figure>' % (
            bild(ordner, zustand_datei, breite, name + ": " + titel), html.escape(name)))
    return '<div class="reihe %s">%s</div>' % (art, "".join(zellen))


def main():
    teile = []
    nav = []
    for schluessel, titel in ZUSTAENDE:
        anker = schluessel
        nav.append('<li><a href="#%s">%s</a></li>' % (anker, html.escape(titel)))
        teile.append('<section id="%s"><h2>%s</h2><h3>Handy 390 × 844</h3>%s<h3>Laptop 1366 × 768</h3>%s</section>' % (
            anker, html.escape(titel), reihe(schluessel + "_390x844.jpg", titel + ", Handy", 585, "handy"),
            reihe(schluessel + "_1366x768.jpg", titel + ", Laptop", 1366, "breit")))
    nav.append('<li><a href="#6_beamer">Beamer nach der Vorhersage</a></li>')
    teile.append('<section id="6_beamer"><h2>Beamer 1280 × 720 nach der Vorhersage</h2>%s</section>' % reihe(
        "6_beamer_nach_vorhersage_1280x720.jpg", "Beamer nach der Vorhersage", 1280, "breit"))
    legende = "".join('<li><b>%s</b> %s</li>' % (html.escape(n), html.escape(t)) for _, n, t in FASSUNGEN)
    seite = """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Gestaltungsvergleich Kaffee-Simulation</title>
<style>
:root { --grund: #f7f7f5; --karte: #ffffff; --text: #1d1f23; --leise: #4d525b; --linie: #d9d9d4; --akzent: #1f4f8f; }
* { box-sizing: border-box; }
body { margin: 0; background: var(--grund); color: var(--text); font: 16px/1.5 system-ui, -apple-system, "Segoe UI", sans-serif; }
header { padding: 20px 16px 8px; max-width: 1800px; margin: 0 auto; }
h1 { font-size: 1.5rem; margin: 0 0 6px; }
h2 { font-size: 1.25rem; margin: 0 0 4px; padding-top: 12px; border-top: 2px solid var(--text); }
h3 { font-size: .95rem; margin: 14px 0 8px; color: var(--leise); font-weight: 600; }
p { margin: 0 0 8px; max-width: 70em; }
ul.legende { margin: 8px 0; padding-left: 1.2em; }
nav ol { display: flex; flex-wrap: wrap; gap: 6px 14px; padding: 0; margin: 10px 0 0; list-style: none; }
nav a { color: var(--akzent); }
main { max-width: 1800px; margin: 0 auto; padding: 0 16px 40px; }
section { margin-top: 26px; }
.reihe { display: grid; gap: 12px; }
.reihe.handy { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.reihe.breit { grid-template-columns: repeat(2, minmax(0, 1fr)); }
@media (max-width: 900px) { .reihe.handy { grid-template-columns: repeat(2, minmax(0, 1fr)); } .reihe.breit { grid-template-columns: 1fr; } }
figure { margin: 0; background: var(--karte); border: 1px solid var(--linie); border-radius: 6px; padding: 6px; min-width: 0; }
figure img { display: block; width: 100%; height: auto; border-radius: 3px; }
figcaption { font-weight: 600; font-size: .9rem; padding: 6px 2px 0; }
.fehlt { color: #a3261b; font-weight: 600; }
a:focus-visible { outline: 3px solid var(--akzent); outline-offset: 2px; }
</style>
</head>
<body>
<header>
<h1>Gestaltungsvergleich: Kaffee mit Milch</h1>
<p>Vier Fassungen derselben Seite in denselben Zuständen, aufgenommen mit Chromium (Playwright) bei Gerätefaktor 2, Bildschirmausschnitt.
Bedienfolge: Vorhersage „Tasse 1, etwa 4 K“; für Frage 1 „50 min“, dann Zugabe 56 min. Bericht: <code>simulation/DESIGN_ENTWUERFE.md</code>.</p>
<ul class="legende">%s</ul>
<nav aria-label="Zustände"><ol>%s</ol></nav>
</header>
<main>
%s
</main>
</body>
</html>
""" % (legende, "".join(nav), "\n".join(teile))
    ziel = os.path.join(HIER, "VERGLEICH.html")
    with open(ziel, "w", encoding="utf-8") as f:
        f.write(seite)
    print("VERGLEICH.html: %d Bytes" % os.path.getsize(ziel))


if __name__ == "__main__":
    main()
