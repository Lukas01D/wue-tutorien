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

1. Offline-Datei `simulation/site/Kaffee_Simulation.html` aus diesem Zweig (nicht die ältere, gleichnamige Datei in `ergebnisse/kaffee/fertig/` oder `ergebnisse/kaffee/simulation/`; Prüfsumme in `simulation/site/BAUNACHWEIS.txt`) auf den Laptop für den Beamer und auf einen USB-Stick legen (Ersatz bei Netzausfall). Einmal im Browser öffnen, eine Vorhersage festhalten, dann unten „Für die nächste Gruppe zurücksetzen“; nach einer Probe mit Messwerten im Messblatt „Kurswerte löschen“.
2. Am Beamer prüfen (Abschnitt 5).
3. Nach der Veröffentlichung den QR-Code der Seite in die Kurzkarte setzen (Platzhalter) und die Adresse einmal am Handy öffnen.

   **Achtung Versuchsdauer:** Das Aufgabenblatt vom 31.10. sieht den Versuch bis 40 min und *kA* ohne Becher vor; die Seite folgt deiner Entscheidung E8 (Versuch bis 60 min, Übernahme mit Becher). Vor der Sitzung entscheiden, welcher Ablauf gilt (offene Frage im Baubericht).
4. Probelauf mit zwei Studierenden am Handy: Zeit vom Öffnen bis zur gemeinsamen Erklärung stoppen (Ziel etwa 10 min, Schätzung).
5. Versuch vorbereiten: Becher 1 (Milch sofort), Becher 2 (Milch nach 60 min), gleiche Becher und Unterlage, Becher vorwärmen und die Uhr erst nach dem Temperaturausgleich starten (etwa 2 min; Konzept 9.5). Becher 3 (Milch mit Raumtemperatur) nur, wenn du ihn misst.

## 3 Ablauf der Simulationsphase (Schätzung)

Der Versuch beginnt in Minute 5 der Sitzung und endet in Minute 65 mit der Milchzugabe in Becher 2 (Versuch bis 60 min, E8). Die Simulation folgt in Minute 75 bis 90.

| Minute | Studierende (zu zweit, ein Gerät je Paar) | Du |
|:--|:--|:--|
| 65 bis 75 | Rechnung der Aufgabe | Messreihe einmal ins Messblatt der Seite eintragen (Raum- und Milchtemperatur, Becher 1 und 2, beide 60-min-Zeilen von Becher 2), „Kurswerte als Link teilen“ (auf der veröffentlichten Seite), Link als QR-Code zeigen |
| 75 | Seite über den QR-Code öffnen | einen QR-Code mit dem Kurslink zeigen (öffnet die Seite mit den Kurswerten) |
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

- Seite im Vollbild (F11), Sprache nach Kurs. „Für die nächste Gruppe zurücksetzen“ behält die gewählte Sprache.
- Browser-Vergrößerung zuerst bei 100 % lassen: Nach dem Festhalten ist der Fragetext eingeklappt („Frage zeigen“), das Diagramm passt sich der Fensterhöhe an, der Regler „Zugabe nach“ steht direkt darunter. Ist die Schrift aus der letzten Reihe zu klein, schrittweise vergrößern (110 bis 125 %) und dafür scrollen; eine eigene Projektionsansicht gibt es nicht. Im echten Hörsaal prüfen.
- Für die Besprechung: Reiter „Versuche“ unten, Karte der Frage öffnen, „Auflösung zeigen“ (erst nach einer festgehaltenen Vorhersage aktiv; für dich gibt es „ohne Vorhersage aufdecken“).

## 6 Kurslink erzeugen und teilen

1. Im Messblatt (unter dem Diagramm, von Anfang an sichtbar, ohne etwas aufzudecken) die Werte eintragen; Komma oder Punkt gehen beide. Becher 1 hat keine Zeile „60 nach der Milch“. Hast du Becher 3 gemessen, „Becher 3 zeigen“ anhaken; wurde mit Deckel gemessen, „mit Deckel gemessen“ anhaken (dann rechnet die Seite keinen zusätzlichen Deckelfaktor).
2. „Kurswerte als Link teilen“: Der Link wird kopiert und zusätzlich zum Abschreiben angezeigt. Er enthält nur die Messwerte (hinter `#`, wird nie an einen Server gesendet).
3. **Den Link auf der veröffentlichten Seite erzeugen**, nicht in der Offline-Datei: Aus der Datei entsteht nur ein Link, der auf diesem Rechner gilt (die Seite sagt das). Der Kurslink enthält die Adresse der Seite; **ein** QR-Code genügt also für Seite und Kurswerte. Einen QR-Code erzeugt die Seite nicht (K-2 nicht gebaut): mit einem QR-Werkzeug erzeugen (zum Beispiel der QR-Funktion des Browsers über „Seite teilen“ oder einer QR-App am Handy), oder den Link in den Kurs-Chat stellen (zum Abschreiben ist er mit etwa 160 Zeichen zu lang). Wer ihn öffnet, wird gefragt „Kurswerte aus dem Link übernehmen? Eure bisherigen Kurswerte werden ersetzt.“; persönliche Antworten bleiben.
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

Wortlaut wie auf der Seite (Konzept 6 mit den Entscheidungen F3 bis F12 der TL vom 06.11.2026, Konzept 12.1), Zahlen aus dem Modell; erzeugt aus `simulation/site/src/texte_de.txt`.

**Start.** *Beide Tassen stehen 60 min, die Milch kommt aus dem Kühlschrank. Dein Mitbewohner meint: „Ob man die Milch sofort oder später hineingießt, ist egal. Die Energie bleibt ja erhalten.“ Welche Tasse ist nach 60 min wärmer, und um etwa wie viel?*
Tasse 1, 3,85 K (34,05 gegen 30,19 °C). Erhalten bleibt die Energie von Kaffee, Milch und Raum zusammen; jede Tasse gibt Wärme an den Raum ab. Tasse 2 war fast bis zur Zugabe (bis etwa 56 min) heißer als Tasse 1 und hat deshalb mehr Wärme abgegeben: $Q_2 - Q_1$ = 3,69 kJ; 3,69 kJ geteilt durch 957,7 J/K (Kaffee und Milch) sind 3,85 K.

**Frage 1 Zeitpunkt.** *Wie ändert sich der Unterschied zwischen den Tassen, wenn die Milch später in Tasse 2 kommt? Bei welchem Zeitpunkt der Zugabe ist er ungefähr am größten? Nach dem Festhalten: Prüft dann: Verschiebt die Zugabe der Milch in Tasse 2. Warum wird der Unterschied bei späterer Zugabe wieder kleiner?*
Etwa nach 56 min (3,86 K; die Anzeige zeigt 3,86 K von 53 bis 59 min), genau am Schnittpunkt der Kurven. Solange der schwarze Kaffee wärmer ist als Tasse 1, gibt er mehr Wärme ab, und der Unterschied wächst; danach gibt er weniger ab. Der Unterschied geht nicht gegen null: Grenzwert 1,91 K (20 °C gegen 18,09 °C), weil die kalte Milch Tasse 2 beim Mischen erneut abkühlt. Seht euch in der Vertiefung in der Ansicht „Wärmestrom“ die Fläche zwischen den Kurven an.

**Frage 2 Versuch.** *Liegen eure Messpunkte über, unter oder auf den Kurven des Modells, oder mal so, mal so? Prüft dann: Beschreibt, wo die Punkte liegen. Nennt eine mögliche Ursache und eine Messung, mit der ihr sie prüfen könntet. Die Einstellungen werden beim Prüfen aus den Messwerten übernommen. (Ohne Kurswerte steht stattdessen: „Prüft dann: Ladet die Messwerte eures Kurses (Link der Tutoriumsleitung). Die Einstellungen werden beim Prüfen aus den Messwerten übernommen. …“)*
Hängt von eurer Messung ab. Häufig beim offenen Becher und *kA* aus den ersten 10 min: Spätere Punkte liegen über den Kurven. Mögliche Ursachen: Die Wärmeabgabe wächst stärker als linear mit $\vartheta - \vartheta_\mathrm{u}$ (Verdunstung, freie Konvektion), die Raumtemperatur stimmt nicht, Anlauf beim Eingießen (Becher nicht ganz vorgewärmt), Lage des Thermometers, ungleiche Becher. Prüfende Messungen: Becher mit Deckel, Raumtemperatur neben den Bechern, gleiche Unterlage, Messreihe in der Ansicht „ln“ (Vertiefung). Der Unterschied zwischen Becher 1 und 2 passt oft besser als die Einzelwerte.

**V1 Milchtemperatur.** *Wie warm müsste die Milch sein, damit beide Tassen nach 60 min ungefähr gleich warm sind? Notiert für euch: Hängt diese Temperatur vom Zeitpunkt der Zugabe ab?*
47,0 °C; 60,9 °C bei Zugabe nach 30 min, 37,3 °C nach 90 min. Ja, die Temperatur hängt vom Zeitpunkt ab: Bei 47,0 °C gleicht die wärmere Milch den Mehrverlust von Tasse 2 gerade aus. Je später die Zugabe, desto kälter ist Tasse 2 vorher und desto weniger warm muss die Milch sein.

**V2 Deckel.** *Mit Deckel kühlen beide Tassen langsamer ab. Wird der größte mögliche Unterschied größer, kleiner oder bleibt er gleich? Wann tritt er ein? Wähle bei *kA* „Keramik mit Deckel“ und suche wie in Frage 1 den Zeitpunkt mit dem größten Unterschied.*
Gleich groß (3,86 K), aber später: bei Zugabe nach etwa 100 min statt 56 min (Anzeige 3,86 K von 94 bis 106 min). Nach 60 min ist der Unterschied mit Deckel kleiner (3,51 K). Grund: *kA* steht nur im Produkt *kA t*; der Deckel streckt die Zeitachse. Gilt bei gleichem *kA* beider Tassen.

**V3 Becher.** *Die Tassen sind vorgewärmte Keramikbecher wie in Teil g. Wird der Unterschied größer oder kleiner? Notiert für euch: Bleibt Tasse 1 wärmer?*
Kleiner: 3,08 statt 3,85 K; die abgegebene Wärme steigt (46,60 und 50,34 kJ statt 34,88 und 38,57 kJ), weil der Becher mit abkühlt; Tasse 1 bleibt wärmer.

**V4 Versuchsplan.** *Becher 1 hat 5 % mehr *kA* als Becher 2 (andere Unterlage); oder *kA* beider Becher ist um 10 % falsch bestimmt. Was verfälscht den Unterschied mehr? Prüft mit „*kA* von Tasse 1 relativ“ (105 %) und mit dem Regler *kA* (±10 %).*
Ungleiches *kA*: Der Unterschied sinkt von 3,85 auf 2,98 K. Falsches *kA* beider Becher ändert ihn um höchstens 0,04 K. Gleiche Becher und Bedingungen zählen mehr als ein genaues *kA*.

**V5 Welcher Becher?.** *Welcher Becher hält den Kaffee am längsten warm? Notiert für euch: Ändert sich damit der größte mögliche Unterschied zwischen den Tassen? Probiere die Voreinstellungen bei *kA* aus.*
Am längsten der Thermobecher offen (Richtwert: von 80 auf 63,5 °C in 30 min statt auf 48,8 °C), dann Keramik mit Deckel. Der größte Unterschied bleibt 3,86 K, er kommt nur später (Thermobecher offen nach etwa 127 min). Nach den Richtwerten (*) sind Glas und Pappe etwa wie Keramik: Die Wand ist nicht der große Widerstand, entscheidend sind offene Oberfläche und Abstrahlung.

Nach geöffneter Auflösung von Frage 2: „Geschafft. Kernsatz: Wer heißer ist, gibt mehr Wärme ab; deshalb Milch sofort. Erhalten bleibt die Energie von Tassen und Raum zusammen. Weiter geht es in der Vertiefung.“

(V6 „Trinken“ gehört zum Kann-Punkt K-6 und ist nicht gebaut.)
