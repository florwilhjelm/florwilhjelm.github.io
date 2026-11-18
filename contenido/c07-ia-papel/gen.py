# Carrusel "¿Ves que todos usan IA…?" — estilo papel Fabriano + birome + avatar Flora
T='#3D2B4F';L='#8F79B3';LI='#C9B6E4'
paper=("background-color:#FAF6EE;background-image:url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='f'><feTurbulence type='fractalNoise' baseFrequency='.05' numOctaves='4' seed='3' result='n'/><feDiffuseLighting in='n' surfaceScale='1.6' lighting-color='%23fffaf0'><feDistantLight azimuth='225' elevation='55'/></feDiffuseLighting><feColorMatrix values='0 0 0 0 .42  0 0 0 0 .36  0 0 0 0 .3  -.8 0 0 0 .78'/></filter><rect width='100%25' height='100%25' filter='url(%23f)'/></svg>\");background-size:400px 400px;")
css=f"""*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;{paper}font-family:'Patrick Hand';color:{T}}}
.s{{position:relative;width:1080px;height:1350px;padding:130px 100px 60px;display:flex;flex-direction:column}}
.t{{font-size:84px;line-height:1.25}}.b{{font-size:66px;line-height:1.3}}
.mk{{padding:0 10px;background:linear-gradient(transparent 22%,{LI} 22%,{LI} 92%,transparent 92%);border-radius:14px 8px 16px 6px}}
.l{{color:{L}}}
.av{{position:absolute;bottom:0}}
.foot{{position:absolute;bottom:50px;left:100px}}.foot img{{height:54px}}
svg.d *{{fill:none;stroke:{L};stroke-width:6;stroke-linecap:round;stroke-linejoin:round}}
.row{{display:flex;align-items:center;gap:30px;font-size:64px;height:118px}}
.nn{{flex:0 0 78px;height:78px;border-radius:50%;border:5px solid {L};color:{L};display:flex;align-items:center;justify-content:center;font-size:52px}}"""
def page(body):
    return f'<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap" rel="stylesheet"><style>{css}</style></head><body><div class="s">{body}<div class="foot"><img src="flora-palabra-lila.png"></div></div></body></html>'
lista=''.join(f'<div class="row"><span class="nn">{i}</span>{t}</div>' for i,t in enumerate(['WhatsApp que responde solo','fotos que venden','descripciones con IA','que te encuentren en Google','publicar con un plan'],1))
S=[
f'''<div class="t" style="font-size:90px">¿Ves que todos usan IA para sus negocios y vos sentís que <span class="mk">te quedaste atrás</span> con tu local?</div>
<img class="av" src="avatar-frustrada.png" style="right:30px;height:640px">
<div class="b l" style="position:absolute;left:100px;bottom:170px">deslizá →</div>''',
f'''<div class="t">Ves marcas que arrancaron hace un año, sin local, y <span class="mk">venden más que vos.</span></div>
<div class="b" style="margin-top:60px;max-width:560px">Y vos pagás alquiler, sueldos, luz… <span class="l">y tenés años de trayectoria.</span></div>
<img class="av" src="avatar-pensativa.png" style="right:40px;height:640px">''',
f'''<div class="t" style="font-size:96px">No te falta tecnología.</div>
<div class="t" style="margin-top:50px;max-width:640px">Te falta <span class="mk">mostrar online lo que ya tenés:</span></div>
<div class="b l" style="margin-top:30px;max-width:560px">clientes, productos y confianza.</div>
<img class="av" src="avatar-senalando.png" style="right:10px;height:600px">''',
f'''<div class="t" style="font-size:78px">Te armé una guía con <span class="mk">5 cosas que podés cambiar hoy</span> en tu negocio</div>
<div style="margin-top:60px">{lista}</div>''',
f'''<div class="t" style="font-size:92px;margin-top:40px">Respondé <span class="mk">IA</span><br>y te la mando 💌</div>
<div class="b l" style="margin-top:40px;max-width:700px">gratis, directo a tu DM</div>
<img class="av" src="avatar-contenta.png" style="right:20px;height:700px">''',
]
for i,b in enumerate(S,1): open(f'slide-{i}.html','w').write(page(b))
