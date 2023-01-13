# -*- coding: utf-8 -*-
#Program 0.4 Newton Interpolation
 
import numpy as np
import math
import matplotlib.pyplot as plt
 
#Recursive quotient
def get_diff_quo(xi, fi):
    if len(xi) > 2 and len(fi) > 2:
        return (get_diff_quo(xi[:len(xi)-1], fi[:len(fi)-1]) - get_diff_quo(xi[1:len(xi)], fi[1:len(fi)])) / float(xi[0] - xi[-1])
    return (fi[0]-fi[1]) / float(xi[0]-xi[1])

# w, use closure function
def get_w(i, xi):
    def wi(x):  
        result = 1.0
        for j in range(i):
            result *= (x - xi[j])
        return result
    return wi
 
 #Do interpolation
def get_Newton(xi, fi):
    def Newton(x):
        result = fi[0]
        for i in range(2, len(xi)):
            result += (get_diff_quo(xi[:i], fi[:i]) * get_w(i-1, xi)(x))
        return result
    return Newton
 
#Known node
#xn = [i for i in range(2, 10, 1)]
xn = np.arange(2-1, 10+1, 0.5)

fn = [math.log(i)/(np.sin(2*i)+1.5) for i in xn]
plt.plot(xn, fn)
#Interpolation function
Nx = get_Newton(xn, fn)
 
#Test Case
tmp_x = [i for i in range(2, 10)]
tmp_y = [Nx(i) for i in tmp_x]

plt.plot(xn, fn, 'r*')
plt.plot(xn, fn, 'y--')
plt.plot(tmp_x, tmp_y, 'b-')
plt.title('Newton Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.show()