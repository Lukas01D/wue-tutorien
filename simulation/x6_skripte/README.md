# Nachweise zur Prüfung X6

Geprüft: Commit `bee711284046211119da07d963a941c93f4568ac`, SHA-256 der Seite `ce238edd33ef5ebadb8dc06d3fbd1eba43f7aa8a8cd168a1c407f4430baad0b0`.

## Rechnung

Vom Repository-Verzeichnis aus:

```sh
python simulation/x6_skripte/eigenrechnung.py
node simulation/x6_skripte/zahlen_pruefen.cjs
python simulation/x6_skripte/referenz_pruefen.py
```

`eigenrechnung.py` ist unabhängig von Modell und Seite. Der Node-Vergleich liest den ausgelieferten Rechenblock und die Texte. `referenz_pruefen.py` importiert anschließend separat das Referenzmodell. Ergebnisse: `eigenrechnung.json`, `zahlen_ergebnis.json`, `referenz_ergebnis.json`. Für exakt null Schnittzeit gilt eine absolute Toleranz von 1e-9 s.

## Browser

Verwendet: Node 24.19.0, Playwright aus der Umgebung, `/usr/bin/chromium` Version 154.0.8037.57, axe-core 4.11.0. Eine separate axe-Installation liegt außerhalb des Repositorys:

```sh
npm install --prefix /tmp/kaffee-x6-deps --cache /tmp/kaffee-x6-npm-cache --no-audit --no-fund axe-core@4.11.0
node simulation/x6_skripte/browser_pruefen.cjs
node simulation/x6_skripte/befunde_pruefen.cjs
```

Wenn Playwright nicht vorinstalliert ist, muss auch dieses Paket bereitstehen. `X6_CHROMIUM` kann auf eine andere Chromium-Datei zeigen, `X6_AXE` auf eine andere `axe.min.js`. Die tatsächlich verwendeten Versionen bei einer Wiederholung dokumentieren.

Ein HTTP-Server ist nicht nötig: Playwright liefert die unveränderte Datei an einer abgefangenen lokalen URL aus, der Browser ist offline. Direkte Datei-Navigation ist durch die verwaltete Umgebung blockiert. Die Tests überschreiben nur eigene Nachweise in diesem Ordner. `browser_ergebnis.json` enthält die sechs Geräte-/Sprachläufe und 30 axe-Ergebnisse. `fehler: []` bezeichnet die fehlerfreie Testausführung, nicht die Freigabe der Seite; fachliche Befunde wie Reset-Inhalte und Textgrenzen werden ausdrücklich separat protokolliert.

`befunde_pruefen.cjs` reproduziert die Beanstandungen gezielt. `befunde_ergebnis.json` enthält die Statusansage samt Accessibility-Snapshot, den Timerfall, den versteckten Link und transformierte Textgrenzen. `befund_ln_390_de.png` und `befund_ln_390_en.png` zeigen die mobile Beschriftung.

`interaktiv.cjs` ist der Eingabe-Runner des eigenen Werkzeugdurchgangs. Er nimmt JavaScript-Aktionen über stdin entgegen. Die tatsächlich ausgeführten Aktionen mit Zeitstempeln stehen in `pflichtweg.jsonl`. `ENDE` beendet den Runner. Die Laufzeiten sind Agentenlaufzeiten, keine Nutzungsstudie.

Die übrigen PNGs zeigen Start, Ergebnis, ln-Ansicht und Neustart bei allen drei Bildschirmgrößen und beiden Sprachen. `pflicht_*.png` stammen aus dem eigenen Werkzeugdurchgang. Ein viewportgroßes Bild kann bei einer höheren mobilen Bühne einen Ausschnitt zeigen; das allein ist kein Produktfehler.

## Bauvergleich

Mit fontTools und Brotli verfügbar:

```sh
python simulation/site/bauen.py --pruefen
```

Hier wurde Brotli mit `python -m pip install --target /tmp/kaffee-x6-python --cache-dir /tmp/kaffee-x6-pip-cache brotli` bereitgestellt und der Bauvergleich mit `PYTHONPATH=/tmp/kaffee-x6-python` ausgeführt. Ergebnis: `gleich`. Die vorhandenen Bauprüfungen unter `simulation/tests/` wurden erst zum Schluss gelesen und nicht verändert.
