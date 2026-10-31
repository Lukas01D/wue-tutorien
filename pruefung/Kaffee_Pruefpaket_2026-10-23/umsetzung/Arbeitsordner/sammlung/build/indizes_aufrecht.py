# -*- coding: utf-8 -*-
"""Beschreibende Indizes in Formeln aufrecht setzen (Ä24, wie in der Kaffee-Aufgabe), für die übrigen Tutorien der Sammlung.

Aufrecht werden Bezeichnungen (Eis, Luft, außen, innen, mittel, AMOC, th, ges, ...). Kursiv bleiben Größen und Zahlen als
Index: p in c_p (Druck), die Koordinate z (Q_z, z+dz, z=0), Ziffern, griechische Buchstaben und Befehle wie \\infty, \\alpha, \\ln.
Bereits aufrechte Indizes (\\mathrm{...}) bleiben, wie sie sind.

Aufruf (im Ordner sammlung):
  python3 build/indizes_aufrecht.py            schreibt die Dateien um und prüft sie
  python3 build/indizes_aufrecht.py --pruefen  ändert nichts, zeigt nur, was sich ändern würde
Gegenprobe: Entfernt man in alter und neuer Fassung jedes \\mathrm{...} (nur die Hülle), sind beide Texte gleich.
"""
import re, sys, os, glob

HIER = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))         # Ordner sammlung
DATEIEN = sorted(glob.glob(os.path.join(HIER, "teile", "*.md")) + glob.glob(os.path.join(HIER, "quellen", "*.md"))
                 + glob.glob(os.path.join(HIER, "skripte", "abb_t*.py")) + [os.path.join(HIER, "build", "sammlung_bauen.py")])
DATEIEN = [d for d in DATEIEN if "kaffee" not in os.path.basename(d)]      # Kaffee-Aufgabe ist schon umgestellt
FORMEL = re.compile(r"\$\$.*?\$\$|\$[^$\n]+?\$", re.S)


def klammer_ende(s, i):
    """Index der schließenden Klammer zur öffnenden Klammer bei s[i]."""
    tiefe = 0
    for k in range(i, len(s)):
        if s[k] == "{":
            tiefe += 1
        elif s[k] == "}":
            tiefe -= 1
            if tiefe == 0:
                return k
    raise ValueError("Klammer nicht geschlossen: " + s[i:i + 40])


def teile_oben(s):
    """Inhalt an Kommas der obersten Ebene trennen."""
    teile, tiefe, start = [], 0, 0
    for k, ch in enumerate(s):
        if ch == "{":
            tiefe += 1
        elif ch == "}":
            tiefe -= 1
        elif ch == "," and tiefe == 0:
            teile.append(s[start:k]); start = k + 1
    teile.append(s[start:])
    return teile


def bleibt_kursiv(teil, pos, basis_c):
    if re.fullmatch(r"[0-9.]+|[0-9]+\{,\}[0-9]+", teil):                     # Zahl
        return True
    if teil.startswith("\\"):                                                  # \alpha, \infty, \ln, \mathrm{...}
        return True
    if re.fullmatch(r"z([+\-=].*)?", teil):                                    # Koordinate z
        return True
    if teil == "p" and pos == 0 and basis_c:                                   # c_p: p = Druck
        return True
    return False


def index_neu(inhalt, basis_c):
    teile = teile_oben(inhalt)
    neu, gruppe = [], []
    for pos, t in enumerate(teile):
        if bleibt_kursiv(t, pos, basis_c):
            if gruppe:
                neu.append(r"\mathrm{" + ",".join(gruppe) + "}"); gruppe = []
            neu.append(t)
        else:
            gruppe.append(t)
    if gruppe:
        neu.append(r"\mathrm{" + ",".join(gruppe) + "}")
    return ",".join(neu)


def formel_neu(f):
    aus, k = [], 0
    while k < len(f):
        ch = f[k]
        if ch == "_" and (k == 0 or f[k - 1] != "\\"):
            basis_c = re.search(r"(?:^|[^A-Za-z\\])c$", f[:k]) is not None
            if f[k + 1] == "{":
                e = klammer_ende(f, k + 1)
                inhalt = f[k + 2:e]
                aus.append("_{" + index_neu(inhalt, basis_c) + "}")
                k = e + 1
                continue
            if f[k + 1] == "\\":                                               # _\infty, _\mathrm{...}
                aus.append(ch); k += 1
                continue
            z = f[k + 1]
            aus.append("_" + (z if bleibt_kursiv(z, 0, basis_c) else r"\mathrm{" + z + "}"))
            k += 2
            continue
        aus.append(ch); k += 1
    return "".join(aus)


def aufrecht(text):
    return FORMEL.sub(lambda m: formel_neu(m.group(0)), text)


def ohne_mathrm(text):
    """Gegenprobe: jede Hülle \\mathrm{...} entfernen (Inhalt bleibt); _\\mathrm{X} wird wieder _X."""
    alt = None
    while alt != text:
        alt = text
        text = re.sub(r"_\\mathrm\{([^{}])\}", r"_\1", text)
        text = re.sub(r"\\mathrm\{([^{}]*)\}", r"\1", text)
    return text


if __name__ == "__main__":
    nur_pruefen = "--pruefen" in sys.argv
    gesamt = 0
    for d in DATEIEN:
        alt = open(d, encoding="utf-8").read()
        neu = aufrecht(alt)
        assert ohne_mathrm(neu) == ohne_mathrm(alt), "Gegenprobe verletzt: " + d
        assert aufrecht(neu) == neu, "nicht stabil: " + d
        n = sum(1 for a, b in zip(re.findall(FORMEL, alt), re.findall(FORMEL, neu)) if a != b)
        gesamt += n
        print(f"{os.path.relpath(d, HIER):34s} {n:4d} Formeln geändert")
        if not nur_pruefen and neu != alt:
            open(d, "w", encoding="utf-8").write(neu)
    print("zusammen", gesamt, "Formeln; Gegenprobe (ohne \\mathrm gleich) für alle Dateien erfüllt")
