# Kaffee-Simulation, schlanke Seite

Auftrag der TL vom 11.11.2026: das Simulationstool ohne Fragen und mit viel weniger Text, Stil der Hauptseite unverändert, Säulen der an den Raum abgegebenen Wärme neben der Kurve, „Abspielen“ behalten. Die Hauptseite (`simulation/site/`) bleibt daneben bestehen.

| Teil | Woher |
|:--|:--|
| Rechenkern, Standardwerte | `site/src/modell.js`, unverändert; `schlank.js` rechnet darauf auf: Tasse mit Wärmekapazität $C_\mathrm{T}$ (immer so warm wie der Inhalt, wie `kaffee_modell.zwei_tassen`), Kaffeemenge, Abkühlung von Tasse 2 nach der Zugabe bis zur Zeit $t$. Bei $C_\mathrm{T}$ = 0 und $t = t_\mathrm{Z}$ gleiche Zahlen wie die Hauptseite. |
| Optik | `site/src/stil.css`, unverändert; dazu `src/schlank.css` nur für die Anordnung |
| Regler, Säulen, Hilfsfunktionen | Bausteine aus `site/src/oberflaeche.js`, beim Bau unverändert übernommen (Liste `BAUSTEINE`); Diagramm, Kasten und Regleranzeige in `schlank.js` im Aufbau der Hauptseite |
| Texte DE und EN | `site/src/texte_*.txt`, dazu `src/texte_schlank_*.txt` |

Regler: Zeit $t$ (1 bis 180 min), Zugabe in Tasse 2 (höchstens $t$), Milchtemperatur, Milchmenge, Kaffeetemperatur, Kaffeemenge, Raumtemperatur, $kA$, Wärmekapazität der Tasse. Der Kasten zeigt die Werte zum angezeigten Zeitpunkt (beim Abspielen laufend), die Säulen die an den Raum abgegebene Wärme bis dahin; es gilt immer $Q_2 - Q_1 = C_G\,(\vartheta_1 - \vartheta_2)$ nach der Zugabe.

Geplant: Alltagsvergleiche neben $kA$ und $C_\mathrm{T}$ (Auftrag in `AUFTRAG_Vergleichswerte.md`).

| Schritt | Befehl |
|:--|:--|
| Bauen | `python3 simulation/minimal/bauen_minimal.py` |
| Prüfen, ob die Datei zum Quellstand passt | `python3 simulation/minimal/bauen_minimal.py --pruefen` |
| Browsertest (Werte, Zeit, Abspielen, Milch 95 °C, Englisch, axe-core, Laptop und Handy) | `node simulation/tests/minimal_test.js` (41 von 41 bestanden am 11.11.2026) |

Stand 11.11.2026: `Kaffee_Simulation_schlank.html`, SHA-256 `8f5d2e266b421789…`. Nicht veröffentlicht; veröffentlicht wird nach Freigabe der TL.
