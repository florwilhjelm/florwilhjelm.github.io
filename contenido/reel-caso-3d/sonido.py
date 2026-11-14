import numpy as np, wave, sys
sr=44100;dur=17.0;n=int(sr*dur);rng=np.random.default_rng(7);out=np.zeros(n)
def bandnoise(m,lo,hi):
    x=rng.standard_normal(m);X=np.fft.rfft(x);f=np.fft.rfftfreq(m,1/sr);X[(f<lo)|(f>hi)]=0;y=np.fft.irfft(X,m);return y/ (np.abs(y).max()+1e-9)
W=[(4.15,5.6),(8.3,8.75),(8.8,9.35),(9.4,9.95),(10.0,10.65),(10.7,11.35),(11.4,11.95)]
for s,e in W:
    i0,i1=int(s*sr),int(e*sr);m=i1-i0;y=bandnoise(m,1800,7000)
    # trazos: envolvente con granos de 40-120ms
    env=np.zeros(m);t=0
    while t<m:
        L=int(rng.uniform(0.04,0.12)*sr);g=min(L,m-t);w=np.hanning(g)*rng.uniform(.5,1);env[t:t+g]+=w;t+=int(L*rng.uniform(.7,1.1))
    fade=np.minimum(1,np.minimum(np.arange(m),m-np.arange(m))/(0.03*sr))
    out[i0:i1]+=y*env*fade*0.16
T=[(7.6,8.3)]
for s,e in T:
    i0,i1=int(s*sr),int(e*sr);m=i1-i0;y=bandnoise(m,300,3500);env=np.sin(np.linspace(0,np.pi,m))**2
    out[i0:i1]+=y*env*0.22
out=np.clip(out,-1,1);fo=int(0.6*sr);out[-fo:]*=np.linspace(1,0,fo)
pcm=(out*32767).astype('<i2')
with wave.open(sys.argv[1],'wb') as w: w.setnchannels(1);w.setsampwidth(2);w.setframerate(sr);w.writeframes(pcm.tobytes())
