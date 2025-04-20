class Perceptron:
    def __init__(self, num_inputs):
        self.weights = np.random.rand(num_inputs)
        self.bias = np.random.rand(1)[0]
        self.learning_rate = 0.1

    def predict(self, inputs):
        weighted_sum = np.dot(inputs, self.weights) + self.bias
        return sigmoid(weighted_sum)

    def train(self, training_inputs, targets, epochs):
        for epoch in range(epochs):
            for inputs, target in zip(training_inputs, targets):
                prediction = self.predict(inputs)
                error = target - prediction

                # Update weights
                for i in range(len(self.weights)):
                    self.weights[i] += self.learning_rate * error * inputs[i]

                # Update bias
                self.bias += self.learning_rate * error

            if epoch % 1000 == 0:
                loss = np.mean((targets - [self.predict(x) for x in training_inputs]) ** 2)
                print(f"Epoch {epoch}, Loss: {loss:.4f}")


   # Training data for NAND
   nand_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
   nand_targets = np.array([1, 1, 1, 0])

   # Create and train the perceptron
   nand_perceptron = Perceptron(num_inputs=2)
   nand_perceptron.train(nand_inputs, nand_targets, epochs=10000)

   # Test the trained perceptron for NAND
   print("\nNAND Gate Results:")
   for inputs in nand_inputs:
     prediction = nand_perceptron.predict(inputs)
     print(f"Input: {inputs}, Prediction: {prediction:.4f}, Target: {nand_targets[np.where((nand_inputs == inputs).all(axis=1))[0][0]]}")

   # Training data for XOR
   xor_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
   xor_targets = np.array([0, 1, 1, 0])

   # Create and train the perceptron
   xor_perceptron = Perceptron(num_inputs=2)
   xor_perceptron.train(xor_inputs, xor_targets, epochs=20000) # XOR might need more epochs

   # Test the trained perceptron for XOR
   print("\nXOR Gate Results:")
   for inputs in xor_inputs:
     prediction = xor_perceptron.predict(inputs)
     print(f"Input: {inputs}, Prediction: {prediction:.4f}, Target: {xor_targets[np.where((xor_inputs == inputs).all(axis=1))[0][0]]}")