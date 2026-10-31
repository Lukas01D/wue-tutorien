# -*- coding: utf-8 -*-
"""Erzeugt Aufgabenblatt und Lösung der Kaffee-Aufgabe (Markdown -> Word und PDF).
Alle Zahlen stammen aus kaffee_modell.py, damit Rechnung und Dokumente übereinstimmen.
Aufruf: python3 build_kaffee.py
"""
import os, re, subprocess

KOPF_RECHTS = "Sommersemester 2027"                                        # rechts in der Kopfzeile (Endfassung, TL 30.10.2026)
from kaffee_modell import P, rechne, nichtlinear, becher, zwei_tassen, gleichstand

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


def aufrecht(text):
    """Beschreibende Indizes in Formeln aufrecht setzen (Ä24); Größen als Index (p, v) und Zahlen bleiben."""
    paare = [("_{ab}", r"_{\mathrm{ab}}"), ("_{zu}", r"_{\mathrm{zu}}"), ("_{KV}", r"_{\mathrm{KV}}"),
             ("_{nachher}", r"_{\mathrm{nachher}}"), ("_{vorher}", r"_{\mathrm{vorher}}"),
             ("_{p,K}", r"_{p,\mathrm{K}}"), ("_{p,M}", r"_{p,\mathrm{M}}"), ("_{K,0}", r"_{\mathrm{K},0}"),
             ("_{M,h}", r"_{\mathrm{M,h}}")]

    def formel(m):
        f = m.group(0)
        for a, b in paare:
            f = f.replace(a, b)
        return re.sub(r"_([KMuBG])(?![A-Za-z])", r"_\\mathrm{\1}", f)
    return re.sub(r"\$\$.*?\$\$|\$[^$]+?\$", formel, text, flags=re.S)
# häufige Werte
mK, mM = r["m_K"], r["m_M"]
CK, CM, CG = r["C_K"], r["C_M"], r["C_G"]
T10, T1, T2K, T2 = r["T1_0"], r["T1"], r["T2_K"], r["T2"]
nl1, nl2 = nichtlinear(4 / 3)
MILCH20 = rechne(dict(P, th_M=20.0))
MILCH60 = rechne(dict(P, th_M=P["th_Mh"]))                                  # f: erwärmte Milch
T_S = P["th_Mh"] + K
BECHER = becher()
assert BECHER["dT"] > 0 and MILCH20["dT"] > 0 and r["dT"] > 0 and MILCH60["dT"] < 0
import math as _m
CB = BECHER["C_T"]; CKB = CK + CB; CGB = CG + CB
T10B = (CKB * r["T_K0"] + CM * r["T_M"]) / CGB
eB = _m.exp(-BECHER["kA"] * P["t_end"] / CGB)
T10S = (CK * r["T_K0"] + CM * T_S) / CG
QM_RAUS = CM * (P["th_U"] - P["th_M"])                                     # Zusatzfrage (2): Milch draußen, höchstens bis Raumtemperatur
DMIN_RAUS = ((r["Q2"] - r["Q1"]) - QM_RAUS) / CG
T2_RAUS = (CK * T2K + CM * (P["th_U"] + K)) / CG
assert abs((T1 - T2_RAUS) - DMIN_RAUS) < 1e-9
EFF1 = CK * (r["T_K0"] - r["T_U"]) * (r["e_G"] - r["e_K"]) / CG          # Kaffee-Effekt in K
EFF2_5 = CM * (r["T_M"] - r["T_U"]) * (r["e_G"] - 1) / CG                 # Milch-Effekt, Milch 5 °C
EFF2_60 = CM * (T_S - r["T_U"]) * (r["e_G"] - 1) / CG                     # Milch-Effekt, erwärmte Milch 60 °C
assert abs(EFF1 + EFF2_5 - r["dT"]) < 1e-9 and abs(EFF1 + EFF2_60 - MILCH60["dT"]) < 1e-9
assert abs(BECHER["T1"] - (r["T_U"] + (T10B - r["T_U"]) * eB)) < 1e-9
_TK60B = r["T_U"] + (r["T_K0"] - r["T_U"]) * _m.exp(-BECHER["kA"] * P["t_end"] / CKB)
BECHER3_DMIN = BECHER["T1"] - (CKB * _TK60B + CM * (P["th_U"] + K)) / CGB   # Versuch: Becher 3 mit Milch auf Raumtemperatur
SAMMLUNG_BLOCK = os.path.join(os.path.dirname(HIER), "sammlung", "teile", "t5a_kaffee.md")

# Werte für die Ergänzungen nach der Prüfung (Oktober 2026), alle aus dem Modell
eKB = _m.exp(-BECHER["kA"] * P["t_end"] / CKB)
EFF1_B = CKB * (r["T_K0"] - r["T_U"]) * (eB - eKB) / CGB                 # Kaffee-Effekt mit Becher
EFF2_B = CM * (r["T_M"] - r["T_U"]) * (eB - 1) / CGB                     # Milch-Effekt mit Becher
assert abs(EFF1_B + EFF2_B - BECHER["dT"]) < 1e-9
KA_VERH = BECHER["kA"] / r["kA"]
TAU_B = CKB / BECHER["kA"]
TAU1_B = CGB / BECHER["kA"]                                               # g: Zeitkonstante von Tasse 1 mit Becher
FEHLER_F1 = r["T_U"] + (T10 - r["T_U"]) * eB                              # g ohne Becher im Mischen
Q66, Q68 = rechne(dict(P, th_mess=66.0)), rechne(dict(P, th_mess=68.0))
TH_TAU = P["th_U"] + (P["th_K0"] - P["th_U"]) * _m.exp(-1)
D_BECHER = 0.08                                                            # m, Innendurchmesser (Annahme für die Abschätzung)
H0 = P["V_K"] / (_m.pi * D_BECHER**2 / 4); HM = (P["V_K"] + P["V_M"]) / (_m.pi * D_BECHER**2 / 4)
A0 = _m.pi * D_BECHER * H0 + 2 * _m.pi * D_BECHER**2 / 4; AM = _m.pi * D_BECHER * HM + 2 * _m.pi * D_BECHER**2 / 4
DT_KA103, DT_KA105 = zwei_tassen(kA1_faktor=1.03)["dT"], zwei_tassen(kA1_faktor=1.05)["dT"]
KIPP_KA = gleichstand(lambda f: zwei_tassen(kA1_faktor=f)["dT"], 1.0, 2.0)
KIPP_KA_B = gleichstand(lambda f: zwei_tassen(C_T=CB, kA1_faktor=f)["dT"], 1.0, 2.0)
KIPP_105 = gleichstand(lambda tm: zwei_tassen(th_M1=tm, kA1_faktor=1.05)["dT"])
KIPP_095 = gleichstand(lambda tm: zwei_tassen(th_M1=tm, kA1_faktor=0.95)["dT"])
KIPP_43 = gleichstand(lambda tm: (lambda a: a[0] - a[1])(nichtlinear(4 / 3, dict(P, th_M=tm))), 0.0, 100.0)
G_SCHAUM = gleichstand(lambda f: zwei_tassen(th_M1=P["th_Mh"], kA1_faktor=f)["dT"], 0.5, 1.0)
G_SCHAUM10 = zwei_tassen(th_M1=P["th_Mh"], kA1_faktor=0.90)["dT"]
G_SPAET_MIN = gleichstand(lambda t2: zwei_tassen(th_M1=P["th_Mh"], th_M2=t2)["dT"])
H2_NUR_SPAET = gleichstand(lambda t2: zwei_tassen(th_M2=t2)["dT"])
M_VERD = 0.5 * r["Q2"] / P["dh_v"]
P60_C, P60_F = r["kA"] * (60.0 - P["th_U"]), BECHER["kA"] * (60.0 - P["th_U"])
T_MAX = max(range(1, 121), key=lambda m: zwei_tassen(t_end=m * 60.0)["dT"])
DT_MAX = zwei_tassen(t_end=T_MAX * 60.0)["dT"]
T_V = 40                                                                   # min, Versuch
V40 = zwei_tassen(C_T=CB, t_end=T_V * 60.0); V40_3 = zwei_tassen(C_T=CB, th_M2=P["th_U"], t_end=T_V * 60.0)
V40_D = zwei_tassen(t_end=T_V * 60.0)
V40_103, V40_105 = zwei_tassen(C_T=CB, t_end=T_V * 60.0, kA1_faktor=1.03), zwei_tassen(C_T=CB, t_end=T_V * 60.0, kA1_faktor=1.05)
RATE40 = BECHER["kA"] * 20.0 / CGB * 60
ZERL_LIN = P["th_M"] + (P["th_Mh"] - P["th_M"]) * r["dT"] / (r["dT"] - MILCH60["dT"])
SIM_KIPP = {t: gleichstand(lambda x: zwei_tassen(th_M1=x, t_end=t * 60.0)["dT"]) for t in (30, 90)}   # Simulation, Frage 2
SIM_B = zwei_tassen(C_T=CB)                                                                          # Simulation, Frage 3
SIM_Q1B, SIM_Q2B = CGB * (SIM_B["T1_0"] - SIM_B["T1"]), CKB * (r["T_K0"] - SIM_B["T2_K"])
SIM_SPAET2 = (CK * P["th_U"] + CM * P["th_M"]) / CG                                                  # Simulation, Frage 1: sehr späte Zugabe
assert abs(zwei_tassen(t_end=1e7)["th2"] - SIM_SPAET2) < 1e-9 and abs(zwei_tassen(t_end=1e7)["th1"] - P["th_U"]) < 1e-9
assert abs(T_MAX - r["t_schnitt"] / 60) < 1.0 and abs(SIM_B["dT"] - BECHER["dT"]) < 1e-9
assert abs(ZERL_LIN - r["th_M_gleich"]) < 1e-6 and abs(G_SCHAUM - 0.944) < 0.001 and V40["dT"] > 0

KOPF = r"""---
lang: de
---

::: center
**[Tutorium 5: Wärmebilanzen (instationär global)]{.underline}**
:::

"""

LOESUNG = rf"""**[Lösung]{{.underline}}**

**[Frage 1]{{.underline}}**

Tasse 1 (Milch sofort) ist nach einer Stunde wärmer: {dt(T1-K)} °C gegenüber {dt(T2-K)} °C. Das Argument des Mitbewohners trägt nicht: Erhalten bleibt die Energie von Kaffee, Milch und Umgebung zusammen; wie viel Wärme an die Umgebung geht, hängt vom Temperaturverlauf ab (Aufgabe 1, Teile d und e).

**[Aufgabe 1]{{.underline}}**

**Geg.:** Größen aus der Tabelle, daraus

$m_K = \rho_K V_K = {de(mK, 3)}{U('kg')}$, $\quad m_M = \rho_M V_M = {de(mM, 4)}{U('kg')}$,

$m_K c_{{p,K}} = {de(CK, 1)}{U('J/K')}$, $\quad m_M c_{{p,M}} = {de(CM, 1)}{U('J/K')}$

**Ges.:** $\vartheta_{{1,0}}$, $kA$, $\vartheta_1$ und $\vartheta_2$ nach 60 min, $Q_1$ und $Q_2$; dazu $\vartheta_1$ und $\vartheta_2$ mit erwärmter Milch (f) sowie $kA$, $\vartheta_1$ und $\vartheta_2$ mit Becher (g)

**Skizze:** Bilanzraum um den Tasseninhalt (Abb. L1)

**Annahmen:** siehe Aufgabe

**Ansatz:** Energiebilanz für das Mischen (a) und globale instationäre Energiebilanz um das geschlossene System „Tasseninhalt“ (b bis e)

![](grafik/AbbL1_Bilanzraum.png){{width=50%}}

**Abb. L1:** Bilanzraum um den Tasseninhalt (in Teil g: Inhalt und Becher)

**a)** Energiebilanz um Kaffee und Milch zusammen (geschlossenes System, keine Wärmeabgabe während des Mischens): Die innere Energie bleibt gleich, $U_{{nachher}} = U_{{vorher}}$.

$$m_K c_{{p,K}}\,(T_{{1,0}} - T_{{K,0}}) + m_M c_{{p,M}}\,(T_{{1,0}} - T_M) = 0$$

Umstellen nach $T_{{1,0}}$ und Werte einsetzen:

$$T_{{1,0}} = \frac{{m_K c_{{p,K}}\,T_{{K,0}} + m_M c_{{p,M}}\,T_M}}{{m_K c_{{p,K}} + m_M c_{{p,M}}}}$$

$$T_{{1,0}} = \frac{{{de(CK,1)}{U('J/K')} \cdot {de(r['T_K0'])}{U('K')} + {de(CM,1)}{U('J/K')} \cdot {de(r['T_M'])}{U('K')}}}{{{de(CG,1)}{U('J/K')}}} = {de(T10)}{U('K')} = {de(T10-K)}{U('°C')}$$

**b)** Allgemeine Energiebilanz (Foliensatz 05, Folie 8, mit den Enthalpieströmen wie in Gl. (4-1) der Einleitung zum bisherigen Tutorium 5):

$$\frac{{dU}}{{dt}} = \dot{{H}}_{{zu}} - \dot{{H}}_{{ab}} + \dot{{Q}}_{{zu}} - \dot{{Q}}_{{ab}} + \dot{{Q}}_{{KV}}$$

Für den Tasseninhalt entfallen $\dot{{H}}_{{zu}} = \dot{{H}}_{{ab}} = 0$ (geschlossenes System; die verdunstete Masse wird vernachlässigt, die mit dem Dampf abgeführte Energie steckt pauschal in $kA$), $\dot{{Q}}_{{zu}} = 0$ (der gesamte Austausch mit der Umgebung steckt in $\dot{{Q}}_{{ab}}$) und $\dot{{Q}}_{{KV}} = 0$ (keine Wärmequelle). Mit $dU = m\,c_v\,dT = m\,c_p\,dT$ (inkompressibel, $V = \mathrm{{const.}}$) und $\dot{{Q}}_{{ab}} = kA\,(T - T_u)$ ergibt sich die globale instationäre Energiebilanz:

$$m\,c_p\,\frac{{dT}}{{dt}} = -kA\,(T - T_u)$$

Trennung der Variablen und Integration von $t = 0\,\mathrm{{s}}$ ($T = T_0$) bis $t$:

$$\int_{{T_0}}^{{T}} \frac{{dT}}{{T - T_u}} = -\frac{{kA}}{{m\,c_p}} \int_0^{{t}} dt \quad\Rightarrow\quad \ln\frac{{T - T_u}}{{T_0 - T_u}} = -\frac{{kA}}{{m\,c_p}}\,t$$

Umstellen nach $T$:

$$T(t) = T_u + (T_0 - T_u)\cdot \exp\left(-\frac{{kA}}{{m\,c_p}}\,t\right)$$

Für Tasse 1 gilt $m\,c_p = m_K c_{{p,K}} + m_M c_{{p,M}}$, für Tasse 2 bis zum Zugießen $m\,c_p = m_K c_{{p,K}}$. Da nur Temperaturdifferenzen vorkommen, darf man auch mit $\vartheta$ in °C rechnen.

**c)** Lösung aus b) für den Kaffee ohne Milch nach $kA$ umstellen und die Messung in Tasse 2 einsetzen:

$$kA = -\frac{{m_K c_{{p,K}}}}{{t}}\,\ln\frac{{T_K(t) - T_u}}{{T_{{K,0}} - T_u}} =-\frac{{{de(CK,1)}{U('J/K')}}}{{{de(P['t_mess'],0)}{U('s')}}}\,\ln\frac{{{de(P['th_mess']-P['th_U'],0)}{U('K')}}}{{{de(P['th_K0']-P['th_U'],0)}{U('K')}}} = {de(r['kA'],4)}{U('W/K')}$$

Annahme für Tasse 1: $kA$ ist mit und ohne Milch gleich. Das ist plausibel, weil es dieselbe Tasse mit derselben freien Oberfläche ist, über die Strahlung und Verdunstung laufen (dafür genügt eine qualitative Begründung; die folgenden Zahlen sind für die Besprechung). Mit Milch steht der Inhalt aber höher (bei {dt(D_BECHER*100,0)} cm Innendurchmesser {dt(HM*100,1)} statt {dt(H0*100,1)} cm), die wärmeabgebende Fläche wächst um {dt((AM/A0-1)*100,1)} %; $kA$ ist in Tasse 1 also eher um 3 bis 5 % größer. Dann sinkt der Unterschied aus d) auf {dt(DT_KA103)} bis {dt(DT_KA105)} K; umkehren würde ihn erst ein um {dt((KIPP_KA-1)*100,0)} % größeres $kA$ (mit Becher {dt((KIPP_KA_B-1)*100,0)} %). Die Messung kalibriert das Modell; ob $kA$ auch für den Milchkaffee gilt, zeigt erst eine eigene Messung.

Zur Einordnung: Zeitkonstante $\tau = m\,c_p/kA$ ohne Milch ${de(r['tau_K']/60,1)}{U('min')}$, mit Milch ${de(r['tau_G']/60,1)}{U('min')}$; nach der Zeit $\tau$ hat der schwarze Kaffee noch {dt(TH_TAU,1)} °C. Das passt zu Messungen an einem offenen, nicht umgerührten Keramikbecher ($\tau \approx 41\,\mathrm{{min}}$ aus der Steigung in Abb. 6 bei Ferreira 2025). Bezogen auf rund {dt(A0*1e4,0)} cm² Oberfläche ist $kA/A \approx {de(r['kA']/A0,0)}{U('W/(m^2\\,K)')}$: freie Konvektion, Strahlung und Verdunstung zusammen.

**d)** Tasse 1: Anfangsbedingung $T(0\,\mathrm{{s}}) = T_{{1,0}}$ und $m\,c_p = m_K c_{{p,K}} + m_M c_{{p,M}}$:

$$T_1 = T_u + (T_{{1,0}} - T_u)\cdot \exp\left(-\frac{{kA\,t}}{{m_K c_{{p,K}} + m_M c_{{p,M}}}}\right)$$

$$T_1 = {de(r['T_U'])}{U('K')} + {de(T10-r['T_U'])}{U('K')} \cdot {de(r['e_G'],4)} = {de(T1)}{U('K')} = {de(T1-K)}{U('°C')}$$

Tasse 2: erst Abkühlen mit $m\,c_p = m_K c_{{p,K}}$, dann Mischen wie in a):

$$T_K(60\,\mathrm{{min}}) = T_u + (T_{{K,0}} - T_u)\cdot \exp\left(-\frac{{kA\,t}}{{m_K c_{{p,K}}}}\right)$$

$$T_K(60\,\mathrm{{min}}) = {de(r['T_U'])}{U('K')} + {de(r['T_K0']-r['T_U'])}{U('K')} \cdot {de(r['e_K'],4)} = {de(T2K)}{U('K')} = {de(T2K-K)}{U('°C')}$$

$$T_2 = \frac{{m_K c_{{p,K}}\,T_K(60\,\mathrm{{min}}) + m_M c_{{p,M}}\,T_M}}{{m_K c_{{p,K}} + m_M c_{{p,M}}}}$$

$$T_2 = \frac{{{de(CK,1)}{U('J/K')} \cdot {de(T2K)}{U('K')} + {de(CM,1)}{U('J/K')} \cdot {de(r['T_M'])}{U('K')}}}{{{de(CG,1)}{U('J/K')}}} = {de(T2)}{U('K')} = {de(T2-K)}{U('°C')}$$

Tasse 1 ist wärmer, Tasse 2 um ${de(r['dT'])}{U('K')}$ kühler.

Zur Einordnung: Liegt die Messung 1 K daneben ({dt(Q66['th_mess'],0)} oder {dt(Q68['th_mess'],0)} °C), ändert sich $kA$ um rund {dt((Q66['kA']/r['kA']-1)*100,0)} % und beide Endtemperaturen um rund 1,6 K, der Unterschied aber nur um 0,03 K ({dt(Q66['dT'])} bzw. {dt(Q68['dT'])} K). Die Aussage „Tasse 1 ist wärmer“ hängt also nicht an der genauen Messung, die Absolutwerte schon.

**e)** Die abgegebene Wärme folgt aus der Energiebilanz über die Abkühlzeit:

$$Q_1 = (m_K c_{{p,K}} + m_M c_{{p,M}})\,(T_{{1,0}} - T_1) = {de(CG,1)}{U('J/K')} \cdot {de(T10-T1)}{U('K')} = {de(r['Q1']/1e3)}{U('kJ')}$$

$$Q_2 = m_K c_{{p,K}}\,(T_{{K,0}} - T_K(60\,\mathrm{{min}})) = {de(CK,1)}{U('J/K')} \cdot {de(r['T_K0']-T2K)}{U('K')} = {de(r['Q2']/1e3)}{U('kJ')}$$

Kontrolle: Beide Tassen enthalten am Ende dieselbe Menge Kaffee und Milch. Der Temperaturunterschied folgt allein aus der Mehrabgabe: $(Q_2 - Q_1)/(m_K c_{{p,K}} + m_M c_{{p,M}}) = {de((r['Q2']-r['Q1'])/CG)}{U('K')}$, wie in d).

Erklärung: Der Wärmestrom $\dot{{Q}}_{{ab}} = kA\,(T - T_u)$ ist umso größer, je heißer der Tasseninhalt ist. Der Kaffee in Tasse 2 startet ohne Milch heißer (Wärmestrom am Anfang {dt(r['Qdot2_0'],1)} W gegenüber {dt(r['Qdot1_0'],1)} W in Tasse 1) und bleibt es bis etwa {dt(r['t_schnitt']/60,0)} min (Abb. L2). Er gibt deshalb mehr Wärme ab. Wärme ist eine Prozessgröße: Wie viel abgegeben wird, entscheidet der Ablauf. Weil keine Arbeit verrichtet wird, ist die abgegebene Wärme gleich der Abnahme der inneren Energie von Kaffee und Milch. Am Anfang ist diese Energie in beiden Fällen gleich; der unterschiedliche Temperaturverlauf führt aber zu verschiedenen Endtemperaturen und damit zu verschiedener Wärmeabgabe. Der Denkfehler des Mitbewohners: Erhalten bleibt die Energie von Tasseninhalt und Umgebung zusammen, nicht die des Tasseninhalts. Wer seinen Kaffee später möglichst warm trinken will, gibt die Milch sofort hinein.

![](grafik/AbbL2_Temperaturverlauf.png){{width=78%}}

**Abb. L2:** Temperaturverlauf beider Tassen (Ausschnitt: Schnittpunkt bei etwa {dt(r['t_schnitt']/60,0)} min)

**f)** Rechnung wie in a) und d), nur mit $T_{{M,h}} = {de(T_S)}{U('K')}$ statt $T_M$:

$$T_{{1,0}} = \frac{{m_K c_{{p,K}}\,T_{{K,0}} + m_M c_{{p,M}}\,T_{{M,h}}}}{{m_K c_{{p,K}} + m_M c_{{p,M}}}} = {de(T10S)}{U('K')}$$

$$T_1 = T_u + (T_{{1,0}} - T_u)\cdot {de(r['e_G'],4)} = {de(MILCH60['T1'])}{U('K')} = {de(MILCH60['T1']-K)}{U('°C')}$$

$$T_2 = \frac{{m_K c_{{p,K}}\,T_K(60\,\mathrm{{min}}) + m_M c_{{p,M}}\,T_{{M,h}}}}{{m_K c_{{p,K}} + m_M c_{{p,M}}}} = {de(MILCH60['T2'])}{U('K')} = {de(MILCH60['T2']-K)}{U('°C')}$$

Jetzt ist Tasse 2 um {dt(-MILCH60['dT'])} K wärmer. Erklärung: Die Milch wirkt zweimal. Während der 60 Minuten macht sie Tasse 1 träger (mehr Wärmekapazität), das spricht immer für „sofort“. Beim späten Zugießen bringt sie ihre eigene Temperatur mit: Kalte Milch kühlt Tasse 2 dann stärker ab, warme Milch wärmt sie stärker auf. Bei 60 °C überwiegt der zweite Effekt.

Zur Erklärung (die Zerlegung ist nicht verlangt): Zieht man die Ergebnisse aus d) voneinander ab, ergeben sich die beiden Anteile

$$\vartheta_1 - \vartheta_2 = \underbrace{{\frac{{m_K c_{{p,K}}\,(\vartheta_{{K,0}} - \vartheta_u)\,(e_G - e_K)}}{{m_K c_{{p,K}} + m_M c_{{p,M}}}}}}_{{\text{{Kaffee-Effekt}}}} + \underbrace{{\frac{{m_M c_{{p,M}}\,(\vartheta_M - \vartheta_u)\,(e_G - 1)}}{{m_K c_{{p,K}} + m_M c_{{p,M}}}}}}_{{\text{{Milch-Effekt}}}}$$

mit $e_G = \exp(-kA\,t/(m_K c_{{p,K}} + m_M c_{{p,M}})) = {de(r['e_G'],4)}$ und $e_K = \exp(-kA\,t/(m_K c_{{p,K}})) = {de(r['e_K'],4)}$. Kaffee-Effekt {dt(EFF1)} K; Milch-Effekt {dt(EFF2_5)} K für kalte Milch (für „sofort“), {dt(EFF2_60)} K für erwärmte Milch (für „später“).

**g)** Der Bilanzraum umfasst jetzt Inhalt und Becher (Abb. L1): Kaffee und vorgewärmter Becher bilden eine gemeinsame Speicherkapazität, auch beim Zugießen der Milch. Das ist gerechtfertigt, weil die Widerstände innen (Kaffee zur Wand) und in der dünnen Keramikwand klein sind gegenüber dem Widerstand außen zur Luft. $C_B = m_B c_B = {de(P['m_B'],3)}{U('kg')} \cdot {de(P['c_B'],0)}{U('J/(kg\\,K)')} = {de(CB,1)}{U('J/K')}$ ({dt(CB/CK*100,1)} % von $m_K c_{{p,K}}$). Messung in Tasse 2 wie in c), jetzt mit $m_K c_{{p,K}} + C_B$:

$$kA = -\frac{{m_K c_{{p,K}} + C_B}}{{t}}\,\ln\frac{{T_K(t) - T_u}}{{T_{{K,0}} - T_u}} = -\frac{{{de(CKB,1)}{U('J/K')}}}{{{de(P['t_mess'],0)}{U('s')}}}\,\ln\frac{{{de(P['th_mess']-P['th_U'],0)}{U('K')}}}{{{de(P['th_K0']-P['th_U'],0)}{U('K')}}} = {de(BECHER['kA'],4)}{U('W/K')}$$

$kA$ ist ein an die Messung angepasster Modellparameter: In c) musste es auch die Wärme erklären, die der Becher abgegeben hat; mit Becher im Bilanzraum ist es um {dt((KA_VERH-1)*100,0)} % größer. Die Zeitkonstante $\tau = (m_K c_{{p,K}} + C_B)/kA = {de(TAU_B/60,1)}{U('min')}$ bleibt gleich.

Tasse 1: Mischen mit Becher (er hat vorher die Kaffeetemperatur), dann Abkühlen:

$$T_{{1,0}} = \frac{{(m_K c_{{p,K}} + C_B)\,T_{{K,0}} + m_M c_{{p,M}}\,T_M}}{{m_K c_{{p,K}} + C_B + m_M c_{{p,M}}}} = {de(T10B)}{U('K')}$$

$$T_1 = T_u + (T_{{1,0}} - T_u)\cdot \exp\left(-\frac{{kA\,t}}{{m_K c_{{p,K}} + C_B + m_M c_{{p,M}}}}\right)$$

$$T_1 = {de(r['T_U'])}{U('K')} + {de(T10B-r['T_U'])}{U('K')} \cdot {de(eB,4)} = {de(BECHER['T1'])}{U('K')} = {de(BECHER['T1']-K)}{U('°C')}$$

Dass $\vartheta_1$ fast gleich bleibt ({dt(BECHER['T1']-K)} statt {dt(T1-K)} °C), liegt an zwei Effekten, die sich fast aufheben: Die Mischtemperatur steigt ({dt(T10B-K)} statt {dt(T10-K)} °C), die Zeitkonstante von Tasse 1 sinkt ({dt(TAU1_B/60,1)} statt {dt(r['tau_G']/60,1)} min).

Tasse 2: Der schwarze Kaffee kühlt mit derselben Zeitkonstante ab wie in der Messung, also wie in d) auf $T_K(60\,\mathrm{{min}}) = {de(T2K)}{U('K')}$. Dann Mischen mit Becher:

$$T_2 = \frac{{(m_K c_{{p,K}} + C_B)\,T_K(60\,\mathrm{{min}}) + m_M c_{{p,M}}\,T_M}}{{m_K c_{{p,K}} + C_B + m_M c_{{p,M}}}} = {de(BECHER['T2'])}{U('K')} = {de(BECHER['T2']-K)}{U('°C')}$$

Die Aussage aus d) gilt weiter, der Unterschied sinkt aber von {dt(r['dT'])} K auf {dt(BECHER['dT'])} K. Beide Anteile aus der Zerlegung in f) werden kleiner: Die Milch erhöht die Wärmekapazität nur noch um {dt(CM/CKB*100,0)} % statt {dt(CM/CK*100,0)} % (Kaffee-Effekt {dt(EFF1_B)} statt {dt(EFF1)} K), und der Becher gibt beim Mischen Wärme an die kalte Milch ab und dämpft den Mischsprung (Milch-Effekt {dt(EFF2_B)} statt {dt(EFF2_5)} K).

"""

HINWEISE = rf"""::: seitenumbruch
:::

**[Hinweise für die Tutoriumsleitung]{{.underline}}**

*Ablauf im Tutorium:* Die Sitzung hat drei Ebenen: zuerst der Versuch (er startet zu Beginn), dann die Rechnung, am Ende ein Simulationstool, mit dem die Studierenden die Parameter des Kaffee-Vorgangs selbst verändern (Milchtemperatur, Zeitpunkt des Zugießens, $kA$, Becher). Kern sind Frage 1, a bis f und der Versuch; g ist Vertiefung; die Zusatzfrage (unten) steht nicht auf dem Blatt. Frage 1 vor dem Austeilen stellen: Vermutung mit Begründung notieren lassen, Handzeichen (Tasse 1, Tasse 2, gleich warm), Verteilung an die Tafel und am Ende wieder zeigen; die Ergebniszeilen späterer Teile verraten sonst die Antwort. Zeitplan als Schätzung, beim ersten Einsatz messen:

| Minute | Ablauf |
|:--------------|:------------------------------------------------------------------------------------------|
| 0 bis 5 | Ausgangssituation, Frage 1 (Vermutung, Handzeichen); TL startet mit zwei Freiwilligen den Versuch ($t = 0$ etwa in Minute 5), dann Blatt austeilen |
| 5 bis 45 | a bis e; b nach etwa 8 min Einzelarbeit gemeinsam an der Tafel (Bilanz vereinfachen, Trennung der Variablen), dann c bis e allein; etwa Minute 15 Messung bei $t = 10\,\mathrm{{min}}$; nach d) Vorhersage für $t = {T_V}\,\mathrm{{min}}$ an der Tafel. Haltepunkt: Sind um Minute 40 viele noch nicht bei e), e) gemeinsam besprechen und f zuerst als Vorhersage mit Handzeichen |
| 45 bis 52 | Messung bei $t = {T_V}\,\mathrm{{min}}$, Vergleich mit der Vorhersage, Auflösung von Frage 1 |
| 52 bis 65 | f mit Vorhersage und Erklärung |
| 65 bis 75 | g für Schnelle, sonst Besprechung; Zusatzfrage für ganz Schnelle |
| 75 bis 90 | Simulation (10 bis 15 min, Fragen unten): Die Studierenden verändern die Parameter selbst, tragen ihre Messwerte ein und prüfen ihre Erklärungen aus d) bis g); zum Schluss kurze Zusammenfassung. Frage 3 der Sammlung zu Tutorium 5 (Biot) als Hausaufgabe |

- *Typische Fehler:* Mischtemperatur nach dem Volumen statt nach $m\,c_p$ gewichtet; in Tasse 1 nur mit $m_K c_{{p,K}}$ gerechnet; in Tasse 2 schon während der 60 Minuten mit $m_K c_{{p,K}} + m_M c_{{p,M}}$ gerechnet; Zeit in Minuten eingesetzt ($kA = {de(-CK/10*r['ln_mess'],2)}$ statt ${de(r['kA'],4)}{U('W/K')}$); Vorzeichen in der Bilanz vergessen (die Temperatur stiege); $Q_2$ mit Kaffee und Milch gerechnet ({dt(CG*(r['T_K0']-T2K)/1e3)} statt {dt(r['Q2']/1e3)} kJ); in g) das alte $kA$ weiterverwendet (dann {dt(becher(kA_neu=False)['T1']-K,1)} und {dt(becher(kA_neu=False)['T2']-K,1)} °C: Aussage gleich, aber nicht mehr passend zur Messung) oder den Becher beim Zugießen nicht mitgemischt ({dt(FEHLER_F1-K)} und {dt(T2-K)} °C); in der Zusatzfrage (2) nur mit dem Kipppunkt argumentiert ({dt(P['th_U'],0)} °C < {dt(r['th_M_gleich'],0)} °C), obwohl Tasse 1 weiter die kalte Milch bekommt.
- *Fehlvorstellungen:* „Energieerhaltung, also egal“: Erhalten bleibt die Energie von Kaffee, Milch und Umgebung zusammen, nicht die des Tasseninhalts (Teil e). „Erwärmte Milch ist kälter als der Kaffee, wirkt also wie kalte Milch“: Entscheidend ist nicht der Vergleich mit dem Kaffee, sondern ob die Milch wärmer als der Kipppunkt aus der Zusatzfrage (1) ist. „Milchkaffee ist heller und strahlt deshalb weniger ab“: Im Infraroten strahlen schwarzer Kaffee und Milchkaffee gleich; die sichtbare Farbe spielt keine Rolle.
- *Zu e:* Hilfe bei Bedarf: „Womit starten beide Tassen, womit enden sie? Stellen Sie die Energiebilanz um Kaffee und Milch zusammen auf.“
- *Zu f:* Hilfe bei Bedarf: „Was bewirkt die Milch während der 60 Minuten, und was beim Zugießen?“ Die späte Portion muss frisch erwärmt sein; unter {dt(G_SPAET_MIN,1)} °C wäre Tasse 2 nicht mehr wärmer. Ein echter Cappuccino verhält sich anders: Der Schaum mischt sich nicht und liegt als dämmende Schicht oben. Schon {dt((1-G_SCHAUM)*100,1)} % weniger $kA$ in Tasse 1 gleichen den Vorsprung von Tasse 2 aus, bei 10 % weniger ist Tasse 1 um {dt(G_SCHAUM10)} K wärmer.
- *Was die Rechnung weglässt:* (1) Die Verdunstung wächst mit dem Dampfdruck, also viel stärker als linear mit $T - T_u$; bei 80 °C trägt sie rund die Hälfte der Wärmeabgabe (Condoret 2007, Tab. 2), bei 35 °C deutlich weniger. Mit $kA$ aus der 10-Minuten-Messung liegen die berechneten Temperaturen nach 60 min deshalb einige Kelvin zu tief (Abschätzung mit einem Verdunstungsmodell: 38 bis 40 statt 34 °C), der Unterschied wächst auf rund 4,5 K. Das Potenzgesetz $\dot{{Q}}_{{ab}} \propto (T - T_u)^{{4/3}}$ (freie Konvektion), angepasst an dieselbe Messung, bildet das nur teilweise ab: $\vartheta_1 = {de(nl1-K)}{U('°C')}$ und $\vartheta_2 = {de(nl2-K)}{U('°C')}$, also {dt(nl1-nl2)} K. (2) Mit Milch ist die Tasse voller, $kA$ steigt um einige Prozent; je 5 % sinkt der Unterschied um rund {dt(r['dT']-DT_KA105,1)} K. Beide Effekte heben sich etwa auf.
- *Zum Weiterdenken:* Hätte die Milch in beiden Tassen Raumtemperatur, wäre der Unterschied mit {dt(MILCH20['dT'],1)} K kleiner, aber vorhanden. Der schwarze Kaffee ist bis etwa {dt(r['t_schnitt']/60,0)} min heißer als das Gemisch in Tasse 1 (Abb. L2) und verliert deshalb mehr Wärme; am größten ist der Unterschied, wenn die Milch nach etwa {T_MAX} min kommt ({dt(DT_MAX)} K). Wie viel Kaffee verdunstet? Geht die Hälfte von $Q_2$ in die Verdunstung, sind es höchstens rund {dt(M_VERD*1e3,0)} g ({dt(M_VERD/mK*100,0)} %); die Annahme ist vertretbar.
- *Impulse:* Zu c): „Wie warm ist der schwarze Kaffee nach der Zeit $\tau$, und passt das zu Ihrer Erfahrung?“ ({dt(TH_TAU,1)} °C). Zu e) (Tafelimpuls statt Auftrag): „Skizzieren Sie den Verlauf $\vartheta(t)$ beider Tassen in einem Diagramm. Welche Tasse ist wann wärmer?“ Danach Abb. L2 zeigen. Umgekehrtes Ziel: Wer den Kaffee möglichst bald bei Trinktemperatur haben will, gießt die kalte Milch spät dazu, aus demselben Grund. Technisch ist die Reihenfolge von Mischen und Kühlen eine Frage der Prozessführung: Soll ein heißer Ansatz schnell abkühlen, gibt man eine kalte Komponente spät zu. Quellterm als Impuls: Ein Tassenwärmer soll den Kaffee bei 60 °C halten; nötig ist $P = kA\,(\vartheta - \vartheta_u)$, also {dt(P60_C,1)} W mit $kA$ aus c) und {dt(P60_F,1)} W mit $kA$ aus g). Wer den Becher bei der Bestimmung von $kA$ vernachlässigt, unterschätzt die Leistung um {dt((1-P60_C/P60_F)*100,0)} %.
- *Fachlicher Beleg* für die Hauptaussage: Rees & Viney (1988, Am. J. Phys. 56, 434); im Netz kursieren auch Fehlschlüsse („der Zeitpunkt ist egal“), Teil e widerlegt sie.
- *Versuch, Ablauf:* Material: drei gleiche Becher, heißes Wasser oder Kaffee aus der Thermoskanne, Milch aus der Kühltasche, ein kleines Glas, Messbecher, ein Einstichthermometer für alle Messungen, Löffel, Uhr. $t = 0$: Raumtemperatur messen; Becher vorwärmen, je 200 ml einfüllen, Start- und Milchtemperatur messen; Becher 1 bekommt die Milch sofort, nach dem Umrühren Mischtemperatur messen (Vergleich mit a). Die Milch für Becher 2 bleibt in der Kühltasche, die für Becher 3 steht im Glas mit Abstand zu den Bechern (sonst erwärmt sie auch der heiße Becher, Zusatzfrage (2)). $t = 10\,\mathrm{{min}}$: Becher 2 und 3 messen; der Unterschied zeigt die Streuung gleicher Becher. Vorhersage nach d) mit dem Mittelwert, für Becher 3 mit Raumtemperatur als obere Grenze; Abkürzung für den schwarzen Kaffee: $\vartheta_K(t) = \vartheta_u + (\vartheta_{{K,0}} - \vartheta_u)\,r^{{t/10\,\mathrm{{min}}}}$ mit $r$ aus der 10-Minuten-Messung. $t = {T_V}\,\mathrm{{min}}$: Milchtemperaturen messen, Milch zugießen, alle drei Becher umrühren und in fester Reihenfolge zügig messen. Messregel: vor jeder Messung umrühren, Thermometer mittig und halb tief, warten, bis die Anzeige steht, Uhrzeit notieren (bei 40 °C kühlt ein Becher um rund {dt(RATE40,1)} K je Minute ab); alle Becher offen nebeneinander auf derselben Unterlage, ohne Zugluft. Ein Thermometer für alle Messungen hebt seinen festen Fehler im Vergleich auf. Heißes Wasser verhält sich wie Kaffee; Verbrühungsgefahr beachten.
- *Versuch, Erwartung:* Mit vorgewärmten Bechern sind nach {T_V} Minuten zwischen Becher 1 und 2 rund 2 bis 3 K zu erwarten (Modell mit Becher {dt(V40['dT'])} K; das Modell aus d) ohne Becher sagt {dt(V40_D['dT'])} K voraus, der Unterschied ist ein Anlass für g), mit einem Thermometer für alle Messungen gut messbar. Becher 3 liegt dazwischen: rund 1 bis 2 K kühler als Becher 1 und oft nur 0,5 bis 1,5 K wärmer als Becher 2, kaum mehr als die Streuung zwischen zwei Bechern. Die Werte sind Modellwerte: Ist $kA$ beim volleren Milchkaffee nur 3 bis 5 % größer, sinkt der Unterschied zwischen Becher 1 und 2 im Modell auf {dt(V40_105['dT'],1)} bis {dt(V40_103['dT'],1)} K; die Verdunstung hebt ihn wieder etwas an. Die gemessenen Temperaturen liegen meist einige Kelvin über der Vorhersage, weil $kA$ mit sinkender Temperatur kleiner wird (Verdunstung). Das ist die Grenze des Modells, kein Messfehler.
- *Simulation (dritte Ebene):* Datei Kaffee_Simulation.html, vorab an die Studierenden verteilen; sie läuft ohne Installation und ohne Internet im Browser auf Handy und Laptop und rechnet mit demselben Modell wie diese Lösung. Die Messwerte aus dem Versuch werden dort eingetragen und erscheinen im Diagramm. Die Fragen sagen selbst, wann die Standardwerte zu laden sind. Fragen zum Ausprobieren mit Erwartung: (1) *Zeitpunkt:* Der Unterschied ist ungefähr bei Zugabe nach {T_MAX} min am größten ({dt(DT_MAX)} K; wegen der Rundung zeigt das Werkzeug denselben Wert von etwa 53 bis 59 min), genau am Schnittpunkt: Solange der schwarze Kaffee wärmer ist als Tasse 1, gibt er mehr Wärme ab, und der Unterschied wächst. Nach dem Schnitt ist der schwarze Kaffee vor der Zugabe kühler als Tasse 1 und gibt weniger Wärme ab, der Unterschied wird kleiner. Er geht aber nicht gegen null: Die beiden Abkühlkurven nähern sich vor der Zugabe der Raumtemperatur, und die frische kalte Milch senkt Tasse 2 beim Mischen erneut (bei sehr später Zugabe {dt(P['th_U'],0)} °C gegenüber {dt(SIM_SPAET2)} °C, also {dt(P['th_U']-SIM_SPAET2)} K). (2) *Milchtemperatur:* ungefähr gleich warm bei {dt(r['th_M_gleich'],1)} °C nach 60 min (Zusatzfrage (1)); der Regler rastet in Schritten von 0,5 K. Der Wert hängt vom Zeitpunkt ab, {dt(SIM_KIPP[30],1)} °C nach 30 min und {dt(SIM_KIPP[90],1)} °C nach 90 min. (3) *Becher* (nach Laden der Standardwerte): Der Unterschied sinkt von {dt(r['dT'])} auf {dt(SIM_B['dT'])} K; die abgegebene Wärme steigt ({dt(SIM_Q1B/1e3)} und {dt(SIM_Q2B/1e3)} kJ statt {dt(r['Q1']/1e3)} und {dt(r['Q2']/1e3)} kJ), weil der Becher mit abkühlt; Tasse 1 bleibt wärmer. (4) *Versuch* (braucht die Messwerte aus dem Versuch): Die Messpunkte liegen meist einige Kelvin über den Kurven, weil $kA$ mit sinkender Temperatur kleiner wird (Verdunstung); der Unterschied zwischen Becher 1 und 2 passt meist besser als die Einzelwerte.
- *Probelauf:* Den Versuch einmal vorab mit den Tutoriumsbechern und dem Thermometer machen (Becher wiegen, Zeitkonstante, Streuung und Wiederholgenauigkeit ansehen, dazu eine Abkühlreihe mit fertigem Milchkaffee, um gleiches $kA$ zu prüfen) und die Messreihe als Reserve bereithalten. Wer Zeit hat, misst Becher 2 zusätzlich nach 5, 20 und 30 min und trägt $\ln(\vartheta - \vartheta_u)$ über $t$ auf: Die Punkte liegen nicht ganz auf einer Geraden (Verdunstung).

*Zusatzfrage für Schnelle* (steht nicht auf dem Blatt; an der Tafel oder mündlich stellen): (1) Bei welcher Milchtemperatur sind beide Tassen nach 60 Minuten gleich warm (ohne Becher)? (2) Die Milch für Tasse 2 steht ab $t = 0$ neben der Tasse und wird nur von der Raumluft erwärmt. Kann Tasse 2 so wärmer werden als Tasse 1? Schätzen Sie ab, wie viel Wärme die Milch höchstens aufnehmen kann, und vergleichen Sie mit $Q_2 - Q_1$ aus e). Kontrollwerte: $\vartheta_M = {de(r['th_M_gleich'],1)}{U('°C')}$, $\quad Q_M \le {de(QM_RAUS/1e3)}{U('kJ')}$.

Zu (1): Beide Anteile aus der Zerlegung in f) heben sich auf, wenn $\vartheta_1 = \vartheta_2$:

$$\vartheta_M = \vartheta_u + \frac{{m_K c_{{p,K}}\,(\vartheta_{{K,0}} - \vartheta_u)\,(e_G - e_K)}}{{m_M c_{{p,M}}\,(1 - e_G)}} = {de(P['th_U'],0)}{U('°C')} + {de(r['th_M_gleich']-P['th_U'],1)}{U('K')} = {de(r['th_M_gleich'],1)}{U('°C')}$$

Zweiter Weg: $\vartheta_1$ und $\vartheta_2$ hängen linear von der Milchtemperatur ab. Der Unterschied ist {dt(r['dT'])} K bei {dt(P['th_M'],0)} °C und {dt(MILCH60['dT'])} K bei {dt(P['th_Mh'],0)} °C, null also bei {dt(P['th_M'],0)} °C + {dt(P['th_Mh']-P['th_M'],0)} K · {dt(r['dT'])}/{dt(r['dT']-MILCH60['dT'])} ≈ {dt(ZERL_LIN,1)} °C (mit ungerundeten Werten).

Erst Milch über etwa {dt(r['th_M_gleich'],0)} °C dreht das Ergebnis um. Der Wert gilt im Modell mit gleichem $kA$ und ist empfindlich: Ist $kA$ mit Milch 5 % größer, liegt er bei etwa {dt(KIPP_105,0)} °C, bei 5 % kleinerem $kA$ bei {dt(KIPP_095,0)} °C; mit überlinearer Wärmeabgabe (Exponent 4/3) bei rund {dt(KIPP_43,0)} °C.

Zu (2): Nein. Die Milch wird nur von der Raumluft erwärmt, also höchstens auf Raumtemperatur, und nimmt dabei höchstens

$$Q_M = m_M c_{{p,M}}\,(\vartheta_u - \vartheta_M) = {de(CM,1)}{U('J/K')} \cdot {de(P['th_U']-P['th_M'],0)}{U('K')} = {de(QM_RAUS/1e3)}{U('kJ')}$$

auf. Tasse 2 hat nach e) aber $Q_2 - Q_1 = {de((r['Q2']-r['Q1'])/1e3)}{U('kJ')}$ mehr abgegeben als Tasse 1. Selbst im günstigsten Fall bleibt Tasse 2 deshalb um mindestens

$$\frac{{(Q_2 - Q_1) - Q_M}}{{m_K c_{{p,K}} + m_M c_{{p,M}}}} = \frac{{{de((r['Q2']-r['Q1'])/1e3)}{U('kJ')} - {de(QM_RAUS/1e3)}{U('kJ')}}}{{{de(CG,1)}{U('J/K')}}} \approx {de(DMIN_RAUS)}{U('K')}$$

kühler (mit ungerundeten Werten gerechnet; mit Milch von 20 °C: $\vartheta_2 = {de(T2_RAUS-K)}{U('°C')}$ gegenüber $\vartheta_1 = {de(T1-K)}{U('°C')}$). Der Kipppunkt aus (1) entscheidet die Frage nicht allein, weil er für gleich warme Milch in beiden Tassen gilt. Die Schranke gilt nur ohne weitere Wärmequelle: Käme Wärme vom heißen Becher dazu, würde schon eine späte Portion von {dt(H2_NUR_SPAET,1)} °C Tasse 2 auf die Temperatur von Tasse 1 bringen.

"""

QUELLEN = rf"""```{{=latex}}
\needspace{{7\baselineskip}}
```

**[Quellen der Arbeitswerte]{{.underline}}**

- Kaffee: gebrüht bei etwa 93 °C, in der Glaskanne einer Haushaltsmaschine bis etwa 11 K kälter, beim Eingießen 2 bis 5 K kälter (Abraham & Diller 2019, J. Food Sci. 84(8), 2011 bis 2014, Tab. 1); 80 °C liegen in diesem Bereich und im Servierbereich 71 bis 85 °C (Brown & Diller 2008, Burns 34(5), 648 bis 654, doi:10.1016/j.burns.2007.09.012). Stoffwerte wie Wasser (SCA, Gehalt an gelösten Stoffen 1,15 bis 1,35 %).
- Milch: Kühlschrank höchstens 7 °C, besser unter 5 °C (Bundesinstitut für Risikobewertung, 2023); im Mittel 31 g Milch je Tasse (FSANZ 2011); Dichte 1027 bis 1033 kg/m³ (Goff, Dairy Science and Technology); $c_p$ wie in Tutorium 8 (Quelle dort).
- Abkühlung: offener, nicht umgerührter Keramikbecher, $\tau \approx 41\,\mathrm{{min}}$ aus der Steigung 0,0241 1/min in Abb. 6 (Ferreira 2025, Forced convection and the coffee cup, Phys. Educ. 60, 035001, doi:10.1088/1361-6552/adb6ea); Haushaltsbecher kühlen je nach Form und Füllung auch schneller ab ($\tau \approx 20$ bis 40 min), die Aussage hängt davon kaum ab. Verdunstung bei 79 °C 12,0 von 22,7 W (Condoret 2007, Teaching transport phenomena around a cup of coffee, Chem. Eng. Educ. 41, 137, Tab. 2; nicht frei einsehbar); als zweiter Beleg senkt ein Deckel das scheinbare $kA$ um 44 % (Ferreira 2025, Abb. 6).
- Erwärmte Milch 55 bis 65 °C (Thermoplan, Coffee knowledge: milk); Keramikbecher 300 g mit 0,85 kJ/(kg·K) als Arbeitswert (Schätzung).
- Hauptaussage: Rees & Viney (1988), On cooling tea and coffee, Am. J. Phys. 56(5), 434 bis 437, doi:10.1119/1.15572.
- Rechenskript: nachrechnung_kaffee.py mit kaffee_modell.py.

"""


def schreibe(name, text):
    with open(os.path.join(HIER, name), "w", encoding="utf-8") as f:
        f.write(text)


# Einleitungssatz und folgende Formeln in einen Absatz: kein Seitenumbruch dazwischen, keine Leerzeile vor der zweiten Formel
LOESUNG = re.sub(r"([^\n])\n\n(\$\$)", r"\1\n\2", LOESUNG)
HINWEISE = re.sub(r"([^\n])\n\n(\$\$)", r"\1\n\2", HINWEISE)
# Aufgabentext genau wie in der Aufgabensammlung (Ausgangssituation, Frage 1, Aufgabe 1, Versuch)
with open(SAMMLUNG_BLOCK, encoding="utf-8") as _f:
    BLOCK = _f.read()
BLOCK = re.sub(r"^## .*\n+", "", BLOCK, count=1).replace("<!-- T5_FRAGEN -->\n\n", "").replace("<!-- T5_FRAGEN -->", "")
# Einzelblatt: Versuch auf eigener Seite (Messblatt zum Kopieren, Ä5)
assert BLOCK.count("**[Versuch zu Aufgabe 1]") == 1
# Einzelblatt: Teil f mit Ergebniszeile nicht über den Seitenwechsel trennen (Abnahme 3)
BLOCK, _n = re.subn(r"(\n   \$Q_1 = [^\n]*\$)(\n)", r"\1`\\needspace{6\\baselineskip}`{=latex}\2", BLOCK, count=1)
assert _n == 1
BLOCK = BLOCK.replace("**[Versuch zu Aufgabe 1]", "::: seitenumbruch\n:::\n\n**[Versuch zu Aufgabe 1]")
md_aufgabe = KOPF + BLOCK
KOPF_L = KOPF.replace("(instationär global)]", "(instationär global), Lösung]")
assert KOPF_L != KOPF
md_loesung = KOPF_L + BLOCK + "::: seitenumbruch\n:::\n\n" + LOESUNG + HINWEISE + QUELLEN
md_loesung_stud = KOPF_L + BLOCK + "::: seitenumbruch\n:::\n\n" + LOESUNG + QUELLEN       # für Studierende, ohne Hinweise
md_aufgabe, md_loesung, md_loesung_stud = aufrecht(md_aufgabe), aufrecht(md_loesung), aufrecht(md_loesung_stud)
schreibe("Kaffee_Aufgabe.md", md_aufgabe)
schreibe("Kaffee_Loesung.md", md_loesung)
schreibe("Kaffee_Loesung_Studierende.md", md_loesung_stud)

# Lösung: Kopfzeile rechts mit „Lösung“ (aus kopf.tex abgeleitet, damit beide gleich bleiben)
with open(os.path.join(B, "kopf.tex"), encoding="utf-8") as _f:
    _kopf = _f.read()
assert KOPF_RECHTS in _kopf
with open(os.path.join(B, "kopf_loesung.tex"), "w", encoding="utf-8") as _f:
    _f.write(_kopf.replace(KOPF_RECHTS, "Lösung, " + KOPF_RECHTS))
for name in ("Kaffee_Aufgabe", "Kaffee_Loesung", "Kaffee_Loesung_Studierende"):
    md = os.path.join(HIER, name + ".md")
    subprocess.run(["pandoc", md, "-o", os.path.join(HIER, name + ".pdf"), "--pdf-engine=xelatex",
                    "-H", os.path.join(B, "kopf_loesung.tex" if name.startswith("Kaffee_Loesung") else "kopf.tex"), "--lua-filter", os.path.join(B, "lehrstuhl.lua"),
                    "-V", "documentclass=article", "-V", "fontsize=11pt", "-V", "mainfont=Carlito",
                    "-V", "mathfont=Latin Modern Math", "--resource-path", HIER + ":" + os.path.join(os.path.dirname(HIER), "sammlung")], check=True)
    subprocess.run(["pandoc", md, "-o", os.path.join(HIER, name + ".docx"),
                    "--reference-doc", os.path.join(B, "referenz_lehrstuhl.docx"),
                    "--lua-filter", os.path.join(B, "lehrstuhl.lua"), "--resource-path", HIER + ":" + os.path.join(os.path.dirname(HIER), "sammlung")], check=True)


def kaffee_breiten(t):
    """Tabelle der gegebenen Größen (Kaffee-Aufgabe): Spalten 3,9 / 4,1 / 3,9 / 4,1 cm (Ä22)."""
    if "Messung in Tasse 2" not in t:
        return t
    t = re.sub(r'<w:tblW w:type="pct" w:w="\d+" />', '<w:tblW w:type="dxa" w:w="9070" />', t, count=1)
    # feste Breiten und Zellränder von 4 pt wie im PDF (\tabcolsep), sonst bricht „Spez. Wärmekapazität“ um
    t = t.replace("<w:tblLook ", '<w:tblLayout w:type="fixed" /><w:tblCellMar><w:left w:w="80" w:type="dxa" />'
                  '<w:right w:w="80" w:type="dxa" /></w:tblCellMar><w:tblLook ', 1)
    return re.sub(r"<w:tblGrid>.*?</w:tblGrid>", '<w:tblGrid><w:gridCol w:w="2211" /><w:gridCol w:w="2324" />'
                  '<w:gridCol w:w="2211" /><w:gridCol w:w="2324" /></w:tblGrid>', t, count=1, flags=re.S)


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
    d = re.sub(r"<w:tblHeader[^>]*/>", "", d)

    def messtabelle(m):
        """Versuchstabelle: Datenzeilen mindestens 10 mm hoch (567 Twips) zum Ausfüllen von Hand."""
        t = m.group(0)
        t = kaffee_breiten(t)
        if "Milch sofort" not in t:
            return t
        return t.replace("<w:trPr><w:cantSplit/>", '<w:trPr><w:cantSplit/><w:trHeight w:val="567" w:hRule="atLeast"/>')
    d = re.sub(r"<w:tbl>.*?</w:tbl>", messtabelle, d, flags=re.S)

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
    d = "".join(teile)
    # Quellenblock als Einheit (Abnahme 3): keine einzelnen Quellenpunkte allein auf der letzten Seite
    k = d.rfind("Quellen der Arbeitswerte")
    if k > 0:
        anfang = max(d.rfind("<w:p>", 0, k), d.rfind("<w:p ", 0, k))
        ende = d.rfind("<w:sectPr")
        absaetze = re.findall(r"<w:p>(?:(?!</w:p>).)*?</w:p>|<w:p .*?</w:p>", d[anfang:ende], flags=re.S)
        rest = d[anfang:ende]
        for par in absaetze[:-1]:
            rest = rest.replace(par, keep(par), 1)
        d = d[:anfang] + rest + d[ende:]
    inhalt["word/document.xml"] = d.encode("utf-8")
    # Marken nummerierter Aufzählungen fett (a), b), …) wie im PDF (Ä20)
    if "word/numbering.xml" in inhalt:
        nb = inhalt["word/numbering.xml"].decode("utf-8")
        nb = re.sub(r'(<w:lvl w:ilvl="\d+">(?:(?!</w:lvl>).)*?<w:numFmt w:val="(?!bullet)[^"]+" />(?:(?!</w:lvl>).)*?)</w:lvl>',
                    r"\1<w:rPr><w:b /><w:bCs /></w:rPr></w:lvl>", nb, flags=re.S)
        inhalt["word/numbering.xml"] = nb.encode("utf-8")
    if os.path.basename(pfad).startswith("Kaffee_Loesung"):
        for n in [n for n in inhalt if n.startswith("word/header")]:
            inhalt[n] = inhalt[n].decode("utf-8").replace(KOPF_RECHTS, "Lösung, " + KOPF_RECHTS).encode("utf-8")
    tmp = pfad + ".tmp"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        for n, b in inhalt.items():
            z.writestr(n, b)
    shutil.move(tmp, pfad)


for name in ("Kaffee_Aufgabe", "Kaffee_Loesung", "Kaffee_Loesung_Studierende"):
    word_zusammenhalten(os.path.join(HIER, name + ".docx"))
print("fertig:", r["T1"] - K, r["T2"] - K)
