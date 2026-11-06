# Gutachten G10: neue Studentin (Handy 360 × 640, Englisch, dann Deutsch)

| | |
|:--|:--|
| Rolle | G10 „neue Studentin“, 3. Semester, Kaffee-Aufgabe gerechnet, Seite zum ersten Mal, zu zweit an einem Handy |
| Datum | 06.11.2026 |
| Runde | 3 |
| Art | getrennte Rollenprüfung desselben Modells (eine unabhängige Prüfung mit einem anderen Modell folgt) |
| Gegenstand | `simulation/site/index.html`, SHA-256 `1d90ce2f84349754592a5dd572a760a5d212cd3383bcafbeb1cceaf06e07292b` (mit `sha256sum` geprüft, stimmt), Fuß: „Stand 2026-11-05 · Version 2c5665e215“ |
| Umgebung | Node 22, Playwright, Chromium headless (`chromium.launch()` ohne Optionen), Viewport 360 × 640, `isMobile`, `hasTouch`, Bedienung mit `tap`; Start über `?lang=en`; Kurslink als Fragment im schon offenen Tab (`location.hash`) erst bei Frage 2; Bildschirmtastatur nachgestellt mit Viewport 360 × 360 |
| Grundlage | `simulation/KONZEPT.md` (Abschnitte 2, 3, 5.2, 6, 9.4, 9.7), Aufgabenblatt `Kaffee_Aufgabe_Tutorium5_2026-10-31.pdf` |

Zeiten sind Expertenschätzungen für ein Paar, das die Aufgabe gerechnet hat, nicht gemessen.

## Ablaufbericht

### 1 Öffnen auf Englisch (etwa 1,0 min)

`?lang=en` wirkt: `lang="en"`, alle Texte englisch, kein waagerechtes Scrollen (scrollWidth 360). Oben steht sofort die Startkarte „Predict first“ mit drei großen Auswahlfeldern, Zahlfeld in K und freiwilliger Begründung. Darunter Achsen mit Raumlinie 20,0 °C und Startpunkt 80 °C, im Diagramm der Hinweis „Axes without curves: the curves appear after your prediction.“

**Prüfung auf Vorabverrat (vor der Startvorhersage):** sichtbarer Text, Ansage (`aria-live`: nur „Answer the start question first.“), „Values as a table“ („appears after your prediction“), Knöpfe „Default values“ und „As in the experiment“ (nur Ansage der Ausgangslage), Reiter „Model“ (nur „Physical problem“ offen, Rest „appears once you have locked in your prediction“), „How the code calculates“ (gesperrt), Rechenwerte und Energiesäulen („appears after your prediction“), CSV-Download (nur Kopfzeile und leere Zeilen), Regler gesperrt, SVG-Beschriftungen. **Nirgends eine Ergebnistemperatur, kein Unterschied, keine Wärme, keine Aussage „Tasse 1 ist wärmer“.** Auch ein Kurslink, der vor der Startfrage geöffnet wird, zeigt keine Messpunkte. Der Text unter „Physical problem“ nennt nur das Modell („the warmer the contents … the more heat they release“), das ist Aufgabenstoff, kein Ergebnis.

### 2 Startfrage auf Englisch (etwa 3,5 min: 2,0 Vorhersage und Einigung, 1,5 Erklärung mit Q₁ und Q₂)

Wir wählen „Cup 1 (milk right away)“, „5“ K, Begründung. „Lock in your prediction and show the curves“ zeigt sofort Kurven, Kernzahlen ϑ₁ 34,05 °C, ϑ₂ 30,19 °C, Δ 3,85 K, Energiesäulen 34,88 und 38,57 kJ (+3,69 kJ) und den Erklärauftrag „Explain the difference using Q₁ and Q₂“. „Show explanation“ zeigt „choice matches“, „Your number: 5 K · model: 3.85 K“ und die Auflösung mit 3,69 kJ / 957,7 J/K = 3,85 K. Nachgerechnet: kA = 836 J/K / 600 s · ln(60/47) = 0,3402 W/K, ϑ₁,₀ = 70,47 °C, ϑ₁ = 34,05 °C, schwarzer Kaffee 33,86 °C, ϑ₂ = 30,19 °C; alles stimmt mit dem Blatt (Teil a, c, d, e).

Diagramm und Kernzahlen heften sich an (Halter 246 px hoch, sticky); darunter bleiben bei 640 px etwa 390 px Arbeitsfläche. Mit Bildschirmtastatur (360 × 360) löst sich die Heftung, das Eingabefeld bleibt sichtbar.

### 3 Wechsel auf Deutsch (etwa 0,5 min)

„EN ↔ DE“ schaltet alles um, `lang="de"`, Vorhersage, Begründung und geöffnete Auflösung bleiben erhalten, Zahlen mit Komma. Der Parameter `?lang=en` verschwindet aus der Adresse; nach Neuladen bleibt Deutsch und der ganze Stand (auch Kurswerte) erhalten. Kein Hänger.

### 4 Frage 1 Zeitpunkt (etwa 3,5 min: 1,0 Vorhersage, 1,5 Regler, 1,0 Auflösung)

Die Karte geht nach der Startfrage direkt zu „Frage 1 von 2 · Zeitpunkt“; Text wie Konzept 6.1. Vor der Vorhersage ist der Regler gesperrt (englisch gesehen: „Lock in your prediction for question 1 first.“), der Rechenwert „Schnitt der Kurven“ ist verdeckt. Die beiden Kurven kreuzen sich im Diagramm kurz vor 60 min; das ist sichtbar, aber nicht markiert und gehört zum Bild (kein Befund).

Wir sagen 30 min voraus. Nach „Vorhersage festhalten, dann prüfen“ klappt die Frage zu („Frage zeigen“); die Karte sagt nur noch „Stimmt eure Vorhersage? Erklärt zu zweit, warum.“ mit „Auflösung zeigen“ direkt darunter. **Hier hänge ich kurz:** Der Auftrag, den Regler zu verschieben, und die Frage „Warum wird der Unterschied bei späterer Zugabe wieder kleiner?“ sind weg (G10-03). Mit Regler und Zahlenfeld (Komma geht, 56,5 wird 57; 0 und 500 ergeben „Bitte einen Wert von 1 bis 180 min eingeben.“): 30 min 3,36 K, 45 min 3,79 K, 53/56/59 min 3,86 K, 60 min 3,85 K, 90 min 3,50 K; Schnitt nach 55,7 min. Stimmt mit Konzept 6.1. Die Ansage wird verzögert aktualisiert (nach etwa 1 s), nicht bei jedem Schritt; gut für Bildschirmleser.

### 5 Frage 2 Versuch, Kurslink im offenen Tab (etwa 5,0 min: 1,0 Link holen und bestätigen, 1,0 Vorhersage, 1,5 Punkte lesen, 1,5 Auflösung, Ursache und Messung nennen)

Die Karte sagt „Noch keine Kurswerte …“; die Vorhersage lässt sich erst nach dem Laden festhalten („Erst Kurswerte laden … sonst Frage 2 überspringen.“). Das widerspricht der Reihenfolge im Kartentext („Notiere zuerst … Prüft dann: Ladet …“) leicht, verrät aber nichts (G10-05).

Link als Fragment im offenen Tab: Banner oben „Kurswerte aus dem Link übernehmen?“ mit „Übernehmen“ / „Nicht übernehmen“ (bei schon gefüllter Tabelle zusätzlich „Eure bisherigen Kurswerte werden ersetzt.“). Nach „Übernehmen“: „Kurswerte geladen: 15 Messwerte.“ (7 + 8, die leere Zelle b1 bei 60 min nach der Milch ist richtig), das Fragment verschwindet aus der Adresse, das Messblatt ist gefüllt. **Messpunkte erscheinen erst nach der Vorhersage** (Legende „Messpunkte“ vorher verborgen). Die Zahlen stehen natürlich im Messblatt; das sind die eigenen Messwerte, kein Verrat.

Wir sagen „unter den Kurven“ voraus. „Prüfen“ übernimmt die Kurswerte: Raum 21,5 °C, Milch 6 °C, Becher an, kA aus 0 und 10 min = 0,4332 W/K, ϑ₁,₀ 72,57 °C, ϑ₁ 35,62 °C, schwarzer Kaffee 35,51 °C, ϑ₂ 32,55 °C, Δ 3,07 K. Nachgerechnet mit m c = 836 + 255 = 1091 J/K: kA = 1091/600 · ln(58,5/46,1) = 0,4331 W/K; die übrigen Werte stimmen auf 0,01 K. Alle Punkte liegen über den Kurven (Becher 1 nach 60 min 39,8 gegen 35,62 °C; Becher 2 nach der Milch 35,2 gegen 32,55 °C). **Hier hänge ich zum zweiten Mal:** Im 338 × 163 px kleinen Diagramm liegen die braunen Kreise (Becher 1) und schwarzen Quadrate (Becher 2) fast deckungsgleich, die Legende „Messpunkte“ steht unter dem angehefteten Bereich (G10-04). Die Auflösung ist allgemein („Hängt von eurer Messung ab …“), Ursachen und prüfende Messungen wie im Konzept. Danach: „Geschafft. Weiter geht es in der Vertiefung.“

**Pflichtweg gesamt: etwa 13,5 min** (Spanne 11 bis 15 min), also über dem Ziel von etwa 10 min (G10-02).

### 6 Vertiefung V3 Becher (etwa 2,5 min)

„Vertiefung öffnen“ führt zu V1; V3 über die Liste im Reiter „Versuche“, „Diese Frage bearbeiten“. **Hier fällt mir vor der Vorhersage auf:** Angeheftet steht noch der Zustand aus Frage 2 (Becher an, kA aus der Messung): Δ 3,07 K, in den Rechenwerten „3,07 K · Tasse 1 wärmer“, im offenen Vertiefungsbereich ist „Wärmekapazität des Bechers berücksichtigen“ angehakt. Aus dem Start kenne ich 3,85 K. Damit ist die Antwort auf V3 („kleiner, Tasse 1 bleibt wärmer“) ablesbar, bevor wir vorhersagen (G10-01). Die Karte sagt dabei „Ausgangslage: Standardwerte, Becher an …“, das Diagramm zeigt aber Kurswerte (Raum 21,5 °C).

Vorhersage „kleiner“, Prüfen: ϑ₁ 34,04 °C, ϑ₂ 30,96 °C, Δ 3,08 K, kA 0,4440 W/K, Q 46,60 / 50,34 kJ, ϑ₁,₀ 72,47 °C, „Auswahl passt“. Stimmt mit Teil g des Blatts und Konzept 6.2.

## Befunde

| ID | Schwere | Befund | Beleg | Vorschlag | CONFIRMED/INFERRED |
|:--|:--|:--|:--|:--|:--|
| G10-01 | high | Vor der eigenen Vorhersage zu V3 „Becher“ zeigt die Seite den Zustand aus Frage 2 mit Becher an: Δ 3,07 K und „Tasse 1 wärmer“; wer den Start (3,85 K) kennt, liest „kleiner, Tasse 1 bleibt wärmer“ ab. Nicht die genaue Auflösung (andere Raum- und Milchtemperatur), daher nicht blocker, aber gegen „Ergebnis erst nach Vorhersage“. | Weg Start, Frage 1, Frage 2 mit Kurslink, „Vertiefung öffnen“, V3 „Diese Frage bearbeiten“: `#kernzahlen` „Δ 3,07 K“, `#rechenwerte` „3,07 K · Tasse 1 wärmer … kA 0,4332 aus der Messung nach 10 min“, Kontrollkästchen „Wärmekapazität des Bechers berücksichtigen (Keramik)=true“; Karte zugleich „Ausgangslage: Standardwerte, Becher an …“; Bild `r3_G10/25_v3_card.png` | Beim Öffnen einer Vertiefungsfrage neutral auf Standardwerte ohne Becher zurückstellen (oder Kernzahlen, Rechenwerte und Säulen bis zur Vorhersage abdecken); die Ausgangslage der Frage weiter erst bei „Prüfen“ setzen. | CONFIRMED (Anzeige); dass ein Paar daraus schließt: INFERRED |
| G10-02 | medium | Pflichtweg am kleinen Handy deutlich über 10 min. Größte Posten: Frage 2 (Link holen, Punkte im kleinen Diagramm deuten) und Frage 1 (Regler unter dem Diagramm). | Zeitschätzung: Öffnen 1,0, Start 3,5, Sprachwechsel 0,5, Frage 1 3,5, Frage 2 5,0, zusammen etwa 13,5 min (11 bis 15) | Vor dem Einsatz wie im Konzept geplant mit zwei Studierenden stoppen; falls bestätigt, Frage-2-Auflösung kürzen oder Link schon zu Beginn laden lassen (verrät nichts, siehe Ablauf 1). | INFERRED |
| G10-03 | medium | Nach „Vorhersage festhalten“ in Frage 1 klappt der Fragetext zu; der Auftrag „Verschiebt die Zugabe …“ und die Frage „Warum wird der Unterschied bei späterer Zugabe wieder kleiner?“ sind nicht mehr sichtbar. Direkt darunter steht „Auflösung zeigen“, der Regler liegt außerhalb der Karte. Ein Paar kann den Regler überspringen. | Karte nach dem Festhalten: „Frage zeigen“ (zu), „Stimmt eure Vorhersage? Erklärt zu zweit, warum.“, „Auflösung zeigen“; Bild `r3_G10/09_500.png` | Nach dem Festhalten den Prüfauftrag sichtbar lassen, etwa „Verschiebt jetzt den Regler unten. Warum wird der Unterschied später wieder kleiner?“, und erst darunter „Auflösung zeigen“. | CONFIRMED |
| G10-04 | medium | Messpunkte bei 360 px schwer zu lesen: Diagramm 338 × 163 px, Becher 1 (brauner Kreis) und Becher 2 (schwarzes Quadrat) liegen fast deckungsgleich (Abstand 0,2 bis 0,5 K), die Legende „Messpunkte“ steht nicht im angehefteten Bereich. „Beschreibt, wo die Punkte liegen“ je Becher wird mühsam. | `#legende-mess` unter dem Diagrammtext, nicht im sticky Halter; Bild `r3_G10/17_chart_zoom.png` | Punkte von Becher 2 hohl oder leicht versetzt zeichnen, Legende der Messpunkte in den angehefteten Bereich; optional eine Zeile „Messpunkte: alle über / unter den Kurven“ nach der Vorhersage. | CONFIRMED |
| G10-05 | low | Frage 2: Die Vorhersage lässt sich erst nach dem Laden der Kurswerte festhalten, der Kartentext nennt die umgekehrte Reihenfolge („Notiere zuerst … Prüft dann: Ladet …“). Kurz irritierend, kein Verrat, Hinweis erklärt es. | Hinweis unter dem Knopf: „Erst Kurswerte laden (Link der Tutoriumsleitung) oder ins Messblatt eintragen; sonst Frage 2 überspringen.“ | Kartentext anpassen: „Ladet zuerst die Kurswerte (die Punkte bleiben bis zur Vorhersage verdeckt). Notiere dann …“ | CONFIRMED |
| G10-06 | low | Das angeheftete Feld „Eure Vorhersage: Tasse 1 (Milch sofort), etwa 5 K“ bleibt während Frage 2 und V3 stehen, obwohl dort eine andere Frage gilt (bei Frage 1 nach dem Festhalten steht stattdessen die Legende). | Bilder `r3_G10/12_after_link.png`, `r3_G10/25_v3_card.png` | Nur die Vorhersage der aktuellen Frage anheften, oder das Feld beschriften („Start: …“). | CONFIRMED |
| G10-07 | low | Nach „Übernehmen“ bleibt oben dauerhaft „Kurswerte aus dem Link übernommen.“ (etwa 55 px), ohne Schließen; am kleinen Handy kostet das Platz über dem Diagramm. | `#link-banner` nach Frage 2 und in V3 weiter sichtbar; Bild `r3_G10/15_q2_locked.png` | Meldung nach einigen Sekunden ausblenden oder mit „×“ schließbar machen (Ansage bleibt). | CONFIRMED |
| G10-08 | low | Der Knopf heißt „Diagramm oben anheften“, obwohl das Diagramm schon angeheftet ist (`aria-pressed="true"`); optisch kein gedrückter Zustand. | `#knopf-anheften`: aria-pressed true, Text unverändert, Hintergrund transparent | Beschriftung je Zustand („Diagramm lösen“ / „Diagramm oben anheften“) oder sichtbarer Gedrückt-Zustand. | CONFIRMED |
| G10-09 | low | V3 fragt zwei Dinge („größer oder kleiner, und bleibt Tasse 1 wärmer?“), die Eingabe bietet nur „größer“ / „kleiner“. | Karte V3, Bild `r3_G10/25_v3_card.png` | Zweiten Teil als „notiert für euch“ kennzeichnen oder Auswahl ergänzen. | CONFIRMED |
| G10-10 | low | Die Auflösung zu Frage 2 bleibt allgemein, obwohl die Daten eindeutig sind (alle Punkte über den Kurven). Becher 1 bei 0 min (nach dem Umrühren) 80,2 °C liegt 7,6 K über der Mischtemperatur des Modells 72,57 °C, ohne Hinweis; das wäre eine gute Spur für „Ursache“ (gemessen vor dem Umrühren?). | Kurslink b1 „80.2“, Rechenwerte ϑ₁,₀ 72,57 °C, Auflösung „Hängt von eurer Messung ab …“ | Optional nach der Vorhersage eine Zeile aus den Daten („x von y Punkten über den Kurven“) und ein Hinweis, wenn Zeile 0 von Becher 1 weit über der Mischtemperatur liegt. | INFERRED |

Zählung: blocker 0, high 1, medium 3, low 6.

## Was gut funktioniert

- **Nichts verrät das Startergebnis vor der Vorhersage:** sichtbarer Text, Diagramm, Tabelle, Reiter, Ansage, CSV und Kurslink geprüft; alles verdeckt oder leer.
- Messpunkte aus dem Kurslink erscheinen erst nach der Vorhersage zu Frage 2; „Schnitt der Kurven“ erst nach der Vorhersage zu Frage 1; Regler bis dahin gesperrt.
- Alle nachgerechneten Zahlen stimmen: Standard 70,47 / 34,05 / 30,19 °C, 3,85 K, 34,88 / 38,57 kJ, kA 0,3402 W/K; Frage 1 3,86 K von 53 bis 59 min, Schnitt 55,7 min; Kurswerte kA 0,4332 W/K, 35,62 / 32,55 °C; V3 kA 0,4440 W/K, 34,04 / 30,96 °C, 46,60 / 50,34 kJ.
- Sprachwechsel mitten im Weg ohne Verlust (Vorhersage, Begründung, offene Auflösung), Zahlenformat wechselt, Stand übersteht Neuladen.
- Kurslink im offenen Tab: klares Banner, Warnung nur bei schon gefüllter Tabelle, 15 Messwerte richtig, Fragment wird entfernt (kein erneuter Import beim Neuladen).
- Keine waagerechte Scrollleiste bei 360 px, große Auswahlfelder, Zahlenfelder nehmen Komma, verständliche Bereichsmeldung; Heftung löst sich bei Bildschirmtastatur.
- Erklärauftrag mit Q₁ und Q₂ direkt nach der Startvorhersage, Auflösung mit „Auswahl passt“ und Vergleich eurer Zahl mit dem Modell.
- Keine Konsolenfehler im ganzen Ablauf.
