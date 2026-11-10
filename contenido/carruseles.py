from gen import slide
import os
def lst(items): return '<ul>'+''.join(f'<li><b class="n">{i+1}</b><span>{t}</span></li>' for i,t in enumerate(items))+'</ul>'
def cover(tag,title,sub=''): return f'<span class="tag">{tag}</span><h1>{title}</h1>'+(f'<p>{sub}</p>' if sub else '')
CAR={
'01-sucursal':[
 ('lila',cover('Negocios con trayectoria','Tu próxima sucursal <i>no necesita alquiler.</i>')),
 ('crema','<h2>Abrir otra sucursal es:</h2>'+lst(['Alquiler y garantía','Sueldos y cargas sociales','Más stock inmovilizado','Meses hasta recuperar lo invertido'])),
 ('dark','<div class="big">24 h</div><h2 style="margin-top:30px">Una tienda online bien hecha vende todos los días, <i>a todo el país.</i></h2>'),
 ('crema','<h2>Lo que necesita para funcionar</h2>'+lst(['Una tienda clara y fácil de comprar','Publicidad que la haga conocer','Contenido real de tu local'])),
 ('beige','<h2>Lo más difícil <i>ya lo tenés.</i></h2><p>Trayectoria, proveedores y clientes que confían en vos. Eso no se compra con publicidad.</p>'),
 ('lila','<h2>Guardalo y pensalo: <i style="color:#3D2B4F">¿cuántas sucursales estás dejando de abrir?</i></h2><span class="cta">Escribime SUCURSAL</span>'),
],
'02-numero-publicidad':[
 ('beige',cover('Antes de invertir','El número que tenés que saber <i>antes de invertir en publicidad.</i>')),
 ('crema','<h2>Vender mucho <i>no siempre es ganar.</i></h2><p>Hay negocios que venden más con anuncios… y pierden plata en cada venta.</p>'),
 ('crema','<span class="tag">Paso 1</span><h2 style="margin-top:24px">Conocé tu margen</h2><p>Es lo que te queda de cada venta después de pagar la mercadería, las comisiones y los impuestos.</p>'),
 ('dark','<span class="tag">Paso 2</span><div class="big" style="margin-top:30px">1 ÷ margen</div><h2 style="margin-top:30px">= tu ROAS mínimo</h2><p>Cuánto tenés que vender por cada $1 que invertís para no perder plata.</p>'),
 ('crema','<span class="tag">Ejemplo</span><h2 style="margin-top:24px">Margen del 40%</h2><p>1 ÷ 0,40 = <b>2,5</b></p><p>Si invertís <b>$100.000</b> en anuncios, tenés que vender al menos <b>$250.000</b> para no perder.</p>'),
 ('beige','<h2>Por debajo de ese número, la publicidad <i>te cuesta plata.</i></h2><p>Por arriba, te deja ganancia. Así de simple.</p>'),
 ('lila','<h2>Tengo una planilla que <i style="color:#3D2B4F">lo calcula sola.</i></h2><span class="cta">Comentá PLANILLA</span>'),
],
'03-black-friday':[
 ('dark',cover('Black Friday','Antes de poner 30% OFF, <i>hacé esta cuenta.</i>')),
 ('crema','<h2>Un descuento no sale de tu ganancia total. <i>Sale de tu margen.</i></h2>'),
 ('crema','<span class="tag">Un producto de $10.000</span>'+lst(['Mercadería: $5.000','Comisiones e impuestos: $1.000','Te quedan: <b>$4.000</b>'])),
 ('dark','<div class="big">30% OFF</div><h2 style="margin-top:30px">Lo vendés a $7.000 y te quedan unos $1.300.</h2><p>Para ganar lo mismo que antes, tenés que vender <b>3 veces más.</b></p>'),
 ('crema','<h2>Opciones que cuidan tu margen</h2>'+lst(['Envío gratis desde un monto','Combos con los productos de más margen','Regalo con la compra','Acceso anticipado para tus clientes'])),
 ('beige','<h2>Regla simple: <i>nunca descuentes más de lo que tu margen aguanta.</i></h2>'),
 ('lila','<h2>¿Hacemos la cuenta <i style="color:#3D2B4F">con tu negocio?</i></h2><span class="cta">Escribime BLACK</span>'),
],
'04-instagram-vidriera':[
 ('lila',cover('Para dueños de locales','3 señales de que tu Instagram <i style="color:#3D2B4F">es solo una vidriera.</i>')),
 ('crema','<div class="big">1</div><h2 style="margin-top:30px">Mostrás productos, pero nadie sabe cómo comprarlos.</h2><p>Sin link, sin precios, sin envíos claros.</p>'),
 ('crema','<div class="big">2</div><h2 style="margin-top:30px">Solo te ven los que ya te siguen.</h2><p>Sin publicidad, tus posteos llegan a la misma gente de siempre.</p>'),
 ('crema','<div class="big">3</div><h2 style="margin-top:30px">No sabés cuánto te vende.</h2><p>Si no se mide, no se puede mejorar.</p>'),
 ('dark','<h2>Si te identificaste con 2 o más, <i>tu Instagram puede vender mucho más.</i></h2><span class="cta">Respondé VIDRIERA</span>'),
],
'05-testimonios':[
 ('beige',cover('Resultados reales','No invirtió más. <i>Invirtió mejor.</i>')),
 ('crema','<div class="q">Cuadruplicamos las ventas en un mes, invirtiendo lo mismo que el mes anterior.</div><div class="who">Cliente ecommerce</div>'),
 ('crema','<div class="q">Desde el lunes a hoy ingresaron 11 ventas. ¡Sos una capa!</div><div class="who">Cliente de moda</div>'),
 ('crema','<div class="q">Hace meses que no me caía una venta de estos productos… ¡Arrancamos bien! 🤍</div><div class="who">Javo</div>'),
 ('dark','<h2>¿Qué cambió?</h2><p>Primero miramos los números. Después, anuncios pensados para su negocio, <b>no una plantilla.</b></p>'),
 ('lila','<h2>¿Querés que tu negocio <i style="color:#3D2B4F">sea el próximo?</i></h2><span class="cta">Escribime DIAGNÓSTICO</span>'),
],
'06-metodo-flora':[
 ('dark',cover('Método Flora','Del local a todo el país, <i>en 90 días.</i>')),
 ('crema','<h2>Para negocios con años en su rubro <i>que quieren vender también online.</i></h2>'),
 ('crema','<span class="tag">Mes 1</span><h2 style="margin-top:24px">Ordenar</h2><p>Números, oferta y tienda lista para vender a todo el país.</p>'),
 ('crema','<span class="tag">Mes 2</span><h2 style="margin-top:24px">Lanzar</h2><p>Publicidad con contenido real de tu local.</p>'),
 ('crema','<span class="tag">Mes 3</span><h2 style="margin-top:24px">Crecer</h2><p>Más de lo que funciona, menos de lo que no.</p>'),
 ('beige','<div class="big">x4</div><h2 style="margin-top:30px">Un local de deportes pasó de 3.000 a 13.000 USD en un mes.</h2>'),
 ('lila','<h2>Abro 5 lugares <i style="color:#3D2B4F">para empezar en enero.</i></h2><span class="cta">Escribime DIAGNÓSTICO</span>'),
],
}
os.makedirs('html',exist_ok=True)
for name,slides in CAR.items():
    N=len(slides)
    for i,(bg,body) in enumerate(slides):
        open(f'html/{name}-{i+1}.html','w').write(slide('',bg,body,i+1,N))
print(sum(len(v) for v in CAR.values()))
