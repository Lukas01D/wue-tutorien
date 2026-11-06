"""Gezielte Nachprüfung der geänderten Bedienung und zeitlicher Layoutzustände."""
import json
import sys
from playwright.sync_api import sync_playwright
from pruefung_a import OUT, URL
from pruefung_b import start, f1, vt, state, commit_field, goto_question, course


def main():
    tests=[]
    only=sys.argv[1] if len(sys.argv)>1 else None
    if only and (OUT/'ergebnis_bedienung.json').exists():
        tests.extend(r for r in json.loads((OUT/'ergebnis_bedienung.json').read_text()) if r['name']!=only)
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
        def run(name,fn,lang):
            if only and name!=only:return
            c=b.new_context(viewport=dict(width=390,height=844),has_touch=True,reduced_motion='reduce')
            pg=c.new_page();pg.set_default_timeout(5000)
            try:
                pg.goto(URL+('?lang=en' if lang=='en' else ''));detail=fn(pg,lang)
                row=dict(name=name,lang=lang,status='PASS',detail=detail)
            except Exception as e:
                row=dict(name=name,lang=lang,status='FAIL' if isinstance(e,AssertionError) else 'ERROR',detail=str(e))
                pg.screenshot(path=str(OUT/'bilder'/f'bedienung_fehler_{name}_{lang}.png'))
            tests.append(row);c.close()
            print(name,lang,row['status'],str(row['detail'])[:200],flush=True)
            (OUT/'ergebnis_bedienung.json').write_text(json.dumps(tests,ensure_ascii=False,indent=2)+'\n')

        def enlarged(pg,lang):
            start(pg);f1(pg);vt(pg)
            pg.locator('#tab-code').click();pg.locator('#tab-versuche').click()
            for key,v in [('tEnd','60'),('tEnd','120'),('tEnd','180'),('thM','47.0')]:commit_field(pg,'#z-'+key,v)
            pg.locator('#knopf-standard').click()
            pg.evaluate("document.documentElement.style.fontSize='200%'")
            series=[]
            for delay in [0,120,130,250,500,1000]:
                pg.wait_for_timeout(delay)
                r=pg.evaluate("""()=>({sticky:document.documentElement.classList.contains('anheften'),
                holder:document.querySelector('#diagramm-halter').getBoundingClientRect().height,
                svg:document.querySelector('#diagramm').getBoundingClientRect().height,height:innerHeight,
                width:innerWidth,scroll:document.documentElement.scrollWidth})""")
                r['elapsed_ms']=sum([0,120,130,250,500,1000][:len(series)+1]);series.append(r)
            pg.screenshot(path=str(OUT/'bilder'/f'200prozent_stabil_{lang}.png'))
            assert all(not r['sticky'] or r['holder']/r['height']<=.451 for r in series[3:]),series
            return series

        def link_focus(pg,lang):
            start(pg);f1(pg);course(pg)
            pg.locator('#mess-link').click();link=pg.locator('#link-ausgabe .link-ausgabe').inner_text()
            pg.goto(link);pg.locator('#link-ja').click()
            pg.wait_for_timeout(16000)
            banner=pg.locator('#link-banner').inner_text()
            assert pg.locator('#link-banner').is_visible()
            button=pg.locator('#link-banner button').first
            label=button.inner_text();button.click()
            focus=pg.evaluate('document.activeElement.id')
            assert focus=='frage-titel',dict(focus=focus,banner=banner)
            return dict(banner_after_16s=banner,button=label,focus=focus)

        def sticky_and_doubletap(pg,lang):
            start(pg);f1(pg);vt(pg)
            records=[]
            for t in ['5','30','56','60','90','120','180']:
                commit_field(pg,'#z-tEnd',t);pg.wait_for_timeout(350)
                r=pg.locator('#diagramm-halter').bounding_box()
                records.append(r['height'])
            assert max(records)-min(records)<2,records
            pg.locator('#knopf-anheften').tap()
            pg.evaluate('scrollBy(0,300)')
            pg.locator('#knopf-anheften').tap();pg.wait_for_timeout(350)
            button=pg.locator('#knopf-anheften')
            d=button.evaluate("""e=>{const r=e.getBoundingClientRect(),h=document.elementFromPoint(r.x+r.width/2,r.y+r.height/2);return {covered:!e.contains(h),top:r.top,bottom:r.bottom};}""")
            assert not d['covered'],d
            goto_question(pg,'v3')
            pg.locator('#frageleiste input[value="kleiner"]').check()
            box=pg.locator('#knopf-fest').bounding_box();x=box['x']+box['width']/2;y=box['y']+box['height']/2
            pg.mouse.click(x,y);pg.wait_for_timeout(600);pg.mouse.click(x,y)
            assert state(pg)['aktuell']=='v3',state(pg)['aktuell']
            return dict(heights=records,button=d,question=state(pg)['aktuell'])

        def errors(pg,lang):
            last_valid=state(pg)['kurs']
            previous=pg.locator('#mess-u').input_value()
            commit_field(pg,'#mess-u','21.555')
            e=pg.locator('#mess-u')
            de=e.get_attribute('aria-describedby');message=pg.locator('#mess-fehler').inner_text()
            assert e.get_attribute('aria-invalid')=='true' and de=='mess-fehler',dict(description=de,message=message)
            pg.locator('#sprachknopf').click()
            translated=pg.locator('#mess-fehler').inner_text()
            current=pg.locator('#mess-u').input_value()
            # Sprachwechsel zeichnet das Messblatt aus den gültigen Daten neu.
            # Nicht akzeptierte Rohwerte werden verworfen (schon vor der Runde).
            # Das ist keine Übersetzung der alten Fehlermeldung.
            assert translated=='' and state(pg)['kurs']==last_valid and current==previous,dict(message=message,translated=translated,current=current,previous=previous)
            return dict(message=message,after_message=translated,description=de,
                        before_input=previous,after_input=current,stored=last_valid,
                        behavior='Nicht angenommener Rohwert verworfen, letzter gültiger Wert wieder angezeigt; keine gespeicherten Daten geändert.')

        for lang in ['de','en']:
            for name,fn in [('200prozent_zeitverlauf',enlarged),('Kurslink_Fokus_Bestaetigung',link_focus),('Anheften_Doppeltipp',sticky_and_doubletap),('Messfehler_Sprache',errors)]:run(name,fn,lang)
        b.close()
    if any(r['status']!='PASS' for r in tests):sys.exit(1)


if __name__=='__main__':main()
