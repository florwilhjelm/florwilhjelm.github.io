const {chromium}=require('playwright');(async()=>{const [,,out,fps,dur]=process.argv;const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+process.cwd()+'/overlay.html');await p.waitForTimeout(2500);const n=Math.round(dur*fps);
for(let i=0;i<n;i++){await p.evaluate(t=>render(t),i/fps);await p.screenshot({path:`${out}/o${String(i).padStart(4,'0')}.png`,omitBackground:true});}await b.close()})();
