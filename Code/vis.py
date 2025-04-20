import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class SimplePerceptronVisualizer:
    def __init__(self, num_inputs):
        self.weights = np.random.rand(num_inputs) - 0.5
        self.bias = np.random.rand(1)[0] - 0.5
        self.learning_rate = 0.1
        self.history_weights = []
        self.history_bias = []

    def predict(self, inputs):
        weighted_sum = np.dot(inputs, self.weights) + self.bias
        return 1 if sigmoid(weighted_sum) >= 0.5 else 0

    def train_step(self, inputs, target):
        prediction = self.predict(inputs)
        error = target - prediction
        self.weights += self.learning_rate * error * inputs
        self.bias += self.learning_rate * error
        self.history_weights.append(self.weights.copy())
        self.history_bias.append(self.bias)

    def plot_decision_boundary(self, ax, x_min, x_max, y_min, y_max):
        if self.weights[1] == 0:
            return  # Avoid division by zero
        x = np.linspace(x_min, x_max, 100)
        y = (-self.weights[0] * x - self.bias) / self.weights[1]
        ax.plot(x, y, 'r--')

# Training data for NAND
nand_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
nand_targets = np.array([1, 1, 1, 0])

# Initialize perceptron and lists for animation
perceptron_visualizer = SimplePerceptronVisualizer(num_inputs=2)
fig, ax = plt.subplots()
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
scatter = ax.scatter(nand_inputs[:, 0], nand_inputs[:, 1], c=nand_targets, cmap=plt.cm.RdYlBu, s=100)
line, = ax.plot([], [], 'g-', linewidth=2)
title = ax.text(0.5, 1.1, '', transform=ax.transAxes, ha='center')

def animate(i):
    perceptron_visualizer.weights = perceptron_visualizer.history_weights[i]
    perceptron_visualizer.bias = perceptron_visualizer.history_bias[i]
    if perceptron_visualizer.weights[1] != 0:
        x = np.linspace(-0.5, 1.5, 100)
        y = (-perceptron_visualizer.weights[0] * x - perceptron_visualizer.bias) / perceptron_visualizer.weights[1]
        line.set_data(x, y)
    title.set_text(f"Iteration: {i+1}, Weights: [{perceptron_visualizer.weights[0]:.2f}, {perceptron_visualizer.weights[1]:.2f}], Bias: {perceptron_visualizer.bias:.2f}")
    return line, title

def train_and_animate(perceptron, inputs, targets, epochs):
    perceptron.history_weights.append(perceptron.weights.copy())
    perceptron.history_bias.append(perceptron.bias)
    for _ in range(epochs):
        for input_data, target in zip(inputs, targets):
            perceptron.train_step(input_data, target)

# Train for a few epochs to see the movement
train_and_animate(perceptron_visualizer, nand_inputs, nand_targets, epochs=20)

ani = animation.FuncAnimation(fig, animate, frames=len(perceptron_visualizer.history_weights), interval=500, blit=True)
plt.xlabel("Input 1")
plt.ylabel("Input 2")
plt.title("Perceptron Learning for NAND")
plt.show()