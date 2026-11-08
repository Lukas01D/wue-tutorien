// Bildschirmfotos des Gestaltungsmusters Fassung 3 (Handy 390, Laptop 1366, Beamer 1280 x 720), Gerätefaktor 2
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const ZIEL = path.resolve(__dirname, '../bildschirmfotos/f3_entwurf');
const DATEI = 'file://' + path.resolve(__dirname, 'muster.html');
const FAELLE = [
  ['1_startkarte_390x844', 390, 844, '0', null],
  ['2_ergebnis_390x844', 390, 844, '2', '#buehne'],
  ['3_warum_390x844', 390, 844, '2', '#s2'],
  ['1_startkarte_1366x768', 1366, 768, '0', null],
  ['2_ergebnis_1366x768', 1366, 768, '2', null],
  ['2_ergebnis_beamer_1280x720', 1280, 720, '2', null],
];
(async () => {
  fs.mkdirSync(ZIEL, { recursive: true });
  const browser = await chromium.launch();
  for (const [name, w, h, z, ziel] of FAELLE) {
    const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 2 });
    await page.goto(DATEI + '?zustand=' + z);
    await page.evaluate(() => document.fonts.ready);
    if (ziel) await page.evaluate(s => document.querySelector(s).scrollIntoView({ block: 'start' }), ziel);
    else if (z !== '0' && w >= 1024) await page.evaluate(() => window.scrollTo(0, document.querySelector('.raster').offsetTop - 10));
    const quer = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
    await page.screenshot({ path: path.join(ZIEL, name + '.png') });
    console.log(name, 'waagerechter Überlauf', quer, 'px');
    await page.close();
  }
  await browser.close();
})();
