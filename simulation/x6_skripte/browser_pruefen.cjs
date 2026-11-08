// X6: eigener Offline-Browsertest. Keine Übernahme der Tests des Baus.
// Voraussetzungen: playwright, axe-core (X6_AXE), Chromium (X6_CHROMIUM).
const {chromium}=require('playwright'),fs=require('fs'),path=require('path');
const assert=require('assert/strict');
const H=__dirname,html=fs.readFileSync(path.resolve(H,'../site/index.html'));
const axe=fs.readFileSync(process.env.X6_AXE||'/tmp/kaffee-x6-deps/node_modules/axe-core/axe.min.js','utf8');
const result={browser:null,laeufe:[],befunde:{},fehler:[]};
const numeric=t=>Number(t.replace('−','-').replace(',','.').match(/-?\d+(?:\.\d+)?/)[0]);
const seek=['43,85','43.85','40,29','40.29','25,49','25.49','28,90','28.90','58,2','58.2','18,6','18.6'];
async function snapshot(p){return await p.evaluate(seek=>{
 const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);const leaks=[];
 while(w.nextNode()){const n=w.currentNode;if(['SCRIPT','STYLE','NOSCRIPT'].includes(n.parentElement.tagName))continue;
   if(seek.some(s=>n.textContent.includes(s)))leaks.push({el:n.parentElement.id||n.parentElement.tagName,text:n.textContent.trim().slice(0,200)});}
 const attrs=[];for(const el of document.querySelectorAll('*'))for(const a of ['title','aria-label','aria-valuetext']){const v=el.getAttribute(a);if(v&&seek.some(s=>v.includes(s)))attrs.push({el:el.id,a,v});}
 return {leaks,attrs,ansage:document.querySelector('#ansage').textContent,title:document.title};
},seek);}
async function layout(p){return await p.evaluate(()=>{
 const w=innerWidth;const overflow=[...document.querySelectorAll('body *')].filter(el=>{
  if(!el.getClientRects().length||getComputedStyle(el).position==='absolute')return false;
  const r=el.getBoundingClientRect();return r.left<-.5||r.right>w+.5;
 }).slice(0,15).map(el=>({id:el.id,tag:el.tagName,right:el.getBoundingClientRect().right}));
 return {width:w,scrollWidth:document.documentElement.scrollWidth,overflow};
});}
async function chartClipping(p){return await p.evaluate(()=>{
const s=document.querySelector('#dia'),v=s.viewBox.baseVal,r=s.getBoundingClientRect();return [...s.querySelectorAll('text')].map(n=>{
 const b=n.getBoundingClientRect();return {text:n.textContent,x:(b.left-r.left)*v.width/r.width,y:(b.top-r.top)*v.height/r.height,w:b.width*v.width/r.width,h:b.height*v.height/r.height,svgW:v.width,svgH:v.height};
}).filter(b=>b.x<0||b.y<0||b.x+b.w>v.width+.5||b.y+b.h>v.height+.5);
});}
async function scan(p){await p.evaluate(axe);return await p.evaluate(async()=>{
 const r=await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa']}});
 return {violations:r.violations.map(v=>({id:v.id,impact:v.impact,description:v.description,nodes:v.nodes.map(n=>({target:n.target,failureSummary:n.failureSummary}))})),incomplete:r.incomplete.map(v=>v.id),passes:r.passes.length};
});}
async function commit1(p,withValues=true){await p.locator('input[name=tasse][value="1"]').check();await p.locator('input[name=grund][value="h"]').check();
 if(withValues){await p.locator('#e1').fill('43,85');await p.locator('#e2').fill('40.29');}await p.locator('#s1-knopf').click();}
async function commit2(p,answer='b'){await p.locator(`input[name=warum][value="${answer}"]`).check();await p.locator('#s2-knopf').click();}
async function field(p,id,v){await p.locator('#rf-'+id).fill(String(v));await p.locator('#rf-'+id).press('Enter');}
async function saveView(p,name,focus){if(focus)await p.locator(focus).scrollIntoViewIfNeeded();await p.screenshot({path:path.join(H,name+'.png')});}
(async()=>{
 const b=await chromium.launch({executablePath:process.env.X6_CHROMIUM||'/usr/bin/chromium',headless:true,args:['--no-sandbox']});result.browser=b.version();
 for(const [width,height] of [[390,844],[1366,768],[1280,720]])for(const lang of ['de','en']){
  const c=await b.newContext({viewport:{width,height},offline:true});const requests=[],errors=[],consoleErrors=[];
  await c.route('**/*',r=>r.request().url().startsWith('http://127.0.0.1:8765/')?r.fulfill({contentType:'text/html',body:html}):r.abort());
  const p=await c.newPage();p.setDefaultTimeout(7000);p.on('request',r=>requests.push(r.url()));p.on('pageerror',e=>errors.push(e.message));p.on('console',m=>{if(m.type()==='error')consoleErrors.push(m.text());});
  const run={width,height,lang,states:[],controls:[],measurements:[],requests,errors,consoleErrors};result.laeufe.push(run);
  try{
   await p.goto('http://127.0.0.1:8765/?lang='+lang);await p.evaluate(()=>document.fonts.ready);
   run.states.push({state:'Z0',snapshot:await snapshot(p),layout:await layout(p),axe:await scan(p)});
   await saveView(p,`start_${width}_${lang}`);
   assert.equal(await p.locator('#s1-knopf').isDisabled(),true);
   await p.locator('input[name=tasse][value="1"]').check();assert.equal(await p.locator('#s1-knopf').isDisabled(),true);
   await p.locator('input[name=grund][value="x"]').check();assert.equal(await p.locator('#s1-knopf').isEnabled(),true);
   await p.locator('#e1').fill('abc');await p.locator('#s1-knopf').click();assert.equal(await p.locator('#e1').getAttribute('aria-invalid'),'true');
   await commit1(p);
   run.states.push({state:'Z1',snapshot:await snapshot(p),bars:await p.locator('#saeulen').textContent(),barLabel:await p.locator('#saeulen').getAttribute('aria-label'),layout:await layout(p),axe:await scan(p)});
   assert(!/kJ/.test(await p.locator('#saeulen').textContent()));
   await p.locator('#zum-modell').click();run.modelLinkZ1={hash:await p.evaluate(()=>location.hash),hidden:await p.locator('#modell').isHidden()};
   await commit2(p);
   assert.equal(await p.locator('#rr-thM').getAttribute('max'),'30');
   await field(p,'thM','70');run.hotLocked={invalid:await p.locator('#rf-thM').getAttribute('aria-invalid'),state:await p.evaluate(()=>KAFFEE.zustand().e.thM)};
   assert.equal(run.hotLocked.state,5);
   await field(p,'thM','5');
   run.states.push({state:'Z2',layout:await layout(p),axe:await scan(p),barText:await p.locator('#saeulen').textContent()});
   await saveView(p,`ergebnis_${width}_${lang}`,'#buehne');
   // Alle Regler: beide Grenzen, Plus/Minus, Komma/Punkt, Pfeil/Home/End/Page, Ziehen.
   await p.locator('#gruppe summary').click();
   const specs=[['thM',2,30,5.5],['tZ',1,180,61],['thK0',60,95,80.5],['thU',10,30,20.5],['kA',.05,.8,.2345],['VM_ml',10,100,35]];
   for(const [id,min,max,mid] of specs){
    const r=p.locator('#rr-'+id),check={id};
    await field(p,id,String(mid).replace('.',','));check.comma=await p.evaluate(id=>KAFFEE.zustand().e[id],id);assert.equal(check.comma,mid);
    await field(p,id,String(mid));check.point=await p.evaluate(id=>KAFFEE.zustand().e[id],id);assert.equal(check.point,mid);
    await p.locator('#rplus-'+id).click();check.plus=await p.evaluate(id=>KAFFEE.zustand().e[id],id);
    await p.locator('#rminus-'+id).click();check.minus=await p.evaluate(id=>KAFFEE.zustand().e[id],id);
    for(const key of ['Home','ArrowRight','PageUp','PageDown','End','ArrowLeft']){await r.press(key);check[key]=await p.evaluate(id=>KAFFEE.zustand().e[id],id);}
    assert.equal(check.Home,min);assert.equal(check.End,max);
    const box=await r.boundingBox();await p.mouse.move(box.x+box.width*.65,box.y+box.height/2);await p.mouse.down();await p.mouse.move(box.x+box.width*.35,box.y+box.height/2,{steps:5});await p.mouse.up();
    check.drag=await p.evaluate(id=>KAFFEE.zustand().e[id],id);
    await field(p,id,max+100);check.invalid=await p.locator('#rf-'+id).getAttribute('aria-invalid');assert.equal(check.invalid,'true');
    run.controls.push(check);await field(p,id,mid);
   }
   await p.locator('#knopf-blatt').click();assert.equal(await p.locator('#rf-kA').inputValue(),lang==='de'?'0,1994':'0.1994');
   await p.locator('#gruppe summary').click();
   for(const [id,v] of [['m1','72,5 x 60.6 55,7 51.4 47,6 44.2'],['m2','80 72 65.1 59,1 53.9 49,3 45.4 41,4'],['m1','-1'],['m1','101'],['m1','NaN'],['m1','1 2 3 4 5 6 7 8'],['m2','1 2 3 4 5 6 7 8 9'],['m1','<img src=https://example.org/x>'],['m2','20 90'],['m1',''],['m2','']]){
    await p.locator('#'+id).fill(v);run.measurements.push({id,v,text:await p.locator('#'+id+'-info').textContent(),invalid:await p.locator('#'+id).getAttribute('aria-invalid')});
   }
   await p.locator('#beispiel').check();await p.locator('#ln').check();
   run.ln={clipping:await chartClipping(p),description:await p.locator('#dia-beschreibung').textContent()};
   await saveView(p,`ln_${width}_${lang}`,'#buehne');
   await p.locator('#ln').uncheck();
   await p.locator('#m1').fill('70,5 x 60.6');await p.reload();await p.evaluate(()=>document.fonts.ready);
   assert.equal(await p.locator('#m1').inputValue(),'70,5 x 60.6');assert.equal(await p.locator('#beispiel').isChecked(),true);assert.equal(await p.locator('#s1-offen').isHidden(),true);
   await p.locator('#s4-text').fill(lang==='de'?'Die Simulation zeigt Modellfälle; der Versuch prüft die Wirklichkeit.':'The simulation shows model cases; the experiment tests reality.');await p.locator('#s4-knopf').click();
   for(const n of [1,2,3]){
    await p.locator('#a'+n+' summary').click();await p.locator('#a'+n+'-knopf').click();assert((await p.locator('#a'+n+'-meldung').textContent()).length>0);
    if(n===2)await p.locator('#a2-zahl').fill('95');else await p.locator(`input[name=a${n}][value="1"]`).check();
    await p.locator('#a'+n+'-knopf').click();assert.equal((await p.evaluate(()=>KAFFEE.zustand().e.tZ)),60);
    if(n===3){await field(p,'thM','70');assert.equal((await p.evaluate(()=>KAFFEE.zustand().e.thM)),70);}
    await p.locator('#a'+n+'-ged-knopf').click();
   }
   await p.locator('#modell summary').click();
   run.states.push({state:'alle_Auftraege_und_Modell',layout:await layout(p),axe:await scan(p)});
   // Englische/deutsche Wechsel auch nach vollen Eingaben.
   await p.locator('#sprache').click();await p.locator('#sprache').click();assert.equal(await p.locator('html').getAttribute('lang'),lang);
   await p.locator('#buehne').scrollIntoViewIfNeeded();
   // Reset darf keine Ergebnisse im DOM oder Status zurücklassen.
   await field(p,'thM','5');await p.waitForTimeout(100);p.once('dialog',d=>d.accept());await p.locator('#von-vorn').click();await p.waitForTimeout(100);
   run.states.push({state:'Z0_nach_Von_vorn',snapshot:await snapshot(p),layout:await layout(p),axe:await scan(p)});
   await saveView(p,`reset_${width}_${lang}`);
   run.resetHtml=await p.evaluate(()=>({kern:document.querySelector('#kern').textContent,kernsatz:document.querySelector('#kernsatz').textContent,saeulen:document.querySelector('#saeulen').textContent}));
  }catch(e){run.failure=e.stack;result.fehler.push({width,lang,error:e.message});}
  fs.writeFileSync(path.join(H,'browser_ergebnis.json'),JSON.stringify(result,null,2)+'\n');await c.close();
 }
 // Gesperrter Speicher: Bedienung bleibt möglich; Hinweis und Reset funktionieren.
 const c=await b.newContext({viewport:{width:390,height:844},offline:true});
 await c.route('**/*',r=>r.fulfill({contentType:'text/html',body:html}));
 await c.addInitScript(()=>{Object.defineProperty(window,'localStorage',{get(){throw new DOMException('Blocked','SecurityError')}});});
 const p=await c.newPage();await p.goto('http://127.0.0.1:8765/');await commit1(p,false);await commit2(p,'c');
 result.gesperrterSpeicher={text:await p.locator('#speicher-text').textContent(),werte:await p.locator('#kern').innerText()};
 p.once('dialog',d=>d.accept());await p.locator('#von-vorn').click();assert(await p.locator('#s1-offen').isVisible());
 await p.reload();assert(await p.locator('#s1-offen').isVisible());await c.close();
 await b.close();fs.writeFileSync(path.join(H,'browser_ergebnis.json'),JSON.stringify(result,null,2)+'\n');
 console.log(JSON.stringify({browser:result.browser,laeufe:result.laeufe.map(r=>({width:r.width,lang:r.lang,failure:r.failure,requests:r.requests,errors:r.errors,
   axe:r.states.map(s=>({state:s.state,violations:s.axe.violations})),reset:r.states.find(s=>s.state==='Z0_nach_Von_vorn')?.snapshot,ln:r.ln})),fehler:result.fehler},null,2));
})().catch(e=>{console.error(e);process.exit(1)});
