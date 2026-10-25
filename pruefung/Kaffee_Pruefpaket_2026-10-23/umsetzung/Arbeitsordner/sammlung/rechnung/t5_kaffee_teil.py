# -*- coding: utf-8 -*-
"""Schreibt den Kaffee-Block (Tutorium 5, Aufgabe 1) der Aufgabensammlung nach ../teile/t5a_kaffee.md
und die Zahlen nach t5_kaffee_ausgabe.txt. Alle Zahlen aus kaffee_modell.py.
Aufruf: python3 t5_kaffee_teil.py
"""
import math
import os
from kaffee_modell import P, rechne, becher

HIER = os.path.dirname(os.path.abspath(__file__))
TEILE = os.path.join(os.path.dirname(HIER), "teile")
K = 273.15
r = rechne(P)
b = becher()
s60 = rechne(dict(P, th_M=60.0))
assert r["dT"] > 0 and b["dT"] > 0 and s60["dT"] < 0

# h (2): Milch für Tasse 2 steht 60 min neben der Tasse und hat höchstens Raumtemperatur; Tasse 1 wie in d)
h2_T2 = (r["C_K"] * r["T2_K"] + r["C_M"] * r["T_U"]) / r["C_G"]
h2_dT = r["T1"] - h2_T2                                   # Tasse 2 bleibt mindestens so viel kühler
h2_Q_M = r["C_M"] * (r["T_U"] - r["T_M"])                 # höchstens aus der Raumluft aufgenommene Wärme
h2_th_gleich = (r["T1"] * r["C_G"] - r["C_K"] * r["T2_K"]) / r["C_M"] - K
assert h2_dT > 0 and abs(h2_dT - (r["Q2"] - r["Q1"] - h2_Q_M) / r["C_G"]) < 1e-9


def versuch_becher(th_milch, m_T=0.300, c_T=850.0):
    """Versuch: vorgewärmte Becher (Modell aus Teil f), Milch nach 60 min mit th_milch in °C."""
    C_T = m_T * c_T
    CKT, CGT = r["C_K"] + C_T, r["C_G"] + C_T
    kA_B = -CKT / P["t_mess"] * r["ln_mess"]
    T2K = r["T_U"] + (r["T_K0"] - r["T_U"]) * math.exp(-kA_B * P["t_end"] / CKT)
    return (CKT * T2K + r["C_M"] * (th_milch + K)) / CGT


def de(x, n=2):
    return f"{x:.{n}f}".replace(".", "{,}")


def dt(x, n=2):
    return f"{x:.{n}f}".replace(".", ",")


U = lambda s: r"\,\mathrm{" + s + "}"

AUSGABE = [
    ("Mischtemperatur Tasse 1", r["T1_0"] - K, "°C"),
    ("kA aus der Messung", r["kA"], "W/K"),
    ("theta_1 nach 60 min", r["T1"] - K, "°C"),
    ("theta_2 nach 60 min", r["T2"] - K, "°C"),
    ("Q_1", r["Q1"] / 1e3, "kJ"),
    ("Q_2", r["Q2"] / 1e3, "kJ"),
    ("Becher: kA neu", b["kA"], "W/K"),
    ("Becher: theta_1", b["T1"] - K, "°C"),
    ("Becher: theta_2", b["T2"] - K, "°C"),
    ("Milchschaum 60 °C: theta_1", s60["T1"] - K, "°C"),
    ("Milchschaum 60 °C: theta_2", s60["T2"] - K, "°C"),
    ("Milchtemperatur für gleich warme Tassen", r["th_M_gleich"], "°C"),
    ("Info h (2): theta_2 mit Milch bei Raumtemperatur", h2_T2 - K, "°C"),
    ("Info h (2): Tasse 2 mindestens kühler um", h2_dT, "K"),
    ("Info h (2): Milch nimmt höchstens auf, C_M (20 - 5) K", h2_Q_M / 1e3, "kJ"),
    ("Info h (2): Q_2 - Q_1", (r["Q2"] - r["Q1"]) / 1e3, "kJ"),
    ("Info h (2): Milchtemperatur für Gleichstand mit Tasse 1", h2_th_gleich, "°C"),
    ("Info Versuch: Becher 1 (wie f)", b["T1"] - K, "°C"),
    ("Info Versuch: Becher 2 (wie f)", versuch_becher(P["th_M"]) - K, "°C"),
    ("Info Versuch: Becher 3, Milch bei Raumtemperatur", versuch_becher(P["th_U"]) - K, "°C"),
]
assert abs(versuch_becher(P["th_M"]) - b["T2"]) < 1e-9

md = rf"""## Kaffee mit Milch

**[Ausgangssituation]{{.underline}}**

Sonntagmorgen in der WG-Küche: Sie haben Filterkaffee gekocht und zwei gleiche Tassen mit je {dt(P['V_K']*1e6, 0)} ml gefüllt. Da klingelt das Telefon, und das Gespräch wird eine Stunde dauern. Ihr Mitbewohner gießt seine Milch sofort in den Kaffee (Tasse 1). Sie stellen Ihre Tasse daneben und wollen die Milch erst nach dem Telefonat hineingießen (Tasse 2), damit der Kaffee „länger heiß bleibt“. Die Milch kommt in beiden Fällen direkt aus dem Kühlschrank.

![](grafik/t5_kaffee_tassen.png){{width=92%}}

**Abb. 1:** Die beiden Tassen

**[Frage 1]{{.underline}}** (Vorab-Frage)

Ihr Mitbewohner meint: „Ob man die Milch sofort oder später hineingießt, ist egal. Die Energie bleibt ja erhalten.“ Welche Tasse ist nach einer Stunde wärmer? Notieren Sie Ihre Vermutung, bevor Sie Aufgabe 1 rechnen.

<!-- T5_FRAGEN -->

**[Aufgabe 1]{{.underline}}** (neu)

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
| Volumen: | $V_K = {de(P['V_K']*1e6, 0)}{U('ml')}$ | Volumen: | $V_M = {de(P['V_M']*1e6, 0)}{U('ml')}$ |
| Dichte: | $\rho_K = {de(P['rho_K'], 0)}{U('kg/m^3')}$ | Dichte: | $\rho_M = {de(P['rho_M'], 0)}{U('kg/m^3')}$ |
| Spez. Wärmekapazität: | $c_{{p,K}} = {de(P['cp_K']/1e3, 2)}{U('kJ/(kg\\,K)')}$ | Spez. Wärmekapazität: | $c_{{p,M}} = {de(P['cp_M']/1e3, 2)}{U('kJ/(kg\\,K)')}$ |
| Temperatur bei $t = 0$: | $\vartheta_{{K,0}} = {de(P['th_K0'], 0)}{U('°C')}$ | Temperatur: | $\vartheta_M = {de(P['th_M'], 0)}{U('°C')}$ |
| | | | |
| ***Umgebung:*** | | ***Messung:*** | |
| Temperatur: | $\vartheta_u = {de(P['th_U'], 0)}{U('°C')}$ | Temperatur nach {dt(P['t_mess']/60, 0)} min: | $\vartheta_K({de(P['t_mess']/60, 0)}{U('min')}) = {de(P['th_mess'], 0)}{U('°C')}$ |
| | | | |
| ***Becher:*** | | ***Milchschaum:*** | |
| Masse: | $m_B = {de(300, 0)}{U('g')}$ | Temperatur: | $\vartheta_S = {de(60, 0)}{U('°C')}$ |
| Spez. Wärmekapazität: | $c_B = {de(0.85, 2)}{U('kJ/(kg\\,K)')}$ | | |

**Aufgabenstellung:**

a) Bestimmen Sie mit einer Energiebilanz die Mischtemperatur $\vartheta_{{1,0}}$ direkt nach dem Zugießen der Milch in Tasse 1.\
   $\vartheta_{{1,0}} = {de(r['T1_0']-K)}{U('°C')}$

b) Zeichnen Sie den Bilanzraum für Tasse 1 in Abb. 1 ein und stellen Sie die instationäre Energiebilanz für den Inhalt einer Tasse auf. Lösen Sie die Differentialgleichung durch Trennung der Variablen für die Anfangstemperatur $T(t = 0\,\mathrm{{s}}) = T_0$.\
   $T(t) = T_u + (T_0 - T_u)\cdot \exp\left(-\frac{{kA}}{{m\,c_p}}\,t\right)$

c) Bestimmen Sie aus der Messung in Tasse 2 das Produkt $kA$.\
   $kA = {de(r['kA'], 4)}{U('W/K')}$

d) Berechnen Sie die Temperaturen $\vartheta_1$ und $\vartheta_2$ beider Tassen nach 60 Minuten, bei Tasse 2 direkt nach dem Zugießen der Milch. Welche Tasse ist kühler?\
   $\vartheta_1 = {de(r['T1']-K)}{U('°C')}$, $\quad\vartheta_2 = {de(r['T2']-K)}{U('°C')}$

e) Berechnen Sie für beide Tassen die Wärme, die in den 60 Minuten an die Umgebung abgegeben wird. Erklären Sie damit das Ergebnis aus d). Hat Ihr Mitbewohner recht?\
   $Q_1 = {de(r['Q1']/1e3)}{U('kJ')}$, $\quad Q_2 = {de(r['Q2']/1e3)}{U('kJ')}$

f) Die Tassen sind in Wirklichkeit Keramikbecher. Sie wurden vorgewärmt und haben immer die Temperatur ihres Inhalts. Bestimmen Sie $kA$ mit Becher erneut aus der Messung und berechnen Sie $\vartheta_1$ und $\vartheta_2$ noch einmal. Bleibt die Aussage aus d) gültig?\
   $kA = {de(b['kA'], 4)}{U('W/K')}$, $\quad\vartheta_1 = {de(b['T1']-K)}{U('°C')}$, $\quad\vartheta_2 = {de(b['T2']-K)}{U('°C')}$

g) Am nächsten Tag trinkt Ihr Mitbewohner Cappuccino: Statt kalter Milch kommt Milchschaum mit $\vartheta_S$ in beide Tassen (gleiche Masse, Becher wieder vernachlässigt). Sagen Sie zuerst voraus, welche Tasse nach 60 Minuten wärmer ist. Prüfen Sie Ihre Vorhersage dann mit den Gleichungen aus d).\
   $\vartheta_1 = {de(s60['T1']-K)}{U('°C')}$, $\quad\vartheta_2 = {de(s60['T2']-K)}{U('°C')}$

h) *Zusatzfrage:* (1) Bei welcher Milchtemperatur ist es egal, ob die Milch sofort oder erst nach 60 Minuten hineinkommt (ohne Becher)? (2) Sie nehmen die Milch für Tasse 2 schon bei $t = 0$ aus dem Kühlschrank und stellen sie neben die Tasse. Kann Tasse 2 dadurch wärmer werden als Tasse 1? Begründen Sie mit einer Abschätzung und den Ergebnissen aus e).\
   Zu (1): $\vartheta_M = {de(r['th_M_gleich'], 1)}{U('°C')}$

**[Versuch zu Aufgabe 1]{{.underline}}** (im Tutorium, läuft neben der Rechnung)

*Material:* drei gleiche Becher, heißes Wasser oder Kaffee aus der Thermoskanne, Milch aus der Kühltasche, ein kleines Glas, Messbecher, ein Einstichthermometer für alle Becher, Löffel, Uhr.

1. Notieren Sie Ihre Vermutung zu Frage 1.
2. $t = 0$: Becher vorwärmen, je 200 ml einfüllen und die Starttemperatur messen. Becher 1 bekommt die Milch sofort. Für Becher 2 bleibt die Milch in der Kühltasche, für Becher 3 steht sie im Glas neben dem Becher.
3. $t = 10\,\mathrm{{min}}$: Becher 2 messen und daraus $kA$ wie in Teil f (mit Becher) bestimmen.
4. Mit den gemessenen Werten die Temperaturen nach 60 Minuten vorhersagen, für Becher 3 mit Milch bei Raumtemperatur.
5. $t = 60\,\mathrm{{min}}$: Milchtemperatur in Kühltasche und Glas messen, Milch in Becher 2 und 3 gießen, umrühren und alle drei Becher messen.

| Becher | Vorhersage nach 60 min | Messung nach 60 min |
|:-------------------------------|:---------------------------|:---------------------------|
| 1: Milch sofort | | |
| 2: Milch nach 60 min aus der Kühltasche | | |
| 3: Milch nach 60 min aus dem Glas | | |

"""

with open(os.path.join(TEILE, "t5a_kaffee.md"), "w", encoding="utf-8") as f:
    f.write(md)
with open(os.path.join(HIER, "t5_kaffee_ausgabe.txt"), "w", encoding="utf-8") as f:
    f.write("Tutorium 5, Aufgabe 1: Kaffee mit Milch (Zahlen aus kaffee_modell.py)\n")
    for name, wert, einheit in AUSGABE:
        f.write(f"{name:45s} {wert:10.4f} {einheit}\n")
print(open(os.path.join(HIER, "t5_kaffee_ausgabe.txt"), encoding="utf-8").read())
