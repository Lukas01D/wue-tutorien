// Browsertest der schlanken Varianten A und B (simulation/minimal), Chromium über Playwright, axe-core wie browsertest.js.
// Aufruf: node simulation/tests/minimal_test.js   (vorher einmal: cd simulation/tests && npm ci)
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const AXE = fs.readFileSync(require.resolve('axe-core/axe.min.js'), 'utf8');
const erg = [];
const pruefe = (name, ok, info) => erg.push([name, !!ok, info || '']);

(async () => {
  const b = await chromium.launch();
  for (const v of ['A', 'B']) {
    const datei = path.join(__dirname, '../minimal/Kaffee_Simulation_' + v + '.html');
    for (const [w, h] of [[1366, 768], [390, 844]]) {
      const ctx = await b.newContext({ viewport: { width: w, height: h }, bypassCSP: true });
      const p = await ctx.newPage();
      const fehler = [], anfragen = [];
      p.on('pageerror', e => fehler.push(e.message));
      p.on('console', m => { if (m.type() === 'error') fehler.push(m.text()); });
      p.on('request', r => { if (!r.url().startsWith('file:') && !r.url().startsWith('data:')) anfragen.push(r.url()); });
      await p.goto('file://' + datei);
      await p.evaluate(() => document.fonts.ready);
      const n = v + ' ' + w + ' px: ';
      const ergebnis = await p.textContent('#ergebnis'), q = await p.textContent('#q-text');
      pruefe(n + 'Werte des Blatts (43,01 / 36,31 / 6,69 K)', ['43,01', '36,31', '6,69'].every(z => ergebnis.includes(z)), ergebnis);
      pruefe(n + 'Säulen 15,50 und 23,82 kJ, Unterschied 8,31 kJ', q.includes('15,50') && q.includes('23,82') && (await p.textContent('#q')).includes('8,31'), q);
      pruefe(n + 'keine Fragen, keine Eingabefelder außer Reglern', (await p.$$('input:not([type=range]), textarea, select, fieldset')).length === 0);
      pruefe(n + 'keine waagerechte Bildlaufleiste', await p.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth));
      pruefe(n + 'Diagramm und Säulen nebeneinander oder direkt untereinander sichtbar', await p.evaluate(() => {
        const d = document.getElementById('dia').getBoundingClientRect(), s = document.getElementById('q').getBoundingClientRect();
        return d.height > 150 && s.height > 150 && (Math.abs(d.top - s.top) < 80 || s.top - d.bottom < 80);
      }));
      // Milch 95 °C: Tasse 2 wärmer, Pfeil nach oben, Beschreibung „steigt“
      await p.$eval('#r-thM', e => { e.value = 95; e.dispatchEvent(new Event('input')); });
      const e95 = await p.textContent('#ergebnis');
      pruefe(n + 'Milch 95 °C: Tasse 2 3,65 K wärmer, „steigt“', e95.includes('Tasse 2 ist 3,65 K') && (await p.textContent('#dia-text')).includes('steigt'), e95);
      pruefe(n + 'Regler Milch bis 95 °C', (await p.$eval('#r-thM', e => e.max)) === '95');
      await p.click('#blatt');
      pruefe(n + 'Werte des Blatts stellt zurück', (await p.textContent('#ergebnis')).includes('43,01'));
      if (v === 'B') {
        pruefe(n + 'Zeitregler sichtbar', !(await p.$eval('#zeit-bereich', e => e.hidden)));
        await p.$eval('#zeit', e => { e.value = 20; e.dispatchEvent(new Event('input')); });
        const q20 = await p.textContent('#q-text');
        pruefe(n + 'Zeit 20 min: 7,72 und 12,48 kJ', q20.includes('7,72') && q20.includes('12,48'), q20);
        await p.click('#abspielen');
        await p.waitForTimeout(6800);
        pruefe(n + 'Abspielen läuft bis zur Zugabe', (await p.textContent('#q-text')).includes('23,82') && (await p.textContent('#abspielen')) === 'Abspielen');
      } else {
        pruefe(n + 'kein Zeitregler', await p.$eval('#zeit-bereich', e => e.hidden));
      }
      await p.addScriptTag({ content: AXE });
      const ax = await p.evaluate(async () => (await axe.run(document, { runOnly: { type: 'tag', values: ['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'] } })).violations.map(x => x.id + ' (' + x.nodes.length + ')'));
      pruefe(n + 'axe-core ohne Verstöße', ax.length === 0, ax.join(', '));
      pruefe(n + 'keine Fehler, keine Netzanfragen', fehler.length === 0 && anfragen.length === 0, fehler.concat(anfragen).join('; '));
      await ctx.close();
    }
  }
  // CSP greift (ohne bypassCSP): Seite rechnet trotzdem
  const ctx = await b.newContext();
  const p = await ctx.newPage();
  await p.goto('file://' + path.join(__dirname, '../minimal/Kaffee_Simulation_A.html'));
  pruefe('CSP: Seite läuft mit eigener CSP', (await p.textContent('#ergebnis')).includes('43,01'));
  await b.close();
  let ok = 0;
  for (const [name, gut, info] of erg) { console.log((gut ? 'bestanden   ' : 'FEHLER      ') + name + (gut || !info ? '' : '  [' + info + ']')); ok += gut; }
  console.log('\n' + ok + ' von ' + erg.length + ' bestanden');
  process.exit(ok === erg.length ? 0 : 1);
})();
