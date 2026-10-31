# Eigener Durchgang der vier Fragen, vor Lesen der Lösung

Festgehalten am 31.10.2026 um 17:09:32 UTC. Zu diesem Zeitpunkt wurde weder die Lösung noch das Referenzskript noch ein vorhandener Test gelesen. Diese Datei hält die eigenen Antworten fest und wird nach dem Vergleich nicht umgeschrieben.

## Vorgehen und Grenzen

Gelesen wurden nur Abschnitt „Dritter Auftrag“ in AGENTS.md und die HTML-Datei des Werkzeugs. Der erste HTML-Leseausschnitt reichte versehentlich bis in den eingebetteten Modellcode. Dessen Formeln wurden für diese Antworten nicht ausgewertet oder aufgerufen. Die unten genannten Zahlen stammen ausschließlich aus sichtbaren Anzeigen im echten Chromium. Der Browser wurde mit Playwright bedient, die Regler mit Home und Pfeiltasten. Eine automatisierte Suche ist keine gemessene Bearbeitungsdauer von Studierenden.

Der erste Browserstart scheiterte an fehlender Socket-Berechtigung, der anschließende Aufruf mit file:// um 17:05:57 UTC an der administrativen URL-Sperre. Die Richtlinie wurde nicht verändert. Ein erster lokaler Durchlauf mit unverändertem HTML in about:blank lief von 17:06:58.225 bis 17:07:28.091 UTC, also 29,866 s, und lieferte die erste Suche für Fragen 1 und 2. Für den reproduzierbaren vollständigen Durchlauf wurde danach der erlaubte Ursprung http://localhost:31460/x3-simulation.html gewählt. Exakt diese Anfrage wurde mit den unveränderten Bytes der lokalen HTML-Datei beantwortet. Es liefen weder ein Webserver noch Internetanfragen. Der Browserkontext blieb offline; alle anderen Anfragen wurden abgebrochen.

Der vollständige Durchlauf dauerte von 17:08:13.831 bis 17:09:04.447 UTC, also 50,616 s. Das Protokoll enthält 509 sichtbare Zustände und keine externe Anfrage. Vom ersten erfolgreichen automatisierten Browserdurchlauf bis zur Festhaltung der Antworten vergingen etwa 2 min 34 s. Das ist tatsächliche technische Ablaufzeit einschließlich Auswertung und Wiederholung, keine menschliche Bearbeitungsdauer.

## Frage 1: Zeitpunkt

Ausgehend von Standardwerten wurde der Zugabezeitpunkt von 1 bis 120 min in Schritten von 1 min verändert. Der größte angezeigte Unterschied beträgt 3,86 K. Diesen Wert zeigt das Werkzeug bei 53, 54, 55, 56, 57, 58 und 59 min. Eine sinnvolle Antwort mit der verfügbaren Anzeige ist daher „ungefähr 56 min“, präziser „zwischen etwa 53 und 59 min liegt ein gerundetes Maximum“. Der erste gleich große Anzeigewert darf nicht als exakter optimaler Zeitpunkt behandelt werden.

Bei 56 min stehen dort 35,30 °C für Tasse 1 und 31,43 °C für Tasse 2. Bei 120 min sind es 23,91 °C und 20,89 °C, also nur noch 3,02 K Unterschied. Bei langer Wartezeit nähern sich beide Kühlkurven der Raumtemperatur. Dadurch wird der zuvor aufgebaute Vorteil der sofortigen Zugabe wieder kleiner. Die kalte Milch kühlt Tasse 2 beim späten Zugießen zusätzlich ab. Aus der Anzeige folgt deshalb nicht, dass der Unterschied gegen null gehen müsste.

Stockstelle: Der dort ebenfalls angezeigte Schnittpunkt 55,7 min könnte zur vorschnellen Antwort führen. Er bezeichnet aber laut Beschriftung den Schnitt mit dem noch schwarzen Kaffee, während der fragliche Unterschied Tasse 2 nach dem Zugießen verwendet. Die Rundung bildet ein sichtbares Plateau. Die Aufgabe ist als ungefähre Suche lösbar, als Frage nach einem eindeutig ablesbaren einzelnen Zeitpunkt nicht.

Belege: fragen_q1_56min.png, fragen_q1_120min.png und Zustände q1_1min bis q1_120min im JSON.

## Frage 2: Milchtemperatur

Nach „Standardwerte (Aufgabe)“ wurde bei 60 min die Milchtemperatur von 2 bis 65 °C in 0,5-K-Schritten verändert. Bei 47,0 °C zeigt das Werkzeug für beide Tassen 35,53 °C, einen Unterschied von 0,00 K und „Beide Tassen sind gleich warm“. Bei 46,5 °C beträgt der Unterschied +0,05 K, bei 47,5 °C −0,05 K. Die studentisch ablesbare Antwort ist damit rund 47 °C.

Die Temperatur hängt vom Vergleichszeitpunkt ab. Bei unverändert 47 °C Milch und Zugabe nach 40 min bleibt Tasse 1 um 0,64 K wärmer, bei 120 min ist Tasse 2 um 1,90 K wärmer. Eine weitere Suche findet den Vorzeichenwechsel bei 40 min zwischen 55,5 °C (+0,02 K) und 56,0 °C (−0,02 K). Bei 120 min liegt er zwischen 30,5 °C (+0,03 K) und 31,0 °C (−0,03 K).

Stockstelle: „nach 60 Minuten“ klingt zunächst wie ein fester Vergleichshorizont. Tatsächlich verändert der Zugaberegler laut eigener Hilfe zugleich den Vergleichszeitpunkt. Eine von der Zugabe unabhängige Auswertung bei festgehaltenen 60 min bietet die Oberfläche nicht. Außerdem erreicht der 0,5-K-Regler bei anderen Zeitpunkten nicht immer eine Anzeige „gleich warm“. Für die qualitative Zeitabhängigkeit ist das kein Hindernis.

Belege: fragen_q2_gleichheit_60min.png, fragen_q2_47grad_40min.png und Zustände q2_40min_* sowie q2_120min_* im JSON.

## Frage 3: Becher

Zuerst wurde bei 60 min und den aus Frage 2 übernommenen 47 °C der Becher eingeschaltet. Die Anzeige wechselt von 0,00 K auf −0,01 K und lautet „Tasse 2 (Milch später) ist um 0,01 K wärmer“. Die Wärme steigt von Q1 = Q2 = 38,57 kJ auf Q1 = 50,35 kJ und Q2 = 50,34 kJ. Bei streng sequentieller Bearbeitung folgt aus der Aufgabe daher keine bestätigende Aussage „Tasse 1 ist wärmer“.

Erst nach einem eigenen zusätzlichen Klick auf „Standardwerte (Aufgabe)“ ergibt der Schaltervergleich die vermutlich beabsichtigte Beobachtung:

| Zustand bei 60 min und 5 °C Milch | Unterschied | Q1 | Q2 |
| --- | ---: | ---: | ---: |
| Ohne Becher | 3,85 K | 34,88 kJ | 38,57 kJ |
| Mit Becher | 3,08 K | 46,60 kJ | 50,34 kJ |

Mit Becher ist der Unterschied kleiner, die abgegebene Wärme beider Tassen größer und Tasse 1 bleibt wärmer. Die Hilfe am Schalter erklärt, dass kA aus derselben Messung neu bestimmt wird. Die Anzeige steigt dabei von 0,3402 auf 0,4440 W/K. Dies ist beim Deuten mitzulesen.

Stockstelle: Zwischen den Fragen steht kein Auftrag, die Standardwerte zurückzusetzen. Die richtige Antwort hängt deshalb von zuvor veränderten Reglern ab. Konkreter Korrekturvorschlag: Frage 3 mit „Stellen Sie zunächst die Standardwerte wieder her“ beginnen. Zusätzlich sollte klar sein, dass beide Wärmemengen mit und ohne Becher auf unterschiedliche Bilanzräume bezogen sind.

Belege: fragen_q3_sequenziell_nach_q2.png, fragen_00_standard.png und fragen_q3_standard_mit_becher.png.

## Frage 4: Versuch

Mir stehen keine echten Versuchsmesswerte zur Verfügung. Ich habe keine Werte als reale Messungen erfunden und kann deshalb nicht behaupten, welche Messpunkte über oder unter den Kurven liegen. Nach „Wie im Versuch: 40 min, Becher“ und „Einstellungen aus den Messwerten übernehmen“ ohne Messdaten steht unten: „Übernommen: Start nicht gefunden, Messwert nach 10 min nicht gefunden, Zugabe nach 40 min, Becher an.“ Die Tabelle meldet „Noch keine Messwerte“.

Aus dem sichtbaren Modelltext lassen sich mögliche Ursachen einer später beobachteten Abweichung nennen: unvollständiges Durchmischen, nicht konstante Wärmeübergangsbedingungen und temperaturabhängige Wärmeabgabe. Welche Ursache zu einem konkreten Messpunkt passt, hängt von dessen Lage und dem tatsächlichen Versuch ab. Aus diesem Durchgang folgt hierzu kein experimenteller Befund.

Stockstelle: Die Frage setzt mitgebrachte Messdaten voraus. Ohne diese ist sie nicht vollständig bearbeitbar. Sie ist als Anschluss an den vorherigen Versuch plausibel. Eine eindeutige allgemeine Antwort kann das Werkzeug allein nicht liefern. Die Übernahme meldet fehlende Daten, zeigt aber gleichzeitig „Übernommen“ und setzt trotzdem 40 min und Becher an.

Beleg: fragen_q4_ohne_messwerte.png und Zustand q4_ohne_messwerte im JSON.

## Einschätzung von Eindeutigkeit und Zeitrahmen

Fragen 1 und 2 sind mit sichtbaren Anzeigen in wenigen Bedienfolgen qualitativ beantwortbar. Die fehlende Rücksetzung vor Frage 3 ist eine konkrete didaktische Unklarheit, die ohne Hilfe zu einer anderen Antwort führt. Frage 4 ist nur mit echten Messwerten vollständig lösbar. Wenn Studierende die Werte bereits bereitliegen haben und das Werkzeug kennen, erscheinen 10 bis 15 min für drei kurze Suchaufgaben und den anschließenden Messvergleich plausibel. Dieser automatisierte Durchgang belegt keine Bearbeitungsdauer von Menschen; eine belastbare Zeitfreigabe erfordert eine Erprobung mit Studierenden. Besonders das vollständige Abtippen zahlreicher Messpunkte könnte das Zeitbudget aufbrauchen.

## Reproduktion

Im Repository: `node ergebnisse/kaffee/codex_skripte/x3/fragen_durchgang.js`. Erforderlich sind Playwright und /usr/bin/chromium. In der hier verwendeten Sandbox brauchte der Chromiumstart eine zusätzliche Netzwerkberechtigung für lokale Browser-Sockets. Der Browser selbst läuft weiterhin offline und erhält nur die unveränderte lokale HTML-Datei über die explizite Route. Der Aufruf überschreibt das eigene JSON-Protokoll und die eigenen Bildschirmfotos, nicht das Werkzeug.
