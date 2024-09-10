import time
import numpy as np
import matplotlib.pyplot as plt

def x_func(n):
    count = 2
    increment_nested(count, n)
    return count
def increment_nested(count, n):
    for _ in range(n):
        for _ in range(n):
            count += 1

def y_func(n):
    count = 2
    add_and_compute(count, n)
    return count
def add_and_compute(count, n):
    for a in range(n):
        for b in range(n):
            count += 1
            temp = compute_sum(a, b)
def compute_sum(a, b):
    return a + b

z = np.arange(1, 116)
x_times = []
y_times = []

for n in z:
    start_time = time.perf_counter()
    x_f(n)
    x_times.append(time.perf_counter() - start_time)  
    start_time = time.perf_counter()
    y_f(n)
    y_times.append(time.perf_counter() - start_time)
    
arc_x = np.polyfit(z, x_times, 4)
totalfit_x = np.polyval(arc_x, z)
arc_y = np.polyfit(z, y_times, 4)
totalfit_y = np.polyval(arc_y, z)
plt.scatter(z, x_times, color='blue', label="Original Execution Times", marker='o')
plt.scatter(z, y_times, color='green', label="Modified Execution Times", marker='x')
plt.plot(z, totalfit_x, color='orange', label="Original fit", linewidth=1.98)
plt.plot(z, totalfit_y, color='red', label="Modified fit", linewidth=1.98)

n_0 = 101
plt.axvline(x=n_0, color='purple', linestyle='--', label=f'Approx. n_0 = {n_0}')
plt.xlabel('(n)')
plt.ylabel('T(seconds)')
plt.title('Execution Time -> Original vs Modified')
plt.legend()
plt.grid(True)
plt.show()

executiontime_n_0_x = x_times[n_0 - 1]
executiontime_n_0_y = y_times[n_0 - 1]

print(f"Approx n_0: {n_0}")
print(f"Execution time at n_0 for original func: {executiontime_n_0_x:.6f} seconds")
print(f"Execution time at n_0 for modified func: {executiontime_n_0_y:.6f} seconds")
