import matplotlib.pyplot as plt
import csv
from math import log

with open("results/cp_model.csv", "r") as f:
	reader = csv.DictReader(f)
	x_25, y_25 = [], []
	x_50 ,y_50 = [], []
	x_75, y_75 = [], []
	for row in reader:
		N, L, p = int(row['vars']), int(row['clauses']), float(row['probability'])
		if L/N > 11:
			continue
		match N:
			case 25:
				x_25.append(L/N)
				y_25.append(p)
			case 50:
				x_50.append(L/N)
				y_50.append(p)
			case 75:
				x_75.append(L/N)
				y_75.append(p)
				

d3, d4 = 1 - 0.5*0.5*0.5, 1 - 0.25*0.25
c3, c4 = 4.24, 9.76
c_mixed = 1/(0.5/c3 + 0.5/c4)

print(d3, d4)
print(c3, c4)
print(c_mixed)
plt.figure()
plt.plot(x_25, y_25, color = 'blue', label = "N = 25", linewidth = 0.5)
plt.plot(x_50, y_50, color = 'red', label = "N = 50", linewidth = 0.5)
plt.plot(x_75, y_75, color = 'purple', label = "N = 75", linewidth = 0.5)
plt.legend(loc = "upper left")
plt.title("Phase Transition in CPM")
plt.xlabel("L/N")
plt.ylabel("Probability")		
plt.show(block = False)


plt.figure()

alfa, v = 3.16, 2.05

t = pow(25, 1/v)
for x in range(len(x_25)):
	x_25[x] -= alfa
	x_25[x] *= t

t = pow(50, 1/v)
for x in range(len(x_50)):
	x_50[x] -= alfa
	x_50[x] *= t

t = pow(75, 1/v)
for x in range(len(x_75)):
	x_75[x] -= alfa
	x_75[x] *= t

plt.plot(x_25, y_25, color = 'blue', label = "N = 25", linewidth = 0.5)
plt.plot(x_50, y_50, color = 'red', label = "N = 50", linewidth = 0.5)
plt.plot(x_75, y_75, color = 'purple', label = "N = 75", linewidth = 0.5)
plt.legend(loc = "upper left")
plt.title("Phase Transition in CPM (rescaled)")
plt.xlabel("(L/N - " + str(alfa) + ")N^1/" + str(v))
plt.ylabel("Probability")		
plt.show()




