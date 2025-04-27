#include <iostream>
#include <cuda_runtime.h>
#include <vector>

__global__
void add(int n, float *x, float *y)
{
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        y[i] = x[i] + y[i];
    }
}

void run_test(int N, std::vector<float>& times_memcpy, std::vector<float>& times_kernel)
{
    float *x, *y;
    float *d_x, *d_y;

    x = (float*)malloc(N * sizeof(float));
    y = (float*)malloc(N * sizeof(float));

    for (int i = 0; i < N; i++) {
        x[i] = 1.0f;
        y[i] = 2.0f;
    }

    cudaEvent_t startMemcpy, stopMemcpy, startKernel, stopKernel;
    cudaEventCreate(&startMemcpy);
    cudaEventCreate(&stopMemcpy);
    cudaEventCreate(&startKernel);
    cudaEventCreate(&stopKernel);

    cudaEventRecord(startMemcpy);
    cudaMalloc(&d_x, N * sizeof(float));
    cudaMalloc(&d_y, N * sizeof(float));
    cudaMemcpy(d_x, x, N * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_y, y, N * sizeof(float), cudaMemcpyHostToDevice);
    cudaEventRecord(stopMemcpy);
    cudaEventSynchronize(stopMemcpy);

    cudaEventRecord(startKernel);
    int blockSize = 256;
    int numBlocks = (N + blockSize - 1) / blockSize;
    add<<<numBlocks, blockSize>>>(N, d_x, d_y);
    cudaEventRecord(stopKernel);
    cudaEventSynchronize(stopKernel);

    cudaMemcpy(y, d_y, N * sizeof(float), cudaMemcpyDeviceToHost);

    float milliseconds_memcpy = 0, milliseconds_kernel = 0;
    cudaEventElapsedTime(&milliseconds_memcpy, startMemcpy, stopMemcpy);
    cudaEventElapsedTime(&milliseconds_kernel, startKernel, stopKernel);

    times_memcpy.push_back(milliseconds_memcpy);
    times_kernel.push_back(milliseconds_kernel);

    cudaFree(d_x);
    cudaFree(d_y);
    free(x);
    free(y);
}

int main()
{
    std::vector<int> sizes;
    std::vector<float> times_memcpy;
    std::vector<float> times_kernel;

    for (int power = 15; power <= 25; power++) {
        int N = 1 << power;
        std::cout << "Running for N = " << N << std::endl;
        run_test(N, times_memcpy, times_kernel);
        sizes.push_back(N);
    }

    // Print results
    std::cout << "\nResults:\n";
    for (int i = 0; i < sizes.size(); i++) {
        std::cout << "N=" << sizes[i]
                  << " | Memcpy Time=" << times_memcpy[i]
                  << " ms | Kernel Time=" << times_kernel[i]
                  << " ms\n";
    }

    return 0;
}
