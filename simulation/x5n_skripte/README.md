# Eigene Nachprüfung X5, Stand 34bdfa6

Bericht: `../X5_CODEX_NACHPRUEFUNG.md`. Alle Ergebnisdateien stammen aus
eigenen Läufen auf den im Bericht identifizierten HTML-Bytes.
`auswertung.json` enthält die aktuelle Provenienz und kompakte Auswertung.
Die Dateigröße ist nach der Entscheidung der TL kein Prüfkriterium.

## Dateien und Ergebnisse

- `pruefung_a.py`, `pruefung_b.py`, `pruefung_layout.py`,
  `pruefung_ergaenzung.py`: bytegleiche Kopien der ursprünglichen eigenen
  X5-Skripte. Alte Skripte und Belege unter `../x5_skripte/` bleiben erhalten.
- `nachpruefung.py`: neue, unabhängige Prüfungen der Entscheidungen, der
  Quellenumschaltung, Sperren, Fachtexte, Beameransicht und Beschriftungen.
- `bedienung.py`: Zeitreihe nach Schriftwechsel, Linkbestätigung und Fokus,
  Anheften, zweiter Tipp sowie die Rücknahme ungültiger Messblatteingaben.
- `auswertung.py`: wertet Rohdaten aus und prüft die Identität der Altskripte.
- `ergebnis_*.json`: vollständige Messdaten. `lauf_*.txt`: Konsolenausgaben.
  Die gezielten Nachläufe `lauf_nachpruefung_texte.txt` und
  `lauf_messfehler.txt` dokumentieren einzelne Prüfungen; die JSON-Dateien
  enthalten den abschließenden Stand.
- `bilder/`: eigene Browserbilder. Dateinamen aus den unveränderten alten
  Skripten wie `becherbilanz_falsches_CG.png` sind historische Testnamen und
  keine Bewertung des jetzt richtigen Bildinhalts.

`pruefung_a.py` schreibt einen **fest codierten alten Commit** in die
Rohdaten. Dieser Text wurde wegen der verlangten Skriptidentität nicht
geändert. Maßgeblich sind `auswertung.json`, der Artefakthash und der Bericht.

Der alte Quellenwechseltest meldet weiterhin ERROR: `check()` kann das
gewollte Zurücksetzen der Auswahl nicht als Erfolg behandeln. Der neue Test
`X5_03` verwendet `click()` und prüft Ablehnung, unveränderte Rechnung,
Messwerterhalt und Ansage. Beide Resultate bleiben getrennt nachvollziehbar.
Der Layoutlauf enthält eine kurzzeitige Überschreitung der Anhefthöhe beim
Schriftwechsel. Sie wird nicht aus der Auswertung entfernt; siehe X5N-01.

## Wiederholen

Voraussetzung: Python mit Playwright, Chromium unter `/usr/bin/chromium`,
fontTools und Brotli, axe-core 4.11.0 unter `/tmp/x5-tools/node_modules`.
Versionen stehen im Bericht. Netzfähigkeit für Browser und lokale Server
muss in dieser Umgebung freigegeben sein. Die Seite selbst fordert keine
externen Ressourcen an.

In getrennten Prozessen aus dem Repository:

```sh
python3 -m http.server 8765 --bind 127.0.0.1 --directory .
python3 -m http.server 8766 --bind 127.0.0.1 --directory /tmp/x5-lernzentrum-v8/dist
```

Der zweite Server ist ausschließlich für die Vergleichsaufrufe der
unveränderten Altskripte erforderlich. Quelle: Lernzentrum v8, Tag und Commit
wie im Bericht, nur `dist` nach `/tmp` ausgecheckt. Ein anfänglicher Lauf der
Ergänzung brach wegen des noch fehlenden zweiten Servers am abschließenden
Vorbildvergleich ab. Nach dessen Bereitstellung wurde das vollständige
unveränderte Skript erneut erfolgreich ausgeführt.

```sh
PYTHONPATH=/tmp/x5-python python3 simulation/site/bauen.py --pruefen
python3 simulation/x5n_skripte/pruefung_a.py
python3 simulation/x5n_skripte/pruefung_b.py
python3 simulation/x5n_skripte/pruefung_layout.py
python3 simulation/x5n_skripte/pruefung_ergaenzung.py
python3 simulation/x5n_skripte/nachpruefung.py
python3 simulation/x5n_skripte/bedienung.py
python3 simulation/x5n_skripte/auswertung.py
```

Die neuen Skripte können mit einem Testnamen als Argument gezielt wiederholt
werden. Die übrigen Einträge derselben JSON-Datei bleiben dann erhalten.
Die alte Bedienprüfung dauert wegen des Quellenwechselabbruchs und der
30-s-Leistungsprobe etwas länger; der einzelne ERROR ist oben eingeordnet.

Die Prüferwartungen stammen aus den Entscheidungen und der unabhängigen
Bilanzrechnung der ursprünglichen eigenen Skripte. Erwartungswerte werden
nicht aus den Tests von Claude oder den Projektmodellen importiert.

`file_probe.json` dokumentiert den neuen erfolglosen Aufruf der absoluten
`file:`-Adresse von `simulation/site/index.html` mit Chromium im Offlineprofil.
Die Browserrichtlinie verhindert ihn. Die passende Offline-Gegenprobe über
eine lokale Route und die Grenzen dieses Ersatzes stehen im Bericht.
