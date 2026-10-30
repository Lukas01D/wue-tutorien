# -*- coding: utf-8 -*-
"""Setzt die Aufgabensammlung aus den Teildateien zusammen und baut Markdown, PDF (XeLaTeX) und Word.

Aufruf: python3 sammlung_bauen.py [ausgabeordner]
Eingaben: ../teile/t1.md ... t8.md (Tutorium 5 aus t5a_kaffee.md, t5_fragen.md, t5b_ozean.md),
          ../quellen/*_quellen.md
"""
import os, re, sys, subprocess

HIER = os.path.dirname(os.path.abspath(__file__))
S = os.path.dirname(HIER)
AUS = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(S, "ausgabe")
NAME = "Aufgabensammlung_Tutorien_WUE_2026-10-30"
STAND = "30.10.2026"

THEMEN = {
    1: ("Wärmeleitung", "Fourier, mehrschichtige Wand, mittlere Wärmeleitfähigkeit, Randbedingungen", "keine"),
    2: ("Konvektion", r"Platte erzwungen und frei, Grenzschicht, lokales und mittleres $\alpha$, charakteristische Länge", "keine"),
    3: ("Wärmedurchgang", r"thermische Widerstände in Reihe, $kA = 1/R_{\mathrm{th}}$, Rohr mit $k_i$ und $k_a$", "stationär global"),
    4: ("Strahlung", r"Stefan-Boltzmann, grauer Strahler, $\alpha + \rho + \tau = 1$, Kirchhoff", "stationär global"),
    5: ("Wärmebilanzen (instationär global)", r"$\mathrm{d}U/\mathrm{d}t$-Bilanz, Mischen, $T(t)$, Zeitkonstante, Massenbilanz", "instationär global; stationär global"),
    6: ("Wärmebilanzen (stationär differentiell)", r"Bilanz am Element $\mathrm{d}z$ und $\mathrm{d}r$ mit Quelle, $T(z)$, $T(r)$", "stationär differentiell"),
    7: ("Wärmebilanzen (instationär differentiell)", "Wärmeleitungsgleichung, Anfangs- und Randbedingungen, Temperaturleitfähigkeit", "instationär differentiell"),
    8: ("Wärmeübertrager und Verdampfer", r"Bilanz beider Ströme, $\Delta T_{\ln}$, $\varepsilon$-NTU, $C^* = 0$, Wärmekapazitätsstrom", "stationär global"),
}


def lies(name):
    with open(os.path.join(S, name), encoding="utf-8") as f:
        return f.read().strip() + "\n\n"


def tutorium(n):
    if n == 5:
        kaffee = lies("teile/t5a_kaffee.md")
        fragen = lies("teile/t5_fragen.md") if os.path.exists(os.path.join(S, "teile/t5_fragen.md")) else ""
        kaffee = kaffee.replace("<!-- T5_FRAGEN -->", fragen.strip())
        ozean = lies("teile/t5b_ozean.md") if os.path.exists(os.path.join(S, "teile/t5b_ozean.md")) else ""
        return f"# Tutorium 5: {THEMEN[5][0]}\n\n" + kaffee + ozean
    pfad = os.path.join(S, f"teile/t{n}.md")
    if not os.path.exists(pfad):
        return f"# Tutorium {n}: {THEMEN[n][0]}\n\n*(Teil fehlt noch.)*\n\n"
    return lies(f"teile/t{n}.md")


def bloecke(text):
    """H2-Titel ohne die Zusatzaufgaben-Überschrift und Zahl der Zusatzaufgaben."""
    titel = [t.strip() for t in re.findall(r"^## (.+)$", text, re.M) if t.strip() != "Zusatzaufgaben"]
    zusatz = len(re.findall(r"\[Zusatzaufgabe \d+\]", text))
    fragen = len(re.findall(r"\[Frage \d+\]", text))
    return titel, zusatz, fragen


TEILE = {n: tutorium(n) for n in range(1, 9)}

zeilen = []
for n in range(1, 9):
    titel, zusatz, fragen = bloecke(TEILE[n])
    auf = "; ".join(titel) if titel else "(fehlt)"
    extra = (f"{fragen} Frage" if fragen == 1 else f"{fragen} Fragen") + (f", {zusatz} Zusatzaufgabe" + ("n" if zusatz > 1 else "") if zusatz else "")
    zeilen.append(f"| {n} | {THEMEN[n][0]} | {auf} | {extra} | {THEMEN[n][1]} |")

UEBERSICHT = "```{=latex}\n\\begingroup\\small\\setstretch{1.05}\n```\n\n" + "\n".join([
    "| Nr. | Thema | Aufgabenblöcke | Fragen, Zusatz | Kernrechnung |",
    "|:------|:------------------|:------------------------------|:-----------------|:-----------------------------|",
] + zeilen) + "\n\n```{=latex}\n\\endgroup\n```"

VORSPANN = rf"""```{{=latex}}
\begin{{center}}{{\LARGE\bfseries Wärmeübertragung: Aufgabensammlung der Tutorien}}\end{{center}}
```

```{{=openxml}}
<w:p><w:pPr><w:pStyle w:val="Title"/></w:pPr><w:r><w:rPr><w:sz w:val="36"/></w:rPr><w:t>Wärmeübertragung: Aufgabensammlung der Tutorien</w:t></w:r></w:p>
```

::: center
Entwurf zur Auswahl · Stand {STAND} · Lehrstuhl für Fluidverfahrenstechnik, Universität Paderborn
:::

Diese Sammlung enthält alle bisher erarbeiteten Aufgaben für die Tutorien 1 bis 8 in einer einheitlichen Struktur nach dem Vorbild der Lehrstuhl-Tutorien. Jeder Aufgabenblock beginnt mit einer **Ausgangssituation** mit Skizze. Danach folgen die **Fragen**, zuerst eine Vorab-Frage, zu der die Studierenden eine Vermutung notieren, und die **Aufgabe** mit Annahmen, gegebenen Größen und Aufgabenstellung. Das Ergebnis steht am Ende jedes rechnenden Teils. Kurze Rechnungen stehen als Zusatzaufgaben am Ende eines Tutoriums.

Die Sammlung ist bewusst umfangreich: Sie ist die Grundlage für die Auswahl und Kürzung je Tutorium. Lösungswege stehen nicht darin. Alle Zahlen stammen aus Rechenskripten, die Quellen der Arbeitswerte stehen im Anhang. Erstellt mit KI-Unterstützung (Claude, Anthropic); Auswahl, fachliche Prüfung und Freigabe durch die Tutoriumsleitung und die Professorin.

**Übersicht**

{UEBERSICHT}

::: seitenumbruch
:::

```{{=latex}}
\begingroup\setstretch{{1.0}}\tableofcontents\endgroup
```

```{{=openxml}}
<w:p><w:pPr><w:pStyle w:val="TOCHeading"/></w:pPr><w:r><w:t>Inhaltsverzeichnis</w:t></w:r></w:p><w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r><w:r><w:instrText xml:space="preserve"> TOC \o "1-2" \h \z \u </w:instrText></w:r><w:r><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:t>Das Inhaltsverzeichnis erscheint nach dem Aktualisieren der Felder (Rechtsklick, Feld aktualisieren).</w:t></w:r><w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>
```

"""


def anhang():
    teile = ["```{=latex}\n\\small\\sloppy\n```\n\n# Anhang: Quellen der Arbeitswerte\n\n",
             "Je Tutorium die Quellen der Arbeitswerte und der Fakten in den Ausgangssituationen. "
             "Die Rechenskripte liegen im Ordner „Rechnung“ des Pakets.\n\n"]
    for n in range(1, 9):
        dateien = []
        if n == 5:
            dateien = ["quellen/t5a_kaffee_quellen.md", "quellen/t5_quellen.md"]
        else:
            dateien = [f"quellen/t{n}_quellen.md"]
        inhalt = ""
        for d in dateien:
            p = os.path.join(S, d)
            if os.path.exists(p):
                t = open(p, encoding="utf-8").read().strip()
                t = re.sub(r"^#{1,6} (.+)$", r"**\1**", t, flags=re.M)   # Überschriften der Teile flach halten
                inhalt += t + "\n\n"
        if inhalt:
            teile.append(f"## Tutorium {n}: {THEMEN[n][0]}\n\n" + inhalt)
    return "".join(teile)


md = "---\nlang: de\n---\n\n" + VORSPANN + "".join(TEILE[n] for n in range(1, 9)) + anhang()
os.makedirs(AUS, exist_ok=True)
pfad_md = os.path.join(AUS, NAME + ".md")
with open(pfad_md, "w", encoding="utf-8") as f:
    f.write(md)

subprocess.run(["pandoc", pfad_md, "-o", os.path.join(AUS, NAME + ".pdf"), "--pdf-engine=xelatex",
                "-H", os.path.join(HIER, "kopf.tex"), "--lua-filter", os.path.join(HIER, "lehrstuhl.lua"),
                "-V", "documentclass=article", "-V", "fontsize=11pt", "-V", "mainfont=Carlito",
                "-V", "mathfont=Latin Modern Math", "-V", "colorlinks=true", "-V", "linkcolor=black",
                "-V", "urlcolor=blue", "--resource-path", S], check=True)
# Word: lange Wörter in den schmalen Spalten der Übersicht mit weichem Trennstrich (U+00AD)
WEICH = {"Wärmedurchgang": "Wärme\u00addurchgang", "Wärmeübertrager": "Wärme\u00adübertrager",
         "Zusatzaufgabe": "Zusatz\u00adaufgabe", "Wärmebilanzen": "Wärme\u00adbilanzen"}
ueb_docx = UEBERSICHT
for alt, neu in WEICH.items():
    ueb_docx = ueb_docx.replace(alt, neu)
pfad_md_docx = os.path.join(AUS, NAME + "_word.md")
with open(pfad_md_docx, "w", encoding="utf-8") as f:
    f.write(md.replace(UEBERSICHT, ueb_docx, 1))
subprocess.run(["pandoc", pfad_md_docx, "-o", os.path.join(AUS, NAME + ".docx"),
                "--reference-doc", os.path.join(HIER, "referenz_sammlung.docx"),
                "--lua-filter", os.path.join(HIER, "lehrstuhl.lua"), "--resource-path", S], check=True)
os.remove(pfad_md_docx)


def word_zusammenhalten(pfad):
    """Word: Tabellen der gegebenen Größen nicht über den Seitenwechsel trennen, Zwischenüberschriften
    („Annahmen:“, „Gegebene Größen:“, „Frage 1“ …) und Bilder mit dem Folgeabsatz zusammenhalten."""
    import zipfile, shutil, tempfile
    with zipfile.ZipFile(pfad) as z:
        inhalt = {n: z.read(n) for n in z.namelist()}
    d = inhalt["word/document.xml"].decode("utf-8")

    def keep(par):
        if "<w:keepNext/>" in par:
            return par
        if "<w:pPr>" in par:
            return re.sub(r'(<w:pPr>(?:<w:pStyle w:val="[^"]*"\s*/>)?)', r"\1<w:keepNext/>", par, count=1)
        return par.replace("<w:p>", "<w:p><w:pPr><w:keepNext/></w:pPr>", 1)

    # 1) Tabellen: alle Absätze außer in der letzten Zeile mit dem Folgeabsatz verbinden, Zeilen nicht teilen
    def tabelle(m):
        t = m.group(0)
        zeilen = re.findall(r"<w:tr>.*?</w:tr>|<w:tr .*?</w:tr>", t, flags=re.S)
        if len(zeilen) > 1:
            for z in zeilen[:-1]:
                neu = re.sub(r"<w:p>.*?</w:p>", lambda mm: keep(mm.group(0)), z, flags=re.S)
                t = t.replace(z, neu, 1)
        t = t.replace("<w:trPr>", "<w:trPr><w:cantSplit/>")
        return re.sub(r"<w:tr>(?!<w:trPr>)", "<w:tr><w:trPr><w:cantSplit/></w:trPr>", t)
    d = re.sub(r"<w:tbl>.*?</w:tbl>", tabelle, d, flags=re.S)

    # Kaffee-Aufgabe wie im Einzelblatt: Tabelle der gegebenen Größen ohne wiederholte Kopfzeile,
    # Versuchstabelle mit Datenzeilen von mindestens 10 mm zum Ausfüllen von Hand
    def kaffee(m):
        t = m.group(0)
        if "Becher in Teil g" in t:
            t = t.replace("<w:tblHeader/>", "").replace('<w:tblHeader w:val="true"/>', "")
        if "Milch sofort" in t:
            t = t.replace("<w:trPr><w:cantSplit/>", '<w:trPr><w:cantSplit/><w:trHeight w:val="567" w:hRule="atLeast"/>')
        return t
    d = re.sub(r"<w:tbl>.*?</w:tbl>", kaffee, d, flags=re.S)

    # 2) Zwischenüberschriften und Bilder mit dem Folgeabsatz zusammenhalten
    muster = re.compile(r"^(Gegebene Größen|Annahmen|Aufgabenstellung|Frage \d|Aufgabe \d|Zusatzaufgabe \d|Ausgangssituation|Versuch zu|Übersicht)")
    def absatz(m):
        par = m.group(0)
        if "<w:tbl>" in par:
            return par
        text = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", par)).strip()
        if muster.match(text) or ("<pic:pic" in par and not text):
            return keep(par)
        return par
    teile = re.split(r"(<w:tbl>.*?</w:tbl>)", d, flags=re.S)
    for k in range(0, len(teile), 2):
        teile[k] = re.sub(r"<w:p>(?:(?!</w:p>).)*?</w:p>|<w:p .*?</w:p>", absatz, teile[k], flags=re.S)
    d = "".join(teile)
    inhalt["word/document.xml"] = d.encode("utf-8")
    tmp = pfad + ".tmp"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        for n, b in inhalt.items():
            z.writestr(n, b)
    shutil.move(tmp, pfad)


word_zusammenhalten(os.path.join(AUS, NAME + ".docx"))
print("fertig:", AUS)
