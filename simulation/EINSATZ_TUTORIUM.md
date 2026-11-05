# Einsatz der Kaffee-Simulation im Tutorium

> Für die Tutoriumsleitung (TL). Nach `BAU_AUFTRAG.md`, Teil 5.1, und `KONZEPT.md` Fassung 2 (Abschnitte 3, 6, 9). Alle Zeitangaben sind **Schätzungen**; vor dem Einsatz mit zwei Studierenden am Handy stoppen (Konzept 3). Zahlen aus dem Modell der Lösung (`kaffee_modell.py`) und seinen getesteten Erweiterungen, gerundet wie auf der Seite. Stand 05.11.2026.

## 1 Was es gibt

| Was | Wo | Wofür |
|:--|:--|:--|
| Seite (eine Datei, offline lauffähig) | `simulation/site/index.html`, bytegleich `Kaffee_Simulation.html` | Studierende am Handy, TL am Beamer |
| Kurzkarte für Studierende | `simulation/kurzkarte/Kurzkarte_DE.pdf`, `Kurzkarte_EN.pdf` | austeilen oder zeigen; QR-Code nach der Veröffentlichung eintragen |
| Abnahmeliste iPhone | `simulation/ABNAHME_IPHONE.md` | einmal vor dem Einsatz durchgehen |

**Sichtbarkeit:** Bis zum Sitzungstag nur für dich; am Sitzungstag schaltet Codex die Seite auf Zuruf öffentlich (Konzept 9.6). Die Seite verrät auch danach nichts vor der eigenen Vorhersage.

## 2 Vorbereitung

1. Offline-Datei `Kaffee_Simulation.html` auf den Laptop für den Beamer und auf einen USB-Stick legen. Einmal im Browser öffnen, eine Vorhersage festhalten, dann unten „Für die nächste Gruppe zurücksetzen“.
2. Am Beamer prüfen (Abschnitt 5).
3. Nach der Veröffentlichung den QR-Code der Seite in die Kurzkarte setzen (Platzhalter) und die Adresse einmal am Handy öffnen.
4. Probelauf mit zwei Studierenden am Handy: Zeit vom Öffnen bis zur gemeinsamen Erklärung stoppen (Ziel etwa 10 min, Schätzung).
5. Versuch vorbereiten wie in der Aufgabe: Becher 1 (Milch sofort), Becher 2 (Milch nach 60 min), gleiche Becher und Unterlage, Becher vorwärmen und die Uhr erst nach dem Temperaturausgleich starten (etwa 2 min; Konzept 9.5). Becher 3 (Milch mit Raumtemperatur) nur, wenn du ihn misst.

## 3 Ablauf der Simulationsphase (Schätzung)

Der Versuch beginnt in Minute 5 der Sitzung und endet in Minute 65 mit der Milchzugabe in Becher 2 (Versuch bis 60 min, E8). Die Simulation folgt in Minute 75 bis 90.

| Minute | Studierende (zu zweit, ein Gerät je Paar) | Du |
|:--|:--|:--|
| 65 bis 75 | Rechnung der Aufgabe | Messreihe einmal ins Messblatt der Seite eintragen (Raum- und Milchtemperatur, Becher 1 und 2, beide 60-min-Zeilen von Becher 2), „Kurswerte als Link teilen“, Link in einen QR-Code oder an die Tafel |
| 75 | Seite über den QR-Code öffnen | QR-Code der Seite und Link mit den Kurswerten zeigen |
| 75 bis 77 | **Start:** jede und jeder notiert eine Vorhersage, das Paar einigt sich und hält sie fest; Kurven und Energiesäulen erscheinen; Auftrag „Erklärt den Unterschied mit $Q_1$ und $Q_2$.“ | ein Paar erklären lassen |
| 77 bis 81 | **Frage 1 Zeitpunkt:** Vorhersage, dann mit dem einzigen Regler „Zugabe nach“ prüfen | Vorhersagen per Handzeichen abfragen; ein Paar mit abweichender Vorhersage begründen lassen |
| 81 bis 85 | **Frage 2 Versuch:** Kurswerte über den Link laden, Lage der Punkte beschreiben, eine Ursache und eine prüfende Messung nennen | zwei Paare erklären lassen |
| 85 bis 90 | Zusammenfassung | Kernsatz: „Wer heißer ist, gibt mehr Wärme ab; deshalb Milch sofort.“ |
| für Schnelle | Vertiefung V1 bis V5 | |

Zwischen zwei Gruppen am selben Gerät (zum Beispiel am Beamer-Laptop): ganz unten „Für die nächste Gruppe zurücksetzen“. Die Kurswerte bleiben dabei erhalten; Antworten, Einstellungen und Ansicht gehen zurück.

Fällt der Versuch aus, bietet Frage 2 „Frage 2 überspringen (Versuch ausgefallen)“ an. Im Pflichtweg gibt es keine erfundenen oder berechneten Ersatzdaten.

## 4 Verbindung zu Versuch und Rechnung (drei Ebenen)

| Ebene | Was die Studierenden tun | Verbindung |
|:--|:--|:--|
| Versuch | messen Becher 1 und 2 im Raum, alle 10 min | dieselben Zeilen stehen im Messblatt der Seite (0 bis 50 min, „60 vor der Milch“, „60 nach der Milch“); Frage 2 legt die Punkte auf die Modellkurven |
| Rechnung (Aufgabe) | Mischtemperatur (Teil a), *kA* aus der Messung nach 10 min (Teil c), Abkühlung, abgegebene Wärme $Q_1$, $Q_2$ (Teil e), Becher (Teil g) | die Seite rechnet dasselbe Modell wie die Lösung (`kaffee_modell.py`, unveränderter Block `MODELL`); Rechenwerte rechts zeigen die Zahlen der Rechnung (Standardwerte: 34,05 und 30,19 °C, 3,85 K) |
| Simulation | sagen voraus, prüfen, verändern einen Regler, erklären | Energiesäulen und Auflösung verbinden den Unterschied mit $Q_2 - Q_1$; Frage 1 zeigt die Wirkung des Zeitpunkts; Vertiefung variiert, was in der Rechnung fest war |

Die Übernahme der Messwerte („Einstellungen aus den Messwerten übernehmen“, auch beim Prüfen von Frage 2) setzt: Anfangstemperatur und Messwert nach 10 min als Mittel der Becher ohne Milch (Becher 2, mit Becher 3 auch dieser), *kA* aus der Messung nach 10 min, Becher an, Zugabe nach 60 min, Raum- und Milchtemperatur aus dem Messblatt. Das ist eine erklärte Vereinfachung (gleiche Startwerte, gleiches *kA* beider Tassen).

## 5 Beamer

- Seite im Vollbild (F11), Sprache nach Kurs.
- Bei 1920 × 1080 die Browser-Vergrößerung auf etwa 150 % stellen, bei 1280 × 720 auf etwa 125 %, dann passen Frageleiste und Diagramm noch gut auf den Schirm (Empfehlung aus den Bildschirmfotos, im echten Hörsaal prüfen).
- Für die Besprechung: Reiter „Versuche“ unten, Karte der Frage öffnen, „Auflösung zeigen“ (erst nach einer festgehaltenen Vorhersage aktiv; für dich gibt es „ohne Vorhersage aufdecken“).
- Diagramm groß zeigen: Bei schmalem Fenster rückt es nach oben und bleibt beim Scrollen angeheftet (Hochformat).

## 6 Kurslink erzeugen und teilen

1. Im Messblatt (unter dem Diagramm, nach der ersten Vorhersage sichtbar) die Werte eintragen; Komma oder Punkt gehen beide. Becher 1 hat keine Zeile „60 nach der Milch“.
2. „Kurswerte als Link teilen“: Der Link wird kopiert und zusätzlich zum Abschreiben angezeigt. Er enthält nur die Messwerte (hinter `#`, wird nie an einen Server gesendet).
3. Link als QR-Code zeigen oder in den Kurs-Chat stellen. Wer ihn öffnet, wird gefragt „Kurswerte aus dem Link übernehmen? Eure bisherigen Kurswerte werden ersetzt.“; persönliche Antworten bleiben.
4. Ein beschädigter Link ändert nichts und nennt den Grund in Worten.

Hinweis: Ein Link, den alle öffnen können, braucht die veröffentlichte Adresse. Vor der Veröffentlichung ist der Kurslink nur lokal getestet.

## 7 Ersatz bei Netzausfall

- Du zeigst die Offline-Datei vom Laptop am Beamer; die Paare halten ihre Vorhersage auf Papier fest, du nimmst eine Vorhersage per Handzeichen und hältst sie in der Seite fest.
- Kurswerte trägst du direkt ins Messblatt der Offline-Datei ein (kein Link nötig).
- Wer die Datei schon hat (zum Beispiel per AirDrop oder USB), kann sie offline öffnen; Werte werden dann im Browser des Geräts gespeichert, wenn er es zulässt.

## 8 Typische Fragen der Studierenden

| Frage | Antwort |
|:--|:--|
| „Die Energie bleibt doch erhalten, also müssten beide Tassen gleich warm sein?“ | Erhalten bleibt die Energie von Kaffee, Milch und Umgebung zusammen. Bis zur Zugabe gibt Tasse 2 als heißerer schwarzer Kaffee mehr Wärme an den Raum ab: $Q_2 - Q_1$ = 3,69 kJ. Geteilt durch die Wärmekapazität von Kaffee und Milch (957,7 J/K) sind das 3,85 K. |
| „Warum ist der Unterschied so klein?“ | Beide Tassen kühlen fast gleich ab; nur der Unterschied in der abgegebenen Wärme zählt (etwa 10 % der abgegebenen Wärme). |
| „Wann ist der Unterschied am größten?“ | Bei Zugabe nach etwa 56 min, am Schnittpunkt der Kurven (gleiche Temperatur, also gleiche Wärmeabgabe bei gleichem *kA*). Danach gibt der schwarze Kaffee weniger ab als Tasse 1. |
| „Geht der Unterschied bei sehr später Zugabe gegen null?“ | Nein, gegen 1,91 K: Beide sind dann auf Raumtemperatur, und die kalte Milch kühlt Tasse 2 beim Mischen auf 18,09 °C ab. |
| „Warum liegen unsere Messpunkte über der Kurve?“ | Häufig beim offenen Becher und *kA* aus den ersten 10 min: Die Wärmeabgabe wächst stärker als linear mit der Temperaturdifferenz (Verdunstung, freie Konvektion); auch Raumtemperatur, Anlauf beim Eingießen, Thermometerlage und ungleiche Becher spielen mit. Der Unterschied der Becher passt oft besser als die Einzelwerte. |
| „Was ist *kA*?“ | Wärmeübergangskoeffizient mal Fläche der Tasse; *kA* mal Temperaturdifferenz zum Raum ist der Wärmestrom. In der Aufgabe aus der Messung nach 10 min (Teil c). |
| „Was ändert der Becher?“ | Der Becher speichert Wärme mit; der Unterschied wird kleiner (3,08 statt 3,85 K), Tasse 1 bleibt wärmer (Teil g, Vertiefung V3). |
| „Werden unsere Eingaben gespeichert oder verschickt?“ | Nur im Browser des Geräts; nichts wird verschickt. Der Kurslink enthält nur die Messwerte. |
| „Wir haben ohne Vorhersage aufgedeckt, ist das schlimm?“ | Nein, die Seite merkt sich „ohne Vorhersage“; für die Erklärung zu zweit ist die eigene Vorhersage aber der Kern. |

## 9 Auflösungen der Fragen

Wortlaut wie auf der Seite (Konzept 6), Zahlen aus dem Modell.

**Start.** *Beide Tassen stehen 60 min, die Milch kommt aus dem Kühlschrank. Welche Tasse ist nach 60 min wärmer, und um etwa wie viel?*
Tasse 1, 3,85 K (34,05 gegen 30,19 °C). Tasse 2 war bis zur Zugabe heißer und hat deshalb mehr Wärme abgegeben: $Q_2 - Q_1$ = 3,69 kJ; 3,69 kJ geteilt durch 957,7 J/K (Kaffee und Milch) sind 3,85 K.

**Frage 1 Zeitpunkt.** *Bei welchem Zeitpunkt der Milchzugabe in Tasse 2 ist der Unterschied ungefähr am größten? Warum wird er bei späterer Zugabe wieder kleiner?*
Etwa nach 56 min (3,86 K; die Anzeige zeigt 3,86 K von 53 bis 59 min), genau am Schnittpunkt der Kurven. Solange der schwarze Kaffee wärmer ist als Tasse 1, gibt er mehr Wärme ab, und der Unterschied wächst; danach gibt er weniger ab. Der Unterschied geht nicht gegen null: Grenzwert 1,91 K (20 °C gegen 18,09 °C), weil die kalte Milch Tasse 2 beim Mischen erneut abkühlt.

**Frage 2 Versuch.** *Liegen eure Messpunkte über, unter oder auf den Kurven, oder mal so, mal so?*
Hängt von eurer Messung ab. Häufig beim offenen Becher und *kA* aus den ersten 10 min: Spätere Punkte liegen über den Kurven. Mögliche Ursachen: Die Wärmeabgabe wächst stärker als linear mit $\vartheta - \vartheta_\mathrm{u}$ (Verdunstung, freie Konvektion), die Raumtemperatur stimmt nicht, Anlauf beim Eingießen (Becher nicht ganz vorgewärmt), Lage des Thermometers, ungleiche Becher. Prüfende Messungen: Becher mit Deckel, Raumtemperatur neben den Bechern, gleiche Unterlage, Messreihe in der Ansicht „ln“ (Vertiefung). Der Unterschied zwischen Becher 1 und 2 passt oft besser als die Einzelwerte.

**V1 Milchtemperatur.** *Wie warm müsste die Milch sein, damit beide Tassen nach 60 min gleich warm sind?*
47,0 °C; 60,9 °C bei Zugabe nach 30 min, 37,3 °C nach 90 min.

**V2 Deckel.** *Wird der größte mögliche Unterschied mit Deckel größer, kleiner oder bleibt er gleich? Wann tritt er ein?*
Gleich groß (3,86 K), aber später: bei Zugabe nach etwa 100 min statt 56 min (Anzeige 3,86 K von 94 bis 106 min). Nach 60 min ist der Unterschied mit Deckel kleiner (3,51 K). Grund: *kA* steht nur im Produkt *kA t*; der Deckel streckt die Zeitachse. Gilt bei gleichem *kA* beider Tassen.

**V3 Becher.** *Vorgewärmte Keramikbecher wie in Teil g: Wird der Unterschied größer oder kleiner, bleibt Tasse 1 wärmer?*
Kleiner: 3,08 statt 3,85 K; die abgegebene Wärme steigt (46,60 und 50,34 kJ statt 34,88 und 38,57 kJ), weil der Becher mit abkühlt; Tasse 1 bleibt wärmer.

**V4 Versuchsplan.** *Becher 1 hat 5 % mehr kA als Becher 2, oder kA beider Becher ist um 10 % falsch bestimmt. Was verfälscht den Unterschied mehr?*
Ungleiches *kA*: Der Unterschied sinkt von 3,85 auf 2,98 K. Falsches *kA* beider Becher ändert ihn um höchstens 0,04 K. Gleiche Becher und Bedingungen zählen mehr als ein genaues *kA*.

**V5 Welcher Becher?** *Welcher Becher hält den Kaffee am längsten warm? Ändert sich der größte mögliche Unterschied?*
Am längsten der Thermobecher offen (Richtwert: von 80 auf 63,5 °C in 30 min statt auf 48,8 °C), dann Keramik mit Deckel. Der größte Unterschied bleibt 3,86 K, er kommt nur später (Thermobecher offen nach etwa 127 min). Glas und Pappe sind etwa wie Keramik: Die Wand ist nicht der große Widerstand, entscheidend sind offene Oberfläche und Abstrahlung.

(V6 „Trinken“ gehört zum Kann-Punkt K-6 und ist nicht gebaut.)
