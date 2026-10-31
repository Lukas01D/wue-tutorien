// Unabhängiger X3-Browsertest. Aufruf im Repository: node ergebnisse/kaffee/codex_skripte/x3/bedienung_browser.js
// Benötigt Playwright und Chromium. Die lokale Datei wird offline per Playwright-Route
// ausgeliefert, da die verwaltete Chromium-Richtlinie file:// sperrt.
const { chromium } = require('playwright');
const fs = require('node:fs');
const path = require('node:path');
const out = __dirname;
const target = path.resolve(out, '../../simulation/Kaffee_Simulation.html');
const localURL = 'http://localhost:31460/x3-simulation.html';
const log = { target: path.relative(process.cwd(), target), started: new Date().toISOString(), requests: [], errors: [], checks: [] };
function record(name, value) { log.checks.push({ name, value }); }
async function snapshot(page) {
  return page.evaluate(() => ({
    sliders: Object.fromEntries([...document.querySelectorAll('input[type=range]')].map(x => [x.id, x.value])),
    toggles: Object.fromEntries([...document.querySelectorAll('input[type=checkbox]')].map(x => [x.id, x.checked])),
    values: document.querySelector('#zahlen').innerText,
    statement: document.querySelector('#aussage').innerText,
    warning: document.querySelector('#warnung').innerText,
    info: document.querySelector('#uebernahme_info').innerText,
    measurements: [...document.querySelectorAll('#messtabelle tbody tr')].map(x => x.innerText),
    width: innerWidth, documentWidth: document.documentElement.scrollWidth,
    invalidSVG: /NaN|Infinity/.test(document.querySelector('#diagramm').innerHTML),
  }));
}
async function slider(page, id, value) {
  await page.locator('#' + id).evaluate((e,v) => { e.value = String(v); e.dispatchEvent(new Event('input', {bubbles:true})); }, value);
}
async function add(page, becher, time, temperature) {
  await page.locator('#m_becher').selectOption(String(becher));
  await page.locator('#m_t').fill(String(time));
  await page.locator('#m_th').fill(String(temperature));
  await page.locator('#messform button').click();
}
async function shot(page, name) { await page.screenshot({path:path.join(out, name + '.png'),fullPage:true}); }
(async () => {
  const browser = await chromium.launch({executablePath:'/usr/bin/chromium',headless:true,args:['--no-sandbox']});
  try {
    for (const width of [1366,390]) {
      const context = await browser.newContext({viewport:{width,height:900},offline:true,locale:'de-DE'});
      await context.route('**/*', route => {
        const url = route.request().url();
        log.requests.push({width,url});
        return url === localURL ? route.fulfill({status:200,contentType:'text/html; charset=utf-8',body:fs.readFileSync(target)}) : route.abort();
      });
      const page = await context.newPage();
      page.on('pageerror', error => log.errors.push({width,message:error.message}));
      page.on('console', message => { if (message.type() === 'error') log.errors.push({width,message:message.text()}); });
      await page.goto(localURL);
      record(width + ' Standard offline',await snapshot(page));
      await shot(page,'bedienung_' + width + '_standard');
      await page.locator('summary').click();
      const ids = await page.locator('input[type=range]').evaluateAll(xs => xs.map(x=>({id:x.id,min:x.min,max:x.max})));
      for (const {id,min,max} of ids) {
        for (const value of [min,max]) {
          await page.locator('#standard').click();
          await slider(page,id,value);
          record(width + ' Regler ' + id + '=' + value,await snapshot(page));
        }
      }
      await page.locator('#standard').click();
      await page.locator('#milch2Raum').check();
      record(width + ' Milch Raum',await snapshot(page));
      await page.locator('#milch2Raum').uncheck();
      await page.locator('#becher').check();
      record(width + ' Becher',await snapshot(page));
      await page.locator('#becher').uncheck();
      await page.locator('#versuch').click();
      record(width + ' Versuchsknopf',await snapshot(page));
      await page.locator('#standard').click();
      await page.locator('#uebernehmen').click();
      record(width + ' Übernehmen ohne Daten',await snapshot(page));
      await page.locator('#standard').click();
      for (const row of [[2,'0','80,2'],[3,'0.0','81.2'],[2,'10,0','66,5'],[3,'10.0','67.5'],[1,'40','39,8'],[2,'40','36.1'],[3,'40','38,2']]) await add(page,...row);
      record(width + ' Komma und Punkt',await snapshot(page));
      await page.reload();
      record(width + ' Neuladen mit Daten',await snapshot(page));
      await page.locator('#uebernehmen').click();
      record(width + ' Mittelwerte übernehmen',await snapshot(page));
      await shot(page,'bedienung_' + width + '_messwerte');
      await page.locator('#messtabelle button').first().click();
      record(width + ' Einzelwert löschen',await snapshot(page));
      await page.locator('#leeren').click();
      await page.reload();
      record(width + ' Alle löschen und neu laden',await snapshot(page));
      for (const [time,temperature] of [['-1','50'],['241','50'],['10','-11'],['10','101'],['abc','50'],['10','Infinity'],['','50'],['10',''],['10min','67°C'],['10,5,9','66.5xyz'],['0','-10'],['240','100']]) {
        await page.locator('#leeren').click();
        await add(page,2,time,temperature);
        record(width + ' Eingabe ' + JSON.stringify([time,temperature]),await snapshot(page));
      }
      await page.locator('#leeren').click();
      await page.locator('#standard').click();
      await slider(page,'thK0',60);
      record(width + ' Messwert größer als Start',await snapshot(page));
      await shot(page,'bedienung_' + width + '_ungueltig');
      await slider(page,'thMess',55);
      record(width + ' Nach Korrektur gültig',await snapshot(page));
      await slider(page,'thU',30);
      await slider(page,'thMess',30);
      record(width + ' Messwert gleich Raum',await snapshot(page));
      await page.locator('#standard').click();
      await page.locator('#leeren').click();
      await add(page,2,0,100); await add(page,3,0,100);
      await add(page,2,10,15); await add(page,3,10,15);
      await page.locator('#uebernehmen').click();
      record(width + ' Übernahme außerhalb Reglerbereich',await snapshot(page));
      await page.locator('#leeren').click();
      await page.locator('#standard').click();
      for (const row of [[2,0,65],[3,0,65],[2,10,70],[3,10,70]]) await add(page,...row);
      await page.locator('#uebernehmen').click();
      record(width + ' Widersprüchliche Messreihe übernehmen',await snapshot(page));
      await shot(page,'bedienung_' + width + '_uebernahme_ungueltig');
      // Prüfe reale Tastaturbedienung, zusätzlich zu programmatischen input-Ereignissen.
      await page.locator('#standard').click();
      await page.locator('#tEnd').focus(); await page.keyboard.press('Home'); await page.keyboard.press('ArrowRight');
      record(width + ' Regler per Tastatur',await snapshot(page));
      await context.close();
    }
  } finally { await browser.close(); log.finished = new Date().toISOString(); fs.writeFileSync(path.join(out,'bedienung_ergebnisse.json'),JSON.stringify(log,null,2)+'\n'); }
  console.log(JSON.stringify({checks:log.checks.length,requests:log.requests,errors:log.errors,overflow:log.checks.filter(c=>c.value.documentWidth>c.value.width).map(c=>c.name)},null,2));
})().catch(error=>{ console.error(error);process.exitCode=1; });
