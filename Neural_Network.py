import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

weights = np.array([10, 10])
bias = -15 

def perceptron(inputs):
    linear_combination = np.dot(inputs, weights) + bias
    return sigmoid(linear_combination) >= 0.5

print(perceptron([1, 1])) 
