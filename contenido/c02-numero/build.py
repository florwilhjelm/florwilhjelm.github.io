import sys
AV=sys.argv[1]  # carpeta de avatares
T='#3D2B4F';L='#8F79B3';LI='#C9B6E4';C='#FBF7F0';B='#F1E8DA'
paper=f"background-color:{C};background-image:linear-gradient(90deg,transparent 118px,rgba(201,182,228,.9) 118px,rgba(201,182,228,.9) 121px,transparent 121px),repeating-linear-gradient(180deg,transparent 0 63px,rgba(61,43,79,.10) 63px 65px);"
def flor(size,color=L,sw=4):
    p=''.join(f'<ellipse cx="50" cy="28" rx="15" ry="22" transform="rotate({i*72} 50 50)"/>' for i in range(5))
    return f'<svg width="{size}" height="{size}" viewBox="0 0 100 100" style="overflow:visible"><g fill="none" stroke="{color}" stroke-width="{sw*2}">{p}</g><g fill="{C}">{p}</g><circle cx="50" cy="50" r="7" fill="none" stroke="{color}" stroke-width="{sw}"/></svg>'
def mk(t,r=-2): return f'<span class="mk" style="--r:{r}deg">{t}</span>'
css=f'''*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;{paper}font-family:'Andika';color:{T}}}
.s{{width:1080px;height:1350px;padding:100px 80px 46px 160px;display:flex;flex-direction:column;position:relative}}
.mk{{position:relative;display:inline-block;padding:0 12px;z-index:0}}
.mk:before{{content:"";position:absolute;left:-4px;right:-4px;top:28%;bottom:4%;background:{LI};border-radius:40% 55% 45% 60%/60% 40% 65% 45%;transform:rotate(var(--r));z-index:-1}}
h1{{font-weight:400;line-height:1.12}} p{{font-size:54px;line-height:1.35}}
.k{{font-size:40px;color:{L}}}
.av{{position:absolute;right:40px;bottom:120px;object-fit:contain;object-position:50% 100%}}
.foot{{margin-top:auto;display:flex;justify-content:center;margin-left:-80px}}.foot img{{height:50px}}
.f{{position:absolute;right:80px;top:80px}}'''
def page(body,av=None,avw=420,avh=440,deco=True):
    a=f'<img class="av" src="{AV}/{av}" style="width:{avw}px;height:{avh}px">' if av else ''
    d=f'<div class="f">{flor(54)}</div>' if deco else ''
    if not av: body=f'<div style="margin-top:auto">{body}</div><div style="position:absolute;right:90px;bottom:150px">{flor(70,LI)}</div>'
    return f'<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Andika:wght@400;700&display=swap" rel="stylesheet"><style>{css}</style></head><body><div class="s">{d}{body}{a}<div class="foot"><img src="flora-palabra-lila.png"></div></div></body></html>'
S=[
(f'<h1 style="font-size:104px;margin-top:40px">El número que tenés que saber antes de invertir en {mk("publicidad.")}</h1><p class="k" style="margin-top:50px">deslizá →</p>','avatar-pensativa.png',400,470),
(f'<h1 style="font-size:100px;margin-top:40px">Vender mucho no siempre es {mk("ganar.")}</h1><p style="margin-top:44px;max-width:540px">Hay negocios que venden más con anuncios… y pierden plata en cada venta.</p>','avatar-frustrada.png',380,400),
(f'<p class="k">paso 1</p><h1 style="font-size:100px;margin-top:6px">Conocé tu {mk("margen.")}</h1><p style="margin-top:44px;max-width:560px">Es lo que te queda de cada venta después de pagar la mercadería, las comisiones y los impuestos.</p>','avatar-senalando.png',380,430),
(f'<p class="k">paso 2</p><h1 style="font-size:150px;margin-top:40px;color:{L}">1 ÷ margen</h1><h1 style="font-size:84px;margin-top:20px">= tu {mk("ROAS mínimo")}</h1><p style="margin-top:50px;max-width:760px">Es cuánto tenés que vender por cada $1 que invertís para no perder plata.</p>',None,0,0),
(f'<p class="k">ejemplo</p><h1 style="font-size:96px;margin-top:6px">Margen del 40%</h1><p style="font-size:70px;margin-top:40px">1 ÷ 0,40 = {mk("2,5",-3)}</p>'
 f'<svg width="140" height="110" viewBox="0 0 140 110" style="margin:24px 0 0 40px"><path d="M15 10 C 20 60, 60 90, 120 80" stroke="{L}" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M98 64 L122 80 L100 98" stroke="{L}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
 f'<p style="margin-top:20px;max-width:780px">Si invertís <b>$100.000</b> en anuncios, tenés que vender al menos <b>$250.000</b> para no perder.</p>',None,0,0),
(f'<h1 style="font-size:96px;margin-top:40px">Por debajo de ese número, la publicidad {mk("te cuesta plata.")}</h1><p style="margin-top:50px;font-size:62px">Por arriba, <b style="color:{L}">te deja ganancia.</b></p><p style="margin-top:20px">Así de simple.</p>',None,0,0),
(f'<h1 style="font-size:100px;margin-top:40px">Tengo una planilla que lo {mk("calcula sola.")}</h1><p style="margin-top:50px;max-width:560px">Enviame <b>PLANILLA</b> por MD y te la mando 🌷</p>','avatar-contenta.png',420,460),
]
for i,(body,av,w,h) in enumerate(S,1):
    open(f'slide-{i}.html','w').write(page(body,av,w,h))
print(len(S))
