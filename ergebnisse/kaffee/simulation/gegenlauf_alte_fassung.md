# Gegenlauf: erweiterte Tests gegen die geprüfte Fassung (Commit 53a78d5)

Zweck: belegen, dass die erweiterten Tests die Befunde Simulation 1 bis 5 der Prüfung X3 gefunden hätten. Die alte Fassung wurde dafür kurz an die Stelle der neuen gelegt und danach wiederhergestellt (31.10.2026).

## test_simulation.py: 24 von 31 bestanden

- Satz 9 und 10 (Schnitt in Gegenrichtung, Befund Simulation 1): Tool meldet keinen Schnitt, unabhängige Suche findet ihn nach 83,43 s bzw. 59,50 s.
- Sätze 1, 3, 4, 6, 12: Richtung nach dem Schnitt fehlt in der alten Fassung.

## browsertest.js: 30 von 60 bestanden (Auszug, Laptop und Handy)

```
FEHLER handy C: Anfang 60 °C unter dem Messwert 67 °C: keine Ergebniszahlen, Hinweis am Ergebnis
FEHLER handy C: Messwert eintragen bei ungültiger Einstellung zeigt keine alten Ergebnisse
ok     handy C: wieder gültig, Ergebnisse wieder da
FEHLER laptop C: Anfang 60 °C unter dem Messwert 67 °C: keine Ergebniszahlen, Hinweis am Ergebnis
FEHLER laptop C: Messwert eintragen bei ungültiger Einstellung zeigt keine alten Ergebnisse
ok     laptop C: wieder gültig, Ergebnisse wieder da
ok     laptop F: vier Fragen im Werkzeug
FEHLER laptop F1: größter Unterschied ungefähr bei 56 min (3,86 K), danach kleiner (120 min: 3,02 K)  [[34,1.52],0.05]
ok     laptop F2: ungefähr gleich warm bei 47,0 °C Milch nach 60 min  47
ok     laptop F2: bei Zugabe nach 30 min passt 47 °C nicht mehr (Temperatur hängt vom Zeitpunkt ab)  0.67
FEHLER laptop F3: Unterschied 3,85 → 3,08 K, Wärme 34,88/38,57 → 46,60/50,34 kJ, Tasse 1 bleibt wärmer
FEHLER laptop F4: Übernahme Start 80,3 °C, 10 min 66,9 °C, 40 min, Becher an, 8 Messpunkte im Diagramm  [80.5,67,12]
ok     laptop F4: kein waagerechtes Scrollen mit Messwerten
FEHLER laptop F4: Messwerte nach dem Neuladen noch da
Ergebnis: 30 von 60 Prüfungen bestanden.
```

Dazu (aus dem Lauf davor, Laptop): A Schnittpunkt ohne Richtung; B Schnitt in Gegenrichtung fehlt; D alle drei unmöglichen Reihen übernommen (z. B. „Start 95,0 °C, nach 10 min 30,0 °C“ statt 100 und 15 °C), Mittelwerte gerundet (80,5 statt 80,7 °C); E „10,5,9“ und „66.5xyz“ angenommen.
