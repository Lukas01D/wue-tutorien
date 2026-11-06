# Gutachten G7: Tutorin im Hörsaal, Runde 3

| Angabe | Wert |
|:--|:--|
| Rolle | G7 „Tutorin im Hörsaal“ (Beamer, Kurswerte, Zurücksetzen, Ersatz ohne Netz, Zeitplan) |
| Datum | 06.11.2026 |
| Runde | 3 (letzte Runde; Nachprüfung der offenen Punkte aus `G7_Tutorin_R2.md`, Einsatzblatt, Rückfälle) |
| Art | getrennte Rollenprüfung desselben Modells |
| Geprüfte Datei | `simulation/site/index.html`, 399 063 Bytes |
| SHA-256 | `1d90ce2f84349754592a5dd572a760a5d212cd3383bcafbeb1cceaf06e07292b` (vor und nach der Prüfung mit `sha256sum` geprüft, stimmt) |
| Weitere Grundlagen | `simulation/EINSATZ_TUTORIUM.md` (Stand 05.11.2026); in `ZUSAMMENFUEHRUNG.md` nur die Zeilen G7-01 bis G7-15 und G7-R2-01 bis G7-R2-08; Blatt vom 31.10.2026 wie in Runde 2 |
| Umgebung | Chromium (Playwright, `chromium.launch()` ohne Optionen), `file://` und lokaler Server `http://127.0.0.1:8765/` als Ersatz für die veröffentlichte Adresse. Beamer 1280 × 720 und 1920 × 1080 (100 %), Zoom nachgestellt als kleineres Fenster mit deviceScaleFactor (125 %, 150 %). Handy 390 × 844. Kein echter Hörsaal, kein echtes Handy. |
| Skripte und Bilder | `/tmp/claude-0/-home-user/8bff1287-c5bb-5641-9916-90393029086f/scratchpad/r3_G247/g7/` (s4, s6, s8 der Runde 2 erneut, s6 mit 16 s Wartezeit; neu u1.js, u2.js; Bilder `bm_*.png`, `u1_*.png`) |

Kurswerte wie in Runde 1 und 2 (erfunden): Becher 1 68,5 bis 38,5 °C, Becher 2 76,5 bis 39,0 °C und 33,5 °C nach der Milch, Becher 3 76,0 bis 38,5 °C und 35,5 °C, Raum 21,5 °C, Milch 7 °C (23 Messwerte).

## 1 Nachprüfung

| ID | Ergebnis am neuen Stand | Beleg |
|:--|:--|:--|
| G7-03 | **teilweise.** Nach dem Festhalten ist der Fragetext eingeklappt („Frage zeigen“). Frageleiste oben am Rand, gemessen Frageleiste + Diagramm + Regler: **1920 × 1080 (100 %)** Start 454 + 437 + 95 = 986, Frage 1 328 + 462 + 73 = 863, Frage 2 425 + 437 + 73 = 935 px: passt (M-6 erfüllt). **1280 × 720 (100 %)** Start 909, Frage 1 328 + 360 + 74 = 762, Frage 2 858 px bei 720 px Höhe: In Frage 1 ist das Diagramm ganz zu sehen, vom Regler nur die Beschriftung, der Reglerbereich endet 42 px unter der Kante, der Schieber ist nicht zu sehen. Die eingeklappte Leiste ist noch 328 px hoch, weil „Zurück / Weiter“, „Eure Vorhersage“, Auftrag und „Auflösung zeigen“ je eine eigene Zeile haben. | s4.js (Rechtecke), `bm_1280_100_f1.png`, `bm_1920_100_f2.png`. Vorschlag: „Zurück / Weiter“ in die Zeile von Titel oder Ausgangslage, „Eure Vorhersage“ und Auftrag in eine Zeile; das spart rund 60 bis 90 px und reicht für 1280 × 720 in Frage 1 |
| G7-05 | **teilweise, unverändert.** Schrift unverändert (Fließtext 16 px, Achsen 12 px, Frageleiste nach dem Festhalten 13,6 px); keine Projektionsansicht. Das Einsatzblatt beschreibt die Abwägung jetzt richtig (zuerst 100 %, bei Bedarf 110 bis 125 % und scrollen, „im echten Hörsaal prüfen“). Lesbarkeit aus der letzten Reihe offen. | s4.js (`fs`, `axfs`); Einsatzblatt 5 |
| G7-06 | **behoben.** kJ-Werte der Energiesäulen: 1280 × 720 bei 100 % 15,9 px; bei 125 % (1024 CSS-px) 15,8 Bildpunkte, bei 150 % (853 CSS-px) 18,9 Bildpunkte. Der Zoom verschlechtert sie nicht mehr. | s8.js |
| G7-09 | **behoben mit offenem Teil (K-2).** Warnung bei `file:` vorhanden. Einen QR-Code erzeugt die Seite weiter nicht; das Einsatzblatt 6.3 sagt jetzt „mit einem QR-Werkzeug auf dem Laptop oder Handy erzeugen, oder den Link in den Kurs-Chat stellen“, nennt aber kein Werkzeug und keine Probe (siehe G7-R2-04). | u2.js; Einsatzblatt 6.3 |
| G7-14 | **teilweise.** Behoben: Rückfrage neben dem Knopf, „Abbrechen“ setzt Fokus und Scrollstelle zurück (1968 → 1968), Meldung „Kurswerte aus dem Link übernommen.“ nach 16 s verschwunden, im frischen Kontext ohne Kurswerte nur „Kurswerte aus dem Link übernehmen?“ ohne „… werden ersetzt“. Geblieben: Nach „Für die nächste Gruppe zurücksetzen“ bleibt die Sprache (Englisch), und das Einsatzblatt sagt es nicht (G7-R2-06 b). | s6.js (`html lang en` nach dem Zurücksetzen), u1.js („Banner frisch“) |
| G7-R2-01 | **teilweise** (wie G7-03): 1920 × 1080 erfüllt, 1280 × 720 nicht. Die falsche Zusage im Einsatzblatt ist weg („dann passen Frageleiste und Diagramm noch gut“ gestrichen). | s4.js; Einsatzblatt 5 |
| G7-R2-02 | **behoben** (siehe G7-06). | s8.js |
| G7-R2-03 | **behoben.** Einsatzblatt 2 nennt die Abweichung: „Das Aufgabenblatt vom 31.10. sieht den Versuch bis 40 min und *kA* ohne Becher vor; die Seite folgt … E8 … Vor der Sitzung entscheiden, welcher Ablauf gilt“. Kleinigkeit: der Kasten hängt an Punkt 3 (QR-Code der Kurzkarte), nicht an Punkt 5 (Versuch vorbereiten), und Punkt 5 sowie Abschnitt 4 sprechen weiter nur von 60 min. | Einsatzblatt 2.3, 2.5, 4 |
| G7-R2-04 | **teilweise.** Behoben: (a) 6.3 „Den Link auf der veröffentlichten Seite erzeugen, nicht in der Offline-Datei“; (d) Minute 75 „einen QR-Code mit dem Kurslink zeigen“. Offen: (b) kein konkretes QR-Werkzeug, keine Probe vorab; (c) Tabelle 3, Minute 65 bis 75 sagt weiter „Link in einen QR-Code **oder an die Tafel**“, während 6.3 sagt „zum Abschreiben ist er mit etwa 160 Zeichen zu lang“; die Seite beschriftet ihn weiter mit „Link zum Abschreiben:“ (lokal 156 Zeichen, veröffentlicht länger). | u2.js („Teilen-Bereich“); Einsatzblatt 3, 6.2, 6.3 |
| G7-R2-05 | **teilweise.** 6.1 richtig („von Anfang an sichtbar, ohne etwas aufzudecken“). Abschnitt 5, letzter Punkt, steht unverändert: „Diagramm groß zeigen: Bei schmalem Fenster rückt es nach oben und bleibt beim Scrollen angeheftet (Hochformat).“ Am Beamer ist das Diagramm bei allen sechs Stufen `position: relative`, also nicht angeheftet; der Punkt hilft der TL am Beamer nicht. | s4.js (`dia … "relative"` bei allen Stufen); Einsatzblatt 5 |
| G7-R2-06 | **teilweise.** (a) behoben: 2.1 „nach einer Probe mit Messwerten im Messblatt ‚Kurswerte löschen‘“. (b) offen: 3 sagt weiter nur „Antworten, Einstellungen und Ansicht gehen zurück“; die Sprache bleibt (s6.js). (c) offen: Liste für Minute 65 bis 75 ohne die Häkchen „Becher 3 zeigen“ und „mit Deckel gemessen“. | s6.js; Einsatzblatt 2.1, 3 |
| G7-R2-07 | **behoben.** Meldung nach 16 s nicht mehr sichtbar; nach dem Zurücksetzen nicht sichtbar. | s6.js |
| G7-R2-08 | **offen (Frage an die TL), unverändert.** Mit Kurslink aus Minute 75 steht in Frage 2 vor dem Festhalten „Prüft dann: Ladet die Messwerte eures Kurses … und übernehmt die Einstellungen“ direkt über „Kurswerte geladen: 23 Messwerte. Ausgangslage: Kurswerte, übernommen beim Prüfen“. Das Einsatzblatt wiederholt es (Tabelle 3, Minute 81 bis 85: „Kurswerte über den Link laden“), obwohl sie seit Minute 75 geladen sind. | u1.js („F2 Leiste“); Einsatzblatt 3 |

**Bilanz:** behoben 4 (G7-06, G7-R2-02, G7-R2-03, G7-R2-07), behoben mit offenem Teil 1 (G7-09, K-2), teilweise 7 (G7-03, 05, 14, G7-R2-01, R2-04, R2-05, R2-06), nicht behoben 0, offen bei der TL 1 (G7-R2-08).

## 2 Einsatzblatt gegen die Seite (Durchgang)

Richtig und mit der Seite übereinstimmend: Ablauf und Minuten (Abschnitt 3), ein QR-Code mit dem Kurslink in Minute 75, Rückfrage beim Kurslink (im frischen Kontext ohne „… werden ersetzt“, sonst mit), „Frage 2 überspringen (Versuch ausgefallen)“, Zurücksetzen behält die Kurswerte, beschädigter Link nennt den Grund, Messblatt vor der ersten Vorhersage eingebbar, „Kurswerte löschen“ nach der Probe, Zahlen der Abschnitte 8 und 9 (Start 34,05 / 30,19 °C, 3,85 K, 3,69 kJ; Frage 1 56 min, 3,86 K, 1,91 K; V1 47,0 / 60,9 / 37,3 °C; V2 3,86 K, 100 min, 94 bis 106 min, 3,51 K; V3 3,08 K, 46,60 / 50,34 kJ; V4 2,98 K, 0,04 K; V5 63,5 / 48,8 °C, 127 min) gleich den Anzeigen der Seite. `simulation/site/Kaffee_Simulation.html` ist bytegleich mit dem geprüften Stand.

Abweichungen: siehe G7-R2-03 (Kleinigkeit), G7-R2-04 (b, c), G7-R2-05 (Abschnitt 5), G7-R2-06 (b, c), G7-R2-08, G7-R3-02.

## 3 Neue Befunde

| ID | Schwere | Befund | Beleg | Vorschlag | CONFIRMED/INFERRED |
|:--|:--|:--|:--|:--|:--|
| G7-R3-01 | low | **Unerklärtes Dreieck ab dem Start, wenn der Kurslink Becher 3 enthält.** Im Sitzungsablauf öffnen alle Paare in Minute 75 den Kurslink vor der Startfrage. Enthält er Becher 3 (Häkchen „Becher 3 zeigen“), zeigt das Diagramm ab dem Start neben den beiden hohlen Endpunkten der Tassen ein hohles blaues Dreieck bei 60 min (Modellwert Becher 3, 32,10 °C) ohne Legende; die Legende „Messpunkte: … Becher 3“ erscheint erst nach Frage 2. Am Beamer und am Handy liegt es zwischen den Endpunkten, die das Paar im Start vergleichen soll. Es verrät nichts zu Start oder Frage 1, kostet aber Erklärzeit („Was ist das blaue Dreieck?“). | u1.js („Start fest“: `▵hohl@728,227:#3d70a3` neben den Kreisen; Beschreibung „Becher 3 nach der Milch 32,10 °C“), `bm_1280_100_f1.png`, `t1_falsch_01_start_fest.png` (Rolle G4) | Modellpunkt Becher 3 erst zusammen mit den Messpunkten nach der Vorhersage zu Frage 2 zeigen; oder, wenn er früher bleiben soll, im Diagramm beschriften („Becher 3“). | CONFIRMED (Anzeige); INFERRED (Rückfragen in der Sitzung) |
| G7-R3-02 | low | **Gleichnamige alte Datei im Übergabeordner.** Das Einsatzblatt nennt für den Beamer-Laptop und den USB-Stick nur den Dateinamen `Kaffee_Simulation.html` (Abschnitt 1 mit Bezug auf `simulation/site/`, Abschnitt 2.1 ohne Pfad). Im Repository liegen unter `ergebnisse/kaffee/fertig/` und `ergebnisse/kaffee/simulation/` zwei Dateien gleichen Namens mit 29 688 Bytes, Stand 04.11.2026, SHA-256 `43f33314…59d5`: ein anderes, älteres Werkzeug ohne die Sperren dieses Stands (`messFrei` kommt nicht vor). Greift die TL im Übergabeordner `fertig/` zu, zeigt sie am Beamer die falsche Seite. | `sha256sum` der drei Dateien; `ls -l`; `grep -c messFrei` (0 gegen 5) | Im Einsatzblatt 2.1 den vollen Pfad nennen (`simulation/site/Kaffee_Simulation.html`); bei der Übergabe die alte Datei ersetzen oder umbenennen. | CONFIRMED (Dateien); INFERRED (Verwechslung) |

**Zählung neue Befunde:** blocker 0, high 0, medium 0, low 2.

## 4 Rückfälle

Keine gefunden. Geprüft: Kurslink im frischen Kontext vor der Startfrage (Rückfrage, Übernahme, keine Messpunkte und keine Legende in Start, Frage 1 und Frage 2 vor der Vorhersage; danach Punkte, Legende „Becher 1 · Becher 2 · Becher 3“, Rechenwerte 36,65 / 33,77 / 35,23 °C, 2,87 K, *Q*₂ − *Q*₁ = 43,08 − 39,60 = 3,48 kJ), Zurücksetzen mit Abbrechen und Bestätigen, Meldung nach 16 s weg, kein waagerechtes Scrollen bei allen sechs Beamer-Stufen, keine Fehler in der Konsole.

## 5 Offene Nachweise

- Echter Hörsaal: Lesbarkeit aus der letzten Reihe bei 100 % und 125 %.
- QR-Code: Werkzeug, Dauer, Scannen auf iPhone und Android.
- Stoppuhr für den Pflichtweg mit zwei Studierenden (Schätzung aus Runde 2: 10 bis 13 min).
- Kurslink auf der wirklich veröffentlichten Adresse.
