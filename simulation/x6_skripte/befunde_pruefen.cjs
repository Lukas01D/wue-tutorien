// Gezielte Reproduktion nach dem breiten Test. Misst auch transformierte SVG-Texte korrekt.
const fs=require('fs'),path=require('path'),{chromium}=require('playwright');
(async()=>{
 const b=await chromium.launch({executablePath:process.env.X6_CHROMIUM||'/usr/bin/chromium',headless:true,args:['--no-sandbox']});
 const out=[];
 for(const lang of ['de','en']){
 const c=await b.newContext({viewport:{width:390,height:844},offline:true});
 await c.route('**/*',r=>r.fulfill({contentType:'text/html',body:fs.readFileSync(path.join(__dirname,'../site/index.html'))}));
 const p=await c.newPage();await p.goto('http://127.0.0.1:8765/?lang='+lang);await p.evaluate(()=>document.fonts.ready);
 await p.check('[name=tasse][value="1"]');await p.check('[name=grund][value="h"]');await p.click('#s1-knopf');
 await p.click('#zum-modell');const linkZ1=await p.evaluate(()=>({hash:location.hash,hidden:document.querySelector('#modell').hidden}));
 await p.check('[name=warum][value="a"]');await p.click('#s2-knopf');
 await p.check('#beispiel');await p.check('#ln');
 const clipping=await p.evaluate(()=>{const s=document.querySelector('#dia'),r=s.getBoundingClientRect();return [...s.querySelectorAll('text')].map(n=>{const b=n.getBoundingClientRect();return {text:n.textContent,right:b.right-r.left,left:b.left-r.left,top:b.top-r.top,bottom:b.bottom-r.top,width:r.width,height:r.height};}).filter(n=>n.left<0||n.right>n.width+.5||n.top<0||n.bottom>n.height+.5);});
 await p.evaluate(()=>document.querySelector('#buehne').scrollIntoView({block:'start'}));await p.screenshot({path:path.join(__dirname,'befund_ln_390_'+lang+'.png')});
 await p.uncheck('#ln');await p.fill('#rf-thM','6');await p.press('#rf-thM','Enter');await p.waitForTimeout(100);
 p.once('dialog',d=>d.accept());await p.click('#von-vorn');await p.waitForTimeout(100);
 const reset=await p.evaluate(()=>({zustand:KAFFEE.zustand().z,ansage:document.querySelector('#ansage').textContent,
  kern:document.querySelector('#kern').textContent,saeulen:document.querySelector('#saeulen').textContent,
  aria:document.querySelector('#saeulen').getAttribute('aria-label')}));
 const accessibility=await p.locator('#ansage').ariaSnapshot();
 // Sofortiger Reset während eine neue Ansage noch aussteht.
 await p.check('[name=tasse][value="1"]');await p.check('[name=grund][value="h"]');await p.click('#s1-knopf');
 await p.check('[name=warum][value="a"]');await p.click('#s2-knopf');
 p.once('dialog',d=>d.accept());
 await p.evaluate(()=>{document.querySelector('#rplus-thM').click();document.querySelector('#von-vorn').click();});await p.waitForTimeout(150);
 const race=await p.locator('#ansage').textContent();
 out.push({lang,linkZ1,clipping,reset,accessibility,race});await c.close();
 }
 await b.close();fs.writeFileSync(path.join(__dirname,'befunde_ergebnis.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out,null,2));
})().catch(e=>{console.error(e);process.exit(1)});
