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
const zahlen = s => (s.match(/−?\d+,\d+/g) || []).map(z => Number(z.replace('−', '-').replace(',', '.')));

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
    const kern = () => p.textContent('#kern'), saeulen = () => p.textContent('#saeulen');
    const k0 = await kern(), s0 = await saeulen();
    pruefe(n + 'Kasten mit Werten des Blatts (43,01 / 36,31 / 6,69 K)', ['43,01', '36,31', '6,69'].every(z => k0.includes(z)), k0);
    pruefe(n + 'Kasten: Tasse 1 (Milch zu Beginn), Tasse 2 (Milch später), Temperaturdifferenz', k0.includes('Milch zu Beginn') && k0.includes('Milch später') && k0.includes('Temperatur­differenz'));
    pruefe(n + 'Säulen 15,50 und 23,82 kJ, Unterschied 8,31 kJ', ['15,50', '23,82', '8,31'].every(z => s0.includes(z)), s0);
    pruefe(n + 'keine Fragen, kein Ausklappen, keine Hinweistexte', (await p.$$('textarea, select, fieldset, details, input[type=radio], input[type=checkbox]')).length === 0 && (await p.$$eval('.regler .hinweis', l => l.filter(x => x.textContent.trim()).length)) === 0);
    pruefe(n + 'zehn Regler mit − und + (mit Kaffeemenge, Tassenwärmer und Wärmekapazität)', (await p.$$('.regler')).length === 10 && (await p.$$('.pm')).length === 20 && !!(await p.$('#rr-QW')) && !!(await p.$('#rr-VK_ml')) && !!(await p.$('#rr-CT')));
    pruefe(n + 'keine waagerechte Bildlaufleiste', await p.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth));
    pruefe(n + 'Säulen neben oder direkt unter dem Diagramm', await p.evaluate(() => {
      const d = document.getElementById('dia').getBoundingClientRect(), s = document.getElementById('saeulen').getBoundingClientRect();
      return d.height > 150 && s.height > 100 && (s.left >= d.right - 1 || s.top - d.bottom < 80);
    }));
    // Zeit bis 180 min, Zugabe höchstens t
    await setze(p, 't', 90);
    const k90 = await kern(), s90 = await saeulen(), d90 = zahlen(k90)[2], q90 = zahlen((await p.$$eval('#saeulen text.zahl', l => l.map(x => x.textContent))).join(' '));   // Säulentext: Q₂ − Q₁, Q₁, Q₂
    pruefe(n + 't = 90 min, Zugabe 45: Temperaturdifferenz 4,34 K, Q₂ − Q₁ = C_G · Δϑ', Math.abs(d90 - 4.34) < 0.006 && Math.abs(1241.8 * d90 / 1000 - q90[0]) < 0.011 && Math.abs(q90[2] - q90[1] - q90[0]) < 0.011, k90 + ' | ' + s90);
    pruefe(n + 'Zeit bis 180 min, Zugabe-Regler bis t', (await p.$eval('#rr-t', e => e.max)) === '180' && (await p.$eval('#rr-tZ', e => e.max)) === '90');
    await setze(p, 'QW', 5);
    const kw = await kern(), dw = zahlen(kw)[2], qw = zahlen((await p.$$eval('#saeulen text.zahl', l => l.map(x => x.textContent))).join(' '));
    pruefe(n + 'Tassenwärmer 5 W bei t = 90 min: wärmer als ohne, Q₂ − Q₁ = C_G · Δϑ', zahlen(kw)[0] > 34.91 && Math.abs(1241.8 * dw / 1000 - qw[0]) < 0.011 && Math.abs(qw[2] - qw[1] - qw[0]) < 0.011, kw);
    await p.fill('#rf-kA', '0,012'); await p.press('#rf-kA', 'Enter');
    pruefe(n + 'Tassenwärmer höchstens bis 95 °C: bei kA 0,012 W/K Obergrenze 0,5 W', (await p.$eval('#rr-QW', e => e.max)) === '0.5' && (await p.$eval('#rf-QW', e => e.value)) === '0,5');
    await p.fill('#rf-kA', '0,1994'); await p.press('#rf-kA', 'Enter');
    await setze(p, 'QW', 0);
    await setze(p, 'tZ', 90);
    pruefe(n + 'Zugabe nicht über t', (await p.$eval('#rr-tZ', e => e.value)) === '90');
    await setze(p, 't', 20);
    pruefe(n + 't kleiner als Zugabe: Zugabe folgt auf 20 min', (await p.$eval('#rf-tZ', e => e.value)) === '20' && (await p.$eval('#rr-tZ', e => e.max)) === '20');
    await p.click('#knopf-blatt');
    pruefe(n + 'Standardwerte stellt zurück, Knopf heißt „Standardwerte“', (await kern()).includes('43,01') && (await p.textContent('#knopf-blatt')) === 'Standardwerte');
    // Abspielen
    await p.click('#abspielen');
    await p.waitForTimeout(1500);
    const mitten = await kern();
    pruefe(n + 'Abspielen: Zwischenstand mit verdeckter Zukunft', !mitten.includes('nach 45 min') && (await p.$$('#dia .zukunft')).length === 1, mitten);
    await p.waitForTimeout(6500);
    pruefe(n + 'Abspielen läuft bis t', (await kern()).includes('43,01') && (await saeulen()).includes('23,82') && (await p.textContent('#abspielen')) === 'Abspielen' && (await p.$$('#dia .zukunft')).length === 0);
    // Milch 95 °C, Wärmekapazität, Kaffeemenge
    await setze(p, 'thM', 95);
    pruefe(n + 'Milch 95 °C: Tasse 2 wärmer (−3,65 K), Bildbeschreibung „steigt“', (await kern()).includes('−3,65') && (await p.textContent('#dia-beschreibung')).includes('steigt'));
    await p.click('#knopf-blatt');
    await setze(p, 'CT', 255);
    const dCT = zahlen(await kern())[2];
    pruefe(n + 'Wärmekapazität 255 J/K: Unterschied kleiner als ohne Tasse', dCT > 3 && dCT < 6.69, String(dCT));
    pruefe(n + 'Vergleich Wärmekapazität 255 J/K: Porzellantasse, Einmachglas', (await p.textContent('#rv-CT')) === '≈ Porzellantasse, Einmachglas' && (await p.$eval('#rr-CT', e => e.getAttribute('aria-valuetext'))).includes('Porzellantasse'));
    await p.click('#knopf-blatt');
    pruefe(n + 'Vergleiche bei Standardwerten: Tasse mit Deckel, Blatt ohne Wärmekapazität', (await p.textContent('#rv-kA')) === '≈ Tasse mit Deckel' && (await p.textContent('#rv-CT')).startsWith('Blatt'));
    await p.fill('#rf-kA', '0,012'); await p.press('#rf-kA', 'Enter');
    pruefe(n + 'kA 0,012 W/K: sehr gute Isolierflasche, Schieber logarithmisch', (await p.textContent('#rv-kA')) === '≈ sehr gute Isolierflasche' && Math.abs(Number(await p.$eval('#rr-kA', e => e.value)) - 1000 * Math.log(1.2) / Math.log(100)) < 1.5);
    await setze(p, 'kA', 1000);
    pruefe(n + 'kA-Schieber ganz rechts: 1 W/K, offene Tasse', (await p.$eval('#rf-kA', e => e.value)) === '1,0000' && (await p.textContent('#rv-kA')).includes('offene Tasse'));
    pruefe(n + 'Regler mit Vergleich stehen unten nebeneinander', await p.evaluate(() => {
      const a = document.querySelector('[data-r=kA]').getBoundingClientRect(), b = document.querySelector('[data-r=CT]').getBoundingClientRect(), t = document.querySelector('[data-r=thU]').getBoundingClientRect();
      return a.top >= t.bottom - 1 && (innerWidth < 700 ? b.top >= a.bottom - 1 : Math.abs(a.top - b.top) < 2);
    }));
    await p.click('#knopf-blatt');
    await setze(p, 'VK_ml', 300);
    const dVK = zahlen(await kern())[2];
    pruefe(n + 'Kaffeemenge 300 ml: Unterschied kleiner als bei 200 ml', dVK > 0 && dVK < 6.69, String(dVK));
    await p.click('#knopf-blatt');
    await p.click('#sprache');
    pruefe(n + 'Englisch: Kasten und Knopf', (await kern()).includes('43.01') && (await kern()).includes('milk at the start') && (await p.textContent('#abspielen')) === 'Play');
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
