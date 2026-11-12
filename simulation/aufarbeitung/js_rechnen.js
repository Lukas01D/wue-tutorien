// Rechnet mit dem Code der GEBAUTEN Seiten (ohne Browser), damit genau das geprüft wird, was veröffentlicht ist.
// Aufruf: node js_rechnen.js < auftrag.json > ergebnis.json
// Auftrag: { schlank: [Einstellung, ...], haupt: [Einstellung, ...] }
//   schlank: { t, tZ, thM, VM_ml, thK0, VK_ml, thU, QW, kA, CT } (Zeiten in min), Ergebnis mit Werten bei t und Stichproben der Kurven
//   haupt:   { thK0, thM, thU, VM_ml, kA, tZ } wie auswerten() der Hauptseite
// Aus der schlanken Seite werden modell.js (vor „const TEXTE“) und aus dem Seitenskript die Funktionen modell, obergrenze,
// bereichNr sowie REGLER und VERGLEICH unverändert herausgeschnitten und in einer leeren Umgebung (vm) ausgeführt.
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const SIM = path.join(__dirname, '..');
const SCHLANK = path.join(SIM, 'minimal', 'Kaffee_Simulation_schlank.html');
const HAUPT = path.join(SIM, 'site', 'index.html');

function skript(datei) {
  const h = fs.readFileSync(datei, 'utf8');
  const a = h.indexOf('<script>') + '<script>'.length;
  return h.slice(a, h.indexOf('</script>', a));
}
function schneide(js, anfang, ende) {          // Text von „anfang“ bis einschließlich „ende“ (erstes Vorkommen danach)
  const a = js.indexOf(anfang);
  if (a < 0) throw new Error('nicht gefunden: ' + anfang);
  const b = js.indexOf(ende, a);
  if (b < 0) throw new Error('kein Ende nach: ' + anfang);
  return js.slice(a, b + ende.length);
}

const sjs = skript(SCHLANK);
const kernS = sjs.slice(0, sjs.indexOf('const TEXTE = '));
const teile = [
  schneide(sjs, 'const REGLER = [', '\n  ];'),
  schneide(sjs, 'const VERGLEICH = {', '\n  };'),
  schneide(sjs, 'function bereichNr(', '}\n'),
  schneide(sjs, 'function modell(e) {', '\n  }\n'),
  schneide(sjs, 'function obergrenze(r) {', '\n  }\n')
].join('\n');
const ctxS = vm.createContext({ Math, Number, Object, Infinity, isFinite, S: { e: {} } });
vm.runInContext(kernS + '\n' + teile + '\n;globalThis.__ = { modell, obergrenze, bereichNr, REGLER, VERGLEICH, KA: kABlatt(), STANDARD };', ctxS);
const S = ctxS.__;

const hjs = skript(HAUPT);
const ctxH = vm.createContext({ Math, Number, Object, Infinity, isFinite });
vm.runInContext(hjs.slice(0, hjs.indexOf('const TEXTE = ')) + '\n;globalThis.__ = { auswerten, KA: kABlatt(), STANDARD };', ctxH);
const H = ctxH.__;

function schlank(e) {
  const m = S.modell(e);
  const n = 60, k1 = [], k2 = [];
  for (let i = 0; i <= n; i++) { const t = e.t * i / n; k1.push(m.th1(t)); k2.push(m.th2(t)); }
  ctxS.S.e = e;
  const QW = S.REGLER.find(r => r.id === 'QW'), kA = S.REGLER.find(r => r.id === 'kA'), CT = S.REGLER.find(r => r.id === 'CT');
  return { kA: m.kA, CK: m.CK, CG: m.CG, th10: m.th10, th2K: m.th2K, th2Z: m.th2Z, th1: m.th1(e.t), th2: m.th2(e.t),
           Q1: m.Q1(e.t), Q2: m.Q2(e.t), k1: k1, k2: k2,
           Q1min: Math.min(...k1.map((_, i) => m.Q1(e.t * i / n))), Q2min: Math.min(...k2.map((_, i) => m.Q2(e.t * i / n))),
           QWmax: S.obergrenze(QW), bereich_kA: S.bereichNr(kA, e.kA), bereich_CT: S.bereichNr(CT, e.CT) };
}
function haupt(e) {
  const r = H.auswerten(e), o = {};
  for (const k in r) if (typeof r[k] === 'number') o[k] = r[k];
  return o;
}

let ein = '';
process.stdin.on('data', d => { ein += d; });
process.stdin.on('end', () => {
  const a = JSON.parse(ein || '{}');
  process.stdout.write(JSON.stringify({
    KA_schlank: S.KA, KA_haupt: H.KA, STANDARD: S.STANDARD,
    REGLER: S.REGLER.map(r => ({ id: r.id, min: r.min, max: r.max, schritt: r.schritt })),
    VERGLEICH: S.VERGLEICH,
    schlank: (a.schlank || []).map(schlank), haupt: (a.haupt || []).map(haupt)
  }));
});
