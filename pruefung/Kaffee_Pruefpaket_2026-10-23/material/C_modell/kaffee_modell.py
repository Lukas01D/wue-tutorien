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
    th_K0=80.0,                                 # °C, Kaffee kurz nach dem Eingießen (Ausschank 71 bis 85 °C,
                                                # Brown & Diller 2008; beim Eingießen 2 bis 5 K weniger)
    th_M=5.0,                                   # °C, Kühlschrank (BfR: höchstens 7 °C, besser unter 5 °C)
    th_U=20.0,                                  # °C, Raum
    t_end=60 * 60.0,                            # s
    t_mess=10 * 60.0, th_mess=67.0,             # Messung ohne Milch: nach 10 min noch 67 °C,
                                                # entspricht tau = 41 min (offener Keramikbecher, Ferreira 2025)
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


def becher(m_T=0.300, c_T=850.0, p=P, kA_neu=True):
    """Tasse mit Wärmekapazität m_T c_T, immer so warm wie ihr Inhalt.
    kA_neu=True: kA aus derselben Messung neu bestimmt (konsistent mit den gegebenen Daten)."""
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
    """Wärmeabgabe c (T - T_U)^n, c so gewählt, dass die Messung (t_mess, th_mess) getroffen wird."""
    r = rechne(p)
    T_U = r["T_U"]

    def sim(T0, C, t, c):
        T, dt = T0, 1.0
        for _ in range(int(t)):
            T -= c * max(T - T_U, 0.0) ** n / C * dt
        return T
    lo, hi = 1e-5, 10.0
    for _ in range(60):
        mid = math.sqrt(lo * hi)
        if sim(r["T_K0"], r["C_K"], p["t_mess"], mid) > r["T_mess"]:
            lo = mid
        else:
            hi = mid
    c = math.sqrt(lo * hi)
    T1 = sim(r["T1_0"], r["C_G"], p["t_end"], c)
    T2K = sim(r["T_K0"], r["C_K"], p["t_end"], c)
    T2 = (r["C_K"] * T2K + r["C_M"] * r["T_M"]) / r["C_G"]
    return T1, T2
