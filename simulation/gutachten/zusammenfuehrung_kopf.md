# Zusammenführung der Rollenprüfungen

> Nach `simulation/BAU_AUFTRAG.md`, Teil 4.3. Getrennte Rollenprüfungen desselben Modells (G1 bis G8); die unabhängige Prüfung mit einem anderen Modell ist X5. Runde 1 prüfte den Stand `index.html` SHA-256 `f519052c…6707` (369 081 Bytes; G2, G3, G5, G6, G8 nach einer Pause am 06.11.2026 auf demselben Stand zu Ende geführt). Korrigierter Stand nach Runde 1 (geprüft in Runde 2): SHA-256 `ea6d3ad2…9c31` (394 754 Bytes). Die Tabelle unten erzeugt `zusammenfuehrung_bauen.py` aus den Befundtabellen der Gutachten und den Entscheidungen im Skript; jede Zahl der Rollen wurde vor der Entscheidung nachgerechnet oder im Browser nachgestellt (Belege: Browsertests in `simulation/tests/browsertest_bau.js`, Kerntests `test_kern.py`).

## Ergebnis Runde 1

- **Zahlen:** Keine Rolle fand eine falsche Modellzahl. G3 rechnete 30 Zustände und alle Auflösungen unabhängig nach (alle gleich), dazu Messblatt, Kurslink, CSV, Wertetabelle und Lage der Kurven.
- **Zwei blocker-Sachverhalte**, beide behoben: Messpunkte waren vor der Vorhersage zu Frage 2 sichtbar (G1-01, G4-01, G7-01); Achsenbeschriftung bei Schrittweite 2,5 gerundet (G2-01, G5-01, dazu G2-21 an der ln-Achse).
- **high**, behoben: Reihenfolge und Anheften am Handy (M-6), verdeckter Fokus, Datenverlust zwischen zwei Tabs, Beamer-Layout, `aria-valuetext`, Speicherhinweis am Handy, Fokus im Kopf, Vergleichslauf, Kontrastmodus, englische CSV und Dezimalkomma, Überlappungen im Diagramm.
- **offen (Frage an die TL)** sind nur Inhalte, die der Bau nicht eigenständig ändern darf (Wortlaut aus Konzept 6 und Anhang A, Ablauf der Sitzung, Blatt gegen Seite, Reitername gegen E6). Die Empfehlungen stehen in der Tabelle und im Baubericht.
- **abgelehnt** mit Grund: Festlegungen aus Konzept oder ZUSTAENDE.md, Kann-Punkte bewusst schlank, technische Grenze der Offline-Datei (Auflösungstexte im Quelltext).

## Bilanz Runde 1 (nach Schwere und Entscheidung)
