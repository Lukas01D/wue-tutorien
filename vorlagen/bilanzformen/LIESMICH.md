# Grafik „Energiebilanz: vier Grundformen“

Fassung **v2 vom 28.10.2026, freigegeben von der TL am 31.10.2026** (erzeugt mit `arbeitsordner/ideen/bilanzformen_v2.py`). Änderungen gegenüber v1 und ihre Begründung: `Aenderungen_v2.md` (u. a. „ganzes Kontrollvolumen“, „gewöhnliche DGL im Ort/in der Zeit“, eine Beispielgleichung je Feld, „T homogen“ im Feld instationär global, gestapelte Brüche). Rückweg: `vorlagen/bilanzformen_v1/`. Hintergrund: `wissen/projekt/Lernziele_und_Bilanzsystematik_2026-10-16.md`, Abschnitt 5.

| Ordner | Inhalt | Größe |
|---|---|---|
| `gross/` | Übersicht mit Bilanz, Ergebnis, Mathematik und Beispielen (SVG und PNG, 300 dpi) | 16 cm breit, volle Textbreite |
| `kompakt/` | Orientierungsschild (SVG und PNG, 300 dpi) | 8,2 cm breit, 5,0 cm hoch |

Neu erzeugen: `BILANZ_FONTS=arbeitsordner/ideen/schriften_bilanz/ python3 arbeitsordner/ideen/bilanzformen_v2.py <ordner>` (mit `kompakt` am Ende nur das Schild).

## Varianten (Ende des Dateinamens)

| Kennung | markiert | Einsatz (Lernziel-Dokument 5.5; Vorschläge D39, D47) |
|---|---|---|
| 0 | nichts | gemischte Aufgaben, die Studierenden ordnen selbst zu (Zusammenfassungsaufgabe V08) |
| 0b | nichts, ohne Grundgleichung (nur groß) | Einstieg in Tutorium 5: erst die vier Felder vergleichen, dann die gemeinsame Bilanz aufdecken |
| 1 | stationär, global | Tutorium 3 und 8 |
| 2 | stationär, differentiell | Tutorium 6; Herleitung von R<sub>th</sub> (Tutorium 3) und Δ*T*<sub>ln</sub> (Tutorium 8) |
| 3 | instationär, global | Tutorium 5 |
| 4 | instationär, differentiell | Tutorium 7 |
| 12 | stationär, global und differentiell | Tutorium 3 und 8 |
| 13 | global, stationär und instationär | Tutorium 5: Übergang vom Aufwärmbeispiel zur Leitaufgabe |
| 24 | differentiell, stationär und instationär | Tutorium 7 |
| 34 | instationär, global und differentiell | Tutorium 5: Biot-Diskussion |

## Aufs Blatt?

**Ja, das kompakte Schild** (Wunsch der TL vom 31.10.2026): oben rechts im Aufgabenkopf jeder Aufgabe, in der eine Energiebilanz aufgestellt wird, mit der Variante der Tabelle oben (Kaffee: 3). Auf dem Blatt etwa 5 bis 6 cm breit. Ob auch Lernziele aufs Blatt kommen, steht in R9 (`03_REGELN.md`). Die große Übersicht dient der Sitzung (Einstieg in Tutorium 5, Zusammenfassung).
