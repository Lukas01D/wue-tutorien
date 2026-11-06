"""X5, eigene Bilanzrechnung, ohne Import der Projektmodelle.

Aufruf aus dem Repository: python3 simulation/x5_skripte/pruefung_a.py
Python 3, Playwright und Chromium unter /usr/bin/chromium erforderlich.
Der lokale HTTP-Server auf Port 8765 muss das Repository ausliefern.
Toleranzen vor Auswertung: 1e-8 absolut, 1e-9 relativ (K, kJ, W/K, min).
"""
import json
import math
import random
import re
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
URL = 'http://127.0.0.1:8765/simulation/site/index.html'
KA = -836 / 600 * math.log(47 / 60)
STD = dict(VK_ml=200, VM_ml=30, thK0=80, thM=5, thU=20, thMess=67,
           tEnd_min=60, becher=False, mB_g=300, milch2Raum=False,
           kAQuelle='fest', kA=KA, kA1Faktor=1)


def own(e):
    # dE/dt = -kA(theta-theta_u), E = C(theta-theta_u).
    ck = e['VK_ml'] * 4.18
    cm = e['VM_ml'] * 1.03 * 3.940
    cb = e['mB_g'] * .850 if e['becher'] else 0
    b, g = ck + cb, ck + cb + cm
    u, k0, milk = e['thU'], e['thK0'], e['thM']
    ka = e['kA'] if e['kAQuelle'] == 'fest' else -b / 600 * math.log((e['thMess']-u)/(k0-u))
    f, sec = e['kA1Faktor'], e['tEnd_min'] * 60
    mix = (b*k0 + cm*milk)/g
    t1 = lambda seconds: u + (mix-u)*math.exp(-f*ka*seconds/g)
    t2 = lambda seconds: u + (k0-u)*math.exp(-ka*seconds/b)
    m2 = u if e['milch2Raum'] else milk
    after = (b*t2(sec)+cm*m2)/g
    cross = lambda ratio: math.log(ratio)/(ka/b-f*ka/g)/60 if ratio > 0 and ka/b != f*ka/g else math.inf
    ts, tq = cross((k0-u)/(mix-u)), cross((k0-u)/(f*(mix-u)))
    ts = ts if ts > 0 else math.inf
    tq = tq if tq > 0 else math.inf
    dq = lambda seconds: (b*(k0-t2(seconds))-g*(mix-t1(seconds)))/1000
    split = min(sec, tq*60)
    q1, q2 = g*(mix-t1(sec))/1000, b*(k0-t2(sec))/1000
    return dict(kA=ka, th10=mix, th1=t1(sec), th2=after, th2K=t2(sec),
                th2Raum=(b*t2(sec)+cm*u)/g, dT=t1(sec)-after, Q1=q1, Q2=q2,
                milch=cm*(milk-m2)/1000, energieRest=0,
                tSchnitt=ts, tWaermestrom=tq, flaecheVor=dq(split), flaecheNach=dq(sec)-dq(split),
                schwarz30=t2(1800), tauMin=b/ka/60, C_K=ck, C_M=cm, C_B=cb, C_KB=b, C_GB=g,
                kurve1=[t1(t*60) for t in (0,1,10,30,55.7,60,120,180)],
                kurve2=[t2(t*60) for t in (0,1,10,30,55.7,60,120,180)],
                qdot1=[f*ka*(t1(t*60)-u) for t in (0,1,10,30,55.7,60,120,180)],
                qdot2=[ka*(t2(t*60)-u) for t in (0,1,10,30,55.7,60,120,180)])


def max_own(e):
    # Unabhängige numerische Maximierung über t_Z, keine Schnittformel.
    lo, hi = 0., 20000.
    for _ in range(150):
        a, b = (2*lo+hi)/3, (lo+2*hi)/3
        if own(dict(e,tEnd_min=a))['dT'] < own(dict(e,tEnd_min=b))['dT']:
            lo = a
        else:
            hi = b
    t = (lo+hi)/2
    return dict(t_min=t,dT_max=own(dict(e,tEnd_min=t))['dT'])


def milk_equal(t):
    lo, hi = 0., 100.
    for _ in range(80):
        mid = (lo+hi)/2
        if own(dict(STD,tEnd_min=t,thM=mid))['dT'] > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def formatted(v,n,lang):
    s = f'{v:.{n}f}'
    return (s.replace('.',',') if lang == 'de' else s).replace('-', '−')


def main():
    cases = [('standard',STD)]
    for key, vals in dict(VK_ml=[100,400],VM_ml=[5,100],thK0=[60,95],thM=[2,60,65],
                          thU=[10,30],tEnd_min=[1,53,56,59,120,180],kA=[.05,1],
                          kA1Faktor=[.9,1.05,1.1],mB_g=[100,600]).items():
        for v in vals:
            case=dict(STD,**{key:v})
            if key=='mB_g':case['becher']=True
            cases.append((f'{key}={v}',case))
    cases += [('becher_messung',dict(STD,becher=True,kAQuelle='messung')),
              ('milch2raum',dict(STD,milch2Raum=True)),
              ('300ml50ml',dict(STD,VK_ml=300,VM_ml=50,thK0=90,thM=10,thU=25,kA=.25))]
    cases += [('messwert30',dict(STD,thU=10,thK0=60,thMess=30,kAQuelle='messung',becher=True)),
              ('messwert90',dict(STD,thK0=95,thMess=90,kAQuelle='messung'))]
    for factor in [1,.56,1,1,.9,.44]:
        cases.append((f'voreinstellung_{factor}',dict(STD,kA=KA*factor)))
    for key, vals in dict(VK_ml=[100,400],thK0=[95],thU=[10,30]).items():
        for v in vals:
            cases.append((f'messung_{key}={v}',dict(STD,kAQuelle='messung',**{key:v})))
    rnd = random.Random(20261106)
    for i in range(400):
        u = rnd.uniform(10,30)
        k = rnd.uniform(60,95)
        cases.append((f'zufall{i}',dict(STD,VK_ml=rnd.uniform(100,400),VM_ml=rnd.uniform(5,100),
            thK0=k,thU=u,thM=rnd.uniform(2,65),thMess=rnd.uniform(u+.1,k-.1),
            becher=rnd.choice([True,False]),mB_g=rnd.uniform(100,600),
            kA=rnd.uniform(.05,1),kAQuelle=rnd.choice(['fest','messung']),
            milch2Raum=rnd.choice([True,False]),kA1Faktor=rnd.uniform(.9,1.1),tEnd_min=rnd.uniform(1,180))))
    results, errors, maxima = [], [], []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
        page = b.new_page()
        page.goto(URL)
        actuals = page.evaluate('''es => es.map(e => { const r=ERW.auswerten(e);
          for(const k of ['kurve1','kurve2','qdot1','qdot2']) r[k]=[0,1,10,30,55.7,60,120,180].map(t=>r[k](t));
          return r; })''',[e for _,e in cases])
        count = 0
        worst = 0
        for (name,e),actual in zip(cases,actuals):
            expected = own(e)
            for key,val in expected.items():
                pairs = zip(val,actual[key]) if isinstance(val,list) else [(val,actual[key])]
                for v,a in pairs:
                    count += 1
                    if math.isinf(v) and a is None:
                        continue
                    delta = abs(v-a)
                    worst = max(worst, delta)
                    if not math.isclose(v,a,abs_tol=1e-8,rel_tol=1e-9):
                        errors.append(dict(case=name,key=key,expected=v,actual=a))
            if not name.startswith('zufall'):
                results.append(dict(case=name,e=e,own=expected,page=actual))
        for cup in [False,True]:
            for factor in [.05/KA,.44,.56,1,1/KA]:
                e = dict(STD,becher=cup,kA=KA*factor)
                a = page.evaluate('e=>ERW.groessterUnterschied(e)',e)
                v = max_own(e)
                assert abs(a['dT_max']-v['dT_max']) < 1e-9
                assert abs(a['t_min']-v['t_min']) < 3e-4
                maxima.append(dict(becher=cup,kA=e['kA'],own=v,page=a))
        # Alle modellabhängigen Zahlentokens in Start, F1, F2, V1 bis V5.
        r = own(STD)
        rb = own(dict(STD,becher=True,kAQuelle='messung'))
        md, ml = max_own(STD), max_own(dict(STD,kA=KA*.56))
        def plateau(e):
            top = formatted(max_own(e)['dT_max'],2,'en')
            ts = [t for t in range(1,181) if formatted(own(dict(e,tEnd_min=t))['dT'],2,'en') == top]
            return min(ts),max(ts)
        v,bis = plateau(STD)
        vd,bd = plateau(dict(STD,kA=KA*.56))
        limit = r['C_M']*15/r['C_GB']
        vals = {key:(r[key],2) for key in ['th1','th2','dT','Q1','Q2']}
        vals.update(dQ=(r['Q2']-r['Q1'],2), CG=(r['C_GB'],1),
            f1_tmax=(md['t_min'],0), dTmax=(md['dT_max'],2), f1_von=(v,0),f1_bis=(bis,0),
            grenz=(limit,2),grenz_th2=(20-limit,2),v2_tmax=(ml['t_min'],0),v2_von=(vd,0),v2_bis=(bd,0),
            v2_d60=(own(dict(STD,kA=KA*.56))['dT'],2),v3_dT=(rb['dT'],2),v3_Q1=(rb['Q1'],2),v3_Q2=(rb['Q2'],2),
            v4_d105=(own(dict(STD,kA1Faktor=1.05))['dT'],2),
            v4_d10=(math.ceil(max(abs(own(dict(STD,kA=KA*f))['dT']-r['dT']) for f in [.9,1.1])*100)/100,2),
            v5_thermo30=(own(dict(STD,kA=KA*.44))['schwarz30'],1),v5_keramik30=(r['schwarz30'],1),
            v5_thermo_t=(max_own(dict(STD,kA=KA*.44))['t_min'],0))
        for t in [30,60,90]: vals[f'v1_{t}'] = (milk_equal(t),1)
        textchecks = []
        for lang in ['de','en']:
            source = (ROOT/f'simulation/site/src/texte_{lang}.txt').read_text()
            parts = dict(re.findall(r'^@(\w+)\n(.*?)(?=^@|\Z)',source,re.M|re.S))
            for key in ['aufl_start','aufl_f1','aufl_f2']+[f'aufl_v{i}' for i in range(1,6)]:
                actual = page.evaluate('([l,k])=>TEXTE[l][k]',[lang,key])
                for token in re.findall(r'\{\{z:(\w+)\}\}',parts[key]):
                    value,places = vals[token]
                    expected = formatted(value,places,lang)
                    ok = expected in actual
                    textchecks.append(dict(lang=lang,key=key,token=token,expected=expected,ok=ok))
                    assert ok,(lang,key,token,expected,actual)
        # Gebaute Kann-Punkte: kalter Becher, Trinkzeit, unabhängige Fits.
        extras = []
        e = dict(STD,becher=True,kA=rb['kA'])
        a = page.evaluate('e=>({kalt:ERW.becherKalt(e),trinken:ERW.trinkzeit(e,60)})',e)
        ck,cm,cb,g = rb['C_K'],rb['C_M'],rb['C_B'],rb['C_GB']
        k0 = (ck*80+cb*20)/(ck+cb)
        mix = (ck*80+cm*5+cb*20)/g
        th1 = 20+(mix-20)*math.exp(-e['kA']*3600/g)
        thk = 20+(k0-20)*math.exp(-e['kA']*3600/(ck+cb))
        th2 = ((ck+cb)*thk+cm*5)/g
        for k,v in dict(th1_0=mix,thK_0=k0,th1=th1,th2=th2,dT=th1-th2).items(): assert abs(a['kalt'][k]-v)<1e-10
        for cup,factor in [(False,1),(False,.56),(True,rb['kA']/KA)]:
            e = dict(STD,becher=cup,kA=KA*factor)
            r0 = own(e)
            expected = dict(tasse1=r0['C_GB']/e['kA']*math.log((r0['th10']-20)/40)/60,
                            schwarz=r0['C_KB']/e['kA']*math.log(60/40)/60)
            actual = page.evaluate('e=>ERW.trinkzeit(e,60)',e)
            for k,v in expected.items(): assert abs(actual[k]-v)<1e-10
            extras.append(dict(e=e,own=expected,page=actual))
        for temps in [[67,56.82,48.84,42.59,37.70,33.86],[67.3,56.9,49.1,42.7,37.4,33.7]]:
            start = 80 if temps[0]==67 else 80.1
            xs,ys = [0]+[t*600 for t in range(1,7)], [0]+[math.log((t-20)/(start-20)) for t in temps]
            n=len(xs); mx=sum(xs)/n; my=sum(ys)/n
            b0=sum(x*y for x,y in zip(xs,ys))/sum(x*x for x in xs)
            b1=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sum((x-mx)**2 for x in xs)
            expected=dict(kA_ursprung=-836*b0,kA_frei=-836*b1,achsenabschnitt=my-b1*mx)
            actual=page.evaluate('([ps,t])=>ERW.ausgleich(ps,t,20,836)',[[[10*(i+1),t] for i,t in enumerate(temps)],start])
            for k,v in expected.items(): assert abs(actual[k]-v)<1e-12
            extras.append(dict(fit=temps,own=expected,page=actual))
        data = dict(commit='da7deb1bd897a69424964d0b20c93222697d4381',browser=b.version,
            seed=20261106,distribution='400 unabhängige gleichverteilte Sätze in den Reglerbereichen, Boolesche Größen zufällig',
            cases=len(cases),comparisons=count,max_abs_error=worst,errors=errors,
            fixed=results,maxima=maxima,textchecks=textchecks,extras=extras,cold_mug=a)
        (OUT/'ergebnis_a.json').write_text(json.dumps(data,indent=2,ensure_ascii=False,allow_nan=True)+'\n')
        print(json.dumps({k:data[k] for k in ['browser','cases','comparisons','max_abs_error','errors']},indent=2))
        print('Zahlentokens der Auflösungen:',len(textchecks))
        b.close()
    assert not errors


if __name__ == '__main__':
    main()
