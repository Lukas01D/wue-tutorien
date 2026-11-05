# Abnahme auf einem echten iPhone (Safari)

> Für die TL. Nach `BAU_AUFTRAG.md`, Teil 3.5. Die Prüfungen im Cloud-Container laufen in Chromium (Playwright); WebKit war dort nicht verfügbar. Chromium ersetzt diesen Gerätenachweis nicht: Er bleibt **offen**, bis du ihn erbracht hast. Dauer etwa 20 min. Trag bei jedem Punkt „ja“, „nein“ oder eine Beobachtung ein und schick die Liste zurück (oder schreib sie in den Chat).

**Vorbereitung**

- iPhone mit aktuellem iOS, Safari, Ton aus. Notiere Modell und iOS-Version: ____________________
- Die Datei `simulation/site/Kaffee_Simulation.html` (bytegleich mit `index.html`) auf das iPhone bringen, zum Beispiel per AirDrop oder in die Dateien-App (iCloud Drive). Prüfsumme siehe `simulation/site/BAUNACHWEIS.txt`.
- Für den Kurslink (Punkt 8) brauchst du die Seite unter einer Adresse (lokaler Server im WLAN oder später die veröffentlichte Adresse). Ohne Adresse diesen Punkt über die Dateien-App prüfen, soweit möglich, und den Rest offen lassen.

## A Offline-Datei aus der Dateien-App

| Nr. | Schritt | Erwartung | Ergebnis |
|:--|:--|:--|:--|
| A1 | Flugmodus an. In der Dateien-App auf `Kaffee_Simulation.html` tippen, „In Safari öffnen“ (falls angeboten) oder Vorschau. | Seite erscheint vollständig, Schrift Fira Sans (Ziffern mit flachen Köpfen, nicht Systemschrift), Formeln mit ϑ und Indizes aufrecht. | |
| A2 | Erstes Öffnen | Startkarte „Erst vorhersagen“, Achsen ohne Kurven, keine Zahlen zu den Ergebnissen. Kopf rechts: „Werte bleiben nur in diesem Browser“ oder „Werte werden nicht gespeichert“ (notiere, welches). | |
| A3 | Flugmodus wieder aus | | |

## B Hochformat

| Nr. | Schritt | Erwartung | Ergebnis |
|:--|:--|:--|:--|
| B1 | Tasse 1 wählen, bei „Unterschied etwa“ 4 eintippen, „Vorhersage festhalten und Kurven zeigen“ | Kurven erscheinen, darunter ϑ₁ 34,05 °C, ϑ₂ 30,19 °C, Δ 3,85 K. Frageleiste springt zu Frage 1, oben der Rückblick „Start: …“. | |
| B2 | Nach unten scrollen bis zum Regler „Zugabe in Tasse 2 nach“ | Das Diagramm bleibt oben angeheftet (mit den drei Kernzahlen), Regler darunter sichtbar. | |
| B3 | Bei Frage 1 „50“ eintippen, festhalten. Den Regler „Zugabe nach“ mit dem Finger ziehen. | Regler folgt dem Finger flüssig, Kurven und Kernzahlen ändern sich sofort, die Seite scrollt dabei nicht mit. | |
| B4 | Plus- und Minusknopf neben dem Regler je dreimal antippen | Wert ändert sich in Schritten von 1 min; Knöpfe gut treffbar (mindestens Fingerkuppe). | |

## C Dezimaleingabe und Bildschirmtastatur

| Nr. | Schritt | Erwartung | Ergebnis |
|:--|:--|:--|:--|
| C1 | „Vertiefung“ öffnen, ins Zahlenfeld „Kaffeetemperatur am Anfang“ tippen | Zahlentastatur mit Komma (bei deutscher Region) erscheint. Das Diagramm ist **nicht** mehr angeheftet, solange die Tastatur offen ist (sonst verdeckt es das Feld). | |
| C2 | „79,5“ eingeben, „Fertig“ bzw. außerhalb tippen | Wert 79,5 übernommen, Kurven ändern sich. | |
| C3 | „79.5“ (mit Punkt) eingeben | ebenfalls übernommen. | |
| C4 | „abc“ eingeben | Meldung unter dem Feld, alter Wert bleibt. | |
| C5 | Im Messblatt einige Werte mit Komma eintippen (z. B. Becher 2: 80,4 und 67,8) | Werte bleiben stehen, keine Rundung beim Tippen, kein Springen der Seite. | |

## D Querformat, Zoom, Scrollen

| Nr. | Schritt | Erwartung | Ergebnis |
|:--|:--|:--|:--|
| D1 | iPhone ins Querformat drehen | Diagramm in voller Breite, **nicht** angeheftet; kein waagrechtes Scrollen der ganzen Seite. | |
| D2 | Zurück ins Hochformat | Anheften wieder an (nach dem Scrollen in den Simulationsbereich). | |
| D3 | Mit zwei Fingern auf etwa 200 % zoomen, dann wieder zurück | Zoomen möglich (nicht gesperrt); nach dem Zurückzoomen nichts verschoben. | |
| D4 | In „Bedienungshilfen > Anzeige & Textgröße > Größerer Text“ eine Stufe größer (optional) | Texte größer, nichts abgeschnitten. | |

## E Sprachwechsel

| Nr. | Schritt | Erwartung | Ergebnis |
|:--|:--|:--|:--|
| E1 | Oben rechts „DE ↔ EN“ antippen | Alles auf Englisch, Zahlen mit Punkt (34.05), eure Vorhersagen und Regler bleiben. | |
| E2 | Seite neu laden | Bleibt Englisch (wenn A2 „Werte bleiben …“ zeigte). | |
| E3 | Zurück auf Deutsch | | |

## F Kurslink (braucht eine Adresse)

| Nr. | Schritt | Erwartung | Ergebnis |
|:--|:--|:--|:--|
| F1 | Auf einem zweiten Gerät (oder Laptop) Messblatt füllen, „Kurswerte als Link teilen“, Link aufs iPhone schicken | | |
| F2 | Link auf dem iPhone öffnen | Rückfrage „Kurswerte aus dem Link übernehmen?“; nach „Übernehmen“ stehen die Werte im Messblatt, die Adresse hat kein `#kurs1=…` mehr. | |
| F3 | Link mit absichtlich verändertem Wert öffnen (z. B. `b2:180` statt `b2:80`) | Meldung mit Grund in Worten, nichts geändert. | |

## G Download

| Nr. | Schritt | Erwartung | Ergebnis |
|:--|:--|:--|:--|
| G1 | Im Messblatt „Als CSV herunterladen“ | Safari bietet die Datei `kaffee_simulation.csv` an (Download-Pfeil oder Teilen-Blatt); in der Dateien-App lesbar, erste Zeile „t [min];Modell Tasse 1 [°C];…“, zweite „0;70,47;80,00;;“. | |
| G2 | Aus der Offline-Datei (Dateien-App, Flugmodus) dasselbe | Download klappt oder ist erklärbar blockiert (notieren). | |

## H Zurücksetzen

| Nr. | Schritt | Erwartung | Ergebnis |
|:--|:--|:--|:--|
| H1 | Ganz unten „Für die nächste Gruppe zurücksetzen“, Rückfrage mit „Ja“ | Startkarte, keine Kurven; die Kurswerte im Messblatt bleiben (nach der nächsten Vorhersage sichtbar). | |

**Gesamturteil der TL:** ☐ abgenommen ☐ abgenommen mit Mängeln (siehe Bemerkungen) ☐ nicht abgenommen

Bemerkungen:
