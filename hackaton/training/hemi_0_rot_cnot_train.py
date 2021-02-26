#! /usr/bin/python3

import pennylane as qml
from pennylane import numpy as np

import sys
from os import path

sys.path.append(path.abspath('../combine'))

import hemi_0_rot_cnot as hrcn


n_qubits = 1 ### Number of qubits in classifier, change it as you wish. Sensor will ALWAYS use only 1st qubit
n_shots = 30 ### This is for TRAINING (to calculate expected values), for testing see shots below

dev_expval = qml.device("default.qubit", wires=range(n_qubits), analytic=False, shots=n_shots)
print(dev_expval)


@qml.qnode(dev_expval)
def combined_expval_train(weights, x, wires):
    return hrcn.combined_expval(weights, x, wires)


def k_power_loss(labels, predictions, k):
    loss = 0.0
    for l, p in zip(labels, predictions):
        #print(p)
        loss += np.abs(l - p) ** k
    loss = loss / len(labels)
    return loss


def cost(weights, wires, X, Y, k):
    predictions = [combined_expval_train(weights, x, wires=wires) for x in X]
    return k_power_loss(Y, predictions, k)


def train(weights, wires, X, Y, steps, batch_size, k):
    #opt = qml.GradientDescentOptimizer(0.1)
    opt = qml.NesterovMomentumOptimizer(0.1)

    for _ in range(steps):
        batch_idx = np.random.randint(0, len(X), (batch_size,))

        X_batch = X[batch_idx]
        Y_batch = Y[batch_idx]

        weights, prev_cost = opt.step_and_cost(lambda weights: cost(weights, wires, X_batch, Y_batch, k), weights)
        print(prev_cost)
        #print(weights)

    opt_cost = cost(weights, wires, X, Y, k)
    print(opt_cost)

    return weights


if __name__ == "__main__":
    np.random.seed(0) ### This ensures results are reproducible

    n_layers = 1 ### number of layers, more than 1 makes sense when n_qubits > 1, or we use data re-upload
    how_many = 500 ### size of training set, random points on Bloch sphere
    X, Y, weights = hrcn.get_data_and_weights(dev_expval.wires, n_layers, how_many)
    #print(X)
    #print(Y)
    print(weights)

    drawer = qml.draw(combined_expval_train)
    print(drawer(weights, X[0], wires=dev_expval.wires))

    k = 1 ### power in cost function, 1 is the best, surprisingly
    steps = 50
    batch_size = 10
    opt_weights = train(weights, dev_expval.wires, X, Y, steps, batch_size, k)
    #print(opt_weights)
    
    drawer = qml.draw(combined_expval_train) ### Sensor has RX and RY gates, then each classifier layer has RX, RY, and RZ, plus CNOTS (if n_qubits > 1)
    print(drawer(opt_weights, X[0], wires=dev_expval.wires))

    #
    # Accuracy on unseen test set
    #
    X_test, Y_test, not_used = hrcn.get_data_and_weights(dev_expval.wires, n_layers, 1000) ### test set has 1000 items
    
    acc_n_shots = 1 ### 1-shot results, change to 30, or 1000, to get results when multiple shots are possible during operation
    dev_acc_expval = qml.device("default.qubit", wires=range(n_qubits), analytic=False, shots=acc_n_shots)
    
    @qml.qnode(dev_acc_expval)
    def acc_combined_expval_train(weights, x, wires):
        return hrcn.combined_expval(weights, x, wires)

    predictions = [acc_combined_expval_train(opt_weights, x, wires=dev_acc_expval.wires) for x in X_test]
    #print(dev_acc_expval.state)

    correct_predictions = 0
    for i in range(len(X_test)):
        if (predictions[i] >= 0.0 and Y_test[i] == 1) or (predictions[i] < 0.0 and Y_test[i] == -1):
            correct_predictions += 1

    accuracy = correct_predictions / len(Y_test)
    print(accuracy)
