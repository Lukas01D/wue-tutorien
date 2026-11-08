// Eigener Werkzeugdurchgang: stdin enthält JS-Browseraktionen, jede Aktion wird protokolliert.
const {chromium}=require('playwright'),fs=require('fs'),path=require('path'),readline=require('readline');
(async()=>{
 const b=await chromium.launch({executablePath:process.env.X6_CHROMIUM||'/usr/bin/chromium',headless:true,args:['--no-sandbox']});
 const c=await b.newContext({viewport:{width:390,height:844},offline:true});
 const p=await c.newPage();const start=Date.now();
 await c.route('**/*',route=>route.request().url()==='http://127.0.0.1:8765/'
   ?route.fulfill({contentType:'text/html',body:fs.readFileSync(path.resolve(__dirname,'../site/index.html'))})
   :route.abort());
 await p.goto('http://127.0.0.1:8765/');await p.evaluate(()=>document.fonts.ready);
 const log=path.join(__dirname,'pflichtweg.jsonl');fs.writeFileSync(log,'');
 console.log('BEREIT',await p.locator('body').innerText());
 const rl=readline.createInterface({input:process.stdin});let chain=Promise.resolve();
 rl.on('line',line=>{chain=chain.then(async()=>{
  if(line==='ENDE'){await b.close();rl.close();process.exit(0);}
  const sec=(Date.now()-start)/1000;
  try{const result=await eval('(async()=>{'+line+'})()');console.log(JSON.stringify({sec,result}));
    fs.appendFileSync(log,JSON.stringify({sec,aktion:line,result})+'\n');
  }catch(e){console.log('FEHLER',e.message);}
 });});
})().catch(e=>{console.error(e);process.exit(1)});
