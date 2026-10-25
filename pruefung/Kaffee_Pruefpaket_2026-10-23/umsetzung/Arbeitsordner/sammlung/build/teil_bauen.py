# -*- coding: utf-8 -*-
"""Baut eine einzelne Teildatei der Sammlung zur Sichtprüfung als PDF und als Seitenbilder (PNG).

Aufruf: python3 teil_bauen.py <teil.md> <ausgabeordner>
Ergebnis: <ausgabeordner>/<name>.pdf und <ausgabeordner>/<name>-<seite>.png (70 dpi, zum Ansehen)
und <ausgabeordner>/<name>_gross-<seite>.png (110 dpi, für Details).
"""
import os, sys, subprocess, tempfile

HIER = os.path.dirname(os.path.abspath(__file__))
SAMMLUNG = os.path.dirname(HIER)


def main():
    teil = os.path.abspath(sys.argv[1])
    aus = os.path.abspath(sys.argv[2])
    os.makedirs(aus, exist_ok=True)
    name = os.path.splitext(os.path.basename(teil))[0]
    with open(teil, encoding="utf-8") as f:
        text = f.read()
    kopf = "---\nlang: de\n---\n\n"
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8", dir=aus) as tmp:
        tmp.write(kopf + text)
        tmpname = tmp.name
    pdf = os.path.join(aus, name + ".pdf")
    subprocess.run(["pandoc", tmpname, "-o", pdf, "--pdf-engine=xelatex",
                    "-H", os.path.join(HIER, "kopf.tex"), "--lua-filter", os.path.join(HIER, "lehrstuhl.lua"),
                    "-V", "documentclass=article", "-V", "fontsize=11pt", "-V", "mainfont=Carlito",
                    "-V", "mathfont=Latin Modern Math", "--resource-path", SAMMLUNG], check=True)
    os.remove(tmpname)
    subprocess.run(["pdftoppm", "-r", "70", "-png", pdf, os.path.join(aus, name)], check=True)
    subprocess.run(["pdftoppm", "-r", "110", "-png", pdf, os.path.join(aus, name + "_gross")], check=True)
    print("PDF:", pdf)


if __name__ == "__main__":
    main()
