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
        for j in range(n_qubits):
            # single-qubit rotations
            qml.RX(weights[i*n_qubits+j,0], wires=j)
            qml.RY(weights[i*n_qubits+j,1], wires=j)
            qml.RZ(weights[i*n_qubits+j,2], wires=j)

        if n_qubits > 1:
            # engtangling gates
            qml.broadcast(qml.CNOT, wires, pattern="ring")


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
    print(weights)
    
    drawer = qml.draw(my_circuit)
    print(drawer(weights, wires=dev.wires))
