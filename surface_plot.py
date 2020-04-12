from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


file = open("Calculus\Calculus\Results.txt")

first_line = file.readline()
first_line = first_line.split()

a = int(first_line[0])
b = int(first_line[1])
N_x = int(first_line[2])
N_y = int(first_line[3])

function_values = []

line = file.readline()
k = 0.001
while line != '':
	function_values.append([k * float(value) for value in line.split()])
	line = file.readline()
file.close()



fig1 = plt.figure()
ax = fig1.add_subplot(111, projection='3d')


h_x = a / N_x
h_y = b / N_y

x = [i * h_x 	for i in range(0, N_x + 1)]
y = [i * h_y 	for i in range(0, N_y + 1)]

X, Y = np.meshgrid(x, y)

Z = np.array(function_values)

ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

plt.legend()
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("function")

plt.show()