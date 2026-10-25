> Lehrstuhl-Tutorium 5 „Bilanzen Teil I“ (bisherige Fassung) mit Lösung des Lehrstuhls: Einleitung und Aufgabe 1 „Instationäre globale Energiebilanz“. Im Original folgen Aufgabe 2 „differentielle Energiebilanzen“ und Aufgabe 3 „Instationäre differentielle Energiebilanzen“ (hier nicht enthalten).

**<u>Tutorium 5 – Bilanzen Teil I</u>**

*Mit einer Energiebilanz lassen sich örtliche und / oder zeitliche Temperaturverläufe bestimmen. Für eine Energiebilanz muss zunächst der Bilanzraum festgelegt werden. Wie dieser zu definieren ist, hängt individuell von der Fragestellung ab. Der Bilanzraum kann sehr klein gewählt werden (differentiell klein), um einen örtlichen Temperaturverlauf zu bestimmen oder dieser kann auch vergleichsweise groß (global) definiert werden, wenn beispielsweise der zeitliche Temperaturverlauf des Inhalts eines Rührkessels gefragt ist. Die Energiebilanz kann als Energiegleichung oder Enthalpiegleichung vereinfacht wie folgt formuliert werden:*

| $$\frac{\partial U}{\partial t} = {\dot{H}}_{zu} - {\dot{H}}_{ab} + {\dot{Q}}_{zu} - {\dot{Q}}_{ab} + {\dot{E}}_{q}\ \ \ \ \ \ \ \ \ \ \ (V = konst.,\ p\ variabel)$$ | (4‑1) |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| $$\frac{\partial H}{\partial t} = {\dot{H}}_{zu} - {\dot{H}}_{ab} + {\dot{Q}}_{zu} - {\dot{Q}}_{ab} + {\dot{E}}_{q}\ \ \ \ \ \ \ \ \ \ \ (p = konst.,\ V\ variabel)$$ | (4‑2) |

*Darin ist* ${\dot{H}}_{zu/ab}$ *der jeweilige zugeführte bzw. abgeführt Enthalpiestrom (Energietransport durch die Bewegung von Materie),* ${\dot{Q}}_{zu/ab}$ *der jeweilige zugeführt bzw. abgeführte Wärmestrom, und* ${\dot{E}}_{q}\ $ *ist ein Quellterm, der beispielsweise bei Wärmeproduktion von Reaktionswärme zutragen kommt. Entsprechend der Fragestellung wird Gleichung (4‑1) oder (4‑2) herangezogen und vereinfacht. Beispielweise entfallen die Terme der Enthalpieströme, wenn kein Materietransport stattfindet (in geschlossenen Systemen). Entsprechend der Problemstellung werden für die Wärmeströme das Fourier’sche Gesetz, das Newton’sche Gesetz oder Gleichungen für den Wärmedurchgang verwendet, um den Wärmestrom zu beschreiben. Dies soll nun in den folgenden zwei Abschnitten näher betrachtet werden.*

*Vereinfachend wollen wir im Folgenden instationäre Energiebilanzen für globale bzw. makroskopische Bilanzräume (Rührkessel, Behälter, Reaktoren…) betrachten, bei denen uns eine räumliche Temperaturverteilung nicht interessiert. Achten Sie darauf, wo Wärme- und Enthalpieströme in das System ein- und austreten und wie genau diese Ströme definiert sind (fließt der Wärmestrom durch die Mantelfläche oder durch die Querschnittsfläche…).*

*Da es sich hier um grundlegende Aufgabentypen handelt, sollen Werte, wie der Wärmeübergangskoeffizient, nicht berechnet werden. Komplexere Aufgabentypen werden später betrachtet.  
*

Aufgabe 1 – Instationäre globale Energiebilanz

**a)** Ein Rührkessel mit dem Volumen $V = 2m³$ wird aufgrund des Rührers als ideal durchmischt betrachtet (keine räumlichen Temperaturunterschiede). In den Rührkessel tritt ein Massenstrom von $\dot{m} = 5\frac{kg}{s}$ eines Gemisches bei $T_{ein} = 78{^\circ}C$ ein. Am Austritt wird ebenfalls ein Massenstrom von $\dot{m} = 5\frac{kg}{s}$ abgezogen, wobei die Temperatur der Gemischtemperatur im Rührkessel entspricht. Zu Beginn bei $t = 0s$ habe das Gemisch im Rührkessel eine Temperatur von $T_{0} = 25{^\circ}C$.

Die Stoffdaten seien nicht temperaturabhängig: $\rho = 875\frac{kg}{m^{3}};\ c_{p} = 3500\frac{J}{kgK}$.

a1) Stellen Sie zunächst die Energiebilanz auf. Welche Ströme treten ein, welche Ströme treten aus? $\rho Vc_{p} \bullet \frac{dT}{dt} = \dot{m}c_{p}T_{ein} - \dot{m}c_{p}T_{(t)}$

a3) Wie lautet die Randbedingung? Lösen Sie die DGL mittels Trennung der Variablen oder der Gl. Nr. 1.2 aus der Formelsammlung $T(t) = 351,15K - 53K \bullet \exp\left( - 0,0025\frac{1}{s}\ t \right)$

<u>Lösung:</u>

a1) Enthalpiebilanz, da p = const.

<table>
<colgroup>
<col style="width: 85%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><span class="math display">$$\frac{\partial H}{\partial t} = {\dot{H}}_{zu} - {\dot{H}}_{ab}\ \ \ \ \ \ \ \ \ \ \ (p = konst.,\ V\ variabel)$$</span></th>
<th>(1)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><span class="math display"><em>Ḣ</em><sub><em>e</em><em>i</em><em>n</em></sub>= <em>ṁ</em><em>c</em><sub><em>p</em></sub><em>T</em><sub><em>e</em><em>i</em><em>n</em></sub></span></p>
<p><span class="math display"><em>Ḣ</em><sub><em>a</em><em>u</em><em>s</em></sub>= <em>ṁ</em><em>c</em><sub><em>p</em></sub><em>T</em><sub>(<em>t</em>)</sub></span></p></td>
<td></td>
</tr>
<tr class="even">
<td><span class="math display">$$\rho Vc_{p} \bullet \frac{dT}{dt} = \dot{m}c_{p}T_{ein} - \dot{m}c_{p}T_{(t)}$$</span></td>
<td>(2)</td>
</tr>
</tbody>
</table>

a2)

<table>
<colgroup>
<col style="width: 85%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><span class="math display"><em>R</em><em>B</em>:          <em>T</em>(<em>t</em>=0<em>s</em>) = <em>T</em><sub>0</sub></span></th>
<th>(3)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span class="math display">$$\frac{dT}{dt} + \frac{\dot{m}}{\rho V}T_{(t)} = \frac{\dot{m}}{\rho V}T_{ein}$$</span></td>
<td></td>
</tr>
<tr class="even">
<td><span class="math display">$$T(t) = T_{ein} + C \bullet \exp\left( - \frac{\dot{m}}{\rho V}t \right)$$</span></td>
<td>(4)</td>
</tr>
<tr class="odd">
<td><p><span class="math display"><em>T</em>(<em>t</em>=0<em>s</em>) = <em>T</em><sub>0</sub>= <em>T</em><sub><em>e</em><em>i</em><em>n</em></sub> + <em>C</em></span></p>
<p><span class="math display"><em>C</em> = <em>T</em><sub>0</sub>− <em>T</em><sub><em>e</em><em>i</em><em>n</em></sub> </span></p></td>
<td></td>
</tr>
<tr class="even">
<td><p><span class="math display">$$T(t) = T_{ein} + \left( T_{0} - \ T_{ein} \right) \bullet \exp\left( - \frac{\dot{m}}{\rho V}t \right)$$</span></p>
<p><span class="math display">$$T(t) = 351,15K - 53K \bullet \exp\left( - 0,0025\frac{1}{s}\ t \right)$$</span></p></td>
<td></td>
</tr>
</tbody>
</table>

**b)** Der Rührkessel wird nun kontinuierlich über einen Kühlmantel gekühlt. Die Ein- und Austrittswerte bleiben unverändert. Das Kühlmedium hat eine konstante Temperatur von  
$T_{K} = 30{^\circ}C$. Der Kühlmantel habe eine Kontaktfläche zum Rührkessel von $A_{K} = 6m²$ und der Wärmedurchgangs-koeffizient ist mit $k = 500\frac{W}{m^{2}K}$ gegeben.

b1) Stellen Sie zunächst die Energiebilanz auf. Wie ist die Temperaturdifferenz für den Kühlmantelwärmestrom zu definieren, wenn dieser mit negativem Vorzeichen in die Bilanz eingeht? $\rho Vc_{p} \bullet \frac{dT}{dt} = \dot{m}c_{p}T_{ein} - \dot{m}c_{p}T_{(t)} - {kA}_{k}(T_{(t)} - T_{K})$

b2) Wie lautet die Randbedingung? Lösen Sie die DGL. $T(t) = 70,96K - 46K \bullet \exp\left( - 0,0033\frac{1}{s}\ t \right)$

b3) Berechnen Sie für Aufgabenteil 4.1 a) und 4.1 b) jeweils die Temperatur im Rührkessel nach 1h. $a)\ T \approx 78{^\circ}C\ \ \ \ \ \ \ \ b)\ T \approx 71{^\circ}C$

<u>Lösung:</u>

b1) Enthalpiebilanz, da p = const.

| $$\frac{\partial H}{\partial t} = {\dot{H}}_{zu} - {\dot{H}}_{ab}\ \  - {\dot{Q}}_{k}\ \ \ \ \ \ \ \ (p = konst.,\ V\ variabel)$$ | (10‑7) |
|-----------------------------------------------------------------------------------------------------------------------------------|--------|
| $$\rho Vc_{p} \bullet \frac{dT}{dt} = \dot{m}c_{p}T_{ein} - \dot{m}c_{p}T_{(t)} - {kA}_{k}(T_{(t)} - T_{K})$$                     | (10‑8) |

b2)

<table>
<colgroup>
<col style="width: 85%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><span class="math display"><em>R</em><em>B</em>:          <em>T</em>(<em>t</em>=0<em>s</em>) = <em>T</em><sub>0</sub></span></th>
<th>(10‑7)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span class="math display">$$\frac{dT}{dt} = \frac{\dot{m}}{\rho V}\ T_{ein} - \frac{\dot{m}}{\rho V}T_{(t)} - \frac{{kA}_{k}}{\rho Vc_{p}}\ T_{(t)} + \frac{{kA}_{k}}{\rho Vc_{p}}T_{K}$$</span></td>
<td></td>
</tr>
<tr class="even">
<td><span class="math display">$$\frac{dT}{dt} + \left( \frac{\dot{m}}{\rho V} + \frac{{kA}_{k}}{\rho Vc_{p}}\  \right)T_{(t)} = \frac{\dot{m}}{\rho V}T_{ein} + \frac{{kA}_{k}}{\rho Vc_{p}}T_{K}$$</span></td>
<td></td>
</tr>
<tr class="odd">
<td><span class="math display">$$\frac{b}{a} = \frac{\dot{m}T_{ein} + \frac{kA_{k}}{c_{p}}T_{K}}{\dot{m} + \frac{kA_{k}}{c_{p}}} = 70,96K$$</span></td>
<td>(10‑8)</td>
</tr>
<tr class="even">
<td><p><span class="math display">$$T(t = 0s) = T_{0} = \ \frac{\dot{m}T_{ein} + \frac{kA_{k}}{c_{p}}T_{K}}{\dot{m} + \frac{kA_{k}}{c_{p}}} + C$$</span></p>
<p><span class="math display">$$C = T_{0} - \ \frac{\dot{m}T_{ein} + \frac{kA_{k}}{c_{p}}T_{K}}{\dot{m} + \frac{kA_{k}}{c_{p}}} = \  - 46K$$</span></p></td>
<td></td>
</tr>
<tr class="odd">
<td><span class="math display">$$T(t) = 70,96K - 46K \bullet \exp\left( - 0,0033\frac{1}{s}\ t \right)$$</span></td>
<td></td>
</tr>
</tbody>
</table>

b3)

<table>
<colgroup>
<col style="width: 85%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><ol type="a">
<li><p><span class="math inline"><em>T</em>(3600<em>s</em>) ≈ 78<sup>∘</sup><em>C</em></span></p></li>
<li><p><span class="math inline"><em>T</em>(3600<em>s</em>) ≈ 71<sup>∘</sup><em>C</em></span></p></li>
</ol></th>
<th>(10‑7)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**c)** In einem Reaktor mit dem Volumen $V_{R} = 5m³$ findet eine exotherme Reaktion statt, welche die volumenspezifische Reaktionsenthalpie $\Delta h_{R} = 25000\frac{W}{m^{3}}$ als Reaktionswärme freisetzt. Um nicht zu überhitzen, wird der Reaktor über einen Kühlmantel mit $kA = 2250\frac{W}{K}$ mit der konstanten Kühlmitteltemperatur $T_{K} = 10{^\circ}C$ gekühlt. Am Eintritt tritt das Reaktionsgemisch mit einer Temperatur $T_{ein} = 30{^\circ}C$, einem Massenstrom $\dot{m} = 5\frac{kg}{s}$ und der spez. Wärmekapazität $c_{p_{ein}}$ ein. Am Austritt tritt ein Massenstrom von $\dot{m} = 5\frac{kg}{s}$ aus und habe den gleichen Zustand wie das Gemisch im Reaktor ($c_{p_{R}},\ T_{R}$). Der Reaktor sei ideal durchmischt.

Stoffdaten:

| $$\rho_{R} = 700\frac{kg}{m^{3}}$$ | $$c_{p_{ein}} = 4000\frac{J}{kgK}$$ | $$c_{p_{R}} = 3000\frac{J}{kgK}$$ |     |
|------------------------------------|-------------------------------------|-----------------------------------|-----|

c1) Stellen Sie die instationäre Energiebilanz auf. Welche Wärme-, Enthalpieströme und Quellterme sind zu berücksichtigen?

$${\dot{H}}_{ein} = \ \dot{m}c_{p}T_{ein};\ {\dot{H}}_{aus} = \ \dot{m}c_{p}T_{(t)};\ {\dot{Q}}_{k} = \ kA\left( T_{(t)} - T_{K} \right);\ E_{q} = \Delta h_{R}V$$

$$\rho_{R}Vc_{p,R} \bullet \frac{dT}{dt} = \dot{m}c_{p,ein}T_{ein} - \dot{m}c_{p,R}T_{(t)} - kA\left( T_{(t)} - T_{K} \right) + \Delta h_{R}V$$

c2) Bringen Sie die Gleichung in die Form $\frac{dT}{dt} + aT = b$ und lösen Sie die DGL für die Anfangstemperatur von$\ T_{0} = 10{^\circ}C$. $T(t) = 395,5K - 112,5K \bullet \exp\left( - 0,00164\frac{1}{s}\ t \right)$

c3) Ermitteln Sie ausgehend von der Energiebilanz in c1) eine Gleichung zur Berechnung des stationären Endwertes und berechnen Sie diesen. $T = \ \frac{\dot{m}\ c_{p,ein}T_{ein} + kAT_{K} + \Delta h_{R}V}{\dot{m}\ c_{p,R} + kA}$

<u>Lösung:</u>

c1) Enthalpiebilanz, da p = const.

| $$\frac{\partial H}{\partial t} = {\dot{H}}_{ein} - {\dot{H}}_{ab}\ \  - {\dot{Q}}_{k} + E_{q}\ \ \ \ \ \ \ (p = konst.,\ V\ variabel)$$                           | (10‑7) |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| $${\dot{H}}_{ein} = \ \dot{m}c_{p}T_{ein};\ {\dot{H}}_{aus} = \ \dot{m}c_{p}T_{(t)};\ {\dot{Q}}_{k} = \ kA\left( T_{(t)} - T_{K} \right);\ E_{q} = \Delta h_{R}V$$ |        |
| $$\rho_{R}Vc_{p,R} \bullet \frac{dT}{dt} = \dot{m}c_{p,ein}T_{ein} - \dot{m}c_{p,R}T_{(t)} - kA\left( T_{(t)} - T_{K} \right) + \Delta h_{R}V$$                    | (10‑8) |

c2)

<table>
<colgroup>
<col style="width: 85%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><span class="math display"><em>R</em><em>B</em>:          <em>T</em>(<em>t</em>=0<em>s</em>) = <em>T</em><sub>0</sub></span></th>
<th>(10‑7)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span class="math display">$$\frac{dT}{dt} + \frac{\dot{m}\ c_{p,R} + kA\ }{\rho_{R}Vc_{p,R}}\ T = \ \frac{\dot{m}\ c_{p,ein}T_{ein} + kAT_{K} + \Delta h_{R}V\ }{\rho_{R}Vc_{p,R}}$$</span></td>
<td></td>
</tr>
<tr class="even">
<td><span class="math display">$$\frac{b}{a} = \frac{\dot{m}\ c_{p,ein}T_{ein} + kAT_{K} + \Delta h_{R}V}{\dot{m}\ c_{p,R} + kA} = 395,5K$$</span></td>
<td>(10‑8)</td>
</tr>
<tr class="odd">
<td><p><span class="math display">$$T(t = 0s) = T_{0} = \frac{b}{a} + C$$</span></p>
<p><span class="math display"><em>C</em> = <em>T</em><sub>0</sub>− 395, 5<em>K</em>=  − 112, 5<em>K</em></span></p></td>
<td></td>
</tr>
<tr class="even">
<td><span class="math display">$$T(t) = 395,5K - 112,5K \bullet \exp\left( - 0,00164\frac{1}{s}\ t \right)$$</span></td>
<td></td>
</tr>
</tbody>
</table>

c3)

<table>
<colgroup>
<col style="width: 85%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span class="math display">$$stationär:\frac{d}{dt} = 0$$</span></p>
<p><span class="math display">0 = <em>ṁ</em><em>c</em><sub><em>p</em>, <em>e</em><em>i</em><em>n</em></sub><em>T</em><sub><em>e</em><em>i</em><em>n</em></sub> − <em>ṁ</em><em>c</em><sub><em>p</em>, <em>R</em></sub><em>T</em> − <em>k</em><em>A</em>(<em>T</em>−<em>T</em><sub><em>K</em></sub>) + <em>Δ</em><em>h</em><sub><em>R</em></sub><em>V</em></span></p>
<p><span class="math display">$$T = \ \frac{\dot{m}\ c_{p,ein}T_{ein} + kAT_{K} + \Delta h_{R}V}{\dot{m}\ c_{p,R} + kA}$$</span></p>
</blockquote></th>
<th>(10‑7)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
