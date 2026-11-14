const {chromium}=require('playwright');(async()=>{const [,,out,fps,dur,test]=process.argv;const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+process.cwd()+'/reel.html');await p.waitForTimeout(2500);
await p.evaluate(()=>{document.querySelectorAll('.sc').forEach(e=>e.style.display='block')});await p.evaluate(()=>prep());
const times=test?test.split(',').map(Number):[...Array(Math.round(dur*fps)).keys()].map(i=>i/fps);
for(let i=0;i<times.length;i++){await p.evaluate(t=>render(t),times[i]);await p.evaluate(()=>{const i=document.getElementById('bg');return i.complete?0:new Promise(r=>{i.onload=r;i.onerror=r})});
await p.screenshot({path:`${out}/f${String(i).padStart(4,'0')}.jpg`,type:'jpeg',quality:90});}await b.close()})();
