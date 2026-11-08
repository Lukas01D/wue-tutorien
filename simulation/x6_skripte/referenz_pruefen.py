"""Separater Vergleich der eigenen Rechnung mit dem unveränderten Referenzmodell."""
import json
import sys
from pathlib import Path
HIER=Path(__file__).resolve().parent
sys.path.insert(0,str(HIER.parent/'modell'))
import kaffee_modell as ref
import werte
d=json.loads((HIER/'eigenrechnung.json').read_text())
mapping={'th10':'T1_0','th1':'T1','th2K':'T2_K','th2':'T2'}
fehler=[]
max_rel=0
anzahl=0
for fall in d['faelle']:
    e=fall['eingabe']
    ck=.2*4180
    p=dict(ref.P,th_K0=e['thK0'],th_M=e['thM'],th_U=e['thU'],V_M=e['VM_ml']*1e-6,
           t_end=e['tZ']*60,th_mess=e['thU']+(e['thK0']-e['thU'])*__import__('math').exp(-e['kA']*600/ck))
    r=ref.rechne(p)
    for k, soll in fall['soll'].items():
        if k=='kurven': continue
        name=mapping.get(k,k)
        ist=(r[name]-273.15) if k in mapping else r[name]
        # Bei exakt null ist ein relativer Fehler undefiniert. 1 s als Bezugsmaß
        # verhindert, dass Kelvin/Celsius-Rundung von 2.93e-11 s als Fehler gilt.
        nenner=1.0 if k=='t_schnitt' and abs(soll)<1e-6 else max(abs(soll),1e-12)
        rel=abs(soll-ist)/nenner
        max_rel=max(max_rel,rel); anzahl+=1
        if rel>=1e-9: fehler.append(dict(fall=fall['name'],feld=k,soll=soll,ist=ist,rel=rel))
standard=dict(thK0=werte.KAFFEE_START,thM=werte.MILCH_KALT,thU=werte.RAUM,VK_ml=werte.V_KAFFEE*1e6,
              VM_ml=werte.V_MILCH*1e6,thMess=werte.MESSWERT,tZ=60,thMh=werte.MILCH_HEISS,trink=werte.TRINK)
html_standard=json.loads((HIER/'zahlen_ergebnis.json').read_text())['standard']
assert standard==html_standard,(standard,html_standard)
out=dict(faelle=len(d['faelle']),vergleiche=anzahl,maxRel=max_rel,fehler=fehler,standard_gegen_werte_py=True)
(HIER/'referenz_ergebnis.json').write_text(json.dumps(out,indent=2)+'\n')
print(out)
assert not fehler
