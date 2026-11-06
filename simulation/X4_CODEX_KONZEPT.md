# X4: Unabhängige Prüfung des Simulationskonzepts

Stand: 04.11.2026. Rolle X4 nach `AGENTS.md`. Prüfgrundlage: Zweig `claude/simulation-tool-kaffee-4kcacl`, Commit `6ccb792a8c000a1b4a0e4096be9fce8ae6bbbfd3`. Berichtszweig: `codex/x4-simulation-konzept`.

## Urteil: mit Änderungen

Das Konzept ist grundsätzlich tragfähig. Die Verbindung von Vorhersage, eigener Variation, Energiebilanz und Messdaten passt zum Tutorium. Die Standardrechnung, der Bechereinfluss, die Deckelskalierung innerhalb des vereinfachten Modells und die Fortsetzung nach der Milchzugabe stimmen. Die wesentlichen didaktischen Quellen tragen die vorgeschlagenen Prinzipien mit den im Konzept überwiegend richtig genannten Übertragungsgrenzen.

Als unveränderte Bauvorgabe empfehle ich das Konzept noch nicht. Mehrere allgemeine Erklärungen gelten nur für den Standardfall, obwohl die Oberfläche weitere Fälle zulässt. Besonders wichtig sind die Energiebilanz bei unterschiedlicher Milchtemperatur, die Aussage zum Abklingen bei ungleichem kA und die Interpretation der Messreihe. Außerdem fehlen verbindliche Regeln für Messzeitpunkt, Kalibrierung und Freischaltung. Der Ablauf in 10 bis 15 Minuten ist eine plausible Planung, noch kein nachgewiesenes Ergebnis.

Empfehlung an die TL: Grundrichtung und eigene Website beibehalten. Vor dem Bau Konzept 1 bis 7 entscheiden und einarbeiten lassen; Konzept 8 bis 11 in die Bauvorgabe übernehmen. Keine Änderung an Konzept, Aufgabe oder Lösung wurde vorgenommen.

## Umfang und Nachweise

Gelesen: `AGENTS.md`, Simulationsauftrag, vollständiges Konzept, die Rechercheberichte R1 bis R3 sowie Aufgabe und die für Modell und Literatur einschlägigen Stellen der Lösung und des Referenzmodells auf diesem Zweig. Keine anderen Zweige oder anderen Rollenberichte für die Urteilsbildung herangezogen. Die ältere X3-Abnahme wurde nicht wiederholt.

Die eigene Rechnung entstand aus Mischbilanz und globaler Energiebilanz, ohne Import von `kaffee_modell.py`, Code der Simulation oder Recherche-Skripten. Nachweise:

- [Eigene Rechnung](x4_skripte/nachrechnung.py), [reproduzierbare Ausgabe](x4_skripte/nachrechnung_ausgabe.json): Standardfälle, Becher, Deckel, Milchtemperatur, ungleiche Bedingungen, spätere Vergleichszeit, nichtlineare Abgabe, Messreihenfit und 10 000 simulierte Messreihen.
- Zusätzlich Integration der Differentialgleichungen mit Runge-Kutta an zwölf eigenen Parametersätzen. Größte Abweichung zur geschlossenen eigenen Rechnung: `4,57e-13 K`. Das kontrolliert die Rechnung, belegt keine Realitätsnähe des Modells.
- [Quellenprüfung](x4_skripte/QUELLENPRUEFUNG.md): jede nummerierte Angabe aus R1 und R2, Quellenliste R3 und zusätzliche Literatur aus Anhang A.4 erfasst. Eigener Abrufstatus und Tragweite sind getrennt von Claudes damaligem Prüfstatus dokumentiert. Nicht zugängliche Originalstellen sind ausdrücklich offen.
- Drei vorhandene Skizzen als Bilder angesehen, darunter Laptop mit 1366 px und Handy mit 390 px. [Browser-Sichtung](x4_skripte/skizzen_pruefen.js), [Ausgabe](x4_skripte/skizzen_befund.json): statische Zeichenflächen, null echte Bedienelemente, keine fremden Anfragen. Die verwaltete Browserrichtlinie sperrt `file:`-Navigation; dieselbe unveränderte Skizzen-Datei wurde deshalb über `setContent` geladen. Das ist kein Nachweis für die spätere Offline-Datei.

### Bestätigte Zahlen

Alle Temperaturen in °C, Unterschiede in K, Wärmen in kJ. Aus ungerundeten Aufgabenwerten gerechnet.

| Fall | Tasse 1 | Tasse 2 nach Milch | Unterschied | Weitere Kontrolle |
|:--|--:|--:|--:|:--|
| Standard, Zugabe 60 min | 34,04648 | 30,19328 | 3,85320 | kA 0,340247765 W/K; Mischung 70,46621 °C; Q1 34,88085; Q2 38,57123 |
| Keramik, Zugabe 60 min | 34,04356 | 30,96472 | 3,07883 | kA 0,444031473 W/K; Q1 46,60254; Q2 50,33638 |
| Keramik, Zugabe 40 min | 41,79168 | 38,81739 | 2,97429 | Versuchsvorgabe im Konzept |
| Deckelfaktor 0,56, ohne Becher | 44,65802 | 41,14838 | 3,50963 | kA 0,190538748 W/K |
| Deckelfaktor 0,56, Keramik | 45,08136 | 42,25528 | 2,82608 | kA 0,248657625 W/K |
| Zugabe 60, Vergleich 90 min | 27,41056 | 25,37771 | 2,03285 | gleiche kA |
| Zugabe 60, Vergleich 120 min | 23,90962 | 22,83714 | 1,07248 | gleiche kA |
| kA von Tasse 1 um 5 % größer | 33,17637 | 30,19328 | 2,98309 | übrige Standardwerte |

Der größte **signierte** Unterschied beim Variieren des Zugabezeitpunkts beträgt ohne Becher 3,8618379 K bei 55,7446689 min. Die Kurven treffen sich vor dem Mischen bei 35,38013 °C. Der Deckelfaktor verschiebt diesen Zeitpunkt auf 99,54405 min. Mit Keramik: 3,0898450 K bei 54,69669 min und 35,77881 °C. Für gleich warme Tassen nach 60 min braucht die Milch 47,00309 °C; bei 30 bzw. 90 min sind es 60,91227 bzw. 37,28450 °C. M6 mit n = 1,25 ergibt unabhängig nachgerechnet 36,84 bzw. 32,63 °C, also rund 4,21 K.

## Befunde nach Wichtigkeit

### Konzept 1: Energiedarstellung benötigt eine eindeutige Größe und eine vorzeichenrichtige Fläche

**Wichtigkeit: hoch, vor dem Bau klären. Stelle:** M-20, S-1, Abschnitt 8.2 M3, Anhang A.2, besonders Zeile 339.

Abschnitt 8.2 spezifiziert einen Wärmestrom über der Zeit, mit einer Fläche als Energiedifferenz. A.2 nennt dieselbe Ansicht dagegen abgegebene Wärme über der Zeit und die Lücke am Endpunkt als Energiedifferenz. Das sind unterschiedliche Diagramme: Bei Q in kJ ist die vertikale Differenz eine Energie; bei Qdot in W ergibt erst das Zeitintegral eine Energie.

Zusätzlich wechselt Qdot2 minus Qdot1 am Schnittpunkt sein Vorzeichen. Schon bei 60 min liegt der Zugabezeitpunkt rechts davon. Eine durchgehend positiv gezählte Fläche zwischen den Kurven wäre deshalb falsch. Bei warmer Milch oder geänderten kA können auch die Energiedifferenz und die Richtung der Wärmeabgabe wechseln.

**Vorschlag:** Eine Darstellung verbindlich festlegen, etwa Wärmestrom Qdot in W über t in min, mit beiden Teilflächen vor und nach dem Schnitt unterschiedlich schraffiert. Beschriftung: `Q2 - Q1 = Integral(Qdot2 - Qdot1) dt`. Die Integration rechnet Sekunden oder berücksichtigt ausdrücklich den Faktor 60. Die Säulen zeigen weiterhin Q in kJ. Testfälle: Zugabe vor, am und nach dem Schnitt, negative Differenz und gegebenenfalls Wärmeaufnahme aus dem Raum. Den Bilanzpfeil am Mischsprung als linksseitigen Wert unmittelbar vor der Zugabe kennzeichnen.

### Konzept 2: Die Energieerklärung ist bei Milch für Tasse 2 auf Raumtemperatur falsch

**Wichtigkeit: hoch, vor dem Bau ergänzen. Stelle:** Lernziel 1, M-20, Abschnitt 8.2 M3, Anhang A.2 und A.8; Schalter in Abschnitt 5.1 und A.4.

Die Gleichung `Q2 - Q1 = C_GB (theta1 - theta2)` setzt gleiche Anfangsenergie einschließlich Milch voraus. Der vorgesehene Schalter für Milch von Tasse 2 bei Raumtemperatur verletzt diese Voraussetzung. Mit Standardwerten und Milch2 = 20 °C bleiben Q1 und Q2 bis zur Zugabe unverändert. Tasse 2 erreicht aber 32,10004 °C; der Unterschied ist 1,94644 K. Die bisherige Energieerklärung würde weiterhin 3,85320 K behaupten.

Für unterschiedliche Milchtemperaturen gilt direkt nach der Zugabe:

`C_GB * (theta1 - theta2) = Q2 - Q1 + C_M * (theta_M1 - theta_M2)`.

**Vorschlag:** Den zusätzlichen Energiebeitrag der Milch sichtbar ausweisen oder die einfache Erklärung ausdrücklich auf gleiche Milchtemperaturen beschränken. Für Becher3 entweder eine eigene berechnete Kurve festlegen oder klar zwischen dem Vergleich mit Becher2 und Becher3 umschalten. Die Kennzahlen müssen benennen, welches Paar gerade verglichen wird. Den obigen Zahlenfall als Pflichtprüfung ergänzen.

### Konzept 3: Gemeinsames exponentielles Abklingen und Maximum am Temperaturschnitt gelten bei ungleichem kA nicht

**Wichtigkeit: hoch, vor dem Bau ergänzen. Stelle:** Abschnitt 8.1 letzter Absatz, 8.2 M4, Anhang A.2, A.8; Regler kA von Tasse 1 relativ.

Die Einzelgleichungen von M4 enthalten die Faktoren f1 und f2 richtig. Der anschließende allgemeine Satz zum exponentiellen Abklingen der Differenz stimmt aber nur für f1 = f2. Mit f1 = 1,05 beträgt die Differenz bei Zugabe nach 60 min 2,98309 K und bei Vergleich nach 90 min 1,35506 K. Ein gemeinsamer Abklingfaktor ergäbe fälschlich rund 1,574 K. Die Tassen können später sogar ihre Reihenfolge tauschen.

Beim Variieren des Zugabezeitpunkts gilt allgemein:

`d(delta theta)/dt_Z = (kA2 * (theta_2K - theta_u) - kA1 * (theta1 - theta_u)) / C_GB`.

Das Extremum liegt bei gleichen **Wärmeströmen**, bei ungleichen kA also nicht am Temperaturschnitt. Abschnitt 8.1 nennt die Einschränkung zwar bereits, A.2 und A.8 übernehmen sie nicht. Auch das gemeinsame C beim späteren Mischen ist mit Becher C_GB, nicht nur die Kapazität der Flüssigkeit.

**Vorschlag:** Erklärtexte dynamisch an die Bedingungen binden. Die Aussage zum Temperaturschnitt und zum einfachen Abklingen nur bei gleichen kA verwenden; sonst die Wärmestrombedingung und die Differenz zweier Exponentialfunktionen erklären. Fragen 1 bis 3 starten mit f1 = 1 und fest benannten übrigen Parametern. Den Vergleichszeitpunkt zunächst an den Zugabezeitpunkt koppeln; erst eine ausdrückliche spätere Vergleichswahl löst diese Kopplung. Andernfalls beantwortet das Verschieben von t_Z eine andere Frage als Frage 1.

### Konzept 4: Der Messreihenfit liefert einen Arbeitswert, aber die angegebene Unsicherheit ist nicht allgemein eine Messunsicherheit

**Wichtigkeit: hoch, vor dem Bau entscheiden. Stelle:** M-21, Abschnitt 8.2 M2, R3 Abschnitt 5, Anhang A.8.

Die logarithmische Ursprungsregression und die Rückübersetzung in einen gleichwertigen 10-min-Messwert sind algebraisch richtig. T10 ergibt 0,3422834 W/K und formal 0,0013328 W/K Standardfehler. Die gekrümmte Reihe bis 40 min ergibt 0,3187081 W/K und einen gleichwertigen Messwert von 67,73222 °C, wie angegeben.

Der Nenner aller logarithmierten Werte enthält aber dieselbe fehlerbehaftete Startmessung. Dadurch sind die Fehler korreliert; bei gleich großen Temperaturfehlern wächst außerdem die Unsicherheit der logarithmierten Werte beim Abkühlen. Die Formel `C*s/sqrt(sum(t_i^2))` behandelt diese Fehlerstruktur nicht. In meiner Kontrolle mit 10 000 ideal exponentiellen Reihen und unabhängigen Temperaturfehlern gleichverteilt zwischen minus und plus 0,3 K beträgt die tatsächliche Streuung des Fits 0,0017553 W/K, sein mittlerer formaler Standardfehler nur 0,0010638 W/K. Kleine Reste schließen einen systematischen Fehler von Start- oder Raumtemperatur ebenfalls nicht aus.

**Vorschlag:** Für die Grundfassung kA als Anpassungswert ohne scheinbar vollständige Plusminus-Messunsicherheit anzeigen. Alternativ ein explizites Fehlermodell mit Fortpflanzung der Start- und Raumtemperaturfehler einführen und unabhängig testen. Bei einem formalen Regressionsfehler müssen Name, Voraussetzung, Freiheitsgrade und Abgrenzung zur Messunsicherheit dabeistehen. Fitbereich und Zahl der einbezogenen Punkte anzeigen. Der gleichwertige 10-min-Wert darf den tatsächlich gemessenen 10-min-Wert nicht überschreiben oder als Messung ausgegeben werden.

### Konzept 5: Für Fit, Messkurven und Teilen fehlt ein eindeutiges Versuchsprotokoll

**Wichtigkeit: hoch, vor dem Bau ergänzen. Stelle:** Abschnitte 5.1, 8.2 M1/M2/M4, 9.4 und 9.5, A.6/A.7.

Die Tabelle hat bei 40 min nur eine Zeile. Im Versuch erfolgt dort die Milchzugabe mit einem Temperatursprung. Ohne Kennzeichnung ist unklar, ob der Eintrag davor oder danach gemessen wurde. Die erste Variante darf in den Schwarzkaffeefit, die zweite nicht. Ein Zeitpunkt allein reicht dafür nicht. Ebenso benötigen Becher2 und Becher3 gegebenenfalls eigene Startwerte. Die Beispielskizze hat bereits 80,5 und 80,0 °C. Ein gemeinsamer Nenner ohne Festlegung würde diese Unterschiede in kA umdeuten.

Deckel, Becherwärmekapazität und Füllmenge gehören zur Kalibrierung. Bei Import wird der Deckelschalter laut M1 pauschal ausgeschaltet. Das verhindert eine doppelte Multiplikation, benennt eine Messung mit Deckel aber anschließend als offenen Fall. Ein erneutes Einschalten würde denselben Deckeleffekt nochmals aufprägen. Das Linkbeispiel in 9.4 transportiert diese Versuchsbedingungen nicht.

**Vorschlag:** Einträge bei der Zugabe mit Phase vor/nach Milch kennzeichnen, gegebenenfalls zwei Zeilen bei gleicher Zeit erlauben. Pro Becher Startwert, Milchtemperatur und Zugabezeit festhalten; gleiche Startwerte und gleiche kA dürfen eine erklärte Modellvereinfachung sein. Fits pro Becher oder klar definiert gemeinsam berechnen. Links müssen neben Temperaturen auch die dafür nötigen Versuchsbedingungen und eine Formatversion enthalten. Messkonfiguration und hypothetische Deckelvariation getrennt benennen. Tests mit Lücken, verschiedenen Startwerten, Messung mit Deckel sowie beiden 40-min-Phasen vorgeben.

### Konzept 6: Frage 4 legt die Deutung der Messung vorab fest

**Wichtigkeit: hoch, vor dem Einsatz umformulieren. Stelle:** Abschnitt 6, Erwartung und Text von Frage 4; M2-Hinweis auf bogenförmige Reste.

Die Antwort erwartet einige Kelvin zu hohe Messpunkte und nennt überlineare Abgabe als Ursache. Das kann beim offenen Becher und einer Kalibrierung aus den ersten zehn Minuten passieren. Es ist keine allgemeine Vorhersage für die noch ausstehende Messung der TL. Bei einem über die ganze Reihe angepassten kA können die Punkte auf beiden Seiten liegen. Mit Deckel kann das lineare Modell gut passen. Eine gekrümmte logarithmische Reihe ist mit veränderlichem kA vereinbar, beweist aber weder Verdunstung noch eine bestimmte andere Ursache; etwa eine falsche Raumtemperatur oder ein Anlauf kann ebenfalls Abweichungen erzeugen.

Das widerspricht gerade dem begründenden Ziel von Holmes et al.: Messdaten sollen Modelle prüfen, ohne auf ein vorgegebenes Ergebnis gebracht zu werden. [Holmes und Wieman 2018, Abschnitt Thinking like a physicist](https://physicstoday.aip.org/features/introductory-physics-labs-we-can-do-better) ist hierfür ein passender Gegenbeleg.

**Vorschlag:** Antwortoptionen oberhalb, unterhalb, wechselnd und innerhalb der Unsicherheit passend anbieten. Erst beschreiben, dann zwei mögliche Erklärungen und eine unterscheidende weitere Messung nennen lassen. Kalibrierpunkte und übrige Prüfpunkte markieren. Automatischer Hinweis höchstens: Die Reste zeigen ein systematisches Muster; konstantes kA und Messbedingungen prüfen. Eine Ursachenbehauptung allein anhand von drei oder vier Punkten streichen. Ohne definierte statistische Schwelle kein automatisches Urteil über Krümmung.

### Konzept 7: Der kurze Pflichtablauf muss von optionalen Funktionen unabhängig werden und Lernziel 1 tatsächlich bearbeiten

**Wichtigkeit: hoch für die Einsatzplanung. Stelle:** Abschnitte 2 bis 4, 6, 9.5, 10 und Entscheidung E4/E8.

Frage 3 benötigt M1, das nur Sollte ist. Frage 4 benötigt eine verfügbare Messreihe; Kurslink und Beispiel sind ebenfalls nur Sollte. Die Beispieldaten stehen noch aus, und bis dahin soll der Knopf verschwinden. M4 ist nötig, wenn Messpunkte nach der Zugabe mit Modellkurven verglichen werden sollen. Damit beschreibt die Muss-Stufe noch keinen vollständig durchführbaren Vier-Fragen-Ablauf.

Der zentrale Zusammenhang von Wärmeabgabe und Endtemperatur ist ein eigenes Lernziel, taucht aber im Arbeitsauftrag nur als Startauflösung auf. Q-Säulen anzusehen stellt noch nicht sicher, dass Studierende die Bilanz zur Erklärung nutzen. Dazu kommen individuelle Vorhersage, Einigung, Eingabe, Variieren, Erklärung, Plenum und Messdatenimport. Für genau diese Kombination gibt es bisher keine Zeitmessung. Crouchs zwei Zusatzminuten betreffen Demonstrationen und sind kein Zeitnachweis für vier Simulationsfragen.

**Vorschlag:** Zwei verbindliche Wege festlegen: Kurzweg für 10 min, etwa Start mit expliziter Erklärung über Q2 minus Q1, eine Variation und Messvergleich; Vollweg für 15 min mit Deckelfrage. Für den gewählten Weg benötigte Funktionen und eine benannte Datenquelle werden Muss. Fehlen reale Daten, Frage 4 sichtbar auslassen oder einen ausdrücklich als berechneten Testfall bezeichneten Datensatz verwenden; keine erfundene Messung. ln-Fit, freie Achsenabschnitte und Residuen bleiben für Schnelle bzw. Nachbereitung. Den vollständigen Pflichtweg mit zwei Studierenden am Handy stoppen, einschließlich Öffnen und gemeinsamer Erklärung. Bis dahin 14 min als unbestätigte Schätzung führen.

### Konzept 8: Handyvorgaben sind sinnvoll, ihre Abnahme benötigt zusätzliche Zustände

**Wichtigkeit: mittel, in die Bauvorgabe aufnehmen. Stelle:** M-6/M-13/M-14/M-15, Abschnitte 5.2 und 10, Skizzen.

Das angeheftete Diagramm ist sinnvoll, wenn es genügend Raum für Eingaben lässt. Die Arbeitsskizze belegt nur die Anordnung: 390 px breite Zeichenfläche, Diagrammkasten rund 294 px hoch, Position im HTML `relative`, keine echten Regler oder Eingabefelder. Sie ist deshalb kein Nachweis für Scrollen, Fokus, Tastatur oder Trefferflächen. Bei eingeblendeter Bildschirmtastatur ist die nutzbare Höhe deutlich kleiner als 844 px. Außerdem bleiben 768 bis 1023 px in der Beschreibung des Seitenaufbaus offen.

WCAG 2.4.11 verlangt auf AA, dass der Fokus nicht vollständig verdeckt ist. Die strengere eigene Forderung, den gesamten fokussierten Regler sichtbar zu halten, ist gut, muss aber als Projektvorgabe kenntlich sein. 44 CSS-px sind ebenfalls ein sinnvoller eigener Zielwert, keine allgemeine AA-Untergrenze. Android empfiehlt 48 dp; Apple-Punkte und Android-dp sind keine CSS-px-Norm.

**Vorschlag:** Anheften bei geöffneter Bildschirmtastatur oder zu kleiner tatsächlich sichtbarer Höhe abschalten; Abschaltknopf erreichbar halten. Prüfen bei 320, 390, 768, 1024 und 1366 px, außerdem 200 % Textvergrößerung, 400 % Browserzoom und Hoch-/Querformat. Plus/Minus, Zahlenfeld und Frage bleiben ohne verdeckten Fokus erreichbar. Beschriftungen bei fast gleichen Kurven kollisionsfrei setzen. Die Quelle APG Slider verlangt ausdrücklich Tests mit berührungsgestützten Hilfstechniken; VoiceOver bzw. TalkBack mit Zahlenfeld und Alternativknöpfen deshalb in den Geräteprobelauf aufnehmen. Automatische axe-Prüfung allein belegt keine WCAG-Konformität.

### Konzept 9: Literatur ist überwiegend tragend, aber die Quellenliste und einzelne Folgerungen sind zu korrigieren

**Wichtigkeit: mittel. Stelle:** Abschnitt 4.4, Anhang B, R1 Nr. 3 und 11, R2 Q12, Anhang A.4.

Die Originalstellen bestätigen Vorhersage vor Beobachtung, anschließendes Erklären, zurückhaltende Reglerzahl, unmittelbare Rückmeldung und redundante Farbkodierung. Ferreira Abb. 6 enthält tatsächlich 0,0241 und 0,0135 pro min. Das Verhältnis 0,5602 begründet einen ungefähr 44 % kleineren **scheinbaren** Koeffizienten für diesen Versuch; der Quelltext warnt zugleich vor einer physikalisch unpassenden linearen Anpassung des offenen Falls. Die Kennzeichnung als Näherung im Konzept ist erforderlich und richtig.

Korrekturbedarf:

- Adams, Paulson und Wieman ist hier **2008**, nicht 2009, zu zitieren: Der [Datensatz der Konferenzsammlung](https://www.compadre.org/portal/items/detail.cfm?ID=7985) nennt AIP 1064, S. 59 bis 62, DOI 10.1063/1.3021273 und Veröffentlichung am 20.10.2008. Inhaltlich trägt die bereits gelesene Autorenfassung die Anforderung.
- D'Angelos g = 0,49 betrifft verschiedene Erweiterungen zusammen. Ein Gerüst als nachgewiesen wirksamsten Zusatz zu bezeichnen ist nicht gedeckt: Exhibit 20 meldet keinen signifikanten Unterschied zwischen Erweiterungsarten (p = 0,37). Für g = 0,60 der Gerüstgruppe deren eigenen Vergleich benennen. [Originalbericht, S. 19 und 28](https://www.sri.com/wp-content/uploads/2021/12/simulations-for-stem-learning-full-report.pdf).
- Die pauschale Aussage, keine Quelle nenne eine Reglerhöchstzahl, stimmt so nicht: Adams II, PDF-S. 25, nennt eine beobachtete Hemmschwelle bei mehr als drei Gruppen mit ungefähr drei Elementen. Das ist eine Interviewbeobachtung, keine allgemeine Obergrenze und kein Nachweis für genau drei neue Regler pro Stufe. [Vorabfassung](https://phet.colorado.edu/publications/PhET_Interviews_II.pdf).
- Crouch Table I vergleicht 77 % mit 61 % ohne Demonstration, mit 70 % beim Beobachten. Diese Bezugsgruppen beibehalten; die h-Werte gehören zum Vergleich mit keiner Demonstration. Die Zeitwerte 11, 13 und 21 min tragen keine Aussage, dass jede neue Frage nur drei Minuten braucht. [Original, S. 836](https://www.otffeo.on.ca/wp-content/uploads/sites/2/2014/11/Mazur_demo-article.pdf).
- A.4 verwendet BfR, FSANZ, Abraham/Diller, Brown/Diller und Goff, die in Anhang B keinen eigenen Eintrag mit Fundstelle und Prüfstatus haben. Besonders die konkrete FSANZ-Angabe von 31 g ließ sich anhand der verkürzten Angabe nicht an einer Originalstelle bestätigen. Solange diese fehlt: 30 ml als Aufgabenwert ausweisen, keinen Literaturbeweis vortäuschen.
- Bei Huestegge/Philipp ist im X4-Abruf nur das Verlagsabstract zugänglich. Der dort bestätigte Vorteil räumlich passender Legenden belegt nicht die völlige Abschaffung einer Legende. Direktbeschriftung trägt hier vor allem Okabe/Ito. Claudes früherer Volltextstatus ist dadurch weder widerlegt noch unabhängig reproduziert.

**Vorschlag:** Das Quellenverzeichnis um die fehlenden Angaben vervollständigen, tatsächliche eigene Zugänglichkeit getrennt dokumentieren und die obigen Überdehnungen zurücknehmen. Offene Nebenbelege dürfen entfallen, ohne dass der didaktische Kern zusammenbricht. Die vollständige Einzelprüfung und ihre Grenzen stehen im beigefügten Quellenprotokoll.

### Konzept 10: Vorhersagesperre und öffentliche Freischaltung müssen genauer unterschieden werden

**Wichtigkeit: mittel, Entscheidung E2 präzisieren. Stelle:** M-2/M-3, Abschnitt 5.2, A.2/A.3/A.8 und E2.

Das Verbergen der Kurven vor einer Vorhersage ist didaktisch plausibel. Der vorgegebene Test auf fehlende SVG-Kurven prüft aber nicht Ergebniszahlen in Statusmeldungen, Tabellen, weiteren Ansichten, gespeicherten Zuständen oder Erklärtexten. A.8 nennt beispielsweise den Höchstwert schon außerhalb der gesperrten Auflösungen. Für spätere Fragen sind außerdem ein zur Vorhersage passender Ausgangszustand und gespeicherte Parameter nötig, sonst bleibt eine Vorhersagemarke nach dem Zurücksetzen mehrdeutig.

Eine öffentliche Seite mit Vorhersagefeld bleibt öffentlich; eine beliebige Auswahl kann die Antwort freigeben. `noindex` verhindert keinen Zugriff und ist deshalb keine Freigabesicherung für eine noch unbekannte Vorabfrage. E2 ist vertretbar, wenn die TL genau diese Folge akzeptiert.

**Vorschlag:** Pro Frage Zustände ungesehen, vorhergesagt, geprüft und erklärt festlegen, jeweils mit zugehörigen Ausgangsparametern. Ergebnisabhängige Texte, Wertetabelle und Bildschirmleserstatus in den Vorhersagezustand einbeziehen. Bei E2 ausdrücklich entscheiden, ob selbstständiges früheres Aufdecken erlaubt ist. Falls die Antwort bis zur Sitzung tatsächlich verborgen bleiben soll, ist eine öffentliche Startkarte keine gleichwertige Alternative zu spätem Veröffentlichen oder Zugangsschutz.

### Konzept 11: Modellannahmen und Offline-Betrieb brauchen zwei kleinere Präzisierungen

**Wichtigkeit: mittel bis gering. Stelle:** A.6, A.8, Abschnitt 9.3 und 10.

Die kleine Biot-Zahl der Keramikwand belegt nicht allein die ideale Durchmischung der Flüssigkeit oder eine quantitativ bestimmte Minute zum Temperaturausgleich. Der in R3 aus Außenwand- und Wassertemperatur geschätzte innere Übergang enthält auch den Widerstand der Wand; daraus folgt die angegebene Zeitkonstante nicht eindeutig. Die Annahmen sind für das Lehrmodell zulässig, die Formulierung gut begründet ist hier stärker als der Nachweis. Für Messungen zählt die tatsächlich nach dem Ausgleich gemessene Starttemperatur, nicht weiter pauschal 80 °C.

Für eine heruntergeladene Ein-Datei-Seite sollte der Ausfall von `localStorage` die Rechnung und Dateneingabe nicht blockieren. [MDN zu localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) beschreibt unter anderem nicht definiertes Verhalten bei `file:`-URLs und mögliche Zugriffsfehler. Bisher prüft der Plan nur den erfolgreichen Speicherweg.

**Vorschlag:** Durchmischung und Temperaturgleichheit von Becher und Inhalt als bewusst vereinfachende Annahmen mit Näherungscharakter bezeichnen. Sämtliche Becherformeln in A.8 mit der richtigen Speicherkapazität versehen. Bei gesperrtem oder nicht verfügbarem Speicher nur vorübergehend im Arbeitsspeicher weiterarbeiten, mit verständlicher Meldung. Neben Neuladen auch gesperrten Speicher und die tatsächliche Offline-Datei testen.

## Vorschlag für die nächste Entscheidung

Die TL kann E1, E3, E5 und E6 unabhängig von diesen Befunden entscheiden. Für E4, E7 und E8 erst den kurzen Pflichtweg und dessen Datenquelle festlegen; für E2 die gewünschte Wirkung der Freischaltung präzisieren. Danach ist ein Bau nach einem korrigierten Konzept sinnvoll. Die spätere Abnahme muss die ergänzten physikalischen Fälle und den vollständigen Ablauf am Gerät einschließen.
