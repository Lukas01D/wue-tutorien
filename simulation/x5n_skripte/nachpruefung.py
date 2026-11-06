"""Eigene Ergänzungen zu X5 Abschnitt 9. Keine Änderungen an der Seite.

Erwartungen aus TL-Entscheidungen und eigener Bilanzrechnung in pruefung_a.
Aufruf und Einschränkungen in README.md. JSON enthält auch fehlgeschlagene
Prüfungen; ein Fehler wird nicht als bestanden ausgegeben.
"""
import hashlib
import importlib.metadata
import json
import math
import re
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright
from pruefung_a import ROOT, OUT, URL, STD, own, milk_equal
from pruefung_b import start, f1, vt, state, result, commit_field, goto_question, course

RESULTS = []


def check(ok, evidence):
    if not ok:
        raise AssertionError(evidence)
    return evidence


def rects(page, selectors):
    return page.evaluate("""ss => Object.fromEntries(ss.map(s=>{
      const e=document.querySelector(s),r=e.getBoundingClientRect();
      return [s,{top:r.top,bottom:r.bottom,width:r.width,height:r.height,
      visible:!!e.getClientRects().length,inView:r.top>=-1&&r.bottom<=innerHeight+1}];}))""", selectors)


def model_provenance(page, context, lang):
    data = (ROOT/'simulation/site/index.html').read_bytes()
    other = (ROOT/'simulation/site/Kaffee_Simulation.html').read_bytes()
    # Markergrenzen wie beim ursprünglichen X5-Nachweis.
    block = re.search(rb'// MODELL-ANFANG[^\n]*\n.*?// MODELL-ENDE\n', data, re.S).group(0)
    digest = hashlib.sha256(block).hexdigest()
    return check(data == other and hashlib.sha256(data).hexdigest() ==
                 'e6f95ca27a5c508344e6802195e9ea62f07ad743694761198057da98e757cc1d'
                 and digest == 'b32e3f9db9f82b09bfc0e300388ffbef72f875cec65540da668d765389f97d24',
                 dict(artifact=hashlib.sha256(data).hexdigest(), model=digest))


def gates_and_q1(page, context, lang):
    evidence = {}
    start(page, wrong=True)
    page.locator('#knopf-aufl-start').click()
    before = page.locator('#aufl-start').inner_text()
    check(not re.search(r'\b56\s*min', before), before)
    check('wieder kleiner' not in page.locator('#frageleiste').inner_text()
          and 'smaller again' not in page.locator('#frageleiste').inner_text(), 'F4 before')
    for tab in ['modell', 'code']:
        page.locator('#tab-'+tab).click()
        page.locator('#panel-'+tab+' details').evaluate_all('es=>es.forEach(e=>e.open=true)')
        text = page.locator('#panel-'+tab).inner_text()
        check(not any(s in text for s in ['Links davon', 'To the left', 'Er wächst, solange',
                                         'It grows as long', '3,86', '3.86', '56 min']), text)
        evidence['before_'+tab] = text
    page.locator('#tab-versuche').click()
    f1(page)
    after = page.locator('[data-karte="start"]').text_content()
    check('56 min' in after, after)
    evidence.update(start_before=before, start_after=after)
    for tab in ['modell', 'code']:
        page.locator('#tab-'+tab).click()
        page.locator('#panel-'+tab+' details').evaluate_all('es=>es.forEach(e=>e.open=true)')
        evidence['after_'+tab] = page.locator('#panel-'+tab).inner_text()
    check(('Er wächst, solange' if lang == 'de' else 'grows') in evidence['after_code'], evidence['after_code'])
    return evidence


def source_change(page, context, lang):
    start(page); f1(page); vt(page)
    page.locator('[name="kaq"][value="messung"]').check()
    commit_field(page, '#z-thMess', '66.5')
    page.locator('[name="kaq"][value="fest"]').check()
    commit_field(page, '#z-kA', '0.25')
    before = result(page)
    page.locator('[name="kaq"][value="messung"]').check()
    e = state(page)['e']; after = result(page)
    check(e['thMessEigen'] == 66.5 and e['thMessErsatz'] and abs(before['dT']-after['dT']) < 1e-10, e)
    label = page.locator('#rl-thMess').inner_text()
    note = page.locator('#thmess-ersatz').inner_text()
    check(('berechnet' if lang == 'de' else 'calculated') in label + note, label + note)
    page.reload()
    check(state(page)['e']['thMessEigen'] == 66.5, state(page)['e'])
    page.locator('#knopf-eigene-messung').click()
    check(state(page)['e']['thMess'] == 66.5 and not state(page)['e']['thMessErsatz'], state(page)['e'])
    # Alte X5-03-Reproduktion, jetzt bewusst abgelehnter Quellenwechsel.
    page.locator('#knopf-standard').click()
    for key, val in [('VK','100'), ('thK0','60'), ('thU','10'), ('kA','1')]:
        commit_field(page, '#z-'+key, val)
    e0 = state(page)['e']; r0 = result(page)
    # click statt check: check erwartet ein bleibendes Häkchen, das laut
    # Entscheidung gerade verhindert werden muss.
    page.locator('[name="kaq"][value="messung"]').click()
    page.wait_for_timeout(400)
    msg = page.locator('#kaq-meldung').text_content()
    live = page.locator('#ansage').text_content()
    check(state(page)['e'] == e0 and result(page)['dT'] == r0['dT'] and
          page.locator('[name="kaq"][value="fest"]').is_checked() and msg and msg == live,
          dict(e=state(page)['e'],message=msg,live=live))
    fieldset = page.locator('[name="kaq"]').first.locator('xpath=ancestor::fieldset')
    check('kaq-meldung' in (fieldset.get_attribute('aria-describedby') or ''), 'missing association')
    return dict(saved=66.5, replacement=e['thMess'], label=label, note=note,
                rejected_value=r0['thMessModell'], message=msg, focus=page.evaluate('document.activeElement.value'))


def neutral_opening(page, context, lang):
    start(page); f1(page); vt(page)
    records = []
    for q in ['v1','v2','v3','v4','v5']:
        page.locator('#knopf-standard').click()
        if q == 'v1': commit_field(page, '#z-thM', '47')
        if q == 'v2': page.locator('[data-vor="keramik_deckel"]').click()
        if q == 'v3': page.locator('#s-becher').check()
        if q == 'v4': commit_field(page, '#z-kA1', '105')
        if q == 'v5': page.locator('[data-vor="thermo_offen"]').click()
        goto_question(page, q)
        e = state(page)['e']
        check(not state(page)['antworten'][q]['fest'] and not e['becher'] and
              e['thM'] == 5 and e['kA1Faktor'] == 1 and abs(result(page)['dT']-own(STD)['dT'])<1e-10,
              dict(q=q,e=e))
        check(page.locator('#neutral-hinweis').is_visible(), q)
        records.append(dict(q=q, parameters=e, hint=page.locator('#neutral-hinweis').inner_text(),
                            live=page.locator('#ansage').inner_text()))
    return records


def texts_and_energy(page, context, lang):
    start(page); f1(page)
    course(page)
    page.locator('#knopf-weiter').click()
    check(('Ladet' if lang=='de' else 'load your') not in page.locator('#frageleiste .frage-text').inner_text(), 'F5 loaded')
    page.locator('#frageleiste input[value="auf"]').check()
    page.locator('#knopf-fest').click()
    check(('Geschafft' if lang=='de' else 'Done') not in page.locator('#frageleiste').inner_text(), 'F8 too early')
    page.locator('#knopf-aufl').click()
    finish = page.locator('#frageleiste').inner_text()
    check(('kalte Milch' if lang=='de' else 'cold milk') in finish, finish)
    goto_question(page,'v1')
    page.locator('#frage-zahl').fill('5')
    page.locator('#knopf-fest').click()
    check(('Milchtemperatur' if lang=='de' else 'milk temperature') in page.locator('#frageleiste .auftrag').inner_text(), 'Q6 V1')
    page.locator('#knopf-aufl').click()
    v1 = page.locator('#aufl-leiste').inner_text()
    check(('dieselbe Energie' if lang=='de' else 'same energy') in v1, v1)
    rows = []
    for minutes in [30,60,90]:
        temp = milk_equal(minutes)
        r = own(dict(STD,tEnd_min=minutes,thM=temp))
        check(abs(r['Q2']-r['Q1'])<1e-9 and abs(r['dT'])<1e-9, r)
        rounded = f'{temp:.1f}'.replace('.', ',' if lang=='de' else '.')
        check(rounded in v1, dict(expected=rounded,text=v1))
        rows.append(dict(minutes=minutes,milk=temp,Q1=r['Q1'],Q2=r['Q2'],difference=r['dT']))
    check(rows[0]['milk'] > rows[1]['milk'] > rows[2]['milk'], rows)
    cards = page.locator('#panel-versuche').text_content()
    check(cards.count('Notiert euch dazu' if lang=='de' else 'Note down for yourselves')==3, 'Q5')
    goto_question(page,'v3')
    page.locator('#knopf-ohne').click(); page.locator('#rueck-ja').click()
    check(page.locator('#aufl-leiste').is_visible() and
          ('was ihr seht' if lang=='de' else 'what you see') in page.locator('#frageleiste .auftrag').inner_text(), 'Q6 without')
    # Becher in beiden erklärenden Gleichungen und in der Lesehilfe.
    r = result(page)
    check(abs((r['Q2']-r['Q1'])*1000/r['C_GB']-r['dT'])<1e-10, r)
    page.locator('#tab-code').click()
    code = page.locator('#panel-code').inner_text()
    subscripts = page.locator('#panel-code math msub').all_text_contents()
    check(sum(re.sub(r'\s','',t)=='CGB' for t in subscripts)>=2, subscripts)
    page.locator('#tab-modell').click()
    page.locator('#panel-modell details').evaluate_all('es=>es.forEach(e=>e.open=true)')
    model = page.locator('#panel-modell').inner_text()
    check('2025a' not in model and 'Ferreira 2025' in model, model)
    check(('verschiedene Vorzeichen' if lang=='de' else 'different signs') in model, 'Q3 signs')
    return dict(v1=v1,v1_energy=rows,finish=finish,code=code,model=model,
                becher=dict(C=r['C_GB'],dT=r['dT'],Q1=r['Q1'],Q2=r['Q2']))


def beamer(page, context, lang):
    evidence=[]
    start(page)
    for phase in ['P2','P4']:
        if phase=='P4': f1(page)
        page.wait_for_timeout(200)
        sels=['#frageleiste','#diagramm']+(['#regler-pflicht'] if phase=='P4' else [])
        boxes=rects(page,sels)
        page.screenshot(path=str(OUT/'bilder'/f'beamer_{page.viewport_size["width"]}_{lang}_{phase}.png'))
        check(all(b['inView'] for b in boxes.values()),dict(phase=phase,boxes=boxes))
        evidence.append(dict(phase=phase,boxes=boxes))
    return evidence


def graphics(page,context,lang):
    start(page);f1(page);vt(page)
    page.locator('#s-trink').check()
    records=[]
    for temp in ['5','47','65']:
        commit_field(page,'#z-thM',temp)
        for t in ['5','30','56','57','60','120','180']:
            commit_field(page,'#z-tEnd',t)
            d=page.evaluate("""()=>{const s=document.querySelector('#diagramm');
            const ts=[...s.querySelectorAll('text')].filter(e=>e.textContent.trim()&&!/^[−\\d.,]+$/.test(e.textContent.trim()));
            const overlap=[];for(let i=0;i<ts.length;i++)for(let j=i+1;j<ts.length;j++){
              const a=ts[i].getBoundingClientRect(),b=ts[j].getBoundingClientRect();
              if(Math.min(a.right,b.right)-Math.max(a.left,b.left)>2&&Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top)>2)
                overlap.push([ts[i].textContent,ts[j].textContent]);}
            const box=document.querySelector('#diagramm-halter').getBoundingClientRect();
            return {overlap,labels:ts.map(e=>e.textContent),sticky:document.documentElement.classList.contains('anheften'),ratio:box.height/innerHeight,
            minFont:Math.min(...ts.map(e=>parseFloat(getComputedStyle(e).fontSize)*s.getBoundingClientRect().width/s.viewBox.baseVal.width))};}""")
            records.append(dict(temp=temp,t=t,**d))
            check(not d['overlap'] and d['minFont']>=10 and (not d['sticky'] or d['ratio']<=.45+.001), records[-1])
    # Umgekehrte Teilflächen, unabhängige Bilanz als Erwartung.
    page.locator('#knopf-standard').click()
    for k,v in [('VK','400'),('kA1','110'),('tEnd','180')]:commit_field(page,'#z-'+k,v)
    page.locator('[data-ansicht="waermestrom"]').click()
    e=state(page)['e'];r=result(page);o=own(e)
    check(abs(o['flaecheVor']-r['flaecheVor'])<1e-10 and o['flaecheVor']<0, r)
    text=page.locator('#flaechen-text').inner_text()
    check(('weniger' if lang=='de' else 'less') in text, text)
    page.screenshot(path=str(OUT/'bilder'/f'teilflaechen_{page.viewport_size["width"]}_{lang}.png'))
    return dict(layouts=records,reversed=dict(parameters=e,text=text,own=o['flaecheVor'],page=r['flaecheVor']))


def main():
    only=sys.argv[1] if len(sys.argv)>1 else None
    if only and (OUT/'ergebnis_nachpruefung.json').exists():
        RESULTS.extend(r for r in json.loads((OUT/'ergebnis_nachpruefung.json').read_text())['tests'] if r['name']!=only)
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
        def run(name,fn,lang='de',w=1366,h=768):
            if only and name!=only:return
            c=browser.new_context(viewport=dict(width=w,height=h),has_touch=w<800,reduced_motion='reduce')
            pg=c.new_page();pg.set_default_timeout(5000)
            errors=[];external=[]
            pg.on('pageerror',lambda e:errors.append(str(e)))
            pg.on('request',lambda r:external.append(r.url) if not r.url.startswith(('http://127.0.0.1:8765/','data:','blob:')) else None)
            try:
                pg.goto(URL+('?lang=en' if lang=='en' else ''))
                detail=fn(pg,c,lang)
                check(not errors and not external,dict(errors=errors,external=external))
                row=dict(name=name,lang=lang,w=w,h=h,status='PASS',detail=detail)
            except Exception as e:
                row=dict(name=name,lang=lang,w=w,h=h,status='FAIL' if isinstance(e,AssertionError) else 'ERROR',detail=str(e))
                pg.screenshot(path=str(OUT/'bilder'/f'fehler_{name}_{lang}_{w}.png'))
            row.update(pageerrors=errors,external=external)
            RESULTS.append(row)
            print(name,lang,w,row['status'],str(row['detail'])[:250],flush=True)
            c.close()
            (OUT/'ergebnis_nachpruefung.json').write_text(json.dumps(dict(browser=browser.version,playwright=importlib.metadata.version('playwright'),tests=RESULTS),ensure_ascii=False,indent=2)+'\n')
        run('Identitaet_MODELL',model_provenance)
        for lang in ['de','en']:
            for name,fn in [('Q1_F4_F11',gates_and_q1),('X5_03',source_change),('Sperren_V1_V5',neutral_opening),('F3_F12_Q2_Q7',texts_and_energy)]:run(name,fn,lang)
            for w,h in [(1280,720),(1366,768)]:run('Beamer',beamer,lang,w,h)
            for w,h in [(320,640),(360,640),(390,844)]:run('Beschriftungen_Q3',graphics,lang,w,h)
        browser.close()
    if any(r['status']!='PASS' for r in RESULTS):sys.exit(1)


if __name__=='__main__':main()
