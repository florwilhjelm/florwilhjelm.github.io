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
(f'<h1 style="font-size:112px;margin-top:30px">Tu local ya es conocido en tu ciudad.</h1><p style="font-size:62px;margin-top:46px;max-width:620px">Ahora te toca expandirte a {mk("todo el país.")}</p><p class="k" style="margin-top:40px">te muestro cómo en 3 pasos →</p>','avatar-pensativa.png',360,430),
(f'<h1 style="font-size:84px;margin-top:30px;max-width:840px">Tenés años en el rubro, clientes fieles y un producto que funciona.</h1><p style="font-size:62px;margin-top:50px;max-width:560px">Ahora te toca expandirte a {mk("todo el país.")}</p>','avatar-frustrada.png',360,380),
(f'<h1 style="font-size:90px;margin-top:30px">Lo más difícil ya lo tenés: {mk("la confianza.")}</h1><p style="margin-top:44px;max-width:560px">Lo que falta no es un producto nuevo. Es que te encuentren y te puedan comprar desde cualquier lugar.</p>','avatar-senalando.png',360,410),
(f'<p class="k">paso 1</p><h1 style="font-size:96px;margin-top:6px">Una tienda online {mk("lista para vender.")}</h1><p style="margin-top:44px;max-width:780px">Fotos y videos claros, talles, descripciones, precios y testimonios. Que comprar sea tan fácil como entrar a tu local.</p>',None,0,0),
(f'<p class="k">paso 2</p><h1 style="font-size:92px;margin-top:6px">Una estrategia de contenido {mk("para anuncios.")}</h1><p style="margin-top:44px;max-width:800px">No alcanza con “poner plata en publicidad”. Necesitás contenido pensado para que tu cliente ideal, esté donde esté, se detenga, te conozca y te compre.</p>',None,0,0),
(f'<p class="k">paso 3</p><h1 style="font-size:96px;margin-top:6px">Contenido real {mk("de tu negocio.")}</h1><p style="margin-top:44px;max-width:800px">Tu local, tus productos y tu historia. La trayectoria que te hizo conocido en tu ciudad es lo que va a hacer que te elijan en todo el país.</p>',None,0,0),
(f'<h1 style="font-size:84px;margin-top:30px;max-width:820px">Un local de deportes hizo esto y pasó de</h1><h1 style="font-size:120px;margin-top:20px">3.000 → {mk("13.000 USD",-3)}</h1><p style="font-size:62px;margin-top:20px">en un mes.</p>','avatar-contenta.png',340,380),
(f'<h1 style="font-size:100px;margin-top:30px">¿Querés ver cómo sería {mk("con tu negocio?")}</h1><p style="margin-top:50px;max-width:560px">Escribime <b>EXPANDIR</b> por MD y lo vemos juntos 🌷</p>','avatar-contenta.png',400,450),
]
for i,(body,av,w,h) in enumerate(S,1):
    open(f'slide-{i}.html','w').write(page(body,av,w,h))
print(len(S))
