# Herkunft der Modelldateien

| Datei | Herkunft | SHA-256 |
|:--|:--|:--|
| `kaffee_modell.py` | unveränderte Kopie aus `pruefung/Kaffee_Pruefpaket_2026-10-23/umsetzung/Arbeitsordner/kaffee/kaffee_modell.py` auf dem Zweig `claude/kaffee-pruefung-sgvo1r` (gelesen auf f8a5ce3, zuletzt geändert in 560b8d4) | eb7efc1d5322b629e1e11494f7c70fa8d8d54ec60e555874326fa491a31757a1 |
| `kaffee_erweitert.py` | Python-Referenz der Erweiterungen (Bau, KONZEPT.md Fassung 2, Abschnitt 8.2); importiert `kaffee_modell.py` | wechselt mit dem Bau |
| `../site/src/modell.js` | unveränderter Block `MODELL-ANFANG` bis `MODELL-ENDE` aus `ergebnisse/kaffee/fertig/Kaffee_Simulation.html` (Kaffee-Zweig, f8a5ce3; bytegleich mit `ergebnisse/kaffee/simulation/Kaffee_Simulation.html` auf `main`) | b32e3f9db9f82b09bfc0e300388ffbef72f875cec65540da668d765389f97d24 |

Geprüft durch `simulation/tests/test_kern.py` (Identität und Zahlen).
