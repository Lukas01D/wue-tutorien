// KI-Protokoll, fortlaufend
// Aufruf: node protokoll_ki.js <ausgabe.docx>
const h = require("./fvt_doc.js");
const { P, Small, H1, H2, Bullet, grid, box, Paragraph, TextRun, AlignmentType, makeDoc, write } = h;
const OUT = process.argv[2] || "KI-Protokoll.docx";
const C = [];

C.push(new Paragraph({ style: "Title", children: [new TextRun("Tutorien Wärmeübertragung: KI-Protokoll")] }));
C.push(P("Einsatz von KI bei der Entwicklung der Tutorien, fortlaufend geführt", { size: 24, color: h.GREY, align: AlignmentType.LEFT, before: 0, after: 120 }));
C.push(Small("**Version:** 8 · **Stand:** 23.10.2026 · **Verantwortlich:** Tutoriumsleitung"));
C.push(Small("**Begleitdokumente:** Entscheidungsprotokoll; „Lernziele, Vorab-Fragen und Bilanz-Systematik“ (16.10.2026); „Leitaufgaben aus Klima und Erde“ (17.10.2026); „Aufgabenideen: Meeresströmungen, Sverdrup und Luftströmungen“ (20.10.2026); „Kaffee mit Milch“ (Aufgabe und Lösung, 21.10.2026); „Strukturvorlage: Aufgaben im Stil des Lehrstuhls“ (21.10.2026); „Aufgabensammlung der Tutorien“ (21.10.2026); Plan und Prüfpaket zur Prüfung der Kaffee-Aufgabe (23.10.2026); Werkzeugkasten Tutorien Wärmeübertragung, Version 1 (23.10.2026)", { after: 160 }));

C.push(box([
  h.boxTitle("Zweck und Grundsätze"),
  Bullet("Das Protokoll macht nachvollziehbar, wofür KI eingesetzt wurde, was sie geliefert hat, wie es geprüft wurde und welche Fehler auftraten."),
  Bullet("**Verantwortung:** Inhalte und Entscheidungen verantwortet die Tutoriumsleitung, die fachliche Freigabe erteilt die Professorin. KI-Ausgaben sind Entwürfe."),
  Bullet("**Quellenpflicht:** Fakten und Studien werden mit Quelle und Prüfstatus angegeben (Volltext, Abstract, Sekundärquelle, nicht geprüft). Zahlen werden mit einem Skript nachgerechnet."),
  Bullet("**Daten:** Es werden keine personenbezogenen Daten von Studierenden an die KI gegeben."),
  Bullet("**Regeln der Universität:** Die Vorgaben der Universität Paderborn zum Einsatz generativer KI in Lehre und Prüfung gelten; die Fundstelle ergänzt die Tutoriumsleitung."),
]));

C.push(H1("1. Eingesetzte Werkzeuge"));
C.push(grid(
  ["Werkzeug", "Angaben"],
  [
    ["KI-Assistent", "Claude (Anthropic), Sitzungskonfiguration claude-opus-5-5; das tatsächlich antwortende Modell kann abweichen. Arbeitsumgebung mit Websuche, Abruf von Webseiten, Python, Node.js, Dateiwerkzeugen und Zugriff auf die Projektablage."],
    ["Rechercheagenten", "vom Assistenten gestartete Teilaufträge mit Websuche, die Fakten oder Literatur prüfen und eine Tabelle mit Quelle, Link und Zitat zurückgeben. Ergebnisse werden stichprobenartig gegen die Quelle geprüft."],
    ["Projektablage", "Vorlesungsfolien 01 bis 08, Formelsammlung SoSe 2026, Zusatzblatt Charakteristische Längen, Holman (2010), FVT-Vorlagen und Logos"],
    ["Lehrstuhlmaterial", "Übungen 1 bis 9, Tutorien 1 bis 8 und Vorlesungen als ZIP-Archive im Chat (21.10.2026); Word-Dateien mit pandoc in Text umgewandelt, handschriftliche Vorlesungsbeispiele als Bild gelesen"],
    ["Rechnen", "Python 3.13.16, numpy 2.5.3, scipy 1.18.1, matplotlib 3.11.2, CoolProp 8.0.0 (Stoffwerte Luft)"],
    ["Dokumente", "Node.js 22.22.0 mit docx 9.7.1 (Word), LibreOffice 24.2.7.2 (PDF), pandoc 3.1.3 (Markdown und Word mit Word-Formeln), XeLaTeX aus TeX Live 2023 (PDF mit Formeln)"],
    ["Prüfagent", "vom Assistenten gestarteter Prüfauftrag ohne Kenntnis der Entstehung des Dokuments; prüft Zahlen gegen die Ausgabe der Nachrechnung, innere Widersprüche, Quellen, Lernzielbezug und Notation und gibt eine nach Wichtigkeit geordnete Befundliste zurück"],
    ["Arbeitsagenten", "vom Assistenten gestartete parallele Teilaufträge, die nach einer gemeinsamen Spezifikation je einen Teil eines Dokuments erstellen (Text, Skizzen, Rechenskript mit Selbstprüfung, Quellen) und einen Bericht mit Änderungen und offenen Punkten zurückgeben; der Assistent setzt die Teile zusammen und prüft sie"],
    ["Ablage", "Sciebo über die Verbindung zum Rechner der Tutoriumsleitung; am 16. und 17.10.2026 nicht erreichbar, Dateien daher im Chat und in der Projektablage übergeben; am 20.10.2026 erreichbar, aber ohne freigegebenen Sciebo-Ordner; seit 21.10.2026 legt die Tutoriumsleitung selbst in Sciebo ab, Zwischenablage auf ihrem Schreibtisch"],
    ["Claude-Dokumente", "bearbeitbare Dokumente auf claude.ai mit Diagrammen, die aus Datenzeilen gezeichnet werden; Diagramme werden nach dem Erstellen als Bild geprüft"],
  ],
  [2000, 7070], { firstColBold: true },
));

C.push(H1("2. Einsatzprotokoll"));
C.push(P("Aufträge sind sinngemäß wiedergegeben. Die Spalte „Prüfung“ nennt, wie das Ergebnis kontrolliert wurde; „Probleme“ nennt Fehler der KI und ihre Korrektur."));
const TAB = (list) => grid(
  ["Nr.", "Datum 2026", "Auftrag", "Tätigkeit der KI", "Ergebnis", "Prüfung", "Probleme und Korrekturen"],
  list,
  [550, 850, 1450, 1650, 1450, 1500, 1620], { firstColBold: true, size: 15 },
);
C.push(TAB([
  ["K01", "16.10.", "zwei Lernziele für ein erstes Tutorium aus dem Modulhandbuch", "Formulierung auf Basis des eingefügten Modulhandbuchtextes", "Vorschläge im Chat", "Auswahl durch die Tutoriumsleitung", "keine"],
  ["K02", "16.10.", "Lernziele speziell für Tutorium 1 (Wärmeleitung); Nachschärfen des eigenen Entwurfs", "Überarbeitung mit markierten Änderungen", "nachgeschärfte Fassung", "Abgleich mit dem Entwurf der Tutoriumsleitung", "keine"],
  ["K03", "16.10.", "Lernziele für alle Tutorien; Frage nach einem vierten Bilanzthema", "Vorschläge; Systematik stationär/instationär und global/differentiell", "Lernziele, 2×2-Systematik", "Tutoriumsleitung", "keine"],
  ["K04", "16.10.", "Grafik im FVT-Stil mit markiertem Feld", "Python-Skript bilanzformen.py, SVG und PNG", "Grafik groß und kompakt, Varianten 0 bis 4", "Sichtprüfung jeder Variante", "erster Entwurf mit Textüberlappungen; Zeilenumbruch und Zellhöhen neu berechnet"],
  ["K05", "16.10.", "alle Vorlesungen gewissenhaft durchgehen, Lernziele anpassen, Lehr-Lern-Methodik recherchieren", "Volltext der Folien 01 bis 08 und der Formelsammlung; Rechercheagent für Literatur", "angepasste Lernziele, acht Regeln, Quellenliste mit Prüfstatus", "eigene Prüfung jeder zitierten Aussage", "Agent schrieb die Ein-Verb-Regel der UPB-Handreichung selbst zu; tatsächlich zitiert die Handreichung die HRK-Leitlinien. Original von Rothkopf & Kaplan nicht zugänglich, daher Tagungsbeitrag zitiert. Zwei Quellen ohne prüfbare Befunde weggelassen."],
  ["K06", "16.10.", "Nachrechnung von Vorlesungsbeispielen", "Python: V05 Beispiel 5, V08 Teile d und e", "*L* ≈ 17,8 m; *Bi* ≈ 5 bis 10 für den Käse", "Plausibilität, Literaturwert für *λ* von Käse", "Käse-Beispiel aus der Grafik entfernt"],
  ["K07", "16.10.", "Ausarbeitung als Word und PDF für Sciebo", "docx-js, LibreOffice, Seitenprüfung als Bild", "16-seitiges Dokument, Markdown in der Projektablage", "jede Seite angesehen", "Zeilenabstände in LibreOffice falsch, Blöcke über Seitenumbrüche, leere Seite: behoben"],
  ["K08", "16.10.", "Ablage in Sciebo", "Zugriff über die Rechnerverbindung", "nicht möglich", "keine", "Rechner nicht erreichbar; Dateien im Chat übergeben"],
  ["K09", "17.10.", "Ideenliste: Leitphänomene aus Klima und Erde, Realbeispiele als Aufgaben, Arbeitsplan", "vier parallele Rechercheagenten (Geo und Eis; Atmosphäre und Ozean; Technik und Mensch; Lehr-Lern-Forschung); Suche in Holman (2010) und in den Folien", "Ideensammlung „Leitaufgaben aus Klima und Erde“", "Fakten mit Quelle; Prüfstatus im Quellenverzeichnis", "siehe Abschnitt 3; Suchkontingent am Ende der Prüfung aufgebraucht, offene Punkte gekennzeichnet"],
  ["K10", "17.10.", "Rechenbarkeit und Plausibilität der Aufgabenskizzen", "Python-Skript nachrechnung_leitphaenomene.py mit den Korrelationen der Formelsammlung und CoolProp", "Rechenprotokoll (Anhang A der Ideensammlung)", "Vergleich mit Messwerten und Größenordnungen der Vorlesung", "keine Rechenfehler gefunden; Arbeitswerte als vorläufig gekennzeichnet"],
  ["K11", "17.10.", "Grafikvarianten mit zwei markierten Feldern; Visualisierung zu *kA* = 1/*R*_{th}", "Erweiterung von bilanzformen.py; neues Skript widerstand_meereis.py", "Varianten 12, 13, 24, 34; Beispielgrafik Meereis", "Sichtprüfung; Einzelvarianten unverändert (Dateigröße verglichen)", "Textüberläufe und fehlendes Zeichen *α* in der Beispielgrafik: in zwei Runden behoben"],
  ["K12", "17.10.", "Lernziele Fassung 2, Arbeitsplan, Entscheidungs- und KI-Protokoll", "Entwurf auf Basis der Rückmeldung", "Word, PDF, Markdown", "Sichtprüfung aller Seiten", "siehe Abschnitt 3"],
  ["K13", "17.10.", "Ablage in Sciebo", "Rechnerverbindung", "nicht möglich", "keine", "Verbindung zum Rechner nicht vorhanden; Dateien im Chat übergeben"],
  ["K14", "17.10.", "Ideensammlung vor der Übergabe unabhängig prüfen", "getrennter Prüfauftrag ohne Kenntnis der Entstehung: Zahlen gegen die Ausgabe der Nachrechnung, Widersprüche, Quellen, Lernzielbezug, Notation; eigenes Prüfskript", "35 Befunde, nach Wichtigkeit geordnet", "Dome C und Schnee an der Quelle nachgeprüft; alle Zahlen mit dem ergänzten Skript neu berechnet; Dokumente neu gebaut und Seite für Seite angesehen", "Fehler der eigenen Entwürfe in Abschnitt 3.2; alle Befunde bearbeitet (Entscheidungsprotokoll D43 bis D50)"],
  ["K15", "17.10.", "Ablage in Sciebo nach der Überarbeitung", "Rechnerverbindung", "nicht möglich", "keine", "Rechner nicht mit der Sitzung verbunden; Dateien im Chat und in der Projektablage übergeben"],
  ["K16", "17.10.", "Entscheidungen E7 bis E17 zeigen; Kurzkonzept für Viola (minimalistisch)", "Übersicht im Chat, Abfrage der Pilot-Entscheidungen; Kurzkonzept als Claude-Dokument", "Kurzkonzept (Idee, Aufbau, acht Leitphänomene, Beispiel Tutorium 1, Fragen)", "Zahlen aus der Nachrechnung übernommen", "keine"],
  ["K17", "17.10.", "Mailentwurf an Viola auf Basis des eigenen Entwurfs der Tutoriumsleitung", "Rechtschreibung und Klarheit geglättet, Änderungen gekennzeichnet; Variante mit Anhang", "zwei Entwürfe", "Tutoriumsleitung prüft und sendet selbst", "„diesen Freitag“ war mehrdeutig, ersetzt durch „am Freitag“"],
  ["K18", "17.10.", "Pilotblatt Tutorium 1 (Aufgabenblatt und Musterlösung)", "Skript pilot_tutorium1.py, zwei Grafiken (pilot_t1_grafiken.py), zwei Word-Dokumente im FVT-Layout", "Aufgabenblatt (4 Seiten), Musterlösung mit Erwartungshorizont und Hinweisen (5 Seiten)", "alle Zahlen aus dem Skript; Seiten als Bild geprüft; Begriffe gegen V01 und V02 abgeglichen", "*λ*_{m} war bisher als Mittel der Randwerte gerechnet; V02 F. 12 definiert das Integralmittel (Unterschied unter 1 %), korrigiert. Word-Vorlage nur als Text verfügbar, Struktur übernommen. Wärmeleitfähigkeit von Stahlbeton nicht an der Norm geprüft."],
  ["K19", "20.10.", "Aufgaben zu Meeresströmungen (Golfstrom, Europas Winter, AMOC mit 20 % weniger Wärmetransport), Sverdrup, Amazonas und Luftströmungen (Passat, Polarjet), nicht zu komplex", "drei parallele Rechercheagenten (Ozean und AMOC; Flüsse und Amazonas; Atmosphäre und Klimadaten); Skript nachrechnung_ozean_atmosphaere.py; Claude-Dokument mit Diagramm", "Aufgabenideen A bis C mit Lösungsskizzen, Sverdrup-Leiter, Entscheidungsvorschläge E18 bis E22, Quellenliste; Markdown in der Projektablage", "alle Zahlen aus dem Skript; Einstrahlungsformel global geprüft (S₀/4); Quellenwerte mit Zitat aus den Agentenberichten; Diagramm als Bild geprüft", "zwölf Arbeitsannahmen abweichend oder nur eingeschränkt belegt (Abschnitt 3.3); Albedo im Winter ohne Messzahl; Normalwerte 1991 bis 2020 für Goose Bay nicht abrufbar. Tiefstellung von Indizes ist in Claude-Dokumenten nicht möglich (c_p statt *c*_{p})"],
  ["K20", "20.10.", "Aufgabenideen vor der Übergabe unabhängig prüfen", "getrennter Prüfauftrag ohne Kenntnis der Entstehung: Zahlen gegen Skript und Faktenberichte, Physik und Vorzeichen, Lösbarkeit, Quellenaussagen, Sprache; eigenes Prüfskript, sechs Websuchen", "ein kritischer, acht wichtige und rund ein Dutzend kleinere Befunde", "Befunde einzeln nachvollzogen; Skript ergänzt (Version 3); Flugzeugtyp an der Quelle nachgeprüft", "Vorzeichenfehler in Teil h und i, fehlende Sverdrup-Definition, Goose-Bay-Vergleich im Gürtel-Fall falsch, 1,2 PW nördlich von 40° N als Obergrenze nicht benannt, Richtung des Wärmestroms in B2 falsch (Abschnitt 3.4); umgesetzt bis auf zwei bewusst belassene Notationshinweise (*p*_{0} und *S*_{0} mit Unicode-Index im Claude-Dokument; 51,7° N für Paderborn, 51,8° N für die Wetterstation)"],
  ["K21", "20.10.", "Ablage in Sciebo", "Rechnerverbindung geprüft", "Rechner erreichbar, aber kein Ordner für die Sitzung freigegeben; Sciebo-Ordner nicht ohne Freigabe auffindbar", "keine", "Dateien als ZIP im Chat und als Markdown in der Projektablage übergeben"],
  ["K22", "21.10.", "Aufgabenideen zusätzlich als PDF", "Markdown-Fassung mit Skript aufgabenideen_ozean.js in Word im FVT-Layout umgesetzt (Indizes tiefgestellt, Diagramm als Bild), PDF mit LibreOffice", "Word und PDF (13 Seiten)", "alle Seiten als Bild geprüft; Text auf übrig gebliebene Markdown-Zeichen durchsucht", "erster Umbruch mit einer fast leeren Seite und einer abgetrennten Tabellenüberschrift; Seitenumbrüche angepasst"],
  ["K23", "21.10.", "Übungen, Tutorien und Vorlesungsbeispiele des Lehrstuhls sichten und die Aufgabenstruktur übernehmen; Vorbilder Tutorium 3, Aufgabe 3 und Tutorium 6, Aufgabe 1", "drei ZIP-Archive entpackt, Word-Dateien mit pandoc umgewandelt; Teilauftrag zur Stilanalyse aller Übungen und Tutorien; Vorlesungsbeispiele 1 bis 9 als Bild gelesen", "Strukturvorlage „Aufgaben im Stil des Lehrstuhls“ (Markdown)", "Vorbildaufgaben und Tutorium 5 selbst gelesen und mit der Stilanalyse abgeglichen", "kaputte Querverweise und Dezimalpunkte im Material nicht übernommen; Rechenstil der Vorlesungsbeispiele nur sinngemäß übertragen (handschriftlich)"],
  ["K24", "21.10.", "Kaffee-Aufgabe: zwei Tassen, Milch sofort oder nach 60 Minuten, welche ist kühler; Struktur wie am Lehrstuhl, minimalistisch, didaktisch fordernd", "Rechercheagent für Arbeitswerte (Ausschanktemperatur, Milchmenge und Kühlschranktemperatur, Abkühlung eines offenen Bechers, Anteil der Verdunstung); Rechenmodell kaffee_modell.py mit nachrechnung_kaffee.py; drei Grafiken; Aufgabe und Lösung aus einer Markdown-Quelle (build_kaffee.py)", "Aufgabenblatt (2 Seiten) und Lösung mit Aufgabentext, Hinweisen und Quellen (6 Seiten), je Word und PDF; Ergebnis: Tasse 2 um 3,85 K kühler", "alle Zahlen im Text aus dem Modell; Empfindlichkeit (Milch 7 und 20 °C, 40 ml, Kaffee 85 °C, schnellere und langsamere Abkühlung, Becher 300 g), nichtlineare Wärmeabgabe, allgemeine Prüfung des Vorzeichens; alle Seiten als Bild geprüft", "„Tasse 2 bleibt die ganze Stunde heißer“ war falsch (Kurven schneiden sich nach etwa 56 min), umformuliert; Teil f behauptete, Tasse 2 verliere im nichtlinearen Modell mehr Wärme als im linearen (stimmt nur im Vergleich zu Tasse 1), korrigiert; Lösungsweg über Formelsammlung Kapitel 5 entfernt (D24); LibreOffice setzt Word-Formeln unsauber, PDF daher über LaTeX; Gradzeichen als Ringoperator durch ° ersetzt"],
  ["K25", "21.10.", "Kaffee-Aufgabe vor der Übergabe unabhängig prüfen", "getrennter Prüfauftrag ohne Kenntnis der Entstehung: eigene Nachrechnung aller Zahlen, Physik und Logik, Didaktik und Sprache, Stil gegen das Lehrstuhlmaterial, Quellen per Websuche", "ein Fehler, sechs wichtige und mehrere kleinere Befunde; alle Zahlen in a bis e bestätigt", "Befunde nachvollzogen; Becher-Fall im Modell nachgerechnet; Dokumente neu gebaut und Seite für Seite angesehen", "Becher-Fall mit falschem *kA*, Rundung in Teil f, veraltete Abb. 1 mit *ϑ*_{U}, mehrdeutiger Bilanzraum, zwei Quellenwerte nur abgeleitet (Abschnitt 3.5); alle umgesetzt außer der Kopfzeile „Entwurf“ (bleibt bis zur Freigabe)"],
  ["K26", "21.10.", "Ablage in Sciebo", "Rechnerverbindung geprüft", "Rechner erreichbar, aber kein Ordner für die Sitzung freigegeben", "keine", "Dateien als ZIP im Chat und als Markdown in der Projektablage übergeben"],
  ["K27", "21.10.", "Erweiterungen der Kaffee-Aufgabe sammeln: Becher, Zeitfrage, Milchschaum, Milch mit 8 °C und Rausstellen (2×2), Live-Versuch", "Nachrechnung mit kaffee_modell.py (Zerlegung in zwei Effekte, Kipppunkt, Temperaturunterschied über der Zeit für den Versuch, Erwärmung der Milch); drei Websuchen mit Abruf der Seiten (Milchschaum, Kühlschranktemperaturen, Vorhersagen bei Demonstrationen)", "Sammlung von acht Bausteinen mit Empfehlung, im Chat und in der Projektablage", "alle Zahlen aus dem Modell; Quellen an der Seite gelesen", "2×2 ergibt nur drei verschiedene Fälle (bei sofortigem Zugießen ist egal, wo die Milch stand); kA der Milch im Kännchen nur geschätzt"],
  ["K28", "21.10.", "Ausgangssituation mit Text und Skizze an den Anfang jedes Aufgabenblocks; diese Struktur auf alle bisher erarbeiteten Aufgaben übertragen; große Aufgabensammlung als PDF und Word, auch mit den Klimaaufgaben; KI-Protokoll weiterführen", "Kaffee-Aufgabe als Muster umgebaut (Ausgangssituation, Frage 1, Aufgabe 1 mit Becher, Milchschaum, Kipppunkt und Versuch); gemeinsame Spezifikation (SPEZ.md) und Skizzenstil (skizze_stil.py); fünf parallele Arbeitsagenten für die übrigen Aufgaben, je Tutorium Text, Skizzen, Rechenskript mit Selbstprüfung und Quellenliste; Zusammenbau mit sammlung_bauen.py (pandoc, XeLaTeX, Word)", "Aufgabensammlung als PDF, Word und Markdown: 14 Aufgabenblöcke mit Ausgangssituation und Skizze, 11 Zusatzaufgaben, Übersicht, Inhaltsverzeichnis, Anhang mit den Quellen der Arbeitswerte; Kaffee-Blatt und Lösung aktualisiert", "Rechenskripte prüfen, dass jede Zahl im Text steht; Berichte der Agenten gelesen; alle Seiten als Bild angesehen; Word-Datei strukturell und in LibreOffice geprüft; unabhängige Gegenprüfung (K29)", "Skizze zu Tutorium 7 verriet die Antwort der Vorab-Frage (gezeichnetes Profil), durch leere Achsen ersetzt; Ergebniszeilen mit „(1)“ wurden als Liste gesetzt, durch „Zu (1):“ ersetzt; Satzfehler (verwaiste Überschriften, getrennte Tabellen, Links über den Seitenrand, absoluter Pfad und rohe Unterstriche im Quellenanhang, ein verirrtes „.0“ vor dem Inhaltsverzeichnis) behoben; Word trennte Tabellen über Seiten, Absätze nachträglich zusammengehalten; offene fachliche Punkte der Agenten im Entscheidungsprotokoll"],
  ["K29", "21.10.", "Aufgabensammlung vor der Übergabe unabhängig prüfen", "drei parallele Prüfaufträge ohne Kenntnis der Entstehung (Tutorium 1 bis 3, 4 und 5, 6 bis 8) mit gemeinsamem Prüfauftrag (PRUEFAUFTRAG.md): eigene Nachrechnung aller Kernergebnisse, Formeln gegen die Formelsammlung, Struktur, Skizzen, Sprache, Querverweise, Quellen, Satz; eindeutige Fehler direkt korrigiert, Entscheidungen nur gemeldet", "29 direkte Korrekturen, keine Zahl auf den Blättern falsch gerechnet; ein Fehler in der Kaffee-Musterlösung; 21 Punkte zur Entscheidung mit Empfehlung", "Befunde nachvollzogen; Kaffee h (2) und Becher 3 mit dem Modell nachgerechnet; 12 Empfehlungen ausgewählt und von den Prüfern umgesetzt, 2 im Satz gelöst, 7 bewusst belassen (D84, D85); Sammlung neu gebaut und alle Seiten angesehen", "Musterlösung Kaffee h (2) nannte 2,48 statt mindestens 1,95 K; Wostoksee mit −3 °C widersprach dem Modell; Tiefgang 220 statt 224 m; gerundetes *d*_{T} passte nicht zu Teil e; fehlende Kennzeichnung von Formeln außerhalb der Formelsammlung; Leitfrage im Block „Pol“ nicht lösbar (Abschnitt 3.6)"],
  ["K30", "21.10.", "Ablage auf dem Schreibtisch der Tutoriumsleitung (Sciebo legt sie selbst ab)", "Freigabe des Schreibtischordners über die Rechnerverbindung angefragt", "Anfrage ohne Antwort abgelaufen", "keine", "Dateien als ZIP im Chat und als Markdown in der Projektablage übergeben; neue Anfrage erst nach Rückmeldung der Tutoriumsleitung"],
  ["K31", "21.10.", "Kaffee-Aufgabe separat als PDF und Word und als Claude-Dokument, in dem die Tutoriumsleitung Feedback in [ ] gibt und die KI direkt ändert", "Einzelblatt aus der Sammlung (Text gegen die Sammlung verglichen); Claude-Dokument mit Ausgangssituation, Abb. 1, Frage 1, Aufgabe 1 (Tabelle der gegebenen Größen, Ergebnisse als abgesetzte Formeln) und Versuch", "PDF und Word (3 Seiten) im Chat; Claude-Dokument „Kaffee mit Milch (Tutorium 5)“", "Text identisch mit der Sammlung; Dokument nach jedem Abschnitt geprüft", "Claude-Dokumente setzen Formeln nur abgesetzt; im Fließtext stehen Formelzeichen daher als V_K oder ϑ_1,0, die Tabelle der gegebenen Größen ist dreispaltig statt vierspaltig"],
  ["K32", "23.10.", "Kaffee-Aufgabe mit Anforderungen, Vorlagen und Lehrstuhlaufgaben unabhängig prüfen lassen (Rollen wie Prüfer, Professorin, Recherche) und Änderungsvorschläge auf didaktischer, technischer und inhaltlicher Ebene finden; nach einer Pause: sechs Rollen mit eigenen Leselisten, ein Gesamtprompt statt einzelner Chats, eine Anleitung, alle Dateien in die Ablage", "Prüfauftrag und fünf Rollen geschrieben, fünf Prüfer gestartet und nach wenigen Minuten auf Wunsch gestoppt (Nutzungsvolumen, noch keine Berichte); danach Prüfpaket für einen neuen Chat: Startprompt, gemeinsamer Prüfauftrag, sechs Rollentexte, Leseliste und Skript rollen_vorbereiten.py (eigener Materialordner je Rolle), Auszüge aus dem Lehrstuhlmaterial, Anleitung, Arbeitsordner für die Umsetzung, Protokollquellen; Trockenlauf durch einen unabhängigen Agenten (Paket entpackt, Rollenordner angelegt, alle Aufträge gelesen, Blätter, Sammlung und Protokolle neu gebaut)", "Prüfpaket als ZIP im Chat; Textfassung und Protokollquellen in der Projektablage (claude/kaffee_pruefung/); Kaffee-Blatt und Lösung neu gebaut (Stand 23.10.2026)", "Trockenlauf mit 3 Muss-, 10 Sollte- und 15 Kann-Punkten; alle Muss- und Sollte-Punkte und fast alle Kann-Punkte umgesetzt, danach Rollenordner neu angelegt und Leselisten gegen die Dateien geprüft", "Der erste Plan nannte Übung 5 und 6 als Vergleich; die instationären globalen Bilanzen stehen in Übung 6 und 7. Die Word-Vorlage „Aufgabenstellungen“ liegt nur als Text vor und stammt aus einem anderen Fach; Referenz für die Gestaltung sind die Original-Tutoriumsblätter. Die Projektablage nimmt keine Binärdateien an, daher das ZIP. Im Trockenlauf gefunden und behoben: KI-Protokoll im ersten Paket noch Version 6; eine zweite Runde der Studierenden-Rolle hätte mit --neu alle Berichte gelöscht; ein Renderbefehl hätte die PDFs im Material überschrieben; Vorschlagsnummern waren mit Protokollnummern verwechselbar; Prüfer hätten frühere Chats durchsuchen können. In der Kaffee-Lösung beantwortete „Frage 1“ noch eine ältere Frageform („Nein.“), korrigiert; im PDF stand „Gegebene Größen“ allein am Seitenende, in Word brach die Versuchstabelle über die Seite, beides behoben"],
  ["K33", "23.10.", "Word-Vorlage „Aufgabenstellungen“ als Datei für die Gestaltungsrolle (kleine Anpassung); alle Erkenntnisse, Vorgänge, Arbeitsweisen und Planungen für spätere Aufgaben sichern, als Dateien oder ZIP, das bei der Überarbeitung einer weiteren Tutoriumsaufgabe angehängt wird; sparsam, ohne die Arbeit einzuschränken; Frage, was die Tutoriumsleitung noch beisteuern kann", "Vorlage ausgelesen (Ränder, Schrift Segoe UI, Farben, Kopf- und Fußzeile) und als Bild mit Original-Tutoriumsblatt und Kaffee-Blatt verglichen; Vorlage, PDF und Maßübersicht ins Prüfpaket (Rolle G mit zwei Referenzen, Auftrag: kleine Anpassungen empfehlen). Werkzeugkasten aus Protokollen, Prüfberichten, Vorgaben und Erinnerungen gebaut: Startprompt mit Modi, Haltepunkten und Sparregeln; Kontext; Regeln R1 bis R43; Ablauf in zwölf Phasen mit Prüfliste; Erkenntnisse aus K01 bis K32; Index mit Leseordnung und Lehrstuhlmaterial je Tutorium. Werkzeuge verallgemeinert (einzelblatt.py, neue_einzelaufgabe.py mit Vorlagen, material_zusammenstellen.py, rollen_vorbereiten.py mit Mustern, Teilrollen und Platzhalterprüfung, umgebung_pruefen.py, werkzeugkasten_packen.py); Lehrstuhlmaterial mit lesbaren Dateinamen, EMF-Bilder als PNG; Protokollquellen an eine Stelle der Projektablage (D92)", "Werkzeugkasten Version 1 als ZIP (rund 16 MB) mit LIESMICH und Startprompt in der Projektablage; Prüfpaket der Kaffee-Aufgabe neu gebaut (Nummern für die Prüfung jetzt K34, K35, G40, D93 ff.); Platz der Projektablage gemessen (94 %) und im Startprompt berücksichtigt", "Probeaufgabe aus der Sammlung (Tutorium 3, Meereis) mit den Vorlagen angelegt und gebaut, Seiten angesehen; Prüfmaterial der Kaffee-Aufgabe mit dem neuen Skript zusammengestellt, Rollenordner für kleine und volle Prüfung angelegt (Leselisten vollständig); Protokolle aus dem Werkzeugkasten gebaut; Neupacken mit Versionszählung getestet; unabhängiger Trockenlauf durch einen Agenten mit einer Probeaufgabe (Tutorium 3, Meereis): alle Werkzeuge liefen, Lesekosten für den Einstieg rund 18 000 bis 23 000 Tokens", "Die Word-Vorlage lag bisher nur als Text vor (K32); jetzt als Datei, ihre Schrift Segoe UI fehlt unter Linux (LibreOffice ersetzt sie durch Noto Sans). Die Projektablage ist zu 94 % voll: Werkzeugkasten nur als ZIP, in der Ablage nur LIESMICH und Startprompt. Die neuen Nummern K33, G39 und D90 bis D92 verschieben die Nummern der noch nicht gestarteten Kaffee-Prüfung auf K34, K35, G40 und D93 ff.; Prüfpaket angepasst. Der Trockenlauf fand: Lösungsabbildungen der Vorlage landeten im falschen Ordner (Variablenname durch skizze_stil überschrieben), pandoc meldete die fehlenden Bilder nur als Warnung; der Protokollstand im Testpaket passte nicht zu den Steuerdateien; Nummern und Ablageort der Protokollquellen hätten mit der Kaffee-Prüfung kollidiert; zu teure Leseschritte (Protokolle über den Chat holen, Lehrstuhlmaterial doppelt); Platzhalterprüfung auch für nicht gewählte Rollen; zusätzliche Entscheidungen ersetzten die Standardauswahl; das Datum der Sammlung stand an vier Stellen von Hand. Alles behoben (Bildprüfung vor dem Bau, Sperre für den Protokollstand beim Packen, Abgleich beider Ablageorte, sparsame Leseschritte, Hilfsskripte folien.py und stand_setzen.py). Inhaltlicher Befund zur Meereis-Aufgabe (die Vorab-Frage hängt an Schneedicke und Wärmeleitfähigkeit des Schnees) in 02_KONTEXT.md vorgemerkt."],
]));

C.push(H1("3. Prüfergebnisse und bekannte Fehler"));
C.push(H2("3.1 Faktenprüfung der Einstiegsideen"));
C.push(P("Ergebnisse der Faktenprüfung, die von den Arbeitsannahmen abwichen oder nur eingeschränkt prüfbar waren. Die Ideensammlung verwendet die korrigierten Werte."));
C.push(grid(
  ["Aussage im Entwurf", "Ergebnis der Prüfung", "Folge"],
  require("./pruefergebnisse.js"),
  [3000, 3600, 2470], { firstColBold: false, size: 16 },
));
C.push(H2("3.2 Unabhängige Gegenprüfung der Ideensammlung (K14)"));
C.push(P("Ein getrennter Prüfauftrag hat die fertige Ideensammlung ohne Kenntnis ihrer Entstehung geprüft und 35 Befunde geliefert. Die Tabelle fasst die inhaltlich wichtigen zusammen; kleinere Befunde zu Wortlaut und Rechtschreibung sind ohne eigene Zeile umgesetzt. Das Websuche-Kontingent des Prüfauftrags war aufgebraucht; einige Hinweise beruhen deshalb auf innerer Konsistenz und Quellenkenntnis (Ideensammlung, 12.4)."));
C.push(grid(
  ["Aussage im Entwurf", "Ergebnis der Prüfung", "Folge"],
  require("./pruefergebnisse_gegenpruefung.js"),
  [3000, 3600, 2470], { firstColBold: false, size: 16 },
));
C.push(H2("3.3 Faktenprüfung der Aufgabenideen Ozean, Flüsse und Atmosphäre vom 20.10.2026 (K19)"));
C.push(P("Arbeitsannahmen, die nach der Faktenprüfung korrigiert, präzisiert oder als Annahme gekennzeichnet wurden. Die Aufgabenideen verwenden die korrigierten Werte; die Quellen stehen dort im Abschnitt Quellen."));
C.push(grid(
  ["Aussage im Entwurf", "Ergebnis der Prüfung", "Folge"],
  require("./pruefergebnisse_ozean.js"),
  [3000, 3600, 2470], { firstColBold: false, size: 16 },
));
C.push(H2("3.4 Unabhängige Gegenprüfung der Aufgabenideen (K20)"));
C.push(P("Ein getrennter Prüfauftrag hat die fertigen Aufgabenideen ohne Kenntnis ihrer Entstehung geprüft. Alle gedruckten Zahlen waren richtig gerechnet und gerundet; die Befunde betrafen Vorzeichen, Modelllogik, fehlende Angaben und Quellenaussagen. Umgesetzt sind alle bis auf zwei Notationshinweise, die bewusst bleiben (siehe K20)."));
C.push(grid(
  ["Aussage im Entwurf", "Ergebnis der Prüfung", "Folge"],
  require("./pruefergebnisse_ozean_gegenpruefung.js"),
  [3000, 3600, 2470], { firstColBold: false, size: 16 },
));

C.push(H2("3.5 Unabhängige Gegenprüfung der Kaffee-Aufgabe (K25)"));
C.push(P("Ein getrennter Prüfauftrag hat Aufgabenblatt, Lösung und Abbildungen ohne Kenntnis ihrer Entstehung geprüft und alle Zahlen mit einem eigenen Skript nachgerechnet. Die Rechnung in a bis e war richtig; die Befunde betrafen den Becher-Fall in den Hinweisen, Rundungen, Abbildungen, Wortlaut und zwei Quellenwerte."));
C.push(grid(
  ["Aussage im Entwurf", "Ergebnis der Prüfung", "Folge"],
  require("./pruefergebnisse_kaffee_gegenpruefung.js"),
  [3000, 3600, 2470], { firstColBold: false, size: 16 },
));

C.push(H2("3.6 Unabhängige Gegenprüfung der Aufgabensammlung (K29)"));
C.push(P("Drei getrennte Prüfaufträge haben die Sammlung ohne Kenntnis ihrer Entstehung geprüft und alle Kernergebnisse mit eigenen Skripten nachgerechnet. Kein gedrucktes Ergebnis war falsch gerechnet; die Befunde betrafen Widersprüche zwischen Text und Modell, eine falsche Begründung in der Kaffee-Musterlösung, fehlende Angaben und Kennzeichnungen, Querverweise, Quellen und den Satz. Die vollständigen Berichte liegen im Arbeitsordner (pruefung/bericht_A.md bis bericht_C.md)."));
C.push(grid(
  ["Aussage im Entwurf", "Ergebnis der Prüfung", "Folge"],
  require("./pruefergebnisse_sammlung_gegenpruefung.js"),
  [3000, 3600, 2470], { firstColBold: false, size: 16 },
));

C.push(H1("4. Bekannte Grenzen"));
[
  "KI kann Quellen falsch zuordnen oder Zahlen verwechseln. Deshalb steht bei jeder Quelle, wie sie geprüft wurde; Angaben aus Sekundärquellen sind gekennzeichnet.",
  "Websuchen erreichen nicht jede Quelle (Bezahlschranken, Abrufsperren). Nicht erreichbare Quellen sind als „nicht geprüft“ markiert.",
  "Zahlen zu Klima, Energie und Recht ändern sich (z. B. Strommix, Energieeffizienzgesetz). Jede Angabe trägt einen Stand.",
  "Vereinfachte Modelle (Schichtmodell der Atmosphäre, lineares Eisprofil) sind bewusst einfach und als solche gekennzeichnet.",
  "Auch die eigene Prüfung kann Fehler übersehen: Die Gegenprüfungen vom 17.10.2026 (35 Befunde), vom 20.10.2026 (ein Vorzeichenfehler, mehrere Lücken in der Modelllogik), vom 21.10.2026 (Becher-Fall mit falschem *kA*) und die Gegenprüfung der Aufgabensammlung (falsche Begründung in der Kaffee-Musterlösung, Widerspruch beim Wostoksee) fanden trotz Faktenprüfung und Nachrechnung Fehler. Eine Prüfung durch Mitarbeitende des Lehrstuhls bleibt vor dem Einsatz nötig (Arbeitsplan, Phase 5).",
  "Sprachliche und didaktische Formulierungen sind Vorschläge; Auswahl und Wortlaut bestimmt die Tutoriumsleitung.",
].forEach((t) => C.push(Bullet(t)));

C.push(H1("5. Reproduzierbarkeit"));
C.push(grid(
  ["Datei", "Zweck", "Aufruf"],
  [
    ["bilanzformen.py", "Grafik „Energiebilanz: vier Grundformen“, alle Varianten", "python3 bilanzformen.py <ordner>"],
    ["widerstand_meereis.py", "Beispielgrafik Wärmedurchgang durch Meereis", "python3 widerstand_meereis.py <ordner>"],
    ["nachrechnung_leitphaenomene.py", "Nachrechnung aller Aufgabenskizzen", "python3 nachrechnung_leitphaenomene.py"],
    ["pilot_tutorium1.py", "Zahlen des Pilotblatts Tutorium 1", "python3 pilot_tutorium1.py"],
    ["pilot_t1_grafiken.py", "Grafiken des Pilotblatts", "python3 pilot_t1_grafiken.py <ordner>"],
    ["aufgabenideen_ozean.js", "Word-Fassung der Aufgabenideen aus dem Markdown", "node aufgabenideen_ozean.js <md> <png> <docx>"],
    ["nachrechnung_ozean_atmosphaere.py", "Nachrechnung der Aufgabenideen Ozean, Flüsse und Atmosphäre", "python3 nachrechnung_ozean_atmosphaere.py"],
    ["kaffee_modell.py", "Modell und Arbeitswerte der Kaffee-Aufgabe (eine Quelle für alle Zahlen)", "wird von den folgenden Skripten geladen"],
    ["nachrechnung_kaffee.py", "Nachrechnung der Kaffee-Aufgabe mit Empfindlichkeit", "python3 nachrechnung_kaffee.py"],
    ["abb_kaffee.py, abb_loesung.py", "Abb. 1 sowie Abb. L1 und L2 der Kaffee-Aufgabe", "python3 abb_kaffee.py <ordner>"],
    ["build_kaffee.py", "Aufgabenblatt und Lösung als Markdown, Word und PDF", "python3 build_kaffee.py (braucht pandoc, XeLaTeX, Ordner build)"],
    ["SPEZ.md, PRUEFAUFTRAG.md", "Spezifikation der Arbeitsagenten und Prüfauftrag der Gegenprüfung (Aufgabensammlung)", "lesen"],
    ["rechnung/t1_rechnung.py bis t8_rechnung.py", "Zahlen je Tutorium; prüft, dass jede Zahl im Text der Sammlung steht", "python3 t1_rechnung.py (im Ordner rechnung)"],
    ["rechnung/t5_kaffee_teil.py", "erzeugt den Kaffee-Teil der Sammlung aus dem Kaffee-Modell", "python3 t5_kaffee_teil.py"],
    ["skripte/abb_t1_eisschild.py bis abb_t8_pol.py, skizze_stil.py", "Skizzen der Sammlung in einheitlichem Stil", "python3 abb_t1_eisschild.py (im Ordner skripte)"],
    ["build/sammlung_bauen.py", "Sammlung als Markdown, PDF und Word (mit kopf.tex, lehrstuhl.lua und referenz_sammlung.docx)", "python3 sammlung_bauen.py <ordner>"],
    ["build/teil_bauen.py", "einzelnen Teil der Sammlung zur Sichtprüfung bauen", "python3 teil_bauen.py <teil.md> <ordner>"],
    ["Kaffee_Pruefpaket: rollen_vorbereiten.py", "legt je Prüferrolle einen Ordner mit Auftrag und nur den Dateien ihrer Leseliste an (leseliste.json)", "python3 rollen_vorbereiten.py <paket> <arbeitsordner>"],
    ["Werkzeugkasten: umgebung_pruefen.py, werkzeugkasten_packen.py", "prüft und richtet die Arbeitsumgebung ein; packt den Werkzeugkasten nach einer Runde mit neuer Version und frischt den Index auf", "python3 umgebung_pruefen.py; python3 werkzeugkasten_packen.py --notiz <Satz>"],
    ["Werkzeugkasten: arbeitsordner/werkzeuge/neue_einzelaufgabe.py, einzelblatt.py", "legt Modell, Nachrechnung, Abbildungen und Bauskript einer neuen Einzelaufgabe an; Bausteine für Blatt und Lösung (PDF, Word, Seitenbilder)", "python3 werkzeuge/neue_einzelaufgabe.py <kurz> --tutorium N --teil tN.md --block <Titel>"],
    ["Werkzeugkasten: pruefung/material_zusammenstellen.py, rollen_vorbereiten.py", "stellt das Prüfmaterial einer Aufgabe zusammen (A bis F) und legt je Rolle einen Ordner an (Muster in Leselisten, Teilrollen, Prüfung auf offene Platzhalter)", "python3 pruefung/material_zusammenstellen.py --aufgabe … --name … --tutorium N --paket …"],
  ],
  [2700, 3700, 2670], { firstColBold: true },
));
C.push(Small("Für die Grafiken werden die Schriften Noto Sans und Caladea benötigt, für die Skizzen und das PDF der Aufgabensammlung Carlito (siehe LIESMICH.txt).", { before: 80 }));

C.push(H1("6. Änderungsverlauf"));
C.push(grid(
  ["Version", "Datum", "Änderung"],
  [
    ["1", "17.10.2026", "Protokoll angelegt; Einsätze vom 16.10.2026 nachgetragen; Einsätze vom 17.10.2026 eingetragen"],
    ["2", "17.10.2026", "Unabhängige Gegenprüfung eingetragen (K14, Abschnitt 3.2); erneuter Ablageversuch (K15); Prüfagent als Werkzeug ergänzt"],
    ["3", "17.10.2026", "Kurzkonzept, Mailentwurf und Pilotblatt Tutorium 1 eingetragen (K16 bis K18); Korrektur der mittleren Wärmeleitfähigkeit in Abschnitt 3.2"],
    ["4", "20.10.2026", "Aufgabenideen Meeresströmungen und Luftströmungen eingetragen (K19 bis K21), Faktenprüfung in Abschnitt 3.3, unabhängige Gegenprüfung in Abschnitt 3.4, Claude-Dokumente als Werkzeug ergänzt"],
    ["4.1", "21.10.2026", "PDF der Aufgabenideen (K22)"],
    ["5", "21.10.2026", "Lehrstuhl-Struktur und Kaffee-Aufgabe (K23 bis K26), unabhängige Gegenprüfung in Abschnitt 3.5, Werkzeuge und Reproduzierbarkeit ergänzt"],
    ["6", "21.10.2026", "Bausteine der Kaffee-Aufgabe (K27), Aufgabensammlung mit Arbeitsagenten (K28), unabhängige Gegenprüfung der Sammlung (K29, Abschnitt 3.6), Ablage (K30); Arbeitsagenten als Werkzeug, Reproduzierbarkeit ergänzt"],
    ["7", "23.10.2026", "Kaffee-Aufgabe als Claude-Dokument (K31); Vorbereitung der unabhängigen Prüfung mit sechs Rollen, Prüfpaket und Trockenlauf (K32); Reproduzierbarkeit ergänzt"],
    ["8", "23.10.2026", "FVT-Vorlage für die Gestaltungsrolle und Werkzeugkasten für künftige Aufgaben (K33); Reproduzierbarkeit ergänzt"],
  ],
  [1200, 1500, 6370], { firstColBold: true },
));
C.push(Small("Vorlage für neue Einträge: Nr. | Datum | Auftrag | Tätigkeit der KI | Ergebnis | Prüfung | Probleme und Korrekturen", { before: 120 }));

write(makeDoc({
  title: "Tutorien Wärmeübertragung: KI-Protokoll",
  description: "Einsatz von KI (Claude) bei der Entwicklung der Tutorien, fortlaufend.",
  footerText: "Tutorien Wärmeübertragung: KI-Protokoll",
  children: C,
}), OUT);
