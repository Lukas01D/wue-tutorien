"""Zusatzprüfung nach abgeschlossenem Erstdurchgang, ohne Import des Paketmodells.

Prüft weitere Zahlen und Grenzen der Aussagen in der Musterlösung.
"""

import json
from math import exp, log

from scipy.integrate import solve_ivp

from codex_eigenrechnung import rechnen


def zusatz():
    r = rechnen()
    ck, cm, cb = (r[k] for k in ('C_K_J_pro_K', 'C_M_J_pro_K', 'C_B_J_pro_K'))
    cg = ck + cm
    h = r['c_kA_W_pro_K']
    eg, ek = exp(-h * 3600 / cg), exp(-h * 3600 / ck)
    schnitt = log(60 / (r['a_theta_1_0_C'] - 20)) / (h / ck - h / cg)

    def becher(t, neu=True, milch_spaet=5):
        hh = h * (ck + cb) / ck if neu else h
        mix = ((ck + cb) * 80 + cm * 5) / (cg + cb)
        t1 = 20 + (mix - 20) * exp(-hh * t / (cg + cb))
        t2_vor = 20 + 60 * exp(-hh * t / (ck + cb))
        t2 = ((ck + cb) * t2_vor + cm * milch_spaet) / (cg + cb)
        return [t1, t2, t1 - t2]

    # Das im Lösungshinweis angegebene Potenzgesetz kann exakt integriert werden.
    potenz = []
    for n in [1.0, 4 / 3, 1.6]:
        a = h if n == 1 else ck * (47 ** (1 - n) - 60 ** (1 - n)) / ((n - 1) * 600)

        def endwert(start, kap, t):
            x = start - 20
            if n == 1:
                return 20 + x * exp(-a * t / kap)
            return 20 + (x ** (1 - n) + (n - 1) * a * t / kap) ** (1 / (1 - n))

        assert abs(endwert(80, ck, 600) - 67) < 1e-10
        t1 = endwert(r['a_theta_1_0_C'], cg, 3600)
        t2_vor = endwert(80, ck, 3600)
        t2 = (ck * t2_vor + cm * 5) / cg
        ode = solve_ivp(lambda t, y: [-a * (y[0] - 20) ** n / cg], (0, 3600),
                        [r['a_theta_1_0_C']], rtol=1e-11, atol=1e-11)
        assert abs(ode.y[0, -1] - t1) < 1e-8
        potenz.append({'n': n, 'theta_1_C': t1, 'theta_2_C': t2, 'Differenz_K': t1 - t2})

    # Schaum in Tasse 1 hat bei Zugabe 60 °C; wie warm muss die späte Portion sein?
    spaete_mindesttemperatur = (cg * r['g_theta_1_C'] - ck * r['d_theta_2_vor_Milch_C']) / cm
    return {
        'Qdot_1_start_W': h * (r['a_theta_1_0_C'] - 20),
        'Qdot_2_start_W': h * 60,
        'Schnittzeit_min': schnitt / 60,
        'e_G': eg, 'e_K': ek,
        'g_Kaffee_Anteil_K': ck * 60 * (eg - ek) / cg,
        'g_Milch_Anteil_kalt_K': cm * (5 - 20) * (eg - 1) / cg,
        'g_Milch_Anteil_heiss_K': cm * (60 - 20) * (eg - 1) / cg,
        'g_Anfangstemperatur_C': (ck * 80 + cm * 60) / cg,
        'g_spaete_Temperatur_fuer_Gleichstand_C': spaete_mindesttemperatur,
        'g_spaete_Temperatur_20_C_ergibt_Tasse_2_C': r['h2_theta_2_max_C'],
        'f_Becherkapazitaet_Anteil_an_Kaffee_prozent': 100 * cb / ck,
        'f_altes_kA_theta1_theta2_Differenz': becher(3600, neu=False),
        'Versuch_30_min_theta1_theta2_Differenz': becher(1800),
        'Versuch_60_min_theta1_theta2_Differenz': becher(3600),
        'Versuch_Milch20_theta1_theta3_Differenz': becher(3600, milch_spaet=20),
        'Nichtlinear_exakt': potenz,
    }


if __name__ == '__main__':
    print(json.dumps(zusatz(), ensure_ascii=False, indent=2))
