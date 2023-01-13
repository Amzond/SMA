from matplotlib import pyplot as plt
import numpy as np


# nuo tasko iki tasko kelias
def distance(x):
    n = len(x)
    d = np.zeros(n-1)

    for i in range(n - 1):
        d[i] = x[i+1] - x[i]
    return d

# Lygciu sistemos matrica ir ja isprendzia
# istrizaine matrica
def values(x,y):
    n = len(x)
    A = np.zeros((n,n))
    b = np.zeros(n)
    d = distance(x)

    for i in range(n - 2):
        A[i,i] = d[i] / 6
        A[i,i+1] = (d[i] + d[i+1]) / 3
        A[i,i+2] = d[i+1] / 6

    for i in range(n - 2):
        b[i] = ((y[i + 2] - y[i + 1]) / d[i + 1]) - ((y[i + 1] - y[i]) / d[i])
    
    A[n - 2, 0] = d[0] / 3
    A[n - 2, 1] = d[0] / 6
    A[n - 1, 0] = 1

    A[n - 2, n - 2] = d[n - 2] / 6
    A[n - 2, n - 1] = d[n - 2] / 3
    A[n - 1, n - 1] = -1
    
    b[n - 2] = ((y[1] - y[0]) / d[0]) - ((y[n - 1] - y[n - 2]) / d[n - 2])
    
    ff = np.linalg.solve(A, b)
    return ff


#  splaino lygits
def splinify(ff1, ff2, s, d, y1, y2):
    a = (ff1 * (s**2 / 2)) - (ff1 * (s**3 / (6*d)))
    b = (ff2 * (s**3 / (6*d))) + (((y2 - y1) / d) * s)
    c = (ff1 * ((d/3) * s)) + (ff2 * ((d/6) * s))

    return a + b - c + y1 


x = [1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]

y = np.array([73.140, 73.870, 71.050, 73.240, 71.420, 74.340, 73.210, 72.300, 71.520, 69.350,
67.960, 62.110, 62.090, 61.350, 57.470, 55.130, 55.400, 58.330, 58.960, 60.880, 60.920 ])

n = 21
aa = 1
x = np.arange(aa,aa+n)

ff = values(x, y)
ff[0] = 0
ff[n-1] = 0
d = distance(x) # visa laik vienas nes metai
its = 100
xx = []
yy = []

x1 = 1

for i in range(1, n):
    x2 = x1
    for j in range(its):
        s = x2 - i
        xx.append(x2)
        value = splinify(ff[i - 1], ff[i], s, d[i - 1], y[i - 1], y[i])
        yy.append(value)
        x2 += 1 / its
    x1 += 1


plt.plot(xx, yy)
plt.scatter(x, y)
plt.plot(x,y, 'y-')
plt.xticks(x, range(1998, 2019))
plt.grid()
plt.show()