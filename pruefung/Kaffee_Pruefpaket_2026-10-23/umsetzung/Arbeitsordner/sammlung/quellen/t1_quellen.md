# Quellen Tutorium 1: Wärmeleitung

Quellen der Arbeitswerte und Fakten in `teile/t1.md`, übernommen aus den Quellenverzeichnissen der Ausgangsdokumente (Ideensammlung „Leitaufgaben aus Klima und Erde“ vom 17.10.2026, Abschnitt 12; Pilotblatt Tutorium 1 mit Musterlösung). In Klammern steht, wo der Wert oder Fakt vorkommt. Zahlen: `rechnung/t1_rechnung.py`.

## Aufgabe 1: Seen unter dem Eisschild

- **Kälterekord −89,2 °C an der Station Wostok am 21.07.1983** (Ausgangssituation, Teil c): WMO. (o. J.). *World record: Lowest temperature, Vostok, Antarctica*. <https://public.wmo.int/node/13122>
- **Hunderte Seen unter dem Eis** (675 erfasst, Stand 2022; Ausgangssituation): Livingstone, S. J., et al. (2022). Subglacial lakes and their changing role in a warming climate. *Nature Reviews Earth & Environment, 3*, 106 bis 124. <https://doi.org/10.1038/s43017-021-00246-9>
- **Bohrung erreicht am 05.02.2012 in 3769 m Tiefe das Wasser des Wostoksees** (Ausgangssituation, Teil f; der Literaturwert von etwa −3 °C wird bewusst nicht genannt: Er passt zu luftgesättigtem Eis mit 0,098 K/MPa, das Modell der Aufgabe rechnet mit reinem Eis, 0,0742 K/MPa, und ergäbe in 3769 m −2,52 °C): Jones, N. (2012). \[Titel nicht erfasst; Nachricht zur Bohrung am Wostoksee\]. *Nature, 482*, 287. <https://doi.org/10.1038/482287a>
- **Wärmestromdichte aus dem Erdinneren im weltweiten Mittel rund 0,09 W/m²** (Ausgangssituation, Zusatzaufgabe 1 b): Davies, J. H., & Davies, D. R. (2010). Earth’s surface heat flux. *Solid Earth, 1*, 5 bis 24. <https://doi.org/10.5194/se-1-5-2010>. Vergleich mit einer 40-W-Glühlampe auf einem Basketballfeld (420 m², also 95 mW/m²): eigene Rechnung der Ideensammlung.
- **Wärmestromdichte aus dem Erdinneren 58 mW/m²** (Tabelle; Dome C aus Bohrlochdaten 57,9 ± 6,4 mW/m²): Talalay, P., et al. (2020). Geothermal heat flux from measured temperature profiles in deep ice boreholes in Antarctica. *The Cryosphere, 14*, 4021 bis 4037. <https://doi.org/10.5194/tc-14-4021-2020>
- **Wärmeleitfähigkeit von Eis λ(T) = 9,828 W/(m K) · exp(−5,7·10⁻³ K⁻¹ · T) und Schmelzpunktsenkung γ = 0,0742 K/MPa (reines Eis; luftgesättigt 0,098 K/MPa)** (Satz unter der Tabelle, Tabelle): Cuffey, K. M., & Paterson, W. S. B. (2010). *The physics of glaciers* (4. Aufl.). Elsevier. Die Formel für λ(T) ist zitiert nach Mony, L., Roberts, J. L., & Halpin, J. A. (2020). Inferring geothermal heat flux from an ice-borehole temperature profile at Law Dome, East Antarctica. *Journal of Glaciology, 66*, 509 bis 519. <https://doi.org/10.1017/jog.2020.27>
- **Messwerte im Bohrloch EPICA Dome C: −4,2 °C in 3200 m und −2,34 °C in 3270,2 m Tiefe** (Tabelle, Teil h): Augustin, L., et al. (2007). EPICA Dome C 2 drilling operations: Performances, difficulties, results. *Annals of Glaciology, 47*, 68 bis 72. <https://doi.org/10.3189/172756407786857767>. Die Tiefe 3270,2 m ist der Wert aus dem Pilotskript `pilot_tutorium1.py`; das Pilotblatt nannte gerundet 3270 m.
- **Dicke der Firnschicht s~F~ = 100 m** (Tabelle, Teil h): Arbeitswert des Pilotblatts („obere 100 m“), dort ohne eigene Quelle.
- **Wärmeleitfähigkeit von Firn λ~F~ = 1,0 W/(m K)** (Tabelle, Teil h; Arbeitswert, bei Dome C 0,9 bis 2,2 W/(m K) je nach Dichte): Calonne, N., et al. (2019). Thermal conductivity of snow, firn, and porous ice from 3-D image-based computations. *Geophysical Research Letters, 46*. Daten: PANGAEA. <https://doi.org/10.1594/PANGAEA.906906>
- **Eisdicke 3700 m und Oberflächentemperatur −55 °C** (Tabelle): Arbeitswerte der Ideensammlung (Abschnitt 4.1, Anhang A) für einen allgemeinen Standort in der Ostantarktis, nicht für die Bohrstelle Wostok (dort friert Seewasser an die Eisbasis an). Zum Vergleich: Wostoksee unter rund 3,8 km Eis, Studinger, M., et al. (2004). \[Titel nicht erfasst; Wostoksee\]. *Geophysical Research Letters, 31*. <https://doi.org/10.1029/2004GL019801>
- **Dichte von Eis 917 kg/m³, Schmelzenthalpie 333,5 kJ/kg, g = 9,81 m/s²** (Tabelle): Standardwerte; Arbeitswerte der Ideensammlung und des Pilotblatts, dort ohne eigene Quelle.
- **Mittlere Wärmeleitfähigkeit als Integralmittel, Randbedingungen nach Dirichlet und von Neumann** (Teil c, d): Riese, J. (2026). *Wärmeübertragung: Foliensätze 01 bis 08* \[Vorlesungsfolien\], V02 F. 12 und F. 28 bis 30. Lehrstuhl für Fluidverfahrenstechnik, Universität Paderborn.

## Aufgabe 2: Kühlhauswand

- **Wärmeleitfähigkeit von Stahlbeton λ~B~ = 2,3 W/(m K)** (Tabelle): Bemessungswert für Stahlbeton mit 1 % Bewehrung nach DIN EN ISO 10456, so im Pilotskript `pilot_tutorium1.py` angegeben. Die Norm wurde nicht eingesehen; die Prüfung ist im Pilotblatt als offen vermerkt.
- **Wärmeleitfähigkeit von Hartschaum aus Polyurethan λ~D~ = 0,025 W/(m K)** (Tabelle): Arbeitswert des Pilotblatts; Prüfung gegen DIN 4108-4 bzw. DIN EN ISO 10456 laut Pilotblatt offen.
- **Dicken 20 cm und 12 cm, Oberflächentemperaturen 28 °C und −22 °C, Fläche 250 m², Grenzwert 8 W/m²** (Ausgangssituation, Tabelle): frei gewählte Arbeitswerte des Pilotblatts (Teil 3, technische Zwillingsaufgabe).

## Zusatzaufgabe 1: Erdwärme in Deutschland

- **Kontinentale Tiefbohrung (KTB) in der Oberpfalz, Endteufe 9101 m**: GFZ Helmholtz-Zentrum für Geoforschung. (2024). *Der Tiefpunkt in Deutschland feierte Jubiläum* \[Meldung zur KTB\]. <https://www.gfz.de/en/press/news/details/der-tiefpunkt-in-deutschland-feierte-jubilaeum>
- **Temperaturgradient etwa 28 K/km**: GFZ (2024), wie oben; Smellie, J. (2004). \[Titel nicht erfasst\] (SKB-Bericht R-04-09). Svensk Kärnbränslehantering. <https://skb.com/publication/21179/R-04-09.pdf>
- **Wärmeleitfähigkeit des Gesteins etwa 2,9 W/(m K)**: Arbeitswert der Ideensammlung, Abschnitt 4.1 (dort zusammen mit GFZ und Smellie, 2004, genannt; ein eigener Beleg für diesen Wert ist nicht ausgewiesen).
- **Weltweites Mittel rund 0,09 W/m²** (Teil b): Davies & Davies (2010), siehe Aufgabe 1.

## Herkunft der Fragen

- Frage 1 (Vorab-Frage Firn oder Eis): Pilotblatt Tutorium 1 und Ideensammlung, Abschnitt 4.1 (Entscheidung D52).
- Frage 2 (Einheiten-Check): Pilotblatt, Zusatzaufgabe 2.1. Hintergrund zur Verwechslung von Wärme und Temperatur: Prince, M., Vigeant, M., & Nottis, K. (2012). Development of the Heat and Energy Concept Inventory: Preliminary results on the prevalence and persistence of engineering students’ misconceptions. *Journal of Engineering Education, 101*(3), 412 bis 438. <https://doi.org/10.1002/j.2168-9830.2012.tb00056.x>
- Frage 3 (Temperaturprofile lesen): Pilotblatt, Zusatzaufgabe 2.2; Abb. 2 neu gezeichnet nach dem Grafikskript des Pilotblatts (`pilot_t1_grafiken.py`, 17.10.2026).
