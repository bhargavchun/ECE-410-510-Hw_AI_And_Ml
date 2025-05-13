import time
import matplotlib.pyplot as plt

sizes = [10, 100, 1000, 10000]
times = []

for size in sizes:
    arr = [random.randint(0, 10000) for _ in range(size)]
    start = time.time()
    systolic_bubble_sort(arr)
    times.append(time.time() - start)

plt.plot(sizes, times)
plt.xlabel('Array Size')
plt.ylabel('Time (s)')
plt.title('Systolic Bubble Sort Performance')
plt.grid(True)
plt.show()
