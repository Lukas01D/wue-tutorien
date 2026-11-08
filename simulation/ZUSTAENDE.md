# Ablauf und Zustände der Kaffee-Simulation (Fassung 3)

> Stand 08.11.2026, nach `simulation/KONZEPT_F3.md`, Abschnitt 2, mit den Entscheidungen der TL (D1 bis D10, T1 bis T3). Umgesetzt in `simulation/site/src/oberflaeche.js`, geprüft in `simulation/tests/browsertest.js`. Die Zustände der Fassung 2 stehen in der Git-Geschichte dieser Datei (bis Commit 7b235ca).

| Zustand | Auslöser | sichtbar | nicht im DOM oder gesperrt |
|:--|:--|:--|:--|
| 0 Start | Öffnen, „Von vorn“ | Kopf, Zweck, 01 Vorhersage; am Laptop leerer Diagrammrahmen mit Achsen und Raumlinie; am Handy keine Bühne | Kurven, Kernzahlen, Säulen, Regler, 02 bis 04, Weiterdenken, Modell (Texte mit Zahlen werden erst bei Freigabe eingesetzt) |
| 1 Ergebnis | „Festhalten und Kurven zeigen“ (Tasse und Grund gewählt; Ergebnisse aus e freiwillig, 0 bis 100 °C) | 01 als Zeile, Kernzahlen nach 60 min, Kernsatz, Kurven mit Direktbeschriftung, Kreuze der eigenen Rechnung, Annahmenzeile, 02 mit Säulen ohne Zahlen | Säulenzahlen, Rückmeldung, Regler, 03, 04, Weiterdenken, Modell |
| 2 Erklärt | „Antwort festhalten“ in 02 | Rückmeldung zur gewählten Erklärung mit Q₁, Q₂ und Überleitung zu f; Säulen mit Zahlen; Regler (Milchtemperatur, Zugabe; Ausgangswerte zugeklappt); 03, 04, Weiterdenken, Modell, „Von vorn“ | Milchtemperatur über 30 °C bis zur Vermutung in Auftrag 3; Auflösungen der Aufträge bis „Gedanken dazu“; Gedanken in 04 bis zur eigenen Antwort |

**Regeln**

1. Vor Zustand 1 steht keine Ergebniszahl im DOM, auch nicht versteckt oder in Attributen (Prüfung: Browsertest „Z0“). Die Texte aller Zustände liegen im Skript der Offline-Datei; eingesetzt werden sie erst bei Freigabe (`data-ab` an den Abschnitten).
2. „Festhalten“ ist erst aktiv, wenn Tasse und Grund gewählt sind (T3). Die Vorhersage bleibt danach fest und steht als Zeile über der Bühne.
3. Der Kernsatz vergleicht die eigene Rechnung nur bei den Werten des Blatts (bis 0,1 K „stimmen überein“, sonst „weicht ab“ mit Werten); sonst steht der Kernsatz nach Leitlinie 6.
4. Eine Vermutung in einem Auftrag stellt die Werte des Blatts ein und zeigt die Zeile „Auftrag n … Deine Vermutung …“ über dem Diagramm.
5. Fortschritt und Eingaben bleiben im Browser des Geräts (D9); ist der Speicher gesperrt, rechnet die Seite weiter und sagt das im Fuß.
