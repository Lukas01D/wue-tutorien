# Auftrag für Codex: unabhängige Prüfung der Kaffee-Simulation Fassung 3 (Rolle X6)

> Für Codex (OpenAI). Startsatz der TL: „Prüfe die Kaffee-Simulation Fassung 3 nach simulation/X6_AUFTRAG.md (Rolle X6).“ Geschrieben von Claude am 08.11.2026 nur mit Fakten (Ziel, Prüfwerte, Entscheidungen der TL, Abnahmekriterien), ohne eigene Bewertung. Deutsch. Keine Gedankenstriche (weder Halbgeviert- noch Geviertstrich), stattdessen Komma, Punkt, Doppelpunkt oder Klammern.

## 1 Geprüfter Stand

Zweig `claude/kaffee-simulation-v3-qw4zb2` (vorher `git fetch origin claude/kaffee-simulation-v3-qw4zb2`, dann `git checkout claude/kaffee-simulation-v3-qw4zb2`). Notiere den Commit (`git rev-parse HEAD`) und den SHA-256 von `simulation/site/index.html`; beides gehört in den Bericht. Arbeite auf einem eigenen Zweig (zum Beispiel `codex/x6-kaffee-f3`), kein Pull Request.

## 2 Ziel der Seite

Eine schlanke Seite zur Kaffee-Aufgabe in Tutorium 5 (instationäre globale Energiebilanz). Sie wird nach Teil e des Blatts geöffnet, also wenn die Temperaturen beider Tassen nach 60 min gerechnet sind, und vor Teil f. Sie muss auch allein zu Hause funktionieren. Pflichtweg: 01 Vorhersage mit Grund, 02 Warum? (Energiesäulen), 03 Messung dazulegen, 04 Zum Schluss. Danach „Weiterdenken: nach dem Tutorium oder zu Hause“ mit drei Aufträgen. Grundlage: `simulation/KONZEPT_F3.md` (Abschnitte 1 bis 7 und Anhang B), Entscheidungen in `simulation/ENTSCHEIDUNGEN_F3.md`.

## 3 Was du liest

- die Seite `simulation/site/index.html` (eine Datei, offline); die Quellen in `simulation/site/src/`, das Bauskript `simulation/site/bauen.py`
- das Modell `simulation/modell/kaffee_modell.py` und die Werte des Blatts `simulation/modell/werte.py`
- `simulation/KONZEPT_F3.md` und `simulation/ENTSCHEIDUNGEN_F3.md`
- **erst am Ende**, zum Vergleich mit deinen eigenen Prüfungen: `simulation/BAU_BERICHT_F3.md`, `simulation/tests/` mit den Ergebnisdateien und `simulation/bildschirmfotos/f3/`

## 4 Prüfwerte (Werte des Blatts, aus `werte.py`)

| Größe | Wert |
|:--|:--|
| kA aus 72 °C nach 10 min | 0,1994 W/K |
| Mischtemperatur Tasse 1 | 70,47 °C |
| nach 60 min: Tasse 1, schwarzer Kaffee, Tasse 2 nach der Milch | 43,85 °C; 45,43 °C; 40,29 °C |
| Unterschied | 3,56 K |
| abgegebene Wärme Q1, Q2 | 25,49 kJ; 28,90 kJ |
| Schnittpunkt der Kurven | etwa 95 min |
| erwärmte Milch 70 °C: Tasse 1, Tasse 2 | 47,76 °C; 48,55 °C |
| Kipppunkt der Milchtemperatur | 58,2 °C |
| Zeit bis 60 °C (Tasse 1) | 18,6 min |

## 5 Entscheidungen der TL, die die Seite betreffen (Wortlaut in `ENTSCHEIDUNGEN_F3.md`)

- G1 minimalistisch und überblickbar; G2 auch ohne Tutorium lösbar.
- B09 Simulation nach Teil e und vor f; die Energiesäulen werfen die Frage auf, die f beantwortet. B05 Simulationswerte sind keine Messwerte. B12 Rechnung, Simulation und Messung werden verglichen. B21, Z3 Vortest und Umfragen laufen im Tutorium, die Seite sammelt keine Daten.
- SE1 Optik von Entwurf A „Messprotokoll“ mit dem Besten aus A, B, C und Variante 0. SE2 Regler: Milchtemperatur, Zugabe, Kaffee bei t0, Raum, kA der Tasse. SE3 kein Kurslink. SE4 ein Eingabefeld je Tasse für eigene Messpunkte. SE5 Deutsch und Englisch. SE6 Standardwerte an einer Stelle, mit Test gegen `werte.py`, als vorläufig gekennzeichnet.
- D1 bis D10 wie empfohlen (Konzept Abschnitt 7), dazu T1 (Vertiefung als „nach dem Tutorium oder zu Hause“ gekennzeichnet), T2 (Pflichtweg 01 bis 04), T3 (Grund Pflicht per Tipp, Freitext freiwillig).
- Das Modell bleibt unverändert; keine Verdunstung, kein Becher, keine überlineare Wärmeabgabe.

## 6 Abnahmekriterien (Abschnitt 4 des Auftrags der TL)

1. Pflichtweg in höchstens 8 min (deine Schätzung); Regler nach SE2 gruppiert.
2. Die Seite funktioniert allein, ohne Tutorium (G2).
3. Gestaltungssynthese mit Tabelle und Quellen (Konzept Anhang A).
4. Alle Prüfwerte exakt (relative Abweichung unter 1e-9 gegen `kaffee_modell.py`).
5. Die 15 Kriterien aus L2, Abschnitt D1 (Konzept Anhang C), mit Ergebnis.
6. Die Startkarte verrät nichts; keine Zahl auf der Seite nimmt eine Teilaufgabe des Blatts vorweg, bevor die eigene Vorhersage festgehalten ist.
7. Keine Verdunstung im Modell.
8. Deutsch und Englisch gleichwertig; offline als eine Datei; axe-core ohne Verstoß (WCAG 2.2 A und AA); am Beamer 1280 × 720 lesbar.
9. Die Seite ist kleiner als die Fassung 2 (433 303 Bytes).
10. `ENTSCHEIDUNGEN_F3.md` enthält jede Entscheidung der TL mit Grund und Quelle.

## 7 Prüffragen

1. **Zahlen:** eigenes Skript, das weder `kaffee_modell.py` noch den Skriptteil der Seite importiert, sondern aus den Gleichungen des Blatts rechnet. Vergleiche mit der Seite (im Browser oder den Skriptteil vor `const TEXTE` in Node) bei den Werten des Blatts und an mindestens zehn eigenen Einstellungen, auch an den Grenzen der Regler. Prüfe auch die Zahlen in den Texten (Rückmeldungen, Aufträge, Modell).
2. **Sperren:** Steht vor dem Festhalten auf der Startkarte eine Ergebniszahl irgendwo im DOM (auch versteckt), in Ansagen, im Titel? Stehen vor der Antwort in 02 die Säulenzahlen, vor Auftrag 3 Milchtemperaturen über 30 °C zur Verfügung?
3. **Bedienung:** Playwright oder ein anderer Browser ohne Internetzugriff, bei 390 × 844, 1366 × 768 und 1280 × 720, in beiden Sprachen: alle Schritte, Regler (Ziehen, Plus und Minus, Zahlenfeld mit Komma und Punkt, Tastatur), Messpunkte (auch unsinnige Eingaben), ln-Ansicht, Aufträge, Neuladen, „Von vorn“, gesperrter Speicher. Bildschirmfotos ansehen: lesbar, nichts abgeschnitten, kein waagerechtes Scrollen? Lädt die Seite etwas von außen?
4. **Pflichtweg:** einmal wie Studierende allein, mit Stoppuhr; notiere, wo du stockst.
5. **Sprache und Zeichen:** verständlich für das dritte Semester, du-Form, keine Gedankenstriche, Formelzeichen wie im Blatt.

## 8 Ergebnis

Bericht nach `simulation/X6_CODEX_PRUEFUNG.md`: geprüfter Stand (Commit, SHA-256), Urteil (abnahmefähig, mit Änderungen, nicht abnahmefähig), Tabelle der Abnahmekriterien mit Ergebnis, dann Befunde nach Wichtigkeit (blocker, high, medium, low) mit Stelle, Beleg und Vorschlag, nummeriert „X6-01“, „X6-02“, … Skripte und Bilder nach `simulation/x6_skripte/`. Nichts an Seite, Quellen, Tests oder Konzept ändern. Committen und auf deinem eigenen Zweig pushen.
