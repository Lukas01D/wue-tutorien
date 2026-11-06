# Gestaltungsentwürfe für die Kaffee-Simulation: Bericht

> Nach `simulation/DESIGN_AUFTRAG.md`, Stand 06.11.2026, Zweig `claude/simulation-design-assignment-w01on3`. Grundlage: gebauter Stand `da7deb1`. Die Analyse und die drei Richtungen stehen ausführlich in `simulation/design_entwuerfe/RICHTUNGEN.md`; die TL hat sie am 06.11.2026 mit drei Anpassungen freigegeben (B: rechteckige, möglichst große Diagrammfläche; Schriften nur mit den gebrauchten Zeichen und frühe Größenprüfung; Ersatz für nicht verfügbare Schriften nennen).
>
> **Unvoreingenommen:** Nicht geöffnet habe ich die im Auftrag ausgeschlossenen Dateien und Ordner, die heutige `stil.css` und die heutige Seite im Browser. Die heutige Seite habe ich erst in Schritt 6 fotografiert, als alle drei Entwürfe fertig waren. Gelesen habe ich Markup, Texte und Oberflächenskript, weil die Entwürfe darauf aufbauen.

**Vergleichsseite:** `simulation/design_entwuerfe/VERGLEICH.html` (offline, Bilder eingebettet).

## 1 Die drei Richtungen

| | A „Messprotokoll“ | B „Kaffeehaus“ | C „Hörsaal“ |
|:--|:--|:--|:--|
| Haltung | sachlich wie ein Versuchsprotokoll: Papier, Tinte, Millimeterraster, nummerierte Schritte | warm und ruhig: Milchschaum, Crema, Espresso, große weiche Karten | für Beamer und letzte Reihe: Weiß, Schwarz, Signalblau, große Schrift, dicke Linien |
| Laptop und Beamer | links die Frage als Spalte mit Schrittleiste, rechts das Diagramm auf Millimeterpapier | eine breite Mittelspalte; vor der Vorhersage die Startkarte oben, danach das Diagramm über die ganze Breite | Diagramm über zwei Drittel links, Frage und Schrittleiste rechts; nach der Vorhersage bleibt die Frage rechts neben Vertiefung und Messblatt |
| Kernzahlen ϑ₁, ϑ₂, Δ | kleine Messwerttabelle in Festbreitenschrift über dem Diagramm | große Serifenzahlen unter dem Diagramm | drei große Kacheln über dem Diagramm, Δ blau hinterlegt |
| Startkarte | Kästchenzeilen, Formularfelder mit Unterstrich | drei breite Kacheln, gewählte Kachel in Espresso gefüllt | dicke Auswahlblöcke, gewählter Block blau mit Haken |
| Regler | Lineal mit Skalenstrichen | dicke Spur mit Verlauf ins Karamell, runder Griff | schwarze Spur, Griff 34 px, Plus und Minus 52 px |
| Reiter | Karteireiter | Pillen im Segmentschalter | über die volle Breite, blauer Balken |
| Schriften (alle SIL OFL 1.1) | IBM Plex Sans, IBM Plex Mono, IBM Plex Math | Fraunces, Source Sans 3, STIX Two Math | Atkinson Hyperlegible Next, Fira Math; für vier Zeichen (˙ ₁ ₂ ↔) eine Teilmenge von Fira Sans |
| Seitengröße | 343 169 Bytes | 373 303 Bytes | 308 511 Bytes |

Zum Vergleich: der heutige Stand hat 399 063 Bytes. Die Schriften sind auf die gebrauchten Zeichen gekürzt (124 Textzeichen, die Formelzeichen und die kursiven Formen der einzeln gesetzten Buchstaben); Formelschriften behalten nur die Hoch- und Tiefstellung (`ssty`) und die MATH-Tabelle. Schriften zusammen: A 77 kB, B 100 kB, C 51 kB, heute 122 kB.

**Abweichungen vom freigegebenen Plan.** B wie von der TL angepasst: rechteckige Fläche statt runder Form. C: Die Kernzahlen stehen als Kacheln über dem Diagramm statt daneben, weil das Skript die Diagrammbreite aus seinem Behälter misst und eine Spalte daneben einen weiteren Eingriff ins Skript gebraucht hätte. Sonst wie in `RICHTUNGEN.md`.

**Schriftquellen.** Alle Schriften waren frei verfügbar, ein Ersatz war nicht nötig. Sie kommen aus dem Google-Fonts-Repository (`github.com/google/fonts`, Ordner `ofl/`) und dem IBM-Plex-Repository (`github.com/IBM/plex`, Plex Math), nicht aus npm-Paketen; die variablen Schriften sind mit fontTools auf feste Schnitte gebracht. Einzige Ergänzung: Atkinson Hyperlegible Next hat weder Griechisch noch tiefgestellte Ziffern noch ↔; Griechisch liefert Fira Math, die vier übrigen Zeichen eine 900-Byte-Teilmenge von Fira Sans. Lizenztexte liegen je Entwurf in `src/schriften/` und stehen als Kommentar in der Seite.

**Farben im Diagramm.** Die Texte legen die Codierung fest („braune Linie ist Tasse 1“, „schwarze gestrichelte Tasse 2“, „graue gepunktete Linie“ für den Raum, „blass“ für den Vergleichslauf). Alle drei Entwürfe halten das ein: Tasse 1 ist ein Braunton, Tasse 2 nahezu schwarz, die Zeichenfläche hell. Kontraste gegen die Zeichenfläche (WCAG, Ziel 3:1 für Linien, 4,5:1 für Text):

| | Tasse 1 | Beschriftung Tasse 1 | Tasse 2 | Raumlinie | Achsenschrift | Becher 3 | Vorhersage-Kasten (Schrift) |
|:--|:--|:--|:--|:--|:--|:--|:--|
| A | 6,7 | 8,1 | 16,3 | 4,8 | 7,4 | 8,0 | 9,3 |
| B | 5,1 | 6,2 | 17,1 | 4,2 | 6,6 | 6,4 | 9,4 |
| C | 8,4 | 9,8 | 19,4 | 4,8 | 9,8 | 8,7 | 8,7 |

Braun gegen Schwarz trennt der Farbprüfer des Skills „dataviz“ auch bei Farbfehlsichtigkeit deutlich (ΔE 22 bis 30); dazu kommen Linienart und Direktbeschriftung.

## 2 Wie gebaut wurde (und was sich nicht geändert hat)

- **Nur die Gestaltung:** `simulation/design_entwuerfe/tests/vergleich_kern_texte.py` belegt für jede Fassung: Rechenkern (`modell.js`, `erweiterung.js`, `hilfen.js`), Texte und Reglerdaten sind **bytegleich** mit `simulation/site/index.html`; das Oberflächenskript unterscheidet sich nur an den Stellen aus `gestaltung_patch.py`.
- **Bauen:** `python3 simulation/design_entwuerfe/bauen_entwurf.py <messprotokoll|kaffeehaus|hoersaal>`; eine Kopie von `site/bauen.py` mit sechs gekennzeichneten Änderungen (E1 bis E6 im Kopf der Datei). Ein Entwurf besteht nur aus `src/stil.css`, `src/vorlage.html` (Farbe der Browserleiste, Symbol, Schalter für die Schrittleiste), `src/schriften.json` und den Schriften. Alles andere kommt unverändert aus `simulation/site/src/`.
- **Gemeinsame Pflichtteile** (`gemeinsam.css`): Bildschirmleser-Klassen, Sprungverweis, am Handy nach der Freigabe die Reihenfolge Diagramm, Frage, Regler (M-6) mit Anheften, reduzierte Bewegung, erzwungene Farben, und die Zuordnung der Diagrammfarben.
- **Diagrammfarben ohne Eingriff ins Skript:** Das Skript schreibt feste Farbwerte als SVG-Attribute; CSS geht Attributen vor. `gemeinsam.css` ordnet jedem festen Wert über einen Attributselektor eine Variable des Entwurfs zu.
- **Änderungen am Oberflächenskript** (`gestaltung_patch.py`, beim Bau angewendet, jede Stelle muss genau passen):
  - G1: Diagrammgröße, Diagrammschrift und Ränder aus CSS-Variablen, mit den heutigen Werten als Vorgabe;
  - G2: geschätzte Zeichenbreite für die Kollisionsprüfung der Beschriftungen aus einer CSS-Variablen, passend zur Schrift;
  - G3: Schrittleiste (Start, Zeitpunkt, Versuch, Vertiefung) aus vorhandenen Textschlüsseln, nur in A und C, für Bildschirmleser verborgen, weil die Frageleiste den Schritt schon in Worten nennt.

## 3 Testergebnisse

Alle Läufe im Cloud-Container mit Chromium (Playwright); WebKit ist hier nicht verfügbar, ein Gerätetest auf dem iPhone steht für jeden Entwurf noch aus (wie beim gebauten Stand). Ergebnisdateien: `simulation/design_entwuerfe/<entwurf>/test_ergebnisse/`. Alles neu ausführen: `bash simulation/design_entwuerfe/tests/alle_pruefen.sh`.

| Prüfung | A Messprotokoll | B Kaffeehaus | C Hörsaal |
|:--|:--|:--|:--|
| Rechenkern `simulation/tests/test_kern.py --html` (unverändert) | 135 von 135 | 135 von 135 | 135 von 135 |
| Browsertests (Kopie mit A1 bis A3, sonst unverändert), darin axe-core 4.14.0 (WCAG 2.0, 2.1, 2.2 A und AA) in P0, P2, Vertiefung, DE und EN, 1366 und 390 px | 95 von 95 | 95 von 95 | 95 von 95 |
| Rechenkern, Texte, Reglerdaten bytegleich zum Stand (`vergleich_kern_texte.py`) | ja | ja | ja |
| Größe unter 450 000 Bytes | 343 169 | 373 303 | 308 511 |
| Zeichenprüfung beim Bau (jedes Zeichen in einer eingebetteten Schrift) | ohne Warnung | ohne Warnung | ohne Warnung |

Die Browsertests decken unter anderem ab: Sperre vor der Vorhersage (keine Ergebniszahl im DOM), alle Zahlen gegen die Python-Referenz, Regler, Kurslink, Messblatt, Sprachwechsel, kein Querscrollen von 320 bis 1920 px und bei 200 % Text, Zielgrößen (44 px, Textverweise 24 px), sichtbarer Fokus, Reiter mit Tastatur, Anheften am Handy (höchstens 45 % der Höhe), Ladezeit und Reaktionszeit der Regler.

**Anpassungen im Browsertest** (`simulation/design_entwuerfe/tests/browsertest_entwurf.js`, im Kopf begründet):
- A1: Die Prüfungen „Schriften eingebettet“ und „Schrift geladen“ fragen fest nach Fira Sans und Fira Math. Die Entwürfe betten andere freie Schriften ein, daher kommen die Familiennamen aus Umgebungsvariablen. Geprüft wird weiter dasselbe: woff2 als data-URL, Text- und Formelschrift geladen.
- A2: Der Fettschnitt ist in A und B 600 statt 700; geprüft wird der eingebettete Fettschnitt.
- A3: nur Pfade (Erwartungswerte, axe-core, Ergebnisdatei).

**Was die Tests während der Arbeit gefunden haben** (behoben, dann erneut geprüft): eine breite Formel im Reiter „So rechnet der Code“ lief bei 320 px über (Formelblöcke sind jetzt scrollbar, in `gemeinsam.css`); das angeheftete Diagramm war am kleinen Handy höher als 45 % (alle drei: niedrigere Diagrammhöhe am Handy, Kernzahlen einzeilig); in B lief die Rechenwerte-Tabelle bei 200 % Text 33 px über.

## 4 Stärken und Schwächen

Bewertet an den Bildern in `VERGLEICH.html` und an den Tests. Die heutige Seite (Variante 0) habe ich erst danach angesehen; sie steht zum Vergleich in der letzten Zeile.

**A Messprotokoll**
- Handy: kompakt, Kernzahlen als schmale Messwertzeile über dem angehefteten Diagramm; die Schrittleiste zeigt den Ablauf auf einen Blick. Text 16 px, etwas kleiner als B und C.
- Beamer: Frage links, Diagramm samt Kernzahlen vollständig rechts daneben, ohne Scrollen. Schrift im Diagramm 12 px Festbreite, aus der letzten Reihe eher klein.
- Diagramm: Millimeterraster hilft beim Ablesen und passt zum Versuch; Zahlen in Festbreite springen beim Ziehen nicht. Das Raster macht die Fläche etwas unruhiger.
- Barrierefreiheit: alle Kontraste hoch (Tasse 1 6,7:1); die Auswahl ist als Kästchen gezeichnet, technisch bleiben es Optionsfelder (Bildschirmleser richtig), Sehende könnten aber Mehrfachauswahl erwarten.

**B Kaffeehaus**
- Handy: am einladendsten, große Kacheln, ruhige Abstände; Kernzahlen groß in Serifen unter dem Diagramm.
- Beamer: nach der Vorhersage steht das Diagramm über die volle Breite oben, mit den Kernzahlen darunter; das größte Diagramm der vier Fassungen. Die Frage steht darunter: Wer am Laptop Frage 1 liest, scrollt am Diagramm vorbei.
- Diagramm: rechteckig auf Crema, nur waagerechte Linien, Kurven 3,2 px; sehr gut lesbar.
- Barrierefreiheit: alle Werte über der Grenze, aber mit dem geringsten Abstand (Tasse 1 5,1:1, Raumlinie 4,2:1). Das Umstellen der Reihenfolge am Laptop nutzt den CSS-Selektor `:has()` (Chrome ab 105, Safari ab 15.4, Firefox ab 121); ältere Browser zeigen die Frage oben, sonst gleich. Größte Datei (373 kB, Grenze 450 kB).

**C Hörsaal**
- Handy: größte Ziele (48 bis 56 px), dicke Auswahlblöcke, Kernzahlen als drei Kacheln im angehefteten Bild, Schrittleiste mit Nummern.
- Beamer: Kernzahlen in Kacheln mit 34 bis 41 px großen Zahlen, Diagramm mit 4-px-Kurven und fetter Achsenschrift, Frage rechts daneben; alles Wesentliche ohne Scrollen sichtbar, auch aus der letzten Reihe.
- Diagramm: höchste Kontraste (Tasse 1 8,4:1, Tasse 2 19,4:1), Beschriftung fett.
- Schwächen: wirkt nüchtern; überall fett schwächt die Rangordnung etwas; die Null von Atkinson Hyperlegible ist durchgestrichen („6Ø“), das ist Absicht der Schrift (0 und O unterscheiden), wirkt in Temperaturen aber ungewohnt; eine Variante ohne Strich hat die Schrift nicht. Ausweg wäre eine andere Textschrift bei sonst gleicher Gestaltung. Nach dem Öffnen der Vertiefung bleibt am Laptop rechts unten Fläche frei.
- Kleinste Datei (309 kB).

**Variante 0 (heutiger Stand), zum Vergleich**
- Handy: solide und ruhig; Kernzahlen als Zeile, die Vorhersage als Kasten unter dem Diagramm.
- Beamer: Nach der Vorhersage steht die Frage über die ganze Breite oben, das Diagramm ist nur zur Hälfte im Bild. Das ist der deutlichste Unterschied: Alle drei Entwürfe zeigen am Beamer Diagramm und Kernzahlen ganz.

## 5 Empfehlung

**Ich empfehle C „Hörsaal“.** Begründung: Die Seite wird im Hörsaal am Handy zu zweit und am Beamer gebraucht. C ist dafür am stärksten: größte Ziele und Schrift, höchste Kontraste im Diagramm, Kernzahlen und ganzes Diagramm am Beamer ohne Scrollen, Schrittleiste für „alle bei Frage 1?“. Dazu ist C die kleinste Datei. Alle Prüfungen bestehen alle drei; der Unterschied liegt in Lesbarkeit auf Abstand und Bedienung.

Zwei Punkte würde ich vor der Übernahme von C noch entscheiden lassen:
1. **Null mit Strich:** Stört er die TL, Atkinson durch eine Schrift mit normaler Null ersetzen (zum Beispiel Source Sans 3 aus B oder Fira Sans vom heutigen Stand); Aufwand gering, Gestaltung sonst gleich.
2. **Wärme:** Wünscht die TL mehr Freundlichkeit, lässt sich C mit den Farben und der Überschriftenschrift von B mischen (Anordnung, Größen und Kacheln aus C; Crema, Espresso und Fraunces aus B). Dann Kontraste neu prüfen, weil B knapper ist.

Wenn die TL den Charakter wichtiger findet als die Fernwirkung: B ist die schönste Fassung und hat das größte Diagramm, verlangt aber am Laptop Scrollen zwischen Diagramm und Frage.

## 6 Aufwand der Übertragung auf den korrigierten Stand

Ein Entwurf ist bewusst klein gehalten: eine CSS-Datei, eine Vorlage mit drei geänderten Zeilen, die Schriften und sieben Stellen im Oberflächenskript (`gestaltung_patch.py`). Für den korrigierten Stand von `claude/simulation-tool-kaffee-4kcacl`:

| Schritt | Aufwand |
|:--|:--|
| Korrigierte Quellen holen und mit `bauen_entwurf.py` bauen. Der Bau meldet jede Stelle aus `gestaltung_patch.py`, die nicht mehr genau passt, und jedes neue Zeichen ohne Schrift. | Minuten, wenn die Korrektur die sieben Stellen nicht berührt |
| Neue oder geänderte Elemente der Oberfläche (neue Klassen, neue Kästen) in der `stil.css` des Entwurfs gestalten; neue feste Farben im Diagramm in `gemeinsam.css` einer Variablen zuordnen. | je nach Korrektur 0,5 bis 2 Stunden |
| Neue Zeichen in den Texten: `schriften_teilen.py` neu laufen lassen (nur A und B; bei C die Ersatzteilmenge). | Minuten |
| Alle Tests mit der korrigierten Testsuite: die Anpassungen A1 bis A3 in die neue Fassung übernehmen, dann `alle_pruefen.sh`; Bilder neu. | etwa 1 Stunde, davon 30 min Laufzeit |
| Endgültige Übernahme in `simulation/site/`: `stil.css` und Schriften ersetzen, die drei Änderungen G1 bis G3 direkt in `oberflaeche.js` schreiben, in `bauen.py` die Schriftliste tauschen, in den Browsertests die Schriftnamen (A1, A2) ändern. | etwa 1 Stunde |

Zusammen etwa 2 bis 4 Stunden für den gewählten Entwurf, davon der größte Teil Prüfen. Mischen (zum Beispiel C mit Farben aus B) kostet zusätzlich etwa 1 Stunde für Farben und Kontrastprüfung. Ein Gerätetest auf dem iPhone bleibt wie beim gebauten Stand offen.

## 7 Dateien

| Pfad | Inhalt |
|:--|:--|
| `simulation/design_entwuerfe/RICHTUNGEN.md` | Analyse und drei Richtungen (Schritt 1 und 2) |
| `simulation/design_entwuerfe/<entwurf>/index.html` | lauffähige Fassung (bytegleich `Kaffee_Simulation.html`), dazu `BAUNACHWEIS.txt` |
| `simulation/design_entwuerfe/<entwurf>/src/` | `stil.css`, `vorlage.html`, `schriften.json`, Schriften mit Lizenz |
| `simulation/design_entwuerfe/<entwurf>/bilder/` | Bildschirmfotos der sechs Zustände (Gerätefaktor 2) |
| `simulation/design_entwuerfe/variante_0/bilder/` | dieselben Zustände für den heutigen Stand |
| `simulation/design_entwuerfe/VERGLEICH.html` | Vergleichsseite, alle vier nebeneinander |
| `simulation/design_entwuerfe/bauen_entwurf.py`, `gemeinsam.css`, `gestaltung_patch.py`, `schriften_teilen.py` | Bau |
| `simulation/design_entwuerfe/bilder_entwurf.js`, `vergleich_bauen.py`, `tests/` | Bilder, Vergleichsseite, Tests |
