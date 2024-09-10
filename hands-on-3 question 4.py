import time
import numpy as np
import matplotlib.pyplot as plt

def simulate_iterations(length):
    total = 2
    for i in range(length):
        for j in range(length):
            total += 1
    return total

z = np.arange(1, 116)
TR = [(lambda n: time.perf_counter() - time.perf_counter() + simulate_iterations(n))(n) for n in z]
arc = np.polyfit(z, TR, 4)
totalfit = np.polyval(arc, z)
plt.scatter(z, TR, color='green', label="Execution Times", marker='x')
plt.plot(z, totalfit, color='orange', label="arc (Polyn)", linewidth=1.98)
n_0 = 101
executiontime_n_0 = TR[n_0 - 1]
plt.axvline(x= n_0, color='red', linestyle='--', label=f'Approx. n_0 = {n_0}')
plt.xlabel('(n)')
plt.ylabel('T(seconds)')
plt.title('T vs n with approx(n_0)')
plt.legend()
plt.grid(True)
plt.show()

print(f"approx n_0: {n_0}")
print(f"Executiontime_n_0: {executiontime_n_0} seconds")