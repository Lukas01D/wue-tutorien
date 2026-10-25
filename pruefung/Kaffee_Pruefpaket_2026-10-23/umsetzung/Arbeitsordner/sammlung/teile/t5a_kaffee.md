## Kaffee mit Milch

**[Ausgangssituation]{.underline}**

Sonntagmorgen in der WG-Küche: Sie haben Filterkaffee gekocht und zwei gleiche Tassen mit je 200 ml gefüllt. Da klingelt das Telefon, und das Gespräch wird eine Stunde dauern. Ihr Mitbewohner gießt seine Milch sofort in den Kaffee (Tasse 1). Sie stellen Ihre Tasse daneben und wollen die Milch erst nach dem Telefonat hineingießen (Tasse 2), damit der Kaffee „länger heiß bleibt“. Die Milch kommt in beiden Fällen direkt aus dem Kühlschrank.

![](grafik/t5_kaffee_tassen.png){width=92%}

**Abb. 1:** Die beiden Tassen

**[Frage 1]{.underline}** (Vorab-Frage)

Ihr Mitbewohner meint: „Ob man die Milch sofort oder später hineingießt, ist egal. Die Energie bleibt ja erhalten.“ Welche Tasse ist nach einer Stunde wärmer? Notieren Sie Ihre Vermutung, bevor Sie Aufgabe 1 rechnen.

<!-- T5_FRAGEN -->

**[Aufgabe 1]{.underline}** (neu)

Um die Frage zu klären, messen Sie nach 10 Minuten die Temperatur in Tasse 2, die bis dahin noch keine Milch enthält.

**Annahmen:**

- Der Tasseninhalt wird als ideal durchmischt angenommen.
- Die Wärmekapazität der Tasse wird bis Teil e vernachlässigt.
- Die gesamte Wärmeabgabe an die Umgebung (Konvektion, Strahlung, Verdunstung und Wärmedurchgang durch die Tassenwand) wird über ein konstantes Produkt $kA$ beschrieben, das mit und ohne Milch gleich ist. Die verdunstete Masse wird vernachlässigt.
- Kaffee und Milch mischen sich sofort und ohne Wärmeverlust.
- Die Stoffdaten sind unabhängig von der Temperatur; Kaffee hat die Stoffdaten von Wasser.

***Gegebene Größen:***

| ***Kaffee:*** | | ***Milch:*** | |
|:---------------------|:-----------------------------|:---------------------|:-----------------------------|
| Volumen: | $V_K = 200\,\mathrm{ml}$ | Volumen: | $V_M = 30\,\mathrm{ml}$ |
| Dichte: | $\rho_K = 1000\,\mathrm{kg/m^3}$ | Dichte: | $\rho_M = 1030\,\mathrm{kg/m^3}$ |
| Spez. Wärmekapazität: | $c_{p,K} = 4{,}18\,\mathrm{kJ/(kg\,K)}$ | Spez. Wärmekapazität: | $c_{p,M} = 3{,}94\,\mathrm{kJ/(kg\,K)}$ |
| Temperatur bei $t = 0$: | $\vartheta_{K,0} = 80\,\mathrm{°C}$ | Temperatur: | $\vartheta_M = 5\,\mathrm{°C}$ |
| | | | |
| ***Umgebung:*** | | ***Messung:*** | |
| Temperatur: | $\vartheta_u = 20\,\mathrm{°C}$ | Temperatur nach 10 min: | $\vartheta_K(10\,\mathrm{min}) = 67\,\mathrm{°C}$ |
| | | | |
| ***Becher:*** | | ***Milchschaum:*** | |
| Masse: | $m_B = 300\,\mathrm{g}$ | Temperatur: | $\vartheta_S = 60\,\mathrm{°C}$ |
| Spez. Wärmekapazität: | $c_B = 0{,}85\,\mathrm{kJ/(kg\,K)}$ | | |

**Aufgabenstellung:**

a) Bestimmen Sie mit einer Energiebilanz die Mischtemperatur $\vartheta_{1,0}$ direkt nach dem Zugießen der Milch in Tasse 1.\
   $\vartheta_{1,0} = 70{,}47\,\mathrm{°C}$

b) Zeichnen Sie den Bilanzraum für Tasse 1 in Abb. 1 ein und stellen Sie die instationäre Energiebilanz für den Inhalt einer Tasse auf. Lösen Sie die Differentialgleichung durch Trennung der Variablen für die Anfangstemperatur $T(t = 0\,\mathrm{s}) = T_0$.\
   $T(t) = T_u + (T_0 - T_u)\cdot \exp\left(-\frac{kA}{m\,c_p}\,t\right)$

c) Bestimmen Sie aus der Messung in Tasse 2 das Produkt $kA$.\
   $kA = 0{,}3402\,\mathrm{W/K}$

d) Berechnen Sie die Temperaturen $\vartheta_1$ und $\vartheta_2$ beider Tassen nach 60 Minuten, bei Tasse 2 direkt nach dem Zugießen der Milch. Welche Tasse ist kühler?\
   $\vartheta_1 = 34{,}05\,\mathrm{°C}$, $\quad\vartheta_2 = 30{,}19\,\mathrm{°C}$

e) Berechnen Sie für beide Tassen die Wärme, die in den 60 Minuten an die Umgebung abgegeben wird. Erklären Sie damit das Ergebnis aus d). Hat Ihr Mitbewohner recht?\
   $Q_1 = 34{,}88\,\mathrm{kJ}$, $\quad Q_2 = 38{,}57\,\mathrm{kJ}$

f) Die Tassen sind in Wirklichkeit Keramikbecher. Sie wurden vorgewärmt und haben immer die Temperatur ihres Inhalts. Bestimmen Sie $kA$ mit Becher erneut aus der Messung und berechnen Sie $\vartheta_1$ und $\vartheta_2$ noch einmal. Bleibt die Aussage aus d) gültig?\
   $kA = 0{,}4440\,\mathrm{W/K}$, $\quad\vartheta_1 = 34{,}04\,\mathrm{°C}$, $\quad\vartheta_2 = 30{,}96\,\mathrm{°C}$

g) Am nächsten Tag trinkt Ihr Mitbewohner Cappuccino: Statt kalter Milch kommt Milchschaum mit $\vartheta_S$ in beide Tassen (gleiche Masse, Becher wieder vernachlässigt). Sagen Sie zuerst voraus, welche Tasse nach 60 Minuten wärmer ist. Prüfen Sie Ihre Vorhersage dann mit den Gleichungen aus d).\
   $\vartheta_1 = 35{,}99\,\mathrm{°C}$, $\quad\vartheta_2 = 37{,}18\,\mathrm{°C}$

h) *Zusatzfrage:* (1) Bei welcher Milchtemperatur ist es egal, ob die Milch sofort oder erst nach 60 Minuten hineinkommt (ohne Becher)? (2) Sie nehmen die Milch für Tasse 2 schon bei $t = 0$ aus dem Kühlschrank und stellen sie neben die Tasse. Kann Tasse 2 dadurch wärmer werden als Tasse 1? Begründen Sie mit einer Abschätzung und den Ergebnissen aus e).\
   Zu (1): $\vartheta_M = 47{,}0\,\mathrm{°C}$

**[Versuch zu Aufgabe 1]{.underline}** (im Tutorium, läuft neben der Rechnung)

*Material:* drei gleiche Becher, heißes Wasser oder Kaffee aus der Thermoskanne, Milch aus der Kühltasche, ein kleines Glas, Messbecher, ein Einstichthermometer für alle Becher, Löffel, Uhr.

1. Notieren Sie Ihre Vermutung zu Frage 1.
2. $t = 0$: Becher vorwärmen, je 200 ml einfüllen und die Starttemperatur messen. Becher 1 bekommt die Milch sofort. Für Becher 2 bleibt die Milch in der Kühltasche, für Becher 3 steht sie im Glas neben dem Becher.
3. $t = 10\,\mathrm{min}$: Becher 2 messen und daraus $kA$ wie in Teil f (mit Becher) bestimmen.
4. Mit den gemessenen Werten die Temperaturen nach 60 Minuten vorhersagen, für Becher 3 mit Milch bei Raumtemperatur.
5. $t = 60\,\mathrm{min}$: Milchtemperatur in Kühltasche und Glas messen, Milch in Becher 2 und 3 gießen, umrühren und alle drei Becher messen.

| Becher | Vorhersage nach 60 min | Messung nach 60 min |
|:-------------------------------|:---------------------------|:---------------------------|
| 1: Milch sofort | | |
| 2: Milch nach 60 min aus der Kühltasche | | |
| 3: Milch nach 60 min aus dem Glas | | |

