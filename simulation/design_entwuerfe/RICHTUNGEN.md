# Gestaltungsentwürfe Kaffee-Simulation: Analyse und drei Richtungen

> Schritt 1 und 2 nach `simulation/DESIGN_AUFTRAG.md`, Stand 06.11.2026. Von der TL am 06.11.2026 freigegeben mit drei Anpassungen (B: rechteckige, möglichst große Diagrammfläche statt runder Form; Schriften nur mit den gebrauchten Zeichen, Größe früh prüfen; Ersatzschriften nennen). Umsetzung und Abweichungen: `simulation/DESIGN_ENTWUERFE.md`. Grundlage: Stand `da7deb1` (Markup, Texte, Diagrammcode, `ZUSTAENDE.md`, `KONZEPT.md` Abschnitte 2, 3, 6). Nicht geöffnet: die im Auftrag ausgeschlossenen Dateien und Ordner, die heutige `stil.css` und die heutige Seite im Browser (die kommt erst in Schritt 6).

## 1 Gestaltungsanalyse

**Was die Seite auf einen Blick vermitteln muss**

1. *Was jetzt zu tun ist:* eine Frage, eine Eingabe, ein Knopf. Im Hörsaal entscheidet die erste Sekunde, ob ein Paar loslegt. Die Frage steht deshalb vor allem anderen, die Auswahl ist groß und eindeutig, der Knopf „Vorhersage festhalten“ ist der einzige starke Farbfleck.
2. *Das Diagramm als Antwort:* nach der Vorhersage ist das Diagramm das Ereignis. Zwei Kurven, zwei Mischsprünge, ein Schnittpunkt, die Raumlinie, der Kasten mit der eigenen Vorhersage. Dazu die drei Kernzahlen ϑ₁, ϑ₂ und Δ, groß und neben oder über dem Diagramm.
3. *Wo man im Ablauf steht:* Start, Frage 1, Frage 2, dann Vertiefung. Ein sichtbarer Fortschritt hilft dem Paar und der Tutorin am Beamer („alle bei Frage 1?“).

**Feste Bindungen aus den Texten (gelten für jeden Entwurf).** Die Texte, die nicht geändert werden dürfen, legen die Codierung des Diagramms fest: „braune Linie ist Tasse 1“, „schwarze gestrichelte Tasse 2“, „graue gepunktete Linie“ für den Raum, „kurze gepunktete Striche“ für die Mischsprünge, Kreis für den Schnitt, Kreis, Quadrat und Dreieck für die Becher, „beschrifteter Kasten“ für die Vorhersage, „blass“ für den gemerkten Lauf, zwei verschiedene Schraffuren für die Teilflächen. Folgen: Die Zeichenfläche des Diagramms bleibt in allen Entwürfen hell (eine schwarze Kurve auf dunklem Grund ginge nicht), Tasse 1 bleibt ein Braunton, Tasse 2 nahezu schwarz. Gestalten lassen sich Farbton und Stärke, Raster, Achsen, Beschriftungsschrift, Kernzahlen, Rahmen und Fläche um das Diagramm.

**Was am Handy im Hörsaal schwierig ist**

- *Wenig Höhe:* Frage, Diagramm und Regler passen bei 390 × 844 nicht gleichzeitig auf den Schirm. In Frage 1 muss man den Regler bewegen und die Kurven sehen. Der Regler gehört deshalb dicht unter das Diagramm, die Kernzahlen gehören in das Bild des Diagramms.
- *Daumen und Enge:* zwei Personen, ein Gerät, oft in der Hand des Nachbarn. Zielgrößen ab 44 px, Auswahl als ganze Fläche statt kleiner Kreise, Regler mit großem Griff und Plus und Minus.
- *Licht und Blickwinkel:* helle Hörsäle, schräger Blick auf das Handy des anderen. Kurven mindestens 2,5 px, Beschriftung im Diagramm nicht unter 11 px (Ziel 12 bis 13 px), keine hellgrauen Texte.
- *Textmenge:* die Fragen sind lang (bis 50 Wörter) und mit Formeln. Zeilenlänge, Zeilenabstand und klare Absätze zählen mehr als Zierrat. Englisch läuft etwas länger als Deutsch; nichts darf auf die Textlänge einer Sprache gebaut sein.
- *Beamer 1280 × 720:* wenig Höhe, Ansicht aus 10 bis 15 m. Das Diagramm braucht dort die Höhe, Bedienelemente rücken zur Seite.

## 2 Drei Richtungen

Gemeinsam für alle drei: Tasse 1 braun und durchgezogen, Tasse 2 nahezu schwarz und gestrichelt, Raum grau gepunktet (Texte), Direktbeschriftung der Kurven wie im heutigen Code, Fokusrahmen mindestens 3 px, Zielgrößen mindestens 44 px, `prefers-reduced-motion` schaltet jede Bewegung ab. Die Diagrammfarben stehen heute fest im Skript; für die Entwürfe bekommen die SVG-Elemente Klassen, die Farben setzt dann die CSS des Entwurfs (kleine Änderung am Markup, Rechnung und Texte unberührt).

Kontrast nach WCAG 2.x (Verhältnis gegen Seitengrund und gegen die Kartenfläche). Kurven und Bedienränder brauchen 3:1, Text 4,5:1. Der Farbprüfer des Skills „dataviz“ meldet für Braun gegen Schwarz eine ausreichende Trennung auch bei Farbfehlsichtigkeit (ΔE 22 bis 30); seine Meldungen „Helligkeitsband“ und „Buntheit“ für die schwarze Kurve sind gewollt, weil der Text „schwarz“ vorschreibt, und werden durch die Linienart ausgeglichen.

### A „Messprotokoll“

**Idee.** Die Seite sieht aus wie ein sauber geführtes Versuchsprotokoll: Papier, Tinte, Millimeterraster, nummerierte Schritte. Sie nimmt die Studierenden als Ingenieurinnen und Ingenieure ernst, die eine Messung auswerten, und ordnet alles in klare Zeilen und Spalten. Zahlen stehen in einer Festbreitenschrift, damit sie beim Ziehen am Regler nicht springen.

| Rolle | Farbe | Kontrast Grund / Karte |
|:--|:--|:--|
| Papier (Grund) | `#f6f3ea` | |
| Karte | `#fffdf8` | |
| Tinte (Text, Tasse 2) | `#1c1f24` | 14,9 / 16,3 |
| Text leise | `#4f5560` | 6,8 / 7,4 |
| Akzent Tintenblau (Knöpfe, Fokus, Vorhersage) | `#1d4f91` | 7,3 / 8,0; Weiß darauf 8,1 |
| Tasse 1 Braun | `#8a4a17` | 6,2 / 6,7 |
| Raumlinie Grau | `#767164` | 4,4 / 4,8 |
| Raster (nur Zierde, keine Information) | `#d8d1c0` | 1,4 / 1,5 |
| Fehler / richtig | `#a3261b` / `#1f6b3a` | 6,6 / 5,9 |

**Schriften.** IBM Plex Sans (Text, 400, 600, kursiv), IBM Plex Mono (Zahlen, Rechenwerte, Achsen), Formeln in IBM Plex Math (frei verfügbar, geprüft). Alle SIL OFL.

**Wichtigste Entscheidungen.**
- *Diagramm:* Zeichenfläche mit feinem Millimeterraster (5er und 10er Linien), Achsenzahlen in Plex Mono, Kurven 2,5 px, Kernzahlen als kleine Messwerttabelle oben im Diagrammrahmen.
- *Startkarte:* wie ein Protokollkopf, Schritt „01 Vorhersage“, Auswahl als Kästchen mit ganzer Zeile als Ziel, Felder mit Unterstrich wie auf einem Formular.
- *Regler:* Lineal mit Skalenstrichen, Wert in Mono rechts daneben, Plus und Minus als eckige Tasten.
- *Reiter:* Karteireiter mit Kante, aktiver Reiter verbindet sich mit dem Inhalt. Ecken 2 px, kaum Schatten.
- *Laptop und Beamer:* links schmale Spalte mit dem Ablauf als nummerierte Schritte, rechts das Diagramm auf Raster.

### B „Kaffeehaus“

**Idee.** Warm, freundlich und erzählend: Milchschaum, Crema, Espresso. Die Seite lädt ein wie eine gute Karte im Café, mit großen weichen Karten, viel Luft und einer Serifenschrift für Überschriften, die an ein Lehrbuch mit Persönlichkeit erinnert. Sie setzt auf Ruhe statt Dichte: eine Sache nach der anderen, das Diagramm groß in der Mitte.

| Rolle | Farbe | Kontrast Grund / Karte |
|:--|:--|:--|
| Milchschaum (Grund) | `#fbf6ee` | |
| Karte | `#ffffff` | |
| Crema (Flächen, Diagrammgrund) | `#f3e6d3` | Fläche, keine Information |
| Espresso (Text, Hauptknopf) | `#2b1d14` / `#3b2416` | 15,2 / 16,3; Schrift `#fff8ee` auf Knopf 13,7 |
| Text leise | `#6a5646` | 6,4 / 6,9 |
| Tasse 1 Karamellbraun | `#9a5a22` | 5,1 / 5,4 |
| Tasse 2 | `#1f140d` | 16,8 / 18,0 |
| Raumlinie | `#857464` | 4,2 / 4,5 |
| Vorhersage, Fokus Pistazie | `#3f6b4f` | 5,7 / 6,1 |
| Fehler / richtig | `#a12a24` / `#2f6b45` | 6,8 / 5,9 |

**Schriften.** Fraunces (Überschriften, Titel, Kernzahlen), Source Sans 3 (Text, 400, 600, kursiv), Formeln in STIX Two Math. Alle SIL OFL.

**Wichtigste Entscheidungen.**
- *Diagramm:* auf einer runden Crema-Fläche, ohne Rahmen, nur waagerechte Hilfslinien, Kurven 3 px mit runden Enden, Kernzahlen in Fraunces groß unter dem Diagramm wie drei Preise auf einer Tafel.
- *Startkarte:* große Karte mit Überschrift in Fraunces, Auswahl als drei breite Kacheln untereinander (am Handy) mit Rand, gewählte Kachel gefüllt.
- *Regler:* dicke runde Spur, die sich bis zum Griff mit Karamell füllt, runder Griff 28 px, Wert als Etikett darüber.
- *Reiter:* Pillen in einer Leiste (Segmentschalter), aktiver Reiter in Espresso gefüllt. Ecken 16 bis 20 px, weiche Schatten.
- *Laptop und Beamer:* eine breite Mittelspalte, Diagramm und Kernzahlen oben, Erklärkästen darunter in zwei Spalten.

### C „Hörsaal“

**Idee.** Gebaut für die letzte Reihe und den Beamer: Weiß, Schwarz, ein kräftiges Signalblau, große Schrift, dicke Linien. Jede Fläche hat einen Zweck, Zierde gibt es keine; der Ablauf steht als große Schrittleiste über allem. Die Gestaltung folgt dem Grundsatz „lesbar aus 15 m und mit dem Daumen bedienbar“.

| Rolle | Farbe | Kontrast Grund / Fläche |
|:--|:--|:--|
| Grund | `#ffffff` | |
| Fläche | `#f1f3f6` | |
| Text, Tasse 2 | `#0b0d12` | 19,4 / 17,5 |
| Text leise | `#3d4452` | 9,8 / 8,8 |
| Signalblau (Knöpfe, Vorhersage, aktiver Schritt) | `#2335c8` | 8,7 / 7,8; Weiß darauf 8,7 |
| Tasse 1 Dunkelbraun | `#7a3d10` | 8,4 / 7,6 |
| Raumlinie | `#6b7280` | 4,8 / 4,4 |
| Fokus: schwarzer Rahmen 3 px mit gelbem Saum | `#0b0d12` + `#ffd60a` | Rahmen 19,4 (Saum nur Verstärkung) |
| Fehler / richtig | `#b0151f` / `#11683a` | 7,1 / 6,9 |

**Schriften.** Atkinson Hyperlegible Next (Text und Zahlen, 400, 700, kursiv; vom Braille Institute für Lesbarkeit entworfen, unterscheidet l, I und 1), Formeln in Fira Math (Griechisch fällt ebenfalls dorthin, weil Atkinson kein Griechisch hat). Alle SIL OFL.

**Wichtigste Entscheidungen.**
- *Diagramm:* so groß wie möglich, Kurven 4 px, Achsenschrift 13 bis 14 px, Beschriftungen fett. Kernzahlen als drei große Kacheln (ϑ₁, ϑ₂, Δ in 28 bis 40 px) neben dem Diagramm, am Handy als Leiste darüber.
- *Startkarte:* Schrittleiste „1 Start, 2 Frage 1, 3 Frage 2, 4 Vertiefung“ darüber, Auswahl als große Blöcke mit dickem Rand, gewählter Block blau gefüllt mit Haken.
- *Regler:* breite Spur 10 px, Griff 32 px, Plus und Minus als 52-px-Tasten, Wert groß daneben.
- *Reiter:* über die volle Breite, groß, aktiver Reiter mit 4-px-Balken unten. Ecken 6 px, keine Schatten.
- *Laptop und Beamer:* Diagramm nimmt etwa zwei Drittel der Breite, rechts Frage und Bedienung; am Beamer ohne Scrollen sichtbar: Frage, Diagramm, Kernzahlen.

## 3 Wie die Entwürfe gebaut werden

Je Entwurf ein Ordner `simulation/design_entwuerfe/<name>/` mit eigenem `src/` (nur die Dateien, die sich ändern: `stil.css`, Schriften, wo nötig `vorlage.html` und eine Kopie von `oberflaeche.js` mit Klassen an den SVG-Elementen) und einer Kopie von `bauen.py`, die fehlende Dateien aus `simulation/site/src/` nimmt. Rechenkern (`modell.js`, `erweiterung.js`), Texte und Regeldaten werden nicht kopiert, sondern unverändert mitgebaut; so ist die Übertragung auf den korrigierten Stand klein.
