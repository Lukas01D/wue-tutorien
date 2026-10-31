# Vergleich nach Abschluss des eigenen Durchgangs

Der eigene Befund wurde zuerst in fragen_erstbefund.md festgehalten. Erst danach wurde der Absatz „Simulation (dritte Ebene)“ in Kaffee_Loesung.md, Zeile 229, gelesen. Vorhandene Tests, deren Ergebnisse und deren Bildschirmfotos wurden für diesen Teilauftrag nicht gelesen.

## Abgleich

| Frage | Eigene Antwort vor der Lektüre | Erwartung und Vergleich |
| --- | --- | --- |
| 1 | Größter sichtbarer Unterschied 3,86 K bei 53 bis 59 min, also etwa 56 min; bei 120 min nur 3,02 K. | Erwartet sind etwa 56 min und 3,86 K. Übereinstimmung. Der genaue Zusammenhang zwischen Maximum und Kurvenschnittpunkt war aus der bloßen Anzeige nicht beweisbar, wurde danach unabhängig nachgerechnet. |
| 2 | Bei 60 min Gleichheit mit 47,0 °C Milch. Andere Zeitpunkte benötigen andere Temperaturen. | Erwartet sind 47,0 °C bei 60 min sowie 60,9 °C bei 30 min und 37,3 °C bei 90 min. Übereinstimmung in Wert und Zeitabhängigkeit. Die zusätzlichen erwarteten Werte sind mit dem 0,5-K-Regler nicht exakt einstellbar; sie eignen sich als rechnerische Vertiefung. |
| 3 | Nach eigenem Standard-Reset sinkt der Unterschied von 3,85 auf 3,08 K. Q1 steigt von 34,88 auf 46,60 kJ und Q2 von 38,57 auf 50,34 kJ. | Exakte Übereinstimmung mit der Erwartung. Die Erwartung setzt aber den im Fragetext fehlenden Reset voraus. Bei tatsächlichem Anschluss an Frage 2 und 47 °C ergibt sich „Tasse 2 ist um 0,01 K wärmer“. |
| 4 | Ohne echte Messwerte keine Aussage über die Lage der Messpunkte. Nur mögliche Gründe aus dem Modelltext benannt. | Die Lösung erwartet meist einige Kelvin zu hohe Messpunkte wegen temperaturabhängigem kA und einen besser passenden Unterschied zwischen Becher 1 und 2. Das ist eine empirische Erwartung, die ohne Versuchsdaten weder bestätigt noch widerlegt werden kann. Für eine konkrete Auswertung müssen die tatsächlich gemessenen Abweichungen maßgeblich bleiben. |

## Nachrechnung der Erwartungen

fragen_nachrechnung.js wurde nach der Lektüre aus Mischbilanz und der sichtbaren Abkühlgleichung eigenständig geschrieben. Es importiert weder das Referenzmodell noch den Modellcode des Werkzeugs noch bestehende Tests. Ergebnisdatei: fragen_nachrechnung.json.

Die unabhängige Intervallsuche liefert das Maximum bei 55,7446676 min mit 3,8618379 K. Die Gleichheitstemperaturen sind 60,9122663 °C bei 30 min, 47,0030928 °C bei 60 min und 37,2845015 °C bei 90 min. Die berechneten Becherwerte runden exakt auf die erwarteten vier Wärmemengen und zwei Unterschiede. Nach Frage 2 mit unverändert 47 °C und Becher an beträgt der Unterschied dagegen −0,0090160 K. Der beim blinden Durchgang entdeckte Reihenfolgeeffekt ist damit bestätigt.

## Konkrete Empfehlungen aus diesem Teilauftrag

1. Vor Frage 3 ausdrücklich „Stellen Sie zunächst die Standardwerte wieder her“ ergänzen. Sonst führt die unmittelbare Fortsetzung von Frage 2 zu einer anderen Aussage als die Lösung.
2. In Frage 1 „ungefähr bei welchem Zeitpunkt“ schreiben oder das sichtbare Rundungsplateau ausdrücklich zulassen.
3. In Frage 2 klarstellen, dass beim Verschieben des Zugabezeitpunkts gleichzeitig der Vergleichszeitpunkt geändert wird. Eine feste Beobachtung nach 60 min bei früherer Zugabe kann das Werkzeug nicht darstellen.
4. Frage 4 als Vergleich mit eigenen, bereits vorliegenden Versuchswerten kennzeichnen. Eine allgemeine Aussage über „meist oberhalb“ ist ohne konkrete Messdaten kein eigenes Ergebnis des Werkzeugdurchgangs.

10 bis 15 min erscheinen mit bereitliegenden Messwerten und nach Beseitigung der Reihenfolgeunklarheit plausibel. Die tatsächlich gemessene automatisierte Bedienzeit von 50,616 s ist kein Beleg für eine menschliche Bearbeitungsdauer.
