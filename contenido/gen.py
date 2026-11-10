import json,html
L='#8F79B3';T='#3D2B4F';B='#F1E8DA';C='#FBF7F0';LI='#C9B6E4'
fonts='<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Playfair+Display:ital,wght@1,500&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">'
css=f'''*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1350px;overflow:hidden;font-family:'DM Sans';color:{T}}}
.s{{width:1080px;height:1350px;padding:110px 96px 90px;display:flex;flex-direction:column;position:relative}}
.tag{{font-size:26px;letter-spacing:7px;font-weight:700;text-transform:uppercase;color:{L}}}
h1{{font-family:Fraunces;font-weight:500;font-size:112px;line-height:1.03;margin-top:34px}}
h2{{font-family:Fraunces;font-weight:500;font-size:80px;line-height:1.08}}
i{{font-family:'Playfair Display';font-style:italic;color:{L}}}
p{{font-size:44px;line-height:1.45;margin-top:38px}}
.big{{font-family:Fraunces;font-size:170px;line-height:1;color:{L}}}
ul{{list-style:none;margin-top:40px;border-top:2px solid rgba(61,43,79,.25)}}
li{{font-size:44px;line-height:1.35;padding:26px 0;border-bottom:2px solid rgba(61,43,79,.15);display:flex;gap:26px}}
li b.n{{font-family:Fraunces;font-weight:500;color:{L};min-width:46px}}
.q{{font-family:Fraunces;font-size:62px;line-height:1.22}}
.q:before{{content:"“";display:block;font-size:180px;line-height:.6;color:{L};margin-bottom:24px}}
.who{{margin-top:40px;font-size:32px;font-weight:700;color:{L}}}
.cta{{margin-top:56px;align-self:flex-start;background:{T};color:{C};font-weight:700;font-size:38px;padding:28px 46px;border-radius:60px}}
.foot{{margin-top:auto;display:flex;justify-content:space-between;align-items:center;font-size:26px;font-weight:500;opacity:.85}}
.foot img{{height:54px}}
.swipe{{font-size:30px;font-weight:700;letter-spacing:2px}}
.dark{{background:{T};color:{C}}} .dark i,.dark .big,.dark .tag,.dark li b.n,.dark .who{{color:{LI}}} .dark .cta{{background:{LI};color:{T}}}
.dark ul,.dark li{{border-color:rgba(251,247,240,.2)}}

.lilabg i{{color:#5E4A7C!important}}
.body{{flex:1;display:flex;flex-direction:column;justify-content:center;padding-bottom:40px}}
.foot{{margin-top:0}}'''
BG={'lila':LI,'beige':B,'crema':C,'dark':T}
def slide(kind,bg,body,n,N,logo=True):
    cls='s dark' if bg=='dark' else ('s lilabg' if bg=='lila' else 's')
    lg='flora-palabra-ciruela.png' if bg=='lila' else 'flora-palabra-lila.png'
    right='<span class="swipe">DESLIZÁ →</span>' if n==1 else f'<span>{n}/{N}</span>'
    return f'<!doctype html><html><head><meta charset="utf-8">{fonts}<style>{css}</style></head><body><div class="{cls}" style="background:{BG[bg]}"><div class="body">{body}</div><div class="foot"><img src="{lg}"><span>@floramarketing.ar</span>{right}</div></div></body></html>'
