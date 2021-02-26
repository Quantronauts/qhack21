#! /usr/bin/python3

import pennylane as qml
from pennylane import numpy as np


def circuit(x, wires):
    n_qubits = len(wires)
    n_rotations = len(x)

    if n_rotations != n_qubits:
        raise Exception("Not all qubits are rotated")

    for i in range(n_qubits):
        qml.RX(x[i,0], wires=i)
        qml.RY(x[i,1], wires=i)


def get_labelled_dataset(wires, how_many):
    n_qubits = len(wires)

    X = np.random.uniform(low=-np.pi, high=np.pi, size=(how_many, n_qubits, 2)) # data vectors
    Y = np.ones(how_many) # labels, 1 means Qat, -1 means DoQ

    for i in range(how_many):
        x = X[i]

        n_east = 0
        n_west = 0
        for j in range(n_qubits):
            if x[j,0] <= 0.0:
                n_east += 1
            else:
                n_west += 1

        # majority voting
        if n_west > n_east:
            Y[i] = -1

    return X, Y


if __name__ == "__main__":
    dev = qml.device("default.qubit", wires=range(3))

    @qml.qnode(dev)
    def my_circuit(x, wires):
        circuit(x, wires)
        return qml.expval(qml.PauliY(0))    

    X, Y = get_labelled_dataset(dev.wires, 5)
    print(X)
    print(Y)
    
    drawer = qml.draw(my_circuit)
    print(drawer(X[0], dev.wires))

    x = np.array([[-np.pi/2, 0.0], [0, 0], [0, 0]], dtype=np.float64)
    print(my_circuit(x, dev.wires))
