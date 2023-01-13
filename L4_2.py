import numpy as np
import matplotlib.pyplot as plt

def funk(X,t):
  h=X[0];v=X[1];k1=0.25;k2=10;m=130;t1=25;g=9.81
  #pagal laika paziuri ar krenta su ar be parasiuto
  if t < t1:
    k=k1
  else:
    k=k2
  
  fff=np.array([2,1],dtype=float)
  if h>0:
    fff[0]=v;#dh/dt=v
    fff[1]=-g-k*v**2/m*np.sign(v)#m*(dv/dt)=-mg-(k*v^2/m)*sign(v)
  else:
    fff[0]=0
    fff[1]=0
  
  return fff

h0=2800; T=150; v0=0

t=np.linspace(0,T,175)#intervalas
dt=t[1]-t[0]
print(dt)
N=len(t)
rez=np.zeros([2,N],dtype=float)#aukstis 2(h ir v), o ilgis pagal linspace
rez[0,0]=h0
rez[1,0]=v0
#naudojam IV eilės Rungės ir Kutos metodas
for i in range(N-1):
  fz=rez[:,i]+dt/2*funk(rez[:,i],t[i]) # eulerio per puse zingsnio
  fzz=rez[:,i]+dt/2*funk(fz,t[i]+dt/2) # atgal eulerio per puse zingscio
  fzzz=rez[:,i]+dt*funk(fzz,t[i]+dt/2) #vidurinio tasko per 1 zingsni
  
  rez[:,i+1]=rez[:,i]+dt/6*(funk(rez[:,i],t[i])+2*(funk(fz,t[i]+dt/2))
                            +2*(funk(fzz,t[i]+dt/2))+(funk(fzzz,t[i]+dt)))

fig1=plt.figure(1)
ax1=fig1.add_subplot(1,1,1)
ax1.set_xlabel('t')
ax1.set_ylabel('h');ax1.grid()
ax1.set_title("aukstis")
ax1.plot(t,rez[0,:],'b-')
plt.show()
fig2=plt.figure(1)
ax2=fig2.add_subplot(1,1,1)
ax2.set_xlabel('t')
ax2.set_ylabel('v');ax2.grid()
ax2.set_title("greitis")
ax2.plot(t,rez[1,:],'r-')
plt.show()