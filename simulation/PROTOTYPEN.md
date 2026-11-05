# Zwei offene Gestaltungsfragen: Prototypen und Wahl

> Nach `BAU_AUFTRAG.md`, Teil 3.4. Je zwei begrenzte Prototypen mit denselben Beispieldaten (Standardwerte der Aufgabe; Energie zusätzlich mit „Milch für Tasse 2 bei Raumtemperatur“), als Bildschirmfoto verglichen. Die Prototypen entstehen nur im Skript `simulation/prototypen/prototypen.js` durch Austausch einzelner Teile der gebauten Seite; die ausgelieferte Datei enthält keinen Prototypcode. Bilder in `simulation/bildschirmfotos/prototypen/` (Chromium, Gerätefaktor 2). Stand 05.11.2026.
>
> Hinweis: Nach der Übernahme von B zeichnet die Seite selbst B; ein neuer Lauf des Prototypskripts zeigt dann in beiden Bildern B. Die Bilder A stammen aus dem Lauf vor der Übernahme (Commit dieses Abschnitts) und bleiben als Beleg im Repository.

## 1 Energiesäulen (M-20)

| | A: zwei Säulen | B: zwei Säulen mit Bezugslinie und Klammer |
|:--|:--|:--|
| Aufbau | $Q_1$ und $Q_2$ als Säulen auf gemeinsamer Nulllinie, Werte darüber, Satz darunter | wie A; dazu gestrichelte Linie auf Höhe von $Q_1$ und an Säule 2 eine Klammer mit „+3,69 kJ“ |
| Bilder | `energie_A_standard_390.png`, `energie_A_standard_1366.png`, `energie_A_milch_390.png`, `energie_A_milch_1366.png` | `energie_B_standard_390.png`, `energie_B_standard_1366.png`, `energie_B_milch_390.png`, `energie_B_milch_1366.png` |
| Beobachtung | Der Unterschied (3,69 von 38,57 kJ, etwa 10 %) ist nur an den Zahlen ablesbar; die Säulen sehen fast gleich aus. | Der Unterschied ist als eigene Strecke sichtbar und trägt dieselbe Zahl wie der Satz darunter ($Q_2 - Q_1$). Die Nulllinie bleibt, keine abgeschnittene Achse. |
| Milchfall | Satz mit Milchbeitrag; Säulen unverändert | Klammer zeigt weiter nur $Q_2 - Q_1$; der Satz nennt den Milchbeitrag. Kein Widerspruch, weil die Klammer genau die erste Zahl des Satzes ist. |

**Wahl: B.** Begründung: Lernziel 1 ist die Erklärung über $Q_2 - Q_1$; B macht genau diese Größe sichtbar, ohne die Säulen von der Nulllinie zu lösen (Längenvergleich auf gemeinsamer Grundlinie nach Cleveland und McGill, Konzept M-20). Übernommen in `oberflaeche.js`, Funktion `energieZeichnen`.

## 2 Vertiefung am Handy (390 × 844)

| | A: alle Gruppen offen | B: Gruppen als Akkordeon (nur „Kaffee“ offen) |
|:--|:--|:--|
| Höhe des Bereichs | 1644 px | 594 px zugeklappt, 785 px mit geöffneter Gruppe „Milch“ |
| Bilder | `vertiefung_A_390_oben.png`, `vertiefung_A_390_regler.png` | `vertiefung_B_390_oben.png`, `vertiefung_B_390_regler.png` |
| Beim Bewegen eines Reglers | Diagramm angeheftet oben, Regler darunter (nach der Korrektur unten) | gleich, nach einem Tippen auf die Gruppe |
| Nachteil | längerer Weg nach unten | Regler versteckt; eine Frage der Vertiefung stellt ihre Ausgangslage in mehreren Gruppen ein (V3: *kA* aus der Messung und Becher in „Raum und Tasse“; V2, V5: Voreinstellungen), geänderte Regler wären dann zugeklappt |

**Wahl: A.** Begründung: Keine versteckten Bedienelemente; was „Prüfen“ einer Vertiefungsfrage verstellt, bleibt sichtbar. Der längere Weg wiegt weniger, weil das Diagramm beim Scrollen angeheftet bleibt.

**Fund beim Vergleich (behoben):** Im ersten Stand endete das Anheften am Ende der Diagrammfigur; beim Bedienen der Vertiefungsregler am Handy war das Diagramm nicht mehr zu sehen. Ursache: `position: sticky` wirkt nur innerhalb des umgebenden Blocks. Behoben in `stil.css` (Raster und Figur geben im angehefteten Zustand ihre Box ab, `display: contents`); der Browsertest prüft jetzt die Lage auf dem Bildschirm (Diagramm oben, Regler „Milchtemperatur“ frei darunter), nicht nur die CSS-Eigenschaft.
