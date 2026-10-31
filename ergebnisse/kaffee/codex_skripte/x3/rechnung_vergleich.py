#!/usr/bin/env python3
"""Eigene Sollwerte gegen den extrahierten Modellteil des HTML-Werkzeugs.

Aufruf vom Repository: python ergebnisse/kaffee/codex_skripte/x3/rechnung_vergleich.py
Benötigt Python und Node. Vorhandene Projekt-Tests werden nicht verwendet.
"""
import json
from pathlib import Path
import subprocess
from rechnung_unabhaengig import rechnen

HERE=Path(__file__).resolve().parent
STANDARD=dict(tEnd_min=60,thM=5,milch2Raum=False,VM_ml=30,thU=20,
              becher=False,thK0=80,thMess=67,VK_ml=200,kA1Faktor=1,mB_g=300)
CASES=[
 ('standard',{}),('f_milch60',dict(thM=60)),('g_becher',dict(becher=True)),
 ('zeit_min',dict(tEnd_min=1)),('zeit_max',dict(tEnd_min=120)),
 ('milch_temp_min',dict(thM=2)),('milch_temp_max',dict(thM=65)),
 ('milch_menge_min',dict(VM_ml=5)),('milch_menge_max',dict(VM_ml=100)),
 ('raum_min',dict(thU=10)),('raum_max',dict(thU=30)),
 ('kaffee_start_min',dict(thK0=60,thMess=50)),
 ('kaffee_start_max',dict(thK0=95)),
 ('mess_min',dict(thMess=30)),('mess_max',dict(thK0=95,thMess=90)),
 ('kaffee_menge_min',dict(VK_ml=100)),('kaffee_menge_max',dict(VK_ml=400)),
 ('faktor_min',dict(kA1Faktor=.9)),('faktor_max',dict(kA1Faktor=1.1)),
 ('becher_masse_min',dict(becher=True,mB_g=100)),
 ('becher_masse_max',dict(becher=True,mB_g=600)),
 ('milch2_raum',dict(milch2Raum=True,tEnd_min=40,becher=True)),
 ('kombiniert_klein',dict(tEnd_min=1,thM=2,VM_ml=5,thU=10,becher=True,thK0=60,thMess=30,VK_ml=100,kA1Faktor=.9,mB_g=100)),
 ('kombiniert_gross',dict(tEnd_min=120,thM=65,VM_ml=100,thU=30,becher=True,thK0=95,thMess=90,VK_ml=400,kA1Faktor=1.1,mB_g=600)),
 ('umgekehrter_schnitt',dict(tEnd_min=60,thK0=60,thM=65,thMess=50,VM_ml=5,kA1Faktor=1.1)),
 ('kein_schnitt',dict(VM_ml=5,VK_ml=400,kA1Faktor=1.1)),
 ('milch_raum',dict(thM=20)),
 ('selbst30',dict(tEnd_min=30,thM=12.5,thU=22.5,VM_ml=45,VK_ml=250,thK0=85.5,thMess=66.5,becher=True,mB_g=430,kA1Faktor=.97)),
 ('selbst90',dict(tEnd_min=90,thM=38.5,thU=15.5,VM_ml=65,VK_ml=170,thK0=74.5,thMess=55,becher=True,mB_g=240,kA1Faktor=1.04)),
]


def main():
    inputs=[]
    oracles=[]
    for name,override in CASES:
        e=STANDARD|override
        r=rechnen(kaffee_ml=e['VK_ml'],milch_ml=e['VM_ml'],start=e['thK0'],
                  milch=e['thM'],raum=e['thU'],messung10=e['thMess'],
                  zugabe_min=e['tEnd_min'],becher=e['becher'],
                  ka_faktor=e['kA1Faktor'],becher_g=e['mB_g'],
                  milch2_raum=e['milch2Raum'])
        times=[e['tEnd_min']*i/160 for i in range(161)]
        inputs.append(dict(name=name,settings=e,times=times))
        oracles.append(r)
    proc=subprocess.run(['node',str(HERE/'rechnung_tool_modell.js')],
                        input=json.dumps(inputs),text=True,capture_output=True,check=True)
    actual=json.loads(proc.stdout)
    rows=[]
    failures=[]
    max_error={}
    for item,r,m in zip(inputs,oracles,actual):
        name=item['name']
        expected=dict(kA=r['ka'],T1_0=r['gemischt']+273.15,
                      T1=r['end1']+273.15,T2=r['end2']+273.15,
                      T2_K=r['schwarz'](item['settings']['tEnd_min'])+273.15,
                      th1=r['end1'],th2=r['end2'],dT=r['differenz'],
                      Q1=r['q1']*1000,Q2=r['q2']*1000)
        deltas={k:abs(m[k]-v) for k,v in expected.items()}
        for k,d in deltas.items():
            max_error[k]=max(max_error.get(k,0),d)
            if d>1e-8:
                failures.append(dict(case=name,key=k,expected=expected[k],actual=m[k],delta=d))
        for key,fun in [('kurve1',r['tasse1']),('kurve2',r['schwarz'])]:
            error=max(abs(a-fun(t)) for a,t in zip(m[key],item['times']))
            max_error[key]=max(max_error.get(key,0),error)
            if error>1e-8:
                failures.append(dict(case=name,key=key,max_error=error))
        expected_cross=r['schnitt']
        actual_cross=m['t_schnitt']/60 if m['t_schnitt'] is not None else None
        if (expected_cross is not None and expected_cross>0 and
            (actual_cross is None or abs(actual_cross-expected_cross)>1e-7)):
            failures.append(dict(case=name,key='t_schnitt_min',expected=expected_cross,actual=actual_cross))
        rows.append(dict(name=name,settings=item['settings'],expected=expected,
                         errors=deltas,expected_cross_min=expected_cross,
                         actual_cross_min=actual_cross,
                         expected_curves=dict(times=item['times'],
                           tasse1=[r['tasse1'](t) for t in item['times']],
                           schwarz=[r['schwarz'](t) for t in item['times']]),
                         actual=m))
    result=dict(cases=len(rows),curve_points_per_curve=161,max_error=max_error,
                failures=failures,results=rows)
    (HERE/'rechnung_ergebnis.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    lines=[f'Parametersätze: {len(rows)}',
           f'Kurvenwerte: {len(rows)*161*2} (beide Kurven, jeweils 161 Punkte bis vor die Zugabe)',
           'Mischsprung: T2_K vor Zugabe und T2 nach Zugabe in jedem Parametersatz verglichen.',
           'Maximale absolute Abweichungen: '+json.dumps(max_error,ensure_ascii=False),
           'Befunde: '+json.dumps(failures,ensure_ascii=False)]
    for row in rows:
        e=row['expected']
        lines.append(f"{row['name']}: T1={e['th1']:.9f} °C, T2={e['th2']:.9f} °C, dT={e['dT']:.9f} K, Q1={e['Q1']/1000:.9f} kJ, Q2={e['Q2']/1000:.9f} kJ, kA={e['kA']:.9f} W/K, Schnitt Soll/Ist={row['expected_cross_min']}/{row['actual_cross_min']} min")
    text='\n'.join(lines)+'\n'
    (HERE/'rechnung_ergebnis.txt').write_text(text)
    print(text)


if __name__=='__main__':
    main()
