# Abnahme Codex (Rolle X2)

## Urteil: mit kleinen Korrekturen

Die neue Kaffee-Aufgabe ist rechnerisch konsistent und nach den unten genannten Korrekturen freigabereif. Die eigene, vom Paketmodell unabhängige Rechnung bestätigt 106 Zahlenvergleiche einschließlich der Zusatzfrage, Sensitivitäten und Fehlrechnungen. Alle 50 Entscheidungen wurden abgeglichen. Die wesentlichen angenommenen Änderungen sind umgesetzt; abgelehnte Varianten und die Vertagung des FVT-Rahmens wurden eingehalten. Restpunkte betreffen eine fachliche Erklärung, die Bilanzraumgrafik, Satz und Detailgestaltung sowie einen alten Teilverweis. Eine sachfremde Änderung der `.gitignore` sollte zurückgenommen werden.

**Prüfstand:** 30.10.2026, Zweig `claude/kaffee-pruefung-sgvo1r`, Commit `560b8d4c9b18860d6688a5e8f7a8be5d78a5f537`. Vergleich gegen `origin/main` bei `500ed249e3a710672a63a287414a54ac14c8ab8d` und gegen die Originalfassungen in `material/A_aufgabe/` und `material/B_loesung/`. Der Bericht liegt auf dem eigenen Zweig `codex/kaffee-abnahme-x2`. Aufgabe, Lösung und Paket wurden bei dieser Abnahme nicht verändert.

**Leseregel:** Zweiter Auftrag aus `AGENTS.md`. Die erste Entscheidungsliste ist zusammen mit den später beschlossenen S1 bis S11 auszuwerten: Warme Milch ist jetzt f, Becher ist g als Vertiefung; die frühere h steht nur in den Hinweisen. Diese Änderungen und die eigene Studierendenlösung sind ausdrücklich entschieden. Andere Rollenberichte wurden für diese Abnahme nicht gelesen.

Stellenangaben unten sind Zeilen des Prüfstands. Abkürzungen:

- `W` = `pruefung/Kaffee_Pruefpaket_2026-10-23/umsetzung/Arbeitsordner/`
- `A` = `W/kaffee/Kaffee_Aufgabe.md`
- `L` = `W/kaffee/Kaffee_Loesung.md`
- `S` = `W/sammlung/teile/t5a_kaffee.md`

## Befunde nach Wichtigkeit

### Abnahme 1: Erklärung der Prozessgröße für diesen Bilanzfall präzisieren

**Stelle:** `L:168`, ebenso Studierendenlösung, beide Lösungs-PDFs und die gerenderten DOCX jeweils Seite 7. Bezug: Ä12.

„Wärme ist eine Prozessgröße“ ist richtig. Der folgende Satz „Wie viel abgegeben wird, hängt vom Temperaturverlauf ab, nicht nur von Anfangs- und Endzustand“ ist für das hier verwendete geschlossene, starre System ohne Arbeit missverständlich. Hier folgt gerade `Q_ab = U_Anfang - U_Ende`. Die korrekte Kontrolle direkt darüber in `L:163` bis `166` verwendet genau diesen Zusammenhang. Gleiche Ausgangsenergie bedeutet keine gleiche Wärmeabgabe, weil die beiden Endzustände verschieden sind.

**Korrekturvorschlag:** „Wärme ist eine Prozessgröße. Im hier betrachteten System ohne Arbeit ist die abgegebene Wärme gleich der Abnahme der inneren Energie. Der Temperaturverlauf führt zu verschiedenen Endtemperaturen und damit zu verschiedener Wärmeabgabe.“ Anschließend den zutreffenden Denkfehler des Mitbewohners beibehalten. Ä12 wurde umgesetzt; die beschlossene Formulierung selbst braucht diese fachliche Präzisierung. Keine Ergebniszahl ändert sich.

### Abnahme 2: Bilanzraum in Abb. L1 um den gesamten Becher legen

**Stelle:** `W/kaffee/abb_loesung.py:35`, `grafik/AbbL1_Bilanzraum.png` und `.svg`; beide Lösungs-PDFs und DOCX-Ansichten Seite 5. Bezug: Ä13 und S2.

Die neue äußere Grenze „in g mit Becher“ durchschneidet die Becherwände oberhalb des Flüssigkeitsspiegels. Ihre Oberkante liegt bei `0,4 - 0,22 + 2,82 = 3,0`, die gezeichnete Wand reicht bis `0,4 + 3,0 = 3,4`. Damit liegt ein Teil des Bechers außerhalb des eingezeichneten Bilanzraums, obwohl die Rechnung die gesamte Wärmekapazität `m_B c_B` einschließt.

**Korrekturvorschlag:** Die obere äußere Grenze oberhalb beider Wandenden schließen, seitlich den Henkel und unten den Boden weiterhin einschließen. Die innere Linie für den Tasseninhalt klar davon unterscheiden. Grafiken und beide Lösungsfassungen neu erzeugen. Modell und Zahlen sind bereits richtig.

### Abnahme 3: Satzumbruch in f und verwaiste Quellenzeile beseitigen

**Stelle:** `A:63` bis `67` und die übernommenen Aufgabenteile beider Lösungen; alle drei neuen Einzel-PDFs Seiten 2 und 3. Zusätzlich `L:260`, Lehrlösung als DOCX, LibreOffice-Ansicht Seite 14. Bezug: Ä20 und der ausdrückliche Umfangsauftrag.

Teil f endet auf Seite 2 mit „und erklären“. Seite 3 beginnt isoliert mit „Sie das Ergebnis.“, gefolgt von Ergebniszeile und g; der Rest bleibt überwiegend leer. Die Inhalte sind vollständig, der Umbruch erschwert aber das Lesen. Die DOCX-Lehrlösung benötigt in der geprüften LibreOffice-Ansicht eine weitere Seite nur für den letzten Quellenpunkt zum Rechenskript.

**Korrekturvorschlag:** f samt Kontrollwert zusammenhalten oder vor f umbrechen. Den Quellenblock durch Absatz- oder Umbruchanpassung so setzen, dass die letzte Zeile mit dem vorherigen Punkt zusammenbleibt. Danach PDF und DOCX erneut als Seitenbilder prüfen. Die eigenständige Versuchsseite soll erhalten bleiben. Die Word-Seitenzahl ist rendererabhängig; eine native Microsoft-Word-Ansicht wurde nicht geprüft.

### Abnahme 4: Veralteten Teilverweis in Nachrechnung und Ausgabe korrigieren

**Stelle:** `W/kaffee/nachrechnung_kaffee.py:82` und `84`; `nachrechnung_kaffee_ausgabe.txt:66` und `67`. Bezug: S2.

Beide Zeilen heißen noch „Typischer Fehler f: Becher nicht mitgemischt“. Nach dem beschlossenen Tausch ist der Becher Teil g. Der Fehler wurde beim Ausführen reproduziert; die Zahlen 33,51 und 30,19 °C stimmen.

**Korrekturvorschlag:** Beide Beschriftungen auf g ändern und die gespeicherte Ausgabe neu erzeugen. In Aufgabe, Lösung, Sammlung und Abb. L1 sind die inhaltlichen f/g-Verweise bereits richtig.

### Abnahme 5: Beschlossene Detailgestaltung und Notation abschließen

**Stellen und Entscheidungen:**

- **Ä20:** Aufgabenmarken a) bis g) sind im Aufgabenblock weiterhin nicht fett (`A:48` bis `67`, PDF Seite 2/3; DOCX-Nummerierungsformat ohne Fettschrift). `W/kaffee/build/lehrstuhl.lua:122` ergänzt bei PDF-Bausteinen 10 pt, setzt die entschiedenen Abstände 18 pt davor und 6 pt danach aber nicht ausdrücklich um. Word verwendet hierfür 18/6 pt. Auch der Bildabstand davor ist in Word 6 statt 4 pt.
- **Ä22:** Die erste DOCX-Tabelle hat Spalten von etwa 3,24/3,75/3,24/3,75 cm statt der beschlossenen 3,9/4,1/3,9/4,1 cm. Die Gruppenüberschriften und Teilverweise sind richtig; die Wiederholungszeile ist abgeschaltet. Inhalt geht nicht verloren.
- **Ä24:** Abb. 1 verwendet `Umgebung: ϑ_u`, Abb. L1 weiterhin `Umgebung: T_u` (`abb_loesung.py:42`). Beschreibende Indizes wie `ab`, `zu`, `K`, `M` und `u` stehen weiterhin vielfach kursiv, etwa `A:29` und `L:128`.
- **Ä18:** In Abb. L2 sind Linienarten, beide Sprünge, Ausschnitt, Endwerte und Schnittpunkt korrekt. Beim Sprung zu Beginn fehlt die eigene Beschriftung; beim Schnittpunkt steht nur „etwa 56 min“, die beschlossene Bedeutung „ab hier ist der schwarze Kaffee kühler“ steht im Begleittext (`L:168`, `225`).

**Korrekturvorschlag:** Marken und Abstände in beiden Ausgabewegen vereinheitlichen, die beschlossenen Tabellenbreiten einstellen, Umgebungssymbol und beschreibende Indizes bereinigen sowie die kurzen Bildbeschriftungen ergänzen. Danach insbesondere Umbrüche gemäß Abnahme 3 kontrollieren. Die derzeitigen Ausgaben sind lesbar; dies sind kleine Ausführungslücken, keine Rechenfehler.

### Abnahme 6: Sachfremde Gitignore-Erweiterung zurücknehmen

**Stelle:** `.gitignore:6` und `7`, im Diff gegen `main` neu.

Die Muster `package.json` und `package-lock.json` blenden Paketmanifeste im gesamten Repository aus. Keine der 50 Entscheidungen betrifft diese Änderung. Sie ist für die fachliche Umsetzung und die Abnahme nicht nötig und kann spätere Änderungen an Abhängigkeiten unbemerkt aus der Versionsverwaltung halten.

**Korrekturvorschlag:** Diese beiden neuen Muster entfernen. Falls nur temporäre Bauhilfen gemeint sind, deren konkreten temporären Pfad ausnehmen. Die ergänzten LaTeX- und LibreOffice-Math-Abhängigkeiten im Setup sowie die neuen Bauquellen sind dagegen nachvollziehbare Begleitänderungen zur entschiedenen Ausgabeerzeugung.

## Zahlenprüfung und Konsistenz

Die eigene Rechnung `codex_skripte/x2_eigenrechnung.py` importiert weder `kaffee_modell.py` noch frühere Codex-Skripte. Sie verwendet nur die Aufgabedaten und die globale Bilanz aus Foliensatz 05, Folie 8, die Mischbilanz und die Lösung der Differentialgleichung durch Trennung der Variablen. Das Potenzgesetz wird ebenfalls analytisch integriert. Gelesen wurden die vorgegebenen Textfassungen der Formelsammlung und des Foliensatzes. Interne Werte bleiben ungerundet.

| Größe | Eigene Rechnung | Gedruckt |
|---|---:|---:|
| Mischtemperatur a | 70,466209 °C | 70,47 °C |
| kA ohne Becher | 0,340247765 W/K | 0,3402 W/K |
| d: Tasse 1 / Tasse 2 | 34,046483 / 30,193282 °C | 34,05 / 30,19 °C |
| Q1 / Q2 | 34,880847 / 38,571235 kJ | 34,88 / 38,57 kJ |
| Energiekontrolle d/e | 3,853201 K | 3,85 K |
| f: Tasse 1 / Tasse 2 | 35,992443 / 37,184729 °C | 35,99 / 37,18 °C |
| g: kA mit Becher | 0,444031473 W/K | 0,4440 W/K |
| g: Tasse 1 / Tasse 2 | 34,043556 / 30,964725 °C | 34,04 / 30,96 °C |
| Zusatzfrage: gleiche Milchtemperatur in beiden Tassen | 47,003093 °C | 47,0 °C |
| Zusatzfrage: maximal aus der Raumluft aufgenommene Wärme | 1,826190 kJ | 1,83 kJ |
| Zusatzfrage: verbleibender Abstand | 1,946442 K | 1,95 K |
| Abb. L2: Schnittpunkt vor später Zugabe | 55,744669 min | etwa 56 min |
| Versuch 40 min: Abstand mit / ohne Becher | 2,974290 / 3,700906 K | 2,97 / 3,70 K |

Die übrigen Vergleiche umfassen Massen, Wärmekapazitäten, Kelvinwerte, Exponentialfaktoren, Zeitkonstanten, Wärmeströme, Geometrie, Messabweichungen, kA-Kipppunkte, Zerlegung in Kaffee- und Milchanteil, Tassenwärmer, typische Fehlzahlen und überlineare Wärmeabgabe. Ergebnis: **106/106 innerhalb der angegebenen Rundung**. Aufgabe, beide Lösungsfassungen und Sammlung tragen dieselben Zahlen und Vorgaben. Abb. L2 stimmt mit der Rechnung überein; Abb. L1 hat den geometrischen Restfehler aus Abnahme 2.

Direktes Einsetzen bereits gerundeter Zwischenwerte erzeugt kleine Rundungsreste: In `L:237` ergeben `5 + 55 × 3,85/5,05` zunächst 46,9307 °C; ungerundet sind es 47,0031 °C. In `L:245` ergeben die gedruckten Zwischenwerte 1,9422 K statt ungerundet 1,9464 K. Die Endwerte 47,0 °C und 1,95 K sind korrekt gerundet. Bei diesen vollständig ausgeschriebenen Einsetzungen wäre ein Näherungszeichen oder der Zusatz „mit ungerundeten Werten“ präziser. Das ändert keine Antwort der Aufgabe.

**Grenzen der Zahlenprüfung:** Ausgangsdaten und zitierte Fremdmessungen sind Vorgaben, keine aus der Aufgabe ableitbaren Ergebnisse. Die Abschätzung „38 bis 40 °C“ aus einem Verdunstungsmodell ist ohne dessen vollständige Parameter nicht eindeutig nachrechenbar; sie ist in der Lösung als Abschätzung bezeichnet. Das festgelegte Potenzgesetz mit Exponent 4/3 liefert unabhängig 37,653280 und 33,340555 °C, also die gedruckten 37,65 und 33,34 °C. Neue Webrecherchen oder ein realer Probelauf mit den Tutoriumsbechern gehörten nicht zu dieser Abnahme. Die entschiedenen Quellenkorrekturen wurden im Text abgeglichen; die externen Seiten wurden nicht erneut aufgerufen.

Der zusätzliche `x2_paketvergleich.py` besteht **11/11 Konsistenzchecks**: Beide Modellkopien sind bytegleich; die vorhandene Nachrechnung erzeugt exakt die gespeicherte Ausgabe; der Sammlungsgenerator reproduziert Kaffee-Teil und Zahlenausgabe bytegenau. Alle schreibenden Generatoren liefen dafür ausschließlich auf Kopien in einem temporären Verzeichnis. Der Aufgabentext ist abgesehen von Gliederungs- und Umbruchmarkierungen in allen vier Textfassungen gleich. Der eigentliche Lösungsteil ist in beiden Lösungen gleich, die Studierendenfassung enthält keine TL-Hinweise oder Zusatzfrage. Der Bildpfad `grafik/t5_kaffee_tassen.png` wird über den Ressourcenpfad zur Sammlung korrekt aufgelöst.

## Abgleich der Entscheidungen

Alle 50 Einträge aus `ergebnisse/kaffee/Aenderungsvorschlaege.md` wurden geprüft. „Umgesetzt“ bezieht sich auf den fachlichen Inhalt; offene Ausführungsdetails sind ausdrücklich genannt. Die späteren Entscheidungen S1 bis S11 haben Vorrang vor den ursprünglichen Teilbuchstaben.

| Entscheidung | Stand und Beleg |
|---|---|
| Ä1 | Umgesetzt: frische, untergerührte warme Milch statt Schaum, `A:42`, `63`; Cappuccino nur als Modellgrenze, `L:223`. |
| Ä2 | Umgesetzt: warme Ergebnisse ohne Zuordnung, jetzt f, `A:64`. |
| Ä3 | Umgesetzt: Kern a bis f, g Vertiefung, Zusatz nur in Hinweisen; `A:66`, `L:208` bis `218`. |
| Ä4 | Umgesetzt: 40-min-Versuch, zwei Messungen nach 10 min, Mittelwert und Modell c/d; `A:74` bis `76`, `L:214`, `228`. |
| Ä5 | Inhaltlich umgesetzt: Tabelle und Zusatzfelder `A:79` bis `89`, Messregeln und Detailablauf `L:228`. Verlagerung zur TL ist durch Umfangsauftrag und TL-geführten Versuch gedeckt. Küchenwaage entfällt nach Ä4. |
| Ä6 | Umgesetzt: Erwartungsbereiche und Modellabweichung, `L:229`. Untergrenze 2,0 statt vorgeschlagener 1,8 K ist für 5 Prozent mehr kA rechnerisch richtig. |
| Ä7 | Umgesetzt: Verlustgleichung und cp=cv, `A:29`, `30`, `L:130`. |
| Ä8 | Umgesetzt: Annahme in c selbst begründen, qualitative und quantitative Modellgrenze, `A:54`, `L:144`, `225`. |
| Ä9 | Umgesetzt: allgemeine Bilanz und begründetes Vereinfachen, `A:51`, `L:127` bis `137`. |
| Ä10 | Umgesetzt: Mischbilanz mit innerer Energie, `L:120` bis `125`. |
| Ä11 | Umgesetzt: begründete Festlegung und Wärmekapazitäten, `A:19`, `57`, `L:208`. |
| Ä12 | Umgesetzt: Energiekontrolle, Denkfehler und Tafelimpuls, `A:60`, `L:162` bis `168`, `222`, `226`. Fachliche Präzisierung nötig, Abnahme 1. |
| Ä13 | Rechnerisch und textlich umgesetzt, `A:66`, `L:186` bis `201`; Bilanzraumgrafik korrigieren, Abnahme 2. |
| Ä14 | Umgesetzt: Erklärauftrag und Hilfe, jetzt f, `A:63`, `L:179`, `223`. |
| Ä15 | Umgesetzt: zweiseitige Modellgrenze `L:224`; nichtlineare Modellprüfung ausdrücklich Näherung/Formtest, Integration nun analytisch, Ausgabe heißt Zusatzprüfung. |
| Ä16 | Umgesetzt: Robustheit bei 66/68 °C, `L:160`. |
| Ä17 | Umgesetzt: Kipppunkt als empfindlicher Modellwert, `L:239`. |
| Ä18 | Weitgehend umgesetzt: Linienarten, Sprünge, Endwerte und Ausschnitt; kurze Bildbeschriftungen fehlen, Abnahme 5. |
| Ä19 | Textkorrekturen umgesetzt: DOIs, Titel, Kaffeeherleitung, zweiter Verdunstungsbeleg und Quellenhinweise; `L:255` bis `259`, Sammlungsquellen. Keine erneute externe Linkprüfung. |
| Ä20 | Teilweise umgesetzt: Hierarchie, Formelgröße und bearbeitbare Word-Formeln vorhanden; Marken, Abstände und Umbrüche offen, Abnahmen 3 und 5. |
| Ä21 | Umgesetzt: Lösung von Seite 1 an erkennbar, Endkopf Sommersemester 2027. |
| Ä22 | Inhaltlich umgesetzt: kompakte Gruppen und f/g-Verweise, keine wiederholte Word-Kopfzeile; Spaltenbreiten offen, Abnahme 5. |
| Ä23 | Vertagung eingehalten: kein neuer FVT-Rahmen mit Logos, Segoe und blauem Titel. |
| Ä24 | Teilweise umgesetzt: Zerlegung als nicht verlangt markiert, neue Fehlvorstellung und aufgeräumte Verweise; Notationsreste, Abnahme 5. `(neu)` bleibt ausdrücklich nach S10. |
| Ä25 | Inhaltlich umgesetzt: Fehlzahlen, Linearität und Versuchskurzformel, `L:220`, `228`, `237`. 20,41 statt vorgeschlagener 20,42 ist die richtige Rundung. Skriptverweis offen, Abnahme 4. |
| Ä26 | Umgesetzt: Zeitkonstante, 42,1 °C und kA/A, `L:146`, `226`. |
| Ä27 | Umgesetzt: umgekehrtes Ziel, technischer Bezug und Fachbeleg, `L:226`, `227`, `259`. |
| Ä28 | Variante eingehalten: Tassenwärmer nur als Impuls, `L:226`. |
| Ä29 | Umgesetzt: Probelauf, Reservemessung und Milchkaffee-Kontrollreihe empfohlen, `L:230`. Kein realer Probelauf durch diese Abnahme. |
| Ä30 | Umgesetzt: nur Raumluft, Milchglas mit Abstand und Gegenbeispiel 35,3 °C, `A:74`, `L:228`, `232`, `241` bis `247`. |
| W1 | Variante A umgesetzt: warme Milch statt Schaum. |
| W2 | Kern vor Vertiefung, nach S2 entsprechend f/g getauscht. |
| W3 | Frage in c plus Hinweis, kein neuer Pflichtteil. |
| W4 | 40 min und Vorhersage durch TL nach d. |
| W5 | Beide warmen Kontrollwerte ohne Zuordnung. |
| W6 | Skizze nur als Tafelimpuls, `L:226`. |
| V1 | Ablehnung eingehalten: Kontrollwerte bleiben; Zuordnung bei Vorhersagen verborgen. |
| V2 | Ablehnung eingehalten: Milch- und Becherwerte bleiben in der gemeinsamen Tabelle. |
| V3 | Ablehnung eingehalten: Titel weiterhin zentriert. |
| S1 | Umgesetzt: d ohne Zuordnung, `A:58`, `S:54`. |
| S2 | In Aufgabe, Lösung, Sammlung und L1 korrekt umnummeriert; zwei alte Skriptbeschriftungen bleiben, Abnahme 4. |
| S3 | Umgesetzt: Folie 8 als Ausgangspunkt, `A:51`, `L:127`. |
| S4 | Umgesetzt: klare Wärmeabschätzung und nur Kontrollwert 1,83 kJ, `L:232`; Auflösung erst `L:244` bis `247`. |
| S5 | Umgesetzt: „wie in Teil c (ohne Becher)“, `A:76`. |
| S6 | Umgesetzt: gemeinsame b-Besprechung und Haltepunkt, `L:214`. |
| S7 | Variante eingehalten: zusätzliche Hilfe nur in Hinweisen, `L:222`. |
| S8 | Umgesetzt: Celsiusrechnung und Erklärung der fast gleichen Temperatur mit Becher, `L:139`, `196`. |
| S9 | Variante eingehalten: Durchmesser nicht auf Blatt; qualitative Begründung genügt, `L:144`. |
| S10 | Umgesetzt: seitliche Wärmepfeile in aktiver Abb. 1, `(neu)` bleibt. |
| S11 | Umgesetzt: frühere h nur als Zusatzfrage in Hinweisen, `L:232` bis `247`. |

Zusätzliche ausdrückliche TL-Entscheidungen sind berücksichtigt: Kaffee bleibt Hauptaufgabe, heißes Wasser ist zulässig, Material liegt bei der TL, Kopf nennt Sommersemester 2027, Studierende erhalten eine eigene Lösung ohne Hinweise. Nicht entschiedene fachliche Eingriffe wurden nicht gefunden. Die sachfremde Gitignore-Änderung ist separat in Abnahme 6 dokumentiert. Neue Sammlungsausgaben und globale Satzfilter sind Begleitänderungen; geprüft wurde daraus nur der Kaffee-Teil, keine Abnahme der übrigen Tutorien.

## PDF und Word als Seitenbilder

Alle unten genannten Seiten wurden tatsächlich als Bilder angesehen, zusätzlich wurden die drei aktiven Abbildungen geprüft. Verwendet wurden PDF-Rasterung und eine LibreOffice-Konvertierung der unveränderten DOCX in einem temporären Profil. Der ausführliche Sichtnachweis steht in `codex_skripte/x2_render_sichtpruefung.md`; SHA256, Originalpfade und Seitenzahlen stehen in `x2_render_ausgabe.json`.

| Ausgabe | Geprüfte Seiten |
|---|---|
| Neue Aufgabe PDF / DOCX-Ansicht | alle 4 / alle 4 |
| Neue Lehrlösung PDF / DOCX-Ansicht | alle 13 / alle 14 |
| Neue Studierendenlösung PDF / DOCX-Ansicht | alle 10 / alle 10 |
| Neue Sammlung PDF | Kaffee 22 bis 25, Kaffeequellen 58 |
| Neue Sammlung DOCX-Ansicht | Kaffee 25 bis 28 |
| Alte Originalaufgabe / Originallösung PDF | alle 3 / alle 9 |

Keine fehlenden Bilder, kaputten Formeln oder abgeschnittenen Tabellen gefunden. Word enthält bearbeitbare OMML-Formeln. Die unterschiedliche Zahl der Lehrlösungsseiten zwischen PDF und DOCX ist kein Inhaltsverlust. Die neue Abb. L2 verbessert die alte Fassung sichtbar. Die Studierendenfassungen enthalten den vollständigen fachlichen Lösungsteil und die Quellen ohne TL-Hinweise. Verbleibende Satzmängel sind in Abnahme 3 beschrieben. Eine pixelgleiche Neuerzeugung der Grafiken wurde wegen abweichender Schriftverfügbarkeit der Prüfumgebung nicht als Abnahmekriterium verwendet.

## Reproduktion

Vom Repositoryverzeichnis aus:

```bash
python ergebnisse/kaffee/codex_skripte/x2_eigenrechnung.py
python ergebnisse/kaffee/codex_skripte/x2_paketvergleich.py
python ergebnisse/kaffee/codex_skripte/x2_render_artefakte.py --word
```

Die ersten beiden Ausgaben liegen als `x2_eigenrechnung.txt` und `x2_paketvergleich.txt` bei. Das Renderskript benötigt PyMuPDF und für DOCX `soffice`; Bilder und konvertierte Dateien schreibt es unter `/tmp/x2_abnahme_render`. Das Rendern allein ersetzt die Sichtprüfung nicht. Die Korrekturen dieses Berichts sind Vorschläge, keine bereits am Paket vorgenommenen Änderungen.
