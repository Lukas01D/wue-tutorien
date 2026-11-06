"""Kennzahlen aus den Ergebnisdateien der X5-Skripte (Codex), alt gegen neu.
Aufruf: python3 simulation/x5_regression/auswertung.py [ordner_mit_json]"""
import json, sys
from pathlib import Path
o = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent
L = json.loads((o/'ergebnis_layout.json').read_text())
E = json.loads((o/'ergebnis_ergaenzung.json').read_text())
B = json.loads((o/'ergebnis_b.json').read_text())
lay = L['layouts']
ueber = [(l['phase'], l['width'], l['lang'], l['scrollWidth']) for l in lay if l['scrollWidth'] > l['width']]
null = [(l['phase'], l['width'], l['lang'], len([s for s in l['tinyTargets'] if s['w'] == 0])) for l in lay if any(s['w'] == 0 for s in l['tinyTargets'])]
klein = [(l['phase'], l['width'], l['lang'], s['id'], s['w'], s['h']) for l in lay for s in l['smallTargets'] if s['w'] > 0]
anteil = [(l['phase'], l['width'], l['height'], l['lang'], round(l['diagram']['holderRatio'], 3)) for l in lay if l['diagram'].get('anheften') and l['diagram']['holderRatio'] > 0.45]
schrift = {}
for l in lay:
    if l['phase'] in ('P2', 'P4', 'VT') and l['diagram'].get('texts'):
        m = min(t['size'] for t in l['diagram']['texts'])
        k = (l['phase'], l['width'], l['height'])
        schrift[k] = round(min(m, schrift.get(k, 99)), 2)
schrift_klein = {k: v for k, v in schrift.items() if v < 9}
fokus = L['focus']
lab = L['labels']; ohne = [x for x in lab if x['circle'] and not x['label']]
print('X5-05 Ueberlauf (Zustaende mit scrollWidth > Breite):', len(ueber), ueber[:8])
print('X5-05 Regler mit Breite 0:', len(null), null[:6])
print('Ziele unter 24/44 px (ohne Breite 0):', len(klein), klein[:6])
print('X5-10 angeheftet > 45 %:', len(anteil), anteil[:8])
print('X5-09 kleinste Diagrammschrift < 9 px:', len(schrift_klein), sorted(schrift_klein.items())[:8])
print('X5-04 verdeckte Fokusmitten (Layoutlauf):', len([f for f in fokus if f.get('centerCovered')]))
fe = E.get('focus_768_1024_32px')
if isinstance(fe, dict):
    print('X5-04 768x1024 32 px:', {k: (v if not isinstance(v, list) else len(v)) for k, v in fe.items()})
elif isinstance(fe, list):
    print('X5-04 768x1024 32 px verdeckt:', len([f for f in fe if f.get('cover') or f.get('centerCovered')]))
print('X5-06 Schnittkreis ohne Beschriftung:', len(ohne), 'von', len([x for x in lab if x['circle']]))
print('X5-02 energy_formula:', json.dumps(E.get('energy_formula'), ensure_ascii=False)[:400])
print('X5-03 measured_replaced:', json.dumps(E.get('measured_replaced'), ensure_ascii=False)[:400])
print('Browserlauf B:', {t['status'] for t in B['tests']}, [t['name'] for t in B['tests'] if t['status'] != 'PASS'])
