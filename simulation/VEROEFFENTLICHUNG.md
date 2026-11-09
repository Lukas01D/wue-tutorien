# Auftrag: Veröffentlichung der Kaffee-Simulation Fassung 3 (Codex, Sites)

> Für Codex. Geschrieben von Claude am 08.11.2026 (Startprompt Fassung 3, Schritt 7). Startsatz der TL: „Veröffentliche die Kaffee-Simulation Fassung 3 nach simulation/VEROEFFENTLICHUNG.md.“ Erst nach dem Merge des Pull Requests durch die TL. Der Auftrag für Fassung 2 und sein Nachweis stehen in der Git-Geschichte und in `simulation/VEROEFFENTLICHUNG_NACHWEIS.md`.

## 1 Quelle

- **Nur der Merge-Commit auf `main`**, den die TL beim Zusammenführen anlegt; er muss den Zweig `claude/kaffee-simulation-v3-qw4zb2` enthalten (`git log --merges -1`). Nie ein Arbeitszweig, nie eine Datei aus `ergebnisse/kaffee/` oder `simulation/f3_entwurf/` (dort liegt nur das Gestaltungsmuster).
- Vorher `git fetch origin main`, `git checkout main`, `git pull origin main`; `git rev-parse HEAD` notieren.
- Datei `simulation/site/index.html`. Vor dem Hochladen prüfen:
  - `sha256sum simulation/site/index.html simulation/site/Kaffee_Simulation.html`: beide gleich und gleich dem Wert in `simulation/site/BAUNACHWEIS.txt`;
  - `python3 simulation/site/bauen.py --pruefen` gibt „gleich“ aus (Python 3 mit fontTools und Brotli);
  - Fuß der Seite: „Stand 2026-11-08 · Version …“ mit den ersten zehn Zeichen der Quellprüfsumme aus dem Baunachweis.
  - Stimmt etwas nicht: abbrechen und der TL melden.
- Genau diese eine Datei als `index.html`, unverändert, ohne zusätzliche Skripte, Analyse- oder Zähldienste.

## 2 Adresse und Zugang (Regel R1 der TL, 09.11.2026: immer öffentlich, ohne private Zwischenstufe)

> Geändert von Claude am 09.11.2026 nach der Regel R1 der TL; ersetzt V1 („zuerst privat prüfen, dann ersetzen“, 08.11.2026). Der frühere Wortlaut steht in der Git-Geschichte dieser Datei.

1. **Veröffentlichungen in wue-tutorien sind immer öffentlich.** Es gibt keine private Zwischenstufe und keine private Prüf-Site mehr; neue Fassungen werden direkt unter ihrer Adresse öffentlich veröffentlicht (Sites-Zugang `public`).
2. Hauptadresse der Kaffee-Simulation: **`waermeuebertragung-kaffee`**; eine neue Fassung wird dort als neue Version derselben Site veröffentlicht, die Adresse und der QR-Code in `simulation/qr/` bleiben gültig. Die Prüfadresse `waermeuebertragung-kaffee-pruefung` (Fassung 3) ist seit 08.11.2026, 22:34 Uhr ebenfalls öffentlich.
3. Die Prüfung erfolgt nach der Veröffentlichung: Live-Abnahme durch Claude (Abschnitt 5) und Gerätetest durch die TL (`simulation/ABNAHME_IPHONE.md`). Ergibt sie einen Fehler, wird er behoben und neu veröffentlicht.
4. Nur der Merge-Commit auf `main` ist Quelle (Abschnitt 1); daran ändert R1 nichts.

## 3 Baunachweis

`simulation/VEROEFFENTLICHUNG_NACHWEIS.md` auf einem eigenen Zweig ergänzen (Abschnitt „Fassung 3“, kein Pull Request): Merge-Commit, Bytes und SHA-256 der Datei im Repository und der ausgelieferten Datei (müssen gleich sein), Antwortkopfzeilen (keine Veränderung durch Sites), Zugang mit Beleg, Adresse, Sites-Version.

## 4 Meldung an die TL

Adresse, Sites-Version, Quelle und SHA-256 gleich dem Repository (ja oder nein), Zugang öffentlich, Zeitpunkt, Abweichungen oder „keine“.

## 5 Live-Abnahme (Claude, danach in `simulation/LIVE_ABNAHME.md`)

| Nr. | Prüfung | Erwartung |
|:--|:--|:--|
| 1 | Datei gleich dem Bau | Skript und Stil zeichengleich mit `simulation/site/index.html` auf dem Merge-Commit; Fuß „Stand 2026-11-08 · Version …“ wie im Baunachweis |
| 2 | Startkarte | keine Kurven, keine Ergebniszahl; Knopf erst nach Tasse und Grund aktiv |
| 3 | Tasse 1, Grund, 43,85 und 40,29, festhalten | Kernzahlen 43,85 °C, 40,29 °C, 3,56 K; „Simulation und deine Rechnung stimmen überein“ |
| 4 | Erklärung a, Antwort festhalten | Rückmeldung mit 25,49 und 28,90 kJ, Säulen mit 3,41 kJ |
| 5 | Milchtemperatur über 30 °C | erst nach der Vermutung in Auftrag 3 möglich |
| 6 | Englisch | Dezimalpunkt (43.85), englische Texte, bleibt nach Neuladen |
| 7 | Konsole und Netzwerk | keine Fehler, keine CSP-Verletzung, keine Anfragen an fremde Server |
| 8 | Laptop und Beamer (1280 × 720) | Kernzahlen, Diagramm und beide Regler ohne Scrollen im Bild |
| 9 | Aufräumen | Einträge `kaffee-simulation-f3` und `kaffee-simulation-sprache` im lokalen Speicher löschen |
