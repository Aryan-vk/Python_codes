import matplotlib.pyplot as plt

with open("VnIvalues.txt", "r") as file:
    lines = file.readlines()

voltages = []
currents = []

for line in lines:
    voltage, current = map(float, line.strip().split())
    voltages.append(voltage)
    currents.append(current)

plt.figure(figsize=(5, 5))
plt.scatter(voltages, currents, marker='*', color='b')
plt.title('Voltage vs Current')
plt.xlabel('Voltage')
plt.ylabel('Current')
plt.grid(True)

def sum_v(voltages):
    sum_v = 0
    for v in voltages:
     sum_v += v
    return sum_v

def sum_i(currents):
    sum_i = 0
    for i in currents:
     sum_i += i
    return sum_i

n = len(voltages)
sum_xy = sum(v * i for v, i in zip(voltages, currents))
sum_x_squared = sum(v ** 2 for v in voltages)

m = (n * sum_xy - sum_v(voltages) * sum_i(currents)) / (n * sum_x_squared - sum_v(voltages) ** 2)
C = (sum_i(currents) - m * sum_v(voltages)) / n

plt.plot(voltages, [m*v + C for v in voltages], color='r', label=f'Y = {m:.2f}X + {C:.2f}')
plt.legend()
plt.show()

print(f"Slope (m): {m}")
print(f"Intercept (C): {C}")

