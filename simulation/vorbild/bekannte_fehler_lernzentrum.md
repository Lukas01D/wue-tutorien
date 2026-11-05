# Bekannte Fehler des Lernzentrums, Entscheidungen aus Runde 12 und Gutachtenformat

Stand 05.11.2026 · von Claude (KI) · Vorbild für die Simulationsseite „Kaffee mit Milch“

Quelle: lokaler Klon `/home/user/lernzentrum_v8` (nur gelesen, nichts geändert). Alle Pfade unten sind relativ zu diesem Klon.

**Vollständig gelesen (Leseliste):** `runden/R12/Runde12_Gutachten_Zusammenfuehrung.md`, `runden/OFFEN.md`, `Sprachumschalter_DE_EN_Pruefbericht.md`, `Layout_Scroll_Reparatur_Pruefbericht.md`, `Bedienung_Layout_2D_Pruefbericht.md`, `Instationaer_Lastschutz_Pruefbericht.md` und die Textdateien in `nachweise/simulation_oben/`, `nachweise/bedienung/`, `nachweise/sprachen/` (Liste in Abschnitt 5).

**Zusätzlich nachgesehen (außerhalb der Leseliste, nur für Fundstellen):** `runden/R12/FREIGABE.md`, `runden/R12/Runde12_Feedback_Lukas_2026-11-04.md`, `runden/R12/AUFTRAG.md`, `runden/R12/RUECKMELDUNG.md`, `runden/R12/RUECKMELDUNG_N1.md`, `runden/R12/LIVE_ABNAHME.md`, Kopf und Tabellen der drei Gutachten in `runden/R12/gutachten/`, einzelne Zeilen aus `runden/R11/AUFTRAG.md`, `runden/R11/NACHBESSERUNG_N1.md`, `runden/R11/entwurf/RUECKMELDUNG.md` und Schlüssel in `oberflaeche/sprachen.json`. Wo eine Zeile darauf beruht, steht die Datei in der Fundstelle.

**Kennzeichnung:** „Fehler“ heißt, das Lernzentrum hat ihn selbst als Befund oder Ursache beschrieben. „Risiko“ heißt, das Lernzentrum hat ihn als Anforderung oder Prüffall geführt, ohne einen eingetretenen Fehlerfall zu belegen. „Beobachtung“ heißt, ich habe es aus einer Nachweisdatei abgelesen; es ist dort nicht als Fehler gemeldet. Die Spalte „So vermeiden wir ihn“ ist meine Empfehlung für unsere Seite.

**Breiten:** Das Lernzentrum prüft seit Runde 11 bei **380 und 1366 px** (`runden/R12/AUFTRAG.md`, „Gilt für alle Aufgaben“), die Berichte vom 07.10.2026 mit 360, 400, 768, 1024, 1280, 1366, 1440, 1920 px. Unser Auftrag nennt **390 und 1366 px** (`simulation/AUFTRAG_Simulation_Kaffee.md`). Empfehlung: zusätzlich 360 px prüfen, weil das die schmalste Breite der Lernzentrum-Prüfungen war.

---

## 1. Bekannte Fehler

### 1.1 Sprache und Sprachwechsel

| Nr. | Fehler (kurz) | Ursache | Behoben oder offen | Fundstelle | So vermeiden wir ihn |
|---|---|---|---|---|---|
| F01 | **Risiko:** Sprachwechsel verliert Zustand (Reglerwerte, laufende Animation, offene Lösungen, Notizen, Antworten, Scrollposition) oder startet eine zweite Rechnung | Der Sprachwechsel baut die Oberfläche teilweise neu auf; stabile IDs, Fokus, Pfeiltasten, Formular und offene Reiter müssen dabei erhalten bleiben | abgesichert durch zehn DOM-Ereignisprüfungen (jsdom, Worker als Attrappe), z. B. „Kein zweiter Rechenstart; L=0.063 und k=12.5 bleiben erhalten“; echte Browserprüfung damals offen | `Sprachumschalter_DE_EN_Pruefbericht.md`, Prüftabelle Zeile „Sitzung/Regler/Animation/Quiz/Antworten“; `nachweise/sprachen/UI_Ereignispruefung.json`, Prüfung „Umschalten während einer Rechnung“; `runden/R11/entwurf/RUECKMELDUNG.md`, Abschnitt „Für alle Varianten“ | Sprachwechsel tauscht nur Texte an Ort und Stelle (alle Elemente mit Schlüssel, `textContent`, `aria-label`, `lang`); er baut kein DOM neu, setzt keine Reglerwerte, rechnet nicht, scrollt nicht und verschiebt den Fokus nicht. Zustand liegt in einem Objekt, nicht im DOM. Test: Regler verstellen, Reiter öffnen, Versuch aufklappen, Sprache zweimal wechseln: Werte, Ergebnis, offener Reiter, Fokus und `scrollY` gleich |
| F02 | **Fehler:** Deutsche Wörter in der englischen Fassung | (a) Diagrammtitel waren im Python-Code fest deutsch („Ebene Wand: Temperaturprofil“, „Kein Wärmestrom“, „Bild“); (b) fehlende englische Blöcke fallen absichtlich deutsch zurück; (c) englischer Download „Quellen“ von Thema 1 enthält „Arbeitsfassung“, „Vorlesung“, „Titelseite“, „Einheit“ | (a) behoben 07.10.2026 über Beschriftungstabellen `{de, en}` im Zeichencode; (b) gewollt, mit Hinweis und Kennzeichnung; (c) **offen** (O-27, Download ausgeblendet) | `nachweise/sprachen/Python_Diff.patch`; `Sprachumschalter_DE_EN_Pruefbericht.md`, Abschnitt „Änderungen“ (Rückfall); `runden/OFFEN.md`, O-27 | Ein Wörterbuch mit genau gleichen Schlüsseln für DE und EN, kein Rückfall auf Deutsch. Auch Diagrammtexte, Achsen, Legende, Statusmeldungen, Fehlermeldungen, `aria-label`, `alt`, `title`, Platzhalter und Dateinamen beim Speichern kommen aus dem Wörterbuch. Test: in der englischen Ansicht den gesamten Text und alle Attribute gegen eine Liste deutscher Wörter und Umlaute prüfen (wie die Lernzentrum-Prüfung „Deutscher Resttext · alle Ansichten“) |
| F03 | **Fehler:** Beschriftung der Farbleiste hing vom Sprachwechsel und vom Vorschau-Bau ab | Ursache dort nicht beschrieben; Nachbesserung N5: „Farbleiste verwendet dauerhaft `plot_temperature`, auch nach Sprachwechsel und im Vorschau-Bau“ | behoben in Runde 12 (N5) | `runden/R12/RUECKMELDUNG_N1.md`, Tabelle „Umgesetzt“, N5 | Jede Beschriftung hat einen festen Schlüssel; derselbe Zeichenweg für Vorschau und Ergebnis (siehe F17) |
| F04 | **Fehler:** Englische KI-Vorlage verlangte eine deutsche Antwort (Q-113) | wörtliche Übersetzung („answer in German“) | behoben: Entscheidung Lukas, englische Vorlagen verlangen ausdrücklich Englisch | `Sprachumschalter_DE_EN_Pruefbericht.md`, „Offene Punkte“ 2; `Bedienung_Layout_2D_Pruefbericht.md`, „Ergebnis und Umfang“; `nachweise/bedienung/UI_Lastschutz.json`, letzte Prüfung | Englische Texte nicht wörtlich übersetzen, sondern auf Sinn prüfen; Suche nach „German“ und „Deutsch“ in der englischen Fassung als Test |
| F05 | **Beobachtung:** Sprachwechsel zeichnet Animationen neu; lokal 7,2 s (instationär, 200 Bilder) und 12,0 s (2D, 180 Bilder) | Beschriftungen sind Teil des Rasterbilds aus Matplotlib, deshalb muss jedes Bild neu gezeichnet werden (Rechnung gesperrt, Daten gleich) | so gebaut | `nachweise/sprachen/Python_Sprachvergleich.json`, Feld `drawing` (`redraw_seconds_local`) | Beschriftungen als Text im SVG oder DOM, nicht ins Bild gebrannt; Sprachwechsel kostet dann keine Rechen- oder Zeichenzeit |

### 1.2 Zahlen und Eingaben

| Nr. | Fehler (kurz) | Ursache | Behoben oder offen | Fundstelle | So vermeiden wir ihn |
|---|---|---|---|---|---|
| F06 | **Fehler (high, LA-04):** Auf Englisch standen Werte mit Zehnerpotenz um den Faktor 1000 falsch, z. B. „1 026 × 10⁻⁵“ statt „1.026 × 10⁻⁵“ | `formula()` in `dist/i18n.js` las die englische Mantisse aus `dist/pilot.js` als deutsche Tausenderzahl | behoben in Runde 10b (Test `tools/tests/r10b_numbers.cjs`); live abgenommen; in Runde 12 erneut live geprüft: `0.002`, `0.025`, …, `11.726` richtig | `runden/OFFEN.md`, O-16; `runden/R12/LIVE_ABNAHME.md`, Zeile „Englische Zahlen, Seite“ | Zahlen intern immer als `Number`; Formatierung nur einmal, ganz am Ende, mit `Intl.NumberFormat('de-DE')` bzw. `('en-GB')`; nie einen formatierten Text wieder einlesen. Test mit festen Fällen in beiden Sprachen (Dezimalwerte unter 1, Werte über 1000, Zehnerpotenzen) |
| F07 | **Fehler:** Getippter Wert mit Tausenderpunkt („15.600“) löst eine Fehlermeldung aus | Eingabe akzeptiert Punkt und Komma als Dezimalzeichen; „15.600“ ist deshalb mehrdeutig, Meldung `r7_number_ambiguous` („Bitte gib die Zahl ohne Tausendertrennzeichen ein, zum Beispiel 7800 oder 7,8.“) | übernommen (CLA-083): Wortlaut angepasst, Ausnahme im Leitfaden für Eingabewerte (Werte, die man eintippen soll, ohne Tausenderpunkt) | `runden/R12/Runde12_Gutachten_Zusammenfuehrung.md`, Abschnitt 4.5, CLA-083; `oberflaeche/sprachen.json`, `r7_number_ambiguous` | Eingabefelder: Punkt und Komma als Dezimalzeichen, kein Tausendertrennzeichen; mehrdeutige Eingabe mit verständlicher Meldung in der aktiven Sprache. In Versuchskarten Werte, die man eintippen soll, ohne Tausendertrennzeichen schreiben (bei uns z. B. Zeiten in s) |
| F08 | **Risiko:** ungültige Eingaben (Buchstaben, leer, außerhalb der Grenzen) | | im Lernzentrum abgefangen: „Please enter all parameters within the specified limits.“, Punkt und Komma gültig, Doppelstart gesperrt | `nachweise/bedienung/Sprach_UI_Regression.json`, Prüfung „Eingaben, Fehlermeldungen und Rückfallhinweis“ und Momentaufnahmen „Ungültiger Wert …“ | gleiche Fälle als Test übernehmen: `letters`, leer, knapp unter und über jeder Grenze, Wert zwischen zwei Rasterschritten |
| F09 | **Fehler:** Standardwert außerhalb der Reglergrenze (λ = 15 bei Reglergrenze 10) | Grenze in `simulationsgrenzen.json` war 15, die angezeigte Reglergrenze 10 | als bekannt und dokumentiert erledigt (CLA-076, GPT-056) | `runden/R12/Runde12_Gutachten_Zusammenfuehrung.md`, Abschnitt 3 | Eine einzige Quelle für Grenzen, Schrittweite und Standardwerte; Test: jeder Standardwert und jede Ausgangslage einer Versuchskarte liegt innerhalb der Grenzen und auf dem Raster |
| F10 | **Fehler:** Kennzahl, die nicht definiert ist, erschien als 0 oder unsinniger Wert | Verstärkungsfaktor bei Wärmestrom null bzw. Rechnung mit `max(1e-12, q_no_fin)` | behoben: Anzeige „nicht definiert“ bzw. „nicht angezeigt“ (CLA-046, GPT-057; O-09) | `runden/OFFEN.md`, O-09; Zusammenführung Abschnitt 3 (GPT-057) und 4.2 (CLA-046) | Für Grenzfälle eine eigene Anzeige: z. B. Starttemperatur gleich Umgebung, Zieltemperatur wird nie erreicht, Mischung ohne Temperaturunterschied. Nie `NaN`, `Infinity`, `-0` oder einen Ersatzwert zeigen; Text trennt Anzeige von Definition |

### 1.3 Layout, Scrollen, Fokus

| Nr. | Fehler (kurz) | Ursache | Behoben oder offen | Fundstelle | So vermeiden wir ihn |
|---|---|---|---|---|---|
| F11 | **Fehler:** schwebende Notiz- und Downloadkästen, beschädigte Simulationskomposition, nicht scrollbare Überprüfungsseiten (gemeldet von Lukas nach Site-Version 15) | Nachträgliche Layoutregeln begrenzten die Höhe der Inhaltsgitter; deren Kinder mit `overflow: hidden` schnitten Inhalte ab | behoben 07.10.2026 (Site-Version 16): Stylesheets zurück auf den Stand vor der Änderung, nur der äußere Rahmen fest, ein gemeinsamer Scrollbereich `workspace-scroll`; echte Bildschirmprüfung damals offen (SP-12) | `Layout_Scroll_Reparatur_Pruefbericht.md` | Die Seite scrollt als Ganzes (Dokument), keine verschachtelten Scrollbereiche, keine feste Höhe auf Inhalt, kein `overflow: hidden` auf Inhaltsbehältern. Test im echten Browser: jedes Element der Seite ist per Scrollen erreichbar, bei 390 × 700 und 1366 × 768 |
| F12 | **Fehler:** Nach der Wahl einer Simulation sprang die Seite an den Seitenanfang | nicht beschrieben; Auftrag R11-03 verlangt stattdessen: Auswahl oben im sichtbaren Bereich, sanft, bei `prefers-reduced-motion: reduce` ohne Animation | in Runde 11 beauftragt (R11-03); Simulation-oben-Fassung richtet den Bereich beim Öffnen und Modellwechsel aus | `runden/R11/AUFTRAG.md`, R11-03; `nachweise/simulation_oben/Pruefbericht.md` | Scrollen nur auf ausdrückliche Handlung (Klick auf „Ausgangslage einstellen“, Sprung aus einem Verweis), nie bei Sprachwechsel, Reglerbewegung oder Neuberechnung. `prefers-reduced-motion` beachten. Test: `scrollY` vor und nach Sprachwechsel und nach Rechnung gleich |
| F13 | **Fehler:** Fokussierter Reiter am Handy nicht sichtbar | Reiterleiste bei 380 px waagrecht wischbar; `focus({preventScroll:true})` macht den fokussierten Reiter nicht sichtbar | für die Reiter unter der Simulation gelöst durch drei Reiter, „am Handy alle drei sichtbar, ohne Wischen“ (R12-09); **offen** für die Hauptreiter: „Anwenden & erklären“ abgeschnitten, „Lernziel-Check“ außer Sicht (O-25) | `runden/R11/entwurf/RUECKMELDUNG.md`, Abschnitt „E-03: Neun Erklärreiter“; `runden/R12/AUFTRAG.md`, R12-09; `runden/OFFEN.md`, O-25 | Alle Reiter passen bei 390 px ohne Wischen (Zeilenumbruch in der Beschriftung erlaubt, DE und EN). Kein `preventScroll`. Sichtbarer Fokusrahmen. Hält ein Bild beim Scrollen oben fest (`sticky`), dann `scroll-padding-top` so setzen, dass ein fokussierter Regler nie unter dem Bild liegt. Test: mit Tab durch die ganze Seite, jedes fokussierte Element ganz im sichtbaren Bereich |
| F14 | **Fehler (Kompromiss):** Am Handy passen Bild und alle Regler nicht gleichzeitig | Höhenbudget: bei 400 × 700 und bei 1366 × 480 reicht die Höhe nicht (`synthetic_core_fits: false`); Mindestbildhöhe 160 px; „Gleichzeitige Sichtbarkeit aller Regler und eines lesbaren Bildes ist dort nicht allgemein zugesichert.“ | akzeptiert; Runde 11: am Handy bleibt das Bild im Reglerbereich oben stehen (R11-04); 2D bei 1366 px nur 6 von 9 Reglern sichtbar (Entscheidung Lukas: großes Bild) | `nachweise/simulation_oben/Pruefbericht.md` und `CSS_DOM_Hoehenbudget.json`; `runden/R11/AUFTRAG.md`, R11-04; `runden/R11/LIVE_ABNAHME.md`, Zeile „Simulationsseite“ | Wenige Regler, kompakt; Höhenbudget im echten Browser messen, nicht mit ausgedachten Maßen (die Werte im Nachweis sind ausdrücklich „synthetic“). Ziel festlegen und testen: bei 390 px sind Diagramm und der gerade bediente Regler zugleich sichtbar |
| F15 | **Fehler (offen, O-13):** Abgesetzte Formeln ragen am Handy über die Spalte (z. B. COND-H19 331 statt 298 px) und lassen sich nur waagrecht verschieben | lange Formeln in einer Zeile | **offen** | `runden/OFFEN.md`, O-13 | Lange Formeln mehrzeilig setzen; Test: keine Formel breiter als ihre Spalte bei 360 und 390 px |
| F16 | **Fehler (offen, O-24, R12-N1, low):** Tabellenkopf „Simulation“ bricht bei 380 px in schmalen Spalten in drei Stücke | zu viele Spalten für die Breite | **offen** | `runden/OFFEN.md`, O-24 | Tabellen am Handy höchstens zwei bis drei Spalten oder als Liste; kurze Köpfe; kein Wort getrennt (Abnahme A6 in `runden/R12/AUFTRAG.md`: keine waagrechte Scrollleiste der Seite bei 380 px, kein Wort im Kasten „Rechenwerte“ getrennt) |

### 1.4 Diagramm und Formelsatz

| Nr. | Fehler (kurz) | Ursache | Behoben oder offen | Fundstelle | So vermeiden wir ihn |
|---|---|---|---|---|---|
| F17 | **Fehler (R11-C01, medium):** Vorschaubilder vor der ersten Rechnung hatten andere Achsenbeschriftungen („x (m)“) als nach der Rechnung („x [m]“) | Vorschaubilder fertig gezeichnet und nicht mit dem Zeichencode erneuert (Matplotlib fehlte) | behoben in Runde 12 (neu gebaut mit `tools/build_runde6_previews.py`) | `runden/OFFEN.md`, O-21 | Kein vorgezeichnetes Bild: Die Seite zeichnet das Diagramm beim Laden mit denselben Funktionen und Standardwerten wie nach jeder Änderung |
| F18 | **Fehler (E5):** Achsen- und Kastenbeschriftung im Diagramm unscharf | Rasterbild wird größer skaliert angezeigt | Runde 12: Bildbreite mindestens doppelte Anzeigebreite (R12-10), Legende siehe F19 | `runden/R12/Runde12_Feedback_Lukas_2026-11-04.md`, E5; `runden/R12/AUFTRAG.md`, R12-10 | Diagramm als SVG (Text bleibt scharf in jeder Größe) oder Canvas mit `devicePixelRatio` |
| F19 | **Fehler (E6):** Legende („Infokasten“) liegt teils vor der Linie | Legende in der Zeichenfläche; Lage hängt von den Werten ab | Runde 12: Legende kleiner und nie auf einer Linie, robuster Weg gewünscht (z. B. feste Lage außerhalb der Achsen), Test mit Standard- und Grenzwerten (R12-11) | Feedback E6; `runden/R12/AUFTRAG.md`, R12-11 | Legende außerhalb der Achsen oder direkte Beschriftung am Linienende; Test bei allen Reglergrenzen (heißeste und kälteste Tasse, kürzeste und längste Zeit) |
| F20 | **Fehler (O-07, O-11, LA-01):** feste y-Achse; roter Punkt bei Werten knapp unter null halb am Rand sichtbar, während der Text „fehlt der Punkt“ sagt | Achsenbereich fest, Text beschrieb ein Verhalten, das die Zeichnung nicht hatte | behoben in Runde 10: feste Stufen mit Bereich unter null und betonter Nulllinie; Sätze geändert | `runden/OFFEN.md`, O-07, O-11 | Achsenbereich in festen Stufen aus den Werten; jede Textaussage über das Diagramm („liegt oben“, „fehlt“) als Test an den Grenzwerten nachprüfen |
| F21 | **Fehler (N1-01, high):** Der Punkt über $Q$ und $q$ war ganz verschwunden | CSS-Regel `math .math-dot > mo {transform:translateY(.1em) scale(1.35)}` schob den Punkt in den Buchstaben | behoben in Runde 12 (N1: Punkt als echte MathML-Fläche `mspace`, 0,16 em breit); live sichtbar | `runden/R11/NACHBESSERUNG_N1.md`, N1-01; `runden/R12/RUECKMELDUNG_N1.md`, N1; `runden/R12/LIVE_ABNAHME.md`, „Skizzen D1, D5“ | Formelzeichen mit Punkt nicht per CSS verschieben. Wenn nötig $\dot Q$ als MathML `<mover>` oder Zeichen mit U+0307 und im Browser ansehen (Chrome, Safari, Firefox) |
| F22 | **Fehler (C5):** Einheiten als Bruch drücken Zeilen auseinander | Bruch im Satz höher als eine Zeile | Runde 12 nach K3: Bruch im Satz höchstens eine Zeile hoch, Zähler und Nenner mindestens 0,65 em; Abnahme: Grundlinienabstand mit und ohne Bruch gleich (höchstens 0,5 px), 380 und 1366 px, DE und EN | Feedback C2, C5; Zusammenführung Abschnitt 1, K3; `runden/R12/AUFTRAG.md`, R12-03 und A3 | Im Fließtext Einheiten nach K3 klein gesetzt oder mit Schrägstrich; Test misst Zeilenabstand mit und ohne Einheit |

### 1.5 Bedienung und Aufbau der Seite

| Nr. | Fehler (kurz) | Ursache | Behoben oder offen | Fundstelle | So vermeiden wir ihn |
|---|---|---|---|---|---|
| F23 | **Fehler (E1, E7):** zu viele Knöpfe und neun Reiter unter der Simulation; Doppelungen („Probier aus“ und „Versuche“, Annahmen zweimal); Namen sagen nicht, was dort steht; beim Öffnen eine Tabelle statt des ersten Versuchs | Reiter wuchsen über Runden; Inhalte teils für das ganze Thema, teils für eine Simulation | behoben in Runde 12 nach K5: drei Reiter (siehe Abschnitt 2); live geprüft: „unter jeder Simulation 3 Reiter, DE und EN“ | Feedback E1, E7; `runden/R12/gutachten/CLA_Gutachten_Claude_2026-11-04.md`, D.1; Zusammenführung Abschnitt 6; `runden/R12/LIVE_ABNAHME.md`, Zeile „Reiter“ | Von Anfang an die drei Reiter nach K5, nur Inhalte dieser Simulation, „Versuche“ offen, erste Karte aufgeklappt |
| F24 | **Fehler (CLA-118):** Knopf nannte das Werkzeug statt der Handlung („Python starten & berechnen“) | technische Sicht | behoben: „Berechnen“ / „Calculate“, sekundär „Standardwerte“ / „Default values“ | Zusammenführung 4.7 (CLA-118) und Abschnitt 6; `oberflaeche/sprachen.json`, `pilot_start`, `pilot_0200` | gleiche Wörter verwenden; keine Technik im Knopf |
| F25 | **Fehler (CLA-080):** Regler ohne Wirkung (Fläche $A$ in der instationären Simulation, das Modell nutzt $A$ nicht) | Regler aus einer anderen Simulation übernommen | behoben: Regler ausgeblendet, Modell unverändert (K5, R12-12) | Zusammenführung 4.5 (CLA-080); `runden/R12/FREIGABE.md`, Zeile „K5 Regler $A$“ | Test: jeder Regler verändert mindestens eine Anzeige; sonst gehört er nicht auf die Seite |
| F26 | **Risiko:** Ergebnis gehört zu einem früheren Parametersatz (Rechnen mit veraltetem Stand) | Rechnung nur auf Knopfdruck (Python im Browser); Regler und Anzeige können auseinanderlaufen | im Lernzentrum mit Statusmeldungen abgefangen: „Eingaben geändert. Das Diagramm zeigt die letzte Rechnung. Erneut berechnen.“ (`pilot_0203`), „Das Ergebnis gehört noch zu den letzten gültigen Eingaben.“ (`r7_result_stale`); GPT-Gutachten: diese Warnung ist „fachlich wichtig und sollte erhalten bleiben“; Doppelstart gesperrt | `runden/R12/gutachten/GPT_Gutachten_GPT-6_2026-11-04.md`, D, Absatz „Rechenwerte“; `oberflaeche/sprachen.json`; `nachweise/bedienung/Sprach_UI_Regression.json`, Prüfung „Eingaben, Fehlermeldungen …“ | Unsere Rechnung ist eine geschlossene Formel und schnell: bei jeder Reglerbewegung sofort neu rechnen, dann gibt es keinen veralteten Stand. Behält die TL einen Knopf „Berechnen“ (wie im Lernzentrum), dann bei jeder Änderung sofort die Meldung „Eingaben geändert …“ zeigen und das Diagramm als alt kennzeichnen. Ergebnis immer aus dem aktuellen Zustandsobjekt; ungültige Eingabe zeigt nie ein Ergebnis zu anderen Werten ohne Hinweis |
| F27 | **Fehler (L16, E8):** Versuchskarten mit sieben Werten im Fließtext schwer lesbar | Parameterlisten als Satz | behoben in Runde 12: Muster CLA L16 (Ausgangslage als Verweis auf Standardwerte und Knopf „Ausgangslage einstellen“, Änderung als Pfeil „λ: 200 → 15 W/(m·K)“, Auflösung als Vorher-nachher-Tabelle; bei abweichender Ausgangslage nur die Abweichungen) | Zusammenführung Abschnitt 2, L16; Feedback E8 | gleiches Muster für unsere Versuchskarten; „Ausgangslage einstellen“ setzt nur Werte, rechnet bzw. deckt keine Lösung auf (Anforderung zu `setStartingSituation` in `runden/R11/entwurf/RUECKMELDUNG.md`) |
| F28 | **Fehler:** Code-Namen und alte Namen auf der Oberfläche ($h$, $T_s$, $T_b$ im Platzhaltermodus; Code-Namen im Lerntext) | Schlüssel und Texte aus dem Python-Code übernommen | behoben in Runde 12 (CLA-108, CLA-030) | Zusammenführung 4.1 (CLA-030), 4.7 (CLA-108) | Formelzeichen der Vorlesung auf der Oberfläche; Code-Namen nur im Reiter „Modell“ (Tabelle „Regler und Einheiten“) und in „So rechnet der Code“ |
| F29 | **Fehler (R12-19-B1, high, und Gegenprüfung Nr. 17):** Löschliste „ungenutzter“ Textschlüssel war falsch; `model_*` und `panda_plot_*` werden dynamisch zusammengesetzt (`'model_'+part+'_'+model`) | Schlüsselnamen zur Laufzeit gebaut, daher per Suche nicht auffindbar | erkannt vor dem Löschen; Familien erhalten | Zusammenführung 4.7 und Abschnitt 9, Nr. 17; `runden/R12/RUECKMELDUNG.md`, „Befunde“ | Nur vollständige Schlüssel im Code, nie zusammengesetzt; Test: jeder Schlüssel hat DE und EN, jeder verwendete Schlüssel existiert, jeder vorhandene wird verwendet |
| F30 | **Beobachtung:** Gedankenstriche in Oberflächentexten | Texte mit Gedankenstrich (U+2013), z. B. „Wärmeleitung“ mit Gedankenstrich (CLA-063); im Nachweis vom 07.10.2026 tragen die Regler-Beschriftungen für Bildschirmleser ein U+2013 vor „Slider“ und „Value“ | Gedankenstriche in Texten in Runde 12 entfernt (CLA-063, CLA-086, CLA-120); ob die Regler-Beschriftungen heute noch U+2013 tragen, nicht geprüft | Zusammenführung 4.5 und 4.7; `nachweise/bedienung/Sprach_UI_Regression.json`, `snapshots[0].attrs` | Test: kein U+2013 oder U+2014 in Wörterbuch, `aria-label`, `title`, `alt` |
| F31 | **Risiko:** Abhängigkeit von nachgeladener Rechenlaufzeit (Python im Browser) | Pyodide wird nachgeladen; ohne Netz Meldung „Python could not be loaded. Check your internet connection and start again.“; Rechenzeit live 2D 21,8 bis 23,4 s; dazu Lastschutz für zu große Rechnungen | so gebaut, mit Lastschutz und verständlichen Fehlern | `nachweise/bedienung/Sprach_UI_Regression.json`, Momentaufnahme „Fehler beim Laden der Laufzeit · EN“; `runden/R12/LIVE_ABNAHME.md`, „Rechenzeit live“; `Bedienung_Layout_2D_Pruefbericht.md`; `Instationaer_Lastschutz_Pruefbericht.md` | Eine HTML-Datei ohne Nachladen (keine Schriften, Skripte oder Bilder von fremden Servern); Rechnung in JavaScript. Test: Seite aus `file://` ohne Netz öffnen, alles funktioniert |
| F32 | **Fehler:** Rechnung mit zu feinem Gitter oder dünner Wand brach mit Python-Fehler ab | explizites Verfahren: $\Delta t = 0{,}49\,\Delta x^2/a$; Grenze 250000 Zeitebenen bzw. 150 Millionen Gitterpunkt-Schritte; Vorabprüfung zuerst nur für 2D | behoben 07.10.2026: Vorabprüfung für 1D und 2D, ausdrücklich übernehmbare Vorschläge, kein stiller Eingriff, kein Start durch Übernahme | `Instationaer_Lastschutz_Pruefbericht.md`, „Ursache und Änderung“; `Bedienung_Layout_2D_Pruefbericht.md`, „Ursache des gemeldeten 2D-Fehlers“ | Newtonsches Abkühlen analytisch rechnen, $T(t) = T_\infty + (T_0 - T_\infty)\,e^{-t/\tau}$; kein Zeitschrittverfahren, also keine Lastgrenze. Falls doch numerisch: Endzeit genau treffen (siehe F33) |
| F33 | **Beobachtung:** Die Rechnung endet nicht genau zur gewünschten Zeit (650 s gewünscht, 650,12 s gerechnet; 3600 s gewünscht, 3608,07 s gerechnet) | Solver rundet die Zahl der Zeitschritte nach oben | so gelassen, im Bericht offen genannt | `Sprachumschalter_DE_EN_Pruefbericht.md`, „EX-Vergleich“; `Bedienung_Layout_2D_Pruefbericht.md`, „Nachweise“ | Angezeigte Zeit ist genau die eingestellte Zeit (analytische Lösung) |
| F34 | **Risiko:** Prüfungen ohne echten Browser | Alle Berichte vom 07.10.2026: jsdom „berechnet keine Geometrie und prüft kein Scrollrad, sichtbare Kastengröße oder Pyodide“; Höhenbudget mit „ausdrücklich synthetischen Abmessungen“; verwaltete Vorschau startete nicht (`bwrap: Can't mount proc …`) | später durch Live-Abnahmen mit Playwright ersetzt (Runde 11, 12) | `Layout_Scroll_Reparatur_Pruefbericht.md`, Zeile „Tatsächlicher Browser“; `nachweise/sprachen/Browser_Status.json`; `nachweise/simulation_oben/CSS_DOM_Hoehenbudget.json`; `runden/R12/LIVE_ABNAHME.md` | Abnahme im echten Browser (Playwright, Chromium, wenn möglich auch WebKit): Bildschirmfotos und Messungen bei 390 und 1366 px, DE und EN, 0 Fehler in der Konsole; synthetische Maße nie als Beleg werten |

---

## 2. Entscheidungen der TL aus Runde 12

Entscheidungen von Lukas vom 04.11.2026 (K1 bis K10) und 05.11.2026 (V8-01, V8-02). Wortlaut aus `runden/R12/FREIGABE.md` (Spalte „Entscheidung Lukas (Wortlaut)“), Folge aus `runden/R12/Runde12_Gutachten_Zusammenfuehrung.md`, Abschnitt 1, Tabelle „Entscheidungen von Lukas (04.11.2026)“. Wo die TL anders entschieden hat als empfohlen, steht die Empfehlung dabei.

### 2.1 K1 bis K5 (Formelsatz und Simulationsseite)

| Nr. | Frage | Entscheidung (Wortlaut) | Folge laut Zusammenführung | Empfehlung vorher | Fundstelle |
|---|---|---|---|---|---|
| K1 | Formelzeichen fett (Punkt C3)? | „Vorläufig fett“: Formelzeichen und Einheiten in Formeln fett, über einen zentralen Schalter | „Formelzeichen und Einheiten in Formeln fett, über **einen zentralen Schalter** (eine Stelle in CSS oder `math.js`), damit es sich mit einer Änderung zurücknehmen lässt. Leitfaden: Regel ‚Keine Formeln in Fettdruck‘ ersetzen durch ‚Formeln fett (vorläufig, Entscheidung Lukas 04.11.2026)‘. Fettes Wort plus fettes Zeichen ist dann doppelt: In den Kernaussagen bleibt der Satz fett, das Zeichen steht in der Erläuterung“ | Claude: **Nein** (alle drei Gutachten: fett heißt Vektor, ISO 80000-2); stattdessen das Wort fett | `runden/R12/FREIGABE.md`; Zusammenführung Abschnitt 1 |
| K2 | Einheit in eckigen Klammern nach dem Formelzeichen im Fließtext (C4)? | „Im Satz ‚in‘, eckige Klammern nur an Reglern, Achsen und Tabellenköpfen“ | „wie Leitfaden heute; alle Stellen ‚Formelzeichen [Einheit]‘ im Fließtext auf ‚in‘ umstellen“; Beispiel: „$\alpha$ in $\mathrm{W}/(\mathrm{m}^2\cdot\mathrm{K})$“ | wie entschieden | wie oben |
| K3 | Einheiten im Fließtext wieder als Bruch (C2)? | „Bruch im Fließtext, klein gesetzt, so dass die Zeile nicht auseinandergeht“; kehrt F6 aus Runde 11 um | „Codex setzt Einheitenbrüche im Satz kleiner (Höhe höchstens eine Zeile); Abnahme: Zeilenabstand mit und ohne Bruch gleich, bei 380 und 1366 px, DE und EN. Kehrt F6 aus Runde 11 um; Leitfaden anpassen“ | Claude: ja, aber nur, wenn die Zeile nicht auseinandergeht; sonst Schrägstrich | wie oben; Umsetzung `runden/R12/AUFTRAG.md`, R12-03, A3 |
| K4 | Zeichen der charakteristischen Länge (D3): $l$, $L$ oder $L_\mathrm{c}$? | „$L_\mathrm{c}$“ | „**$L_\mathrm{c}$**, weil die Vorlesung $L_\mathrm{c}$ für nichts anderes verwendet (geprüft: Folien 01 bis 08 und Python-Codes, kein $L_\mathrm{c}$, CONFIRMED)“; CLA-015 und Merke-Kasten L4 mit $L_\mathrm{c}$ | Claude: $l$ behalten (bei Incropera ist $L_\mathrm{c}$ die korrigierte Rippenlänge, Gl. 3.93, S. 166) | wie oben; Wortlaut Merke-Kasten in Abschnitt 2, L4 |
| K5 | Reiter unter der Simulation | „3 Reiter“: Versuche (offen), Modell, So rechnet der Code; Knopf „Berechnen“ | „**3 Reiter** (Zuordnung der bisherigen neun Reiter siehe Abschnitt 6)“ | Claude: 3 Reiter (CLA 4, GPT 3, GEM 3) | wie oben |
| K5 (Zusatz) | Regler $A$ der instationären Simulation | „Regler $A$ der instationären Simulation ausblenden (nur Darstellung, Modell unverändert; als Freigabe in `FREIGABE.md` eintragen)“ | Regler ausblenden, Satz entfällt; Modell unverändert (CLA-080) | wie entschieden | `runden/R12/FREIGABE.md`; Zusammenführung 4.5 |

**K5 im Einzelnen** (Zusammenführung Abschnitt 6, Umsetzung `runden/R12/AUFTRAG.md` R12-04 bis R12-09; Wortlaute aus `oberflaeche/sprachen.json`):

| Nr. | Reiter DE / EN | Inhalt | Standard |
|---|---|---|---|
| 1 | **Versuche** / Experiments (`reference_experiments`) | Satz „Erst vermuten, dann rechnen.“ / „First predict, then calculate.“ (`r12_try_first`); die Versuchskarten **dieser** Simulation im Muster L16, je mit „Ausgangslage einstellen“ / „Set up the starting situation“; am Ende „Alle Versuche zurücksetzen“ / „Reset all experiments“ | **offen**, erste Karte aufgeklappt |
| 2 | **Modell** / Model (`r12_reference_model`) | zugeklappte Abschnitte untereinander, in dieser Reihenfolge: „Physikalisches Problem“ / „Physical problem“ (mit Skizze); „Annahmen“ / „Assumptions“; „Was die Simulation macht“ / „What the simulation does“; „Regler und Einheiten“ / „Sliders and units“ (Bereich, Standardwert, Einheit, Name im Code); „So liest du die Ergebnisse“ / „How to read the results“. Doppelte Texte nur einmal | zu |
| 3 | **So rechnet der Code** / How the code calculates (`reference_code`) | wie bisher, mit „Für alle, die es genauer wissen wollen. Für den Wissenstest brauchst du das nicht.“ / „For anyone who wants to know more. You do not need this for the knowledge check.“ (`topic_0236`) | zu |

Dazu (Zusammenführung Abschnitt 6, „Dazu“):
- **Lesehinweis direkt unter dem Diagramm**, eine Zeile (`@teil lesehinweis`, genau ein Satz), in der Vorschau und nach der Rechnung, DE und EN (R12-06).
- **Hilfen an den Reglern** bleiben; deshalb kein eigener Reiter „Parameter“.
- **Knöpfe:** primär „Berechnen“ / „Calculate“ (`pilot_start`), sekundär „Standardwerte“ / „Default values“; „Vorigen Lauf zum Vergleich anzeigen“, Farbskala und ähnliche Einstellungen unter „Für Fortgeschrittene“ / „Advanced controls“ (`r6_advanced`), zugeklappt.
- **Reiter als Reiter erkennbar** (E7): mindestens 44 px hoch, gewählter Reiter mit der Fläche darunter verbunden, mindestens 8 px Abstand, am Handy alle drei ohne Wischen sichtbar (R12-09).
- **Knopf „Berechnen“** bündig mit der Oberkante des Simulationsfensters, höchstens 1 px Abweichung (E4, R12-08, A7).
- **Sprungziele:** Verweise öffnen den passenden Reiter, klappen den Abschnitt auf und rollen dorthin (R12-05, A5).

Begründung in der Zusammenführung: drei Tätigkeiten statt neun Auswahlpunkte (Sweller et al. 2019), Doppelungen entfallen (Mayer, Kohärenz), Namen sagen, was man dort tut (Signalisierung), Versuch vorn und offen (Tulodziecki, Herzig & Grafe 2021, Kap. 3.3.3, laut Inhaltsverzeichnis).

### 2.2 K6 bis K10

| Nr. | Entscheidung (Wortlaut bzw. Kurzfassung) | Folge laut Zusammenführung | Fundstelle |
|---|---|---|---|
| K6 | „Vertiefung bleibt“, mit Hinweis „für den Wissenstest“ (Empfehlung war: in die Grundlagen) | Titel „Vertiefung: Verstärkungsfaktor und Rippenwirkungsgrad“; erster Satz DE „Dieser Abschnitt geht über die Vorlesung hinaus. Für den Wissenstest brauchst du ihn.“ EN „This section goes beyond the lecture. You need it for the knowledge check.“ | `runden/R12/FREIGABE.md`; Zusammenführung Abschnitt 1 |
| K7 | „Knopf vor der Musterantwort, mit Checkliste“ | Knopf „Rückmeldung von einer KI holen“ erscheint, sobald eine eigene Antwort eingegeben ist; Checkliste bleibt im kopierten Text (Abschnitt 5) | wie oben; `runden/R12/AUFTRAG.md`, R12-15 |
| K8 | je Thema genau eine neue Bankversion | Abschnitte 4.3 und 4.5 | wie oben |
| K9 | Rippen als Ergänzung zur Vorlesung kennzeichnen | Satz nach CLA-022 am Anfang von CONV-H10 | wie oben |
| K10 | „Lerntext Thema 1: alles jetzt, auch Lernziele, Vorab-Fragen und Sprache“ (Empfehlung war: nur fachliche Präzisierungen) | alle Befunde in 4.5 in Runde 12 | wie oben |

### 2.3 Weitere Entscheidungen mit Kennung

| Kennung | Entscheidung (Wortlaut) | Datum | Fundstelle |
|---|---|---|---|
| V8-01 `/links` | „Ja, bitte den kleinen Pull Request mit LINKS.json, /links und Teil B auf den neuen Commit.“ | 05.11.2026 | `runden/R12/FREIGABE.md` |
| V8-02 frühere Fassungen | „v0 bis v7 waren nicht absichtlich gesperrt.“ „Nimm v0 bis v7 in /links wie bisher als erreichbar auf.“ | 05.11.2026 | `runden/R12/FREIGABE.md` |
| O-30 | Lerntext Thema 2 kürzen: etwa 10 Minuten Lesezeit, Richtwert 3 bis 7 (Entscheidung Lukas 04.11.2026) | 04.11.2026 | `runden/OFFEN.md` |
| O-31 | Hinweis „Entwurfsfassung · Die Inhalte werden noch fachlich geprüft.“ bleibt auch in v8 (Entscheidung Lukas 04.11.2026) | 04.11.2026 | `runden/OFFEN.md` |

Ohne Kennung, ebenfalls in `runden/R12/FREIGABE.md` (alle 04.11.2026): Ziel der Runde („Alle Punkte unten umsetzen, als Werkstatt veröffentlichen und abnehmen, danach v8 als feste Kopie und auf der Hauptadresse.“), Hauptadresse wieder öffentlich schalten, „Nichts mergen oder veröffentlichen ohne mich.“, Hinweis „Entwurfsfassung“ „nicht entfernen“, Hinweis „final technical review pending“ „entfernen“, Datum der Kennzeichnung v8 „05.11.2026“, Handouts „für v8 so lassen“, Lerntext Thema 2 „für v8 so lassen, in der nächsten Runde kürzen“, Freigabe feste Kopie v8 und Hauptadresse.

### 2.4 Vorgaben der TL aus dem Feedback zu Runde 12 (mit Kennung, für Formelsatz und Simulationsseite)

Das sind Rückmeldungen von Lukas, keine Entscheidungen zwischen Varianten; wo eine K-Entscheidung dazu gehört, gilt sie. Quelle: `runden/R12/Runde12_Feedback_Lukas_2026-11-04.md`.

| Kennung | Vorgabe (eng zusammengefasst bzw. Wortlaut) |
|---|---|
| C1 | Punkt über Q und q „knapp darüber wie in der üblichen Schreibweise, dicker und prägnanter“ |
| C2 | Einheiten im Fließtext wieder als Brüche (K3) |
| C3 | Formelzeichen und Einheiten fett (K1) |
| C4 | Einheit nach Formeln in eckigen Klammern (entschieden anders: K2) |
| C5 | „Einheiten dürfen Zeilen nicht auseinanderdrücken oder den Text zerschießen.“ |
| E1 | „Unten viel zu viele Knöpfe, überfordernd: deutlich vereinfachen, nach didaktischen Gestaltungsregeln.“ (K5) |
| E2 | Quellenverzeichnis unten rechts vorerst aus dem Lernzentrum nehmen |
| E3 | Lob: Struktur ohne die Knöpfe „Lernen“ und „Lernüberprüfung“ ist besser |
| E4 | „Berechnen“ etwas tiefer, bündig mit der Oberkante des Simulationsfensters |
| E5 | Regleranordnung deutlich besser; Achsen- und Kastenbeschriftung unscharf: schärfen |
| E6 | Legende kleiner und ohne Kollision mit der Linie, ohne fehleranfälliges Ausweichen |
| E7 | Reiter unter der Simulation deutlicher als Reiter kennzeichnen, mehr Platz (mit E1) |
| E8 | Versuchskarten mit Parameterliste schlecht lesbar; überall solche Listen besser darstellen (L16) |

---

## 3. Offene Punkte aus `runden/OFFEN.md`, relevant für eine Simulationsseite

Stand der Datei: 04.11.2026 (O-34 mit Nachtrag 05.11.2026).

| ID | Punkt (kurz) | Stand laut OFFEN.md | Bedeutung für unsere Seite |
|---|---|---|---|
| O-13 | Abgesetzte Formeln ragen bei 380 px über die Spalte, nur waagrecht verschiebbar | offen | Formeln mehrzeilig; Test bei 360 und 390 px (F15) |
| O-24 | Tabellenkopf bricht bei 380 px in drei Stücke (Modell-Reiter) | offen | kurze Köpfe, wenige Spalten am Handy (F16) |
| O-25 | Hauptreiter am Handy wischbar, „Anwenden & erklären“ abgeschnitten, „Lernziel-Check“ außer Sicht | offen | alle Reiter ohne Wischen sichtbar (F13) |
| O-27 | Englischer Download „Quellen“ Thema 1 mit deutschen Wörtern, doppeltem Eintrag und internen Dateinamen | offen (Download ausgeblendet) | Sprachprüfung auch für alles, was man herunterladen oder kopieren kann (F02) |
| O-28, O-29 | Seitenumbrüche und Kleinigkeiten in PDF und Word (z. B. fehlende Tiefstellung „TW“) | offen | nur relevant, falls wir einen Download oder eine Druckansicht anbieten; dann Druckansicht prüfen |
| O-26 | Word-Prüfung braucht LibreOffice; Matplotlib-Test braucht eigenen Python-Ordner, rund zehn Minuten | Hinweis | Prüfwerkzeuge vorher bereitstellen; unsere Tests sollen ohne Python-Zeichenbibliothek laufen |
| O-30 | Lerntext Thema 2 kürzen (Richtwert 3 bis 7 Minuten Lesezeit) | offen | Richtwert für Texte auf unserer Seite (Modell-Reiter knapp halten) |
| O-31 | Hinweis „Entwurfsfassung · Die Inhalte werden noch fachlich geprüft.“ bleibt in v8 | offen | Frage an die TL, ob unsere Seite denselben Hinweis trägt |
| O-20 | Inhaltsprüfung verlangt genau vier `@selbstcheck`-Zeilen je Thema | offen | nicht relevant |
| O-32, O-33, O-34 | Kennzeichnung der Werkstatt, `/links`, frühere Fassungen | offen bzw. erledigt | nicht relevant |

**Erledigt, aber als Lehre wichtig:** O-07 und O-11 (Achse, Punkt am Rand, F20), O-09 („nicht definiert“ statt 0, F10), O-16 (englische Zahlen um Faktor 1000 falsch, F06), O-21 (Vorschaubilder mit anderen Achsen, F17).

---

## 4. Gutachtenrollen von Runde 12 (Vorbild für unsere Rollenprüfungen)

### 4.1 Rollen

| Kürzel | Gutachter | Umfang | Befund-IDs | Fundstelle |
|---|---|---|---|---|
| **CLA** | Claude Opus 5.5 | 120 Befunde, L1 bis L16 mit Wortlaut DE und EN, KI-Vorlagen, 4 Reiter vorgeschlagen; alle Zahlen nachgerechnet, kein Fehler | CLA-001 bis CLA-120 | `runden/R12/gutachten/CLA_Gutachten_Claude_2026-11-04.md`; Zusammenführung Abschnitt 0 |
| **GPT** | in der Zusammenführung „GPT-6.1“, im Kopf des Gutachtens „Gutachten GPT-6 (Codex)“ | 63 Befunde, L1 bis L16, KI-Vorlagen, 3 Reiter; alle Zahlen nachgerechnet, kein Fehler; Incropera mit Seitenzahlen | GPT-001 bis GPT-063 | `runden/R12/gutachten/GPT_Gutachten_GPT-6_2026-11-04.md` |
| **GEM** | Gemini („unabhängige Gutachterin für Fachwissenschaft, Didaktik und wissenschaftliches Lektorat“) | 4 Befunde, kurze Antworten, eine gemeinsame KI-Vorlage; keine Nachrechnung | GEM-01 bis GEM-04 | `runden/R12/gutachten/GEM_Gutachten_Gemini_2026-11-04.md` |

Alle drei hatten **denselben Auftrag** (Prüfpaket `Gutachten_Paket_Lernzentrum_2026-11-04.zip`, Prompt `00_PROMPT.md`, Einzelfragen in `01_Kontext_und_Vorgaben.md` laut Feedback-Datei). Es gab also keine Aufteilung in Fach-, Didaktik- und Sprachrollen; jede Rolle prüfte alles. Prompt und Paket: **im Klon nicht gefunden**.

### 4.2 Aufbau jedes Gutachtens

Gleiche Gliederung bei allen drei (Überschriften der Gutachten):

- **A.** Einzelfragen L1 bis L16 (je Frage Urteil, Beleg, neuer Wortlaut DE und EN)
- **B.** Befundliste (Tabelle, Format unten)
- **C.** Vorlagen „Mit KI besprechen“
- **D.** Aufbau der Simulationsseite
- **E.** Die zehn wichtigsten Änderungen (CLA: „nach Wirkung“)
- **F.** Verwendete Literatur (vollständig, mit Fundstellen)

Zusätzlich: CLA eine Vorbemerkung „Vorgehen, Nachrechnung, Kennzeichnung“ mit Nachrechnungstabelle `| Stelle | Werte im Text | Nachgerechnet |`; GPT einen Prüfanhang (Kontrollierte Rechenwerte `| Fall | Nachrechnung | Vergleich mit Paket |`, Abdeckung der Inhaltsdateien, Repository-Prüfungen `| Prüfung | Ergebnis | Nachweis bzw. Grenze |`, Eingabestand mit SHA-256).

### 4.3 Format der Befundtabelle

Spalten (GPT, wörtlich; CLA gleich, Kopf nur „Schwere“; GEM ohne die letzte Spalte und „Neuer Wortlaut (DE)“):

`| ID | Datei | Block-ID oder Schlüssel | Schwere (hoch/mittel/niedrig) | Art | Heutiger Wortlaut (wörtlich) | Problem | Neuer Wortlaut (wörtlich, DE; EN wenn betroffen) | Beleg | belegt oder eigene Einschätzung |`

**Schweregrade:** hoch, mittel, niedrig. GPT definiert: „‚hoch‘ bedeutet hier ein relevantes Risiko falscher Rechnungen oder Begriffsbildung, keine Aussage über den Gesamtnutzen des Angebots.“ Verteilung (ausgezählt): CLA 2 hoch, 37 mittel, 81 niedrig; GPT 6 hoch, 40 mittel, 17 niedrig; GEM 1 hoch, 2 mittel, 1 niedrig.

**Art (Kategorien):** fachlich, Didaktik, Konsistenz, Ausdruck, Englisch, Format. Verteilung CLA: Konsistenz 39, Didaktik 22, fachlich 19, Ausdruck 18, Englisch 14, Format 8; GPT: fachlich 23, Didaktik 13, Konsistenz 10, Englisch 7, Ausdruck 7, Format 3.

**Letzte Spalte:** „belegt“ (gestützt auf eine genannte Quelle oder nachvollziehbare Nachrechnung) oder „eigene Einschätzung“ (CLA, Vorbemerkung).

### 4.4 Zusammenführung

Von Claude, 04.11.2026 (`runden/R12/Runde12_Gutachten_Zusammenfuehrung.md`):

| Abschnitt | Inhalt und Tabellenformat |
|---|---|
| 0 Kurzfassung | Spalten Gutachten · Umfang · Nachrechnung · Stärke · Schwäche, dazu ein Ergebnissatz |
| 1 Entscheidungen | Spalten Nr. · Frage · Gutachten · Empfehlung Claude · Beleg (K1 bis K10, je mit klarer Empfehlung); danach Spalten Nr. · Entscheidung · Folge für Runde 12 mit den Entscheidungen von Lukas |
| 2 Einzelfragen L1 bis L16 | je **Ergebnis** (wer was sagt, was gewählt wird) und neuer Wortlaut DE und EN als Zitat |
| 3 Abgelehnte oder erledigte Befunde | Spalten ID · Antwort · Begründung mit Beleg · Folge |
| 4 Befundliste zusammengeführt | „Format nach CLAUDE.md: Spalten ID · Antwort · Begründung mit Beleg · Folge“, gruppiert (4.1 bis 4.8 nach Thema und Dateiart); gleiche Befunde mehrerer Gutachten in einer Zeile (z. B. „CLA-012, GPT-005“). Antworten: übernehmen, übernehmen mit Änderung oder nach K-Entscheidung, ablehnen, erledigt, prüfen, Schlüssel löschen, erledigt durch Löschen. 4.6 (Englisch) nur Spalten ID · Antwort · Folge; 4.8 (Folien, nur zur Kenntnis) Spalten ID · Stelle · Befund · Prüfung |
| 5 Gemeinsame Fassung der KI-Vorlagen | Spalten Baustein · Wirkung · Beleg und Wortlaute |
| 6 Simulationsseite | Empfehlung mit Zuordnung alt nach neu |
| 7 Die zehn wichtigsten Änderungen | Liste |
| 8 Selbst geprüfte Belege | Spalten Quelle · Fundstelle · Wofür · Status, dazu „Fehler in den Gutachten selbst“ (z. B. CLA nennt Incropera 3.6.4 statt 3.6.3; GEM nennt DIN 1338 statt DIN 1313) |
| 9 Gegenprüfung | „Eine unabhängige Instanz hat dieses Dokument geprüft“; 17 Mängel, alle eingearbeitet; Spalten Nr. · Mangel · Korrektur |

**Belegkennzeichnung in der Zusammenführung:** CONFIRMED („ich habe die Stelle selbst nachgesehen“) und INFERRED („eigene Einschätzung“). Zahlen: „Zwei unabhängige Nachrechnungen finden keinen Rechen- oder Übertragungsfehler.“

**Rückmeldeformat von Codex in Runde 12** (zum Vergleich): je Aufgabe eine Meldestufe (Z, U, Ä, AB, N; `runden/R12/AUFTRAG.md`, Kopf) und Befunde als `| ID | Schwere | Befund | Beleg | Vorschlag | CONFIRMED/INFERRED |` mit high, medium, low (`runden/R12/RUECKMELDUNG.md`, `RUECKMELDUNG_N1.md`).

### 4.5 Was wir übernehmen sollten (Empfehlung)

1. Befundtabelle mit den zehn Spalten aus 4.3, Schwere hoch, mittel, niedrig (mit der Definition von GPT für „hoch“), Art aus den sechs Kategorien; für die Simulationsseite zusätzlich „Bedienung“ und „Darstellung“ als Art erwägen (im Lernzentrum nicht verwendet).
2. Jede Rolle rechnet alle Zahlen nach und legt eine Nachrechnungstabelle bei (`| Stelle | Werte im Text | Nachgerechnet |`).
3. Jede Aussage als „belegt“ oder „eigene Einschätzung“ kennzeichnen; in der Bündelung CONFIRMED oder INFERRED.
4. Bündelung im Format `| ID | Antwort | Begründung mit Beleg | Folge |`, gleiche Befunde zusammenfassen, abgelehnte Befunde mit Begründung getrennt aufführen, Fehler der Gutachten selbst ausweisen.
5. Entscheidungsfragen an die TL als eigene Tabelle mit klarer Empfehlung; Entscheidung der TL danach getrennt mit Folge eintragen.
6. Gegenprüfung der Bündelung durch eine unabhängige Instanz.

---

## 5. Gelesene Nachweisdateien

**`nachweise/simulation_oben/`** (Textdateien gelesen): `Pruefbericht.md`, `Aenderungsumfang.json`, `CSS_DOM_Hoehenbudget.json`, `Archiv_Quellvergleich.json`, `Veroeffentlichung.json`, `Sprach_UI_Regression.json` (Prüfungen, Fehlerliste und Struktur der 29 Momentaufnahmen gelesen; die Momentaufnahmen selbst sind Textlisten der Oberfläche, nicht einzeln durchgesehen).

**`nachweise/bedienung/`**: `Ausgangsstand.json`, `Python_Lastschutz.json`, `UI_Lastschutz.json`, `Archiv_Quellvergleich.json`, `Veroeffentlichung.json`, `Sprach_UI_Regression.json` (wie oben; deutsche Treffer in den Momentaufnahmen: keine; Fehlerliste leer).

**`nachweise/sprachen/`**: `Abstimmung_Protokollschutz.json`, `Browser_Status.json`, `Dateien_Downloadquellen.json`, `Inhaltsbau.json`, `Inhaltsvergleich.json`, `Python_Diff.patch`, `Python_Sprachvergleich.json`, `UI_Ereignispruefung.json` (wie oben), `Veroeffentlichung.json`, `Veroeffentlichung_Vorpruefung.json`, `ausgangsstand.json`. Ordner `baseline/`: unveränderte Ausgangsdateien für Vergleiche (`MANIFEST.json` gelesen; 11 Code-Dateien `dist/01_conduction/*.py`, `*.ipynb`, `*.js`, `dist/02_convection/fin.py`, `non_fin.py` nur aufgelistet, „keine aktive Text- oder Modellquelle“ laut Manifest).

**Bilder (nur aufgelistet):** `nachweise/sprachen/EX01_EN.png`, `EX04_EN.png`, `EX06_EN.png`.

**Nicht gefunden:** Prompt `00_PROMPT.md` und Paket `Gutachten_Paket_Lernzentrum_2026-11-04.zip` der Gutachten von Runde 12; die Ordner `nachweise/layout_reparatur/` und `nachweise/instationaer/`, auf die der Layoutbericht und der Lastschutzbericht verweisen, liegen nicht im Klon (in `nachweise/` gibt es die Unterordner `bedienung`, `simulation_oben`, `sprachen` und lose Dateien, die nicht zur Leseliste gehören).
