# Gestaltungsmuster Fassung 3 (Konzeptstopp)

Muster der Gestaltungssynthese aus `simulation/KONZEPT_F3.md`, Abschnitt 6 und Anhang A. **Kein fertiger Bau:** nur die Zustände Startkarte und Ergebnis, Deutsch, Regler Milchtemperatur und Zugabe wirken, die übrigen Schritte sind angedeutet. Rechnung wie `kaffee_modell.py` mit den Werten aus `werte.py` (72 °C nach 10 min).

| Datei | wofür |
|:--|:--|
| `muster_src.html` | Quelle (HTML, CSS, Skript) |
| `bauen_muster.py` | bettet die Schriften ein und schreibt `muster.html` (`python3 bauen_muster.py`) |
| `muster.html` | das Muster, offline; Zustand über `?zustand=0` oder `?zustand=2` |
| `bilder_muster.js` | Bildschirmfotos nach `simulation/bildschirmfotos/f3_entwurf/` (`node bilder_muster.js`) |
| `schriften/` | IBM Plex Sans, Mono, Math als Teilmengen aus Entwurf A, mit OFL-Lizenztexten |
