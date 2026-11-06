# G5 Barrierefreiheit: Nachprüfung Runde 3

## 1 Kopf

| Feld | Angabe |
|:--|:--|
| Rolle | G5 Barrierefreiheit (WCAG 2.2, Stufe A und AA; KONZEPT M-6, M-10 bis M-15) |
| Datum | 06.11.2026 |
| Runde | 3 (letzte Runde; Nachprüfung der offenen und neuen Befunde aus Runde 2 und Suche nach Rückfällen, nicht von vorn) |
| Art | getrennte Rollenprüfung desselben Modells |
| Gegenstand | `simulation/site/index.html` (399 063 Byte) |
| SHA-256 | `1d90ce2f84349754592a5dd572a760a5d212cd3383bcafbeb1cceaf06e07292b` (vor Beginn und vor Abgabe mit `sha256sum` geprüft, stimmt) |
| Grundlage | eigenes Gutachten `G5_Barrierefreiheit_R2.md`, Zeilen mit G5-IDs in `ZUSAMMENFUEHRUNG.md` (Runde 1 und Abschnitt „Runde 2“), `KONZEPT.md` M-6, M-10 bis M-15 |
| Umgebung | wie Runde 2: Playwright mit Chromium ohne Kopf (`chromium.launch()` ohne Optionen), axe-core aus `simulation/tests/node_modules` per `page.evaluate`, CDP-Zugänglichkeitsbaum, CDP `Page.setFontSizes` für die Grundschrift, eigene Kontrastrechnung |
| Skripte und Bilder | `/tmp/claude-0/-home-user/8bff1287-c5bb-5641-9916-90393029086f/scratchpad/r3_G5/` (Skripte aus Runde 2 kopiert und erneut ausgeführt, neue Skripte `r3_*.js`, Bilder in `bilder/`, Ausgaben `out_*.txt`) |

## 2 Nachprüfung

Geprüft sind alle G5-Befunde, die in Runde 2 „teilweise“ oder „nicht behoben“ waren, und die neuen Befunde G5-R2-01 bis 08.

| ID | Ergebnis am neuen Stand | Beleg |
|:--|:--|:--|
| G5-05 | behoben | Code: Vergleichskurve Tasse 1 jetzt `opacity="0.8"`; #8b5a2b mit 0,8 auf Weiß ergibt #a27b55, **3,82:1** (Runde 2: 2,58:1); Tasse 2 weiter #909090, 3,19:1. Satz „Blass: gemerkter Vergleichslauf …“ unter dem Diagramm vorhanden (`t10_becher3.js`). Rest ohne Wertung: gleiche Strichart „2 3“ wie die Mischsprünge |
| G5-06 | teilweise (unverändert) | `t20_namen.js` (CDP), Deutsch und Englisch: Spaltenköpfe weiter „ [min]“ (das *t* fehlt), Begriffe der Rechenwerte „Tasse 1 “, „Unterschied “, „abgegeben / “ („Heat released / “); Flächentext in „ln“ weiter „0,3701 WK“ (`out_r2_f2.txt`). Regler und Hilfeknöpfe richtig benannt. Rest: medium wie in Runde 2 |
| G5-07 | teilweise (unverändert) | `r2_f2.js`, `t06_tastatur.js`: Name und Beschreibung folgen der Ansicht; die Wertetabelle zeigt in „Wärmestrom“ und „ln“ weiter nur Temperaturen („t [min] / Tasse 1 [°C] / Tasse 2 [°C] …“). Rest: low |
| G5-08 | teilweise (besser) | `t10_becher3.js`: Die Beschreibung nennt jetzt „Becher 3 nach der Milch 32,10 °C“ (Runde 2 nur in den Rechenwerten). Die Dreiecksmarke im Diagramm bleibt ohne Beschriftung und ohne Legende, solange keine Messwerte da sind (Bild `bilder/b3_ohne_messwerte.png`). Rest: low |
| G5-11 | teilweise (besser) | `r2_mess.js`: Wird die erste von zwei falschen Zellen korrigiert, nennt die Meldung jetzt die verbleibende („Becher 1 (Milch sofort), 30 min: …“), Runde 2: leer. Weiter nur eine gemeinsame Meldung: Solange zwei Zellen falsch sind, beschreibt sie nur die zuletzt geänderte, und die erste Zelle zeigt per `aria-describedby` auf diesen Text. Rest: low |
| G5-18 | behoben | `r2_ueberlapp.js`, `r2_b3.js`, `r3_legende.js`: keine Überlappung von SVG-Texten bei 1366, 390, 360 und 320 px, auch mit Vergleichslauf, Deckel, Trinklinie und Becher 3 und bei Zugabe nach 1, 3, 5 und 30 min; kein Text ragt aus dem SVG. Ersatzlegende als umbrechender HTML-Text (Bilder `bilder/r3_legende_320_tz3.png`, `bilder/r3_legende_360_tz30.png`) |
| G5-21 | behoben | `r2_dia.js`, `r3_dia_ax.js`: `svg role="img"` mit `aria-labelledby="diagramm-name"` und `aria-describedby="diagramm-beschreibung"`, Absatz `aria-hidden="true"`; CDP: Bild „Temperaturverlauf beider Tassen“, Beschreibung einmal, `figure` ohne eigenen Namen. Die Kurzbeschreibung steht nur noch einmal im Lesefluss |
| G5-23 | teilweise (unverändert) | `r2_forced.js`: Diagramm und Säulen im Kontrastmodus weiter lesbar; die gewählte Ansicht bleibt ununterscheidbar („Temperatur“ mit `aria-pressed="true"` und die anderen: Rand 1 px Weiß, Grund Schwarz, Schrift 600; Bild `bilder/r3_forced_dark_ansichten.png`). Rest: low |
| G5-26 | teilweise (unverändert) | `r2_schrift.js`: 24 px Grundschrift ohne Überlauf; 32 px weiter waagerechtes Scrollen (390 px: `scrollWidth` 406; 320 px: 371, Feld „Zeitpunkt etwa … min“ bis 356 px). Rest: low |
| G5-27 | teilweise (Begründung trägt) | `t32_quer.js`: Nebeneinander weiter nicht gebaut (Abweichung ausgewiesen). Die Verdeckung durch die Kernleiste im Querformat ist weg: 915 × 412 rückwärts 1 von 101 Stopps „nicht ganz im Fenster“ (Runde 2: 16), 844 × 390 1 (Runde 2: 5); der eine Stopp ist das Reiterfeld „Versuche“, das höher als das Fenster ist, unverdeckt |
| G5-R2-01 | behoben (Standardschrift); Rückfall bei großer Grundschrift, siehe G5-R3-01 | `r3_kern.js`, Vertiefung offen, 46 Stopps rückwärts: 1366 × 768, 1024 × 600, 1280 × 400, 800 × 500, 1024 × 768, 768 × 1024, 915 × 412, 768 × 400 jeweils **0** teilweise verdeckt (Runde 2: bis 14, einmal 100 %). `scroll-padding-top` 56 px ab 768 px, Kernleiste 34 px |
| G5-R2-02 | behoben (Standardschrift); Rückfall bei größerer Schrift, siehe G5-R3-02 | `r2_anteil.js`, `r3_anteil_zustaende.js`: 320 × 568 **236 px (41,5 %)**, 360 × 640 **246 px (38,5 %)**, 375 × 667 **259 px (38,8 %)**; mit Vergleichslauf, Deckel und Trinklinie 40,6 / 37,7 / 38,0 %; Frage 2 mit Kurswerten 36,8 / 33,8 / 34,3 %. Einziges angeheftetes Element ist `#diagramm-halter`; Schalter „Diagramm oben anheften“ außerhalb. Nebenwirkung siehe G5-R3-03 |
| G5-R2-03 | behoben | wie G5-18: Ersatzlegende als Text unter den Kernzahlen, bricht um, liegt nicht mehr über den Achsenzahlen |
| G5-R2-04 | behoben | `t_lm.js`: nur noch ein Bereich `#messblatt`; `r3_messwrap.js`: Hülle bei 1366 px ohne Rolle, bei 320 px mit Becher 3 (Überlauf 362 > 298 px) `role="region"`, `aria-label="Tabelle, waagrecht scrollbar"`, `tabindex="0"`; axe 0 Verstöße in beiden Zuständen |
| G5-R2-05 | behoben | `r2_neu.js` Teil C, CDP: „Vertiefung“, „Werte als Tabelle“, „Frage 1 von 2 · Zeitpunkt“, „Vertiefung V1 · Milchtemperatur“, ohne ▸ oder ▾ im Namen (Vorlesen INFERRED) |
| G5-R2-06 | behoben | `r2_neu.js` Teil B: fester Text „Diagramm oben anheften“, `aria-pressed` true/false wechselt mit Enter und Leertaste, Fokus bleibt auf dem Schalter |
| G5-R2-07 | behoben | `r2_hinweis.js`: „-3“ am Start ergibt „Diese Zahl liegt außerhalb des sinnvollen Bereichs.“ mit `aria-invalid="true"` und `aria-describedby`; „abc“ weiter „Bitte nur eine Zahl …“. Rest ohne Wertung: Der Bereich wird nicht genannt, Hinweis ohne Live-Bereich (für WCAG 3.3.1 nicht nötig) |
| G5-R2-08 | behoben | `r2_f2.js`, `t25_kurslink.js`: nach „Übernehmen“ Fokus auf `p#link-ende`, `#ansage` leer (Runde 2: gleicher Text doppelt) |

Nebenbei bestätigt: Escape schließt jetzt auch die Rückfragen und setzt den Fokus auf den Auslöser (`r3_esc_rueck.js`; in Runde 2 als unkritisch vermerkt).

Zusammen: von 18 nachgeprüften Punkten behoben 11 (G5-05, 18, 21 und G5-R2-01 bis 08; davon G5-R2-01 und G5-R2-02 mit Rückfall bei vergrößerter Schrift), teilweise 7 (G5-06, 07, 08, 11, 23, 26 und G5-27 mit tragender Begründung), nicht behoben 0.

## 3 axe-core

58 Läufe (Regeln wcag2a, wcag2aa, wcag21a, wcag21aa, wcag22aa, best-practice):

- `t02_axe.js`, 48 Läufe: Deutsch und Englisch, je 1366 × 768 und 390 × 844, je 12 Zustände (P0 vor der Vorhersage, nach der Vorhersage, Auflösung Start mit Wertetabelle, Frage 1 festgehalten mit Auflösung, Vertiefung mit allen Hilfen offen, Ansicht Wärmestrom, Ansicht ln, Messblatt gefüllt mit Becher 3 und übernommen, Eingabefehler, Reiter Modell, Code, Versuche offen).
- `r2_f2.js`, 8 Läufe: Frage 2 mit echtem Kurslink festgehalten, Ansicht Temperatur und ln, Deutsch und Englisch, 1366 und 390 px.
- `r3_messwrap.js`, 2 Läufe: Messblatt mit Becher 3 bei 320 und 1366 px.

Ergebnis: **0 Verstöße in allen 58 Läufen** (Runde 2: 1 Verstoß `landmark-unique` in allen Läufen, jetzt behoben). „Unvollständig“ wie bisher nur `color-contrast` (SVG-Text und MathML, von Hand gerechnet) und `label-content-name-mismatch` (Plus und Minus).

Weitere Rückfallprüfungen:

- **Fokusverdeckung am Handy** (`t07_verdeckt.js`, Frage 1 fest, Vertiefung offen): 390 × 844 vorwärts 0 von 85, rückwärts 0 von 87; 375 × 667 vorwärts 0 von 85, rückwärts 0 von 87 Stopps verdeckt.
- **Fokusverdeckung ab 768 px** mit offener Vertiefung: siehe G5-R2-01, an acht Fenstergrößen 0 Stopps verdeckt.
- **Anteil des angehefteten Bereichs**: siehe G5-R2-02, bei Standardschrift überall unter 45 %.
- **Tastaturdurchgang Pflichtweg** (`t06_tastatur.js`, 1366 px): Sprunglink, Vorhersage mit Leertaste und Pfeiltasten, Festhalten mit Ansage, Frage 1, Auflösung, Regler (Pfeile, Bild auf/ab, Pos1, Ende; `aria-valuetext` „61 min“; 10 schnelle Pfeiltasten ergeben 1 Ansage), Plus, Zahlfeld mit Fehlertext, Hilfe mit Escape, Vertiefung (47 Stopps), Voreinstellung, Ansichten, Reiter nach APG, Sprache, Zurücksetzen mit Rückfrage und Escape: ohne Hänger, 0 Konsolenfehler.
- **Fokusanzeige** (`t16_fokussichtbar.js`, `r3_fokusstil.js`): Ring 2 px #173d5e mit 2 px Abstand an allen geprüften Elementen, `:focus-visible` greift; Sprachknopf wie in Runde 2.
- **Zielgrößen** (`t13_ziele.js`): 121 bis 123 Ziele bei 1366, 390, 320 px, keines unter 44 px.
- **Umbruch** (`t09_umbruch.js`): kein waagerechtes Scrollen von 341 × 192 bis 1366 px, auch bei 200 % Zoom (683 × 384).
- **Ungültige Einstellung** (`t19_ungueltig.js`): 0 Änderungen am `role="alert"` bei 5 Reglerschritten.

## 4 Neue Befunde

| ID | Schwere | Befund | Beleg | Vorschlag | CONFIRMED/INFERRED |
|:--|:--|:--|:--|:--|:--|
| G5-R3-01 | medium | Ab 768 px Breite verdeckt die Kernleiste der Vertiefung den Fokus wieder, sobald die Grundschrift des Browsers vergrößert ist: `scroll-padding-top` ist fest 56 px, die Kernleiste wächst mit der Schrift (0,9rem) und bricht in der schmalen Spalte um. Verletzt in dieser Einstellung M-6 („Fokus nie vollständig verdeckt“, WCAG 2.4.11); die Kernleiste lässt sich nicht lösen. Bei Standardschrift und 24 px ist alles frei. | `r3_kern_schrift.js`, `r3_kern_schrift2.js`, Vertiefung offen, 46 Stopps rückwärts: 768 × 1024 mit 32 px Grundschrift Kernleiste 158 px, **15 Stopps zu 100 % verdeckt** (Häkchen „Trinkzeit bis 60 °C zeigen“, Zahlfeld und Plus von *kA* Tasse 1 …; Bild `bilder/r3_kern_ganz_768_32.png`); 800 × 500 mit 32 px Kernleiste 112 px, 9 teilweise, 1 zu 100 %; 1024 × 768 mit 32 px 67 px, 11 teilweise (bis 48 %); 1366 × 768 mit 32 px 14 teilweise (24 %), mit 28 px 4 teilweise (bis 7 %); 20 und 24 px: 0 | `scroll-padding-top` aus der gemessenen Höhe der Kernleiste setzen (wie `--anheft` am Handy, zum Beispiel per `ResizeObserver`), oder Kernleiste einzeilig halten (`white-space: nowrap`, Einheiten nicht umbrechen) und den Abstand in `rem` angeben | CONFIRMED |
| G5-R3-02 | medium | Am Handy überschreitet der angeheftete Bereich die 45-%-Grenze aus M-6, sobald die Grundschrift größer als 16 px ist. Die Diagrammhöhe ist in `vh` gedeckelt (`min(29vh, 45vh − 125px)`), die Kernzahlen darunter wachsen aber mit der Schrift; die 125 px gelten nur für 16 px. KONZEPT nennt „200 % Text“ ausdrücklich als Handy-Prüffall. Umweg: Schalter „Diagramm oben anheften“; der Fokus bleibt frei (bei 200 % Text 0 Stopps zu mindestens 95 % verdeckt). | `r3_anteil_schrift.js`, nach der Vorhersage: 320 × 568 bei 20 px **45,9 %**, bei 24 px **56,6 %**; 360 × 640 bei 20 px 45,8 %, bei 24 px 49,7 %; 375 × 667 bei 20 px 45,7 %, bei 24 px 49,5 %; `r3_verdeckt_32.js` bei 32 px: 375 × 667 **63 %** (420 px), 390 × 844 53 % (446 px) | Höhe des Diagramms per Skript aus `visualViewport.height × 0,45` minus gemessene Höhe der Kernzahlen begrenzen, oder das Anheften automatisch abschalten, wenn 45 % nicht einzuhalten sind (wie bei zu kleiner sichtbarer Höhe) | CONFIRMED |
| G5-R3-03 | medium | Nebenwirkung der Korrektur zu G5-R2-02: Angeheftet wird das Diagramm auf kleinen Handys auf etwa 56 bis 64 % verkleinert, die Schrift im SVG (Achsenzahlen, Achsentitel, „Raum 20,0 °C“, „Eure Vorhersage“, „Trinktemperatur 60 °C“) schrumpft mit auf 7 bis 8 CSS-Pixel. Kein eigenes WCAG-Kriterium (Zoomen mit zwei Fingern ist erlaubt, Werte stehen auch in Kernzahlen und Wertetabelle), erschwert aber das Ablesen des Diagramms am Handy spürbar, genau dort, wo Frage und Diagramm zusammen gesehen werden sollen (M-6). | `r3_svgschrift.js`, nach der Vorhersage: 320 × 568 SVG 298 × 131 px bei viewBox 298 × 232, Schrift **6,8 bis 7,3 px**; 360 × 640 7,4 bis 8,0 px; 375 × 667 7,6 bis 8,3 px; 390 × 844 10,2 bis 11,1 px; gelöst jeweils 12 bis 13 px. Bild `bilder/r3_anteil_voll_320.png` | Im angehefteten Zustand die viewBox-Höhe an die tatsächliche Höhe anpassen (Diagramm flacher zeichnen statt verkleinern), damit die Schrift bei 12 px bleibt; notfalls weniger Achsenzahlen | CONFIRMED (Maße); INFERRED (Lesbarkeit) |

Zahl der neuen Befunde: blocker 0, high 0, medium 3, low 0.

Restpunkte aus „teilweise“ (nicht neu gezählt): Spaltenköpfe und Rechenwerte ohne MathML-Teil (G5-06, medium); Wertetabelle nicht je Ansicht (G5-07, low); Becher-3-Marke ohne Legende (G5-08, low); gemeinsame Fehlermeldung im Messblatt bei mehreren falschen Zellen (G5-11, low); Ansicht im Kontrastmodus nicht erkennbar (G5-23, low); Überlauf bei 32 px Grundschrift (G5-26, low); Querformat nicht nebeneinander (G5-27, Begründung trägt).

## 5 Offene Nachweise

- **Bildschirmleser:** weiter keiner verfügbar. Offen (M-15: VoiceOver und TalkBack am Gerät): Ausgabe von `aria-valuetext` (CDP zeigt es nicht an), Ansage der Rückfragen-Gruppe, Vorlesen der Ausklapper ohne Zeichen (G5-R2-05), MathML-Teile (G5-06), Beschreibung des Diagramms über `aria-describedby` (G5-21).
- **Echte Geräte:** Anteil des angehefteten Bereichs mit echter Adressleiste. Chromium ohne Kopf rechnet `vh` gleich der sichtbaren Höhe; im echten Browser ist `vh` die große Höhe ohne Leisten. Schätzung für 375 × 667 mit etwa 553 px sichtbarer Höhe: 259 / 553 = 46,8 % (INFERRED, also knapp über 45 %). Dazu Textgröße von Android (Schriftskalierung) und iOS, Abschalten bei offener Bildschirmtastatur.
- **Andere Browser und Systeme:** Firefox und Safari nicht geprüft; Kontrastmodus nur in Chromium emuliert, echtes Windows mit Edge offen (G5-23).
- **Beobachtung außerhalb der Rolle (für G2):** Englische Wärmestrom-Ansicht mit Kurswerten und Zugabe nach 60 min (`out_r2_f2.txt`): „before the intersection … 3.73 kJ · after the intersection … 0.00 kJ · Q2−Q1 = 3.72 kJ (sum of both areas)“. Gerundet passt 3,73 − 0,00 nicht zu 3,72; vermutlich Rundung zweier Werte nahe 3,725 und 0,005. Nicht nachgerechnet.
