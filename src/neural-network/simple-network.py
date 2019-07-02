import numpy as np
from numpy import random

batch_size = 64      # number of networks
n_iterations = 500   # number of iterations
n_input = 1000       # number of input neurons
n_hidden = 100       # number of hidden neurons
n_output = 10        # number of output neurons
learning_rate = 1e-6 # learning rate

# Create randomized input
random.seed(1)
input = random.randn(batch_size, n_input)

# Create randomized output
random.seed(2)
output = random.randn(batch_size, n_output)

# Create randomized weights
random.seed(3)
w1 = np.random.randn(n_input, n_hidden)     # input  --> hidden
random.seed(4)
w2 = np.random.randn(n_hidden, n_output)    # hidden --> output

for i in range(n_iterations):

    # -------------------------------------
    # FORWARD PASS
    # -------------------------------------

    # Calculate net input for hidden neurons
    hidden_input = input.dot(w1)

    # Calculate net output for hidden neurons
    # using ReLU as activation function
    hidden_output = np.maximum(0, hidden_input)

    # Calculate predictions (output neurons)
    predictions = hidden_output.dot(w2)

    # Calculate MSE (mean squared error)
    mse = (1/n_output) * np.square(predictions - output).sum()
    print(f'{i}:\t MSE =', mse)

    # -------------------------------------
    # BACKPROPAGATION
    # -------------------------------------

    # Calculate 
    error_signal = 2.0 * (predictions - output)
    delta_w2 = hidden_output.T.dot(error_signal)
    delta_hidden_relu = error_signal.dot(w2.T)
    delta_hidden = delta_hidden_relu.copy()
    delta_hidden[hidden_input < 0] = 0
    delta_w1 = input.T.dot(delta_hidden)

    # Update weights
    w1 -= learning_rate * delta_w1
    w2 -= learning_rate * delta_w2
