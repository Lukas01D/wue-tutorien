# Ablauf und Zustände der Kaffee-Simulation

> Festgelegt vor dem Bau nach `simulation/BAU_AUFTRAG.md`, Teil 1.5 (P09, P10, P11) und 3.5 (P13). Grundlage: `KONZEPT.md` Fassung 2 (Abschnitte 3, 4, 5, 6, 9), Entscheidungen E1 bis E8 und K1 bis K11, Entscheidung K5 des Lernzentrums (drei Reiter). Was hier steht, prüfen die Tests in `simulation/tests/`.

## 1 Zustände des Pflichtwegs

Die Seite hat einen Fortschritt je Gerät (im Browser gespeichert, Abschnitt 2). Die Frageleiste über dem Diagramm zeigt immer die aktuelle Frage; dieselben Fragen stehen als Karten im Reiter „Versuche“ (Muster der Versuchskarten des Lernzentrums v8).

| Nr. | Zustand | Auslöser | Sichtbar | Nicht sichtbar (gesperrt) |
|:--|:--|:--|:--|:--|
| P0 | **Startkarte** | erstes Öffnen, nach „Für die nächste Gruppe zurücksetzen“ | Kopf, Sprachumschalter, Startkarte (Frage, Auswahl Tasse 1, Tasse 2, gleich warm; Feld „etwa … K“; Feld „Warum? (ein Satz)“), Diagrammrahmen mit Achsen, Raumlinie und Startpunkt 80 °C, Lesehinweis, Reiter | Kurven, Mischsprünge, Schnittpunkt, Rechenwerte (Kasten zeigt „erscheint nach eurer Vorhersage“), Energiesäulen, Bilanzraum, Wertetabelle des Diagramms, Statusansage mit Zahlen, Regler, Vertiefung, Messblatt-Übernahme |
| P1 | **Vorhersage gewählt** | Auswahl einer Tasse | wie P0; Knopf „Vorhersage festhalten und Kurven zeigen“ wird aktiv. Das Feld „etwa … K“ und die Begründung sind freiwillig. | wie P0 |
| P2 | **Freigabe** | Knopf in P1 | Kurven, Rechenwerte, Säulen „Energie bis zur Zugabe“, eigene Vorhersage als beschrifteter Kasten im Diagramm; Auftrag „Erklärt den Unterschied mit *Q*₁ und *Q*₂.“; in der Karte „Start“ der Knopf „Auflösung zeigen“; Frageleiste springt zu Frage 1 | Regler „Zugabe nach“ (gesperrt mit Hinweis „Erst eure Vorhersage zu Frage 1 festhalten“), Auflösung von Frage 1 und 2 |
| P3 | **Frage 1 ungesehen** | nach P2 | Fragetext, Feld „… min“, Begründung, Knopf „Vorhersage festhalten, dann prüfen“ | Regler, Auflösung Frage 1 |
| P4 | **Frage 1 geprüft** | Knopf in P3: hält die Vorhersage fest, stellt die Ausgangslage ein (Standardwerte) und sagt das an | Regler „Zugabe nach“ wirkt sofort; Auftrag „Prüft dann: Verschiebt die Zugabe … Warum wird der Unterschied bei späterer Zugabe wieder kleiner? Stimmt eure Vorhersage? Erklärt zu zweit, warum.“ *(geändert 06.11.2026, Entscheidung F4 der TL)*; Knopf „Auflösung zeigen“; „Weiter zu Frage 2“ | Auflösung Frage 2 |
| P5 | **Frage 2 ungesehen** | „Weiter“ oder Frageleiste | Fragetext, Auswahl über, unter, auf den Kurven, mal so, mal so; Begründung; Hinweis auf die Kurswerte: geladen (Datum der Werte, Zahl der Messpunkte) oder „Noch keine Kurswerte“ mit „Messblatt öffnen“ und „Frage 2 überspringen (Versuch ausgefallen)“ | Auflösung Frage 2 |
| P6 | **Frage 2 geprüft** | Knopf „Vorhersage festhalten, dann prüfen“; nur mit Kurswerten aktiv | Messpunkte im Diagramm, Einstellungen aus den Messwerten übernommen (Ausgangslage), Auftrag „Beschreibt, wo die Punkte liegen. Nennt eine mögliche Ursache und eine Messung, mit der ihr sie prüfen könntet.“; „Auflösung zeigen“ | nichts mehr gesperrt |
| P7 | **Pflichtweg fertig** | nach P6, sobald die Auflösung von Frage 2 geöffnet ist, oder nach „überspringen“ *(F8)* | Hinweis „Geschafft. Kernsatz: Wer heißer ist, gibt mehr Wärme ab; deshalb Milch sofort. Erhalten bleibt die Energie von Tassen und Raum zusammen. Weiter geht es in der Vertiefung.“ *(F8)* mit Knopf „Vertiefung öffnen“ | |

**Regeln:**

1. Vor P2 zeigt **nichts** die Antwort auf die Startfrage: keine Kurve, keine Zahl, keine Säule, keine Tabelle, keine Ansage, kein Text in „Modell“ oder „So rechnet der Code“ (Abschnitt 3). Ein Browsertest durchsucht DOM, `aria-live` und alle Reiter nach Ergebnissen (z. B. „34,05“, „30,19“, „3,85“, „wärmer“ in Ergebnissätzen).
2. Nach P2 wirken alle sichtbaren Regler sofort (keine Berechnen-Taste; M-5). Der einzige getrennte Prüfschritt ist „Vorhersage festhalten, dann prüfen“ je Frage (Konzept M-3).
3. „Vorhersage festhalten“ ist erst aktiv, wenn eine Auswahl oder Zahl eingegeben ist. Die Begründung ist freiwillig, das Feld steht aber vor dem Knopf.
4. „Auflösung zeigen“ einer Frage ist erst nach ihrer festgehaltenen Vorhersage aktiv. Wie im Lernzentrum gibt es darunter den kleinen Verweis „ohne Vorhersage aufdecken“ (für die TL und Wiederholer); er hält „ohne Vorhersage“ als Vorhersage fest. *(Übernahme aus dem Lernzentrum, `dist/topic.js`, „ohne Vermutung aufdecken“.)*
5. Die Vertiefung ist erst nach P2 erreichbar. Sie ist frei: Wer sie vor Frage 1 öffnet, sieht den Hinweis „Die Vertiefung ist für danach gedacht. Erst Frage 1 und 2.“, wird aber nicht gesperrt.

## 2 Vertiefung

Jede Vertiefungsfrage V1 bis V6 hat die Zustände ungesehen, vorhergesagt und geprüft, wie im Pflichtweg; „Prüfen“ stellt ihre Ausgangslage ein:

| Frage | Ausgangslage (Konzept 6.2) | Eingabe |
|:--|:--|:--|
| V1 Milchtemperatur | Standardwerte | Zahl in °C |
| V2 Deckel | Standardwerte, *kA* festhalten (Voreinstellung „Keramik mit Deckel“ wählen die Studierenden selbst) | Auswahl größer, kleiner, gleich; Zahl in min |
| V3 Becher | Standardwerte, *kA* aus der Messung, Becher an | Auswahl größer, kleiner |
| V4 Versuchsplan | Standardwerte | Auswahl „ungleiches *kA*“, „falsches *kA* beider Becher“ |
| V5 Welcher Becher? | Standardwerte, *kA* festhalten | Auswahl der Voreinstellungen |
| V6 Trinken (nur mit K-6) | Standardwerte, Vergleich nach 90 min | Auswahl größer, kleiner, gleich |

Die Regler der Vertiefung (Konzept S-2) sind nach P2 immer bedienbar, unabhängig vom Zustand der Vertiefungsfragen.

*Ergänzt am 06.11.2026 (Korrekturrunde nach X5):*

- **Öffnen einer Vertiefungsfrage ohne Vorhersage (X5-01):** Enthält die Einstellung schon die Bedingung der Frage (V1 Milch ab 30 °C, V2 Deckel, V3 Becher an, V4 *kA* von Tasse 1 ungleich 100 %, V5 andere Voreinstellung als Keramik), stellt die Seite die Standardwerte ein und sagt das an. Sonst bleibt die Einstellung.
- **Sätze zum Schnitt (F11):** In „Modell“ (Lesehilfe: Kreis, Wärmestrom) und „So rechnet der Code“ (Absatz „Zeitpunkt der Zugabe“) erst nach der Vorhersage zu Frage 1.
- **Quelle von *kA* (X5-03, Konzept 8.2 M8 und 8.5):** Der Wechsel auf „aus der Messung“ ändert die Kurven nicht. Passt die gespeicherte Messung nicht zum aktuellen *kA*, steht im Feld der gleichwertige Wert, beschriftet als „aus *kA* berechnet“, keine Messung; die eigene Messung bleibt gespeichert und lässt sich wieder verwenden. Liegt der gleichwertige Wert außerhalb von 30 bis 90 °C, bleibt die Quelle „festhalten“ mit Meldung.

## 3 Was die drei Reiter in jedem Zustand zeigen

Zuordnung der Texte aus Konzept Anhang A siehe `VORBILD_LERNZENTRUM.md`, Abschnitt 7.

| Reiter | P0 und P1 | ab P2 |
|:--|:--|:--|
| **Versuche** (offen) | Satz „Erst vorhersagen, dann prüfen.“, Karte „Start“ aufgeklappt mit denselben Feldern wie die Startkarte; Karten Frage 1, Frage 2 und Vertiefung zugeklappt mit dem Hinweis „nach dem Start“; „Alle Fragen zurücksetzen“ | alle Karten; Auflösungen je Karte nach deren Vorhersage |
| **Modell** (zu) | alle fünf Abschnitte nur mit dem Hinweis (F11: auch „Physikalisches Problem“ erst nach der Startvorhersage) „erscheint nach eurer Vorhersage auf der Startkarte“ | fünf zugeklappte Abschnitte: Physikalisches Problem, Annahmen, Was die Simulation macht, Regler und Einheiten, So liest du die Ergebnisse |
| **So rechnet der Code** (zu) | Hinweis „erscheint nach eurer Vorhersage auf der Startkarte“ | Rechenweg (Bilanz, Lösung, *kA*, Mischen, Wärme, Zeitpunkt der Zugabe, *kA* festhalten, Ausgleichsgerade) und Beschreibung des Codes |

Kein Text in „Modell“ oder „So rechnet der Code“ nennt eine Antwort auf Frage 1, Frage 2 oder eine Vertiefungsfrage (K10); diese stehen nur in den Auflösungen.

## 4 Was erhalten bleibt

Speicher: `localStorage`, Schlüssel mit Vorsilbe `kaffee-sim-v2-` (Konzept 9.3). Getrennte Schlüssel für **persönliche Antworten** (`antworten`: Startkarte, Vorhersagen, Begründungen, Zustände der Fragen), **Einstellungen** (`einstellungen`), **Kurswerte** (`kurswerte`), **Ansicht** (`ansicht`: Sprache, offene Reiter, Vertiefung offen, Diagrammansicht).

| Ereignis | Antworten | Einstellungen | Kurswerte | Ansicht |
|:--|:--|:--|:--|:--|
| Sprachwechsel | bleiben | bleiben (keine fachliche Änderung, nur Zahlenformat) | bleiben | Sprache neu, sonst gleich; Fokus bleibt auf dem Umschalter |
| Reiterwechsel | bleiben | bleiben | bleiben | Reiter neu |
| Neuladen | bleiben (aus dem Speicher) | bleiben | bleiben | bleiben |
| Kurslink öffnen | bleiben | bleiben, bis „Übernehmen“ (oder Frage 2 „Prüfen“) | werden **nach Rückfrage** ersetzt; bei „Nein“ unverändert | bleiben |
| „Alle Fragen zurücksetzen“ (Reiter Versuche) | Fragen 1, 2, V1 bis V6 zurück; Startkarte bleibt | Standardwerte | bleiben | bleiben |
| „Für die nächste Gruppe zurücksetzen“ (Fuß der Seite, mit Rückfrage) | alles zurück, auch die Startkarte (P0) | Standardwerte | **bleiben** (gehören dem Kurs) | Sprache bleibt; Reiter, Vertiefung, Ansicht zurück |
| „Kurswerte löschen“ (Messblatt, mit Rückfrage) | bleiben | bleiben | gelöscht | bleiben |
| Speicher gesperrt (privates Fenster, `file:` ohne Speicher) | nur im Arbeitsspeicher | nur im Arbeitsspeicher | nur im Arbeitsspeicher | Hinweis im Kopf „Werte werden nicht gespeichert“ |

## 5 Kurslink (Konzept 9.4, M-21)

**Format, Version 1.** Alles hinter `#` der Adresse, nie an einen Server gesendet:

`#kurs1=u:21.5;m:6;d:0;b:1.2;b1:70.9,,,,,,34.1,;b2:80.4,67.8,57.0,49.2,43.1,38.2,34.6,31.2`

| Feld | Bedeutung | Prüfung |
|:--|:--|:--|
| `kurs1` | Formatkennung und Version | sonst: „Dieser Link enthält keine Kurswerte dieser Seite.“, nichts geändert |
| `u` | Raumtemperatur in °C | Zahl 5 bis 40 |
| `m` | Milchtemperatur in °C (Milch für Becher 1 und 2) | Zahl 0 bis 70 |
| `d` | mit Deckel gemessen (0 oder 1) | 0 oder 1 |
| `b` | gemessene Becher, durch Punkt getrennt (1, 2, 3) | nur 1, 2, 3; Becher 2 Pflicht |
| `b1`, `b2`, `b3` | acht Werte in °C für die Zeilen 0, 10, 20, 30, 40, 50, „60 vor der Milch“, „60 nach der Milch“; leere Stellen erlaubt | je Wert leer oder Zahl 0 bis 100 mit höchstens zwei Nachkommastellen; Becher 1 hat an Stelle 8 keinen Wert |

- **Grenzen:** höchstens 400 Zeichen hinter `#`; höchstens drei Becher, je acht Werte; Dezimalpunkt im Link (unabhängig von der Sprache).
- **Ablauf beim Öffnen:** Link prüfen. Ungültig: Hinweis mit Grund („Wert 3 von Becher 2 ist keine Temperatur zwischen 0 und 100 °C“), nichts geändert, `#…` wird aus der Adresse entfernt. Gültig: Rückfrage „Kurswerte aus dem Link übernehmen? Eure bisherigen Kurswerte werden ersetzt.“; bei Ja ersetzen und speichern, bei Nein nichts ändern. Persönliche Antworten bleiben immer.
- **Erzeugen:** „Kurswerte als Link teilen“ im Messblatt baut den Link aus der Tabelle und kopiert ihn (mit Anzeige zum Abschreiben, falls die Zwischenablage gesperrt ist).
- **Grenzen der Umgebung:** Ein Kurslink, den alle öffnen können, braucht die veröffentlichte Adresse. Ohne Netz ist der Ersatz die Offline-Datei mit Eintippen der Werte. Dass die Seite bis zum Sitzungstag nur für die TL sichtbar ist, regelt die Veröffentlichung (Konzept 9.6), nicht dieser Bau. Vor der Veröffentlichung ist der Link nur lokal getestet (`file:` und lokaler Server).

## 6 Messblatt und Übernahme (M-7)

- Zeilen fest: 0, 10, 20, 30, 40, 50, „60 vor der Milch“, „60 nach der Milch“ (min). Spalten: Becher 1 (Milch sofort), Becher 2 (Milch nach 60 min), Becher 3 (Milch bei Raumtemperatur, zuschaltbar).
- Eingabe mit höchstens zwei Nachkommastellen wie im Kurslink; mehr gilt als ungültig mit Hinweis am Feld *(X5-07, 06.11.2026)*.
- Becher 1 bekommt die Milch bei 0 min; seine Zeile „60 nach der Milch“ ist gesperrt.
- **Übernahme** („Einstellungen aus den Messwerten übernehmen“, auch beim Prüfen von Frage 2): Anfangstemperatur = Mittel von Becher 2 (und 3, falls gezeigt) bei 0 min; Messung nach 10 min = Mittel bei 10 min; *kA*-Quelle „aus der Messung“; Becher an; Zugabe 60 min; Raum- und Milchtemperatur aus dem Messblatt. Wie D116: Mittelwerte ungerundet prüfen und unverändert übernehmen oder gar nicht, mit Meldung.
- Fit (Vertiefung, M2): nur Zeilen 0 bis „60 vor der Milch“ von Becher 2 (und 3).

## 7 Abdeckungsmatrix (Teil 3.5, P13)

**Größen:** 390 × 844 (Handy hoch), 360 × 640 (kleines Handy), 844 × 390 (Handy quer), 1366 × 768 (Laptop), 1280 × 720 und 1920 × 1080 (Beamer). Dazu für den Umbruch 320 px Breite, 200 % Text und 400 % Zoom (Konzept M-14).

| Zustand | Bild je Größe (DE) | Bild EN | Test |
|:--|:--|:--|:--|
| P0 Startkarte | alle sechs Größen | 390, 1366 | Sperre: keine Ergebnisse im DOM |
| P2 Freigabe (Standardwerte) | alle sechs | 390, 1366 | Zahlen gegen Modell |
| P4 Frage 1 geprüft, Zugabe 56 min | 390, 1366 | 390 | Zahlen, Regler, Ansage |
| P6 Frage 2 mit Kurswerten (Beispielreihe aus T10, gekennzeichnet als Testdaten) | 390, 1366, 1280 | 1366 | Übernahme, Messpunkte |
| Vertiefung offen, *kA*-Voreinstellungen | 390, 1366 | 390 | Voreinstellungen, Anzeige 30 min |
| Ansicht „Wärmestrom“ mit Teilflächen | 1366 | | Teilflächen |
| Ansicht „ln“ mit Ausgleichsgerade | 1366, 390 | | T09, T10 |
| Messblatt leer, halb, voll, mit Deckel, mit Becher 3 | 390, 1366 | | Eingaben |
| Reiter Modell und So rechnet der Code offen | 1366, 390 | 1366 | Sperre vor P2 |
| Fehler: ungültige Einstellung (D116) | 390, 1366 | 390 | Ergebnisse verdeckt |
| Fehler: ungültiger Kurslink | 390 | 390 | nichts geändert |
| Fehler: Speicher gesperrt | 390 | | Hinweis, Seite nutzbar |
| Fehler: unsinnige Zahl im Feld | 390 | 390 | Meldung, Wert bleibt |
| Tastaturfokus sichtbar | 1366 | | Fokusreihenfolge |
| Handy mit Bildschirmtastatur (Zahlenfeld fokussiert) | 390 (Simulation durch kleinere Fensterhöhe) | | Anheften aus |

Layoutzustände belegen Bilder in `simulation/bildschirmfotos/`, Verhalten die reproduzierbaren Tests in `simulation/tests/`. Alle Browserprüfungen sind **Chromium-Prüfungen** (WebKit nicht verfügbar, siehe Baubericht); der Gerätenachweis auf dem iPhone steht in `simulation/ABNAHME_IPHONE.md`.
