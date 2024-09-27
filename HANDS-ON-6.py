import random
import time
import matplotlib.pyplot as plt

def sort_fixed(arr):
    if len(arr) <= 1:
        return arr
    mid = arr[len(arr) // 2]
    left = [x for x in arr if x < mid]
    equal = [x for x in arr if x == mid]
    right = [x for x in arr if x > mid]
    return sort_fixed(left) + equal + sort_fixed(right)

def sort_random(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return sort_random(left) + equal + sort_random(right)

def measure_time(data, func):
    times = []
    for d in data:
        start = time.time()
        func(d)
        end = time.time()
        times.append(end - start)
    return times

size = 212
sizes = list(range(1, size + 1))

best_case = [list(range(1, n + 1)) for n in sizes]
worst_case = [list(range(n, 0, -1)) for n in sizes]
average_case = [random.sample(range(1, n + 1), n) for n in sizes]

plt.plot(sizes, measure_time(best_case, sort_fixed), label='Best Case')
plt.plot(sizes, measure_time(worst_case, sort_fixed), label='Worst Case')
plt.plot(sizes, measure_time(average_case, sort_fixed), label='Average Case')

plt.xlabel('Size')
plt.ylabel('Time')
plt.title('Benchmark of non-random pivot points :')
plt.legend()
plt.show()