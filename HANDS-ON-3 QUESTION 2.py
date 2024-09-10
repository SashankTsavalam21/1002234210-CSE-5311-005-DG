import time
import numpy as np
import matplotlib.pyplot as plt

def simulate_iterations(length):
    total = 2
    total += sum(1 for _ in range(length) for _ in range(length))
    return total

z = np.arange(1, 116)

TR = [(lambda n: time.perf_counter() - time.perf_counter() + simulate_iterations(n))(n) for n in z]

arc = np.polyfit(input_sizes, TR, 4)
totalfit = np.polyval(arc, input_sizes)

plt.scatter(input_sizes, TR , c='green', label="no of times measured", marker='x')
plt.plot(input_sizes, totalfit, c='orange', label="arc", linewidth=1.98)
plt.xlabel('(n)')
plt.ylabel('T(seconds)')
plt.title(' t vs n')
plt.legend()
plt.grid(True)
plt.show()
