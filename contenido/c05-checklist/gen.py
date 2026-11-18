# Carrusel "Checklist: ¿tu negocio está listo para vender online?" — estilo foto + carteles

T = '#3D2B4F'; L = '#8F79B3'; LI = '#C9B6E4'; BE = '#FAF6EE'
paper = ("background-color:#FAF6EE;background-image:url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='f'><feTurbulence type='fractalNoise' baseFrequency='.05' numOctaves='4' seed='3' result='n'/><feDiffuseLighting in='n' surfaceScale='1.6' lighting-color='%23fffaf0'><feDistantLight azimuth='225' elevation='55'/></feDiffuseLighting><feColorMatrix values='0 0 0 0 .42  0 0 0 0 .36  0 0 0 0 .3  -.8 0 0 0 .78'/></filter><rect width='100%25' height='100%25' filter='url(%23f)'/></svg>\");background-size:400px 400px;")

css = f"""*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;font-family:'Andika',sans-serif;background:#111}}
.s{{position:relative;width:1080px;height:1350px;background-size:cover;background-position:center}}
.s:before{{content:'';position:absolute;inset:0;background:linear-gradient(rgba(20,12,28,.55),rgba(20,12,28,.25) 40%,rgba(20,12,28,.6))}}
.c{{position:absolute;left:0;right:0;display:flex;flex-direction:column;align-items:center;text-align:center;gap:14px;padding:0 70px}}
.box{{background:{BE};color:{T};font-weight:700;font-size:54px;line-height:1.18;padding:14px 30px 18px;border-radius:22px;box-shadow:0 6px 24px rgba(0,0,0,.25)}}
.w{{color:#fff;font-weight:700;font-size:50px;line-height:1.2;text-shadow:0 3px 14px rgba(0,0,0,.6)}}
.h{{color:{LI}}}
.dk{{background:rgba(30,20,40,.82);color:#fff;font-weight:700;font-size:56px;padding:14px 30px 18px;border-radius:20px}}
.logo{{position:absolute;bottom:46px;left:0;right:0;text-align:center}} .logo img{{height:58px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))}}
.bub{{position:absolute;width:150px;height:62px;border-radius:22px;background:{LI};box-shadow:0 0 30px rgba(201,182,228,.85),inset 0 -6px 0 rgba(143,121,179,.35)}}
.bub:after{{content:'';position:absolute;right:16px;bottom:-14px;border:12px solid transparent;border-top-color:{LI};border-right-color:{LI}}}
.paper{{position:absolute;left:90px;right:90px;bottom:120px;height:560px;{paper}border-radius:6px;box-shadow:0 14px 40px rgba(0,0,0,.45);transform:rotate(-1.2deg);
  font-family:'Patrick Hand';color:{T};font-size:52px;padding:46px 56px}}
.row{{display:flex;align-items:center;height:88px}} .row .n{{width:470px}} .ok{{color:{L};font-size:60px}} .fa{{color:{L};display:flex;align-items:center;gap:14px}}
"""

def page(bg, body):
    return (f'<!doctype html><html><head><meta charset="utf-8">'
            f'<link href="https://fonts.googleapis.com/css2?family=Andika:wght@400;700&family=Patrick+Hand&display=swap" rel="stylesheet">'
            f'<style>{css}</style></head><body><div class="s" style="background-image:url(fotos/{bg}.jpg)">{body}</div></body></html>')

bubbles = ''.join(f'<div class="bub" style="left:{x}px;top:{y}px;width:{w}px;opacity:{o}"></div>' for x, y, w, o in [
    (700, 380, 170, 1), (640, 480, 140, .95), (760, 560, 180, 1), (660, 660, 150, .95), (780, 750, 130, .9),
    (620, 840, 170, 1), (740, 935, 140, .95), (650, 1030, 120, .9)])

flecha = '<svg width="120" height="30" viewBox="0 0 120 30"><path d="M4 15 H110 M96 4 L112 15 L96 26" fill="none" stroke="#8F79B3" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
items = [('fotos de productos', True), ('stock al día', True), ('catálogo en WhatsApp', False), ('medios de pago', True), ('envíos', False)]
lista = ''.join(f'<div class="row"><span class="n">{n}</span>' + (f'<span class="ok">✓</span>' if ok else f'<span class="fa">{flecha} falta</span>') + '</div>' for n, ok in items)

S = [
    ('noche', f'''{bubbles}<div class="c" style="top:80px"><div class="box">¿Tu local cierra a las 20<br>y te escriben a las 23<br>para comprar?</div></div>'''),
    ('ciudad', '''<div class="c" style="bottom:170px"><div class="box">Esa consulta la contestás<br>recién mañana.</div>
      <div class="w" style="margin-top:10px">Y para mañana,<br><span class="h">ya compró en otro lado</span></div></div>'''),
    ('cafe', '''<div class="c" style="top:110px"><div class="box">No te faltan clientes.</div>
      <div class="w" style="margin-top:10px">Te falta un negocio que<br><span class="h">venda cuando vos no estás</span></div></div>'''),
    ('mesa', f'''<div class="c" style="top:70px"><div class="box">Te armé una checklist para ver<br>si tu negocio está listo para vender online</div>
      <div class="w" style="margin-top:8px;font-size:44px">qué tenés, qué te falta<br>y <span class="h">por dónde empezar primero</span></div></div>
      <div class="paper">{lista}</div>'''),
    ('flores', '''<div class="c" style="bottom:190px"><div class="dk">Respondé <span class="h">ONLINE</span> y te la mando</div></div>
      <div class="logo"><img src="flora-palabra-lila.png"></div>'''),
]

for i, (bg, body) in enumerate(S, 1):
    open(f'slide-{i}.html', 'w').write(page(bg, body))
