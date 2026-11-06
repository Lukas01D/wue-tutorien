# Gutachten G3, Runde 2: Fachgutachter Wärmeübertragung

| | |
|:--|:--|
| Rolle | G3 „Fachgutachter Wärmeübertragung“ |
| Datum | 06.11.2026 |
| Runde | 2 (Nachprüfung der eigenen Befunde aus Runde 1, Regressionsrechnung, neue Anzeigen) |
| Art | getrennte Rollenprüfung desselben Modells |
| Gegenstand | `simulation/site/index.html` |
| SHA-256 | `ea6d3ad224030ff9a783517b7c6af059c8bba48600c80c83819c41db85ea9c31` (vor und nach der Prüfung mit `sha256sum` geprüft, gleich) |
| Umgebung | Linux-Container, Node v22.23.4, Playwright mit Chromium (`chromium.launch()` ohne Optionen), Python 3.13.18, Fenster 1366 × 900 px, Seite als `file:`-Aufruf |
| Maßstab | wie Runde 1: `simulation/KONZEPT.md`, Aufgabe und Lösung in der fertigen Fassung vom 31.10.2026 |

Gelesen: eigenes Gutachten aus Runde 1, in `ZUSAMMENFUEHRUNG.md` nur die Zeilen G3-01 bis G3-24. Nicht gelesen: Code der Seite, `BAU_BERICHT.md`, `ZWISCHENSTAND.md`, `PROTOTYPEN.md`, `tests/`, `recherche/`, andere Gutachten, Git-Protokoll. Alle Sollwerte stammen aus meiner eigenen Rechnung (`g3_rechnung.py` aus Runde 1, unverändert kopiert).

**Kurzurteil.** Alle 30 Zustände stimmen weiter in jeder angezeigten Zahl (30 von 30, dazu zwei Zusatzfälle). Die neuen Anzeigen rechnen richtig: Zahlvergleich in den Auflösungen, Becher 3 mit eigenem Mischsprung und eigenem Unterschied, Gerade mit freiem Achsenabschnitt (jetzt 14 Punkte, 0,4493 W/K), Wertetabelle mit Zeile „nach der Milch“ und Messwerten, Teilflächen, Trinkzeit, Becher kalt, CSV (deutsch und englisch, 0 Abweichungen in 8 Dateien). Von 13 übernommenen Befunden sind 10 behoben und 3 teilweise behoben. Neu: ein kleiner Befund (Wärmestrom-Text nennt einen Schnitt, den es bis zur Zugabe nicht gibt). Keine falsche Zahl, keine falsche Physik.

## 1 Nachprüfung

Bedienung jeweils: Startfrage (Tasse 1) festhalten, Frage 1 (56 min) festhalten, Vertiefung öffnen; für Messpunkte zusätzlich Kurswerte übernehmen und Frage 2 festhalten (wie im Bedienhinweis).

| ID | Entscheidung | Ergebnis am neuen Stand | Beleg |
|:--|:--|:--|:--|
| G3-01 | übernehmen | **behoben.** Die Rückmeldung trennt Auswahl und Zahl: „Auswahl passt“ und darunter „Eure Zahl: 50 K · Modell: 3,85 K (Standardwerte)“. Eine falsche Größenordnung bekommt kein bestätigendes Zeichen mehr. Ebenso Frage 1 („Eure Zahl: 56 min · Modell: etwa 56 min“), V1 („50 °C · Modell: 47,0 °C“), V2 („50 min · Modell: etwa 100 min“), englisch „Your number … model …“. Modellzahlen gleich meinen (3,8532 K; 55,745 min; 47,003 °C; 99,54 min). | `erkunde4.js`, `erkunde5.js`, `g3_vertiefung_r2.js` (de, en) |
| G3-02 | offen | Text unverändert („Tasse 2 war bis zur Zugabe heißer …“). Die Empfehlung in der Zusammenführung („bis etwa 56 min heißer und gab bis zur Zugabe insgesamt mehr Wärme ab“) ist fachlich richtig (Schnitt 55,745 min) und trägt. | `erkunde3.js` |
| G3-03 | ablehnen | Unverändert: Kurven, Rechenwerte und Energie zeigen bei gesetztem Schalter „Becher beim Eingießen kalt (Raumtemperatur)“ den vorgewärmten Becher, ohne es zu sagen; die Zusatzzeile stimmt (bei *kA* 0,444: 59,85 / 65,98 °C, 30,67 / 28,05 °C, 2,62 K, vorgewärmt 3,08 K; bei 0,3402: 34,52 / 31,95 °C, 2,56 K, vorgewärmt 3,05 K; eigene 59,8549 / 65,9762, 30,6680 / 28,0510 / 2,6170 bzw. 34,5157 / 31,9526 / 2,5631, 3,0528). Die Begründung trägt für die Kurven (neue Darstellung, M9 verlangt sie nicht), aber nicht für die fehlende Kennzeichnung. Empfehlung bleibt die kleine Lösung: bei gesetztem Schalter in den Rechenwerten „(Becher vorgewärmt; kalt siehe Zeile unter dem Diagramm)“. | `r2_csv.js` Fall „kalt“, `r2_rest.js`, `vergleich30.py` (Z29) |
| G3-04 | offen | Deutsch unverändert „Wärmeabgabe der Tasse *kA* [W/K]“; englisch jetzt „Heat loss coefficient *kA*“ (richtig). Die Begründung (Wortlaut M-9, Entscheidung der TL) trägt formal; fachlich bleibt die Doppelbedeutung mit $\dot{Q}_\mathrm{ab}$ in W. | `r2_csv.js` Fall „std_en“ |
| G3-05 | offen | Unverändert (Ansicht ln: „Steigung $-kA/(m\,c_p)$“). Empfehlung „mit Becher $C_\mathrm{GB}$“ trägt. | `r2_legende.js` |
| G3-06 | offen | Unverändert: bei 100 ml Milch steht weiter „Mischsprung von 80 auf 70,47 °C“ (Rechenwerte 55,49 °C). Empfehlung „(Standardwerte)“ trägt. | `r2_b3tz.js` |
| G3-07 | offen | Unverändert („Schnitt der Kurven nach 84,9 min“ gegen Teilflächen „vor dem Schnitt … 2,86 kJ“ mit Teilung bei 60,96 min). Empfehlung trägt. | `r2_csv.js` Fall „tz120_105“ |
| G3-08 | übernehmen | **behoben.** V3 nennt „Ausgangslage: Standardwerte, Becher an, *kA* aus der Messung nach 10 min (wie Teil g)“ und stellt genau das ein; nach „Einstellungen aus den Messwerten übernehmen“ steht „Ausgangslage eingestellt: Kurswerte übernommen (kA aus 0 und 10 min, Becher an)“. | `g3_vertiefung_r2.js`, `r2_f1.js` |
| G3-09 | übernehmen | **behoben.** Kaffee 60 °C mit *kA* aus der Messung (67 °C): Rechenwerte „Keine Rechnung: Einstellung ungültig“, ebenso die Energiezeile. | `r2_rest.js` |
| G3-10 | offen | Unverändert („gemessen sind ‚Keramik offen‘ (Aufgabe) …“). Empfehlung trägt. | `r2_b3tz.js` |
| G3-11 | offen | Unverändert (deutsch und englisch „Glas und Pappe sind etwa wie Keramik“). Empfehlung trägt. | `g3_vertiefung_r2.js` |
| G3-12 | ablehnen | Unverändert fest 60 °C. Begründung trägt (K-3 ist im Konzept „kann“); Zahlen richtig: 10,9 / 16,6 min, mit Becher 12,4 / 16,6 min, mit Deckel 19,5 / 29,7 min (eigene 10,904 / 16,604; 12,353 / 16,604; 19,471 / 29,650). | `vergleich30.py` (Z01t, Z22, Z30) |
| G3-13 | offen | Unverändert drei Reiter; außerhalb der fachlichen Rolle, keine neue Beurteilung. | Startseite |
| G3-14 | übernehmen | **teilweise behoben.** Der zweite Mischsprung ist da: blau gepunktet (`#3d70a3`) von 34,15 auf 32,73 °C nach Pixeln (eigene 34,1577 → 32,7364), 5 px rechts neben dem Sprung von Becher 2, mit hohler Endmarke; er folgt der Zugabezeit (bei 30 min: Rechenwerte 46,20 °C, eigene 46,1977). Es fehlt weiter eine Beschriftung im Bild, und Lesehinweis („die kurzen gepunkteten Striche sind die Mischsprünge“) und Diagrammbeschreibung nennen Becher 3 nicht; die Legende darunter nennt nur die Messpunkte. Bei 1366 px ist der Sprung 6,7 px hoch und von den Messdreiecken kaum zu trennen. | `r2_f1.js`, `r2_lage_f1.json`, `r2_diag_f1.png`, `r2_legende.js`, `r2_b3tz.js` |
| G3-15 | übernehmen | **behoben.** „Becher 3 (Milch mit Raumtemperatur) 32,74 °C“ ohne $\vartheta_2$, dazu „Unterschied Tasse 1 und Becher 3 1,57 K“ (eigene 34,3095 − 32,7364 = 1,5731 K); bei Zugabe 30 min 1,18 K (eigene 1,1801). | `r2_f1.js`, `r2_b3tz.js` |
| G3-16 | übernehmen | **behoben.** Englische CSV: Feld in Anführungszeichen, `csv`-Leser findet 5 Kopf- und 5 Datenfelder; Werte stimmen (0 Abweichungen). | `r2_csv_std_en.csv`, `r2_check.py` |
| G3-17 | ablehnen | Unverändert: keine Bedingungen, kein Modellwert Becher 3 nach der Milch, Zeile „56 nach der Milch“ hinter den leeren Zeilen 57 bis 60. Begründung (M11 verlangt Zeit, Modell, Messblatt) trägt für den Pflichtumfang; für die Nachbereitung (K-5) bleibt die Datei ohne Raum- und Milchtemperatur schwer auswertbar. Keine Zahl falsch. | `r2_csv_f1.csv`, `r2_csv_tz56.csv` |
| G3-18 | übernehmen | **teilweise behoben.** Wertetabelle hat jetzt die Zeile „60 nach der Milch“ (34,31 / 31,23 °C) getrennt von „60“ (34,31 / 34,16 °C) und nach Frage 2 die Messwerte von Becher 1 bis 3 (Becher 1 ohne Wert nach der Milch, richtig). Alle 13 Modellzeilen gleich meiner Rechnung. Es fehlen weiter der Modellwert von Becher 3 nach der Milch (32,74 °C) und der Vergleichslauf (der steht nur als Satz unter dem Diagramm). | `r2_tabelle_f1.txt`, `r2_check.py`, `r2_rest.js` |
| G3-19 | übernehmen | **teilweise behoben.** Gerechnet und angezeigt wird jetzt einheitlich mit ganzen Minuten (30,4 → „nach 30 min“ mit Werten für 30 min: 46,62 / 43,27; 7,5 → „nach 8 min“ mit 62,55 / 61,17, eigene 62,5542 / 61,1721); beim Verlassen des Feldes (Tab) steht dort 30. Nach Enter bleibt im Feld aber „30,4“ bzw. „7,5“ stehen, während Regler und Rechnung 30 bzw. 8 zeigen. | `r2_csv.js`, `r2_rest.js`, `r2_b3tz.js` |
| G3-20 | übernehmen | **behoben.** „mit freiem Achsenabschnitt 0,4493 W/K“ (eigene 14 Punkte, Startpunkt je Becher: 0,44932, Abschnitt +0,0056); Ursprungsgerade 0,4470 W/K aus 12 Punkten (eigene 0,44698). | `r2_legende.js`, `r2_check.py` |
| G3-21 | übernehmen | **behoben.** Vergleichslauf mit Mischsprung (Deckkraft 0,5, Sprung auf 30,20 °C nach Pixeln) und Satz „Blass: gemerkter Vergleichslauf (Zugabe nach 60 min): Tasse 1 34,05 °C, Tasse 2 30,19 °C, Unterschied 3,85 K.“ Zahlen gleich Z01. | `r2_rest.js`, `r2_vergleich.png` |
| G3-22 | übernehmen | **behoben.** Satz einmal als Fußnote; der Stern hinter der Erklärung ist der Fußnotenverweis. | `r2_rest.js` (HTML des Kastens) |
| G3-23 | übernehmen | **behoben** (a und b). (a) Ändert sich nur der Teil hinter `#`, erscheint die Abfrage mit „Übernehmen“. (b) Leeres Messblatt: kein Link, Meldung „Das Messblatt ist leer; erst Werte eintragen.“ | `r2_rest.js` |
| G3-24 | übernehmen | **behoben.** Nach Sprachwechsel lautet die offene Abfrage „Use the class data from the link? Your previous class data will be replaced.“ | `r2_rest.js` |

Zusammen: übernommen 13, davon behoben 10 (G3-01, G3-08, G3-09, G3-15, G3-16, G3-20, G3-21, G3-22, G3-23, G3-24), teilweise behoben 3 (G3-14, G3-18, G3-19), nicht behoben 0. Offen 8 (G3-02, G3-04 bis G3-07, G3-10, G3-11, G3-13) und abgelehnt 3 (G3-03, G3-12, G3-17): unverändert; die Begründungen bzw. Empfehlungen tragen fachlich, bei G3-03 nur für die Kurven, nicht für die fehlende Kennzeichnung.

## 2 Regressionsrechnung: 30 Zustände

Skripte `g3_seite_r2.js` (aus `g3_seite.js` aus Runde 1; geändert nur: Frage 1 mit 56 min vor dem Ablesen, damit die Schnittzeit erscheint; Kasten `#rechenwerte` mitgelesen) und `vergleich30.py` (Sollwerte aus `g3_rechnung.zustand`, je Zustand 12 bis 14 Größen als gerundeter Text gesucht: $\vartheta_1$, $\vartheta_2$, Δ, $Q_1$, $Q_2$, $Q_2 - Q_1$, $\vartheta_{1,0}$, *kA* auf vier Stellen, Schnitt oder „kein Schnitt bis zur Zugabe“, 30-min-Wert, Zeitkonstante, $\vartheta_\mathrm{2,K}$ bei der Zugabe; dazu Milchbeitrag, Trinkzeit und Zusatzzeile Becher kalt, wo sie gelten). Fehlerschwelle wie Runde 1 (Abschnitt 2.3).

**Ergebnis: 30 von 30 Zustände gleich**, dazu Z28b (Pappbecher) und Z01t (Trinkzeit Standard) gleich; keine Abweichung, auch keine von einer Einheit der letzten Stelle. Die Seite rechnet weiter mit dem ungerundeten $kA_0$ = 0,340246 W/K (30,19 °C und 35,96 °C bei Edelstahl).

## 3 Neue und geänderte Anzeigen

| Anzeige | Fall | Seite | eigene Werte | Urteil |
|:--|:--|:--|:--|:--|
| Zahlvergleich Start, Frage 1, V1, V2 | Standard | 3,85 K; etwa 56 min; 47,0 °C; etwa 100 min | 3,8532 K; 55,745 min; 47,003 °C; 99,54 min | stimmt |
| Auflösungen V3, V4, V5 (de, en) | wie Runde 1 | 3,08 / 3,85 K, 46,60 / 50,34 kJ; 2,98 K, höchstens 0,04 K; 63,5 / 48,8 °C, 127 min | wie Runde 1 | stimmt |
| Becher 3 und Unterschied | F1 (Kurslink aus Runde 1) | 32,74 °C; 1,57 K; *kA* 0,4371; 34,31 / 31,23 / 3,08; 46,17 / 49,90 kJ; Schnitt 55,6 min | 32,7364; 1,5731; 0,43713; 34,3095 / 31,2306 / 3,0789; 46,1709 / 49,9049; 55,58 | stimmt |
| Becher 3 bei Zugabe 30 min | F1 | 47,38 / 44,69 / 46,20 °C; 2,69 / 1,18 K | 47,3778 / 44,6919 / 46,1977; 2,6859 / 1,1801 | stimmt |
| Mischsprung Becher 3 (Pixel) | F1 | 34,15 → 32,73 °C bei *t* = 60 min (+5 px) | 34,1577 → 32,7364 | stimmt (Lage); Beschriftung G3-14 |
| Ansicht ln | F1 | 0,4470 W/K (12 Punkte); frei 0,4493 W/K | 0,44698; 0,44932 (14 Punkte) | stimmt |
| Wertetabelle | F1 | 13 Zeilen je 5 min, „60 nach der Milch“ 34,31 / 31,23, Messwerte | 0 Abweichungen | stimmt |
| Teilflächen Wärmestrom | F1; Standard; 120 min; 120 min mit 105 %; Becher 0,444 | 3,74 / −0,01 / 3,73; 3,70 / −0,01 / 3,69; 3,70 / −0,81 / 2,89; 2,86 / −0,41 / 2,44; 3,75 / −0,01 / 3,73 kJ | 3,7431 / −0,0091 / 3,7340; 3,6987 / −0,0083 / 3,6904; 3,6987 / −0,8055 / 2,8932; 2,8573 / −0,4136 / 2,4437; 3,7472 / −0,0133 / 3,7339 | stimmt; Text siehe G3-R2-01 |
| Trinkzeit | Standard, Becher, Deckel | 10,9 / 16,6; 12,4 / 16,6; 19,5 / 29,7 min | 10,904 / 16,604; 12,353 / 16,604; 19,471 / 29,650 | stimmt |
| Becher kalt | *kA* 0,444 und 0,3402 | siehe G3-03 | siehe G3-03 | stimmt |
| Vergleichslauf | Standard gemerkt, dann Deckel | 34,05 / 30,19 / 3,85; aktuell 44,66 / 41,15 / 3,51 | Z01, Z25 | stimmt |
| CSV | F1 (de), Standard (en), Zugabe 56, 120, 120 mit 105 %, 7,5 (gerechnet 8), Becher 0,444, Deckel | jede Minute beider Modellspalten und Zeile „nach der Milch“ | 0 Abweichungen in 8 Dateien | stimmt |

Messpunkte erscheinen erst nach Frage 2 (vor Frage 2 sechs Marken im Bild, nur Schnittkreis und Linienmarken; nach Frage 2 Kreise, Quadrate und Dreiecke an den Messwerten). Keine Konsolenfehler in allen Läufen.

## 4 Neue Befunde

| ID | Schwere | Befund | Beleg | Vorschlag | CONFIRMED/INFERRED |
|:--|:--|:--|:--|:--|:--|
| G3-R2-01 | low | Ansicht Wärmestrom: Liegt der Schnitt erst nach der Zugabe, sagen Beschreibung und Flächentext trotzdem „Bis zum Schnitt gibt Tasse 2 mehr Wärme ab (3,22 kJ), danach weniger (0,00 kJ)“ bzw. „vor dem Schnitt … nach dem Schnitt …“, während die Rechenwerte „kein Schnitt bis zur Zugabe“ zeigen. Betroffen sind gerade die Lehrfälle Zugabe 30 min, „Keramik mit Deckel“ (V2, Schnitt erst bei 99,5 min), Becher mit festem *kA* und Zugabe 7,5 min. Zahlen richtig (eigene 3,2158 kJ, 3,3613 kJ, Wechsel der Wärmeströme bei 55,7 bzw. 99,5 min). | `r2_csv.js` Fälle „tz30_4“, „vergleich“ (Deckel), „tz7_5“; `r2_check.py` | Ohne Schnitt vor der Zugabe nur „Tasse 2 gibt bis zur Zugabe durchweg mehr Wärme ab: 3,22 kJ (der Schnitt kommt erst nach der Zugabe)“ | CONFIRMED |

Zählung Runde 2: übernommen 13, davon behoben 10, teilweise 3 (G3-14, G3-18, G3-19), nicht behoben 0. Neue Befunde: blocker 0, high 0, medium 0, low 1.

## 5 Anhang: Skripte

Ordner `/tmp/claude-0/-home-user/8bff1287-c5bb-5641-9916-90393029086f/scratchpad/r2_G3/`:

- `g3_rechnung.py`, `g3_flaechen.py`, `g3_f_rechnung.py`, `g3_f_csvcheck.py`: aus Runde 1 kopiert, unverändert; `g3_ergebnis.json` neu erzeugt
- `g3_seite_r2.js`, `g3_seite_r2.json`, `g3_seite_r2.txt`: 30 Zustände in der Seite; `vergleich30.py`: automatischer Vergleich
- `g3_vertiefung_r2.js` (de, en): Fragen V1 bis V5, Ausgangslage, Auflösung mit Zahlvergleich
- `erkunde*.js`: Ablauf Start, Frage 1, Frage 2
- `r2_f1.js`, `r2_legende.js`, `r2_b3tz.js`: Kurslink F1, Frage 2, Diagrammelemente, Becher 3, Ansicht ln, Wertetabelle, Wärmestrom
- `r2_csv.js`, `r2_check.py`: CSV, Wertetabelle, Teilflächen, ln-Geraden, Becher kalt gegen eigene Rechnung
- `r2_rest.js`: Vergleichslauf, Zahlfeld, ungültige Einstellung, Fußnote, Kurslink in offener Seite, leeres Messblatt, Sprachwechsel
