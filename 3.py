import matplotlib.pyplot as plt
import numpy as np

# pasidaro matrica
# pakelia laipsniu x
def Base(x, m):
    matrix = np.zeros((len(x), m))
    for j in range(m):
        matrix[:, j] = x[:] ** j
    return matrix

Y = np.array([ 73.140, 73.870, 71.050, 73.240, 71.420, 74.340, 73.210, 72.300, 71.520, 69.350,
67.960, 62.110, 62.090, 61.350, 57.470, 55.130, 55.400, 58.330, 58.960, 60.880, 60.920 ])
X = np.arange(1, len(Y) + 1, 1)

m = 4
plt.plot(X, Y, "ro")
matrix1 = Base(X, m)



# apversta matrica sudaugina su paprasta matrica,     apversta x matrica sudaugina su Y array
# ir randa   sprendinius
coefs = np.linalg.solve(np.dot(matrix1.T, matrix1), np.dot(matrix1.T, Y))

xxx = np.linspace(min(X), max(X), 200)
matrix2 = Base(xxx, m)
yyy = np.dot(matrix2, coefs)

plt.plot(xxx, yyy, "b-")
plt.grid()

plt.xticks(np.arange(1, len(Y) + 1, 1), np.arange(1998, 2019, 1))
plt.show()
