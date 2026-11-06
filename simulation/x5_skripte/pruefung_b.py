"""X5, eigene Browserprüfung des unveränderten Artefakts.

Aufruf: python3 simulation/x5_skripte/pruefung_b.py
Voraussetzung: HTTP-Server des Repositorys auf 127.0.0.1:8765,
Playwright, /usr/bin/chromium, axe-core 4.11.0 in /tmp/x5-tools.
FAIL ist ein reproduzierter Produktbefund, ERROR ein Prüfhindernis.
"""
import csv
import io
import json
import re
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright
from pruefung_a import ROOT, OUT, URL, own

RESULTS = []
IMAGES = OUT/'bilder'
IMAGES.mkdir(exist_ok=True)


def state(page):
    return page.evaluate('KAFFEE.zustand()')


def result(page):
    return page.evaluate('JSON.parse(JSON.stringify(KAFFEE.ergebnis()))')


def commit_field(page,selector,text):
    page.locator(selector).fill(text)
    page.locator(selector).press('Tab')


def choose(page,value):
    page.locator(f'#frageleiste input[type=radio][value="{value}"]').check()


def start(page,wrong=False):
    choose(page,'2' if wrong else '1')
    page.locator('#frage-zahl').fill('4')
    page.locator('#frage-warum').fill('Die frühere Abkühlung senkt die Wärmeabgabe.')
    page.locator('#knopf-fest').click()


def f1(page):
    page.locator('#frage-zahl').fill('56')
    page.locator('#frage-warum').fill('Bei gleichen Wärmeströmen wächst der Unterschied nicht weiter.')
    page.locator('#knopf-fest').click()


def vt(page):
    if not page.locator('#vertiefung').get_attribute('open') is not None:
        page.locator('#vertiefung > summary').click()


def goto_question(page,q):
    page.locator('#tab-versuche').click()
    card=page.locator(f'[data-karte="{q}"]')
    if card.get_attribute('open') is None:
        card.locator('summary').click()
    card.locator('[data-zur]').click()


def course(page,third=False):
    if third: page.locator('#mess-b3').check()
    for b,values in [(1,[70.9,61.0,53.4,47.0,41.9,37.7,34.1]),(2,[80.4,67.8,57.0,49.2,43.1,38.2,34.6,31.2])]+([(3,[79.8,66.9,57.2,49.1,43.0,38.4,34.5,32.5])] if third else []):
        for i,v in enumerate(values):
            commit_field(page,f'.zelle input[data-b="{b}"][data-i="{i}"]',str(v).replace('.',',' if i%2 else '.'))
    commit_field(page,'#mess-u','21,5')
    commit_field(page,'#mess-m','6.0')
    page.locator('#mess-d').check()


def shot(page,name,selector=None):
    if selector: page.locator(selector).scroll_into_view_if_needed()
    page.screenshot(path=str(IMAGES/f'{name}.png'))


def main():
    only=sys.argv[1] if len(sys.argv)>1 else None
    if only and (OUT/'ergebnis_b.json').exists():
        RESULTS.extend(t for t in json.loads((OUT/'ergebnis_b.json').read_text())['tests'] if t['name']!=only)
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
        def run(name,fn,width=1366,height=768,lang='de',init=None):
            if only and name!=only:return
            context=browser.new_context(viewport=dict(width=width,height=height),has_touch=width<800,
                                        accept_downloads=True,reduced_motion='reduce')
            page=context.new_page()
            page.set_default_timeout(8000)
            errors=[]; external=[]
            page.on('pageerror',lambda e:errors.append(str(e)))
            page.on('request',lambda r:external.append(r.url) if not r.url.startswith(('http://127.0.0.1:8765/','data:','blob:')) else None)
            if init: page.add_init_script(init)
            try:
                page.goto(URL+('?lang=en' if lang=='en' else ''))
                detail=fn(page,context)
                RESULTS.append(dict(name=name,status='PASS',detail=detail,pageerrors=errors,external=external))
            except AssertionError as e:
                RESULTS.append(dict(name=name,status='FAIL',detail=str(e),pageerrors=errors,external=external))
                shot(page,'befund_'+re.sub('[^a-zA-Z0-9]','_',name))
            except Exception as e:
                RESULTS.append(dict(name=name,status='ERROR',detail=str(e),pageerrors=errors,external=external))
            finally:
                (OUT/'ergebnis_b.json').write_text(json.dumps(dict(browser=browser.version,tests=RESULTS),ensure_ascii=False,indent=2)+'\n')
                context.close()
            print(name,RESULTS[-1]['status'],str(RESULTS[-1]['detail'])[:450],flush=True)

        def p0(page,context):
            evidence={}
            for tab in ['versuche','modell','code']:
                page.locator('#tab-'+tab).click()
                for d in page.locator('#panel-'+tab+' details').all(): d.evaluate('(e)=>e.open=true')
                raw=page.evaluate('''()=>{const b=document.body.cloneNode(true);b.querySelectorAll('script,style').forEach(e=>e.remove());return b.textContent;}''')
                ax=context.new_cdp_session(page).send('Accessibility.getFullAXTree')
                axtext=json.dumps(ax,ensure_ascii=False)
                bad=[s for s in ['34,05','30,19','3,85','70,47','34.05','30.19','3.85','70.47'] if s in raw or s in axtext]
                assert not bad,(tab,bad)
                assert page.locator('#ansage').inner_text()==''
                assert page.locator('#diagramm polyline').count()==0
                evidence[tab]=dict(dom_result_hits=bad,ax_nodes=len(ax['nodes']))
            # Source strings are not rendered nodes or accessibility content.
            assert '3,85' in page.evaluate('TEXTE.de.aufl_start')
            assert '3,85' not in page.evaluate('KAFFEE.csv()')
            page.locator('#tab-versuche').click()
            shot(page,'p0_'+state(page)['sprache'])
            return evidence
        run('P0_DOM_AX_live_DE',p0,width=390,height=844)
        run('P0_DOM_AX_live_EN',p0,lang='en')

        def sequence(page,context):
            start(page,wrong=True)
            assert '34,05' in page.locator('#rechenwerte').inner_text()
            assert state(page)['aktuell']=='f1'
            assert page.locator('#r-tEnd').is_disabled()
            page.locator('#knopf-aufl-start').click()
            assert 'Tasse 1' in page.locator('#aufl-start').inner_text()
            assert '34,05' in page.locator('#aufl-start').inner_text()
            f1(page)
            assert page.locator('#r-tEnd').is_enabled()
            page.locator('#z-tEnd').fill('56')
            page.locator('#z-tEnd').press('Enter')
            assert '3,86' in page.locator('#rechenwerte').inner_text()
            page.locator('#knopf-aufl').click()
            assert '56 min' in page.locator('#aufl-leiste').inner_text()
            page.locator('#knopf-weiter').click()
            assert state(page)['aktuell']=='f2'
            assert page.locator('#knopf-fest').is_disabled()
            course(page,third=True)
            choose(page,'wechselnd')
            page.locator('#knopf-fest').click()
            assert state(page)['antworten']['f2']['fest']
            e=state(page)['e']; r=result(page); expected=own(e)
            assert e['thK0']==80.1 and e['thMess']==67.35
            assert e['becher'] and e['kAQuelle']=='messung'
            assert abs(expected['dT']-r['dT'])<1e-10
            page.locator('#knopf-aufl').click()
            assert 'Hängt von eurer Messung ab' in page.locator('#aufl-leiste').inner_text()
            shot(page,'pflichtweg_kurs390','#diagramm-halter')
            return dict(parameters=e,own=expected['dT'],display=page.locator('#rechenwerte').inner_text())
        run('Pflichtweg_falsche_Vorhersage_Kurswerte',sequence,width=390,height=844)

        def skip(page,context):
            page.locator('#knopf-ohne').click()
            page.locator('#rueck-ja').click()
            assert state(page)['antworten']['start']['ohne']
            page.locator('#knopf-ohne').click()
            page.locator('#rueck-ja').click()
            page.locator('#knopf-weiter').click()
            page.locator('#knopf-f2-weg').click()
            assert 'Geschafft' in page.locator('#frageleiste').inner_text()
            return 'Ohne Vorhersage, Frage 2 ohne Versuch übersprungen.'
        run('Ohne_Vorhersage_Versuch_ausgefallen',skip)

        def questions(page,context):
            start(page); f1(page)
            evidence=[]
            for q,pred in [('v1','47'),('v2','gleich'),('v3','kleiner'),('v4','ungleich'),('v5','thermo_offen')]:
                goto_question(page,q)
                before=state(page)
                assert not before['antworten'][q]['fest']
                assert page.locator('#knopf-aufl').count()==0
                if q=='v1': page.locator('#frage-zahl').fill(pred)
                else: choose(page,pred)
                page.locator('#frage-warum').fill('Vorhersage aus der Wärmebilanz.')
                page.locator('#knopf-fest').click()
                after=state(page)
                assert after['antworten'][q]['fest']
                assert after['e']['becher']==(q=='v3')
                page.locator('#knopf-aufl').click()
                evidence.append(dict(q=q,parameters=after['e'],text=page.locator('#aufl-leiste').inner_text()))
            return evidence
        run('V1_bis_V5_Ausgangslage_und_Aufloesung_DE',questions)

        def leak_v3(page,context):
            start(page);f1(page)
            page.locator('#knopf-weiter').click()
            # Standardmessung aus Teil g, ausdrücklich eigene Prüfdaten.
            for i,v in [(0,'80'),(1,'67')]:commit_field(page,f'.zelle input[data-b="2"][data-i="{i}"]',v)
            choose(page,'auf');page.locator('#knopf-fest').click()
            goto_question(page,'v3')
            shot(page,'v3_vorhersage_vor_ergebnis','#diagramm-halter')
            detail=dict(fest=state(page)['antworten']['v3']['fest'],values=page.locator('#rechenwerte').inner_text(),question=page.locator('#frageleiste').inner_text())
            assert '3,08' not in detail['values'],detail
        run('V3_Antwort_vor_Vorhersage',leak_v3)

        def sliders(page,context):
            start(page);f1(page);vt(page)
            evidence=[]
            for id,value in [('VK','300'),('VM','50'),('thK0','90,0'),('thM','10.0'),('thU','25,0'),('kA','0,2500'),('kA1','105')]:
                commit_field(page,'#z-'+id,value)
                e=state(page)['e']; r=result(page); o=own(e)
                assert abs(r['dT']-o['dT'])<1e-10
                evidence.append([id,e,r['dT']])
                assert page.locator('#r-'+id).get_attribute('aria-valuetext')
            page.locator('#s-becher').check()
            commit_field(page,'#z-mB','600')
            page.locator('#s-milch2Raum').check()
            assert 'Milchbeitrag' in page.locator('#energie-inhalt').inner_text()
            page.locator('#r-tEnd').focus()
            for key in ['Home','End','PageDown','PageUp','ArrowLeft','ArrowRight']:
                page.keyboard.press(key)
            page.locator('[data-r="VK"][data-pm="1"]').click()
            assert state(page)['e']['VK_ml']==310
            page.locator('[data-hilfe="VK"]').click()
            assert page.locator('#h-VK').is_visible()
            page.locator('[data-hilfe="VK"]').press('Escape')
            assert not page.locator('#h-VK').is_visible()
            old=state(page)['e']
            for text in ['abc','1000','1.2.3','', '-1']:
                commit_field(page,'#z-VK',text)
                assert page.locator('#z-VK').get_attribute('aria-invalid')=='true'
                assert state(page)['e']==old
            commit_field(page,'#z-VK','300')
            page.locator('[name="kaq"][value="messung"]').check()
            commit_field(page,'#z-thMess','66,5')
            assert state(page)['e']['thMess']==66.5
            return evidence
        run('Regler_alle_Felder_Tasten_Hilfe_Ungueltig',sliders)

        def source_change(page,context):
            start(page);f1(page);vt(page)
            commit_field(page,'#z-VK','100')
            commit_field(page,'#z-thK0','60')
            commit_field(page,'#z-thU','10')
            commit_field(page,'#z-kA','1.0000')
            before=result(page)
            page.locator('[name="kaq"][value="messung"]').check()
            after=result(page)
            detail=dict(before=before['dT'],after=after['dT'],kAbefore=before['kA'],kAafter=after['kA'],thMess=state(page)['e']['thMess'])
            assert abs(before['kA']-after['kA'])<1e-10,detail
            return detail
        run('Quellenwechsel_haelt_Kurven_bei_kA1',source_change)

        def invalid(page,context):
            start(page);f1(page);vt(page)
            page.locator('[name="kaq"][value="messung"]').check()
            commit_field(page,'#z-thK0','60')
            assert result(page) is None
            assert page.locator('#einstellung-fehler').is_visible()
            assert page.locator('#diagramm polyline').count()==0
            assert '34,05' not in page.locator('#rechenwerte').inner_text()
            assert '34,88' not in page.locator('#energie-inhalt').inner_text()
            old=page.locator('#einstellung-fehler').inner_text()
            page.locator('#sprachknopf').click()
            new=page.locator('#einstellung-fehler').inner_text()
            assert old!=new,dict(de=old,en=new,lang=page.locator('html').get_attribute('lang'))
        run('Ungueltige_Einstellung_und_Sprachwechsel',invalid)

        def measurement_rejection(page,context):
            start(page);f1(page)
            for i,v in [(0,'80.01'),(1,'67.03')]:commit_field(page,f'.zelle input[data-b="2"][data-i="{i}"]',v)
            page.locator('#mess-b3').check()
            for i,v in [(0,'80.02'),(1,'67.04')]:commit_field(page,f'.zelle input[data-b="3"][data-i="{i}"]',v)
            page.locator('#mess-ueber').click()
            e=state(page)['e']
            assert abs(e['thK0']-80.015)<1e-12 and abs(e['thMess']-67.035)<1e-12
            commit_field(page,'#mess-u','40')
            page.locator('#mess-ueber').click()
            assert state(page)['e']==e
            assert 'nicht' in page.locator('#mess-info').inner_text()
            commit_field(page,'#mess-u','20')
            x='.zelle input[data-b="2"][data-i="2"]'
            commit_field(page,x,'n/a')
            assert page.locator(x).get_attribute('aria-invalid')=='true'
            commit_field(page,x,'')
            assert state(page)['kurs']['werte']['b2'][2] is None
            return dict(accepted=e,rejected=page.locator('#mess-info').inner_text())
        run('Messblatt_ungerundet_Grenze_Unsinn_Loeschen',measurement_rejection)

        def links(page,context):
            start(page);f1(page);course(page,third=True)
            before=state(page)
            page.locator('#mess-link').click()
            link=page.locator('#link-ausgabe .link-ausgabe').inner_text()
            assert '#kurs1=' in link and len(link.split('#')[1])<=400
            page.goto(link)
            assert state(page)==before
            page.locator('#link-nein').click()
            assert state(page)==before and '#' not in page.url
            # Neuer Kontext, Import erst nach Zustimmung.
            q=context.new_page();q.goto(URL)
            q.locator('#mess-weg').click();q.locator('#rueck-ja').click()
            q.goto(link)
            assert state(q)['kurs']!=before['kurs']
            q.locator('#link-ja').click()
            assert state(q)['kurs']==before['kurs']
            assert state(q)['antworten']==before['antworten'] and '#' not in q.url
            data=state(q)['kurs']
            details=[]
            for suffix in ['kurs2=abc','kurs1=%ZZ','kurs1=u:101;m:5;d:0;b:2;b2:80,67,,,,,,','kurs1='+('a'*401)]:
                q.goto(URL+'#'+suffix)
                assert state(q)['kurs']==data
                assert q.locator('#link-banner').is_visible()
                assert '#' not in q.url
                details.append(q.locator('#link-banner').inner_text())
            return dict(link=link,reasons=details)
        run('Kurslink_Hin_Rueck_Nein_Ja_Beschaedigt',links)

        def foreign(page,context):
            page.goto(URL+'#foreign-data=123')
            assert page.locator('#link-banner').is_visible() and '#' not in page.url,dict(url=page.url,banner=page.locator('#link-banner').inner_text())
        run('Kurslink_fremdes_Format',foreign)

        def precision_link(page,context):
            commit_field(page,'#mess-u','21.555')
            commit_field(page,'#mess-m','6.123')
            commit_field(page,'.zelle input[data-b="2"][data-i="0"]','80')
            old=state(page)['kurs']
            page.locator('#mess-link').click()
            link=page.locator('#link-ausgabe .link-ausgabe').inner_text()
            page.goto(link);page.locator('#link-ja').click()
            new=state(page)['kurs']
            assert new==old,dict(before=old,after=new,link=link)
        run('Kurslink_alle_akzeptierten_Nachkommastellen',precision_link)

        def reset(page,context):
            start(page);f1(page);course(page)
            page.locator('#sprachknopf').click()
            before=state(page);page.reload()
            assert state(page)==before
            page.locator('#tab-code').click()
            page.locator('#tab-code').focus();page.keyboard.press('Home')
            assert page.locator('#tab-versuche').get_attribute('aria-selected')=='true'
            page.keyboard.press('ArrowRight')
            assert page.locator('#tab-modell').get_attribute('aria-selected')=='true'
            page.locator('#knopf-gruppe').click();page.locator('#rueck-nein').click()
            assert state(page)['kurs']==before['kurs']
            page.locator('#knopf-gruppe').click();page.locator('#rueck-ja').click()
            after=state(page)
            assert after['sprache']=='en' and after['kurs']==before['kurs']
            assert not after['antworten']['start']['fest']
            return dict(before=before,after=after)
        run('Sprache_Persistenz_Reiter_Reset',reset)

        def denied(page,context):
            assert page.evaluate('KAFFEE.speicherOk()') is False
            assert page.locator('#speicher-hinweis').inner_text()
            start(page);f1(page)
            assert result(page) is not None
            return page.locator('#speicher-hinweis').inner_text()
        run('Speicher_gesperrt',denied,init="Object.defineProperty(window,'localStorage',{get(){throw new DOMException('blocked','SecurityError')}})")

        def offline(page,context):
            # Browserrichtlinie sperrt file:. Exakte Bytes ersatzweise über Route,
            # in einem zweiten frischen Kontext ohne Netz geladen.
            c=browser.new_context(offline=True)
            c.route(URL,lambda route:route.fulfill(status=200,content_type='text/html',body=(ROOT/'simulation/site/index.html').read_bytes()))
            q=c.new_page(); requests=[]
            q.on('request',lambda r:requests.append(r.url))
            q.goto(URL);start(q);f1(q)
            assert result(q)
            assert requests==[URL],requests
            # CSP muss neues, nicht gehashtes Inline-Skript blockieren.
            q.evaluate("()=>{const s=document.createElement('script');s.textContent='window.x5Injected=true';document.body.append(s)}")
            assert q.evaluate('window.x5Injected===undefined')
            c.close()
            return dict(offline_requests=requests,csp_inline_blocked=True,file='ERR_BLOCKED_BY_ADMINISTRATOR, separat beobachtet')
        run('Offline_frisches_Profil_CSP',offline)

        def csv_check(page,context):
            start(page);f1(page)
            texts={}
            for lang,delimiter in [('de',';'),('en',',')]:
                if state(page)['sprache']!=lang: page.locator('#sprachknopf').click()
                with page.expect_download() as dl:page.locator('#mess-csv').click()
                text=Path(dl.value.path()).read_text(encoding='utf-8-sig')
                rows=list(csv.reader(io.StringIO(text),delimiter=delimiter))
                assert len(rows)==63,len(rows)
                assert rows[1][1]==('70,47' if lang=='de' else '70.47')
                assert rows[11][2]==('67,00' if lang=='de' else '67.00')
                assert rows[-1][2]==('30,19' if lang=='de' else '30.19')
                texts[lang]=dict(name=dl.value.suggested_filename,start=rows[1],ten=rows[11],end=rows[-1])
            vt(page);page.locator('#s-trink').check()
            assert '10.9' in page.locator('#zusatz-text').inner_text()
            page.locator('#s-becher').check();page.locator('#s-kalt').check()
            assert 'Cold mug' in page.locator('#zusatz-text').inner_text() or 'cold' in page.locator('#zusatz-text').inner_text()
            return texts
        run('CSV_Download_DE_EN_Trinkzeit_Becherkalt',csv_check)

        def axe(page,context):
            # axe per Playwright evaluate, keine gelockerte CSP der Seite.
            page.evaluate(Path('/tmp/x5-tools/node_modules/axe-core/axe.min.js').read_text())
            evidence=[]
            for name in ['P0','P4','Vertiefung','Code']:
                if name=='P4':start(page);f1(page)
                if name=='Vertiefung':vt(page)
                if name=='Code':page.locator('#tab-code').click()
                r=page.evaluate("async()=>await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21aa','wcag22aa']}})")
                evidence.append(dict(state=name,violations=r['violations'],incomplete_count=len(r['incomplete'])))
            (OUT/'axe.json').write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n')
            assert not any(r['violations'] for r in evidence),[(r['state'],[(v['id'],len(v['nodes'])) for v in r['violations']]) for r in evidence]
            return evidence
        run('WCAG_axe_4_11_0',axe,width=390,height=844)

        def source_texts(page,context):
            texts=page.evaluate('TEXTE')
            assert set(texts['de'])==set(texts['en'])
            bad={l:[k for k,v in d.items() if '\u2013' in v or '\u2014' in v] for l,d in texts.items()}
            assert not any(bad.values()),bad
            assert not any('{{' in v for d in texts.values() for v in d.values())
            return dict(keys=len(texts['de']),dashes=bad)
        run('Textschluessel_Gedankenstriche_Platzhalter',source_texts)

        def performance(page,context):
            start(page);f1(page)
            values=[]
            # 30-s-Folge; einzelne Frames messen inklusive Zeichnung.
            t0=time.monotonic()
            while time.monotonic()-t0<30:
                ms=page.evaluate('''()=>{const x=document.querySelector('#r-tEnd');const t=performance.now();
                   x.value=Number(x.value)===60?120:60;x.dispatchEvent(new Event('input',{bubbles:true}));return performance.now()-t}''')
                values.append(ms)
                assert own(state(page)['e'])['dT']-result(page)['dT']<1e-8
                page.wait_for_timeout(100)
            assert max(values)<100,dict(max_ms=max(values),median=sorted(values)[len(values)//2])
            return dict(duration=time.monotonic()-t0,events=len(values),max_ms=max(values),median_ms=sorted(values)[len(values)//2])
        run('Reglerfolge_30s_100ms',performance)
        browser.close()


if __name__=='__main__':main()
