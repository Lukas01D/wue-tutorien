# Kaffee-Simulation, schlanke Varianten A und B

Auftrag der TL vom 11.11.2026: das Simulationstool ganz schlank, ohne Fragen und ohne sonstige Bereiche; nur die Simulationskurve und daneben zwei Säulen mit der an den Raum abgegebenen Wärme von Tasse 1 und Tasse 2. Zur Auswahl in zwei Varianten. Die Hauptseite (`simulation/site/`) bleibt unverändert daneben bestehen.

| Variante | Datei | Was sie zeigt |
|:--|:--|:--|
| A: Überblick | `Kaffee_Simulation_A.html` | Kurven bis zur Zugabe, Säulen mit Q1 und Q2 bis zur Zugabe, Ergebniszeile, sechs Regler, Knopf „Werte des Blatts“ |
| B: Zeitlauf | `Kaffee_Simulation_B.html` | wie A, dazu ein Zeitregler mit „Abspielen“: Kurven und Säulen wachsen gemeinsam von 0 bis zur Zugabe |

Gemeinsam: Rechenkern und Standardwerte aus `simulation/site/src/modell.js` (unverändert eingebunden), Milchtemperatur bis 95 °C, Sprung durch die Milch gestrichelt mit Pfeil (nach unten oder nach oben), Säulen mit Q₂ − Q₁; es gilt Q₂ − Q₁ = C_G (ϑ1 − ϑ2). Nur Deutsch; Englisch folgt nach der Wahl der TL. Keine Speicherung im Browser, keine Netzanfragen, eigene CSP.

| Schritt | Befehl |
|:--|:--|
| Bauen | `python3 simulation/minimal/bauen_minimal.py` |
| Prüfen, ob die Dateien zum Quellstand passen | `python3 simulation/minimal/bauen_minimal.py --pruefen` |
| Browsertest (Werte, Milch 95 °C, Zeitregler, axe-core, Laptop und Handy) | `node simulation/tests/minimal_test.js` (49 von 49 bestanden am 11.11.2026) |

Stand 11.11.2026: Variante A SHA-256 `d4af39a4131894d2…`, Variante B `433cfdff7a90c829…`. Nicht veröffentlicht; veröffentlicht wird erst nach der Wahl der TL.
