# Bericht Prüferin S (Studierende): Kaffee mit Milch

Stand 29.10.2026. Grundlage: Aufgabenblatt (PDF als Bild angesehen, Markdown zum Nachlesen), Formelsammlung 2026, Foliensatz 05 Folien 1 bis 21. Lösung erst nach eigener Bearbeitung aller Teile geöffnet (Notizen davor: `notizen/protokoll_vor_loesung.md`). Eigene Rechnungen: `notizen/rechnung.py`, `notizen/check_loesung.py`. Keine Websuche.

## 1. Gesamturteil

Als Studentin finde ich die Aufgabe stark: eine Alltagsfrage, bei der mein Bauchgefühl wirklich unsicher ist, ein klarer Rechenweg (Mischen, DGL, kA aus Messung) und mit e) ein echter Aha-Moment, warum „Energie bleibt erhalten“ hier nicht trägt. Alle Ergebnisse auf dem Blatt konnte ich selbst reproduzieren (a bis h, siehe Protokoll). Das größte Problem ist, dass die Vorhersagen ausgehebelt werden: In g) steht das Ergebnis direkt unter „Sagen Sie zuerst voraus“, und die Ergebnisse von d) verraten Frage 1, sobald man umblättert. Dazu kommen einige kleine Unklarheiten (kA ohne Gleichung, m c_p für das Gemisch, Becher beim Mischen in f), an denen ich ohne Lösung hängen geblieben wäre oder falsch weitergerechnet hätte. Mit rund 85 bis 95 Minuten für alle Teile füllt die Aufgabe allein ein Tutorium; nach kleinen Textänderungen ist sie einsatzbereit.

## 1a. Protokoll je Teil

Zeiten: meine Schätzung für eine durchschnittliche Studentin im Tutorium (mit Taschenrechner, ohne Lösung).

| Teil | Zeit | Wo ich hänge, was unklar ist | Ergebnis auf dem Blatt | Motivation |
|---|---|---|---|---|
| Frage 1 | 2 bis 3 min | Nichts. Ich hätte „Tasse 2“ getippt, weil der Kaffee „länger heiß bleibt“. | Die Antwort steht auf Seite 2 (d). Wer beim Austeilen durchblättert, sieht sie. | hoch, Alltag, WG |
| a) | 5 min | Masse aus ρV, dann gewichtetes Mittel mit m c_p. Leicht. | hilft (Kontrolle), nimmt nichts vorweg | Aufwärmen |
| b) | 12 bis 15 min | (1) Welches der beiden Bilder von Tasse 1 soll ich nehmen, und kommt die Tassenwand in den Bilanzraum? (2) kA ist auf dem Blatt nicht mit einer Gleichung eingeführt; ich muss Q̇_ab = kA(ϑ − ϑ_u) selbst annehmen. k kenne ich aus den Folien 1 bis 21 noch nicht. (3) Was ist „m c_p“ für Kaffee mit Milch? | Die Lösungsformel steht da. Gut als Rettungsanker, aber man ist versucht, die Herleitung zu überspringen. | mittel, DGL ist Pflicht |
| c) | 5 min | Sekunden statt Minuten (mit Minuten kommt 20,42 heraus). Dass Tasse 2 noch ohne Milch ist, steht zum Glück da. | hilft | gut, „aus Messung bestimmen“ fühlt sich nach Ingenieurin an |
| d) | 10 min | Für Tasse 1 m c_p = 957,7 J/K, für Tasse 2 erst 836,0 J/K, dann mischen. Das musste ich mir selbst klarmachen; die Formel aus b) sagt es nicht. | hilft, verrät aber Frage 1 | hoch, Auflösung |
| e) | 10 min | Q_2 nur für den schwarzen Kaffee (80 → 33,86 °C), Mischen ohne Wärmeabgabe. Die Verbindung zu d) habe ich erst gesehen, als ich Q_2 − Q_1 = 3,69 kJ durch 957,7 J/K geteilt habe: genau 3,85 K. Dieser Schritt steht nicht auf dem Blatt. | hilft | sehr hoch, das ist der Kern |
| f) | 12 bis 15 min | Nimmt der Becher am Mischen teil? Nur dann kommen 34,04 °C heraus. Ohne Becher im Mischen erhalte ich 33,51 °C und 30,19 °C und suche den Fehler. Überraschend: ϑ_K(60 min) bleibt 33,86 °C, und ϑ_1 ändert sich kaum. Das Blatt fragt nicht, warum. | hilft beim Finden des Fehlers | eher mühsam (alles noch einmal), die Warum-Frage wäre spannend |
| g) | 8 bis 10 min | Stoffdaten des Schaums fehlen (ich nehme die der Milch). „Ihr Mitbewohner trinkt Cappuccino“, aber Schaum in beide Tassen: wer trinkt was? Schaum schwimmt oben, „ideal durchmischt“ wirkt hier seltsam. | Verrät die Vorhersage sofort (37,18 > 35,99) | wäre die spannendste Wendung, wenn sie nicht verraten wäre |
| h) | 12 bis 15 min | (1) Algebra mit ϑ_M auf beiden Seiten; 47,0 °C ist überraschend (ich hätte 20 °C oder 33,86 °C getippt). (2) Mein erster Gedanke war: „Milch höchstens 20 °C < 47 °C, also nein.“ Das trägt aber nicht, weil Tasse 1 die 5 °C-Milch bekommt. Erst der Hinweis „mit den Ergebnissen aus e)“ führt zur Abschätzung 1,83 kJ < 3,69 kJ. | hilft in (1); in (2) gibt es kein Ergebnis | hoch, aber anspruchsvoll |
| Versuch | 5 min Aufbau, 5 min Abschluss, sonst nebenher | Milchtemperatur bei t = 0 wird nicht gemessen, für Becher 1 brauche ich sie aber. Keine Waage für die Bechermasse (Teil f) und 30 ml mit dem Messbecher sind ungenau. Wann sage ich vorher? Teil f erreiche ich erst gegen Minute 55 bis 60. Mit einem Thermometer dauert jede Runde. | | sehr hoch, besonders Becher 3 |

**Gesamt:** Frage 1 bis h rund 85 bis 95 min, Kern (Frage 1, a bis e) rund 45 bis 50 min. Was ich mitnehme: Wie viel Wärme abgeht, hängt vom Temperaturverlauf ab; Energieerhaltung gilt für Tasse plus Umgebung. Und: kA aus einer Messung „schluckt“ Modellfehler (f).

**Vergleich mit der Lösung:** Die Lösung deckt meine Stolperstellen fachlich ab (m c_p je Tasse in b, Kontrolle 3,85 K in e, Becher beim Mischen in f, Kipppunkt-Falle in h(2)). Diese Klärungen stehen aber nur in der Lösung, nicht als Hinweis auf dem Blatt. Alle Zahlen der Lösung habe ich nachgerechnet und bestätigt, auch Schnittpunkt 55,7 min, Kaffee-Effekt 2,48 K, Milch-Effekt 1,38 K und −3,67 K, (T − T_u)^(4/3)-Variante 37,65 und 33,34 °C, Versuch nach 30 min 2,71 K.

## 2. Änderungsvorschläge

**Stud1: Ergebnis in g) ohne Zuordnung angeben**
- Ebene: didaktisch
- Stelle: Aufgabe, Teil g
- Befund: Direkt unter „Sagen Sie zuerst voraus, welche Tasse nach 60 Minuten wärmer ist“ steht ϑ_1 = 35,99 °C, ϑ_2 = 37,18 °C. Die Vorhersage ist damit wertlos; das ist ein Widerspruch im Blatt.
- Vorschlag: Ergebniszeile ersetzen durch: „Ergebnis (Zuordnung zu den Tassen selbst bestimmen): 35,99 °C und 37,18 °C“. Die Vorgabe „Ergebnis am Ende jedes rechnenden Teils“ bleibt erfüllt, und man kann trotzdem kontrollieren.
- Begründung: eigene Rechnung (`notizen/rechnung.py`): ϑ_1 = 35,99 °C, ϑ_2 = 37,18 °C. Die Wendung in g) (Tasse 2 jetzt wärmer) ist die stärkste Überraschung der Aufgabe und braucht eine ehrliche Vorhersage.
- Priorität: muss · Aufwand: klein
- Folgen: keine für Lösung, Zahlen, Abbildungen

**Stud2: Frage 1 vor dem Austeilen abstimmen lassen**
- Ebene: didaktisch, praktisch
- Stelle: Lösung, Hinweise für die Tutoriumsleitung (und Versuch Schritt 1)
- Befund: Die Ergebnisse von d) (34,05 °C gegenüber 30,19 °C, „Welche Tasse ist kühler?“) stehen auf Seite 2. Wer das Blatt bekommt und durchblättert, kennt die Antwort auf Frage 1, bevor er eine Vermutung notiert. In der Word-Fassung kann d) je nach Umbruch sogar näher an Frage 1 rutschen.
- Vorschlag: In die Hinweise für die Tutoriumsleitung: „Frage 1 vor dem Austeilen vorlesen oder nur Seite 1 zeigen und per Handzeichen abstimmen lassen; Ergebnis an die Tafel.“ Versuch Schritt 1 dazu passend: „Stimmen Sie über Frage 1 ab, bevor Sie rechnen.“
- Begründung: Vorab-Fragen wirken nur, wenn die Vermutung vor der Auflösung fest steht; das Abstimmungsergebnis an der Tafel macht das Ende (e, Versuch) spannender.
- Priorität: sollte · Aufwand: klein
- Folgen: keine

**Stud3: Wärmeabgabe als Gleichung in die Annahme**
- Ebene: didaktisch, technisch
- Stelle: Aufgabe, Annahmen, dritter Punkt
- Befund: kA wird nur als „konstantes Produkt“ eingeführt. Bis zur Bilanzierung (Folien 1 bis 21) kommt k nicht vor; die Formelsammlung enthält keine Gleichung dafür. Ich musste Q̇_ab = kA(ϑ − ϑ_u) erraten. In der Lösung steht die Gleichung erst in Abb. L1.
- Vorschlag: „Die gesamte Wärmeabgabe an die Umgebung (Konvektion, Strahlung, Verdunstung und Wärmedurchgang durch die Tassenwand) wird mit $\dot Q_{ab} = kA\,(\vartheta - \vartheta_u)$ beschrieben. Das Produkt $kA$ ist konstant und mit und ohne Milch gleich. Die verdunstete Masse wird vernachlässigt.“
- Begründung: Foliensatz 05, Folie 8, liefert nur dU/dt = Q̇_zu − Q̇_ab + Q̇_KV; der Ansatz für Q̇_ab fehlt im Material. Mit der Gleichung bleibt die eigentliche Leistung (Bilanz aufstellen, DGL lösen) erhalten.
- Priorität: sollte · Aufwand: klein
- Folgen: keine; Lösung b) passt schon

**Stud4: In d) nach der Wärmekapazität je Tasse fragen**
- Ebene: didaktisch
- Stelle: Aufgabe, Teil d (bezieht sich auf b)
- Befund: Die Formel in b) enthält „m c_p“. Für Tasse 1 (Gemisch) ist unklar, ob (m_K + m_M) mal eine gemittelte Wärmekapazität oder die Summe gemeint ist; für Tasse 2 muss man erkennen, dass bis 60 min nur der Kaffee abkühlt. Genau das sind zwei der vier typischen Fehler, die die Lösung selbst nennt.
- Vorschlag: d) ergänzen: „Berechnen Sie die Temperaturen ϑ_1 und ϑ_2 beider Tassen nach 60 Minuten, bei Tasse 2 direkt nach dem Zugießen der Milch. Welche Wärmekapazität $m\,c_p$ setzen Sie jeweils ein? Welche Tasse ist kühler?“
- Begründung: Lösung b) letzter Satz und „Typische Fehler“ (in Tasse 1 nur m_K c_p,K; in Tasse 2 schon während der 60 min mit Milch). Eine Frage statt eines Hinweises verrät nichts, lenkt aber den Blick. Zahlen: m c_p = 957,7 J/K bzw. 836,0 J/K.
- Priorität: sollte · Aufwand: klein
- Folgen: keine

**Stud5: In f) klarstellen, dass der Becher mitgemischt wird (Variante B: Warum-Frage)**
- Ebene: technisch, didaktisch
- Stelle: Aufgabe, Teil f
- Befund: „haben immer die Temperatur ihres Inhalts“ lässt offen, ob der Becher beim Zugießen der Milch mitgemischt wird. Das Blattergebnis 34,04 °C gilt nur dann. Übernimmt man ϑ_1,0 = 70,47 °C aus a) und mischt Tasse 2 ohne Becher, kommen 33,51 °C und 30,19 °C heraus; ich hätte lange nach dem Fehler gesucht. Außerdem ist f) als reine Wiederholung eher langweilig, obwohl ein schöner Befund drinsteckt: ϑ_K(60 min) = 33,86 °C ändert sich nicht, weil kA aus derselben Messung neu bestimmt wird.
- Vorschlag: Variante A (Klarstellung): „… Sie wurden vorgewärmt und haben immer die Temperatur ihres Inhalts, auch beim Zugießen der Milch.“ Variante B (zusätzlich): „Warum ändert sich die Temperatur des schwarzen Kaffees in Tasse 2 vor dem Zugießen dadurch nicht?“
- Begründung: eigene Rechnung: mit Becher im Mischen ϑ_1,0 = 72,47 °C, ϑ_1 = 34,04 °C, ϑ_2 = 30,96 °C (wie Blatt); ohne 33,51 °C und 30,19 °C. ϑ_K(60) = ϑ_u + (ϑ_K,0 − ϑ_u)·(47/60)^6 = 33,86 °C, unabhängig von der Wärmekapazität. Die Lösung sagt das in einem Satz („kühlt mit derselben Zeitkonstante ab wie in der Messung“).
- Priorität: sollte (A), kann (B) · Aufwand: klein
- Folgen: Lösung f) bei Variante B um zwei Sätze ergänzen; Zahlen unverändert

**Stud6: In e) die Kontrolle Q_2 − Q_1 = (m c_p)_1 (ϑ_1 − ϑ_2) verlangen**
- Ebene: didaktisch
- Stelle: Aufgabe, Teil e
- Befund: „Erklären Sie damit das Ergebnis aus d)“ ist offen; die quantitative Verbindung (3,69 kJ / 957,7 J/K = 3,85 K) steht nur in der Lösung. Gerade diese Rechnung brauche ich später in h(2).
- Vorschlag: „… Erklären Sie damit das Ergebnis aus d), und prüfen Sie, ob der Temperaturunterschied aus d) zur Differenz $Q_2 - Q_1$ passt. Hat Ihr Mitbewohner recht?“
- Begründung: eigene Rechnung: Q_2 − Q_1 = 3,690 kJ = 957,7 J/K · 3,853 K. Plausibilitätsprüfungen sind ausdrücklich gewollt (Vorgaben); diese ist kurz und zeigt die Energieerhaltung auf einen Blick.
- Priorität: sollte · Aufwand: klein
- Folgen: keine; Lösung e) enthält die Kontrolle schon

**Stud7: Wortlaut und Stoffdaten in g)**
- Ebene: sprachlich, technisch
- Stelle: Aufgabe, Teil g
- Befund: „Ihr Mitbewohner trinkt Cappuccino“, aber Schaum kommt „in beide Tassen“: Wer trinkt was? Stoffdaten des Schaums fehlen (die Lösung setzt stillschweigend die der Milch ein).
- Vorschlag: „Am nächsten Tag gibt es Cappuccino: Statt kalter Milch kommt in beide Tassen Milchschaum mit $\vartheta_S$ (gleiche Masse und Stoffdaten wie die Milch, Becher wieder vernachlässigt). Sagen Sie zuerst mit kurzer Begründung voraus, welche Tasse nach 60 Minuten wärmer ist. Prüfen Sie Ihre Vorhersage dann mit den Gleichungen aus d).“ In der Lösung unter „Was die Rechnung weglässt“ einen Satz: Schaum schwimmt oben und mischt sich nicht sofort.
- Begründung: Lösung g) rechnet mit m_M c_p,M = 121,7 J/K und T_S statt T_M; das sollte auf dem Blatt stehen.
- Priorität: sollte · Aufwand: klein
- Folgen: keine

**Stud8: Versuch: Messablauf und Material ergänzen**
- Ebene: praktisch
- Stelle: Aufgabe, Versuch
- Befund: (1) Die Milchtemperatur bei t = 0 wird nicht gemessen, ist aber für die Vorhersage von Becher 1 nötig. (2) Becher 1 wird nach dem Zugießen nicht gemessen, obwohl das Teil a direkt prüfen würde. (3) Für „kA wie in Teil f (mit Becher)“ braucht man die Bechermasse; eine Waage fehlt. (4) 30 ml mit einem Messbecher sind ungenau; ±5 ml Milch verschieben Becher 2 um ±0,44 K. (5) Umrühren vor der Messung steht nur in den Hinweisen der Lösung, nicht auf dem Blatt. (6) Mit einem Thermometer verschiebt sich jede Messung; bei 34 °C kühlt ein Becher um rund 0,3 K pro Minute. (7) Die Tabellenzeilen sind zum Eintragen von Hand sehr niedrig.
- Vorschlag: Material: „… Küchenwaage …“. Schritt 2: „t = 0: Becher vorwärmen und wiegen, je 200 ml einfüllen, umrühren, Starttemperatur und Milchtemperatur messen. Becher 1 bekommt 31 g Milch (abwiegen) sofort; umrühren und Becher 1 messen (Kontrolle von Teil a). …“ Zusatzzeile unter die Schritte: „Vor jeder Messung umrühren, Thermometer immer mittig und gleich tief, Uhrzeit jeder Messung notieren.“ Tabellenzeilen höher setzen.
- Begründung: eigene Rechnung mit Becher: Becher 1 34,04 °C, Becher 2 30,96 °C, Becher 3 (Milch 20 °C) 32,47 °C; die Abstände von 1,5 bis 3,1 K sind messbar, aber nur bei sauberem Ablauf. ϑ(10 min) ±1 K verschiebt die Vorhersage für Becher 1 um ±1,6 K, den Abstand Becher 1 zu 2 aber kaum (3,05 bis 3,09 K).
- Priorität: sollte · Aufwand: klein
- Folgen: Hinweise zum Versuch in der Lösung anpassen

**Stud9: Umfang an die Sitzung anpassen und Zeitplan für den Versuch**
- Ebene: inhaltlich (Umfang), praktisch
- Stelle: Aufgabe, Teile f und h; Lösung, Hinweise
- Befund: Ich brauche für alles rund 85 bis 95 min, den Kern (Frage 1, a bis e) rund 45 bis 50 min. Das ist eine ganze Sitzung. Die Aufgabe heißt „Aufgabe 1“; gibt es in Tutorium 5 weitere Aufgaben, passt sie nicht. Für den Versuch: Die Vorhersage (Schritt 4) braucht Teil f, den die meisten erst gegen Minute 55 bis 60 erreichen, der Versuch endet aber bei Minute 60 bis 65.
- Vorschlag: Wenn weitere Aufgaben folgen: f) wie h) als *Zusatzfrage* kennzeichnen. In die Hinweise einen Zeitplan: Versuch in den ersten 5 Minuten starten; die Vorhersage für die Becher rechnet die Tutoriumsleitung gegen Minute 40 bis 45 an der Tafel mit den gemessenen Werten vor (oder eine Gruppe, die schon bei f ist).
- Begründung: Protokoll je Teil (Abschnitt 1a). Annahme 90 min laut Auftrag.
- Priorität: sollte · Aufwand: klein bis mittel
- Folgen: Versuch Schritt 3 verweist auf Teil f; bei f als Zusatz dort „wie in Teil c oder f“ schreiben

**Stud10: Bilanzraum in b) eindeutig benennen**
- Ebene: sprachlich, didaktisch
- Stelle: Aufgabe, Teil b
- Befund: Abb. 1 zeigt Tasse 1 zweimal (t = 0 beim Zugießen und t = 60 min). Unklar ist auch, ob die Tassenwand in den Bilanzraum gehört; die Lösung (Abb. L1) legt ihn um den Inhalt.
- Vorschlag: „Zeichnen Sie den Bilanzraum um den Inhalt von Tasse 1 in Abb. 1 (rechts, nach dem Zugießen) ein …“
- Begründung: Lösung, Skizze: „Bilanzraum um den Tasseninhalt“. Bis e) wird die Tasse vernachlässigt; in f) kommt sie dazu, das ist ein schöner Kontrast, wenn der Bilanzraum in b) klar um den Inhalt liegt.
- Priorität: kann · Aufwand: klein
- Folgen: keine

**Stud11: Tipp für h(1): Linearität nutzen**
- Ebene: didaktisch
- Stelle: Aufgabe, Teil h(1)
- Befund: Die Algebra mit ϑ_M auf beiden Seiten kostet 10 Minuten und ist fehleranfällig. Dabei liegen nach d) und g) schon zwei Wertepaare vor.
- Vorschlag: „(1) … (ohne Becher)? Tipp: ϑ_1 und ϑ_2 hängen linear von der Milchtemperatur ab; d) und g) liefern je zwei Werte.“
- Begründung: Differenz ϑ_1 − ϑ_2 = 3,853 K bei 5 °C und −1,192 K bei 60 °C; linear auf null: 5 °C + 55 K · 3,853/5,045 = 47,0 °C, wie Blatt und Lösung. Der algebraische Weg der Lösung bleibt daneben gültig.
- Priorität: kann · Aufwand: klein
- Folgen: Lösung h(1) um einen Satz zum zweiten Weg ergänzen

**Stud12: Typische Fehler in der Lösung ergänzen**
- Ebene: didaktisch
- Stelle: Lösung, Hinweise für die Tutoriumsleitung, „Typische Fehler“
- Befund: Weitere Fehler, die mir beim Rechnen passiert wären oder fast passiert sind, fehlen in der Liste.
- Vorschlag: ergänzen: „t in Minuten eingesetzt (kA = 20,42 statt 0,3402 W/K; die Temperaturen stimmen trotzdem, wenn auch in d) Minuten stehen); Vorzeichen in der Bilanz vergessen (Temperatur steigt, Plausibilität!); Q_2 mit Kaffee und Milch berechnet (44,19 kJ statt 38,57 kJ); in f) den Becher nicht mitgemischt (33,51 und 30,19 °C); in h(2) nur mit dem Kipppunkt argumentiert (20 °C < 47 °C), obwohl Tasse 1 die 5 °C-Milch bekommt.“
- Begründung: eigene Rechnungen (`notizen/rechnung.py`, `notizen/check_loesung.py`).
- Priorität: kann · Aufwand: klein
- Folgen: nur Lösung

**Stud13: Abkürzung für die Vorhersage im Versuch**
- Ebene: praktisch, didaktisch
- Stelle: Lösung, Hinweise zum Versuch (optional als Plausibilitätsfrage in d)
- Befund: Für den schwarzen Kaffee braucht man weder kA noch Bechermasse: 60 min sind sechsmal 10 min.
- Vorschlag: Hinweis: „ϑ_K(60 min) = ϑ_u + (ϑ_K,0 − ϑ_u)·r^6 mit r = (ϑ_K(10 min) − ϑ_u)/(ϑ_K,0 − ϑ_u)“. Für Becher 2 und 3 reicht dann das Mischen mit der gemessenen Milchtemperatur.
- Begründung: (47/60)^6 = 0,2310, also 33,86 °C wie in d) und f). Macht die Vorhersage im Versuch in zwei Minuten möglich und erklärt nebenbei, warum ϑ_K(60) in f) gleich bleibt (Stud5).
- Priorität: kann · Aufwand: klein
- Folgen: keine Zahlen

## 3. Was bleiben sollte

- Die WG-Geschichte und das Mitbewohner-Zitat „Die Energie bleibt ja erhalten“: Das ist genau die Fehlvorstellung, die ich auch hatte.
- kA aus einer Messung bestimmen (c) statt vorgeben: fühlt sich nach echtem Ingenieursvorgehen an.
- e) als Herzstück: Wärmeabgabe vergleichen und damit d) erklären.
- Die Wendung in g) (heißer Schaum dreht das Ergebnis) und der überraschende Kipppunkt 47,0 °C in h(1).
- h(2) mit der Abschätzung 1,83 kJ < 3,69 kJ: elegant, und der Hinweis „mit den Ergebnissen aus e)“ ist nötig.
- Abb. 1 mit Zeitstrahl, Q̇_ab-Pfeilen und den gesuchten Temperaturen: sofort verständlich.
- Ergebnisse zur Selbstkontrolle bei a) bis f) und h(1); die Formel in b) als Rettungsanker.
- Der Versuch mit drei Bechern, besonders Becher 3 (Milch draußen) als zusätzlicher Test der Rechnung.
- Die Lösung mit Kontrolle in e), Zerlegung in Kaffee- und Milch-Effekt in g) und der Begründung, warum der Kipppunkt h(2) nicht allein entscheidet.

## 4. Offene Fragen an die Tutoriumsleitung

1. Ist „Kaffee mit Milch“ die einzige Aufgabe in Tutorium 5, oder folgen weitere? Davon hängt Stud9 ab.
2. Bekommen die Studierenden das Blatt vorab (z. B. im Lernraum)? Dann wirken Frage 1 und die Vorhersage in g) nur, wenn die Ergebnisse dort nicht direkt lesbar sind (Stud1, Stud2).
3. Wer führt den Versuch durch: die Tutoriumsleitung vorne oder eine Gruppe? Gibt es mehr als ein Thermometer?
4. Wurde der Wärmedurchgang (k) vor Tutorium 5 schon in der Vorlesung behandelt? Wenn nicht, ist Stud3 wichtiger.
5. Geht die Lösung mit „Hinweisen für die Tutoriumsleitung“ und „Quellen“ an die Studierenden? Dann verwirrt dort „c_p wie in Tutorium 8“ (Vorgriff auf ein späteres Tutorium).
6. Was bedeutet „(neu)“ hinter „Aufgabe 1“? Ist das eine Kennzeichnung des Lehrstuhls? Wenn nicht, für die Studierenden streichen.
