// Entscheidungsprotokoll (Grundlagen und Entscheidungen), fortlaufend
// Aufruf: node protokoll_entscheidungen.js <ausgabe.docx>
const h = require("./fvt_doc.js");
const { P, Small, H1, H2, Bullet, grid, box, boxTitle, Paragraph, TextRun, AlignmentType, makeDoc, write, W } = h;
const OUT = process.argv[2] || "Entscheidungsprotokoll.docx";
const C = [];

C.push(new Paragraph({ style: "Title", children: [new TextRun("Tutorien Wärmeübertragung: Entscheidungsprotokoll")] }));
C.push(P("Grundlagen und Entscheidungen der Aufgabenentwicklung, fortlaufend geführt", { size: 24, color: h.GREY, align: AlignmentType.LEFT, before: 0, after: 120 }));
C.push(Small("**Version:** 10 · **Stand:** 30.10.2026 · **Geführt von:** Tutoriumsleitung, Einträge vorbereitet mit KI-Unterstützung (Claude, Anthropic)"));
C.push(Small("**Begleitdokumente:** „Lernziele, Vorab-Fragen und Bilanz-Systematik“ (16.10.2026), „Leitaufgaben aus Klima und Erde“ (17.10.2026), „Aufgabenideen: Meeresströmungen, Sverdrup und Luftströmungen“ (20.10.2026), „Kaffee mit Milch“ (Aufgabe und Lösung, 21.10.2026), „Strukturvorlage: Aufgaben im Stil des Lehrstuhls“ (21.10.2026), „Aufgabensammlung der Tutorien“ (21.10.2026), Plan und Prüfpaket zur Prüfung der Kaffee-Aufgabe (23.10.2026), Prüfberichte, Bündelung und Änderungsvorschläge zur Kaffee-Aufgabe (29.10.2026), KI-Protokoll", { after: 160 }));

C.push(box([
  h.boxTitle("Wozu dieses Protokoll?"),
  h.boxPara("Mitarbeitende und Wissenschaftler:innen am Lehrstuhl sollen nachvollziehen können, welche Entscheidung wann, von wem und auf welcher Grundlage getroffen wurde und wie sie sich zurücknehmen lässt. Neue Einträge werden unten angehängt, die Nummern laufen weiter. Ändert sich der Status, wird die Zeile angepasst und die Änderung im Änderungsverlauf vermerkt."),
]));

C.push(H1("1. Legende"));
C.push(grid(
  ["Feld", "Bedeutung"],
  [
    ["Status", "**vorgeschlagen** (liegt zur Entscheidung vor) · **entschieden** · **umgesetzt** · **offen** (wartet auf eine Person oder Information) · **verworfen**"],
    ["Entschieden von", "**TL** Tutoriumsleitung · **Prof.** Professorin · **KI** Vorschlag von Claude, noch nicht entschieden"],
    ["Grundlage", "**V** Vorlesung, Formelsammlung, Übungen und Tutorien des Lehrstuhls · **L** bereitgestellte Literatur (Holman 2010) · **F** Lehr-Lern-Forschung · **G** Leitfäden und Richtlinien · **D** Fachdaten (Klima und Erde, Stoffwerte, Alltagswerte) · **N** eigene Nachrechnung · **M** Vorgabe oder Rückmeldung der Tutoriumsleitung"],
    ["Bezug", "Nummer in den Begleitdokumenten, z. B. E1 bis E6 (16.10.2026), E7 bis E17 (17.10.2026) und E18 bis E22 (20.10.2026)"],
    ["Neue Einträge", "Nr. | Gegenstand und Entscheidung | Grundlage | Von | Status | Rückweg; Nummern laufen weiter"],
  ],
  [1800, 7270], { firstColBold: true },
));

C.push(H1("2. Grundlagen"));
C.push(P("Vollständige Literaturangaben stehen in den Quellenverzeichnissen der Begleitdokumente (16.10.2026: Abschnitt 10; 17.10.2026: Abschnitt 12), jeweils mit Prüfstatus (Volltext, Abstract, Sekundärquelle, nicht geprüft)."));
C.push(grid(
  ["Nr.", "Grundlage", "Typ", "Genutzt für"],
  [
    ["G01", "Vorlesungsfolien Wärmeübertragung 01 bis 08, SoSe 2026 (Riese)", "V", "Abgleich aller Lernziele, Notation, Unterthemen, Beispiele"],
    ["G02", "Formelsammlung SoSe 2026 und Zusatzblatt Charakteristische Längen", "V", "Lösbarkeit der Aufgaben, Korrelationen, charakteristische Länge"],
    ["G03", "Modulhandbuch, Auszug Inhalte und Lernergebnisse (Fassung unbekannt)", "V", "Lernziele, Bezug je Tutorium"],
    ["G04", "Holman (2010), Heat Transfer", "L", "erster Entwurf; Strahlung der Umwelt (Abschnitt 8-15); periodische Randbedingung (Aufgaben 4-18, 4-19)"],
    ["G05", "FVT-Vorlagen (Präsentation, Aufgabenstellung, Poster, Logos)", "M", "Gestaltung der Grafiken und Dokumente"],
    ["G06", "Leitfäden zu Lernzielen: Kennedy (2006), Gröblinghoff (2015), UPB-Handreichung (2024), Biggs (2014)", "G", "Regeln für Lernziele"],
    ["G07", "Lernziele und Vorab-Fragen: Sana et al. (2020), St. Hilaire et al. (2024), Pan & Carpenter (2023), Kaplan & Rothkopf (1972), Melton (1978)", "F", "Vorab-Fragen, Platzierung der Lernziele"],
    ["G08", "Taxonomie: Anderson & Krathwohl (2001), Krathwohl (2002)", "F", "Stufen der Lernziele"],
    ["G09", "Aufgabenvergleich und Ordnen: Alfieri et al. (2013), Chi et al. (1981), Dufresne et al. (1992), Rohrer & Taylor (2007), Brunmair & Richter (2019)", "F", "Bilanz-Systematik, Zuordnen, gemischtes Üben"],
    ["G10", "Gestaltung: Schneider et al. (2018), Reigeluth & Stein (1983)", "F", "Grafik mit Markierung, wiederkehrende Übersicht"],
    ["G11", "Schwierige Konzepte: Streveler et al. (2003)", "F", "stationär gegenüber Gleichgewicht, differentiell gegenüber integral"],
    ["G12", "Aufgabendesign: Blum & Leiß (2007), Renkl & Atkinson (2003), Kalyuga et al. (2003), Kirschner et al. (2006), Gentner et al. (2003), Rey (2012), Sundararajan & Adesope (2020), Hidi & Renninger (2006), Hulleman & Harackiewicz (2009), Chi et al. (1994), Bisra et al. (2018), Prince et al. (2012), Crouch & Mazur (2001), Adesope et al. (2017), Bennett et al. (2007)", "F", "Aufgabenbauplan, Einstiegstexte, Zusatzaufgaben, Reflexion"],
    ["G13", "Bildungstheorie: Klafki, epochaltypische Schlüsselprobleme; Climate Literacy (USGCRP 2009)", "F", "Begründung der Klima- und Erdkontexte"],
    ["G14", "Fachdaten zu Klima und Erde (Quellenliste der Ideensammlung, Abschnitt 12.2)", "D", "Zahlen und Fakten der Aufgabenskizzen"],
    ["G15", "Nachrechnung V05 Beispiel 5 und V08 Teile d und e", "N", "Aufwärmbeispiel, Käse-Diskussionsfall"],
    ["G16", "Nachrechnung der Aufgabenskizzen (Skript nachrechnung_leitphaenomene.py)", "N", "Lösbarkeit und Plausibilität der Leitaufgaben"],
    ["G17", "Rückmeldung der Tutoriumsleitung zum Dokument vom 16.10.2026", "M", "Entscheidungen E1 bis E6 und Folgeentscheidungen"],
    ["G18", "Gespeicherte Vorgaben der Tutoriumsleitung (Typografie, neutrale Formulierung, Notation)", "M", "Gestaltung aller Texte"],
    ["G19", "Unabhängige Gegenprüfung der Ideensammlung vom 17.10.2026 (getrennter Prüfauftrag, 35 Befunde; KI-Protokoll K14)", "N", "Korrekturen D43 bis D50"],
    ["G20", "Nachprüfung an der Quelle am 17.10.2026: Bohrbericht EPICA Dome C (Augustin et al., 2007), Wärmeleitfähigkeit von Schnee (Sturm et al., 1997)", "D", "Dome C, Spannbreite für Schnee"],
    ["G21", "Entscheidungen der Tutoriumsleitung zum Pilot vom 17.10.2026 (Abfrage im Chat)", "M", "D51 bis D54"],
    ["G22", "Nachrechnung Pilotblatt Tutorium 1 (Skript pilot_tutorium1.py)", "N", "Zahlen des Pilotblatts und der Musterlösung"],
    ["G23", "Wunsch der Tutoriumsleitung vom 20.10.2026: Aufgaben zu Meeresströmungen (Wärme im Golfstrom und Temperaturen in Europa, AMOC mit 20 % weniger Wärmetransport), zur Einheit Sverdrup, zum Amazonas mit *Q̇* = *ṁ* *c*_{p} Δ*T* und zu Luftströmungen (Polarjet, Passat), ohne die Aufgaben zu komplex zu machen", "M", "Aufgabenideen A bis C, D57 bis D63"],
    ["G24", "Faktenprüfungen vom 20.10.2026 zu Ozean, Flüssen und Atmosphäre (drei Rechercheagenten; Quellenliste der Aufgabenideen; KI-Protokoll K19 und Abschnitt 3.3)", "D", "Zahlen, Einstiegsfakten und Forschungsstand der Aufgabenideen"],
    ["G25", "Nachrechnung der Aufgabenideen (Skript nachrechnung_ozean_atmosphaere.py, Version 3)", "N", "Kernzahlen und Lösungsskizzen der Aufgaben A bis C"],
    ["G26", "Unabhängige Gegenprüfung der Aufgabenideen vom 20.10.2026 (getrennter Prüfauftrag; KI-Protokoll K20 und Abschnitt 3.4)", "N", "Korrekturen in D64"],
    ["G27", "Lehrstuhlmaterial vom 21.10.2026: Übungen 1 bis 9 (SoSe 2026, mit Kurzlösung und Lösung), Tutorien 1 bis 8 mit Lösung, handschriftliche Vorlesungsbeispiele 1 bis 9; Vorbilder laut Tutoriumsleitung: Tutorium 3, Aufgabe 3 (Fußbodenheizung, Klausur 2022-02-17) und Tutorium 6, Aufgabe 1 (Nikolaus, Klausur 2017-08-09)", "V", "Strukturvorlage, D65 und D66"],
    ["G28", "Wunsch der Tutoriumsleitung vom 21.10.2026: Kaffee-Aufgabe mit zwei Tassen (Milch sofort oder nach 60 Minuten, Wärmekapazität der Tasse null), welche Tasse ist kühler; Aufgabenstruktur näher am Lehrstuhl, Rechenstil der Professorin einbeziehen, minimalistisch, nicht zu komplex, aber didaktisch sinnvoll fordernd", "M", "D65 bis D70"],
    ["G29", "Recherche der Arbeitswerte zur Kaffee-Aufgabe vom 21.10.2026 (Rechercheagent; Quellen in der Lösung: Brown & Diller 2008, Abraham & Diller 2019, SCA, BfR 2023, FSANZ 2011, Goff, Ferreira 2025, Condoret 2007)", "D", "Arbeitswerte in D68"],
    ["G30", "Nachrechnung der Kaffee-Aufgabe (Skripte kaffee_modell.py und nachrechnung_kaffee.py: Empfindlichkeit, Becher, nichtlineare Wärmeabgabe, allgemeine Prüfung des Vorzeichens)", "N", "alle Zahlen in Aufgabe und Lösung"],
    ["G31", "Unabhängige Gegenprüfung der Kaffee-Aufgabe vom 21.10.2026 (getrennter Prüfauftrag mit eigener Nachrechnung und Quellenprüfung; KI-Protokoll K25 und Abschnitt 3.5)", "N", "Korrekturen in D71"],
    ["G32", "Rückmeldung der Tutoriumsleitung vom 21.10.2026 (15:36) zu den Erweiterungen der Kaffee-Aufgabe: Becher mit Wärmekapazität als Teilaufgabe, Zeitfrage T(60 min) oder t(60 °C), Milchschaum-Variante, Live-Versuch, Milch mit 8 °C und Rausstellen der Milch (2×2 Fälle)", "M", "D72 bis D75, D81"],
    ["G33", "Rückmeldung der Tutoriumsleitung vom 21.10.2026 (15:46): Ausgangssituation mit Text und Skizze ganz am Anfang; Frage vor der Aufgabenstellung beibehalten; Struktur für alle bisher erarbeiteten Aufgaben übernehmen; große Aufgabensammlung als PDF und Word; Ablage in Sciebo durch die Tutoriumsleitung, bis dahin auf dem Schreibtisch; KI-Protokoll fortführen", "M", "D76 bis D80"],
    ["G34", "Recherche vom 21.10.2026: Milchschaum 55 bis 65 °C (Thermoplan), Kühlschranktemperaturen in Haushalten (Evans et al., 2014, nach IIR), Vorhersagen bei Demonstrationen (Crouch et al., 2004, Am. J. Phys. 72, 835)", "D, F", "D74, D75, D81"],
    ["G35", "Nachrechnungen der Aufgabensammlung: kaffee_modell.py mit Becher und Kipppunkt, t5_kaffee_teil.py, Rechenskripte je Tutorium (t1 bis t8)", "N", "alle Ergebniszeilen der Sammlung"],
    ["G36", "Unabhängige Gegenprüfung der Aufgabensammlung vom 21.10.2026 (drei getrennte Prüfaufträge für Tutorium 1 bis 3, 4 und 5 sowie 6 bis 8, je mit eigener Nachrechnung; Berichte A, B und C im Arbeitsordner; KI-Protokoll K29 und Abschnitt 3.6)", "N", "D82 bis D86"],
    ["G37", "Wunsch der Tutoriumsleitung vom 21.10.2026 (19:04): Kaffee-Aufgabe separat als PDF, Word und als Claude-Dokument, in dem sie Feedback in [ ] gibt und die KI direkt ändert", "M", "D87"],
    ["G38", "Wünsche der Tutoriumsleitung vom 23.10.2026 (00:37 bis 09:22): die Kaffee-Aufgabe mit Anforderungen, Vorlagen und Lehrstuhlaufgaben unabhängig prüfen lassen (Rollen wie Prüfer, Professorin, Recherche) und Änderungsvorschläge auf didaktischer, technischer und inhaltlicher Ebene finden; Pause wegen des Nutzungsvolumens; alle Rollen mit dem Hauptmodell, Leselisten je Rolle; zusätzlich eine Gestaltungsrolle mit Blick auf die Formatvorlagen; ein Gesamtprompt statt einzelner Chats, eine Anleitung, alle Dateien in die Ablage", "M", "D88, D89"],
    ["G39", "Wünsche der Tutoriumsleitung vom 23.10.2026 (10:34): die Word-Vorlage „Aufgabenstellungen“ als Datei für die Gestaltungsrolle (kleine Anpassung); alle Erkenntnisse, Vorgänge, Arbeitsweisen und Planungen für spätere Aufgaben sichern, als Dateien oder ZIP, das bei der Überarbeitung einer weiteren Tutoriumsaufgabe angehängt wird und sofort weiterarbeiten lässt; möglichst sparsam, ohne die Arbeit einzuschränken", "M", "D90 bis D92"],
    ["G40", "Prüfberichte P, T, D, R, S und G vom 29.10.2026 und Bericht von Codex (Rolle X) vom 30.10.2026: unabhängige Prüfung der Kaffee-Aufgabe mit sechs Rollen, je mit eigener Leseliste, eigenem Materialordner und eigener Nachrechnung, dazu die Gegenprüfung durch Codex; Bündelung zu den Änderungsvorschlägen Ä1 bis Ä30 mit Nachrechnung aller Zahlen durch die Koordination (KI-Protokoll K34 und Abschnitt 3.7; Berichte, Bündelung und Vorlage im Repository unter ergebnisse/kaffee/ und im Tab „Änderungsvorschläge“ des Claude-Dokuments)", "N, F", "D93 bis D102"],
    ["G41", "Entscheidung der Tutoriumsleitung vom 30.10.2026 im Chat: Ä1 bis Ä22, Ä24 bis Ä27, Ä29 und Ä30 ja; Ä23 vertagt; Ä28 nur als Impuls; Widersprüche W1 bis W6 und Vorgaben V1 bis V3 wie empfohlen. Zusätzlich: beim Umsetzen auf den Umfang des Aufgabenblatts achten und die Länge danach gegen die Strukturvorlage prüfen; was nicht zwingend auf das Blatt muss, kommt in die Lösung oder die Hinweise", "M", "D93 bis D102"],
  ],
  [600, 4300, 600, 3570], { firstColBold: true },
));

C.push(H1("3. Entscheidungen"));
const rows = (list) => list.map((r) => r);
const TAB = (list) => grid(
  ["Nr.", "Gegenstand und Entscheidung", "Grundlage", "Von", "Status", "Rückweg"],
  rows(list),
  [650, 3300, 1450, 650, 1450, 1570], { firstColBold: true, size: 16 },
);

C.push(H2("3.1 Sitzung vom 16.10.2026: Lernziele, Bilanz-Systematik, Grafik"));
C.push(TAB([
  ["D01", "Je Tutorium zwei Lernziele: Ziel 1 Anwenden (berechnen, herleiten, aufstellen), Ziel 2 Bewerten (beurteilen). Tutorium 1 ausgehend vom Entwurf der Tutoriumsleitung, Änderungen markiert.", "G03, G06, G08", "TL", "umgesetzt; Fassung 2 als Entwurf (D34)", "zwei Ziele beibehalten"],
  ["D02", "Satzmuster und acht Regeln für Lernziele (u. a. ein Verb je Ziel, keine vagen Verben, Ziele direkt vor den Aufgabenteil).", "G06, G07, G08", "TL nach KI", "umgesetzt; Regel 1 gelockert (D12)", "Regel einzeln streichen"],
  ["D03", "Themenfolge der acht Tutorien wie von der Tutoriumsleitung vorgegeben.", "M", "TL", "umgesetzt", "Reihenfolge ändern"],
  ["D04", "Abgleich mit den Folien: Sichtfaktor, Strahlungsschirm, Rippe und Fourier-Zahl entfernt; ε-NTU-Konzept, Nußelt, Parallelschaltung, Kugelschale, Isolationsdicke ergänzt.", "G01, G02", "TL nach KI", "umgesetzt", "Folienstand erneut prüfen"],
  ["D05", "Bilanz-Systematik mit zwei Achsen (stationär/instationär, global/differentiell). Stationär global ohne eigenes Tutorium; die drei Bilanz-Tutorien bleiben getrennt.", "G01 (V05 F. 8), G11", "TL nach KI", "umgesetzt", "Tutorium 5 bis 7 zusammenlegen"],
  ["D06", "Grafik „Energiebilanz: vier Grundformen“ im FVT-Stil, groß und kompakt, ein markiertes Feld je Aufgabe.", "G05, G10", "TL", "umgesetzt", "Grafik nicht verwenden"],
  ["D07", "Beispiel „Käse im Kühltunnel“ nicht als Beispiel für instationär global in der Grafik (*Bi* ≈ 5 bis 10); V08 Teil e als Diskussionsfall vorgeschlagen.", "G15", "TL nach KI", "umgesetzt; bestätigt durch D17", "Rückfrage an die Übungsleitung"],
  ["D08", "Vorab-Frage in jedem Tutorium (E2).", "G07", "TL", "entschieden (D13)", "Fragen weglassen"],
  ["D09", "Blockziel „Bilanzaufgaben einer Grundform zuordnen“ für Tutorium 5 bis 7 (E3).", "G09", "TL", "entschieden (D14)", "Ziel streichen"],
  ["D10", "Ausarbeitung als Word und PDF im FVT-Layout für Sciebo; Markdown in der Projektablage.", "M", "TL", "umgesetzt; Ablage in Sciebo offen (Rechner nicht erreichbar)", "anderes Format"],
  ["D11", "Typografie: keine Gedankenstriche, Bereiche mit „bis“, typografische Anführungszeichen; Texte für Betreuende neutral, KI-Einsatz offen benannt.", "G18", "TL", "umgesetzt", "keiner nötig"],
]));

C.push(H2("3.2 Rückmeldung der Tutoriumsleitung zum Dokument vom 16.10.2026"));
C.push(TAB([
  ["D12", "E1: Lernziele dürfen mehr als ein Verb haben, wenn weitere Themenschwerpunkte sehr relevant sind.", "G17", "TL", "entschieden; umgesetzt im Entwurf Fassung 2", "ein Verb je Ziel"],
  ["D13", "E2: Vorab-Fragen bleiben; Anpassung an die Leitaufgaben möglich.", "G17, G07", "TL", "entschieden; Vorschläge in E10", "bisherige Fragen"],
  ["D14", "E3: Das Zuordnen der Bilanzformen kann eine Aufgabe werden.", "G17, G09", "TL", "entschieden; Zusatzaufgabe „Bilanz-Detektiv“", "nur Lernziel"],
  ["D15", "E4: Tutorium 6 heißt „Wärmebilanzen (stationär differentiell)“.", "G17", "TL", "umgesetzt", "alter Name"],
  ["D16", "E5: Rohrwand nicht in Tutorium 1; Komplexität schrittweise erhöhen.", "G17, G12", "TL", "entschieden; Rohr in Tutorium 3", "Rohr in Tutorium 1"],
  ["D17", "E6: Diskussion und Reflexion in jedem Tutorium; weg vom reinen Rechnen, hin zum Gesamtdenken in einem Realfall.", "G17", "TL", "entschieden; Phase 5 im Bauplan", "keiner nötig"],
  ["D18", "Eine große Leitaufgabe je Tutorium mit Einstiegstext, Teilaufgaben in kleinen Schritten, Prüfung und Reflexion; dazu kleine Zusatzaufgaben.", "G17", "TL", "entschieden; Bauplan als Vorschlag (D33)", "bisherige Aufgabenform"],
  ["D19", "Leitaufgaben aus Klima- und Erdthemen; Begründung über Klafkis epochaltypische Schlüsselprobleme (Umweltfrage).", "G17, G13", "TL", "entschieden; Auswahl offen (D30)", "technische Kontexte"],
  ["D20", "Lernziele direkt über die Leitaufgabe; kompaktes Bilanz-Schild in den Aufgabenkopf.", "G17, G07", "TL", "entschieden", "Ziele gesammelt am Anfang"],
  ["D21", "Plausibilitätsrechnungen als fester Bestandteil.", "G17", "TL", "entschieden; Phase 4 im Bauplan", "keiner nötig"],
  ["D22", "Begriffe und Mathematik eng an der Vorlesung; Zusatzwissen gekennzeichnet.", "G17, G01", "TL", "entschieden", "keiner nötig"],
  ["D23", "Unterthemen aufnehmen: Geschwindigkeits- und Temperaturgrenzschicht, Kirchhoff’sches Gesetz, Bezugsfläche, charakteristische Länge (bei Konvektion), *kA* = 1/*R*, d*T*/d*t* gegenüber d*T*/d*x* und d*T*/d*r*, Massenbilanz und Kontinuität.", "G17, G01", "TL", "entschieden; umgesetzt im Entwurf Fassung 2", "Unterthema einzeln streichen"],
  ["D24", "Nicht aufnehmen: Euler- und Lagrange-Betrachtung; Lösen von Differentialgleichungen mit Kapitel 5 der Formelsammlung.", "G17", "TL", "entschieden", "aufnehmen"],
  ["D25", "Druckverlust und Pumpenleistung, Filmkondensation nach Nußelt, Sieden, Latentwärmespeicher nur nach Rücksprache mit der Professorin; Qualität vor Quantität.", "G17", "TL", "offen (Prof.)", "nicht aufnehmen"],
  ["D26", "Methodisches Vorgehen nach V01 F. 28 und das Verstehen und Aufstellen von Annahmen werden gefördert und gefordert, auch als Lernziel.", "G17, G01", "TL", "entschieden; Querschnitts­ziel Q1", "keiner nötig"],
  ["D27", "Grafikvarianten mit zwei markierten Feldern ansehen und dann entscheiden.", "G17", "TL", "Varianten erzeugt; Entscheidung offen (E14)", "nur ein Feld je Schild"],
  ["D28", "Englische Fassung: entscheidet die Professorin (Klausuren sind deutsch).", "G17", "TL", "offen (Prof.)", "keiner nötig"],
  ["D29", "Entscheidungen fundiert begründen und protokollieren; zusätzlich ein KI-Protokoll führen.", "G17", "TL", "umgesetzt mit diesem Dokument", "keiner nötig"],
]));

C.push(H2("3.3 Sitzung vom 17.10.2026: Vorschläge zur Entscheidung"));
C.push(TAB([
  ["D30", "E7: Leitphänomen je Tutorium wie Tabelle 1 der Ideensammlung (Eisschild, Rinnen im Meereis, Meereis und Pipeline, Strahlungsbilanz, Ozean als Speicher, Erdwärme, Bodentemperatur, Wärmepumpe).", "G01, G02, G12 bis G14, G16", "KI", "vorgeschlagen", "Alternativen aus Abschnitt 4 und 5"],
  ["D31", "E8: Polarblock in Tutorium 1 bis 3 behalten.", "G16", "KI", "vorgeschlagen", "Bohrloch, Windchill"],
  ["D32", "E9: Technische Zwillingsaufgabe in jedem Tutorium.", "G12 (Gentner et al. 2003)", "KI", "vorgeschlagen", "nur ausgewählte Tutorien"],
  ["D33", "Aufgabenbauplan in fünf Phasen; Regeln für Einstiegstexte; Gerüst nimmt über das Semester ab.", "G01 (V01 F. 28), G12", "KI", "vorgeschlagen; Umsetzung im Format des Lehrstuhls (D65)", "Bauplan anpassen"],
  ["D34", "Querschnittsziele Q1 bis Q3 und Fachziele Fassung 2.", "D12, D17, D21, D23, D26", "KI", "vorgeschlagen", "Fassung vom 16.10.2026"],
  ["D35", "E10: Vorab-Fragen thematisch anpassen, in Tutorium 4 die bisherige Frage behalten.", "G07", "KI", "vorgeschlagen", "bisherige Fragen"],
  ["D36", "E11: Zusatzwissen in Tutorium 7 (gegebene Lösung der Temperaturwelle, Eindringtiefe) gekennzeichnet verwenden.", "G04, G01", "KI", "vorgeschlagen; Rücksprache Prof.", "nur Aufstellen und Deuten"],
  ["D37", "E12: Pilot mit Tutorium 1.", "G12", "KI", "vorgeschlagen", "Tutorium 3"],
  ["D38", "E13: Bodentemperaturen des Deutschen Wetterdienstes in Tutorium 7.", "G14", "KI", "vorgeschlagen; Daten prüfen", "Literaturwerte"],
  ["D39", "E14: Zwei-Feld-Varianten 12 (Tutorium 3 und 8), 13 (Übergang vom Aufwärmbeispiel zur Leitaufgabe in Tutorium 5), 34 (Biot-Diskussion in Tutorium 5), 24 (Tutorium 7).", "G10, G19", "KI", "vorgeschlagen", "ein Feld je Schild"],
  ["D40", "E15: Protokolle als Word und PDF für Sciebo und als Markdown in der Projektablage.", "G17", "KI", "vorgeschlagen", "nur eine Form"],
  ["D41", "Zeitplan mit Annahme Durchlauf im Sommersemester 2027; Pilot bis Mitte Dezember 2026.", "M", "KI", "vorgeschlagen", "Zeitplan verschieben"],
  ["D42", "Zahlen in den Aufgabenskizzen sind Arbeitswerte; endgültige Werte erst mit Primärquelle und Stand im Aufgabenblatt.", "G14, G16", "KI", "umgesetzt (Kenn­zeichnung)", "keiner nötig"],
]));

C.push(H2("3.4 Gegenprüfung vom 17.10.2026: Korrekturen und neue Vorschläge"));
C.push(P("Die Ideensammlung wurde vor der Übergabe von einem getrennten Prüfauftrag gegengeprüft (G19). Korrekturen, die nur Wortlaut, Rundung oder Quellenangaben betreffen, sind in D50 zusammengefasst; Einzelheiten stehen im KI-Protokoll, Abschnitt 3.2."));
C.push(TAB([
  ["D43", "Dome C (Tutorium 1): Die Basis liegt knapp unter dem Druckschmelzpunkt; ob sie schmilzt, ist aus den Werten nicht entscheidbar. Die Konstante der Schmelzpunktsenkung wird genannt (0,0742 K/MPa, Alternative 0,098 K/MPa). Der Vergleich 56 gegenüber 57,9 mW/m² gilt nur als Konsistenzprüfung von *λ*(*T*).", "G16, G19, G20", "KI", "umgesetzt", "keiner nötig"],
  ["D44", "Zeitkonstanten in Tutorium 5 mit den Eingangswerten der Aufgabe: 4,5 Jahre mit Tiefsee (*h* = 70 m, 2,0 W/(m²·K)), 2,4 Jahre mit 4*σT*_{e}^{3} = 3,74 W/(m²·K) aus Tutorium 4; Geoffroy et al. (2013) und die Planck-Antwort von 3,2 W/(m²·K) nur als Vergleich.", "G16, G19", "KI", "umgesetzt", "keiner nötig"],
  ["D45", "Kirchhoff in Tutorium 4: erklärt *α*_{A} = *ε*_{A} im Infraroten; die Durchlässigkeit für Sonnenlicht ist eine Modellannahme (tatsächlich rund 80 von 340 W/m² absorbiert). Teil g prüft Z3 (fehlende Konvektion und Verdunstung an der Oberfläche), Teil h prüft Z2.", "G01, G14, G19", "KI", "umgesetzt", "Teil e nur als Ankreuzaufgabe"],
  ["D46", "E16: *α* außen in Tutorium 3 als eigener Arbeitswert (15 W/(m²·K), große Scholle), begründet mit der Abnahme von *α* mit der Lauflänge aus Tutorium 2; der Wert 19,6 W/(m²·K) dient als Vergleich in Teil e.", "G16, G19", "KI", "vorgeschlagen", "19,6 W/(m²·K) übernehmen"],
  ["D47", "Tutorium 5: Metallkugel an Luft als technische Zwillingsaufgabe; Käse aus V08 Teil e nur als Diskussionsfall. Variante 34 des Bilanz-Schilds für die Biot-Diskussion, Variante 13 für den Übergang vom Aufwärmbeispiel zur Leitaufgabe (siehe D39).", "G01, G15, G19", "KI", "vorgeschlagen", "Käse als Zwilling mit Hinweis auf *Bi*"],
  ["D48", "E17: Zusatzaufgaben zählen für die Prüfung der Lernziele, wenn sie mit dem Ziel gekennzeichnet sind. Tutorium 1 prüft Z1 neu in Teil d (Firn mit Luft in den Poren).", "G06, G19", "KI", "vorgeschlagen", "jedes Ziel in der Leitaufgabe prüfen"],
  ["D49", "Einstiegsideen tragen die Teilaufgabe, in der ihre Zahl vorkommt; Ideen ohne Bezug zur Rechnung sind als „Reserve“ markiert (Regel 6.7).", "G12, G19", "KI", "umgesetzt", "Kennzeichnung entfernen"],
  ["D50", "Begriffe, Formelzeichen und Quellen vereinheitlicht: Wärmestromdichte bzw. Strahlungsflussdichte für W/m², planetare Albedo *ρ*_{p}, Amplitude Δ*T*_{0}, Index O für die Oberfläche, einjähriges Meereis, Druckschmelzpunkt; je Größe ein gerundeter Wert; Schnee rund 0,03 bis 0,7 W/(m·K); Quellenverzeichnis ergänzt und sortiert.", "G01, G18, G19, G20", "KI", "umgesetzt", "keiner nötig"],
]));

C.push(H2("3.5 Pilot Tutorium 1 vom 17.10.2026"));
C.push(TAB([
  ["D51", "Pilot mit Tutorium 1 und dem Leitphänomen „Seen unter dem Eisschild“ (E7 für Tutorium 1, E12).", "G16, G21", "TL", "entschieden", "Erdwärme im Bohrloch"],
  ["D52", "Vorab-Frage Tutorium 1: „Firn gegenüber Eis“ (E10 für Tutorium 1).", "G07, G21", "TL", "entschieden", "Hauswand mit Dämmung"],
  ["D53", "Technische Zwillingsaufgabe Tutorium 1: Kühlhauswand mit Dämmung (E9 für Tutorium 1; Empfehlung war der Industrieofen aus V02 Beispiel 1).", "G12, G21", "TL", "entschieden", "Industrieofen"],
  ["D54", "Pilot zunächst im vollen Umfang (Teile a bis i einschließlich Dome C, Zusatzaufgaben, Zwilling); Kürzung nach dem Probelauf.", "G21", "TL", "entschieden", "Kürzungsvorschläge in der Musterlösung"],
  ["D55", "Mittlere Wärmeleitfähigkeit in allen Rechnungen als Integralmittel nach V02 F. 12 statt als Mittel der Randwerte (2,43 statt 2,45 W/(m·K)); Ideensammlung und Nachrechnung angepasst.", "G01, G22", "KI", "umgesetzt", "keiner nötig"],
  ["D56", "Kurzkonzept (Claude-Dokument) und Mailentwurf an Viola als Grundlage für die Abstimmung; Versand durch die Tutoriumsleitung.", "M", "KI", "vorgeschlagen", "nur Mail ohne Anhang"],
]));

C.push(H2("3.6 Aufgabenideen Meeresströmungen und Luftströmungen vom 20.10.2026"));
C.push(TAB([
  ["D57", "E18: Aufgabe A „Die AMOC und Europas milde Winter“ wird die Leitaufgabe in Tutorium 5; die bisherige Deckschicht-Aufgabe geht als Teil i darin auf.", "G23 bis G25, G12", "KI", "vorgeschlagen", "A als Zusatz, Deckschicht-Aufgabe bleibt Leitaufgabe"],
  ["D58", "E19: Aufgabe B (Amazonas, B1 und B2) als Aufwärmen in Tutorium 5; das Kraftwerk am Fluss wird technische Zwillingsaufgabe.", "G23 bis G25, G12 (Gentner et al. 2003)", "KI", "vorgeschlagen", "B ganz in Tutorium 8"],
  ["D59", "E20: Aufgabe C (Luftströmungen) als Zusatz in Tutorium 8; der Rekordflug (C5) nur als Exkurs, weil er Kinematik statt Wärmeübertragung übt.", "G23, G24", "KI", "vorgeschlagen", "C in Tutorium 5; C5 streichen"],
  ["D60", "E21: Umstrittene Forschung (Beitrag des Ozeans zu Europas Wintern; bisherige Abschwächung der AMOC) offen als Prüfanker zeigen, beide Positionen mit Quelle; die Rechnung zeigt, woran der Streit hängt.", "G24, G12", "KI", "vorgeschlagen", "nur gesicherte Zahlen, Debatte weglassen"],
  ["D61", "E22: Sverdrup (1 Sv = 10^{6} m³/s) als gekennzeichnetes Zusatzwissen; gerechnet wird immer auch in m³/s und kg/s.", "G01, G23, D22", "KI", "vorgeschlagen", "nur m³/s verwenden"],
  ["D62", "Arbeitswerte nach der Faktenprüfung: AMOC 17 Sv (gemessen 16,9 ± 1,2 Sv) und 1,2 PW; Januarmittel Paderborn +2,1 °C (Bad Lippspringe, 1991 bis 2020) und Goose Bay −17,6 °C (1981 bis 2010); Einstrahlung im Januar 93 W/m² (eigene Rechnung); Albedo 0,4 und Deckschicht 100 m als gekennzeichnete Annahmen.", "G24, G25", "KI", "umgesetzt", "keiner nötig"],
  ["D63", "Aufgabenideen als Claude-Dokument mit Diagramm (Sverdrup-Leiter) und als Markdown in der Projektablage; Word und PDF im FVT-Layout zunächst zurückgestellt; auf Wunsch der Tutoriumsleitung am 21.10.2026 als Word und PDF erstellt.", "M, D40", "TL", "umgesetzt", "nur Claude-Dokument und Markdown"],
  ["D64", "Korrekturen nach der Gegenprüfung: eigenes Symbol Δ*q̇*_{AMOC} mit richtigem Vorzeichen in Teil h und i; Sverdrup-Definition im Aufgabentext; Goose-Bay-Vergleich nur für das Viertel (50° W bis 40° O); 1,2 PW nördlich von 40° N als Obergrenze; Richtung des Wärmestroms in B2; Hadley-Zelle eingeordnet; Rückstrom in C4; kleinere Befunde.", "G26", "KI", "umgesetzt", "keiner nötig"],
]));

C.push(H2("3.7 Lehrstuhl-Struktur, Kaffee-Aufgabe und Aufgabensammlung vom 21.10.2026"));
C.push(TAB([
  ["D65", "Neue Aufgaben folgen der Struktur des Lehrstuhls (Strukturvorlage vom 21.10.2026): Frage, Aufgabe mit Herkunft (Klausur oder „neu“), kurzer Einstiegstext, Abb. 1, Annahmen, gegebene Größen als Tabelle nach Objekt, Aufgabenstellung a) bis f) mit dem Ergebnis am Ende jedes Teils; Formatierung minimalistisch. Der Bauplan aus D33 wird darin umgesetzt (Phasen als Teilaufgaben, kein eigenes Layout).", "G27, G28", "TL", "umgesetzt in der Kaffee-Aufgabe und in der Aufgabensammlung (mit Ausgangssituation, D76)", "Bauplan-Layout aus D33"],
  ["D66", "Lösungen im Stil der Vorlesungsbeispiele und Kurzlösungen: Geg., Ges., Skizze mit Bilanzraum, Annahmen, Ansatz, dann je Teil die Rechnung mit kurzen Sätzen („Umstellen nach T:“), Zahlen mit Einheiten, Ergebnis in K und °C. Differentialgleichungen durch Trennung der Variablen mit Integrationsgrenzen, nicht über Kapitel 5 der Formelsammlung (D24).", "G27, D24", "TL nach KI", "umgesetzt in der Kaffee-Aufgabe", "bisherige Lösungsform"],
  ["D67", "Kaffee-Aufgabe „Kaffee mit Milch“ (Idee der Tutoriumsleitung, ausgearbeitet von KI) als neue Aufgabe für Tutorium 5 (instationär global): Vorab-Frage „Milch sofort oder später, egal?“, Versuch mit zwei Tassen, *kA* aus einer Messung in Tasse 2, Vergleich nach 60 Minuten, abgegebene Wärme als Erklärung, Zusatzfrage zur nichtlinearen Wärmeabgabe. Einordnung offen: Alltagsaufgabe vor der Leitaufgabe, Ersatz der Metallkugel als Zwillingsaufgabe (D47) oder Zusatz.", "G28 bis G30, G12", "TL, KI", "vorgeschlagen", "nicht verwenden oder in eine Übung verschieben"],
  ["D68", "Arbeitswerte: 200 ml Kaffee mit 80 °C (Stoffwerte von Wasser), 30 ml Milch mit 5 °C (*ρ* = 1030 kg/m³, *c*_{p} = 3,94 kJ/(kg·K) wie in Tutorium 8), Raum 20 °C, Messung 67 °C nach 10 Minuten (Zeitkonstante rund 41 Minuten). Ergebnis: Tasse 2 ist um 3,85 K kühler (30,19 gegenüber 34,05 °C).", "G29, G30", "KI", "umgesetzt", "Werte im Rechenmodell ändern, alle Zahlen folgen"],
  ["D69", "Die Wärmekapazität der Tasse wird vernachlässigt (Vorgabe der Tutoriumsleitung). Die Hinweise für die Tutoriumsleitung zeigen, dass ein Becher von 300 g das Ergebnis nicht umkehrt (36,1 gegenüber 39,1 °C).", "G28, G30", "TL", "umgesetzt", "Becher als Zusatzteil"],
  ["D70", "Erstellung aus einer Markdown-Quelle mit Zahlen aus dem Rechenmodell: Word mit Word-Formeln (pandoc), PDF über LaTeX, weil die Umwandlung aus Word die Formeln unsauber setzt; schlichter Kopf „Wärmeübertragung, Entwurf, Stand“ statt FVT-Logokopf. Strukturvorlage in der Projektablage.", "G05, G27", "KI", "umgesetzt", "FVT-Layout wie bei den Begleitdokumenten (fvt_doc.js)"],
  ["D71", "Korrekturen nach der Gegenprüfung: Becher-Fall mit *kA* aus derselben Messung (30,96 gegenüber 34,04 °C); Teil f mit zwei Nachkommastellen; Bilanzraum „für Tasse 1“; Temperaturunterschied in Teil f benannt; typischer Fehler zu Tasse 2 neu formuliert; Fundstellen bei Ferreira (Abb. 6) und Condoret (Tab. 2); Abbildungen korrigiert; Auflösung der Vorab-Frage am Anfang der Lösung; „Zum Weiterdenken“ mit Milch über 47 °C. Kopfzeile „Entwurf“ bleibt bis zur Freigabe.", "G31", "KI", "umgesetzt", "keiner nötig"],

  ["D72", "Becher mit Wärmekapazität als zusätzliche Teilaufgabe der Kaffee-Aufgabe (Teil f), um die Komplexität leicht zu steigern; kA wird mit Becher aus derselben Messung neu bestimmt.", "G32", "TL", "umgesetzt", "Teil streichen"],
  ["D73", "Kernfrage bleibt die Temperatur nach 60 Minuten; die Zeit bis 60 °C passt für Tasse 2 nicht (Milch erst nach 60 Minuten) und übt dasselbe Umstellen wie Teil c.", "G32", "KI", "vorgeschlagen; in der Sammlung umgesetzt", "Zeitfrage als eigener Teil"],
  ["D74", "Milchschaum als Teil g mit Vorhersage vor der Rechnung (60 °C, das Ergebnis kippt); Kipppunkt bei 47 °C und Rausstellen der Milch als Zusatzfrage h. Erklärung über zwei Effekte (Wärmekapazität des Gemischs, Temperatur der spät zugegossenen Milch).", "G32, G34", "TL (Idee), KI", "umgesetzt in der Sammlung; Auswahl offen", "nur Kern a bis e"],
  ["D75", "Versuch im Tutorium zur Kaffee-Aufgabe mit drei Bechern, Vorhersage und Messtabelle; Begründung: Vorhersagen vor einer Demonstration verbessern das Verständnis (Crouch et al., 2004).", "G32, G34", "TL", "umgesetzt in der Sammlung", "Versuch weglassen"],
  ["D76", "Jeder Aufgabenblock beginnt mit einer Ausgangssituation (Text und Skizze), danach folgen die Fragen (zuerst die Vorab-Frage) und die Aufgabe.", "G33", "TL", "umgesetzt in der Sammlung und der Strukturvorlage", "Szenario innerhalb der Aufgabe"],
  ["D77", "Diese Struktur gilt für alle bisher erarbeiteten Aufgaben; daraus entsteht eine große Aufgabensammlung als PDF und Word mit allen Tutorien, auch den Klimaaufgaben.", "G33", "TL", "umgesetzt", "einzelne Blätter je Tutorium"],
  ["D78", "Ablage: Die Tutoriumsleitung legt selbst in Sciebo ab; bis dahin liegen die Dateien auf ihrem Schreibtisch.", "G33", "TL", "entschieden; Zugriff auf den Schreibtisch offen", "Übergabe nur im Chat"],
  ["D79", "Auf den Blättern stehen keine Lernziele, kein Bilanz-Schild, keine Lernziel-Kennzeichen und keine Kästen „Wussten Sie schon?“; die Fakten gehen in die Ausgangssituation ein, Thema und Kernrechnung stehen in der Übersicht der Sammlung. Abweichung von D20 zugunsten der schlanken Lehrstuhlstruktur.", "G33, G27", "KI", "vorgeschlagen; in der Sammlung umgesetzt", "Lernziele über der Aufgabe wie in D20"],
  ["D80", "Die Sammlung enthält Aufgaben mit Ergebnissen, aber keine Lösungswege; die Musterlösungen (Pilot Tutorium 1, Kaffee) bleiben eigene Dokumente, ein Lösungsband folgt nach der Auswahl.", "G33", "KI", "vorgeschlagen", "Lösungen in die Sammlung"],
  ["D81", "Milchtemperatur in der Aufgabe bleibt 5 °C (belegt); 8 °C (wärmerer Kühlschrank) ändert nur die Zahlen, nicht die Aussage, und dient als Vergleich.", "G32, G34", "KI", "umgesetzt", "durchgehend 8 °C"],
  ["D82", "Wostoksee in der Ausgangssituation von Tutorium 1 ohne Temperaturangabe („kälter als 0 °C und trotzdem flüssig“): Der Literaturwert von etwa −3 °C gilt für luftgesättigtes Eis; das Modell der Aufgabe rechnet mit reinem Eis und ergäbe in 3769 m −2,52 °C, Seewasser von −3 °C müsste dort gefrieren.", "G36", "KI", "umgesetzt", "−3 °C nennen und den Unterschied in Teil f besprechen"],
  ["D83", "Korrekturen nach der Gegenprüfung mit geänderten Zahlen oder Aufträgen: Tiefgang des Eisbergs 224 m aus dem Auftrieb (Tutorium 5); *d*_{T} = 0,117 m statt 0,12 m, damit Teil e passt (Tutorium 7); Kaffee h (2) mit einer Abschätzung statt „ohne Rechnung“, Musterlösung korrigiert (Tasse 2 mindestens 1,95 K kühler, nicht 2,48 K); Gegenstrahlung mit Auftrag zur Erklärung und Himmelstemperatur der Autoscheibe als Umgebung erklärt (Tutorium 4); *COP*_{C}, Δ*T*_{ln} und *ε*-NTU als nicht in der Formelsammlung gekennzeichnet; Wärmestrom der AMOC und neue Vorab-Frage im Block „Pol“ (Tutorium 8). Kleinere Korrekturen: KI-Protokoll, Abschnitt 3.6.", "G36", "KI", "umgesetzt", "einzelne Punkte zurücknehmen"],
  ["D84", "Bewusst belassen: Tutorium 2 ohne technischen Zwilling (die Rinne deckt die Platte bei erzwungener und freier Konvektion ab, der Windchill den Zylinder); zwei Abbildungen im ersten Block von Tutorium 1 (Frage 3 braucht die Profile); Überleitungssatz zu Aufgabe 3 in Tutorium 5 als Hinweis für die Auswahl; mehrfach belegte Formelzeichen in Tutorium 5 (jede Aufgabe definiert ihre Zeichen); Linearisierung 4σ*T*_{e}³ als gekennzeichnete Vereinfachung.", "G36", "KI", "vorgeschlagen", "Zwilling (V03, Beispiel 3) ergänzen; Profile streichen"],
  ["D85", "Für den Lösungsband: Abweichungen in der letzten Stelle durch Rundungsketten gelten als richtig; 1 Jahr = 365,25 d nennen; in Tutorium 4 h den Unterschied zwischen 4σ*T*_{e}³ und 4σ*T*_{O}³ (1 − *ε*_{A}/2) in einem Satz nennen; frostfreie Gründungstiefe (Tutorium 7 g) vor der Lösung an DIN 1054 mit DIN EN 1997-1/NA prüfen.", "G36", "KI", "vorgeschlagen", "keiner nötig"],
  ["D86", "Der Rekordflug (Tutorium 8, Zusatzaufgabe 2) ist reine Kinematik und wird als Exkurs gekennzeichnet, damit er bei Zeitmangel zuerst entfällt (vgl. E20).", "G36", "KI", "umgesetzt", "Aufgabe streichen"],
]));

C.push(H2("3.8 Prüfung der Kaffee-Aufgabe, vorbereitet am 23.10.2026"));
C.push(TAB([
  ["D87", "Die Kaffee-Aufgabe liegt zusätzlich als Claude-Dokument vor. Die Tutoriumsleitung schreibt Feedback in [eckigen Klammern] in den Text; die KI arbeitet es ein, rechnet geänderte Zahlen nach und nimmt die Klammer heraus. Einzelblatt (PDF, Word) und Sammlung bleiben textgleich.", "G37", "TL", "umgesetzt", "Feedback im Chat"],
  ["D88", "Unabhängige Prüfung mit sechs Rollen: Professorin, Technik, Didaktik, Recherche, Studierende und Gestaltung, alle mit dem Hauptmodell. Jede Rolle bekommt eine eigene Leseliste, einen eigenen Materialordner und eine Obergrenze für Websuchen (5, 10, 10, 20, 0 und 5). Die Prüfer machen nur Vorschläge.", "G38", "TL", "umgesetzt (29.10.2026, K34, G40)", "fünf Rollen; günstigeres Modell für Recherche und Studierende"],
  ["D89", "Durchführung in einem neuen Chat mit Prüfpaket und einem Startprompt: Der koordinierende Chat startet alle sechs Prüfer, bündelt die Vorschläge und legt sie als Tab „Änderungsvorschläge“ im Claude-Dokument vor. Die Tutoriumsleitung entscheidet je Vorschlag in [ ]; erst danach wird umgesetzt.", "G38", "KI", "umgesetzt (29.10.2026, Cloud-Sitzung statt Chat, K34); entschieden am 30.10.2026 (G41, D93 bis D102), umgesetzt (K35)", "Durchführung in dieser Sitzung"],
]));

C.push(H2("3.9 FVT-Vorlage und Werkzeugkasten vom 23.10.2026"));
C.push(TAB([
  ["D90", "Die offizielle FVT-Aufgabenvorlage („Vorlage Aufgabenstellungen“, Word) ist für die Rolle Gestaltung die zweite Referenz neben den Original-Tutoriumsblättern. Die Rolle empfiehlt, welcher Referenz Blatt und Lösung folgen sollen und welche kleinen Anpassungen dafür reichen; der Aufbau nach der Strukturvorlage bleibt. Über das Aussehen entscheidet die Tutoriumsleitung nach der Prüfung der Kaffee-Aufgabe.", "G39", "TL", "umgesetzt (im Prüfpaket); Aussehen vertagt (D100)", "Rolle G nur mit den Original-Tutoriumsblättern"],
  ["D91", "Werkzeugkasten als Arbeitsgrundlage für alle weiteren Aufgaben: ein ZIP mit Startprompt (Modi, Haltepunkte, Sparregeln), Kontext, Regeln, Ablauf, Erkenntnissen, Index, Werkzeugen, Vorlagen und Lehrstuhlmaterial. Gelesen wird gestuft statt vorab; geprüft wird klein (Technik, Didaktik, Studierende) oder voll (sechs Rollen). Am Ende jeder Runde wird der Werkzeugkasten fortgeschrieben und mit neuer Version gepackt.", "G39", "TL", "umgesetzt", "einzelne Prompts und Pakete je Aufgabe wie bei der Kaffee-Prüfung"],
  ["D92", "Die Quelldateien der Protokolle liegen in der Projektablage an einer Stelle (claude/protokolle_quelle/) statt im Ordner der Kaffee-Prüfung; jede Runde legt geänderte Quellen dort ab.", "G39", "KI", "umgesetzt", "Ordner claude/kaffee_pruefung/protokolle_quelle/"],
]));

C.push(H2("3.10 Umsetzung der Prüfung der Kaffee-Aufgabe vom 30.10.2026"));
C.push(TAB([
  ["D93", "Teil g mit erwärmter, untergerührter Milch (*ϑ*_{M,h} = 60 °C, gleiche Masse und Stoffdaten) statt Milchschaum; Ergebnis ohne Zuordnung („35,99 °C und 37,18 °C (Zuordnung selbst bestimmen)“); Auftrag, das Ergebnis zu erklären, ohne die Umkehr zu verraten (Ä1, Ä2, Ä14; W1 Variante A, W5).", "G40, G41", "TL", "umgesetzt (30.10.2026, K35)", "Cappuccino mit sichtbarer Idealisierung (W1 Variante B)"],
  ["D94", "Kern, Vertiefung und Zusatz: Kern sind Frage 1, a bis e, g und der Versuch; f ist als *Vertiefung* gekennzeichnet, h bleibt Zusatzfrage. Neuer Hinweis „Ablauf im Tutorium“ mit Zeitplan für 90 Minuten (Ä3, W2 nach Did7).", "G40, G41", "TL", "umgesetzt (30.10.2026, K35)", "alle Teile gleichrangig wie im Entwurf"],
  ["D95", "Versuch über 40 statt 60 Minuten mit drei vorgewärmten Bechern; Messung nach 10 Minuten an Becher 2 und 3, *kA* aus dem Mittelwert wie in c, Vorhersage mit den Gleichungen aus d (die TL rechnet bei Bedarf an der Tafel); Messtabelle passend zu den Schritten; Erwartung in den Hinweisen als Bereiche (rund 2 bis 3 K zwischen Becher 1 und 2) mit angekündigter Abweichung vom Modell (Ä4 bis Ä6, W4).", "G40, G41", "TL", "umgesetzt (30.10.2026, K35)", "60 Minuten mit Vorhersage aus f"],
  ["D96", "Annahmen und Bilanz: Wärmeabgabe als Gleichung *Q̇*_{ab} = *kA* (*ϑ* − *ϑ*_{u}) mit konstantem *kA* und *c*_{p} = *c*_{v} in den Annahmen; „gleiches *kA* mit und ohne Milch“ begründen die Studierenden selbst in c (Vorgabe D26); b geht von der allgemeinen Energiebilanz aus, mit Bilanzraum um den Inhalt von Tasse 1; die Mischung in a ist eine Bilanz der inneren Energie (Ä7 bis Ä10, W3 nach Did6 mit Hinweis).", "G40, G41", "TL", "umgesetzt (30.10.2026, K35)", "Annahmen und Lösungsweg wie im Entwurf"],
  ["D97", "Frage 1 als Festlegung mit drei Antworten und einem Satz Begründung; d fragt „Welche Tasse ist wärmer?“ und nach *m c*_{p} je Tasse; e verlangt die Kontrolle über *Q*_{2} − *Q*_{1} und den Denkfehler des Mitbewohners; der Temperaturverlauf ist nur Tafelimpuls, kein Auftrag (Ä11, Ä12, W6).", "G40, G41", "TL", "umgesetzt (30.10.2026, K35)", "Fassung vom 21.10.2026"],
  ["D98", "f als Vertiefung: Bilanzraum um Inhalt und Becher, der Becher mischt beim Zugießen mit, *kA* als Modellparameter neu bestimmt (Ä13); h (2) auf die Raumluft als Wärmequelle eingegrenzt (Ä30); Lösung und Hinweise ergänzt: Verdunstung in beide Richtungen, Robustheit von c und d, Kipppunkt als Modellwert, typische Fehler und zweiter Weg in h (1), Plausibilität von *kA*, umgekehrtes Ziel und technischer Bezug, Probelauf der TL (Ä15 bis Ä17, Ä25 bis Ä27, Ä29).", "G40, G41", "TL", "umgesetzt (30.10.2026, K35)", "Fassung vom 21.10.2026"],
  ["D99", "Gestaltung und Quellen: Abb. L2 überarbeitet; Hierarchie, Abstände und Formelgröße in PDF und Word gleich; Lösung ab der ersten Seite gekennzeichnet; Tabelle mit Gruppenköpfen und Teilverweis; Kleinigkeiten in Form und Notation; Quellen korrigiert (Ä18 bis Ä22, Ä24). Die Vorgaben bleiben: Ergebnis am Ende jedes rechnenden Teils, alle gegebenen Größen in der Tabelle, Titel zentriert (V1 bis V3).", "G40, G41", "TL", "umgesetzt (30.10.2026, K35)", "Gestaltung vom 23.10.2026"],
  ["D100", "Rahmen der FVT-Vorlage (Logos, Fußzeile, Segoe UI) für Blatt und Lösung wird vertagt: eigenes Vorhaben für alle Tutorien, zusammen mit der Lage des Titels (Ä23, V3), nachdem geklärt ist, ob die Vorlage für Tutorien freigegeben ist.", "G40, G41", "TL", "vertagt", "FVT-Rahmen sofort für die Kaffee-Aufgabe"],
  ["D101", "Quellterm und offene Systeme nur als Impuls in „Zum Weiterdenken“ (Tassenwärmer: 13,6 W mit *kA* aus c, 17,8 W mit *kA* aus f); keine eigene Zusatzaufgabe (Ä28).", "G40, G41", "TL", "umgesetzt (30.10.2026, K35)", "eigene Zusatzaufgabe, wenn Tutorium 5 sonst kein offenes System übt"],
  ["D102", "Umfang nach der Strukturvorlage (etwa 175 bis 425 Wörter je Aufgabe): Aufgabe 1 hat nach der Umsetzung 441 Wörter (Formeln als ein Wort, mit Tabelle und Ergebniszeilen; ohne Ergebniszeilen 420), vorher 431. Damit alle angenommenen Ergänzungen Platz haben, sind Material, Ablauf und Messregel des Versuchs in die Hinweise gewandert (Versuch 154 statt 163 Wörter), der Schritt „Vermutung notieren“ entfällt im Versuch (steht in Frage 1), und der Versuch steht auf einer eigenen Seite. Möglich, falls kürzer gewünscht: h als Zusatzaufgabe in die Hinweise (rund 390 Wörter).", "G41", "KI", "umgesetzt (30.10.2026, K35); h auf dem Blatt offen", "Versuchsablauf wieder auf das Blatt"],
]));

C.push(H1("4. Offene Punkte"));
[
  "Auswahl der Leitphänomene für Tutorium 2 bis 8 und die übrigen Entscheidungen E7 bis E17 (Tutoriumsleitung)",
  "Rückmeldung von Viola zum Kurzkonzept und zur Probeaufgabe Tutorium 1",
  "Fachliche Durchsicht durch Mitarbeitende vor dem Einsatz (Arbeitsplan, Phase 5); die Gegenprüfung vom 17.10.2026 ersetzt sie nicht",
  "Fragen an die Professorin: Grundidee, optionale Inhalte, Zusatzwissen, Lösen einfacher Differentialgleichungen, englische Fassung, V08 Teil e, Veröffentlichung von Lösungen, Zeitrahmen (Ideensammlung, Abschnitt 10)",
  "Ablage: Die Tutoriumsleitung legt selbst in Sciebo ab (D78); die Freigabe des Schreibtischordners für die Sitzung steht noch aus",
  "Entscheidung über E18 bis E22 (Aufgabenideen Meeresströmungen und Luftströmungen)",
  "Zitate der Ozean- und Atmosphärenquellen vor dem Druck im Original gegenlesen (Johns 2023, Caesar 2018, Seager 2002, van Westen 2024)",
  "Entscheidung über D67 (Einordnung der Kaffee-Aufgabe in Tutorium 5)",
  "Auswahl und Kürzung je Tutorium aus der Aufgabensammlung (D77); danach Lösungsband (D80, D85)",
  "Entscheidung über D79 (keine Lernziele auf den Blättern, Abweichung von D20) und D84 (bewusst belassene Punkte)",
  "Abnahmeprüfung der umgesetzten Kaffee-Aufgabe durch Codex und Übergabe (K35)",
  "Kaffee-Aufgabe: h auf dem Blatt lassen oder in die Hinweise verlegen (D102); Antworten der TL zu Hauptaufgabe der Sitzung, heißem Wasser im Raum und Semester im Kopf der Endfassung",
  "Aussehen der Blätter (bisherige Tutoriumsblätter oder FVT-Vorlage) als eigenes Vorhaben für alle Tutorien (D90, D100)",
  "Werkzeugkasten nach der Umsetzung der Kaffee-Prüfung auf den neuen Arbeitsstand bringen (D91)",
  "Offene fachliche Punkte der Sammlung: Normwerte für Stahlbeton und PUR-Hartschaum (DIN EN ISO 10456, DIN 4108-4) nicht eingesehen; *λ* = 2,9 W/(m K) der KTB ohne Primärquelle; Arbeitswerte in Tutorium 6 und 7 ohne eigene Quelle; England et al. (2007) nicht abrufbar; VDI 4640 nur über eine Sekundärquelle; Abschätzung zum Entenfuß als eigene Rechnung gekennzeichnet",
].forEach((t) => C.push(Bullet(t)));

C.push(H1("5. Änderungsverlauf"));
C.push(grid(
  ["Version", "Datum", "Änderung"],
  [
    ["1", "17.10.2026", "Protokoll angelegt; Entscheidungen vom 16.10.2026 nachgetragen; Rückmeldung der Tutoriumsleitung und Vorschläge vom 17.10.2026 aufgenommen"],
    ["2", "17.10.2026", "Gegenprüfung eingearbeitet: Grundlagen G19 und G20, Entscheidungen D43 bis D50 (darunter neue Vorschläge E16 und E17), D39 um Variante 34 ergänzt, offene Punkte erweitert"],
    ["3", "17.10.2026", "Pilot Tutorium 1: Grundlagen G21 und G22, Entscheidungen D51 bis D56"],
    ["4", "20.10.2026", "Aufgabenideen Meeresströmungen und Luftströmungen: Grundlagen G23 bis G26, Entscheidungen D57 bis D64 (Vorschläge E18 bis E22), offene Punkte ergänzt"],
    ["4.1", "21.10.2026", "D63: Aufgabenideen auf Wunsch als Word und PDF erstellt"],
    ["5", "21.10.2026", "Lehrstuhl-Struktur und Kaffee-Aufgabe: Grundlagen G27 bis G31, Entscheidungen D65 bis D71, Status von D33 ergänzt, Legende erweitert, offene Punkte ergänzt"],
    ["6", "21.10.2026", "Bausteine der Kaffee-Aufgabe, neue Struktur mit Ausgangssituation und Aufgabensammlung, Gegenprüfung der Sammlung: Grundlagen G32 bis G36, Entscheidungen D72 bis D86, offene Punkte aktualisiert"],
    ["7", "23.10.2026", "Kaffee-Aufgabe als Claude-Dokument und Vorbereitung der unabhängigen Prüfung: Grundlagen G37 und G38, Entscheidungen D87 bis D89 (Abschnitt 3.8), offene Punkte ergänzt"],
    ["8", "23.10.2026", "FVT-Vorlage für die Gestaltungsrolle und Werkzeugkasten für künftige Aufgaben: Grundlage G39, Entscheidungen D90 bis D92 (Abschnitt 3.9), offene Punkte ergänzt"],
    ["9", "29.10.2026", "Unabhängige Prüfung der Kaffee-Aufgabe durchgeführt: Grundlage G40, Status von D88 und D89 auf „umgesetzt“, offene Punkte aktualisiert; Entscheidungen D93 ff. folgen nach der Auswahl der Tutoriumsleitung"],
    ["10", "30.10.2026", "Entscheidung der Tutoriumsleitung über die Änderungsvorschläge und Umsetzung: Grundlage G41, Entscheidungen D93 bis D102 (Abschnitt 3.10), Status von D89 und D90 angepasst, offene Punkte aktualisiert"],
  ],
  [1200, 1500, 6370], { firstColBold: true },
));

write(makeDoc({
  title: "Tutorien Wärmeübertragung: Entscheidungsprotokoll",
  description: "Grundlagen und Entscheidungen der Aufgabenentwicklung. Einträge mit KI-Unterstützung (Claude) vorbereitet.",
  footerText: "Tutorien Wärmeübertragung: Entscheidungsprotokoll",
  children: C,
}), OUT);
