# Kaffee-Simulation, schlanke Seite

Auftrag der TL vom 11.11.2026: das Simulationstool ohne Fragen und mit viel weniger Text, Stil der Hauptseite unverändert, Säulen der an den Raum abgegebenen Wärme neben der Kurve, „Abspielen“ behalten. Die Hauptseite (`simulation/site/`) bleibt daneben bestehen.

| Teil | Woher |
|:--|:--|
| Rechenkern, Standardwerte | `site/src/modell.js`, unverändert; `schlank.js` rechnet darauf auf: Tasse mit Wärmekapazität $C_\mathrm{T}$ (immer so warm wie der Inhalt, wie `kaffee_modell.zwei_tassen`), Kaffeemenge, Abkühlung von Tasse 2 nach der Zugabe bis zur Zeit $t$. Bei $C_\mathrm{T}$ = 0 und $t = t_\mathrm{Z}$ gleiche Zahlen wie die Hauptseite. |
| Optik | `site/src/stil.css`, unverändert; dazu `src/schlank.css` nur für die Anordnung |
| Regler, Säulen, Hilfsfunktionen | Bausteine aus `site/src/oberflaeche.js`, beim Bau unverändert übernommen (Liste `BAUSTEINE`); Diagramm, Kasten und Regleranzeige in `schlank.js` im Aufbau der Hauptseite |
| Texte DE und EN | `site/src/texte_*.txt`, dazu `src/texte_schlank_*.txt` |

Regler: Zeit $t$ (1 bis 180 min), Zugabe in Tasse 2 (höchstens $t$), Milchtemperatur, Milchmenge, Kaffeetemperatur, Kaffeemenge, Raumtemperatur, Tassenwärmer $\dot{Q}_\mathrm{W}$ (0 bis 10 W in beide Tassen, höchstens so viel, dass $\vartheta_u + \dot{Q}_\mathrm{W}/kA \le$ 95 °C), $kA$, Wärmekapazität der Tasse. Der Kasten zeigt die Werte zum angezeigten Zeitpunkt (beim Abspielen laufend), die Säulen die an den Raum abgegebene Wärme bis dahin; es gilt immer $Q_2 - Q_1 = C_G\,(\vartheta_1 - \vartheta_2)$ nach der Zugabe.

Alltagsvergleiche neben $kA$ (logarithmischer Regler, 0,01 bis 1 W/K) und $C_\mathrm{T}$: Bereiche in `src/schlank.js` (Liste `VERGLEICH`), Belege in `QUELLEN_Vergleichswerte.md`, Prüfung mit `python3 simulation/minimal/vergleichswerte.py`. Beide Regler stehen unten nebeneinander, die übrigen acht darüber (breite Ansicht: vier Spalten). Darstellung der Vergleiche: `DESIGN` in `bauen_minimal.py` (1 Etikett in der Namenszeile, 2 kleiner Kasten mit Spanne und Beschreibung, 3 Band unter der Skala); Vorschau einer anderen Darstellung mit `--design 2 --ziel DATEI`.

Entscheidung der TL vom 12.11.2026: Die schlanke Seite ersetzt unter der bisherigen Adresse die alte Seite (Auftrag für Codex oben in `simulation/VEROEFFENTLICHUNG.md`).

| Schritt | Befehl |
|:--|:--|
| Bauen | `python3 simulation/minimal/bauen_minimal.py` |
| Prüfen, ob die Datei zum Quellstand passt | `python3 simulation/minimal/bauen_minimal.py --pruefen` |
| Browsertest (Werte, Zeit, Abspielen, Milch 95 °C, Englisch, axe-core, Laptop und Handy) | `node simulation/tests/minimal_test.js` (55 von 55 bestanden am 12.11.2026) |

Stand 12.11.2026: `Kaffee_Simulation_schlank.html`, SHA-256 `1626ef8f7c559822…`. Nicht veröffentlicht; veröffentlicht wird nach Freigabe der TL.
