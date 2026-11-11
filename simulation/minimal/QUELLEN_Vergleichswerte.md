# Vergleichswerte für kA und Wärmekapazität der Tasse

Recherche vom 12.11.2026 für die Alltagsvergleiche neben den Reglern der schlanken Seite (Auftrag: `AUFTRAG_Vergleichswerte.md`). Rechnungen: `vergleichswerte.py` (erzeugt die Tabellen unten und prüft die Bereiche in `src/schlank.js`).

## Rechenweg

- kA aus einer Abkühlung im Modell des Blatts: $kA = C/t \cdot \ln[(\vartheta_0 - \vartheta_u)/(\vartheta - \vartheta_u)]$ mit $C$ = Wasser (4180 J/(kg K)) plus Gefäß, wo bekannt.
- Wärmekapazität der Tasse: $C_\mathrm{T} = m\,c$.
- Annahmen sind in der Spalte „Bemerkung“ genannt (zum Beispiel Füllmenge oder Raumtemperatur, wenn die Quelle sie nicht nennt). Die Vergleiche sind daher Größenordnungen, keine Messwerte.

### kA (W/K)

| Gegenstand | kA | Quelle | Bemerkung |
|:--|:--|:--|:--|
| Isolierflasche 0,5 l, Mindestwert der Norm | bis 0,039 | Q1 | EN 12546-1: 95 °C, 6 h, 20 °C, am Ende mindestens 70 °C; Wert ist die Obergrenze für eine Flasche, die die Norm erfüllt |
| Isolierflasche 1 l, Mindestwert der Norm | bis 0,050 | Q1 | wie oben, am Ende mindestens 78 °C |
| sehr gute Isolierflasche (Ikea Volym) | 0,012 bis 0,013 | Q3 | 95 °C, nach 6 h 86 °C, nach 24 h fast 64 °C; Füllung 0,5 l und Raum 20 °C angenommen (nicht genannt) |
| guter Thermobecher (bester im Test) | 0,024 bis 0,032 | Q2 | 80 °C, in der ersten Stunde 4 K weniger; Füllung 0,3 bis 0,4 l und Raum 20 °C angenommen |
| schwacher Thermobecher (schlechtester im Test) | 0,133 bis 0,177 | Q2 | 80 °C, in der ersten Stunde 19 K weniger; Annahmen wie oben |
| Trinkglas 140 ml, Seitenwand (oben und unten gedämmt) | 0,242 | Q4 | τ = 49 min; C aus 140 cm³ Wasser und 152 g Glas |
| Kunststoffbecher 140 ml, Seitenwand | 0,181 | Q4 | τ = 55 min |
| Styroporbecher 140 ml, Seitenwand | 0,153 | Q4 | τ = 65 min |
| Keramiktasse 200 ml mit Deckel (Blatt, vorläufig) | 0,199 | Q13 | aus 72 °C nach 10 min (Annahme der TL, Messung im Januar) |
| Tasse mit Deckel, Abschätzung h·A | 0,200 bis 0,360 | eigene Abschätzung | h = 10 bis 12 W/(m²K) (freie Konvektion und Strahlung), benetzte Außenfläche 0,02 bis 0,03 m² |
| offene Tasse (mit Verdunstung, grob) | 0,827 bis 1,143 | Q5 und eigene Abschätzung | τ ≈ 22 min für offenen Kaffee; Füllung 0,2 bis 0,3 l und Porzellantasse 255 J/K angenommen; Verdunstung ist im Modell nicht enthalten, der Wert ist nur ein Ersatz |

### Wärmekapazität der Tasse C_T (J/K)

| Gegenstand | Masse in g | C_T | Quelle | Bemerkung |
|:--|:--|:--|:--|:--|
| Pappbecher 0,3 l mit Deckel | 14,4 | 19 bis 19 | Q8, Q6 | Becher 11 g (10 bis 18 g), Deckel 3,4 g; c Papier 1340, Deckel als Kunststoff etwa 1300 angenommen |
| doppelwandiges Glas 0,25 l (Bodum Pavina) | 100 | 75 bis 84 | Q12, Q6 | etwa 100 g je Glas, falls 0,6 kg für den Satz gelten (unklar); mit dem Inhalt in Kontakt ist nur die Innenwand |
| dünnes Trinkglas | 152 | 128 | Q4, Q6, Q7 | 152 g; c Fensterglas 840 (Q6, Q7); Q4 nennt 500 bis 840, der untere Wert gilt für Bleiglas |
| Steingutbecher 30 cl (Ikea Dinera) | 300 | 240 | Q9, Q6 | Paket 0,32 kg, Becher also etwa 0,30 kg (geschätzt); c Steingut 800 |
| Porzellantasse 300 g (Blatt, Experiment) | 300 | 255 | Q13 | werte.py: M_TASSE 0,300 kg, C_KERAMIK 850 |
| Einmachglas 580 ml (Weck) | 306 | 257 | Q10, Q6 | 306 g (ob mit Deckel, ist nicht angegeben) |
| schwerer Porzellanbecher 300 ml | 540 | 459 bis 578 | Q11, Q6 | 540 g; c Porzellan 850 (Blatt) bis 1070 (Q6) |

### Prüfung: Welcher Vergleich erscheint beim belegten Wert?

| Regler | Gegenstand | Wert | angezeigt |
|:--|:--|:--|:--|
| kA | Isolierflasche 0,5 l, Mindestwert der Norm | 0,039 | ≈ Isolierflasche, Thermobecher |
| kA | Isolierflasche 1 l, Mindestwert der Norm | 0,050 | ≈ Isolierflasche, Thermobecher |
| kA | sehr gute Isolierflasche (Ikea Volym) | 0,013 | ≈ sehr gute Isolierflasche |
| kA | guter Thermobecher (bester im Test) | 0,028 | ≈ Isolierflasche, Thermobecher |
| kA | schwacher Thermobecher (schlechtester im Test) | 0,155 | ≈ Tasse mit Deckel |
| kA | Trinkglas 140 ml, Seitenwand (oben und unten gedämmt) | 0,242 | ≈ Tasse mit Deckel |
| kA | Kunststoffbecher 140 ml, Seitenwand | 0,181 | ≈ Tasse mit Deckel |
| kA | Styroporbecher 140 ml, Seitenwand | 0,153 | ≈ Tasse mit Deckel |
| kA | Keramiktasse 200 ml mit Deckel (Blatt, vorläufig) | 0,199 | ≈ Tasse mit Deckel |
| kA | Tasse mit Deckel, Abschätzung h·A | 0,280 | ≈ Tasse mit Deckel |
| kA | offene Tasse (mit Verdunstung, grob) | 0,985 | ≈ offene Tasse (grob) |
| C_T | Pappbecher 0,3 l mit Deckel | 19 | ≈ Pappbecher mit Deckel |
| C_T | doppelwandiges Glas 0,25 l (Bodum Pavina) | 80 | ≈ doppelwandiges Glas |
| C_T | dünnes Trinkglas | 128 | ≈ dünnes Trinkglas |
| C_T | Steingutbecher 30 cl (Ikea Dinera) | 240 | ≈ Porzellantasse, Einmachglas |
| C_T | Porzellantasse 300 g (Blatt, Experiment) | 255 | ≈ Porzellantasse, Einmachglas |
| C_T | Einmachglas 580 ml (Weck) | 257 | ≈ Porzellantasse, Einmachglas |
| C_T | schwerer Porzellanbecher 300 ml | 518 | ≈ schwerer Porzellanbecher |

Bereiche passen zu den Belegen.

## Bereiche auf der Seite

| Regler | ab | Vergleich (DE) | Vergleich (EN) |
|:--|:--|:--|:--|
| kA in W/K (logarithmisch, 0,01 bis 1) | 0,01 | ≈ sehr gute Isolierflasche | ≈ very good vacuum flask |
| | 0,02 | ≈ Isolierflasche, Thermobecher | ≈ vacuum flask, travel mug |
| | 0,06 | ≈ einfacher Thermobecher | ≈ basic travel mug |
| | 0,12 | ≈ Tasse mit Deckel | ≈ cup with lid |
| | 0,4 | ≈ offene Tasse (grob) | ≈ open cup (rough) |
| $C_\mathrm{T}$ in J/K (0 bis 600) | 0 | Blatt: Tasse speichert keine Wärme | worksheet: cup stores no heat |
| | 1 | ≈ Pappbecher mit Deckel | ≈ paper cup with lid |
| | 50 | ≈ doppelwandiges Glas | ≈ double-walled glass |
| | 110 | ≈ dünnes Trinkglas | ≈ thin drinking glass |
| | 200 | ≈ Porzellantasse, Einmachglas | ≈ porcelain cup, mason jar |
| | 350 | ≈ schwerer Porzellanbecher | ≈ heavy porcelain mug |

## Grenzen

- kA hängt von der Füllmenge (benetzte Fläche) und vom Deckel ab. Die Vergleiche gelten für etwa 200 bis 400 ml mit Deckel.
- Eine offene Tasse kühlt zusätzlich durch Verdunstung, die das Modell nicht enthält. Der Bereich „offene Tasse“ ist nur ein grober Ersatz (Q5 nennt weder Füllung noch Gefäß).
- Ein schwacher Thermobecher (schlechtester im Test Q2) liegt im Bereich „Tasse mit Deckel“. Das passt zur Aussage der Quelle, dass nicht alle Thermobecher lange warm halten.
- Für das doppelwandige Glas ist das Gewicht unsicher (Q12 sagt nicht, ob 0,6 kg für ein Glas oder den Satz gilt); mit dem Inhalt in Kontakt ist nur die Innenwand.
- Spezifische Wärmekapazität von Porzellan: 850 J/(kg K) im Blatt, 1070 J/(kg K) in Q6. Der Bereich „Porzellantasse“ deckt beides ab.

## Quellen (abgerufen am 12.11.2026)

| Nr. | Quelle | Verwendet für |
|:--|:--|:--|
| Q1 | Galaxus: „How long do thermos flasks keep liquids hot?“ (Beschreibung der Prüfung nach EN 12546-1), https://www.galaxus.de/en/page/how-long-do-thermos-flasks-keep-liquids-hot-the-specs-arent-always-accurate-39978 | Isolierflasche, Mindestwerte der Norm |
| Q2 | Stiftung Warentest: „Thermobecher im Test: Nicht alle halten lange warm“, https://www.test.de/Thermobecher-im-Test-5246429-0/ | Thermobecher, bester und schlechtester |
| Q3 | Stiftung Warentest: „Isolierflaschen im Test: Die Ikea-Flasche hält 24 Stunden warm“, https://www.test.de/Isolierflaschen-im-Test-Die-Ikea-Flasche-haelt-24-Stunden-warm-5391117-0/ | sehr gute Isolierflasche |
| Q4 | Conti u. a.: Abkühlung von Wasser in Gefäßen aus Glas, Kunststoff und Styropor, The Physics Teacher 52 (2014) 109, https://iris.unipa.it/retrieve/e3ad8916-97d7-da0e-e053-3705fe0a2b96/Conti%20-%20Phys%20Teach%2052%20%282014%29%20109.pdf | Trinkglas, Kunststoff- und Styroporbecher; Masse Trinkglas |
| Q5 | University of Florida: „Cooling coffee“, https://web.mae.ufl.edu/uhk/COOLING-COFFEE.pdf | offene Tasse (Zeitkonstante) |
| Q6 | Engineering ToolBox: Specific heat of solids, https://www.engineeringtoolbox.com/specific-heat-solids-d_154.html | c von Glas, Porzellan, Steingut, Papier |
| Q7 | chemie.de: Spezifische Wärmekapazität, https://www.chemie.de/lexikon/Spezifische_W%C3%A4rmekapazit%C3%A4t.html | c Fensterglas |
| Q8 | Deutsche Umwelthilfe: Coffee to go, Hintergrund, https://www.duh.de/uploads/tx_duhdownloads/DUH_Coffee-to-go_Hintergrund_01.pdf | Masse Pappbecher und Deckel |
| Q9 | IKEA DINERA Becher 30 cl, Steingut, https://www.ikea.com/fi/en/p/dinera-mug-dark-grey-30362820 | Masse Steingutbecher (Paketgewicht) |
| Q10 | Original Unverpackt: Weck Sturzglas 580 ml, https://shop.original-unverpackt.de/en/products/weck-sturzglas-580-ml | Masse Einmachglas |
| Q11 | Loveramics Bond 300 ml, https://eushop.loveramics.com/de/collections/bond/products/bond-300ml-mug | Masse schwerer Porzellanbecher |
| Q12 | kaqtu: Bodum Pavina 0,25 l, https://www.kaqtu.ch/en/products/drinking-glass-pavina-double-wall-6-stucco-0-25-l | Masse doppelwandiges Glas (unsicher) |
| Q13 | `simulation/modell/werte.py` (Blatt): Keramiktasse 300 g, 850 J/(kg K); kA 0,1994 W/K vorläufig | Bezug zum Blatt und zum Experiment |
