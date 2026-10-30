# -*- coding: utf-8 -*-
"""Wörter je Baustein eines Aufgabenblatts (Markdown). Formeln ($...$) zählen als ein Wort,
Tabellenstriche und Formatierung zählen nicht. Aufruf: python3 woerter.py <datei.md>"""
import re, sys
t = open(sys.argv[1], encoding="utf-8").read()
t = re.sub(r"\$\$.*?\$\$", " F ", t, flags=re.S)
t = re.sub(r"\$[^$]*\$", " F ", t)
t = re.sub(r"!\[\]\([^)]*\)\{[^}]*\}", " ", t)
t = re.sub(r"```.*?```", " ", t, flags=re.S)
t = re.sub(r"\{\.underline\}|\{=latex\}|:::.*", " ", t)
def zaehle(s):
    s = re.sub(r"[|*\\\[\]#:_-]{1,}", " ", s)
    return len(re.findall(r"[\wäöüÄÖÜß0-9,.%°]+", s))
teile = re.split(r"\n(?=\*\*\[(?:Ausgangssituation|Frage \d|Aufgabe \d|Versuch zu)[^\]]*\])", t)
gesamt = 0
for p in teile:
    m = re.match(r"\*\*\[([^\]]+)\]", p.strip())
    if not m: continue
    name = m.group(1)
    n = zaehle(p)
    # Ergebniszeilen (Zeilen, die nur aus Formeln bestehen) separat
    erg = sum(zaehle(z) for z in p.split("\n") if re.fullmatch(r"\s*(\(1\)\s*|Zu \(1\):\s*)?(F[,\s]*(und)?\s*)+(\(Zuordnung selbst bestimmen\))?\s*\\?\s*", z.replace("\\quad", "")) and "F" in z)
    print(f"{name:25s} {n:5d} Wörter (davon Ergebniszeilen etwa {erg})")
    gesamt += n
print("gesamt", gesamt)
