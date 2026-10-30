# Bericht Prüferin S (Studierende), Aufgabe „Kaffee mit Milch“, Runde 2

Stand 30.10.2026. Material: Aufgabenblatt (PDF als Bild angesehen, Markdown), Formelsammlung 2026, Foliensatz 05 (Folien 1 bis 21). Die Lösung habe ich erst nach meinem eigenen Durchgang geöffnet (Notizen davor: `notizen/protokoll_vor_loesung.md`). Rechnungen: `notizen/eigene_rechnung.py`, `notizen/zusatz.py`, `notizen/check_loesung.py`. Websuchen: keine.

## 1. Gesamturteil

Die Aufgabe macht Spaß. Die WG-Geschichte kennt man, Frage 1 lockt mich auf die falsche Fährte, und in g) dreht sich das Ergebnis um. Ich habe dabei wirklich etwas über Bilanzen gelernt (Wärme ist eine Prozessgröße, *kA* ist ein angepasster Modellparameter). Alle Ergebnisse auf dem Blatt habe ich selbst nachgerechnet und bestätigt. Das größte Problem aus Sicht der Studierenden: Das Ergebnis von d) steht mit Zuordnung eine Seite nach Frage 1 und verrät die Antwort. Außerdem steht die Vertiefung f) vor dem Kernteil g), sodass man g) leicht nicht mehr erreicht. Dazu kommen ein paar knappe Stellen (Ausgangspunkt der Bilanz in b), Arbeitsauftrag in h)(2), Milchmenge im Versuch). Mit kleinen Änderungen ist die Aufgabe einsatzbereit. Für Frage 1, a bis e, g und den Versuch brauche ich realistisch 70 bis 100 Minuten, also eher mehr als die 90 Minuten.

## 1a. Protokoll je Teil

Zeiten sind meine Schätzung für eine Studentin mit Taschenrechner (ich selbst habe mit Python gerechnet, das ist schneller). Mit „Nach Lösung“ markiere ich, was ich erst beim Vergleich mit der Lösung gesehen habe.

| Teil | Zeit | Wo ich hänge, was unklar ist | Ergebnis auf dem Blatt | Motivation |
|---|---|---|---|---|
| Lesen, Frage 1 | 5 min | Nichts unklar. Mein Tipp wäre „Tasse 2“ (heißer Kaffee bleibt länger heiß) oder „egal“ gewesen. | Die Antwort steht auf S. 2 in d) mit Zuordnung (34,05 und 30,19 °C), beim Umblättern sieht man sie sofort. | hoch: Alltagsfrage, zwei Meinungen, man will es wissen |
| a) | 5 bis 8 min | Massen aus *V* und *ρ* bilden, *m c<sub>p</sub>* gewichten. Gut machbar (Thermo I). | 70,47 °C hilft gegen den Fehler „mit Volumen gewichtet“. | mittel, Routine |
| b) | 15 bis 20 min | Welche „allgemeine Energiebilanz“? In meinen Folien gibt es Folie 8 ($dU/dt = \dot Q_{zu} - \dot Q_{ab} + \dot Q_{KV}$, ohne Enthalpieströme) und die differentielle Form (Folie 19/20). Ich habe Folie 8 genommen. Vorzeichen von $\dot Q_{ab}$, Betrag im ln. Die Frage „Darf ich in °C einsetzen?“ (*T* in b, *ϑ* sonst) ist mir gekommen. **Nach Lösung:** Die Lösung startet mit $\dot H_{zu}$, $\dot H_{ab}$ aus „Gl. (4-1) der bisherigen Tutoriumsunterlage“; die habe ich nicht. | Die Formel hilft beim Kontrollieren; den Weg nimmt sie nicht weg. Risiko: Wer es eilig hat, überspringt die Herleitung. | mittel |
| c) | 5 bis 8 min | Richtiges *m c<sub>p</sub>* (nur Kaffee). Die Plausibilitätsfrage beantworte ich nur qualitativ (gleiche Tasse, aber Füllhöhe und Verdunstung). **Nach Lösung:** Die Lösung rechnet mit 8 cm Innendurchmesser und 201 cm²; beides steht nicht auf dem Blatt. | 0,3402 W/K fängt den Fehler „Zeit in Minuten“ ab (20,41). | mittel |
| d) | 8 bis 12 min | Die Frage „Welches *m c<sub>p</sub>* jeweils?“ ist ein sehr gutes Gerüst. Fehlerquelle: Mischen am Ende von Tasse 2 vergessen. | verrät Frage 1 (siehe oben) | hoch: Hier löst sich die Wette auf |
| e) | 10 bis 15 min | „Zeigen Sie, dass $Q_2 - Q_1$ den Unterschied erklärt“: Ich musste erst darauf kommen, dass Kaffee und Milch in beiden Fällen gleich starten. Tasse 1 beginnt bei 70,47 °C, Tasse 2 bei 80 °C; das verwirrt zuerst. „Warum“ verstanden habe ich erst mit Abb. L2 (Schnittpunkt bei 56 min). | Die *Q*-Werte helfen. | hoch: Der Denkfehler wird greifbar |
| f) | 15 bis 20 min | Verstanden: dieselbe Messung, neue Deutung, *kA* steigt. Verwirrend: *ϑ*<sub>1</sub> ändert sich kaum (34,04 statt 34,05 °C), *ϑ*<sub>K</sub>(60 min) ist exakt gleich. Den zweiten Punkt erklärt die Lösung (gleiche Zeitkonstante), den ersten nicht. | hilft | mittel: viel Wiederholung, kleine, aber tiefe Erkenntnis |
| g) | 10 bis 15 min | Die Vorhersage ist schwer, und genau das ist gewollt. „je Tasse kurz vorher“ musste ich zweimal lesen. | „Zuordnung selbst bestimmen“ ist super: Die Zahlen helfen, verraten aber nichts. | sehr hoch: Umkehr! |
| h) | 15 bis 20 min | (1) ist linear, gut lösbar. (2) „mit einer Abschätzung und e)“: Ich wusste nicht, welche Abschätzung gemeint ist. Mein erster Gedanke war „20 °C < 47 °C, also nein“. **Nach Lösung:** Genau das steht als typischer Fehler drin (Tasse 1 bekommt weiter kalte Milch). Für (2) steht kein Ergebnis auf dem Blatt. | (1) hilft, (2) fehlt | mittel |
| Versuch | 10 bis 15 min Auswertung | Milchmenge fehlt (für die Vorhersage brauche ich *m*<sub>M</sub>). „Vorgewärmte Becher“ erinnert an f), der Auftrag sagt aber „wie in c“ und „Gleichungen aus d)“: Mit oder ohne Becher? „Aus dem Mittelwert“: Mittelwert der Temperaturen oder der *kA*-Werte? Becher 3: „Milch bei Raumtemperatur“, die Tabelle will aber die gemessene Milchtemperatur. | nicht vorgesehen | hoch: Ich würde mitmachen |

**Typische Fehler und Umwege (nach Vergleich mit der Lösung):** Die Liste der typischen Fehler in der Lösung deckt alles ab, worüber ich gestolpert bin, außer drei Punkten: (1) Unsicherheit über die Ausgangsbilanz in b), (2) der Gedanke „gleicher Anfangszustand“ in e), (3) die Frage, warum *ϑ*<sub>1</sub> in f) fast gleich bleibt. Ein kleiner Hinweis auf dem Blatt hätte bei b), e) und h)(2) geholfen (Vorschläge Stud3, Stud4, Stud7).

**Versuch:** Ja, ich würde mitmachen, besonders als Freiwillige mit Thermometer. Spannend ist, dass wir die Vorhersage an die Tafel schreiben und nach 40 Minuten prüfen. Becher 3 testet direkt h)(2). Praktisch schwierig: ein Thermometer für drei Becher zur selben Zeit, Umrühren vor jeder Messung, heißes Wasser im Seminarraum, Milch 40 Minuten kalt halten. Die Lösung regelt das gut (feste Reihenfolge, Messregel). Der erwartete Unterschied Becher 1 zu 2 (Modell 2,97 K mit Becher, 3,70 K ohne; beide nachgerechnet) ist mit einem einzigen Thermometer gut messbar. Becher 1 zu 3 (1,5 bis 1,8 K) ist knapp.

**Gesamteindruck:** Lohnt sich. Ich nehme mit: (1) Energieerhaltung gilt für Inhalt plus Umgebung, nicht für die Tasse allein. (2) Wärme ist eine Prozessgröße. (3) Ein aus einer Messung angepasster Parameter hängt am Modell (f). (4) Ob „früh“ oder „spät“ besser ist, hängt von der Milchtemperatur ab (Kipppunkt 47 °C). Zeit insgesamt: Kern (Frage 1, a bis e, g, Versuch) 70 bis 100 min, alles mit f und h 100 bis 140 min.

## 2. Änderungsvorschläge

**Stud1: Ergebnis von d) ohne Zuordnung angeben**
- Ebene: didaktisch
- Stelle: Aufgabe, Teil d (Ergebniszeile)
- Befund: Frage 1 (S. 1) verlangt eine Vermutung, „bevor Sie Aufgabe 1 rechnen“. Auf S. 2 steht in d) $\vartheta_1 = 34{,}05\,°C$, $\vartheta_2 = 30{,}19\,°C$. Wer umblättert, kennt die Antwort. Die Lösung weiß das („die Ergebnisse in d) verraten sonst die Antwort“) und rät, Frage 1 vor dem Austeilen zu stellen. Das Blatt wird aber auch ohne Tutorium gelesen (Nacharbeit, Fehlen, Klausurvorbereitung).
- Vorschlag: Ergebniszeile d): „$34{,}05\,\mathrm{°C}$ und $30{,}19\,\mathrm{°C}$ (Zuordnung selbst bestimmen)“, genau wie in g). Die Vorgabe „Ergebnis am Ende jedes rechnenden Teils“ bleibt erfüllt.
- Begründung: Das Muster aus g) funktioniert gut: Die Zahlen helfen beim Kontrollieren, und die Kernfrage bleibt offen. Dass e) danach $Q_1 < Q_2$ zeigt, stört nicht, denn e) kommt nach d).
- Priorität: sollte · Aufwand: klein
- Folgen: nur die Ergebniszeile in d) (Blatt und Wiederholung des Blatts in der Lösung). Keine Zahlen ändern sich.

**Stud2: Kernteil g) vor die Vertiefung f) stellen**
- Ebene: didaktisch, praktisch
- Stelle: Aufgabe, Teile f und g; Lösung, f, g und Hinweise
- Befund: Im Zeitplan der Lösung ist g) Kern (Minute 58 bis 72) und f) Vertiefung „für Schnelle“ (72 bis 85). Auf dem Blatt steht f) aber vor g). Wer von oben nach unten arbeitet, bleibt 15 bis 20 Minuten in f) hängen und erreicht g), die spannendste Stelle, nicht mehr. Außerdem gehören g) und h)(1) zusammen (Milchtemperatur, Kipppunkt), und f) steht dazwischen. Die Lösung von f) verweist schon auf „die Zerlegung in g)“, also nach vorn.
- Vorschlag: Variante A (empfohlen): Reihenfolge tauschen. Neues f) = Milchkaffee (bisher g), neues g) = *Vertiefung* Becher (bisher f), h) bleibt. Variante B (Minimum): Reihenfolge lassen, f) überschreiben mit „*Vertiefung* (kann übersprungen werden, weiter mit g)“.
- Begründung: Zeitplan und Kernteile aus den Hinweisen der Lösung. Eigene Zeitschätzung: Bis Ende e) brauche ich 45 bis 60 min, danach bleibt im Tutorium nur Zeit für einen der beiden Teile.
- Priorität: sollte · Aufwand: mittel (A), klein (B)
- Folgen (A): Annahme „Wärmekapazität der Tasse wird bis Teil e vernachlässigt“ wird zu „außer in Teil g vernachlässigt“. Tabellenköpfe: „Milch in Teil f“, „Becher in Teil g“. Abb. L1: „Bilanzraum (a bis f)“, „in g mit Becher“. Lösungstexte f/g tauschen (der Verweis auf die Zerlegung zeigt dann nach hinten). Hinweise: Zeitplan, typische Fehler („in f)“), „Zu g“, Versuch-Erwartung („Anlass für f)“) umnummerieren. Keine Zahlen ändern sich.

**Stud3: In b) den Ausgangspunkt der allgemeinen Energiebilanz nennen**
- Ebene: didaktisch, sprachlich
- Stelle: Aufgabe, Teil b
- Befund: „Vereinfachen Sie die allgemeine Energiebilanz“: Mit Foliensatz 05 als Material habe ich zwei Kandidaten, Folie 8 (ohne Enthalpieströme) und die differentielle Form auf Folie 19/20. Die Lösung startet mit $dU/dt = \dot H_{zu} - \dot H_{ab} + \dot Q_{zu} - \dot Q_{ab} + \dot Q_{KV}$ nach „Gl. (4-1) der bisherigen Tutoriumsunterlage“, die nicht in meinem Material ist. Wer von Folie 8 startet, kann die Enthalpieströme gar nicht „begründet streichen“.
- Vorschlag: „Vereinfachen Sie die allgemeine Energiebilanz (Gl. (4-1) aus Tutorium 4 bzw. Foliensatz 05, Folie 8) zur globalen instationären Bilanz …“. Die Gleichung selbst nicht hinschreiben, sonst fällt die Denkarbeit weg.
- Begründung: Foliensatz 05, Folie 8 und Folie 19/20; Lösung b). Den Schritt „welche Terme entfallen“ kann man nur begründen, wenn klar ist, welche Terme da stehen.
- Priorität: sollte · Aufwand: klein
- Folgen: keine für Zahlen. Die Nummer der Gleichung und des Tutoriums muss die TL bestätigen (siehe Offene Fragen).

**Stud4: h)(2) eindeutiger stellen und Ergebnis ergänzen**
- Ebene: didaktisch, sprachlich
- Stelle: Aufgabe, Teil h (2) und Ergebniszeile
- Befund: „Begründen Sie mit einer Abschätzung und e)“ ist zu knapp. Mein erster Gedanke war „20 °C < 47 °C, also nein“. Die Lösung nennt genau das als typischen Fehler, weil Tasse 1 weiter die kalte Milch bekommt. Für (2) fehlt das Ergebnis am Ende, obwohl gerechnet wird.
- Vorschlag: „(2) Die Milch für Tasse 2 steht ab $t = 0$ in einem Glas mit etwas Abstand zur Tasse und wird nur von der Raumluft erwärmt. Kann Tasse 2 so wärmer werden als Tasse 1? Schätzen Sie ab, wie viel Wärme die Milch höchstens aufnehmen kann, und vergleichen Sie mit $Q_2 - Q_1$ aus e).“ Ergebniszeile: „(1) $\vartheta_M = 47{,}0\,\mathrm{°C}$, (2) $Q_M \le 1{,}83\,\mathrm{kJ}$; Tasse 2 bleibt mindestens $1{,}95\,\mathrm{K}$ kühler“.
- Begründung: eigene Rechnung: $Q_M = 121{,}7\,\mathrm{J/K} \cdot 15\,\mathrm{K} = 1{,}83\,\mathrm{kJ}$; $(3{,}69 - 1{,}83)\,\mathrm{kJ}/957{,}7\,\mathrm{J/K} = 1{,}95\,\mathrm{K}$; direkt: $\vartheta_1 = 34{,}05\,°C$, $\vartheta_2(\vartheta_M = 20\,°C) = 32{,}10\,°C$. „Mit etwas Abstand“ statt „neben“ passt zu den Versuchshinweisen der Lösung („mit Abstand zu den Bechern, sonst erwärmt sie auch der heiße Becher“).
- Priorität: sollte · Aufwand: klein
- Folgen: Ergebniszeile h) auf dem Blatt; Lösung unverändert.

**Stud5: Versuchsanleitung präzisieren (Milchmenge, Modell, Glas, Mittelwert)**
- Ebene: praktisch, sprachlich
- Stelle: Aufgabe, Versuch zu Aufgabe 1
- Befund: (1) Die Milchmenge fehlt; für die Vorhersage braucht man *m*<sub>M</sub>. (2) „Vorgewärmte Becher“ lässt an f) denken, der Auftrag sagt „wie in Teil c“ und „Gleichungen aus d)“, also ohne Becher; ich war unsicher. (3) „Glas neben den Bechern“ widerspricht dem Hinweis der Lösung („mit Abstand“). (4) „aus dem Mittelwert“ ist mehrdeutig. (5) „Becher 3 mit Milch bei Raumtemperatur“ passt nicht zur Spalte „Milch *ϑ*<sub>M</sub>“, in die man den Messwert einträgt.
- Vorschlag: „Drei gleiche, vorgewärmte Becher mit je 200 ml heißem Wasser oder Kaffee, dazu je 30 ml Milch: Becher 1 bekommt die Milch sofort, Becher 2 und 3 erst nach 40 Minuten (Becher 2: Milch aus der Kühltasche; Becher 3: Milch, die ab Beginn in einem Glas mit etwas Abstand zu den Bechern steht). Nach 10 Minuten werden Becher 2 und 3 gemessen. 1. Bestimmen Sie *kA* für Becher 2 und 3 wie in Teil c (ohne Becher) und bilden Sie den Mittelwert. Sagen Sie mit den Gleichungen aus d) die Temperaturen nach 40 Minuten voraus (Becher 3: Milch höchstens bei Raumtemperatur, obere Grenze).“
- Begründung: Hinweise der Lösung zum Versuch (Messbecher, Glas mit Abstand, Raumtemperatur als obere Grenze, Modell ohne Becher als Anlass für f). Ohne Milchmenge kann man die Vorhersage nicht rechnen.
- Priorität: sollte · Aufwand: klein
- Folgen: nur Versuchstext; Erwartungswerte in der Lösung bleiben (nachgerechnet: 3,70 K ohne Becher, 2,97 K mit Becher).

**Stud6: Zeitplan für a bis e entlasten (b gemeinsam)**
- Ebene: praktisch
- Stelle: Lösung, Hinweise, Zeitplan (Minute 12 bis 50)
- Befund: Für a bis e sind 38 Minuten geplant. Meine Schätzung: a 5 bis 8, b 15 bis 20, c 5 bis 8, d 8 bis 12, e 10 bis 15, zusammen 45 bis 60 min, dazu Ablenkung durch den Versuch. Dann fallen g) (Kern) oder die Auflösung weg.
- Vorschlag: In den Zeitplan: „b) nach etwa 8 min Einzelarbeit gemeinsam an der Tafel (Bilanz vereinfachen, Trennung der Variablen), dann c bis e allein“. Dazu ein Haltepunkt: „Sind um Minute 50 viele noch nicht bei e), e) gemeinsam besprechen, g) zuerst als Vorhersage mit Handzeichen“.
- Begründung: eigene Zeitschätzung (Protokoll oben); die Lösung sagt selbst „Zeitplan als Schätzung, beim ersten Einsatz messen“.
- Priorität: sollte · Aufwand: klein
- Folgen: nur Hinweise der Lösung.

**Stud7: Kleiner Denkanstoß in e) zum gleichen Anfangszustand**
- Ebene: didaktisch
- Stelle: Aufgabe, Teil e
- Befund: „Zeigen Sie, dass $Q_2 - Q_1$ den Temperaturunterschied aus d) erklärt“: Ich habe gehangen, weil Tasse 1 bei 70,47 °C und Tasse 2 bei 80 °C beginnt. Der Schlüssel (gleicher Kaffee und gleiche Milch am Anfang, gleicher Inhalt am Ende) steht nur in der Lösung.
- Vorschlag: „Zeigen Sie mit einer Energiebilanz um Kaffee und Milch zusammen (Anfang: Kaffee mit 80 °C und Milch mit 5 °C, noch getrennt), dass $Q_2 - Q_1$ den Temperaturunterschied aus d) erklärt.“
- Begründung: eigene Rechnung: $(Q_2 - Q_1)/(m_K c_{p,K} + m_M c_{p,M}) = 3{,}69\,\mathrm{kJ}/957{,}7\,\mathrm{J/K} = 3{,}85\,\mathrm{K}$, genau der Unterschied aus d).
- Priorität: kann · Aufwand: klein
- Folgen: keine für Zahlen.

**Stud8: Temperaturverlauf qualitativ skizzieren lassen (oder Abb. L2 zeigen)**
- Ebene: didaktisch
- Stelle: Aufgabe, Teil e (oder Hinweise der Lösung)
- Befund: Das „Warum“ habe ich erst mit Abb. L2 verstanden: Der schwarze Kaffee ist bis etwa 56 min heißer und gibt deshalb mehr Wärme ab. Auf dem Blatt rechnet man nur Endwerte.
- Vorschlag: In e) ergänzen: „Skizzieren Sie *ϑ*(*t*) beider Tassen qualitativ in einem gemeinsamen Diagramm.“ Ohne Platz und Zeit dafür: in den Hinweisen „Abb. L2 bei der Auflösung von Frage 1 zeigen“.
- Begründung: Abb. L2 der Lösung; eigene Rechnung: Der Unterschied ist bei 55,7 min am größten (3,86 K), 60 min ist also eine sehr gute Wahl.
- Priorität: kann · Aufwand: klein
- Folgen: Bei der Skizze plus 3 bis 5 min, sonst keine.

**Stud9: Lösung f) mit einem Satz zu *ϑ*<sub>1</sub> ergänzen, Hinweis zu °C in b)**
- Ebene: inhaltlich (Lösung)
- Stelle: Lösung, Teile f und b
- Befund: (1) In f) bleibt *ϑ*<sub>1</sub> fast gleich (34,04 statt 34,05 °C). Studierende fragen „Warum hat der Becher bei Tasse 1 keinen Einfluss?“. Die Lösung erklärt nur, warum *ϑ*<sub>K</sub>(60 min) gleich bleibt. (2) Die Lösung rechnet alles in K um. Viele rechnen direkt in °C und fragen, ob das erlaubt ist.
- Vorschlag: (1) Nach *T*<sub>1</sub> in f): „Dass *ϑ*<sub>1</sub> fast gleich bleibt, ist Zufall der Zahlen: Die Mischtemperatur steigt (72,47 statt 70,47 °C), aber die Zeitkonstante von Tasse 1 sinkt (45,5 statt 46,9 min).“ (2) In b) nach der Lösung: „Da nur Temperaturdifferenzen vorkommen, darf man auch mit *ϑ* in °C rechnen.“
- Begründung: eigene Rechnung: $\tau_1 = 957{,}7/0{,}3402\,\mathrm{s} = 46{,}9\,\mathrm{min}$, mit Becher $1212{,}7/0{,}4440\,\mathrm{s} = 45{,}5\,\mathrm{min}$.
- Priorität: kann · Aufwand: klein
- Folgen: nur Lösungstext.

**Stud10: Angaben für die Plausibilitätsprüfung in c) auf das Blatt**
- Ebene: didaktisch
- Stelle: Aufgabe, Tabelle und Teil c
- Befund: Die Lösung beantwortet „ist sie plausibel?“ mit 8 cm Innendurchmesser, Füllhöhe 4,0 bzw. 4,6 cm, +7,5 % Fläche und $kA/A \approx 17\,\mathrm{W/(m^2\,K)}$. Diese Angaben haben Studierende nicht; sie können nur qualitativ antworten.
- Vorschlag: In die Tabelle (Kaffee-Spalte oder Becher): „Innendurchmesser der Tasse $d_i = 8\,\mathrm{cm}$“. Alternativ in den Hinweisen: „Qualitative Begründung genügt; die Zahlen sind Zusatz für die Besprechung.“
- Begründung: eigene Rechnung: Füllhöhe 3,98 bzw. 4,58 cm; Fläche (Boden, Mantel, Oberfläche) 200,5 bzw. 215,5 cm² (+7,5 %); $0{,}3402/0{,}02005 = 17{,}0\,\mathrm{W/(m^2\,K)}$. Die Lösung bestätigt mit +3 bis 5 % *kA* einen Unterschied von 3,32 bis 2,98 K (nachgerechnet).
- Priorität: kann · Aufwand: klein
- Folgen: eine Tabellenzeile; Lösung unverändert.

**Stud11: Kleinigkeiten in der Gestaltung**
- Ebene: gestalterisch, sprachlich
- Stelle: Aufgabe, Überschrift „Aufgabe 1 (neu)“ und Abb. 1; Lösung, Abb. L2
- Befund: (1) „(neu)“ hinter Aufgabe 1 sagt Studierenden nichts (neu gegenüber was?). (2) In Abb. 1 zeigen die Pfeile $\dot Q_{ab}$ nur nach oben. Das legt nahe, dass nur die Oberfläche Wärme abgibt; Abb. L1 hat zu Recht auch Pfeile zur Seite. (3) In Abb. L2 liegt die Achsbeschriftung „40“ des Ausschnitts auf der gestrichelten Kurve des Hauptdiagramms (bei etwa *t* = 32 min).
- Vorschlag: (1) „(neu)“ auf dem Studierendenblatt streichen, falls es keine Lehrstuhlkonvention ist. (2) In Abb. 1 kleine seitliche Pfeile ergänzen wie in Abb. L1. (3) Ausschnitt in Abb. L2 etwas nach oben oder rechts schieben.
- Begründung: Ansicht von Blatt (S. 1) und Abb. L2.
- Priorität: kann · Aufwand: klein
- Folgen: Abbildungen neu erzeugen; keine Zahlen.

## 3. Was bleiben sollte

- Die Geschichte (WG, Telefonat, Mitbewohner) und Frage 1 mit drei Antwortmöglichkeiten: Beide Intuitionen („egal“ und „später bleibt länger heiß“) sind falsch, das bleibt hängen.
- Die Gerüstfrage in d) „Welches *m c<sub>p</sub>* setzen Sie jeweils ein?“ fängt den häufigsten Fehler ab.
- e) mit dem Denkfehler des Mitbewohners: „Wärme ist eine Prozessgröße“ verknüpft Thermo und Wärmeübertragung.
- „Zuordnung selbst bestimmen“ in g); das sollte Vorbild für d) werden (Stud1).
- Die Umkehr in g) und der Kipppunkt in h)(1): Hier versteht man, dass es nicht um „früh oder spät“ geht, sondern um die Milchtemperatur.
- f) als Lehrstück „*kA* ist ein an die Messung angepasster Parameter“ (als Vertiefung).
- Die Ergebnisse am Ende der Teile: Sie fangen typische Fehler ab (Minuten statt Sekunden in c, Volumen statt Masse in a).
- 60 min als Dauer: liegt fast genau beim größten Unterschied (55,7 min, 3,86 K).
- Der Versuch mit Vorhersage an der Tafel und Becher 3 als Test für h)(2).
- Alle Zahlen auf dem Blatt stimmen (eigene Nachrechnung aller Teile a bis h und der Versuchserwartung).

## 4. Offene Fragen an die Tutoriumsleitung

1. Bekommen die Studierenden die Lösung **mit** den „Hinweisen für die Tutoriumsleitung“? Dann lesen sie dort „Frage 1 vor dem Austeilen stellen“ und den Zeitplan. Ich würde die Hinweise in ein eigenes Dokument für Tutorinnen und Tutoren verschieben.
2. Der Zeitplan nennt „Frage 3 (Biot)“ (Minute 5 bis 12). Auf diesem Blatt gibt es nur Frage 1. Steht Frage 3 auf einem anderen Teil des Blatts zu Tutorium 5?
3. Haben die Studierenden die „Gl. (4-1) der bisherigen Tutoriumsunterlage“ (allgemeine Energiebilanz mit Enthalpieströmen), und aus welchem Tutorium stammt sie (für Stud3)?
4. Ist „(neu)“ hinter Aufgabe 1 eine Lehrstuhlkonvention, die auf dem Studierendenblatt bleiben soll?
5. Die Quellen verweisen für *c<sub>p</sub>* der Milch auf „Tutorium 8“. Für Studierende in Tutorium 5 ist das ein Vorgriff. Ist das so gewollt?
