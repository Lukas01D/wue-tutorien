# -*- coding: utf-8 -*-
"""Bau eines Gestaltungsentwurfs der Kaffee-Seite. Kopie von simulation/site/bauen.py (Stand da7deb1) mit diesen Änderungen:
  E1  Quellen: zuerst simulation/design_entwuerfe/<entwurf>/src/, sonst simulation/site/src/ (Rechenkern, Texte, Regler unverändert).
  E2  Stil: Schriften + gemeinsam.css (Pflichtteile aller Entwürfe) + <entwurf>/src/stil.css (darf gemeinsam.css überschreiben).
  E3  Schriften aus <entwurf>/src/schriften.json statt fest Fira Sans und Fira Math.
  E4  oberflaeche.js wird beim Bau mit gestaltung_patch.py angepasst (nur Darstellung, siehe dort).
  E5  Zeichenprüfung über alle Textschriften des Entwurfs (Ersatz über den font-family-Stapel) und die Formelschrift.
  E6  Ausgabe nach <entwurf>/ (index.html und bytegleich Kaffee_Simulation.html, BAUNACHWEIS.txt).

Aufruf: python3 simulation/design_entwuerfe/bauen_entwurf.py <entwurf>   (messprotokoll, kaffeehaus, hoersaal)

Schritte: Texte lesen (texte_de.txt, texte_en.txt), Platzhalter aus zahlen.py füllen, Formeln nach MathML (tex2mathml.py),
Regler mit MathML, Schriften als data:-URL, Skripte zusammensetzen, CSP mit SHA-256 der eingebetteten Blöcke.
Der Bau ist deterministisch: gleiche Quellen ergeben gleiche Bytes (Stand aus STAND, Version aus der Prüfsumme der Quellen).
"""
import base64
import hashlib
import json
import os
import re
import sys

ENTWURF_HIER = os.path.dirname(os.path.abspath(__file__))
HIER = os.path.join(os.path.dirname(ENTWURF_HIER), "site")                 # Bauhilfen und Grundquellen des gebauten Stands
SRC = os.path.join(HIER, "src")
ENTWURF = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else None
if ENTWURF not in ("messprotokoll", "kaffeehaus", "hoersaal"):
    sys.exit("Aufruf: bauen_entwurf.py <messprotokoll|kaffeehaus|hoersaal>")
EIGEN = os.path.join(ENTWURF_HIER, ENTWURF)
EIGEN_SRC = os.path.join(EIGEN, "src")
sys.path.insert(0, HIER)
sys.path.insert(0, ENTWURF_HIER)
import tex2mathml  # noqa: E402
import zahlen  # noqa: E402
import gestaltung_patch  # noqa: E402

STAND = "2026-11-05"
GRENZE_BYTES = 450000
SPRACHEN = ("de", "en")
SKRIPTE = ["modell.js", "erweiterung.js", "hilfen.js"]
SCHRIFTEN_DATEN = json.load(open(os.path.join(EIGEN_SRC, "schriften.json"), encoding="utf-8"))   # E3
SCHRIFTEN = [tuple(x) for x in SCHRIFTEN_DATEN["schriften"]]     # (Familie, Gewicht, Stil, Datei)
MATHE_FAMILIE = SCHRIFTEN_DATEN["formel"]


class BauFehler(Exception):
    pass


def pfad(name):          # E1: eigene Datei des Entwurfs vor der Grundquelle
    eigen = os.path.join(EIGEN_SRC, name)
    return eigen if os.path.exists(eigen) else os.path.join(SRC, name)


def lies(name, binaer=False):
    with open(pfad(name), "rb" if binaer else "r", encoding=None if binaer else "utf-8") as f:
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
            for zeichen in ("–", "—"):
                if zeichen in t:
                    raise BauFehler("%s/%s: Gedankenstrich" % (s, k))
            fertig[s][k] = t
    return roh, fertig


def regler_bauen():
    d = json.loads(lies("regler.json"))
    for r in d["regler"]:
        r["mathml"] = tex2mathml.tex_zu_mathml(r["tex"])
    d.pop("_hinweis", None)
    return d


def schriften_css():
    teile = []
    for familie, gewicht, stil, datei in SCHRIFTEN:
        b64 = base64.b64encode(lies(os.path.join("schriften", datei), binaer=True)).decode("ascii")
        teile.append('@font-face { font-family: "%s"; font-weight: %d; font-style: %s; font-display: swap; '
                     'src: url(data:font/woff2;base64,%s) format("woff2"); }' % (familie, gewicht, stil, b64))
    return "\n".join(teile)


def lizenz_kommentar():
    teile = []
    for fam, datei in SCHRIFTEN_DATEN["lizenzen"]:
        zeilen = lies(os.path.join("schriften", datei)).strip().split("\n")
        teile.append(fam + ": " + " ".join(z.strip() for z in zeilen[:3] if z.strip()) + " (SIL Open Font License 1.1)")
    text = "\n".join(teile)
    if "*/" in text:
        raise BauFehler("Lizenztext enthält */")
    return "/* Schriften (Teilmengen, eingebettet):\n" + text + "\n*/"


def js_daten(name, wert):
    s = json.dumps(wert, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    return "const %s = %s;" % (name, s.replace("</", "<\\/"))


def quellen_pruefsumme():
    h = hashlib.sha256()
    for wurzel in (SRC, EIGEN_SRC):
        namen = sorted(os.listdir(wurzel)) + ["schriften/" + n for n in sorted(os.listdir(os.path.join(wurzel, "schriften")))]
        for n in namen:
            p = os.path.join(wurzel, n)
            if os.path.isfile(p):
                h.update(n.encode() + b"\0" + open(p, "rb").read() + b"\0")
    for n in ("gemeinsam.css", "gestaltung_patch.py", "bauen_entwurf.py"):
        h.update(n.encode() + b"\0" + open(os.path.join(ENTWURF_HIER, n), "rb").read() + b"\0")
    for n in ("zahlen.py", "tex2mathml.py", "bauen.py"):
        h.update(n.encode() + b"\0" + open(os.path.join(HIER, n), "rb").read() + b"\0")
    for n in ("kaffee_modell.py", "kaffee_erweitert.py"):
        h.update(n.encode() + b"\0" + open(os.path.join(HIER, "..", "modell", n), "rb").read() + b"\0")
    return h.hexdigest()


def zeichen_pruefen(texte, js):
    """Jedes Zeichen der Texte muss in Fira Sans liegen (sonst Ersatzschrift)."""
    try:
        from fontTools.ttLib import TTFont
    except ImportError:
        return ["fontTools fehlt: Zeichenprüfung nicht ausgeführt"]
    sans, mathe = None, set()       # E5: ein Zeichen gilt als vorhanden, wenn jede Textfamilie es selbst oder über ihren Stapel hat
    familien = {}
    for fam, gew, stil, datei in SCHRIFTEN:
        cm = set(TTFont(pfad(os.path.join("schriften", datei))).getBestCmap())
        if fam == MATHE_FAMILIE:
            mathe |= cm
        else:
            familien[fam] = cm if fam not in familien else familien[fam] & cm
    for fam, cm in familien.items():
        if fam not in SCHRIFTEN_DATEN.get("ersatz", {}):      # reine Ersatzschrift (nur einzelne Zeichen): nicht selbst prüfen
            continue
        mit_ersatz = cm | set().union(*[familien[e] for e in SCHRIFTEN_DATEN.get("ersatz", {}).get(fam, []) if e in familien]) | \
            (mathe if MATHE_FAMILIE in SCHRIFTEN_DATEN.get("ersatz", {}).get(fam, []) else set())
        sans = mit_ersatz if sans is None else sans & mit_ersatz
    fehlt = {}
    for s in SPRACHEN:
        for k, t in texte[s].items():
            ohne_mathe = re.sub(r"<math.*?</math>", " ", t, flags=re.S)
            for c in set(ohne_mathe):
                if ord(c) > 0x20 and ord(c) not in sans:
                    fehlt.setdefault(c, set()).add(s + "/" + k)
            for m in re.findall(r"<math.*?</math>", t, flags=re.S):
                inhalt = re.sub(r"<[^>]+>", "", m)
                for c in set(inhalt):
                    if ord(c) > 0x20 and ord(c) not in mathe and ord(c) not in sans:
                        fehlt.setdefault(c, set()).add(s + "/" + k + " (Formel)")
    for c in set(re.findall(r"[^\x00-\x7f]", js)):
        if ord(c) not in sans:
            fehlt.setdefault(c, set()).add("Skript")
    return ["Zeichen U+%04X (%s) fehlt in der Schrift: %s" % (ord(c), c, ", ".join(sorted(w)[:4])) for c, w in sorted(fehlt.items())]


def bauen():
    roh, texte = texte_bauen()
    regler = regler_bauen()
    summe = quellen_pruefsumme()
    bau = {"stand": STAND, "version": summe[:10]}
    js_teile = ["// Kaffee mit Milch: Simulation. Gebaut aus simulation/site/src mit simulation/site/bauen.py (Stand %s, Quellen %s)."
                % (STAND, summe[:10])]
    for n in SKRIPTE:
        js_teile.append(lies(n).strip())
    js_teile += [js_daten("TEXTE", texte), js_daten("REGLER_DEF", regler), js_daten("BAU", bau),
                 gestaltung_patch.anwenden(lies("oberflaeche.js")).strip()]       # E4
    js = "\n".join(js_teile) + "\n"
    if "</script" in js.lower():
        raise BauFehler("</script im Skript")
    gemeinsam = open(os.path.join(ENTWURF_HIER, "gemeinsam.css"), encoding="utf-8").read()       # E2
    css = (schriften_css() + "\n" + gemeinsam.rstrip() + "\n" + lies("stil.css").rstrip() + "\n" + lizenz_kommentar() + "\n")
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
    warnungen = zeichen_pruefen(texte, lies("oberflaeche.js"))
    return seite.encode("utf-8"), summe, warnungen, {"js": len(js.encode()), "css": len(css.encode()),
                                                       "texte": len(json.dumps(texte, ensure_ascii=False).encode())}


def main():
    seite, summe, warnungen, teile = bauen()
    for w in warnungen:
        print("WARNUNG:", w)
    if len(seite) >= GRENZE_BYTES:
        raise BauFehler("Seite zu groß: %d Bytes (Grenze %d)" % (len(seite), GRENZE_BYTES))
    ausgabe = EIGEN                                                          # E6
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
        f.write("Baunachweis Gestaltungsentwurf „%s“ der Kaffee-Simulation (geschrieben von bauen_entwurf.py)\n" % ENTWURF)
        f.write("Stand: %s\nPrüfsumme der Quellen (SHA-256): %s\n" % (STAND, summe))
        f.write("index.html und Kaffee_Simulation.html (bytegleich): %d Bytes, SHA-256 %s\n" % (len(seite), sha))
        f.write("Anteile: Skript %(js)d Bytes, Stil mit Schriften %(css)d Bytes, Texte %(texte)d Bytes\n" % teile)
        f.write("Grenze: unter %d Bytes unkomprimiert\n" % GRENZE_BYTES)
        f.write("Warnungen: %s\n" % ("keine" if not warnungen else "; ".join(warnungen)))
    print("gebaut: %d Bytes, SHA-256 %s" % (len(seite), sha))
    print("Anteile:", teile)


if __name__ == "__main__":
    try:
        main()
    except BauFehler as e:
        print("BAUFEHLER:", e)
        sys.exit(1)
