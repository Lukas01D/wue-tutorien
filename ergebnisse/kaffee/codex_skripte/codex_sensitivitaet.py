#!/usr/bin/env python3
"""Unabhängige Sensitivität aus der originalen Aufgabenstellung.

Keine Importe aus dem gelieferten Rechenmodell. Aufruf aus beliebigem Ordner:
python ergebnisse/kaffee/codex_skripte/codex_sensitivitaet.py

Nichtlineare Verlustgesetze sind bewusst hypothetische Formtests. Sie liefern
keine empirische Verdunstungsprognose und verändern die Masse nicht.
"""

from itertools import product
from math import exp, log

from scipy.integrate import quad, solve_ivp


CK = 0.200 * 4180.0
CM = 0.030 * 1030.0 * 3940.0 / 1000.0
CB = 0.300 * 850.0
TIME = 3600.0
TU = 20.0
T0 = 80.0
TM = 5.0
T10 = 67.0


def linear(cup=0.0, milk=CM, initial=T0, milk_temp=TM, ambient=TU,
           measured=T10, ratio=1.0, calibrated_k=None):
    """kA wird an Tasse 2 kalibriert; ratio multipliziert nur kA von Tasse 1."""
    plain_capacity = CK + cup
    capacity = plain_capacity + milk
    k = (plain_capacity / 600.0 * log((initial - ambient) /
                                     (measured - ambient))
         if calibrated_k is None else calibrated_k)
    mix = (plain_capacity * initial + milk * milk_temp) / capacity
    early = ambient + (mix - ambient) * exp(-ratio * k * TIME / capacity)
    plain_final = ambient + (initial - ambient) * exp(-k * TIME / plain_capacity)
    late = (plain_capacity * plain_final + milk * milk_temp) / capacity
    return k, early, late, early - late


def nonlinear(shape, cup=0.0):
    """C dT/dt = -scale*shape(T), gemeinsame Verlustfunktion beider Tassen.

    scale wird so bestimmt, dass reiner Kaffee 80 -> 67 °C in 600 s erfüllt.
    Die Kalibrierung ist C*Integral(1/shape,67,80)/600.
    """
    plain_capacity = CK + cup
    capacity = plain_capacity + CM
    scale = plain_capacity / 600.0 * quad(lambda temp: 1.0 / shape(temp),
                                        T10, T0, epsabs=1e-12)[0]
    mix = (plain_capacity * T0 + CM * TM) / capacity

    def cool(initial, c, time):
        result = solve_ivp(lambda _t, y: [-scale * shape(y[0]) / c],
                           (0.0, time), [initial], rtol=1e-10, atol=1e-10)
        assert result.success
        return result.y[0, -1]

    assert abs(cool(T0, plain_capacity, 600.0) - T10) < 1e-6
    early = cool(mix, capacity, TIME)
    plain = cool(T0, plain_capacity, TIME)
    late = (plain_capacity * plain + CM * TM) / capacity
    return early, late, early - late


def show(label, result):
    k, first, second, gap = result
    print(f"{label}: kA={k:.9f} W/K; T1={first:.6f} °C; "
          f"T2={second:.6f} °C; T1-T2={gap:.6f} K")


def main():
    print("CODEx: Unabhängige Sensitivitätsrechnung aus Aufgabe allein")
    print("C_K=%.6f J/K; C_M=%.6f J/K; C_B=%.6f J/K" % (CK, CM, CB))
    for cup in (0.0, CB):
        print(f"\nBECHERKAPAZITÄT {cup:.1f} J/K")
        base = linear(cup=cup)
        show("Basis", base)
        print("Nur 10-min-Messung variiert, übrige Eingaben fest:")
        for measured in (66.0, 67.0, 68.0):
            show(f"T10={measured:.0f} °C", linear(cup=cup, measured=measured))

        corners = []
        for initial, measured, ambient, milk_temp in product(
                (79.0, 81.0), (66.0, 68.0), (19.0, 21.0), (4.0, 6.0)):
            result = linear(cup=cup, initial=initial, measured=measured,
                            ambient=ambient, milk_temp=milk_temp)
            corners.append((result[3], initial, measured, ambient, milk_temp))
        print("Gemeinsame 16 Eckkombinationen unabhängiger Eingabefehler ±1 K")
        print("(Gap, T0, T10, Tu, Tm), Minimum:", min(corners))
        print("(Gap, T0, T10, Tu, Tm), Maximum:", max(corners))
        shifted = linear(cup=cup, initial=81.0, measured=68.0,
                         ambient=21.0, milk_temp=6.0)
        assert abs(shifted[3] - base[3]) < 1e-12
        print("Gemeinsamer Offset +1 K aller vier Temperaturangaben: Gap unverändert.")

        print("Milchvolumen variiert, kA fest auf Basiswert:")
        for ml in (15.0, 30.0, 45.0, 60.0):
            show(f"V_M={ml:.0f} ml", linear(cup=cup, milk=ml*1e-6*1030*3940,
                                           calibrated_k=base[0]))
        print("Starttemperatur variiert, kA fest auf Basiswert:")
        for initial in (70.0, 80.0, 90.0):
            show(f"T0={initial:.0f} °C", linear(cup=cup, initial=initial,
                                              calibrated_k=base[0]))

        c = CK + cup + CM
        mix = ((CK+cup)*T0 + CM*TM) / c
        critical = -c / TIME / base[0] * log((base[2]-TU)/(mix-TU))
        print(f"Kippverhältnis kA_mit_Milch/kA_ohne_Milch={critical:.9f}")
        assert abs(linear(cup=cup, ratio=critical)[3]) < 1e-10
        for ratio in (0.8, 1.0, 1.15, 1.2, 1.3):
            show(f"Verhältnis kA1/kA2={ratio:.2f}", linear(cup=cup, ratio=ratio))
        print("Temperaturabfall Tasse 1 zu Beginn der Schlussmessung: "
              f"{base[0]/c*(base[1]-TU)*60:.6f} K/min (momentan)")

        print("Hypothetische GEMEINSAME temperaturabhängige Verlustgesetze:")
        shapes = {
            "linear": lambda temp: temp-TU,
            "reine Strahlungsform, Koeffizient kalibriert":
                lambda temp: (temp+273.15)**4-(TU+273.15)**4,
            "Formtest (T-Tu)*exp(0,02*(T-60)), keine Stoffwertprognose":
                lambda temp: (temp-TU)*exp(0.02*(temp-60.0)),
            "Formtest (T-Tu)*exp(0,05*(T-60)), keine Stoffwertprognose":
                lambda temp: (temp-TU)*exp(0.05*(temp-60.0)),
        }
        for label, shape in shapes.items():
            early, late, gap = nonlinear(shape, cup=cup)
            print(f"{label}: T1={early:.6f} °C; T2={late:.6f} °C; Gap={gap:.6f} K")
            assert gap > 0

    print("\nModellgrenzen und mathematische Kontrolle:")
    print("Ein gemeinsames monoton wachsendes Verlustgesetz q(T) kann bei "
          "kalter Milch die Reihenfolge nicht allein umdrehen, solange der "
          "reine Kaffee wärmer als die Milch bleibt: Sei F(t) die frühe "
          "Mischtemperatur und G(t) die hypothetische späte Mischung zum "
          "Zeitpunkt t. An jedem Kontakt F=G ist "
          "(F-G)'=[q(T_rein)-q(G)]/(C_K+C_B+C_M)>0.")
    print("Bei tatsächlicher Verdunstung können Masse, Gleichgewichtstemperatur "
          "und q(T) zwischen Kaffee und Milchkaffee abweichen. Diese Effekte "
          "sind mit einem Messpunkt nicht identifizierbar.")
    print("Kein Zahlenwert für Biot aus dem Material bestimmbar: Geometrie, "
          "Wärmeleitfähigkeit und interner Wärmeübergang fehlen. Für Flüssigkeit "
          "ist eine Aussage über Durchmischung/Zirkulation erforderlich; "
          "kA ist kein separat gemessener lokaler Wärmeübergangskoeffizient.")


if __name__ == "__main__":
    main()
