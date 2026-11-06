// Sichtung der statischen Entwurfsdatei, keine Funktionsabnahme der Simulation.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

(async () => {
  const browser = await chromium.launch({headless:true, executablePath:'/usr/bin/chromium', args:['--no-sandbox']});
  const page = await browser.newPage({viewport:{width:1366,height:768}});
  const fremdeAnfragen = [];
  await page.route('**/*', route => {
    const url = route.request().url();
    if (!url.startsWith('file:')) {
      fremdeAnfragen.push(url);
      return route.abort();
    }
    return route.continue();
  });
  // Die verwaltete Browserrichtlinie sperrt file:-Navigation. Die unveraenderte
  // Datei deshalb direkt laden. Das prueft die Skizze, nicht file:-Unterstuetzung.
  await page.setContent(fs.readFileSync(path.resolve(__dirname,'../skizzen/skizzen.html'),'utf8'));
  const daten = await page.evaluate(() => ({
    realeBedienelemente:document.querySelectorAll('button,input,select,textarea').length,
    frames:[...document.querySelectorAll('.frame')].map(el=>({id:el.id,breite:el.getBoundingClientRect().width,hoehe:el.getBoundingClientRect().height})),
    diagrammPosition:getComputedStyle(document.querySelector('.sticky')).position,
    handyDiagrammHoehe:document.querySelector('#handy2 .sticky').getBoundingClientRect().height
  }));
  fs.writeFileSync(path.join(__dirname,'skizzen_befund.json'),JSON.stringify({...daten,fremdeAnfragen},null,2)+'\n');
  console.log(JSON.stringify(daten));
  await browser.close();
})().catch(error => {console.error(error.message);process.exit(1);});
