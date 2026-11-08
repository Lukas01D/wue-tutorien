# Baubericht Fassung 3: Kaffee-Simulation, schlank

> Bau durch Claude am 08.11.2026 auf dem Zweig `claude/kaffee-simulation-v3-qw4zb2` (von `main`, 7b235ca) nach `simulation/KONZEPT_F3.md` mit den Entscheidungen der TL vom 08.11.2026 (D1 bis D10 wie empfohlen, T1 bis T3; Beleg `simulation/ENTSCHEIDUNGEN_F3.md`). Fassung 2 (Bau vom 06.11.2026, `simulation/BAU_BERICHT.md`) ist damit in `simulation/site/` ersetzt; ihre Berichte und Prüfungen bleiben als Archiv im Repository. **Status: gebaut, in Chromium geprüft und von Codex unabhängig geprüft (X6, „mit Änderungen“, vier Befunde); alle vier Befunde übernommen und mit Tests belegt (`simulation/X6_ANTWORT.md`). Bereit für den Pull Request.**

## 1 Stand

| Punkt | Wert |
|:--|:--|
| Seite | `simulation/site/index.html`, bytegleich `Kaffee_Simulation.html`, 175 471 Bytes (Fassung 2: 433 303 Bytes, also 60 % kleiner), SHA-256 in `simulation/site/BAUNACHWEIS.txt` |
| Bau | `python3 simulation/site/bauen.py`; `--pruefen` vergleicht und gibt „gleich“ aus (deterministisch) |
| Modell | `simulation/modell/kaffee_modell.py` unverändert (SHA-256 eb7efc1d…757a1, bytegleich mit dem Startpaket); `werte.py` unverändert aus dem Startpaket (08e1caee…e259); `rechne()` in der Seite bytegleich mit `main` (SHA-256 6fded445…2f9a) |
| Umgebung | Python 3.13 mit fontTools und Brotli, Node 22, Playwright mit Chromium (vorinstalliert), axe-core 4.14.0 (`simulation/tests/package.json`); WebKit und Bildschirmleser nicht verfügbar |

## 2 Was gebaut ist

| Datei | Inhalt |
|:--|:--|
| `site/src/vorlage.html` | Gerüst: Kopf mit „DE ↔ EN“, Zweck, 01 Vorhersage, Bühne (Kernzahlen, Kernsatz, Auftragszeile, Diagramm, Legende, Annahmenzeile, Regler), 02 Warum?, 03 Messung dazulegen, 04 Zum Schluss, Weiterdenken (nach dem Tutorium oder zu Hause), Modell, „Von vorn“; gesperrte Abschnitte tragen `data-ab` (Stufe der Freigabe) |
| `site/src/stil.css` | Optik A mit der Synthese aus Anhang A des Konzepts; Laptop und Beamer zwei Spalten mit angehefteter Bühne, Handy eine Spalte |
| `site/src/modell.js` | Block MODELL (`P`, `K`, `rechne()` wie `kaffee_modell.py`), `STANDARD` und `BEISPIEL` (einzige Stelle der Werte des Blatts, SE6), `parameter()` (kA fest, gleichwertiger Messwert nach 10 min), `kABlatt()`, `auswerten()` |
| `site/src/oberflaeche.js` | Zustände 0 bis 2, Sperren, Regler mit Lineal, Plus und Minus, Zahlenfeld, Diagramm (auch ln-Ansicht), Säulen, Messpunkte, Aufträge, Speicher im Browser, Sprache |
| `site/src/texte_de.txt`, `texte_en.txt` | alle Texte (du-Form; Englisch nach dem Glossar der Fassung 2); Zahlen als Platzhalter aus `zahlen.py` |
| `site/zahlen.py` | Zahlen der Texte aus `kaffee_modell.py` mit `werte.py` |
| `site/schriften_teilen.py`, `src/schriften/` | IBM Plex Sans 400 und 600, Plex Mono 400 und 600, Plex Math als Teilmengen (49 kB), OFL-Lizenztexte |
| `site/bauen.py`, `tex2mathml.py` | Bau mit CSP-Hashes, Formeln nach MathML, Zeichenprüfung (jedes Zeichen in einer eingebetteten Schrift) |
| `tests/` | `test_kern.py`, `test_texte.py`, `browsertest.js`, `bilder.js`, Ergebnisdateien |
| entfernt | `src/erweiterung.js`, `src/hilfen.js`, `src/regler.json`, Fira-Schriften, `modell/kaffee_erweitert.py`, alle Tests der Fassung 2, `simulation/kurzkarte/`, `simulation/EINSATZ_TUTORIUM.md` (Kurslink, QR-Code und Fragen der Fassung 2); erhalten bleibt nach Entscheidung Q1 ein schlanker QR-Code nur mit der Adresse in `simulation/qr/` (SVG, PNG, Erzeugerskript) |

## 3 Abweichungen vom Konzept (mit Grund; je ein Eintrag in `ENTSCHEIDUNGEN_F3.md`, Abschnitt 5)

| Nr. | Abweichung | Grund |
|:--|:--|:--|
| A1 | **du-Form durchgehend**, auch in 02 bis 04 und in den Aufträgen (Konzept: „Wählt“, „Legt“, „Notiert“) | G2: Die Seite muss allein zu Hause passen; der Kernsatz nach Leitlinie 6 steht ohnehin in du-Form |
| A2 | Kernsatz mit eigenen Werten aus e nur bei den Werten des Blatts; „stimmen überein“ bis 0,1 K Abweichung | Die eigene Rechnung gilt für das Blatt; Rundung auf zwei Stellen und ein auf 0,1994 gerundetes kA ergeben weniger als 0,03 K |
| A3 | Überschriften für 03 („Rechnung, Simulation und Messung“) und 04 („Was zeigt welches Medium?“) | Jeder Abschnitt braucht eine Überschrift (Bildschirmleser, Signalisierung) |
| A4 | Hinweis bei Messwerten über dem ersten Wert von Tasse 2; Sprung „Zum Diagramm ↑“ am Handy | L2 C2.9 (Plausibilität); am Handy steht das Diagramm über den Eingabefeldern |
| A5 | Bühne am Laptop scrollt in sich, wenn sie höher als der Bildschirm wird (nur bei geöffneten „Ausgangswerten“ an kleinen Bildschirmen) | Sonst wären die unteren Regler bei angehefteter Bühne erst am Seitenende erreichbar |
| A6 | Reglerbereiche: Milch 2 bis 80 °C (vor Auftrag 3 bis 30 °C), Zugabe 1 bis 180 min, Kaffee 60 bis 95 °C, Raum 10 bis 30 °C, kA 0,05 bis 0,80 W/K (Schritt 0,005), Milch 10 bis 100 ml | Das Konzept legt keine Bereiche fest; Bereiche wie in Fassung 2, kA nach oben auf 0,80 W/K begrenzt (offene Tasse etwa 0,43 W/K) |
| A7 | Zeichen ○ □ ● ■ der Legende aus Plex Math (Ersatz im Schriftstapel) | Plex Sans und Mono haben diese Zeichen nicht |
| A8 | Rückmeldung c beginnt mit „Nein.“ | Klare Rückmeldung mit Begründung (L1 S5), Wortlaut sonst wie im Konzept |
| A9 | Kein Verweis „ohne Vorhersage aufdecken“ | G1; die TL kann am Beamer einfach eine Vorhersage wählen |

## 4 Tests und Ergebnisse (Chromium im Cloud-Container)

```
python3 simulation/site/bauen.py --pruefen
python3 simulation/tests/test_kern.py
python3 simulation/tests/test_texte.py
cd simulation/tests && npm ci && cd ../..
node simulation/tests/browsertest.js
node simulation/tests/bilder.js
```

| Test | Ergebnis | Inhalt |
|:--|:--|:--|
| `bauen.py --pruefen` | gleich | Bau reproduzierbar, keine Zeichenwarnung |
| `test_kern.py` | 34 von 34 | `rechne()` bytegleich mit `main`; STANDARD und Beispielwerte gleich `werte.py`; alle Prüfwerte relativ unter 1e-9; 2006 Parametersätze (Blatt, 2000 Zufallssätze, Ränder) gegen `kaffee_modell.py`; Energiebilanz ohne Verdunstung; Zahlen der Aufträge und Rückmeldungen |
| `test_texte.py` | 16 von 16 | Schlüssel und Platzhalter DE = EN; keine Gedankenstriche; Dezimalzeichen; du-Form; Kernsatz wörtlich; T1, T2, T3; Startkarte ohne Ergebnis; jede Zahl mit Herkunft |
| `browsertest.js` | 107 von 107 (davon 14 zu X6) | Größe; CSP greift; Sperren Z0 und Z1 im ganzen DOM; Kernzahlen; Kernsatz in drei Fassungen; Säulen ohne und mit Zahlen; Regler (Grenze 30 °C, Komma, Punkt, Tastatur, kA fest, Werte des Blatts); Messpunkte, Beispielwerte, ln-Ansicht; drei Aufträge; Schluss; Speicher, „Von vorn“, gesperrter Speicher; Englisch; kein waagerechtes Scrollen bei 320 bis 1920 px in beiden Sprachen und bei 200 % Text; Beamer 1280 × 720 und 1366 × 768; Handy 390 × 844; Zielgrößen; Fokus; axe-core in 12 Zuständen ohne Verstoß; Reglerschritt im Median 2,3 ms |
| `bilder.js` | 23 Bilder | `simulation/bildschirmfotos/f3/` (Liste in `LISTE.txt`), von Claude angesehen; dabei gefunden und behoben: Beschriftung bei sich kreuzenden Kurven, „−0,00 K“, zu hohe Bühne bei offenen Ausgangswerten |

## 5 Abnahmekriterien (Abschnitt 4 des Auftrags)

| Kriterium | Stand | Beleg |
|:--|:--|:--|
| Pflichtweg höchstens 8 min | Schätzung Claude: 6,5 bis 8,5 min (01 etwa 1,5; 02 etwa 2,5; 03 etwa 2; 04 etwa 1,5); Schätzung der Prüfrolle X6 offen, Messung beim ersten Einsatz | O4 |
| Regler nach SE2 gruppiert | erfüllt | D1; Browsertest |
| Seite allein ohne Tutorium (G2) | erfüllt: du-Form, Beispielwerte, keine Tafel nötig; Vertiefung für zu Hause | T1, A1 |
| Gestaltungssynthese mit Tabelle und Quellen | erfüllt | `KONZEPT_F3.md`, Anhang A |
| Prüfwerte exakt (unter 1e-9) | erfüllt | `test_kern.py` |
| 15 Kriterien L2 D1 | 13 erfüllt, 1 teilweise, 1 bewusst nicht | Abschnitt 6 |
| Startkarte verrät nichts; keine Zahl vor der Vorhersage | erfüllt (DOM, versteckte Teile, Attribute, Ansagen) | Browsertest Z0, Z1 |
| Keine Verdunstung im Modell | erfüllt | `test_kern.py` |
| DE und EN gleichwertig, offline eine Datei, axe-core ohne Verstoß, Beamer lesbar | erfüllt (Chromium) | Browsertest |
| Kleiner als heute | erfüllt: 175 471 gegen 433 303 Bytes | Browsertest |
| `ENTSCHEIDUNGEN_F3.md` mit jeder Entscheidung der TL | erfüllt, wird nachgeführt | |

## 6 Prüfliste L2 D1 (Ergebnis nach dem Bau)

| Nr. | Kriterium | Ergebnis | Wo |
|:--|:--|:--|:--|
| S1 | Zweck am Anfang | erfüllt | Zweck-Satz über der Startkarte |
| S2 | Vorhersage mit Grund vor den Kurven | erfüllt | 01: Tasse und Grund Pflicht (T3) |
| S3 | ersetzt nicht die Rechnung | erfüllt | „nach Teil e“; Säulenzahlen erst nach 02; warme Milch erst nach Auftrag 3 |
| S4 | Zusammenhang sichtbar | teilweise | Säulen, Bilanz und Lösung im Modell; Bilanzraum-Skizze und Wärmestrom-Ansicht bewusst weggelassen (G1) |
| S5 | Startwerte, Bereiche, Herkunft | erfüllt | Ausgangswerte mit „vorläufig“, Skalen mit Min und Max, Beispielwerte gekennzeichnet |
| S6 | Annahmen bei den Ergebnissen | erfüllt | Annahmenzeile unter dem Diagramm |
| S7 | wofür das Modell taugt | erfüllt | Modell, Abschnitt „Grenzen“ |
| S8 | Rechenweg offen, Prüfwert aus dem Blatt | erfüllt | Modell: d1 und d2; Block MODELL im Quelltext |
| S9 | Vergleich mit Messwerten, nur er prüft das Modell | erfüllt | 03, Kernsatz |
| S10 | Modellvarianten nebeneinander | bewusst nicht | Becher und Voreinstellungen entfallen (Blatt, G1); Variation über die Regler |
| S11 | Form passt zum Inhalt | erfüllt | Direktbeschriftung, gleiche Farben, Klammer Q₂ − Q₁ |
| S12 | Ablauf selbst steuern | erfüllt | keine Animation; „Werte des Blatts“, „Von vorn“ |
| S13 | offline, responsiv, barrierearm, zweisprachig | erfüllt (Chromium) | Browsertest; Geräte offen |
| S14 | geteilte Messwerte ohne Personenbezug | erfüllt | kein Teilen; nur im Browser; Plausibilitätshinweis |
| S15 | keine Punkte und Uhr, Schluss mit Grenzen | erfüllt | 04 |

## 7 Prüfung X6 durch Codex

Bericht `simulation/X6_CODEX_PRUEFUNG.md` (Stand bee7112, Nachweise `simulation/x6_skripte/`): Rechnung unabhängig bestätigt (858 Vergleiche, größte relative Abweichung 8,5e-12), Pflichtweg geschätzt 7,5 min, 30 axe-Prüfungen ohne Verstoß. Befunde X6-01 (high, Neustart), X6-02 (medium, Entscheidungsprotokoll), X6-03 und X6-04 (low): alle übernommen, Antwort mit Beleg in `simulation/X6_ANTWORT.md`.

## 8 Offen

| Was | Wer | Wo |
|:--|:--|:--|
| iPhone mit Safari, Android, Bildschirmleser, Beamer im Hörsaal | TL | `simulation/ABNAHME_IPHONE.md` (neu für Fassung 3) |
| Zeit des Pflichtwegs mit Studierenden (Ziel höchstens 8 min) | TL, erster Einsatz | O4 |
| Messung im Januar 2027: ändert nur `STANDARD` und `BEISPIEL` in `site/src/modell.js` (und `werte.py`) | TL, danach Bau | O5, SE6 |
| Text für die Hinweise (ersetzt „Stand der Seite“) | TL nach dem Merge | `simulation/HINWEISE_TEXT_F3.md` |
| Veröffentlichung (zuerst privat prüfen, dann ersetzen, V1) und Live-Abnahme | TL beauftragt Codex nach dem Merge | `simulation/VEROEFFENTLICHUNG.md` |
