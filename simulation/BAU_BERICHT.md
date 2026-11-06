# Baubericht: Simulation „Kaffee mit Milch“

> Bau durch Claude nach `simulation/BAU_AUFTRAG.md` (Stand 6526feb, Rollentausch, Entscheidung der TL vom 05.11.2026). Grundlage: `simulation/KONZEPT.md` Fassung 2 (93cb32e). Teile 0 bis 7 abgeschlossen am 06.11.2026, danach Korrekturrunde nach der Abnahme X5 (06.11.2026). **Status: abnahmebereit bis auf die Fragen Q1 bis Q7 an die TL und die Nachweise in der echten Welt; streng nach Bauauftrag 6 noch unvollständige Übergabe** (ein medium-Wortlaut wartet auf Q2). Einzelheiten am Ende.

## Umgebung (Teil 0)

| Punkt | Ergebnis |
|:--|:--|
| Repository `wue-tutorien`, Zweig `claude/simulation-tool-kaffee-4kcacl` | vorhanden, Stand 6526feb zu Beginn |
| Kaffee-Zweig `claude/kaffee-pruefung-sgvo1r` | erreichbar, Stand f8a5ce3 (wie erwartet) |
| Lernzentrum-Repository `Lukas01D/waermeuebertragung-lernzentrum` | nur Lesen, flach und ausgedünnt geklont nach `/home/user/lernzentrum_v8` (außerhalb dieses Repositorys), Tag `hauptadresse-v8-2026-11-05`, Commit c2af968fab5c883a52d8323771b7eebb5a969373 (2026-11-05 11:09 +0100, „Merge pull request #25 from Lukas01D/runde-12-v8-abnahme“); nicht als Arbeitsverzeichnis angemeldet |
| Python | 3.13.18 (numpy 2.5.3, reportlab 5.0.1) |
| Node, npm | 22.23.4, 10.9.9 |
| Playwright, Chromium | 1.63.0 mit vorinstalliertem Chromium 1243 (`/opt/pw-browsers`) |
| axe-core | 4.14.0, lokal und festgehalten in `simulation/tests/package.json` und `package-lock.json` (nur Prüfwerkzeug, nicht Teil der Seite) |
| pdftotext, pdftoppm, pandoc | vorhanden |
| Live-Adressen Lernzentrum und Werkstatt | **nicht erreichbar**: beide antworten mit 401 („Sign in required“), mit curl und im zweiten Versuch mit Chromium. Am 04.11.2026 war die Werkstatt noch offen (Bildschirmfotos von damals als ergänzender Vergleich). Ersatz: Lernzentrum lokal aus einer zweiten Kopie des Tags. |
| WebKit | **nicht verfügbar** (nicht in `/opt/pw-browsers`). Nicht nachinstalliert: Die Umgebung untersagt `playwright install`, weil es die vorhandene Chromium-Einrichtung stören kann. Alle Browserprüfungen sind Chromium-Prüfungen; der Safari-Nachweis bleibt für die TL (`simulation/ABNAHME_IPHONE.md`). |
| Bildschirmleser | keiner verfügbar (nur kopflose Browser); Nachweis bleibt offen |

## Quellcommits und Prüfsummen

| Quelle | Commit | SHA-256 |
|:--|:--|:--|
| `kaffee_modell.py` (Kaffee-Zweig, `pruefung/Kaffee_Pruefpaket_2026-10-23/umsetzung/Arbeitsordner/kaffee/`) | zuletzt geändert in 560b8d4, gelesen auf f8a5ce3 | eb7efc1d5322b629e1e11494f7c70fa8d8d54ec60e555874326fa491a31757a1 |
| `Kaffee_Simulation.html` (Kaffee-Zweig, `ergebnisse/kaffee/fertig/`, gleich `ergebnisse/kaffee/simulation/` dort; vier Fragen mit Vorhersage) | zuletzt geändert in 174e613, gelesen auf f8a5ce3 | 6f16a78ca8de373eb997ab9dea69b222f9bc57c9c97d7def3f49f9d01c6fdc83 |
| `Kaffee_Simulation.html` auf `main` (Stand 31.10.2026, ältere Fragen) | im Repository | 43f333149afd1fd805a499bf158cffb6e3beafd62e08fed134376fd436d259d5 |
| `test_simulation.py` (`ergebnisse/kaffee/simulation/`) | im Repository | fe9a55d2d37fd1e579757d47959c4c4d31d6ef77d59173f866c5bb047dec7dd3 |
| `browsertest.js` (`ergebnisse/kaffee/simulation/`) | im Repository | 354afbecf0d8c28a0ea94e7879a0b3ff501b1471e3bc5b17ff1ea223be9a92cd |
| Lernzentrum v8 | Tag `hauptadresse-v8-2026-11-05`, c2af968 | |

Ergänzung zur Umgebung (06.11.2026): Chromium 153.0.8010.12 über Playwright 1.63.0 (für alle Browserprüfungen), Node 22.23.4, Python 3.13.18 mit fontTools 4.68.0 (Schriftteilmengen, Zeichenprüfung beim Bau). **Alle Browserprüfungen sind Chromium-Prüfungen im Cloud-Container**; Messwerte zur Leistung stammen aus diesem Container, nicht von einem Gerät der TL.

## Gebauter Stand

| Datei | Inhalt |
|:--|:--|
| `simulation/site/index.html`, bytegleich `Kaffee_Simulation.html` | die Seite (eine Datei, offline, CSP mit Hashes, Schriften eingebettet); Größe und SHA-256 in `simulation/site/BAUNACHWEIS.txt` und unten im Status |
| `simulation/site/src/` | Quellen: `vorlage.html`, `stil.css`, `modell.js` (Block MODELL wörtlich, SHA-256 b32e3f9d…7d24), `erweiterung.js`, `hilfen.js`, `oberflaeche.js`, `texte_de.txt`, `texte_en.txt`, `regler.json`, `schriften/` (Teilmengen Fira Sans, Fira Math, OFL-Lizenztexte) |
| `simulation/site/bauen.py` | Bauskript (deterministisch; `--pruefen` vergleicht, `--ziel` baut zur Probe in einen anderen Ordner); `zahlen.py` setzt alle Ergebniszahlen der Texte aus der Python-Referenz; `tex2mathml.py` setzt die Formeln (Ä24) |
| `simulation/modell/` | wörtliche Kopie `kaffee_modell.py` (Herkunft `HERKUNFT.md`), Python-Referenz der Erweiterungen `kaffee_erweitert.py` |
| `simulation/tests/` | `test_kern.py` (Rechenkern gegen Python), `test_texte.py` (Texte und Zahlen), `browsertest_bau.js` (Chromium), `erwartung_browser.py` (Erwartungen aus Python), `bilder_bau.js` (Abdeckungsbilder), Ergebnisdateien `*_ergebnis.txt` |
| `simulation/ZUSTAENDE.md`, `VORBILD_LERNZENTRUM.md`, `PROTOTYPEN.md` | Ablauf und Zustände, Vorbild, Prototypen und Wahl |
| `simulation/gutachten/` | Gutachten G1 bis G10 (drei Runden) und Runde 4 nach der Korrekturrunde (`*_R4.md`), `ZUSAMMENFUEHRUNG.md` |
| `simulation/X5_CODEX_ABNAHME.md`, `simulation/x5_skripte/` | Abnahme X5 durch Codex (Zweig `codex/x5-abnahme-da7deb1`, eingemergt) |
| `simulation/X5_ANTWORT.md`, `simulation/x5_regression/` | Antwort auf X5 mit Nachweis je Befund; Kopie der Codex-Skripte mit Läufen auf dem neuen Stand |
| `simulation/EINSATZ_TUTORIUM.md`, `simulation/kurzkarte/` | Begleitmaterial (Teil 5) |
| `simulation/ABNAHME_IPHONE.md` | Abnahmeliste für die TL am iPhone |
| `simulation/bildschirmfotos/bau/`, `/prototypen/`, `/lernzentrum/` | Bilder |

## Nachweistabelle

Status nur „bestanden“, „fehlgeschlagen“, „nicht geprüft“, „nicht anwendbar“. BT = `simulation/tests/browsertest_bau.js` (Prüfungsname in Anführungszeichen), KT = `simulation/tests/browsertest_korrektur.js` (Korrekturrunde, Befund-ID), TK = `test_kern.py`, TT = `test_texte.py`, Bild = `simulation/bildschirmfotos/bau/`. Stand nach der Korrekturrunde vom 06.11.2026.

### Muss (Konzept 4.1)

| ID | Umsetzung | Nachweis | Status |
|:--|:--|:--|:--|
| M-1 Modelltreue | Block MODELL wörtlich aus `kaffee_modell.py` in `modell.js`; Erweiterungen in `erweiterung.js` | TK 134 und 135 von 135; G3 30 von 30 Zuständen (Runde 1 und 2), 42 Zahlenzeilen (Runde 4); X5: 441 Sätze, 23 814 Vergleiche ohne Abweichung; Rechenweg mit $C_\mathrm{GB}$ (X5-02), Ersatzwert keine Messung (X5-03), KT | bestanden |
| M-2 Startzustand ohne Ergebnis | Sperre aller Ausgaben bis zur Startvorhersage | BT „Sperre P0 (de/en)“, G1, G9; Bild `P0_start_*` | bestanden (Auflösungstexte stehen im Skript-Quelltext, siehe Abweichungen) |
| M-3 Vorhersage vor jedem Prüfen | Zustände je Frage, Knopf erst nach Eingabe, Ausgangslage beim Prüfen; Sperre für Frage 1 (Schnitt) und Frage 2 (Messpunkte) | BT „P1“, „P3“, „P5“, „Sperre Frage 1“, „Sperre Frage 2“, „Vertiefung V1 bis V5“; KT X5-01, F3/G1-R4-01; Codex `V3_Antwort_vor_Vorhersage` PASS | bestanden (Korrekturrunde: V3 ohne Vorgriff, X5-01; Zeitangabe der Startauflösung erst nach Frage 1, G1-R4-01 mit Frage Q1 an die TL) |
| M-4 Fachliche Fragen, sinnvolle Bereiche | Fragen Konzept 6; Bereiche `regler.json` | TT, Durchsicht G3 | bestanden |
| M-5 Sofortige Rückmeldung | kein Knopf „Berechnen“, Zeichnen bei jeder Eingabe | BT „Leistung L3“ (Median 3,0 ms), G8 mit Event Timing (höchstens 80 ms bei CPU · 6) | bestanden |
| M-6 Frage, Vorhersage, Diagramm zugleich | Laptop: Frageleiste über dem Diagramm, nach dem Festhalten kurz, Regler direkt darunter; Handy: Diagramm angeheftet, in seiner echten Größe gezeichnet (Schrift 11 bis 12 px), höchstens 45 % der Höhe gemessen mit Kernzahlen und Legende, konstante Höhe; zu wenig Platz (kleine Höhe, große Schrift): nicht angeheftet; Kernleiste der Vertiefung mit gemessenem Fokusabstand | BT „M-6 am Handy“, „Anheften abschaltbar“; KT X5-04, X5-09, X5-10, G1-R4-08, G1-R4-10; Codex-Layout 108 Zustände: 0 verdeckte Fokusmitten, 0 über 45 %; G5 Runde 4 | bestanden in Chromium; echtes Gerät offen |
| M-7 Messblatt nach Versuchsprotokoll | feste Zeilen, Becher 3 zuschaltbar, Deckel, Übernahme ganz oder gar nicht | BT „Messblatt …“, „Übernahme …“, „P6“; Bilder `M_messblatt_*` | bestanden |
| M-8 Pflichtweg mit einem Regler | nur „Zugabe nach“ sichtbar, Rest in der Vertiefung | Bild `P2_*` | bestanden |
| M-9 Kurze Beschriftungen | Regler mit Name, Formelzeichen, Einheit; Hilfe „?“ | Durchsicht, G2, G6 | bestanden |
| M-10 Farbe nie allein, Kontrast | Linienarten, Formen, direkte Beschriftung; Feldränder 3,4:1; Fokus im Kopf weiß | axe (BT), G5 und G6 Kontrastrechnung | bestanden |
| M-11 Direkte Beschriftung kollisionsfrei | Beschriftung mit Kollisionsprüfung gegen Kurven, Punkte, Raumlinie; Ersatzlegende | KT X5-06 (0 von 168 ohne Beschriftung), G5-R4-01 (0 von 128 mit Überdeckung), G6-R3-05; Skript G5 Runde 4: 0 von 648 Zuständen mit Überdeckung; Codex-Layout: Schnitt ohne Text 0 | bestanden (ohne Platz: Name in der Legende unter dem Diagramm, 4 von 648 Zuständen) |
| M-12 Regler ohne Ziehen | `input type="range"` mit `aria-valuetext`, Plus und Minus, Zahlenfeld mit Komma und Punkt | BT „P4 Pfeiltaste“, „Minus-Knopf“, „M-12“ | bestanden |
| M-13 Ziele und Schrift | 44 px Knöpfe und Felder, 24 px Textverweise; Zoom frei | BT „Zielgrößen bei 390 px“; KT X5-05 (200 % Text: kein Regler unter 44 px); Codex-Layout 0 kleine Ziele | bestanden |
| M-14 Umbruch | eine Spalte bis 767 px, kein waagrechtes Scrollen 320 bis 1920 px, 200 % Text | BT „Umbruch“, „200 % Text“; KT X5-05, X5-09; Codex-Layout 108 Zustände ohne Überlauf | bestanden |
| M-15 Bildschirmleser | `figure` mit Namen je Ansicht, Beschreibung, Wertetabelle mit Messwerten, Statusansage, `lang` | axe (BT), G5; echter Bildschirmleser fehlt | bestanden (automatisch und Chromium-Baum); VoiceOver und TalkBack **nicht geprüft** (Gerät fehlt) |
| M-16 Gültigkeit | ungültige Einstellung blendet Diagramm und Zahlen aus, Meldung oben und am Feld | BT „Ungültige Einstellung“ | bestanden |
| M-17 Offline, ohne fremde Server | eine Datei, CSP `default-src 'none'`, keine Anfrage nach außen | BT „Artefakt Datei“, „Artefakt lokaler Server“ (frisches Profil) | bestanden |
| M-18 Aufbau wie das Lernzentrum | Kopf mit „DE ↔ EN“, **drei** Reiter (Lernzentrum K5, Bauauftrag) statt neun, auch am Handy als Reiter | BT „Reiter mit Tastatur“; G6 | bestanden mit Abweichung (drei Reiter, siehe unten) |
| M-19 Sprachen | DE und EN vollständig, „du“ und „you“, keine Gedankenstriche, Dezimalkomma und Dezimalpunkt, Sprache bleibt, `?lang=` | TT 14 von 14, BT „Sprachwechsel …“, KT X5-08 (stehende Meldungen übersetzt), G2 | bestanden |
| M-20 Energie als Säulen | Säulen auf gemeinsamer Nulllinie mit Bezugslinie und Klammer (Prototyp B), Satz mit Milchbeitrag | BT „P2: Energiesäulen“, „Milch für Tasse 2 bei Raumtemperatur“; PROTOTYPEN.md | bestanden |
| M-21 Kurswerte als Link | Format `kurs1` (ZUSTAENDE.md 5), Rückfrage, Prüfung, auch im offenen Tab | BT „Kurslink …“; KT X5-07 (zwei Nachkommastellen wie im Link), X5-11 (fremdes Fragment gemeldet und entfernt), G1-R4-02 und -06 | bestanden |
| M-22 Erklärtexte an Bedingungen | Texte aus Konzept 6 mit Bedingung „gleiches *kA*“; Becher 3 mit eigenem Unterschied | G3 (Runde 1 bis 4); KT G3-R4-02 (Teilflächen nach dem Vorzeichen), G3-R4-03 | bestanden; allgemeine Sätze zum Wärmestrom im Randbereich: Frage Q3 an die TL |

### Sollte (Konzept 4.2)

| ID | Umsetzung | Nachweis | Status |
|:--|:--|:--|:--|
| S-1 Vertiefung V1 bis V5 | Fragen mit Vorhersage, Ausgangslage, Auflösung | BT „Vertiefung V1 bis V5“, KT X5-01, G3, G10; Codex `V1_bis_V5_Ausgangslage_und_Aufloesung_DE` PASS | bestanden (Begründung V1: Frage Q2 an die TL) |
| S-2 Alle Regler, *kA*-Voreinstellungen | Regler, sechs Voreinstellungen nach Tabelle 8.2.1, Anzeige 30 min, *kA*-Quelle | BT „Voreinstellung Keramik mit Deckel“, TK | bestanden |
| S-3 Ausgleichsgerade, Ansicht ln | Ursprungsgerade und freie Gerade, Becher 2 und 3 | BT „Ansicht ln …“ | bestanden |
| S-4 Ansicht Wärmestrom | zwei Teilflächen verschieden schraffiert | BT „Ansicht Wärmestrom …“ | bestanden |
| S-5 Bilanzraum-Skizze | Skizze beider Tassen mit Pfeilen nach dem Wärmestrom vor der Zugabe (Vertiefung) | Durchsicht, Bild `P*_1366` | bestanden |
| S-6 Vergleichslauf | „Lauf zum Vergleich merken“, blass mit Mischsprung und Zahlen | G3, G5 | bestanden |
| S-7 Lesehilfe | ein Satz unter dem Diagramm je Ansicht (Lernzentrum), nicht wegklickbar | Durchsicht | bestanden mit Abweichung (nicht wegklickbar) |
| S-8 Schrift und Farben wie im Lernzentrum | Fira Sans und Fira Math eingebettet, Farben aus `vorbild/gestaltungswerte_lernzentrum.md` | BT „Schriften eingebettet“, G6 | bestanden |
| S-9 Beispielmessung der TL | Tabelle der Vorabmessung liegt nicht vor; kein Knopf | | nicht anwendbar (Daten fehlen) |
| S-10 Englische Texte | aus den deutschen Vorlagen nach Glossar Anhang C | TT, G2 (zwei Runden) | bestanden |

### Kann (Konzept 4.3)

| ID | Status |
|:--|:--|
| K-1 Zeitzeiger, mitlaufende Pfeile | nicht anwendbar (nicht gebaut, Bauauftrag 3.2: nur wenn sauber machbar) |
| K-2 QR-Code offline | nicht anwendbar (nicht gebaut; Link wird angezeigt und kopiert) |
| K-3 Trinkzeit 60 °C | bestanden (BT „Kann K-3“, Werte M10) |
| K-4 Becher kalt | bestanden als Zusatzzeile (BT „Kann K-4“, Werte M9); Kurven dazu nicht gebaut |
| K-5 CSV | bestanden (BT „Kann K-5“, Werte M11, RFC 4180) |
| K-6 Kurven nach der Zugabe, V6 | nicht anwendbar (nicht gebaut) |
| K-7 überlineare Vergleichskurve | nicht anwendbar (nicht gebaut) |
| K-8 Druckansicht | nicht anwendbar (nicht gebaut) |

### Änderungen der Fassung 2 (F2-1 bis F2-17)

| ID | Status und Nachweis |
|:--|:--|
| F2-1 Pflichtweg schlank, Rest Vertiefung | bestanden (M-8, Bild `P2_*`) |
| F2-2 „du“ in beiden Sprachen | bestanden (TT, Durchsicht G2, G9) |
| F2-3 DE und EN mit Umschalter | bestanden (M-19) |
| F2-4 Sichtbarkeit bis zum Sitzungstag | nicht anwendbar (regelt die Veröffentlichung, nicht der Bau) |
| F2-5 Versuch bis 60 min, Messblatt | bestanden (M-7) |
| F2-6 Energie mit vollständiger Bilanz, Wärmestrom nur Vertiefung | bestanden (M-20, S-4) |
| F2-7 Schnittpunkt und Abklingen nur bei gleichem *kA* | bestanden (M-22) |
| F2-8 Ausgleichsgerade ohne „±“ | bestanden (S-3) |
| F2-9 Frage Versuch offen | bestanden (Wortlaut Konzept 6.1) |
| F2-10 Vorhersagesperre für alle Ausgaben | bestanden (M-2, M-3; V3 nach X5-01; Startauflösung nach G1-R4-01) |
| F2-11 Handy | bestanden in Chromium (M-6, M-13, M-14, auch mit großer Schrift); VoiceOver und TalkBack nicht geprüft |
| F2-12 Literatur | nicht anwendbar (Konzept) |
| F2-13 Annahmen, Rechnen ohne Speicher | bestanden (BT „Speicher gesperrt“; Texte A.6) |
| F2-14 Neue Regler mit Voreinstellungen | bestanden (S-2) |
| F2-15 *kA* festhalten gegen *kA* aus der Messung | bestanden (TK, BT „Vertiefung V1 bis V5“) |
| F2-16 Kann-Ideen geprüft | bestanden (K-3 bis K-5 gebaut, Rest begründet) |
| F2-17 Entfallenes | bestanden (nicht gebaut) |

### Entscheidungen K1 bis K11 (Annahme der X4-Befunde) und E1 bis E8

| ID | Status und Nachweis |
|:--|:--|
| K1 Energieansicht | bestanden (M-20, S-4) |
| K2 Bilanz mit Milchbeitrag | bestanden (BT „Milch für Tasse 2 bei Raumtemperatur“, 1,95 K) |
| K3 Bedingung gleiches *kA* | bestanden (M-22) |
| K4 Ausgleichsgerade ohne Standardfehler | bestanden (S-3) |
| K5 Messblatt und Link mit Bedingungen | bestanden (M-7, M-21) |
| K6 Frage Versuch offen | bestanden |
| K7 Pflichtweg | bestanden; Zeit nur geschätzt (G1 Runde 4: etwa 14 min, Spanne 12,5 bis 16,5 min für ein Paar am Handy), Stoppuhr mit Studierenden offen |
| K8 Handy | wie F2-11; Geräte offen |
| K9 Literatur | nicht anwendbar (Konzept) |
| K10 Sperre aller Ausgaben | bestanden (M-2, M-3) |
| K11 Annahmen, Speicher bei `file:` | bestanden (BT „Speicher gesperrt“) |
| E1 Eigene Website | bestanden (eigene Seite im Aussehen des Lernzentrums) |
| E2 Startkarte; Sichtbarkeit bis zum Sitzungstag | Startkarte bestanden; Sichtbarkeit nicht anwendbar (Veröffentlichung) |
| E3 Deutsch und Englisch | bestanden |
| E4 Erweiterungen | bestanden (S-2 bis S-6, K-3 bis K-5) |
| E5 „du“ | bestanden |
| E6 Reiter „Auflösungen“ | erledigt durch Entscheidung F1 der TL (drei Reiter, erster heißt „Versuche“) |
| E7 Fragen | bestanden (Wortlaut Konzept 6) |
| E8 Messwerte bis 60 min, Link | bestanden; Vorabmessung der TL fehlt (S-9) |

## Abweichungen vom Konzept (mit Grund)

1. **Drei Reiter statt neun** (M-18) und erster Reiter „Versuche“ statt „Auflösungen“ (E6): Bauauftrag und Lernzentrum-Entscheidung K5 gehen dem Konzept vor; von der TL bestätigt (F1).
2. **Auflösungstexte im Skript-Quelltext:** Eine Offline-Datei muss sie enthalten. Die Sperre gilt für Darstellung, Barrierefreiheitsbaum und Ansagen (ZUSTAENDE.md Regel 1); die Prüfschnittstelle gibt vor der Freigabe kein Ergebnis.
3. **Sperren über das Konzept hinaus:** Schnittzeit und Schnittkreis erst nach der Vorhersage zu Frage 1, Messpunkte erst nach der Vorhersage zu Frage 2 (Befunde der Rollen; F2-10).
4. **Frageleiste springt nach dem Start zu Frage 1** (ZUSTAENDE P2) mit einem Rückblick (eigene Vorhersage, Auftrag, Auflösung zum Start) über Frage 1.
5. **Säulentitel** „Energie bis zur Zugabe: an den Raum abgegebene Wärme“ statt „Energie bis zur Zugabe“ (Klarstellung nach G1-08 und G4-04; Wort des Konzepts bleibt). Änderung an einem Konzeptwort, von der TL rücknehmbar.
6. **Lesehilfe** ein Satz je Ansicht wie im Lernzentrum, nicht wegklickbar (S-7).
7. **Querformat am Handy:** Diagramm und Regler untereinander mit begrenzter Diagrammhöhe statt nebeneinander (Konzept 5.2); beide zugleich sichtbar.
8. **Stand und Version** im Fuß statt im Kopf (Konzept 5.1 Nr. 1).
9. **Messblatt schon vor der Freigabe** eingebbar (ohne Übernahme), damit die TL vor der Sitzung eintragen kann (G7-08).
10. **„ohne Vorhersage aufdecken“** wie im Lernzentrum, mit Rückfrage.
11. **Kann-Punkte** K-1, K-2, K-6, K-7, K-8 nicht gebaut; K-4 nur als Zusatzzeile.
12. **Zwei Rückmeldezeilen:** „Auswahl passt“ und Vergleich „Eure Zahl … Modell …“ (Modell der Standardlage).

## Übernahmen aus dem Lernzentrum v8 (Tag `hauptadresse-v8-2026-11-05`)

| Was | Datei und Stelle im Lernzentrum | Kaffee-Seite |
|:--|:--|:--|
| Farben, Schriftgrößen, Abstände | `dist/design.css`, `audit.css`, `runde10.css`, `runde11.css` (Werte in `simulation/vorbild/gestaltungswerte_lernzentrum.md`) | `src/stil.css`, Variablen am Anfang |
| Schrift Fira Sans und Fira Math (OFL) | `dist/fonts/` | Teilmengen in `src/schriften/`, erzeugt mit `schriften_teilen.py` |
| Formelsatz: eigener Umsetzer nach MathML, beschreibende Indizes aufrecht, Formeln fett (K1), Brüche im Satz klein (K3), eckige Klammern nur an Reglern, Achsen, Tabellenköpfen (K2) | `dist/math.js`, `typeset.css`, Leitfaden 2 und 3 | `tex2mathml.py`, `stil.css` |
| Kopf mit Sprachknopf „DE ↔ EN“, Sprache gespeichert | `audit.css` 199, `design.css` 86, `i18n.js`, `sprachen.js` | `vorlage.html`, `oberflaeche.js` |
| Drei Reiter Versuche, Modell, So rechnet der Code (APG Tabs, auch am Handy) | R12-09, `dist/topic.js` | Reiterleiste |
| Versuchskarten mit Vermutung, „Auflösung zeigen“, „ohne Vermutung aufdecken“ | `dist/topic.js` | Karten im Reiter Versuche, Frageleiste |
| Regler: Beschriftung mit Formelzeichen und Einheit, Hilfe „?“, Zahlenfeld | `pilot.css`, `parameter-help.js`, `numeric-input.js` | `reglerHtml` (dazu Plus und Minus nach M-12) |
| Rechenwerte-Kasten zweispaltig | `runde10.css` | `#rechenwerte` |
| Ein dunkler Hauptknopf je Bereich | Leitfaden, `design.css` | `.knopf-haupt` |
| Bekannte Fehler F01 bis F34 vermieden | `simulation/vorbild/bekannte_fehler_lernzentrum.md` | VORBILD_LERNZENTRUM.md, Abschnitt 5 |

## Testbefehle und Ergebnisse

Vom Repository aus:

```
python3 simulation/site/bauen.py --pruefen
python3 simulation/tests/test_kern.py
python3 simulation/tests/test_kern.py --html simulation/site/index.html
python3 simulation/tests/test_texte.py
node simulation/tests/browsertest_bau.js
node simulation/tests/browsertest_korrektur.js
node simulation/tests/bilder_bau.js
```

Korrekturrunde: derselbe Test auf einem anderen Stand mit `KAFFEE_ORDNER=<ordner mit index.html> node simulation/tests/browsertest_korrektur.js`. Skripte von Codex (Python mit Playwright, Server auf Port 8765 und 8766): Anleitung in `simulation/x5_skripte/README.md`; die Kopie in `simulation/x5_regression/` schreibt ihre Ergebnisse dort hin, Auswertung mit `python3 simulation/x5_regression/auswertung.py`.

Voraussetzung für die Browsertests: `npm ci` in `simulation/tests/` (axe-core 4.14.0) und Playwright mit Chromium.

Ergebnisse auf dem übergebenen Stand (06.11.2026, Cloud-Container, Chromium 153 über Playwright 1.63.0):

| Befehl | Ergebnis | Ergebnisdatei |
|:--|:--|:--|
| `bauen.py --pruefen` | „gleich“ (Bau reproduzierbar) | |
| `test_kern.py` | 134 von 134 bestanden (Rechenkern der Quellen gegen `kaffee_modell.py` und `kaffee_erweitert.py`, 10 000 Zufallssätze) | `test_kern_ergebnis.txt` |
| `test_kern.py --html` | 135 von 135 bestanden (dasselbe aus der gebauten Seite, dazu Identität des Blocks MODELL) | `test_kern_html_ergebnis.txt` |
| `test_texte.py` | 14 von 14 bestanden (Schlüssel DE und EN gleich, keine Gedankenstriche, Dezimalzeichen, Zahlen aus `zahlen.py`, „du“) | `test_texte_ergebnis.txt` |
| `browsertest_bau.js` | 95 von 95 bestanden (Artefakt, Sperren, Pflichtweg, Vertiefung, Messblatt, Kurslink, Sprache, Speicher, Umbruch 320 bis 1920 px, 200 % Text, axe-core, Kann-Punkte) | `browsertest_bau_ergebnis.txt` |
| Leistung (im Browsertest) | L2 bedienbar nach 92 ms; L3 je Reglerschritt Median 3,0 ms, 95 % 3,4 ms, höchstens 3,8 ms; L4 Bedienfolge 30 s mit 1411 Schritten ohne Fehler, Speicherzuwachs 1,33 MB | dieselbe |
| `browsertest_korrektur.js` | 43 von 43 (je behobenem Befund aus X5, Runde 3 und Runde 4 ein Test); auf dem Stand vor der Korrektur 0 von 29 (die 29 Tests zu X5 und Runde 3) | `browsertest_korrektur_ergebnis.txt`, `browsertest_korrektur_alt_ergebnis.txt` |
| Skripte von Codex (Kopie) | Zahlen: 441 Sätze, 23 814 Vergleiche, ohne Abweichung; Layout 108 Zustände ohne Überlauf, ohne verdeckten Fokus, Schnitt ohne Text 0; Bedienlauf 19 von 20 Prüfschritten bestanden, 1 Abbruch | `simulation/x5_regression/` |
| `bilder_bau.js` | 54 Bilder der Abdeckungsmatrix (ZUSTAENDE.md 7) | `simulation/bildschirmfotos/bau/LISTE.txt` |

Die Leistungswerte stammen aus dem Cloud-Container, nicht von einem Handy. Die Rollen G5, G6, G8, G10 haben mit eigenen Skripten (in ihren Arbeitsordnern, nicht eingecheckt) weitere Zustände geprüft; ihre Messwerte stehen in den Gutachten.

## Bilanz der Rollenprüfungen

Drei Runden nach Bauauftrag 4.3; getrennte Rollenprüfungen desselben Modells. Gutachten in `simulation/gutachten/`: Runde 1 G1 bis G8 (`G<Nr>_<Rolle>.md`; G2, G3, G5, G6, G8 nach der Pause am 06.11.2026 auf demselben Stand zu Ende geführt), Runde 2 alle acht Rollen (`*_R2.md`) und die neue Studentin G9, Runde 3 G2, G4, G5, G6, G7, G8 (`*_R3.md`; G1 und G3 ohne offene Punkte) und die neue Studentin G10. Jede Entscheidung mit Beleg in `ZUSAMMENFUEHRUNG.md` (erzeugt von `zusammenfuehrung_bauen.py`).

| Runde | geprüfter Stand (SHA-256) | Befunde | blocker | high | medium | low | übernommen | abgelehnt | offen |
|:--|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| 1 | `f519052c…6707` | 189 | 5 | 20 | 70 | 94 | 154 | 13 | 22 |
| 2 | `ea6d3ad2…9c31` | 60 | 1 | 9 | 13 | 37 | 52 | 3 | 5 |
| 3 | `1d90ce2f…292b` (an X5 übergeben) | 27 | 0 | 2 | 9 | 16 | 1 (in der Korrekturrunde: 24 behoben) | 0 | 26 (danach 3: G10-02 Zeit, zwei durch F entschieden) |
| X5 (Codex) | `1d90ce2f…292b` | 11 | 2 | 6 | 3 | 0 | 11 | 0 | 0 |
| 4 (nach der Korrekturrunde) | `10b428ef…e878` | 31 | 4 | 1 | 10 | 16 | 25 | 0 | 6 (Q1 bis Q7, eine Bedienfunktion) |

- **Zahlen:** Keine Rolle fand in drei Runden eine falsche Modellzahl. G3 rechnete in Runde 1 und 2 je 30 Zustände und alle Auflösungen unabhängig nach; G9 und G10 rechneten Standardwerte, Frage 1 und Frage 2 mit eigenen Formeln nach.
- **blocker** (alle behoben und in der Folgerunde bestätigt): Messpunkte vor der Vorhersage zu Frage 2; Achsenbeschriftung bei Schrittweite 2,5; CSV mit Modellwerten vor der Freigabe (Runde 2).
- **Sperren:** In Runde 3 hielten alle Sperren im Pflichtweg (G8 suchte in DOM, Titel, Ansagen, CSV, Prüfschnittstelle und Barrierebaum); offen ist die Ausgangslage von V3 (G10-01).
- **Offen** sind nach der Korrekturrunde nur Wortlaute für die TL (Q1 bis Q7) und eine neue Bedienfunktion (G1-R4-13); siehe Status.

## Offene Nachweise in der echten Welt

| Nachweis | Wer | Wo |
|:--|:--|:--|
| iPhone mit Safari (Hoch- und Querformat, Regler mit dem Finger, Dezimaleingabe, Bildschirmtastatur, Zoom, Sprachwechsel, Kurslink, Download, Offline-Datei) | TL | `simulation/ABNAHME_IPHONE.md` |
| Android, Firefox, Safari am Laptop | TL oder Codex | nicht geprüft (nur Chromium) |
| Studierende: Zeit des Pflichtwegs mit Stoppuhr (Ziel etwa 10 min; Schätzungen der Rollen 11 bis 16 min mit Kurswerten) | TL | Probelauf mit zwei Studierenden (Konzept 3) |
| Hörsaal: Lesbarkeit am Beamer, Netz, QR-Code | TL | `simulation/EINSATZ_TUTORIUM.md` Abschnitt 5 |
| Bildschirmleser (VoiceOver, TalkBack, NVDA) | TL oder Prüfperson | nicht verfügbar in der Umgebung |
| Windows-Kontrastmodus | Prüfperson | nur Chromium-Emulation |

## Korrekturrunde nach X5 (06.11.2026)

Auftrag der TL vom 06.11.2026 nach der Abnahme X5 (Codex: „nicht abnahmefähig“, 11 Befunde, 2 blocker, 6 high, 3 medium; `simulation/X5_CODEX_ABNAHME.md`). Der Zweig von Codex (`codex/x5-abnahme-da7deb1`, 9a9208b) ist eingemergt (nur Bericht, Skripte, Bilder).

1. **Entscheidungen F1 bis F14** im Abschnitt „Fragen an die TL“ eingetragen; Wortlaute in `simulation/KONZEPT.md` 12.1, Ablauf in `simulation/ZUSTAENDE.md`.
2. **X5 nachgeprüft:** alle elf Befunde mit den Skripten von Codex und eigenen Messungen bestätigt; Antwort und Nachweis je Befund in `simulation/X5_ANTWORT.md`.
3. **Umgesetzt** in der Reihenfolge der TL: X5-01 und X5-02, X5-03 bis X5-08, F1 bis F12, die offenen Befunde der Runde 3, X5-09 bis X5-11.
4. **Regression:** Jeder behobene Befund hat einen Test in `simulation/tests/browsertest_korrektur.js`. Ergebnisse: auf dem Stand vor der Korrektur (`1d90ce2f…292b`) 0 von 29 (die 29 Tests zu X5 und Runde 3), auf dem von Runde 4 geprüften Stand (`10b428ef…e878`) die 14 Tests zu Befunden der Runde 4 alle rot, auf dem neuen Stand 43 von 43. Die Skripte von Codex laufen als Kopie in `simulation/x5_regression/` (Ergebnisse dort): Zahlenprüfung ohne Abweichung, Layout und Ergänzung ohne Befund, Bedienlauf 19 von 20 Prüfschritten bestanden, 1 Abbruch (der eine Abbruch ist der jetzt abgelehnte Wechsel der *kA*-Quelle bei *kA* = 1 W/K, gewollt nach X5-03).
5. **Runde 4** mit frischen Rollen nur für die geänderten Stellen: G1 Studentin am Handy (14 Befunde: 1 blocker, 5 medium, 8 low), G3 Fach (11: 3 blocker, 1 medium, 7 low), G5 Barrierefreiheit (6: 1 high, 4 medium, 1 low). Übernommen und behoben 25, davon alle 4 blocker und der high; offen 6 (Wortlaute für die TL Q1 bis Q7, eine neue Bedienfunktion). Bestätigt behoben: X5-02 bis X5-05, X5-08 bis X5-11, G5-R3-01 bis -03 (G3, G5). Keine falsche Zahl (G3: 42 Zahlenzeilen DE und EN). Einzelheiten: `simulation/gutachten/ZUSAMMENFUEHRUNG.md`, Abschnitt „Korrekturrunde nach X5 und Runde 4“.
6. **Begleitmaterial** nachgezogen: Einsatzblatt Abschnitt 9 aus den Quelltexten neu erzeugt, iPhone-Liste um B2a ergänzt; 54 Abdeckungsbilder neu.

## Status

**Stand nach der Korrekturrunde: abnahmebereit bis auf die Fragen an die TL und die Nachweise in der echten Welt.** Streng nach Bauauftrag 6 bleibt es eine **unvollständige Übergabe**, solange ein medium offen ist: Die Begründung in der Auflösung V1 ist nach G1 und G3 irreführend; sie ist Wortlaut der Entscheidung F8 und wartet auf Q2. Alle technischen blocker, high und medium aus X5, Runde 3 und Runde 4 sind behoben und mit Tests belegt. Nicht erbracht sind weiterhin die Nachweise am echten Gerät (M-15 mit Bildschirmleser, iPhone und Safari, Hörsaal, Zeit mit Studierenden).

Übergebener Stand: `simulation/site/index.html`, bytegleich `simulation/site/Kaffee_Simulation.html`, SHA-256 `e44b4961145f8e34db8b1f4e11973862e362797e61a89df899ab4f1959393ce3`, 429 897 Bytes, Commit 188ba12. `python3 simulation/site/bauen.py --pruefen` gibt „gleich“ aus. Tests: `test_kern.py` 134 von 134, `--html` 135 von 135, `test_texte.py` 14 von 14, `browsertest_bau.js` 95 von 95, `browsertest_korrektur.js` 43 von 43.

**Offen:**

| Was | Art | Nächster Schritt |
|:--|:--|:--|
| Q1 bis Q7 (Wortlaute aus Runde 4) | Entscheidung der TL | unten; danach umsetzen und X5 nachprüfen lassen |
| G1-R4-13: Wechsel zwischen V1 bis V5 umständlich (Auswahl V1 bis V5 in der Frageleiste fehlt) | low, neue Bedienfunktion | Empfehlung für eine spätere Runde |
| F13 Vorabmessung der TL (Beispielmessung, S-9) | Daten fehlen | Messreihe der TL |
| iPhone mit Safari, Android, Firefox, Bildschirmleser, Hörsaal, Zeit mit Studierenden | echte Welt | `simulation/ABNAHME_IPHONE.md`, Probelauf |
| Nachprüfung durch Codex (nur betroffene Punkte) | unabhängige Prüfung | `simulation/X5_AUFTRAG.md`, Abschnitt 9 |

## Fragen an die TL (mit Empfehlung)

Die Belege stehen in `simulation/gutachten/ZUSAMMENFUEHRUNG.md` unter der jeweiligen ID. Alle Punkte betreffen Inhalte oder Entscheidungen, die der Bau nicht eigenständig ändern darf. Die TL hat am 06.11.2026 im Chat entschieden: „F1 bis F12 wie von dir empfohlen. F13 folgt, sobald ich meine Vorabmessung habe. F14 ja“.

| Nr. | Frage | Befunde | Empfehlung | Entscheidung der TL (06.11.2026) |
|:--|:--|:--|:--|:--|
| F1 | Drei Reiter (Bauauftrag, Lernzentrum K5) statt neun (M-18), erster Reiter „Versuche“ statt „Auflösungen“ (E6)? | G3-13, G2-07, G9-07 | Drei Reiter und „Versuche“ beibehalten (wie das Lernzentrum); E6 damit als erledigt werten | wie empfohlen |
| F2 | Blatt vom 31.10. (Versuch bis 40 min, *kA* ohne Becher) und Seite (E8: bis 60 min, Übernahme mit Becher) weichen ab. Welcher Ablauf gilt in der Sitzung? | G1-09, G7-12, G9-06 | Seite und Messblatt nach E8 (60 min); das Einsatzblatt sagt es schon an; Blatt bei der nächsten Überarbeitung der Kaffee-Aufgabe angleichen | wie empfohlen |
| F3 | Auflösung zum Start: „Tasse 2 war bis zur Zugabe heißer“ stimmt nur bis 55,7 min | G3-02 | „Tasse 2 war fast bis zur Zugabe (bis etwa 56 min) heißer als Tasse 1 und hat deshalb mehr Wärme abgegeben“ (auch in KONZEPT.md 6.1) | wie empfohlen |
| F4 | Wortlaut Frage 1 (Vorhersage „wann am größten“ setzt die Form der Kurve voraus) | G4-03, G9-08 | Vorhersage erst offen: „Wie ändert sich der Unterschied, wenn die Milch später in Tasse 2 kommt? Bei welcher Zugabe ist er am größten?“; „Warum wird er wieder kleiner?“ erst nach dem Festhalten | wie empfohlen |
| F5 | Wortlaut Frage 2: „übernehmt die Einstellungen“ und Reihenfolge Laden, Vorhersage | G1-18, G7-R2-08, G9-10, G10-05 | Satz je Zustand: mit geladenen Kurswerten nur „Prüft dann: Beschreibt, wo die Punkte liegen …“, dazu „Die Einstellungen werden beim Prüfen aus den Messwerten übernommen.“ | wie empfohlen |
| F6 | Fehlvorstellung „Energie bleibt erhalten“ ausdrücklich ansprechen | G4-04 | Ja: Satz des Mitbewohners in die Startkarte und ein Satz zur Erhaltung (Kaffee, Milch und Raum zusammen) in die Auflösung zum Start; Säulentitel des Baus (Abweichung 5) bestätigen | wie empfohlen |
| F7 | Startfrage nach der Rechnung im Tutorium schon beantwortet | G4-05 | Für die Sitzung behalten, die TL fragt mündlich nach dem Grund; eine zweite Startfrage erst nach dem Probelauf erwägen | wie empfohlen |
| F8 | Auflösung V1 ohne Begründung; Abschlusssatz „Geschafft“ zu früh und ohne Zusammenfassung | G4-15, G4-16 | beides ja, mit den Sätzen aus G4-15 und G4-16 (Zahlen vorher von der Fachrolle prüfen lassen) | wie empfohlen |
| F9 | Fragenzuschnitt V1, V3, V5 (zwei Teilfragen, eine Eingabe); V4 ohne Werkzeug; V5 Auflösung | G4-17, G10-09, G4-24, G3-11 | zweiten Teil als „notiert für euch“ kennzeichnen; V4 nennt „*kA* von Tasse 1 relativ“; V5 „Nach den Richtwerten (*) sind Glas und Pappe etwa wie Keramik“ | wie empfohlen |
| F10 | Auflösung Frage 2 bleibt allgemein | G10-10 | so lassen (K6, offen formuliert); optional eine Zeile aus den Daten nach der Vorhersage | wie empfohlen |
| F11 | Texte Anhang A: Satz A.5 im Reiter „Modell“ schon vor dem Start lesbar; A.2 und A.8 nennen den Schnitt vor Frage 1 | G1-16, G1-07 | Abschnitte „Physikalisches Problem“ und die Sätze zum Schnitt erst nach der Startvorhersage bzw. Frage 1 zeigen | wie empfohlen |
| F12 | Kleine Textpunkte: „Wärmeabgabe *kA*“, *C*_G mit Becher, Zahlen der Standardlage in A.2, Schnitt bei ungleichem *kA*, Annahmentext Keramik mit Deckel, Verweis auf die Ansicht Wärmestrom, Benennung „Frage 1“ gegen Blatt | G3-04, G3-05, G3-06, G3-07, G3-10, G4-20, G4-22 | G3-05, G3-06, G3-07, G3-10 nach Vorschlag der Rollen; „Wärmeabgabe *kA*“ (M-9) und „Frage 1, Frage 2“ beibehalten; G4-20 als Satz in der Auflösung zu Frage 1 | wie empfohlen |
| F13 | Vorabmessung der TL als Beispielmessung (S-9) | | Messreihe schicken, sobald vorhanden; dann Knopf „Beispielmessung laden“ | folgt, sobald die Vorabmessung vorliegt |
| F14 | Weiterer Weg nach Runde 3 | Status oben | X5 jetzt auf diesem Stand, danach eine gemeinsame Korrekturrunde | ja; Codex hat geprüft (X5, Zweig `codex/x5-abnahme-da7deb1`, Commit 9a9208b), danach gemeinsame Korrekturrunde |

### Fragen aus Runde 4 (06.11.2026)

Belege in `simulation/gutachten/G1_Studentin_R4.md`, `G3_Fachgutachter_R4.md`, `G5_Barrierefreiheit_R4.md`. Antwort zum Beispiel „Q1 A, Q2 ja, …“.

| Nr. | Frage | Befunde | Empfehlung | Entscheidung der TL |
|:--|:--|:--|:--|:--|
| Q1 | Startauflösung „(bis etwa 56 min)“ verrät die Antwort auf Frage 1. Übergangsweise erscheint die Klammer erst nach der Vorhersage zu Frage 1 (A). Alternative B: Klammer ganz streichen. | G1-R4-01, G3-R4-01 (blocker) | **A** | offen |
| Q2 | Begründung V1 ersetzen durch: „Bei 47,0 °C gibt Tasse 1, in der die warme Milch von Anfang an ist, bis zur Zugabe genauso viel Wärme ab wie der schwarze Kaffee in Tasse 2 (*Q*₁ = *Q*₂); die Milch selbst bringt in beide Tassen dieselbe Energie. Je später die Zugabe, desto mehr von der Wärme der warmen Milch hat Tasse 1 bis dahin an den Raum abgegeben, während Tasse 2 sie erst bei der Zugabe bekommt; deshalb reicht dann kühlere Milch.“ (EN von G3) | G1-R4-04, G3-R4-04 (medium) | **ja** | offen |
| Q3 | Allgemeine Sätze zum Wärmestrom für den Randbereich mit umgekehrter Reihenfolge: Rechenweg „Er wächst, solange Tasse 2 mehr Wärme abgibt, und sinkt, solange sie weniger abgibt.“; Lesehilfe „vor und nach dem Schnitt der Wärmeströme haben die Teilflächen verschiedene Vorzeichen: positiv, solange Tasse 2 mehr abgibt; …“ (Beschriftungen und Lesehinweis unter dem Diagramm richten sich schon nach dem Vorzeichen) | G3-R4-02 | **ja** | offen |
| Q4 | Kernsatz „… deshalb kalte Milch sofort.“ (bei warmer Milch gilt das Gegenteil, Teil f) | G3-R4-05 | **ja** | offen |
| Q5 | „Notiert für euch:“ ersetzen durch „Notiert euch dazu:“ | G1-R4-11 | **ja** | offen |
| Q6 | Nach dem Festhalten von V1: „Prüft mit dem Regler Milchtemperatur (Abschnitt Milch).“; nach „ohne Vorhersage aufdecken“ statt „Stimmt eure Vorhersage?“: „Erklärt zu zweit, was ihr seht.“ | G1-R4-14, G1-R4-12 | **ja** | offen |
| Q7 | „Ferreira 2025a“ ohne Literaturverzeichnis ersetzen durch „Ferreira 2025“ wie in der Lösung | G3-R4-11 | **ja** | offen |
