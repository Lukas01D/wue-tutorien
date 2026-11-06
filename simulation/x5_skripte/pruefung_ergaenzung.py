"""Gezielte X5-Gegenproben zu Zeichnung, Fachtexten, Messwert und Fokus.

Aufruf wie pruefung_b.py. Grafik vorab: höchstens 0,2 SVG-Einheiten
Abweichung, einschließlich der Rundung der Achsen und Koordinaten.
"""
import json
import math
import re
from playwright.sync_api import sync_playwright
from pruefung_a import OUT,URL,own
from pruefung_b import start,f1,vt,state,result,commit_field,goto_question,shot


def main():
    evidence={}
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
        c=b.new_context(viewport=dict(width=1366,height=768));page=c.new_page();page.set_default_timeout(8000)
        page.goto(URL);start(page);f1(page);vt(page)
        graphics=[]
        for case,edits in [('standard',[]),('100ml',[('VK','100')]),('400ml',[('VK','400')]),
                          ('milch65',[('thM','65')]),('raum10',[('thU','10')]),('105prozent',[('kA1','105')]),
                          ('kA05',[('kA','0.05')]),('kA1',[('kA','1')])]:
            page.locator('#knopf-standard').click()
            for key,v in edits:commit_field(page,'#z-'+key,v)
            data=page.evaluate('''()=>{const s=document.querySelector('#diagramm');return {
              y:[...s.querySelectorAll('text[text-anchor=end]')].filter(x=>/^\\d+([.,]\\d+)?$/.test(x.textContent)).map(x=>[x.textContent,Number(x.getAttribute('y'))-4]),
              x:[...s.querySelectorAll('text[text-anchor=middle]')].filter(x=>/^\\d+([.,]\\d+)?$/.test(x.textContent)).map(x=>[x.textContent,Number(x.getAttribute('x'))]),
              lines:[...s.querySelectorAll('polyline')].map(x=>({stroke:x.getAttribute('stroke'),points:x.getAttribute('points')}))};}''')
            e=state(page)['e'];expected=own(e)
            axes=[]
            for name in ['x','y']:
                ps=[(float(v.replace(',','.')),pos) for v,pos in data[name]]
                k=(ps[-1][1]-ps[0][1])/(ps[-1][0]-ps[0][0]);a=ps[0][1]-k*ps[0][0]
                axes.append((a,k))
            ax,kx=axes[0];ay,ky=axes[1];worst=0;count=0
            for line in data['lines']:
                ck=expected['C_KB'];cg=expected['C_GB'];ka=expected['kA'];u=e['thU']
                for pt in line['points'].split():
                    x,y=map(float,pt.split(','));t=(x-ax)/kx
                    if line['stroke']=='#8b5a2b':temperature=u+(expected['th10']-u)*math.exp(-e['kA1Faktor']*ka*t*60/cg)
                    else:temperature=u+(e['thK0']-u)*math.exp(-ka*t*60/ck)
                    delta=abs(y-(ay+ky*temperature));worst=max(worst,delta);count+=1
            # X rounding also changes sampled t, at largest slopes < 0.2.
            assert worst<.2,(case,worst)
            graphics.append(dict(case=case,points=count,max_error_svg=worst))
        evidence['graphics']=graphics

        # Die ergänzende Wahl der Messquelle überschreibt einen echten Messwert
        # mit dem rechnerisch gleichwertigen Wert aus der festgehaltenen kA-Quelle.
        page.locator('#knopf-standard').click()
        page.locator('[name="kaq"][value="messung"]').check()
        commit_field(page,'#z-thMess','66.5')
        original=state(page)['e']['thMess']
        page.locator('[name="kaq"][value="fest"]').check()
        commit_field(page,'#z-kA','0.25')
        page.locator('[name="kaq"][value="messung"]').check()
        evidence['measured_replaced']=dict(before=original,after=state(page)['e']['thMess'],visible=page.locator('#z-thMess').input_value(),label=page.locator('#rl-thMess').inner_text())
        shot(page,'messwert_durch_modellwert_ersetzt','#z-thMess')
        # Physikalischer Gegenbeleg zur unbedingten C_G-Formel, Becherfall Teil g.
        goto_question(page,'v3');page.locator('#frageleiste input[value=kleiner]').check();page.locator('#knopf-fest').click()
        r=result(page);cg=r['C_K']+r['C_M'];cgb=r['C_GB']
        page.locator('#tab-code').click()
        evidence['energy_formula']=dict(CG=cg,CGB=cgb,difference=r['dT'],heat_difference=r['Q2']-r['Q1'],
             wrong=(r['Q2']-r['Q1'])*1000/cg,right=(r['Q2']-r['Q1'])*1000/cgb,
             text=page.locator('#panel-code').inner_text())
        shot(page,'becherbilanz_falsches_CG','#panel-code')
        # Ausgleichsgerade: nach der Milch darf kein Fitpunkt entstehen.
        page.locator('#tab-versuche').click()
        for i,v in enumerate([80.1,67.3,56.9,49.1,42.7,37.4,33.7,31.0]):
            commit_field(page,f'.zelle input[data-b="2"][data-i="{i}"]',str(v))
        goto_question(page,'f2')
        page.locator('#frageleiste input[value=auf]').check()
        page.locator('#knopf-fest').click()
        page.locator('[data-ansicht=ln]').click()
        before=page.locator('#flaechen-text').inner_text()
        commit_field(page,'.zelle input[data-b="2"][data-i="7"]','10')
        after=page.locator('#flaechen-text').inner_text()
        assert before==after
        page.locator('#knopf-ausgleich').click()
        evidence['fit_ui']=dict(text=before,parameters=state(page)['e'],measured=state(page)['kurs']['werte']['b2'][1])
        assert state(page)['e']['thMess']==67.3
        temps=[67.3,56.9,49.1,42.7,37.4,33.7]
        xs=[t*600 for t in range(1,7)]
        ys=[math.log((t-20)/(80.1-20)) for t in temps]
        expected=-1091*sum(x*y for x,y in zip(xs,ys))/sum(x*x for x in xs)
        assert abs(state(page)['e']['kA']-expected)<1e-10
        c.close()

        # Vollständiger englischer Fragenlauf mit absichtlich falschen Antworten.
        c=b.new_context(viewport=dict(width=390,height=844));page=c.new_page();page.set_default_timeout(8000)
        page.goto(URL+'?lang=en');start(page,wrong=True);f1(page)
        english=[]
        for q,v in [('v1','5'),('v2','larger'),('v3','groesser'),('v4','falsch'),('v5','glas')]:
            goto_question(page,q)
            if q=='v1':page.locator('#frage-zahl').fill(v)
            else:
                value='groesser' if q=='v2' else v
                page.locator(f'#frageleiste input[value="{value}"]').check()
            page.locator('#knopf-fest').click();page.locator('#knopf-aufl').click()
            english.append(dict(q=q,explanation=page.locator('#aufl-leiste').inner_text()))
        evidence['english_wrong']=english
        c.close()

        # Bekannter Fokusbefund: 32 px, 768 x 1024, rückwärts aus dem Messblatt.
        c=b.new_context(viewport=dict(width=768,height=1024));page=c.new_page();page.goto(URL);start(page);f1(page);vt(page)
        page.evaluate("document.documentElement.style.fontSize='32px'")
        page.locator('#mess-u').focus()
        covered=[]
        for i in range(70):
            page.keyboard.press('Shift+Tab')
            d=page.evaluate('''()=>{const e=document.activeElement,r=e.getBoundingClientRect(),x=r.x+r.width/2,y=r.y+r.height/2,t=document.elementFromPoint(x,y);return {id:e.id,tag:e.tagName,top:r.top,bottom:r.bottom,hit:t&&t.id,cover:!!t&&!e.contains(t)&&!t.contains(e)};}''')
            if d['cover'] and d['tag']!='BODY':
                covered.append(d)
                if len(covered)==1:shot(page,'fokus_768_1024_32px')
        evidence['focus_768_1024_32px']=covered
        c.close()

        # Vergleich mit den richtigen Simulationsseiten des Lernzentrums.
        vorbild=[]
        for w,h in [(390,844),(1366,768)]:
            for topic,model in [('01','steady'),('02','convection_no_fin')]:
                c=b.new_context(viewport=dict(width=w,height=h));page=c.new_page()
                page.goto(f'http://127.0.0.1:8766/index.html#topic-{topic}/simulation/{model}')
                page.wait_for_timeout(700)
                # Die aktive Simulation wird per Route angewählt; zum Bild scrollen.
                figure=page.locator('#simulation-detail')
                if figure.count():figure.scroll_into_view_if_needed()
                shot(page,f'vorbild_thema{topic}_{w}')
                vorbild.append(dict(w=w,topic=topic,url=page.url,text=figure.inner_text()[:1500] if figure.count() else page.locator('body').inner_text()[:1000]))
                c.close()
        evidence['vorbild']=vorbild
        b.close()
    (OUT/'ergebnis_ergaenzung.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in evidence.items() if k not in ['energy_formula','english_wrong','vorbild']},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
