"""X6: eigene Rechnung aus Mischbilanz und C dtheta/dt = -kA(theta-theta_u).

Importiert weder das Referenzmodell noch die Seite. Ausgabe: eigene Sollwerte.
Aufruf im Repository: python simulation/x6_skripte/eigenrechnung.py
"""
import json
import math
import random
from pathlib import Path

HIER = Path(__file__).resolve().parent
KA = -(0.200 * 4180) / 600 * math.log((72 - 20) / (80 - 20))
BLATT = dict(thK0=80, thM=5, thU=20, VM_ml=30, kA=KA, tZ=60)


def temperatur(theta0, theta_u, C, kA, sekunden):
    return theta_u + (theta0 - theta_u) * math.exp(-kA * sekunden / C)


def rechnen(e):
    ck = 0.200 * 4180
    cm = e['VM_ml'] * 1e-6 * 1030 * 3940
    cg = ck + cm
    mix = lambda a, b: (ck * a + cm * b) / cg
    start = mix(e['thK0'], e['thM'])
    sekunden = e['tZ'] * 60
    a = temperatur(start, e['thU'], cg, e['kA'], sekunden)
    schwarz = temperatur(e['thK0'], e['thU'], ck, e['kA'], sekunden)
    b = mix(schwarz, e['thM'])
    schnitt = math.log((e['thK0'] - e['thU']) / (start - e['thU'])) / (e['kA'] / ck - e['kA'] / cg)
    kurven = [[temperatur(start, e['thU'], cg, e['kA'], t),
               temperatur(e['thK0'], e['thU'], ck, e['kA'], t)]
              for t in [0, 60, 600, 1800, 3600, sekunden]]
    return dict(kA=e['kA'], C_K=ck, C_G=cg, a_K=e['kA']/ck, a_G=e['kA']/cg,
                th_mess=temperatur(e['thK0'], e['thU'], ck, e['kA'], 600),
                th10=start, th1=a, th2K=schwarz, th2=b, dT=a-b,
                Q1=cg*(start-a), Q2=ck*(e['thK0']-schwarz), t_schnitt=schnitt,
                kurven=kurven)


def nullstelle(f, lo, hi):
    for _ in range(100):
        mitte = (lo + hi) / 2
        if f(mitte) > 0:
            lo = mitte
        else:
            hi = mitte
    return (lo + hi) / 2


def main():
    faelle = [('Blatt', BLATT), ('Milch_70', dict(BLATT, thM=70)), ('Raummilch', dict(BLATT, thM=20))]
    grenzen = {'thM': (2, 30, 80), 'tZ': (1, 180), 'thK0': (60, 95),
               'thU': (10, 30), 'kA': (0.05, 0.8), 'VM_ml': (10, 100)}
    for k, werte in grenzen.items():
        for x in werte:
            faelle.append((f'{k}={x}', dict(BLATT, **{k: x})))
    faelle += [('alles_unten', dict(thM=2, tZ=1, thK0=60, thU=10, kA=.05, VM_ml=10)),
               ('alles_oben', dict(thM=80, tZ=180, thK0=95, thU=30, kA=.8, VM_ml=100))]
    rng = random.Random(7112)
    for i in range(15):
        faelle.append((f'eigener_Fall_{i+1}', {k: rng.uniform(min(v), max(v)) for k, v in grenzen.items()}))
    r = rechnen(BLATT)
    kipp = {str(t): nullstelle(lambda m: rechnen(dict(BLATT, thM=m, tZ=t))['dT'], 2, 95)
            for t in [30, 60, 90]}
    maximum = rechnen(dict(BLATT, tZ=r['t_schnitt']/60))
    zusatz = dict(kipp=kipp, warm70=rechnen(dict(BLATT, thM=70)),
                  raummilch=rechnen(dict(BLATT, thM=20)),
                  maximum_min=r['t_schnitt']/60, maximum_K=maximum['dT'],
                  grenz_K=(r['C_G']-r['C_K'])/r['C_G']*(20-5),
                  trink_min=r['C_G']/KA*math.log((r['th10']-20)/(60-20))/60,
                  sprung1=80-r['th10'], sprung2=r['th2K']-r['th2'],
                  dQ_kJ=(r['Q2']-r['Q1'])/1000)
    daten = dict(herleitung='Mischbilanz; theta-u=(theta0-u) exp(-kA*t/C); Q=C*(theta0-theta)',
                 faelle=[dict(name=n, eingabe=e, soll=rechnen(e)) for n,e in faelle], zusatz=zusatz)
    (HIER/'eigenrechnung.json').write_text(json.dumps(daten, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(dict(anzahl=len(faelle), blatt=r, zusatz=zusatz), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
