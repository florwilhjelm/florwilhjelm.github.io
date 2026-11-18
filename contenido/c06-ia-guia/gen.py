# Carrusel "Guía 5 cosas con IA" — estilo foto + carteles

T = '#3D2B4F'; L = '#8F79B3'; LI = '#C9B6E4'; BE = '#FAF6EE'
paper = ("background-color:#FAF6EE;background-image:url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='f'><feTurbulence type='fractalNoise' baseFrequency='.05' numOctaves='4' seed='3' result='n'/><feDiffuseLighting in='n' surfaceScale='1.6' lighting-color='%23fffaf0'><feDistantLight azimuth='225' elevation='55'/></feDiffuseLighting><feColorMatrix values='0 0 0 0 .42  0 0 0 0 .36  0 0 0 0 .3  -.8 0 0 0 .78'/></filter><rect width='100%25' height='100%25' filter='url(%23f)'/></svg>\");background-size:400px 400px;")

css = f"""*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;font-family:'Andika',sans-serif;background:#111}}
.s{{position:relative;width:1080px;height:1350px;background-size:cover;background-position:center}}
.s:before{{content:'';position:absolute;inset:0;background:linear-gradient(rgba(20,12,28,.55),rgba(20,12,28,.25) 40%,rgba(20,12,28,.6))}}
.c{{position:absolute;left:0;right:0;display:flex;flex-direction:column;align-items:center;text-align:center;gap:14px;padding:0 70px}}
.box{{white-space:nowrap;background:{BE};color:{T};font-weight:700;font-size:54px;line-height:1.18;padding:14px 30px 18px;border-radius:22px;box-shadow:0 6px 24px rgba(0,0,0,.25)}}
.w{{white-space:nowrap;color:#fff;font-weight:700;font-size:50px;line-height:1.2;text-shadow:0 3px 14px rgba(0,0,0,.6)}}
.h{{color:{LI}}}
.dk{{background:rgba(30,20,40,.82);color:#fff;font-weight:700;font-size:56px;padding:14px 30px 18px;border-radius:20px}}
.logo{{position:absolute;bottom:46px;left:0;right:0;text-align:center}} .logo img{{height:58px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))}}
.bub{{position:absolute;width:150px;height:62px;border-radius:22px;background:{LI};box-shadow:0 0 30px rgba(201,182,228,.85),inset 0 -6px 0 rgba(143,121,179,.35)}}
.bub:after{{content:'';position:absolute;right:16px;bottom:-14px;border:12px solid transparent;border-top-color:{LI};border-right-color:{LI}}}
.paper{{position:absolute;left:90px;right:90px;bottom:120px;height:560px;{paper}border-radius:6px;box-shadow:0 14px 40px rgba(0,0,0,.45);transform:rotate(-1.2deg);
  font-family:'Patrick Hand';color:{T};font-size:52px;padding:46px 56px}}
.row2{{display:flex;align-items:center;gap:26px;height:92px}} .nn{{flex:0 0 64px;height:64px;border-radius:50%;border:4px solid {L};color:{L};display:flex;align-items:center;justify-content:center;font-size:44px}}
.row{{display:flex;align-items:center;height:88px}} .row .n{{width:470px}} .ok{{color:{L};font-size:60px}} .fa{{color:{L};display:flex;align-items:center;gap:14px}}
"""

def page(bg, body):
    return (f'<!doctype html><html><head><meta charset="utf-8">'
            f'<link href="https://fonts.googleapis.com/css2?family=Andika:wght@400;700&family=Patrick+Hand&display=swap" rel="stylesheet">'
            f'<style>{css}</style></head><body><div class="s" style="background-image:url(fotos/{bg}.jpg)">{body}</div></body></html>')


lista = ''.join(f'<div class="row2"><span class="nn">{i}</span>{t}</div>' for i, t in enumerate([
    'WhatsApp que responde solo', 'fotos que venden', 'descripciones con IA', 'que te encuentren en Google', 'publicar con un plan'], 1))

S = [
    ('ciudad', '''<div class="c" style="top:110px"><div class="box">¿Ves que todos usan IA<br>para sus negocios y vos sentís<br>que te quedaste atrás<br>con tu local?</div></div>'''),
    ('noche', '''<div class="c" style="top:90px"><div class="box">Ves marcas que arrancaron<br>hace un año, sin local,<br>y venden más que vos.</div>
      <div class="w" style="margin-top:12px">Y vos pagás alquiler, sueldos, luz…<br><span class="h">y tenés años de trayectoria</span></div></div>'''),
    ('cafe', '''<div class="c" style="top:110px"><div class="box">No te falta tecnología.</div>
      <div class="w" style="margin-top:12px">Te falta <span class="h">mostrar online</span><br><span class="h">lo que ya tenés:</span><br>clientes, productos y confianza</div></div>'''),
    ('mesa', f'''<div class="c" style="top:70px"><div class="box">Te armé una guía con 5 cosas<br>que podés cambiar hoy<br>en tu negocio</div>
      <div class="w" style="margin-top:8px;font-size:44px">con ayuda de la IA y<br><span class="h">sin dejar tu local</span></div></div>
      <div class="paper">{lista}</div>'''),
    ('flores', '''<div class="c" style="bottom:190px"><div class="dk">Respondé <span class="h">IA</span> y te la mando</div></div>
      <div class="logo"><img src="flora-palabra-lila.png"></div>'''),
]
for i, (bg, body) in enumerate(S, 1):
    open(f'slide-{i}.html', 'w').write(page(bg, body))
