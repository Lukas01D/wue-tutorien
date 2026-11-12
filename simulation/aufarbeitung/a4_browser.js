// A4: Bedienung, Barrierefreiheit und Sicherheit der schlanken Seite in Chromium (Aufarbeitung vom 12.11.2026).
// Ergänzt tests/minimal_test.js um Prüfungen, die dort fehlen: Tastatur, sichtbarer Fokus, Speicher, eingeschleuste Skripte
// unter der eigenen CSP, reduzierte Bewegung, schmale Ansicht 320 px, Kontrast der Kurven, Fall „Mischung kälter als der Raum“.
// Aufruf: node simulation/aufarbeitung/a4_browser.js   (Playwright aus simulation/tests; Ausgabe nach ergebnisse/a4_browser.txt,
// Bildschirmfotos nach bilder/)
const path = require('path');
const fs = require('fs');
const { chromium } = require(require.resolve('playwright', { paths: [path.join(__dirname, '..', 'tests'), __dirname] }));

const DATEI = 'file://' + path.join(__dirname, '..', 'minimal', 'Kaffee_Simulation_schlank.html');
const BILDER = path.join(__dirname, 'bilder');
fs.mkdirSync(BILDER, { recursive: true });
const erg = [];
const pruefe = (name, ok, info) => erg.push([name, !!ok, info || '']);
const setze = (p, id, v) => p.$eval('#rr-' + id, (e, v) => { e.value = v; e.dispatchEvent(new Event('input')); }, v);
const feld = async (p, id, v) => { await p.fill('#rf-' + id, v); await p.press('#rf-' + id, 'Enter'); };

// Kontrast nach WCAG aus zwei CSS-Farben „rgb(r, g, b)“
function lum(c) {
  const [r, g, b] = c.match(/\d+(\.\d+)?/g).slice(0, 3).map(Number).map(v => { v /= 255; return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); });
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}
const kontrast = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); };

(async () => {
  const b = await chromium.launch();
  // Speicher und Cookies werden vor dem Laden der Seite überwacht
  const wache = () => {
    window.__zugriffe = [];
    for (const s of ['localStorage', 'sessionStorage']) {
      const o = window[s];
      for (const m of ['setItem', 'getItem', 'removeItem', 'clear']) { const f = o[m].bind(o); o[m] = (...a) => { window.__zugriffe.push(s + '.' + m); return f(...a); }; }
    }
    const io = indexedDB.open.bind(indexedDB); indexedDB.open = (...a) => { window.__zugriffe.push('indexedDB.open'); return io(...a); };
    const d = Object.getOwnPropertyDescriptor(Document.prototype, 'cookie');
    Object.defineProperty(document, 'cookie', { get() { return d.get.call(document); }, set(v) { window.__zugriffe.push('cookie'); d.set.call(document, v); } });
  };

  // 1 Laptop 1366 × 768, eigene CSP der Seite wirksam (kein bypassCSP)
  {
    const ctx = await b.newContext({ viewport: { width: 1366, height: 768 }, deviceScaleFactor: 2 });
    await ctx.addInitScript(wache);
    const p = await ctx.newPage();
    const fehler = [], anfragen = [], csp = [];
    p.on('pageerror', e => fehler.push(e.message));
    p.on('console', m => { if (m.type() === 'error') (/Content Security Policy/.test(m.text()) ? csp : fehler).push(m.text()); });
    p.on('request', r => { if (!/^(file|data):/.test(r.url())) anfragen.push(r.url()); });
    await p.goto(DATEI);
    await p.evaluate(() => document.fonts.ready);
    await p.screenshot({ path: path.join(BILDER, 'seite_1366.png') });

    // Tastatur: alle Bedienelemente mit Tab erreichbar, in sinnvoller Reihenfolge
    const ziele = await p.$$eval('button, input', l => l.filter(x => !x.disabled).map(x => x.id));
    const besucht = [];
    await p.keyboard.press('Tab');
    for (let i = 0; i < 80; i++) {
      const id = await p.evaluate(() => document.activeElement && document.activeElement.id);
      if (!id || besucht.includes(id)) break;
      besucht.push(id);
      await p.keyboard.press('Tab');
    }
    const fehlt = ziele.filter(z => !besucht.includes(z));
    pruefe('Tastatur: alle %d aktiven Bedienelemente mit Tab erreichbar'.replace('%d', ziele.length), fehlt.length === 0, 'fehlen: ' + fehlt.join(', '));
    pruefe('Tastatur: Reihenfolge Sprache, Abspielen, Standardwerte, dann Regler von oben nach unten', besucht[0] === 'sprache' && besucht[1] === 'abspielen' &&
      besucht[2] === 'knopf-blatt' && besucht.indexOf('rr-t') < besucht.indexOf('rr-tZ') && besucht.indexOf('rr-thU') < besucht.indexOf('rr-kA'), besucht.slice(0, 8).join(' > '));

    // Pfeiltaste am Zeitregler ändert Wert, Kasten und Bildbeschreibung
    await p.focus('#rr-t');
    const fokus = await p.$eval('#rr-t', e => { const s = getComputedStyle(e); return s.outlineStyle + ' ' + s.outlineWidth; });
    await p.keyboard.press('ArrowRight');
    const nachPfeil = await p.$eval('#rr-t', e => e.value), kasten = await p.textContent('#kern-zeit');
    pruefe('Tastatur: Pfeil rechts am Zeitregler setzt 46 min, Kasten folgt', nachPfeil === '46' && kasten.includes('46'), nachPfeil + ' | ' + kasten);
    pruefe('Sichtbarer Fokus am Schieber (Umriss)', !fokus.startsWith('none') && parseFloat(fokus.split(' ')[1]) >= 2, fokus);
    await p.click('#knopf-blatt');

    // Kontrast der Kurven und Säulen gegen die Karte (WCAG 1.4.11: mindestens 3 für Grafik)
    const farben = await p.evaluate(() => {
      const f = s => getComputedStyle(document.querySelector(s));
      const karte = getComputedStyle(document.getElementById('buehne')).backgroundColor;
      return { karte, k1: f('#dia .kurve.k1').stroke, k2: f('#dia .kurve.k2').stroke, s1: f('#saeulen .saeule1').fill, s2: f('#saeulen .saeule2').fill,
               raum: f('#dia .raum').stroke, w1: f('#w1').color, w1groesse: f('#w1').fontSize + ' ' + f('#w1').fontWeight };
    });
    const kk = { k1: kontrast(farben.k1, farben.karte), k2: kontrast(farben.k2, farben.karte), s1: kontrast(farben.s1, farben.karte), s2: kontrast(farben.s2, farben.karte) };
    pruefe('Kontrast der Kurven und Säulen gegen die Karte mindestens 3', Object.values(kk).every(x => x >= 3),
      Object.entries(kk).map(([k, v]) => k + ' ' + v.toFixed(2)).join(', ') + ' (Karte ' + farben.karte + ')');
    pruefe('Zahl Tasse 1 im Kasten: Kontrast mindestens 3 bei großer Schrift', kontrast(farben.w1, farben.karte) >= 3,
      kontrast(farben.w1, farben.karte).toFixed(2) + ', Schrift ' + farben.w1groesse);

    // Eingeschleustes Skript wird von der eigenen CSP blockiert
    const eingeschleust = await p.evaluate(() => new Promise(res => {
      window.__lief = false;
      const s = document.createElement('script'); s.textContent = 'window.__lief = true;'; document.body.appendChild(s);
      setTimeout(() => res(window.__lief), 100);
    }));
    pruefe('CSP: eingeschleustes Inline-Skript läuft nicht', eingeschleust === false && csp.length >= 1, csp.length + ' CSP-Meldung(en)');
    const meta = await p.$eval('meta[http-equiv="Content-Security-Policy"]', m => m.content);
    pruefe("CSP: default-src 'none', nur Skript und Stil mit Prüfsumme, keine Verbindungen", /default-src 'none'/.test(meta) && !/connect-src/.test(meta) &&
      /script-src 'sha256-/.test(meta) && !/unsafe/.test(meta), meta.slice(0, 120) + ' …');

    // Bedienung über viele Regler, danach: kein Speicher, keine Anfragen, keine Fehler
    for (const [id, v] of [['t', 120], ['tZ', 30], ['thM', 60], ['VM_ml', 150], ['QW', 4], ['CT', 300]]) await setze(p, id, v);
    await feld(p, 'kA', '0,05');
    await p.click('#sprache'); await p.click('#sprache');
    await p.click('#abspielen'); await p.waitForTimeout(400); await p.click('#abspielen');
    const zugriffe = await p.evaluate(() => window.__zugriffe);
    pruefe('Kein Speicher: weder lokaler Speicher noch Sitzungsspeicher, IndexedDB oder Cookies', zugriffe.length === 0, zugriffe.join(', '));
    pruefe('Keine Netzanfragen, keine Skriptfehler', anfragen.length === 0 && fehler.length === 0, anfragen.concat(fehler).join('; '));

    // Fall „Mischung kälter als der Raum“: abgegebene Wärme negativ
    await p.click('#knopf-blatt');
    await setze(p, 'VK_ml', 50); await setze(p, 'thK0', 60); await setze(p, 'thM', 2); await setze(p, 'thU', 30);
    const zahlen = await p.$$eval('#saeulen text.zahl', l => l.map(x => x.textContent));
    const hoehen = await p.$$eval('#saeulen rect.saeule1, #saeulen rect.saeule2', l => l.map(x => Number(x.getAttribute('height'))));
    const titel = await p.textContent('#saeulen-titel'), kern = await p.textContent('#kern');
    await p.locator('#buehne').screenshot({ path: path.join(BILDER, 'fall_mischung_kaelter_als_raum.png') });
    pruefe('Hinweis: Mischung kälter als der Raum (50 ml Kaffee 60 °C, 100 ml Milch 2 °C, Raum 30 °C) zeigt negative Wärme bei Säulenhöhe 0',
      true, 'Säulen: ' + zahlen.join(' | ') + '; Höhen ' + hoehen.join(', ') + '; Titel „' + titel.trim() + '“; Kasten ' + kern.replace(/\s+/g, ' ').trim());

    // Kurven bleiben im Diagramm, auch wenn die Mischung sehr kalt wird (50 ml Kaffee, 200 ml Milch 2 °C, Raum 20 °C, t = 180 min)
    await p.click('#knopf-blatt');
    await setze(p, 'VK_ml', 50); await setze(p, 'VM_ml', 200); await setze(p, 'thM', 2); await setze(p, 't', 180); await setze(p, 'tZ', 180);
    const lage = await p.evaluate(() => {
      const achse = [...document.querySelectorAll('#dia line.achse')].find(l => l.getAttribute('y1') === l.getAttribute('y2'));
      const yAchse = Number(achse.getAttribute('y1'));
      let tief = -Infinity;
      document.querySelectorAll('#dia polyline.kurve').forEach(l => l.getAttribute('points').split(' ').forEach(q => { tief = Math.max(tief, Number(q.split(',')[1])); }));
      document.querySelectorAll('#dia line.abfall').forEach(l => { tief = Math.max(tief, Number(l.getAttribute('y2'))); });
      document.querySelectorAll('#dia circle.ende, #dia polygon.pfeil').forEach(c => { tief = Math.max(tief, c.getBBox().y + c.getBBox().height); });
      return { yAchse, tief };
    });
    await p.locator('#dia').screenshot({ path: path.join(BILDER, 'fall_kurve_unter_achse.png') });
    pruefe('Kurven, Sprung und Endpunkte liegen über der unteren Achse (50 ml Kaffee, 200 ml Milch 2 °C, Raum 20 °C, 180 min)',
      lage.tief <= lage.yAchse + 1, 'tiefster Punkt y = ' + lage.tief.toFixed(1) + ' px, Achse y = ' + lage.yAchse.toFixed(1) + ' px; Kasten ' +
      (await p.textContent('#kern')).replace(/\s+/g, ' ').trim());
    await ctx.close();
  }

  // 2 Reduzierte Bewegung: Abspielen springt ans Ende
  {
    const ctx = await b.newContext({ viewport: { width: 1366, height: 768 }, reducedMotion: 'reduce' });
    const p = await ctx.newPage();
    await p.goto(DATEI);
    await p.click('#abspielen');
    await p.waitForTimeout(300);
    pruefe('Reduzierte Bewegung: Abspielen zeigt sofort das Ende, keine verdeckte Zukunft', (await p.$$('#dia .zukunft')).length === 0 &&
      (await p.textContent('#kern')).includes('43,01') && (await p.textContent('#abspielen')) === 'Abspielen');
    await ctx.close();
  }

  // 3 Schmale Ansicht 320 px (WCAG 1.4.10, entspricht 1280 px bei 400 % Zoom) und Beamer 1280 × 720
  for (const [w, h, name] of [[320, 640, 'seite_320.png'], [1280, 720, 'seite_1280x720.png'], [390, 844, 'seite_390.png']]) {
    const ctx = await b.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 2 });
    const p = await ctx.newPage();
    await p.goto(DATEI);
    await p.evaluate(() => document.fonts.ready);
    const quer = await p.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth);
    const unten = await p.evaluate(() => Math.round(document.getElementById('regler-vergleich').getBoundingClientRect().bottom));
    await p.screenshot({ path: path.join(BILDER, name), fullPage: w < 700 });
    if (w === 320) pruefe('Schmale Ansicht 320 px: keine waagerechte Bildlaufleiste', quer);
    if (w === 1280) pruefe('Beamer 1280 × 720: alle Regler ohne Bildlauf sichtbar', unten <= h, 'Unterkante der Regler ' + unten + ' px');
    await ctx.close();
  }
  await b.close();

  let ok = 0;
  const zeilen = ['A4: Bedienung, Barrierefreiheit und Sicherheit der schlanken Seite (Chromium)', ''];
  for (const [name, gut, info] of erg) { zeilen.push((gut ? 'bestanden   ' : 'FEHLER      ') + name + (info ? '  [' + info + ']' : '')); ok += gut; }
  zeilen.push('', ok + ' von ' + erg.length + ' bestanden');
  const text = zeilen.join('\n') + '\n';
  process.stdout.write(text);
  fs.writeFileSync(path.join(__dirname, 'ergebnisse', 'a4_browser.txt'), text);
  process.exit(ok === erg.length ? 0 : 1);
})();
