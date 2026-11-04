# Konzept: Simulation „Kaffee mit Milch“ als eigene Website

> Stand 04.11.2026, Phase 1 nach `simulation/AUFTRAG_Simulation_Kaffee.md`, geschrieben von Claude (Cloud-Sitzung) für die Tutoriumsleitung (TL) und zur Prüfung durch Codex (Rolle X4). Entwurf: Die TL entscheidet über die Punkte in Abschnitt 12. Belege und Rechnungen liegen in `simulation/recherche/` (R1 Lernen mit Simulationen, R2 Gestaltung und Bedienbarkeit, R3 Fach und Modell, eigene Nachrechnung in `claude_nachrechnung/`). Skizzen in `simulation/skizzen/`.

## Kurzfassung

- **Ziel:** Das Simulationstool der Kaffee-Aufgabe wird eine eigene Seite mit festem Link, im Aussehen und Ablauf der Simulationsseiten des Lernzentrums, offline als eine Datei lauffähig. Modell unverändert aus `kaffee_modell.py`; Erweiterungen nur mit Herleitung und Testfall.
- **Didaktischer Kern:** erst vorhersagen, dann prüfen (Startzustand ohne Ergebnis, Vorhersage im Werkzeug festhalten, Auflösung erst danach), wenige Regler in Stufen, Messwerte und Modell in einem Diagramm, Energie als Säulen. Belegt meist mittel (Crouch et al. 2004, Holmes et al. 2015, PhET-Studien), Barrierefreiheit stark (WCAG 2.2).
- **Neu gegenüber heute:** Frageleiste mit Vorhersagefeld, angeheftetes Diagramm am Handy, Messblatt alle 10 min mit Link zum Teilen, *kA* aus allen Messpunkten mit Ansicht „ln“, Energie und Bilanzraum, Deckel, Kurven nach der Zugabe, Reiter wie im Lernzentrum.
- **Fachlich bestätigt:** Der größte Unterschied der Tassen liegt genau am Schnittpunkt der Kurven, ist 3,86 K bei jedem *kA* (schwarzer Kaffee dann 35,4 °C) und kommt mit Deckel nur später (100 statt 56 min); ein schwerer Becher verkleinert ihn auf 3,09 K. Deckel: *kA* · 0,56 nach Ferreira 2025a, Abb. 6.
- **Fragen:** Start, Zeitpunkt, Milchtemperatur, Deckel (neu), Versuch; Zusatz Becher, Versuchsplan, Trinken. Etwa 14 min.
- **Entscheidungen E1 bis E8** in Abschnitt 12, je mit Empfehlung; die wichtigste ist E2 (Freischaltung): öffentlich mit Startzustand, der nichts verrät, Link erst in der Sitzung.
- **Nächster Schritt:** Prüfung durch Codex (Rolle X4), dann Entscheidung der TL, dann Bau durch Codex.

## 1 Ausgangslage

**Heutiges Werkzeug.** `Kaffee_Simulation.html` (Zweig `claude/kaffee-pruefung-sgvo1r`, `ergebnisse/kaffee/fertig/`, 30 KB, eine Datei, offline): Diagramm beider Tassen mit Schnittpunkt und Raumlinie, Kennzahlen, sechs Regler und zwei Schalter, fünf weitere Größen aufklappbar, Messwerte aus dem Versuch als Punkte (einzeln eingetragen, im Browser gespeichert), Übernahme in die Einstellungen, vier Fragen mit Vorhersage zu zweit (D114, D116, D124). Das Modell steht zwischen `MODELL-ANFANG` und `MODELL-ENDE` und entspricht `rechne()` und `zwei_tassen()` aus `kaffee_modell.py`; Codex hat es in X3 an 9338 Kurvenwerten bestätigt, die sechs Befunde sind behoben (D116).

**Was bleibt.** Das Modell, die Gültigkeitsprüfungen (ungültige Einstellung blendet Ergebnisse aus), die geprüfte Übernahme der Messwerte (ungerundet oder gar nicht), die Zahleneingabe mit Komma und Punkt, die Fragen mit Vorhersage zu zweit und die Testskripte (`test_simulation.py`, `browsertest.js`) als Grundlage der neuen Tests.

**Was fehlt oder stört** (eigene Sichtung und X3):

1. Die Seite ist eine lange Spalte; am Handy liegen Regler und Fragen weit unter dem Diagramm, man sieht die Wirkung eines Reglers nicht (X3: „Die mobile Bedienung benötigt zusätzliche Scrollwege“).
2. Frage 4 ist ohne eigene Messwerte nicht lösbar (X3), und Messwerte einzeln einzutippen kostet in 10 bis 15 Minuten zu viel Zeit, erst recht beim neuen Versuch mit Messung alle 10 Minuten.
3. Die Energie (Teil e, Kern des Denkfehlers „Die Energie bleibt ja erhalten“) erscheint nur als zwei Zahlen.
4. Die Seite verrät die Antwort auf die Vorab-Frage, sobald sie geöffnet ist.
5. Die Vorhersagen werden nur auf Papier notiert; das Werkzeug zeigt sie nicht neben dem Ergebnis.
6. Aussehen und Ablauf weichen von den Simulationsseiten des Lernzentrums ab.

**Vorbild Lernzentrum** (öffentliche Werkstatt-Seite <https://waermeuebertragung-werkstatt.qarri196.chatgpt.site>, am 04.11.2026 bei 1366 und 390 px angesehen): Schrift Fira Sans; Farben Marine `#102d49` und `#173d5e`, Überschriften `#39718e`, Text `#142337`, Nebentext `#5a6b7f`, Linien `#d8e1ea`, Flächen `#eef5fb`; Ecken 4 px. Über der Simulation Umschaltknöpfe („Stationär · Instationär · Instationär in 2D“), darunter Bild links (bis 780 px) und Knöpfe rechts („Python starten & berechnen“, „Parameter zurücksetzen“), Regler mit Zahlenfeld und Fragezeichen-Hilfe in drei Spalten, Kasten „Rechenwerte“ rechts daneben, dann die Reiterleiste mit neun Reitern. „Probier aus“ ist eine Tabelle (Versuch · Stell dir vor … · Was vermutest du?), die Auflösung steht unter „Versuche“ und „erscheint erst, wenn du sie aufklappst“. Ab dem zweiten Lauf erscheint der vorige Lauf gestrichelt. Am Handy steht das Bild oben, ist aber ein verkleinertes Rasterbild mit sehr kleiner Schrift; Knöpfe und Rechenwerte folgen darunter, die Regler erst nach einer Bildschirmhöhe. Das Lernzentrum duzt; Blatt und heutiges Werkzeug siezen.

## 2 Lernziele der Simulation

Passend zu Tutorium 5 (instationäre globale Bilanz) und zu Lernziel 2 der Variante B (D120). Ein Verb je Ziel.

Nach der Simulation können Sie …

1. erklären, warum Tasse 1 trotz Energieerhaltung wärmer ist, mit der Wärme, die beide Tassen bis zur Zugabe abgeben ($Q_2 - Q_1 = (m_\mathrm{K} c_{p,\mathrm{K}} + m_\mathrm{M} c_{p,\mathrm{M}})(\vartheta_1 - \vartheta_2)$, Teil e).
2. die Wirkung von Zeitpunkt der Zugabe, Milchtemperatur und Deckel auf den Unterschied der Tassen mit dem Wärmestrom $\dot{Q}_\mathrm{ab} = kA\,(\vartheta - \vartheta_\mathrm{u})$ begründen.
3. Abweichungen zwischen Ihren Messwerten und dem Modell mit den Annahmen des Modells begründen (wie Lernziel 2 der Variante B).

Vertiefung für Schnelle und zum Selbstlernen: $kA$ aus einer ganzen Messreihe bestimmen (Ausgleichsgerade von $\ln\frac{\vartheta - \vartheta_\mathrm{u}}{\vartheta_0 - \vartheta_\mathrm{u}}$ über $t$).

## 3 Ablauf in der Sitzung

Minute 75 bis 90 nach dem Zeitplan der Hinweise (D110), zu zweit, ein Gerät je Paar (Handy oder Laptop). Die Studierenden haben a bis e gerechnet und den Versuch bis 40 min gemessen.

| Minute | Studierende (zu zweit) | Tutoriumsleitung |
|:--|:--|:--|
| 75 | Seite über den QR-Code öffnen; Startkarte: Vorhersage antippen (geht schnell, das Ergebnis kennen sie aus d) | QR-Code und Link zeigen; Messwerte des Kurses als Link bereitstellen (Abschnitt 9.4) |
| 76 bis 79 | Frage 1 (Zeitpunkt): Vorhersage notieren und im Feld festhalten, prüfen | Vorhersagen abfragen (Handzeichen), ein Paar mit abweichender Vorhersage begründen lassen (wie D124) |
| 79 bis 82 | Frage 2 (Milchtemperatur) | wie oben |
| 82 bis 85 | Frage 3 (Deckel) | wie oben |
| 85 bis 89 | Frage 4 (Versuch): Messwerte des Kurses laden, Lage der Punkte erklären | zwei Paare erklären lassen; an die Annahmen erinnern |
| 89 bis 90 | Zusammenfassung | Kernsatz: „Wer heißer ist, gibt mehr Wärme ab; deshalb Milch sofort“ |
| für Schnelle | Zusatzfragen (Becher, Versuchsplan, Trinken), Ansicht „ln“ | |

Zeitbedarf: Startkarte 1 min, Fragen 1 bis 3 je etwa 3 min, Frage 4 etwa 4 min, zusammen 14 min. Das ist eine Schätzung; X3 hat ausdrücklich keine Lernzeit gemessen. Beim ersten Einsatz die Zeit je Frage messen (offener Punkt im Protokoll, D114).

**Außerhalb der Sitzung** (Selbstlernen, Nachbereitung): Dieselbe Seite funktioniert allein; die Startkarte sichert die Vorhersage vor dem Aufdecken, die Auflösungen erscheinen erst nach dem Festhalten einer Vorhersage.

## 4 Anforderungen mit Beleg

Stufen: **muss** (ohne das wird nicht eingesetzt), **sollte** (deutlicher Gewinn, mit Aufwand vertretbar), **kann** (wenn Zeit bleibt). Belege: R1 = `recherche/R1_Lernen_mit_Simulationen.md` (Nummern der Folgerungen A1 bis A10 und der Quellen), R2 = `recherche/R2_Gestaltung_Bedienbarkeit.md` (Folgerungen F1 bis F15, Quellen Q1 bis Q37), R3 = `recherche/R3_Fach_und_Modell.md`, X3 = Prüfbericht des heutigen Werkzeugs. Stärke wie in den Berichten: stark (Norm oder Volltext mit klarer Aussage), mittel (Volltext, Übertrag nötig), schwach (Festlegung, Abstract, Erfahrung). Keine didaktische Anforderung ist stark belegt; die Studien betreffen meist Demonstrationen, Schulklassen oder andere Fächer. Was die Literatur nicht trägt, steht in Abschnitt 4.4.

### 4.1 Muss

| Nr. | Anforderung (prüfbar) | Beleg (Stärke) | Prüfung |
|:--|:--|:--|:--|
| M-1 | **Modelltreue.** Grundmodell unverändert aus `kaffee_modell.py` (Block `MODELL` wie im geprüften Werkzeug); jede angezeigte Zahl aus diesem Modell oder einer Erweiterung aus Abschnitt 8.2 mit Testfall. | Auftrag, D114, X3 (stark) | Tests gegen `kaffee_modell.py` und gegen Abschnitt 8 |
| M-2 | **Startzustand ohne Ergebnis.** Vor der ersten Vorhersage zeigt die Seite keine Kurven und keine Endtemperaturen; die Vorhersage (Tasse 1, Tasse 2, gleich; Unterschied in K) wird festgehalten, dann sofort aufgedeckt und bleibt als beschriftete Marke im Diagramm. | R1 A1: Crouch et al. 2004 (Vorhersagen 77 % statt 61 % richtige Ergebnisse, h = 0,35, kostet 2 min; an der Quelle nachgesehen), Brod 2021, Adams, Paulson und Wieman 2009 (mittel; keine Studie prüft genau das Verbergen in einer Simulation) | Browsertest: kein Kurvenpunkt im SVG vor der Vorhersage |
| M-3 | **Vorhersage vor jedem Prüfen.** Jede Frage: Vorhersage im Feld festhalten, erst dann „Prüfen“; die Auflösung ist bis dahin gesperrt. Nach dem Prüfen ein Satz „Stimmt Ihre Vorhersage? Erklären Sie zu zweit, warum.“ | R1 A1, A2: Alfieri et al. 2011 (eingeforderte Erklärungen d = 0,36), Crouch et al. 2004 (nur 30 % richtige Erklärungen trotz Vorhersage), Chi und Wylie 2014; D124 (mittel) | Browsertest je Frage |
| M-4 | **Fachliche Fragen statt Klickanleitung; Ausgangszustand durch „Prüfen“.** Der Knopf lädt den Ausgangszustand der Frage und sagt das an; Regler nur über physikalisch sinnvolle Bereiche. | R1 A5: Adams, Paulson und Wieman 2009, Podolefsky, Perkins und Adams 2010 (implizites Gerüst), Alfieri et al. 2011 (reines Entdecken d = −0,38); X3 Befund Simulation 4 (mittel) | Browsertest: nach „Prüfen“ Standardwerte gesetzt |
| M-5 | **Sofortige Rückmeldung.** Kurven und Rechenwerte folgen dem Regler ohne Knopf „Berechnen“ innerhalb 100 ms. | R1 A6: Adams et al. 2008a/b, D'Angelo et al. 2014; R2 F13: Nielsen 1993/2014 (mittel) | Zeitmessung im Browsertest |
| M-6 | **Frage, Vorhersage und Diagramm zugleich sichtbar.** Laptop: Frageleiste über dem Diagramm. Handy: Diagramm mit drei Kernzahlen angeheftet (höchstens 45 % der Höhe, nur hochkant, abschaltbar), Frage direkt darunter; ein fokussierter Regler wird nicht verdeckt (`scroll-padding-top`). | R2 F9, F15: WCAG 2.4.11 (stark für „nicht verdeckt“), Mayer 2024 räumliche Nähe (Übertrag, mittel); X3 („zusätzliche Scrollwege“) | Browsertest 390 px: Diagramm im Bild, während der Regler fokussiert ist |
| M-7 | **Messwerte und Modell in einem Diagramm.** Messblatt mit Zeilen alle 10 min und drei Bechern; Punkte mit eigener Form je Becher; Übernahme wie D116 (ungerundet oder gar nicht); Frage 4 fragt, ob die Abweichung an der Messung oder am Modell liegt. | R1 A3: Holmes, Wieman und Bonn 2015 (mittel); Lernziel 3; Versuchsplanung der TL | Browsertest mit Komma, Punkt, Lücken, Unsinn |
| M-8 | **Wenige Regler zu Beginn, Freischaltung nach Fragen.** Frage 1 zeigt nur den Zeitpunkt der Zugabe, Frage 2 dazu Milchtemperatur und Milchmenge, Frage 3 Raum, Becher, Deckel, Frage 4 das Messblatt; „Alle Regler zeigen“ für freies Arbeiten. | R1 A4: Adams et al. 2008b (Interviews, mittel); R2 F14: Sweller, van Merriënboer und Paas 2019 (mittel für die Reihenfolge, schwach für die Zahl) | Browsertest: sichtbare Regler je Frage |
| M-9 | **Kurze Beschriftungen, keine nackten Abkürzungen.** Ein bis drei Wörter am Regler, Formelzeichen dazu („Milchtemperatur $\vartheta_\mathrm{M}$“), *kA* mit Wort („Wärmeabgabe *kA*“); Erklärungen in den Reitern und der Fragezeichen-Hilfe. | R1 A7: Adams et al. 2008b (mittel) | Durchsicht |
| M-10 | **Farbe nie allein, Kontrast.** Text mindestens 4,5:1, Kurven, Punkte, Raumlinie, Regler, Fokus mindestens 3:1; Tasse 1 durchgezogen, Tasse 2 gestrichelt, Becher 3 strichpunktiert, Raum gepunktet; Punkte Kreis, Quadrat, Dreieck. Palette nach R2 C3 (Becher 3 `#3d70a3`, Raumlinie `#8a8984`, kein Rot im Diagramm, Marken über Form und Text). | R2 F1 bis F3: WCAG 2.2 1.4.1, 1.4.3, 1.4.11 (stark); Okabe und Ito 2008; eigene Rechnung `r2_kontrast.py` | `r2_kontrast.py` für jede Farbe der Seite; Graustufenbild |
| M-11 | **Direkte Beschriftung.** Kurvennamen am Kurvenzug, keine eigene Farblegende für die Kurven; Schnittpunkt markiert und beschriftet. | R2 F4: Okabe und Ito 2008, Huestegge und Philipp 2011, Mayer 2024 Signalisierung (mittel) | Bildschirmfotos |
| M-12 | **Regler bedienbar ohne Ziehen.** Natives `input type="range"` mit sichtbarem Label, Wert mit Einheit, `aria-valuetext`; Plus und Minus; Zahlenfeld `type="text"` mit `inputmode="decimal"`, Komma und Punkt; Pfeiltasten, Bild auf/ab, Pos1/Ende. | R2 F6: WCAG 2.1.1, 2.5.7, 4.1.2, APG Slider, GOV.UK (stark) | Tastaturtest, axe |
| M-13 | **Ziele und Schrift.** Trefferflächen 44 × 44 px (Pflicht mindestens 24 × 24 px); Eingabefelder mindestens 16 px Schrift; Zoom nicht gesperrt. | R2 F5, F7: WCAG 2.5.8 (stark für 24 px), Apple HIG, Android (mittel für 44 px) | Browsertest misst Größen |
| M-14 | **Umbruch.** Bei 320 bis 767 px eine Spalte, kein waagerechtes Scrollen; Diagramm in tatsächlicher Breite gezeichnet (Schrift nicht verkleinert). | R2 F8: WCAG 1.4.10 (stark); Beobachtung am Lernzentrum (Rasterbild am Handy zu klein) | `scrollWidth` bei 320, 390, 1366 px |
| M-15 | **Bildschirmleser.** Diagramm als `figure` mit Namen, wechselnder Kurzbeschreibung und aufklappbarer Wertetabelle; Kernzahlen nach dem Loslassen über `role="status"`; sichtbarer Fokus 2 px. | R2 F10 bis F12: WCAG 1.1.1, 4.1.3, 2.4.7, W3C Complex Images, Watson 2017 (stark) | axe, Tastaturtest, Sichtprüfung mit Bildschirmleser |
| M-16 | **Gültigkeit.** Ungültige Einstellungen blenden Diagramm und Zahlen sichtbar aus (D116). | X3 Befund Simulation 2 (stark, Erfahrung) | bestehende Tests übernehmen |
| M-17 | **Offline und ohne fremde Server.** Eine Datei, die ohne Netz läuft; keine Anfragen an andere Adressen, keine Zählpixel, keine Links nach außen in der Simulationsansicht; Messwerte und Vorhersagen nur im Browser. | Auftrag; R2 F15 und Sana, Weston und Cepeda 2013 (Ablenkung vermeiden, mittel) | Netzwerkprotokoll im Browsertest (0 fremde Anfragen) |
| M-18 | **Aufbau wie das Lernzentrum.** Bild bis 780 px, Knöpfe rechts, Regler in drei Spalten, „Rechenwerte“ rechts daneben, Reiterleiste mit neun Reitern (APG Tabs, Pfeiltasten); am Handy Akkordeon. | Auftrag; R2 F15: APG Tabs, Sunwall 2024 (mittel) | Bildschirmfotos neben dem Lernzentrum |
| M-19 | **Sprache.** Deutsch, Anrede wie das Blatt, keine Gedankenstriche, Formelzeichen wie in Aufgabe und Lösung, beschreibende Indizes aufrecht (Ä24). | Auftrag, Ä24, D113 | Textprüfung im Test (Zeichen U+2013 und U+2014 verboten) |
| M-20 | **Energie und Bilanzraum** (Erweiterung M3). Kasten „Energie bis zur Zugabe“ mit zwei Säulen $Q_1$, $Q_2$ auf gemeinsamer Nulllinie, Werten und dem Satz „$Q_2 - Q_1$ = … kJ entspricht … K Unterschied“; daneben die Skizze beider Tassen mit gestrichelter Bilanzgrenze und Pfeil $\dot{Q}_\mathrm{ab}$. | Lernziel 1 (Denkfehler „Die Energie bleibt ja erhalten“), Teil b und e; R3 (Bilanzraum muss); R2 Q13/Q14: Cleveland und McGill 1984 über Heer und Bostock 2010, Länge statt Fläche (mittel); R1 A10 (schwach bis mittel) | Zahlen gegen 8.2 (M3) |
| M-21 | ***kA* aus allen Messpunkten** mit Ansicht „Messwerte linear (ln)“, Gerade und Resten (Erweiterung M2). | R3 (muss: Grundlage für Vorabmessung und neuen Versuch; Streuung von *kA* 0,5 bis 0,7 % statt 1,9 %, gekrümmte Reihe sichtbar); R1 A3: Holmes, Wieman und Bonn 2015 (mittel); Hinweis „Probelauf“ der Lösung | Testfälle T09, T10 und gekrümmte Reihe (8.2) |

### 4.2 Sollte

| Nr. | Anforderung | Beleg (Stärke) | Prüfung |
|:--|:--|:--|:--|
| S-1 | **Ansicht „Energie“:** Wärmeströme $\dot{Q}_\mathrm{ab}(t)$ beider Tassen, Fläche dazwischen bis zur Zugabe getönt und mit $Q_2 - Q_1$ beschriftet (Erweiterung M3). | R3 Abschnitt 6 (die Kurven schneiden sich beim größten Unterschied); Flächen nur zusätzlich zu den Säulen, weil Flächen schlechter verglichen werden (R2 Q13/Q14) | Zahlen gegen 8.2 |
| S-2 | **Deckel** (Erweiterung M1), Frage 3. | R3; Ferreira 2025a (an der Quelle nachgesehen); Lernziel 2; Versuchsplanung der TL (Becher eventuell mit Deckel) | Testfälle 8.2 |
| S-3 | **Kurven nach der Zugabe und Vergleichszeitpunkt** (Erweiterung M4): Die Kurven laufen bis zum spätesten Messpunkt bzw. bis „Vergleich nach“ weiter. | R3 (sollte, passt zur Messreihe der TL); neuer Versuch misst auch nach der Zugabe | Testfälle 8.2 |
| S-4 | **Messwerte des Kurses als Link teilen; Beispielmessung.** Die TL trägt die Werte einmal ein und teilt einen Link (Werte im Teil hinter `#`, gehen nicht an einen Server); die Vorabmessung der TL ist als Beispielmessung eingebaut, damit Frage 4 auch ohne Versuch lösbar ist. | X3 (Frage 4 ohne Daten nicht lösbar); Zeitbudget 10 bis 15 min (schwach, Erfahrung) | Browsertest: Link hin und zurück, gleiche Werte |
| S-5 | **Zu zweit so, dass beide beitragen.** Fragenanfang „Notieren Sie erst jede und jeder für sich …, dann einigen Sie sich zu zweit“ (Änderung eines Textes der TL, Entscheidung E7). | R1 A9: Chi und Wylie 2014, Smith et al. 2009 (mittel für die Form, schwach für „zu zweit besser als allein“) | Durchsicht |
| S-6 | **Vergleichslauf.** „Lauf zum Vergleich merken“ legt die aktuellen Kurven blass ins Diagramm (wie im Lernzentrum der vorige Lauf), z. B. für Becher an und aus. | Lernzentrum (schwach, Vorbild) | Browsertest |
| S-7 | **Lesehilfe zum Diagramm.** Höchstens drei Sätze vor der ersten Frage (Achsen, Raumtemperatur, Sprung bei der Milchzugabe), wegklickbar. | R2 F14: Mayer 2024 Vortraining (Übertrag, mittel) | Durchsicht |
| S-8 | **Schrift und Farben wie im Lernzentrum** (Fira Sans eingebettet, SIL Open Font License; Marine, Hellblau). | Auftrag | Bildschirmfotos |
| S-9 | **Druckansicht der Fragen** (eine Seite, mit dem Satz „Laden Sie zuerst die Standardwerte“). | Erfahrung: Vorhersagen werden auf Papier notiert (D124) (schwach) | Druckvorschau |

### 4.3 Kann

| Nr. | Anforderung | Beleg (Stärke) |
|:--|:--|:--|
| K-1 | Zeitzeiger: Tippen ins Diagramm zeigt beide Temperaturen und Wärmeströme zu diesem Zeitpunkt; der Bilanzraum folgt. | R2 Q2 (schwach); van der Meij und de Jong 2003: Verknüpfung hilft nicht sicher, nur schlank umsetzen |
| K-2 | QR-Code für den Link der Kursmesswerte, offline erzeugt. | Zeitbudget (schwach) |
| K-3 | Englische Fassung (Texte so ablegen, dass sie übersetzbar sind). | Entscheidung E3 |
| K-4 | Bechermaterial mit Masse und $c_\mathrm{B}$ als Eingabe (Erweiterung M5). | R3 |
| K-5 | Vergleichskurve mit überlinearer Wärmeabgabe ($n = 5/4$) im Reiter „Modell im Detail“ (Erweiterung M6). | R3; Ferreira 2025a |

### 4.4 Was die Belege nicht tragen

- Dass Simulation und Versuch zusammen mehr bringen als eins allein: Zacharia und Olympiou (2011) fanden zu Wärme und Temperatur keinen Unterschied (R1 Nr. 16). Getragen ist nur: Die Simulation ergänzt den Versuch und zeigt, was die Becher nicht zeigen.
- Dass Arbeit zu zweit besser ist als allein (R1 A9; D'Angelo et al. 2014: nicht signifikant). Getragen ist die Form des Gesprächs (beide tragen bei).
- Eine Höchstzahl von Reglern: keine Quelle nennt eine; „wenige zu Beginn, dann in Stufen“ ist getragen, die Zahl drei ist eine Festlegung (R2).
- Effektstärken nach Mayer: aus Lehrbotschaften, nicht aus Simulationen; sie werden nicht als erwartete Wirkung genannt.
- Ob die Seite vor der Sitzung öffentlich sein darf: Entscheidung der TL (E2), nicht der Literatur.
- Nur als Abstract oder Sekundärquelle geprüft und deshalb nur Nebenbeleg: de Jong und van Joolingen 1998, Lazonder und Harmsen 2016, Rutten et al. 2012, Smetana und Bell 2012, de Jong, Linn und Zacharia 2013, White und Gunstone 1992, Ainsworth 2006, Franconeri et al. 2021 (Einzelheiten in R1 und R2, jeweils Abschnitt „Gestrichen oder nur eingeschränkt“).


## 5 Seitenaufbau

### 5.1 Laptop (ab 1024 px, Abnahme bei 1366 px)

![Skizze Laptop](skizzen/skizze_laptop_1366.png)

Von oben nach unten, wie die Simulationsseiten des Lernzentrums, ohne die Seitenleiste mit den Themen (eine Seite, ein Thema):

1. **Kopf** (Marine): Kürzel „WÜ“, Zeile „Tutorium 5 · Wärmebilanzen, instationär global“, Titel „Kaffee mit Milch: Simulation“; rechts Stand und „Werte bleiben nur in diesem Browser“.
2. **Frageleiste** (hellblau, eine Zeile): aktuelle Frage mit Nummer, Vorhersagefeld, Knopf „Vorhersage festhalten, dann prüfen“, vor und zurück. Abweichung vom Lernzentrum (dort stehen die Fragen nur im Reiter „Probier aus“), damit Frage, Vorhersage und Diagramm zugleich zu sehen sind (M-6).
3. **Ansicht des Diagramms** als Umschaltknöpfe wie „Stationär · Instationär“: „Temperatur“ (Standard), „Energie“, „Messwerte linear (ln)“ (erst aktiv, wenn mindestens drei Messwerte eines Bechers ohne Milch vorliegen).
4. **Diagramm** links, bis 780 px breit, als SVG in der tatsächlichen Breite gezeichnet (Schrift am Handy so groß wie am Laptop). Kurven direkt beschriftet („Tasse 1: Milch sofort“, „Tasse 2: Milch nach 60 min“), Linienart zusätzlich zur Farbe, Mischsprünge kurz gepunktet, Schnittpunkt als Kreis, Raumtemperatur gepunktet, Messpunkte mit eigener Form je Becher, die festgehaltene Vorhersage als beschriftete Marke (Kasten mit Text; Farbe nur zusätzlich, weil neben vier Linienfarben keine fünfte bei Farbsehschwäche sicher unterscheidbar ist, R2 C3), ein gemerkter Vergleichslauf blass.
5. **Knöpfe** rechts: „Standardwerte (Aufgabe)“ (Hauptknopf), „Wie im Versuch (40 min, Becher)“, „Lauf zum Vergleich merken“, „Vorhersage neu“. Darunter zwei kleine Darstellungen: **Energie bis zur Zugabe** (Säulen $Q_1$ und $Q_2$ mit Werten und dem Satz „$Q_2 - Q_1$ = 3,69 kJ entspricht 3,85 K Unterschied“) und **Bilanzraum** (beide Tassen mit gestrichelter Bilanzgrenze, Pfeil $\dot{Q}_\mathrm{ab}$, dessen Breite mit dem Wärmestrom am rechten Rand des Diagramms wächst).
6. **Regler** in drei Spalten, freigeschaltet nach Fragen (M-8; die Skizze zeigt den Stand bei Frage 2): *Milch* (Zugabe nach $t_\mathrm{Z}$, ab Frage 2 Milchtemperatur $\vartheta_\mathrm{M}$ und Milchmenge $V_\mathrm{M}$), *Tasse und Raum* (ab Frage 3: Raumtemperatur $\vartheta_\mathrm{u}$, Becher ohne/Keramik, Deckel offen/zu), *Weitere Größen* (zugeklappt: Anfangstemperatur $\vartheta_\mathrm{K,0}$, Messung nach 10 min, Kaffeemenge $V_\mathrm{K}$, Wärmeabgabe *kA* von Tasse 1 relativ, Bechermasse, Milch für Tasse 2 bei Raumtemperatur, Vergleich nach $t_\mathrm{V}$) und „Alle Regler zeigen“. Jeder Regler mit Zahlenfeld, Plus und Minus und Fragezeichen-Hilfe wie im Lernzentrum.
7. **Rechenwerte** rechts neben den Reglern: $\vartheta_1$, $\vartheta_2$, Unterschied mit Satz („Tasse 1 wärmer“), Schnitt der Kurven, $Q_1$ und $Q_2$, $kA$ aus der Messung, Mischtemperatur $\vartheta_{1,0}$, Ihre Vorhersage.
8. **Messwerte aus dem Versuch** als Messblatt: Zeilen alle 10 min (0 bis 60, weitere Zeile möglich), Spalten Becher 1 (sofort), Becher 2 (Kühltasche), Becher 3 (Glas); Raum- und Milchtemperatur; Knöpfe „Einstellungen aus den Messwerten übernehmen“, „kA aus allen Punkten“, „Beispielmessung laden“, „Messwerte als Link teilen“, „Alle löschen“.
9. **Reiterleiste** mit den neun Reitern des Lernzentrums (Texte in Anhang A). „Versuche“ heißt hier „Auflösungen“, damit es nicht mit dem Becherversuch verwechselt wird (Entscheidung E6).
10. **Fuß**: Stand, Version, Prüfsumme der Datei (Baunachweis), Verweis auf Blatt und Lösung, keine Werbung, keine Zählpixel.

### 5.2 Handy (bis 767 px, Abnahme bei 390 px)

| Startzustand | Beim Arbeiten |
|:--:|:--:|
| ![Skizze Handy Start](skizzen/skizze_handy_start.png) | ![Skizze Handy Arbeit](skizzen/skizze_handy_arbeit.png) |

- **Startzustand:** Achsen, Raumlinie und der Startpunkt 80 °C sind zu sehen, die Kurven nicht. Die Karte „Erst vorhersagen“ fragt: Welche Tasse ist nach 60 min wärmer (Tasse 1, Tasse 2, gleich), um etwa wie viel K? Erst „Kurven zeigen“ zeichnet die Kurven; die Vorhersage bleibt als Marke im Diagramm.
- **Beim Arbeiten:** Diagramm und die drei wichtigsten Zahlen ($\vartheta_1$, $\vartheta_2$, Unterschied) bleiben oben angeheftet (höchstens 45 % der Bildschirmhöhe, abschaltbar), darunter scrollen Frageleiste, Regler und alles Weitere. So sieht man beim Verschieben eines Reglers die Wirkung.
- Eine Spalte. Reglergruppen als aufklappbare Abschnitte (*Milch* offen, die anderen zu). Jeder Regler mit Minus- und Plusknopf und Zahlenfeld, Zielgröße mindestens 44 px. Rechenwerte, Messblatt und Erklärungen als aufklappbare Abschnitte; die neun Reiter werden am Handy zu aufklappbaren Abschnitten in derselben Reihenfolge.
- Kein waagerechtes Scrollen bei 320 bis 767 px; Querformat zeigt Diagramm und Regler nebeneinander.

### 5.3 Zustände, die die Abnahme ansieht

Startzustand vor der Vorhersage; Standardwerte; jede Frage nach „Prüfen“; ungültige Einstellung (Diagramm sichtbar durchgestrichen, keine alten Zahlen, wie D116); Messblatt leer, halb und voll; Ansicht „Energie“ und „ln“; Vergleichslauf; Deckel und Becher an; Handy hoch und quer; Tastatur allein; Bildschirmleser (Abschnitt 10).

## 6 Fragen (Probier aus)

Jede Frage beginnt mit „Sagen Sie erst zu zweit voraus und notieren Sie …“ (D124). Neu: Die Vorhersage wird zusätzlich im Werkzeug festgehalten (Zahl oder Auswahl), erst dann gibt „Prüfen“ den Ausgangszustand frei (Standardwerte laden und sagen, dass sie geladen sind; X3, Befund Simulation 4) und schaltet die Auflösung zum Aufklappen frei. Die erwarteten Antworten sind von Claude unabhängig nachgerechnet (`claude_nachrechnung/n1_hoechstwert.txt`, `n2_erweiterungen.txt`, `n3_fragen.txt`, `n5_r3_gegenpruefung.txt`); die Zahlen der Fragen 1, 2 und der Zusatzfrage Becher stimmen mit den Hinweisen der Lösung überein.

| Nr. | Stellen Sie sich vor … | Was sagen Sie voraus? (Eingabe) | Erwartung (Auflösung) |
|:--|:--|:--|:--|
| Start | Beide Tassen stehen 60 min, Milch aus dem Kühlschrank. | Welche Tasse ist nach 60 min wärmer, um etwa wie viel K? (Tasse 1, Tasse 2, gleich; Zahl in K) | Tasse 1, 3,85 K (34,05 gegen 30,19 °C). Tasse 2 war vor der Zugabe heißer und hat mehr Wärme abgegeben: $Q_2 - Q_1$ = 3,69 kJ. |
| 1 Zeitpunkt | Die Milch kommt früher oder später in Tasse 2. | Bei welchem Zeitpunkt der Zugabe ist der Unterschied am größten? (Zahl in min) | Etwa nach 56 min (3,86 K; die Anzeige zeigt 3,86 K von 53 bis 59 min), genau am Schnittpunkt. Danach ist der schwarze Kaffee kühler als Tasse 1 und gibt weniger Wärme ab. Der Unterschied geht nicht gegen null: Grenzwert 1,91 K (20 °C gegen 18,09 °C), weil die kalte Milch Tasse 2 beim Mischen erneut abkühlt. |
| 2 Milchtemperatur | Die Milch ist wärmer. | Wie warm müsste die Milch sein, damit beide Tassen nach 60 min gleich warm sind? (Zahl in °C) | 47,0 °C. Der Wert hängt vom Zeitpunkt ab: 60,9 °C bei Zugabe nach 30 min, 37,3 °C nach 90 min. |
| 3 Deckel (neu) | Beide Tassen bekommen einen Deckel; sie kühlen langsamer ab ($kA$ um 44 % kleiner). | Wird der größte mögliche Unterschied größer, kleiner oder bleibt er gleich, und wann tritt er ein? (Auswahl; Zahl in min) | Gleich groß (3,86 K), aber später: bei Zugabe nach etwa 100 min statt 56 min (Anzeige 3,86 K von 94 bis 106 min). Nach 60 min ist der Unterschied mit Deckel sogar kleiner (3,51 K). Grund: $kA$ steht nur im Produkt $kA\,t$; der Deckel streckt die Zeitachse, die Kurven schneiden sich immer bei 35,4 °C des schwarzen Kaffees. |
| 4 Versuch | Sie vergleichen Ihre Messwerte mit dem Modell. | Liegen Ihre Messpunkte über oder unter den Kurven, und warum? (Auswahl) | Meist einige Kelvin darüber, je später, desto mehr: Die Wärmeabgabe wächst stärker als linear mit $\vartheta - \vartheta_\mathrm{u}$ (Verdunstung, freie Konvektion), also wird das wirksame $kA$ mit sinkender Temperatur kleiner. In der Ansicht „ln“ liegen die Punkte nicht auf einer Geraden. Der Unterschied zwischen Becher 1 und 2 passt meist besser als die Einzelwerte. |
| Zusatz Becher | Die Tassen sind vorgewärmte Keramikbecher (Teil g). | Wird der Unterschied größer oder kleiner, und bleibt Tasse 1 wärmer? | Kleiner: 3,08 statt 3,85 K; die abgegebene Wärme steigt (46,60 und 50,34 kJ statt 34,88 und 38,57 kJ), weil der Becher mit abkühlt; Tasse 1 bleibt wärmer. |
| Zusatz Versuchsplan | Becher 1 steht auf einer anderen Unterlage und hat 5 % mehr *kA* als Becher 2; oder *kA* beider Becher ist um 10 % falsch bestimmt. | Was verfälscht den Unterschied mehr? | Ungleiches *kA*: Der Unterschied sinkt von 3,85 auf 2,98 K. Falsches *kA* beider Becher ändert ihn um höchstens 0,04 K. Im Versuch zählen gleiche Becher und gleiche Bedingungen mehr als ein genaues *kA*. |
| Zusatz Trinken | Sie trinken erst 30 min nach der Zugabe (Zugabe nach 60 min). | Wird der Unterschied bis dahin größer, kleiner oder bleibt er? | Er klingt ab: 2,03 K nach 90 min, 1,07 K nach 120 min, weil nun beide Tassen dasselbe $m\,c_p$ und $kA$ haben (nur mit Erweiterung M4). |

Fragetexte im Werkzeug (Vorschlag; Frage 1, 2 und Becher wörtlich wie heute nach D116 und D124, Frage 3 und 4 neu):

1. **Zeitpunkt.** Sagen Sie erst zu zweit voraus und notieren Sie: Bei welchem Zeitpunkt der Milchzugabe in Tasse 2 ist der Unterschied zwischen den Tassen ungefähr am größten? Prüfen Sie dann: Verschieben Sie die Zugabe der Milch in Tasse 2. Warum wird der Unterschied bei späterer Zugabe wieder kleiner?
2. **Milchtemperatur.** Sagen Sie erst zu zweit voraus und notieren Sie: Wie warm müsste die Milch sein, damit beide Tassen nach 60 Minuten ungefähr gleich warm sind? Prüfen Sie dann: Stellen Sie die Milch so warm ein, dass beide Tassen ungefähr gleich warm sind. Hängt diese Temperatur vom Zeitpunkt der Zugabe ab?
3. **Deckel.** Sagen Sie erst zu zweit voraus und notieren Sie: Mit Deckel kühlen beide Tassen langsamer ab. Wird der größte mögliche Unterschied zwischen den Tassen größer, kleiner, oder bleibt er gleich? Wann tritt er ein? Prüfen Sie dann: Setzen Sie den Deckel auf und suchen Sie wie in Frage 1 den Zeitpunkt der Zugabe mit dem größten Unterschied. Vergleichen Sie mit Frage 1.
4. **Versuch.** Sagen Sie erst zu zweit voraus und notieren Sie: Liegen Ihre Messwerte über oder unter den Kurven des Modells, und warum? Prüfen Sie dann: Laden Sie die Messwerte Ihres Kurses (Link der Tutoriumsleitung) oder tragen Sie sie ein und übernehmen Sie die Einstellungen aus den Messwerten. Wo liegen die Messpunkte? Liegen die Punkte von Becher 2 in der Ansicht „Messwerte linear (ln)“ auf einer Geraden?

Bei Annahme von E7 beginnt jede Frage mit „Notieren Sie erst jede und jeder für sich …, dann einigen Sie sich zu zweit.“ Den Satz „Laden Sie zuerst die Standardwerte“ übernimmt der Knopf „Prüfen“ (er lädt sie und sagt es an); in der gedruckten Fassung der Fragen (Reiter „Probier aus“, Druckansicht) bleibt der Satz stehen.

## 7 Texte der Reiter

Textvorlagen für alle neun Reiter (Probier aus, Ergebnisse lesen, Auflösungen, Parameter, Physikalisches Problem, Annahmen, Was die Simulation macht, Modell im Detail, So rechnet der Code) stehen in Anhang A, damit der Bau keine eigenen Texte erfinden muss. Zahlen in eckigen Klammern setzt der Bau aus dem Modell ein.

## 8 Modell und Erweiterungen

Regel des Auftrags: Jede Zahl kommt aus `kaffee_modell.py` oder aus einer begründeten, getesteten Erweiterung. Die Erweiterungen ändern das Grundmodell nicht, sie setzen auf ihm auf. Alle Testwerte unten hat Claude mit eigenen Skripten ohne `kaffee_modell.py` gerechnet (`recherche/claude_nachrechnung/`); der Bau prüft sie zusätzlich gegen eine Python-Referenz, die `kaffee_modell.py` importiert.

### 8.1 Grundmodell (unverändert, M0)

Wie `rechne()` und `zwei_tassen()` und wie der geprüfte Block `MODELL-ANFANG` bis `MODELL-ENDE` des heutigen Werkzeugs. Mit $C_\mathrm{K} = \rho_\mathrm{K} V_\mathrm{K} c_{p,\mathrm{K}}$, $C_\mathrm{M} = \rho_\mathrm{M} V_\mathrm{M} c_{p,\mathrm{M}}$, Becher $C_\mathrm{B} = m_\mathrm{B} c_\mathrm{B}$ (sonst 0), $C_\mathrm{KB} = C_\mathrm{K} + C_\mathrm{B}$, $C_\mathrm{GB} = C_\mathrm{K} + C_\mathrm{M} + C_\mathrm{B}$:

- $kA = -\dfrac{C_\mathrm{KB}}{t_\mathrm{mess}} \ln\dfrac{\vartheta_\mathrm{mess} - \vartheta_\mathrm{u}}{\vartheta_\mathrm{K,0} - \vartheta_\mathrm{u}}$ (Teil c, mit Becher Teil g)
- Mischen ohne Wärmeverlust: $\vartheta_{1,0} = \dfrac{C_\mathrm{KB}\,\vartheta_\mathrm{K,0} + C_\mathrm{M}\,\vartheta_\mathrm{M}}{C_\mathrm{GB}}$, ebenso Tasse 2 bei der Zugabe
- Abkühlen: $\vartheta(t) = \vartheta_\mathrm{u} + (\vartheta_0 - \vartheta_\mathrm{u}) \exp(-kA\,t / C)$ mit $C = C_\mathrm{GB}$ (Tasse 1) bzw. $C_\mathrm{KB}$ (schwarzer Kaffee)
- abgegebene Wärme bis zur Zugabe aus der Energiebilanz (Teil e): $Q_1 = C_\mathrm{GB}(\vartheta_{1,0} - \vartheta_1)$, $Q_2 = C_\mathrm{KB}(\vartheta_\mathrm{K,0} - \vartheta_\mathrm{2,K})$
- Schnittpunkt beider Kurven vor der Zugabe in beiden Richtungen (D116)

Testfälle (aus der Lösung, bestätigt): Standard $kA$ = 0,3402 W/K, $\vartheta_{1,0}$ = 70,47 °C, $\vartheta_1$ = 34,05 °C, $\vartheta_2$ = 30,19 °C, $Q_1$ = 34,88 kJ, $Q_2$ = 38,57 kJ, Schnitt nach 55,8 min; mit Becher $kA$ = 0,4440 W/K, 34,04 und 30,96 °C, $Q_1$ = 46,60 kJ, $Q_2$ = 50,34 kJ; wie im Versuch (40 min, Becher) 41,79 und 38,82 °C.

**Eine Eigenschaft, die das Konzept trägt** (eigene Herleitung, `n1_hoechstwert.txt`): Der Unterschied $\vartheta_1 - \vartheta_2$ ist als Funktion des Zeitpunkts der Zugabe genau dann am größten, wenn Tasse 1 und der schwarze Kaffee gleich warm sind (Ableitung null, weil beide dann denselben Wärmestrom abgeben). Am Schnitt ist $\vartheta_\mathrm{x} - \vartheta_\mathrm{u} = (\vartheta_\mathrm{K,0} - \vartheta_\mathrm{u})\,q^{-C_\mathrm{GB}/C_\mathrm{M}}$ mit $q = (\vartheta_\mathrm{K,0} - \vartheta_\mathrm{u})/(\vartheta_{1,0} - \vartheta_\mathrm{u})$, unabhängig von $kA$, und der größte Unterschied ist $C_\mathrm{M}(\vartheta_\mathrm{x} - \vartheta_\mathrm{M})/C_\mathrm{GB}$. Zahlen: ohne Becher $\vartheta_\mathrm{x}$ = 35,38 °C und 3,862 K, mit Becher 35,78 °C und 3,090 K, jeweils für jedes $kA$; nur der Zeitpunkt verschiebt sich (55,8 min; $kA \cdot 0{,}56$: 99,5 min; $kA/2$: 111,5 min; $2\,kA$: 27,9 min). Die Behauptung der Übergabe („rund 3,9 K bei jedem $kA$, schwarzer Kaffee etwa 35 °C, Dämmung verzögert nur“) ist damit bestätigt (R3 Abschnitt 7 kommt unabhängig zum selben Ergebnis), mit zwei Einschränkungen: Sie gilt nur bei gleichem $kA$ beider Tassen, und „Dämmung“ heißt hier kleineres $kA$; die Wärmekapazität eines schweren Bechers verkleinert den Höchstwert (3,09 statt 3,86 K).

### 8.2 Erweiterungen

Grundlage ist R3 (`recherche/R3_Fach_und_Modell.md`, Skript `r3_skripte/r3_rechnungen.py`, Testfälle T01 bis T18). Claude hat die verwendeten Zahlen unabhängig nachgerechnet (`claude_nachrechnung/n2` bis `n6`) und die Deckelzahl an der Quelle nachgesehen. Wo `kaffee_modell.py` eine Funktion hat (`becher`, `zwei_tassen`, `nichtlinear`), stimmen beide Rechnungen mit ihr überein.

| Nr. | Erweiterung | Gleichung und Umsetzung | Grundlage | Testfälle (Standardwerte, wenn nicht anders gesagt) | Stufe |
|:--|:--|:--|:--|:--|:--|
| **M1** | **Deckel** auf beiden Tassen | $kA_\mathrm{Deckel} = f_\mathrm{D}\,kA$ mit $f_\mathrm{D} = 0{,}56$ (Anzeige „44 % kleiner“), für beide Tassen; Schalter „Deckel“. Die Übernahme aus Messwerten schaltet ihn aus (eine Messung mit Deckel enthält ihn schon). | Ferreira 2025a, Abb. 6 (Volltext des Autorenmanuskripts; von Claude an der Quelle nachgesehen): Steigungen von $\ln(T_\mathrm{w} - T_\mathrm{a})$ über $t$ 0,0241 1/min offen und 0,0135 1/min mit 18 mm Styropordeckel, Verhältnis 0,560; der offene Wert entspricht $\tau$ = 41,5 min (Arbeitswert der Aufgabe 41 min). | $kA$ = 0,1905 W/K; $\vartheta_1$ 44,66 °C, $\vartheta_2$ 41,15 °C, Unterschied 3,51 K; $Q_1$ 24,72 kJ, $Q_2$ 28,08 kJ. Größter Unterschied 3,862 K bei Zugabe nach 99,5 min (Anzeige 3,86 K von 94 bis 106 min). Mit Becher: $kA$ 0,2487 W/K, 45,08 und 42,26 °C, 2,83 K. (R3 rechnet mit 0,5602 und erhält 44,65 und 41,14 °C; das Werkzeug nimmt 0,56.) | sollte |
| **M2** | ***kA* aus allen Messpunkten**, Ansicht „ln“ | $y_i = \ln\frac{\vartheta_i - \vartheta_\mathrm{u}}{\vartheta_0 - \vartheta_\mathrm{u}}$ für Becher 2 und 3 vor der Zugabe; Ursprungsgerade $b = \sum t_i y_i / \sum t_i^2$, $kA = -C\,b$ mit $C = C_\mathrm{KB}$, Standardfehler $C\,s/\sqrt{\sum t_i^2}$; zum Vergleich die Gerade mit freiem Achsenabschnitt (ein Abschnitt ungleich null zeigt einen Anlauf). Bogenförmige Reste (außen positiv, innen negativ) ergeben den Hinweis „Kurve gekrümmt: *kA* wird mit sinkender Temperatur kleiner“. **Übernahme ohne Eingriff ins Modell:** Das Werkzeug setzt den gleichwertigen Messwert $\vartheta_\mathrm{mess} = \vartheta_\mathrm{u} + (\vartheta_\mathrm{K,0} - \vartheta_\mathrm{u})\exp(-kA \cdot 600\,\mathrm{s}/C)$, aus dem der Block `MODELL` dasselbe *kA* rechnet. | eigene Herleitung (R3 Abschnitt 5); Ferreira 2025a wertet ebenso über $\ln(T_\mathrm{w} - T_\mathrm{a})$ aus; Hinweis „Probelauf“ der Lösung | T09 exakte Reihe 80,00; 67,00; 56,82; 48,84; 42,59; 37,70; 33,86 °C: alle Verfahren 0,3402 W/K. T10 Reihe 80,1; 67,3; 56,9; 49,1; 42,7; 37,4; 33,7 °C: zwei Punkte 0,3337 W/K, Ursprungsgerade 0,3423 ± 0,0013 W/K, frei 0,3444 ± 0,0021 W/K (Abschnitt +0,007). Gekrümmte Reihe (n = 5/4) 67,00; 57,34; 50,04; 44,43 °C bei 10 bis 40 min: Ursprungsgerade 0,3187 W/K, gleichwertiger Messwert 67,73 °C (mit Becher 0,4159 W/K, ebenfalls 67,73 °C). | muss |
| **M3** | **Energie** | $Q_1(t) = C_\mathrm{GB}(\vartheta_{1,0} - \vartheta_1(t))$, $Q_2(t) = C_\mathrm{KB}(\vartheta_\mathrm{K,0} - \vartheta_\mathrm{2,K}(t))$ bis zur Zugabe, $\dot{Q}_\mathrm{ab}(t) = kA\,(\vartheta - \vartheta_\mathrm{u})$; Säulen bei $t_\mathrm{Z}$ mit $Q_2 - Q_1 = C_\mathrm{GB}(\vartheta_1 - \vartheta_2)$ aus ungerundeten Werten. Ansicht „Energie“: $\dot{Q}_\mathrm{ab}(t)$ beider Tassen, Fläche zwischen den Kurven bis $t_\mathrm{Z}$ getönt und mit $Q_2 - Q_1$ beschriftet; die Kurven schneiden sich beim größten Unterschied. Bilanzraum-Skizze mit Pfeilbreite nach $\dot{Q}_\mathrm{ab}(t_\mathrm{Z})$. Nur Größen des Modells. | eigene Herleitung (R3 Abschnitt 6), Teil e | $Q_1$ 34,88 kJ, $Q_2$ 38,57 kJ, $Q_2 - Q_1$ 3,69 kJ; $\dot{Q}_\mathrm{ab}(0)$ 17,17 W und 20,41 W, bei 60 min 4,78 W und 4,72 W; Schnitt der Wärmeströme bei 55,7 min. Mit Becher: 46,60 und 50,34 kJ, $Q_2 - Q_1$ = 3,73 kJ (aus ungerundeten Werten; die Differenz der gerundeten Anzeigen wäre 3,74). | muss (Säulen, Bilanzraum), sollte (Ansicht) |
| **M4** | **Kurven nach der Zugabe** und eigener Vergleichszeitpunkt | Für $t > t_\mathrm{Z}$ kühlen beide Tassen als Gemisch weiter: $\vartheta_i(t) = \vartheta_\mathrm{u} + (\vartheta_i(t_\mathrm{Z}) - \vartheta_\mathrm{u})\exp(-f_i\,kA\,(t - t_\mathrm{Z})/C_\mathrm{GB})$ ($f_1$ = *kA* von Tasse 1 relativ, $f_2 = 1$); der Unterschied klingt mit $\tau_\mathrm{G} = C_\mathrm{GB}/kA$ ab. Regler „Vergleich nach“ $t_\mathrm{V} \ge t_\mathrm{Z}$, Standard $t_\mathrm{V} = t_\mathrm{Z}$ (dann gleiche Zahlen wie heute). Nötig, damit Messpunkte nach der Zugabe (Versuch: Becher 2 und 3 nach 40 min) neben einer Kurve liegen. | eigene Herleitung (R3 Abschnitt 8, Claude nachgerechnet) | Zugabe 60, Vergleich 90 min: 27,41 und 25,38 °C, 2,03 K; Vergleich 120 min: 23,91 und 22,84 °C, 1,07 K; $\tau_\mathrm{G}$ = 46,91 min. Mit Becher, Zugabe 60, Vergleich 90: 1,59 K. Versuch mit Becher, Zugabe 40: Vergleich 50 min 37,49 und 35,11 °C (2,39 K), 60 min 34,04 und 32,13 °C (1,92 K). Fester Trinkzeitpunkt 60 min: Zugabe nach 10 min 0,57 K, nach 30 min 1,77 K. | sollte |
| M5 | Bechermaterial | Masse und $c_\mathrm{B}$ frei, *kA* weiter aus der Messung (kein *kA*-Faktor je Material, der wäre nur geschätzt). | R3 Abschnitt 2 (Pappbecher 8,3 g nach openLCA 2018; Porzellan $c$ 1,07 kJ/(kg K) nach Engineering ToolBox) | Pappe 11 J/K: 3,81 K; Porzellan 310 g, 1070 J/(kg K): 2,90 K; $\vartheta_1$ bleibt 34,04 bis 34,05 °C. | kann (Empfehlung E4: nur Keramik wie Teil g, Masse frei wie heute) |
| M6 | Überlineare Wärmeabgabe | $\dot{Q}_\mathrm{ab} = c\,(\vartheta - \vartheta_\mathrm{u})^n$, $n = 5/4$ (laminare freie Konvektion an der Tasse), $c$ aus der Messung; Funktion `nichtlinear(n)` des Modells. | R3 Abschnitt 4; Ferreira 2025a (Nu = 0,59 (Gr Pr)^1/4) | $\vartheta_1$ 36,84 °C, $\vartheta_2$ 32,63 °C, Unterschied 4,21 K; größter Unterschied 4,22 K bei 38,18 °C. | kann, nur als Vergleichskurve im Reiter „Modell im Detail“ |
| M7 | Verdunstung als eigener Vorgang | (Stoffübergang mit Dampfdruck, an Ferreira kalibriert) | R3 Abschnitt 3: Anteil etwa 46 % über 60 min, 5 bis 11 g verdunstet, nur Größenordnung | keiner | **nicht**: fremd kalibriert, nicht an eigener Messung getestet; eine Zahl würde die Hausaufgabe beantworten (D123) |

**Zusätzliche Erkenntnisse aus R3 für Versuch und Fragen** (nachgerechnet):

- *Gleiches kA zählt mehr als genaues kA:* *kA* beider Tassen um 10 % falsch ändert den Unterschied nach 60 min nur um höchstens 0,04 K (3,816 bzw. 3,860 statt 3,853 K), 5 % mehr *kA* nur bei Tasse 1 senkt ihn auf 2,98 K, 10 % auf 2,17 K. Gute Zusatzfrage zum Versuchsplan (Abschnitt 6).
- *Nicht vorgewärmter Becher:* Ein Becher mit 255 J/K bei 20 °C senkt 80 °C Kaffee sofort auf 65,98 °C; startet die Uhr beim Eingießen, misst man nach 10 min 56,01 °C, und das Zwei-Punkte-*kA* wird 0,7112 W/K, 2,1-mal zu groß. Für die Vorabmessung der TL: Becher vorwärmen und die Uhr erst nach dem Temperaturausgleich starten (etwa 2 min); Reihe mit und ohne Deckel getrennt auswerten.
- *Erwärmte Milch (60 °C):* Bei früher Zugabe ist erst Tasse 1 wärmer (höchstens +0,34 K bei Zugabe nach 14 min), nach 60 min Tasse 2 (−1,19 K, Teil f).
- *Einschränkung der Kernaussage:* Kleineres *kA* (Deckel, Dämmung) verschiebt den größten Unterschied nur; die Wärmekapazität des Bechers verkleinert ihn (3,09 statt 3,86 K). Bei ungleichem *kA* der Tassen gilt die Unabhängigkeit nicht.


### 8.3 Was das Werkzeug nicht rechnet

- Verdunstung als eigener Vorgang, verdunstete Masse: bleibt pauschal in $kA$ (Annahme der Aufgabe). Eine Zahl dafür im Werkzeug würde die Hausaufgabe zur Verdunstung vorwegnehmen (D123).
- Temperaturverteilung in der Tasse (ideal durchmischt, Annahme der Aufgabe), Wärmeleitung im Becher, Strahlung getrennt.
- Abkühlen des Bechers vor dem Eingießen (vorgewärmt, immer so warm wie der Inhalt, Teil g).


## 9 Technik

### 9.1 Form

- **Eine Datei** `simulation/site/index.html` mit HTML, CSS, JavaScript und Schrift eingebettet. Dieselbe Datei ist die Offline-Fassung (Kopie als `Kaffee_Simulation.html`); so gibt es nichts abzugleichen, und der Baunachweis ist eine Prüfsumme. Ziel unter 400 KB.
- **Keine fremden Server:** keine Bibliotheken aus dem Netz, kein MathJax, keine Webschrift von Google. Inhaltssicherheitsregel im Kopf der Datei (`Content-Security-Policy`: `default-src 'none'`, Stil, Skript und Schrift nur eingebettet, Bilder nur `data:`), damit jede fremde Anfrage im Test auffällt.
- **Kein Rahmenwerk:** einfaches JavaScript wie heute, kein Bauwerkzeug nötig; Formeln in MathML (von aktuellen Browsern ohne Zusatz dargestellt) oder HTML.
- **Schrift:** Fira Sans Regular und Semibold als WOFF2, auf die benötigten Zeichen beschränkt (Lateinisch, Griechisch für $\vartheta$ und $\tau$, °, ·, −, Indizes), Lizenz SIL Open Font License 1.1 als Kommentar in der Datei; Ersatz `system-ui`.

### 9.2 Rechnung im Code

- Block `MODELL-ANFANG` bis `MODELL-ENDE` aus dem geprüften Werkzeug unverändert übernehmen (Gleichungen und Standardwerte wie `kaffee_modell.py`).
- Neuer Block `ERWEITERUNG-ANFANG` bis `ERWEITERUNG-ENDE` mit M1 bis M4 (Abschnitt 8.2), nur Funktionen ohne Bezug auf die Oberfläche, damit Node sie im Test laden kann.
- Python-Referenz `simulation/modell/kaffee_erweitert.py`, die `kaffee_modell.py` importiert (Kopie aus dem Arbeitsordner mit Hinweis auf die Herkunft) und die Erweiterungen in Python enthält; Tests vergleichen JavaScript, Python-Referenz und die Testwerte aus Abschnitt 8.
- Kein Zeitschrittverfahren: Alle Kurven sind geschlossene Lösungen; die Zeichnung tastet sie ab.

### 9.3 Speicher und Datenschutz

Nur `localStorage` im Browser, Schlüssel mit Vorsilbe `kaffee-sim-v2-` (Messwerte, Vorhersagen, gewählte Ansicht, Lesehilfe gesehen). Knopf „Alles zurücksetzen“ löscht sie. Keine Cookies, keine Zählung, keine Formulare an Server. Damit fallen keine personenbezogenen Daten an.

### 9.4 Messwerte teilen

„Messwerte als Link teilen“ schreibt die Tabelle kompakt in den Teil der Adresse hinter `#` (Beispiel `#m=0:71,80.5,80;10:,68,67.5;u:21;M:6`); dieser Teil wird nie an den Server geschickt. Beim Öffnen fragt die Seite: „Messwerte aus dem Link übernehmen? Ihre Tabelle wird ersetzt.“ Ungültige Links werden mit Meldung abgelehnt, nichts wird verändert (wie D116). Die TL zeigt den Link um Minute 75 als QR-Code (selbst erzeugt oder K-2).

### 9.5 Beispielmessung

Die Vorabmessung der TL zu Hause wird als „Beispielmessung (Messung der Tutoriumsleitung, Datum)“ fest eingebaut, mit Angaben zu Becher (Material, Masse), Füllung, Deckel, Raum- und Milchtemperatur und Thermometer. Bis die Daten da sind, bleibt der Knopf ausgeblendet; es werden keine erfundenen Messwerte eingebaut.

### 9.6 Baunachweis und Veröffentlichung

Der Bau legt `simulation/site/BAUNACHWEIS.txt` an: Version, Datum, Commit, SHA-256 von `index.html`, Ergebnis aller Tests. Die Seite zeigt im Fuß Version und Datum. Veröffentlichung über Sites unter `waermeuebertragung-kaffee` (Vorschlag), Seite mit `noindex`. Die Live-Abnahme vergleicht die SHA-256 der ausgelieferten Datei mit dem Baunachweis.


## 10 Prüfplan

| Bereich | Was | Wie | Wer | Erfüllt, wenn |
|:--|:--|:--|:--|:--|
| Zahlen, Grundmodell | Block `MODELL` gegen `kaffee_modell.py` | Gitter über alle Regler wie in X3 (mindestens 9000 Kurvenwerte) | Bau (Codex) | Abweichung höchstens 1e−9 K |
| Zahlen, Erweiterungen | M1 bis M4 gegen Python-Referenz und Testwerte in 8.2 | Node und Python | Bau | Abweichung höchstens 0,005 K bzw. 0,005 kJ |
| Zahlen, Anzeige | angezeigte Werte gegen Modell (Rundung, Komma) | Browsertest liest das DOM | Bau | jede Anzeige gleich dem gerundeten Modellwert |
| Zahlen, unabhängig | Standardwerte, Fragen, zehn eigene Sätze, Grenzen der Regler | eigene Rechnung ohne Code der Seite | Claude (Abnahme) | wie oben |
| Ablauf | Startkarte, vier Fragen und Zusatzfragen in der Reihenfolge der Studierenden, Zeit je Frage | Hand, Handy und Laptop | Claude (Abnahme) | jede Frage ohne Hilfe lösbar, zusammen höchstens 15 min |
| Bedienung | alle Regler, Plus/Minus, Zahlenfelder (Komma, Punkt, Unsinn, Grenzen), Messblatt, Übernahme, Link teilen hin und zurück, Neuladen, Zurücksetzen | Playwright bei 390 × 844, 1366 × 768, dazu 320 px und 844 × 390 quer | Bau, Claude | alle Fälle wie erwartet |
| Handy | kein waagerechtes Scrollen, angeheftetes Diagramm verdeckt keinen fokussierten Regler, Trefferflächen | Playwright misst `scrollWidth`, Rechtecke, Fokus | Bau, Claude | M-6, M-13, M-14 |
| Barrierefreiheit | WCAG 2.2 A und AA | axe-core nur im Test (nicht in der Seite), Tastatur allein, Kontrast mit `r2_kontrast.py`, Bildschirmleser (VoiceOver oder NVDA, Stichprobe) | Bau, Claude | keine Verstöße; alle Funktionen per Tastatur |
| Netz | keine fremden Anfragen | Playwright zählt Anfragen, Seite ohne Netz öffnen | Bau, Claude | 0 fremde Anfragen, offline voll nutzbar |
| Texte | Deutsch, keine Gedankenstriche, Indizes Ä24, Formelzeichen | Suche nach U+2013 und U+2014, Durchsicht | Bau, Claude | 0 Treffer |
| Echte Geräte | iPhone und Android der TL, WLAN im Seminarraum | Probelauf vor der Sitzung | TL | Seite lädt, Regler gehen mit dem Finger |
| Live | Datei gleich dem Bau, Rechenwerte, Handy, Konsole | SHA-256, Stichprobe, Konsole | Claude (Live-Abnahme) | gleich, keine Fehler |

Abnahme nach dem Auftrag: Wer baut, prüft nicht selbst ab. Codex baut und testet, Claude nimmt ab und meldet Befunde zurück, bis nichts Wichtiges offen ist.


## 11 Aufwand (Schätzung)

| Wer | Was | Umfang |
|:--|:--|:--|
| Codex | Prüfung des Konzepts (X4) | ein Lauf |
| TL | Entscheidungen E1 bis E8 | etwa 15 min |
| TL | Vorabmessung zu Hause als Tabelle (Zeit, Temperatur je Becher, Raum, Milch, Becher, Füllung, Deckel) | ohnehin geplant, Abschrift 10 min |
| Codex | Bau mit Tests und Bericht (S-Bau): Grundaufbau, Reiter, Messblatt, Erweiterungen, Barrierefreiheit | zwei bis drei Läufe; Muss und Sollte zusammen etwa doppelt so viel Code wie heute (heute 30 KB) |
| Claude | Abnahme: Zahlen, Fragen, Seiten, Texte; Befunde | eine Sitzung, dazu eine kurze zweite Runde |
| Codex, Claude | Veröffentlichung und Live-Abnahme | je ein kurzer Lauf |
| TL | Probelauf am eigenen Handy, Freigabe | 15 min |

Größter Posten ist die Barrierefreiheit mit Tests; sie ist Muss, weil sie zugleich die Bedienung am Handy sichert. Was nur „kann“ ist, fällt weg, wenn der Bau länger dauert.


## 12 Entscheidungen für die TL

Je Punkt eine klare Empfehlung. Entscheiden tut die TL; danach setzt Codex um (S-Bau).

| Nr. | Frage | Empfehlung | Begründung | Möglich statt dessen |
|:--|:--|:--|:--|:--|
| **E1** | Eigene Website oder Teil des Lernzentrums? | **Eigene Website** unter `waermeuebertragung-kaffee`, Aussehen und Ablauf wie die Simulationsseiten des Lernzentrums; die Arbeitsstränge bleiben getrennt. | Die Seite gehört zu einer Sitzung mit Versuch und Blatt, hat eigene Fragen und ein eigenes Messblatt; im Lernzentrum würde sie dessen Prüf- und Veröffentlichungsrunden binden. Ein Link aus dem Lernzentrum ist später jederzeit möglich. | als viertes Thema im Lernzentrum |
| **E2** | Freischaltung: Die Simulation verrät die Antwort auf die Vorab-Frage. | **Öffentlich mit Startzustand, der nichts verrät** (M-2: Kurven erst nach der eigenen Vorhersage), **Link erst in der Sitzung** (QR-Code um Minute 75), Seite mit `noindex`. | Die Vorhersage vor dem Aufdecken ist didaktisch gewollt (R1 A1) und zeigt das Ergebnis auch dann erst nach einer eigenen Vorhersage, wenn jemand die Seite vorher öffnet; ein Zugangsschutz müsste zur Sitzung von Hand gelöst werden und kann am Tag selbst scheitern. Folge: Der Satz „vorab an die Studierenden verteilen“ in den Hinweisen der Lösung passt dann nicht mehr; ihn ändert ein eigener Auftrag (Blatt und Lösung ändert dieser Auftrag nicht). | (a) nur für die TL sichtbar, öffentlich erst zur Sitzung (Zugang über Sites, falls verlässlich schaltbar); (b) öffentlich ohne Sperre (nicht empfohlen) |
| **E3** | Sprache | **Nur Deutsch**; Texte im Code an einer Stelle gesammelt, damit Englisch später möglich ist (K-3). | Tutorium und Blatt sind deutsch; eine zweite Sprache verdoppelt Texte, Prüfung und Abnahme. | Deutsch und Englisch umschaltbar wie im Lernzentrum |
| **E4** | Welche Erweiterungen? | **M2 *kA* aus allen Punkten mit Ansicht „ln“ und M3 Energie (Säulen, Bilanzraum) als Muss; M1 Deckel, M3 Ansicht „Energie“ und M4 Kurven nach der Zugabe als Sollte**; M5 Bechermaterial und M6 überlineare Vergleichskurve nur als Kann (Becher sonst nur Keramik wie Teil g); **M7 Verdunstung nicht**. | M2 und M4 braucht der neue Versuch (Messung alle 10 min, auch nach der Zugabe) und die Vorabmessung; M1 trägt Frage 3 und den Versuch mit Deckel; M3 trägt Lernziel 1. Verdunstung als Zahl würde die Hausaufgabe beantworten (D123), andere Becher brauchen ein neu gemessenes *kA*. | jede Erweiterung einzeln an oder aus |
| **E5** | Anrede | **„Sie“** wie Blatt, Lösung und heutiges Werkzeug. | Die Seite gehört zum Tutorium; das Lernzentrum duzt, die Abweichung fällt neben dem Blatt nicht auf. | „du“ wie im Lernzentrum |
| **E6** | Name des Reiters „Versuche“ | **„Auflösungen“** | „Versuche“ hieße hier zweierlei (Lernzentrum: Auflösungen der Probierfragen; Tutorium: der Becherversuch). | „Versuche“ wie im Lernzentrum |
| **E7** | Fragen: Auswahl und Anfang | **Frage 3 „Deckel“ neu statt „Becher“** (Becher wird Zusatzfrage); Fragenanfang auf **„Notieren Sie erst jede und jeder für sich …, dann einigen Sie sich zu zweit.“** ändern (Änderung eines Textes der TL, D124). | Der Deckel zeigt das überraschendste Ergebnis (größter Unterschied bleibt 3,86 K, kommt nur später) und gehört zum geplanten Versuch; Becher ist Teil g und nur für Schnelle. Erst einzeln, dann zu zweit sichert, dass beide beitragen (R1 A9). | Fragen wie heute (D124) |
| **E8** | Messwerte im Tutorium | **TL trägt die Kurswerte einmal ein und teilt sie als Link (S-4); Vorabmessung der TL als Beispielmessung einbauen** (bitte die Messreihe als Tabelle liefern: Zeit, Temperatur je Becher, Raum, Milch, Becher mit Material und Masse, Füllung, Deckel; Becher vorwärmen und die Uhr erst nach dem Temperaturausgleich starten, sonst wird das Zwei-Punkte-*kA* bis 2,1-mal zu groß, Abschnitt 8.2). | Eintippen von bis zu 15 Werten je Paar kostet einen großen Teil der 10 bis 15 Minuten; Frage 4 wird so auch ohne eigenen Versuch lösbar (X3). | jedes Paar tippt selbst |


## Anhang A: Texte der Reiter

Textvorlagen für die Website, Anrede „Sie“ (Entscheidung E5). Formeln setzt der Bau in MathML oder HTML (Formelzeichen kursiv, beschreibende Indizes aufrecht nach Ä24), ohne fremde Server. Stellen in eckigen Klammern füllt der Bau aus dem Modell. Wörtlich vom Aufgabenblatt übernommene Sätze sind als solche gekennzeichnet.

### A.1 Probier aus

**Probieren Sie es aus: erst vorhersagen, dann prüfen.** Bearbeiten Sie die Fragen zu zweit. Sagen Sie zuerst voraus, was passiert, notieren Sie es und halten Sie es im Feld fest. Erst dann prüfen Sie im Diagramm. Die Auflösung erscheint im Reiter „Auflösungen“, sobald Sie eine Vorhersage festgehalten haben.

Darunter die Tabelle aus Abschnitt 6 (Spalten Nr., „Stellen Sie sich vor …“, „Was sagen Sie voraus?“) und die vier Fragetexte; je Frage ein Knopf „Diese Frage oben bearbeiten“, der sie in die Frageleiste holt. Druckansicht mit dem Satz „Laden Sie zuerst die Standardwerte.“

### A.2 Ergebnisse lesen

- **Braune durchgezogene Linie:** Tasse 1. Die Milch kommt bei *t* = 0 hinein; der kurze gepunktete Strich bei *t* = 0 ist der Mischsprung von [80] auf [70,47] °C.
- **Schwarze gestrichelte Linie:** Tasse 2, schwarzer Kaffee bis zur Zugabe der Milch. Der gepunktete Strich am Ende ist der Mischsprung beim Zugießen.
- **Kreis:** Schnittpunkt der beiden Kurven. Links davon ist der schwarze Kaffee wärmer als Tasse 1 und gibt mehr Wärme ab, rechts davon weniger. Gibt Tasse 2 die Milch genau am Schnittpunkt dazu, ist der Unterschied am größten.
- **Graue gestrichelte Linie:** Raumtemperatur. Beide Kurven nähern sich ihr, erreichen sie aber nicht.
- **Formen:** Ihre Messwerte (Kreis Becher 1, Quadrat Becher 2, Dreieck Becher 3).
- **Grüne Marke:** Ihre festgehaltene Vorhersage. **Blasse Kurven:** der gemerkte Vergleichslauf.
- **Rechenwerte:** Temperaturen direkt nach der Zugabe in Tasse 2. Der Unterschied ist $\vartheta_1 - \vartheta_2$; positiv heißt: Tasse 1 ist wärmer.
- **Energie bis zur Zugabe:** Wärme, die jede Tasse bis zur Zugabe an die Umgebung abgegeben hat (Teil e). $Q_2 - Q_1$ geteilt durch $m\,c_p$ des Gemischs ergibt genau den Unterschied der Temperaturen.
- **Ansicht „Energie“:** abgegebene Wärme über der Zeit. Die Lücke zwischen den Kurven bei der Zugabe ist $Q_2 - Q_1$.
- **Ansicht „Messwerte linear (ln)“:** $\ln\frac{\vartheta - \vartheta_\mathrm{u}}{\vartheta_0 - \vartheta_\mathrm{u}}$ über *t* für die Becher ohne Milch. Bei konstantem *kA* liegen die Punkte auf einer Geraden durch den Ursprung mit der Steigung $-kA/(m\,c_p)$. Biegt sich die Punktreihe nach oben, wird das wirksame *kA* mit sinkender Temperatur kleiner.
- **Rundung:** Temperaturen auf 0,01 K, Wärmen auf 0,01 kJ. Benachbarte Einstellungen zeigen deshalb manchmal denselben Wert.

### A.3 Auflösungen

Je Frage ein aufklappbarer Abschnitt mit dem Text der Spalte „Erwartung“ aus Abschnitt 6. Gesperrt (Hinweis „Erst eine Vorhersage festhalten“), bis zu dieser Frage eine Vorhersage festgehalten ist; danach zeigt der Abschnitt oben die eigene Vorhersage und darunter die Auflösung.

### A.4 Parameter

| Größe | Zeichen | Standard | Bereich, Schritt | Grundlage |
|:--|:--|:--|:--|:--|
| Zugabe der Milch in Tasse 2 nach | $t_\mathrm{Z}$ | 60 min | 1 bis 180 min, 1 min (heute bis 120 min; 180 min, damit das Maximum mit Deckel bei rund 100 min mittig liegt) | Aufgabe; Versuch 40 min |
| Milchtemperatur | $\vartheta_\mathrm{M}$ | 5 °C | 2 bis 65 °C, 0,5 K | Kühlschrank (BfR), erwärmte Milch 60 °C (Teil f) |
| Milch für Tasse 2 bei Raumtemperatur | | aus | Schalter | Becher 3 im Versuch, Zusatzfrage (2) |
| Milchmenge | $V_\mathrm{M}$ | 30 ml | 5 bis 100 ml, 5 ml | FSANZ 2011, im Mittel 31 g je Tasse |
| Raumtemperatur | $\vartheta_\mathrm{u}$ | 20 °C | 10 bis 30 °C, 0,5 K | Aufgabe |
| Becher | $m_\mathrm{B}$, $c_\mathrm{B}$ | ohne | ohne oder Keramik 300 g, 0,85 kJ/(kg K) | Teil g, Arbeitswert |
| Deckel | | offen | offen oder zu ($kA$ · 0,56) | Ferreira 2025a, Abb. 6 (Erweiterung M1) |
| Vergleich nach | $t_\mathrm{V}$ | gleich $t_\mathrm{Z}$ | $t_\mathrm{Z}$ bis 180 min, 1 min | Erweiterung M4 |
| Anfangstemperatur | $\vartheta_\mathrm{K,0}$ | 80 °C | 60 bis 95 °C, 0,1 K | Abraham und Diller 2019, Brown und Diller 2008 |
| Messung nach 10 min | $\vartheta_\mathrm{K}(10\,\mathrm{min})$ | 67 °C | 30 bis 90 °C, 0,1 K | Aufgabe; entspricht $\tau$ = 41 min (Ferreira 2025) |
| Kaffeemenge | $V_\mathrm{K}$ | 200 ml | 100 bis 400 ml, 10 ml | Aufgabe |
| $kA$ von Tasse 1 relativ | | 100 % | 90 bis 110 %, 1 % | Diskussion in Teil c |
| Masse des Bechers | $m_\mathrm{B}$ | 300 g | 100 bis 600 g, 10 g | Arbeitswert |
| fest: Kaffee | $\rho_\mathrm{K}$, $c_{p,\mathrm{K}}$ | 1000 kg/m³, 4,18 kJ/(kg K) | | Stoffwerte von Wasser |
| fest: Milch | $\rho_\mathrm{M}$, $c_{p,\mathrm{M}}$ | 1030 kg/m³, 3,94 kJ/(kg K) | | Goff; Tutorium 8 |

### A.5 Physikalisches Problem

Wörtlich vom Aufgabenblatt: „Sonntagmorgen in der WG-Küche: Sie haben Filterkaffee gekocht und zwei gleiche Tassen mit je 200 ml gefüllt. Da klingelt das Telefon, und das Gespräch wird eine Stunde dauern. Ihr Mitbewohner gießt seine Milch sofort in den Kaffee (Tasse 1). Sie stellen Ihre Tasse daneben und wollen die Milch erst nach dem Telefonat hineingießen (Tasse 2), damit der Kaffee ‚länger heiß bleibt‘. Die Milch kommt in beiden Fällen direkt aus dem Kühlschrank.“

Ihr Mitbewohner meint: „Ob man die Milch sofort oder später hineingießt, ist egal. Die Energie bleibt ja erhalten.“ Welche Tasse ist nach einer Stunde wärmer?

Beide Tassen geben über ihre Oberfläche Wärme an den Raum ab. Wie viel, hängt davon ab, wie viel wärmer der Inhalt als der Raum ist. Die Simulation rechnet den Vorgang mit der instationären globalen Energiebilanz aus Tutorium 5 und lässt Sie Zeitpunkt der Zugabe, Milch, Raum, Becher und Deckel verändern.

### A.6 Annahmen

Wie auf dem Aufgabenblatt:

- Der Tasseninhalt ist ideal durchmischt, die Milch mischt sich sofort und ohne Wärmeverlust.
- Die Wärmekapazität der Tasse wird vernachlässigt, außer wenn Sie den Becher einschalten (Teil g): Dann ist der Becher immer so warm wie sein Inhalt, auch beim Zugießen der Milch.
- Die gesamte Wärmeabgabe (auch durch Strahlung und Verdunstung) ist $\dot{Q}_\mathrm{ab} = kA\,(\vartheta - \vartheta_\mathrm{u})$ mit konstantem $kA$; die verdunstete Masse wird vernachlässigt.
- Kaffee (Stoffdaten von Wasser) und Milch sind inkompressibel ($c_p = c_v$); die Stoffdaten sind konstant.

Zusätzlich in der Simulation:

- $kA$ kommt aus der Messung nach 10 min und gilt für beide Tassen (Teil c); der Regler „$kA$ von Tasse 1 relativ“ verändert das nur für Tasse 1.
- Deckel: $kA$ beider Tassen ist um 44 % kleiner als bei der Messung ohne Deckel. Der Wert stammt aus einer Messreihe an einem Keramikbecher (Ferreira 2025) und gilt für andere Becher und Deckel nur ungefähr. Wurde die Messung schon mit Deckel gemacht, bleibt der Schalter aus.
- Messwerte: Für die Übernahme gelten Becher 2 und 3 bis zur Zugabe als schwarzer Kaffee mit gleichem $kA$.
- Ideal durchmischt und „Becher so warm wie der Inhalt“ sind gut begründet: Die Biot-Zahl der Keramikwand ist etwa 0,035, und der Becher folgt dem Inhalt in rund einer Minute (R3, Abschnitt 9b; Frage 3 der Sammlung).

### A.7 Was die Simulation macht

1. Aus Anfangstemperatur und Messung nach 10 min bestimmt sie $kA$ (Teil c, mit Becher Teil g).
2. Tasse 1: Sie mischt Kaffee und Milch bei *t* = 0 (Teil a) und lässt das Gemisch bis zur Zugabe abkühlen (Teil b und d).
3. Tasse 2: Sie lässt den schwarzen Kaffee bis zur Zugabe abkühlen und mischt dann die Milch hinein.
4. Sie vergleicht beide Tassen direkt nach der Zugabe, berechnet die abgegebene Wärme aus der Energiebilanz (Teil e) und den Schnittpunkt der Kurven.
5. Sie zeichnet Ihre Messwerte ein. Auf Wunsch übernimmt sie Starttemperatur und Messwert nach 10 min aus Ihren Messungen (Mittel von Becher 2 und 3) oder bestimmt $kA$ aus allen Messpunkten.

Sie rechnet nicht: Verdunstung als eigenen Vorgang (das ist Ihre Hausaufgabe), Temperaturunterschiede innerhalb der Tasse, eine Wärmeabgabe, die stärker als linear mit der Temperatur wächst. Alle Zahlen entstehen in Ihrem Browser; die Seite sendet nichts.

### A.8 Modell im Detail

**Bilanz.** Bilanzraum ist der Inhalt einer Tasse (mit Becher: Inhalt und Becher). Aus der allgemeinen Energiebilanz (Foliensatz 05, Folie 8) bleiben ohne Stoffströme und ohne Arbeit nur die Änderung der inneren Energie und der Wärmestrom an die Umgebung:
$$m\,c_p\,\frac{\mathrm{d}T}{\mathrm{d}t} = -kA\,(T - T_\mathrm{u})$$
Trennung der Variablen mit $T(t = 0\,\mathrm{s}) = T_0$ ergibt
$$T(t) = T_\mathrm{u} + (T_0 - T_\mathrm{u}) \exp\left(-\frac{kA}{m\,c_p}\,t\right), \qquad \tau = \frac{m\,c_p}{kA}.$$
**kA aus der Messung.** $kA = -\frac{m\,c_p}{t_\mathrm{mess}} \ln\frac{T_\mathrm{mess} - T_\mathrm{u}}{T_0 - T_\mathrm{u}}$ (Teil c).
**Mischen.** $\vartheta_\mathrm{misch} = \frac{m_\mathrm{K} c_{p,\mathrm{K}}\,\vartheta_\mathrm{K} + m_\mathrm{M} c_{p,\mathrm{M}}\,\vartheta_\mathrm{M}}{m_\mathrm{K} c_{p,\mathrm{K}} + m_\mathrm{M} c_{p,\mathrm{M}}}$ (Teil a).
**Abgegebene Wärme.** $Q = m\,c_p\,(\vartheta_\mathrm{Anfang} - \vartheta_\mathrm{Ende})$ für jeden Bilanzraum (Teil e); daraus $Q_2 - Q_1 = (m_\mathrm{K} c_{p,\mathrm{K}} + m_\mathrm{M} c_{p,\mathrm{M}})(\vartheta_1 - \vartheta_2)$.
**Größter Unterschied.** Ändert man den Zeitpunkt der Zugabe, wächst der Unterschied, solange der schwarze Kaffee wärmer ist als Tasse 1 (er gibt dann mehr Wärme ab), und sinkt danach. Am größten ist er genau am Schnittpunkt. Weil *kA* nur im Produkt $kA\,t$ vorkommt, verschiebt ein anderes *kA* (Deckel, Dämmung) nur die Zeit: Der größte Unterschied bleibt gleich (bei den Standardwerten 3,86 K, der schwarze Kaffee hat dann 35,4 °C). Ein schwerer Becher dagegen verkleinert ihn (3,09 K), weil er beim späten Zugießen Wärme an Tasse 2 abgibt.
**Deckel** (Erweiterung M1): $kA_\mathrm{Deckel} = 0{,}56\,kA$ (Ferreira 2025a).
**Nach der Zugabe** (Erweiterung M4): Beide Tassen haben dann dasselbe $m\,c_p$ und *kA*; ihr Unterschied klingt mit $\exp(-kA\,t/(m\,c_p)_\mathrm{G})$ ab.
**kA aus allen Messpunkten** (Erweiterung M2): Ausgleichsgerade durch den Ursprung in der Ansicht „ln“, Steigung $b = \sum t_i y_i / \sum t_i^2$ mit $y_i = \ln\frac{\vartheta_i - \vartheta_\mathrm{u}}{\vartheta_0 - \vartheta_\mathrm{u}}$, dann $kA = -m\,c_p\,b$.

### A.9 So rechnet der Code

Die Seite ist eine einzige Datei. Die Rechnung steht in zwei gekennzeichneten Blöcken: `MODELL` enthält dieselben Gleichungen und Standardwerte wie das Rechenskript `kaffee_modell.py` der Lösung (Funktionen `rechne` und `zwei_tassen`), `ERWEITERUNG` die Erweiterungen M1 bis M4. Für jede Einstellung rechnet der Code die Kurven geschlossen aus (keine Zeitschritte, kein Näherungsverfahren); nur die Zeichnung tastet die Kurven in [160] Punkten ab. Geprüft wird mit automatischen Tests: [Zahl] Werte gegen `kaffee_modell.py`, die Erweiterungen gegen eine eigene Rechnung, Bedienung im Browser bei 390 und 1366 px. Stand [Datum], Version [v], Prüfsumme [SHA-256 der Datei] (Baunachweis). Sie können den Code mit „Quelltext anzeigen“ im Browser lesen.

## Anhang B: Im Konzept verwendete Quellen

Vollständige Angaben, Fundstellen und Zitate in R1, R2 und R3. Prüfstatus wie dort; „nachgesehen“ heißt: Claude hat die Stelle zusätzlich selbst an der Quelle gelesen.

| Quelle | Wofür im Konzept | Prüfstatus |
|:--|:--|:--|
| Crouch, Fagen, Callan und Mazur 2004, Am. J. Phys. 72(6), 835 bis 838, doi:10.1119/1.1707018 | M-2, M-3 (Vorhersage vor dem Aufdecken, Zeitbedarf) | Volltext (R1); Table I und „adds only 2 min“ von Claude nachgesehen |
| Brod 2021, Psychon. Bull. Rev. 28(6), 1839 bis 1847, doi:10.3758/s13423-021-01904-1 | M-2 | Volltext (R1); gilt laut Autor für einfaches deklaratives Lernen |
| Adams, Paulson und Wieman 2009, AIP Conf. Proc. 1064, 59 bis 62 | M-2, M-4 | Volltext (R1), DOI und Seiten nur aus Suchergebnis |
| Adams et al. 2008a und 2008b, J. Interactive Learning Research 19 | M-4, M-5, M-8, M-9 | Volltext der Vorabfassung (R1) |
| Wieman, Adams und Perkins 2008, Science 322, 682 bis 683 | M-8 | Volltext (R1) |
| Podolefsky, Perkins und Adams 2010, PRST-PER 6, 020117; Podolefsky, Moore und Perkins 2013, arXiv:1306.6544 | M-4 (implizites Gerüst) | Volltext (R1); 2013 nur als Preprint |
| Alfieri, Brooks, Aldrich und Tenenbaum 2011, J. Educ. Psychol. 103(1) | M-3, M-4 | Volltext (R1) |
| Chi und Wylie 2014, Educ. Psychol. 49(4), 219 bis 243 | M-3, S-5 | Volltext (R1) |
| Smith et al. 2009, Science 323 | S-5 | Abstract (R1) |
| Holmes, Wieman und Bonn 2015, PNAS 112(36); Holmes und Wieman 2018, Physics Today 71(1) | M-7, M-21 | Volltext (R1) |
| D'Angelo et al. 2014, SRI International | M-5 | Volltext (R1); nur Schulklassen |
| Zacharia und Olympiou 2011, Learning and Instruction 21(3) | 4.4 (Kombination nicht automatisch besser) | Abstract (R1) |
| W3C: WCAG 2.2, Empfehlung vom 12.12.2024 (erstmals 05.10.2023), mit „Understanding WCAG 2.2“ | M-6, M-10, M-12 bis M-15 | Volltext (R2) |
| W3C WAI-ARIA Authoring Practices: Slider, Tabs; W3C WAI Images Tutorial: Complex Images; Watson 2017 | M-12, M-15, M-18 | Volltext (R2) |
| Okabe und Ito 2008, Color Universal Design | M-10, M-11 | Volltext (R2) |
| Huestegge und Philipp 2011, Atten. Percept. Psychophys. | M-11 | Volltext (R2) |
| Mayer 2024, Educ. Psychol. Rev. (Prinzipien mit Effektstärken) | M-6, M-11, S-7 | Volltext (R2); Effektstärken aus Lehrbotschaften, nicht aus Simulationen |
| Sweller, van Merriënboer und Paas 2019, Educ. Psychol. Rev. 31 | M-8 | Volltext (R2) |
| Heer und Bostock 2010, CHI (mit Cleveland und McGill 1984) | M-20, S-1 | Volltext (R2); Cleveland und McGill nur darüber |
| Apple Human Interface Guidelines; Android Developers (Barrierefreiheit) | M-13 | Volltext (R2) |
| Laakso 2020, GOV.UK; MDN inputmode; Coyier 2021 | M-12, M-13 | Volltext (R2); iOS-Zoom nur Sekundärquelle |
| Nielsen 1993/2014, Response Times; Sunwall 2024, Tabs; Harley 2015, Slider | M-5, M-18 | Volltext (R2) |
| Sana, Weston und Cepeda 2013, Computers and Education 62 | M-17 | Volltext (R2); Laptops in einer Vorlesung |
| Ferreira 2025a, Forced convection and the coffee cup, Phys. Educ. 60, 035001, doi:10.1088/1361-6552/adb6ea | M1 Deckel, M2, M6, Arbeitswert $\tau$ | Volltext des Autorenmanuskripts (R3); Abb. 6 (Steigungen 0,0135 und 0,0241 1/min) von Claude nachgesehen |
| Ferreira 2025b, Radiation in the coffee cup, Phys. Educ. 60, 015011, doi:10.1088/1361-6552/ad8f84 | Biot-Zahl, Wandtemperatur | Volltext des Autorenmanuskripts (R3) |
| Martin, Bunsen und Ciroth 2018, openLCA Fallstudie Keramik- und Pappbecher; Engineering ToolBox; Suleman und Gas 2024, Int. J. Heat Technol. 42(2) | M5 Bechermaterial | Volltext (R3); Händlermassen und Edelstahl nicht geprüft |
| Condoret 2007, Chem. Eng. Educ. 41(2), 137 bis 143 | M7 (nicht übernommen) | Sekundärquelle (R3) |

