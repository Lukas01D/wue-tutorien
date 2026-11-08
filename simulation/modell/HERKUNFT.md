# Herkunft der Modelldateien (Fassung 3)

| Datei | Herkunft | SHA-256 |
|:--|:--|:--|
| `kaffee_modell.py` | unverändert; bytegleich mit `neu/kaffee_modell.py` im Startpaket Fassung 3 der TL (08.11.2026) und mit der Kopie aus Fassung 2 (Kaffee-Zweig `claude/kaffee-pruefung-sgvo1r`, 560b8d4) | eb7efc1d5322b629e1e11494f7c70fa8d8d54ec60e555874326fa491a31757a1 |
| `werte.py` | unverändert aus `neu/werte.py` im Startpaket Fassung 3 (Standardwerte des Blatts Fassung 3: 72 °C nach 10 min mit Deckel, erwärmte Milch 70 °C, Trinktemperatur 60 °C; vorläufige Werte bis zur Messung im Januar 2027) | 08e1caee608132e6cba1b13cb3db555d98e0e51a9b4d3ad3ec561c0e65f1e259 |
| `../site/src/modell.js` | Block `MODELL-ANFANG` bis `MODELL-ENDE`: `P`, `K` und `rechne()` wie in `kaffee_modell.py` (aus dem geprüften Block der Fassung 2, ohne die dort entfernten Erweiterungen); Standardwerte des Blatts außerhalb des Blocks in `STANDARD` | siehe `simulation/tests/test_kern_ergebnis.txt` |

`kaffee_erweitert.py` (Erweiterungen der Fassung 2) ist mit Fassung 3 entfernt. Geprüft durch `simulation/tests/test_kern.py`.
