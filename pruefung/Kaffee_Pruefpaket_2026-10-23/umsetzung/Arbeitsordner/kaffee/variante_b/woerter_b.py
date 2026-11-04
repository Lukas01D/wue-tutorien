# -*- coding: utf-8 -*-
"""Wörter je Abschnitt der Variante B (wie ergebnisse/kaffee/nachrechnung_koordination/woerter.py: Formeln zählen als ein
Wort, Tabellenstriche und Formatierung zählen nicht; Ergebniszeilen der Teile a bis g getrennt ausgewiesen).
Aufruf: python3 woerter_b.py <datei.md>"""
import re, sys
t = open(sys.argv[1], encoding="utf-8").read()
t = re.sub(r"^---.*?---\n", "", t, flags=re.S)
t = re.sub(r"\$\$.*?\$\$", " F ", t, flags=re.S)
t = re.sub(r"\$[^$]*\$", " F ", t)
t = re.sub(r"!\[\]\([^)]*\)\{[^}]*\}", " ", t)
t = re.sub(r"`[^`]*`\{=latex\}", " ", t)
t = re.sub(r"\{\.underline\}|:::.*", " ", t)


def zaehle(s):
    s = re.sub(r"[|*\\\[\]#:_-]{1,}", " ", s)
    return len(re.findall(r"[\wäöüÄÖÜß0-9,.%°…]+", s))


teile = re.split(r"\n(?=\*\*\[[^\]]+\]\{?)", "\n" + re.sub(r"\{\.underline\}", "", t))
gesamt = 0
for p in teile:
    m = re.match(r"\*\*\[([^\]]+)\]", p.strip())
    if not m:
        continue
    n = zaehle(p)
    erg = sum(zaehle(z) for z in p.split("\n") if re.fullmatch(r"\s*(F[,\s]*(und)?\s*)+(\(Zuordnung selbst bestimmen\))?\s*\\?\s*", z.replace("\\quad", "")) and "F" in z)
    zusatz = f" (davon Ergebniszeilen {erg})" if erg and m.group(1).startswith("Gesucht") else ""
    if "Frage 1 (Vorab-Frage)" in p:
        a, b = p.split("**Frage 1 (Vorab-Frage):**")
        zusatz += f" (Ausgangssituation {zaehle(a)}, Frage 1 {zaehle('Frage 1 (Vorab-Frage)' + b)})"
    print(f"{m.group(1):50s} {n:5d}{zusatz}")
    gesamt += n
print(f"{'gesamt':50s} {gesamt:5d}")
