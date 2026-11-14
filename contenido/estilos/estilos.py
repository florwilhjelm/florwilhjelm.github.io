fonts='<link href="https://fonts.googleapis.com/css2?family=Patrick+Hand&family=Caveat:wght@500;600;700&display=swap" rel="stylesheet">'
T='#3D2B4F';L='#8F79B3';LI='#C9B6E4';SOFT='#E9DFF5';C='#FBF7F0'
def rough_underline(w,color=L):
    return f'<svg width="{w}" height="26" viewBox="0 0 {w} 26" style="display:block;margin:-6px auto 0"><path d="M6 10 C {w*.3} 4, {w*.6} 14, {w-6} 8" stroke="{color}" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M20 20 C {w*.35} 14, {w*.65} 22, {w-20} 17" stroke="{color}" stroke-width="3.5" fill="none" stroke-linecap="round"/></svg>'
spark_l=f'<svg width="70" height="110" viewBox="0 0 70 110"><g stroke="{L}" stroke-width="5" stroke-linecap="round"><path d="M10 15 L50 38"/><path d="M8 55 L55 55"/><path d="M10 95 L50 72"/></g></svg>'
spark_r=spark_l.replace('<svg','<svg style="transform:scaleX(-1)"')
A_css=f'''*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;background:{C};font-family:'Patrick Hand';color:{T}}}
.s{{width:1080px;height:1350px;padding:90px 70px 60px;display:flex;flex-direction:column;align-items:center;text-align:center}}
.t1{{font-size:64px;line-height:1.1}}.box{{border:5px solid {L};border-radius:8px;padding:18px 36px;font-size:78px;line-height:1.08;color:{L};margin:24px 0}}
.row{{display:flex;align-items:center;gap:10px}}.t2{{font-size:56px;line-height:1.25}}.hl{{color:{L}}}
.av{{margin-top:auto;width:520px;height:520px;border-radius:50% 50% 0 0;border:4px dashed {LI};display:grid;place-items:center;color:{L};font-size:34px}}
.pill{{background:{SOFT};border-radius:34px;padding:28px 40px;font-size:52px;line-height:1.25}}
.foot{{margin-top:22px;font-size:28px;color:{L};display:flex;gap:14px;align-items:center}}.foot img{{height:40px}}'''
A1=f'''<div class="s"><div class="t1">Si hoy tuviera un local con 20 años en el rubro,</div>
<div class="row">{spark_l}<div class="box">ASÍ LO HARÍA VENDER<br>EN TODO EL PAÍS</div>{spark_r}</div>
<div class="t2">empezando <span class="hl">mañana mismo.</span>{rough_underline(300)}</div>
<div class="av">acá va tu avatar<br>(ilustrado, parecido a vos)</div>
<div class="foot"><img src="flora-palabra-lila.png"> @floramarketing.ar</div></div>'''
A2=f'''<div class="s" style="text-align:left;align-items:stretch">
<div style="text-align:center"><div class="row" style="justify-content:center">{spark_l}<div class="pill" style="font-size:72px;padding:12px 40px;color:{L}">Primero,</div>{spark_r}</div>
<div style="font-size:72px;margin-top:6px"><span class="hl">NO</span> haría descuentos.{rough_underline(260)}</div></div>
<div style="display:flex;gap:30px;margin-top:40px;align-items:flex-start">
<div style="flex:1.1;display:flex;flex-direction:column;align-items:center;gap:14px">
<div class="pill" style="text-align:center">Bajás precios para vender más.</div>
<svg width="40" height="70"><path d="M20 5 L20 60 M6 46 L20 62 L34 46" stroke="{L}" stroke-width="5" fill="none" stroke-linecap="round"/></svg>
<div class="pill" style="text-align:center">Vendés más… pero <span class="hl">ganás menos.</span></div></div>
<div style="flex:1;height:420px;border:4px dashed {LI};border-radius:30px;display:grid;place-items:center;color:{L};font-size:32px;text-align:center">avatar<br>(pensativa)</div></div>
<div class="pill" style="text-align:center;margin-top:40px;font-size:56px">Primero, tus números.<br><span class="hl" style="font-size:66px">Después, la publicidad.</span>{rough_underline(420)}</div>
<div class="foot" style="justify-content:center;margin-top:auto"><img src="flora-palabra-lila.png"> @floramarketing.ar</div></div>'''
B_css=f'''*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;background:url(papel.png);font-family:'Caveat';color:{T}}}
.s{{width:1080px;height:1350px;padding:120px 90px 70px;display:flex;flex-direction:column}}
.t{{font-size:84px;line-height:1.28;font-weight:500}}.mk{{background:linear-gradient(transparent 15%,{LI} 15%,{LI} 85%,transparent 85%);padding:0 10px;border-radius:6px}}
.foot{{margin-top:auto;display:flex;justify-content:space-between;align-items:center;font-size:36px;color:{L}}}.foot img{{height:46px}}'''
B1=f'''<div class="s"><div class="t">¿Hace 20 años que vendés<br>en tu ciudad?<br>Así podés vender<br>en todo el país<br><span class="mk">sin abrir otra sucursal</span></div>
<svg width="900" height="380" style="margin-top:40px"><text x="40" y="300" font-family="Caveat" font-size="96" font-weight="600" fill="{T}">tu local</text>
<path d="M330 270 C 400 230, 430 180, 470 120" stroke="{T}" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M440 116 L472 118 L466 150" stroke="{T}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<text x="470" y="80" font-family="Caveat" font-size="88" font-weight="600" fill="{L}">todo el país</text></svg>
<div class="foot"><img src="flora-palabra-lila.png"><span>deslizá →</span></div></div>'''
B2=f'''<div class="s"><div class="t" style="font-size:78px">Antes de invertir en publicidad<br>mirá estas dos cosas</div>
<svg width="900" height="720" viewBox="0 0 900 720" style="margin-top:30px"><g fill="none" stroke="{T}" stroke-width="5"><path d="M330 160 C 180 150, 110 280, 140 400 C 170 520, 330 560, 420 470 C 500 390, 480 170, 330 160 Z"/><path d="M520 158 C 370 150, 300 290, 330 400 C 360 520, 550 560, 640 470 C 730 380, 680 165, 520 158 Z"/></g>
<text x="390" y="345" text-anchor="middle" font-family="Caveat" font-size="40" fill="{L}" font-weight="700">tu ganancia</text>
<text x="220" y="620" text-anchor="middle" font-family="Caveat" font-size="54" fill="{T}">tu margen</text><text x="600" y="620" text-anchor="middle" font-family="Caveat" font-size="54" fill="{T}">tu costo por venta</text></svg>
<div class="foot"><img src="flora-palabra-lila.png"><span>@floramarketing.ar</span></div></div>'''
for n,css,b in [('estilo-ilustrado-1',A_css,A1),('estilo-ilustrado-2',A_css,A2),('estilo-cuaderno-1',B_css,B1),('estilo-cuaderno-2',B_css,B2)]:
    open(n+'.html','w').write(f'<!doctype html><html><head><meta charset="utf-8">{fonts}<style>{css}</style></head><body>{b}</body></html>')
