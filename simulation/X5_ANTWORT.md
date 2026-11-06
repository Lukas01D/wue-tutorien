# Antwort auf die Abnahme X5 (Codex)

> Antwort von Claude auf `simulation/X5_CODEX_ABNAHME.md` (Zweig `codex/x5-abnahme-da7deb1`, Commit 9a9208b, geprüfter Stand da7deb1, Artefakt SHA-256 `1d90ce2f…292b`). Auftrag der TL vom 06.11.2026: jeden Befund nachprüfen, beantworten, in der Reihenfolge X5-01 und X5-02, X5-03 bis X5-08, F1 bis F12, offene Befunde der Runde 3, X5-09 bis X5-11 umsetzen.

## Nachprüfung

Die Skripte von Codex liefen unverändert als Kopie in `simulation/x5_regression/` (damit die Belege von Codex in `simulation/x5_skripte/` unverändert bleiben), mit Playwright 1.63.0 für Python und dem Chromium 153 dieser Umgebung, axe-core 4.11.0 wie bei Codex. Auswertung der Ergebnisdateien: `simulation/x5_regression/auswertung.py`, Stand vor der Korrektur in `auswertung_alt_1d90ce2f.txt`.

- `pruefung_b.py` auf dem alten Stand: 15 PASS, 5 FAIL, genau die Befunde X5-01, X5-03, X5-07, X5-08, X5-11.
- `pruefung_layout.py` und `pruefung_ergaenzung.py` auf dem alten Stand: Überlauf bei 200 % Text in 6 Zuständen (320 px: 371 px breit, 8 Regler 0 px breit), angehefteter Bereich über 45 % in 6 Zuständen (bis 63,7 %), kleinste Diagrammschrift unter 9 px in 6 Zuständen (bis 6,79 px), 16 verdeckte Fokusmitten bei 768 × 1024 mit 32 px Grundschrift, Schnittkreis ohne Beschriftung in 16 von 72 Zuständen, Messwert 66,5 °C nach dem Quellenwechsel durch 70,145 °C ersetzt.
- X5-02 eigene Rechnung: mit Becher $C_\mathrm{GB} = 957{,}746 + 255 = 1212{,}746$ J/K, $Q_2 - Q_1 = 3{,}73384$ kJ; $3733{,}84 / 1212{,}746 = 3{,}0788$ K (richtig, gleich der Anzeige), $3733{,}84 / 957{,}746 = 3{,}8986$ K (gedruckte Formel mit $C_\mathrm{G}$).

Alle elf Befunde sind damit bestätigt. Keine Zahl der Seite war falsch; X5-02 betrifft eine allgemeine Gleichung im Text, nicht die Rechnung.

## Befunde

| ID | Entscheidung | Begründung mit Beleg | Folge |
|:--|:--|:--|:--|
| X5-01 | übernehmen | Reproduziert (`V3_Antwort_vor_Vorhersage` FAIL): Beim Öffnen von V3 nach Frage 2 bleibt der Zustand mit Becher und *kA* aus der Messung stehen, Rechenwerte 3,08 K. Gleich G10-01. Verletzt ZUSTAENDE Regel 1 und M-3. Schwere blocker nach Bauauftrag 4.1 angenommen. | Beim Öffnen einer Vertiefungsfrage ohne festgehaltene Vorhersage stellt die Seite die Standardwerte ein (ohne Becher, ohne Deckel, *kA* festgehalten; deren Ergebnis kennt man aus dem Start) und sagt das an; die Regler bleiben frei (ZUSTAENDE 2). behoben, Test in `browsertest_korrektur.js` |
| X5-02 | übernehmen | Nachgerechnet (oben). In `texte_de.txt` und `texte_en.txt` stehen in der Energiedifferenz und ihrer Ableitung $C_\mathrm{G}$ ohne Becher. Gleich G3-05 (dort low; die TL hat F12 mit dem Vorschlag der Rolle entschieden). | Beide Gleichungen mit $C$ der Tasse nach der Zugabe, definiert als $C_\mathrm{G}$ ohne Becher und $C_\mathrm{GB} = C_\mathrm{G} + m_\mathrm{B} c_\mathrm{B}$ mit Becher, DE und EN. behoben, Test in `browsertest_korrektur.js` |
| X5-03 | übernehmen | Reproduziert (`Quellenwechsel_haelt_Kurven_bei_kA1` FAIL; 66,5 → 70,145 °C, Anzeige „Messung nach 10 min“). Code: beim Wechsel auf „aus der Messung“ wird der gleichwertige Wert des Modells in das Messfeld geschrieben und auf 30 bis 90 °C begrenzt. Widerspricht KONZEPT 8.2 (M8, „wird nie als Messung angezeigt“) und 8.5 („Ein Wechsel der Quelle ändert die Kurven nicht sofort“). | Rechnerischer Ersatzwert getrennt von der eigenen Messung: Er steht als „aus *kA* berechnet, keine Messung“ am Feld; die eigene Messung bleibt gespeichert und lässt sich mit einem Knopf wieder verwenden. Liegt der Ersatzwert außerhalb des Messbereichs, bleibt die Quelle „festhalten“ mit Meldung, ohne stille Begrenzung. behoben, Test in `browsertest_korrektur.js` |
| X5-04 | übernehmen | Reproduziert (16 verdeckte Fokusmitten bei 768 × 1024 und 32 px). Gleich G5-R3-01. `scroll-padding-top` ist fest 56 px. | Abstand aus der gemessenen Höhe der Kernleiste (bei jeder Größenänderung); wird die Kernleiste höher als ein Viertel des Fensters, ist sie nicht mehr angeheftet. Test vorwärts und rückwärts; behoben |
| X5-05 | übernehmen | Reproduziert (Überlauf in 6 Zuständen, 8 Regler 0 px breit bei 320 px). Neu gegenüber Runde 3. Feste Spalten der Reglerzeile. | Reglerzeile bricht um, wenn der Platz fehlt (Regler eigene Zeile, Minus, Zahlenfeld, Plus darunter). Test 320 bis 1024 px mit 200 % Text; behoben |
| X5-06 | übernehmen | Reproduziert (16 von 72). Gleich G6-R3-01 und G6-R3-02. Code lässt die Beschriftung weg, wenn kein freier Platz gefunden wird. | Mehr Kandidaten rund um den Kreis und am Rand der Zeichenfläche mit Verbindungslinie; erst wenn auch das scheitert, steht „Schnitt“ in der Legende unter dem Diagramm. Kurvennamen mit mehr Kandidaten am Kurvenzug. Test über alle Zustände von Codex; behoben |
| X5-07 | übernehmen | Reproduziert (`Kurslink_alle_akzeptierten_Nachkommastellen` FAIL). ZUSTAENDE 5 erlaubt im Link höchstens zwei Nachkommastellen; das Messblatt nahm mehr an. | Das Messblatt nimmt wie der Link höchstens zwei Nachkommastellen an; mehr gilt als ungültig mit Hinweis am Feld. Damit sind Eingabe, Speicher, Anzeige und Link gleich genau. behoben, Test in `browsertest_korrektur.js` |
| X5-08 | übernehmen | Reproduziert (`Ungueltige_Einstellung_und_Sprachwechsel` FAIL). Die Fehlermeldung wird nur bei geändertem Fehlercode neu gesetzt. | Sprache gehört zum Schlüssel; alle stehenbleibenden Meldungen (Fehler, Statuszeile, Hinweise an Feldern, Kurslink) nach dem Sprachwechsel geprüft. behoben, Test in `browsertest_korrektur.js` |
| X5-09 | übernehmen | Reproduziert (bis 6,79 px). Gleich G6-R3-03, G5-R3-03. | Zeichnung in der tatsächlichen Breite und Höhe der Box; Schrift bleibt 11 bis 12 px. behoben, Test in `browsertest_korrektur.js` |
| X5-10 | übernehmen | Reproduziert (bis 63,7 %). Gleich G5-R3-02. Abzug von 125 px wächst nicht mit der Schrift. | Höhe des Diagramms aus `visualViewport.height · 0,45` minus der gemessenen Höhe von Kernzahlen und Vorhersagezeile; reicht der Platz nicht für ein lesbares Diagramm, wird nicht angeheftet. behoben, Test in `browsertest_korrektur.js` |
| X5-11 | übernehmen | Reproduziert (`Kurslink_fremdes_Format` FAIL). ZUSTAENDE 5 verlangt für alles ohne `kurs1` den Hinweis „Dieser Link enthält keine Kurswerte dieser Seite.“; die Seite schwieg bei Fragmenten ohne `kurs`. Eigener Sprunganker der Seite ist nur `#hauptinhalt`. | Fragmente, die auf ein Element der Seite zeigen, bleiben unberührt; alle anderen ohne `kurs1` bekommen den Hinweis und verschwinden aus der Adresse. behoben, Test in `browsertest_korrektur.js` |

Zu den Muss-Bewertungen von X5: M-13 (Regler 0 px bei 320 px und 200 % Text) fällt unter X5-05; M-17 bleibt für das Öffnen als Datei offen in Codex' Umgebung, ist hier mit `file:` im Browsertest „Artefakt Datei“ belegt; M-15 mit echtem Bildschirmleser bleibt offen (Gerät fehlt). Die übrigen Muss-Bewertungen von X5 decken sich mit dem Baubericht.

## Umsetzung und Nachweis

Umgesetzt in der Reihenfolge der TL (Commits 437295c bis 188ba12 auf `claude/simulation-tool-kaffee-4kcacl`; Endstand der Seite SHA-256 `e44b4961…3ce3`, 429 897 Bytes). Jeder Befund hat einen Test in `simulation/tests/browsertest_korrektur.js`: 29 Tests zu X5 und Runde 3 (auf dem Stand vor der Korrektur `1d90ce2f…292b` **0 von 29** bestanden, `browsertest_korrektur_alt_ergebnis.txt`), dazu 14 Tests zu den Befunden der Rollenprüfung Runde 4 (auf dem von Runde 4 geprüften Stand e2f9cd9 alle rot, `browsertest_korrektur_e2f9cd9_ergebnis.txt`). Neuer Stand: **45 von 45** einschließlich der Tests zum Beamer-Befund und zu den Entscheidungen Q2 bis Q7 (`browsertest_korrektur_ergebnis.txt`). Endstand der Seite nach Q1 bis Q7 und Beamer-Befund: SHA-256 `e6f95ca2…cc1d`, 433 303 Bytes, Commit 6077a92.

| ID | Test (Kurzname) | Messwert alt | Messwert neu (Endstand) |
|:--|:--|:--|:--|
| X5-01 | V3 nach Frage 2 ohne Becher-Lage | Becher an, 3,08 K vor der Vorhersage | Standardwerte, Ansage „Ausgangslage vor deiner Vorhersage“ |
| X5-02 | $C_\mathrm{GB}$ im Rechenweg DE und EN | 0 | in beiden Gleichungen, beide Sprachen |
| X5-03 | Quellenwechsel | 66,5 °C durch 70,145 °C ersetzt, Feld „Messung nach 10 min“ | Feld „Gleichwertiger Wert nach 10 min, aus *kA* berechnet“, eigene Messung gespeichert mit Knopf „Deine Messung 66,5 °C wieder verwenden“; außerhalb 30 bis 90 °C abgelehnt, *kA* unverändert |
| X5-04 | Fokus bei 768 × 1024, 32 px | 16 verdeckte Fokusmitten (Codex-Lauf) | 0 von 93 Stopps (eigener Test), 0 (Codex-Lauf) |
| X5-05 | 200 % Text | Seite 371 px breit bei 320 px, 8 Regler 0 px | kein Überlauf 320 bis 1024 px, kein Regler unter 44 px |
| X5-06 | Schnittbeschriftung | 16 von 72 (Codex), 86 von 180 (eigene Stichprobe) ohne Text | 0 von 72 (Codex), 0 von 168 (eigener Test) |
| X5-07 | Nachkommastellen | 21,555 angenommen, im Link 21,56 | mehr als zwei Stellen abgelehnt mit Hinweis am Feld |
| X5-08 | Sprachwechsel | Fehlermeldung bleibt deutsch | übersetzt; ebenso Hinweis zum Kurslink |
| X5-09 | Diagrammschrift angeheftet | bis 6,79 px | 11 px (320 × 640 bis 412 × 915) |
| X5-10 | Anteil angeheftet | bis 63,7 % | höchstens 44,8 %; bei zu wenig Platz nicht angeheftet |
| X5-11 | fremdes Fragment | still, bleibt in der Adresse | Hinweis, aus der Adresse entfernt; `#hauptinhalt` bleibt |

**Skripte von Codex auf dem neuen Stand** (Kopie in `simulation/x5_regression/`, Läufe `lauf_*.txt`, Ergebnisse `ergebnis_*.json`, Auswertung `auswertung_neu.txt` gegen `auswertung_alt_1d90ce2f.txt`):

- `pruefung_a.py`: 441 Sätze, 23 814 Vergleiche, größte Abweichung 1,15e-9, keine außerhalb der Toleranz; alle Zahlen der Auflösungen (76 auf dem Endstand) gleich der Rechnung von Codex.
- `pruefung_b.py`: 19 PASS, 1 ERROR. Der ERROR ist `Quellenwechsel_haelt_Kurven_bei_kA1`: Das Skript erwartet, dass sich „aus der Messung“ bei *kA* = 1 W/K anklicken lässt; die Seite lehnt diesen Wechsel jetzt ab (gleichwertiger Wert 26 °C außerhalb 30 bis 90 °C), wie von Codex als eine der beiden Möglichkeiten vorgeschlagen. Die Eigenschaft, die das Skript prüft (*kA* bleibt gleich), belegt Test K03.
- `pruefung_layout.py`: 108 Layouts, kein Überlauf, keine Regler mit Breite 0, kein angehefteter Bereich über 45 %, keine Diagrammschrift unter 9 px, 0 verdeckte Fokusmitten, Schnitt ohne Text 0.
- `pruefung_ergaenzung.py`: 0 verdeckte Fokusmitten bei 768 × 1024 mit 32 px; `measured_replaced` meldet weiter 66,5 → 70,145 °C im Feld, das Feld heißt jetzt aber „Gleichwertiger Wert nach 10 min, aus *kA* berechnet“ und die Messung bleibt gespeichert (gewollt, siehe X5-03).

Die übrigen Tests: `test_kern.py` 134 von 134, `--html` 135 von 135, `test_texte.py` 14 von 14, `browsertest_bau.js` 95 von 95 (zwei Prüfungen an die Entscheidungen angepasst: „Geschafft“ erst nach geöffneter Auflösung, F8; 45 % gilt für den angehefteten Zustand, X5-10).

**Nach der Rollenprüfung Runde 4** (G1, G3, G5 auf e2f9cd9) wurden die dort gefundenen Nebenwirkungen ebenfalls behoben, unter anderem: Zeitangabe der Startauflösung erst nach Frage 1 (G1-R4-01, G3-R4-01; Frage Q1 an die TL), Beschriftungen ohne Überdeckung im flacheren Handy-Diagramm (G5-R4-01; Skript der Rolle: 0 von 648 Zuständen), Teilflächen nach dem Vorzeichen (G3-R4-02), Becher in der Lesehilfe (G3-R4-03). Einzelheiten in `simulation/gutachten/ZUSAMMENFUEHRUNG.md`, letzter Abschnitt.
