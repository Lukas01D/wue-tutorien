"""Eigene X5-Layout-, Fokus- und Darstellungsprüfung, nur Lesezugriff auf die Seite.

Aufruf: python3 simulation/x5_skripte/pruefung_layout.py
Lokaler Server: Repository Port 8765, Lernzentrum-v8/dist Port 8766.
"""
import json
import time
from playwright.sync_api import sync_playwright
from pruefung_a import OUT,URL
from pruefung_b import start,f1,vt,state,result,commit_field,shot,IMAGES

MEASURE = '''()=>{
 const svg=document.querySelector('#diagramm'), b=svg.getBoundingClientRect(), h=document.querySelector('#diagramm-halter').getBoundingClientRect();
 const texts=[...svg.querySelectorAll('text')].map(e=>{const m=e.getScreenCTM();return {text:e.textContent,size:parseFloat(getComputedStyle(e).fontSize)*Math.hypot(m.a,m.b)};});
 const targets=[...document.querySelectorAll('button,input,summary')].filter(e=>e.getClientRects().length&&!e.disabled).map(e=>{
   const t=e.matches('input[type=radio],input[type=checkbox]')?e.closest('label'):e,r=t.getBoundingClientRect();
   return {id:e.id||e.getAttribute('aria-label')||e.textContent.trim().slice(0,50),w:r.width,h:r.height,font:getComputedStyle(e).fontSize};});
 return {width:innerWidth,height:innerHeight,scrollWidth:document.documentElement.scrollWidth,
   diagram:{width:b.width,height:b.height,viewbox:svg.getAttribute('viewBox'),holderHeight:h.height,holderRatio:h.height/innerHeight,
   anheften:document.documentElement.classList.contains('anheften'),texts},
   smallTargets:targets.filter(e=>e.w<43.9||e.h<43.9),tinyTargets:targets.filter(e=>e.w<23.9||e.h<23.9),
   smallInputs:targets.filter(e=>e.id.startsWith('z-')&&parseFloat(e.font)<16),
   visibleSliders:[...document.querySelectorAll('input[type=range]')].filter(e=>e.getClientRects().length).length};}'''


def main():
    records=[];focus=[];labels=[];contrast=[];special=[]
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
        for w,h in [(320,640),(360,640),(390,844),(844,390),(768,768),(1024,768),(1366,768),(1280,720),(1920,1080)]:
            for lang in ['de','en']:
                c=b.new_context(viewport=dict(width=w,height=h),has_touch=w<800,reduced_motion='reduce')
                page=c.new_page();page.set_default_timeout(8000)
                page.goto(URL+('?lang=en' if lang=='en' else ''))
                for phase in ['P0','P2','P4','VT','CODE']:
                    if phase=='P2':start(page)
                    if phase=='P4':f1(page)
                    if phase=='VT':vt(page)
                    if phase=='CODE':
                        page.locator('#tab-code').click()
                        if w==390 and lang=='de':shot(page,'code_becher_formel','#panel-code')
                    m=page.evaluate(MEASURE)
                    m.update(phase=phase,lang=lang)
                    records.append(m)
                    if phase in ['P2','VT'] and w in [360,390,1366] and lang=='de':
                        shot(page,f'{phase}_{w}x{h}_{lang}','#diagramm-halter')
                    if phase=='P4':
                        page.locator('#z-tEnd').focus()
                        keyboard=[]
                        for key in ['Home','ArrowRight','End','PageDown','PageUp','ArrowLeft']:
                            page.keyboard.press(key)
                            keyboard.append([key,state(page)['e']['tEnd_min']])
                        special.append(dict(name='Tastatur',w=w,h=h,lang=lang,values=keyboard))
                        commit_field(page,'#z-tEnd','60')
                # Schnitt in Standard-, End- und fast gleichen Kurvenzuständen.
                page.locator('#tab-versuche').click()
                for id,value in [('tEnd','60'),('tEnd','120'),('tEnd','180'),('thM','47.0')]:
                    commit_field(page,'#z-'+id,value)
                    r=result(page)
                    has_circle=page.locator('#diagramm circle[r="5.5"]').count()>0
                    has_label=page.locator('#diagramm text').filter(has_text='Schnitt' if lang=='de' else 'Intersection').count()>0
                    labels.append(dict(w=w,h=h,lang=lang,changed=id,value=value,cross=r['tSchnitt'],circle=has_circle,label=has_label))
                    if has_circle and not has_label and w in [390,1366] and lang=='de':shot(page,f'schnitt_unbeschriftet_{w}_{value}','#diagramm-halter')
                # Reflow bei 200% Grundschrift, echter Browser-Zoom bleibt offen.
                page.locator('#knopf-standard').click()
                page.evaluate("document.documentElement.style.fontSize='200%'")
                page.wait_for_timeout(120)
                m=page.evaluate(MEASURE);m.update(phase='VT_200prozent_Text',lang=lang);records.append(m)
                if w in [390,768] and lang=='de':
                    shot(page,f'grosse_schrift_{w}','#diagramm-halter')
                    # Vollständige Tab-Folge mit automatischem Scrollen.
                    page.locator('#sprachknopf').focus()
                    for i in range(180):
                        page.keyboard.press('Tab' if i<90 else 'Shift+Tab')
                        x=page.evaluate('''()=>{const a=document.activeElement,r=a.getBoundingClientRect(),x=Math.max(0,Math.min(innerWidth-1,r.x+r.width/2)),y=Math.max(0,Math.min(innerHeight-1,r.y+r.height/2));
                          const hit=document.elementFromPoint(x,y);return {id:a.id,tag:a.tagName,text:a.getAttribute('aria-label')||a.textContent.trim().slice(0,60),top:r.top,bottom:r.bottom,
                          centerCovered:!!hit&&!a.contains(hit)&&!hit.contains(a),cover:hit&&hit.id};}''')
                        if x['centerCovered'] and x['tag'] not in ['BODY']:
                            focus.append(dict(w=w,h=h,lang=lang,step=i,**x))
                            if len([f for f in focus if f['w']==w])==1:shot(page,f'fokus_verdeckt_{w}')
                if w==390:
                    page.evaluate("document.documentElement.style.fontSize='100%'")
                    page.set_viewport_size(dict(width=390,height=380))
                    page.locator('#z-thK0').focus();page.wait_for_timeout(150)
                    special.append(dict(name='Tastatur_kleine_Hoehe',lang=lang,measure=page.evaluate(MEASURE)))
                    if lang=='de':shot(page,'tastatur_390x380','#z-thK0')
                    page.set_viewport_size(dict(width=390,height=844))
                    page.locator('#mess-u').focus();page.wait_for_timeout(150)
                    special.append(dict(name='Messfeld_Anheften_aus',lang=lang,measure=page.evaluate(MEASURE)))
                    page.locator('#sprachknopf').focus()
                    page.locator('#knopf-anheften').tap()
                    assert not page.evaluate("document.documentElement.classList.contains('anheften')")
                    special.append(dict(name='Tippen_Anheften_aus',lang=lang,ok=True))
                c.close()
                print('Layout',w,h,lang,flush=True)
        # Farben unabhängig rechnen, gemeinsame weiße Diagrammfläche.
        def lum(hex):
            rgb=[int(hex[i:i+2],16)/255 for i in (1,3,5)]
            rgb=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in rgb]
            return sum(v*k for v,k in zip(rgb,[.2126,.7152,.0722]))
        for col in ['#8b5a2b','#222222','#3d70a3','#8a8984','#39718e','#5a6b7f','#173d5e','#7d8fa1']:
            ratio=(1.05)/(lum(col)+.05)
            contrast.append(dict(color=col,on='#ffffff',ratio=ratio))
        # Eigenes Graustufenbild, CSS-Filter nur im Browserprofil.
        c=b.new_context(viewport=dict(width=1366,height=768));page=c.new_page();page.goto(URL);start(page);f1(page)
        page.evaluate("document.documentElement.style.filter='grayscale(1)'")
        shot(page,'graustufen','#diagramm-halter');c.close()
        # Vorbild lokal, unveränderter Tag, kein Schreiben in dessen Repository.
        comparisons=[]
        for w,h in [(390,844),(1366,768)]:
            c=b.new_context(viewport=dict(width=w,height=h));page=c.new_page()
            try:
                page.goto('http://127.0.0.1:8766/index.html#topic-01/simulation/steady')
                page.wait_for_timeout(1000)
                shot(page,f'lernzentrum_v8_{w}')
                comparisons.append(dict(w=w,text=page.locator('body').inner_text()[:3000],url=page.url))
            except Exception as e:comparisons.append(dict(w=w,error=str(e)))
            c.close()
        data=dict(browser=b.version,layouts=records,focus=focus,labels=labels,contrast=contrast,special=special,vorbild=comparisons)
        (OUT/'ergebnis_layout.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
        print('Layouts',len(records),'Fokusmitten verdeckt',len(focus),'Schnitt ohne Text',sum(r['circle'] and not r['label'] for r in labels))
        b.close()


if __name__=='__main__':main()
