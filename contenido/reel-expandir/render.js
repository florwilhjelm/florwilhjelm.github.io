const {chromium}=require('playwright');
(async()=>{const [,,out,fps,dur,test]=process.argv;const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+process.cwd()+'/reel.html');await p.waitForTimeout(2500);
await p.evaluate(async()=>{const AVP=['avatar-pensativa.png','avatar-senalando.png','avatar-frustrada.png','avatar-contenta.png'];const base=document.querySelector('script').textContent.match(/const AV='([^']+)'/)[1];await Promise.all(AVP.map(n=>new Promise(r=>{const i=new Image();i.onload=r;i.onerror=r;i.src=base+n;})));});
const times=test?test.split(',').map(Number):[...Array(Math.round(dur*fps)).keys()].map(i=>i/fps);
for(let i=0;i<times.length;i++){await p.evaluate(t=>{render(t)},times[i]);await p.evaluate(()=>{const a=document.querySelector('.av');return a.complete?null:a.decode().catch(()=>null)});
await p.screenshot({path:`${out}/f${String(i).padStart(4,'0')}.jpg`,type:'jpeg',quality:90});}
await b.close()})();
