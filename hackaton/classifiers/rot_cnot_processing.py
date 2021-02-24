#! /usr/bin/python3

import pennylane as qml
from pennylane import numpy as np


def circuit(params, wires):
    """
    Args:
        params (np.ndarray): An array of floating-point numbers with size (n, 3),
            where n is the number of parameter sets required.
        wires (qml.Wires): The device wires this circuit will run on.
    """
    n_qubits = len(wires)
    n_rotations = len(params)
    n_layers = n_rotations // n_qubits

    if n_rotations % n_qubits != 0:
        raise Exception("Last layer is incomplete, not all qubits are rotated")

    # Alternating layers of unitary rotations on every qubit followed by a
    # ring cascade of CNOTs.
    for layer_idx in range(n_layers):
        layer_params = params[layer_idx * n_qubits : layer_idx * n_qubits + n_qubits, :]
        qml.broadcast(qml.Rot, wires, pattern="single", parameters=layer_params)
        if n_qubits > 1:
            qml.broadcast(qml.CNOT, wires, pattern="ring")


def init_params(wires, n_layers):
    n_qubits = len(wires)
    return np.random.uniform(low=-np.pi, high=np.pi, size=(n_layers * n_qubits, 3))


if __name__ == "__main__":
    wires = range(3)
    dev = qml.device("default.qubit", wires=wires)

    @qml.qnode(dev)
    def my_circuit(params, wires):
        circuit(params, wires)
        return qml.expval(qml.PauliZ(0))    

    n_layers = 2
    params = init_params(dev.wires, n_layers)
    
    drawer = qml.draw(my_circuit)
    print(drawer(params=params, wires=wires))
