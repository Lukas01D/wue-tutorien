> Lösung des Lehrstuhls zu Tutorium 3, Aufgabe 3.

**<u>Aufgabe 3</u>** (Klausur 2022-02-17)

Ein 16m² großer Wohnraum mit zwei außenliegenden Wänden wird durch eine Fußbodenheizung beheizt. Der Raum hat eine quadratische Grundfläche mit den Maßen 4m x 4m x 2,4m (L x B x H). Einen schematischen Aufbau der Fußbodenheizung zeigt Abb. 2. Dabei wird vereinfacht angenommen, dass anstelle einzelner Rohre, ein ebener Kanal mit Heizungswasser unter einer Schicht Estrichbeton liegt.

<img src="media/T3L_1.png" style="width:4.24183in;height:2.52209in" alt="Ein Bild, das Tisch enthält. Automatisch generierte Beschreibung" />

**Abb. 2:** Vereinfachter Schichtaufbau der Fußbodenheizung

Das Heizungswasser gibt kontinuierlich Wärme an den Estrichbeton ab. Dieser fungiert auch als Wärmespeicher und gibt die Wärme nach und nach an die Raumluft ab und hält so die Raumtemperatur auf einer konstanten Temperatur $\vartheta_{R}$.

| ***Daten zur Raumluftluft:***   |                                       | ***Fußbodenheizung:***                |                                   |
|---------------------------------|---------------------------------------|---------------------------------------|-----------------------------------|
| Temperatur:                     | $\vartheta_{R} = 20{^\circ}C$         | Oberflächentemperatur:                | $\vartheta_{B} = 22{^\circ}C$     |
| Dynamische Viskosität:          | $\eta_{L} = 1,82 \cdot 10^{- 5}Pa\ s$ | Estrichbeton Dicke:                   | $\delta_{E} = 0,07m$              |
| Wärmeleitfähigkeit:             | $\lambda_{L} = 0,0259\frac{W}{mK}$    | Wärmeleitfähigkeit Estrichbeton:      | $\lambda_{E} = 0,2\frac{W}{mK}$   |
| Spez. Wärmekapazität:           | $c_{p,L} = 1006\frac{J}{kgK}$         | Wärmeübergangskoeffizient Heizwasser: | $\alpha_{W} = 10\frac{W}{m^{2}K}$ |
| Dichte:                         | $\rho_{L} = 1,205\frac{kg}{m^{3}}$    |                                       |                                   |
|                                 |                                       |                                       |                                   |
| ***Daten zu den Außenwänden:*** |                                       | ***Heizkörper:***                     |                                   |
| Wärmedurchgangskoeffizient:     | $k_{wand} = 0,75\frac{W}{m^{2}K}$     | Oberflächentemperatur:                | $\vartheta_{HK} = 50{^\circ}C$    |
| Umgebungstemperatur:            | $\vartheta_{u} = 5{^\circ}C$          | Breite:                               | $B_{HK} = 1,2m$                   |
|                                 |                                       | Höhe:                                 | $H_{HK} = 0,5m$                   |

Aufgaben:

1)  Berechnen Sie den Wärmeübergangskoeffizienten $\alpha_{B}$ für den Übergang Fußboden-Raumluft. Gehen Sie davon aus, dass man den beheizten Fußboden als gute Näherung als waagerechte Platte ($L = B$) betrachten kann. Gehen Sie nur für Berechnung des Wärmeübergangskoeffizienten davon aus, dass der Fußboden eine Oberflächentemperatur von $\vartheta_{B} = 22{^\circ}C$ hat.

*Ersatzergebnis:* $\alpha_{B} = 1,8\frac{W}{m^{2}K}$

2)  Näherungsweise betrachten wir den Aufbau der Fußbodenheizung wie in Abb. 2 dargestellt. Die untere Schicht sei Heizungswasser, welches eine konstante Temperatur $\vartheta_{W}$ habe. Darüber liegt eine Schicht Estrichbeton ($\lambda_{E} = 0,2\frac{W}{mK}$) der Stärke $\delta_{E} = 0,07m$, durch welche die Wärme an die Raumluft übertragen wird. Der Wärmeübergangskoeffizient Heizungswasser-Estrichbeton ist mit $\alpha_{W} = 10\frac{W}{m^{2}K}$ bekannt. Berechnen Sie den Wärmedurchgangskoeffizienten $k_{B}$ von dem Heizungswasser zur Raumluft.

*Ersatzergebnis:* $k_{B} = 1\frac{W}{m^{2}K}$

3)  Der betrachtete Raum hat zwei Außenwände, über welche konstant Wärme abgegeben wird. Der Wärmedurchgangskoeffizient der Außenwände ist mit $k_{wand} = 0,75\frac{W}{m^{2}K}$ gegeben. Berechnen Sie welche Temperatur das Heizungswasser $\vartheta_{W}$ haben muss, damit bei einer Außentemperatur von $\vartheta_{u} = 5{^\circ}C$ die Raumtemperatur konstant bei $\vartheta_{R} = 20{^\circ}C$ bleibt. Nutzen Sie dazu den Wärmedurchgangskoeffizienten $k_{B}$ aus dem vorherigen Aufgabenteil.

4)  Nun wird die Fußbodenheizung mit einem Flachheizkörper der Breite $B_{HK} = 1,2m$ und Höhe $H_{HK} = 0,5m$ verglichen. Der Heizkörper wird in einem baugleichen Raum nah an der Wand angebracht, sodass angenommen wird, dass zur Wärmeübertragung nur eine Fläche von $A_{HK} = 1,5 \cdot B_{HK}H_{HK}$ effektiv genutzt wird.

    1.  Berechnen Sie den Wärmeübergangskoeffizienten $\alpha_{HK}$ für den Übergang Heizkörper-Raumluft. Gehen Sie nur für die Berechnung des Wärmeübergangskoeffizienten davon aus, dass der Heizkörper eine Oberflächentemperatur von  
        $\vartheta_{HK} = 50{^\circ}C$ hat.

> *Ersatzergebnis:* $\alpha_{HK} = 3,75\frac{W}{m^{2}K}$

2.  Um wieviel Grad heißer muss die Heizwassertemperatur $\vartheta_{W,HK}$ im Heizkörper im Vergleich zur Fußbodenheizung sein, wenn die Raumtemperatur ebenfalls konstant bei $\vartheta_{R} = 20{^\circ}C$ bleiben soll? Für den Wärmedurchgangskoeffizient vom Heizungswasser zur Raumtemperatur kann folgende Annahme getroffen werden: $k_{HK} \approx \alpha_{HK}$.

**<u>Lösung:</u>**

**<u>a)</u>**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><span class="math display">$$\Pr{= \frac{\eta_{L}c_{P,L}}{\lambda_{L}}} = 0,71$$</span></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span class="math display">$${Gr}{= \frac{g\beta_{th}\Delta TL^{3}}{\nu^{2}}} = 1,88 \bullet 10^{10}$$</span></td>
</tr>
<tr class="even">
<td><span class="math display">$$f\left( \Pr \right) = \ \left\lbrack 1 + \left( \frac{0,322}{\Pr} \right)^{\frac{11}{20}} \right\rbrack^{- \frac{20}{11}} = 0,4028$$</span></td>
</tr>
<tr class="odd">
<td><span class="math display"><em>G</em><em>r</em> • <em>P</em><em>r</em> • <em>f</em>(Pr) = 5, 35 • 10<sup>9</sup> &gt; 7 • 10<sup>4</sup></span></td>
</tr>
<tr class="even">
<td>Freie Konvektion über waagerechte Platte, Turbulent:<br />
<span class="math display">$$Nu = 0,15 \bullet \left\lbrack Gr \bullet Pr \bullet f\left( \Pr \right) \right\rbrack^{\frac{1}{3}} = 262,3$$</span></td>
</tr>
<tr class="odd">
<td><span class="math display">$$\alpha_{B} = \frac{\lambda_{L}Nu}{L} = 1,6984\frac{W}{m^{2}K}$$</span></td>
</tr>
</tbody>
</table>

**<u>b)</u>**

| $$R_{th} = R_{W} + R_{E} + R_{B}$$                                                                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------|
| $$R_{W} = \frac{1}{\alpha_{W}A}$$                                                                                                               |
| $$R_{E} = \frac{\delta_{E}}{\lambda_{E}A}$$                                                                                                     |
| $$R_{B} = \frac{1}{\alpha_{B}A}$$                                                                                                               |
| $$k_{B} = \frac{1}{R_{th}A} = \frac{1}{\frac{1}{\alpha_{W}} + \frac{\delta_{E}}{\lambda_{E}} + \frac{1}{\alpha_{B}}} = 0,9626\frac{W}{m^{2}K}$$ |

**<u>c)</u>**

| $$\frac{dU}{dt} = \ {\dot{Q}}_{B} - {\dot{Q}}_{Wand} = 0$$                                                         |
|--------------------------------------------------------------------------------------------------------------------|
| $$k_{B}A_{B}\left( T_{B} - T_{U} \right) - k_{Wand}A_{Wand}\left( T_{R} - T_{U} \right) = \ 0$$                    |
| $$T_{W,B} = T_{R} + \frac{k_{Wand}A_{Wand}}{k_{B}A_{B}}\left( T_{R} - T_{U} \right) = \ 307,17K = 34,02{^\circ}C$$ |

**<u>d)</u>**

**1) Freie Konvektion an Senkrechter Platte**

| $$\Pr{= \frac{\eta_{L}c_{P,L}}{\lambda_{L}}} = 0,71 > 10^{- 3}$$                                                                              |     |
|-----------------------------------------------------------------------------------------------------------------------------------------------|-----|
| $${Gr}{= \frac{g\beta_{th}\Delta TL^{3}}{\nu^{2}}} = 5,5 \bullet 10^{8}$$                                                                     |     |
| $$10^{- 1} < Gr \bullet \Pr{= 3,98\  \bullet 10^{8}} < 10^{12}$$                                                                              |     |
| $$f\left( \Pr \right) = \ \left\lbrack 1 + \left( \frac{0,492}{\Pr} \right)^{\frac{9}{16}} \right\rbrack^{- \frac{16}{9}} = 0,3464$$          |     |
| $$Gr \bullet Pr \bullet f\left( \Pr \right) = 5,35 \bullet 10^{9} > 7 \bullet 10^{4}$$                                                        |     |
| $$Nu = \left( {0,825 + 0,387 \bullet \left\lbrack Gr \bullet Pr \bullet f\left( \Pr \right) \right\rbrack}^{\frac{1}{6}} \right)^{2} = 91,9$$ |     |
| $$\alpha_{HK} = \frac{\lambda_{L}Nu}{L} = 4,7609\frac{W}{m^{2}K}$$                                                                            |     |

**2)**

| $$T_{HK} = T_{R} + \frac{k_{W}A_{W}}{k_{HK}A_{HK}}\left( T_{R} - T_{U} \right) = \ 343,56K = 70,41{^\circ}C$$ |
|---------------------------------------------------------------------------------------------------------------|
| $$\Delta T = T_{W,HK} - T_{W,B} = 36,39K$$                                                                    |
