# -*- coding: utf-8 -*-
"""Bau der schlanken Kaffee-Seite: minimal/src -> Kaffee_Simulation_schlank.html.

Aufruf: python3 simulation/minimal/bauen_minimal.py            (baut)
        python3 simulation/minimal/bauen_minimal.py --pruefen   (baut im Speicher und vergleicht mit der Datei)

Damit die Seite aussieht und rechnet wie die Hauptseite, übernimmt der Bau unverändert aus simulation/site/src:
modell.js (Rechenkern), stil.css (Optik), texte_de.txt und texte_en.txt (Texte) und aus oberflaeche.js die Bausteine
für Regler, Diagramm, Kasten und Säulen (Liste BAUSTEINE). Eigene Teile: src/vorlage.html, src/schlank.js,
src/schlank.css und die wenigen zusätzlichen Texte in src/texte_schlank_*.txt. Der Bau ist deterministisch.
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
import bauen as haupt  # noqa: E402
import tex2mathml  # noqa: E402

STAND = "2026-11-11"
ZIEL = os.path.join(HIER, "Kaffee_Simulation_schlank.html")
BAUSTEINE = ["T", "F", "zahl", "liesZahl", "textOhneTags", "el", "zeichne", "imBild", "saeulen", "begrenze",
             "reglerBauen", "reglerTexte", "setze", "reglerAnzeigen", "istBlatt", "kern", "ansage"]
# Einzige Änderung an einem Baustein: Maßstab der Säulen aus den Werten bei der Zugabe, damit sie beim Abspielen wachsen
ERSATZ = {"saeulen": [("max = Math.max(erg.Q1, erg.Q2, 1e-9)", "max = Math.max(erg.Q1max, erg.Q2max, 1e-9)")]}
# Achsen der Hauptseite, die zeitDarstellen in schlank.js nachbildet; ändern sie sich dort, bricht der Bau ab
ACHSEN = ["const xmax = Math.max(60, Math.ceil(e.tZ / 10) * 10);", "const Lr = 46, R = 24, Tr = 12, B = 38, P = 12;",
          "const X = t => Lr + P + (W - Lr - P - R) * t / xmax, Y = v => Tr + (H - Tr - B) * (ymax - v) / (ymax - ymin);"]


def lies(pfad):
    with open(pfad, encoding="utf-8") as f:
        return f.read()


def baustein(quelle, name):
    """Holt eine Funktion oder Konstante der obersten Ebene (zwei Leerzeichen Einzug) aus oberflaeche.js."""
    m = re.search(r"\n(  (?:function %s\(|const %s = ))" % (re.escape(name), re.escape(name)), quelle)
    if not m:
        raise haupt.BauFehler("Baustein fehlt in oberflaeche.js: " + name)
    start = m.start(1)
    zeile = quelle[start:quelle.index("\n", start)]
    kopf = re.sub(r"\s+//[^\"']*$", "", zeile).rstrip()        # Kommentar am Zeilenende zählt nicht
    if kopf.endswith("{") or kopf.endswith("["):
        ende = re.compile(r"\n  [}\]];?\n").search(quelle, start)
        return quelle[start:ende.end() - 1]
    return zeile


def texte():
    _, fertig = haupt.texte_bauen()
    for s in haupt.SPRACHEN:
        k = None
        for zeile in lies(os.path.join(SRC, "texte_schlank_%s.txt" % s)).split("\n"):
            if zeile.startswith("#") or not zeile.strip():
                continue
            if zeile.startswith("@"):
                k = zeile[1:].strip()
                if k in fertig[s]:
                    raise haupt.BauFehler("Schlüssel schon in den Haupttexten: " + k)
                fertig[s][k] = ""
                continue
            t = tex2mathml.ersetze_formeln(zeile.strip())
            if "$" in t or "\u2013" in t or "\u2014" in t:
                raise haupt.BauFehler("%s/%s: $ oder Gedankenstrich" % (s, k))
            fertig[s][k] = (fertig[s][k] + " " + t).strip()
    if set(fertig["de"]) != set(fertig["en"]):
        raise haupt.BauFehler("Schlüssel nur in einer Sprache")
    return fertig


def pruefsumme():
    h = hashlib.sha256()
    for n in sorted(os.listdir(SRC)):
        h.update(n.encode() + b"\0" + open(os.path.join(SRC, n), "rb").read() + b"\0")
    for n in ("modell.js", "oberflaeche.js", "stil.css", "texte_de.txt", "texte_en.txt"):
        h.update(n.encode() + b"\0" + open(os.path.join(SITE, "src", n), "rb").read() + b"\0")
    h.update(b"bauen_minimal.py\0" + open(os.path.abspath(__file__), "rb").read())
    return h.hexdigest()


def bauen():
    ober = lies(os.path.join(SITE, "src", "oberflaeche.js"))
    zeichne = baustein(ober, "zeichne")
    for a in ACHSEN:
        if a not in zeichne:
            raise haupt.BauFehler("Achsen der Hauptseite geändert, zeitDarstellen anpassen: " + a)
    teile = []
    for n in BAUSTEINE:
        b = baustein(ober, n)
        for alt, neu in ERSATZ.get(n, []):
            if b.count(alt) != 1:
                raise haupt.BauFehler("Ersatz in %s nicht genau einmal: %s" % (n, alt))
            b = b.replace(alt, neu)
        teile.append("  // aus oberflaeche.js: %s\n%s" % (n, b))
    eigen = lies(os.path.join(SRC, "schlank.js"))
    for platz in ("//@@REGLER@@", "//@@BAUSTEINE@@"):
        if eigen.count(platz) != 1:
            raise haupt.BauFehler("schlank.js: Platzhalter " + platz)
    eigen = eigen.replace("  //@@REGLER@@", "  // aus oberflaeche.js: REGLER\n" + baustein(ober, "REGLER"))
    eigen = eigen.replace("  //@@BAUSTEINE@@", "\n\n".join(teile))
    summe = pruefsumme()
    js = "\n".join([
        "// Kaffee mit Milch: Simulation, schlanke Seite. Gebaut mit simulation/minimal/bauen_minimal.py (Stand %s, Quellen %s)." % (STAND, summe[:10]),
        lies(os.path.join(SITE, "src", "modell.js")).strip(),
        haupt.js_daten("TEXTE", texte()),
        haupt.js_daten("BAU", {"stand": STAND, "version": summe[:10]}),
        eigen.strip()]) + "\n"
    if "</script" in js.lower():
        raise haupt.BauFehler("</script im Skript")
    css = (lies(os.path.join(SITE, "src", "stil.css")).replace("{{FONTS}}", haupt.schriften_css()).rstrip() + "\n"
           + lies(os.path.join(SRC, "schlank.css")).rstrip() + "\n" + haupt.lizenz_kommentar() + "\n")
    h = lambda s: "'sha256-" + base64.b64encode(hashlib.sha256(s.encode("utf-8")).digest()).decode("ascii") + "'"
    csp = ("default-src 'none'; script-src %s; style-src %s; font-src data:; img-src data:; base-uri 'none'; form-action 'none'"
           % (h(js), h(css)))
    vorlage = lies(os.path.join(SRC, "vorlage.html"))
    if re.search(r"\sstyle\s*=", vorlage) or re.search(r"\son[a-z]+\s*=", vorlage):
        raise haupt.BauFehler("Vorlage: style= oder on...= (CSP)")
    return vorlage.replace("{{CSP}}", csp).replace("{{CSS}}", css).replace("{{JS}}", js).encode("utf-8")


def main():
    seite = bauen()
    if "--pruefen" in sys.argv:
        alt = open(ZIEL, "rb").read() if os.path.exists(ZIEL) else b""
        print("gleich" if alt == seite else "VERSCHIEDEN")
        sys.exit(0 if alt == seite else 1)
    with open(ZIEL, "wb") as f:
        f.write(seite)
    print("%d Bytes, SHA-256 %s" % (len(seite), hashlib.sha256(seite).hexdigest()))


if __name__ == "__main__":
    main()
