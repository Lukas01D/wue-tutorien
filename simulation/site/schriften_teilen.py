# -*- coding: utf-8 -*-
"""Teilmengen der Schriften Fira Sans und Fira Math für die Kaffee-Seite (einmalig, Ergebnis liegt in src/schriften/).

Quelle: Schriftdateien des Lernzentrums v8 (dist/fonts/, SIL Open Font License 1.1, Lizenztexte liegen in src/schriften/).
Aufruf: python3 schriften_teilen.py <Ordner mit FiraSans-*.woff2 und FiraMath-Regular.woff2>
Der Bau (bauen.py) prüft, dass jedes Zeichen der Seite in der Teilmenge liegt.
"""
import os
import sys

from fontTools import subset

ZEICHEN_TEXT = ("U+0020-007E,U+00A0-00FF,U+0152-0153,U+02D9,U+0307,U+0391-03A9,U+03B1-03C9,U+03D1,U+03D5,U+2018-201E,U+2022,"
                "U+2026,U+2039-203A,U+2070,U+2074-208E,U+2190-2194,U+2212,U+2248,U+2264-2265")
ZEICHEN_MATHE = ("U+0020-007E,U+00B7,U+00D7,U+0307,U+0391-03A9,U+03B1-03C9,U+03D1,U+03D5,U+2192,U+2202,U+2211,U+2212,U+221E,"
                 "U+2248,U+2264-2265,U+1D400-1D433,U+1D434-1D467,U+1D468-1D49B")
DATEIEN = [("FiraSans-Regular.woff2", ZEICHEN_TEXT), ("FiraSans-SemiBold.woff2", ZEICHEN_TEXT), ("FiraSans-Bold.woff2", ZEICHEN_TEXT),
           ("FiraSans-Italic.woff2", ZEICHEN_TEXT), ("FiraMath-Regular.woff2", ZEICHEN_MATHE)]


def main(quelle):
    ziel = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src", "schriften")
    for name, zeichen in DATEIEN:
        aus = os.path.join(ziel, name.replace(".woff2", "-teil.woff2").replace("-Regular-teil", "-teil") if name.startswith("FiraMath")
                           else name.replace(".woff2", "-teil.woff2"))
        subset.main([os.path.join(quelle, name), "--unicodes=" + zeichen, "--flavor=woff2", "--layout-features=*",
                     "--no-hinting", "--desubroutinize", "--output-file=" + aus])
        print(aus, os.path.getsize(aus))


if __name__ == "__main__":
    main(sys.argv[1])
