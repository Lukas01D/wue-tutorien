# -*- coding: utf-8 -*-
"""Schreibt den Kaffee-Block (Tutorium 5, Aufgabe 1) der Aufgabensammlung nach ../teile/t5a_kaffee.md
und die Zahlen nach t5_kaffee_ausgabe.txt. Alle Zahlen aus kaffee_modell.py.
Aufruf: python3 t5_kaffee_teil.py
"""
import math
import os
from kaffee_modell import P, rechne, becher, zwei_tassen

HIER = os.path.dirname(os.path.abspath(__file__))
TEILE = os.path.join(os.path.dirname(HIER), "teile")
K = 273.15
r = rechne(P)
b = becher()
s60 = rechne(dict(P, th_M=P["th_Mh"]))
T_VERSUCH = 40                                             # min, Versuch im Tutorium (Ä4)
assert r["dT"] > 0 and b["dT"] > 0 and s60["dT"] < 0

# h (2): Milch für Tasse 2 steht 60 min neben der Tasse und hat höchstens Raumtemperatur; Tasse 1 wie in d)
h2_T2 = (r["C_K"] * r["T2_K"] + r["C_M"] * r["T_U"]) / r["C_G"]
h2_dT = r["T1"] - h2_T2                                   # Tasse 2 bleibt mindestens so viel kühler
h2_Q_M = r["C_M"] * (r["T_U"] - r["T_M"])                 # höchstens aus der Raumluft aufgenommene Wärme
h2_th_gleich = (r["T1"] * r["C_G"] - r["C_K"] * r["T2_K"]) / r["C_M"] - K
assert h2_dT > 0 and abs(h2_dT - (r["Q2"] - r["Q1"] - h2_Q_M) / r["C_G"]) < 1e-9


def versuch_becher(th_milch, t_min=60):
    """Versuch: vorgewärmte Becher (Modell aus Teil f), Milch nach t_min mit th_milch in °C."""
    return zwei_tassen(C_T=P["m_B"] * P["c_B"], th_M2=th_milch, t_end=t_min * 60.0)["T2"]


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
    ("Erwärmte Milch 60 °C: theta_1", s60["T1"] - K, "°C"),
    ("Erwärmte Milch 60 °C: theta_2", s60["T2"] - K, "°C"),
    ("Milchtemperatur für gleich warme Tassen", r["th_M_gleich"], "°C"),
    ("Info h (2): theta_2 mit Milch bei Raumtemperatur", h2_T2 - K, "°C"),
    ("Info h (2): Tasse 2 mindestens kühler um", h2_dT, "K"),
    ("Info h (2): Milch nimmt höchstens auf, C_M (20 - 5) K", h2_Q_M / 1e3, "kJ"),
    ("Info h (2): Q_2 - Q_1", (r["Q2"] - r["Q1"]) / 1e3, "kJ"),
    ("Info h (2): Milchtemperatur für Gleichstand mit Tasse 1", h2_th_gleich, "°C"),
    ("Info Versuch nach 40 min: Becher 1 (wie f)", zwei_tassen(C_T=P["m_B"] * P["c_B"], t_end=T_VERSUCH * 60.0)["T1"] - K, "°C"),
    ("Info Versuch nach 40 min: Becher 2 (wie f)", versuch_becher(P["th_M"], T_VERSUCH) - K, "°C"),
    ("Info Versuch nach 40 min: Becher 3, Milch 20 °C", versuch_becher(P["th_U"], T_VERSUCH) - K, "°C"),
]
assert abs(versuch_becher(P["th_M"]) - b["T2"]) < 1e-9

md = rf"""## Kaffee mit Milch

**[Ausgangssituation]{{.underline}}**

Sonntagmorgen in der WG-Küche: Sie haben Filterkaffee gekocht und zwei gleiche Tassen mit je {dt(P['V_K']*1e6, 0)} ml gefüllt. Da klingelt das Telefon, und das Gespräch wird eine Stunde dauern. Ihr Mitbewohner gießt seine Milch sofort in den Kaffee (Tasse 1). Sie stellen Ihre Tasse daneben und wollen die Milch erst nach dem Telefonat hineingießen (Tasse 2), damit der Kaffee „länger heiß bleibt“. Die Milch kommt in beiden Fällen direkt aus dem Kühlschrank.

![](grafik/t5_kaffee_tassen.png){{width=92%}}

**Abb. 1:** Die beiden Tassen

**[Frage 1]{{.underline}}** (Vorab-Frage)

Ihr Mitbewohner meint: „Ob man die Milch sofort oder später hineingießt, ist egal. Die Energie bleibt ja erhalten.“ Welche Tasse ist nach einer Stunde wärmer: Tasse 1, Tasse 2, oder sind beide gleich warm? Notieren Sie Ihre Vermutung mit einem Satz Begründung, bevor Sie Aufgabe 1 rechnen.

<!-- T5_FRAGEN -->

**[Aufgabe 1]{{.underline}}** (neu)

Um die Frage zu klären, messen Sie nach 10 Minuten die Temperatur in Tasse 2 (noch ohne Milch).

**Annahmen:**

- Der Tasseninhalt ist ideal durchmischt, die Milch mischt sich sofort und ohne Wärmeverlust.
- Die Wärmekapazität der Tasse wird bis Teil e vernachlässigt.
- Die gesamte Wärmeabgabe (auch durch Strahlung und Verdunstung) ist $\dot{{Q}}_{{ab}} = kA\,(\vartheta - \vartheta_u)$ mit konstantem $kA$; die verdunstete Masse wird vernachlässigt.
- Kaffee (Stoffdaten von Wasser) und Milch sind inkompressibel ($c_p = c_v$); die Stoffdaten sind konstant.

**Gegebene Größen:**

| **Kaffee** | | **Milch** | |
|:-------------------------------------|:-------------------------------------------|:-------------------------------------|:-------------------------------------------|
| Volumen | $V_K = {de(P['V_K']*1e6, 0)}{U('ml')}$ | Volumen | $V_M = {de(P['V_M']*1e6, 0)}{U('ml')}$ |
| Dichte | $\rho_K = {de(P['rho_K'], 0)}{U('kg/m^3')}$ | Dichte | $\rho_M = {de(P['rho_M'], 0)}{U('kg/m^3')}$ |
| Spez. Wärmekapazität | $c_{{p,K}} = {de(P['cp_K']/1e3, 2)}{U('kJ/(kg\\,K)')}$ | Spez. Wärmekapazität | $c_{{p,M}} = {de(P['cp_M']/1e3, 2)}{U('kJ/(kg\\,K)')}$ |
| Anfangstemperatur | $\vartheta_{{K,0}} = {de(P['th_K0'], 0)}{U('°C')}$ | Temperatur | $\vartheta_M = {de(P['th_M'], 0)}{U('°C')}$ |
| **Umgebung** | | **Messung in Tasse 2** | |
| Temperatur | $\vartheta_u = {de(P['th_U'], 0)}{U('°C')}$ | nach {dt(P['t_mess']/60, 0)} min | $\vartheta_K({de(P['t_mess']/60, 0)}{U('min')}) = {de(P['th_mess'], 0)}{U('°C')}$ |
| **Becher ab Teil f** | | **Milch in Teil g** | |
| Masse | $m_B = {de(P['m_B']*1e3, 0)}{U('g')}$ | Temperatur | $\vartheta_{{M,h}} = {de(P['th_Mh'], 0)}{U('°C')}$ |
| Spez. Wärmekapazität | $c_B = {de(P['c_B']/1e3, 2)}{U('kJ/(kg\\,K)')}$ | | |

**Aufgabenstellung:**

a) Bestimmen Sie mit einer Energiebilanz die Mischtemperatur $\vartheta_{{1,0}}$ direkt nach dem Zugießen der Milch in Tasse 1.\
   $\vartheta_{{1,0}} = {de(r['T1_0']-K)}{U('°C')}$

b) Zeichnen Sie den Bilanzraum um den Inhalt von Tasse 1 in Abb. 1 ein. Vereinfachen Sie die allgemeine Energiebilanz zur globalen instationären Bilanz für den Inhalt einer Tasse und begründen Sie, welche Terme entfallen. Lösen Sie sie durch Trennung der Variablen für $T(t = 0\,\mathrm{{s}}) = T_0$.\
   $T(t) = T_u + (T_0 - T_u)\cdot \exp\left(-\frac{{kA}}{{m\,c_p}}\,t\right)$

c) Bestimmen Sie $kA$ aus der Messung in Tasse 2. Welche Annahme brauchen Sie, um diesen Wert auch für Tasse 1 zu verwenden, und ist sie plausibel?\
   $kA = {de(r['kA'], 4)}{U('W/K')}$

d) Berechnen Sie $\vartheta_1$ und $\vartheta_2$ nach 60 Minuten (Tasse 2 direkt nach dem Zugießen). Welches $m\,c_p$ setzen Sie jeweils ein? Welche Tasse ist wärmer?\
   $\vartheta_1 = {de(r['T1']-K)}{U('°C')}$, $\quad\vartheta_2 = {de(r['T2']-K)}{U('°C')}$

e) Berechnen Sie die Wärme, die jede Tasse in 60 Minuten an die Umgebung abgibt. Zeigen Sie, dass $Q_2 - Q_1$ den Temperaturunterschied aus d) erklärt. Wo liegt der Denkfehler Ihres Mitbewohners?\
   $Q_1 = {de(r['Q1']/1e3)}{U('kJ')}$, $\quad Q_2 = {de(r['Q2']/1e3)}{U('kJ')}$

f) *Vertiefung:* Die Tassen sind vorgewärmte Keramikbecher, die immer die Temperatur ihres Inhalts haben, auch beim Zugießen der Milch. Passen Sie Bilanzraum und Bilanz aus b) an, bestimmen Sie $kA$ neu und berechnen Sie $\vartheta_1$ und $\vartheta_2$. Gilt die Aussage aus d) weiter?\
   $kA = {de(b['kA'], 4)}{U('W/K')}$, $\quad\vartheta_1 = {de(b['T1']-K)}{U('°C')}$, $\quad\vartheta_2 = {de(b['T2']-K)}{U('°C')}$

g) Am nächsten Tag gibt es Milchkaffee: Die Milch wird je Tasse kurz vorher auf $\vartheta_{{M,h}}$ erwärmt und untergerührt (gleiche Masse und Stoffdaten, ohne Becher). Welche Tasse ist nach 60 Minuten wärmer? Sagen Sie es mit kurzer Begründung voraus, prüfen Sie dann mit den Gleichungen aus d) und erklären Sie das Ergebnis.\
   ${de(s60['T1']-K)}{U('°C')}$ und ${de(s60['T2']-K)}{U('°C')}$ (Zuordnung selbst bestimmen)

h) *Zusatzfrage:* (1) Bei welcher Milchtemperatur sind beide Tassen nach 60 Minuten gleich warm (ohne Becher)? (2) Die Milch für Tasse 2 steht ab $t = 0$ neben der Tasse und wird nur von der Raumluft erwärmt. Kann Tasse 2 so wärmer werden als Tasse 1? Begründen Sie mit einer Abschätzung und e).\
   $\vartheta_M = {de(r['th_M_gleich'], 1)}{U('°C')}$

**[Versuch zu Aufgabe 1]{{.underline}}** (im Tutorium, läuft neben der Rechnung)

Drei gleiche, vorgewärmte Becher mit je 200 ml heißem Wasser oder Kaffee und je 30 ml Milch: Becher 1 bekommt die Milch sofort, Becher 2 und 3 erst nach {T_VERSUCH} Minuten (Milch aus der Kühltasche bzw. aus einem Glas mit etwas Abstand zu den Bechern). Nach {dt(P['t_mess']/60, 0)} Minuten werden Becher 2 und 3 gemessen.

1. Bestimmen Sie $kA$ wie in Teil c aus dem Mittelwert der beiden Messungen und sagen Sie mit den Gleichungen aus d) die Temperaturen nach {T_VERSUCH} Minuten voraus (Becher 3 mit Milch bei Raumtemperatur).
2. Ist der gemessene Unterschied zwischen Becher 1 und 2 größer als die Messunsicherheit? Nennen Sie zwei Gründe für Abweichungen vom Modell.

| Becher | Start $\vartheta(0)$ | $\vartheta({dt(P['t_mess']/60, 0)}\,\mathrm{{min}})$ | Milch $\vartheta_M$ | Vorhersage $\vartheta({T_VERSUCH}\,\mathrm{{min}})$ | Messung $\vartheta({T_VERSUCH}\,\mathrm{{min}})$ |
|:----------------------------------------------|:---------------------|:-----------------------|:--------------------|:------------------------|:------------------------|
| 1: Milch sofort | | | | | |
| 2: Milch nach {T_VERSUCH} min aus der Kühltasche | | | | | |
| 3: Milch nach {T_VERSUCH} min aus dem Glas | | | | | |

Raumtemperatur: \_\_\_\_\_\_\_\_\_\_ °C

Mischtemperatur Becher 1: \_\_\_\_\_\_\_\_\_\_ °C

$kA$ aus Becher 2 und 3: \_\_\_\_\_\_\_\_\_\_ W/K

"""

with open(os.path.join(TEILE, "t5a_kaffee.md"), "w", encoding="utf-8") as f:
    f.write(md)
with open(os.path.join(HIER, "t5_kaffee_ausgabe.txt"), "w", encoding="utf-8") as f:
    f.write("Tutorium 5, Aufgabe 1: Kaffee mit Milch (Zahlen aus kaffee_modell.py)\n")
    for name, wert, einheit in AUSGABE:
        f.write(f"{name:45s} {wert:10.4f} {einheit}\n")
print(open(os.path.join(HIER, "t5_kaffee_ausgabe.txt"), encoding="utf-8").read())
