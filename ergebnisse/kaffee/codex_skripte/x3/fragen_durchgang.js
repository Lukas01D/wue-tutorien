/* Unabhaengiger Erst-Durchgang: nur sichtbare Oberflaeche, keine Modellfunktionen. */
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const out = __dirname;
const base = path.resolve(out, '../../simulation/Kaffee_Simulation.html');
const localUrl = 'http://localhost:31460/x3-simulation.html';
const log = { beginn: new Date().toISOString(), browser: '/usr/bin/chromium', datei: base, netzversuche: [], schritte: [] };
const save = () => fs.writeFileSync(path.join(out, 'fragen_browserprotokoll.json'), JSON.stringify(log, null, 2) + '\n');
(async () => {
  const browser = await chromium.launch({ executablePath: '/usr/bin/chromium', headless: true, args: ['--no-sandbox', '--disable-background-networking', '--disable-component-update', '--no-first-run'] });
  const context = await browser.newContext({ viewport: { width: 1366, height: 1000 }, offline: true });
  await context.route('**/*', async route => {
    if (route.request().url() === localUrl) return route.fulfill({ status: 200, contentType: 'text/html; charset=utf-8', body: fs.readFileSync(base) });
    log.netzversuche.push({ zeit: new Date().toISOString(), url: route.request().url() });
    await route.abort('internetdisconnected');
  });
  const page = await context.newPage();
  async function snapshot(name, screenshot = false) {
    const data = {
      schritt: name, zeit: new Date().toISOString(),
      zahlen: await page.locator('#zahlen').innerText(),
      aussage: await page.locator('#aussage').innerText(),
      warnung: await page.locator('#warnung').innerText(),
      regler: await page.locator('output').allTextContents(),
      becher: await page.locator('#becher').isChecked(),
      milch2Raum: await page.locator('#milch2Raum').isChecked()
    };
    if (screenshot) await page.screenshot({ path: path.join(out, 'fragen_' + name + '.png'), fullPage: true });
    log.schritte.push(data); save(); console.log(JSON.stringify(data));
    return data;
  }
  async function slider(id, value) {
    const control = page.locator('#' + id);
    const bounds = await control.evaluate(e => ({ min: Number(e.min), step: Number(e.step) }));
    await control.focus(); await control.press('Home');
    const count = Math.round((value - bounds.min) / bounds.step);
    for (let i = 0; i < count; i++) await control.press('ArrowRight');
  }
  // file:// ist in diesem Container durch die administrativen URL-Regeln gesperrt.
  // Der unveraenderte lokale HTML-Inhalt wird deshalb unter einer erlaubten lokalen Adresse geladen.
  // Es gibt keinen lokalen Webserver und keinerlei Internetzugriff.
  log.lademethode = 'Unveraenderte lokale HTML-Datei per context.route unter http://localhost:31460/x3-simulation.html, da file:// administrativ gesperrt';
  await page.goto(localUrl, { waitUntil: 'load' });
  await snapshot('00_standard', true);
  // Frage 1: Zeitpunkt an sichtbarem Regler durchlaufen, Maximum der Anzeige ablesen.
  await slider('tEnd', 1);
  for (let t = 1; t <= 120; t++) {
    if (t > 1) await page.locator('#tEnd').press('ArrowRight');
    await snapshot('q1_' + t + 'min', [56, 120].includes(t));
  }
  // Frage 2: bei 60 min nur die Milchtemperatur veraendern.
  await page.locator('#standard').click();
  await slider('thM', 2);
  for (let th = 2; th <= 65; th += 0.5) {
    if (th > 2) await page.locator('#thM').press('ArrowRight');
    await snapshot('q2_60min_' + th + 'grad');
  }
  await slider('thM', 47);
  await snapshot('q2_gleichheit_60min', true);
  for (const t of [40, 120]) {
    await slider('tEnd', t);
    await slider('thM', 47);
    await snapshot('q2_47grad_' + t + 'min', t === 40);
    await slider('thM', 2);
    for (let th = 2; th <= 65; th += 0.5) {
      if (th > 2) await page.locator('#thM').press('ArrowRight');
      await snapshot('q2_' + t + 'min_' + th + 'grad');
    }
  }
  // Frage 3 wird zuerst unmittelbar nach Frage 2, danach bei Standardwerten geprueft.
  await slider('tEnd', 60);
  await slider('thM', 47);
  await page.locator('#becher').check();
  await snapshot('q3_sequenziell_nach_q2', true);
  await page.locator('#standard').click();
  await snapshot('q3_standard_ohne_becher');
  await page.locator('#becher').check();
  await snapshot('q3_standard_mit_becher', true);
  // Frage 4: Es liegen keine echten Versuchswerte vor. Keine Daten erfinden.
  await page.locator('#versuch').click();
  await page.locator('#uebernehmen').click();
  const q4 = await snapshot('q4_ohne_messwerte', true);
  q4.uebernahme = await page.locator('#uebernahme_info').innerText();
  q4.tabellenzeilen = await page.locator('#messtabelle tbody tr').count();
  log.ende = new Date().toISOString();
  log.dauerSekunden = (Date.parse(log.ende) - Date.parse(log.beginn)) / 1000;
  save();
  await browser.close();
})().catch(error => { log.fehler = String(error.stack); log.ende = new Date().toISOString(); save(); console.error(error); process.exit(1); });
