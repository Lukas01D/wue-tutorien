// Bildschirmfotos der Kaffee-Seite Fassung 3 (Gerätefaktor 2, JPEG) nach simulation/bildschirmfotos/f3/. Aufruf: node simulation/tests/bilder.js
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const URL = 'file://' + path.resolve(__dirname, '../site/index.html');
const ZIEL = path.resolve(__dirname, '../bildschirmfotos/f3');
const GERAETE = { handy: [390, 844], laptop: [1366, 768], beamer: [1280, 720] };

async function zustand(p, z) {
  if (z === 'start') return;
  await p.check('input[name=tasse][value="1"]'); await p.check('input[name=grund][value="h"]');
  await p.fill('#e1', '43,01'); await p.fill('#e2', '36,31');
  await p.click('#s1-knopf');
  if (z === 'ergebnis') return;
  await p.check('input[name=warum][value="a"]'); await p.click('#s2-knopf');
  if (z === 'erklaert') return;
  if (z === 'messung' || z === 'ln') {
    await p.fill('#m1', '59,9 55,9 52 49,2 46 44,9');
    await p.fill('#m2', '79,6 71,8 64,9 59,2 54,1 51,6 39,2');
    await p.check('#beispiel');
    if (z === 'ln') await p.check('#ln');
    return;
  }
  if (z === 'auftrag3') {
    await p.click('#a3 summary'); await p.check('input[name=a3][value="1"]'); await p.click('#a3-knopf');
    await p.fill('#rf-tZ', '90'); await p.press('#rf-tZ', 'Enter');
    await p.fill('#rf-thM', '50'); await p.press('#rf-thM', 'Enter');
    await p.click('#a3-ged-knopf');
    return;
  }
  if (z === 'modell') { await p.click('#gruppe summary'); await p.click('#modell summary'); }
}
async function blick(p, geraet, z) {
  const handy = geraet === 'handy';
  const ziel = { start: null, ergebnis: '#buehne', erklaert: handy ? '#s2' : null, messung: handy ? '#s3' : '#s3', ln: handy ? '#buehne' : '#s3', auftrag3: handy ? '#buehne' : '#weiter', modell: '#modell' }[z];
  if (!handy && z !== 'start') await p.evaluate(() => window.scrollTo(0, document.querySelector('.raster').getBoundingClientRect().top + scrollY - 10));
  if (ziel && (handy || ['messung', 'ln', 'auftrag3', 'modell'].includes(z))) await p.evaluate(s => document.querySelector(s).scrollIntoView({ block: 'start' }), ziel);
  await p.waitForTimeout(150);
}
const FAELLE = [
  ['1_start', 'start', ['handy', 'laptop', 'beamer'], ['de', 'en']],
  ['2_ergebnis', 'ergebnis', ['handy', 'laptop'], ['de']],
  ['3_erklaert', 'erklaert', ['handy', 'laptop', 'beamer'], ['de', 'en']],
  ['4_messung', 'messung', ['handy', 'laptop'], ['de']],
  ['5_ln', 'ln', ['handy', 'laptop'], ['de', 'en']],
  ['6_auftrag3', 'auftrag3', ['handy', 'laptop'], ['de']],
  ['7_modell', 'modell', ['laptop'], ['de']],
];
(async () => {
  fs.mkdirSync(ZIEL, { recursive: true });
  const b = await chromium.launch();
  const liste = [];
  for (const [name, z, geraete, sprachen] of FAELLE) for (const g of geraete) for (const l of sprachen) {
    const [w, h] = GERAETE[g];
    const ctx = await b.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 2 });
    const p = await ctx.newPage();
    p.on('dialog', d => d.accept());
    await p.goto(URL + '?lang=' + l);
    await p.evaluate(() => document.fonts.ready);
    await zustand(p, z);
    await blick(p, g, z);
    const datei = `${name}_${g}_${w}x${h}_${l}.jpg`;
    await p.screenshot({ path: path.join(ZIEL, datei), type: 'jpeg', quality: 82 });
    liste.push(datei);
    await ctx.close();
  }
  await b.close();
  fs.writeFileSync(path.join(ZIEL, 'LISTE.txt'), 'Bildschirmfotos Fassung 3 (node simulation/tests/bilder.js), Gerätefaktor 2:\n' + liste.join('\n') + '\n');
  console.log(liste.length, 'Bilder');
})();
