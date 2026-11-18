// node render.js  -> png/placa-N.jpg desde slide-N.html
const { chromium } = require('playwright'); const path = require('path');
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  for (let i = 1; i <= 5; i++) { await p.goto('file://' + path.resolve(`slide-${i}.html`)); await p.waitForTimeout(1500);
    await p.screenshot({ path: `png/placa-${i}.jpg`, type: 'jpeg', quality: 92 }); } await b.close(); })();
