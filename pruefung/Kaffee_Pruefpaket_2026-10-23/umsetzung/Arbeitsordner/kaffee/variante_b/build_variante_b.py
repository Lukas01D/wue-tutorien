# -*- coding: utf-8 -*-
"""Variante B des Kaffee-Aufgabenblatts (nur Einzelblatt, PDF und Word; Wunsch der TL vom 31.10.2026).

Reihenfolge: Grundlagen (Schild „instationär, global“ rechts, etwa 6 cm, Text fließt daneben und darunter weiter),
Lernziele, Einführung (Ausgangssituation, Abb. 1, Frage 1), Gegeben (Messung, Annahmen, Werte), Gesucht (Teile a bis g),
Hausaufgabe (wie im Einzelblatt A, aus hausaufgabe_verdunstung.md), Versuch als Messblatt auf eigener Seite.
Formelzeichen (R17): In Formeln steht T (Grundlagen, Annahmen, Teil b), Celsius-Werte heißen ϑ (Tabelle, Ergebnisse).
Ausgangssituation, Frage 1, Annahmen, Tabelle, Teile a bis g und Versuch werden aus sammlung/teile/t5a_kaffee.md
übernommen (gleiche Quelle wie Sammlung und Einzelblatt); geändert werden nur die Verweise auf „Aufgabe 1“
und das Formelzeichen in der Annahme zur Wärmeabgabe (T statt ϑ, wie in den Grundlagen).
Sammlung, Lösung und Einzelblatt (build_kaffee.py) bleiben unverändert.
Aufruf: python3 build_variante_b.py
"""
import os, re, shutil, subprocess, tempfile, zipfile

HIER = os.path.dirname(os.path.abspath(__file__))
KAFFEE = os.path.dirname(HIER)
W = os.path.dirname(KAFFEE)
REPO = os.path.abspath(os.path.join(W, "..", "..", "..", ".."))
B = os.path.join(HIER, "build")
NAME = "Kaffee_Aufgabe_Variante_B"
SCHILD = "Bilanzformen_kompakt_3_instationaer_global"
VORLAGE = os.path.join(REPO, "vorlagen", "bilanzformen", "kompakt")
KOPF_RECHTS = "Sommersemester 2027"

# Schild: PNG für Word, SVG als Vektor-PDF für LaTeX (Text in der SVG als Pfade, daher ohne Schriften umwandelbar)
os.makedirs(os.path.join(HIER, "grafik"), exist_ok=True)
shutil.copyfile(os.path.join(VORLAGE, SCHILD + ".png"), os.path.join(HIER, "grafik", SCHILD + ".png"))
try:
    import cairosvg
    cairosvg.svg2pdf(url=os.path.join(VORLAGE, SCHILD + ".svg"), write_to=os.path.join(HIER, "grafik", SCHILD + ".pdf"))
except ImportError:                                                         # ohne cairosvg: eingechecktes PDF verwenden
    assert os.path.exists(os.path.join(HIER, "grafik", SCHILD + ".pdf")), "pip install cairosvg"

# Aufgabentext aus der Sammlung zerlegen
with open(os.path.join(W, "sammlung", "teile", "t5a_kaffee.md"), encoding="utf-8") as f:
    QUELLE = f.read()


def zwischen(text, a, b):
    assert text.count(a) == 1 and text.count(b) >= 1, (a, b)
    i = text.index(a) + len(a)
    return text[i:text.index(b, i)].strip("\n")


AUSGANG = zwischen(QUELLE, "**[Ausgangssituation]{.underline}**\n\n", "**[Frage 1]")
FRAGE = zwischen(QUELLE, "**[Frage 1]{.underline}** (Vorab-Frage)\n\n", "<!-- T5_FRAGEN -->")
AUFGABE = zwischen(QUELLE, "**[Aufgabe 1]{.underline}** (neu)\n\n", "**[Versuch zu Aufgabe 1]")
VERSUCH = QUELLE[QUELLE.index("**[Versuch zu Aufgabe 1]"):].strip("\n")
MESSUNG = AUFGABE.split("\n\n", 1)[0]
assert MESSUNG.startswith("Um die Frage zu klären, messen Sie")
ANNAHMEN = zwischen(AUFGABE, "**Annahmen:**\n\n", "**Gegebene Größen:**")
TABELLE = zwischen(AUFGABE, "**Gegebene Größen:**\n\n", "**Aufgabenstellung:**")
TEILE = AUFGABE[AUFGABE.index("**Aufgabenstellung:**\n\n") + len("**Aufgabenstellung:**\n\n"):].strip("\n")
assert TEILE.startswith("a) ") and "\ng) " in TEILE

# Verweise auf „Aufgabe 1“ (gibt es in Variante B nicht mehr als Baustein)
assert FRAGE.count("bevor Sie Aufgabe 1 rechnen.") == 1
FRAGE = FRAGE.replace("bevor Sie Aufgabe 1 rechnen.", "bevor Sie rechnen.")
assert VERSUCH.count("**[Versuch zu Aufgabe 1]{.underline}**") == 1
VERSUCH = VERSUCH.replace("**[Versuch zu Aufgabe 1]{.underline}**", "**[Versuch]{.underline}**")
assert "Aufgabe 1" not in FRAGE + VERSUCH + TEILE + ANNAHMEN + AUSGANG
# Formelzeichen wie in den Grundlagen (R17): Formeln mit T, Celsius-Werte mit ϑ
ALT_ANNAHME = r"$\dot{Q}_{\mathrm{ab}} = kA\,(\vartheta - \vartheta_\mathrm{u})$"
assert ANNAHMEN.count(ALT_ANNAHME) == 1
ANNAHMEN = ANNAHMEN.replace(ALT_ANNAHME, r"$\dot{Q}_{\mathrm{ab}} = kA\,(T - T_\mathrm{u})$")
# Hausaufgabe: gleicher Text wie im Einzelblatt A
with open(os.path.join(KAFFEE, "hausaufgabe_verdunstung.md"), encoding="utf-8") as f:
    HAUSAUFGABE = f.read().strip("\n")
# Teil e mit Ergebniszeile nicht über den Seitenwechsel trennen (wie im Einzelblatt, Abnahme 3)
TEILE, _n = re.subn(r"(\n   \$Q_1 = [^\n]*\$)(\n)", r"\1`\\needspace{6\\baselineskip}`{=latex}\2", TEILE, count=1)
assert _n == 1

GRUNDLAGEN = r"""**[Grundlagen]{.underline}** (Energiebilanz: instationär, global)

::: umfliessen
**Voraussetzung:** Die Temperatur ist im ganzen Kontrollvolumen gleich (homogen) und ändert sich nur mit der Zeit. Das gilt, wenn der Inhalt ideal durchmischt ist oder wenn in einem Festkörper die Wärmeleitung Unterschiede viel schneller ausgleicht, als Wärme über die Oberfläche abgeht (Biot-Zahl $Bi \ll 1$, Foliensatz 02, Folie 16).

**Bilanz** für ein ruhendes Kontrollvolumen ohne innere Wärmequellen (Foliensatz 05, Folie 8), mit der inneren Energie eines inkompressiblen Stoffs mit konstanten Stoffdaten:
$$\frac{dU}{dt} = \dot{Q}_{zu} - \dot{Q}_{ab}, \qquad dU = m\,c_p\,dT$$
$m\,c_p$ (in J/K) ist die Wärmekapazität des Inhalts. Die Wärmeabgabe an die Umgebung beschreibt ein Wärmedurchgang:
$$\dot{Q}_{ab} = kA\,(T - T_u)$$
$kA$ (in W/K), das Produkt aus Wärmedurchgangskoeffizient $k$ und Fläche $A$, ist der abgegebene Wärmestrom je Kelvin Temperaturunterschied zur Umgebung; es fasst alle Wege nach außen zusammen. Temperaturdifferenzen sind in K und °C gleich; Werte in °C heißen auf dem Blatt $\vartheta$.

**Lösungsweg:** Eingesetzt entsteht eine gewöhnliche DGL erster Ordnung in der Zeit, $dT/dt = f(T)$. Trennung der Variablen: alle Terme mit $T$ auf eine Seite, $dt$ auf die andere, dann vom Anfang ($t = 0$, $T = T_0$) bis zur Zeit $t$ integrieren:
$$\int_{T_0}^{T} \frac{dT}{f(T)} = \int_{0}^{t} dt$$

![](grafik/""" + SCHILD + r""".png){width=6cm}
:::

"""

LERNZIELE = r"""**[Lernziele]{.underline}**

Nach diesem Tutorium können Sie …

- den Temperaturverlauf $T(t)$ einer ideal durchmischten Flüssigkeit, etwa Kaffee in einer Tasse, aus einer instationären globalen Energiebilanz berechnen.
- Abweichungen zwischen der Vorhersage des Modells und Ihren Messwerten (Versuch und Simulationstool) mit den Annahmen des Modells begründen.

"""

GESUCHT_SATZ = "Gesucht ist, welche Tasse nach einer Stunde wärmer ist, und warum. Die Teile a bis f bauen aufeinander auf, Teil g vertieft das Modell."

md = ("---\nlang: de\n---\n\n::: center\n**[Tutorium 5: Wärmebilanzen (instationär global)]{.underline}**\n:::\n\n"
      + GRUNDLAGEN + LERNZIELE
      + "**[Einführung]{.underline}**\n\n" + AUSGANG + "\n\n**Frage 1 (Vorab-Frage):**\n\n" + FRAGE + "\n\n"
      + "**[Gegeben]{.underline}**\n\n" + MESSUNG + "\n\n**Annahmen:**\n\n" + ANNAHMEN + "\n\n**Werte:**\n\n" + TABELLE + "\n\n"
      + "**[Gesucht]{.underline}**\n\n" + GESUCHT_SATZ + "\n\n" + TEILE + "\n\n" + HAUSAUFGABE + "\n\n"
      + "::: seitenumbruch\n:::\n\n" + VERSUCH + "\n")


def aufrecht(text):
    """Beschreibende Indizes in Formeln aufrecht setzen (Ä24), wie in build_kaffee.py; Größen als Index (p, v) und Zahlen bleiben."""
    paare = [("_{ab}", r"_{\mathrm{ab}}"), ("_{zu}", r"_{\mathrm{zu}}"), ("_{KV}", r"_{\mathrm{KV}}"),
             ("_{p,K}", r"_{p,\mathrm{K}}"), ("_{p,M}", r"_{p,\mathrm{M}}"), ("_{K,0}", r"_{\mathrm{K},0}"),
             ("_{M,h}", r"_{\mathrm{M,h}}")]

    def formel(m):
        f = m.group(0)
        for a, b in paare:
            f = f.replace(a, b)
        return re.sub(r"_([KMuBG])(?![A-Za-z])", r"_\\mathrm{\1}", f)
    return re.sub(r"\$\$.*?\$\$|\$[^$]+?\$", formel, text, flags=re.S)


md = aufrecht(md)
for a in (r"\dot{Q}_{\mathrm{zu}}", r"\dot{Q}_{\mathrm{ab}}", r"T_\mathrm{u}", "c_p"):
    assert a in md, a
assert "Formelsammlung" not in md and "Gl. 5.1" not in md               # gestrichen (D24)
assert "–" not in md and "—" not in md                                     # keine Gedankenstriche
with open(os.path.join(HIER, NAME + ".md"), "w", encoding="utf-8") as f:
    f.write(md)

RES = HIER + ":" + os.path.join(W, "sammlung")
# PDF: Pandoc erzeugt das LaTeX, XeLaTeX läuft hier. Pandocs Vorlage lädt babel mit bidi=default; das schaltet
# wrapfig aus (Schild landet am Ende). Bidi braucht nur Rechts-nach-links-Schrift, deshalb babel ohne diese Option.
tex = subprocess.run(["pandoc", NAME + ".md", "-s", "-t", "latex",
                      "-H", os.path.join(KAFFEE, "build", "kopf.tex"), "-H", os.path.join(B, "kopf_b.tex"),
                      "--lua-filter", os.path.join(B, "lehrstuhl_b.lua"),
                      "-V", "documentclass=article", "-V", "fontsize=11pt", "-V", "mainfont=Carlito",
                      "-V", "mathfont=Latin Modern Math"], check=True, cwd=HIER, capture_output=True, text=True).stdout
assert tex.count(r"\usepackage[bidi=default]{babel}") == 1
tex = tex.replace(r"\usepackage[bidi=default]{babel}", r"\usepackage{babel}")
with tempfile.TemporaryDirectory() as tmp:
    with open(os.path.join(tmp, NAME + ".tex"), "w", encoding="utf-8") as f:
        f.write(tex)
    umgebung = dict(os.environ, TEXINPUTS=HIER + "//:" + os.path.join(W, "sammlung") + "//:")
    for _ in range(2):                                                      # zweiter Lauf für stabile Seitenumbrüche
        lauf = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", "-output-directory", tmp,
                               os.path.join(tmp, NAME + ".tex")], cwd=HIER, env=umgebung, capture_output=True, text=True)
        assert lauf.returncode == 0, lauf.stdout[-3000:]
    with open(os.path.join(tmp, NAME + ".log"), encoding="utf-8", errors="replace") as f:
        log = f.read()
    print("PDF: Zeilen mit Überlänge (Overfull \\hbox):", log.count("Overfull \\hbox"))
    for m in re.finditer(r"Overfull \\hbox \(([\d.]+)pt too wide\)[^\n]*\n([^\n]*)", log):
        print("   ", m.group(1), "pt:", m.group(2)[:100])
    shutil.copyfile(os.path.join(tmp, NAME + ".pdf"), os.path.join(HIER, NAME + ".pdf"))
subprocess.run(["pandoc", NAME + ".md", "-o", NAME + ".docx",
                "--reference-doc", os.path.join(KAFFEE, "build", "referenz_lehrstuhl.docx"),
                "--lua-filter", os.path.join(B, "lehrstuhl_b.lua"), "--resource-path", RES], check=True, cwd=HIER)


# Word-Nachbearbeitung wie in build_kaffee.py (Tabellen zusammenhalten, Breiten der Wertetabelle, Messtabelle,
# fette Marken), dazu das Schild als umflossenes Bild rechts im ersten Absatz der Grundlagen
def keep(par):
    if "<w:keepNext/>" in par:
        return par
    if "<w:pPr>" in par:
        return re.sub(r'(<w:pPr>(?:<w:pStyle w:val="[^"]*"\s*/>)?)', r"\1<w:keepNext/>", par, count=1)
    return par.replace("<w:p>", "<w:p><w:pPr><w:keepNext/></w:pPr>", 1)


def tabelle(m):
    t = m.group(0)
    zeilen = re.findall(r"<w:tr>.*?</w:tr>|<w:tr .*?</w:tr>", t, flags=re.S)
    for z in zeilen[:-1]:
        t = t.replace(z, re.sub(r"<w:p>.*?</w:p>", lambda mm: keep(mm.group(0)), z, flags=re.S), 1)
    t = t.replace("<w:trPr>", "<w:trPr><w:cantSplit/>")
    t = re.sub(r"<w:tr>(?!<w:trPr>)", "<w:tr><w:trPr><w:cantSplit/></w:trPr>", t)
    if "Messung in Tasse 2" in t:                                           # Wertetabelle: Spalten 3,9 / 4,1 / 3,9 / 4,1 cm (Ä22)
        t = re.sub(r'<w:tblW w:type="pct" w:w="\d+" />', '<w:tblW w:type="dxa" w:w="9070" />', t, count=1)
        t = t.replace("<w:tblLook ", '<w:tblLayout w:type="fixed" /><w:tblCellMar><w:left w:w="80" w:type="dxa" />'
                      '<w:right w:w="80" w:type="dxa" /></w:tblCellMar><w:tblLook ', 1)
        t = re.sub(r"<w:tblGrid>.*?</w:tblGrid>", '<w:tblGrid><w:gridCol w:w="2211" /><w:gridCol w:w="2324" />'
                   '<w:gridCol w:w="2211" /><w:gridCol w:w="2324" /></w:tblGrid>', t, count=1, flags=re.S)
    if "Milch sofort" in t:                                                 # Messtabelle: Zeilen mindestens 10 mm hoch
        t = t.replace("<w:trPr><w:cantSplit/>", '<w:trPr><w:cantSplit/><w:trHeight w:val="567" w:hRule="atLeast"/>')
    return t


pfad = os.path.join(HIER, NAME + ".docx")
with zipfile.ZipFile(pfad) as z:
    inhalt = {n: z.read(n) for n in z.namelist()}
d = inhalt["word/document.xml"].decode("utf-8")
d = re.sub(r"<w:tbl>.*?</w:tbl>", tabelle, d, flags=re.S)
d = re.sub(r"<w:tblHeader[^>]*/>", "", d)


def umfliessen(m):
    """Schild: eingebettetes Bild (wp:inline) als Bild rechts am Rand, Text links daneben (wp:anchor, wrapSquare)."""
    innen = m.group(1)
    extent = re.search(r"<wp:extent [^>]*/>", innen).group(0)
    effekt = re.search(r"<wp:effectExtent [^>]*/>", innen)
    rest = innen.replace(extent, "", 1).replace(effekt.group(0), "", 1) if effekt else innen.replace(extent, "", 1)
    return ('<wp:anchor distT="0" distB="72000" distL="126000" distR="0" simplePos="0" relativeHeight="251658240" '
            'behindDoc="0" locked="0" layoutInCell="1" allowOverlap="0"><wp:simplePos x="0" y="0" />'
            '<wp:positionH relativeFrom="margin"><wp:align>right</wp:align></wp:positionH>'
            '<wp:positionV relativeFrom="paragraph"><wp:posOffset>36000</wp:posOffset></wp:positionV>'
            + extent + '<wp:effectExtent l="0" t="0" r="0" b="0" /><wp:wrapSquare wrapText="left" />' + rest + "</wp:anchor>")


k = d.index("Voraussetzung:")
anfang = max(d.rfind("<w:p>", 0, k), d.rfind("<w:p ", 0, k))
ende = d.index("</w:p>", k)
absatz_g, _n = re.subn(r"<wp:inline[^>]*>(.*?)</wp:inline>", umfliessen, d[anfang:ende], count=1, flags=re.S)
assert _n == 1, "Schild nicht im ersten Absatz der Grundlagen"
d = d[:anfang] + absatz_g + d[ende:]
muster = re.compile(r"^(Werte|Annahmen|Frage \d|Grundlagen|Lernziele|Nach diesem Tutorium|Einführung|Gegeben|Gesucht|Versuch|Hausaufgabe|Um die Frage zu klären)")


def absatz(m):
    par = m.group(0)
    text = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", par)).strip()
    if muster.match(text) or ("<pic:pic" in par and not text):
        return keep(par)
    return par


teile = re.split(r"(<w:tbl>.*?</w:tbl>)", d, flags=re.S)
for k in range(0, len(teile), 2):
    teile[k] = re.sub(r"<w:p>(?:(?!</w:p>).)*?</w:p>|<w:p .*?</w:p>", absatz, teile[k], flags=re.S)
d = "".join(teile)
# Aufzählungspunkte (Teile a bis g mit Ergebniszeile, Annahmen, Lernziele) nicht über den Seitenwechsel trennen
d = re.sub(r"<w:pPr>((?:(?!</w:pPr>).)*?<w:numPr>)", lambda m: m.group(0) if "<w:keepLines/>" in m.group(1) else "<w:pPr><w:keepLines/>" + m.group(1), d, flags=re.S)
inhalt["word/document.xml"] = d.encode("utf-8")
if "word/numbering.xml" in inhalt:                                          # Marken a), b), … fett (Ä20)
    nb = inhalt["word/numbering.xml"].decode("utf-8")
    nb = re.sub(r'(<w:lvl w:ilvl="\d+">(?:(?!</w:lvl>).)*?<w:numFmt w:val="(?!bullet)[^"]+" />(?:(?!</w:lvl>).)*?)</w:lvl>',
                r"\1<w:rPr><w:b /><w:bCs /></w:rPr></w:lvl>", nb, flags=re.S)
    inhalt["word/numbering.xml"] = nb.encode("utf-8")
with zipfile.ZipFile(pfad + ".tmp", "w", zipfile.ZIP_DEFLATED) as z:
    for n, b in inhalt.items():
        z.writestr(n, b)
shutil.move(pfad + ".tmp", pfad)
print("fertig:", NAME)
