# Unabhängige Gegenprüfung der Kaffee-Aufgabe, Rolle X

Datum: 30. Oktober 2026. Prüfstand: ursprüngliches Material des Pakets `Kaffee_Pruefpaket_2026-10-23` im Ausgangscommit `500ed24`. Dies ist die Gegenprüfung X, keine Abnahme X2.

## 1. Gesamturteil

Die Kernaufgabe ist fachlich tragfähig: Die eigene Herleitung bestätigt sämtliche Ergebniszahlen in a bis h innerhalb der angegebenen Rundung. Besonders stark sind die Bilanz über die Wärmeabgabe, die explizite Trennung von Abkühlen und Mischen sowie die Becherkorrektur mit erneuter Parameterbestimmung. Die wichtigste technische Grenze liegt in der Übertragbarkeit des gemeinsamen Verlustmodells auf den realen Versuch; die Schaumvariante könnte ihre Idealisierung deutlicher benennen. Unter den vorgegebenen Annahmen ist die Rechenfassung einsatzbereit, während die Zusage eines gut messbaren Versuchsabstandes kontrollierte Randbedingungen und eine Vorprüfung von kA braucht. Es wurde kein zwingender Korrekturbedarf an den Kernrechnungen gefunden.

### Vorgehen und Grenzen

Zuerst wurden ausschließlich Aufgabe, Formelsammlung und Bilanzierungsfolien gelesen. Die Herleitung und die Stolperstellen sind in [ERSTDURCHGANG.md](codex_skripte/ERSTDURCHGANG.md) festgehalten. [codex_eigenrechnung.py](codex_skripte/codex_eigenrechnung.py) und seine Ausgabe wurden vor Öffnen der Musterlösung und des Paketmodells erstellt. Die auf dem Aufgabenblatt bereits abgedruckten Resultate waren sichtbar; sie wurden weder als Rechenvorgaben noch als Sollwerte im Erstskript verwendet.

Danach wurden Lösung und Modell verglichen. Eine separate Sensitivitätsprüfung entstand ebenfalls ausschließlich aus der Aufgabe. Es wurden keine anderen Rollenberichte, Entscheidungen, Umsetzungsstände oder anderen Zweige gelesen. Keine Websuche; die in der Lösung genannten Literaturwerte wurden deshalb nicht extern verifiziert. Die Prüfung bestätigt Modellkonsistenz und quantifiziert Annahmen, sie ersetzt keinen Versuch mit den tatsächlich eingesetzten Bechern.

### Eigene Zahlenkontrolle

Alle Kapazitäten wurden aus Masse und spezifischer Wärmekapazität gebildet: C_K = 836,0 J/K, C_M = 121,746 J/K, C_B = 255,0 J/K. Die DGL wurde durch Trennung der Variablen gelöst. Direkte DGL-Integration einschließlich integrierter Wärmeabgabe sowie eine getrennte Quadratur bestätigen die analytische Rechnung.

| Teil | Eigene Rechnung | Vergleich mit Aufgabe und Lösung |
|:---|:---|:---|
| a | ϑ_1,0 = 70,4662 °C | 70,47 °C stimmt |
| b | C dT/dt = −kA(T − T_u), T = T_u + (T_0 − T_u) exp(−kAt/C) | Bilanz, Vorzeichen, Einheiten und Variablentrennung stimmen |
| c | kA = 0,340247765 W/K; τ_K = 40,9506 min; τ_G = 46,9141 min | 0,3402 W/K, 41,0 min und 46,9 min stimmen |
| d | Vor Milchzugabe 33,8622 °C; danach ϑ_1 = 34,0465 °C, ϑ_2 = 30,1933 °C | 34,05 °C, 30,19 °C und 3,85 K stimmen |
| e | Q_1 = 34,88085 kJ; Q_2 = 38,57123 kJ; Differenz 3,69039 kJ | 34,88 kJ und 38,57 kJ stimmen; ΔQ/C_G = 3,85320 K |
| f | kA = 0,444031473 W/K; Mischtemperatur 72,4708 °C; Endwerte 34,0436 °C und 30,9647 °C | Alle angegebenen Zahlen stimmen |
| g | Bei Zugabe jeweils 60 °C und unverändertem Modell: 35,9924 °C und 37,1847 °C | 35,99 °C und 37,18 °C stimmen unter diesen Bedingungen |
| h (1) | Milchtemperatur 47,0031 °C | 47,0 °C stimmt für dieselbe Zugabetemperatur in beiden Tassen |
| h (2) | Maximale Aufnahme aus einem Raum bei 20 °C: 1,82619 kJ; ϑ_2,max = 32,1000 °C; Restabstand 1,94644 K | 1,83 kJ, 32,10 °C und 1,95 K stimmen bei ausschließlicher Erwärmung durch den Raum |

Auch die Nebenrechnungen stimmen: anfänglich 17,1710 W und 20,4149 W, Schnitt der Abkühlkurven nach 55,7447 min, Beiträge in g von +2,4772 K und bei kalter Milch +1,3760 K beziehungsweise heißer Milch −3,6694 K. Mit unverändertem alten kA ergibt die Bechervariante tatsächlich 39,1106 °C und 36,0578 °C. Der Versuchshinweis mit Becher liefert nach 30 min 2,7068 K und nach 60 min 3,0788 K Abstand; für die dritte Tasse bei Zugabe von 20 °C warmer Milch bleiben 1,5730 K.

Das in den Hinweisen verwendete Potenzgesetz mit Exponent 4/3 wurde separat exakt integriert und an dieselbe Messung angepasst: 37,6533 °C und 33,3406 °C, Differenz 4,3127 K. Es bestätigt die gedruckten Zahlen, ist jedoch keine eigenständige Modellierung realer Verdunstung. Der kopierte Paketlauf reproduziert seine mitgelieferte Textausgabe exakt.

### Dokumente und Abbildungen

Alle drei Seiten der Aufgaben-PDF und alle neun Seiten der Lösungs-PDF wurden als Bilder gerendert und vollständig visuell geprüft. Zusätzlich wurden Abb. 1, L1 und L2 in Originalauflösung angesehen. Keine fehlenden Abbildungen, kaputten Formeln, abgeschnittenen Tabellen oder sichtbaren Widersprüche zwischen Zahlen und Grafiken gefunden. Die ersten drei Lösungsseiten stimmen mit der Aufgaben-PDF überein. Abb. L1 zeigt einen geschlossenen Bilanzraum mit nach außen gerichteter Wärmeabgabe; Abb. L2 stellt Abkühlung und Mischsprünge plausibel dar. Word-Dateien gehören nicht zum hier freigegebenen Lesematerial und wurden nicht geprüft.

## 2. Änderungsvorschläge

Nach Wichtigkeit geordnet. Die Vorschläge ändern keine der als korrekt bestätigten Kernzahlen.

### Codex 1: Gleiches kA als entscheidende, experimentell ungeprüfte Annahme kennzeichnen

- Ebene: technisch
- Stelle: Annahmen, Aufgabe Zeile 29; Versuch, Schritte 3 bis 4; Lösung c, Zeile 139, und Hinweis „Was die Rechnung weglässt“, Zeile 209
- Befund: Ein Messpunkt bestimmt bei vorgegebener Wärmekapazität genau einen effektiven Leitwert. Er bestätigt weder konstantes kA über eine Stunde noch dasselbe kA für 200 ml schwarzen Kaffee und 230 ml Milchkaffee. Unterschiedliche Füllhöhen verändern die benetzte Wandfläche; bei nicht zylindrischen Tassen kann sich auch die freie Oberfläche ändern. Zusammensetzung und Oberflächenzustand können die Verdunstung verändern. Eine gemeinsame temperaturabhängige Verlustfunktion untersucht diese Unterschiede nicht.
- Vorschlag: Lösungshinweis ergänzen: „Die Messung kalibriert das angenommene Modell. Ob der Leitwert auch für den Milchkaffee gilt, muss gesondert geprüft werden.“ Für die Versuchsvorbereitung eine eigene Abkühlreihe mit bereits gemischtem Milchkaffee und weitere Messpunkte vorsehen, beispielsweise bei 20 und 40 min. Die Übereinstimmung einer Zeitkonstante mit einem Literaturversuch nur als Größenordnungseinordnung bezeichnen.
- Begründung: Die unabhängige Sensitivität ergibt ohne Becher Gleichstand bei (kA)_1/(kA)_2 = 1,25071, mit Becher bereits bei 1,18776. Bei 15 % höherem kA für Milchkaffee sinkt der Becherabstand von 3,0788 K auf 0,5595 K; bei 20 % kehrt er sich rechnerisch zu −0,1755 K um. Das ist eine quantifizierte Modellgrenze, kein Nachweis einer tatsächlich so großen Abweichung. Dagegen drehen die geprüften gemeinsamen temperaturabhängigen Verlustgesetze die Richtung nicht um. Details und Annahmen: `codex_sensitivitaet.py`.
- Priorität: sollte. Aufwand: mittel für die Vorprüfung, klein für den Hinweis
- Folgen: Die Rechenaufgabe und ihre Zahlen bleiben erhalten. Versuchsvorhersagen werden als Modellwerte ausgewiesen und anhand der tatsächlichen Becher eingeordnet.

### Codex 2: Messprotokoll und quantitative Versuchsvorhersage vervollständigen

- Ebene: praktisch (Durchführung)
- Stelle: Aufgabe, Materialliste und Versuchsschritte 2 bis 5, Zeilen 77 bis 83; Lösung, Hinweis „Versuch“, Zeile 211
- Befund: Drei gleiche Becher, Starttemperaturmessung und ein gemeinsames Thermometer sind sinnvoll. Auf dem Aufgabenblatt fehlen jedoch die in der Lösung verlangte Durchmischung vor jeder Messung sowie Angaben zu realen Bechermassen, Umgebung, Milchmenge, Zeitversatz und Deckelbedingungen. Aus „Küchenthermometer“ allein folgt keine bekannte Differenzmessunsicherheit. Schritt 4 setzt für die Milch im Glas bereits Raumtemperatur voraus, obwohl das Protokoll ihre Temperatur erst später misst.
- Vorschlag: Leere Becher wiegen, die Milchportionen abwiegen und die Raumtemperatur messen. Vorwärmen, Abtropfen und Stellfläche vereinheitlichen; alle Becher offen oder mit identischen Deckelbedingungen betreiben und Zugluft vermeiden. Vor jeder Messung gleichartig rühren, gleiche Eintauchtiefe verwenden, eine stabile Anzeige abwarten und die tatsächlichen Zeitpunkte dokumentieren. Für Becher 3 zunächst die Rechnung mit Raumtemperatur ausdrücklich als obere Grenze verwenden und nach der Milchmessung aktualisieren. Einmalige Vorprüfung mit denselben Bechern und dem Thermometer; Messauflösung und Wiederholstreuung protokollieren.
- Begründung: ±1 K ausschließlich beim 10-min-Kalibrierwert ergibt mit Becher 3,0493 bis 3,0898 K Abstand, verändert die einzelnen Endtemperaturen aber von etwa 32,50/29,46 °C bis 35,73/32,64 °C. Ein gemeinsamer konstanter Thermometeroffset hebt sich im direkten Temperaturvergleich auf, unterschiedliche Messbedingungen nicht. Tasse 1 kühlt am Schluss im Modell mit rund 0,31 K/min weiter ab; Zeitversatz ist daher zu dokumentieren. Mit 15 ml statt 30 ml Milch sinkt das nominelle Bechersignal auf 1,6518 K. Die in f genutzten 300 g und 850 J/(kg K) sind Arbeitswerte und müssen für andere Gefäße als Schätzung kenntlich bleiben.
- Priorität: sollte. Aufwand: klein bis mittel
- Folgen: Materialliste und Versuchstabelle erhalten Felder für Masse, Umgebung, Milchtemperatur und Uhrzeit. Keine Änderung der theoretischen Musterwerte; ihre direkte Übernahme als garantierte Messwerte entfällt.

### Codex 3: Idealisierung der Schaumvariante ausdrücklich benennen

- Ebene: technisch
- Stelle: Aufgabe g, Zeilen 69 bis 70; Lösung g, Zeilen 178 bis 186, und Hinweis „Fehlvorstellungen“, Zeile 208
- Befund: Die Rechnung ist unter den vorhandenen Vorgaben konsistent: g nennt 60 °C für beide Zugaben, die allgemeinen Annahmen setzen ideales Mischen und gemeinsames kA voraus. Der Begriff „Milchschaum“ kann aber zusätzlich eine isolierende Deckschicht oder eine während der Wartezeit abkühlende Schaumportion nahelegen. Beides bildet die Rechnung nicht ab. „Gleiche Masse“ sollte ausdrücklich die ursprüngliche Milchmasse bezeichnen; gleiches Schaumvolumen wäre keine gleichwertige Vorgabe.
- Vorschlag: Als Klarstellung ergänzen: „Die flüssige Milchmasse beträgt je 30,9 g; die Wärmekapazität der eingeschlossenen Luft wird vernachlässigt. Der Schaum hat bei jeder Zugabe 60 °C und wird vollständig untergemischt. Eine isolierende Schaumschicht wird nicht betrachtet; kA bleibt unverändert.“ Frische Herstellung oder geeignetes Warmhalten kann die angenommene Zugabetemperatur sicherstellen.
- Begründung: Bei sofortiger Zugabe von 60 °C warmer Milch muss die späte Portion mindestens 50,6206 °C haben, damit die zweite Tasse gleich warm bleibt. Kühlt sie bis 20 °C ab, endet Tasse 2 bei 32,1000 °C statt 37,1847 °C und ist gegenüber Tasse 1 mit 35,9924 °C wieder kühler. Der Wert 47,0 °C aus h gilt für gleiche Zugabetemperaturen beider Portionen und ersetzt diese Bedingung nicht. Eigene Rechnung: `codex_zusatzpruefung.py`.
- Priorität: sollte, zur Verdeutlichung des bereits vorausgesetzten idealisierten Modells. Aufwand: klein
- Folgen: Bei vorgeschlagener Definition bleiben Zahlen und Abbildungen unverändert. Bei einer echten isolierenden Schaumschicht oder einer gemeinsam bereitgestellten, abkühlenden Schaummenge wären zusätzliche Daten und ein neues Modell nötig.

### Codex 4: Die obere Schranke in h (2) auf ihre Wärmequelle beschränken

- Ebene: technisch
- Stelle: Aufgabe h (2), Zeile 72; Lösung h (2), Zeilen 193 bis 199; Versuchsschritt 2
- Befund: Die Rechnung mit maximal 1,83 kJ aus der Raumluft ist korrekt. „Neben die Tasse“ garantiert aber keine ausschließliche Erwärmung durch einen Raum bei 20 °C: Wärmestrahlung des heißen Bechers, direkter Kontakt oder eine warme Stellfläche sind zusätzliche Wärmequellen. Dann ist 20 °C keine allgemeine obere Schranke mehr.
- Vorschlag: Ergänzen: „Die Milch wird ausschließlich durch die Umgebung bei 20 °C erwärmt; Wärmeübertragung vom heißen Becher und anderen Wärmequellen wird vernachlässigt.“ Im Versuch das Milchglas mit Abstand zu den heißen Bechern auf derselben raumtemperierten Unterlage abstellen. Die vorhandene Energiebilanz und die Unterscheidung vom Kipppunkt in h (1) beibehalten.
- Begründung: Bei festgehaltenem Kaffee-Abkühlverlauf müsste nur die späte Milchportion auf 35,3122 °C erwärmt werden, damit Tasse 2 zur ursprünglichen Tasse 1 mit 34,0465 °C aufschließt. Die 47,0 °C gelten dagegen für beide Portionen mit derselben Temperatur. Ob zusätzliche reale Wärmequellen den niedrigeren Wert erreichen, ist mit den vorliegenden Daten offen; bei einer Kopplung zum Kaffee müsste auch dessen Wärmeverlust neu bilanziert werden. Der Bericht behauptet deshalb keine reale Umkehr. `codex_eigenrechnung.py`, Ausgabe h2.
- Priorität: sollte. Aufwand: klein
- Folgen: Keine neuen Zahlen oder Abbildungen. Der Gültigkeitsbereich der bereits richtigen Abschätzung wird ausdrücklich genannt.

### Codex 5: Flüssigkeit und Becher als idealisierte gemeinsame Speicherkapazität erklären

- Ebene: technisch
- Stelle: Annahmen, Aufgabe Zeile 27; Aufgabe f, Zeile 66; Lösung b und f, Zeilen 125 bis 134 und 165 bis 176
- Befund: Ideale Durchmischung und ein Becher, der immer die Inhaltstemperatur hat, sind zulässige Aufgabenannahmen. Sie sind aber nicht allein durch die gefundene Abkühlkonstante belegt. Für eine quantitative Biot-Prüfung fehlen Abmessungen, Wärmeleitfähigkeiten und Angaben zu innerem Wärmeübergang beziehungsweise Zirkulation. Das globale Produkt kA kann nicht unmittelbar als lokaler Wärmeübergangskoeffizient eingesetzt werden. Beim realen Eingießen und Milchzugeben braucht auch der Temperaturausgleich zwischen Keramik und Flüssigkeit Zeit.
- Vorschlag: In den Lösungshinweisen ergänzen: „Das Ein-Körper-Modell setzt hinreichend schnellen Temperaturausgleich gegenüber der Abkühlung voraus. In f werden Kaffee und vorgewärmter Becher als gemeinsame Speicherkapazität behandelt, auch beim Mischvorgang. Der Versuch nähert dies durch Vorwärmen und gleichartiges Durchmischen an; räumliche und zeitliche Temperaturunterschiede bleiben Modellabweichungen.“ Keine zusätzliche Pflichtrechnung zur Biot-Zahl verlangen, solange Geometrie und Stoffdaten fehlen.
- Begründung: C_B/C_K = 30,50 % ist groß genug, um beim Mischen berücksichtigt werden zu müssen. Genau das tut die Musterlösung richtig. Die Bilanzierungsfolien 6 bis 10 verlangen einen klaren Bilanzraum; Folie 20 betont die vereinfachenden Annahmen sowie Anfangs- und Randbedingungen. Die Parameteridentifikation ersetzt diese Begründung nicht.
- Priorität: sollte. Aufwand: klein
- Folgen: Keine Änderung der korrekten Becherrechnung. Ein genaueres Zwei-Körper-Modell bleibt außerhalb des notwendigen Tutoriumsumfangs.

### Codex 6: Numerischen Zusatzlauf eindeutig zuordnen und seine Genauigkeit dokumentieren

- Ebene: technisch
- Stelle: `C_modell/nachrechnung_kaffee.py`, Ausgabeüberschrift „f) nichtlineare Wärmeabgabe“; `kaffee_modell.py`, Funktion `nichtlinear`
- Befund: Teil f der Aufgabe ist die Becherkorrektur. Die Ausgabebezeichnung ordnet ihm stattdessen das nichtlineare Zusatzmodell zu. Dieses wird mit explizitem Euler-Verfahren und festem Schritt von einer Sekunde berechnet; eine Genauigkeitsangabe fehlt. Das ist für die dokumentierten 4/3-Zahlen unkritisch, erklärt aber eine Rundungsabweichung beim zusätzlichen Exponenten 1,6.
- Vorschlag: Überschrift „Zusatzprüfung: temperaturabhängige Wärmeabgabe“ verwenden. Das reine Potenzgesetz analytisch integrieren oder eine Schrittweitenkontrolle beziehungsweise einen adaptiven Integrator einsetzen. Den Zusatz als Formtest bei unveränderter Masse und gemeinsamem Verlustgesetz kennzeichnen.
- Begründung: Die exakte Lösung liefert bei n = 1,6 für Tasse 1 39,95443 °C, also 39,95 °C auf zwei Stellen; die Paket-Ausgabe nennt 39,96 °C. Bei n = 4/3 bleiben die gedruckten 37,65 °C und 33,34 °C unverändert richtig. Der Nachweis steht in `codex_zusatzpruefung.py`; die DGL wurde zusätzlich direkt integriert.
- Priorität: kann. Aufwand: klein
- Folgen: Nur Überschrift und Implementierung des Zusatzlaufs; keine Kernzahlen der Aufgabe betroffen.

## 3. Was bleiben sollte

- Die Bilanz und die Lösung durch Trennung der Variablen. Sie sind fachlich sauber und entsprechen dem Prüfauftrag.
- Die Gewichtung mit m c_p statt mit dem Volumen und die getrennten Schritte für Tasse 2.
- Die Kontrolle (Q_2 − Q_1)/C_G = ϑ_1 − ϑ_2. Sie beantwortet das Energieerhaltungsargument unmittelbar.
- Die erneute Bestimmung von kA in f aus derselben Messung. Der Hinweis auf das unpassende Weiterverwenden des alten kA ist korrekt und hilfreich.
- Die Unterscheidung zwischen gleich temperierter Milch in h (1) und ausschließlich später erwärmter Milch in h (2). Die vorhandene Lösung erkennt diesen Unterschied ausdrücklich.
- Der Versuch als Vergleich von Vorhersage und Messung, einschließlich dritter Tasse und gemeinsamem Thermometer. Abweichungen sollten zum Prüfen der Annahmen verwendet werden.
- Die drei Abbildungen. Technisch ist keine Neuzeichnung nötig.

## 4. Offene Fragen an die Tutoriumsleitung

1. Soll g eine Temperaturvariation im gleichen Mischmodell sein oder tatsächlich die isolierende Wirkung einer Schaumschicht behandeln? Für Letzteres reichen die vorgegebenen Daten nicht aus.
2. Welche Becher und welches Thermometer stehen tatsächlich zur Verfügung? Gibt es bereits eine Abkühlreihe mit Milchkaffee zur Prüfung von Codex 1?
3. Soll der Versuch vorrangig die qualitative Reihenfolge zeigen oder auch die Endtemperaturen quantitativ bestätigen? Davon hängt der nötige Aufwand der Vorprüfung ab.

### Reproduzierbare Unterlagen

Eigene Skripte, Ausgaben und Erstprotokoll liegen in [codex_skripte](codex_skripte/README.md). Die Bilddateien der PDF-Prüfung sowie Kopien des gelieferten Modells sind lokale Arbeitsartefakte; die beigefügten Hilfsskripte erzeugen sie erneut. Am Prüfpaket wurde nichts geändert.
