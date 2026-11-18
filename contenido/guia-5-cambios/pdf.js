const { chromium } = require('playwright'); const path = require('path');
(async () => { const b = await chromium.launch(); const p = await b.newPage();
 await p.goto('file://' + path.resolve('guia.html')); await p.waitForTimeout(2000);
 await p.pdf({ path: 'Guia-5-cosas-Flora-Marketing.pdf', format: 'A4', printBackground: true, preferCSSPageSize: true });
 await b.close(); })();
