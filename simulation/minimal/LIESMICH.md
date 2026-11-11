# Kaffee-Simulation, schlanke Seite

Auftrag der TL vom 11.11.2026: das Simulationstool ohne Fragen und mit viel weniger Text, Stil der Hauptseite unverändert, Säulen der an den Raum abgegebenen Wärme neben der Kurve, „Abspielen“ behalten. Die Hauptseite (`simulation/site/`) bleibt daneben bestehen.

| Teil | Woher |
|:--|:--|
| Rechenkern, Standardwerte | `site/src/modell.js`, unverändert |
| Optik | `site/src/stil.css`, unverändert; dazu `src/schlank.css` nur für die Anordnung (Säulen neben dem Diagramm, Zeitzeile) |
| Regler, Diagramm, Kasten, Säulen | Bausteine aus `site/src/oberflaeche.js`, beim Bau unverändert übernommen (Liste `BAUSTEINE` in `bauen_minimal.py`); einzige Änderung: Maßstab der Säulen aus den Werten bei der Zugabe, damit sie beim Abspielen wachsen |
| Texte DE und EN | `site/src/texte_*.txt`, dazu vier Texte in `src/texte_schlank_*.txt` (Abspielen, Anhalten, Zeit, Säulentitel bis t) |
| Eigenes | `src/vorlage.html`, `src/schlank.js` (Zeitregler, Abspielen, verdeckte Zukunft im Diagramm) |

Ändert sich die Hauptseite, übernimmt der nächste Bau die Änderung. Ändern sich dort die Achsen des Diagramms, bricht der Bau mit einer Meldung ab (`ACHSEN`), damit die Zeitlinie nicht verrutscht.

| Schritt | Befehl |
|:--|:--|
| Bauen | `python3 simulation/minimal/bauen_minimal.py` |
| Prüfen, ob die Datei zum Quellstand passt | `python3 simulation/minimal/bauen_minimal.py --pruefen` |
| Browsertest (Werte, Zeit, Abspielen, Milch 95 °C, Englisch, axe-core, Laptop und Handy) | `node simulation/tests/minimal_test.js` (31 von 31 bestanden am 11.11.2026) |

Stand 11.11.2026: `Kaffee_Simulation_schlank.html`, SHA-256 `2898c8eae95dfbc9…`. Nicht veröffentlicht; veröffentlicht wird nach Freigabe der TL.
