# Bericht Prüferin P (Professorin): Kaffee mit Milch, Tutorium 5, Aufgabe 1

Geprüft am 29.10.2026 auf Grundlage von Aufgabe und Lösung (Entwurf, Stand 23.10.2026; PDF als Bild angesehen) sowie dem Lehrstuhlmaterial in `material/E_lehrstuhl/`. Eigene Rechnungen: `notizen/nachrechnung_P.py`, `notizen/nachrechnung_P2.py`, `notizen/nachrechnung_P3.py`. Websuchen: 2 Suchen und 1 Seitenabruf.

## 1. Gesamturteil

Die Aufgabe ist fachlich richtig: Alle Zahlen in Aufgabe und Lösung habe ich nachgerechnet, sie stimmen bis auf Rundung. Bilanzformulierung und Lösungsweg passen zur Vorlesung (Foliensatz 05, Folie 8) und zu Übung 6. Didaktisch ist die Aufgabe deutlich stärker als die bisherige Aufgabe 1 (Rührkessel). Die echte Fehlvorstellung „Energie bleibt erhalten, also egal“, die Bestimmung von *kA* aus einer Messung und die Kontrolle über die abgegebene Wärme in e) sind sehr gut gelöst. Die größten Probleme sind der Umfang (acht Teile plus Versuch, rund 620 Wörter statt 175 bis 425 laut Strukturvorlage) und Teil g. Eine Schicht Milchschaum widerspricht den Annahmen, und schon ein um 6 % kleineres *kA* in Tasse 1 kehrt das Ergebnis von g um. Außerdem müssen die Studierenden nirgends selbst eine Annahme begründen, und offene Systeme sowie Wärmequellen kommen nicht vor. **Freigabe: ja, unter Bedingungen.** Prof1 und Prof2 müssen umgesetzt sein, und Prof8 muss geklärt sein. Prof3 bis Prof7 empfehle ich nachdrücklich.

## 2. Änderungsvorschläge

**Prof1: Umfang auf 90 Minuten zuschneiden (Kern a bis e, Vertiefung f, Zusatz h)**
- Ebene: inhaltlich (Umfang)
- Stelle: Aufgabe, gesamte Aufgabenstellung und Versuch; Lösung, Hinweise für die Tutoriumsleitung
- Befund: Die Aufgabe hat ohne Ausgangssituation rund 620 Wörter, mit Versuch rund 860. Die Strukturvorlage (Punkt 7) nennt 175 bis 425 Wörter je Aufgabe. Tutorium 5 enthält laut Überblick außerdem die Fragen 2 und 3 sowie vier weitere Blöcke. Meine Zeitschätzung für eine Gruppe im 3. Semester: Frage 1 und Start des Versuchs 5 min, a) 5, b) 15, c) 5, d) 10, e) 10, f) 10, Auswertung des Versuchs 10 min. Das sind schon rund 70 min. Mit Frage 2 oder 3 ist die Sitzung voll; g und h passen nicht mehr hinein.
- Vorschlag: In den Hinweisen für die Tutoriumsleitung einen Zeitplan ergänzen: „Kern: a bis e (etwa 45 min). Vertiefung: f. Zusatz oder Hausaufgabe: h.“ Teil g streichen oder ersetzen (siehe Prof2 und Prof3). Auf dem Blatt h als „Zusatzfrage“ belassen. Der Versuch läuft nur, wenn er in den ersten fünf Minuten startet; sonst als Küchenversuch für zu Hause.
- Begründung: Strukturvorlage, Punkt 7. Die bisherige Aufgabe 1 hatte drei Teilblöcke mit je zwei bis drei kurzen Schritten (LS_Tutorium5_Aufgabe1_mit_Loesung.md). Übung 6 hat drei Teile.
- Priorität: muss · Aufwand: klein
- Folgen: keine für Zahlen und Abbildungen; Zeitplan in den Hinweisen neu.

**Prof2: Teil g ohne Milchschaum (warme Milch statt Schaum) oder streichen**
- Ebene: technisch (fachliche Strenge)
- Stelle: Aufgabe, Teil g und Tabelle „Milchschaum“; Lösung g, Hinweis „Fehlvorstellungen“, Quellen
- Befund: Milchschaum schwimmt oben und mischt sich nicht „sofort“ (Annahme 4). Er bildet außerdem eine luftreiche Deckschicht, die die Oberfläche dämmt und die Verdunstung bremst. Nach der eigenen Lösung (Hinweis „Was die Rechnung weglässt“, Condoret 2007) trägt die Verdunstung bei hoher Temperatur rund die Hälfte der Wärmeabgabe. Tasse 1 trägt diese Schicht die ganze Stunde, Tasse 2 nicht. Damit ist die Annahme „*kA* mit und ohne Milch gleich“ gerade in diesem Szenario am wenigsten haltbar. Nachgerechnet: Ist *kA* in Tasse 1 nur um 5,6 % kleiner, sind beide Tassen gleich warm. Bei 10 % kleinerem *kA* ist Tasse 1 um 0,99 K wärmer, also umgekehrt zum Ergebnis von g (Tasse 2 um 1,19 K wärmer). Das Szenario selbst kehrt also die Aussage des Modells um.
- Vorschlag (Variante A, empfohlen): Den Schaum durch erhitzte, untergerührte Milch ersetzen. Neuer Wortlaut: „g) Am nächsten Tag erwärmt Ihr Mitbewohner die Milch vorher auf $\vartheta_{M,w} = 60\,\mathrm{°C}$ und rührt sie unter (gleiche Masse, Becher wieder vernachlässigt). Sagen Sie zuerst voraus, welche Tasse nach 60 Minuten wärmer ist. Prüfen Sie Ihre Vorhersage dann mit den Gleichungen aus d).“ In der Tabelle heißt der Block dann „Warme Milch: Temperatur $\vartheta_{M,w} = 60\,\mathrm{°C}$“. Variante B: g streichen und an seiner Stelle den Teil „Annahmen prüfen“ aus Prof3 aufnehmen. Die Kernaussage von g (Kipppunkt) bleibt in h(1) erhalten.
- Begründung: eigene Rechnung (`notizen/nachrechnung_P3.py`). Dass Schaum das Abkühlen verzögert, berichtet für Espresso-Crema [InsideHook, „Scientists Discover the Perfect Cup of Coffee“](https://www.insidehook.com/science/science-behind-espresso-foam/) über eine Studie von Arii und Nishizawa (Mukogawa Women's University). Laut Artikel ist sie unter DOI 10.1080/09168451.2017.1280662 erschienen; die Originalarbeit habe ich nicht geöffnet. Für Milchschaum auf Cappuccino habe ich keine Messung gefunden. Ich stütze mich deshalb auf das physikalische Argument, nicht auf eine Messung.
- Priorität: muss (Widerspruch zwischen Szenario und Annahmen, Aussage nicht belastbar) · Aufwand: klein
- Folgen: In Variante A bleiben die Zahlen (35,99 °C und 37,18 °C; Milch-Effekt −3,67 K). Symbol $\vartheta_S$ durch $\vartheta_{M,w}$ ersetzen. Fehlvorstellung umformulieren: „Warme Milch ist kälter als der Kaffee, wirkt also wie kalte Milch.“ Quelle Thermoplan als Beleg für die Temperatur erhitzter Milch (55 bis 65 °C) behalten.

**Prof3: Einen Teil „Annahmen prüfen“ aufnehmen (Vorgabe D26)**
- Ebene: didaktisch
- Stelle: Aufgabe, neuer Teil (anstelle von g in Variante B oder als Ergänzung zu e); Lösung entsprechend
- Befund: Alle Annahmen stehen fertig auf dem Blatt. Kein Teil verlangt, eine Annahme selbst zu begründen oder zu prüfen. Laut Vorgaben (Abschnitt 2) und Strukturvorlage (D26) ist genau das gewollt, und in der Klausur wird es regelmäßig verlangt.
- Vorschlag, Wortlaut: „Prüfen Sie zwei Annahmen. (1) Schätzen Sie ab, wie viel Kaffee in Tasse 2 während der Stunde höchstens verdunstet, wenn die Hälfte der Wärmeabgabe aus e) auf Verdunstung entfällt ($\Delta h_v \approx 2400\,\mathrm{kJ/kg}$). Darf die verdunstete Masse vernachlässigt werden? (2) Mit Milch steht der Kaffee höher in der Tasse. Wie wirkt sich das auf $kA$ in Tasse 1 aus? Kann das die Aussage aus d) umkehren?“ Ergebnisse für die Lösung: (1) $m_v \le 0{,}5 \cdot 38{,}57\,\mathrm{kJ} / 2400\,\mathrm{kJ/kg} = 8{,}0\,\mathrm{g}$, also höchstens 4,0 % von $m_K$: Die Annahme ist vertretbar. (2) Die benetzte Wand wird größer, *kA* in Tasse 1 also etwas größer, und $\vartheta_1$ sinkt. Bei +5 % beträgt der Unterschied noch 2,98 K statt 3,85 K, bei +3 % noch 3,32 K. Umkehren würde die Aussage erst bei +25 %. Zur Abschätzung (Innendurchmesser 8 cm angenommen): Die Füllhöhe steigt von 4,0 auf 4,6 cm, Wand, Boden und Oberfläche zusammen um 7,5 %. Die Oberfläche, über die die Verdunstung läuft, bleibt gleich, deshalb sind realistisch +3 bis +5 % für *kA* anzusetzen.
- Begründung: Vorgaben (Abschnitt 2), Strukturvorlage („Was aus den bisherigen Entscheidungen dazukommt“, D21 und D26). Die Rechnungen stehen in `notizen/nachrechnung_P2.py` und `nachrechnung_P3.py`. Teil (2) zeigt außerdem, dass das Hauptergebnis robust ist. Das ist die Plausibilitätsprüfung, die eine Professorin vor einer Freigabe sehen will.
- Priorität: sollte · Aufwand: mittel
- Folgen: neuer Lösungsteil; für (1) ein Tabelleneintrag „Verdampfungsenthalpie Wasser“. Bleibt g in Variante A erhalten, kommt der Teil als h) und die Zusatzfrage wird i). Die Höchstzahl von neun Teilen ist damit erreicht, deshalb empfehle ich eher Variante B von Prof2.

**Prof4: Bilanz in b) aus der allgemeinen Form herleiten lassen (Terme streichen und begründen)**
- Ebene: inhaltlich (Relevanz, Klausurnähe)
- Stelle: Aufgabe, Teil b; Lösung b
- Befund: Teil b verlangt „die instationäre Energiebilanz für den Inhalt einer Tasse“. Der klausurtypische Schritt, von der allgemeinen Bilanz auszugehen und zu begründen, welche Terme entfallen, wird nicht verlangt. Die Lösung nennt ihn nur in der Klammer „(V = const., kein Zu- und Abfluss, keine Quelle)“. Damit kommen Enthalpieströme und Quellterm in Tutorium 5 gar nicht mehr vor (siehe Prof8). Das Wort „global“ fehlt im Aufgabentext.
- Vorschlag, Wortlaut b): „Zeichnen Sie den Bilanzraum für Tasse 1 in Abb. 1 ein. Stellen Sie, ausgehend von der allgemeinen Energiebilanz, die globale instationäre Energiebilanz für den Inhalt einer Tasse auf und begründen Sie, welche Terme entfallen. Lösen Sie die Differentialgleichung durch Trennung der Variablen für die Anfangstemperatur $T(t = 0\,\mathrm{s}) = T_0$.“ In der Lösung vor der Bilanz ergänzen: „$\frac{dU}{dt} = \dot{H}_{zu} - \dot{H}_{ab} + \dot{Q}_{zu} - \dot{Q}_{ab} + \dot{Q}_{KV}$ mit $\dot{H}_{zu} = \dot{H}_{ab} = 0$ (geschlossenes System; die verdunstete Masse wird vernachlässigt, der mit dem Dampf abgeführte Enthalpiestrom steckt pauschal in $kA$), $\dot{Q}_{zu} = 0$, $\dot{Q}_{KV} = 0$ (keine Quelle), $\dot{Q}_{ab} = kA\,(T - T_u)$.“
- Begründung: Foliensatz 05, Folie 8 ($dU/dt = \dot{Q}_{zu} - \dot{Q}_{ab} + \dot{Q}_{KV}$). Die bisherige Einleitung von Tutorium 5 (Gl. 4‑1, 4‑2) betont: „Entsprechend der Fragestellung wird Gleichung (4‑1) oder (4‑2) herangezogen und vereinfacht.“ Klausuraufgaben zu Tutorium 5 enthalten die Frage F 1 „Enthalpie vs. Wärme“ (2013, 2014, 2015). Die Verdunstung ist das natürliche Beispiel dafür, dass die Tasse streng genommen ein offenes System ist. Für dieses Lernziel braucht es keine zusätzliche Rechnung.
- Priorität: sollte · Aufwand: klein
- Folgen: Lösung b um zwei Zeilen länger; keine neuen Zahlen.

**Prof5: Annahme „inkompressibel ($c_p = c_v$)“ ergänzen und die Mischbilanz in a) als $\Delta U = 0$ schreiben**
- Ebene: technisch (fachliche Strenge)
- Stelle: Aufgabe, Annahmen; Lösung a und b
- Befund: (1) Die Lösung geht von $dU/dt$ zu $m\,c_p\,dT/dt$ über, ohne $c_p = c_v$ zu begründen. Der Lehrstuhl schreibt das in Übung 6 ausdrücklich in Aufgabe, Annahmen und Lösung. (2) Lösung a begründet die Mischung mit „Die Wärme, die der Kaffee abgibt, nimmt die Milch auf.“ Im Bilanzraum Kaffee plus Milch überschreitet aber keine Wärme die Systemgrenze; bilanziert wird die innere Energie. Gerade diese Aufgabe lebt von der sauberen Trennung von Energie und Wärme (Frage 1, Teil e).
- Vorschlag: Neue Annahme auf dem Blatt: „Kaffee und Milch sind inkompressibel ($c_p = c_v$).“ Lösung b: „… für inkompressible Flüssigkeiten ($c_p = c_v$) und mit $\dot{Q}_{ab} = kA\,(T - T_u)$: $m\,c_p\,dT/dt = -kA\,(T - T_u)$“. Lösung a: „Energiebilanz um Kaffee und Milch zusammen (geschlossenes System, keine Wärmeabgabe während des Mischens): Die innere Energie bleibt gleich, $U_{nachher} = U_{vorher}$: $m_K c_{p,K}\,(T_{1,0} - T_{K,0}) + m_M c_{p,M}\,(T_{1,0} - T_M) = 0$“. Danach wie bisher umstellen.
- Begründung: LS_Uebung6_Kugeltank_mit_Loesung.md, Aufgabentext, Annahmen und Gl. (18‑9): „…für inkompressible Fluide ($c_{p,W} = c_{v,W}$)“. Foliensatz 05, Folie 17: „dichtebeständige Fluide …; $c_p = c_v$“. Klausurfrage F 1 „Enthalpie vs. Wärme“ in der Übersicht zu Tutorium 5.
- Priorität: sollte · Aufwand: klein
- Folgen: keine Zahlen; die Liste der Annahmen wird um eine Zeile länger. Zum Ausgleich kann die Klammer in Annahme 3 kürzer werden: „Alle Wärmeverluste (auch Strahlung und Verdunstung) werden pauschal über $\dot{Q}_{ab} = kA\,(T - T_u)$ mit konstantem, mit und ohne Milch gleichem $kA$ erfasst.“ Das nennt zugleich das Gesetz, das bisher auf dem Blatt fehlt.

**Prof6: In f) den Bilanzraum ausdrücklich anpassen lassen und *kA* als Modellparameter benennen**
- Ebene: didaktisch
- Stelle: Aufgabe, Teil f; Lösung f
- Befund: f ist die klausurtypische „leichte Steigerung“, aber der Kern bleibt unausgesprochen: Der Bilanzraum ändert sich (Becher gehört jetzt dazu). Für dieselbe Messung ergibt sich dann ein um 31 % größeres *kA* (0,4440 statt 0,3402 W/K). Die Lösung sagt das nur indirekt („kommt zu jedem Tasseninhalt hinzu“). Die Annahme „haben immer die Temperatur ihres Inhalts“ bleibt unbegründet.
- Vorschlag, Wortlaut f): „Die Tassen sind in Wirklichkeit Keramikbecher. Sie wurden vorgewärmt und haben immer die Temperatur ihres Inhalts. Passen Sie Bilanzraum und Energiebilanz aus b) an, bestimmen Sie $kA$ erneut aus der Messung und berechnen Sie $\vartheta_1$ und $\vartheta_2$ noch einmal. Bleibt die Aussage aus d) gültig?“ In der Lösung ergänzen: „$kA$ ist ein an die Messung angepasster Modellparameter. Wer den Becher mitbilanziert, braucht ein um 31 % größeres $kA$, damit dieselbe Messung herauskommt. Die Zeitkonstante des schwarzen Kaffees (41,0 min) ist dagegen modellunabhängig.“ Dazu ein Satz zur Annahme: „Gerechtfertigt, weil die Widerstände innen (Kaffee zur Wand) und in der dünnen Keramikwand klein sind gegenüber dem Widerstand außen zur Luft“. Das schlägt die Brücke zu Tutorium 3 und zur Biot-Frage 3.
- Begründung: Nachgerechnet: $0{,}4440/0{,}3402 = 1{,}305$. $\tau = 836{,}0/0{,}3402\,\mathrm{s} = 1091{,}0/0{,}4440\,\mathrm{s} = 2457\,\mathrm{s} = 41{,}0\,\mathrm{min}$. Der typische Fehler „altes *kA* weiterverwendet“ (39,1 und 36,1 °C, nachgerechnet) wird so verständlich statt nur benannt.
- Priorität: sollte · Aufwand: klein
- Folgen: Lösung f um drei Sätze länger; keine neuen Zahlen.

**Prof7: Qualitative Skizze des Temperaturverlaufs von den Studierenden verlangen**
- Ebene: didaktisch (Klausurnähe)
- Stelle: Aufgabe, Teil e; Lösung e mit Abb. L2
- Befund: Die Erklärung in e beruht auf dem Verlauf beider Tassen (Abb. L2, Schnittpunkt bei etwa 56 min). Diesen Verlauf erarbeiten die Studierenden aber nicht selbst. Qualitative Temperaturverläufe skizzieren ist ein fester Klausurbaustein (Übung 7, Teil 3; Klausurübersicht Tutorium 2, F 8 „Konv WÜ, Temp.verlauf“; Tutorium 3, F 7).
- Vorschlag, Wortlaut e): „Berechnen Sie für beide Tassen die Wärme, die in den 60 Minuten an die Umgebung abgegeben wird. Skizzieren Sie den Verlauf $\vartheta(t)$ beider Tassen qualitativ in einem Diagramm und erklären Sie damit das Ergebnis aus d). Hat Ihr Mitbewohner recht?“
- Begründung: LS_Uebung7_Eis_am_Stiel_mit_Loesung.md, Aufgabenteil 3. Nachgerechnet: Der schwarze Kaffee ist bis 55,7 min heißer als Tasse 1; der Wärmestrom zu Beginn beträgt 20,4 W gegenüber 17,2 W.
- Priorität: sollte · Aufwand: klein
- Folgen: Abb. L2 wird zur Lösung dieses Schritts; Abbildung bleibt.

**Prof8: Offene Systeme und Wärmequelle in Tutorium 5 sichern (bedingt: Zusatzaufgabe „Tassenwärmer“)**
- Ebene: inhaltlich (Relevanz)
- Stelle: Tutorium 5 insgesamt; gegebenenfalls Kaffee-Aufgabe, neue Zusatzaufgabe
- Befund: Die bisherige Aufgabe 1 übte drei Fälle: offenes System mit Enthalpieströmen (a), Kühlmantel (b), Quellterm und stationären Endwert (c). Die Kaffee-Aufgabe deckt nur das geschlossene System ohne Quelle ab. Der Klausurübersicht nach enthalten die Bilanzaufgaben fast immer Enthalpieströme oder Quellen (Schaltschrank, Reaktor, Nikolaus, Fondue, Rührkessel, Rohrreaktor, Chili-Topf, konti Reaktor, Extruder). Ob AMOC, Ozean oder Sverdrup das in Tutorium 5 auffangen, kann ich aus dem Überblick nicht erkennen.
- Vorschlag: Wenn kein anderer Block in Tutorium 5 eine instationäre globale Bilanz mit Enthalpiestrom oder Quelle enthält, eine kurze Zusatzaufgabe ergänzen: „Zusatzaufgabe: Ein elektrischer Tassenwärmer gibt die Heizleistung $P$ an den Inhalt eines Bechers ab. Erweitern Sie die Energiebilanz aus b) um den Quellterm. Welche Leistung ist nötig, damit der Kaffee dauerhaft 60 °C hat? Rechnen Sie mit $kA$ aus c) und aus f) und erklären Sie den Unterschied.“ Ergebnisse: $P = kA\,(\vartheta - \vartheta_u) = 13{,}6\,\mathrm{W}$ (Modell ohne Becher) bzw. 17,8 W (Modell mit Becher). Wer den Becher bei der Bestimmung von *kA* vernachlässigt, unterschätzt die nötige Leistung um 23 %. Für den stationären Fall ist f also nicht nur eine Nebenrechnung. Alternativ bleibt die bisherige Rührkessel-Aufgabe (Teil c) als Zusatzaufgabe in der Sammlung.
- Begründung: LS_Tutorium5_Aufgabe1_mit_Loesung.md, Teile a bis c; LS_Klausuraufgaben_Uebersicht.md, Bilanzen Teil I bis III und „Neue Klausuren“. Die Werte habe ich in `notizen/nachrechnung_P3.py` nachgerechnet.
- Priorität: sollte (muss geklärt werden, bevor Tutorium 5 freigegeben wird) · Aufwand: mittel
- Folgen: kurze neue Lösung (zwei Gleichungen); keine Änderung an den bisherigen Zahlen.

**Prof9: Form und Notation an das Lehrstuhlformat angleichen (Kleinigkeiten)**
- Ebene: sprachlich und gestalterisch
- Stelle: Aufgabe und Lösung, mehrere Stellen
- Befund und Vorschlag:
  - h): „Zu (1): $\vartheta_M = 47{,}0\,\mathrm{°C}$“ in „(1) $\vartheta_M = 47{,}0\,\mathrm{°C}$“ ändern. Die Strukturvorlage verlangt das Ergebnis ohne Label.
  - Einheitlich „Becher“ oder „Tasse“: Bis e heißt es „Tasse“, ab f „Becher“, die Annahme sagt „Wärmekapazität der Tasse“. Vorschlag: durchgehend „Tasse“; in f nur „Die Tassen sind Keramikbecher mit …“.
  - Im PDF stehen die Ergebnisse in größerer Formelschrift als der Text; beim Lehrstuhl (Tutorium 3, Aufgabe 3) stehen sie in Textgröße. Gleiche Schriftgröße wäre ruhiger.
  - Lösung g: Die Zerlegung in „Kaffee-Effekt“ und „Milch-Effekt“ ist gut, wird aber nicht verlangt und steht über dem Niveau der Lehrstuhllösungen. Ich würde sie mit „Zur Erklärung (nicht verlangt):“ einleiten.
- Begründung: Strukturvorlage, Punkt 4; LS_Tutorium3_Aufgabe3.md.
- Priorität: kann · Aufwand: klein
- Folgen: keine für Zahlen.

**Prof10: Versuch als Vorführung der Tutoriumsleitung und Becherdaten klären**
- Ebene: praktisch (Durchführung)
- Stelle: Aufgabe, Versuch; Lösung, Hinweis „Versuch“
- Befund: Schritt 3 verlangt *kA* „wie in Teil f (mit Becher)“. Dafür braucht man Masse und Wärmekapazität des Bechers, aber auf der Materialliste fehlt eine Waage. Der Versuch mit heißen Flüssigkeiten in Gruppen kostet Zeit und braucht eine Sicherheitsabsprache. Der erwartete Unterschied zwischen Becher 1 und 3 ist mit 1,57 K klein gegenüber der Genauigkeit eines Küchenthermometers (typisch ±1 K). Es bleibt nur deshalb messbar, weil für alle Becher dasselbe Thermometer verwendet wird.
- Vorschlag: Die Tutoriumsleitung führt den Versuch mit einem Satz Becher vorne vor; die Gruppen machen die Vorhersage. Schritt 3 ergänzen: „(Becher wiegen oder Arbeitswerte aus der Tabelle verwenden)“. Den Hinweis zu Verbrühung und Lebensmitteln im Seminarraum mit dem Lehrstuhl abstimmen.
- Begründung: nachgerechnet (`notizen/nachrechnung_P2.py`, mit Becher): nach 30 min 2,71 K, nach 60 min 3,08 K zwischen Becher 1 und 2, 1,57 K zwischen Becher 1 und 3 (Milch bei 20 °C). Damit stimmen die Angaben „gut 2,5 K“, „rund 3 K“ und „mindestens 1,6 K“.
- Priorität: kann · Aufwand: klein
- Folgen: keine für Zahlen.

**Prof11: Technischen Bezug in einem Satz herstellen**
- Ebene: inhaltlich (Relevanz)
- Stelle: Lösung, Hinweise, „Zum Weiterdenken“
- Befund: Für einen Lehrstuhl für Fluidverfahrenstechnik fehlt der Schritt vom Kaffee zur Prozessführung.
- Vorschlag, Wortlaut: „Technisch: Die Reihenfolge von Mischen und Kühlen ist eine Frage der Prozessführung. Soll ein heißer Ansatz möglichst schnell abkühlen, gibt man eine kalte Komponente spät zu (großes $\Delta T$ zur Umgebung oder zum Kühlmantel bleibt länger erhalten). Soll Wärme gespart werden, gibt man sie früh zu.“
- Begründung: Strukturvorlage, Punkt 6 (technischer Zwilling); Rührkessel und Kühlmantel aus der bisherigen Aufgabe 1.
- Priorität: kann · Aufwand: klein
- Folgen: keine.

## 3. Was bleiben sollte

- **Ausgangssituation und Frage 1:** Die Vorab-Frage greift eine echte, verbreitete Fehlvorstellung auf. Die Auflösung ist fachlich genau: „Erhalten bleibt die Energie von Kaffee, Milch und Umgebung zusammen.“ Das ist besser als jede abstrakte Einleitung.
- ***kA* aus einer Messung (Teil c):** Die inverse Aufgabe ersetzt die Nußelt-Rechnung, die hier noch nicht geübt werden soll. Das passt zur bisherigen Einleitung von Tutorium 5 („Werte, wie der Wärmeübergangskoeffizient, sollen nicht berechnet werden“) und ist dennoch nicht trivial.
- **Formulierung der Bilanz in der Lösung:** „Globale instationäre Energiebilanz um das geschlossene System … (V = const.)“, dann $dU/dt = -\dot{Q}_{ab}$, Trennung der Variablen mit Integrationsgrenzen bis $\ln((T - T_u)/(T_0 - T_u))$. Das entspricht Wort für Wort Übung 6 (Gl. 18‑8 bis 18‑11) und Übung 7 (Gl. 19‑10, 19‑11).
- **Kontrolle in e):** $(Q_2 - Q_1)/(m_K c_{p,K} + m_M c_{p,M}) = 3{,}85\,\mathrm{K}$ ergibt genau den Unterschied aus d). Das ist eine elegante Plausibilitätsprüfung im Sinne von D21 und entspricht der Form $\Delta Q = \Delta U$ aus Übung 6, Teil 3.
- **Klausurnähe:** Die Teile a bis e könnten fast unverändert als Klausuraufgabe zur Bilanz stehen (etwa 25 min), f als Steigerung. Frage 1 und h(2) eignen sich als Klausurfragen.
- **h(2):** Die Abschätzung über Energien (Milch nimmt höchstens 1,83 kJ aus der Raumluft auf, Tasse 2 hat 3,69 kJ mehr abgegeben) ist kurz, streng und lehrreich.
- **Hinweise für die Tutoriumsleitung:** Die typischen Fehler sind mit konkreten Fehlzahlen genannt; „Was die Rechnung weglässt“ ist ehrlich und quantifiziert.
- **Zahlen:** Alle Werte habe ich nachgerechnet und bestätigt: 70,47 °C; 0,3402 W/K; τ 41,0 und 46,9 min; 34,05 und 30,19 °C; 34,88 und 38,57 kJ; 0,4440 W/K; 34,04 und 30,96 °C; 35,99 und 37,18 °C; Kipppunkt 47,0 °C; 1,95 K; 4/3-Gesetz 37,65 und 33,34 °C. Das Hauptergebnis ist robust: Es kehrt sich erst um, wenn *kA* in Tasse 1 um 25 % größer ist.

## 4. Offene Fragen an die Tutoriumsleitung

1. In welchem Block von Tutorium 5 kommen eine instationäre globale Bilanz mit Enthalpieströmen (offenes System) und ein Quellterm vor? Davon hängt ab, ob Prof8 nötig ist.
2. Steht die allgemeine Energiebilanz (bisher Gl. 4‑1 und 4‑2 in der Einleitung von Tutorium 5) noch irgendwo im neuen Tutorium 5? Prof4 setzt voraus, dass die Studierenden sie kennen oder nachschlagen können.
3. Welche weiteren Blöcke sollen in derselben 90-Minuten-Sitzung laufen? Mit Kern a bis f und Versuch ist die Sitzung praktisch voll.
4. Ist der Versuch mit heißen Flüssigkeiten und Lebensmitteln im vorgesehenen Raum zulässig, und wer stellt Thermoskanne, Becher und Thermometer?
5. Soll die Kaffee-Aufgabe auch als Klausurvorbereitung dienen? Dann würde ich für c) zusätzlich ein Ersatzergebnis (zum Beispiel $kA = 0{,}35\,\mathrm{W/K}$) in der Lösung angeben, wie in Tutorium 3, Aufgabe 3.
