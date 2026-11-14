fonts='<link href="https://fonts.googleapis.com/css2?family=Patrick+Hand&family=Caveat:wght@600;700&display=swap" rel="stylesheet">'
T='#3D2B4F';L='#8F79B3';LI='#C9B6E4';SOFT='#E9DFF5';C='#FBF7F0';B='#F1E8DA'
def flor(size,color=L,sw=4):
    p=''.join(f'<ellipse cx="50" cy="28" rx="15" ry="22" transform="rotate({i*72} 50 50)"/>' for i in range(5))
    return f'<svg width="{size}" height="{size}" viewBox="0 0 100 100" style="overflow:visible"><g fill="none" stroke="{color}" stroke-width="{sw*2}">{p}</g><g fill="{C}" stroke="none">{p}</g><circle cx="50" cy="50" r="7" fill="none" stroke="{color}" stroke-width="{sw}"/></svg>'
def marker(txt,rot=-2):
    return f'<span class="mk" style="--r:{rot}deg">{txt}</span>'
css=f'''*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;background:{C};font-family:'Patrick Hand';color:{T}}}
.s{{width:1080px;height:1350px;padding:100px 80px 56px;display:flex;flex-direction:column;position:relative}}
.mk{{position:relative;display:inline-block;padding:0 14px;z-index:0}}
.mk:before{{content:"";position:absolute;left:-4px;right:-4px;top:22%;bottom:6%;background:{LI};border-radius:40% 55% 45% 60% / 60% 40% 65% 45%;transform:rotate(var(--r));z-index:-1;opacity:.9}}
.kicker{{font-family:Caveat;font-weight:700;font-size:52px;color:{L}}}
h1{{font-weight:400;font-size:104px;line-height:1.02;margin-top:14px}}
p{{font-size:50px;line-height:1.3;margin-top:28px}}
.note{{background:{B};padding:34px 38px 30px;font-size:46px;line-height:1.25;position:relative;box-shadow:0 10px 20px rgba(61,43,79,.10)}}
.note:before{{content:"";position:absolute;top:-18px;left:50%;width:150px;height:38px;margin-left:-75px;background:{LI};opacity:.85;transform:rotate(-3deg)}}
.foot{{margin-top:auto;display:flex;justify-content:center}}.foot img{{height:52px}}
.avatar{{border-radius:50%;background:{SOFT};display:grid;place-items:center;color:{L};font-size:30px;text-align:center;overflow:hidden}}
.avatar img{{width:100%;height:100%;object-fit:cover}}'''
def page(body): return f'<!doctype html><html><head><meta charset="utf-8">{fonts}<style>{css}</style></head><body><div class="s">{body}<div class="foot"><img src="flora-palabra-lila.png"></div></div></body></html>'
AV1='<div class="avatar" style="width:470px;height:470px">avatar</div>'
AV2='<div class="avatar" style="width:330px;height:330px">avatar</div>'
S1=f'''<div class="kicker">para dueños de locales</div>
<h1>Tu local ya es conocido en tu ciudad. ¿Y si tu próximo cliente {marker("está en otra provincia?",-2)}</h1>
<div style="display:flex;align-items:flex-end;justify-content:space-between;margin-top:30px">
<p style="max-width:440px;margin:0 0 40px">Te muestro cómo llegar a él en 3 pasos <span style="color:{L}">→</span></p>{AV1}</div>
<div style="position:absolute;left:110px;top:1110px">{flor(64)}</div><div style="position:absolute;right:70px;top:110px">{flor(56,LI)}</div>'''
S2=f'''<div style="display:flex;align-items:center;gap:20px">{flor(84)}<div><div class="kicker" style="margin:0">paso 1</div><h1 style="margin:0;font-size:96px">Ordená tus {marker("números",-3)}</h1></div></div>
<div style="display:flex;gap:44px;margin-top:70px;align-items:flex-start">
<div style="flex:1.15;display:flex;flex-direction:column;gap:60px">
<div class="note" style="transform:rotate(-2deg)">Invertís en anuncios sin saber tu margen.</div>
<svg width="160" height="80" viewBox="0 0 160 80" style="margin-left:120px"><path d="M10 10 C 40 70, 110 70, 140 30" stroke="{L}" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M118 28 L142 28 L138 52" stroke="{L}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>
<div class="note" style="transform:rotate(1.5deg)">Vendés… pero no sabés si <b style="color:{L};font-weight:400">estás ganando.</b></div></div>
<div style="flex:.85;display:flex;flex-direction:column;align-items:center;gap:20px">{AV2}<div style="font-family:Caveat;font-size:44px;color:{L};text-align:center;transform:rotate(-3deg)">¿me suena conocido?</div></div></div>
<p style="text-align:center;margin-top:70px;font-size:56px">Con tu margen sabés {marker("cuánto podés invertir",2)} sin perder plata.</p>'''
for n,b in [('flora-ilustrado-1',S1),('flora-ilustrado-2',S2)]:
    open(n+'.html','w').write(page(b))
