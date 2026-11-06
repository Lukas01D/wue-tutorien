# Vorbild Lernzentrum v8: Werte, Aufbau, Fehler, Zuordnung

> Teil 1 des Baus nach `simulation/BAU_AUFTRAG.md`. Ausführliche Belege: `simulation/vorbild/gestaltungswerte_lernzentrum.md` (Werte mit Datei:Zeile, im Browser gemessen) und `simulation/vorbild/bekannte_fehler_lernzentrum.md` (Fehler F01 bis F34, Entscheidungen K1 bis K5, Gutachtenformat). Beide von Agenten zusammengetragen; die tragenden Werte hat Claude im Code nachgesehen (`design.css` Zeile 2, `simulation-layout.js` Zeile 10, `runde11.css` Zeilen 58 bis 120, `topic.js` Zeile 167, `i18n.js`).

## 1 Quelle

| Punkt | Wert |
|:--|:--|
| Repository | `Lukas01D/waermeuebertragung-lernzentrum`, nur gelesen |
| Tag | `hauptadresse-v8-2026-11-05` |
| Commit | c2af968fab5c883a52d8323771b7eebb5a969373 (05.11.2026, „Merge pull request #25 from Lukas01D/runde-12-v8-abnahme“) |
| Klon | flach und ausgedünnt unter `/home/user/lernzentrum_v8` (Pfade nach dem Bauauftrag); Betrachtungskopie von `dist/` getrennt im Arbeitsbereich |
| Live | Haupt- und Werkstattadresse am 05.11.2026 nur mit Anmeldung (401); deshalb lokal angesehen (`dist/` über einen lokalen Server, Python-Laufzeit vom Netz gesperrt, nur Darstellung) |
| Bilder | `simulation/bildschirmfotos/lernzentrum/` (Thema 1 und 2, DE und EN, 390 × 844 und 1366 × 768, je mehrere Bildschirmhöhen) |
| Gelesen | `docs/Stand_Lernzentrum.md` (Runden 10 bis 12), `docs/Leitfaden_Lerntexte_DE_EN.md` (Abschnitte 1 bis 4 und 8 selbst, übrige durch Agent), `runden/R12/AUFTRAG.md` (Aufgaben R12-03 bis R12-23 und Abnahme), `runden/R12/Runde12_Feedback_Lukas_2026-11-04.md`, `runden/R11/AUFTRAG.md` (durch Agent), `runden/R12/Runde12_Gutachten_Zusammenfuehrung.md`, `runden/OFFEN.md` und die drei Prüfberichte (durch Agent) |

## 2 Gestaltungswerte (wirksam in v8)

| Bereich | Wert | Fundstelle |
|:--|:--|:--|
| Farben | Marine `#102d49` (Seitenleiste, einzige dunkle Hauptaktion), `#173d5e` (Fokusring, aktive Umschalter, Regler), Überschriften und Reitertext `#39718e`, Text `#142337`, Nebentext `#5a6b7f`, Linien `#d8e1ea`, Flächen und Rechenwerte `#eef5fb`, Hellblau `#a9d5ef`; Fehler Rand `#b63434`, Text `#862828`; Tabellenkopf `#174d68` mit weißer Schrift; Vermutung richtig `#227b48`, falsch `#a23838`; keine Schatten | `design.css:2`, `:159` |
| Ecken | 4 px; Reiter oben 6 px | `design.css:2`, `runde11.css:98` |
| Schrift | Fira Sans 400, 400 kursiv, 600, 700; Formeln Fira Math; Fließtext 16 px, Zeilenhöhe 1,58 (in Reitern 1,65); h1 `clamp(1.9rem, 2.4vw, 2.5rem)` | `fonts.css`, `design.css` |
| Regler | Beschriftung 0,78 rem fett mit Formelzeichen und Einheit in eckigen Klammern („$T_\mathrm{W1}$ [°C]“), Fragezeichen-Hilfe rechts, Schieberegler und Zahlenfeld 0,83 rem in einer Zeile, Raster drei Spalten | `pilot.css`, `runde11.css` |
| Rechenwerte | Kasten `#eef5fb` rechts neben den Reglern, zwei Spalten, Werte 0,85 rem, Gewicht 650, gleich breite Ziffern; Einheiten als Brüche | `runde10.css` |
| Bild | höchstens 780 px breit; v8 als Rasterbild 1560 × 720 px | `simulation-layout.js:10` |
| Umbrüche | ab 1200 px: Raster `minmax(0,1fr) 128px 180px`, Bild über zwei Spalten, Knöpfe gestapelt in 180 px, Regler darunter in drei Spalten, Rechenwerte rechts; 768 bis 1199 px: Bild links, Knöpfe 180 px rechts, Rest darunter; bis 767 px: eine Spalte, Bild oben und beim Scrollen angeheftet; bis 920 px Seitenleiste als Schublade | `runde11.css:58`, `:69`, `:79` |
| Knopfrangfolge | 1 „Berechnen“ Marine mit weißer Schrift (einzige dunkle Hauptaktion); 2 „Standardwerte“ `#eef5fb`, Schrift `#39718e`, Rand `#c9dfed`; 3 Umschalter aktiv `#d9edf9`, Rand `#93bbd4`, 2 px unten `#39718e`; 4 schlichte Knöpfe in Reitern; 5 Textknopf „ohne Vermutung aufdecken“ | `design.css:323` |
| Reiter unter der Simulation | drei Reiter als Raster mit drei Spalten (auch am Handy, kein Wischen), mindestens 44 px hoch, 13 px, Gewicht 600; gewählter Reiter weiß mit 3 px Linie oben in `#39718e`, mit der Fläche darunter verbunden; nicht gewählte `#edf2f6`; 8 px Abstand; `role="tablist"`, Pfeiltasten, Pos1, Ende | `runde11.css:97` bis `:100`, `topic.js:167` |
| Formelsatz | eigener Umsetzer nach MathML (kein KaTeX); Formelzeichen und Einheiten vorläufig fett über einen zentralen Schalter (K1); Einheiten im Satz als kleiner Bruch, Zeilenabstand unverändert (K3); im Satz „in“, eckige Klammern nur an Reglern, Achsen, Tabellenköpfen (K2); Punkt über $Q$ als eigene Fläche (N1) | `math.js`, `typeset.css`, Leitfaden 2 und 3 |
| Zahlen | Deutsch `de-DE` (Dezimalkomma, Tausenderpunkt), Englisch `en-GB` (Dezimalpunkt); Eingabefelder nehmen Komma oder Punkt und lehnen Tausendertrennung ab | `i18n.js`, `numeric-input.js` |

## 3 Aufbau der Simulationsseite nach Runde 12

1. Umschalter der Simulationen über dem Bild (Thema 1: Stationär · Instationär · Instationär in 2D).
2. Bild links (bis 780 px), rechts gestapelt „Berechnen“ (Oberkante bündig mit dem Bild, R12-08), „Standardwerte“, Varianten (Wand · Rohr · Kugel).
3. Lesehinweis in einem Satz direkt unter dem Bild (R12-06).
4. Regler in drei Spalten mit Fragezeichen-Hilfe; Kasten „Rechenwerte“ rechts daneben.
5. „Für Fortgeschrittene“ zugeklappt (Vergleich mit dem vorigen Lauf, Farbskala).
6. Drei Reiter: **Versuche** (offen; Satz „Erst vermuten, dann rechnen.“, Versuchskarten, erste aufgeklappt, „Alle Versuche zurücksetzen“), **Modell** (zu; fünf zugeklappte Abschnitte: Physikalisches Problem, Annahmen, Was die Simulation macht, Regler und Einheiten, So liest du die Ergebnisse), **So rechnet der Code** (zu; mit dem Hinweis, dass der Wissenstest das nicht braucht).
7. Versuchskarte: „Stell dir vor: …“, Simulation, Ausgangslage (Standardwerte, Knopf „Ausgangslage einstellen“), Das änderst du (Pfeil mit Wert), Was vermutest du?; Auswahl der Vermutung; „Auflösung zeigen“ erst nach der Auswahl („Wähle zuerst eine Vermutung.“), daneben der Textknopf „ohne Vermutung aufdecken“; Auflösung auf `#eef5fb` mit Vergleich ✓ oder ×.
8. Handy: Bild oben, beim Scrollen angeheftet; Rechenwerte, Knöpfe, Regler einspaltig; drei Reiter nebeneinander.

## 4 Sprachumschalter

Knopf „DE ↔ EN“ (mit Flagge) im Kopf rechts; Sprache im Browser gespeichert, `lang` des Dokuments wechselt, Reglerwerte, gewählter Reiter und Scrollposition bleiben (laut Prüfberichten). Englische Begriffe des Lernzentrums: Experiments · Model · How the code calculates; „First predict, then calculate.“; „Imagine:“; „Baseline: default values (“Set up the starting situation” button)“; „What you change:“; „What do you predict?“; „Set up the starting situation“; „Show explanation“; „Choose a prediction first.“; „reveal without a prediction“; „Reset all experiments“; „Calculated values“; „Calculate“; „Default values“; „Advanced controls“.

## 5 Bekannte Fehler und wie die Kaffee-Seite sie vermeidet

| Fehler im Lernzentrum (Nr. in `vorbild/bekannte_fehler_lernzentrum.md`) | Vermeidung auf der Kaffee-Seite | Test |
|:--|:--|:--|
| Sprachwechsel verliert Zustand oder rechnet neu (F01, F05) | Zustand getrennt vom Text; Wechsel tauscht nur Texte und Zahlenformat, keine Neuberechnung, Fokus bleibt auf dem Umschalter | Browsertest: Werte, Vorhersagen, Reiter vor und nach dem Wechsel gleich |
| Deutsche Wörter in Englisch, englische Zahlen falsch (F02, F06) | alle Texte aus einem Wörterbuch mit Schlüsseln; Zahlen nur über eine Formatfunktion je Sprache; Diagrammbeschriftung im SVG aus demselben Wörterbuch | Test: jeder Schlüssel in beiden Sprachen; Suche nach deutschen Wörtern in EN; Zahlenformat |
| Tausenderpunkt in Eingaben mehrdeutig (F07) | Bereiche der Kaffee-Seite unter 1000; Eingaben mit Komma oder Punkt als Dezimalzeichen, Tausendertrennung abgelehnt mit Meldung | Test mit „1.000“, „15,5“, „15.5“ |
| ungültige Eingaben (F08) | Meldung am Feld (rot, `aria-describedby`), Wert bleibt der letzte gültige; ungültige Einstellung blendet Ergebnisse aus (D116) | Test |
| Grenzen an zwei Stellen (F09) | eine Tabelle der Reglerbereiche im Code für Regler, Zahlenfeld und Prüfung | Test |
| abgeschnittene Inhalte, Scrollsprünge (F11, F12) | keine festen Höhen mit `overflow: hidden`; Seite scrollt normal; Wechsel von Fragen und Reitern ohne Sprung | Browsertest: `scrollY` bleibt |
| fokussierter Reiter am Handy unsichtbar (F13) | drei Reiter ohne Wischen; keine `preventScroll`-Fokussierung | Browsertest 360 px |
| Bild und Regler passen am Handy nicht zugleich (F14) | angeheftetes Bild höchstens 45 % der sichtbaren Höhe, Pflichtweg mit einem Regler | Browsertest 390 × 844 und 360 × 640 |
| Formeln breiter als die Spalte, Tabellen umbrechen (F15, F16) | Formeln kurz oder umbrechbar; Tabellen am Handy höchstens drei Spalten | Test: keine Formel breiter als ihre Spalte bei 360 px |
| unscharfe Beschriftung, Legende auf der Linie (F18, F19) | Diagramm als SVG in tatsächlicher Breite; Kurven direkt beschriftet mit Platzprüfung; Legende der Messpunkte außerhalb der Achsen | Bildschirmfotos bei Grenzwerten |
| veraltete Ergebnisse (F26) | sofortige Rechnung bei jeder Änderung (geschlossene Lösung, unter 100 ms); keine Rechentaste | Leistungstest |
| Code-Namen und Gedankenstriche auf der Oberfläche (F28, F30) | Formelzeichen der Vorlesung; Test auf U+2013 und U+2014 in allen Texten und `aria`-Namen | Test |
| abhängige Laufzeit aus dem Netz (F31) | keine: reines JavaScript in einer Datei | Netzwerkprotokoll |
| Prüfungen ohne echten Browser (F34) | alle Prüfungen in Chromium mit Playwright; Geräteprüfung auf dem iPhone durch die TL | ABNAHME_IPHONE.md |

Nicht übernehmen (wirkt in v8 anders als gemeint): Fehlertext grau statt rot (`pilot.css:9` überstimmt die rote Regel), alte Farben für Favicon und `theme-color`.

## 6 Schreibregeln (Leitfaden, gelten für die Kaffee-Seite)

- Anrede „du“; keine Sätze mit „man“ oder „Sie“ (Leitfaden 3, E5). Fragen und Versuche beginnen mit einer Situation, nicht mit einer Bedienhandlung.
- Wärme „wird übertragen“ oder „abgegeben“, nie „fließt“.
- Zu jedem Zahlenwert die Einheit; im Satz „in“, eckige Klammern nur an Reglern, Achsen, Tabellenköpfen (K2); Einheiten im Satz als kleiner Bruch (K3); Formelzeichen und Einheiten in Formeln fett über einen zentralen Schalter (K1).
- Dezimalkomma im Deutschen, Dezimalpunkt im Englischen; Werte zum Eintippen ohne Tausenderpunkt.
- „Simulierte Zeit“: „Du lässt die Simulation …“; genau benennen, wer etwas tut und wo etwas gilt.
- Englisch: britisch (colour), Kleinschreibung nach Doppelpunkt, „After completing …, you will be able to …“, feste Fachbegriffe (heat flow rate, heat transfer coefficient, overall heat transfer coefficient, transient), Formelzeichen-Indizes übersetzen, wenn sie Wörter sind (Leitfaden 4); auf der Kaffee-Seite bleiben die Indizes K, M, u, G, B wie in Vorlesung und Aufgabe und werden einmal erklärt (Konzept Anhang C).
- Versuchskarten nach Muster L16: Ausgangslage als Verweis auf Standardwerte und Knopf, Änderung als Pfeil mit Wert, Ergebnis als kleine Vorher-nachher-Tabelle.
- Keine Gedankenstriche.

## 7 Zuordnung Konzept Fassung 2 zu Aufbau v8

| Konzept F2 | Aufbau auf der Kaffee-Seite | Abweichung und Grund |
|:--|:--|:--|
| Kopf mit Umschalter (5.1 Nr. 1) | wie v8, ohne Seitenleiste der Themen | keine Themenleiste: eine Seite, ein Thema |
| Frageleiste über dem Diagramm (5.1 Nr. 2, M-6) | Leiste mit der aktuellen Frage des Pflichtwegs und dem Knopf „Vorhersage festhalten, dann prüfen“ als **einziger dunkler Hauptaktion** | v8 hat keine Frageleiste; beibehalten nach M-6 (Frage, Vorhersage und Diagramm zugleich sichtbar). Die Knopfrangfolge von v8 bleibt: eine dunkle Hauptaktion |
| Ansicht Temperatur, Wärmestrom, ln (5.1 Nr. 3) | Umschaltknöpfe wie die Simulationswahl in v8; im Pflichtweg nur „Temperatur“ | keine |
| Diagramm (5.1 Nr. 4) | SVG in tatsächlicher Breite, bis 780 px | v8 nutzt Rasterbilder; SVG vermeidet F18 und F19 |
| Knöpfe rechts (5.1 Nr. 5) | „Standardwerte“ (Stil Rang 2, Oberkante bündig mit dem Diagramm), „Wie im Versuch (60 min, Becher)“; „Lauf zum Vergleich merken“ unter „Für Fortgeschrittene“ in der Vertiefung; „Vorhersage neu“ als „Alle Fragen zurücksetzen“ im Reiter Versuche | v8 hat „Berechnen“; die Kaffee-Seite rechnet sofort (M-5, Bauauftrag 1.5). Vergleichslauf wie in v8 unter „Für Fortgeschrittene“ (R12-07) |
| Energie und Bilanzraum (5.1 Nr. 5) | Kasten „Energie bis zur Zugabe“ unter den Knöpfen; Bilanzraum in der Vertiefung | keine |
| Regler (5.1 Nr. 6) | Beschriftung wie v8 mit Formelzeichen und Einheit in eckigen Klammern, Fragezeichen-Hilfe, Zahlenfeld; zusätzlich Minus und Plus (M-12) | Plus und Minus fehlen in v8; Konzept M-12 verlangt sie |
| Rechenwerte (5.1 Nr. 7) | Kasten wie v8 | keine |
| Messblatt (5.1 Nr. 8) | eigener Abschnitt unter den Reglern | v8 hat kein Messblatt |
| Lesehilfe (S-7) | Lesehinweis in einem Satz direkt unter dem Diagramm (R12-06) | Konzept: bis drei Sätze, wegklickbar; v8-Muster mit einem Satz ist kürzer und immer sichtbar |
| **Reiterleiste mit neun Reitern (5.1 Nr. 9, M-18, Anhang A)** | **drei Reiter: Versuche, Modell, So rechnet der Code** | **Abweichung vom Konzept, Grund: K5 (Lernzentrum, Runde 12) und Bauauftrag 1.4.** Texte nur umsortiert, nicht geändert, siehe Tabelle unten |
| Reiter am Handy als Akkordeon (5.2, M-18) | drei Reiter nebeneinander, auch am Handy | Grund: K5 und R12-09 („am Handy alle drei sichtbar, ohne Wischen“) |
| Reiter „Auflösungen“ (E6) | Reiter heißt „Versuche“ (EN „Experiments“) wie im Bauauftrag 1.4; die Auflösungen stehen in den Karten | **Konflikt:** E6 benannte den alten Reiter um, damit er nicht mit dem Becherversuch verwechselt wird; der Bauauftrag (Rang 1) nennt „Versuche“. Umgesetzt nach Bauauftrag, als Frage an die TL gemeldet (Empfehlung im Baubericht) |
| Fragen (Abschnitt 6) | Versuchskarten im Reiter Versuche und dieselbe Frage in der Frageleiste | Kartenmuster aus v8 (Ausgangslage, Vermutung, Auflösung zeigen, ohne Vermutung aufdecken); Wortlaut der Fragen aus dem Konzept unverändert |
| Vertiefung (5.3) | Bereich „Vertiefung“ unter dem Pflichtweg, zugeklappt; enthält „Für Fortgeschrittene“ | keine |

**Zuordnung der Texte aus Konzept Anhang A zu den drei Reitern (nur umsortiert, K5):**

| Reiter | Abschnitt | Text aus Konzept Anhang A |
|:--|:--|:--|
| Versuche | Einleitung | A.1 „Probier es aus: erst vorhersagen, dann prüfen …“ |
| Versuche | Karten | Fragen aus Abschnitt 6.1 und 6.2, Auflösungen aus A.3 und Abschnitt 6 (Spalte Erwartung) |
| Modell | Physikalisches Problem | A.5 |
| Modell | Annahmen | A.6 |
| Modell | Was die Simulation macht | A.7 |
| Modell | Regler und Einheiten | A.4 (Tabelle Parameter) |
| Modell | So liest du die Ergebnisse | A.2 |
| So rechnet der Code | Rechenweg | A.8 (Modell im Detail: Bilanz, Lösung, Mischen, Wärme, Zeitpunkt, kA festhalten, Ausgleichsgerade) |
| So rechnet der Code | Code | A.9 |

A.8 steht unter „So rechnet der Code“ statt unter „Modell“, weil nach Leitfaden 2 Differentialgleichungen und Lösungen nur dort stehen.
