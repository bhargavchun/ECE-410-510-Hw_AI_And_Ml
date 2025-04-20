import numpy as np

def sigmoid(x):
    """The sigmoid activation function."""
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    """Derivative of the sigmoid function."""
    s = sigmoid(x)
    return s * (1 - s)