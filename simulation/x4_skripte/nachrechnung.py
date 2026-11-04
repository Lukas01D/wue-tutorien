"""Unabhaengige X4-Rechnung, nur Standardbibliothek und Aufgabenwerte.

Keine Importe aus dem Referenzmodell oder den Recherche-Skripten.
Aufruf im Repository: python3 simulation/x4_skripte/nachrechnung.py
"""

import json
import math
import random
import statistics


CK = 0.0002 * 1000 * 4180
CM = 0.00003 * 1030 * 3940


def rechnen(cb=0, deckel=1, f1=1, tm=5, tm2=None, tz=60, tv=None,
            tk=80, tu=20, mess=67, ck=CK, cm=CM):
    """Mischbilanz und integrierte globale Energiebilanz, Zeit in min."""
    tm2 = tm if tm2 is None else tm2
    tv = tz if tv is None else tv
    c = ck + cb
    g = c + cm
    h = -c / 600 * math.log((mess - tu) / (tk - tu)) * deckel
    start = (c * tk + cm * tm) / g
    eins_z = tu + (start - tu) * math.exp(-f1 * h * tz * 60 / g)
    schwarz_z = tu + (tk - tu) * math.exp(-h * tz * 60 / c)
    zwei_z = (c * schwarz_z + cm * tm2) / g
    eins = tu + (eins_z - tu) * math.exp(-f1 * h * (tv - tz) * 60 / g)
    zwei = tu + (zwei_z - tu) * math.exp(-h * (tv - tz) * 60 / g)
    q1 = g * (start - eins_z)
    q2 = c * (tk - schwarz_z)
    assert abs(g * (eins_z - zwei_z) - (q2 - q1 + cm * (tm - tm2))) < 1e-8
    return dict(kA=h, misch=start, t1=eins, t2=zwei, delta=eins-zwei,
                schwarz=schwarz_z, q1_kJ=q1/1000, q2_kJ=q2/1000,
                energie_delta_K=(q2-q1)/g)


def maximum(cb=0, deckel=1):
    c, g = CK + cb, CK + cb + CM
    start = (c * 80 + CM * 5) / g
    h = -c / 600 * math.log(47/60) * deckel
    t = math.log(60/(start-20)) / (h * (1/c - 1/g)) / 60
    r = rechnen(cb=cb, deckel=deckel, tz=t)
    return dict(t_min=t, temperatur=r['schwarz'], delta=r['delta'])


def fit(temps, times, tu=20):
    y = [math.log((v-tu)/(temps[0]-tu)) for v in temps[1:]]
    ts = times[1:]
    ss = sum(t*t for t in ts)
    slope = sum(t*v for t,v in zip(ts,y))/ss
    resid = [v-slope*t for t,v in zip(ts,y)]
    se = CK * math.sqrt(sum(v*v for v in resid)/(len(ts)-1)/ss)
    return -CK*slope, se


def rk4(temp, seconds, c, h, tu):
    step = seconds / 2000
    f = lambda v: -h * (v-tu) / c
    for _ in range(2000):
        a = f(temp)
        b = f(temp+step*a/2)
        d = f(temp+step*b/2)
        e = f(temp+step*d)
        temp += step*(a+2*b+2*d+e)/6
    return temp


def pruefen():
    # Numerische Integration der Bilanz als zusaetzliche Kontrolle der Formel.
    rng = random.Random(20261104)
    largest = 0
    for _ in range(12):
        cb = rng.choice([0, 255, 331.7])
        tk, tu = rng.uniform(65,95), rng.uniform(10,28)
        tm, tm2 = rng.uniform(0,60), rng.uniform(0,60)
        mess = tu + rng.uniform(.55,.9)*(tk-tu)
        tz, f1 = rng.uniform(0,120), rng.uniform(.8,1.2)
        deckel = rng.choice([1,.56])
        r = rechnen(cb=cb,tk=tk,tu=tu,tm=tm,tm2=tm2,mess=mess,
                    tz=tz,f1=f1,deckel=deckel)
        c,g = CK+cb,CK+cb+CM
        n1 = rk4(r['misch'],tz*60,g,r['kA']*f1,tu)
        ns = rk4(tk,tz*60,c,r['kA'],tu)
        n2 = (c*ns+CM*tm2)/g
        largest = max(largest,abs(n1-r['t1']),abs(n2-r['t2']))
    assert largest < 1e-9
    cases = dict(standard=rechnen(),becher=rechnen(cb=255),
                 versuch=rechnen(cb=255,tz=40),deckel=rechnen(deckel=.56),
                 deckel_becher=rechnen(cb=255,deckel=.56),
                 trinken90=rechnen(tv=90),trinken120=rechnen(tv=120),
                 ungleich=rechnen(f1=1.05),milch2_raum=rechnen(tm2=20),
                 ungleich90=rechnen(f1=1.05,tv=90))
    # Analytische Milchtemperatur fuer gleiche Endtemperaturen.
    c,g = CK,CK+CM
    h = cases['standard']['kA']
    milk_equal = {}
    for tz in [30,60,90]:
        a,b = math.exp(-h*tz*60/g),math.exp(-h*tz*60/c)
        milk_equal[tz] = 20 + c*60*(a-b)/(CM*(1-a))
    # Gekruemmte Reihe aus Qdot = a * theta**1.25, am 10-min-Punkt geeicht.
    n = 1.25
    rate = (47**(1-n)-60**(1-n))/((n-1)*600)
    curved = [20+(60**(1-n)+(n-1)*rate*t*60)**(1/(1-n)) for t in [0,10,20,30,40]]
    curved_fit = fit(curved,[0,600,1200,1800,2400])
    nonlinear = lambda initial, t, c: 20 + ((initial-20)**(1-n) + (n-1)*rate*CK*t*60/c)**(1/(1-n))
    mixed = cases['standard']['misch']
    n1 = nonlinear(mixed,60,CK+CM)
    ns = nonlinear(80,60,CK)
    n2 = (CK*ns+CM*5)/(CK+CM)
    # T09 benutzt gerundete Temperaturen, kein exakt exponentieller Datensatz.
    rounded = [80,67,56.82,48.84,42.59,37.70,33.86]
    exact = [20+60*math.exp(-h*t*60/CK) for t in range(0,61,10)]
    noisy = [80.1,67.3,56.9,49.1,42.7,37.4,33.7]
    # Startmessfehler wirkt gemeinsam auf alle logarithmierten Werte.
    vals,ses = [],[]
    for _ in range(10000):
        samples = [v+rng.uniform(-.3,.3) for v in exact]
        val,se = fit(samples,list(range(0,3601,600)))
        vals.append(val)
        ses.append(se)
    k,cg = h,CK+CM
    # Bei ungleichem kA muessen die Unterschiede nach Zugabe nicht abklingen.
    r = cases['ungleich']
    crossing_after_z = math.log((r['t1']-20)/(r['t2']-20))*cg/(.05*k)/60
    out = dict(cases=cases, maxima={str((cb,d)):maximum(cb,d) for cb in [0,255] for d in [1,.56,.5,2]},
               milch_gleich_C=milk_equal,fit_gekruemmt=dict(temperaturen=curved,kA=curved_fit[0],
               mess_aequivalent=20+60*math.exp(-curved_fit[0]*600/CK)),
               fit_T09_gerundet=fit(rounded,list(range(0,3601,600))),
               fit_T10=fit(noisy,list(range(0,3601,600))),
               nichtlinear=dict(n=n,t1=n1,t2=n2,delta=n1-n2),
               monte_carlo=dict(reihen=10000,streuung_kA=statistics.stdev(vals),
                                mittlerer_formaler_SE=statistics.mean(ses)),
               ungleich_schnitt_nach_z_min=crossing_after_z,
               rk4=dict(parametersaetze=12,max_fehler_K=largest))
    print(json.dumps(out,indent=2,ensure_ascii=False))


if __name__ == '__main__':
    pruefen()
