#! /usr/bin/python3

import pennylane as qml
from pennylane import numpy as np


def circuit(weights, wires):
    n_qubits = len(wires)
    n_rotations = len(weights)
    n_layers = n_rotations // n_qubits

    if n_rotations % n_qubits != 0:
        raise Exception("Last layer is incomplete, not all qubits are rotated")

    for i in range(n_layers):
        w_i = weights[i * n_qubits : (i+1) * n_qubits, :]

        qml.broadcast(qml.Rot, wires, pattern="single", parameters=w_i) # single-qubit rotations

        if n_qubits > 1:
            qml.broadcast(qml.CNOT, wires, pattern="ring") # engtangling gates


def get_initial_weights(wires, n_layers):
    n_qubits = len(wires)
    return np.random.uniform(low=-np.pi, high=np.pi, size=(n_layers * n_qubits, 3))


if __name__ == "__main__":
    dev = qml.device("default.qubit", wires=range(3))

    @qml.qnode(dev)
    def my_circuit(weights, wires):
        circuit(weights, wires)
        return qml.expval(qml.PauliZ(0))    

    n_layers = 2
    weights = get_initial_weights(dev.wires, n_layers)
    
    drawer = qml.draw(my_circuit)
    print(drawer(weights, wires=dev.wires))
