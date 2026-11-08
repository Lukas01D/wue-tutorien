# -*- coding: utf-8 -*-
"""Schriften der Kaffee-Seite Fassung 3 (IBM Plex, Optik von Entwurf A): feste Schnitte, gekürzt auf die gebrauchten Zeichen.

Quellen (SIL Open Font License 1.1, Lizenztexte werden mitkopiert):
  https://raw.githubusercontent.com/google/fonts/main/ofl/ibmplexsans/IBMPlexSans%5Bwdth,wght%5D.ttf  (als IBMPlexSans-var.ttf), OFL.txt
  https://raw.githubusercontent.com/google/fonts/main/ofl/ibmplexmono/IBMPlexMono-Regular.ttf, -SemiBold.ttf, OFL.txt
  https://raw.githubusercontent.com/IBM/plex/master/packages/plex-math/fonts/complete/otf/IBMPlexMath-Regular.otf, LICENSE.txt
Aufruf: python3 simulation/site/schriften_teilen.py <ordner mit den heruntergeladenen Quelldateien>; danach bauen.py.

Zeichenmenge: alle Zeichen der fertigen Texte (DE und EN) außerhalb von Formeln, alle Nicht-ASCII-Zeichen von Skript und Vorlage,
druckbares ASCII. Plex Math zusätzlich: alle Textzeichen (Ersatz im Schriftstapel, z. B. für ○ □ ● ■ und ϑ), Zeichen in Formeln
und die kursiven Formen der einzeln gesetzten Buchstaben (MathML setzt ein einzelnes <mi> über U+1D434 ff. kursiv). Bei Plex Math
bleibt nur das Merkmal ssty (Hoch- und Tiefstellung) samt der MATH-Tabelle.
"""
import os
import re
import shutil
import sys

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
import bauen  # noqa: E402

DATEIEN = [  # (Ziel, Quelle, Achsen oder None, Art, Lizenz (Quelle, Ziel))
    ("PlexSans-400.woff2", "IBMPlexSans-var.ttf", {"wght": 400, "wdth": 100}, "text", ("IBMPlexSans-OFL.txt", "IBMPlexSans-OFL.txt")),
    ("PlexSans-600.woff2", "IBMPlexSans-var.ttf", {"wght": 600, "wdth": 100}, "text", None),
    ("PlexMono-400.woff2", "IBMPlexMono-Regular.ttf", None, "text", ("IBMPlexMono-OFL.txt", "IBMPlexMono-OFL.txt")),
    ("PlexMono-600.woff2", "IBMPlexMono-SemiBold.ttf", None, "text", None),
    ("PlexMath.woff2", "IBMPlexMath-Regular.otf", None, "mathe", ("LICENSE.txt", "IBMPlexMath-OFL.txt")),
]
MATHE_ZUSATZ = "U+0020-007E,U+00B7,U+00D7,U+0307,U+2192,U+2202,U+2211,U+2212,U+221E,U+2248,U+2264-2265"


def kursiv(c):
    o = ord(c)
    if c == "h":
        return "ℎ"
    if 65 <= o <= 90:
        return chr(0x1D434 + o - 65)
    if 97 <= o <= 122:
        return chr(0x1D44E + o - 97)
    if 0x3B1 <= o <= 0x3C9:
        return chr(0x1D6FC + o - 0x3B1)
    return {"ϑ": "\U0001d717", "ϕ": "\U0001d719"}.get(c, c)


def zeichenmengen():
    _, texte = bauen.texte_bauen()
    text, mathe = set(chr(c) for c in range(0x20, 0x7f)), set()
    quellen = [t for s in bauen.SPRACHEN for t in texte[s].values()]
    vorlage = bauen.lies("vorlage.html")
    quellen.append(vorlage)
    for t in quellen:
        for m in re.findall(r"<mi[^>]*>([^<]*)</mi>", t):
            if len(m) == 1:
                mathe.add(kursiv(m))
        for m in re.findall(r"<math.*?</math>", t, flags=re.S):
            mathe |= set(re.sub(r"<[^>]+>", "", m))
        text |= set(re.sub(r"<[^>]+>", " ", re.sub(r"<math.*?</math>", " ", t, flags=re.S)))
    for n in ("oberflaeche.js", "modell.js"):
        text |= set(re.findall(r"[^\x00-\x7f]", bauen.lies(n)))
    text |= set("  ")
    for z in ("\n", "\r", "\t"):
        text.discard(z)
    return text, mathe


def main(quelle):
    text, mathe = zeichenmengen()
    uni_text = ",".join("U+%04X" % ord(c) for c in sorted(text))
    uni_mathe = ",".join("U+%04X" % ord(c) for c in sorted(mathe | text)) + "," + MATHE_ZUSATZ
    print("Zeichen Text:", len(text), "Formel:", len(mathe))
    ziel = os.path.join(HIER, "src", "schriften")
    summe = 0
    for aus, ein, achsen, art, lizenz in DATEIEN:
        f = TTFont(os.path.join(quelle, ein))
        if achsen is not None:
            f = instancer.instantiateVariableFont(f, achsen, updateFontNames=False)
        tmp = os.path.join(ziel, "_tmp.ttf")
        f.save(tmp)
        subset.main([tmp, "--unicodes=" + (uni_mathe if art == "mathe" else uni_text), "--flavor=woff2",
                     "--layout-features=" + ("ssty" if art == "mathe" else "kern,liga,tnum"), "--no-hinting", "--desubroutinize",
                     "--name-IDs=*", "--output-file=" + os.path.join(ziel, aus)])
        os.remove(tmp)
        if lizenz:
            shutil.copy(os.path.join(quelle, lizenz[0]), os.path.join(ziel, lizenz[1]))
        g = os.path.getsize(os.path.join(ziel, aus))
        summe += g
        print("  %-20s %7d Bytes" % (aus, g))
    print("  zusammen %d Bytes (base64 etwa %d)" % (summe, summe * 4 // 3))


if __name__ == "__main__":
    main(sys.argv[1])
