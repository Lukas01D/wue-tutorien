const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1420, height: 1000 }, deviceScaleFactor: 2 });
  await p.goto('file://' + process.cwd() + '/skizzen.html'); await p.waitForTimeout(400);
  await (await p.$('#laptop')).screenshot({ path: 'skizze_laptop_1366.png' });
  const h1 = await p.$('#handy1'), h2 = await p.$('#handy2');
  await h1.screenshot({ path: 'skizze_handy_start.png' }); await h2.screenshot({ path: 'skizze_handy_arbeit.png' });
  await b.close();
})();
