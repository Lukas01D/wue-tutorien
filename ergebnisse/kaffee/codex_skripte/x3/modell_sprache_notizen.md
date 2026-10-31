# X3: Modelltreue und Sprache

Geprüfter Stand: `53a78d55a28eb4902aceb832c3a0ae7d9321b9c7`.

Gelesen wurden nur der dritte Auftrag in AGENTS.md, das HTML-Werkzeug, das Referenzmodell im Arbeitsordner, Aufgabe, mathematischer Lösungsteil vor den Hinweisen sowie die genannten Lehrstuhlquellen. Die erwarteten Antworten zur Simulation und die vorhandenen Testartefakte wurden für diese Teilprüfung nicht gelesen.

## Grundlage der Regler und Anzeigen

| Werkzeug | Grundlage im Referenzmodell |
|:---|:---|
| Zugabezeit | `P.t_end`, Argument `t_end` von `zwei_tassen` |
| Milchtemperatur und Milchmenge | `P.th_M`, `P.V_M`, Wärmekapazität `C_M` |
| Raumtemperatur | `P.th_U` |
| Milch für Tasse 2 bei Raumtemperatur | gesondertes Argument `th_M2` von `zwei_tassen` |
| Becher und Bechermasse | `P.m_B`, `P.c_B`, `C_T`, Funktion `becher` und `zwei_tassen` |
| Anfangstemperatur und 10-min-Messung | `P.th_K0`, `P.th_mess`, Kalibrierung von `kA` |
| Kaffeemenge | `P.V_K`, Wärmekapazität `C_K` |
| Relatives `kA` von Tasse 1 | Argument `kA1_faktor` von `zwei_tassen` |
| Endtemperaturen und Mischtemperatur | Mischbilanz und Exponentialabkühlung, `rechne` und `zwei_tassen` |
| Abgegebene Wärme | Energiebilanz wie `Q1`, `Q2` in `rechne`, beim Becher um dessen Wärmekapazität erweitert |
| Schnittpunkt | Gleichsetzen der beiden Exponentialkurven; im Werkzeug für verändertes `kA` verallgemeinert, dabei Fehler für eine zulässige Richtung, siehe unten |

Die Kurve von Tasse 2 zeigt den schwarzen Kaffee bis zum Zugießen, der senkrechte Sprung danach das sofortige Mischen. Eine nachfolgende Abkühlkurve wird nicht behauptet. Die Messpunkte sind Datenüberlagerungen und keine zusätzliche physikalische Modellierung.

Das Werkzeug bildet den linearen Teil des Referenzskripts ab. Das Referenzskript enthält zusätzlich `nichtlinear` als Formtest und `gleichstand` als Hilfsfunktion. Ihr Fehlen ist für die vorgesehenen vier Fragen kein Fehler. Die Grenze des linearen Modells wird im Werkzeug ausdrücklich erklärt. Es gibt keinen Regler für eine physikalische Größe ohne Grundlage im Referenzskript.

## Konkreter Befund: Schnittpunkt bei umgekehrter Überquerung fehlt

Stelle: `Kaffee_Simulation.html`, Zeilen 221 bis 224; die Anzeige und Beschreibung in Zeilen 156, 318 und 324 sind ebenfalls betroffen.

Gültige Reglerwerte: 200 ml Kaffee, 5 ml Milch, Kaffee anfangs 60 °C, Milch 65 °C, Raum 20 °C, Messung nach 10 min 50 °C, relatives `kA` von Tasse 1 110 %, ohne Becher. Zugabe nach 60 min.

Unabhängig mit den Stoffdaten der Aufgabe gerechnet:

- `C_K = 836 J/K`, `C_M = 20,291 J/K`.
- Mischtemperatur von Tasse 1 `60,11848191794611 °C`, schwarzer Kaffee anfangs `60 °C`.
- `a1 = 0,0005149192541372378 /s`, `a2 = 0,00047947012075296813 /s`.
- Schnittzeit aus Gleichsetzen der Exponentialkurven: `ln((60-20)/(60,11848191794611-20))/(a2-a1) = 83,4341899448 s = 1,3905698324 min`.
- Nach 60 min hat Tasse 1 vor dem Vergleich `26,2847609665 °C`, der schwarze Kaffee `27,1191406250 °C`. Der schwarze Kaffee ist nach dem Schnitt also wärmer.

Das Werkzeug setzt wegen `d <= 0` stattdessen `Infinity` und meldet keinen Schnittpunkt. Die Formel ist für `d != 0` anwendbar; ein positiver Schnitt ist anschließend auf das angezeigte Zeitintervall zu prüfen. Die Richtung sollte neutral formuliert oder aus den Temperaturen vor und nach dem Schnitt bestimmt werden. Der Sonderfall gleicher Abklingraten ist gesondert zu behandeln. Dies ist ein Fehler innerhalb der freigegebenen Reglerbereiche, kein nichtphysikalischer Eingabefall.

## Sprache und Zeichen

Die gesamte HTML-Datei enthält keine Zeichen U+2013 oder U+2014. Die Minuszeichen U+2212 in Formeln und negativen Zahlen sind korrekt. Deutsch, Einheiten und Zeichen `ϑ`, `kA`, `Q`, `C` passen zu Aufgabe und Lösung. Die Erklärung von `C` als Wärmekapazität des Bilanzraums macht die zusätzliche Abkürzung verständlich. Die Begriffe Mischen, Bilanzraum, konstante Stoffdaten und Becher sind für das dritte Semester angemessen.

Als unverbindliche Ergänzung wäre eine Anzeige der Zeitkonstanten `tau_K`, `tau_G` aus dem Referenzskript nützlich. Sie erklärt den Einfluss der Wärmekapazität ohne neuen Modellansatz. Eine Anzeige der Gleichstandstemperatur würde dagegen Frage 2 vorwegnehmen und ist für die Sitzung nicht erforderlich. Die vorhandenen Anzeigen decken die verlangten Rechenergebnisse ab.
