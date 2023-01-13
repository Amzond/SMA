import numpy as np
import math 
import matplotlib.pyplot as plt
def f(x):
    return math.log(x)/(np.sin(2*x)+1.5)


def ciobyshevo_taskai ( a, b, nP ):
  x = np.ones(nP).astype(float)
  for i in range (nP):
    x[i] = np.cos(np.pi * (2.0 * i + 1.0)/ (2.0* nP))
  return x * (b - a) / 2.0 +  (b + a) / 2.0

X = np.arange(2, 10, 1)
cc = np.arange(np.min(X)-1, np.max(X)+1, 0.1) 
f2 = np.vectorize(f)
Y = f2(X)
cio_x = ciobyshevo_taskai(2, 10, 8)
cio_y = f2(cio_x)
dd = f2(cc)


n = len(X)
n = len(cio_x)

N = np.zeros((n,n))
x = np.array(X)
y = np.array(Y)
y = np.array(cio_y)

N[:,0] = x**0
for i in range(1,n):
  N[i:, i] = N[i:, i-1] * (x[i:]-x[i-1])
    
a = np.linalg.solve(N,y)

#print(a)
xx = np.arange(np.min(X)-1, np.max(X)+1, 0.1)
#xx = np.arange(np.min(cio_x), np.max(cio_x), 0.1)
NN = np.ones((len(xx), n))
##NN[:, 1] = xx**0

for i in range(1, n):
  NN[:, i] = NN[:, i-1] * (xx[:]-x[i-1])


iks = np.linspace(2,10, 100)
igrek = f2(iks)
#print(Y)
plt.plot(iks,igrek, 'c-') # funkcijos grafikas
plt.plot(X,Y, 'ro')
#plt.plot(ccc,Y2, 'ro')
plt.plot(cc,dd, 'y-')
#plt.plot(ccc,ddd, 'g-')
yy = NN@a
plt.plot(xx, yy, 'b-')
plt.grid()
plt.show()
#print(N)
