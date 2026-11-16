import random,math
T='#3D2B4F';L='#8F79B3';LI='#C9B6E4';C='#FBF7F0';B='#F1E8DA'
def series(n,noise,trend,seed):
    r=random.Random(seed);ys=[trend*i/(n-1)+r.uniform(-noise,noise) for i in range(n)]
    ys[-2]=max(ys[:-2])+noise*0.2; ys[-1]=ys[-2]+max(noise*0.9,trend*0.06); return ys
def chart(ys,w=260,h=300):
    lo,hi=min(ys),max(ys);pts=[(18+i*(w-50)/(len(ys)-1),h-30-(y-lo)/(hi-lo)*(h-90)) for i,y in enumerate(ys)]
    d='M'+' L'.join(f'{x:.1f} {y:.1f}' for x,y in pts)
    x1,y1=pts[-2];x2,y2=pts[-1];a=math.atan2(y2-y1,x2-x1)
    ah=f'M{x2-24*math.cos(a-0.5):.1f} {y2-24*math.sin(a-0.5):.1f} L{x2:.1f} {y2:.1f} L{x2-24*math.cos(a+0.5):.1f} {y2-24*math.sin(a+0.5):.1f}'
    return f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}"><path d="M12 14 C 11 120, 13 200, 12 {h-22} C 90 {h-20}, 170 {h-24}, {w-10} {h-22}" stroke="{T}" stroke-opacity=".35" stroke-width="3" fill="none" stroke-linecap="round"/><path d="{d}" stroke="{L}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/><path d="{ah}" stroke="{L}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
a=series(18,1.0,0.6,3);b=series(22,0.45,2.6,5);c=series(26,0.18,4.5,8)
s=open('placa.html').read()
import re
svgs=re.findall(r'<svg viewBox.*?</svg>',s,re.S);print(len(svgs))
for old,new in zip(svgs,[chart(a),chart(b),chart(c)]): s=s.replace(old,new)
open('placa.html','w').write(s)
