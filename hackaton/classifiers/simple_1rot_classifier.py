#################################
# Simple one rotation classifier
#################################

import pennylane as qml


@qml.template
def classifier(params, wires):
    # qml.RZ(params, wires=wires[0])
    # qml.RY(params, wires=wires[0])
    n_qubits = len(wires)
    n_rotations = len(params)
    n_layers = n_rotations // n_qubits

    if n_rotations % n_qubits != 0:
        raise Exception("Last layer is incomplete, not all qubits are rotated")

    # Alternating layers of unitary rotations on every qubit followed by a
    # ring cascade of CNOTs.
    for layer_idx in range(n_layers):
        layer_params = params[layer_idx * n_qubits: layer_idx * n_qubits + n_qubits, :]
        qml.broadcast(qml.Rot, wires, pattern="single", parameters=layer_params)
        if n_qubits > 1:
            qml.broadcast(qml.CNOT, wires, pattern="ring")
