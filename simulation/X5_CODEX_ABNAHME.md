# X5: Abnahme des Baus der Kaffee-Simulation

Geprüft am 06.11.2026, Rolle X5, unabhängig vom Bau durch Claude.
Beide Prüfteile A und B sind abgeschlossen. Es wurden ausschließlich dieser
Bericht und eigene Prüfskripte samt Ergebnissen und Bildern ergänzt.

## Urteil

**Nicht abnahmefähig.** Der Rechenkern und die Ergebniszahlen der Auflösungen
bestehen die unabhängige Nachrechnung. Die Vorhersagesperre von V3 wird jedoch
im normalen Ablauf verletzt. Außerdem fehlt im erklärenden Rechenweg die
Becherwärmekapazität in zwei Gleichungen. Weitere Befunde betreffen die
Umstellung der kA-Quelle, vergrößerte Schrift, Beschriftungen, Kurslinks und
eine nicht übersetzte Fehlermeldung. Die Befunde stehen mit Reproduktion und
Korrekturvorschlag weiter unten. An der Simulation wurde nichts korrigiert.

## Geprüfter Stand und Umgebung

| Punkt | Nachweis |
|:--|:--|
| Ausgangszweig | `claude/simulation-tool-kaffee-4kcacl`, vom Nutzer vorgegeben und von `origin` geholt |
| Geprüfter Commit, vor eigenen Änderungen mit `git rev-parse HEAD` festgestellt | `da7deb1bd897a69424964d0b20c93222697d4381` |
| Eigener Zweig | `codex/x5-abnahme-da7deb1` |
| Artefakte | `simulation/site/index.html` und `simulation/site/Kaffee_Simulation.html`, bytegleich, je 399 063 Bytes |
| SHA-256 beider Artefakte | `1d90ce2f84349754592a5dd572a760a5d212cd3383bcafbeb1cceaf06e07292b` |
| Reproduzierbarkeit | `PYTHONPATH=/tmp/x5-python python3 simulation/site/bauen.py --pruefen`: **gleich** |
| Referenzmodell, SHA-256 | `eb7efc1d5322b629e1e11494f7c70fa8d8d54ec60e555874326fa491a31757a1`, stimmt mit HERKUNFT.md überein |
| MODELL-Block, SHA-256 | `b32e3f9db9f82b09bfc0e300388ffbef72f875cec65540da668d765389f97d24`, unverändert |
| Laufzeit | Linux in der Codex-Cloud, Python 3.12.14, Node 24.19.0, Playwright 1.62.0, Chromium 154.0.8037.57 |
| Bauabhängigkeiten | fontTools 4.61.1, Brotli 1.2.1; Brotli war zunächst nicht installiert und wurde nur in `/tmp/x5-python` ergänzt |
| Barrierefreiheitswerkzeug | axe-core 4.11.0, getrennt unter `/tmp/x5-tools`, keine Abhängigkeit der Seite |
| Vorbild | Lernzentrum, Tag `hauptadresse-v8-2026-11-05`, unabhängig nach `/tmp` geholt, Commit `c2af968fab5c883a52d8323771b7eebb5a969373`, nur gelesen |

Maßgeblich waren X5_AUFTRAG, BAU_AUFTRAG, E1 bis E8 und K1 bis K11,
KONZEPT Fassung 2, ZUSTAENDE und der ursprüngliche Simulationsauftrag.
Die drei Reiter und der Name „Versuche“ folgen dem höherrangigen Bauauftrag.
Die ältere Neun-Reiter-Vorgabe und E6 wurden deshalb nicht als Fehler gewertet.
Die Stoffdaten wurden zusätzlich mit dem fertigen Aufgaben-PDF abgeglichen.

Nicht vollständig prüfbar: echtes iPhone/Safari, WebKit, VoiceOver und TalkBack,
echte Bildschirmtastatur, wirklicher Browserzoom und Lesbarkeit im Hörsaal.
Die Browserrichtlinie dieser Umgebung verweigert `file:` mit
`ERR_BLOCKED_BY_ADMINISTRATOR`. Geprüft wurden deshalb die lokale HTTP-Datei
und, als zusätzliche Offline-Gegenprobe, die exakten HTML-Bytes über eine
Playwright-Route in einem frischen Kontext mit `offline=True`. Das ersetzt den
Gerätenachweis aus der Dateien-App nicht. 320 CSS-Pixel wurden direkt geprüft,
200 Prozent Text durch 32 px Grundschrift; das ist kein ausgeführter nativer
400-Prozent-Browserzoom. Ein Durchgang mit zwei Studierenden fehlt weiterhin.

## A: Zahlen und Fachliches

### Eigenständige Rechnung und Umfang

`x5_skripte/pruefung_a.py` importiert weder `kaffee_modell.py` noch
`kaffee_erweitert.py`, `zahlen.py` oder JavaScript-Rechenfunktionen als
Erwartungsquelle. Die eigene Rechnung verwendet die Mischbilanz sowie
`dE/dt = -kA (theta - theta_u)` bei `E = C (theta - theta_u)`. Die Milchzugabe
ist ein eigener Bilanzschritt. Mit Becher werden seine 255 J/K zur jeweiligen
Wärmekapazität addiert. kA aus der Messung und festgehaltenes kA werden getrennt
berechnet. Das Maximum über den Zugabezeitpunkt wird numerisch gesucht, die
Milchtemperatur für gleiche Endtemperaturen durch Nullstellensuche.

Verglichen wurde mit dem JavaScript im unveränderten fertigen Artefakt:
**441 Parametersätze, 23 814 Einzelvergleiche, keine Abweichung außerhalb der
vorab festgelegten Toleranzen** (absolut 1e-8, relativ 1e-9).
Größte absolute Differenz: 1,15e-9, bei einer Zeitgröße.
400 Sätze sind unabhängig gleichverteilt in den Reglerbereichen, Seed 20261106;
die anderen 41 enthalten Standard-, Grenz- und Risikofälle. Bechermassen 100
und 600 g wurden mit eingeschaltetem Becher geprüft, Messwerte 30 und 90 °C
mit jeweils gültigen übrigen Temperaturen. Einzelheiten stehen in
`x5_skripte/ergebnis_a.json`.

Zehn zusätzliche Maximumprüfungen bei kA von 0,05 bis 1,00 W/K, jeweils mit
und ohne Becher, bestätigen die Unabhängigkeit des Höchstwerts von kA.
Bei kA = 0,05 W/K liegt das Maximum außerhalb der Reglergrenze von 180 min.
Das ist eine Grenze des Ausschnitts, kein Widerspruch zum analytischen Maximum.

`pruefung_ergaenzung.py` vergleicht außerdem **3 872 tatsächlich gezeichnete
SVG-Punkte** in acht Fällen mit der eigenen Bilanzrechnung. Die größte
Abweichung beträgt 0,102 SVG-Einheiten bei vorher festgelegten 0,2 als Grenze,
einschließlich der gerundeten Achsen und Punktkoordinaten. Ein richtiger Kern
allein wurde somit nicht als Beweis für richtig gezeichnete Kurven genommen.

### Nachgerechnete Zahlen

„Seite“ bezeichnet hier den Wert aus dem gebauten JavaScript, bei den
Standardwerten zusätzlich die sichtbaren Rechenwerte und Energiesäulen. In der
Vertiefung wurden die geänderten Eingaben gegen die sichtbare Ausgabe geprüft.
Die ausführlichen ungerundeten Werte und Parameter stehen in den JSON-Dateien.

| Größe oder Fall | Eigene Rechnung | Seite | Urteil |
|:--|--:|--:|:--|
| Standard, Temperatur Tasse 1 | 34,046483 °C | 34,05 °C | stimmt |
| Standard, Temperatur Tasse 2 nach Milch | 30,193282 °C | 30,19 °C | stimmt |
| Standard, Unterschied | 3,853201 K | 3,85 K | stimmt |
| Standard, Q1 / Q2 | 34,880847 / 38,571235 kJ | 34,88 / 38,57 kJ | stimmt |
| Standard, Mischtemperatur | 70,466209 °C | 70,47 °C | stimmt |
| Standard, kA | 0,340247765 W/K | 0,3402 W/K | stimmt |
| Schnitt und Maximum ohne Becher | 55,744669 min; 3,861838 K | 55,7 min; 3,86 K | stimmt |
| Maximum mit Becher, gleicher kA beider Tassen | 3,089845 K | 3,089845 K im Kern | stimmt |
| Deckel, Maximum | 99,54405 min; 3,861838 K | etwa 100 min; 3,86 K | stimmt |
| Deckel, feste Zugabe nach 60 min | 44,658017 / 41,148383 °C; 3,509635 K | 44,66 / 41,15 °C; 3,51 K | stimmt, andere Größe als Maximum |
| Becher und kA aus Messung | 0,444031471 W/K; 34,043556 / 30,964725 °C | 0,4440 W/K; 34,04 / 30,96 °C | stimmt |
| Becher, Unterschied / Q1 / Q2 | 3,078831 K; 46,602543 / 50,336384 kJ | 3,08 K; 46,60 / 50,34 kJ | stimmt |
| Milch für Tasse 2 bei Raumtemperatur | Tasse 2: 32,100041 °C; 1,946442 K | 32,10 °C; 1,95 K | stimmt |
| Milchbeitrag im vorigen Fall | -1,826190 kJ | -1,83 kJ, im Satz berücksichtigt | stimmt |
| Tasse 1 mit 105 Prozent kA, nach 60 min | 2,983093 K | 2,98 K | stimmt |
| 105 Prozent, gleiche Wärmeströme / Temperaturschnitt | 60,955260 / 84,890932 min | dieselben Werte im Kern | stimmt, zwei verschiedene Zeitpunkte |
| Grenzwert bei sehr später Zugabe | 20,000000 gegen 18,093242 °C; 1,906758 K | Auflösung: 1,91 K | stimmt |
| kA fest, Kaffee 95 °C | 37,69 / 33,22 °C; 4,47 K | ebenso gerundet | stimmt |
| kA aus Messung, Kaffee 95 °C | kA 0,6512 W/K; 25,50 / 22,06 °C | ebenso gerundet | stimmt |
| kA fest, Kaffee 100 / 400 ml | Unterschied 5,36 / 1,87 K | ebenso gerundet | stimmt |
| kA fest, Raum 10 / 30 °C | Unterschied 3,35 / 4,36 K | ebenso gerundet | stimmt |
| 100 ml Milch / Milch 60 °C | Unterschied 8,81 / -1,19 K | ebenso gerundet | stimmt |
| 300 ml Kaffee, 50 ml Milch, 90 / 10 / 25 °C, kA 0,25 | 54,04 / 50,21 °C; 3,83 K | ebenso gerundet | stimmt |
| Untere / obere kA-Grenze | Unterschied 1,50 / 2,38 K | ebenso gerundet | stimmt |
| Milchtemperatur für Gleichheit, Zugabe 30 / 60 / 90 min | 60,9 / 47,0 / 37,3 °C | DE und EN jeweils dieselben Zahlen | stimmt |
| Gerundetes Plateau ohne / mit Deckel | 53 bis 59 / 94 bis 106 min | dieselben Grenzen | stimmt |
| Beide kA um 10 Prozent falsch | höchstens 0,04 K, aufgerundete Schranke | 0,04 K | stimmt |
| Thermobecher offen, schwarzer Kaffee nach 30 min | 63,467111 °C | Auflösung: 63,5 °C | stimmt |
| Thermobecher offen, Maximum | 126,69243 min; 3,861838 K | etwa 127 min; 3,86 K | stimmt |
| Trinkzeit 60 °C, Standard | 10,90 / 16,60 min | 10,9 / 16,6 min | stimmt |
| Trinkzeit, Deckel | 19,47 / 29,65 min | dieselben Kernwerte | stimmt |
| Trinkzeit, Becher mit Mess-kA | 12,35 / 16,60 min | dieselben Kernwerte | stimmt |
| Becher kalt, kA 0,444031471 | 30,67 / 28,05 °C; 2,62 K | dieselben Kernwerte und Zusatzanzeige | stimmt |
| T10-Fit ohne Becher, Ursprung / frei | 0,3423 / 0,3444 W/K | ebenso gerundet | stimmt |
| Derselbe Fit im Messblatt mit Becher | 0,446688031 / 0,4495 W/K | 0,4467 / 0,4495 W/K | stimmt, andere Wärmekapazität |
| CSV, Standard bei 0 / 10 / 60 nach Milch | 70,47 und 80,00 / 60,78 und 67,00 / 34,05 und 30,19 °C | heruntergeladene CSV in DE und EN | stimmt |

Alle sechs Voreinstellungen aus Tabelle 8.2.1 wurden mit ihren genauen
Faktoren 1,00, 0,56, 1,00, 1,00, 0,90 und 0,44 geprüft. Die Richtwerte sind
als geschätzt gekennzeichnet. Kein unbelegter Thermobecher mit Deckel wurde
ergänzt. Die **74 Vorkommen modellabhängiger Zahlentokens** in Start, Frage 1,
Frage 2 und V1 bis V5 beider Sprachen stimmen mit der eigenen Rechnung.
Frage 2 enthält keine vorgegebene Ergebniszahl. Die Zahlen in den Auflösungen
sind korrekt; X5-02 betrifft ihre allgemeine fachliche Erklärung im Code-Reiter.

Nicht gebaute Kann-Punkte, insbesondere V6 und frei wählbarer Vergleich nach
der Milchzugabe, wurden nicht zum Pflichtmangel erklärt. Trinkzeit, kalter
Becher und CSV sind gebaut und wurden geprüft.

## B: Bedienung, Sprache und Barrierefreiheit

### Eigene Browserläufe

`pruefung_b.py` enthält 20 unabhängig formulierte Prüfgruppen. Der Pflichtweg
wurde mit falscher Startvorhersage, Begründung, Festhalten, Startauflösung,
Frage 1, Reglerprüfung und Frage 2 mit eigenen, ausdrücklich synthetischen
Kursdaten durchgespielt. Ein zweiter Ablauf verwendet „ohne Vorhersage
aufdecken“ und überspringt Frage 2 bei ausgefallenem Versuch. V1 bis V5 wurden
in der Reihenfolge der Studierenden bearbeitet und auf Ausgangslage und
Auflösung geprüft. Ein ergänzender englischer Lauf enthält bewusst falsche
Antworten in der Vertiefung. Die Auflösungen bleiben bis zum Festhalten gesperrt;
die Ausnahme V3 ist in X5-01 dokumentiert.

Eigene Vorhersagen aus der Bilanz: Tasse 1 um etwa 4 K wärmer, Maximum ungefähr
bei 56 min, Milch etwa 47 °C, Deckel verschiebt das Maximum, Becher verkleinert
den Unterschied, ungleiches kA wirkt stärker, Thermobecher hält am längsten warm.
Bei Frage 2 ist eine Aussage erst anhand der konkreten Messreihe möglich.
Diese waren Expertendurchgänge nach der Fachprüfung, keine unvorbereiteten
Studierendenläufe. Automatisierte Klickzeiten sind kein Nachweis für 10 Minuten
Lernzeit. Als Expertenschätzung bleiben für Start 2 bis 3, Frage 1 3 bis 4 und
Frage 2 mit schon geladenen Kurswerten 3 bis 5 Minuten plausibel. Die Länge der
Handyseite und der Rückweg zu den Karten kosten zusätzliche Orientierung.
Der echte Paarversuch bleibt offen.

Komma und Punkt, leere Felder, Unsinn, Werte außerhalb des Bereichs,
ungerundete Mittelwerte von Becher 2 und 3, beide 60-min-Zeilen, Messwertlöschung,
Deckel, Reload, Sprachwechsel, gesperrter Speicher, Rücksetzen mit Abbruch und
Bestätigung wurden geprüft. Die Übernahme von 80,015 und 67,035 °C bleibt
ungerundet. Eine Raumtemperatur von 40 °C wird bei der Übernahme mit Grund
zurückgewiesen, ohne die Einstellungen zu verändern. Bei ungültiger
Messkonfiguration verschwinden Kurven, Rechenwerte und Säulen.

Die Kurslink-Prüfung bestätigt Rückfrage, „Nicht übernehmen“, Zustimmung,
Erhalt persönlicher Antworten, drei Messspalten, Deckel und identische Werte
bei zwei Nachkommastellen. Defekte Version, Kodierung, Bereich und Überlänge
werden zurückgewiesen, der Fragmentteil verschwindet. X5-07 und X5-11 nennen
die zusätzlichen Randfälle. In den Browserläufen gab es keine externe Anfrage
der Kaffee-Seite und keinen JavaScript-Laufzeitfehler. Die CSP blockiert ein
zusätzlich eingeschobenes, nicht freigegebenes Inline-Skript. Der Offline-Lauf
benötigt nur die per Route bereitgestellte HTML-Datei, keine Begleitdatei.

**Vorhersagesperre P0:** In DE und EN wurden alle drei Reiter geöffnet und ihre
Abschnitte aufgeklappt. Sichtbare und versteckte DOM-Inhalte ohne Script/Style,
der Chromium-Barrierefreiheitsbaum und `aria-live` enthalten keine Ergebniszahl.
Es gibt keine Temperaturkurven und keine modellierten CSV-Werte. Die
Auflösungstexte in den Scriptbytes sind **keine Verletzung der didaktischen
Sperre**: Sie sind in dieser Offline-Datei unvermeidlich mitgeliefert, aber
weder gerendert noch im Barrierefreiheitsbaum oder in Ansagen. Ein Quelltextleser
oder selbst ausgeführtes JavaScript kann die Rechnung natürlich untersuchen.
Das ist kein zugesagter Zugangsschutz.

### Layout und Barrierefreiheit

108 Layoutzustände: neun Größen, jeweils DE und EN, P0, P2, P4, Vertiefung,
Code-Reiter und 200 Prozent Text. Größen: 320 × 640, 360 × 640, 390 × 844,
844 × 390, 768 × 768, 1024 × 768, 1366 × 768, 1280 × 720, 1920 × 1080.
Weitere Fokusprüfung bei 768 × 1024 und Tastatursimulation bei 390 × 380.
Bei Standardschrift kein Seitenüberlauf. Regler reagieren auf Pfeile, Bild
auf/ab, Pos1 und Ende; Plus/Minus und Zahlenfeld funktionieren. Reiter folgen
dem APG-Muster mit Pfeilen, Pos1 und Ende. Die Hilfen schließen mit Escape.
Am Handy funktioniert der Anheftschalter per simuliertem Tippen; bei geringer
Fensterhöhe und im Messfeld wird das Anheften abgeschaltet.

axe findet in P0, P4, Vertiefung und Code-Reiter bei 390 × 844 keine
WCAG-A/AA-Verstöße, jeweils mit einer manuell zu prüfenden Kategorie.
Das ist kein vollständiger WCAG-2.2-AA-Nachweis. Fokusverdeckung und zu kleine
Diagrammschrift wurden zusätzlich unabhängig reproduziert. Bei Standardschrift
sind die geprüften Bedienflächen mindestens 44 × 44 px, Textfelder mindestens
16 px. Die Bedienelemente haben Namen und die Bereichsregler `aria-valuetext`.
Statusmeldungen enthalten nach dem Loslassen die Kernzahlen, `lang` folgt dem
Umschalter. Formel- und Tabellenbereiche erhalten bei Bedarf Tastaturzugang.

Eigene Kontrastrechnung gegen Weiß: Tasse 1 5,84:1, Tasse 2 15,91:1,
Becher 3 5,19:1, Raumlinie 3,50:1, Überschriften 5,35:1, Nebentext 5,46:1,
Feldrand mit tatsächlich wirksamer Korrekturfarbe `#7d8fa1` 3,33:1.
Ein selbst erzeugtes und angesehenes Graustufenbild bestätigt die zusätzlichen
Linienarten. Diese Befunde bestätigen die Palette, nicht die Lesbarkeit der
verkleinerten Schrift.

Eine 30-Sekunden-Reglerfolge hatte zunächst einen einzelnen Cloud-Ausreißer
von 118,5 ms bei Median 2,6 ms. Die gezielte Wiederholung ohne parallele
Prüfläufe ergab 265 Schritte in 30,00 s, Median 2,7 ms, Maximum 11,9 ms,
keine veralteten Resultate und keine Laufzeitfehler. Eine harte 100-ms-Garantie
auf beliebigen Geräten ist damit nicht nachgewiesen. Der Ausreißer wird nicht
als gesicherter eigener Produktfehler ausgegeben.

Die 352 Textschlüssel sind in beiden Sprachen vorhanden; keine Gedankenstriche
U+2013/U+2014 und keine übrig gebliebenen Platzhalter. Frage- und
Auflösungstexte folgen Konzept 6, „du“ beziehungsweise „you“ und dem Glossar;
die Dezimalzeichen wechseln richtig. Ausnahme: X5-08 im Fehlerzustand.

Lernzentrum v8 wurde lokal in den Simulationsansichten von Thema 01 und 02 bei
390 und 1366 px angesehen. Vergleichsbilder `vorbild_thema*` und Kaffee-Bilder
liegen im eigenen Bildordner. Marine/Blau, Fira, Knopfhierarchie, Reglerhilfen,
Rechenwerte und drei Reiter passen erkennbar zum Vorbild. Die zusätzlichen
Vorhersagekarten, Plus/Minus, Energiesäulen, Messblatt und unmittelbare Rechnung
sind durch die Kaffee-Anforderungen begründet. Fehlende Themen-Seitenleiste
und fehlender Berechnen-Knopf sind daher keine Mängel.

## Muss-Anforderungen, einzeln bewertet

„Offen“ bedeutet fehlenden unabhängigen Nachweis, keinen behaupteten Fehler
des Produkts. Ein bestandener Teiltest hebt einen anderen Befund derselben
Anforderung nicht auf.

| ID | Ergebnis | Eigener Beleg |
|:--|:--|:--|
| M-1 | nicht vollständig erfüllt | Kern und Zahlen bestehen A; fachliche Gleichungen im Reiter stimmen beim Becher nicht, X5-02. Umstellung der Quelle verändert Voraussetzungen, X5-03. |
| M-2 | erfüllt | DE/EN, drei Reiter, DOM, AX-Baum, Ansage und CSV vor dem Start ohne Ergebnis; eigene Vorhersage bleibt beschriftet. |
| M-3 | nicht erfüllt | V3 nach Frage 2 verrät 3,08 K und die Richtung bereits vor der Vorhersage, X5-01; übrige Zustände bestanden. |
| M-4 | erfüllt | Wortlaut fachlich, Bereiche physikalisch sinnvoll; unzulässige Kombinationen werden mit Gültigkeitsprüfung behandelt. |
| M-5 | im geprüften Cloud-Lauf erfüllt | Sofortige Rechnung, kein Berechnen-Knopf, gezielte 30-s-Wiederholung maximal 11,9 ms; erster Ausreißer oben dokumentiert. |
| M-6 | nicht erfüllt | Verdeckter Tastaturfokus und zu großer angehefteter Bereich bei großer Schrift, X5-04 und X5-10. |
| M-7 | erfüllt | Feste Zeilen, drei Becher, zwei Mischsprünge, Deckel, ungerundete Übernahme, Ablehnung ganz oder gar nicht; Fit ohne Nachmilchwert. |
| M-8 | erfüllt | Im Pflichtweg genau ein sichtbarer Regler, weitere Regler erst nach Öffnen der Vertiefung. |
| M-9 | erfüllt | Beschriftung, Zeichen und Einheit sowie aufklappbare Hilfen im eigenen Browserlauf. |
| M-10 | erfüllt | Unabhängige Kontrastrechnung, Graustufenbild, Linienarten und Punktformen. |
| M-11 | nicht erfüllt | Kreis ohne Schnittbeschriftung in 16 von 72 gezielt geprüften Zuständen; außerdem Ersatzlegende statt direkter Kurvenbeschriftung, X5-06. |
| M-12 | erfüllt | Native Regler, Namen, aria-valuetext, Minus/Plus, Zahlenfelder, Komma/Punkt und alle geforderten Tasten. |
| M-13 | nicht in allen geprüften Zuständen erfüllt | Standardschrift besteht; bei 320 px und 200 Prozent Text kollabieren Bereichsregler auf 0 px Breite, X5-05. |
| M-14 | nicht erfüllt | Überlauf bei 200 Prozent Text und verkleinertes SVG im angehefteten Zustand, X5-05 und X5-09. |
| M-15 | offen, Teilnachweise bestanden | Namen/Beschreibung des SVG, Tabelle, Ansagen, Fokusstil und lang geprüft; echter Bildschirmleser fehlt, Fokusproblem X5-04 bleibt. |
| M-16 | erfüllt | Ungültige Einstellung blendet Ergebnisse aus; Bedienweg zum Wiederherstellen vorhanden. Sprachfehler separat X5-08. |
| M-17 | offen für tatsächliches Öffnen als Datei, übrige Teile erfüllt | HTTP, exakte Bytes bei offline=True, 0 externe Anfragen, wirksame CSP, gesperrter Speicher; file: durch Umgebung gesperrt. |
| M-18 | erfüllt nach höherrangigem Bauauftrag | Drei Reiter, Tastaturmuster und lokaler Vergleich mit dem echten v8-Tag; begründete Abweichungen akzeptiert. |
| M-19 | nicht erfüllt | 352 vollständige Textschlüssel und richtige Zahlenformate; aktuelle Fehlermeldung bleibt bei Sprachwechsel deutsch, X5-08. |
| M-20 | erfüllt | Gemeinsame Nulllinie, Werte und Satz zu Q2 minus Q1; Milchbeitrag -1,83 kJ erklärt den Unterschied 1,95 K. |
| M-21 | nicht für alle akzeptierten Eingaben erfüllt | Normaler Hin-/Rückweg besteht; Rundungsverlust und ignoriertes fremdes Format, X5-07 und X5-11. |
| M-22 | nicht vollständig erfüllt | 105-Prozent-Fall trennt Temperatur- und Wärmestromschnitt korrekt; Texte enthalten die Bedingung gleichen kA. Für die angebotene Becherbilanz fehlt jedoch C_B in den zwei allgemeinen Gleichungen, X5-02. |

## Befunde nach Schwere

Schwere nach BAU_AUFTRAG 4.1: blocker bei falscher fachlicher Gleichung oder
Ergebnis vor der eigenen Vorhersage, high bei verletzter Muss-Anforderung,
medium bei spürbarer Erschwernis. Alle folgenden Befunde wurden selbst
reproduziert. Die bekannten Befunde werden ausdrücklich als solche benannt.

| ID | Schwere | Befund | Beleg | Vorschlag |
|:--|:--|:--|:--|:--|
| X5-01 | blocker | **V3 beantwortet sich vor der eigenen Vorhersage.** Nach Frage 2 mit Messwerten 80 und 67 °C steht bei ungeprüfter V3 bereits „3,08 K, Tasse 1 wärmer“. Bekannt als G10-01; nach der vorgegebenen Schwerehierarchie hier blocker. | `ergebnis_b.json`, Test `V3_Antwort_vor_Vorhersage`: `fest=false`, Rechenwerte 34,04/30,96 °C, 3,08 K, 46,60/50,34 kJ; Bild `v3_vorhersage_vor_ergebnis.png`. `oberflaeche.js:297` wechselt die Frage ohne Ergebnisverdeckung. | V3 bekommt vor ihrer Vorhersage eine ergebnisfreie Ansicht oder einen eindeutig festgelegten Ablauf, der die Antwort nicht vorwegnimmt. Nicht nur den Auflösungsknopf sperren. Lernziel und Fragen nicht eigenmächtig ändern. |
| X5-02 | blocker | **Becherwärmekapazität fehlt in der allgemeinen Energiedifferenz und ihrer Zeitableitung.** Der Code-Reiter verwendet in DE und EN unbedingt C_G statt C_GB. Nach der Notation von Aufgabe und Konzept ist C_G nur Kaffee plus Milch. Mit Becher ergibt die gedruckte Formel 3,89857 statt 3,07883 K. Neuer Befund. | `texte_de.txt:767`, `:768`, `texte_en.txt:754`, `:755`; `ergebnis_ergaenzung.json`, `energy_formula`: C_G=957,746, C_GB=1212,746 J/K, Wärmeunterschied 3,733840 kJ. Bild `becherbilanz_falsches_CG.png`. Der numerische Kern selbst ist richtig. | In beiden Gleichungen C_GB verwenden und definieren, C_B=0 für den Fall ohne Becher; dieselbe Unterscheidung bei Erläuterungen und Tests sicherstellen. |
| X5-03 | high | **Wechsel zu „aus der Messung“ zeigt einen berechneten Ersatzwert als Messung und kann die Kurven sofort verändern.** Eingetragene 66,5 °C werden nach Festhalten, kA=0,25 und Rückwechsel durch 70,144996 °C ersetzt (Anzeige 70,1). Bei 100 ml, 60 °C Kaffee, 10 °C Raum und kA=1 wird zusätzlich auf 30 °C geklemmt: kA springt auf 0,638349 W/K, Unterschied von 1,168461 auf 1,501360 K. Widerspricht Konzept 8.5 und „nie als Messung angezeigt“. Neuer Befund. | `oberflaeche.js:768`; Test `Quellenwechsel_haelt_Kurven_bei_kA1`; `ergebnis_ergaenzung.json`, `measured_replaced`; Bild `messwert_durch_modellwert_ersetzt.png`. | Echte Messung und rechnerischen Ersatzwert getrennt halten. Ersatzwert nicht als Messung beschriften. Bei nicht darstellbarem Quellenwechsel verständliche Rückfrage oder Ablehnung, keine stille Begrenzung. Die entschiedene Eigenschaft „Quellenwechsel ändert Kurven nicht sofort“ mit Grenzfällen prüfen. |
| X5-04 | high | **Tastaturfokus hinter der Kernleiste bei großer Grundschrift.** Eigene Rückwärtsfolge bei 768 × 1024 und 32 px findet 16 verdeckte Fokusmitten, unter anderem `s-trink` und `z-kA1`. Bei 768 × 768 weitere acht Fälle. Bekannter G5-R3-01 bestätigt. | `ergebnis_ergaenzung.json`, `focus_768_1024_32px`; `ergebnis_layout.json`, `focus`; Bilder `fokus_768_1024_32px.png`, `fokus_verdeckt_768.png`. CSS `scroll-padding-top:56px` bleibt fest, die Kernleiste wächst. | Scrollabstand aus der tatsächlichen Höhe bestimmen oder Kernleiste bei Platzmangel lösen. Vorwärts- und Rückwärtstastenfolgen bei großer Grundschrift prüfen. |
| X5-05 | high | **Waagerechter Seitenüberlauf bei 200 Prozent Text, teils verschwindet der Regler.** Bei 320 px Breite wird die Seite 371 px breit, bei 360 px 391 px, bei 390 px 406 px, bei 768 px 797 px. Bei 320 px kollabieren acht sichtbare Bereichsregler auf 0 px Breite. Zusätzlich zu den bekannten Schriftproblemen selbst gefunden. | `ergebnis_layout.json`, Zustände `VT_200prozent_Text`, DE und EN. Bilder `grosse_schrift_390.png`, `grosse_schrift_768.png`; `.regler-zeile` hat feste Knopfspalten und ein 5,2-rem-Zahlenfeld. | Bei großer Schrift die Reglerzeile umbrechen, Zahlenfeld gegebenenfalls in eine zweite Zeile. Minimale Spaltenbreiten vermeiden, die zusammen breiter als die Seite werden. 320 px mit 200 Prozent Text gezielt nachprüfen. |
| X5-06 | high | **Schnittkreis ohne Beschriftung; Kurven teils nur in Ersatzlegende.** Bekannt als G6-R3-01 und -02. In der eigenen gezielten Stichprobe fehlen 16-mal bei vorhandenem Schnittkreis die Schnitttexte (72 Zustände, beide Sprachen). Beispiel: 390 × 844, t_Z=180 min, Milch 47 °C. | `ergebnis_layout.json`, `labels`; Bild `schnitt_unbeschriftet_390_47.0.png`; `oberflaeche.js:445` lässt die Beschriftung beim Scheitern der Platzsuche ausdrücklich weg. | Platz für Beschriftungen reservieren und bei Bedarf eine freie Randbeschriftung mit Verbindungslinie verwenden. Den Schnittpunkt eindeutig benennen und die direkte Kurvenzuordnung auch am Handy erhalten. |
| X5-07 | high | **Kurslink verändert akzeptierte Versuchsbedingungen.** Raum 21,555 °C und Milch 6,123 °C werden im Messblatt angenommen und gespeichert; nach Teilen und bestätigtem Rückimport stehen intern 21,56 und 6,12 °C. Der Verlust wird nicht angekündigt. Neuer Befund. | Test `Kurslink_alle_akzeptierten_Nachkommastellen` in `ergebnis_b.json`; `hilfen.js:20` rundet pauschal auf zwei Nachkommastellen, während die Bedingungsfelder beliebige Nachkommastellen annehmen. | Einheitliche Genauigkeitsregel für Eingabe, Speicher, Anzeige und Link. Entweder dieselbe zulässige Genauigkeit schon sichtbar bei der Eingabe festlegen oder alle angenommenen Stellen verlustfrei teilen. |
| X5-08 | high | **Englische Seite mit deutscher aktueller Fehlermeldung.** Aus Messung wählen, Kaffee auf 60 °C bei Messwert 67 °C setzen, dann Sprache wechseln: Dokument ist `en`, Hauptfehlermeldung bleibt „Der Messwert nach 10 min muss zwischen …“. Neuer Befund, verletzt M-19 im wichtigen Fehlerzustand. | Test `Ungueltige_Einstellung_und_Sprachwechsel`; Bild `befund_Ungueltige_Einstellung_und_Sprachwechsel.png`; `oberflaeche.js:783` zeichnet den Text nur bei geändertem Fehlercode. | Fehlermeldung auch bei Sprachwechsel neu übersetzen oder Sprache in den Aktualisierungsschlüssel aufnehmen. Alle bestehenbleibenden Meldungen entsprechend prüfen. |
| X5-09 | medium | **Sehr kleine Diagrammschrift am kleinen Handy.** Die SVG-Gesamtfläche bleibt breit, der Inhalt wird durch die Höhenbegrenzung verkleinert. Bei 360 × 640 misst der tatsächliche Transformationsmaßstab etwa 7,41 px für Rasterzahlen und 6,79 px für die Vorhersage. Bekannter Befund bestätigt. | `ergebnis_layout.json`, DE/P4/360; `getScreenCTM` statt bloßer CSS-Schriftgröße. Angesehenes Bild `P2_360x640_de.png`. Bei 390 × 844 beträgt der kleinste Text etwa 9,4 px. | Diagramm in seiner tatsächlichen Darstellungsgröße neu zeichnen und Beschriftungsgrößen erhalten; beim Platzkonflikt Anheften reduzieren oder lösen, nicht die gesamte Zeichnung verkleinern. |
| X5-10 | medium | **Angehefteter Bereich überschreitet 45 Prozent bei großer Schrift.** Gemessen bei 320 × 640 rund 63,7 Prozent, 360 × 640 rund 57,0 Prozent und 390 × 844 rund 47,0 Prozent. Abschalten ist möglich. Bekannter G5-R3-02 bestätigt. | `ergebnis_layout.json`, `diagram.holderRatio` bei `VT_200prozent_Text`; Bild `grosse_schrift_390.png`. Die Kernzahlen wachsen, der feste Abzug von 125 px in CSS wächst nicht mit. | Gesamthöhe einschließlich Kernzahlen und Vorhersage gegen `visualViewport.height` prüfen; bei Überschreitung automatisch lösen oder die Diagrammhöhe aus der verbleibenden Höhe berechnen. |
| X5-11 | medium | **Fremdes Fragment ohne kurs-Präfix wird still ignoriert.** `#foreign-data=123` lässt die Seite unverändert, zeigt aber keinen Grund und bleibt in der Adresse. Fremde Versionen mit kurs-Präfix werden dagegen korrekt gemeldet. Neuer Randfall gegenüber der allgemeinen Formulierung des X5-Auftrags. | Test `Kurslink_fremdes_Format`; `oberflaeche.js:897` kehrt für `art=fremd` ohne Präfix zurück. | Eigene Sprunganker ausdrücklich ausnehmen; fremde Datenformate verständlich melden und wie vorgegeben entfernen. Alternativ die Grenze zulässiger Seitenfragmente ausdrücklich in ZUSTAENDE festlegen lassen. |

## Ergänzende Belege und offene Nachweise

Erst nach eigener Nachrechnung wurden vorhandene Tests stichprobenartig
ausgeführt: `test_kern.py --html simulation/site/index.html` besteht mit
135 von 135, `test_texte.py` mit 14 von 14. Ausgaben sind im eigenen Ordner
gespeichert. Dass diese Tests grün sind, widerspricht den zusätzlichen
Bedienbefunden nicht: Beispielsweise prüft ein Vergleich des Rechenkerns nicht,
welchen Messwert der Quellenwechsel in der Oberfläche überschreibt.

Baubericht, bekannte Befunde, Prototypdokumentation, Zusammenführung der
Gutachten, EINSATZ_TUTORIUM und die Kurzkarte wurden als ergänzende
Stichproben gelesen. Die bekannte unvollständige Übergabe wird durch die
eigenen Befunde bestätigt. Die echte Vorabmessung der TL, der Paarversuch mit
Zeitmessung und die Geräteabnahme bleiben offen; synthetische Prüfdaten wurden
nicht als Kursmessung oder als Studierendennachweis ausgegeben.

Nach Korrekturen müssen zumindest die jeweiligen Reproduktionsfälle, die
betroffenen Muss-Anforderungen, der unveränderte Rechenkern, die neue
Artefakt-Prüfsumme und der reproduzierbare Bau erneut geprüft werden.
Es wurde nichts veröffentlicht und kein Pull Request angelegt.
