# Änderung der Kaffee-Simulation am 10.11.2026 (Fassung 3, 100 ml und 45 min)

Anlass: Entscheidungen der TL zum Blatt vom 09.11.2026 (R01 bis R22) und 10.11.2026 (100 ml kalte Milch, 45 min Wartezeit, Trinktemperatur 50 °C). Auftrag der TL: „simulation einmal entsprechend aller änderungen anpassen“.

| Bereich | Änderung |
|:--|:--|
| Standardwerte (`modell/werte.py`, `STANDARD` in `site/src/modell.js`) | Milch 100 ml statt 30 ml, Zugabe nach 45 min statt 60 min, Trinktemperatur 50 °C statt 60 °C; alle übrigen Werte gleich (vorläufig bis zur Messung im Januar 2027) |
| Rechenkern | unverändert (`modell/kaffee_modell.py` bytegleich, Block MODELL in `modell.js` unverändert) |
| Messpunkte | Zeitpunkte 0, 10, 20, 30, 40, 45 min und „45 min, nach der Milch“ (Liste `ZEITEN`); Beispielwerte neu aus `werte.py` |
| Regler | Milchmenge bis 200 ml (vorher 100 ml); Marken der Zugabe 1, 45, 90, 135, 180 min |
| Texte DE und EN | Zeitangaben aus dem Blatt (45 min) statt „eine Stunde“ und „60 min“; „Versuch“ heißt wie auf dem Blatt „Experiment“, auch im Kernsatz; Verdunstung ist Teil j (vorher h); Prüfwerte aus d und h1 (vorher d1 und d2); ln-Darstellung gehört zu Experiment 4 |
| Lokaler Speicher | neuer Schlüssel `kaffee-simulation-f3-45min`, damit alte Stände mit 30 ml und 60 min nicht übernommen werden |
| Tests | Erwartungswerte auf die neuen Zahlen umgestellt; Rechenkern 34 von 34, Texte 16 von 16, Browser 107 von 107 bestanden |
| Bildschirmfotos | `bildschirmfotos/f3/` neu (23 Bilder) |

Neue Prüfwerte (Blatt und Seite): Tasse 1 nach dem Zugießen 55,49 °C; nach 45 min Tasse 1 43,01 °C, schwarzer Kaffee 51,51 °C, Tasse 2 nach der Milch 36,31 °C, Unterschied 6,69 K; Q1 15,50 kJ, Q2 23,82 kJ; Kipppunkt 63,2 °C; Zeit bis 50 °C 17,4 min; Schnittpunkt 112 min.
