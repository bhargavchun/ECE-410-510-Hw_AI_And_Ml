import numpy as np

def matrix_multiply(A, B):
    print("Performing matrix multiplication...")
    print(f"Matrix A shape: {A.shape}")
    print(f"Matrix B shape: {B.shape}")
    result = np.dot(A, B)
    print("Matrix multiplication complete.")
    print(f"Result shape: {result.shape}")
    return result

print("Generating random matrices A and B...")
A = np.random.rand(100, 100)
B = np.random.rand(100, 100)

print("Calling matrix_multiply...")
C = matrix_multiply(A, B)

print("Result matrix C (first 5x5 block):")
print(C[:5, :5])  # Prints the top-left 5x5 portion of the matrix for readability

print("Done.")