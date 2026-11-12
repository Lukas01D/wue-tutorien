# Aufarbeitung des Simulationscodes: Prüfskripte

Auftrag: `simulation/AUFTRAG_Aufarbeitung_Code.md`. Stand der Prüfung und Befunde: `HALTEPUNKT.md`.
Die Skripte ändern nichts am Code. Sie rechnen mit den **gebauten** Dateien (`minimal/Kaffee_Simulation_schlank.html`, `site/index.html`), also mit dem, was veröffentlicht ist.

## Ausführen (aus der Wurzel des Repositorys)

Voraussetzungen: Python 3 mit numpy, Node mit Playwright und Chromium (wie für `simulation/tests`).

| Skript | Prüft | Dauer | Ausgabe |
|:--|:--|:--|:--|
| `python3 simulation/aufarbeitung/a1_nachrechnung.py` | Werte des Blatts aus den Formeln des Blatts und numerisch aus der Differentialgleichung, ohne `kaffee_modell.py` | 1 s | `ergebnisse/a1_nachrechnung.txt` |
| `python3 simulation/aufarbeitung/a2_vergleich.py` | schlanke Seite gegen Differentialgleichung (61 049 Einstellungen), gegen `kaffee_modell.zwei_tassen`, gegen die Hauptseite; Hauptseite gegen `kaffee_modell.rechne` | 1 min | `ergebnisse/a2_vergleich.txt` |
| `python3 simulation/aufarbeitung/a3_physik.py` | 10 physikalische Proben an der schlanken Seite | 20 s | `ergebnisse/a3_physik.txt` |
| `node simulation/aufarbeitung/a4_browser.js` | Tastatur, Fokus, Kontraste, CSP, Speicher, Netz, reduzierte Bewegung, 320 px, Beamer, Extremfälle | 20 s | `ergebnisse/a4_browser.txt`, Bilder in `bilder/` |
| `bash simulation/aufarbeitung/a5_bau.sh` | zwei Bauten bytegleich, gleich `main`, gleich Sites-Version 5 | 10 s | `ergebnisse/a5_bau.txt` |

Hilfsdatei: `js_rechnen.js` schneidet aus den gebauten Seiten den Rechenkern und die Funktionen `modell`, `obergrenze`, `bereichNr` heraus und rechnet damit in Node (ohne Browser).

Die Ausgaben der vorhandenen Tests vom selben Tag liegen ebenfalls in `ergebnisse/` (`test_kern.txt`, `test_texte.txt`, `browsertest.txt`, `minimal_test.txt`, `vergleichswerte.txt`).

## Ergebnisse vom 12.11.2026 (Stand `main` 3c2c0d2)

| Skript | Ergebnis |
|:--|:--|
| a1 | alle Werte des Blatts bestätigt |
| a2 | alle Vergleiche innerhalb der Grenzen (größte Abweichung gegen die Differentialgleichung 6,7·10⁻¹¹ K) |
| a3 | 10 von 10 |
| a4 | 14 von 15; Fehler: Kurve unter der Achse in einer Extremeinstellung (Befund A-01) |
| a5 | bytegleich, gleich Sites-Version 5 |
| vorhandene Tests | 34/34, 16/16, 107/107, 57/57 |
