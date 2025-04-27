import matplotlib.pyplot as plt

# Fill these with your actual measured values
sizes = [2**i for i in range(15, 26)]
memcpy_times = [your_memcpy_times_here]  # ms
kernel_times = [your_kernel_times_here]  # ms

plt.figure(figsize=(12, 6))
plt.bar([str(s) for s in sizes], memcpy_times, alpha=0.7, label='Memory Copy Time')
plt.bar([str(s) for s in sizes], kernel_times, alpha=0.7, label='Kernel Execution Time')

plt.xlabel('Vector Size (N)')
plt.ylabel('Time (ms)')
plt.title('CUDA Vector Addition Timing')
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()
