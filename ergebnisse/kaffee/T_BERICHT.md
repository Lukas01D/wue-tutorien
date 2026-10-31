# Bericht Prüfer T: Technik (Kaffee mit Milch, Entwurf 23.10.2026)

Grundlage: Aufgabe und Lösung (PDF als Bild und Markdown), Abb. 1, L1, L2, Rechenmodell, Formelsammlung, Foliensatz 05. Eigene Rechnungen in `notizen/rechnung/` (t1 bis t6, siehe Anhang). Das vorhandene Rechenmodell habe ich nur zum Vergleich ausgeführt (`notizen/modell/lauf.txt`, identisch mit der beigelegten Ausgabe).

## 1. Gesamturteil

Das Modell ist sauber, die Bilanz (dU/dt = −Q̇_ab wie Folie 8), die Trennung der Variablen und alle Zahlen in Aufgabe und Lösung stimmen; ich habe jede Ergebniszahl mit einem eigenen Skript bestätigt (Abweichung höchstens in der letzten Stelle). Die Kernaussage aus d) ist technisch sehr robust: Messfehler, Starttemperatur, Raumtemperatur und Milchmenge verschieben die Absolutwerte um mehrere Kelvin, den Unterschied aber kaum (3,8 bis 3,9 K bei ±1 K Messfehler); umdrehen könnte ihn erst ein um 25 % größeres *kA* mit Milch (mit Becher 19 %) oder Milch über 47 °C. Das größte Problem ist Teil g: Echter Milchschaum mischt sich nicht, sondern liegt als dämmende Schicht oben; schon 6 % weniger *kA* in Tasse 1 drehen das Ergebnis von g um, die Lösung lehrt dort also vermutlich das Gegenteil dessen, was ein echter Cappuccino tut. Zweites Problem ist der Versuch: Becher 1 gegen 2 ist messbar (realistisch 2,5 bis 3,5 K), Becher 3 aber kaum von Becher 2 zu unterscheiden, und im Ablauf fehlen Raumtemperatur, Umrühren und eine Kontrolle der Streuung. Die Teile a bis f und h sind nach kleinen Ergänzungen einsatzbereit; g und der Versuch brauchen eine Überarbeitung (Aufwand klein bis mittel).

## 2. Änderungsvorschläge

**Tech1: Milchschaum in g widerspricht der Annahme „mischen sich sofort“; Ergebnis kippt bei 6 % weniger kA**
- Ebene: technisch (Modellgültigkeit), inhaltlich
- Stelle: Aufgabe, Teil g und Tabelle „Milchschaum“; Lösung g und Hinweise „Fehlvorstellungen“
- Befund: 30,9 g Milch als Schaum (Dichte geschätzt 300 bis 500 kg/m³) sind 60 bis 100 ml und bilden auf 50 cm² eine Schicht von 1,2 bis 2,0 cm. Schaum schwimmt und dämmt die Oberfläche, über die der größte Teil der Wärme geht (Verdunstung, Strahlung). Die Lösung rechnet dagegen mit sofortiger Mischung und gleichem *kA*. Eigene Rechnung (t1): Ist *kA* in Tasse 1 nur 5,6 % kleiner (Faktor 0,944), sind beide Tassen gleich warm; bei −10 % ist Tasse 1 um 1,0 K wärmer, bei −20 % um 3,5 K. Selbst wenn der Schaum nach 15 min zerfällt und *kA* bis dahin um 30 % senkt, ist Tasse 1 wärmer (+0,4 K, t6). Die Aussage „Jetzt ist Tasse 2 um 1,19 K wärmer“ gilt also nur im Modell und ist für einen echten Cappuccino wahrscheinlich falsch. Messdaten zur Dämmwirkung von Milchschaum habe ich nicht gefunden (Websuche ohne belastbaren Treffer); die Schichtwirkung ist eine eigene Abschätzung.
- Vorschlag (Variante A, empfohlen): Schaum durch heiße Milch ersetzen, Zahlen bleiben gleich. Neuer Wortlaut g: „Am nächsten Tag trinkt Ihr Mitbewohner Milchkaffee: Statt kalter Milch kommt heiße Milch mit $\vartheta_H$ aus dem Milchaufschäumer in beide Tassen (gleiche Menge, Becher wieder vernachlässigt). …“ Tabelle: „***Heiße Milch:*** Temperatur $\vartheta_H = 60\,\mathrm{°C}$“. Variante B: Schaum behalten, Annahme ergänzen („Der Schaum fällt sofort zusammen und mischt sich mit dem Kaffee; eine Schaumschicht auf dem Kaffee wird vernachlässigt.“) und in den Hinweisen: „Eine echte Schaumschicht dämmt die Oberfläche. Schon 6 % weniger *kA* in Tasse 1 drehen das Ergebnis um; ein Cappuccino mit Schaumkrone bleibt vermutlich in Tasse 1 wärmer.“
- Begründung: Rechnung t1 und t6; Annahme 4 der Aufgabe („Kaffee und Milch mischen sich sofort“) passt nicht zu Schaum.
- Priorität: muss · Aufwand: klein
- Folgen: Variante A: nur Wortlaut in Aufgabe, Lösung g, Hinweis „Fehlvorstellungen“ („Heiße Milch ist kälter als der Kaffee, wirkt also wie kalte Milch“) und Quelle (Thermoplan als Arbeitswert für aufgeschäumte Milch bleibt passend). Zahlen unverändert.

**Tech2: Hinweis „Was die Rechnung weglässt“ ist einseitig; Exponent 4/3 bildet die Verdunstung nicht ab**
- Ebene: technisch
- Stelle: Lösung, Hinweise für die Tutoriumsleitung, dritter Punkt
- Befund: (1) Der Exponent 4/3 gehört zur turbulenten freien Konvektion. Die Verdunstung folgt dem Dampfdruck (80 °C: 47 kPa, 34 °C: 5 kPa) und fällt viel stärker als linear. Mein physikalisches Modell (Oberseite: freie Konvektion nach Formelsammlung, Strahlung, Verdunstung über Analogie Wärme/Stoff; Seitenwand: senkrechter Zylinder; geeicht auf 67 °C nach 10 min, t3) ergibt bei 50 % Verdunstungsanteil bei 80 °C: $\vartheta_1 \approx 39{,}3\,\mathrm{°C}$, Unterschied 4,7 K bei gleicher Füllhöhe (Lösung: 37,65 °C und 4,31 K). Die Richtung der Lösung stimmt, die Größe ist unterschätzt. (2) Der Gegeneffekt fehlt: Mit Milch steht der Inhalt 4,6 statt 4,0 cm hoch, die benetzte Wand ist 15 % größer, *kA* steigt um einige Prozent. Je 5 % mehr *kA* in Tasse 1 sinkt der Unterschied um 0,87 K (t1); im physikalischen Modell um 0,9 K (4,7 auf 3,8 K). Beide Effekte heben sich etwa auf; der lineare Wert 3,85 K ist deshalb eine gute Schätzung, die Absolutwerte nach 60 min sind aber zu niedrig (je nach Verdunstungsanteil um 1 bis 6 K, bei 50 % um rund 5 K).
- Vorschlag: Hinweis ersetzen durch: „*Was die Rechnung weglässt:* (1) Die Verdunstung wächst mit dem Dampfdruck, also viel stärker als linear mit $T - T_u$; bei 80 °C trägt sie rund die Hälfte der Wärmeabgabe (Condoret 2007, Tab. 2), bei 35 °C deutlich weniger. Mit *kA* aus der 10-Minuten-Messung liegen die berechneten Temperaturen nach 60 min deshalb einige Kelvin zu tief (Abschätzung: rund 39 statt 34 °C); der heißere schwarze Kaffee verliert noch mehr, der Unterschied wächst auf rund 4,7 K. (2) Mit Milch ist die Tasse voller und die benetzte Wand 15 % größer; *kA* steigt um einige Prozent, je 5 % sinkt der Unterschied um rund 0,9 K. Beide Effekte heben sich etwa auf. Umdrehen könnte das Ergebnis erst ein um 25 % größeres *kA* mit Milch.“
- Begründung: t1 (Kipp bei Faktor 1,251 ohne, 1,188 mit Becher), t3 (Varianten 0 bis 60 % Verdunstung: Unterschied ohne Becher 2,8 bis 4,0 K mit Füllhöhen-Effekt, 4,2 bis 4,8 K ohne).
- Priorität: sollte · Aufwand: klein
- Folgen: nur Hinweistext; im Rechenskript `nichtlinear(n)` als Näherung kennzeichnen oder ersetzen.

**Tech3: Versuchsablauf: Raumtemperatur, Umrühren, Mischtemperatur und Streuungskontrolle fehlen**
- Ebene: praktisch (Durchführung)
- Stelle: Aufgabe, Versuch zu Aufgabe 1, Material und Schritte 2 bis 5
- Befund: Für *kA* in Schritt 3 braucht man $\vartheta_u$; die Messung steht nicht im Ablauf. Umrühren steht nur in Schritt 5, ein unberührter Becher ist aber geschichtet (t5: Bi mit reiner Leitung 0,2 bis 0,27, mit innerer freier Konvektion etwa 0,05; dass ohne Rühren zwischen Boden und Oberfläche 1 bis 3 K liegen können, ist eine nicht gerechnete Schätzung). Becher 2 und 3 sind bis $t = 60\,\mathrm{min}$ gleich (beide schwarz); misst man beide bei 10 min, bekommt man die Streuung zwischen den Bechern umsonst. Für $C_B$ fehlt eine Waage. Bei 0,3 K/min Abkühlung nach 60 min (t1) zählt auch die Messreihenfolge.
- Vorschlag (neuer Wortlaut, Änderungen gegenüber dem Entwurf):
  - *Material:* … „ein Einstichthermometer für alle Messungen, Küchenwaage, Löffel, Uhr.“
  - 2. „$t = 0$: Raumtemperatur messen. Becher vorwärmen (2 min mit heißem Wasser), je 200 ml einfüllen, umrühren, Starttemperatur messen. Becher 1: Milch zugießen, umrühren, Mischtemperatur messen (Vergleich mit Teil a). …“
  - 3. „$t = 10\,\mathrm{min}$: Becher 2 und 3 umrühren und messen. Aus dem Mittelwert $kA$ wie in Teil f bestimmen; der Unterschied zwischen 2 und 3 zeigt, wie stark gleiche Becher streuen.“
  - 5. „… Milch in Becher 2 und 3 gießen, alle drei Becher umrühren und in fester Reihenfolge zügig messen (Thermometer in die Mitte, halbe Tiefe, warten, bis die Anzeige steht; Löffel nicht im Becher lassen).“
  - Ein Satz für alle: „Alle Becher stehen nebeneinander auf derselben Unterlage, ohne Deckel, nicht am Fenster oder an der Heizung.“
- Begründung: Ein Thermometer für alles hebt dessen Grundfehler (bei Einstichthermometern laut Datenblättern oft ±1 bis ±2 K, nur aus Suchtreffern, z. B. PCE-ST 1: ±1,5 % ±2 °C) in allen Differenzen auf, auch in $\vartheta - \vartheta_u$ für *kA*. 5 % Unterschied im *kA* zweier „gleicher“ Becher verschiebt die Temperatur nach 60 min um 0,9 K (t1); das muss man kennen, um 1 bis 3 K Unterschied zu deuten.
- Priorität: sollte · Aufwand: klein
- Folgen: Lösung, Hinweis „Versuch“ kürzen (Rühren steht dann im Ablauf); Material um Waage ergänzen.

**Tech4: Erwartungswerte zum Versuch korrigieren; Becher 3 ist kaum von Becher 2 zu trennen**
- Ebene: praktisch, technisch
- Stelle: Lösung, Hinweise „Versuch“
- Befund: „Becher 3 bleibt um mindestens 1,6 K kühler als Becher 1“ gilt nur im linearen Modell mit Milch bei genau 20 °C (eigene Rechnung: 1,57 K). Real: Die Milch im Glas erreicht in 60 min nur etwa 13 bis 17 °C (Zeitkonstante Glas mit 30 ml rund 40 bis 80 min, t4), die Milch in der Kühltasche wird 7 bis 10 °C warm. Mit Becher, kA aus der Messung: Becher 1 minus 2 rund 2,6 bis 3,1 K, Becher 1 minus 3 rund 1,6 bis 2,3 K, Becher 3 minus 2 nur 0,3 bis 1,5 K. Mit Füllhöhen-Effekt (Tech2) sinkt alles um bis zu 1 K (physikalisches Modell mit Becher: Becher 1 minus 2 rund 2,3 bis 2,8 K, Becher 1 minus 3 rund 1,3 K). Die Becherstreuung liegt bei etwa 0,5 bis 1 K. Becher 3 gegen 2 ist damit nicht sicher messbar, und „mindestens“ ist für den Versuch nicht garantiert.
- Vorschlag: Hinweis neu: „Mit echten, vorgewärmten Bechern sind nach 60 Minuten zwischen Becher 1 und 2 rund 2,5 bis 3 K zu erwarten (nach 30 Minuten schon gut 2,5 K), mit einem Thermometer für alle Messungen gut messbar. Becher 3 liegt dazwischen: rund 1,5 bis 2 K kühler als Becher 1, aber nur 0,5 bis 1 K wärmer als Becher 2, das ist kaum mehr als die Streuung zwischen den Bechern (Schritt 3). Die gemessenen Temperaturen liegen meist einige Kelvin über der Vorhersage, weil *kA* mit sinkender Temperatur kleiner wird (Verdunstung).“ Optional für ein deutlicheres Signal: im Versuch 50 ml Milch nehmen (Becher 1 minus 2 dann 3,9 bis 4,7 K, Becher 1 minus 3 rund 2,3 bis 3,4 K, t4); die Vorhersage rechnet ohnehin mit den gemessenen Werten.
- Begründung: t4 (Signalgrößen), t3 (Verlauf mit Becher: Unterschied nach 30 min 2,8 K, nach 60 min 2,8 K bei 50 % Verdunstung), t1 (Streuung).
- Priorität: sollte · Aufwand: klein
- Folgen: Hinweistext; bei 50 ml Milch Material „Messbecher“ durch Waage (51,5 g) ersetzen.

**Tech5: Robustheit der Kernaussage als Plausibilitätsprüfung in die Lösung**
- Ebene: technisch, didaktisch
- Stelle: Lösung c und d (Hinweis); optional Aufgabe h als (3)
- Befund: Die Messung bei 10 min trägt die ganze Rechnung. 1 K Ablesefehler ändert *kA* um 8,7 % und $\vartheta_1$, $\vartheta_2$ um je etwa 1,6 K, den Unterschied aber nur um 0,03 K (66 °C: 32,55 und 28,73 °C, 3,82 K; 68 °C: 35,68 und 31,82 °C, 3,86 K). Ebenso Starttemperatur ±1 K (3,82 bis 3,87 K), Raumtemperatur 18 bis 22 °C (3,76 bis 3,95 K). Stärker wirken nur Milchmenge (25 ml: 3,31 K; 35 ml: 4,37 K) und Milchtemperatur (7 °C: 3,67 K). Das ist ein starkes Argument für die Kernaussage und genau die Art Plausibilitätsprüfung, die gewollt ist; in der Lösung fehlt sie.
- Vorschlag: In der Lösung nach d) ergänzen: „Zur Einordnung: Liegt die Messung 1 K daneben (66 oder 68 °C), ändern sich *kA* um 9 % und beide Endtemperaturen um rund 1,6 K, der Unterschied aber nur um 0,03 K. Die Aussage ‚Tasse 1 ist wärmer‘ hängt also nicht an der genauen Messung, die Absolutwerte schon.“ Optional als Studierendenfrage (Zusatz): „Wie ändern sich $\vartheta_1$, $\vartheta_2$ und ihr Unterschied, wenn die Messung 1 K zu hoch war?“
- Begründung: t1, Abschnitte „Messung“ und „Start“.
- Priorität: sollte · Aufwand: klein
- Folgen: ein Absatz in der Lösung; keine Abbildung.

**Tech6: f) erklären, warum sich kA ändert, und beide Anteile nennen**
- Ebene: technisch, didaktisch
- Stelle: Lösung f; Abb. L1
- Befund: (1) Ohne Erklärung wirkt es widersprüchlich, dass derselbe Becher plötzlich ein größeres *kA* hat. Grund: *kA* ist hier eine aus der Messung bestimmte Modellgröße; in c) hat sie die Wärme des Bechers stillschweigend mit erklärt. (2) Die Lösung nennt als Grund für den kleineren Unterschied nur das Dämpfen des Mischsprungs. Zerlegt wie in g sinken beide Anteile: Kaffee-Effekt 2,48 auf 1,98 K (die Milch erhöht die Wärmekapazität nur noch um 11 % statt 15 %), Milch-Effekt 1,38 auf 1,10 K (eigene Rechnung). (3) Der Bilanzraum umfasst in f den Becher; Abb. L1 zeigt nur den Inhalt.
- Vorschlag: In f ergänzen: „Die Messung ist dieselbe, nur das Modell ist ein anderes: In c) musste *kA* auch die Wärme erklären, die der Becher abgegeben hat; mit Becher im Bilanzraum ist *kA* deshalb größer. Die Zeitkonstante $\tau = (m_K c_{p,K} + C_B)/kA = 41{,}0\,\mathrm{min}$ bleibt gleich.“ Und: „Beide Anteile aus g werden kleiner: Die Milch erhöht die Wärmekapazität nur noch um 11 % statt 15 % (Kaffee-Effekt 1,98 statt 2,48 K), und der Becher dämpft den Mischsprung (Milch-Effekt 1,10 statt 1,38 K).“ In Abb. L1 optional eine zweite gestrichelte Linie um Inhalt und Becher mit „Bilanzraum in f“.
- Begründung: eigene Rechnung: $e_G = 0{,}2677$, $e_K = 0{,}2310$ mit $C_B = 255\,\mathrm{J/K}$; Summe 3,08 K wie in der Lösung.
- Priorität: sollte · Aufwand: klein
- Folgen: zwei Sätze in der Lösung; Abb. L1 optional.

**Tech7: Kipppunkt 47 °C als Modellwert kennzeichnen**
- Ebene: technisch
- Stelle: Lösung h (1), Satz „Erst Milch über etwa 47 °C dreht das Ergebnis um“; Hinweis „Fehlvorstellungen“
- Befund: Der Kipppunkt reagiert stark auf *kA*-Unterschiede zwischen den Tassen: 5 % mehr *kA* in Tasse 1 (realistisch durch die höhere Füllung, Tech2) senken ihn auf 37 °C, 5 % weniger heben ihn auf 59 °C (t1). Mit Becher 46,9 °C.
- Vorschlag: „Im Modell mit gleichem *kA* dreht erst Milch über etwa 47 °C das Ergebnis um. Der Wert ist empfindlich: Ist *kA* mit Milch 5 % größer, liegt er bei etwa 37 °C.“
- Begründung: t1, Abschnitt „h1 Kipppunkt mit kA-Faktor“.
- Priorität: sollte · Aufwand: klein
- Folgen: ein Satz.

**Tech8: Abb. L2: Mischsprung von Tasse 2 und Schnittpunkt sichtbar machen**
- Ebene: gestalterisch, technisch
- Stelle: Lösung, Abb. L2
- Befund: Bei $t = 60\,\mathrm{min}$ verdeckt der Punkt von Tasse 1 (34,05 °C) das Kurvenende von Tasse 2 (33,86 °C) und den Sprung auf 30,19 °C; nur ein Strichrest ist zu sehen (Ausschnitt `notizen/L2_ausschnitt.png`). Den Schnittpunkt bei 55,7 min, auf den Lösung e und die Hinweise verweisen, sieht man nicht, weil beide Kurven ab 45 min fast aufeinander liegen.
- Vorschlag: Sprung von Tasse 2 wie bei Tasse 1 als gepunktete Senkrechte von 33,86 auf 30,19 °C, Punkte leicht versetzt oder x-Achse bis 65 min; Wert 33,86 °C klein beschriften; Schnittpunkt mit Marke „≈ 56 min“ und Hinweis „ab hier ist der schwarze Kaffee kühler“. Optional kleiner Ausschnitt 45 bis 60 min.
- Begründung: Abbildung angesehen; Zahlen aus t1 (55,7 min).
- Priorität: sollte · Aufwand: klein
- Folgen: Abbildung neu erzeugen.

**Tech9: Zusätzliche Plausibilitätsprüfungen für die Lösung (kA pro Fläche, verdunstete Masse, Durchmischung)**
- Ebene: technisch, didaktisch
- Stelle: Lösung c) und Hinweise; optional Versuch
- Befund: Die Lösung prüft *kA* nur über die Zeitkonstante gegen eine Quelle. Drei kurze Prüfungen machen die Annahmen greifbar: (1) Becher mit 8 cm Innendurchmesser: wärmeabgebende Fläche rund 230 cm², also $k = kA/A \approx 15\,\mathrm{W/(m^2\,K)}$ (mit Becher 20); das passt zu freier Konvektion (rund 5 bis 8) plus Strahlung (rund 6 bis 7) plus Verdunstung. (2) Verdunstete Masse in 60 min je nach Verdunstungsanteil 2 bis 8 g, bei 50 % rund 5 g, also rund 2,5 % des Kaffees (t3); die Annahme „verdunstete Masse vernachlässigt“ ist damit begründet (Einfluss auf den Unterschied rund 0,1 bis 0,2 K). Im Versuch lässt sich das mit einer Küchenwaage an Becher 2 messen und zeigt, wie viel der abgegebenen Wärme verdunstet ist (rund 2,4 kJ je g). (3) Ideale Durchmischung: Mit reiner Wärmeleitung wäre Bi ≈ 0,2 (zu groß), die freie Konvektion im Becher hält den Inhalt aber weitgehend gleich warm (Bi mit innerer Konvektion ≈ 0,05, t5); vor dem Messen umrühren.
- Vorschlag: In c) nach „Zur Einordnung“ einen Satz zu (1); in den Hinweisen „Was die Rechnung weglässt“ einen Satz zu (2); (3) als Halbsatz beim Versuch. Werte als Abschätzung kennzeichnen.
- Begründung: t2, t3, t5; Formelsammlung Abschnitt 1 (freie Konvektion, waagerechte Platte und senkrechter Zylinder) für die Größenordnung von α.
- Priorität: kann · Aufwand: klein
- Folgen: Text; Material Versuch ggf. Waage (siehe Tech3).

**Tech10: Kleinigkeiten in Notation und Genauigkeit**
- Ebene: sprachlich, technisch
- Stelle: Lösung c bis f; Aufgabe, Ergebnisse
- Befund: (1) $T_K(60\,\mathrm{min}) = 307{,}01\,\mathrm{K}$: Index K (Kaffee) neben Einheit K kann verwirren. (2) Ergebnisse mit vier Stellen (0,3402 W/K, 34,05 °C) aus einer Messung mit ±1 K; das ist als Kontrollwert in Ordnung, sollte aber nicht als Genauigkeit gelesen werden (Tech5). (3) 200 ml Kaffee bei 80 °C wiegen 194 g, nicht 200 g (ρ_Wasser bei 80 °C rund 972 kg/m³, aus dem Gedächtnis); durch die Annahme „Stoffdaten unabhängig von der Temperatur“ gedeckt, Einfluss auf den Unterschied rund +0,1 K. (4) Mögliche Fehlvorstellung für die Hinweise: „Milchkaffee ist heller und strahlt deshalb weniger ab.“ Im Infraroten strahlen schwarzer Kaffee und Milchkaffee gleich (Emissionsgrad von Wasser rund 0,95, aus dem Gedächtnis); die Farbe spielt keine Rolle.
- Vorschlag: (1) optional $T_{K}$ in der Lösung bei der ersten Verwendung als „Kaffee“ ausschreiben oder Index „Kaf“; (2) und (3) nur in den Hinweisen; (4) als zusätzlicher Punkt unter „Fehlvorstellungen“.
- Begründung: siehe Befund.
- Priorität: kann · Aufwand: klein
- Folgen: keine Zahlenänderungen.

## 3. Was bleiben sollte

- Das Modell mit einem *kA* aus einer Messung: einfach, zur Folie 8 passend, und die Kernaussage ist robust (Tech5). Die Kalibrierung über die Messung macht f elegant: $\vartheta_1$ ändert sich kaum (34,05 auf 34,04 °C), nur der Mischsprung.
- Die Erklärung über die abgegebene Wärme in e) mit der Kontrolle $(Q_2 - Q_1)/(m_K c_{p,K} + m_M c_{p,M}) = 3{,}85\,\mathrm{K}$: physikalisch genau der richtige Kern gegen „Energie bleibt erhalten“.
- Die Zerlegung in Kaffee-Effekt und Milch-Effekt in g und der Kipppunkt in h (1); daraus folgt allgemein, dass Tasse 2 immer kühler ist, wenn die Milch nicht wärmer als der Raum ist (beide Anteile dann ≥ 0, im Skript geprüft). Das könnte die Lösung als einen Satz ausdrücklich sagen.
- h (2) mit der oberen Schranke „höchstens Raumtemperatur“: technisch sauber und richtig begründet (1,95 K bestätigt).
- Ein Thermometer für alle Becher und das Messen der Milchtemperaturen im Versuch.
- Die ehrliche Liste „Was die Rechnung weglässt“ und die Quellen der Arbeitswerte (Zahlen plausibel: τ = 41 min, Becher 255 J/K = 31 % der Wärmekapazität des Kaffees).

## 4. Offene Fragen an die Tutoriumsleitung

1. Teil g: Soll der Cappuccino als Bild bleiben (dann Variante B aus Tech1 mit ausdrücklicher Annahme) oder reicht „heiße Milch“ (Variante A, empfohlen)?
2. Gibt es einen Vorversuch zu Hause oder am Lehrstuhl? Mit drei Bechern lassen sich Streuung, tatsächliche Zeitkonstante und die Abweichung der Absolutwerte (Tech2, Tech4) vorab sehen; das würde die Erwartungswerte in den Hinweisen absichern.
3. Stehen im Tutorium wirklich drei gleiche Becher, eine Küchenwaage und eine Steckdose für den Wasserkocher bzw. eine Thermoskanne mit mindestens 0,7 l zur Verfügung?
4. Darf der Versuch mit 50 ml Milch laufen (größeres Signal), auch wenn die Aufgabe mit 30 ml rechnet?
5. Quelle Ferreira: Laut Suchtreffern heißen die Arbeiten „Radiation in the coffee cup“ (Phys. Educ., 2024) und „Forced convection and the coffee cup“ (Phys. Educ., 2025, DOI 10.1088/1361-6552/adb6ea). Ob „60, 035001“ und die Steigung 0,0241 1/min in Abb. 6 dazu gehören, konnte ich nicht prüfen (Volltext gesperrt). Bitte von der Quellenrolle bestätigen lassen.

## Anhang: eigene Rechnungen und Websuche

| Skript in `notizen/rechnung/` | Inhalt | wichtigste Ergebnisse |
|---|---|---|
| `t1_linear.py` | unabhängige Nachrechnung, Empfindlichkeit | alle Lösungszahlen bestätigt; d) kippt bei kA·1,251 (mit Becher 1,188); g) kippt bei kA·0,944 in Tasse 1; Kipppunkt 47,0 °C (±5 % kA: 36,8 bis 58,5 °C) |
| `t2_physikalisch.py` | Wärmeabgabe nach Mechanismen (Formelsammlung, Strahlung, Verdunstung) | ungeeicht zu schnell (Verdunstung überschätzt), deshalb Eichung auf die Messung |
| `t3_varianten.py` | Verdunstungsanteil 0 bis 60 %, Füllhöhe, Massenverlust, kA aus 30-min-Messung | Unterschied ohne Becher 2,8 bis 4,0 K, mit Becher 2,0 bis 3,1 K; $\vartheta_1$ 35 bis 40 °C statt 34 °C; verdunstet 2 bis 8 g |
| `t4_versuch.py` | Signalgrößen im Versuch, Erwärmung der Milch im Glas | Becher 1 minus 2: 2,6 bis 3,1 K; Becher 3 minus 2: 0,3 bis 1,5 K; Milch im Glas nach 60 min 13 bis 17 °C |
| `t5_biot.py` | Biot-Zahl, innere Konvektion | Bi 0,20 bis 0,27 (Leitung), etwa 0,05 mit innerer Konvektion |
| `t6_schaum.py` | Dämmwirkung einer Schaumschicht in g | schon kA −30 % für 15 min dreht g um |

Websuche (9 von 10 genutzt, davon 3 Seitenabrufe ohne Ergebnis): Ferreira-Volltext ([repositorio.ucp.pt](https://repositorio.ucp.pt/bitstreams/facfcba7-6c1c-4700-92ec-4d50ef8a2565/download)) durch Bot-Sperre nicht lesbar; Condoret 2007 ([journals.flvc.org](https://journals.flvc.org/cee/article/view/122462/121419)) mit HTTP 403 gesperrt, Tab. 2 daher nicht geprüft; zu Milchschaum (Dämmung, Dichte, Standzeit) keine belastbaren Messdaten gefunden; Thermometer-Genauigkeit nur aus Suchtreffern (Datenblatt PCE-ST 1 über [conrad.com](https://asset.conrad.com/media10/add/160267/c1/-/gl/815712761DS00/tehnicni-podatki-2452652-pce-instruments-pce-st-1-vbodni-termometer.pdf), nicht geöffnet). Stoffwerte ohne Link (Dampfdruck, Wasserdichte, Emissionsgrad) stammen aus dem Gedächtnis bzw. der Magnus-Formel im Skript.
