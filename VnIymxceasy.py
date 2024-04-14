import matplotlib.pyplot as plt
import numpy as np

with open('VnIvalues.txt', "r") as file:
    lines = file.readlines()

voltages = []
currents = []

for line in lines:
    voltage, current = map(float, line.strip().split())
    voltages.append(voltage)
    currents.append(current)

plt.scatter(voltages, currents, marker='*', color='b')
plt.title('Voltage vs Current')
plt.xlabel('Voltage')
plt.ylabel('Current')
plt.grid(True)

# To implement the equation Y=mX+C we need to perform linear regression :-
coefficients = np.polyfit(voltages, currents, 1)
m, C = coefficients 
print(f'The values of m,C are :- {coefficients}')

plt.plot(voltages, m*np.array(voltages) + C, color='r', label=f'Y = {m:.2f}X + {C:.2f}')
plt.legend()
plt.show()

print(f"Slope (m): {m}")
print(f"Intercept (C): {C}")
