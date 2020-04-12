import matplotlib.pyplot as plt

file = open("Calculus\Calculus\Results.txt")

first_line = file.readline()
first_line = first_line.split()

a = int(first_line[0])
b = int(first_line[1])
N_x = int(first_line[2])
N_y = int(first_line[3])

function_values = []

line = file.readline()
while line != '':
	function_values.append([float(value) for value in line.split()])
	line = file.readline()
file.close()



fig1 = plt.figure()
ax = fig1.add_subplot(111)

h_x = a / N_x
h_y = b / N_y

x = [i * h_x 	for i in range(0, N_x + 1)]
y = [i * h_y 	for i in range(0, N_y + 1)]

for i in range(0, N_y + 1):
	plt.plot(x, function_values[i],label = "y = " + str((b - y[i])))
	
plt.legend()
ax.set_xlabel("X")
ax.set_ylabel("function U(x,y)")

plt.show()