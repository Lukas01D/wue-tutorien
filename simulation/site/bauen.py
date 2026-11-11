# -*- coding: utf-8 -*-
"""Bau der Kaffee-Seite, Fassung 3 (KONZEPT_F3.md): Quellen in src/ -> index.html und bytegleich Kaffee_Simulation.html.

Aufruf: python3 simulation/site/bauen.py         (baut, prüft, schreibt BAUNACHWEIS.txt)
        python3 simulation/site/bauen.py --pruefen   (baut nur im Speicher und vergleicht mit index.html)
        python3 simulation/site/bauen.py --ziel <ordner>   (Probebau in einen anderen Ordner)

Schritte: Texte lesen (texte_de.txt, texte_en.txt), Verweise {{t:schluessel}} einsetzen, Platzhalter aus zahlen.py füllen,
Formeln nach MathML (tex2mathml.py), Schriften als data:-URL, Skripte zusammensetzen, CSP mit SHA-256 der eingebetteten Blöcke.
Der Bau ist deterministisch: gleiche Quellen ergeben gleiche Bytes (Stand aus STAND, Version aus der Prüfsumme der Quellen).
"""
import base64
import hashlib
import json
import os
import re
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HIER, "src")
sys.path.insert(0, HIER)
import tex2mathml  # noqa: E402
import zahlen  # noqa: E402

STAND = "2026-11-11"
SPRACHEN = ("de", "en")
SKRIPTE = ["modell.js"]
SCHRIFTEN = [("Plex Sans", 400, "normal", "PlexSans-400.woff2"), ("Plex Sans", 600, "normal", "PlexSans-600.woff2"),
             ("Plex Mono", 400, "normal", "PlexMono-400.woff2"), ("Plex Mono", 600, "normal", "PlexMono-600.woff2"),
             ("Plex Math", 400, "normal", "PlexMath.woff2")]
LIZENZEN = [("IBM Plex Sans", "IBMPlexSans-OFL.txt"), ("IBM Plex Mono", "IBMPlexMono-OFL.txt"), ("IBM Plex Math", "IBMPlexMath-OFL.txt")]


class BauFehler(Exception):
    pass


def lies(name, binaer=False):
    with open(os.path.join(SRC, name), "rb" if binaer else "r", encoding=None if binaer else "utf-8") as f:
        return f.read()


def texte_lesen(name):
    """Format: '@schluessel' und darunter der Text bis zum nächsten '@' oder Kommentar ('#' am Zeilenanfang)."""
    out, k, zeilen = {}, None, []
    for zeile in lies(name).split("\n"):
        if zeile.startswith("@") or zeile.startswith("#"):
            if k is not None:
                out[k] = "\n".join(zeilen).strip()
            k, zeilen = None, []
            if zeile.startswith("@"):
                k = zeile[1:].strip()
                if k in out:
                    raise BauFehler("%s: Schlüssel doppelt: %s" % (name, k))
            continue
        if k is not None:
            zeilen.append(zeile)
    if k is not None:
        out[k] = "\n".join(zeilen).strip()
    return out


PLATZ = re.compile(r"\{\{([zev]):([A-Za-z0-9_]+)\}\}")


def texte_bauen():
    roh = {s: texte_lesen("texte_%s.txt" % s) for s in SPRACHEN}
    fehlt = set(roh["de"]) ^ set(roh["en"])
    if fehlt:
        raise BauFehler("Schlüssel nur in einer Sprache: " + ", ".join(sorted(fehlt)))
    for s in SPRACHEN:      # Verweise {{t:schluessel}} auf einen anderen Text derselben Sprache (eine Ebene)
        for k, text in list(roh[s].items()):
            roh[s][k] = re.sub(r"\{\{t:([A-Za-z0-9_]+)\}\}", lambda m: roh[s][m.group(1)], text)
    fertig = {}
    for s in SPRACHEN:
        werte = zahlen.alle(s)
        fertig[s] = {}
        for k, text in roh[s].items():
            def ersetze(m):
                n = m.group(1) + ":" + m.group(2)
                if n not in werte:
                    raise BauFehler("%s/%s: unbekannter Platzhalter {{%s}}" % (s, k, n))
                return werte[n]
            t = PLATZ.sub(ersetze, text)
            try:
                t = tex2mathml.ersetze_formeln(t)
            except tex2mathml.Fehler as e:
                raise BauFehler("%s/%s: Formel: %s" % (s, k, e))
            if "{{" in t or "}}" in t:
                raise BauFehler("%s/%s: Platzhalter nicht aufgelöst" % (s, k))
            t = re.sub(r"(<math>(?:(?!</math>).)*</math>)([.,;:)])", r'<span class="nb">\1\2</span>', t, flags=re.S)   # Satzzeichen bleiben an der Formel
            if "$" in t:
                raise BauFehler("%s/%s: einzelnes $ übrig" % (s, k))
            for zeichen in ("\u2013", "\u2014"):
                if zeichen in t:
                    raise BauFehler("%s/%s: Gedankenstrich" % (s, k))
            fertig[s][k] = t
    return roh, fertig


def schriften_css():
    teile = []
    for familie, gewicht, stil, datei in SCHRIFTEN:
        b64 = base64.b64encode(lies(os.path.join("schriften", datei), binaer=True)).decode("ascii")
        teile.append('@font-face { font-family: "%s"; font-weight: %d; font-style: %s; font-display: block; '
                     'src: url(data:font/woff2;base64,%s) format("woff2"); }' % (familie, gewicht, stil, b64))
    return "\n".join(teile)


def lizenz_kommentar():
    teile = []
    for name, datei in LIZENZEN:
        teile.append(name + ":\n" + lies(os.path.join("schriften", datei)).strip())
    text = "\n\n".join(teile)
    if "*/" in text:
        raise BauFehler("Lizenztext enthält */")
    return "/* Schriften (Teilmengen, eingebettet), SIL Open Font License 1.1:\n" + text + "\n*/"


def js_daten(name, wert):
    s = json.dumps(wert, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    return "const %s = %s;" % (name, s.replace("</", "<\\/"))


def quellen_pruefsumme():
    h = hashlib.sha256()
    namen = sorted(os.listdir(SRC)) + ["schriften/" + n for n in sorted(os.listdir(os.path.join(SRC, "schriften")))]
    for n in namen:
        p = os.path.join(SRC, n)
        if os.path.isfile(p):
            h.update(n.encode() + b"\0" + open(p, "rb").read() + b"\0")
    for n in ("zahlen.py", "tex2mathml.py", "bauen.py"):
        h.update(n.encode() + b"\0" + open(os.path.join(HIER, n), "rb").read() + b"\0")
    for n in ("kaffee_modell.py", "werte.py"):
        h.update(n.encode() + b"\0" + open(os.path.join(HIER, "..", "modell", n), "rb").read() + b"\0")
    return h.hexdigest()


def zeichen_pruefen(texte, js):
    """Jedes Zeichen der Texte und Skripte muss in Plex Sans oder Plex Math liegen (Schriftstapel), Formeln in Plex Math."""
    try:
        from fontTools.ttLib import TTFont
    except ImportError:
        return ["fontTools fehlt: Zeichenprüfung nicht ausgeführt"]
    sans = set(TTFont(os.path.join(SRC, "schriften", "PlexSans-400.woff2")).getBestCmap())
    mathe = set(TTFont(os.path.join(SRC, "schriften", "PlexMath.woff2")).getBestCmap())
    fehlt = {}
    for s in SPRACHEN:
        for k, t in texte[s].items():
            ohne_mathe = re.sub(r"<[^>]+>", " ", re.sub(r"<math.*?</math>", " ", t, flags=re.S))
            for c in set(ohne_mathe):
                if ord(c) > 0x20 and ord(c) not in sans and ord(c) not in mathe:
                    fehlt.setdefault(c, set()).add(s + "/" + k)
            for m in re.findall(r"<math.*?</math>", t, flags=re.S):
                for c in set(re.sub(r"<[^>]+>", "", m)):
                    if ord(c) > 0x20 and ord(c) not in mathe:
                        fehlt.setdefault(c, set()).add(s + "/" + k + " (Formel)")
    for c in set(re.findall(r"[^\x00-\x7f]", js)):
        if ord(c) not in sans and ord(c) not in mathe:
            fehlt.setdefault(c, set()).add("Skript")
    return ["Zeichen U+%04X (%s) fehlt in der Schrift: %s" % (ord(c), c, ", ".join(sorted(w)[:4])) for c, w in sorted(fehlt.items())]


def bauen():
    roh, texte = texte_bauen()
    summe = quellen_pruefsumme()
    bau = {"stand": STAND, "version": summe[:10]}
    js_teile = ["// Kaffee mit Milch: Simulation. Gebaut aus simulation/site/src mit simulation/site/bauen.py (Stand %s, Quellen %s)."
                % (STAND, summe[:10])]
    for n in SKRIPTE:
        js_teile.append(lies(n).strip())
    js_teile += [js_daten("TEXTE", texte), js_daten("BAU", bau), lies("oberflaeche.js").strip()]
    js = "\n".join(js_teile) + "\n"
    if "</script" in js.lower():
        raise BauFehler("</script im Skript")
    css = lies("stil.css").replace("{{FONTS}}", schriften_css()).rstrip() + "\n" + lizenz_kommentar() + "\n"
    if "</style" in css.lower():
        raise BauFehler("</style im Stil")
    h = lambda s: "'sha256-" + base64.b64encode(hashlib.sha256(s.encode("utf-8")).digest()).decode("ascii") + "'"
    csp = ("default-src 'none'; script-src %s; style-src %s; font-src data:; img-src data:; base-uri 'none'; form-action 'none'"
           % (h(js), h(css)))
    vorlage = lies("vorlage.html")
    for p in ("{{CSP}}", "{{CSS}}", "{{JS}}"):
        if vorlage.count(p) != 1:
            raise BauFehler("Vorlage: Platzhalter %s nicht genau einmal" % p)
    if re.search(r"\sstyle\s*=", vorlage) or re.search(r"\son[a-z]+\s*=", vorlage):
        raise BauFehler("Vorlage: style= oder on...= (CSP)")
    seite = vorlage.replace("{{CSP}}", csp).replace("{{CSS}}", css).replace("{{JS}}", js)
    warnungen = zeichen_pruefen(texte, lies("oberflaeche.js") + lies("vorlage.html"))
    return seite.encode("utf-8"), summe, warnungen, {"js": len(js.encode()), "css": len(css.encode()),
                                                       "texte": len(json.dumps(texte, ensure_ascii=False).encode())}


def main():
    seite, summe, warnungen, teile = bauen()
    for w in warnungen:
        print("WARNUNG:", w)
    ausgabe = sys.argv[sys.argv.index("--ziel") + 1] if "--ziel" in sys.argv else HIER   # --ziel <ordner>: Probebau außerhalb von site/
    os.makedirs(ausgabe, exist_ok=True)
    ziel = os.path.join(ausgabe, "index.html")
    if "--pruefen" in sys.argv:
        alt = open(ziel, "rb").read() if os.path.exists(ziel) else b""
        print("gleich" if alt == seite else "VERSCHIEDEN")
        sys.exit(0 if alt == seite else 1)
    for n in ("index.html", "Kaffee_Simulation.html"):
        with open(os.path.join(ausgabe, n), "wb") as f:
            f.write(seite)
    sha = hashlib.sha256(seite).hexdigest()
    with open(os.path.join(ausgabe, "BAUNACHWEIS.txt"), "w", encoding="utf-8") as f:
        f.write("Baunachweis Kaffee-Simulation Fassung 3 (geschrieben von bauen.py)\n")
        f.write("Stand: %s\nPrüfsumme der Quellen (SHA-256): %s\n" % (STAND, summe))
        f.write("index.html und Kaffee_Simulation.html (bytegleich): %d Bytes, SHA-256 %s\n" % (len(seite), sha))
        f.write("Anteile: Skript %(js)d Bytes, Stil mit Schriften %(css)d Bytes, Texte %(texte)d Bytes\n" % teile)
        f.write("Warnungen: %s\n" % ("keine" if not warnungen else "; ".join(warnungen)))
    print("gebaut: %d Bytes, SHA-256 %s" % (len(seite), sha))
    print("Anteile:", teile)


if __name__ == "__main__":
    try:
        main()
    except BauFehler as e:
        print("BAUFEHLER:", e)
        sys.exit(1)
