#! /usr/bin/python3

import sys
import pennylane as qml
import numpy as np


def classify_data(X_train, Y_train, X_test):
    """Develop and train your very own variational quantum classifier.

    Use the provided training data to train your classifier. The code you write
    for this challenge should be completely contained within this function
    between the # QHACK # comment markers. The number of qubits, choice of
    variational ansatz, cost function, and optimization method are all to be
    developed by you in this function.

    Args:
        X_train (np.ndarray): An array of floats of size (250, 3) to be used as training data.
        Y_train (np.ndarray): An array of size (250,) which are the categorical labels
            associated to the training data. The categories are labeled by -1, 0, and 1.
        X_test (np.ndarray): An array of floats of (50, 3) to serve as testing data.

    Returns:
        str: The predicted categories of X_test, converted from a list of ints to a
            comma-separated string.
    """

    # Use this array to make a prediction for the labels of the data in X_test
    predictions = []

    # QHACK #
    dev = qml.device("default.qubit", wires=1)

    @qml.qnode(dev)
    def classifier(weights, x):
        qml.RY(weights[0,0]*x[0]+weights[0,1], wires=0)
        qml.RY(weights[1,0]*x[1]+weights[1,1], wires=0)
        qml.RY(weights[2,0]*x[2]+weights[2,1], wires=0)
        return qml.expval(qml.PauliZ(0))    

    def square_loss(labels, predictions):
        loss = 0
        for l, p in zip(labels, predictions):
            loss = loss + (l - p) ** 2
        loss = loss / len(labels)
        #print(loss)
        return loss

    def cost(weights, X, Y):
        predictions = [classifier(weights, x) for x in X]
        return square_loss(Y, predictions)

    w = np.array([[1.0, 0.0], [1.0, 0.0], [1.0, 0.0]], dtype=np.float64)

    steps = 20
    batch_size = 25
    opt = qml.GradientDescentOptimizer(0.1)

    np.random.seed(0)
    for _ in range(steps):
        batch_index = np.random.randint(0, len(X_train), (batch_size,))
        X_batch = X_train[batch_index]
        Y_batch = Y_train[batch_index]
        w = opt.step(lambda weights: cost(weights, X_batch, Y_batch), w)

    #predictions = [classifier(w, x) for x in X_train]
    #for i in range(len(X_train)):
    #    if predictions[i] < -0.5:
    #        predictions[i] = -1
    #    elif predictions[i] > 0.5:
    #        predictions[i] = 1
    #    else:
    #        predictions[i] = 0
    #    if np.abs(predictions[i] - Y_train[i]) > 0.1:
    #        print("HELLO")

    predictions = [classifier(w, x) for x in X_test]
    for i in range(len(X_test)):
        if predictions[i] < -0.5:
            predictions[i] = -1
        elif predictions[i] > 0.5:
            predictions[i] = 1
        else:
            predictions[i] = 0

    #from matplotlib import pyplot as plt
    #plt.style.use("seaborn")
    #fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')
    #for i in range(50):
    #    ax.scatter(X_train[i,0],X_train[i,1],X_train[i,2])
        #ax.scatter(X_test[i,0],X_test[i,2],X_test[i,2])
    #plt.show()

    # QHACK #

    return array_to_concatenated_string(predictions)


def array_to_concatenated_string(array):
    """DO NOT MODIFY THIS FUNCTION.

    Turns an array of integers into a concatenated string of integers
    separated by commas. (Inverse of concatenated_string_to_array).
    """
    return ",".join(str(x) for x in array)


def concatenated_string_to_array(string):
    """DO NOT MODIFY THIS FUNCTION.

    Turns a concatenated string of integers separated by commas into
    an array of integers. (Inverse of array_to_concatenated_string).
    """
    return np.array([int(x) for x in string.split(",")])


def parse_input(giant_string):
    """DO NOT MODIFY THIS FUNCTION.

    Parse the input data into 3 arrays: the training data, training labels,
    and testing data.

    Dimensions of the input data are:
      - X_train: (250, 3)
      - Y_train: (250,)
      - X_test:  (50, 3)
    """
    X_train_part, Y_train_part, X_test_part = giant_string.split("XXX")

    X_train_row_strings = X_train_part.split("S")
    X_train_rows = [[float(x) for x in row.split(",")] for row in X_train_row_strings]
    X_train = np.array(X_train_rows)

    Y_train = concatenated_string_to_array(Y_train_part)

    X_test_row_strings = X_test_part.split("S")
    X_test_rows = [[float(x) for x in row.split(",")] for row in X_test_row_strings]
    X_test = np.array(X_test_rows)

    return X_train, Y_train, X_test


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block

    X_train, Y_train, X_test = parse_input(sys.stdin.read())
    output_string = classify_data(X_train, Y_train, X_test)
    print(f"{output_string}")
