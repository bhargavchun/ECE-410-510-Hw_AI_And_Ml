class MultiLayerPerceptron:
    def __init__(self, num_inputs, num_hidden, num_outputs):
        self.num_inputs = num_inputs
        self.num_hidden = num_hidden
        self.num_outputs = num_outputs

        # Initialize weights with random values
        self.weights_input_hidden = np.random.rand(self.num_inputs, self.num_hidden) - 0.5
        self.bias_hidden = np.random.rand(1, self.num_hidden) - 0.5
        self.weights_hidden_output = np.random.rand(self.num_hidden, self.num_outputs) - 0.5
        self.bias_output = np.random.rand(1, self.num_outputs) - 0.5
        self.learning_rate = 0.1

    def forward(self, inputs):
        # Hidden layer
        self.hidden_layer_input = np.dot(inputs, self.weights_input_hidden) + self.bias_hidden
        self.hidden_layer_output = sigmoid(self.hidden_layer_input)

        # Output layer
        self.output_layer_input = np.dot(self.hidden_layer_output, self.weights_hidden_output) + self.bias_output
        self.output_layer_output = sigmoid(self.output_layer_input)

        return self.output_layer_output

    def backward(self, inputs, targets, outputs):
        # Output layer error
        output_error = targets - outputs
        output_delta = output_error * sigmoid_derivative(self.output_layer_input)

        # Hidden layer error
        hidden_error = np.dot(output_delta, self.weights_hidden_output.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.hidden_layer_input)

        # Update weights and biases
        self.weights_hidden_output += self.learning_rate * np.dot(self.hidden_layer_output.T, output_delta)
        self.bias_output += self.learning_rate * np.sum(output_delta, axis=0, keepdims=True)
        self.weights_input_hidden += self.learning_rate * np.dot(inputs.T, hidden_delta)
        self.bias_hidden += self.learning_rate * np.sum(hidden_delta, axis=0, keepdims=True)

    def train(self, training_inputs, targets, epochs):
        for epoch in range(epochs):
            for inputs, target in zip(training_inputs, targets):
                # Forward pass
                output = self.forward(inputs)

                # Backward pass and weight update
                self.backward(inputs, target, output)

            if epoch % 1000 == 0:
                predictions = np.array([self.forward(x) for x in training_inputs])
                loss = np.mean((targets - predictions) ** 2)
                accuracy = np.mean(((predictions > 0.5).astype(int) == targets.astype(int)))
                print(f"Epoch {epoch}, Loss: {loss:.4f}, Accuracy: {accuracy:.4f}")

    def predict(self, inputs):
        return self.forward(inputs)