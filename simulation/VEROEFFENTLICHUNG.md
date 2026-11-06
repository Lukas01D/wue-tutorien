# Auftrag: Veröffentlichung der Kaffee-Simulation (Codex, Sites)

> Für Codex. Geschrieben von Claude am 06.11.2026 im Auftrag der TL. Startsatz der TL: „Veröffentliche die Kaffee-Simulation nach simulation/VEROEFFENTLICHUNG.md.“ Erst nach dem Merge des Pull Requests durch die TL. Grundlage: `simulation/KONZEPT.md` 9.6, Entscheidung E2 (bis zum Sitzungstag nur für die TL sichtbar, am Sitzungstag öffentlich auf Zuruf).

## 1 Quelle

- **Nur der Merge-Commit auf `main`**, den die TL beim Zusammenführen des Pull Requests anlegt. Nie ein Arbeitszweig (`claude/…`, `codex/…`), nie eine lokale Kopie, nie eine Datei aus `ergebnisse/kaffee/` (dort liegt eine ältere Simulation mit gleichem Dateinamen).
- Vorher: `git fetch origin main`, `git checkout main`, `git pull origin main`. Notiere `git rev-parse HEAD` und prüfe, dass dieser Commit ein Merge-Commit ist, der den Zweig `claude/simulation-tool-kaffee-4kcacl` enthält (`git log --merges -1`).
- Datei: `simulation/site/index.html`. Prüfe vor dem Hochladen:
  - `sha256sum simulation/site/index.html simulation/site/Kaffee_Simulation.html`: beide gleich und gleich dem Wert in `simulation/site/BAUNACHWEIS.txt`.
  - `python3 simulation/site/bauen.py --pruefen` gibt „gleich“ aus (Python 3 mit fontTools und Brotli).
  - Stimmt etwas nicht: abbrechen und der TL melden, nichts veröffentlichen.
- Veröffentlicht wird genau diese eine Datei als Startseite (`index.html`), ohne Änderung, ohne Umbenennen von Inhalten, ohne zusätzliche Skripte, Analyse- oder Zähldienste. Die Seite braucht keine weiteren Dateien.

## 2 Adresse und Zugang

- Adresse: **`waermeuebertragung-kaffee`** (Sites).
- **Zugang zunächst nur für die TL.** Keine öffentliche Freigabe, kein Link an andere, kein Teilen in Kanälen. Die Seite hat `noindex, nofollow`; das ersetzt den Zugangsschutz nicht.
- **Öffentlich erst am Sitzungstag auf Zuruf der TL**, etwa „Schalte die Kaffee-Seite öffentlich.“ Ohne diesen Zuruf bleibt der Zugang beschränkt, auch wenn ein Termin naheliegt.
- Beim Öffentlichschalten wird an der Datei nichts geändert; nur der Zugang.

## 3 Baunachweis

Lege nach dem Hochladen `simulation/VEROEFFENTLICHUNG_NACHWEIS.md` auf einem eigenen Zweig an (zum Beispiel `codex/kaffee-veroeffentlichung`, kein Pull Request), mit:

| Punkt | Inhalt |
|:--|:--|
| Quelle | Merge-Commit auf `main` (vollständige Kennung), Datum |
| Datei im Repository | `simulation/site/index.html`, Bytes, SHA-256 |
| ausgelieferte Datei | von der veröffentlichten Adresse abgerufen (mit dem Zugang der TL oder dem Zugang von Sites), Bytes, SHA-256; **muss gleich der Datei im Repository sein** |
| Antwortkopfzeilen | Content-Type, Content-Encoding, Cache-Control, ob Sites die Datei verändert (zum Beispiel eingefügte Skripte); jede Veränderung ist ein Abbruchgrund |
| Zugang | wer die Seite sehen kann (Beleg: Einstellung in Sites; Abruf ohne Anmeldung wird abgewiesen) |
| Adresse | vollständige Adresse der Seite |

## 4 Was Codex danach meldet

An die TL, kurz:

1. Adresse der Seite.
2. Quelle (Merge-Commit) und SHA-256 der ausgelieferten Datei, gleich dem Repository: ja oder nein.
3. Zugang: nur die TL, mit Beleg.
4. Abweichungen oder Probleme (zum Beispiel veränderte Auslieferung), sonst „keine“.
5. Den Satz, mit dem die TL am Sitzungstag öffentlich schalten lässt.

Nach dem Öffentlichschalten erneut: Adresse, SHA-256 der ausgelieferten Datei (unverändert), Zugang „öffentlich“, Zeitpunkt.

## 5 Live-Abnahme durch Claude (Liste)

Claude kann eine Seite mit Zugangsschutz nicht abrufen. Die Abnahme der geschützten Seite macht deshalb die TL mit dieser Liste (Laptop und iPhone), die Prüfung der Datei Claude über die Prüfsumme aus dem Nachweis von Codex; nach dem Öffentlichschalten wiederholt Claude die Punkte 1 bis 4 selbst.

| Nr. | Prüfung | Erwartung | Ergebnis |
|:--|:--|:--|:--|
| 1 | **Datei gleich dem Bau:** SHA-256 der ausgelieferten Datei (Nachweis von Codex, nach dem Öffentlichschalten von Claude selbst abgerufen) | gleich `simulation/site/BAUNACHWEIS.txt` auf dem Merge-Commit | |
| 2 | **Fuß der Seite** | „Stand 2026-11-05 · Version …“ mit der Version aus dem Baunachweis | |
| 3 | **Rechenwerte:** Start „Tasse 1“, „4“, festhalten | ϑ₁ 34,05 °C, ϑ₂ 30,19 °C, Δ 3,85 K; Energiesäulen 34,88 und 38,57 kJ | |
| 4 | **Frage 1:** „56“ festhalten, Regler auf 56 min | Δ 3,86 K; „Schnitt“ beschriftet; nach der Vorhersage erscheint „(bis etwa 56 min)“ in der Startauflösung | |
| 5 | **Englisch:** „DE ↔ EN“ | Zahlen mit Dezimalpunkt (34.05), Texte englisch, Sprache bleibt nach Neuladen | |
| 6 | **Handy (iPhone, Safari, hochkant):** Start und Frage 1 | Diagramm oben angeheftet, Schrift gut lesbar, Frage direkt darunter, Regler mit dem Finger bedienbar, kein waagrechtes Scrollen; quer nicht angeheftet | |
| 7 | **Kurslink:** im Messblatt zwei Werte eintragen, „Kurswerte als Link teilen“, Link in neuem Tab öffnen | Rückfrage „Kurswerte aus dem Link übernehmen?“, nach „Übernehmen“ gleiche Werte; `#…` verschwindet aus der Adresse | |
| 8 | **Konsole ohne Fehler** (Laptop, Entwicklerwerkzeuge, Reiter Konsole, Seite neu laden, Start und Frage 1 bedienen) | keine roten Fehler, keine CSP-Verletzung, keine Anfragen an fremde Server (Reiter Netzwerk: nur die Seite selbst) | |
| 9 | **Zugang wirklich nur für die TL:** Adresse in einem privaten Fenster ohne Anmeldung und auf einem zweiten Gerät ohne Anmeldung öffnen | Anmeldung verlangt oder abgewiesen; die Seite ist nicht zu sehen | |
| 10 | **Offline-Ersatz:** `simulation/site/Kaffee_Simulation.html` vom Merge-Commit auf USB-Stick, ohne Netz im Browser öffnen | dieselbe Seite, Punkt 3 gleich | |
