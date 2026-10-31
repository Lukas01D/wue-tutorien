#!/usr/bin/env python3
"""Eigenständige Herleitung aus Aufgabe a bis g, vor Einsicht ins HTML-Modell.

Aus Folie 8: dU/dt = -Q_ab, mit U=C*T und Q_ab=kA*(T-Tu).
Trennen: dT/(T-Tu)=-(kA/C)dt; integrieren von 0 bis t:
ln((T-Tu)/(T0-Tu))=-kA*t/C. Dies liefert die Abkühlfunktion.
Mischung ohne Wärmeverlust: C_KB*T_K + C_M*T_M = C_ges*T_mix.
Aus der Messung: kA= -C_KB/600*ln((T10-Tu)/(T0-Tu)).
Der Becher hat vor der Mischung ebenfalls T_K: C_KB=C_K+C_B.
Wärmeabgabe wird aus Anfangsenergie plus zugeführter Milchenergie
minus Endenergie berechnet, nicht durch Kopieren einer Q-Formel des Tools.
Der erste Kurvenschnitt vor Zugabe wird durch Bisektion bestimmt.
Dieses Skript importiert weder das Referenzmodell noch den HTML-Modellteil.
"""
import math


def rechnen(*, kaffee_ml=200, milch_ml=30, start=80, milch=5,
            raum=20, messung10=67, zugabe_min=60, becher=False,
            ka_faktor=1, becher_g=300, milch2_raum=False):
    c_k = kaffee_ml * 1e-6 * 1000 * 4180
    c_m = milch_ml * 1e-6 * 1030 * 3940
    c_b = becher_g / 1000 * 850 if becher else 0
    c_s = c_k + c_b
    c_g = c_s + c_m
    ka = -c_s / 600 * math.log((messung10 - raum)/(start - raum))
    gemischt = (c_s * start + c_m * milch) / c_g

    def abkuehlen(t0, c, sekunden):
        return raum + (t0 - raum) * math.exp(-ka * sekunden / c)

    def schwarz(minuten):
        return abkuehlen(start, c_s, minuten * 60)

    def tasse1(minuten):
        return abkuehlen(gemischt, c_g, minuten * 60 * ka_faktor)

    def tasse2(minuten, nach_zugabe=True):
        if minuten < zugabe_min or not nach_zugabe:
            return schwarz(minuten)
        milch_spaet = raum if milch2_raum else milch
        beim_zuguss = (c_s * schwarz(zugabe_min) + c_m * milch_spaet) / c_g
        return abkuehlen(beim_zuguss, c_g, (minuten-zugabe_min)*60)

    end1 = tasse1(zugabe_min)
    end2 = tasse2(zugabe_min)
    anfangsenergie = c_s * start + c_m * milch
    q1 = (anfangsenergie - c_g * end1)/1000
    anfangsenergie2 = c_s * start + c_m * (raum if milch2_raum else milch)
    q2 = (anfangsenergie2 - c_g * end2)/1000

    def diff(t):
        # Gemeinsamen positiven Exponentialfaktor kürzen, damit nahe der
        # Raumtemperatur kein falscher Schnitt durch Auslöschung entsteht.
        r_black=ka/c_s*60
        r_mix=ka*ka_faktor/c_g*60
        r_min=min(r_black,r_mix)
        return ((start-raum)*math.exp(-(r_black-r_min)*t)
                -(gemischt-raum)*math.exp(-(r_mix-r_min)*t))

    # Keine algebraische Schnittpunktformel des Prüflings verwenden.
    schnitt = None
    if ka > 0:
        links, rechts = 0.0, 1.0
        if abs(diff(0)) < 1e-12:
            schnitt = 0.0
        else:
            while rechts < 1e6 and diff(links)*diff(rechts) > 0:
                rechts *= 2
            if rechts < 1e6 and diff(links)*diff(rechts) <= 0:
                for _ in range(90):
                    mitte = (links+rechts)/2
                    if diff(links)*diff(mitte) > 0:
                        links=mitte
                    else:
                        rechts=mitte
                schnitt=(links+rechts)/2
    return dict(c_k=c_k,c_m=c_m,c_b=c_b,c_s=c_s,c_g=c_g,ka=ka,
                gemischt=gemischt,end1=end1,end2=end2,differenz=end1-end2,
                q1=q1,q2=q2,schnitt=schnitt,
                tasse1=tasse1,tasse2=tasse2,schwarz=schwarz)


if __name__ == '__main__':
    r = rechnen()
    for k,v in r.items():
        if not callable(v):
            print(f'{k}: {v}')
