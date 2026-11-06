# Gutachten G1, Runde 2: Studentin im dritten Semester

| | |
|:--|:--|
| Rolle | G1 „Studentin im dritten Semester“ (Maschinenbau, hat die Kaffee-Aufgabe im Tutorium gerechnet), Handy 390 × 844 hochkant, Deutsch |
| Datum | 06.11.2026 |
| Runde | 2 (Nachprüfung der eigenen Befunde aus Runde 1 und Suche nach Rückfällen) |
| Art der Prüfung | getrennte Rollenprüfung desselben Modells |
| Geprüfte Datei | `simulation/site/index.html`, SHA-256 `ea6d3ad224030ff9a783517b7c6af059c8bba48600c80c83819c41db85ea9c31` (mit `sha256sum` geprüft, stimmt) |
| Umgebung | Cloud-Container (Linux), Chromium über Playwright (`chromium.launch()` ohne Optionen), `viewport 390 × 844`, `isMobile`, `hasTouch`, `deviceScaleFactor 1`, Seite als `file://`; Bedienung mit `tap`, Texteingabe, Touch-Ziehen über CDP. Kein echtes Handy, keine Bildschirmtastatur, kein Bildschirmleser. |
| Belege | Skripte, Protokolle und Bildschirmfotos in `/tmp/claude-0/-home-user/8bff1287-c5bb-5641-9916-90393029086f/scratchpad/r2_G1/` (unten nur Dateiname, alle in diesem Ordner) |

Gelesen: eigenes Gutachten aus Runde 1, in `ZUSAMMENFUEHRUNG.md` nur die Zeilen G1-01 bis G1-19, `KONZEPT.md` (bekannt aus Runde 1). Nicht gelesen: Baubericht, Zwischenstand, Prototypen, Tests, andere Gutachten, Git-Protokoll. Quelltext nur per Textsuche an zwei Stellen (Reitertexte, G1-07 und G1-17).

## 1 Pflichtweg am Handy mit Messwerten (Weg A)

Messwerte wie in Runde 1 (Raum 21,5 °C, Milch 6 °C; Becher 1: 79,0 / 62,6 / 55,2 / 49,5 / 45,0 / 41,4 / 38,6 °C; Becher 2: 79,2 / 67,8 / 59,6 / 53,2 / 48,1 / 44,0 / 40,7 / nach der Milch 37,3 °C), als TL ins Messblatt getippt, „Kurswerte als Link teilen“ (`s02_tl.js`, Link in `02_link.txt`), dann als Studentin in einem frischen Browser geöffnet (`s03_pfad.js`, `s04_f1.js`, `s05_f2.js`).

**Alle Zeiten sind Expertenschätzungen aus meinem Durchgang, keine Messung mit Studierenden;** angenommen ist ein Paar an einem Handy.

| Schritt | Was ich tue und sehe | Zeit (Expertenschätzung) |
|:--|:--|:--|
| 0 Öffnen | Leiste „Kurswerte aus dem Link übernehmen?“, „Übernehmen“; Leiste wird zu „Kurswerte aus dem Link übernommen.“ Startdiagramm nur mit Achsen, Raumlinie, 80 °C, Platzhalter sauber umbrochen. | 0,5 min |
| 1 Start: vorhersagen | „Tasse 1“, „4 K“ getippt, Knopf wird sofort aktiv, kein Hänger mehr. | 1,5 min |
| 2 Start: erklären | Nach dem Festhalten steht das Diagramm mit beiden Kurven oben angeheftet im Bild, darunter ϑ₁ 34,05 °C, ϑ₂ 30,19 °C, Δ 3,85 K, darunter meine Vorhersage und „Erklärt den Unterschied mit *Q*₁ und *Q*₂.“ Die Säulen *Q*₁ 34,88 kJ, *Q*₂ 38,57 kJ liegen aber erst nach Frage-1-Karte und Regler (etwa 1,5 Bildschirme tiefer, `03_04_scroll_1200.png`). Auflösung: „Auswahl passt“, „Eure Zahl: 4 K · Modell: 3,85 K (Standardwerte)“. | 2,0 min |
| 3 Frage 1: vorhersagen | „40 min“ getippt, angenommen. Kein Schnittkreis, keine Schnittzeit vor dem Festhalten (Rechenwerte: „Schnitt der Kurven: nach eurer Vorhersage zu Frage 1“). | 1,5 min |
| 4 Frage 1: prüfen | Nach dem Festhalten: Diagramm (mit senkrechter Linie „Eure Vorhersage: 40 min“ und Schnittkreis), Kernzahlen, „Eure Vorhersage: 40 min“, Auftrag „Stimmt eure Vorhersage? Erklärt zu zweit, warum.“ und Regler zugleich im Bild (`04_03_regler_sicht.png`). Regler per Tippen, Ziehen, Plus/Minus und Zahlenfeld bedienbar; Höchstwert 3,86 K von 53 bis 59 min schnell gefunden. Auflösung mit „Eure Zahl: 40 min · Modell: etwa 56 min“. | 2,0 min |
| 5 Frage 2: vorhersagen | Diagramm zeigt keine Messpunkte, keine Legende „Messpunkte“, die Wertetabelle nur Modellwerte. „über den Kurven“ gewählt, festgehalten. | 1,0 min |
| 6 Frage 2: prüfen | Kurven springen auf die Kurswerte (Raum 21,5 °C, *kA* 0,4002 W/K, ϑ₁,₀ 71,85 °C; 36,85 / 33,80 °C, 3,05 K; *Q* 42,45 / 46,15 kJ; „kein Schnitt bis zur Zugabe“), jetzt mit Messpunkten und Legende. Lage beschreiben, Ursache und Prüfmessung nennen, Auflösung lesen; „Geschafft. Weiter geht es in der Vertiefung.“ | 2,5 min |
| **Summe Weg A** | | **etwa 11 min** (Runde 1: 12,5 bis 14 min) |

Gegenprobe Weg B (ohne Link, `s06_misc.js`): Frage 2 nach der Auswahl mit grauem Knopf und direktem Hinweis „Erst Kurswerte laden … sonst Frage 2 überspringen.“, Knopf „Frage 2 überspringen (Versuch ausgefallen)“ gleich darunter; Link danach im selben Tab eingefügt: Rückfrage erscheint, Übernahme klappt, Auswahl bleibt, Knopf wird aktiv, Messpunkte weiter verborgen (`s07_leak.js`). Auch Eintippen ins Messblatt während Frage 2 zeigt keine Punkte vor dem Festhalten.

Nachgerechnet (Skript `nachrechnung.py`, Formeln wie Teil a bis e und g): Standardlage 34,05 / 30,19 °C, 3,85 K, *Q* 34,88 / 38,57 kJ, Schnitt 55,7 min, Regler 30 / 50 / 53 / 56 / 59 / 60 / 70 / 120 / 180 min ergibt 3,36 / 3,84 / 3,86 / 3,86 / 3,86 / 3,85 / 3,78 / 3,02 / 2,35 K. Kurswerte von Hand: *C* mit Becher = 0,4002 · 600 / ln(57,7/46,3) ≈ 1091 J/K; Mischung Tasse 1 (1091 · 79,2 + 121,7 · 6) / 1212,7 = 71,85 °C; Tasse 2 vor der Milch 21,5 + 57,7 · e^(−1,3206) = 36,90 °C, gemischt 33,80 °C; *Q*₁ = 1212,7 · 35,00 = 42,45 kJ, *Q*₂ = 1091 · 42,30 = 46,15 kJ. Alle angezeigten Zahlen stimmen, keine falsche Zahl gefunden.

## 2 Nachprüfung

| ID | Entscheidung | Ergebnis am neuen Stand | Beleg |
|:--|:--|:--|:--|
| G1-01 | übernehmen | **behoben.** Vor dem Festhalten von Frage 2 keine Messpunkte, keine Legende, keine Messwerte in der Wertetabelle; geprüft mit Link beim Öffnen, mit Link im selben Tab während Frage 2 und mit Eintippen ins Messblatt während Frage 2. Nach dem Festhalten erscheinen 15 Punkte und die Legende. | `s05.log` („legende-mess vor F2 versteckt“, Tabelle nur Modellwerte), `s07.log`, `04_08_f2_scroll_400.png`, `05_03_f2_diagramm_karte.png` |
| G1-02 | übernehmen | **behoben.** Am Handy Reihenfolge Diagramm (angeheftet), Frage, Regler; beim Bedienen des Reglers sind Diagramm mit Vorhersagelinie, Kernzahlen, eigene Vorhersage, Auftrag und Regler gleichzeitig sichtbar. Schalter „Diagramm lösen“ / „Diagramm oben anheften“ vorhanden, wirkt und bleibt nach Neuladen erhalten. Rest: Der eigentliche Fragetext („Warum wird der Unterschied … wieder kleiner?“) liegt beim Schieben meist unter dem angehefteten Diagramm; der Kurzauftrag in der Karte reicht mir aber. | `04_03_regler_sicht.png`, `06_03_tz180.png`, `s09_loesen.js` |
| G1-03 | übernehmen | **teilweise.** Die Kurven stehen nach dem Festhalten sofort im Bild (behoben). Die Säulen *Q*₁ / *Q*₂, mit denen der Auftrag „Erklärt den Unterschied mit *Q*₁ und *Q*₂“ zu lösen ist, liegen weiterhin unter Frage-1-Karte, Regler, Bildunterschrift und zwei Knöpfen (Energie-Kasten bei 1753 px, bei angeheftetem Diagramm erst nach etwa 1200 px Scrollen sichtbar); Frage 1 folgt direkt unter der Startkarte. | `03_03_start_fest.png`, `03_04_scroll_1200.png`, `s03.log` |
| G1-04 | übernehmen | **behoben.** „Auswahl passt“ und getrennt „Eure Zahl: 10 K · Modell: 3,85 K (Standardwerte)“; negative Zahl wird nicht mehr angenommen. | `s06.log` |
| G1-05 | übernehmen | **teilweise.** „4 K“, „4K“, „ca. 4“, „~4“, „etwa 4“, „4,5 K“, „40 min“, „40min“, „ca. 40“ gelten als Zahl; sonst Hinweis am Feld mit `aria-invalid` und `aria-describedby`. Offen: Frage 1 nimmt weiter „-5“, „0“ und „1000“ min an (Regler 1 bis 180 min); „-4“ und „4,“ werden abgelehnt mit „Bitte nur eine Zahl, zum Beispiel 4 oder 3,5.“, was bei „-4“ nicht die Ursache trifft. Klein, kein Hänger mehr im Pflichtweg. | `s06.log` |
| G1-06 | übernehmen | **behoben.** Direkt am gesperrten Knopf: „Erst Kurswerte laden (Link der Tutoriumsleitung) oder ins Messblatt eintragen; sonst Frage 2 überspringen.“, Überspringen-Knopf gleich darunter. | `06_04_f2_ohne_werte.png`, `s06.log` |
| G1-07 | übernehmen | **behoben (Anzeige).** Schnittkreis, Beschriftung „Schnitt“ und Schnittzeit erscheinen erst nach der Vorhersage zu Frage 1. Die Erklärsätze in den Reitern („Er wächst, solange Tasse 2 mehr Wärme abgibt, und sinkt danach.“, „Links davon …“) stehen weiter; als Frage an die TL offen, Begründung (Konzepttexte A.2, A.8) nachvollziehbar. | `s03.log` („Schnitt der Kurven: nach eurer Vorhersage zu Frage 1“), `04_03_regler_sicht.png`, `08_code.txt` |
| G1-08 | übernehmen | **behoben.** Sichtbarer Titel „Energie bis zur Zugabe: an den Raum abgegebene Wärme“. | `03_04_scroll_1200.png` |
| G1-09 | offen | Begründung nachvollziehbar: Das Blatt vom 31.10. ist fertig und soll im Auftrag nicht geändert werden, die 60 min sind Entscheidung der TL (E8). Die Entscheidung, ob Blatt oder Seite einen Hinweis bekommt, liegt richtig bei der TL. | Zeile G1-09 in `ZUSAMMENFUEHRUNG.md` |
| G1-10 | übernehmen | **behoben.** Link im schon offenen Tab (Hash geändert) zeigt die Rückfrage „Kurswerte aus dem Link übernehmen? Eure bisherigen Kurswerte werden ersetzt.“; Übernahme mitten in Frage 2 klappt, Auswahl bleibt erhalten. | `06_05_hashchange.png`, `s06.log` |
| G1-11 | übernehmen | **behoben.** Kasten im Diagramm zeigt die Vorhersage der aktuellen Frage („Eure Vorhersage: 40 min“, „über den Kurven“) bei jeder Zugabezeit bis 180 min, in Frage 1 mit senkrechter Linie bei 40 min. Rest siehe G1-R2-01 (andere Stellen zeigen weiter die Startvorhersage). | `04_03_regler_sicht.png`, `06_03_tz180.png`, `05_03_f2_diagramm_karte.png` |
| G1-12 | übernehmen | **behoben.** Einleitung des Messblatts: „Becher 1 hat die Milch schon bei 0 min (Zeile 0 nach dem Umrühren) und keine Zeile „60 nach der Milch““; das Feld ist gesperrt. | `01_start.txt`, `02a_tl_messblatt.png` |
| G1-13 | übernehmen | **behoben.** Platzhalter „Achsen ohne Kurven: Die Kurven erscheinen nach eurer Vorhersage.“ zweizeilig, mittig, nichts abgeschnitten. | `06_01_start_diagramm.png` |
| G1-14 | übernehmen | **teilweise.** Punkt bleibt an der Formel („*Q*₂.“), behoben; Achse oben (90) nicht mehr angeschnitten. Einheiten im Fließtext und in den Rechenwerten stehen weiter als kleine Brüche („J/K“ 11,75 px, „W/K“ 11,16 px hoch gestapelt), am Handy schwer lesbar. | `04_01_f1_eingabe.png` (957,7 J/K), `s08_tabs.js` (Ausgabe `mfrac`) |
| G1-15 | übernehmen | **behoben.** „ohne Vorhersage aufdecken“ fragt nach: „Ohne eigene Vorhersage aufdecken? Die Auflösung ist dann sofort sichtbar.“; „Nein“ deckt nichts auf. | `06_02_ohne_rueckfrage.png`, `s06.log` |
| G1-16 | offen | Begründung nachvollziehbar: Der Satz nennt den Mechanismus, kein Ergebnis, und steht so im Konzept (A.5); Entscheidung der TL. Ich würde ihn weiter erst nach der Startvorhersage zeigen, halte es aber nicht für zwingend. | Zeile G1-16 |
| G1-17 | übernehmen | **behoben.** Quelltext enthält „Versuch, Becher 3“, kein „Zusatzfrage“ mehr. | Textsuche in `index.html` |
| G1-18 | offen | Begründung nachvollziehbar (Fragetext aus Konzept 6.1, Empfehlung an die TL liegt vor). Am neuen Stand steht der Satz unverändert, auch nach dem Festhalten. | `s05.log` (Frage-2-Text) |
| G1-19 | übernehmen | **behoben** (soweit ohne Bildschirmleser prüfbar). Regler hat `aria-valuetext` „56 min“; nach dem Festhalten Ansage „Vorhersage festgehalten, Kurven und Rechenwerte sind sichtbar. Tasse 1 34,05 °C, Tasse 2 30,19 °C, Unterschied 3,85 K.“; beim Schieben Ansage der Kernzahlen. | `s04.log`, `s03.log` |

## 3 Neue Befunde (Rückfälle und Neues)

Keine Rückfälle bei „Vorhersage vor Ergebnis“ (Start, Frage 1, Frage 2 dicht), bei der Reihenfolge Diagramm, Frage, Regler und bei der Bedienung des Reglers am Handy (Tippen, Ziehen, Plus/Minus, Zahlenfeld, Pfeiltasten). Kein waagerechtes Scrollen, keine Fehlermeldungen in der Konsole.

| ID | Schwere | Befund | Beleg | Vorschlag | CONFIRMED/INFERRED |
|:--|:--|:--|:--|:--|:--|
| G1-R2-01 | low | Neben dem behobenen Kasten im Diagramm zeigen zwei Stellen weiter nur die Startvorhersage: die grüne Zeile unter dem Regler („Eure Vorhersage: Tasse 1 (Milch sofort), etwa 4 K“) während der Eingabe zu Frage 1 und Frage 2, und der Eintrag „Eure Vorhersage“ in den Rechenwerten auch nach dem Festhalten von Frage 2 (neben Kurswerten). Beim Vorhersagen zu Frage 2 wirkt die Zeile, als sei schon etwas festgehalten. | `04_08_f2_scroll_800.png`, `s05.log` (RECHENWERTE), `s09_loesen.js` | Zeile und Rechenwert an die aktuelle Frage koppeln oder vor deren Festhalten ausblenden. | CONFIRMED |
| G1-R2-02 | low | „Ausgangslage“ in Frage 2 passt nicht zum Zustand. Mit geladenem Link steht vor dem Festhalten „Kurswerte übernommen (*kA* aus 0 und 10 min, Becher an)“, Diagramm und Kernzahlen stehen aber noch auf Standardwerten mit Zugabe nach 56 min aus Frage 1 (35,30 / 31,43 °C). Werden die Werte während Frage 2 ins Messblatt getippt, steht oben „Kurswerte geladen: 15 Messwerte.“, darunter weiter „Ausgangslage: Kurswerte übernehmen, sobald sie geladen sind“. | `04_07_f2.png`, `04_08_f2_scroll_400.png`, `s07.log` (F2 karte) | Vor dem Festhalten einheitlich „Ausgangslage beim Prüfen: Kurswerte (*kA* aus 0 und 10 min, Becher an)“; Text beim Laden aus dem Messblatt nachziehen. | CONFIRMED |
| G1-R2-03 | low | Bei später Zugabe (180 min) überlagern sich Beschriftungen: „Schnitt“ steht auf „Raum 20,0 °C“, die senkrechte Vorhersagelinie läuft durch „Tasse 1: Milch sofort“. Lesbar, aber unruhig. | `06_03_tz180.png` | Beschriftung „Schnitt“ oberhalb des Kreises setzen bzw. Kurvennamen bei Kollision verschieben. | CONFIRMED |

## 4 Kurz

Von 16 übernommenen Befunden: 13 behoben, 3 teilweise (G1-03 *Q*-Säulen weit unten, G1-05 Grenzen in Frage 1, G1-14 Einheiten als kleine Brüche), keiner nicht behoben. Begründungen zu den offenen G1-09, G1-16, G1-18 (und dem offenen Textteil von G1-07) nachvollziehbar. Neue Befunde: 0 blocker, 0 high, 0 medium, 3 low. Pflichtweg mit Messwerten nach meiner Schätzung etwa 11 min statt 12,5 bis 14 min.
