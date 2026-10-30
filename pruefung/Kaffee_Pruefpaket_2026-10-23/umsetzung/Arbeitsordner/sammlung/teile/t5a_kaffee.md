## Kaffee mit Milch

**[Ausgangssituation]{.underline}**

Sonntagmorgen in der WG-Küche: Sie haben Filterkaffee gekocht und zwei gleiche Tassen mit je 200 ml gefüllt. Da klingelt das Telefon, und das Gespräch wird eine Stunde dauern. Ihr Mitbewohner gießt seine Milch sofort in den Kaffee (Tasse 1). Sie stellen Ihre Tasse daneben und wollen die Milch erst nach dem Telefonat hineingießen (Tasse 2), damit der Kaffee „länger heiß bleibt“. Die Milch kommt in beiden Fällen direkt aus dem Kühlschrank.

![](grafik/t5_kaffee_tassen.png){width=92%}

**Abb. 1:** Die beiden Tassen

**[Frage 1]{.underline}** (Vorab-Frage)

Ihr Mitbewohner meint: „Ob man die Milch sofort oder später hineingießt, ist egal. Die Energie bleibt ja erhalten.“ Welche Tasse ist nach einer Stunde wärmer: Tasse 1, Tasse 2, oder sind beide gleich warm? Notieren Sie Ihre Vermutung mit einem Satz Begründung, bevor Sie Aufgabe 1 rechnen.

<!-- T5_FRAGEN -->

**[Aufgabe 1]{.underline}** (neu)

Um die Frage zu klären, messen Sie nach 10 Minuten die Temperatur in Tasse 2 (noch ohne Milch).

**Annahmen:**

- Der Tasseninhalt ist ideal durchmischt, die Milch mischt sich sofort und ohne Wärmeverlust.
- Die Wärmekapazität der Tasse wird außer in Teil g vernachlässigt.
- Die gesamte Wärmeabgabe (auch durch Strahlung und Verdunstung) ist $\dot{Q}_{ab} = kA\,(\vartheta - \vartheta_u)$ mit konstantem $kA$; die verdunstete Masse wird vernachlässigt.
- Kaffee (Stoffdaten von Wasser) und Milch sind inkompressibel ($c_p = c_v$); die Stoffdaten sind konstant.

**Gegebene Größen:**

| **Kaffee** | | **Milch** | |
|:-------------------------------------|:-------------------------------------------|:-------------------------------------|:-------------------------------------------|
| Volumen | $V_K = 200\,\mathrm{ml}$ | Volumen | $V_M = 30\,\mathrm{ml}$ |
| Dichte | $\rho_K = 1000\,\mathrm{kg/m^3}$ | Dichte | $\rho_M = 1030\,\mathrm{kg/m^3}$ |
| Spez. Wärmekapazität | $c_{p,K} = 4{,}18\,\mathrm{kJ/(kg\,K)}$ | Spez. Wärmekapazität | $c_{p,M} = 3{,}94\,\mathrm{kJ/(kg\,K)}$ |
| Anfangstemperatur | $\vartheta_{K,0} = 80\,\mathrm{°C}$ | Temperatur | $\vartheta_M = 5\,\mathrm{°C}$ |
| **Umgebung** | | **Messung in Tasse 2** | |
| Temperatur | $\vartheta_u = 20\,\mathrm{°C}$ | nach 10 min | $\vartheta_K(10\,\mathrm{min}) = 67\,\mathrm{°C}$ |
| **Milch in Teil f** | | **Becher in Teil g** | |
| Temperatur | $\vartheta_{M,h} = 60\,\mathrm{°C}$ | Masse | $m_B = 300\,\mathrm{g}$ |
| | | Spez. Wärmekapazität | $c_B = 0{,}85\,\mathrm{kJ/(kg\,K)}$ |

**Aufgabenstellung:**

a) Bestimmen Sie mit einer Energiebilanz die Mischtemperatur $\vartheta_{1,0}$ direkt nach dem Zugießen der Milch in Tasse 1.\
   $\vartheta_{1,0} = 70{,}47\,\mathrm{°C}$

b) Zeichnen Sie den Bilanzraum um den Inhalt von Tasse 1 in Abb. 1 ein. Vereinfachen Sie die allgemeine Energiebilanz (Foliensatz 05, Folie 8) zur globalen instationären Bilanz für den Inhalt einer Tasse und begründen Sie, welche Terme entfallen. Lösen Sie sie durch Trennung der Variablen für $T(t = 0\,\mathrm{s}) = T_0$.\
   $T(t) = T_u + (T_0 - T_u)\cdot \exp\left(-\frac{kA}{m\,c_p}\,t\right)$

c) Bestimmen Sie $kA$ aus der Messung in Tasse 2. Welche Annahme brauchen Sie, um diesen Wert auch für Tasse 1 zu verwenden, und ist sie plausibel?\
   $kA = 0{,}3402\,\mathrm{W/K}$

d) Berechnen Sie $\vartheta_1$ und $\vartheta_2$ nach 60 Minuten (Tasse 2 direkt nach dem Zugießen). Welches $m\,c_p$ setzen Sie jeweils ein? Welche Tasse ist wärmer?\
   $34{,}05\,\mathrm{°C}$ und $30{,}19\,\mathrm{°C}$ (Zuordnung selbst bestimmen)

e) Berechnen Sie die Wärme, die jede Tasse in 60 Minuten an die Umgebung abgibt. Zeigen Sie, dass $Q_2 - Q_1$ den Temperaturunterschied aus d) erklärt. Wo liegt der Denkfehler Ihres Mitbewohners?\
   $Q_1 = 34{,}88\,\mathrm{kJ}$, $\quad Q_2 = 38{,}57\,\mathrm{kJ}$

f) Am nächsten Tag gibt es Milchkaffee: Die Milch wird je Tasse kurz vorher auf $\vartheta_{M,h}$ erwärmt und untergerührt (gleiche Masse und Stoffdaten). Welche Tasse ist nach 60 Minuten wärmer? Sagen Sie es mit kurzer Begründung voraus, prüfen Sie dann mit den Gleichungen aus d) und erklären Sie das Ergebnis.\
   $35{,}99\,\mathrm{°C}$ und $37{,}18\,\mathrm{°C}$ (Zuordnung selbst bestimmen)

g) *Vertiefung:* Die Tassen sind vorgewärmte Keramikbecher, die immer die Temperatur ihres Inhalts haben, auch beim Zugießen der Milch. Passen Sie Bilanzraum und Bilanz aus b) an, bestimmen Sie $kA$ neu und berechnen Sie $\vartheta_1$ und $\vartheta_2$ wie in d). Gilt die Aussage aus d) weiter?\
   $kA = 0{,}4440\,\mathrm{W/K}$, $\quad\vartheta_1 = 34{,}04\,\mathrm{°C}$, $\quad\vartheta_2 = 30{,}96\,\mathrm{°C}$

**[Versuch zu Aufgabe 1]{.underline}** (im Tutorium, läuft neben der Rechnung)

Drei gleiche, vorgewärmte Becher mit je 200 ml heißem Wasser oder Kaffee und je 30 ml Milch: Becher 1 bekommt die Milch sofort, Becher 2 und 3 erst nach 40 Minuten (Milch aus der Kühltasche bzw. aus einem Glas mit etwas Abstand zu den Bechern). Nach 10 Minuten werden Becher 2 und 3 gemessen.

1. Bestimmen Sie $kA$ wie in Teil c (ohne Becher) aus dem Mittelwert der beiden Messungen und sagen Sie mit den Gleichungen aus d) die Temperaturen nach 40 Minuten voraus (Becher 3 mit Milch bei Raumtemperatur).
2. Ist der gemessene Unterschied zwischen Becher 1 und 2 größer als die Messunsicherheit? Nennen Sie zwei Gründe für Abweichungen vom Modell.

| Becher | Start $\vartheta(0)$ | $\vartheta(10\,\mathrm{min})$ | Milch $\vartheta_M$ | Vorhersage $\vartheta(40\,\mathrm{min})$ | Messung $\vartheta(40\,\mathrm{min})$ |
|:----------------------------------------------|:---------------------|:-----------------------|:--------------------|:------------------------|:------------------------|
| 1: Milch sofort | | | | | |
| 2: Milch nach 40 min aus der Kühltasche | | | | | |
| 3: Milch nach 40 min aus dem Glas | | | | | |

Raumtemperatur: \_\_\_\_\_\_\_\_\_\_ °C

Mischtemperatur Becher 1: \_\_\_\_\_\_\_\_\_\_ °C

$kA$ aus Becher 2 und 3: \_\_\_\_\_\_\_\_\_\_ W/K

