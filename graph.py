import matplotlib.pyplot as plt
import csv
from math import log

path = "./results/proba.csv"

with open(path, "r") as f:
	reader = csv.DictReader(f)
	x_25, y_25, z_25 = [], [], []
	x_50 ,y_50, z_50 = [], [], []
	x_75, y_75, z_75 = [], [], []
	x_100, y_100, z_100 = [], [], []
	for row in reader:
		N, L, p, branches = int(row['vars']), int(row[' clauses']), float(row['sat']), float(row['decisions'])
		if L/N > 11:
			continue
		match N:
			case 25:
				x_25.append(L/N)
				y_25.append(p)
				z_25.append(branches)
			case 50:
				x_50.append(L/N)
				y_50.append(p)
				z_50.append(branches)
			case 75:
				x_75.append(L/N)
				y_75.append(p)
				z_75.append(branches)
			case 100:
				x_100.append(L/N)
				y_100.append(p)
				z_100.append(branches)
fig, ax1 = plt.subplots()
ax1.set_xlabel('L/N')
ax1.set_ylabel('Probability')
ax1.plot(x_25, y_25, color = 'blue', label = "N = 25", linewidth = 1)
ax1.plot(x_50, y_50, color = 'red', label = "N = 50", linewidth = 1)
ax1.plot(x_75, y_75, color = 'purple', label = "N = 75", linewidth = 1)
# ax1.plot(x_100, y_100, color = 'pink', label = "N = 100", linewidth = 1)

ax2 = ax1.twinx()
ax2.set_ylabel('Average number of decisions')
ax2.plot(x_25, z_25, color = "brown", label = "N = 25, branches", linewidth = 1, linestyle = 'dashed')
ax2.plot(x_50, z_50, color = "grey", label = "N = 50, branches", linewidth = 1, linestyle = 'dashed')
ax2.plot(x_75, z_75, color = "green", label = "N = 75, branches", linewidth = 1, linestyle = 'dashed')
# ax2.plot(x_100, z_100, color = "indigo", label = "N = 100, branches", linewidth = 1, linestyle = 'dashed')
ax1.legend(loc = "upper left")
ax2.legend(loc = "upper right")
plt.title("Phase Transition in Mixed 3-4 SAT model")		
plt.show(block = False)


plt.figure()

alfa, v = 5.91, 1.35

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

t = pow(100, 1/v)
for x in range(len(x_100)):
	x_100[x] -= alfa
	x_100[x] *= t


plt.plot(x_25, y_25, color = 'blue', label = "N = 25", linewidth = 1)
plt.plot(x_50, y_50, color = 'red', label = "N = 50", linewidth = 1)
plt.plot(x_75, y_75, color = 'purple', label = "N = 75", linewidth = 1)
# plt.plot(x_100, y_100, color = 'pink', label = "N = 100", linewidth = 1)
plt.legend(loc = "upper left")
plt.title("Phase Transition in Mixed 3-4 SAT model (rescaled)")
plt.xlabel("(L/N - " + str(alfa) + ")N^1/" + str(v))
plt.ylabel("Probability")		
plt.show()




