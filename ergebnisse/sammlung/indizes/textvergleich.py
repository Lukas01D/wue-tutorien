# -*- coding: utf-8 -*-
"""Textvergleich zur Umstellung der beschreibenden Indizes (Ä24) in der Aufgabensammlung.

Belegt, dass sich nur die Schrift der Indizes geändert hat, keine Zahl und kein Wort:
  1. Quellen (Teile, Quellen, Abbildungsskripte, Bauskript): alt und neu sind gleich, sobald jede Hülle \\mathrm{...} entfernt ist.
  2. Gebautes Markdown der Sammlung: ebenso.
  3. PDF: Text je Seite (pdftotext) ohne Leerraum und Akzentzeichen, Mathematikbuchstaben als normale Buchstaben:
     gleich, oder nur dieselben Bruchstücke in anderer Reihenfolge ausgelesen.
  4. Word: aller Text (w:t und m:t) in Reihenfolge gleich; gezählt wird, wie viele Formelzeichen aufrecht gesetzt sind (m:sty p).
Vergleich gegen einen Git-Stand (Vorgabe: origin/main vor der Umstellung).

Aufruf vom Repository aus: python3 ergebnisse/sammlung/indizes/textvergleich.py [Git-Stand]
"""
import os, re, sys, subprocess, tempfile, unicodedata, zipfile, difflib, glob
from collections import Counter

REPO = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True).stdout.strip()
W = "pruefung/Kaffee_Pruefpaket_2026-10-23/umsetzung/Arbeitsordner/sammlung"
sys.path.insert(0, os.path.join(REPO, W, "build"))
from indizes_aufrecht import ohne_mathrm, DATEIEN, FORMEL   # noqa: E402

REV = sys.argv[1] if len(sys.argv) > 1 else "origin/main"
NAME = "Aufgabensammlung_Tutorien_WUE_2026-10-31"


def git_alt(pfad, binaer=False):
    r = subprocess.run(["git", "show", f"{REV}:{pfad}"], cwd=REPO, capture_output=True, check=True)
    return r.stdout if binaer else r.stdout.decode("utf-8")


def neu(pfad, binaer=False):
    with open(os.path.join(REPO, pfad), "rb" if binaer else "r", **({} if binaer else {"encoding": "utf-8"})) as f:
        return f.read()


def pdf_seiten(daten):
    """Text je Seite ohne Leerraum und ohne Akzentzeichen (der Punkt von q̇ wird je nach Schrift des Index
    an einen anderen Buchstaben gehängt), Unicode-Mathematikbuchstaben als normale Buchstaben (NFKD)."""
    with tempfile.NamedTemporaryFile(suffix=".pdf") as t:
        t.write(daten); t.flush()
        n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", t.name], capture_output=True, text=True).stdout).group(1))
        seiten = []
        for i in range(1, n + 1):
            text = subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), t.name, "-"], capture_output=True, text=True).stdout
            text = unicodedata.normalize("NFKD", text)
            seiten.append("".join(c for c in text if not c.isspace() and unicodedata.category(c) != "Mn"))
    return seiten


def docx_text(daten):
    with tempfile.NamedTemporaryFile(suffix=".docx") as t:
        t.write(daten); t.flush()
        d = zipfile.ZipFile(t.name).read("word/document.xml").decode("utf-8")
    return re.findall(r"<(?:w|m):t(?: [^>]*)?>([^<]*)</(?:w|m):t>", d), d


bericht = [f"# Textvergleich: Indizes aufrecht in der Aufgabensammlung", "",
           f"Vergleich der Arbeitskopie mit `{REV}` "
           f"({subprocess.run(['git', 'rev-parse', '--short', REV], cwd=REPO, capture_output=True, text=True).stdout.strip()}).", ""]
ok_alle = True

# 1. Quellen
bericht += ["## 1. Quellen", "", "| Datei | Formeln geändert | ohne \\mathrm gleich |", "|---|---:|---|"]
for d in DATEIEN:
    rel = os.path.relpath(d, REPO)
    a, n_ = git_alt(rel), neu(rel)
    gleich = ohne_mathrm(a) == ohne_mathrm(n_)
    geaendert = sum(1 for x, y in zip(FORMEL.findall(a), FORMEL.findall(n_)) if x != y)
    ok_alle &= gleich
    if geaendert:
        bericht.append(f"| {os.path.relpath(d, os.path.join(REPO, W))} | {geaendert} | {'ja' if gleich else 'NEIN'} |")
bericht.append("")

# 2. Markdown der Sammlung
md_pfad = f"{W}/ausgabe/{NAME}.md"
a, n_ = git_alt(md_pfad), neu(md_pfad)
gleich = ohne_mathrm(a) == ohne_mathrm(n_)
ok_alle &= gleich
bericht += ["## 2. Gebautes Markdown", "",
            f"`{NAME}.md`: {sum(1 for x, y in zip(FORMEL.findall(a), FORMEL.findall(n_)) if x != y)} Formeln geändert; "
            f"ohne \\mathrm gleich: **{'ja' if gleich else 'NEIN'}**.", ""]

# 3. PDF: je Seite gleich, oder nur Bruchstücke von pdftotext in anderer Reihenfolge ausgelesen (gleiche Zeichen, Verschiebung)
sa, sn = pdf_seiten(git_alt(f"{W}/ausgabe/{NAME}.pdf", True)), pdf_seiten(neu(f"{W}/ausgabe/{NAME}.pdf", True))
gleich_seiten, verschoben, falsch = 0, [], []
for i, (x, y) in enumerate(zip(sa, sn), 1):
    if x == y:
        gleich_seiten += 1
        continue
    ops = [(o, x[i1:i2], y[j1:j2]) for o, i1, i2, j1, j2 in difflib.SequenceMatcher(None, x, y, autojunk=False).get_opcodes() if o != "equal"]
    if Counter(x) == Counter(y):                                          # dieselben Zeichen, nur andere Reihenfolge
        verschoben.append((i, sorted(set(a for o, a, b in ops if a))))
    else:
        falsch.append((i, ops[:8]))
ok_alle &= len(sa) == len(sn) and not falsch
bericht += ["## 3. PDF", "", f"Seiten vorher {len(sa)}, nachher {len(sn)}; Text je Seite (ohne Leerraum und Akzentzeichen) gleich auf "
            f"**{gleich_seiten}** Seiten. Auf {len(verschoben)} Seiten liest pdftotext dieselben Zeichen in anderer Reihenfolge aus "
            "(gleiche Zeichen in gleicher Anzahl, nur Bruchstücke verschoben; ausgelesen wurden):", ""]
bericht += [f"- Seite {i}: " + ", ".join(f"„{t}“" for t in teile) for i, teile in verschoben]
bericht += ["", f"Seiten mit echter Abweichung: **{len(falsch)}**", ""] + [f"- Seite {i}: {ops}" for i, ops in falsch] + [""]

# 4. Word
ta, da = docx_text(git_alt(f"{W}/ausgabe/{NAME}.docx", True))
tn, dn = docx_text(neu(f"{W}/ausgabe/{NAME}.docx", True))
gleich = ta == tn
ok_alle &= gleich
bericht += ["## 4. Word", "", f"Textstücke vorher {len(ta)}, nachher {len(tn)}; Text gleich: **{'ja' if gleich else 'NEIN'}**. "
            f"Aufrecht gesetzte Formelzeichen (m:sty p): vorher {da.count('<m:sty m:val=\"p\" />')}, nachher {dn.count('<m:sty m:val=\"p\" />')}.", ""]

bericht += ["## Ergebnis", "", "**Nur die Schrift der Indizes hat sich geändert; keine Zahl und kein Wort.**" if ok_alle
            else "**Abweichung gefunden, siehe oben.**", ""]
ziel = os.path.join(os.path.dirname(os.path.abspath(__file__)), "TEXTVERGLEICH.md")
open(ziel, "w", encoding="utf-8").write("\n".join(bericht))
print("\n".join(bericht))
sys.exit(0 if ok_alle else 1)
