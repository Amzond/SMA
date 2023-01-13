#eulerio
import numpy as np
import matplotlib.pyplot as plt

def funk(X,t):
 # h=X[0]
  v=X
  
  g=9.81
  m1, m2 = 0.15, 0.2
  mass = m1 + m2
  ks, k1, k2 = 0.01, 0.05, 0.001
  ts, t_max = 2, 10
  
  #pagal laika paziuri ar krenta su ar be parasiuto
  k = ks
  if t > ts:
    mass = m1
    k=k1
  else:
    mass = m2
    k=k2
  
  
  fff=np.array([2,1],dtype=float)
  fff[0]=v;#dh/dt=v
  #fff[1]=-g-k*v**2/m*np.sign(v)#m*(dv/dt)=-mg-(k*v^2/m)*sign(v)
  fff[1] = -mass * g - k * v * np.abs(v) / mass
  
  return  -mass * g - k * v * np.abs(v) / mass


h0=0; T=10; v0=70

t=np.linspace(0,T,2000)#intervalas

t = np.linspace(0,1,2)


dt=t[1]-t[0]# atstumas nuo tasko iki tasko

N=len(t)

rez=np.zeros([2,N],dtype=float)
rez[0,0]=h0
rez[1,0]=v0
v = 0
#naudojam eulerio formule
for i in range(N-1):
  v += v + dt*funk(v, h0) 
 # rez[:,i+1]=rez[:,i]+dt*funk(rez[:,i],t[i])



fig1=plt.figure(1)
ax1=fig1.add_subplot(1,1,1)
ax1.set_xlabel('t')
ax1.set_ylabel('h')
ax1.grid()
ax1.set_title("aukštis")
ax1.plot(t,rez[0,:],'b-')
#ax1.plot(tt,rezz[0,:],'g-')
plt.show()
fig2=plt.figure(1)
ax2=fig2.add_subplot(1,1,1)
ax2.set_xlabel('t')
ax2.set_ylabel('v');ax2.grid()
ax2.set_title("greitis")
ax2.plot(t,rez[1,:],'r-')

#ax2.plot(tt,rezz[1,:],'g-')
plt.show()