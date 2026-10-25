> Formelsammlung Wärmeübertragung 2026 des Lehrstuhls (Textfassung; das Original-PDF liegt in der Projektablage).

**Dimensionslose Kennzahlen**

| **Kennzahl**  | **Formulierung**                                        | **Bedeutung**                            |
|---------------|---------------------------------------------------------|------------------------------------------|
| Reynolds-Zahl | $$Re = \frac{\rho\ w\ L}{\eta}$$                        | $$\frac{Trägheit}{Reibung}$$             |
| Grashof-Zahl  | $$Gr = \frac{g\ \beta_{th}\ \Delta T\ L^{3}}{\nu^{2}}$$ | $$\frac{Auftrieb,Trägheit}{Reibung}$$    |
| Nußelt-Zahl   | $$Nu = \frac{\alpha\ L}{\lambda}$$                      | $$\frac{Wärmekonvektion}{Wärmeleitung}$$ |
| Prandtl-Zahl  | $$\Pr = \frac{\nu}{a} = \frac{\eta\ c_{p}}{\lambda}$$   | $$\frac{Reibung}{Wärmeleitung}$$         |

$L$: Charakteristische Länge

Für ideales Gas*:* $\beta_{th} = \frac{1}{T_{u}}\ $, $\Delta T > 0$

**Korrelationen zur Berechnung der *Nußelt*-Zahl** (Stoffwerte beziehen sich auf $T_{m}$)

1.  **Freie Konvektion**

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 41%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Geometrie</strong></th>
<th><strong>Strömungsform</strong></th>
<th><strong>Korrelation</strong></th>
<th><strong>Gültigkeitsbereich</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Senkrechte</strong></p>
<p><strong>Platte</strong></p></td>
<td>Alle</td>
<td><p><span class="math display">$$Nu_{m} = \left\lbrack 0,825 + 0,387\left( Gr\ Prf(Pr) \right)^{\frac{1}{6}} \right\rbrack^{2}$$</span></p>
<p><span class="math display">$$f\left( \Pr \right) = \left\lbrack 1 + \left( \frac{0,492}{\Pr} \right)^{\frac{9}{16}} \right\rbrack^{\frac{- 16}{9}}$$</span></p></td>
<td><p><span class="math display">10<sup>−1</sup> &lt; <em>G</em><em>r</em> <em>P</em><em>r</em> &lt; 10<sup>12</sup></span></p>
<p><span class="math display">10<sup>−3</sup> &lt; <em>P</em><em>r</em></span></p></td>
</tr>
<tr class="even">
<td><p><strong>Waagerechte</strong></p>
<p><strong>Platte</strong></p></td>
<td>Laminar</td>
<td><p><span class="math display">$$Nu_{l} = 0,766\left\lbrack Gr\ Pr\ f\left( \Pr \right) \right\rbrack^{\frac{1}{5}}$$</span></p>
<p><span class="math display">$$f\left( \Pr \right) = \left\lbrack 1 + \left( \frac{0,322}{\Pr} \right)^{\frac{11}{20}} \right\rbrack^{\frac{- 20}{11}}$$</span></p></td>
<td><span class="math display"><em>G</em><em>r</em> <em>P</em><em>r</em> <em>f</em>(Pr) ≤ 7 ⋅ 10<sup>4</sup></span></td>
</tr>
<tr class="odd">
<td><p><strong>Waagerechte</strong></p>
<p><strong>Platte</strong></p></td>
<td>Turbulent</td>
<td><p><span class="math display">$$Nu_{t} = 0,15\left\lbrack Gr\ Pr\ f\left( \Pr \right) \right\rbrack^{\frac{1}{3}}$$</span></p>
<p><span class="math display">$$f\left( \Pr \right) = \left\lbrack 1 + \left( \frac{0,322}{\Pr} \right)^{\frac{11}{20}} \right\rbrack^{\frac{- 20}{11}}$$</span></p></td>
<td><span class="math display"><em>G</em><em>r</em> <em>P</em><em>r</em> <em>f</em>(Pr) &gt; 7 ⋅ 10<sup>4</sup></span></td>
</tr>
<tr class="even">
<td><p><strong>Waager.</strong></p>
<p><strong>Zylinder</strong></p></td>
<td>Übergangsbereich</td>
<td><p><span class="math display">$$Nu_{m} = \left\lbrack 0,752 + 0,387\left\lbrack Gr\ Pr\ f\left( \Pr \right) \right\rbrack^{\frac{1}{6}} \right\rbrack^{2}$$</span></p>
<p><span class="math display">$$f\left( \Pr \right) = \left\lbrack 1 + \left( \frac{0,559}{\Pr} \right)^{\frac{9}{16}} \right\rbrack^{\frac{- 16}{9}}$$</span></p></td>
<td><p><span class="math display">10<sup>−1</sup> &lt; <em>G</em><em>r</em> <em>P</em><em>r</em> &lt; 10<sup>12</sup></span></p>
<p><span class="math display">10<sup>−3</sup> &lt; <em>P</em><em>r</em></span></p></td>
</tr>
<tr class="odd">
<td><p><strong>Senkr.</strong></p>
<p><strong>Zylinder</strong></p></td>
<td>Alle</td>
<td><span class="math display">$$Nu_{m} = 0,435\frac{h}{d} + Nu_{m,senkr.Platte}$$</span></td>
<td><p><span class="math display">10<sup>−1</sup> &lt; <em>G</em><em>r</em> <em>P</em><em>r</em> &lt; 10<sup>12</sup></span></p>
<p><span class="math display">10<sup>−3</sup> &lt; <em>P</em><em>r</em></span></p></td>
</tr>
<tr class="even">
<td><strong>Kugel</strong></td>
<td>Alle</td>
<td><span class="math display">$$Nu_{m} = 2 + 0,56\left\lbrack Gr\ Pr\ \left( \frac{\Pr}{0,846 + Pr} \right) \right\rbrack^{\frac{1}{4}}$$</span></td>
<td><p><span class="math display">10<sup>−1</sup> &lt; <em>G</em><em>r</em> <em>P</em><em>r</em> &lt; 10<sup>12</sup></span></p>
<p><span class="math display">0, 7 &lt; <em>P</em><em>r</em> &lt; 100</span></p></td>
</tr>
</tbody>
</table>

2.  **Erzwungene Konvektion für um- bzw. überströmte Körper**

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 41%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Geometrie</strong></th>
<th><strong>Strömungsform</strong></th>
<th><strong>Korrelation</strong></th>
<th><strong>Gültigkeitsbereich</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2"><strong>Längsumströmte Platte</strong></td>
<td>Laminar</td>
<td><span class="math display">$$Nu_{l} = 0,664\ \sqrt{Re}\ \sqrt[3]{\Pr}$$</span></td>
<td><p><span class="math display">0, 5 &lt; <em>P</em><em>r</em></span></p>
<p><span class="math display"><em>R</em><em>e</em> &lt; 5 ⋅ 10<sup>5</sup></span></p></td>
</tr>
<tr class="even">
<td>Turbulent</td>
<td><span class="math display">$$Nu_{t} = \frac{0,037Re^{0,8}\Pr}{1 + 2,443Re^{- 0,1}\left( \Pr^{\frac{2}{3}} - 1 \right)}$$</span></td>
<td><p><span class="math display">0, 5 &lt; <em>P</em><em>r</em> &lt; 2000</span></p>
<p><span class="math display">5 ⋅ 10<sup>5</sup> &lt; <em>R</em><em>e</em> &lt; 10<sup>7</sup></span></p></td>
</tr>
<tr class="odd">
<td rowspan="3"><strong>Querumströmter Zylinder</strong></td>
<td>Laminar</td>
<td><span class="math display">$$Nu_{l} = 0,664\ \sqrt{Re}\ \sqrt[3]{\Pr}$$</span></td>
<td><p><span class="math display">0, 5 &lt; <em>P</em><em>r</em> &lt; 2000</span></p>
<p><span class="math display"><em>R</em><em>e</em> &lt; 10<sup>5</sup></span></p></td>
</tr>
<tr class="even">
<td>Turbulent</td>
<td><span class="math display">$$Nu_{t} = \frac{0,037Re^{0,8}\Pr}{1 + 2,443Re^{- 0,1}\left( \Pr^{\frac{2}{3}} - 1 \right)}$$</span></td>
<td><p><span class="math display">0, 5 &lt; <em>P</em><em>r</em> &lt; 2000</span></p>
<p><span class="math display">5 ⋅ 10<sup>5</sup> &lt; <em>R</em><em>e</em> &lt; 10<sup>7</sup></span></p></td>
</tr>
<tr class="odd">
<td>Übergangsbereich</td>
<td><span class="math display">$$Nu_{m} = 0,3 + \sqrt{Nu_{l}^{2} + Nu_{t}^{2}}$$</span></td>
<td><p><span class="math display">0, 5 &lt; <em>P</em><em>r</em> &lt; 2000</span></p>
<p><span class="math display">10<sup>1</sup> &lt; <em>R</em><em>e</em> &lt; 10<sup>7</sup></span></p></td>
</tr>
<tr class="even">
<td rowspan="2"><strong>Kugel</strong></td>
<td>Laminar</td>
<td><span class="math display">$$Nu_{l} = 0,664\ \sqrt{Re}\ \sqrt[3]{\Pr}$$</span></td>
<td><p><span class="math display">0, 5 &lt; <em>P</em><em>r</em></span></p>
<p><span class="math display"><em>R</em><em>e</em> ≤ 10<sup>5</sup></span></p></td>
</tr>
<tr class="odd">
<td>Turbulent</td>
<td><span class="math display">$$Nu_{t} = \frac{0,037Re^{0,8}\Pr}{1 + 2,443Re^{- 0,1}\left( \Pr^{\frac{2}{3}} - 1 \right)}$$</span></td>
<td><p><span class="math display">0, 5 &lt; <em>P</em><em>r</em> &lt; 2000</span></p>
<p><span class="math display">10<sup>6</sup> ≤ <em>R</em><em>e</em> ≤ 10<sup>7</sup></span></p></td>
</tr>
<tr class="even">
<td><strong>Kugel</strong></td>
<td>Übergangsbereich</td>
<td><span class="math display">$$Nu_{m} = 2 + \sqrt{Nu_{l}^{2} + Nu_{t}^{2}}$$</span></td>
<td><p><span class="math display">0, 6 &lt; <em>P</em><em>r</em> &lt; 1000</span></p>
<p><span class="math display">10<sup>0</sup> &lt; <em>R</em><em>e</em> &lt; 10<sup>6</sup></span></p></td>
</tr>
</tbody>
</table>

3.  **Erzwungene Konvektion für durchströmte Körper**

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 41%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Geometrie</strong></th>
<th><strong>Strömungsform</strong></th>
<th><strong>Korrelation</strong></th>
<th><strong>Gültigkeitsbereich</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="3"><strong>Durchströmtes Rohr</strong></td>
<td>Laminar</td>
<td><span class="math display">$$Nu_{l} = \sqrt[3]{49,37 + \left\lbrack 1,615\ \left( Re\ Pr\frac{d}{l} \right)^{\frac{1}{3}} - 0,7 \right\rbrack^{3}}$$</span></td>
<td><p><span class="math display">0 &lt; <em>P</em><em>r</em></span></p>
<p><span class="math display"><em>R</em><em>e</em> &lt; 2300</span></p></td>
</tr>
<tr class="even">
<td>Turbulent</td>
<td><p><span class="math display">$$Nu_{t} = \frac{(\zeta/8)\ Re\ Pr}{1 + 12,7\ \sqrt{\zeta/8}\ \left( \Pr^{\frac{2}{3}} - 1 \right)}\left\lbrack 1 + \left( \frac{d}{l} \right)^{\frac{2}{3}} \right\rbrack$$</span></p>
<p>Mit dem Druckverlustbeiwert:</p>
<p><span class="math inline"><em>ζ</em> = [1,8log<sub>10</sub>(<em>R</em><em>e</em>)−1,5]<sup>−2</sup> </span></p></td>
<td><p><span class="math display">10<sup>−1</sup> &lt; <em>P</em><em>r</em> &lt; 10<sup>3</sup></span></p>
<p><span class="math display">10<sup>4</sup> &lt; <em>R</em><em>e</em> &lt; 10<sup>6</sup></span></p></td>
</tr>
<tr class="odd">
<td>Übergangsbereich</td>
<td><p><span class="math display"><em>N</em><em>u</em><sub><em>m</em></sub> = (1−<em>γ</em>)<em>N</em><em>u</em><sub><em>l</em>, 2300</sub> + <em>γ</em><em>N</em><em>u</em><sub><em>t</em>, 10<sup>4</sup></sub></span></p>
<p><span class="math display"><em>N</em><em>u</em><sub><em>l</em>, 2300</sub> = <em>N</em><em>u</em><sub><em>l</em></sub>(<em>R</em><em>e</em>=2300)</span></p>
<p><span class="math display"><em>N</em><em>u</em><sub><em>t</em>, 10<sup>4</sup></sub> = <em>N</em><em>u</em><sub><em>t</em></sub>(<em>R</em><em>e</em>=10<sup>4</sup>)</span></p>
<p><span class="math display">$$\gamma = \frac{Re - 2300}{10^{4} - 2300}$$</span></p></td>
<td><p><span class="math display">0, 6 &lt; <em>P</em><em>r</em> &lt; 1000</span></p>
<p><span class="math display">2300 &lt; <em>R</em><em>e</em> &lt; 10<sup>4</sup></span></p></td>
</tr>
</tbody>
</table>

4.  **Anströmbedingungen**

Charakteristische Länge $L$ zur Bestimmung der *Nußelt*-Zahlen:

Allgemeine Definition: $L = \frac{A}{U}$ mit $A$: Fläche des Körpers

$U$: Umfang des projizierten Schattens

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 35%" />
<col style="width: 16%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Körper</strong></th>
<th><strong>Strömungsbild</strong></th>
<th><strong>Körper</strong></th>
<th><strong>Strömungsbild</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Längsangeströmte, (unendlich) breite Platte der Länge</strong> <span class="math inline"><strong>L</strong></span></td>
<td><img src="media/FS_1.png" style="width:2.58803in;height:0.65945in" /></td>
<td><strong>Konzentrisches, durchströmtes Rohr mit Durchmesser</strong> <span class="math inline"><strong>d</strong></span></td>
<td><img src="media/FS_2.png" style="width:1.06739in;height:1.03757in" /></td>
</tr>
<tr class="even">
<td><strong>Querumströmte Zylinder mit Durchmesser</strong> <span class="math inline"><strong>d</strong></span></td>
<td><img src="media/FS_3.png" style="width:2.51596in;height:0.98582in" /></td>
<td><strong>Umströmte Kugel mit Durchmesser</strong> <span class="math inline"><strong>d</strong></span></td>
<td><img src="media/FS_4.png" style="width:1.43761in;height:1.13608in" /></td>
</tr>
<tr class="odd">
<td><p><strong>Aufrechter Zylinder</strong></p>
<p><strong>(freie Konvektion)</strong></p></td>
<td><img src="media/FS_5.png" style="width:1.14433in;height:1.68433in" /></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

5.  **Lösung von Differentialgleichungen**

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 31%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><strong>DGL</strong></th>
<th><strong>allgemeine Lösung</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>5.1</strong></td>
<td><span class="math display">$$\frac{dy}{dx} + ay = b$$</span></td>
<td><span class="math display">$$y = \frac{b}{a} + Ce^{- ax}$$</span></td>
</tr>
<tr class="even">
<td><strong>5.2</strong></td>
<td><span class="math display">$$\frac{d^{2}y}{dx^{2}} + a\frac{dy}{dx} + by + c = 0$$</span></td>
<td><p><span class="math display"><strong>F</strong><strong>a</strong><strong>l</strong><strong>l</strong> <strong>1</strong><strong>:</strong>     <em>a</em><sup>2</sup> − 4<em>b</em> &gt; 0:</span></p>
<p><span class="math display">$$y = C_{1}e^{y_{1}x} + C_{2}e^{y_{2}x} - \frac{c}{b}$$</span></p>
<p><span class="math display"><strong>F</strong><strong>a</strong><strong>l</strong><strong>l</strong> <strong>2</strong><strong>:</strong>      <em>a</em><sup>2</sup> − 4<em>b</em> = 0:</span></p>
<p><span class="math display">$$y = \left( C_{1}x + C_{2} \right)e^{- \frac{a}{2}x} - \frac{c}{b}$$</span></p>
<p><span class="math display"><strong>F</strong><strong>a</strong><strong>l</strong><strong>l</strong> <strong>3</strong> : <em>a</em><sup>2</sup> − 4<em>b</em> &lt; 0:</span></p>
<p><span class="math display">$$y = \left( C_{1}\cos(\beta x) + C_{2}\sin{(\beta x)} \right)e^{- \frac{a}{2}x} - \frac{c}{b}$$</span></p>
<p><span class="math display">$$mit:y_{1,2} = - \frac{a}{2} \pm \sqrt{\frac{a^{2}}{4} - b}$$</span></p>
<p><span class="math display">$$und:\beta = \sqrt{\left| \frac{a^{2}}{4} - b \right|}$$</span></p></td>
</tr>
<tr class="odd">
<td><strong>5.3</strong></td>
<td><span class="math display">$$\frac{d^{2}y}{dx^{2}} + a\frac{dy}{dx} + b = 0$$</span></td>
<td><span class="math display">$$y = C_{1}e^{- ax} - \frac{b}{a}x + C_{2}$$</span></td>
</tr>
<tr class="even">
<td><strong>5.4</strong></td>
<td><span class="math display">$$\frac{d^{2}y}{dx^{2}} + ay + b = 0$$</span></td>
<td><p><span class="math display"><strong>F</strong><strong>a</strong><strong>l</strong><strong>l</strong> <strong>1</strong> : <em>a</em> &gt; 0:</span></p>
<p><span class="math display">$$y = C_{1}\cos{\left( \sqrt{a}x \right) + C_{2}\sin{\left( \sqrt{a}x \right) - \frac{b}{a}}}$$</span></p>
<p><span class="math display"><strong>F</strong><strong>a</strong><strong>l</strong><strong>l</strong> <strong>2</strong><strong>:</strong><em>a</em> = 0:</span></p>
<p><span class="math display">$$y = - \frac{b}{2}x^{2} + C_{1}x + C_{2}$$</span></p>
<p><span class="math display"><strong>F</strong><strong>a</strong><strong>l</strong><strong>l</strong> <strong>3</strong> : <em>a</em> &lt; 0:</span></p>
<p><span class="math display">$$y = C_{1}e^{- \sqrt{|a|}x} + C_{2}e^{\sqrt{|a|}x} - \frac{b}{a}$$</span></p></td>
</tr>
</tbody>
</table>
