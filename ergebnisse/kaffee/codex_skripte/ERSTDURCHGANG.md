# Eigener Durchgang vor Öffnen von Lösung und Rechenmodell

Quellen: Aufgabe im Originalpaket, Formelsammlung und Foliensatz 05, Folien 1 bis 21. Musterlösung und C_modell waren bei Erstellung dieses Protokolls und des Skripts noch ungeöffnet.

## Herleitung a bis e

a) Beim adiabaten Mischen gilt C_K (ϑ_K,0 − ϑ_1,0) = C_M (ϑ_1,0 − ϑ_M), mit C_i = m_i c_p,i. Die Mischungstemperatur folgt als gewichteter Mittelwert.

b) Bilanzraum ist der ideal durchmischte Inhalt, nach abgeschlossener Zugabe eine konstante Masse. Ohne Arbeit und Quellen gilt dU/dt = −Q̇_ab = −kA (T − T_u). Mit dU = C dT und Trennung: ∫dT/(T − T_u) = −∫(kA/C)dt. Die Anfangsbedingung liefert ln[(T − T_u)/(T_0 − T_u)] = −kAt/C. Für die Mischung ist C = C_K + C_M, für schwarzen Kaffee C = C_K. Die bekannte Exponentialform folgt durch Exponentieren.

c) Die Messung bestimmt den effektiven Leitwert H = kA aus dem logarithmischen Verhältnis der Übertemperaturen, nicht aus einem linearen Temperaturabfall.

d) Tasse 1: Erst mischen, dann mit der größeren Wärmekapazität abkühlen. Tasse 2: Nur Kaffee abkühlen, dann adiabatisch mischen. Verglichen werden dieselben Endmassen unmittelbar nach der letzten Zugabe.

e) Q_1 = (C_K + C_M)(ϑ_1,0 − ϑ_1), Q_2 = C_K(ϑ_K,0 − ϑ_2,vor). Daraus muss Q_2 − Q_1 = (C_K + C_M)(ϑ_1 − ϑ_2) folgen. Die Energieerhaltung gilt einschließlich der Umgebung und bedeutet keine identischen Verluste.

## Stolperstellen

1. Die Aufgabenfassung druckt Ergebnisse für a bis e bereits ab. Ein völlig ergebnisblinder Durchgang ist damit unmöglich. Das eigene Skript enthält keine dieser Ergebniszahlen als Rechenvorgabe oder Prüfung; es leitet alle Werte aus der Gegebenentabelle ab.
2. In b) ist m c_p für die Mischung als Summe der Wärmekapazitäten zu lesen. Ein bloßer Massenmittelwert der Temperaturen oder das unveränderte Kaffee-c_p wäre falsch.
3. Für Q_2 in e) ist die Kaffeetemperatur unmittelbar vor Zugabe einzusetzen. Die Mischtemperatur aus d) würde bei alleiniger Kaffee-Wärmekapazität die Wärmebilanz verfälschen.
4. Die Gleichheit von kA trotz verschiedener Füllmengen ist eine ausdrückliche Modellannahme. Aus der einzigen Messung ohne Milch folgt sie nicht.
5. Das Vorwärmen und die Aussage, der Becher habe immer Inhaltstemperatur, erfordern in f) eine gemeinsame Mischbilanz einschließlich Becherkapazität. Die Milchzugabe darf nicht erst nach einer unabhängigen Becherbilanz erfolgen.
6. In g) bleibt offen, ob die spät zugegebene Schaummasse nach einer Stunde noch 60 °C hat. Für eine Rechnung allein nach d) muss das zusätzlich vorausgesetzt werden.

Die Rechnung wurde auch für f bis h aus der Aufgabe abgeleitet. Die Ausgabedatei wird vor Öffnen der Musterlösung erzeugt. Analytische Lösung, direkte DGL-Integration und Integration des Wärmestroms werden unabhängig gegeneinander geprüft.
