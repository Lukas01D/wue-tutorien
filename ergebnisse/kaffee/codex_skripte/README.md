# Rechenunterlagen zur Gegenprüfung X

Aus dem Repository-Hauptordner ausführen. Benötigt werden Python 3 mit SciPy sowie für die PDF-Bilder `pdftoppm`.

```bash
python ergebnisse/kaffee/codex_skripte/codex_eigenrechnung.py
python ergebnisse/kaffee/codex_skripte/codex_sensitivitaet.py
python ergebnisse/kaffee/codex_skripte/codex_zusatzpruefung.py
python ergebnisse/kaffee/codex_skripte/codex_paketvergleich.py
python ergebnisse/kaffee/codex_skripte/codex_pdf_rendern.py
```

Die zugehörigen Textausgaben sind eingecheckt. `ERSTDURCHGANG.md` protokolliert die eigenständige Herleitung vor Öffnen von Musterlösung und Paketmodell. Das Erstskript und die separat angefertigte Sensitivitätsprüfung importieren kein Paketmodell. Das Zusatzskript prüft die Nebenrechnungen und integriert das Potenzgesetz exakt. Assertions kontrollieren analytische Rechnung, direkte DGL-Integration und Wärmebilanz.

Erst der ausdrücklich getrennte Paketvergleich kopiert die zwei gelieferten Python-Dateien in `paketvergleich/`, führt die Kopien aus und vergleicht Zahlen und Ausgabe. Der Paketvergleich enthält auch SHA256-Prüfsummen zur Zuordnung des geprüften Materials. Kopien und Python-Caches werden nicht eingecheckt.

Die PDF-Sichtprüfung umfasste alle drei Aufgabenseiten, alle neun Lösungsseiten und die drei Originalabbildungen. Sie ergab keine fehlenden oder abgeschnittenen Inhalte. Die vom Renderskript erzeugten PNGs bleiben unter `pdf_notizen/` und sind vom Commit ausgenommen. Word und externe Literaturquellen wurden nicht geprüft. Am Prüfpaket wurde nichts geändert.
