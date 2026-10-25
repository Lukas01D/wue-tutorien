# -*- coding: utf-8 -*-
"""Erzeugt Aufgabenblatt und Lösung der Kaffee-Aufgabe (Markdown -> Word und PDF).
Alle Zahlen stammen aus kaffee_modell.py, damit Rechnung und Dokumente übereinstimmen.
Aufruf: python3 build_kaffee.py
"""
import os, re, subprocess
from kaffee_modell import P, rechne, nichtlinear, becher

HIER = os.path.dirname(os.path.abspath(__file__))
B = os.path.join(HIER, "build")
r = rechne(P)
K = 273.15


def de(x, n=2):
    """Zahl mit Dezimalkomma für LaTeX-Mathe (4{,}18)."""
    s = f"{x:.{n}f}"
    return s.replace(".", "{,}")


def dt(x, n=2):
    """Zahl mit Dezimalkomma für Fließtext (negatives Vorzeichen als echtes Minuszeichen)."""
    return f"{x:.{n}f}".replace(".", ",").replace("-", "\u2212")


U = lambda s: r"\,\mathrm{" + s + "}"
# häufige Werte
mK, mM = r["m_K"], r["m_M"]
CK, CM, CG = r["C_K"], r["C_M"], r["C_G"]
T10, T1, T2K, T2 = r["T1_0"], r["T1"], r["T2_K"], r["T2"]
nl1, nl2 = nichtlinear(4 / 3)
MILCH20 = rechne(dict(P, th_M=20.0))
MILCH60 = rechne(dict(P, th_M=60.0))
BECHER = becher()
assert BECHER["dT"] > 0 and MILCH20["dT"] > 0 and r["dT"] > 0 and MILCH60["dT"] < 0
import math as _m
CB = BECHER["C_T"]; CKB = CK + CB; CGB = CG + CB
T10B = (CKB * r["T_K0"] + CM * r["T_M"]) / CGB
eB = _m.exp(-BECHER["kA"] * P["t_end"] / CGB)
T_S = 60.0 + K
T10S = (CK * r["T_K0"] + CM * T_S) / CG
QM_RAUS = CM * (P["th_U"] - P["th_M"])                                     # h (2): Milch draußen, höchstens bis Raumtemperatur
DMIN_RAUS = ((r["Q2"] - r["Q1"]) - QM_RAUS) / CG
T2_RAUS = (CK * T2K + CM * (P["th_U"] + K)) / CG
assert abs((T1 - T2_RAUS) - DMIN_RAUS) < 1e-9
EFF1 = CK * (r["T_K0"] - r["T_U"]) * (r["e_G"] - r["e_K"]) / CG          # Kaffee-Effekt in K
EFF2_5 = CM * (r["T_M"] - r["T_U"]) * (r["e_G"] - 1) / CG                 # Milch-Effekt, Milch 5 °C
EFF2_60 = CM * (T_S - r["T_U"]) * (r["e_G"] - 1) / CG                     # Milch-Effekt, Schaum 60 °C
assert abs(EFF1 + EFF2_5 - r["dT"]) < 1e-9 and abs(EFF1 + EFF2_60 - MILCH60["dT"]) < 1e-9
assert abs(BECHER["T1"] - (r["T_U"] + (T10B - r["T_U"]) * eB)) < 1e-9
_TK60B = r["T_U"] + (r["T_K0"] - r["T_U"]) * _m.exp(-BECHER["kA"] * P["t_end"] / CKB)
BECHER3_DMIN = BECHER["T1"] - (CKB * _TK60B + CM * (P["th_U"] + K)) / CGB   # Versuch: Becher 3 mit Milch auf Raumtemperatur
SAMMLUNG_BLOCK = os.path.join(os.path.dirname(HIER), "sammlung", "teile", "t5a_kaffee.md")

KOPF = r"""---
lang: de
---

::: center
**[Tutorium 5: Wärmebilanzen (instationär global)]{.underline}**
:::

"""

LOESUNG = rf"""**[Lösung:]{{.underline}}**

**[Frage 1:]{{.underline}}** Tasse 1 (Milch sofort) ist nach einer Stunde wärmer: {dt(T1-K)} °C gegenüber {dt(T2-K)} °C. Das Argument des Mitbewohners trägt nicht: Erhalten bleibt die Energie von Kaffee, Milch und Umgebung zusammen; wie viel Wärme an die Umgebung geht, hängt vom Temperaturverlauf ab (Aufgabe 1, Teile d und e).

**[Aufgabe 1:]{{.underline}}**

[Geg.:]{{.underline}} Größen aus der Tabelle, daraus

$m_K = \rho_K V_K = {de(mK, 3)}{U('kg')}$, $\quad m_M = \rho_M V_M = {de(mM, 4)}{U('kg')}$,

$m_K c_{{p,K}} = {de(CK, 1)}{U('J/K')}$, $\quad m_M c_{{p,M}} = {de(CM, 1)}{U('J/K')}$

[Ges.:]{{.underline}} $\vartheta_{{1,0}}$, $kA$, $\vartheta_1$ und $\vartheta_2$ nach 60 min, $Q_1$ und $Q_2$; dazu $kA$, $\vartheta_1$ und $\vartheta_2$ mit Becher (f), mit Milchschaum (g) und die Milchtemperatur aus h

[Skizze:]{{.underline}} Bilanzraum um den Tasseninhalt (Abb. L1)

[Annahmen:]{{.underline}} siehe Aufgabe

[Ansatz:]{{.underline}} Energiebilanz für das Mischen (a) und globale instationäre Energiebilanz um das geschlossene System „Tasseninhalt“ (b bis e)

![](grafik/AbbL1_Bilanzraum.png){{width=44%}}

**Abb. L1:** Bilanzraum um den Tasseninhalt

**a)** Energiebilanz für das Mischen (geschlossenes System, keine Wärmeabgabe während des Mischens): Die Wärme, die der Kaffee abgibt, nimmt die Milch auf.

$$m_K c_{{p,K}}\,(T_{{K,0}} - T_{{1,0}}) = m_M c_{{p,M}}\,(T_{{1,0}} - T_M)$$

Umstellen nach $T_{{1,0}}$ und Werte einsetzen:

$$T_{{1,0}} = \frac{{m_K c_{{p,K}}\,T_{{K,0}} + m_M c_{{p,M}}\,T_M}}{{m_K c_{{p,K}} + m_M c_{{p,M}}}}$$

$$T_{{1,0}} = \frac{{{de(CK,1)}{U('J/K')} \cdot {de(r['T_K0'])}{U('K')} + {de(CM,1)}{U('J/K')} \cdot {de(r['T_M'])}{U('K')}}}{{{de(CG,1)}{U('J/K')}}} = {de(T10)}{U('K')} = {de(T10-K)}{U('°C')}$$

**b)** Globale instationäre Energiebilanz um das geschlossene System „Tasseninhalt“ ($V = \mathrm{{const.}}$, kein Zu- und Abfluss, keine Quelle):

$$\frac{{dU}}{{dt}} = -\dot{{Q}}_{{ab}} \quad\Rightarrow\quad m\,c_p\,\frac{{dT}}{{dt}} = -kA\,(T - T_u)$$

Trennung der Variablen und Integration von $t = 0\,\mathrm{{s}}$ ($T = T_0$) bis $t$:

$$\int_{{T_0}}^{{T}} \frac{{dT}}{{T - T_u}} = -\frac{{kA}}{{m\,c_p}} \int_0^{{t}} dt \quad\Rightarrow\quad \ln\frac{{T - T_u}}{{T_0 - T_u}} = -\frac{{kA}}{{m\,c_p}}\,t$$

Umstellen nach $T$:

$$T(t) = T_u + (T_0 - T_u)\cdot \exp\left(-\frac{{kA}}{{m\,c_p}}\,t\right)$$

Für Tasse 1 gilt $m\,c_p = m_K c_{{p,K}} + m_M c_{{p,M}}$, für Tasse 2 bis zum Zugießen $m\,c_p = m_K c_{{p,K}}$.

**c)** Lösung aus b) für den Kaffee ohne Milch nach $kA$ umstellen und die Messung in Tasse 2 einsetzen:

$$kA = -\frac{{m_K c_{{p,K}}}}{{t}}\,\ln\frac{{T_K(t) - T_u}}{{T_{{K,0}} - T_u}} =-\frac{{{de(CK,1)}{U('J/K')}}}{{{de(P['t_mess'],0)}{U('s')}}}\,\ln\frac{{{de(P['th_mess']-P['th_U'],0)}{U('K')}}}{{{de(P['th_K0']-P['th_U'],0)}{U('K')}}} = {de(r['kA'],4)}{U('W/K')}$$

Zur Einordnung: Zeitkonstante $\tau = m\,c_p/kA$ ohne Milch ${de(r['tau_K']/60,1)}{U('min')}$, mit Milch ${de(r['tau_G']/60,1)}{U('min')}$. Das passt zu Messungen an einem offenen, nicht umgerührten Keramikbecher ($\tau \approx 41\,\mathrm{{min}}$ aus der Steigung in Abb. 6 bei Ferreira 2025).

**d)** Tasse 1: Anfangsbedingung $T(0\,\mathrm{{s}}) = T_{{1,0}}$ und $m\,c_p = m_K c_{{p,K}} + m_M c_{{p,M}}$:

$$T_1 = T_u + (T_{{1,0}} - T_u)\cdot \exp\left(-\frac{{kA\,t}}{{m_K c_{{p,K}} + m_M c_{{p,M}}}}\right)$$

$$T_1 = {de(r['T_U'])}{U('K')} + {de(T10-r['T_U'])}{U('K')} \cdot {de(r['e_G'],4)} = {de(T1)}{U('K')} = {de(T1-K)}{U('°C')}$$

Tasse 2: erst Abkühlen mit $m\,c_p = m_K c_{{p,K}}$, dann Mischen wie in a):

$$T_K(60\,\mathrm{{min}}) = T_u + (T_{{K,0}} - T_u)\cdot \exp\left(-\frac{{kA\,t}}{{m_K c_{{p,K}}}}\right)$$

$$T_K(60\,\mathrm{{min}}) = {de(r['T_U'])}{U('K')} + {de(r['T_K0']-r['T_U'])}{U('K')} \cdot {de(r['e_K'],4)} = {de(T2K)}{U('K')} = {de(T2K-K)}{U('°C')}$$

$$T_2 = \frac{{m_K c_{{p,K}}\,T_K(60\,\mathrm{{min}}) + m_M c_{{p,M}}\,T_M}}{{m_K c_{{p,K}} + m_M c_{{p,M}}}}$$

$$T_2 = \frac{{{de(CK,1)}{U('J/K')} \cdot {de(T2K)}{U('K')} + {de(CM,1)}{U('J/K')} \cdot {de(r['T_M'])}{U('K')}}}{{{de(CG,1)}{U('J/K')}}} = {de(T2)}{U('K')} = {de(T2-K)}{U('°C')}$$

Tasse 2 ist um ${de(r['dT'])}{U('K')}$ kühler.

**e)** Die abgegebene Wärme folgt aus der Energiebilanz über die Abkühlzeit:

$$Q_1 = (m_K c_{{p,K}} + m_M c_{{p,M}})\,(T_{{1,0}} - T_1) = {de(CG,1)}{U('J/K')} \cdot {de(T10-T1)}{U('K')} = {de(r['Q1']/1e3)}{U('kJ')}$$

$$Q_2 = m_K c_{{p,K}}\,(T_{{K,0}} - T_K(60\,\mathrm{{min}})) = {de(CK,1)}{U('J/K')} \cdot {de(r['T_K0']-T2K)}{U('K')} = {de(r['Q2']/1e3)}{U('kJ')}$$

Kontrolle: Beide Tassen enthalten am Ende dieselbe Menge Kaffee und Milch. Der Temperaturunterschied folgt allein aus der Mehrabgabe: $(Q_2 - Q_1)/(m_K c_{{p,K}} + m_M c_{{p,M}}) = {de((r['Q2']-r['Q1'])/CG)}{U('K')}$, wie in d).

Erklärung: Der Wärmestrom $\dot{{Q}}_{{ab}} = kA\,(T - T_u)$ ist umso größer, je heißer der Tasseninhalt ist. Der Kaffee in Tasse 2 startet ohne Milch heißer (Wärmestrom am Anfang {dt(r['Qdot2_0'],1)} W gegenüber {dt(r['Qdot1_0'],1)} W in Tasse 1) und bleibt es bis etwa {dt(r['t_schnitt']/60,0)} min (Abb. L2). Er gibt deshalb mehr Wärme ab. Die Energie bleibt erhalten, aber wie viel davon an die Umgebung geht, hängt vom Temperaturverlauf ab. Der Mitbewohner hat also nicht recht. Wer seinen Kaffee später möglichst warm trinken will, gibt die Milch sofort hinein.

![](grafik/AbbL2_Temperaturverlauf.png){{width=70%}}

**Abb. L2:** Temperaturverlauf beider Tassen

**f)** Die Wärmekapazität des Bechers kommt zu jedem Tasseninhalt hinzu: $C_B = m_B c_B = {de(0.300,3)}{U('kg')} \cdot {de(850,0)}{U('J/(kg\\,K)')} = {de(CB,1)}{U('J/K')}$. Messung in Tasse 2 wie in c), jetzt mit $m_K c_{{p,K}} + C_B$:

$$kA = -\frac{{m_K c_{{p,K}} + C_B}}{{t}}\,\ln\frac{{T_K(t) - T_u}}{{T_{{K,0}} - T_u}} = -\frac{{{de(CKB,1)}{U('J/K')}}}{{{de(P['t_mess'],0)}{U('s')}}}\,\ln\frac{{{de(P['th_mess']-P['th_U'],0)}{U('K')}}}{{{de(P['th_K0']-P['th_U'],0)}{U('K')}}} = {de(BECHER['kA'],4)}{U('W/K')}$$

Tasse 1: Mischen mit Becher (er hat vorher die Kaffeetemperatur), dann Abkühlen:

$$T_{{1,0}} = \frac{{(m_K c_{{p,K}} + C_B)\,T_{{K,0}} + m_M c_{{p,M}}\,T_M}}{{m_K c_{{p,K}} + C_B + m_M c_{{p,M}}}} = {de(T10B)}{U('K')}$$

$$T_1 = T_u + (T_{{1,0}} - T_u)\cdot \exp\left(-\frac{{kA\,t}}{{m_K c_{{p,K}} + C_B + m_M c_{{p,M}}}}\right)$$

$$T_1 = {de(r['T_U'])}{U('K')} + {de(T10B-r['T_U'])}{U('K')} \cdot {de(eB,4)} = {de(BECHER['T1'])}{U('K')} = {de(BECHER['T1']-K)}{U('°C')}$$

Tasse 2: Der schwarze Kaffee kühlt mit derselben Zeitkonstante ab wie in der Messung, also wie in d) auf $T_K(60\,\mathrm{{min}}) = {de(T2K)}{U('K')}$. Dann Mischen mit Becher:

$$T_2 = \frac{{(m_K c_{{p,K}} + C_B)\,T_K(60\,\mathrm{{min}}) + m_M c_{{p,M}}\,T_M}}{{m_K c_{{p,K}} + C_B + m_M c_{{p,M}}}} = {de(BECHER['T2'])}{U('K')} = {de(BECHER['T2']-K)}{U('°C')}$$

Tasse 2 bleibt kühler, der Unterschied sinkt von {dt(r['dT'])} K auf {dt(BECHER['dT'])} K: Der Becher gibt beim Mischen Wärme an die kalte Milch ab und dämpft so den Mischsprung.

**g)** Rechnung wie in a) und d), nur mit $T_S = {de(T_S)}{U('K')}$ statt $T_M$:

$$T_{{1,0}} = \frac{{m_K c_{{p,K}}\,T_{{K,0}} + m_M c_{{p,M}}\,T_S}}{{m_K c_{{p,K}} + m_M c_{{p,M}}}} = {de(T10S)}{U('K')}$$

$$T_1 = T_u + (T_{{1,0}} - T_u)\cdot {de(r['e_G'],4)} = {de(MILCH60['T1'])}{U('K')} = {de(MILCH60['T1']-K)}{U('°C')}$$

$$T_2 = \frac{{m_K c_{{p,K}}\,T_K(60\,\mathrm{{min}}) + m_M c_{{p,M}}\,T_S}}{{m_K c_{{p,K}} + m_M c_{{p,M}}}} = {de(MILCH60['T2'])}{U('K')} = {de(MILCH60['T2']-K)}{U('°C')}$$

Jetzt ist Tasse 2 um {dt(-MILCH60['dT'])} K wärmer. Zieht man die Ergebnisse aus d) voneinander ab, ergeben sich zwei Anteile:

$$\vartheta_1 - \vartheta_2 = \underbrace{{\frac{{m_K c_{{p,K}}\,(\vartheta_{{K,0}} - \vartheta_u)\,(e_G - e_K)}}{{m_K c_{{p,K}} + m_M c_{{p,M}}}}}}_{{\text{{Kaffee-Effekt}}}} + \underbrace{{\frac{{m_M c_{{p,M}}\,(\vartheta_M - \vartheta_u)\,(e_G - 1)}}{{m_K c_{{p,K}} + m_M c_{{p,M}}}}}}_{{\text{{Milch-Effekt}}}}$$

mit $e_G = \exp(-kA\,t/(m_K c_{{p,K}} + m_M c_{{p,M}})) = {de(r['e_G'],4)}$ und $e_K = \exp(-kA\,t/(m_K c_{{p,K}})) = {de(r['e_K'],4)}$. Kaffee-Effekt: Mit Milch ist mehr Wärmekapazität in der Tasse, der Kaffee kühlt langsamer ab; er spricht immer für „sofort“ ({dt(EFF1)} K). Milch-Effekt: Spät zugegossene Milch bringt ihre Temperatur unverändert mit. Kalte Milch kühlt dann stärker ({dt(EFF2_5)} K für „sofort“), heißer Schaum wärmt stärker ({dt(EFF2_60)} K, also für „später“).

**h)** (1) Beide Anteile heben sich auf, wenn $\vartheta_1 = \vartheta_2$:

$$\vartheta_M = \vartheta_u + \frac{{m_K c_{{p,K}}\,(\vartheta_{{K,0}} - \vartheta_u)\,(e_G - e_K)}}{{m_M c_{{p,M}}\,(1 - e_G)}} = {de(P['th_U'],0)}{U('°C')} + {de(r['th_M_gleich']-P['th_U'],1)}{U('K')} = {de(r['th_M_gleich'],1)}{U('°C')}$$

Erst Milch über etwa {dt(r['th_M_gleich'],0)} °C dreht das Ergebnis um.

Zu (2): Nein. Draußen erwärmt sich die Milch höchstens auf Raumtemperatur und nimmt dabei aus der Raumluft höchstens

$$Q_M = m_M c_{{p,M}}\,(\vartheta_u - \vartheta_M) = {de(CM,1)}{U('J/K')} \cdot {de(P['th_U']-P['th_M'],0)}{U('K')} = {de(QM_RAUS/1e3)}{U('kJ')}$$

auf. Tasse 2 hat nach e) aber $Q_2 - Q_1 = {de((r['Q2']-r['Q1'])/1e3)}{U('kJ')}$ mehr abgegeben als Tasse 1. Selbst im günstigsten Fall bleibt Tasse 2 deshalb um mindestens

$$\frac{{(Q_2 - Q_1) - Q_M}}{{m_K c_{{p,K}} + m_M c_{{p,M}}}} = \frac{{{de((r['Q2']-r['Q1'])/1e3)}{U('kJ')} - {de(QM_RAUS/1e3)}{U('kJ')}}}{{{de(CG,1)}{U('J/K')}}} = {de(DMIN_RAUS)}{U('K')}$$

kühler (mit Milch von 20 °C: $\vartheta_2 = {de(T2_RAUS-K)}{U('°C')}$ gegenüber $\vartheta_1 = {de(T1-K)}{U('°C')}$). Der Kipppunkt aus (1) entscheidet die Frage nicht allein, weil er für gleich warme Milch in beiden Tassen gilt.

"""

HINWEISE = rf"""```{{=latex}}
\needspace{{7\baselineskip}}
```

**[Hinweise für die Tutoriumsleitung]{{.underline}}**

- *Typische Fehler:* Mischtemperatur nach dem Volumen statt nach $m\,c_p$ gewichtet; in Tasse 1 nur mit $m_K c_{{p,K}}$ gerechnet; in Tasse 2 schon während der 60 Minuten mit $m_K c_{{p,K}} + m_M c_{{p,M}}$ gerechnet; in f) das alte $kA$ weiterverwendet (dann {dt(becher(kA_neu=False)['T1']-K,1)} und {dt(becher(kA_neu=False)['T2']-K,1)} °C: Aussage gleich, aber nicht mehr passend zur Messung).
- *Fehlvorstellungen:* „Energieerhaltung, also egal“: Erhalten bleibt die Energie von Kaffee, Milch und Umgebung zusammen, nicht die des Tasseninhalts (Teil e). „Schaum ist kälter als der Kaffee, wirkt also wie kalte Milch“: Entscheidend ist nicht der Vergleich mit dem Kaffee, sondern ob die Milch wärmer als der Kipppunkt aus h ist.
- *Was die Rechnung weglässt:* Bei hoher Temperatur trägt die Verdunstung rund die Hälfte der Wärmeabgabe (Condoret 2007, Tab. 2), deshalb ist $kA$ in Wirklichkeit nicht konstant. Mit einer überlinearen Wärmeabgabe $\dot{{Q}}_{{ab}} \propto (T - T_u)^{{4/3}}$, angepasst an dieselbe Messung, ergeben sich $\vartheta_1 = {de(nl1-K)}{U('°C')}$ und $\vartheta_2 = {de(nl2-K)}{U('°C')}$, also {dt(nl1-nl2)} K statt {dt(r['dT'])} K: Der Vorsprung der heißeren Tasse 2 beim Wärmeverlust wächst.
- *Zum Weiterdenken:* Hätte die Milch in beiden Tassen Raumtemperatur, wäre der Unterschied mit {dt(MILCH20['dT'],1)} K kleiner, aber vorhanden. Der schwarze Kaffee ist bis etwa {dt(r['t_schnitt']/60,0)} min heißer als das Gemisch in Tasse 1 (Abb. L2) und verliert deshalb mehr Wärme; erst die kalte Milch am Ende macht Tasse 2 deutlich kühler.
- *Versuch:* Mit echten, vorgewärmten Bechern sind nach 60 Minuten zwischen Becher 1 und 2 rund 3 K Unterschied zu erwarten (nach 30 Minuten schon gut 2,5 K), mit einem Küchenthermometer gut messbar; Becher 3 (Milch draußen) bleibt um mindestens {dt(BECHER3_DMIN,1)} K kühler als Becher 1. Starttemperatur messen statt 80 °C annehmen, ein Thermometer für alle Becher verwenden, vor jeder Messung umrühren. Heißes Wasser verhält sich wie Kaffee; Verbrühungsgefahr beachten.

```{{=latex}}
\needspace{{7\baselineskip}}
```

**[Quellen der Arbeitswerte]{{.underline}}**

- Kaffee: Ausschank 71 bis 85 °C (Brown & Diller 2008, Burns 34, 648); beim Eingießen 2 bis 5 K weniger (Abraham & Diller 2019, J. Food Sci. 84); Stoffwerte wie Wasser (SCA, Gehalt an gelösten Stoffen 1,15 bis 1,35 %).
- Milch: Kühlschrank höchstens 7 °C, besser unter 5 °C (Bundesinstitut für Risikobewertung, 2023); im Mittel 31 g Milch je Tasse (FSANZ 2011); Dichte 1027 bis 1033 kg/m³ (Goff, Dairy Science and Technology); $c_p$ wie in Tutorium 8.
- Abkühlung: offener, nicht umgerührter Keramikbecher, $\tau \approx 41\,\mathrm{{min}}$ aus der Steigung 0,0241 1/min in Abb. 6 (Ferreira 2025, Phys. Educ. 60, 035001); Verdunstung bei 79 °C 12,0 von 22,7 W (Condoret 2007, Chem. Eng. Educ. 41, 137, Tab. 2).
- Milchschaum 55 bis 65 °C (Thermoplan, Coffee knowledge: milk); Keramikbecher 300 g mit 0,85 kJ/(kg·K) als Arbeitswert (Schätzung).
- Rechenskript: nachrechnung_kaffee.py mit kaffee_modell.py.

"""


def schreibe(name, text):
    with open(os.path.join(HIER, name), "w", encoding="utf-8") as f:
        f.write(text)


# Einleitungssatz und folgende Formeln in einen Absatz: kein Seitenumbruch dazwischen, keine Leerzeile vor der zweiten Formel
LOESUNG = re.sub(r"([^\n])\n\n(\$\$)", r"\1\n\2", LOESUNG)
# Aufgabentext genau wie in der Aufgabensammlung (Ausgangssituation, Frage 1, Aufgabe 1, Versuch)
with open(SAMMLUNG_BLOCK, encoding="utf-8") as _f:
    BLOCK = _f.read()
BLOCK = re.sub(r"^## .*\n+", "", BLOCK, count=1).replace("<!-- T5_FRAGEN -->\n\n", "").replace("<!-- T5_FRAGEN -->", "")
md_aufgabe = KOPF + BLOCK
md_loesung = KOPF + BLOCK + "::: seitenumbruch\n:::\n\n" + LOESUNG + HINWEISE
schreibe("Kaffee_Aufgabe.md", md_aufgabe)
schreibe("Kaffee_Loesung.md", md_loesung)

for name in ("Kaffee_Aufgabe", "Kaffee_Loesung"):
    md = os.path.join(HIER, name + ".md")
    subprocess.run(["pandoc", md, "-o", os.path.join(HIER, name + ".pdf"), "--pdf-engine=xelatex",
                    "-H", os.path.join(B, "kopf.tex"), "--lua-filter", os.path.join(B, "lehrstuhl.lua"),
                    "-V", "documentclass=article", "-V", "fontsize=11pt", "-V", "mainfont=Carlito",
                    "-V", "mathfont=Latin Modern Math", "--resource-path", HIER + ":" + os.path.join(os.path.dirname(HIER), "sammlung")], check=True)
    subprocess.run(["pandoc", md, "-o", os.path.join(HIER, name + ".docx"),
                    "--reference-doc", os.path.join(B, "referenz_lehrstuhl.docx"),
                    "--lua-filter", os.path.join(B, "lehrstuhl.lua"), "--resource-path", HIER + ":" + os.path.join(os.path.dirname(HIER), "sammlung")], check=True)


def word_zusammenhalten(pfad):
    """Word: Tabellen nicht über den Seitenwechsel trennen, Zwischenüberschriften und Bilder mit dem Folgeabsatz
    zusammenhalten (gleiche Nachbearbeitung wie in sammlung/build/sammlung_bauen.py)."""
    import zipfile, shutil
    with zipfile.ZipFile(pfad) as z:
        inhalt = {n: z.read(n) for n in z.namelist()}
    d = inhalt["word/document.xml"].decode("utf-8")

    def keep(par):
        if "<w:keepNext/>" in par:
            return par
        if "<w:pPr>" in par:
            return re.sub(r'(<w:pPr>(?:<w:pStyle w:val="[^"]*"\s*/>)?)', r"\1<w:keepNext/>", par, count=1)
        return par.replace("<w:p>", "<w:p><w:pPr><w:keepNext/></w:pPr>", 1)

    def tabelle(m):
        t = m.group(0)
        zeilen = re.findall(r"<w:tr>.*?</w:tr>|<w:tr .*?</w:tr>", t, flags=re.S)
        for z in zeilen[:-1]:
            t = t.replace(z, re.sub(r"<w:p>.*?</w:p>", lambda mm: keep(mm.group(0)), z, flags=re.S), 1)
        t = t.replace("<w:trPr>", "<w:trPr><w:cantSplit/>")
        return re.sub(r"<w:tr>(?!<w:trPr>)", "<w:tr><w:trPr><w:cantSplit/></w:trPr>", t)
    d = re.sub(r"<w:tbl>.*?</w:tbl>", tabelle, d, flags=re.S)

    muster = re.compile(r"^(Gegebene Größen|Annahmen|Aufgabenstellung|Frage \d|Aufgabe \d|Ausgangssituation|Versuch zu|Lösung|Hinweise für|Quellen der)")
    def absatz(m):
        par = m.group(0)
        text = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", par)).strip()
        if muster.match(text) or ("<pic:pic" in par and not text):
            return keep(par)
        return par
    teile = re.split(r"(<w:tbl>.*?</w:tbl>)", d, flags=re.S)
    for k in range(0, len(teile), 2):
        teile[k] = re.sub(r"<w:p>(?:(?!</w:p>).)*?</w:p>|<w:p .*?</w:p>", absatz, teile[k], flags=re.S)
    inhalt["word/document.xml"] = "".join(teile).encode("utf-8")
    tmp = pfad + ".tmp"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        for n, b in inhalt.items():
            z.writestr(n, b)
    shutil.move(tmp, pfad)


for name in ("Kaffee_Aufgabe", "Kaffee_Loesung"):
    word_zusammenhalten(os.path.join(HIER, name + ".docx"))
print("fertig:", r["T1"] - K, r["T2"] - K)
