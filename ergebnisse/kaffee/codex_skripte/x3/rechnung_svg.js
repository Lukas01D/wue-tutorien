// Prüft die sichtbaren Zahlen und sämtliche 161 SVG-Stützpunkte beider Kurven.
// Sollwerte stammen ausschließlich aus rechnung_unabhaengig.py.
// Aufruf: node ergebnisse/kaffee/codex_skripte/x3/rechnung_svg.js
const fs=require('fs');
const path=require('path');
const {chromium}=require('playwright');
const here=__dirname;
const root=path.resolve(here,'../../../..');
const data=JSON.parse(fs.readFileSync(path.join(here,'rechnung_ergebnis.json'),'utf8'));
const fmt=(x,n)=>x.toFixed(n).replace('.',',').replace('-','−');
const ids={tEnd:'tEnd_min',thM:'thM',VM:'VM_ml',thU:'thU',thK0:'thK0',thMess:'thMess',VK:'VK_ml',kA1:'kA1Faktor',mB:'mB_g'};
(async()=>{
  const browser=await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});
  const ctx=await browser.newContext({viewport:{width:1366,height:900},offline:true});
  const localUrl='http://localhost:31460/kaffee-x3-rechnung';
  const html=fs.readFileSync(path.join(root,'ergebnisse/kaffee/simulation/Kaffee_Simulation.html'),'utf8');
  const requests=[];
  await ctx.route('**/*',route=>{
    // Die verwaltete Browser-Policy sperrt file://. Nur diese virtuelle lokale
    // Seite aus den unveränderten Dateibytes bedienen, kein HTTP-Server nötig.
    if(route.request().url()===localUrl)return route.fulfill({status:200,contentType:'text/html; charset=utf-8',body:html});
    if(/^https?:/.test(route.request().url())){ requests.push(route.request().url());return route.abort(); }
    return route.continue();
  });
  const page=await ctx.newPage();
  const errors=[];page.on('pageerror',e=>errors.push(String(e)));
  await page.goto(localUrl);
  const rows=[];
  for(const row of data.results){
    const e=row.settings,m=row.expected;
    await page.evaluate(({e,ids})=>{
      for(const [id,key] of Object.entries(ids)){
        const input=document.getElementById(id);
        input.value=e[key]*(id==='kA1'?100:1);
      }
      document.getElementById('becher').checked=e.becher;
      document.getElementById('milch2Raum').checked=e.milch2Raum;
      document.getElementById('tEnd').dispatchEvent(new Event('input',{bubbles:true}));
    },{e,ids});
    const got=await page.evaluate(()=>{
      const svg=document.getElementById('diagramm');
      return {numbers:[...document.querySelectorAll('.zahl')].map(x=>x.innerText.split('\n')),
        viewBox:svg.getAttribute('viewBox').split(' ').map(Number),
        curves:[...svg.querySelectorAll('polyline')].map(x=>x.getAttribute('points').split(' ').map(p=>p.split(',').map(Number))),
        lines:[...svg.querySelectorAll('line')].map(x=>Object.fromEntries(['x1','x2','y1','y2','stroke-dasharray'].map(a=>[a,x.getAttribute(a)]))),
        warning:document.getElementById('warnung').innerText};
    });
    const crossExpected=row.expected_cross_min>0&&row.expected_cross_min<e.tEnd_min?fmt(row.expected_cross_min,1)+' min':'keiner bis zur Zugabe';
    const expectedNumbers=[
      ['Tasse 1 nach '+fmt(e.tEnd_min,0)+' min','ϑ₁ = '+fmt(m.th1,2)+' °C','Mischung bei 0 min: '+fmt(m.T1_0-273.15,2)+' °C'],
      ['Tasse 2 nach '+fmt(e.tEnd_min,0)+' min','ϑ₂ = '+fmt(m.th2,2)+' °C','vor dem Zugießen: '+fmt(m.T2_K-273.15,2)+' °C'],
      ['Unterschied','ϑ₁ − ϑ₂ = '+fmt(m.dT,2)+' K',Math.abs(m.dT)<.005?'gleich warm':m.dT>0?'Tasse 1 ist wärmer':'Tasse 2 ist wärmer'],
      ['Abgegebene Wärme','Q₁ = '+fmt(m.Q1/1000,2)+' kJ','Q₂ = '+fmt(m.Q2/1000,2)+' kJ, Q₂ − Q₁ = '+fmt((m.Q2-m.Q1)/1000,2)+' kJ'],
      ['Schnittpunkt',crossExpected,'ab hier ist der schwarze Kaffee kühler'],
      ['kA aus der Messung',fmt(m.kA,4)+' W/K',e.becher?'mit Becher (wie Teil g)':'ohne Becher (wie Teil c)']];
    const mismatches=[];
    for(let i=0;i<6;i++) for(let j=0;j<3;j++){
      if(got.numbers[i][j]!==expectedNumbers[i][j])mismatches.push({card:i,line:j,expected:expectedNumbers[i][j],actual:got.numbers[i][j]});
    }
    const [, ,W,H]=got.viewBox,L=48,R=12,O=14,U=42,xMax=e.tEnd_min*1.03+.5;
    const ys=[e.thU,e.thK0,m.th2,m.th1,m.T2_K-273.15];
    let yMin=Math.min(...ys)-3,yMax=Math.max(...ys)+3;
    const step=yMax-yMin>40?10:5;
    yMin=Math.floor(yMin/step)*step;yMax=Math.ceil(yMax/step)*step;
    const X=t=>L+(W-L-R)*t/xMax,Y=t=>O+(H-O-U)*(yMax-t)/(yMax-yMin);
    let maxPixelError=0;
    const wantCurves=[row.expected_curves.schwarz,row.expected_curves.tasse1];
    for(let c=0;c<2;c++) for(let i=0;i<161;i++){
      const [x,y]=got.curves[c][i];
      maxPixelError=Math.max(maxPixelError,Math.abs(x-X(row.expected_curves.times[i])),Math.abs(y-Y(wantCurves[c][i])));
    }
    const mixLines=got.lines.filter(x=>x['stroke-dasharray']==='2 3');
    const jump=[{x:X(0),y1:Y(e.thK0),y2:Y(m.T1_0-273.15)},
      {x:X(e.tEnd_min),y1:Y(m.T2_K-273.15),y2:Y(m.th2)}];
    let maxJumpError=0;
    for(let i=0;i<2;i++){
      const actual=mixLines[i],want=jump[i];
      maxJumpError=Math.max(maxJumpError,Math.abs(+actual.x1-want.x),Math.abs(+actual.x2-want.x),Math.abs(+actual.y1-want.y1),Math.abs(+actual.y2-want.y2));
    }
    rows.push({name:row.name,numberMismatches:mismatches,maxPixelError,maxJumpError,warning:got.warning});
    if(row.name==='umgekehrter_schnitt'){
      await page.screenshot({path:path.join(here,'rechnung_schnitt_fehlt.png'),fullPage:true});
    }
  }
  await browser.close();
  const result={cases:rows.length,externalRequests:requests,pageErrors:errors,results:rows};
  fs.writeFileSync(path.join(here,'rechnung_svg_ergebnis.json'),JSON.stringify(result,null,2)+'\n');
  console.log(JSON.stringify({cases:rows.length,externalRequests:requests,pageErrors:errors,
    maxPixelError:Math.max(...rows.map(r=>r.maxPixelError)),maxJumpError:Math.max(...rows.map(r=>r.maxJumpError)),
    mismatches:rows.filter(r=>r.numberMismatches.length)},null,2));
})().catch(err=>{console.error(err);process.exitCode=1;});
