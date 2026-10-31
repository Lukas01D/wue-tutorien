#!/usr/bin/env python3
"""Eigene Nachrechnung der Aussagen zu Zeitpunkt, Milch und Becher.

Verwendet ausschließlich das unabhängige Gleichungsskript, keine Hinweise,
kein Referenzmodell, keinen HTML-Modellcode. Maximaler Unterschied wird
numerisch durch Intervallschachtelung gesucht; Gleichstand per Bisektion.
"""
from pathlib import Path
import json
from rechnung_unabhaengig import rechnen

HERE=Path(__file__).resolve().parent


def maximum(f, lo, hi):
    ratio=(5**.5-1)/2
    a=hi-ratio*(hi-lo)
    b=lo+ratio*(hi-lo)
    for _ in range(150):
        if f(a)<f(b):
            lo=a
            a=b
            b=lo+ratio*(hi-lo)
        else:
            hi=b
            b=a
            a=hi-ratio*(hi-lo)
    t=(hi+lo)/2
    return t,f(t)


def milch_gleich(zeit):
    lo,hi=-50,150
    for _ in range(100):
        mid=(lo+hi)/2
        if rechnen(zugabe_min=zeit,milch=mid)['differenz']>0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def main():
    r=rechnen()
    tmax,dmax=maximum(lambda t:rechnen(zugabe_min=t)['differenz'],1,120)
    # Schwarzer Kaffee nähert sich vor Zugabe Tu, danach kommt frische Milch
    # hinzu. Energiebilanz ohne Grenzwert der Exponentialterme aus dem Tool.
    t2_inf=(r['c_s']*20+r['c_m']*5)/r['c_g']
    result=dict(maximum_zeit_min=tmax,maximum_differenz_K=dmax,
                schwarzer_schnitt_min=r['schnitt'],
                limit_t1_C=20,limit_t2_nach_zugabe_C=t2_inf,
                limit_differenz_K=20-t2_inf,
                gleichstand_milch_C={str(t):milch_gleich(t) for t in [30,60,90]},
                probe_grosse_zeiten={str(t):{
                  k:v for k,v in rechnen(zugabe_min=t).items()
                  if k in ('end1','end2','differenz')}
                    for t in [120,240,1000,10000]},
                bechervergleich={str(b):{
                  k:v for k,v in rechnen(becher=b).items()
                  if k in ('end1','end2','differenz','q1','q2','ka')}
                    for b in [False,True]})
    text=json.dumps(result,indent=2,ensure_ascii=False)+'\n'
    (HERE/'rechnung_zusatz_ergebnis.json').write_text(text)
    print(text)


if __name__=='__main__':main()
