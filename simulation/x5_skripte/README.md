# Eigene Prüfung X5, Stand da7deb1

Die Skripte ändern weder die Simulation noch ihre Quellen. `PASS` bezeichnet
bestandene Prüfschritte, `FAIL` reproduzierte Produktbefunde, `ERROR` ein
Prüfhindernis. Die gespeicherten JSON-Dateien enthalten die Belege der Abnahme.
Der zugehörige Bericht steht in `../X5_CODEX_ABNAHME.md`.

Umgebung des Laufs vom 06.11.2026: Python 3.12.14, Playwright 1.62.0,
Chromium 154.0.8037.57, Node 24.19.0, fontTools 4.61.1,
Brotli 1.2.1, axe-core 4.11.0. Das ältere axe als das des Baus ist eine
unabhängige, festgehaltene Prüfversion, kein Nachweis vollständiger Konformität.

## Wiederholen

Aus dem Repository, in drei getrennten Terminals beziehungsweise Prozessen:

```sh
python3 -m http.server 8765 --bind 127.0.0.1 --directory .
python3 -m http.server 8766 --bind 127.0.0.1 --directory /tmp/x5-lernzentrum-v8/dist
python3 simulation/x5_skripte/pruefung_a.py
python3 simulation/x5_skripte/pruefung_b.py
python3 simulation/x5_skripte/pruefung_layout.py
python3 simulation/x5_skripte/pruefung_ergaenzung.py
```

Der zweite Server benötigt den Tag `hauptadresse-v8-2026-11-05` von
`Lukas01D/waermeuebertragung-lernzentrum`, Commit
`c2af968fab5c883a52d8323771b7eebb5a969373`, flach und ausgedünnt nach `/tmp`
geklont. Es werden nur Dateien gelesen. Die Vergleichsbilder verwenden die
Simulationsseiten der Themen 01 und 02. Alte Bilder `lernzentrum_v8_*` zeigen
ergänzend die Einstiegsansicht, `vorbild_thema*` die richtige Simulation.

Die Browserprüfung erwartet axe unter `/tmp/x5-tools/node_modules/axe-core`:

```sh
npm install --prefix /tmp/x5-tools --cache /tmp/x5-npm-cache --no-audit --no-fund axe-core@4.11.0
python3 -m pip install --target /tmp/x5-python brotli==1.2.1
PYTHONPATH=/tmp/x5-python python3 simulation/site/bauen.py --pruefen
```

Playwright wird als Python-Paket, Chromium als Systemprogramm benötigt.
Der Pfad `/usr/bin/chromium` kann für andere Umgebungen angepasst werden.
Diese Cloud-Umgebung benötigt für den Browser und lokale Server freigegebene
Netzwerkfähigkeiten. Ihre Browserrichtlinie verbietet `file:`. Der Ersatztest
lädt die unveränderten HTML-Bytes bei `offline=True` über eine lokale
Playwright-Route in einen frischen Browserkontext. Er ist ausdrücklich kein
Test des Öffnens aus der Dateien-App eines iPhones.

`pruefung_b.py TESTNAME` wiederholt gezielt einen Prüfschritt und ersetzt nur
dessen Eintrag in `ergebnis_b.json`. Daher enthält diese Datei den abschließenden
Stand, nicht die Summe aller Wiederholungen. Zur Latenz gab es einen ersten
Lauf mit einem Ausreißer von 118,5 ms (Median 2,6 ms). Der gezielte zweite Lauf
ohne parallel laufende Prüfungen ist in `ergebnis_b.json` gespeichert.

`pruefung_a.py` importiert keines der Projektmodelle. Mischbilanz und
exponentielle Abkühlung sind eigenständig implementiert; das Maximum wird
numerisch mit Intervallsuche bestimmt, die benötigte Milchtemperatur mit
Nullstellensuche. Verglichen wird mit dem JavaScript im gebauten Artefakt.
Zusätzliche SVG-Prüfungen lesen Achsen und Linien aus dem Browser und vergleichen
3.872 gezeichnete Punkte mit der eigenen Rechnung. Die 400 Zufallssätze sind
mit Seed 20261106 wiederholbar, die Verteilung steht in Skript und Ergebnis.

`stichprobe_kern.txt` und `stichprobe_texte.txt` sind erst nach der eigenen
Nachrechnung erzeugte Gegenproben mit den vorhandenen Tests. Sie ersetzen die
eigene Prüfung nicht.
