import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.log(x) / (np.sin(x*2) + 1.5)

#coeficientus suskaiciuoja 
def coefs(range_x, range_y):
    a = [range_y]
    for i in range(len(range_x)):
        a.append([])
        for j in range(1, len(range_x) - i):
            a[i + 1].append((a[i][j] - a[i][j - 1]) / (range_x[np.min([i + j, len(range_x) - 1])] - range_x[np.max([i + j - (i + 1), 0])]))

    return [a[0] for a in a[:-1]]

# interpoliuoja nuo taško iki taško
# kas taska keicia koef
def newton_interpolation_f(range_x, range_y):
    a_coefficients = coefs(range_x, range_y)
    
    def interpolation_f(x):
        ff = a_coefficients[0]
        tmp = 1
        for ii in range(1, len(a_coefficients)):
            tmp *= (x - range_x[ii - 1])
            ff += a_coefficients[ii] * tmp
            
        return ff
    return interpolation_f   

#ciobyshevo taskus apskciuoja
def chebyshev_range(count, start, end):
    range_x = []
    for i in range(count):
        temp = (end + start) / 2 + (end - start) / 2 * np.cos((2 * i + 1) * np.pi / (2 * count))
        range_x.append(temp)

    return range_x


a = 2
b = 10
pts = 15
step_size = (b - a) / pts
#print(step_size)
x_range = np.arange(a, b, step_size)
x_range = np.append(x_range, b)
#x_range = chebyshev_range(pts, a, b)
y_range = [f(x) for x in x_range]

interpol_f = newton_interpolation_f(x_range, y_range)

plt.axhline(0)
plt.plot(np.linspace(a, b, 100), [f(x) for x in np.linspace(a, b, 100)],'b', label='funkcija')
plt.plot(np.linspace(a, b, 100), [interpol_f(x) for x in np.linspace(a, b, 100)], 'r-', label='Interpoliuota')
plt.plot(np.linspace(a, b, 100), [(f(x) - interpol_f(x)) for x in np.linspace(a, b, 100)], 'g-', label='Netektis')


plt.scatter(x_range, y_range, color='black')
plt.legend()
plt.ylim(top=6, bottom=-3.5)
plt.grid(True)
plt.show()
