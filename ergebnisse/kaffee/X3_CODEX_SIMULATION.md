# Prüfung des Simulationstools, Rolle X3

**Urteil: mit kleinen Korrekturen.** Temperatur- und Wärmerechnung stimmen in den untersuchten Fällen. Bei der Schnittpunktanzeige besteht der nachstehende Randfallfehler. Vor dem Einsatz sollten die Fehler bei Schnittpunkt, ungültigen Einstellungen, Messwertübernahme und Fragenfolge korrigiert werden. Ein Umbau des Rechenmodells ist dafür nicht erforderlich.

Geprüft am 31.10.2026, Ausgangszweig `claude/kaffee-pruefung-sgvo1r`, Commit `53a78d55a28eb4902aceb832c3a0ae7d9321b9c7`. Bericht und eigene Prüfartefakte liegen auf `codex/kaffee-x3-simulation`. Werkzeug, Aufgabe und Lösung wurden nicht verändert.

## Befunde nach Wichtigkeit

Alle HTML-Zeilen beziehen sich auf `ergebnisse/kaffee/simulation/Kaffee_Simulation.html` im geprüften Ausgangscommit.

### Simulation 1: Ein zulässiger Kurvenschnitt wird als nicht vorhanden angezeigt

**Wichtigkeit: mittel. Stelle:** HTML 219 bis 224, 295 bis 298, 318 und 324 sowie die Erklärung in 156.

**Reproduktion:** Standardwerte laden, dann Kaffee anfangs 60 °C, Messung nach 10 min 50 °C, Milch 65 °C, Milchmenge 5 ml, relatives kA von Tasse 1 auf 110 % setzen. Die übrigen Werte bleiben bei 200 ml Kaffee, 20 °C Raumtemperatur, Zugabe nach 60 min, ohne Becher.

Die sofortige Mischung startet mit 60,118481918 °C knapp über dem schwarzen Kaffee. Sie kühlt schneller ab. Die Kurven schneiden sich nach **1,390569832 min**; danach ist der schwarze Kaffee wärmer. Das Werkzeug meldet jedoch **„keiner bis zur Zugabe“** und zeichnet keine Schnittmarke. Ursache: `d > 0` schließt die ebenfalls mögliche Richtung mit `d < 0` aus. Die Endtemperaturen sind auch hier richtig.

**Korrekturvorschlag:** Den Schnitt für beide Vorzeichen von `a2 - a1` bestimmen, Sonderfälle gleicher Abklingraten gesondert behandeln und anschließend auf eine positive Zeit innerhalb des dargestellten Intervalls prüfen. Die Beschriftung richtungsneutral formulieren oder aus dem tatsächlichen Verlauf ableiten. Die feste Aussage „ab hier ist der schwarze Kaffee kühler“ gilt in diesem Beispiel nicht.

**Belege:** `codex_skripte/x3/rechnung_ergebnis.json`, Fall `umgekehrter_schnitt`; `rechnung_svg_ergebnis.json`; `rechnung_schnitt_fehlt.png`.

### Simulation 2: Ungültige Einstellungen lassen alte Ergebnisse als aktuelle Ergebnisse stehen

**Wichtigkeit: mittel. Stelle:** HTML 310 bis 315, außerdem Aufruf durch die Messwertübernahme in 367.

**Reproduktion:** Standardwerte laden und allein die Anfangstemperatur auf 60 °C setzen. Der 10-min-Messwert bleibt 67 °C. Die Warnung erscheint, aber Diagramm, kA, Endtemperaturen und Aussage bleiben bei den alten Standardergebnissen. Nach Übernahme einer Messreihe mit Start 65 °C und 10-min-Wert 70 °C zeigen die Regler sogar 40 min und „Becher an“, während die Ergebniskarten weiter 60 min und „ohne Becher“ ausweisen.

Das ist auf dem Handy besonders missverständlich: Diagramm und Ergebnis stehen oberhalb der Regler; die Warnung liegt außerhalb des sichtbaren Ausschnitts. Auch neu eingetragene Messpunkte gelangen bei ungültiger Einstellung nicht in das wegen `return` unveränderte Diagramm.

**Korrekturvorschlag:** Bei ungültiger Konstellation Ergebniszahlen, Aussage und Diagramm sichtbar als ungültig kennzeichnen oder ausblenden. Die Fehlermeldung auch unmittelbar am Ergebnis anzeigen. Eine erfolgreiche Übernahme darf bei ungültiger Messreihe nicht gemeldet werden.

**Belege:** `bedienung_ergebnisse.json`, Einträge „Messwert größer als Start“, „Messwert gleich Raum“ und „Widersprüchliche Messreihe übernehmen“; `bedienung_390_uebernahme_ungueltig.png` und `bedienung_1366_ungueltig.png`.

### Simulation 3: Übernahme verändert Messwerte vor der Plausibilitätsprüfung

**Wichtigkeit: mittel. Stelle:** HTML 361 bis 369.

**Reproduktion:** Für Becher 2 und 3 jeweils bei 0 min 100 °C und bei 10 min 15 °C eingeben, Raumtemperatur 20 °C. Die Tabelle akzeptiert diese Werte innerhalb ihrer Eingabegrenzen. Beim Übernehmen werden daraus 95 °C und 30 °C. Danach rechnet das Werkzeug ohne Warnung mit kA = 3,6638 W/K und meldet „Übernommen“.

Die Originalreihe ist unter dem vorausgesetzten Abkühlmodell unmöglich, weil die Temperatur ohne Milch unter die Umgebungstemperatur gefallen sein soll. Das Begrenzen auf die Reglergrenzen macht daraus unbemerkt eine andere, scheinbar plausible Reihe. Auch normale Mittelwerte werden vor der Übernahme auf halbe Grad gerundet, beispielsweise 80,2 und 81,2 °C zu 80,5 statt 80,7 °C.

**Korrekturvorschlag:** Zuerst die unveränderten Mittelwerte gegen Modellgültigkeit und zulässigen Wertebereich prüfen. Unmögliche Reihen ablehnen. Eine erforderliche Begrenzung oder Rundung ausdrücklich mit Originalwert und übernommenem Wert nennen; besser die gemessenen Mittelwerte intern unverändert für die Rechnung verwenden. Die Tabelle mit den Rohdaten beibehalten.

**Beleg:** `bedienung_ergebnisse.json`, Eintrag „Übernahme außerhalb Reglerbereich“ und Vergleich mit „Mittelwerte übernehmen“.

### Simulation 4: Frage 3 setzt einen nicht genannten Rücksprung auf Standardwerte voraus

**Wichtigkeit: mittel. Stelle:** HTML 140 bis 145, insbesondere Frage 3 in Zeile 144; Erwartung in `Kaffee_Loesung.md`, Zeile 229.

Nach Frage 2 steht die Milch bei 47,0 °C, wenn die Gleichheit nach 60 min gefunden wurde. Wer nun wie aufgefordert nur den Becher einschaltet, erhält **Tasse 2 um 0,01 K wärmer**, nicht „Tasse 1 bleibt wärmer“. Auch die erwartete Änderung von 3,85 auf 3,08 K ist so nicht zu beobachten. Wird in Frage 2 zusätzlich der Zeitpunkt verändert, hängt Frage 3 auch von diesem zurückgelassenen Wert ab. Dieser Effekt wurde im unabhängigen Erst-Durchgang tatsächlich beobachtet.

**Korrekturvorschlag:** Vor Frage 3 ausdrücklich schreiben: „Laden Sie zunächst die Standardwerte der Aufgabe. Notieren Sie Unterschied und Wärmeabgaben. Schalten Sie dann den Becher ein.“ Auch vor Frage 1 den Ausgangszustand nennen und bei Frage 2 „ungefähr gleich warm“ erlauben. Die 0,01-K-Anzeige ist hier rechnerisch korrekt; die Aufgabenfolge ist unklar.

**Belege:** `fragen_q3_sequenziell_nach_q2.png`, `fragen_q3_standard_mit_becher.png`, `fragen_browserprotokoll.json`.

### Simulation 5: Fehlerhafte Zahlentexte werden teilweise als Messwerte gespeichert

**Wichtigkeit: niedrig. Stelle:** HTML 343 bis 350, Statusmeldung in `uebernahme_info`.

Zeit `10,5,9` und Temperatur `66.5xyz` werden als 10,5 min und 66,5 °C übernommen. `parseFloat` verwertet nur den gültigen Anfang. Die Eingabe ist damit scheinbar erfolgreich, obwohl der eingegebene Text keine eindeutige Zahl ist. Nach einem vorangegangenen Fehler bleibt zudem dessen Meldung bei einer späteren erfolgreichen Eintragung stehen.

**Korrekturvorschlag:** Nach Normalisierung eines Dezimalkommas die gesamte Eingabe als Zahl validieren, beispielsweise durch vollständige Formatprüfung und `Number`. Leere Eingaben weiterhin gesondert abweisen. Den Eingabestatus bei erfolgreichem Eintragen aktualisieren. Komma und Punkt müssen weiterhin funktionieren.

**Beleg:** `bedienung_ergebnisse.json`, Einträge `Eingabe ["10,5,9","66.5xyz"]` in beiden Breiten. Reine Buchstaben, unendliche Werte und Werte außerhalb der numerischen Grenzen werden bereits abgewiesen.

### Simulation 6: Erwartung zur sehr späten Zugabe braucht eine genauere Formulierung

**Wichtigkeit: niedrig, redaktionelle Präzisierung ohne Freigabehindernis. Stelle:** `Kaffee_Loesung.md`, Zeile 229, Erwartung zu Frage 1: „beide nähern sich der Raumtemperatur“. Das kann bereits die beiden unmittelbar zuvor genannten Abkühlkurven meinen; eine falsche Werkzeugrechnung liegt nicht vor.

Das stimmt für die beiden Abkühlkurven **vor** der späten Milchzugabe. Es stimmt nicht für die verglichenen Endtemperaturen **nach** Zugabe frischer kalter Milch. Bei den Standardwerten gilt für sehr späte Zugabe:

\[
\vartheta_1\to20\,^{\circ}\mathrm C,\qquad
\vartheta_2\to\frac{836\cdot20+121{,}746\cdot5}{957{,}746}
=18{,}09324\,^{\circ}\mathrm C.
\]

Der Unterschied fällt nach seinem Maximum gegen **1,90676 K**, nicht gegen null. Das Werkzeug rechnet dies richtig; die Formulierung in den Hinweisen kann zu einer falschen Erklärung führen.

**Korrekturvorschlag:** Vor und nach dem Mischen ausdrücklich unterscheiden: „Nach dem Schnitt ist der schwarze Kaffee vor der Zugabe kühler als Tasse 1; die zusätzliche Wärmeabgabe von Tasse 1 verkleinert den Unterschied. Die beiden Abkühlkurven nähern sich vor der späten Zugabe der Raumtemperatur. Frische kalte Milch senkt die Temperatur von Tasse 2 beim Mischen erneut.“

**Beleg:** `rechnung_zusatz.py` und `rechnung_zusatz_ergebnis.json`, Grenzwert und Kontrollrechnung bei 10.000 min. Dies ist eine Prüfung des Grenzverhaltens außerhalb des Reglers, keine Behauptung über einen zusätzlichen zulässigen Reglerwert.

## Eigene Rechnung und Umfang

Die eigenständige Herleitung steht in `codex_skripte/x3/rechnung_unabhaengig.py`. Dieses Skript entstand vor Einsicht in den HTML-Modellteil und importiert weder ihn noch `kaffee_modell.py`. Grundlage waren Aufgabe, Formelsammlung und Foliensatz 05. Aus der globalen Bilanz folgt durch Trennung der Variablen:

\[
C\frac{d\vartheta}{dt}=-kA(\vartheta-\vartheta_u),\quad
\ln\frac{\vartheta-\vartheta_u}{\vartheta_0-\vartheta_u}=-\frac{kA}{C}t.
\]

Mischung wird aus der Erhaltung der inneren Energie berechnet. Für den Becher wird dessen Kapazität sowohl beim Mischen als auch beim Abkühlen und Kalibrieren eingeschlossen. Die Wärmeabgabe wird unabhängig als Anfangsenergie einschließlich der jeweiligen Milchenergie abzüglich Endenergie berechnet. Der Kurvenschnitt wird numerisch durch Bisektion gesucht, nicht mit der Formel des Werkzeugs übernommen.

### Standardwerte und Teile f und g

| Fall | ϑ₁ in °C | ϑ₂ in °C | Unterschied in K | Q₁ in kJ | Q₂ in kJ | kA in W/K |
|:---|---:|---:|---:|---:|---:|---:|
| Standardwerte | 34,046483 | 30,193282 | 3,853201 | 34,880847 | 38,571235 | 0,340247765 |
| Milch 60 °C, Teil f | 35,992443 | 37,184729 | −1,192286 | 39,713141 | 38,571235 | 0,340247765 |
| Becher 300 g, Teil g | 34,043556 | 30,964725 | 3,078831 | 46,602543 | 50,336384 | 0,444031473 |

Die anfängliche Mischtemperatur ohne Becher beträgt 70,466209 °C, der schwarze Kaffee vor der späten Standardzugabe 33,862160 °C. Der Schnitt liegt bei 55,744669 min. Alle gerundeten Standardanzeigen stimmen mit der Lösung überein. Die Differenz wird aus ungerundeten Temperaturen berechnet; aus 34,05 minus 30,19 folgt deshalb nicht die angezeigte letzte Nachkommastelle.

### Eigene Parametersätze

29 Sätze insgesamt: Standard, Teil f, Teil g und 26 eigene Varianten. Die vollständigen Eingaben und Soll-/Istwerte sind in `rechnung_ergebnis.json` enthalten. Grenzen wurden einzeln und in Kombination geprüft:

| Größe | Geprüfte Grenzen / zusätzliche Kombinationen |
|:---|:---|
| Zugabezeit | 1 und 120 min; zusätzlich 30, 40, 60 und 90 min |
| Milchtemperatur | 2 und 65 °C; zusätzlich 12,5, 20, 38,5 und 60 °C |
| Milchmenge | 5 und 100 ml; zusätzlich 45 und 65 ml |
| Raumtemperatur | 10 und 30 °C; zusätzlich 15,5 und 22,5 °C |
| Anfangstemperatur | 60 und 95 °C, jeweils mit zulässiger Messung |
| 10-min-Messung | 30 und 90 °C, für 90 °C mit Anfangstemperatur 95 °C |
| Kaffeemenge | 100 und 400 ml; zusätzlich 170 und 250 ml |
| Relatives kA von Tasse 1 | 90 und 110 %; zusätzlich 97 und 104 % |
| Bechermasse | 100 und 600 g bei eingeschaltetem Becher; zusätzlich 240 und 430 g |
| Schalter | Becher an/aus; Milch für Tasse 2 bei Raumtemperatur |

Je Satz wurden beide Kurven an 161 Zeitpunkten einschließlich Start und Zustand unmittelbar vor der Zugabe geprüft, insgesamt **9.338 Werte**. Vorher-/Nachherzustand des Mischsprungs wurde ebenfalls verglichen. Das Werkzeug behauptet keine weitere Abkühlkurve nach dem Vergleichszeitpunkt.

Außer Simulation 1 gab es keine numerische Abweichung: Temperaturen maximal etwa 1,2 · 10⁻¹³ K, Wärmeabgaben maximal 1,7 · 10⁻¹⁰ J, kA etwa 1,2 · 10⁻¹⁶ W/K. Dies ist Gleitkommarundung. In Chromium wurden anschließend alle Ergebniskarten und die tatsächlich erzeugten SVG-Polylinien dieser 29 Sätze gegen die eigenen Sollwerte geprüft. Die SVG-Abweichung bleibt unter 0,05 Zeichenpixeln, genau der Rundung auf eine Nachkommastelle in den SVG-Koordinaten. Die Mischsprünge stimmen ebenfalls.

## Modelltreue, Sprache und Darstellung

Alle Regler sind durch `P`, `rechne`, `zwei_tassen` oder `becher` im Referenzmodell begründet. Die getrennte Temperatur der späten Milch und das relative kA von Tasse 1 sind dort ausdrücklich vorgesehen. Wärmeabgaben mit Becher folgen derselben Energiebilanz mit erweitertem Bilanzraum. Die Diagrammkurve von Tasse 2 zeigt bis zum Zugießen schwarzen Kaffee, der Sprung dessen anschließende Mischung.

Die Funktionen `nichtlinear` und `gleichstand` des Referenzskripts müssen für die vier vorgesehenen Fragen nicht als weitere Regler erscheinen. Die Grenze des linearen Modells wird erklärt. Eine zusätzliche Anzeige der Zeitkonstanten wäre nützlich, aber kein Freigabehindernis. Die automatische Anzeige der Gleichstandsmilch würde dagegen Frage 2 vorwegnehmen.

Deutsch, Begriffe und Formelzeichen passen zu Aufgabe und Lösung und sind für Studierende im dritten Semester angemessen. In der HTML-Datei wurden keine Gedankenstriche der Zeichen U+2013 und U+2014 gefunden; mathematische Minuszeichen sind korrekt. Detaillierte Zuordnung: `modell_sprache_notizen.md`.

Der Bedienungstest erzeugte **92 dokumentierte Zustände** bei 1366 × 900 und 390 × 900 Pixeln. Alle neun Regler wurden an beiden Grenzen, beide Schalter in beiden Zuständen, das Aufklappen der weiteren Größen, beide Voreinstellungsknöpfe, Übernehmen mit und ohne Daten, einzelnes und vollständiges Löschen sowie Neuladen geprüft. Zusätzlich wurde ein Regler per Tastatur bedient. Messwerte für alle drei Becher wurden mit Komma und Punkt eingetragen. Messpunkte und Tabelle bleiben nach Neuladen erhalten, nach vollständigem Löschen auch nach erneutem Neuladen leer. Einstellungen selbst werden beim Neuladen auf Standard gesetzt; dauerhafte Speicherung wird im Werkzeug nur für Messwerte zugesagt.

Die Bildschirmfotos wurden visuell angesehen. Bei beiden Breiten sind Inhalte und Bedienelemente lesbar, die Tabellen umbrechen, es gibt kein waagerechtes Scrollen. Bei 390 Pixeln erfordert der Wechsel zwischen Diagramm und Reglern vertikales Scrollen. Das ist bedienbar, verstärkt aber den Effekt von Simulation 2. Keine abgeschnittenen Formeln, überlappenden Kurvenbeschriftungen oder JavaScript-Fehler in den dokumentierten Zuständen. Die Fotos `bedienung_1366_standard.png`, `bedienung_390_standard.png`, `bedienung_390_messwerte.png` und die Fehlerfotos belegen die Bewertung.

### Offline-Prüfung und Grenze der Umgebung

Die HTML-Datei enthält CSS und JavaScript vollständig eingebettet und fordert keine externen Dateien an. Alle eigenen Browsertests liefen mit `offline: true`. Die unveränderten lokalen HTML-Bytes wurden per Playwright-Route unter `http://localhost:31460/x3-simulation.html` ausgeliefert, alle anderen Anfragen blockiert. Es gab keine Anfragen an externe Ziele und keine Browserfehler.

Ein direkter Start über `file://` wurde versucht, ist in dieser verwalteten Chromium-Umgebung aber durch die vorhandene Unternehmensrichtlinie mit `ERR_BLOCKED_BY_ADMINISTRATOR` gesperrt. Diese Richtlinie wurde nicht geändert. Die Datei ist damit als unveränderte Einzelseite ohne Internet browsergeprüft; der direkte Doppelklick auf eine lokale Datei in einem unverwalteten Browser ist hier nicht praktisch verifiziert. Die zur Prüfung benötigten Werkzeuge gehören zur Prüfumgebung, nicht zu den Voraussetzungen der HTML-Anwendung.

## Vier Fragen: unabhängiger Erst-Durchgang

Methodische Offenlegung: Beim Orientierungsscan der Koordination wurde versehentlich bereits die Erwartungszeile der Lösung sichtbar. Deshalb übernahm ein frisch gestarteter Teilprüfer ohne diesen Kontext den Erst-Durchgang. Er las zunächst nur X3-Auftrag und Werkzeug, benutzte für Antworten ausschließlich die sichtbare Oberfläche und hielt sein Protokoll vor dem Erwartungsvergleich fest. Die getrennte Gegenrechnung und Bedienungsprüfung verwendeten keine vorhandenen Tests.

Der vollständige automatisierte Browserlauf dauerte **50,616 s** vom 31.10.2026, 18:08:13 bis 18:09:04 Uhr MEZ, einschließlich dichter Reglerdurchläufe und 509 protokollierter Zustände. Voraus gingen dokumentierte Startversuche und ein erster lokaler Teildurchlauf; bis zur schriftlichen Festhaltung der Antworten vergingen ab dem ersten erfolgreichen Lauf etwa 2 min 34 s. Das ist technische Ablaufzeit und keine gemessene Lernzeit von Studierenden. Eine tatsächliche Bearbeitungsdauer von 10 bis 15 Minuten wurde nicht durch einen Versuch mit Studierenden nachgewiesen.

| Frage | Eigene Beobachtung allein mit dem Werkzeug | Stockstelle / Bewertung |
|:---|:---|:---|
| 1, Zeitpunkt | Maximum ungefähr 56 min, Anzeige 3,86 K; bei 120 min nur noch 3,02 K. Die Kurven erklären den Wechsel der relativen Wärmeabgabe nach ihrem Schnitt. | Wegen Rundung steht von 53 bis 59 min jeweils 3,86 K. Ein genauer einzelner Minutenwert ist allein aus der Differenzanzeige nicht eindeutig. „Ungefähr“ genügt. |
| 2, Milchtemperatur | Bei 60 min zeigt 47,0 °C Milch „gleich warm“; 46,5 °C ergibt +0,05 K, 47,5 °C −0,05 K. Bei verändertem Zeitpunkt ist eine andere Temperatur nötig. | Der Regler rastet in 0,5-K-Schritten. Für andere Zeitpunkte ist exakte Gleichheit nicht immer einstellbar. Zeitpunkt und Vergleichszeit sind derselbe Regler. |
| 3, Becher | Direkt nach Frage 2 wird Tasse 2 um 0,01 K wärmer. Nach Standard-Reset sinkt der Unterschied korrekt von 3,85 auf 3,08 K, Q₁/Q₂ steigen auf 46,60/50,34 kJ. | Fehlende Reset-Anweisung, siehe Simulation 4. Mit geklärtem Ausgangszustand leicht lösbar. |
| 4, Versuch | Ohne reale Messwerte bleibt die Tabelle leer; Übernehmen meldet fehlende Start-/10-min-Werte und setzt 40 min sowie Becher an. | Es lagen keine eigenen realen Versuchsdaten vor. Eine tatsächliche Lage realer Messpunkte wurde daher nicht behauptet. Synthetische Werte dienten separat nur der Bedienungsprüfung. |

Für die vorgesehene Schlussphase erscheint ein Durchgang in 10 bis 15 Minuten nach Klärung des Ausgangszustands plausibel, wenn die realen Messwerte bereits vorliegen und vorbereitet sind. Die Begründung in Frage 1 greift auf die zuvor erarbeitete Bilanz zurück. Frage 4 kann ohne Versuchsdaten nicht vollständig bearbeitet werden. Die mobile Bedienung benötigt zusätzliche Scrollwege. Diese Einschätzung ersetzt keine Zeitmessung im Tutorium.

### Nachrechnung der erwarteten Antworten

Die eigene Nachrechnung ergibt das Maximum bei **55,74467 min mit 3,861837922 K**. Die Gleichstandsmilch liegt bei **60,91227 °C nach 30 min**, **47,00309 °C nach 60 min** und **37,28450 °C nach 90 min**. Die in den Hinweisen genannten gerundeten Zahlen stimmen. Becherwerte stimmen ebenfalls, wenn vorher die Standardwerte geladen werden. Die Erklärung zum Grenzverhalten braucht die Präzisierung aus Simulation 6. Eine allgemeine Erwartung zur tatsächlichen Lage realer Messpunkte ist eine Versuchshypothese und wurde hier mangels realer Versuchsdaten nicht bestätigt.

## Abschließender Vergleich mit vorhandenen Tests

Erst nach Abschluss der eigenen Rechnungs-, Bedienungs- und Fragenprüfungen wurden `simulation/test_simulation.py`, `simulation/browsertest.js`, deren gespeicherte Ergebnisdateien sowie alle sechs vorhandenen Bildschirmfotos gelesen beziehungsweise angesehen. Die gespeicherten Ergebnisse nennen **26 von 26** und **30 von 30** bestandene Prüfungen. Sie wurden als vorhandene Protokolle eingeordnet und hier nicht erneut ausgeführt oder überschrieben.

Die positiven Standardbefunde und die lesbare Darstellung stimmen mit der eigenen Prüfung überein. Die neuen Befunde werden durch diese Tests nicht ausgeschlossen:

- Der vorhandene Zahlentest importiert das Referenzmodell. Ein fehlender Schnitt wird bei den verallgemeinerten Fällen nicht unabhängig gesucht: Die Gleichheit am Schnitt wird nur geprüft, wenn das Werkzeug selbst eine endliche positive Schnittzeit meldet. Ein fälschlich fehlender Schnitt wie Simulation 1 fällt damit nicht auf.
- Der vorhandene Browsertest setzt vor dem Bechertest ausdrücklich auf Standard zurück. Er bearbeitet deshalb nicht die im Fragetext naheliegende direkte Fortsetzung von Frage 2.
- Widersprüchliche Regler-/Messwertkonstellationen, stille Begrenzung und mehrdeutige Zahlentexte sind dort nicht abgedeckt. Die Messwertbeispiele sind in dessen Kommentar ausdrücklich als erfunden bezeichnet.

Die unabhängigen Skripte erweitern somit die Prüfabdeckung. Die vorhandenen Tests wurden nicht als Beweis für die Richtigkeit des Modells verwendet.

## Reproduzierbarkeit

Aufrufe vom Repository-Stamm, mit Python 3.12, Node 24, Playwright und Chromium der Prüfumgebung:

```bash
python ergebnisse/kaffee/codex_skripte/x3/rechnung_vergleich.py
node ergebnisse/kaffee/codex_skripte/x3/rechnung_svg.js
python ergebnisse/kaffee/codex_skripte/x3/rechnung_zusatz.py
node ergebnisse/kaffee/codex_skripte/x3/bedienung_browser.js
node ergebnisse/kaffee/codex_skripte/x3/fragen_durchgang.js
node ergebnisse/kaffee/codex_skripte/x3/fragen_nachrechnung.js
```

Die Skripte speichern die eigenen Ergebnisse als JSON beziehungsweise Text und erzeugen die genannten Bildschirmfotos. Bekannte Abweichungen werden als Befunde dokumentiert; ein erfolgreicher Skriptaufruf bedeutet daher nicht, dass der Prüfling fehlerfrei ist. Die Browserausführung benötigt in dieser Sandbox zusätzliche Prozess-/Netzwerkrechte, auch für ausschließlich lokal erfüllte Anfragen.
