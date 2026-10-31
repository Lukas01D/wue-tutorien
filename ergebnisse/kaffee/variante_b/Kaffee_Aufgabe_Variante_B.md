---
lang: de
---

::: center
**[Tutorium 5: Wärmebilanzen (instationär global)]{.underline}**
:::

**[Grundlagen]{.underline}** (Energiebilanz: instationär, global)

::: zweispaltig
**Voraussetzung:** Die Temperatur ist im ganzen Kontrollvolumen gleich (homogen) und ändert sich nur mit der Zeit. Das gilt, wenn der Inhalt ideal durchmischt ist oder wenn in einem Festkörper die Wärmeleitung Unterschiede viel schneller ausgleicht, als Wärme über die Oberfläche abgeht (Biot-Zahl $Bi \ll 1$, Foliensatz 02, Folie 16).

**Bilanz** für ein ruhendes Kontrollvolumen ohne innere Wärmequellen (Foliensatz 05, Folie 8), mit der inneren Energie eines inkompressiblen Stoffs mit konstanten Stoffdaten:
$$\frac{dU}{dt} = \dot{Q}_{\mathrm{zu}} - \dot{Q}_{\mathrm{ab}}, \qquad dU = m\,c_p\,dT$$
$m\,c_p$ (in J/K) ist die Wärmekapazität des Inhalts. Die Wärmeabgabe an die Umgebung beschreibt ein Wärmedurchgang:
$$\dot{Q}_{\mathrm{ab}} = kA\,(T - T_\mathrm{u})$$
$kA$ (in W/K), das Produkt aus Wärmedurchgangskoeffizient $k$ und Fläche $A$, ist der abgegebene Wärmestrom je Kelvin Temperaturunterschied zur Umgebung; es fasst alle Wege nach außen zusammen.

**Lösungsweg:** Eingesetzt entsteht eine gewöhnliche DGL erster Ordnung in der Zeit, $dT/dt = f(T)$. Trennung der Variablen: alle Terme mit $T$ auf eine Seite, $dt$ auf die andere, dann vom Anfang ($t = 0$, $T = T_0$) bis zur Zeit $t$ integrieren (zur Kontrolle: Formelsammlung, Kap. 5, Gl. 5.1):
$$\int_{T_0}^{T} \frac{dT}{f(T)} = \int_{0}^{t} dt$$

![](grafik/Bilanzformen_kompakt_3_instationaer_global.png){width=5.2cm}
:::

**[Lernziele]{.underline}**

Nach diesem Tutorium können Sie …

- den Temperaturverlauf $T(t)$ einer ideal durchmischten Flüssigkeit, etwa Kaffee in einer Tasse, aus einer instationären globalen Energiebilanz berechnen.
- mit der Durchmischung oder der Biot-Zahl beurteilen, ob bei einem Abkühlvorgang (Kaffee in der Tasse, Becher in Teil g) eine überall gleiche Temperatur angenommen werden darf.

**[Einführung]{.underline}**

Sonntagmorgen in der WG-Küche: Sie haben Filterkaffee gekocht und zwei gleiche Tassen mit je 200 ml gefüllt. Da klingelt das Telefon, und das Gespräch wird eine Stunde dauern. Ihr Mitbewohner gießt seine Milch sofort in den Kaffee (Tasse 1). Sie stellen Ihre Tasse daneben und wollen die Milch erst nach dem Telefonat hineingießen (Tasse 2), damit der Kaffee „länger heiß bleibt“. Die Milch kommt in beiden Fällen direkt aus dem Kühlschrank.

![](grafik/t5_kaffee_tassen.png){width=92%}

**Abb. 1:** Die beiden Tassen

**Frage 1 (Vorab-Frage):**

Ihr Mitbewohner meint: „Ob man die Milch sofort oder später hineingießt, ist egal. Die Energie bleibt ja erhalten.“ Welche Tasse ist nach einer Stunde wärmer: Tasse 1, Tasse 2, oder sind beide gleich warm? Notieren Sie Ihre Vermutung mit einem Satz Begründung, bevor Sie rechnen.

**[Gegeben]{.underline}**

Um die Frage zu klären, messen Sie nach 10 Minuten die Temperatur in Tasse 2 (noch ohne Milch).

**Annahmen:**

- Der Tasseninhalt ist ideal durchmischt, die Milch mischt sich sofort und ohne Wärmeverlust.
- Die Wärmekapazität der Tasse wird außer in Teil g vernachlässigt.
- Die gesamte Wärmeabgabe (auch durch Strahlung und Verdunstung) ist $\dot{Q}_{\mathrm{ab}} = kA\,(\vartheta - \vartheta_\mathrm{u})$ mit konstantem $kA$; die verdunstete Masse wird vernachlässigt.
- Kaffee (Stoffdaten von Wasser) und Milch sind inkompressibel ($c_p = c_v$); die Stoffdaten sind konstant.

**Werte:**

| **Kaffee** | | **Milch** | |
|:-------------------------------------|:-------------------------------------------|:-------------------------------------|:-------------------------------------------|
| Volumen | $V_\mathrm{K} = 200\,\mathrm{ml}$ | Volumen | $V_\mathrm{M} = 30\,\mathrm{ml}$ |
| Dichte | $\rho_\mathrm{K} = 1000\,\mathrm{kg/m^3}$ | Dichte | $\rho_\mathrm{M} = 1030\,\mathrm{kg/m^3}$ |
| Spez. Wärmekapazität | $c_{p,\mathrm{K}} = 4{,}18\,\mathrm{kJ/(kg\,K)}$ | Spez. Wärmekapazität | $c_{p,\mathrm{M}} = 3{,}94\,\mathrm{kJ/(kg\,K)}$ |
| Anfangstemperatur | $\vartheta_{\mathrm{K},0} = 80\,\mathrm{°C}$ | Temperatur | $\vartheta_\mathrm{M} = 5\,\mathrm{°C}$ |
| **Umgebung** | | **Messung in Tasse 2** | |
| Temperatur | $\vartheta_\mathrm{u} = 20\,\mathrm{°C}$ | nach 10 min | $\vartheta_\mathrm{K}(10\,\mathrm{min}) = 67\,\mathrm{°C}$ |
| **Milch in Teil f** | | **Becher in Teil g** | |
| Temperatur | $\vartheta_{\mathrm{M,h}} = 60\,\mathrm{°C}$ | Masse | $m_\mathrm{B} = 300\,\mathrm{g}$ |
| | | Spez. Wärmekapazität | $c_\mathrm{B} = 0{,}85\,\mathrm{kJ/(kg\,K)}$ |

**[Gesucht]{.underline}**

Gesucht ist, welche Tasse nach einer Stunde wärmer ist, und warum. Die Teile a bis f bauen aufeinander auf, Teil g vertieft das Modell.

a) Bestimmen Sie mit einer Energiebilanz die Mischtemperatur $\vartheta_{1,0}$ direkt nach dem Zugießen der Milch in Tasse 1.\
   $\vartheta_{1,0} = 70{,}47\,\mathrm{°C}$

b) Zeichnen Sie den Bilanzraum um den Inhalt von Tasse 1 in Abb. 1 ein. Vereinfachen Sie die allgemeine Energiebilanz (Foliensatz 05, Folie 8) zur globalen instationären Bilanz für den Inhalt einer Tasse und begründen Sie, welche Terme entfallen. Lösen Sie sie durch Trennung der Variablen für $T(t = 0\,\mathrm{s}) = T_0$.\
   $T(t) = T_\mathrm{u} + (T_0 - T_\mathrm{u})\cdot \exp\left(-\frac{kA}{m\,c_p}\,t\right)$

c) Bestimmen Sie $kA$ aus der Messung in Tasse 2. Welche Annahme brauchen Sie, um diesen Wert auch für Tasse 1 zu verwenden, und ist sie plausibel?\
   $kA = 0{,}3402\,\mathrm{W/K}$

d) Berechnen Sie $\vartheta_1$ und $\vartheta_2$ nach 60 Minuten (Tasse 2 direkt nach dem Zugießen). Welches $m\,c_p$ setzen Sie jeweils ein? Welche Tasse ist wärmer?\
   $34{,}05\,\mathrm{°C}$ und $30{,}19\,\mathrm{°C}$ (Zuordnung selbst bestimmen)

e) Berechnen Sie die Wärme, die jede Tasse in 60 Minuten an die Umgebung abgibt. Zeigen Sie, dass $Q_2 - Q_1$ den Temperaturunterschied aus d) erklärt. Wo liegt der Denkfehler Ihres Mitbewohners?\
   $Q_1 = 34{,}88\,\mathrm{kJ}$, $\quad Q_2 = 38{,}57\,\mathrm{kJ}$`\needspace{6\baselineskip}`{=latex}

f) Am nächsten Tag gibt es Milchkaffee: Die Milch wird je Tasse kurz vorher auf $\vartheta_{\mathrm{M,h}}$ erwärmt und untergerührt (gleiche Masse und Stoffdaten). Welche Tasse ist nach 60 Minuten wärmer? Sagen Sie es mit kurzer Begründung voraus, prüfen Sie dann mit den Gleichungen aus d) und erklären Sie das Ergebnis.\
   $35{,}99\,\mathrm{°C}$ und $37{,}18\,\mathrm{°C}$ (Zuordnung selbst bestimmen)

g) *Vertiefung:* Die Tassen sind vorgewärmte Keramikbecher, die immer die Temperatur ihres Inhalts haben, auch beim Zugießen der Milch. Passen Sie Bilanzraum und Bilanz aus b) an, bestimmen Sie $kA$ neu und berechnen Sie $\vartheta_1$ und $\vartheta_2$ wie in d). Gilt die Aussage aus d) weiter?\
   $kA = 0{,}4440\,\mathrm{W/K}$, $\quad\vartheta_1 = 34{,}04\,\mathrm{°C}$, $\quad\vartheta_2 = 30{,}96\,\mathrm{°C}$

::: seitenumbruch
:::

**[Versuch]{.underline}** (im Tutorium, läuft neben der Rechnung)

Drei gleiche, vorgewärmte Becher mit je 200 ml heißem Wasser oder Kaffee und je 30 ml Milch: Becher 1 bekommt die Milch sofort, Becher 2 und 3 erst nach 40 Minuten (Milch aus der Kühltasche bzw. aus einem Glas mit etwas Abstand zu den Bechern). Nach 10 Minuten werden Becher 2 und 3 gemessen.

1. Bestimmen Sie $kA$ wie in Teil c (ohne Becher) aus dem Mittelwert der beiden Messungen und sagen Sie mit den Gleichungen aus d) die Temperaturen nach 40 Minuten voraus (Becher 3 mit Milch bei Raumtemperatur).
2. Ist der gemessene Unterschied zwischen Becher 1 und 2 größer als die Messunsicherheit? Nennen Sie zwei Gründe für Abweichungen vom Modell.

| Becher | Start $\vartheta(0)$ | $\vartheta(10\,\mathrm{min})$ | Milch $\vartheta_\mathrm{M}$ | Vorhersage $\vartheta(40\,\mathrm{min})$ | Messung $\vartheta(40\,\mathrm{min})$ |
|:----------------------------------------------|:---------------------|:-----------------------|:--------------------|:------------------------|:------------------------|
| 1: Milch sofort | | | | | |
| 2: Milch nach 40 min aus der Kühltasche | | | | | |
| 3: Milch nach 40 min aus dem Glas | | | | | |

Raumtemperatur: \_\_\_\_\_\_\_\_\_\_ °C

Mischtemperatur Becher 1: \_\_\_\_\_\_\_\_\_\_ °C

$kA$ aus Becher 2 und 3: \_\_\_\_\_\_\_\_\_\_ W/K
