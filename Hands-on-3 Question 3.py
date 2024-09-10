import time
import numpy as np
import matplotlib.pyplot as plt

def perform_iterations(length):
    counter = 2
    counter += sum(1 for _ in range(length) for _ in range(length))
    return counter
input_sizes = np.arange(1, 121)

et = [(lambda x: time.perf_counter() - time.perf_counter() + perform_iterations(x))(x) for x in input_sizes]

p_c = np.polyfit(input_sizes, et, 3)
fit = np.polyval(p_c, input_sizes)

upperbound_x = np.polyfit(input_sizes, et, 1)
lowerbound_x = np.polyfit(input_sizes, et, 2)

upperbound_y = np.polyval(upperbound_x, input_sizes)
lowerbound_y = np.polyval(lowerbound_x, input_sizes)

plt.scatter(input_sizes, et, color='green', label='Execution Times', marker='x')
plt.plot(input_sizes, fit, color='orange', label='arc', linewidth=1.99)
plt.plot(input_sizes, upperbound_y, color='blue', linestyle='--', label='Upperbound', linewidth=1.98)
plt.plot(input_sizes, lowerbound_y, color='red', linestyle='--', label='LowerBound', linewidth=1.97)
plt.xlabel('(n)')
plt.ylabel('T(seconds)')
plt.title('T vs n')
plt.legend()
plt.grid(True)
plt.show()
print("arc:", np.poly1d(fit))
print("Upperbound O(n)", np.poly1d(upperbound_x))
print("Lowerbound Ω(n)", np.poly1d(lowerbound_x))