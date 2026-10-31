#!/usr/bin/env python3
"""Unabhaengige X2-Abnahme, nur Standardbibliothek, kein Import des Paketmodells.

Ausgangspunkt: Daten der Aufgabe, dU/dt = -G*(theta-theta_u),
Energieerhaltung beim Mischen. Alle internen Rechnungen bleiben ungerundet.
Aufruf im Repository: python ergebnisse/kaffee/codex_skripte/x2_eigenrechnung.py
Die Sollwerte sind die gedruckten Werte der Loesung, keine Modell-Ausgabe.
Gerundete Angaben werden mit einer halben Einheit der letzten Stelle geprueft;
bei ausdruecklichen Schaetzungen ist die angegebene Toleranz groesser.
Empirische Quellenwerte und Zeitplanangaben sind keine Rechenergebnisse.
"""

from math import exp, log, pi


# SI-Eingaben direkt aus der Aufgabentabelle.
VK, VM = 200e-6, 30e-6
rhoK, rhoM, cpK, cpM = 1000.0, 1030.0, 4180.0, 3940.0
coffee0, cold, ambient, measured, hot = 80.0, 5.0, 20.0, 67.0, 60.0
measurement_time, end_time = 600.0, 3600.0
mug_mass, mug_cp = 0.300, 850.0
mK, mM = VK * rhoK, VM * rhoM
CK, CM, CB = mK * cpK, mM * cpM, mug_mass * mug_cp
CG = CK + CM


def conductance(capacity=CK, measurement=measured):
    return capacity / measurement_time * log((coffee0 - ambient) / (measurement - ambient))


def mixed(temperature, milk, capacity=CK):
    return (capacity * temperature + CM * milk) / (capacity + CM)


def cooled(start, capacity, time, loss):
    return ambient + (start - ambient) * exp(-loss * time / capacity)


def cups(milk1=cold, milk2=None, mug=0.0, time=end_time, factor=1.0,
         measurement=measured, old_loss=False):
    milk2 = milk1 if milk2 is None else milk2
    c = CK + mug
    loss = conductance(CK if old_loss else c, measurement)
    initial = mixed(coffee0, milk1, c)
    black = cooled(coffee0, c, time, loss)
    early = cooled(initial, c + CM, time, loss * factor)
    late = mixed(black, milk2, c)
    return initial, black, early, late


def root(function, lower, upper):
    assert function(lower) * function(upper) <= 0, 'Nullstelle nicht eingeschlossen'
    for _ in range(100):
        middle = (lower + upper) / 2
        if function(lower) * function(middle) <= 0:
            upper = middle
        else:
            lower = middle
    return (lower + upper) / 2


def difference(**kwargs):
    _, _, early, late = cups(**kwargs)
    return early - late


def power_cups(exponent, milk=cold):
    """Separierte DGL: z^(1-n)-z0^(1-n)=(n-1)*a*t/C, z=theta-theta_u."""
    if exponent == 1:
        return cups(milk1=milk)[2:]
    q = 1 - exponent
    rate = CK * ((measured - ambient)**q - (coffee0 - ambient)**q) / (-q * measurement_time)

    def evolve(start, capacity):
        return ambient + ((start - ambient)**q - q * rate * end_time / capacity)**(1 / q)

    return evolve(mixed(coffee0, milk), CG), mixed(evolve(coffee0, CK), milk)


rows = []


def check(place, name, value, expected, digits=2, tolerance=None, unit=''):
    tolerance = 0.5 * 10**(-digits) if tolerance is None else tolerance
    ok = abs(value - expected) <= tolerance + 1e-10
    rows.append(ok)
    print(f"{'OK' if ok else 'ABWEICHUNG'} | {place} | {name} | {value:.8f} {unit} | "
          f"Text {expected:g}, Toleranz {tolerance:g}")


def main():
    print('X2-Eigenrechnung: unabhaengige Ableitung aus Aufgabedaten')
    print('Einheiten intern: kg, J, s, W; Temperaturdifferenzen in K.')
    print('Stellen beziehen sich auf Kaffee_Loesung.md des Pruefstands 560b8d4.\n')
    loss = conductance()
    initial, black, early, late = cups()
    _, _, warm1, warm2 = cups(milk1=hot)
    bi, bk, b1, b2 = cups(mug=CB)
    loss_b = conductance(CK + CB)
    eG, eK = exp(-loss * end_time / CG), exp(-loss * end_time / CK)
    eB = exp(-loss_b * end_time / (CG + CB))
    heat1, heat2 = CG * (initial - early), CK * (coffee0 - black)
    coffee_effect = CK * (coffee0 - ambient) * (eG - eK) / CG
    milk_effect = CM * (cold - ambient) * (eG - 1) / CG
    checks = [
        ('104', 'm_K', mK, 0.200, 3), ('104', 'm_M', mM, 0.0309, 4),
        ('106', 'C_K', CK, 836.0, 1), ('106', 'C_M', CM, 121.7, 1),
        ('125', 'C_G', CG, 957.7, 1), ('125', 'T_K0', coffee0 + 273.15, 353.15, 2),
        ('125', 'T_M', cold + 273.15, 278.15, 2),
        ('125', 'T_1,0', initial + 273.15, 343.62, 2), ('a/49', 'theta_1,0', initial, 70.47, 2),
        ('142', 'Messung-Uebertemperatur', measured - ambient, 47.0, 0),
        ('142', 'Start-Uebertemperatur', coffee0 - ambient, 60.0, 0),
        ('c/55,142', 'kA', loss, 0.3402, 4),
        ('146', 'tau_K in min', CK / loss / 60, 41.0, 1),
        ('146', 'tau_G in min', CG / loss / 60, 46.9, 1),
        ('146,226', 'theta_K(tau)', ambient + (coffee0 - ambient) / exp(1), 42.1, 1),
        ('150,184', 'e_G', eG, 0.2783, 4), ('154,184', 'e_K', eK, 0.2310, 4),
        ('150', 'T_1', early + 273.15, 307.20, 2), ('d/58,98,150', 'theta_1', early, 34.05, 2),
        ('154', 'T_K(60)', black + 273.15, 307.01, 2), ('154,Abb.L2', 'theta_K(60)', black, 33.86, 2),
        ('156', 'T_2', late + 273.15, 303.34, 2), ('d/58,98,156', 'theta_2', late, 30.19, 2),
        ('158,166', 'theta_1-theta_2', early - late, 3.85, 2),
        ('163', 'Abkuehlung Tasse 1', initial - early, 36.42, 2),
        ('164', 'Abkuehlung Tasse 2', coffee0 - black, 46.14, 2),
        ('e/61,163', 'Q_1 in kJ', heat1 / 1000, 34.88, 2),
        ('e/61,164', 'Q_2 in kJ', heat2 / 1000, 38.57, 2),
        ('244', 'Q_2-Q_1 in kJ', (heat2 - heat1) / 1000, 3.69, 2),
        ('166', 'Energiekontrolle', (heat2 - heat1) / CG, early - late, 10),
        ('168', 'Qdot_1(0)', loss * (initial - ambient), 17.2, 1),
        ('168', 'Qdot_2(0)', loss * (coffee0 - ambient), 20.4, 1),
        ('174', 'T_M,h', hot + 273.15, 333.15, 2),
        ('175', 'T_1,0 warm', mixed(coffee0, hot) + 273.15, 350.61, 2),
        ('176', 'T_1 warm', warm1 + 273.15, 309.14, 2),
        ('f/64,176', 'theta_1 warm', warm1, 35.99, 2),
        ('177', 'T_2 warm', warm2 + 273.15, 310.33, 2),
        ('f/64,177', 'theta_2 warm', warm2, 37.18, 2),
        ('179', 'Vorsprung Tasse 2 warm', warm2 - warm1, 1.19, 2),
        ('184', 'Kaffee-Effekt', coffee_effect, 2.48, 2),
        ('184', 'Milch-Effekt kalt', milk_effect, 1.38, 2),
        ('184', 'Milch-Effekt warm', CM * (hot - ambient) * (eG - 1) / CG, -3.67, 2),
        ('186', 'C_B', CB, 255.0, 1), ('186', 'C_B/C_K Prozent', CB / CK * 100, 30.5, 1),
        ('187', 'C_K+C_B', CK + CB, 1091.0, 1), ('g/67,187', 'kA Becher', loss_b, 0.4440, 4),
        ('189', 'tau Becher schwarz min', (CK + CB) / loss_b / 60, 41.0, 1),
        ('192', 'T_1,0 Becher', bi + 273.15, 345.62, 2),
        ('194', 'Uebertemperatur Becher', bi - ambient, 52.47, 2),
        ('194', 'e_G Becher', eB, 0.2676, 4), ('194', 'T_1 Becher', b1 + 273.15, 307.19, 2),
        ('g/67,194', 'theta_1 Becher', b1, 34.04, 2),
        ('196', 'theta_1,0 Becher', bi, 72.47, 2),
        ('196', 'tau_G Becher min', (CG + CB) / loss_b / 60, 45.5, 1),
        ('198', 'T_K(60) Becher', bk + 273.15, 307.01, 2),
        ('199', 'T_2 Becher', b2 + 273.15, 304.11, 2),
        ('g/67,199', 'theta_2 Becher', b2, 30.96, 2),
        ('201', 'Differenz Becher', b1 - b2, 3.08, 2),
        ('201', 'Milchzuwachs Becher Prozent', CM / (CK + CB) * 100, 11, 0),
        ('201', 'Milchzuwachs ohne Becher Prozent', CM / CK * 100, 15, 0),
        ('201', 'Kaffee-Effekt Becher', (CK + CB) * (coffee0 - ambient) * (eB - eK) / (CG + CB), 1.98, 2),
        ('201', 'Milch-Effekt Becher', CM * (cold - ambient) * (eB - 1) / (CG + CB), 1.10, 2),
        ('220', 'Fehler kA mit Minuten', loss * 60, 20.41, 2),
        ('220', 'Fehler Q_2 mit Gemisch kJ', CG * (coffee0 - black) / 1000, 44.19, 2),
        ('220', 'Fehler altes kA: theta_1', cups(mug=CB, old_loss=True)[2], 39.1, 1),
        ('220', 'Fehler altes kA: theta_2', cups(mug=CB, old_loss=True)[3], 36.1, 1),
        ('220', 'Fehler Becher nicht mitgemischt: theta_1', cooled(initial, CG + CB, end_time, loss_b), 33.51, 2),
        ('223', 'Spate Milch, Grenzwert warm', (CG * warm1 - CK * black) / CM, 50.6, 1),
        ('223', '10 Prozent weniger kA, Vorsprung Tasse 1', difference(milk1=hot, factor=0.9), 0.99, 2),
        ('224', 'Potenz 4/3, theta_1', power_cups(4 / 3)[0], 37.65, 2),
        ('224', 'Potenz 4/3, theta_2', power_cups(4 / 3)[1], 33.34, 2),
        ('224', 'Potenz 4/3, Differenz', power_cups(4 / 3)[0] - power_cups(4 / 3)[1], 4.31, 2),
        ('226', 'Tassenwaermer ohne Becher W', loss * (60 - ambient), 13.6, 1),
        ('226', 'Tassenwaermer mit Becher W', loss_b * (60 - ambient), 17.8, 1),
        ('226', 'Unterschaetzung Prozent', (1 - loss / loss_b) * 100, 23, 0),
        ('228', 'Abkuehlrate bei 40 C, K/min', loss_b * 20 / (CG + CB) * 60, 0.4, 1),
        ('229', '40 min, Unterschied mit Becher', difference(mug=CB, time=2400), 2.97, 2),
        ('229', '40 min, Unterschied ohne Becher', difference(time=2400), 3.70, 2),
        ('229', '40 min, 3 Prozent mehr kA', difference(mug=CB, time=2400, factor=1.03), 2.4, 1),
        ('229', '40 min, 5 Prozent mehr kA', difference(mug=CB, time=2400, factor=1.05), 2.0, 1),
        ('232,242', 'Q_M maximal kJ', CM * (ambient - cold) / 1000, 1.83, 2),
        ('245', 'Untergrenze Abstand K', (heat2 - heat1 - CM * (ambient - cold)) / CG, 1.95, 2),
        ('247', 'theta_2 bei spaeter Milch 20 C', cups(milk2=ambient)[3], 32.10, 2),
        ('247', 'Spaete Milch, Gleichstand mit kalter Tasse 1', (CG * early - CK * black) / CM, 35.3, 1),
    ]
    for place, name, value, expected, digits in checks:
        check(place, name, value, expected, digits)

    crossing = log((coffee0 - ambient) / (initial - ambient)) / (loss / CK - loss / CG)
    check('168,225,Abb.L2', 'Schnittpunkt min', crossing / 60, 55.7, 1)
    check('225', 'Maximale Differenz K', difference(time=crossing), 3.86)
    for temperature, expected in [(66, 3.82), (68, 3.86)]:
        check('160', f'Differenz Messung {temperature} C', difference(measurement=temperature), expected)
        print(f'INFO | 160 | Messung {temperature}: kA {conductance(measurement=temperature):.8f}, '
              f'Aenderung {(conductance(measurement=temperature)/loss-1)*100:.3f} %, '
              f'Temperaturen {cups(measurement=temperature)[2:]}')
    area = 2 * pi * 0.08**2 / 4 + pi * 0.08 * (VK / (pi * 0.08**2 / 4))
    check('144', 'Fuellhoehe Kaffee cm', VK / (pi * 0.08**2 / 4) * 100, 4.0, 1)
    check('144', 'Fuellhoehe mit Milch cm', (VK + VM) / (pi * 0.08**2 / 4) * 100, 4.6, 1)
    check('144', 'Flaechenzuwachs Prozent', 4 * VM / 0.08 / area * 100, 7.5, 1)
    check('146', 'Flaeche cm2', area * 1e4, 201, 0)
    check('146', 'kA/A W/(m2 K)', loss / area, 17, 0)
    for factor, expected in [(1.03, 3.32), (1.05, 2.98)]:
        check('144', f'Differenz kA Faktor {factor}', difference(factor=factor), expected)
    for mug, expected in [(0, 25), (CB, 19)]:
        threshold = root(lambda x: difference(mug=mug, factor=x), 1, 2)
        check('144', f'kA-Kipppunkt Prozent, Becher {mug:g}', (threshold - 1) * 100, expected, 0)
    reduction = (1 - root(lambda x: difference(milk1=hot, factor=x), 0.5, 1)) * 100
    check('223', 'kA-Reduktion warm, Gleichstand Prozent', reduction, 5.6, 1)
    for factor, expected in [(1, 47.0), (1.05, 37), (0.95, 58)]:
        threshold = root(lambda x: difference(milk1=x, factor=factor), -20, 100)
        check('235,239', f'Milchkipppunkt kA Faktor {factor}', threshold, expected,
              digits=1 if factor == 1 else 0)
    threshold = root(lambda x: power_cups(4 / 3, x)[0] - power_cups(4 / 3, x)[1], 0, 100)
    check('239', 'Milchkipppunkt Potenz 4/3', threshold, 50, 0)
    check('225', 'Differenz beide Milchportionen 20 C', difference(milk1=ambient), 2.5, 1)
    check('225', 'Verdunstete Masse g bei dh_v=2380 kJ/kg', 0.5 * heat2 / 2.38e6 * 1000, 8, 0)
    check('225', 'Verdunsteter Massenanteil Prozent', 0.5 * heat2 / 2.38e6 / mK * 100, 4, 0)
    check('189', 'Zunahme kA Prozent', (loss_b / loss - 1) * 100, 31, 0)

    print('\nINFO | 229 | Becher 3 bei Milch 20 C ist eine obere Temperaturgrenze.')
    _, _, v1, v3 = cups(mug=CB, time=2400, milk2=ambient)
    v2 = cups(mug=CB, time=2400)[3]
    print(f'INFO | 229 | 40 min: B1={v1:.8f}, B2={v2:.8f}, B3_max={v3:.8f} C; '
          f'B1-B3={v1-v3:.8f}, B3-B2={v3-v2:.8f} K')
    print('INFO | 224 | Verdunstungsmodell 38 bis 40 C und empirische Bereiche sind Schaetzungen, '
          'ohne festgelegte Modellparameter nicht eindeutig nachrechenbar.')
    print('INFO | 255-258 | Quellen-, Stoffdaten- und Versuchsangaben sind Vorgaben oder Fremdmessungen, '
          'keine aus dieser Aufgabe ableitbaren Zahlen.')
    print(f'INFO | 237 | Nur mit gedruckten Zwischenwerten: 5+55*3.85/5.05={5+55*3.85/5.05:.8f} C; '
          'mit ungerundeten Zwischenwerten 47.00309280 C. Die Gleichheit ist eine Naeherung.')
    print(f'INFO | 245 | Nur mit gedruckten Zwischenwerten: (3.69-1.83)*1000/957.7='
          f'{(3.69-1.83)*1000/957.7:.8f} K; mit ungerundeten Zwischenwerten 1.94644242 K.')
    print(f'\nErgebnis: {sum(rows)}/{len(rows)} Zahlenvergleiche innerhalb der angegebenen Rundung/Toleranz.')
    raise SystemExit(0 if all(rows) else 1)


if __name__ == '__main__':
    main()
