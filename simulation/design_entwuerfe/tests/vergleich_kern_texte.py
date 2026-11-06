# -*- coding: utf-8 -*-
"""Belegt „nur die Gestaltung ändert sich“: Rechenkern (MODELL, ERWEITERUNG, HILFEN), Texte (TEXTE) und Regeldaten (REGLER_DEF)
im Skript jeder Entwurfsseite sind bytegleich mit dem gebauten Stand simulation/site/index.html. Das Oberflächenskript darf
sich nur an den Stellen aus gestaltung_patch.py unterscheiden (geprüft: rückgängig gemacht ergibt es den Stand).
Aufruf: python3 simulation/design_entwuerfe/tests/vergleich_kern_texte.py
"""
import os
import re
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
ENTW = os.path.dirname(HIER)
SIM = os.path.dirname(ENTW)
sys.path.insert(0, ENTW)
import gestaltung_patch  # noqa: E402


def teile(pfad):
    html = open(pfad, encoding="utf-8").read()
    js = re.search(r"<script>(.*)</script>", html, flags=re.S).group(1)
    i_texte = js.index("const TEXTE = ")
    i_oberfl = js.index("// OBERFLAECHE:")
    kopf_ende = js.index("\n") + 1                      # erste Zeile: Bauvermerk mit Stand und Prüfsumme (unterscheidet sich gewollt)
    return {"Rechenkern (modell.js, erweiterung.js, hilfen.js)": js[kopf_ende:i_texte],
            "Texte und Regeldaten (TEXTE, REGLER_DEF)": re.sub(r"const BAU = \{[^\n]*\};\n", "", js[i_texte:i_oberfl]),
            "Oberfläche": js[i_oberfl:]}


def main():
    soll = teile(os.path.join(SIM, "site", "index.html"))
    gesamt = True
    zeilen = []
    for name in ("messprotokoll", "kaffeehaus", "hoersaal"):
        ist = teile(os.path.join(ENTW, name, "index.html"))
        for k in soll:
            if k == "Oberfläche":
                ok = ist[k] == gestaltung_patch.anwenden(soll[k])
                art = "gleich dem Stand mit gestaltung_patch.py"
            else:
                ok = ist[k] == soll[k]
                art = "bytegleich"
            gesamt &= ok
            zeilen.append(("ok    " if ok else "FEHLT ") + name + ": " + k + " " + art + " (" + str(len(ist[k])) + " Zeichen)")
    zeilen.append("\nErgebnis: " + ("alle gleich" if gesamt else "ABWEICHUNG"))
    print("\n".join(zeilen))
    return 0 if gesamt else 1


if __name__ == "__main__":
    sys.exit(main())
