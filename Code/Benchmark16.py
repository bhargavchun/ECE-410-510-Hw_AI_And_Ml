import time

start = time.time()
output = model(x)
torch.cuda.synchronize()
end = time.time()
print("PyTorch time:", end - start)
