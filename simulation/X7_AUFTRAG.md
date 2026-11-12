# Auftrag für Codex: unabhängige Prüfung der schlanken Kaffee-Simulation (Rolle X7)

> Für Codex (OpenAI). Startsatz der TL: „Prüfe die schlanke Kaffee-Simulation nach simulation/X7_AUFTRAG.md (Rolle X7).“ Geschrieben von Claude am 12.11.2026 nur mit Fakten (Ziel, Modell, Prüfwerte, Entscheidungen der TL, Abnahmekriterien), ohne eigene Bewertung. Deutsch. Keine Gedankenstriche (weder Halbgeviert- noch Geviertstrich), stattdessen Komma, Punkt, Doppelpunkt oder Klammern.

## 1 Geprüfter Stand

Zweig `claude/aufarbeitung-befunde` (vorher `git fetch origin claude/aufarbeitung-befunde`, dann `git checkout claude/aufarbeitung-befunde`). Notiere den Commit (`git rev-parse HEAD`) und den SHA-256 von `simulation/minimal/Kaffee_Simulation_schlank.html`; beides gehört in den Bericht. Arbeite auf einem eigenen Zweig (zum Beispiel `codex/x7-schlank`) und öffne am Ende einen Pull Request nach `main`, der nur neue Dateien enthält (Bericht und Skripte). Nichts veröffentlichen.

## 2 Ziel der Seite

Die schlanke Seite ersetzt seit dem 12.11.2026 (Sites-Version 4 und 5) unter `waermeuebertragung-kaffee` die bisherige Simulation; der QR-Code auf dem Blatt von Tutorium 5 führt dorthin. Sie zeigt ohne Fragen und mit wenig Text, wie sich zwei Tassen Kaffee abkühlen: Tasse 1 bekommt die Milch sofort, Tasse 2 nach $t_\mathrm{Z}$. Kasten mit den Temperaturen und der Differenz, Diagramm, Säulen der an den Raum abgegebenen Wärme, „Abspielen“, zehn Regler, Deutsch und Englisch, eine Datei ohne Netz.

## 3 Was du liest

- die Seite `simulation/minimal/Kaffee_Simulation_schlank.html`; die Quellen `simulation/minimal/src/`, das Bauskript `simulation/minimal/bauen_minimal.py` und was es aus `simulation/site/src/` übernimmt (`modell.js`, `stil.css`, Texte, Bausteine aus `oberflaeche.js`)
- das Modell des Blatts `simulation/modell/kaffee_modell.py` und die Werte `simulation/modell/werte.py`
- `simulation/minimal/LIESMICH.md`, `simulation/AENDERUNG_2026-11-11.md` (Entscheidungen der TL), `simulation/minimal/QUELLEN_Vergleichswerte.md`
- **erst am Ende**, zum Vergleich mit deinen eigenen Prüfungen: `simulation/tests/minimal_test.js` und `simulation/aufarbeitung/` (Prüfskripte und Haltepunkt der Aufarbeitung durch Claude)

## 4 Modell der schlanken Seite (Festlegung)

| Teil | Festlegung |
|:--|:--|
| Bilanz je Tasse | $C\,\mathrm{d}\vartheta/\mathrm{d}t = -kA\,(\vartheta - \vartheta_u) + \dot Q_\mathrm{W}$, gleiches $kA$ und gleicher Tassenwärmer $\dot Q_\mathrm{W}$ für beide Tassen |
| Wärmekapazitäten | $C_K = \rho_K V_K c_{p,K} + C_\mathrm{T}$, $C_M = \rho_M V_M c_{p,M}$, $C_G = C_K + C_M$; die Tasse hat immer die Temperatur ihres Inhalts |
| Tasse 1 | Mischung bei $t = 0$ ohne Verlust, danach Abkühlung mit $C_G$ |
| Tasse 2 | Abkühlung mit $C_K$ bis $t_\mathrm{Z}$, Mischung ohne Verlust, danach Abkühlung mit $C_G$ bis $t$ |
| abgegebene Wärme | $Q_i(t) = \int_0^t kA\,(\vartheta_i - \vartheta_u)\,\mathrm{d}t$ |
| Regler | $t$ 1 bis 180 min; $t_\mathrm{Z}$ 1 bis $t$; Milch 2 bis 95 °C und 10 bis 200 ml; Kaffee 60 bis 95 °C und 50 bis 400 ml; Raum 10 bis 30 °C; $kA$ 0,01 bis 1 W/K (logarithmisch); $C_\mathrm{T}$ 0 bis 600 J/K; $\dot Q_\mathrm{W}$ 0 bis 35 W, höchstens so viel, dass $\vartheta_u + \dot Q_\mathrm{W}/kA \le$ 95 °C |
| Stoffwerte | wie Blatt: $\rho_K$ = 1000 kg/m³, $c_{p,K}$ = 4180 J/(kg K), $\rho_M$ = 1030 kg/m³, $c_{p,M}$ = 3940 J/(kg K) |

## 5 Prüfwerte (Werte des Blatts, aus `werte.py`)

| Größe | Wert |
|:--|:--|
| kA aus 72 °C nach 10 min | 0,1994 W/K |
| $C_G$ | 1241,8 J/K |
| nach 45 min: Tasse 1, Tasse 2 | 43,01 °C; 36,31 °C |
| Temperaturdifferenz | 6,69 K |
| abgegebene Wärme $Q_1$, $Q_2$, $Q_2 - Q_1$ | 15,50 kJ; 23,82 kJ; 8,31 kJ |

Weitere Werte (Tassenwärmer, Wärmekapazität der Tasse, $t > t_\mathrm{Z}$) rechnest du selbst.

## 6 Entscheidungen der TL, die die Seite betreffen

- Seite ohne Fragen, wenig Text, Stil der bisherigen Seite; Säulen der abgegebenen Wärme neben der Kurve; „Abspielen“ bleibt; alle Regler sichtbar, nicht ausklappbar (11. und 12.11.2026).
- Kopf: „Tasse 1 (Milch zu Beginn)“, „Tasse 2 (Milch später)“, „Temperaturdifferenz“; Knopf „Standardwerte“; Tasse 1 hellbraun, Tasse 2 dunkelbraun durchgezogen, Differenz rotorange.
- Zeit bis 180 min unabhängig von der Zugabe, Zugabe höchstens $t$; Tasse 2 kühlt nach der Milch weiter ab.
- Milch bis 95 °C; Regler für Kaffeemenge, Wärmekapazität der Tasse und Tassenwärmer (bis 35 W).
- $kA$ logarithmisch; Alltagsvergleiche für $kA$ und $C_\mathrm{T}$ aus recherchierten Werten, als Band unter der Skala (Variante 3).
- Am 12.11.2026 nach der Aufarbeitung (Wortlaut der TL: „A01 gerne beheben und wenns sinn ergibt auch gern in einem rutsch A02 bis A04 auch noch erledigen“): Grenzen des Diagramms aus allen gezeichneten Werten; Säulen mit Nulllinie, negative Wärme zeigt nach unten, darunter ein Hinweissatz.

## 7 Abnahmekriterien

1. Alle Zahlen der Seite (Kasten, Säulen, Bildbeschreibung, Ansage) stimmen mit dem Modell aus Abschnitt 4 überein (relative Abweichung unter 1e-9), auch beim Abspielen und an den Grenzen der Regler.
2. Das Modell aus Abschnitt 4 ist physikalisch richtig umgesetzt; wo die Festlegung selbst fragwürdig ist, sagst du es.
3. Alles Gezeichnete liegt im Diagramm; Säulen, Klammer und Zahlen passen zueinander, auch bei negativer Wärme.
4. Kein Wert über 95 °C durch den Tassenwärmer.
5. Alltagsvergleiche: Bereiche passen zu den Quellen (mindestens drei Quellen selbst öffnen).
6. Deutsch und Englisch gleichwertig; axe-core ohne Verstoß (WCAG 2.2 A und AA); Tastatur; 390 × 844, 1366 × 768, 1280 × 720 ohne waagerechtes Scrollen, am Beamer alle Regler ohne Bildlauf.
7. Eine Datei; keine Netzanfragen, kein Speicher; Inhaltssicherheitsrichtlinie wirksam.
8. `python3 simulation/minimal/bauen_minimal.py --pruefen` gibt „gleich“ aus; zwei Bauten sind bytegleich.

## 8 Prüffragen

1. **Physik:** Leite die Lösung für beide Tassen mit Tassenwärmer und Tassenwärmekapazität selbst her. Ist $Q_i = \dot Q_\mathrm{W}\,t + C\,(\vartheta_\text{Start} - \vartheta_i)$ (stückweise) richtig? Gilt $Q_2 - Q_1 = C_G(\vartheta_1 - \vartheta_2)$ nach der Zugabe?
2. **Zahlen:** eigenes Skript, das weder `kaffee_modell.py` noch den Skriptteil der Seite importiert. Vergleiche mit der Seite (im Browser oder den Rechenteil in Node) bei den Werten des Blatts und an mindestens 20 eigenen Einstellungen, auch an allen Reglergrenzen und mit $t > t_\mathrm{Z}$.
3. **Darstellung:** Bildschirmfotos ansehen, auch bei Extremeinstellungen (zum Beispiel wenig Kaffee, viel kalte Milch, warmer Raum; starker Tassenwärmer bei großem $kA$). Stimmen Diagramm, Säulen, Kasten und Bildbeschreibung zueinander?
4. **Bedienung:** Playwright oder ein anderer Browser ohne Internetzugriff, in beiden Sprachen: Regler (Ziehen, Plus und Minus, Zahlenfeld mit Komma und Punkt, Tastatur), Abspielen und Anhalten, Standardwerte, Neuladen.
5. **Sprache:** verständlich für das dritte Semester, keine Gedankenstriche, Formelzeichen wie im Blatt.
6. **Vergleich am Ende:** Wo weichen deine Ergebnisse von `simulation/tests/minimal_test.js` und `simulation/aufarbeitung/` ab, und wer hat recht?

## 9 Ergebnis

Bericht nach `simulation/X7_CODEX_PRUEFUNG.md`: geprüfter Stand (Commit, SHA-256), Urteil (veröffentlichungsfähig, mit Änderungen, nicht veröffentlichungsfähig), Tabelle der Abnahmekriterien mit Ergebnis, dann Befunde nach Wichtigkeit (blocker, high, medium, low) mit Stelle, Beleg und Vorschlag, nummeriert „X7-01“, „X7-02“, … Skripte und Bilder nach `simulation/x7_skripte/`. Nichts an Seite, Quellen, Tests oder Texten ändern. Pull Request nach `main` mit Bericht und Skripten; gemergt wird von der TL.
