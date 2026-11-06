# -*- coding: utf-8 -*-
"""Schriften der drei Gestaltungsentwürfe: feste Schnitte aus den freien Quelldateien, gekürzt auf die gebrauchten Zeichen.

Quellen (alle SIL Open Font License 1.1, Lizenztexte werden mitkopiert):
  Google-Fonts-Repository  https://raw.githubusercontent.com/google/fonts/main/ofl/<familie>/
  IBM-Plex-Repository      https://raw.githubusercontent.com/IBM/plex/master/packages/plex-math/
Aufruf: python3 simulation/design_entwuerfe/schriften_teilen.py <ordner mit den heruntergeladenen Quelldateien>

Zeichenmenge: alle Zeichen der fertigen Texte (DE und EN, nach dem Bau von simulation/site/bauen.py) außerhalb von Formeln,
alle Nicht-ASCII-Zeichen der Skripte, druckbares ASCII. Formelschriften zusätzlich: Zeichen in Formeln und die
kursiven Formen der einzeln gesetzten Buchstaben (MathML setzt ein einzelnes <mi> über U+1D434 ff. kursiv). Bei Formelschriften
bleibt nur das Merkmal ssty (Hoch- und Tiefstellung) samt der MATH-Tabelle; das spart bei IBM Plex Math zwei Drittel.
"""
import os
import re
import shutil
import sys

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

HIER = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(os.path.dirname(HIER), "site")
sys.path.insert(0, SITE)
import bauen  # noqa: E402

# Entwurf -> Liste (Zieldatei, Quelldatei, Achsen für feste Schnitte oder None, Art "text"/"mathe", Lizenzdatei)
ENTWUERFE = {
    "messprotokoll": [
        ("PlexSans-400.woff2", "IBMPlexSans-var.ttf", {"wght": 400, "wdth": 100}, "text", "IBMPlexSans-OFL.txt"),
        ("PlexSans-600.woff2", "IBMPlexSans-var.ttf", {"wght": 600, "wdth": 100}, "text", None),
        ("PlexSans-400i.woff2", "IBMPlexSans-Italic-var.ttf", {"wght": 400, "wdth": 100}, "text", None),
        ("PlexMono-400.woff2", "IBMPlexMono-Regular.ttf", None, "text", "IBMPlexMono-OFL.txt"),
        ("PlexMono-600.woff2", "IBMPlexMono-SemiBold.ttf", None, "text", None),
        ("PlexMath.woff2", "IBMPlexMath-Regular.otf", None, "mathe", "IBMPlexMath-OFL.txt"),
    ],
    "kaffeehaus": [
        ("Fraunces-600.woff2", "Fraunces-var.ttf", {"wght": 600, "opsz": 48, "SOFT": 50, "WONK": 0}, "text", "Fraunces-OFL.txt"),
        ("SourceSans3-400.woff2", "SourceSans3-var.ttf", {"wght": 400}, "text", "SourceSans3-OFL.txt"),
        ("SourceSans3-600.woff2", "SourceSans3-var.ttf", {"wght": 600}, "text", None),
        ("SourceSans3-400i.woff2", "SourceSans3-Italic-var.ttf", {"wght": 400}, "text", None),
        ("STIXTwoMath.woff2", "STIXTwoMath-Regular.ttf", None, "mathe", "STIXTwoMath-OFL.txt"),
    ],
    "hoersaal": [
        ("Atkinson-400.woff2", "AtkinsonNext-var.ttf", {"wght": 400}, "text", "AtkinsonNext-OFL.txt"),
        ("Atkinson-700.woff2", "AtkinsonNext-var.ttf", {"wght": 700}, "text", None),
        ("Atkinson-400i.woff2", "AtkinsonNext-Italic-var.ttf", {"wght": 400}, "text", None),
        # Formeln: Fira Math wie im gebauten Stand (Teilmenge liegt schon in simulation/site/src/schriften/)
    ],
}
MATHE_ZUSATZ = "U+0020-007E,U+00B7,U+00D7,U+0307,U+2192,U+2202,U+2211,U+2212,U+221E,U+2248,U+2264-2265"


def kursiv(c):
    """Mathematisch kursive Form eines Buchstabens, wie MathML ein einzelnes <mi> darstellt."""
    o = ord(c)
    if c == "h":
        return "\u210e"
    if 65 <= o <= 90:
        return chr(0x1D434 + o - 65)
    if 97 <= o <= 122:
        return chr(0x1D44E + o - 97)
    if 0x3B1 <= o <= 0x3C9:
        return chr(0x1D6FC + o - 0x3B1)
    return {"\u03d1": "\U0001d717", "\u03d5": "\U0001d719"}.get(c, c)


def zeichenmengen():
    _, texte = bauen.texte_bauen()
    text, mathe = set(chr(c) for c in range(0x20, 0x7f)), set()
    regler = bauen.regler_bauen()
    quellen = [t for s in bauen.SPRACHEN for t in texte[s].values()] + [r["mathml"] for r in regler["regler"]]
    text |= set(re.sub(r"<[^>]+>", " ", bauen.lies("regler.json")))
    for t in quellen:
        for m in re.findall(r"<mi>([^<]*)</mi>", t):
            if len(m) == 1:
                mathe.add(kursiv(m))
    for t in quellen:
        for m in re.findall(r"<math.*?</math>", t, flags=re.S):
            mathe |= set(re.sub(r"<[^>]+>", "", m))
        text |= set(re.sub(r"<[^>]+>", " ", re.sub(r"<math.*?</math>", " ", t, flags=re.S)))
    for n in ("oberflaeche.js", "hilfen.js", "erweiterung.js", "modell.js"):
        text |= set(re.findall(r"[^\x00-\x7f]", open(os.path.join(SITE, "src", n), encoding="utf-8").read()))
    text |= set("   ✓→←…·×−")       # Leerzeichenarten und Zeichen der Entwurfs-CSS (content)
    for z in ("\n", "\r", "\t"):
        text.discard(z)
    return text, mathe


def main(quelle):
    text, mathe = zeichenmengen()
    uni_text = ",".join("U+%04X" % ord(c) for c in sorted(text))
    uni_mathe = ",".join("U+%04X" % ord(c) for c in sorted(mathe | text)) + "," + MATHE_ZUSATZ
    print("Zeichen Text:", len(text), "Formel:", len(mathe))
    for name, dateien in ENTWUERFE.items():
        ziel = os.path.join(HIER, name, "src", "schriften")
        os.makedirs(ziel, exist_ok=True)
        summe = 0
        for aus, ein, achsen, art, lizenz in dateien:
            f = TTFont(os.path.join(quelle, ein))
            if achsen is not None:
                f = instancer.instantiateVariableFont(f, achsen, updateFontNames=False)
            tmp = os.path.join(ziel, "_tmp.ttf")
            f.save(tmp)
            subset.main([tmp, "--unicodes=" + (uni_mathe if art == "mathe" else uni_text), "--flavor=woff2",
                         "--layout-features=" + ("ssty" if art == "mathe" else "*"), "--no-hinting", "--desubroutinize", "--name-IDs=*", "--output-file=" + os.path.join(ziel, aus)])
            os.remove(tmp)
            if lizenz:
                shutil.copy(os.path.join(quelle, lizenz), os.path.join(ziel, lizenz))
            g = os.path.getsize(os.path.join(ziel, aus)); summe += g
            print("  %-14s %-24s %7d Bytes" % (name, aus, g))
        print("  %-14s %-24s %7d Bytes (base64 etwa %d)" % (name, "zusammen", summe, summe * 4 // 3))


if __name__ == "__main__":
    main(sys.argv[1])
