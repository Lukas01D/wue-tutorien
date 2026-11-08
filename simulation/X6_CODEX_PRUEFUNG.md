# X6: unabhängige Prüfung der Kaffee-Simulation Fassung 3

Prüfung am 08.11.2026 nach `simulation/X6_AUFTRAG.md`. Sprache: Deutsch. Die Seite, ihre Quellen, die vorhandenen Tests und das Konzept wurden nicht geändert. Kein Pull Request, keine Veröffentlichung.

## Geprüfter Stand und Urteil

| Gegenstand | Stand |
|:--|:--|
| Angeforderter Zweig | `claude/kaffee-simulation-v3-qw4zb2`, ausdrücklich von origin geholt und vor der Prüfung ausgecheckt |
| Geprüfter Commit | `bee711284046211119da07d963a941c93f4568ac` |
| SHA-256 von `simulation/site/index.html` | `ce238edd33ef5ebadb8dc06d3fbd1eba43f7aa8a8cd168a1c407f4430baad0b0` |
| Dateigröße | 175 471 Bytes, 59,50 % kleiner als 433 303 Bytes |
| Prüfzweig | `codex/x6-kaffee-f3`, direkt vom geprüften Commit |
| Eigene Nachweise | `simulation/x6_skripte/` |

**Urteil: mit Änderungen.** Die Rechnung ist richtig und die Gestaltung trägt den Pflichtweg. Vor der Abnahme muss insbesondere der Neustart die Vorhersagesperre wieder vollständig herstellen (X6-01). Das Entscheidungsdokument muss die bereits bestätigten Entscheidungen richtig ausweisen (X6-02). Hinzu kommen zwei kleine Bedienungsbefunde (X6-03, X6-04). Keine Befunde der Stufe blocker.

## Abnahmekriterien

| Nr. | Kriterium des X6-Auftrags | Ergebnis und Beleg |
|:--|:--|:--|
| 1 | Pflichtweg höchstens 8 min, Regler gruppiert | **Nach Schätzung erfüllt:** etwa 7,5 min (01: 1,5; 02: 2,5; 03: 2; 04: 1,5). Milchtemperatur und Zugabe sichtbar, vier Ausgangswerte zugeklappt. Der unten dokumentierte Agentendurchgang ist kein Zeitnachweis mit Studierenden. |
| 2 | Allein ohne Tutorium lösbar | **Im Wesentlichen erfüllt:** mit dem Blatt, ohne Betreuung, mit du-Form, Beispielwerten, Erklärungen und Schlussfrage nutzbar. Der Modell-Link vor Schritt 02 hat ein verstecktes Ziel (X6-04). |
| 3 | Gestaltungssynthese mit Tabelle und Quellen | **Erfüllt:** Konzept Anhang A enthält den Vergleich A, B, C, 0 und die Quellen. Optik, Regler, Direktbeschriftung und Säulen entsprechen der Synthese. Eine erneute Literaturprüfung aller Originalquellen gehört nicht zu diesem Bauabgleich. |
| 4 | Prüfwerte relativ unter 1e-9 gegen das Referenzmodell | **Erfüllt:** eigene Rechnung, ausgelieferter Rechenblock und Referenz stimmen überein. 33 eigene Einstellungen einschließlich Grenzen, 858 Vergleiche mit der Seite, 462 mit der Referenz; Einzelheiten unten. |
| 5 | 15 Kriterien L2 D1 mit Ergebnis | **Erfüllt als Prüfanforderung:** vollständige Tabelle unten, einschließlich bewusst entfallener Modellvarianten und der Einschränkungen. |
| 6 | Keine Ergebniszahlen vor der Vorhersage | **Nicht erfüllt beim Neustart:** frischer Aufruf korrekt, nach „Von vorn“ verbleiben Ergebnisse im DOM und in der zugänglichen Statusansage (X6-01). Säulenzahlen werden im frischen Ablauf erst nach 02 freigegeben. |
| 7 | Keine Verdunstung im Modell | **Erfüllt:** nur Mischung und exponentielle Abkühlung mit konstantem kA. Kein Becher, kein zusätzlicher Wärmeverlust, keine nichtlineare Wärmeabgabe im Rechenweg der Seite. Die gesondert gekennzeichneten Beispielpunkte ändern das Modell nicht. |
| 8 | DE/EN gleichwertig, offline eine Datei, axe ohne Verstoß, Beamer lesbar | **Teilweise erfüllt:** beide Sprachen funktional gleichwertig, eine vollständig eingebettete Datei, keine externen Anfragen, 30 axe-Prüfungen ohne Verstoß. Bei 1280 × 720 passen Kernzahlen, Diagramm und beide Hauptregler ins Bild. ln-Beschriftung bei 390 px abgeschnitten (X6-03). Direkte `file:`-Navigation ist in dieser Umgebung gesperrt, siehe Prüfgrenzen. |
| 9 | Kleiner als Fassung 2 | **Erfüllt:** 175 471 < 433 303 Bytes. |
| 10 | Jede TL-Entscheidung mit Grund und Quelle dokumentiert | **Nicht vollständig erfüllt:** A1 bis A10 stehen trotz Bestätigung noch als offen in der Entscheidungsspalte. GS06 enthält die überholte Nummerierung 01 bis 05 (X6-02). |

## Befunde nach Wichtigkeit

### X6-01 (high): „Von vorn“ stellt die Ergebnissperre nicht wieder her

**Stelle:** `simulation/site/src/oberflaeche.js`, `aktualisiere()` ab Zeile 506, `ansage()` ab Zeile 439 und Neustart ab Zeile 551; ausgeliefert in `simulation/site/index.html`.

**Reproduktion:** Vorhersage festhalten, 02 beantworten, einen Regler verändern, „Von vorn“ bestätigen. Der Zustand ist wieder Z0. Dennoch enthalten `#kern`, `#saeulen` und dessen `aria-label` weiter die zuletzt berechneten Ergebnisse. `#ansage` bleibt im Accessibility-Baum mit den vollständigen Temperaturen und dem Unterschied erhalten. Mit den Blattwerten stehen dort weiterhin 43,85 °C, 40,29 °C und 3,56 K. Im gezielten Lauf mit Milch 6 °C lautet die Statusansage nach dem Neustart: „Nach 60 min: Tasse 1 43,91 °C, Tasse 2 40,41 °C, Unterschied 3,50 K.“ Auch die vorherige Zusammenfassung eigener Rechenwerte wird nur versteckt.

**Beleg:** `x6_skripte/browser_ergebnis.json`, Zustand `Z0_nach_Von_vorn` in allen sechs Läufen; `x6_skripte/befunde_ergebnis.json`, Felder `reset` und `accessibility`. Es gibt außerdem einen zweiten Pfad: Erfolgt der Neustart unmittelbar nach einer Regleränderung, schreibt der noch ausstehende 60-ms-Timer die Ergebnisansage erst nach dem Neustart in Z0 (`race`). Axe erkennt diesen fachlichen Sperrfehler nicht.

**Wirkung:** Die nächste Gruppe erhält einen Startzustand mit vorhandenen Antworten. Die ausdrückliche Anforderung, auch versteckte DOM-Inhalte und Ansagen zu sperren, wird verletzt.

**Vorschlag:** Beim Übergang nach Z0 alle Ergebnisinhalte und Ergebnisattribute einschließlich Zusammenfassung, Kernzahlen, Kernsatz, Säulen und Status leeren. Ansage-Timer verwalten und beim Neustart abbrechen; eine ausstehende Ansage zusätzlich an den gültigen Zustand binden. Die DOM-Sperrprüfung nach einem vollständigen Durchgang und nach einem sofortigen Neustart innerhalb des Timerfensters wiederholen, jeweils in DE und EN.

### X6-02 (medium): Bestätigte Entscheidungen bleiben als offen dokumentiert

**Stelle:** `simulation/ENTSCHEIDUNGEN_F3.md`, Abschnitt 5, Zeilen 101 bis 117; GS06 in Zeile 71.

**Beleg:** Der geprüfte Commit trägt den Betreff „Simulation Fassung 3: QR-Code nur mit der Adresse (Q1), A1 bis A10 bestätigt, Veröffentlichung zuerst privat (V1)“. Auch die Überschrift von Abschnitt 5 sagt „bestätigt am 08.11.2026“. In den zehn Einzelzeilen A1 bis A10 stehen jedoch weiterhin „offen“ und leere Datumsfelder. GS06 sagt „01 bis 05“, während T2 die durchgehende Nummerierung 01 bis 04 festlegt und die Seite sie korrekt umsetzt.

**Wirkung:** Das geforderte Entscheidungsprotokoll widerspricht sich. Eine spätere Umsetzung kann aus den Einzelzeilen nicht zuverlässig erkennen, was bereits freigegeben ist. Die Bestätigung selbst wird damit nicht infrage gestellt.

**Vorschlag:** Die vorhandene Bestätigung in A1 bis A10 mit Datum und genauer Quelle nachtragen, die zugehörigen Gründe erhalten und GS06 an T2 anpassen. A11 gesondert behandeln, dessen Status folgt nicht aus der Bestätigung A1 bis A10. Keine erneute Entscheidung über bereits bestätigte Punkte erforderlich.

### X6-03 (low): ln-Beschriftung wird am Handy rechts abgeschnitten

**Stelle:** `simulation/site/src/oberflaeche.js`, `zeichneLn()`, Zeile 323.

**Reproduktion:** Bei 390 × 844 nach 02 die Beispielwerte und die ln-Ansicht einschalten. Der Text „Modell mit kA = 0,1994 W/K“ wird an der festen x-Position für 32 min platziert. Seine rechte Kante liegt bei 358,39 px, das SVG ist 356 px breit. Englisch reicht der Text bis 362,03 px. Der letzte Teil der Einheit wird abgeschnitten.

**Beleg:** `x6_skripte/befund_ln_390_de.png`, `befund_ln_390_en.png` und `befunde_ergebnis.json`. Die gezielte Messung berücksichtigt die Texttransformationen, die senkrechte Achsenbeschriftung bei 390 px ist nicht betroffen. Es entsteht kein waagerechtes Scrollen, weshalb ein reiner Scrollbreitentest den Fehler übersieht.

**Vorschlag:** Die tatsächliche Textbreite berücksichtigen und die Position auf die SVG-Breite begrenzen, rechtsbündig setzen oder die Beschriftung bei schmalen Diagrammen in eine eigene Zeile legen. Beide Sprachen mit den tatsächlichen Textgrenzen prüfen.

### X6-04 (low): Modell-Link verweist vor 02 auf einen versteckten Abschnitt

**Stelle:** `simulation/site/src/texte_de.txt`, Schlüssel `annahmen`, entsprechend Englisch; `vorlage.html`, Zeile 72 und Modellabschnitt mit `data-ab="2"`.

**Reproduktion und Beleg:** Nach der Vorhersage, vor der Antwort auf 02, ist „Modell“ unter dem Diagramm als Link vorhanden. Ein Klick setzt `location.hash` auf `#modell`; der Zielabschnitt ist weiter `hidden`. In allen sechs Läufen ist `modelLinkZ1.hidden` wahr, zusätzlich gezielt in `befunde_ergebnis.json` belegt. Auf großen Bildschirmen ist der Link schon im leeren Diagramm auf der Startseite vorhanden.

**Wirkung:** Wer beim Selbstlernen die Annahmen genauer nachlesen möchte, erreicht über den sichtbaren Link keinen Inhalt.

**Vorschlag:** Den Link erst mit seinem Ziel freigeben und davor einen kurzen Hinweis zur Freigabe zeigen. Eine vorzeitig zugängliche Modellversion müsste die gesperrten Prüfwerte weiter auslassen. Beim freigegebenen Link kann der Modellbereich zusätzlich aufgeklappt werden.

## Eigene Zahlenprüfung

`x6_skripte/eigenrechnung.py` importiert weder das Referenzmodell noch JavaScript der Seite. Es rechnet in Celsius aus

\[
C_\mathrm{K}=0{,}200\cdot4180,\quad
C_\mathrm{M}=V_\mathrm{M}\rho_\mathrm{M}c_{p,\mathrm{M}},\quad
\vartheta_\mathrm{mix}=\frac{C_\mathrm{K}\vartheta_\mathrm{K}+C_\mathrm{M}\vartheta_\mathrm{M}}{C_\mathrm{K}+C_\mathrm{M}},
\]

\[
kA=-\frac{C_\mathrm{K}}{600}\ln\frac{72-20}{80-20},\quad
\vartheta(t)=\vartheta_\mathrm{u}+(\vartheta_0-\vartheta_\mathrm{u})e^{-kA t/C},\quad
Q=C(\vartheta_0-\vartheta).
\]

Der Schnittpunkt folgt aus der Gleichheit der beiden Abkühlkurven. Die Kipppunkte wurden durch eigene Bisektion des Temperaturunterschieds ermittelt. Das Maximum des Unterschieds liegt dort, wo dessen Ableitung, also der Unterschied der Wärmeverlustraten geteilt durch die gemeinsame Endwärmekapazität, null wird. Daher ist es bei gleichem kA der Schnittpunkt der Kurven vor der späten Zugabe.

| Prüfgröße | Eigene Rechnung | Gerundete Angabe im Auftrag |
|:--|--:|--:|
| kA | 0,199387175472671 W/K | 0,1994 W/K |
| Mischtemperatur Tasse 1 | 70,466209203693 °C | 70,47 °C |
| Tasse 1 nach 60 min | 43,851387846678 °C | 43,85 °C |
| Schwarzer Kaffee nach 60 min | 45,425166748971 °C | 45,43 °C |
| Tasse 2 nach der Milch | 40,286432313098 °C | 40,29 °C |
| Unterschied | 3,564955533580 K | 3,56 K |
| Q1 | 25,490238695396 kJ | 25,49 kJ |
| Q2 | 28,904560597860 kJ | 28,90 kJ |
| Schnittpunkt | 95,126474151575 min | etwa 95 min |
| Milch 70 °C, Tasse 1 | 47,756474559494 °C | 47,76 °C |
| Milch 70 °C, Tasse 2 | 48,549051003230 °C | 48,55 °C |
| Kipppunkt bei 60 min | 58,177374460809 °C | 58,2 °C |
| Zeit bis 60 °C, Tasse 1 | 18,607320719680 min | 18,6 min |

Geprüft wurden 33 Einstellungen: Blatt, Milch 70 °C, Milch bei Raumtemperatur, jede Reglergrenze einschließlich der 30-°C-Sperre, zwei kombinierte Randfälle und 15 eigene reproduzierbare Zufallsfälle. Pro Fall wurden Kennzahlen und beide Kurven bei sechs Zeiten verglichen. Die Zeit wird in Sekunden eingesetzt; der kA-Regler bleibt bei Änderung von Kaffee und Raum fest. Der Rechenblock der ausgelieferten HTML-Datei stimmt in 858 skalaren Vergleichen mit der eigenen Rechnung überein, maximale relative Abweichung 8,54e-12. Ein separater Referenzvergleich umfasst 462 Werte und bestätigt außerdem `STANDARD` gegen `werte.py`.

Bei Milchtemperatur gleich Kaffeetemperatur ist die Schnittzeit mathematisch null. Die Referenz liefert durch die Kelvin-Umrechnung 2,93e-11 s, die eigene Rechnung und die Seite null. Ein relativer Fehler ist bei null nicht sinnvoll; für diesen Fall wird absolut mit 1e-9 s geprüft. Das ist kein fachlicher Fehler. Die übrigen Prüfwerte liegen unter der geforderten relativen Grenze.

Zusätzlich stimmen 34 Zahlenvergleiche in den deutschen und englischen Texten mit der eigenen Rechnung: Rückmeldungen a und b, Aufgaben 1 bis 3 und Modell-Prüfwerte. Insbesondere 3,41 kJ, 957,7 J/K, 2,56 K bei Milch 20 °C, Maximum 3,86 K bei etwa 95 min, Grenzwert 1,91 K sowie Kipppunkte 68,1 / 58,2 / 49,9 °C bei 30 / 60 / 90 min sind richtig. Deutsch und Englisch verwenden die jeweiligen Dezimalzeichen. Keine Gedankenstriche in den beiden Textquellen, du-Form und Formelzeichen sind konsistent.

## Bedienung und eigener Pflichtweg

Eigene Playwright-Läufe: Chromium 154.0.8037.57 bei 390 × 844, 1366 × 768 und 1280 × 720, jeweils DE und EN. Netzstatus offline, die unveränderten HTML-Bytes werden als einzige Testressource lokal bereitgestellt; alle anderen Anfragen werden abgebrochen und protokolliert. Beobachtet wurden ausschließlich die anfängliche lokale Navigation und das gezielte Neuladen. Kein externer Request, kein JavaScript- oder Konsolenfehler. Die CSP blieb eingeschaltet.

Geprüft sind Vorhersagepflicht mit auswählbarem Grund und freiwilligem Text, gültige und unsinnige Ergebnisse aus e, alle sechs Regler mit Ziehen, Plus, Minus, Komma, Punkt, Pfeiltasten, Home, End, PageUp und PageDown, Grenzen und Fehlermeldungen. Messpunkte: Komma/Punkt gemischt, fehlender Wert x, leere Felder, zu viele Werte, negative Werte, über 100 °C, ungültiger Text und Plausibilitätshinweis. Beispielwerte, ln-Ansicht, alle drei Aufträge, Schlussantwort, Sprachwechsel, Neuladen mit Erhalt der Eingaben, „Werte des Blatts“, „Von vorn“ und gesperrter Speicher wurden durchlaufen. Die warme Milch ist vor Auftrag 3 korrekt gesperrt und danach verfügbar.

Bei allen sechs Läufen bleibt die Seitenbreite gleich der Viewportbreite. Eigene Bildschirmfotos wurden angesehen, insbesondere Start, Ergebnis, ln-Ansicht und Beamer in beiden Sprachen. Das Ergebnisdiagramm und die Hauptregler sind bei 1280 × 720 vollständig lesbar. Der konkrete Ausreißer ist X6-03. Axe-core 4.11.0 meldet in fünf Zuständen je Lauf, insgesamt 30 Prüfungen mit den Tags WCAG 2.0/2.1/2.2 A und AA, **null Verstöße**. Das ist keine vollständige manuelle WCAG-Zertifizierung.

Ein eigener Durchgang nur durch die Bedienelemente ist mit Zeitstempeln in `x6_skripte/pflichtweg.jsonl` dokumentiert. Wahl: Tasse 1, weil heißerer Kaffee mehr Wärme abgibt; eigene Rechenwerte 43,85 und 40,29 °C. Danach Erklärung a, Beispielpunkte mit ln-Ansicht und eine eigene Schlussantwort. Vom Start des Browserdurchgangs bis zum Beginn der abschließenden Eingabeaktion vergingen 37,03 s; das anschließende Ausführen der Aktion ist darin noch nicht enthalten. Dieser schnelle Agentenlauf ersetzt keinen Erstlauf mit Studierenden. Mit Lesezeit, Erklären und Eingeben schätze ich den Pflichtweg auf etwa 7,5 min. Bei vielen selbst einzutragenden Messwerten kann er länger dauern; beim ersten Einsatz stoppen.

Gestockt habe ich am abgeschnittenen Modelltext in der mobilen ln-Ansicht. Bei der späteren Vertiefung zeigt die auf zwei Dezimalstellen gerundete Differenz bei 90, 95 und 100 min jeweils 3,86 K. Mit dem Werkzeug lässt sich daher ein breites Maximum um 95 min erkennen, keine minutengenaue Optimierung verlangen. Auftrag 1 ergab 2,56 K; bei Auftrag 3 ergaben 68,1 °C nach 30 min und 49,9 °C nach 90 min jeweils gerundet 0,00 K. Die jeweilige Auflösung wurde erst nach der eigenen Prüfung geöffnet. Die Vertiefung ist deutlich als Tätigkeit nach dem Tutorium oder zu Hause gekennzeichnet.

## 15 Kriterien L2 D1

| Nr. | Kriterium | Eigenes Ergebnis |
|:--|:--|:--|
| S1 | Zweck am Anfang | erfüllt: Zweck und Einordnung nach e |
| S2 | Vorhersage mit Grund vor Kurven | erfüllt im frischen Lauf; bei Wiederverwendung Einschränkung X6-01 |
| S3 | Ersetzt nicht die Rechnung | teilweise: Hinweis nach e, Säulenzahlen nach 02 und warme Milch nach Auftrag 3 richtig; Neustart verrät vorhandene Antworten |
| S4 | Zusammenhang sichtbar | teilweise und so konzipiert: Säulen und Bilanz vorhanden, Bilanzraum-Skizze und Wärmestrom-Ansicht bewusst entfallen |
| S5 | Startwerte, Bereiche, Herkunft | erfüllt: Herkunft am Blatt, vorläufige Ausgangswerte, Skalen und Grenzen; `STANDARD` gegen `werte.py` geprüft |
| S6 | Annahmen bei Ergebnissen | erfüllt: Annahmenzeile am Diagramm |
| S7 | Eignung und Grenzen des Modells | erfüllt: Modellbereich, Hinweis auf Versuch, Tasse, konstantes kA und fehlende Verdunstung |
| S8 | Rechenweg offen, Prüfwerte | erfüllt nach Freigabe: Gleichungen und d1/d2, Quelltext eingebettet; Link vorher ohne zugängliches Ziel, X6-04 |
| S9 | Vergleich mit Messung | erfüllt: eigene Punkte, getrennte Beispielpunkte, Kernsatz zur Modellprüfung |
| S10 | Modellvarianten nebeneinander | bewusst nicht umgesetzt: Entscheidung für ein unverändertes Modell, Variation über Regler |
| S11 | Form passt zum Inhalt | weitgehend erfüllt: direkte Kurvennamen, unterscheidbare Linien und Säulen, hervorgehobene Differenz; ln-Textgrenze X6-03 |
| S12 | Selbststeuerung | teilweise: ruhende Darstellung, freie Eingaben und Blattwerte; Neustart technisch unvollständig, X6-01 |
| S13 | Offline, responsiv, barrierearm, zweisprachig | überwiegend erfüllt im beschriebenen Testumfang: kein Querscrollen, axe null, DE/EN; mobile Beschriftung und Prüfgrenzen beachten |
| S14 | Daten ohne Personenbezug | keine geteilten Messwerte vorgesehen: ausschließlich lokaler Speicher, keine Übertragung; verständlicher Hinweis bei gesperrtem Speicher |
| S15 | Keine Punkte/Uhr, Schluss mit Grenzen | erfüllt: qualitative Rückmeldungen mit Gründen, eigene Schlussantwort |

## Vergleich mit den vorhandenen Bauprüfungen und Prüfgrenzen

Erst nach den eigenen Rechnungen, dem Werkzeugdurchgang und den sechs Browserläufen wurden `BAU_BERICHT_F3.md`, die vorhandenen Tests und Ergebnisdateien sowie die Bilder unter `bildschirmfotos/f3/` gelesen beziehungsweise angesehen. Die dort berichteten 34 Rechenprüfungen, 16 Textprüfungen und 93 Browserprüfungen wurden nicht als eigener Prüfnachweis ausgegeben und nicht erneut ausgeführt, da sie ihre vorhandenen Ergebnisdateien überschreiben würden.

Die positiven Rechen- und Sprachbefunde stimmen mit den Bauprüfungen überein. Die Abweichungen sind erklärbar: Der vorhandene Test „Von vorn löscht alles“ prüft nur Zustandsobjekt und Speicher, nicht die verbleibenden DOM- und Statusinhalte (`tests/browsertest.js:179`). Die vorhandene Z0-DOM-Prüfung erfolgt am frisch geladenen Dokument. Die Bildliste enthält eine ln-Aufnahme nur für Laptop und Deutsch, keine für Handy. Damit decken diese Nachweise X6-01 und X6-03 nicht ab. Die vorhandenen Tests wurden nicht geändert.

`bauen.py --pruefen` ergibt **gleich** und bestätigt den deterministischen Bau ohne Änderung der Seite. Dafür wurde die fehlende Brotli-Abhängigkeit außerhalb des Repositories bereitgestellt. Die verwendeten Skripte und Voraussetzungen stehen in `x6_skripte/README.md`.

Die verwaltete Chromium-Installation verhindert direkte `file:`-Aufrufe mit `ERR_BLOCKED_BY_ADMINISTRATOR`. Ein zusätzlicher Browserdownload war durch die Netzrichtlinie gesperrt. Deshalb erfolgt der Offline-Funktionstest mit exakt denselben Datei-Bytes über eine abgefangene lokale Adresse; ein direkter Nachweis des Öffnens vom Dateisystem ist damit nicht erbracht. Safari, echte Touchgeräte und ein physischer Bildschirmleser beziehungsweise Hörsaalbeamer waren nicht Teil dieses Laufs. Für die Statusansage liegt ein Accessibility-Snapshot vor. Diese Grenzen ändern die reproduzierten Befunde nicht.
