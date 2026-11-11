// Browsertest der Kaffee-Seite Fassung 3 (Chromium über Playwright, axe-core 4.14.0 für WCAG 2.0, 2.1, 2.2 A und AA).
// Aufruf: node simulation/tests/browsertest.js   (vorher einmal: cd simulation/tests && npm ci). Ergebnis: browsertest_ergebnis.txt
// Andere Datei prüfen: KAFFEE_DATEI=<pfad zu index.html> node simulation/tests/browsertest.js
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const DATEI = path.resolve(process.env.KAFFEE_DATEI || path.join(__dirname, '../site/index.html'));
const URL = 'file://' + DATEI;
const AXE = fs.readFileSync(require.resolve('axe-core/axe.min.js'), 'utf8');
const GROESSE_F2 = 433303;       // Fassung 2 (simulation/site vor Fassung 3)
const ERGEBNISSE_DE = ['43,01', '36,31', '6,69', '51,51', '55,49', '15,50', '23,82', '8,31', '0,1994', '17,4', '63,2', '56,78', '57,55', '4,97', '8,83'];
const ergebnisse = [];
let browser;

function pruefe(name, ok, info) { ergebnisse.push([name, !!ok, info || '']); }

async function seite(opt = {}) {
  // bypassCSP nur, damit axe-core eingefügt werden kann; die CSP selbst prüft der Test „CSP greift“ ohne diese Option
  const ctx = await browser.newContext({ viewport: { width: opt.w || 1366, height: opt.h || 768 }, bypassCSP: opt.csp !== true, ...(opt.ctx || {}) });
  if (opt.init) await ctx.addInitScript(opt.init);
  const p = await ctx.newPage();
  p.fehler = [];
  p.anfragen = [];
  p.on('pageerror', e => p.fehler.push(e.message));
  p.on('console', m => { if (m.type() === 'error') p.fehler.push(m.text()); });
  p.on('request', r => { if (!r.url().startsWith('file:') && !r.url().startsWith('data:')) p.anfragen.push(r.url()); });
  p.on('dialog', d => d.accept());
  await p.goto(URL + (opt.q || ''));
  await p.evaluate(() => document.fonts.ready);
  return p;
}
async function start(p, e1, e2) {
  await p.check('input[name=tasse][value="1"]');
  await p.check('input[name=grund][value="h"]');
  if (e1 !== undefined) await p.fill('#e1', e1);
  if (e2 !== undefined) await p.fill('#e2', e2);
  await p.click('#s1-knopf');
}
async function erklaere(p, wahl = 'a') { await p.check(`input[name=warum][value="${wahl}"]`); await p.click('#s2-knopf'); }
const text = (p, sel) => p.$eval(sel, el => el.textContent);
const sichtbar = (p, sel) => p.$eval(sel, el => !!(el.getClientRects().length) && getComputedStyle(el).visibility !== 'hidden');
async function axe(p, name) {
  await p.addScriptTag({ content: AXE });
  const r = await p.evaluate(async () => (await axe.run(document, { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'] } })).violations.map(v => v.id + ' (' + v.nodes.length + ')'));
  pruefe('axe-core ohne Verstoß: ' + name, r.length === 0, r.join(', '));
}

async function tests() {
  // ---------------------------------------------------------------- Datei
  {
    const groesse = fs.statSync(DATEI).size;
    pruefe('Datei kleiner als Fassung 2 (' + groesse + ' gegen ' + GROESSE_F2 + ' Bytes)', groesse < GROESSE_F2);
    const html = fs.readFileSync(DATEI, 'utf8');
    const csp = (html.match(/http-equiv="Content-Security-Policy" content="([^"]*)"/) || [])[1] || '';
    pruefe('CSP ohne fremde Quellen', /default-src 'none'/.test(csp) && /script-src 'sha256-/.test(csp) && !/https?:|\*/.test(csp), csp.slice(0, 80));
    const p = await seite({ csp: true });
    await start(p); await erklaere(p); await p.click('#gruppe summary');
    pruefe('CSP greift: ganzer Pflichtweg ohne CSP-Verstoß und ohne Anfragen nach außen', p.fehler.length === 0 && p.anfragen.length === 0, p.fehler.concat(p.anfragen).join('; '));
    await p.context().close();
  }
  // ---------------------------------------------------------------- Z0: Sperre
  {
    const p = await seite();
    const body = await p.evaluate(() => { const c = document.body.cloneNode(true); c.querySelectorAll('script').forEach(s => s.remove()); return c.innerHTML; });
    const gefunden = ERGEBNISSE_DE.filter(z => body.includes(z));
    pruefe('Z0: keine Ergebniszahl im DOM (auch versteckt, auch Attribute)', gefunden.length === 0, gefunden.join(', '));
    pruefe('Z0: keine Kurven, keine Säulen, keine Regler', await p.evaluate(() => !document.querySelector('#dia polyline') && !document.querySelector('#saeulen rect') && document.querySelectorAll('#regler-sichtbar input[type=range]').length === 2 && document.getElementById('regler-bereich').hidden));
    pruefe('Z0: nur Startkarte sichtbar (s2, s3, s4, Weiterdenken, Modell versteckt)', await p.evaluate(() => ['s2', 's3', 's4', 'weiter', 'modell'].every(id => document.getElementById(id).hidden)));
    pruefe('Z0: Knopf erst nach Tasse und Grund aktiv', await p.$eval('#s1-knopf', b => b.disabled));
    await p.check('input[name=tasse][value="2"]');
    pruefe('Z0: nur Tasse reicht nicht', await p.$eval('#s1-knopf', b => b.disabled));
    await p.check('input[name=grund][value="x"]');
    pruefe('Z0: „anderer Grund“ ohne Freitext reicht (T3)', !(await p.$eval('#s1-knopf', b => b.disabled)));
    await p.fill('#e1', '120');
    await p.click('#s1-knopf');
    pruefe('Z0: ungültige Ergebnisse aus e werden gemeldet', (await text(p, '#e-meldung')).length > 0 && await p.evaluate(() => window.KAFFEE.zustand().z === 0));
    pruefe('Z0: keine Konsolenfehler, keine fremden Anfragen', p.fehler.length === 0 && p.anfragen.length === 0, p.fehler.concat(p.anfragen).join('; '));
    await axe(p, 'Z0 Deutsch 1366');
    await p.context().close();
  }
  // ---------------------------------------------------------------- Z1 und Z2
  {
    const p = await seite();
    await start(p, '43,01', '36.31');
    pruefe('Z1: Kernzahlen wie Prüfwerte', (await text(p, '#w1')) === '43,01 °C' && (await text(p, '#w2')) === '36,31 °C' && (await text(p, '#wd')) === '6,69 K' && (await text(p, '#kern-zeit')) === 'nach 45 min');
    pruefe('Z1: Kernsatz „stimmen überein“', (await text(p, '#kernsatz')).startsWith('Simulation und deine Rechnung stimmen überein'));
    pruefe('Z1: zwei Kurven, Kreuze der eigenen Rechnung', await p.evaluate(() => document.querySelectorAll('#dia polyline').length === 2 && [...document.querySelectorAll('#dia text')].filter(t => t.textContent === '×').length === 2));
    pruefe('Z1: Direktbeschriftung beider Kurven', await p.evaluate(() => { const t = [...document.querySelectorAll('#dia text')].map(x => x.textContent); return t.includes('Tasse 1: Milch sofort') && t.includes('Tasse 2: Milch nach 45 min'); }));
    const saeulen = await p.$eval('#saeulen', s => s.textContent);
    pruefe('Z1: Säulen ohne Zahlen vor der Antwort (D4)', !/kJ|\d,\d/.test(saeulen) && (await p.$$('#saeulen rect')).length >= 2, saeulen);
    pruefe('Z1: Regler, Messung, Schluss, Weiterdenken noch gesperrt', await p.evaluate(() => ['s3', 's4', 'weiter', 'modell', 'regler-bereich'].every(id => document.getElementById(id).hidden)));
    const body = await p.evaluate(() => { const c = document.body.cloneNode(true); c.querySelectorAll('script').forEach(s => s.remove()); return c.innerHTML; });
    pruefe('Z1: Q-Werte, kA, Kipppunkt, Zeit bis 50 °C noch nicht im DOM', !['15,50', '23,82', '8,31', '0,1994', '63,2', '17,4', '4,97'].some(z => body.includes(z)));
    await axe(p, 'Z1 Deutsch 1366');
    await erklaere(p, 'a');
    const rueck = await text(p, '#s2-rueck');
    pruefe('Z2: Rückmeldung a mit Begründung und Q-Werten, Überleitung zu f', rueck.startsWith('Ja.') && rueck.includes('15,50') && rueck.includes('23,82') && rueck.includes('8,31') && rueck.includes('1241,8') && rueck.includes('f1 und f2'), rueck);
    pruefe('Z2: Säulen mit Zahlen', /15,50 kJ/.test(await p.$eval('#saeulen', s => s.textContent)) && /8,31 kJ/.test(await p.$eval('#saeulen', s => s.textContent)));
    pruefe('Z2: Antwort gesperrt, Regler, Messung, Schluss, Weiterdenken, Modell sichtbar', await p.evaluate(() => [...document.querySelectorAll('input[name=warum]')].every(x => x.disabled) && ['s3', 's4', 'weiter', 'modell', 'regler-bereich'].every(id => !document.getElementById(id).hidden)));
    pruefe('Z2: Modell nennt Prüfwerte aus d und h1', /0,1994 W\/K/.test(await text(p, '#modell')) && /17,4 min/.test(await text(p, '#modell')));
    // Regler
    pruefe('Regler: Milch bis 30 °C begrenzt vor Auftrag 3 (D3)', (await p.$eval('#rr-thM', e => e.max)) === '30' && (await text(p, '#rh-thM')).includes('Auftrag 3'));
    await p.fill('#rf-thM', '50'); await p.press('#rf-thM', 'Enter');
    pruefe('Regler: 50 °C im Feld wird abgelehnt', (await text(p, '#rm-thM')).includes('30') && await p.evaluate(() => window.KAFFEE.zustand().e.thM === 5));
    await p.fill('#rf-thM', '20,5'); await p.press('#rf-thM', 'Enter');
    pruefe('Regler: Komma im Feld', await p.evaluate(() => window.KAFFEE.zustand().e.thM === 20.5));
    await p.fill('#rf-tZ', '95.0'); await p.press('#rf-tZ', 'Enter');
    const erw = await p.evaluate(() => { const z = window.KAFFEE.zustand(); const r = window.KAFFEE.auswerten(z.e); return [r.th1, r.th2, r.dT]; });
    const fmt = x => x.toFixed(2).replace('.', ',').replace('-', '−');
    pruefe('Regler: Punkt im Feld, Anzeige folgt dem Modell', (await text(p, '#w1')) === fmt(erw[0]) + ' °C' && (await text(p, '#wd')) === fmt(erw[2]) + ' K' && (await text(p, '#kern-zeit')) === 'nach 95 min');
    pruefe('Regler: Kernsatz ohne Vergleich, wenn nicht die Werte des Blatts', (await text(p, '#kernsatz')).startsWith('Stimmt die Simulation mit deiner Rechnung überein'));
    await p.focus('#rr-tZ'); await p.keyboard.press('ArrowRight'); await p.keyboard.press('End');
    pruefe('Regler: Tastatur (Pfeil, Ende)', await p.evaluate(() => window.KAFFEE.zustand().e.tZ === 180));
    await p.click('#rminus-tZ');
    pruefe('Regler: Minus-Taste', await p.evaluate(() => window.KAFFEE.zustand().e.tZ === 179));
    pruefe('Regler: Wertansage mit Einheit', (await p.$eval('#rr-tZ', e => e.getAttribute('aria-valuetext'))) === '179 min');
    await p.click('#gruppe summary');
    await p.fill('#rf-kA', '0,3'); await p.press('#rf-kA', 'Enter');
    await p.fill('#rf-thK0', '90'); await p.press('#rf-thK0', 'Enter');
    const ka = await p.evaluate(() => window.KAFFEE.auswerten(window.KAFFEE.zustand().e).kA);
    pruefe('Regler: kA bleibt fest, wenn sich der Kaffee ändert', Math.abs(ka - 0.3) < 1e-12, String(ka));
    pruefe('Regler: Anzeige „entspricht … °C nach 10 min“', /entspricht \d+,\d °C nach 10 min/.test(await text(p, '#rh-kA')));
    await p.click('#knopf-blatt');
    pruefe('Regler: „Werte des Blatts“ setzt zurück', (await text(p, '#w1')) === '43,01 °C' && (await text(p, '#kernsatz')).startsWith('Simulation und deine Rechnung stimmen überein') && (await text(p, '#gruppe-zus')).includes('vorläufig'));
    // Messpunkte
    await p.fill('#m1', '72,1 66 x 55.9');
    await p.fill('#m2', '79,8 71,9 64,8 59 53,7 51,4 38,8');
    pruefe('Messung: Komma, Punkt, x erkannt', (await text(p, '#m1-info')).includes('30 min 55,9') && !(await text(p, '#m1-info')).includes('20 min') && (await text(p, '#m2-info')).includes('45 min, nach der Milch 38,8'));
    pruefe('Messung: eigene Punkte gefüllt im Diagramm (3 + 7)', await p.evaluate(() => document.querySelectorAll('#dia circle.punkt:not(.hohl)').length === 3 && document.querySelectorAll('#dia rect.punkt:not(.hohl)').length === 7));
    await p.check('#beispiel');
    pruefe('Messung: Beispielwerte hohl (6 + 7) und in der Legende als berechnet', await p.evaluate(() => document.querySelectorAll('#dia .punkt.hohl').length === 13) && (await text(p, '#legende')).includes('berechnet'));
    await p.fill('#m1', 'abc');
    pruefe('Messung: Fehler bei Text', (await text(p, '#m1-info')).includes('keine Zahl'));
    await p.fill('#m1', '120');
    pruefe('Messung: Fehler außerhalb 0 bis 100 °C', (await text(p, '#m1-info')).includes('nicht zwischen'));
    await p.fill('#m1', '1 2 3 4 5 6 7 8');
    pruefe('Messung: Fehler bei zu vielen Werten', (await text(p, '#m1-info')).includes('Höchstens 6'));
    await p.fill('#m1', '90');
    pruefe('Messung: Hinweis bei Wert über dem Start von Tasse 2', (await text(p, '#m1-info')).includes('über dem ersten Wert'));
    await p.check('#ln');
    pruefe('ln-Ansicht: Gerade des Modells und 6 Punkte von Tasse 2 (D6)', await p.evaluate(() => [...document.querySelectorAll('#dia text')].some(t => t.textContent.includes('Modell mit kA = 0,1994')) && document.querySelectorAll('#dia rect.punkt').length === 6));
    await axe(p, 'Z2 mit ln-Ansicht, Gruppe offen');
    await p.uncheck('#ln');
    // Aufträge
    await p.click('#a3 summary');
    await p.click('#a3-knopf');
    pruefe('Auftrag 3: ohne Vermutung nicht prüfbar', (await text(p, '#a3-meldung')).length > 0);
    await p.check('input[name=a3][value="1"]');
    await p.click('#a3-knopf');
    pruefe('Auftrag 3: Vermutung hebt die 30-°C-Grenze auf, Zeile über dem Diagramm', (await p.$eval('#rr-thM', e => e.max)) === '95' && !(await p.$eval('#auftrag-zeile', e => e.hidden)) && (await text(p, '#auftrag-zeile')).includes('Auftrag 3'));
    pruefe('Auftrag 3: Auflösung erst nach „Gedanken dazu“', (await p.$eval('#a3-ged', e => e.textContent)) === '');
    await p.fill('#rf-thM', '63,2'); await p.press('#rf-thM', 'Enter');
    pruefe('Auftrag 3: Kipppunkt 63,2 °C ergibt Unterschied nahe 0', /^−?0,0\d K$/.test(await text(p, '#wd')), await text(p, '#wd'));
    await p.click('#a3-ged-knopf');
    pruefe('Auftrag 3: Gedanken mit 68,3, 63,2, 50,8 °C', /68,3 °C.*63,2 °C.*50,8 °C/.test(await text(p, '#a3-ged')));
    await p.click('#a1 summary');
    await p.check('input[name=a1][value="1"]');
    await p.click('#a1-knopf');
    await p.click('#a1-ged-knopf');
    pruefe('Auftrag 1: Gedanken mit 4,97 K (wie die Austrittsfrage)', (await text(p, '#a1-ged')).includes('4,97 K'));
    await p.click('#a2 summary');
    await p.fill('#a2-zahl', '60');
    await p.click('#a2-knopf');
    pruefe('Auftrag 2: Zahl als Vermutung, Werte des Blatts eingestellt', (await text(p, '#a2-vermutung')).includes('60 min') && (await text(p, '#w1')) === '43,01 °C');
    await p.click('#a2-ged-knopf');
    pruefe('Auftrag 2: Gedanken mit 112 min und 8,83 K', /112 min \(8,83 K\)/.test(await text(p, '#a2-ged')));
    // Schluss
    pruefe('Schluss: Knopf erst nach eigener Antwort', await p.$eval('#s4-knopf', b => b.disabled));
    await p.fill('#s4-text', 'Die Simulation zeigt den Verlauf.');
    await p.click('#s4-knopf');
    pruefe('Schluss: Gedanken zu Simulation, Experiment, Rechnung', /Simulation:.*Experiment:.*Rechnung:/.test(await text(p, '#s4-rueck')));
    await p.click('#modell summary');
    await axe(p, 'Z2 Deutsch 1366, Aufträge und Modell offen');
    // Speicher
    await p.reload(); await p.evaluate(() => document.fonts.ready);
    pruefe('Speicher: Zustand bleibt beim Neuladen', await p.evaluate(() => { const z = window.KAFFEE.zustand(); return z.z === 2 && z.a[3].fest && z.schlussGez && z.m2.startsWith('79,8'); }) && (await text(p, '#speicher-text')).includes('nur in diesem Browser'));
    await p.click('#von-vorn');
    pruefe('„Von vorn“ löscht alles', await p.evaluate(() => { const z = window.KAFFEE.zustand(); return z.z === 0 && z.tasse === null && z.m2 === '' && !z.a[3].fest; }) && await p.evaluate(() => localStorage.getItem('kaffee-simulation-f3-45min') === null || JSON.parse(localStorage.getItem('kaffee-simulation-f3-45min')).z === 0));
    pruefe('Z2-Lauf: keine Konsolenfehler, keine fremden Anfragen', p.fehler.length === 0 && p.anfragen.length === 0, p.fehler.concat(p.anfragen).join('; '));
    await p.context().close();
  }
  // ---------------------------------------------------------------- X6-01: „Von vorn“ stellt die Sperre wieder her
  for (const lang of ['de', 'en']) {
    const p = await seite({ q: '?lang=' + lang });
    const zahlen = lang === 'de' ? ERGEBNISSE_DE : ERGEBNISSE_DE.map(z => z.replace(',', '.'));
    await start(p, lang === 'de' ? '43,01' : '43.01', lang === 'de' ? '36,31' : '36.31');
    await erklaere(p, 'a');
    await p.fill('#rf-thM', '6'); await p.press('#rf-thM', 'Enter');
    await p.click('#gruppe summary');
    await p.fill('#m2', '80 72');
    await p.click('#a1 summary'); await p.check('input[name=a1][value="1"]'); await p.click('#a1-knopf'); await p.click('#a1-ged-knopf');
    await p.fill('#rf-thM', '6'); await p.press('#rf-thM', 'Enter');
    await p.waitForTimeout(150);
    const vorher = [await text(p, '#w1'), await text(p, '#w2'), await text(p, '#wd'), (await text(p, '#ansage')).trim()];
    await p.click('#von-vorn');
    await p.waitForTimeout(200);
    // DOM ohne Skript; im Diagramm nur Texte und Namen prüfen (Koordinaten wie x="118.6" sind keine Ergebnisse)
    const dom = await p.evaluate(() => { const c = document.body.cloneNode(true); c.querySelectorAll('script').forEach(x => x.remove()); const d = c.querySelector('#dia'); const t = d.textContent + ' ' + (d.getAttribute('aria-label') || ''); d.remove(); return c.innerHTML + ' ' + t; });
    const kern = vorher.slice(0, 3).map(v => v.split(' ')[0]);
    const gefunden = zahlen.concat(kern).filter(z => dom.includes(z));
    pruefe('X6-01 Von vorn (' + lang + '): keine Ergebniszahl im DOM, auch nicht in Attributen (vorher ' + vorher.slice(0, 3).join(', ') + ')', gefunden.length === 0 && vorher[3].length > 0, gefunden.join(', '));
    pruefe('X6-01 Von vorn (' + lang + '): Statusansage leer, Säulen ohne Inhalt und Namen', (await text(p, '#ansage')) === '' && await p.evaluate(() => !document.getElementById('saeulen').hasChildNodes() && !document.getElementById('saeulen').hasAttribute('aria-label')));
    const axText = await p.locator('body').ariaSnapshot();
    pruefe('X6-01 Von vorn (' + lang + '): Barrierefreiheitsbaum ohne Ergebniszahl', !zahlen.concat(kern).some(z => axText.includes(z)));
    await p.context().close();
  }
  {
    // zweiter Pfad: Neustart innerhalb des 60-ms-Fensters einer ausstehenden Ansage
    const p = await seite();
    await start(p); await erklaere(p);
    await p.evaluate(() => { document.getElementById('rf-tZ').value = '61'; document.getElementById('rf-tZ').dispatchEvent(new Event('change')); document.getElementById('von-vorn').click(); });
    await p.waitForTimeout(250);
    const dom = await p.evaluate(() => { const c = document.body.cloneNode(true); c.querySelectorAll('script').forEach(x => x.remove()); return c.innerHTML; });
    pruefe('X6-01 Neustart während ausstehender Ansage: Ansage leer, keine Ergebniszahl', (await text(p, '#ansage')) === '' && !ERGEBNISSE_DE.concat(['3,58']).some(z => dom.includes(z)) && await p.evaluate(() => window.KAFFEE.zustand().z === 0));
    await p.context().close();
  }
  // ---------------------------------------------------------------- X6-03: Beschriftungen im Diagramm, auch ln am Handy
  for (const lang of ['de', 'en']) {
    for (const [w, h] of [[390, 844], [320, 640]]) {
      const p = await seite({ w, h, q: '?lang=' + lang });
      await start(p); await erklaere(p);
      const randNormal = await p.evaluate(() => { const s = document.getElementById('dia'), W = s.viewBox.baseVal.width; return [...s.querySelectorAll('text')].filter(t => !t.getAttribute('transform')).map(t => t.getBBox()).filter(b => b.x < 0 || b.x + b.width > W + 0.5).length; });
      await p.check('#beispiel'); await p.check('#ln');
      const randLn = await p.evaluate(() => { const s = document.getElementById('dia'), W = s.viewBox.baseVal.width; return [...s.querySelectorAll('text')].filter(t => !t.getAttribute('transform')).map(t => t.getBBox()).filter(b => b.x < 0 || b.x + b.width > W + 0.5).length; });
      pruefe(`X6-03 Beschriftungen ganz im Diagramm ${w} px ${lang} (Kurven ${randNormal}, ln ${randLn} außerhalb)`, randNormal === 0 && randLn === 0);
      await p.context().close();
    }
  }
  // ---------------------------------------------------------------- X6-04: Modell-Link erst mit Ziel
  {
    const p = await seite();
    pruefe('X6-04 Z0: kein Link „Modell“', !(await p.$('#zum-modell')));
    await start(p);
    pruefe('X6-04 Z1: kein Link „Modell“ (Ziel noch gesperrt)', !(await p.$('#zum-modell')));
    await erklaere(p);
    await p.click('#zum-modell');
    pruefe('X6-04 Z2: Link vorhanden, öffnet das Modell', await p.evaluate(() => !document.getElementById('modell').hidden && document.getElementById('modell').open && location.hash === '#modell'));
    await p.context().close();
  }
  // ---------------------------------------------------------------- Rückmeldungen b und c, abweichende Rechnung
  for (const [w, anfang] of [['b', 'Das denken viele.'], ['c', 'Nein.']]) {
    const p = await seite();
    await start(p, '44', '');
    pruefe('Kernsatz bei abweichender Rechnung nennt die Abweichung', (await text(p, '#kernsatz')).includes('weicht ab') && (await text(p, '#kernsatz')).includes('44,00 statt 43,01'));
    await erklaere(p, w);
    const r = await text(p, '#s2-rueck');
    pruefe('Rückmeldung ' + w + ' mit eigenem Anfang und Begründung', r.startsWith(anfang) && r.includes('15,50') && (w !== 'b' || r.includes('15,2 K gegen 24,5 K')), r.slice(0, 80));
    await p.context().close();
  }
  // ---------------------------------------------------------------- Sprache
  {
    const p = await seite({ q: '?lang=en' });
    pruefe('Englisch über ?lang=en', (await p.evaluate(() => document.documentElement.lang)) === 'en' && (await text(p, '#s1-titel')) === 'Which cup is warmer after 45 min?');
    await axe(p, 'Z0 Englisch 1366');
    await start(p, '43.01', '36.31');
    await erklaere(p, 'a');
    pruefe('Englisch: Dezimalpunkt in Kernzahlen und Rückmeldung', (await text(p, '#w1')) === '43.01 °C' && (await text(p, '#s2-rueck')).includes('15.50 kJ') && (await text(p, '#kernsatz')).startsWith('Simulation and your calculation agree'));
    await p.click('#sprache');
    pruefe('Sprachknopf wechselt nach Deutsch, Zustand bleibt', (await p.evaluate(() => document.documentElement.lang)) === 'de' && (await text(p, '#w1')) === '43,01 °C' && (await text(p, '#s2-rueck')).includes('15,50 kJ'));
    await p.click('#sprache');
    await p.click('#modell summary');
    await axe(p, 'Z2 Englisch 1366');
    await p.context().close();
  }
  // ---------------------------------------------------------------- Speicher gesperrt
  {
    const p = await seite({ init: () => { Object.defineProperty(window, 'localStorage', { get() { throw new Error('gesperrt'); } }); } });
    await start(p);
    pruefe('Speicher gesperrt: Seite rechnet weiter und sagt es', (await text(p, '#w1')) === '43,01 °C' && (await text(p, '#speicher-text')).includes('nicht gespeichert') && p.fehler.length === 0, p.fehler.join('; '));
    await p.context().close();
  }
  // ---------------------------------------------------------------- Umbruch, Beamer, Handy, Zielgrößen, Fokus
  for (const [w, h] of [[320, 640], [390, 844], [768, 1024], [1024, 768], [1280, 720], [1366, 768], [1920, 1080]]) {
    for (const lang of ['de', 'en']) {
      const p = await seite({ w, h, q: '?lang=' + lang });
      const q0 = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth);
      await start(p); await erklaere(p);
      await p.click('#gruppe summary'); await p.click('#modell summary'); await p.click('#a1 summary');
      const q2 = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth);
      pruefe(`kein waagerechtes Scrollen ${w} × ${h} ${lang} (Start ${q0} px, alles offen ${q2} px)`, q0 <= 0 && q2 <= 0);
      await p.context().close();
    }
  }
  {
    const p = await seite({ w: 390, h: 844 });
    await p.addStyleTag({ content: 'html { font-size: 200% !important; }' });
    await start(p); await erklaere(p);
    pruefe('200 % Text bei 390 px ohne waagerechtes Scrollen', (await p.evaluate(() => document.documentElement.scrollWidth - innerWidth)) <= 0);
    await p.context().close();
  }
  for (const [w, h] of [[1280, 720], [1366, 768]]) {
    const p = await seite({ w, h });
    await start(p); await erklaere(p);
    await p.evaluate(() => window.scrollTo(0, document.querySelector('.raster').getBoundingClientRect().top + scrollY - 10));
    await p.waitForTimeout(100);
    const box = await p.evaluate(() => { const b = document.getElementById('buehne').getBoundingClientRect(); const s = document.querySelector('#gruppe summary').getBoundingClientRect(); return [b.top, s.bottom, innerHeight]; });
    pruefe(`Beamer ${w} × ${h}: Kernzahlen, Diagramm, beide Regler und Ausgangswerte im Bild`, box[0] >= 0 && box[1] <= box[2], box.map(Math.round).join(', '));
    await p.context().close();
  }
  {
    const p = await seite({ w: 390, h: 844 });
    await start(p); await erklaere(p);
    await p.evaluate(() => document.getElementById('kern').scrollIntoView({ block: 'start' }));
    const hoehe = await p.evaluate(() => document.querySelector('[data-r="tZ"] .lineal').getBoundingClientRect().bottom - document.getElementById('kern').getBoundingClientRect().top);
    pruefe('Handy 390 × 844: Kernzahlen bis Regler „Zugabe“ in einem Bild (' + Math.round(hoehe) + ' px)', hoehe <= 844);
    const klein = await p.evaluate(() => {
      const sel = 'button:not([hidden]), .wahl label, .haken, input[type=range], .feld, summary, .sprache';
      return [...document.querySelectorAll(sel)].filter(e => e.getClientRects().length).map(e => [e.id || e.className || e.tagName, e.getBoundingClientRect()]).filter(([, r]) => r.height < 44 || r.width < 44).map(([n, r]) => n + ' ' + Math.round(r.width) + '×' + Math.round(r.height));
    });
    pruefe('Zielgrößen mindestens 44 × 44 px (Knöpfe, Auswahlzeilen, Regler, Felder, Aufklapper)', klein.length === 0, klein.slice(0, 6).join('; '));
    await p.keyboard.press('Tab');
    await p.focus('#rplus-thM');
    const fokus = await p.$eval('#rplus-thM', e => { const s = getComputedStyle(e); return [s.outlineStyle, parseFloat(s.outlineWidth)]; });
    pruefe('Fokus sichtbar (mindestens 2 px)', fokus[0] !== 'none' && fokus[1] >= 2, fokus.join(' '));
    await axe(p, 'Z2 Deutsch 390');
    await p.context().close();
  }
  {
    const p = await seite({ w: 390, h: 844, q: '?lang=en' });
    await axe(p, 'Z0 Englisch 390');
    await start(p); await erklaere(p);
    await axe(p, 'Z2 Englisch 390');
    await p.context().close();
  }
  {
    const p = await seite({ w: 1280, h: 720 });
    await start(p); await erklaere(p);
    await axe(p, 'Z2 Deutsch Beamer 1280 × 720');
    // Leistung: Reglerschritt bis zur neuen Anzeige
    const zeiten = await p.evaluate(() => { const r = document.getElementById('rr-tZ'); const z = []; for (let i = 1; i <= 60; i++) { const t0 = performance.now(); r.value = i; r.dispatchEvent(new Event('input')); z.push(performance.now() - t0); } z.sort((a, b) => a - b); return [z[30], z[57]]; });
    pruefe('Leistung: Reglerschritt Median unter 50 ms (' + zeiten.map(x => x.toFixed(1)).join(' / ') + ' ms, Median / 95 %)', zeiten[0] < 50);
    await p.context().close();
  }
}

(async () => {
  browser = await chromium.launch();
  try { await tests(); } catch (e) { pruefe('Testlauf ohne Ausnahme', false, e.stack); }
  await browser.close();
  const gut = ergebnisse.filter(e => e[1]).length;
  const zeilen = ['Browsertest Fassung 3 (' + path.relative(path.join(__dirname, '..', '..'), DATEI) + ', Chromium über Playwright, axe-core 4.14.0)', ''];
  for (const [n, ok, info] of ergebnisse) zeilen.push((ok ? 'bestanden   ' : 'FEHLGESCHLAGEN ') + n + (info && !ok ? '  [' + info + ']' : ''));
  zeilen.push('', gut + ' von ' + ergebnisse.length + ' bestanden');
  const t = zeilen.join('\n') + '\n';
  if (!process.env.KAFFEE_DATEI) fs.writeFileSync(path.join(__dirname, 'browsertest_ergebnis.txt'), t);
  console.log(t);
  process.exit(gut === ergebnisse.length ? 0 : 1);
})();
