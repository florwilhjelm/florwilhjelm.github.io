T='#3D2B4F';L='#8F79B3';LI='#C9B6E4'
paper=("background-color:#FAF6EE;background-image:url(\"data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'><filter id='f'><feTurbulence type='fractalNoise' baseFrequency='.05' numOctaves='4' seed='3' result='n'/><feDiffuseLighting in='n' surfaceScale='1.6' lighting-color='%23fffaf0'><feDistantLight azimuth='225' elevation='55'/></feDiffuseLighting><feColorMatrix values='0 0 0 0 .42  0 0 0 0 .36  0 0 0 0 .3  -.8 0 0 0 .78'/></filter><rect width='100%25' height='100%25' filter='url(%23f)'/></svg>\");background-size:400px 400px;")
css=f"""*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;{paper}font-family:'Patrick Hand';color:{T}}}
.s{{width:1080px;height:1350px;padding:130px 100px 60px;display:flex;flex-direction:column}}
.t{{font-size:84px;line-height:1.25}}.b{{font-size:68px;line-height:1.3}}
.mk{{padding:0 10px;background:linear-gradient(transparent 22%,{LI} 22%,{LI} 92%,transparent 92%);border-radius:14px 8px 16px 6px}}
.l{{color:{L}}}
.foot{{margin-top:auto;display:flex;justify-content:center}}.foot img{{height:54px}}
svg.d{{display:block}} svg.d *{{fill:none;stroke:{L};stroke-width:6;stroke-linecap:round;stroke-linejoin:round}}"""
def page(body,n): 
    return f'<!doctype html><html><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Patrick+Hand&display=swap" rel="stylesheet"><style>{css}</style></head><body><div class="s">{body}<div class="foot"><img src="flora-palabra-lila.png"></div></div></body></html>'
S=[
f'''<div class="t" style="font-size:96px;margin-top:40px">Tu negocio físico está perdiendo clientes <span class="mk">sin darte cuenta</span></div>
<svg class="d" width="880" height="420" viewBox="0 0 880 420" style="margin-top:70px"><path d="M120 300 C 260 300, 320 150, 470 120"/><path d="M440 92 L472 120 L436 146"/>
<text x="40" y="380" style="font-family:Patrick Hand;font-size:72px;fill:#3D2B4F;stroke:none">tu local</text><text x="470" y="70" style="font-family:Patrick Hand;font-size:72px;fill:#3D2B4F;stroke:none">la competencia</text></svg>
<div class="b l" style="text-align:right;margin-top:10px">deslizá →</div>''',
f'''<div class="t">El cliente de hoy busca primero en <span class="mk">Google o Instagram.</span></div>
<div class="b" style="margin-top:70px">Si no te encuentra, va al que sí está presente.</div>
<svg class="d" width="520" height="300" viewBox="0 0 520 300" style="margin:70px auto 0"><circle cx="190" cy="140" r="100"/><path d="M262 212 L360 300"/></svg>''',
f'''<div class="t">No alcanza con tener un perfil actualizado o una dirección con fotos en <span class="mk">Google Maps.</span></div>
<svg class="d" width="300" height="380" viewBox="0 0 300 380" style="margin:90px auto 0"><path d="M150 360 C 60 240, 30 190, 30 140 A 120 120 0 0 1 270 140 C 270 190, 240 240, 150 360 Z"/><circle cx="150" cy="140" r="45"/></svg>''',
f'''<div class="t">Los negocios que más crecen <span class="l">no son los más grandes.</span></div>
<div class="t" style="margin-top:50px">Son los que tienen un <span class="mk">sistema digital que trabaja solo.</span></div>
<svg class="d" width="560" height="260" viewBox="0 0 560 260" style="margin:60px auto 0"><path d="M40 220 L160 150 L260 180 L400 70 L520 30"/><path d="M480 24 L522 28 L510 70"/></svg>''',
f'''<div class="t">No hace falta hacer todo de una vez.</div>
<div class="t" style="margin-top:50px">Hace falta <span class="mk">empezar por lo correcto.</span></div>
<svg class="d" width="620" height="330" viewBox="0 0 620 330" style="margin:60px auto 0"><path d="M30 300 h150 v-90 h150 v-90 h150 v-90 h110"/><path d="M560 6 L600 30 L560 56" /></svg>''',
f'''<div class="t" style="font-size:84px">¿Querés saber qué cambios implementar <span class="mk">hoy mismo</span> para que tu negocio físico crezca online?</div>
<div class="t l" style="font-size:104px;margin-top:70px">Hablame 💬</div>''',
]
for i,b in enumerate(S,1): open(f'slide-{i}.html','w').write(page(b,i))
