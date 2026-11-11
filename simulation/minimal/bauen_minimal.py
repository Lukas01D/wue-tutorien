# -*- coding: utf-8 -*-
"""Bau der schlanken Kaffee-Seiten (Varianten A und B): Quellen in minimal/src -> Kaffee_Simulation_A.html und _B.html.

Aufruf: python3 simulation/minimal/bauen_minimal.py            (baut beide Seiten)
        python3 simulation/minimal/bauen_minimal.py --pruefen   (baut im Speicher und vergleicht mit den Dateien)

Rechenkern und Standardwerte: simulation/site/src/modell.js (unverändert eingebunden, wie auf der Hauptseite).
Schriften, Lizenzhinweis und CSP wie in simulation/site/bauen.py. Der Bau ist deterministisch.
"""
import base64
import hashlib
import os
import re
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HIER, "src")
SITE = os.path.join(HIER, "..", "site")
sys.path.insert(0, SITE)
import bauen as haupt  # noqa: E402  (Schriften, Lizenz, js_daten)

STAND = "2026-11-11"
VARIANTEN = ("A", "B")


def lies(pfad):
    with open(pfad, encoding="utf-8") as f:
        return f.read()


def pruefsumme():
    h = hashlib.sha256()
    for n in sorted(os.listdir(SRC)):
        h.update(n.encode() + b"\0" + open(os.path.join(SRC, n), "rb").read() + b"\0")
    for p in (os.path.join(SITE, "src", "modell.js"), os.path.abspath(__file__)):
        h.update(os.path.basename(p).encode() + b"\0" + open(p, "rb").read() + b"\0")
    return h.hexdigest()


def zeichen_pruefen(text):
    try:
        from fontTools.ttLib import TTFont
    except ImportError:
        return ["fontTools fehlt: Zeichenprüfung nicht ausgeführt"]
    schr = os.path.join(SITE, "src", "schriften")
    da = set(TTFont(os.path.join(schr, "PlexSans-400.woff2")).getBestCmap()) | set(TTFont(os.path.join(schr, "PlexMath.woff2")).getBestCmap())
    da |= set(TTFont(os.path.join(schr, "PlexMono-400.woff2")).getBestCmap())
    return ["Zeichen U+%04X (%s) fehlt in der Schrift" % (ord(c), c) for c in sorted(set(re.findall(r"[^\x00-\x7f]", text))) if ord(c) not in da]


def bauen(variante):
    summe = pruefsumme()
    js = "\n".join([
        "// Kaffee mit Milch: Simulation, schlanke Variante %s. Gebaut mit simulation/minimal/bauen_minimal.py (Stand %s, Quellen %s)." % (variante, STAND, summe[:10]),
        lies(os.path.join(SITE, "src", "modell.js")).strip(),
        haupt.js_daten("BAU", {"stand": STAND, "version": summe[:10]}),
        'const VARIANTE = "%s";' % variante,
        lies(os.path.join(SRC, "minimal.js")).strip()]) + "\n"
    if "</script" in js.lower():
        raise haupt.BauFehler("</script im Skript")
    css = lies(os.path.join(SRC, "minimal.css")).replace("{{FONTS}}", haupt.schriften_css()).rstrip() + "\n" + haupt.lizenz_kommentar() + "\n"
    h = lambda s: "'sha256-" + base64.b64encode(hashlib.sha256(s.encode("utf-8")).digest()).decode("ascii") + "'"
    csp = ("default-src 'none'; script-src %s; style-src %s; font-src data:; img-src data:; base-uri 'none'; form-action 'none'"
           % (h(js), h(css)))
    vorlage = lies(os.path.join(SRC, "vorlage.html"))
    if re.search(r"\sstyle\s*=", vorlage) or re.search(r"\son[a-z]+\s*=", vorlage):
        raise haupt.BauFehler("Vorlage: style= oder on...= (CSP)")
    seite = vorlage.replace("{{CSP}}", csp).replace("{{CSS}}", css).replace("{{JS}}", js).replace("{{VARIANTE}}", variante)
    return seite.encode("utf-8"), zeichen_pruefen(lies(os.path.join(SRC, "minimal.js")) + vorlage)


def main():
    pruefen = "--pruefen" in sys.argv
    gleich = True
    for v in VARIANTEN:
        seite, warn = bauen(v)
        for w in warn:
            print("WARNUNG:", w)
        ziel = os.path.join(HIER, "Kaffee_Simulation_%s.html" % v)
        if pruefen:
            alt = open(ziel, "rb").read() if os.path.exists(ziel) else b""
            gleich &= alt == seite
        else:
            with open(ziel, "wb") as f:
                f.write(seite)
            print("Variante %s: %d Bytes, SHA-256 %s" % (v, len(seite), hashlib.sha256(seite).hexdigest()))
    if pruefen:
        print("gleich" if gleich else "VERSCHIEDEN")
        sys.exit(0 if gleich else 1)


if __name__ == "__main__":
    main()
