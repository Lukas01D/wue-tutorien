// Vergleicht unabhängig berechnete JSON-Sollwerte mit dem ausgelieferten HTML.
const fs = require('fs'), path = require('path'), vm = require('vm'), assert = require('assert/strict');
const H = __dirname;
const html = fs.readFileSync(path.join(H,'../site/index.html'),'utf8');
const js = html.match(/<script>([\s\S]*?)<\/script>/)[1].split('const TEXTE')[0];
const ctx = vm.createContext({});
vm.runInContext(js + ';globalThis.api={auswerten,STANDARD,kABlatt,BEISPIEL}', ctx);
const daten = JSON.parse(fs.readFileSync(path.join(H,'eigenrechnung.json')));
vm.runInContext('const TEXTE'+html.split('const TEXTE')[1].split('\nconst BAU')[0]+';globalThis.texte=TEXTE',ctx);
const fehler = []; let maxRel = 0, vergleiche = 0;
for(const f of daten.faelle){
  const ist = ctx.api.auswerten(f.eingabe);
  ist.kurven = [0,60,600,1800,3600,f.eingabe.tZ*60].map(t=>[ist.kurve1(t),ist.kurve2(t)]);
  for(const k of Object.keys(f.soll)){
    const aa = Array.isArray(f.soll[k]) ? f.soll[k].flat() : [f.soll[k]];
    const bb = Array.isArray(ist[k]) ? ist[k].flat() : [ist[k]];
    aa.forEach((a,i)=>{const rel=Math.abs(a-bb[i])/Math.max(Math.abs(a),1e-12); maxRel=Math.max(maxRel,rel);vergleiche++;
      if(rel>=1e-9)fehler.push({fall:f.name,k,position:i,soll:a,ist:bb[i],rel});});
  }
}
// Zahlen der Rückmeldungen und Modelltexte gegen die eigene Rechnung.
const s=daten.faelle[0].soll,z=daten.zusatz;
const textwerte={s2_rueck_a:[[s.Q1/1000,2],[s.Q2/1000,2],[z.dQ_kJ,2],[s.C_G,1],[s.dT,2]],
 s2_rueck_b:[[z.sprung1,1],[z.sprung2,1]],a1_gedanken:[[s.dT,2],[z.raummilch.dT,2]],
 a2_gedanken:[[z.maximum_min,0],[z.maximum_K,2],[z.grenz_K,2]],
 a3_gedanken:Object.values(z.kipp).map(n=>[n,1]),m_pruef:[[s.kA,4],[z.trink_min,1]]};
let texteGeprueft=0;
for(const lang of ['de','en'])for(const [key,values] of Object.entries(textwerte))for(const [n,stellen] of values){
 let soll=n.toFixed(stellen);if(lang==='de')soll=soll.replace('.',',');texteGeprueft++;
 if(!ctx.texte[lang][key].includes(soll))fehler.push({lang,key,soll,text:ctx.texte[lang][key]});
}
const r={faelle:daten.faelle.length,vergleiche,maxRel,texteGeprueft,fehler,standard:ctx.api.STANDARD};
fs.writeFileSync(path.join(H,'zahlen_ergebnis.json'),JSON.stringify(r,null,2)+'\n');
console.log(r); assert.equal(fehler.length,0);
