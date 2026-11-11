// Browsertest der schlanken Seite (simulation/minimal/Kaffee_Simulation_schlank.html), Chromium über Playwright, axe-core wie browsertest.js.
// Aufruf: node simulation/tests/minimal_test.js   (vorher einmal: cd simulation/tests && npm ci)
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const DATEI = 'file://' + path.join(__dirname, '../minimal/Kaffee_Simulation_schlank.html');
const AXE = fs.readFileSync(require.resolve('axe-core/axe.min.js'), 'utf8');
const erg = [];
const pruefe = (name, ok, info) => erg.push([name, !!ok, info || '']);
const setze = (p, id, v) => p.$eval('#rr-' + id, (e, v) => { e.value = v; e.dispatchEvent(new Event('input')); }, v);

(async () => {
  const b = await chromium.launch();
  for (const [w, h] of [[1366, 768], [390, 844]]) {
    const ctx = await b.newContext({ viewport: { width: w, height: h }, bypassCSP: true });
    const p = await ctx.newPage();
    const fehler = [], anfragen = [];
    p.on('pageerror', e => fehler.push(e.message));
    p.on('console', m => { if (m.type() === 'error') fehler.push(m.text()); });
    p.on('request', r => { if (!r.url().startsWith('file:') && !r.url().startsWith('data:')) anfragen.push(r.url()); });
    await p.goto(DATEI);
    await p.evaluate(() => document.fonts.ready);
    const n = w + ' px: ';
    const kern = () => p.textContent('#kern');
    const k0 = await kern(), s0 = await p.textContent('#saeulen');
    pruefe(n + 'Kasten mit Werten des Blatts (43,01 / 36,31 / 6,69 K)', ['43,01', '36,31', '6,69'].every(z => k0.includes(z)));
    pruefe(n + 'Säulen 15,50 und 23,82 kJ, Unterschied 8,31 kJ', ['15,50', '23,82', '8,31'].every(z => s0.includes(z)));
    pruefe(n + 'keine Fragen, keine Textfelder außer Zahlenfeldern der Regler', (await p.$$('textarea, select, fieldset, input[type=radio], input[type=checkbox]')).length === 0);
    pruefe(n + 'Regler wie Hauptseite: 6 Regler plus Zeit, mit − und +', (await p.$$('.regler')).length === 7 && (await p.$$('.pm')).length === 14);
    pruefe(n + 'keine waagerechte Bildlaufleiste', await p.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth));
    pruefe(n + 'Säulen neben oder direkt unter dem Diagramm', await p.evaluate(() => {
      const d = document.getElementById('dia').getBoundingClientRect(), s = document.getElementById('saeulen').getBoundingClientRect();
      return d.height > 150 && s.height > 100 && (s.left >= d.right - 1 || s.top - d.bottom < 80);
    }));
    await setze(p, 't', 20);
    const s20 = await p.textContent('#saeulen');
    pruefe(n + 'Zeit 20 min: Säulen 7,72 und 12,48 kJ, Kasten bleibt beim Endwert', s20.includes('7,72') && s20.includes('12,48') && (await kern()).includes('43,01'), s20);
    pruefe(n + 'Zeit 20 min: Zukunft verdeckt, Zeitlinie da', (await p.$$('#dia .zukunft')).length === 1 && (await p.$$('#dia .jetzt')).length === 1);
    await p.click('#abspielen');
    await p.waitForTimeout(6800);
    pruefe(n + 'Abspielen läuft bis zur Zugabe', (await p.textContent('#saeulen')).includes('23,82') && (await p.textContent('#abspielen')) === 'Abspielen' && (await p.$$('#dia .zukunft')).length === 0);
    await setze(p, 'thM', 95);
    pruefe(n + 'Milch 95 °C: Tasse 2 wärmer (−3,65 K), Bildbeschreibung „steigt“', (await kern()).includes('−3,65') && (await p.textContent('#dia-beschreibung')).includes('steigt'));
    pruefe(n + 'Regler Milch bis 95 °C ohne Sperre', (await p.$eval('#rr-thM', e => e.max)) === '95');
    await p.click('#knopf-blatt', { force: true }).catch(async () => { await p.click('#gruppe summary'); await p.click('#knopf-blatt'); });
    pruefe(n + 'Werte des Blatts stellt zurück', (await kern()).includes('43,01'));
    await p.click('#sprache');
    pruefe(n + 'Englisch: Kasten und Knopf', (await kern()).includes('43.01') && (await p.textContent('#abspielen')) === 'Play');
    await p.click('#sprache');
    await p.addScriptTag({ content: AXE });
    const ax = await p.evaluate(async () => (await axe.run(document, { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'] } })).violations.map(x => x.id + ' (' + x.nodes.length + ')'));
    pruefe(n + 'axe-core ohne Verstöße', ax.length === 0, ax.join(', '));
    pruefe(n + 'keine Fehler, keine Netzanfragen', fehler.length === 0 && anfragen.length === 0, fehler.concat(anfragen).join('; '));
    await ctx.close();
  }
  const ctx = await b.newContext();
  const p = await ctx.newPage();
  await p.goto(DATEI);
  pruefe('CSP: Seite läuft mit eigener CSP', (await p.textContent('#kern')).includes('43,01'));
  await b.close();
  let ok = 0;
  for (const [name, gut, info] of erg) { console.log((gut ? 'bestanden   ' : 'FEHLER      ') + name + (gut || !info ? '' : '  [' + info + ']')); ok += gut; }
  console.log('\n' + ok + ' von ' + erg.length + ' bestanden');
  process.exit(ok === erg.length ? 0 : 1);
})();
