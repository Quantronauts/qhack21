#! /usr/bin/python3

import pennylane as qml
from pennylane import numpy as np


def circuit(params, wires):
    n_qubits = len(wires)
    n_rotations = len(params)

    if n_rotations != n_qubits:
        raise Exception("Not all qubits are rotated")

    for i in range(n_qubits):
        qml.RY(params[i,0], wires=i)
        qml.RZ(params[i,1], wires=i)


def init_params(wires):
    n_qubits = len(wires)
    return np.random.uniform(low=-np.pi, high=np.pi, size=(n_qubits, 2))


if __name__ == "__main__":
    wires = range(2)
    dev = qml.device("default.qubit", wires=wires)

    @qml.qnode(dev)
    def my_circuit(params, wires):
        circuit(params, wires)
        return qml.expval(qml.PauliY(0))    

    params = init_params(dev.wires)
    
    drawer = qml.draw(my_circuit)
    print(drawer(params=params, wires=wires))

    #params = np.array([[np.pi/2, np.pi/2], [0, 0]], dtype=np.float64)
    #print(my_circuit(params, wires))
