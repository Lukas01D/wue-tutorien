# -*- coding: utf-8 -*-
"""Modell und Arbeitswerte der Kaffee-Aufgabe (eine Quelle für Skript und Dokumente).

Kaffee bzw. Kaffee-Milch-Gemisch ideal durchmischt, Wärmekapazität der Tasse vernachlässigt,
Wärmeabgabe Q_ab = kA (T - T_U) mit konstantem kA (Tutorium 5, instationär global).
Tasse 1: Milch bei t = 0, dann t_end abkühlen. Tasse 2: Kaffee t_end abkühlen, dann Milch zugeben.
"""
import math

P = dict(
    V_K=200e-6, rho_K=1000.0, cp_K=4180.0,      # Kaffee: Stoffwerte von Wasser (TDS 1,15 bis 1,35 %, SCA)
    V_M=30e-6, rho_M=1030.0, cp_M=3940.0,       # Milch: 30 ml (FSANZ 2011: im Mittel 31 g je Tasse);
                                                # rho 1027 bis 1033 kg/m³ (Goff et al.); c_p wie Tutorium 8 (3,94)
    th_K0=80.0,                                 # °C, Kaffee in der Tasse (gebrüht bei etwa 93 °C, in der Glaskanne
                                                # bis etwa 11 K kälter, beim Eingießen 2 bis 5 K kälter:
                                                # Abraham & Diller 2019; Servierbereich 71 bis 85 °C: Brown & Diller 2008)
    th_M=5.0,                                   # °C, Kühlschrank (BfR: höchstens 7 °C, besser unter 5 °C)
    th_U=20.0,                                  # °C, Raum
    t_end=60 * 60.0,                            # s
    t_mess=10 * 60.0, th_mess=67.0,             # Messung ohne Milch: nach 10 min noch 67 °C,
                                                # entspricht tau = 41 min (offener Keramikbecher, Ferreira 2025)
    th_Mh=60.0,                                 # °C, erwärmte Milch in Teil g (Thermoplan: 55 bis 65 °C)
    m_B=0.300, c_B=850.0,                       # Keramikbecher in Teil f und im Versuch (Arbeitswert, Schätzung)
    dh_v=2380e3,                                # J/kg, Verdampfungsenthalpie von Wasser bei etwa 50 °C (Abschätzung)
)


def rechne(p=P):
    r = dict(p)
    K = 273.15
    r["m_K"] = p["rho_K"] * p["V_K"]
    r["m_M"] = p["rho_M"] * p["V_M"]
    r["C_K"] = r["m_K"] * p["cp_K"]
    r["C_M"] = r["m_M"] * p["cp_M"]
    r["C_G"] = r["C_K"] + r["C_M"]
    T_K0, T_M, T_U = p["th_K0"] + K, p["th_M"] + K, p["th_U"] + K
    r.update(T_K0=T_K0, T_M=T_M, T_U=T_U, T_mess=p["th_mess"] + K)
    # kA aus der Messung (Tasse ohne Milch)
    r["ln_mess"] = math.log((r["T_mess"] - T_U) / (T_K0 - T_U))
    r["kA"] = -r["C_K"] / p["t_mess"] * r["ln_mess"]
    r["a_K"] = r["kA"] / r["C_K"]           # 1/s
    r["a_G"] = r["kA"] / r["C_G"]
    r["tau_K"] = 1 / r["a_K"]
    r["tau_G"] = 1 / r["a_G"]
    mix = lambda TK: (r["C_K"] * TK + r["C_M"] * T_M) / r["C_G"]
    # Tasse 1
    r["T1_0"] = mix(T_K0)
    r["e_G"] = math.exp(-r["a_G"] * p["t_end"])
    r["T1"] = T_U + (r["T1_0"] - T_U) * r["e_G"]
    # Tasse 2
    r["e_K"] = math.exp(-r["a_K"] * p["t_end"])
    r["T2_K"] = T_U + (T_K0 - T_U) * r["e_K"]
    r["T2"] = mix(r["T2_K"])
    r["dT"] = r["T1"] - r["T2"]
    # abgegebene Wärme in 60 min
    r["Q1"] = r["C_G"] * (r["T1_0"] - r["T1"])
    r["Q2"] = r["C_K"] * (T_K0 - r["T2_K"])
    r["Qdot1_0"] = r["kA"] * (r["T1_0"] - T_U)
    r["Qdot2_0"] = r["kA"] * (T_K0 - T_U)
    # Zeitpunkt, ab dem der Kaffee ohne Milch kälter ist als das Gemisch (falls vorhanden)
    d = r["a_K"] - r["a_G"]
    r["t_schnitt"] = math.log((T_K0 - T_U) / (r["T1_0"] - T_U)) / d if d > 0 else float("inf")
    # Milchtemperatur, bei der beide Tassen nach t_end gleich warm wären (lineares Modell)
    r["th_M_gleich"] = p["th_U"] + r["C_K"] * (T_K0 - T_U) * (r["e_G"] - r["e_K"]) / (r["C_M"] * (1 - r["e_G"]))
    return r


def zwei_tassen(p=P, C_T=0.0, th_M1=None, th_M2=None, kA1_faktor=1.0, t_end=None):
    """Beide Tassen allgemein: Becher mit Wärmekapazität C_T (immer so warm wie der Inhalt, mischt beim Zugießen mit),
    kA aus derselben Messung, Zugabe der späten Milch nach t_end, Milchtemperaturen th_M1 (Tasse 1) und th_M2 (Tasse 2)
    in °C, kA von Tasse 1 um kA1_faktor gegenüber der Messung verändert (z. B. höhere Füllung mit Milch)."""
    K = 273.15
    r = rechne(p)
    th_M1 = p["th_M"] if th_M1 is None else th_M1
    th_M2 = th_M1 if th_M2 is None else th_M2
    t = p["t_end"] if t_end is None else t_end
    CKT, CGT = r["C_K"] + C_T, r["C_G"] + C_T
    kA = -CKT / p["t_mess"] * r["ln_mess"]
    T10 = (CKT * r["T_K0"] + r["C_M"] * (th_M1 + K)) / CGT
    T1 = r["T_U"] + (T10 - r["T_U"]) * math.exp(-kA1_faktor * kA * t / CGT)
    T2K = r["T_U"] + (r["T_K0"] - r["T_U"]) * math.exp(-kA * t / CKT)
    T2 = (CKT * T2K + r["C_M"] * (th_M2 + K)) / CGT
    return dict(kA=kA, T1_0=T10, T1=T1, T2_K=T2K, T2=T2, dT=T1 - T2, th1=T1 - K, th2=T2 - K)


def becher(m_T=None, c_T=None, p=P, kA_neu=True):
    """Tasse mit Wärmekapazität m_T c_T, immer so warm wie ihr Inhalt.
    kA_neu=True: kA aus derselben Messung neu bestimmt (konsistent mit den gegebenen Daten)."""
    m_T = p["m_B"] if m_T is None else m_T
    c_T = p["c_B"] if c_T is None else c_T
    r = rechne(p)
    C_T = m_T * c_T
    CKT, CGT = r["C_K"] + C_T, r["C_G"] + C_T
    kA = -CKT / p["t_mess"] * r["ln_mess"] if kA_neu else r["kA"]
    T10 = (CKT * r["T_K0"] + r["C_M"] * r["T_M"]) / CGT
    T1 = r["T_U"] + (T10 - r["T_U"]) * math.exp(-kA * p["t_end"] / CGT)
    T2K = r["T_U"] + (r["T_K0"] - r["T_U"]) * math.exp(-kA * p["t_end"] / CKT)
    T2 = (CKT * T2K + r["C_M"] * r["T_M"]) / CGT
    return dict(C_T=C_T, anteil=C_T / r["C_K"], kA=kA, T1=T1, T2=T2, dT=T1 - T2)


def nichtlinear(n, p=P):
    """Wärmeabgabe c (T - T_U)^n, c so gewählt, dass die Messung (t_mess, th_mess) getroffen wird.
    Formtest bei gleicher Masse und gemeinsamem Verlustgesetz, keine Modellierung der Verdunstung.
    Exakte Lösung der Differentialgleichung C dT/dt = -c (T - T_U)^n (n > 1) durch Trennung der Variablen:
    (T - T_U)^(1 - n) = (T_0 - T_U)^(1 - n) + (n - 1) c t / C."""
    r = rechne(p)
    T_U = r["T_U"]

    def ende(T0, C, t, c):
        if n == 1:
            return T_U + (T0 - T_U) * math.exp(-c * t / C)
        return T_U + ((T0 - T_U) ** (1 - n) + (n - 1) * c * t / C) ** (1 / (1 - n))
    # c aus der Messung (geschlossen lösbar)
    if n == 1:
        c = -r["C_K"] / p["t_mess"] * r["ln_mess"]
    else:
        c = ((r["T_mess"] - T_U) ** (1 - n) - (r["T_K0"] - T_U) ** (1 - n)) * r["C_K"] / ((n - 1) * p["t_mess"])
    T1 = ende(r["T1_0"], r["C_G"], p["t_end"], c)
    T2K = ende(r["T_K0"], r["C_K"], p["t_end"], c)
    T2 = (r["C_K"] * T2K + r["C_M"] * r["T_M"]) / r["C_G"]
    return T1, T2


def gleichstand(f, lo=-50.0, hi=200.0):
    """Nullstelle einer monotonen Funktion f (Bisektion), z. B. Milchtemperatur für gleich warme Tassen."""
    flo = f(lo)
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if (f(mid) > 0) == (flo > 0):
            lo, flo = mid, f(mid)
        else:
            hi = mid
    return 0.5 * (lo + hi)
