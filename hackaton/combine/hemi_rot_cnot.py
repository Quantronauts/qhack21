#! /usr/bin/python3

import pennylane as qml
#from pennylane import numpy as np

import sys
from os import path

sys.path.append(path.abspath('../sensors'))
sys.path.append(path.abspath('../classifiers'))

import n_hemispheres as hemi
import rot_cnot_processing as rcnp


def combined_expval(weights, x, wires):
    hemi.circuit(x, wires)
    rcnp.circuit(weights, wires)

    # create PauliZ ⊗ ... ⊗ PauliZ
    op = qml.PauliZ(0)
    for i in range(1, len(wires)):
        op = op @ qml.PauliZ(i)

    return qml.expval(op)


def combined_1shot(weights, x, wires):
    hemi.circuit(x, wires)
    rcnp.circuit(weights, wires)

    # create PauliZ ⊗ ... ⊗ PauliZ
    op = qml.PauliZ(0)
    for i in range(1, len(wires)):
        op = op @ qml.PauliZ(i)

    return qml.sample(op)


def get_data_and_weights(wires, n_layers, how_many):
    X, Y = hemi.get_labelled_dataset(wires, how_many)
    weights = rcnp.get_initial_weights(wires, n_layers)
    return X, Y, weights


if __name__ == "__main__":
    dev_expval = qml.device("default.qubit", wires=range(3))
    print(dev_expval)

    dev_1shot = qml.device("default.qubit", wires=range(3), shots=1)
    print(dev_1shot)

    @qml.qnode(dev_expval)
    def my_combined_expval(weights, x, wires):
        return combined_expval(weights, x, wires)

    @qml.qnode(dev_1shot)
    def my_combined_1shot(weights, x, wires):
        return combined_1shot(weights, x, wires)

    X, Y, weights = get_data_and_weights(dev_expval.wires, 2, 5)
    print(X)
    print(Y)
    print(weights)

    drawer = qml.draw(my_combined_expval)
    print(drawer(weights, X[0], wires=dev_expval.wires))

    # expval classifier output for sensor data x (weights were not optimized)
    print(my_combined_expval(weights, X[0], wires=dev_expval.wires))

    # 1shot classifier output for sensor data x (weights were not optimized)
    print(my_combined_1shot(weights, X[0], wires=dev_1shot.wires))
