"""Kompakte Auswertung eigener Läufe, ohne die alten Rohdaten umzuschreiben."""
import collections
import hashlib
import importlib.metadata
import json
import subprocess
import sys
from pathlib import Path

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[1]


def read(name):
    return json.loads((OUT/name).read_text())


def main():
    a=read('ergebnis_a.json'); b=read('ergebnis_b.json')
    l=read('ergebnis_layout.json'); e=read('ergebnis_ergaenzung.json')
    n=read('ergebnis_nachpruefung.json'); ui=read('ergebnis_bedienung.json')
    identity=next(t['detail'] for t in n['tests'] if t['name']=='Identitaet_MODELL')
    originals={}
    for name in ['pruefung_a.py','pruefung_b.py','pruefung_layout.py','pruefung_ergaenzung.py']:
        old=(ROOT/'simulation/x5_skripte'/name).read_bytes()
        new=(OUT/name).read_bytes()
        assert old==new,name
        originals[name]=hashlib.sha256(new).hexdigest()
    layouts=l['layouts']
    status=collections.Counter(t['status'] for t in b['tests'])
    stale=[dict(width=r['width'],height=r['height'],phase=r['phase'],lang=r['lang'],ratio=r['diagram']['holderRatio'])
           for r in layouts if r['diagram']['anheften'] and r['diagram']['holderRatio']>.451]
    summary=dict(
        date='2026-11-06',branch='codex/x5-nachpruefung',
        reviewed_commit='34bdfa6e996010ebfb9073b8062aa3eb72434cda',
        source_commit=subprocess.check_output(['git','log','-1','--format=%H','--','simulation/site/index.html'],cwd=ROOT,text=True).strip(),
        identity=identity,script_sha256=originals,
        python=sys.version.split()[0],node=subprocess.check_output(['node','--version'],text=True).strip(),
        playwright=importlib.metadata.version('playwright'),fontTools=importlib.metadata.version('fontTools'),
        brotli='1.2.1 (in /tmp/x5-python)',axe='4.11.0',browser=b['browser'],
        a=dict(cases=a['cases'],comparisons=a['comparisons'],max_abs_error=a['max_abs_error'],
               errors=len(a['errors']),textchecks=len(a['textchecks']),text_failures=sum(not t['ok'] for t in a['textchecks']),
               metadata_note='commit in ergebnis_a.json ist im unveränderten Alt-Skript fest auf da7deb1 gesetzt; geprüfter Stand siehe reviewed_commit und Identitätsprüfung.'),
        b=dict(counts=dict(status),exceptions=[dict(name=t['name'],status=t['status']) for t in b['tests'] if t['status']!='PASS']),
        layout=dict(count=len(layouts),overflow=sum(r['scrollWidth']>r['width'] for r in layouts),
                    focus_covered=len(l['focus']),small_targets=sum(len(r['smallTargets']) for r in layouts),
                    unnamed_intersections=sum(r['circle'] and not r['label'] for r in l['labels']),
                    transient_over_45_percent=stale,minimum_font=min(t['size'] for r in layouts for t in r['diagram']['texts'])),
        graphics=dict(points=sum(r['points'] for r in e['graphics']),max_error_svg=max(r['max_error_svg'] for r in e['graphics'])),
        extra_focus_covered=len(e['focus_768_1024_32px']),
        supplementary=dict(count=len(n['tests']),counts=dict(collections.Counter(t['status'] for t in n['tests']))),
        interaction=dict(count=len(ui),counts=dict(collections.Counter(t['status'] for t in ui))),
        file_probe=read('file_probe.json'))
    (OUT/'auswertung.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    assert not a['errors'] and all(t['ok'] for t in a['textchecks'])
    assert status=={'PASS':19,'ERROR':1}
    assert summary['b']['exceptions']==[{'name':'Quellenwechsel_haelt_Kurven_bei_kA1','status':'ERROR'}]
    assert not any(summary['layout'][k] for k in ['overflow','focus_covered','small_targets','unnamed_intersections'])
    assert summary['extra_focus_covered']==0
    assert all(t['status']=='PASS' for t in n['tests']+ui)
    print(json.dumps(summary,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
