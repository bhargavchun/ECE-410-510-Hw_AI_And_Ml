def systolic_bubble_sort(arr):
    n = len(arr)
    A = arr.copy()
    for i in range(n):
        for j in range(1 - i % 2, n - 1, 2):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A

# Test
import random
arr = [random.randint(0, 100) for _ in range(100)]
print(systolic_bubble_sort(arr))
