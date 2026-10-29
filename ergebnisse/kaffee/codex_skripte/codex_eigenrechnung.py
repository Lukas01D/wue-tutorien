"""Unabhängige Erstlösung, vor Lesen von Lösung und C_modell erstellt.

Quelle: ausschließlich Aufgabe, Formelsammlung und Bilanzierungsfolien.
Alle Rechnungen in SI; Temperaturen in °C nur in Differenzen/Mischungen.
Aufruf: python ergebnisse/kaffee/codex_skripte/codex_eigenrechnung.py
"""

import json
from math import exp, log

from scipy.integrate import quad, solve_ivp


def rechnen():
    m_k = 200e-6 * 1000
    m_m = 30e-6 * 1030
    c_k = m_k * 4180
    c_m = m_m * 3940
    c_b = 0.300 * 850
    c_ges = c_k + c_m
    t_u, t_k, t_m, t_10 = 20.0, 80.0, 5.0, 67.0
    dauer = 3600.0

    # a: C_K*(theta_K-theta_mix)=C_M*(theta_mix-theta_M).
    mix = (c_k * t_k + c_m * t_m) / c_ges
    # b: C*dT/dt=-H*(T-T_u); dT/(T-T_u)=-H/C*dt.
    # ln[(T-T_u)/(T_0-T_u)]=-Ht/C, also T=T_u+(T_0-T_u)e^(-Ht/C).
    # c: H=-C_K/t_mess * ln[(theta_mess-theta_u)/(theta_K0-theta_u)].
    h = -c_k / 600 * log((t_10 - t_u) / (t_k - t_u))

    def kalt(start, kapazitaet, leitwert=h, t=dauer):
        return t_u + (start - t_u) * exp(-leitwert * t / kapazitaet)

    t_1 = kalt(mix, c_ges)
    t_2_vor = kalt(t_k, c_k)
    t_2 = (c_k * t_2_vor + c_m * t_m) / c_ges
    q_1 = c_ges * (mix - t_1)
    q_2 = c_k * (t_k - t_2_vor)
    # Unabhängige numerische Integration der DGL und des Wärmestroms.
    numerisch = []
    for start, kap in [(mix, c_ges), (t_k, c_k)]:
        sol = solve_ivp(
            lambda t, y: [-h * (y[0] - t_u) / kap, h * (y[0] - t_u)],
            (0, dauer), [start, 0], rtol=1e-11, atol=1e-11,
        )
        numerisch.append(sol.y[:, -1].tolist())
    assert abs(numerisch[0][0] - t_1) < 1e-8
    assert abs(numerisch[1][0] - t_2_vor) < 1e-8
    assert abs(numerisch[0][1] - q_1) < 1e-5
    assert abs(numerisch[1][1] - q_2) < 1e-5
    assert abs((q_2 - q_1) - c_ges * (t_1 - t_2)) < 1e-8
    assert abs(quad(lambda t: h * (kalt(mix, c_ges, t=t) - t_u), 0, dauer)[0] - q_1) < 1e-6

    # f: identische Messung, zusätzliche Speicherkapazität in beiden Bechern.
    h_b = h * (c_k + c_b) / c_k
    mix_b = ((c_k + c_b) * t_k + c_m * t_m) / (c_ges + c_b)
    t_1_b = kalt(mix_b, c_ges + c_b, h_b)
    t_2_b = ((c_k + c_b) * kalt(t_k, c_k + c_b, h_b) + c_m * t_m) / (c_ges + c_b)

    # g: gleiche Milchmasse und gleiche Wärmekapazität, nur 60 °C statt 5 °C.
    mix_s = (c_k * t_k + c_m * 60) / c_ges
    t_1_s = kalt(mix_s, c_ges)
    t_2_s = (c_k * t_2_vor + c_m * 60) / c_ges

    # h1: C_K*(theta_K0-theta_u)*(E_ges-E_K)=C_M*(theta_M-theta_u)*(1-E_ges).
    e_k = exp(-h * dauer / c_k)
    e_ges = exp(-h * dauer / c_ges)
    kipp = t_u + c_k * (t_k - t_u) * (e_ges - e_k) / (c_m * (1 - e_ges))
    # h2: Milch nur in Tasse 2 wird vor Zugabe auf maximal Umgebungstemperatur erwärmt.
    t_2_raum = (c_k * t_2_vor + c_m * t_u) / c_ges
    t_m_fuer_gleichstand = t_m + c_ges * (t_1 - t_2) / c_m

    return {
        'm_K_kg': m_k, 'm_M_kg': m_m,
        'C_K_J_pro_K': c_k, 'C_M_J_pro_K': c_m, 'C_B_J_pro_K': c_b,
        'a_theta_1_0_C': mix,
        'c_kA_W_pro_K': h, 'tau_K_s': c_k / h, 'tau_1_s': c_ges / h,
        'd_theta_2_vor_Milch_C': t_2_vor, 'd_theta_1_C': t_1, 'd_theta_2_C': t_2,
        'd_Differenz_K': t_1 - t_2,
        'e_Q1_kJ': q_1 / 1000, 'e_Q2_kJ': q_2 / 1000, 'e_DeltaQ_kJ': (q_2 - q_1) / 1000,
        'Numerik_Endtemperatur_und_Integral_J': numerisch,
        'f_kA_W_pro_K': h_b, 'f_theta_1_0_C': mix_b,
        'f_theta_1_C': t_1_b, 'f_theta_2_C': t_2_b,
        'g_theta_1_C': t_1_s, 'g_theta_2_C': t_2_s,
        'h1_Kipptemperatur_C': kipp,
        'h2_Waermeaufnahme_Milch_max_kJ': c_m * (t_u - t_m) / 1000,
        'h2_theta_2_max_C': t_2_raum, 'h2_Restabstand_K': t_1 - t_2_raum,
        'h2_Milchtemperatur_fuer_Gleichstand_C': t_m_fuer_gleichstand,
    }


if __name__ == '__main__':
    print(json.dumps(rechnen(), ensure_ascii=False, indent=2))
