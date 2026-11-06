# Gutachten G4: Lernpsychologie und Fachdidaktik, Runde 3

## 1 Kopf

| | |
|:--|:--|
| Rolle | G4 „Lernpsychologie und Fachdidaktik“ |
| Datum | 06.11.2026 |
| Runde | 3 (letzte Runde; Nachprüfung, nicht von vorn) |
| Art | getrennte Rollenprüfung desselben Modells |
| Geprüfte Datei | `simulation/site/index.html`, 399063 Bytes, SHA-256 `1d90ce2f84349754592a5dd572a760a5d212cd3383bcafbeb1cceaf06e07292b` (vor und nach der Prüfung mit `sha256sum` bestätigt) |
| Grundlagen | eigenes Gutachten Runde 2 (`G4_Lernpsychologie_R2.md`); in `ZUSAMMENFUEHRUNG.md` nur die Zeilen G4-01 bis G4-24 und G4-R2-01 bis G4-R2-06; KONZEPT.md und Blatt vom 31.10.2026 wie in Runde 2 |
| Umgebung | Chromium über Playwright (`chromium.launch()` ohne Optionen), `file://`; Handy 390 × 844 (isMobile, hasTouch, Tippen), Laptop 1366 × 768 |
| Durchgespielt | Handy, Kurslink vor dem Start übernommen (wie in der Sitzung), zweimal Pflichtweg: **richtig** (Start „Tasse 1, 4 K, Tasse 2 bleibt länger heiß und gibt mehr ab“, Frage 1 „55 min“, Frage 2 „über den Kurven“) und **falsch** (Start „beide gleich warm, 0 K, Die Energie bleibt ja erhalten“, Frage 1 „90 min“, Frage 2 „auf den Kurven“), jeweils mit Auflösungen. Laptop: Frage 2 ohne Kurswerte und übersprungen, V1, V2, „ohne Vorhersage aufdecken“ mit Escape, Ansicht „Wärmestrom“ vor Frage 1 |
| Skripte und Bilder | `/tmp/claude-0/-home-user/8bff1287-c5bb-5641-9916-90393029086f/scratchpad/r3_G247/g4/` (Skripte s5, s6, s12 der Runde 2 erneut; neu t1.js, t2.js; Bilder `t1_*.png`) |
| Nicht gelesen | BAU_BERICHT, ZWISCHENSTAND, PROTOTYPEN, tests, andere Gutachten, Git-Protokoll |

## 2 Nachprüfung

| ID | Ergebnis am neuen Stand | Beleg |
|:--|:--|:--|
| G4-08 | **behoben nach dem Festhalten.** Kasten im Diagramm und Zeile der Rechenwerte zeigen dieselbe, aktuelle Vorhersage mit Fragenname: „Eure Vorhersage (Zeitpunkt) 55 min“, „(Versuch) über den Kurven“, „(Milchtemperatur) 30 °C“. Vor dem Festhalten einer neuen Frage Rest siehe G4-R2-03. | t1.js („F1 fest“, „F2 fest“), t2.js („V1 fest“) |
| G4-11 | **teilweise, unverändert.** Nach dem Festhalten des Starts stehen Rückblick (Erklärauftrag, „Auflösung zeigen“) und die volle Frage 1 mit Eingabe in einer Leiste; der Fokus springt auf den Titel von Frage 1. Einen eigenen Schritt „Start besprechen“ gibt es nicht. Am Handy liegt der Rückblick direkt unter Diagramm und Kernzahlen („Auflösung zeigen“ bei 580 bis 624 px im falschen Lauf), das Feld von Frage 1 rund 350 px tiefer (935 px). | t1.js (`active: frage-titel`; Positionen), `t1_falsch_01_start_fest.png` |
| G4-R2-01 | **teilweise, wie entschieden; Lernwirkung weitgehend gesichert.** Der Erklärauftrag nennt am Handy die Zahlen direkt: „Erklärt den Unterschied mit *Q*₁ und *Q*₂. (abgegeben bis zur Zugabe: Tasse 1 34,88 kJ, Tasse 2 38,57 kJ)“, die Auflösung des Starts ergänzt „*Q*₂ − *Q*₁ = 3,69 kJ … sind 3,85 K“. Damit lässt sich der Auftrag ohne die Säulen bearbeiten. Die Säulen selbst stehen weiter weit unten (Kasten 1660 bis 1928 px, „Auflösung zeigen“ unter dem Auftrag bei 580 bis 624 px), Bild und Auftrag also nie zugleich. | t1.js, `t1_falsch_01_start_fest.png`; nachgerechnet 38,57 − 34,88 = 3,69 kJ, 3690 J / 957,7 J/K = 3,85 K |
| G4-R2-02 | **behoben.** Ansicht „Wärmestrom“ vor Frage 1: Flächentext und Beschreibung nur „Tasse 2 gibt bis zur Zugabe insgesamt 3,69 kJ mehr Wärme ab als Tasse 1.“; kein Schnitt, keine Teilflächen. | s5.js |
| G4-R2-03 | **teilweise.** Nach dem Festhalten richtig (G4-08). Solange eine neue Frage noch nicht festgehalten ist, zeigen Kasten im Diagramm **und** Zeile „Eure Vorhersage“ weiter die Startvorhersage, ohne den Zusatz „Start“: in Frage 1 und Frage 2 „Eure Vorhersage: beide gleich warm, etwa 0 K“, in V1 und V2 „Eure Vorhersage: Tasse 1 (Milch sofort), etwa 4 K“, während die Frage nach einer Zeit, einer Lage der Punkte oder einer Milchtemperatur fragt. Der zweite Teil des Vorschlags (Kasten bis zum Festhalten ausblenden) ist nicht umgesetzt. | t1.js („F1 vor fest“, „F2 vor“ im falschen Lauf), t2.js („V1 vor“, „V2 vor“). Vorschlag: bis zum Festhalten Kasten weglassen und Zeile „Eure Vorhersage (…): noch keine“ |
| G4-R2-04 | **teilweise, wie entschieden.** Escape schließt die Rückfrage, der Fokus geht zurück auf „ohne Vorhersage aufdecken“. Der Fokus startet weiter auf „Ja“, der Text nennt weiter nur die Folge („Die Auflösung ist dann sofort sichtbar.“). | s6.js, t2.js (`focus rueck-ja`, nach Escape `knopf-ohne`) |
| G4-R2-05 | **behoben.** Ansage „Ohne Vorhersage aufgedeckt. Tasse 1 34,05 °C, …“. | s6.js |
| G4-R2-06 | **behoben** für Eingaben und Knöpfe: Nach „Frage 2 überspringen“ nur noch „Zurück“, „Weiter“, „Vertiefung öffnen“; ohne Kurswerte kein „ohne Vorhersage aufdecken“ (Knopf fehlt). Rest an Texten: G4-R3-01. | t2.js („inputs sichtbar“, „knopf-ohne … fehlt“); s12.js bricht deshalb erwartungsgemäß ab |

**Bilanz:** von 8 nachzuprüfenden Punkten 4 behoben (G4-08, G4-R2-02, G4-R2-05, G4-R2-06), 4 teilweise (G4-11, G4-R2-01, G4-R2-03, G4-R2-04; davon G4-R2-01 und G4-R2-04 im Umfang der Entscheidung umgesetzt), keiner nicht behoben.

Unverändert offen bei der TL (nicht nachgeprüft, Empfehlungen aus Runde 2, Abschnitt 3, gelten weiter): G4-03 (Fragetext Frage 1 verrät „wieder kleiner“ vor der Vorhersage, am Handy so gesehen), G4-04 (Erhaltungssatz fehlt; im falschen Lauf steht „Eure Begründung: Die Energie bleibt ja erhalten“ ohne Antwort darauf), G4-05, G4-15, G4-16 („Geschafft“ erscheint weiter sofort beim Festhalten von Frage 2, vor der Auflösung), G4-17, G4-20, G4-22, G4-24, Texte zu G4-02.

## 3 Neue Befunde

Kein blocker, kein high. Die Sperren halten: vor dem Start „Achsen ohne Kurven“, vor Frage 1 kein Schnitt (auch nicht in der Ansicht „Wärmestrom“), vor Frage 2 keine Messpunkte und Legende verborgen, auch mit Kurslink vor dem Start.

| ID | Schwere | Befund | Beleg | Vorschlag | CONFIRMED/INFERRED |
|:--|:--|:--|:--|:--|:--|
| G4-R3-01 | low | **Übersprungene Frage 2 widerspricht sich noch in Texten.** Nach „Frage 2 überspringen“ stehen über „Frage 2 übersprungen: Es gibt keine Messwerte.“ weiter der volle Fragetext mit „Prüft dann: Ladet die Messwerte …“, die Zeile „Noch keine Kurswerte. Öffnet den Link der Tutoriumsleitung oder tragt die Werte ins Messblatt ein.“ und „Ausgangslage: Kurswerte, übernommen beim Prüfen“. Selbstlernende lesen eine Aufforderung, die nicht mehr gilt; bei festgehaltenen Fragen ist der Fragetext dagegen eingeklappt. | Laptop, Frage 2 ohne Kurswerte, `#knopf-f2-weg` (t2.js, Ausgabe „F2 übersprungen“) | Nach dem Überspringen wie nach dem Festhalten: Fragetext einklappen („Frage zeigen“), Zeile „Noch keine Kurswerte …“ und Ausgangslage weglassen. | CONFIRMED |

### Zählung

Nachprüfung: behoben 4, teilweise 4, nicht behoben 0. Neue Befunde: blocker 0, high 0, medium 0, low 1.

## 4 Durchgang Pflichtweg am Handy (richtig und falsch)

- **Rückmeldung** unterscheidet sauber: richtig „Auswahl passt“, „Eure Zahl: 4 K · Modell: 3,85 K“, „Eure Zahl: 55 min · Modell: etwa 56 min“; falsch „× Auswahl passt nicht“, „Eure Zahl: 0 K · Modell: 3,85 K“, „Eure Zahl: 90 min · Modell: etwa 56 min“; eigene Begründung jeweils über der Auflösung.
- **M-6 am Handy:** Diagramm angeheftet, beim Regeln bleibt es sichtbar (Regler 772 bis 846 px, Diagramm 0 bis 298 px); Vorhersagelinie bei 55 bzw. 90 min sichtbar.
- **Kurslink in der Sitzung:** Mit Becher 3 im Link steht ab dem Start ein hohles blaues Dreieck (Modellwert Becher 3) ohne Legende zwischen den Endpunkten; es verrät nichts zu Start oder Frage 1, ist aber ein unerklärtes Zeichen in der Phase, in der die Paare nur zwei Tassen vergleichen sollen. In der Rolle G7 als Befund aufgenommen.
- Kein waagerechtes Scrollen, keine Skriptfehler.
