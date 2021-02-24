#! /usr/bin/python3

import pennylane as qml
from pennylane import numpy as np

import sys
from os import path

sys.path.append(path.abspath('../sensors'))
sys.path.append(path.abspath('../classifiers'))

import n_hemispheres as hemi
import rot_cnot_processing as rcnp


dev_expval = qml.device("default.qubit", wires=range(3), shots=30)
print(dev_expval)

dev_1shot = qml.device("default.qubit", wires=range(3), shots=1)
print(dev_1shot)


@qml.qnode(dev_expval)
def combined_expval(weights, x, wires):
    hemi.circuit(x, wires)
    rcnp.circuit(weights, wires)

    # create PauliZ x ... x PauliZ
    op = qml.PauliZ(0)
    for i in range(1, len(wires)):
        op = op @ qml.PauliZ(i)

    return qml.expval(op)


@qml.qnode(dev_1shot)
def combined_1shot(weights, x, wires):
    hemi.circuit(x, wires)
    rcnp.circuit(weights, wires)

    # create PauliZ x ... x PauliZ
    op = qml.PauliZ(0)
    for i in range(1, len(wires)):
        op = op @ qml.PauliZ(i)

    return qml.sample(op)


if __name__ == "__main__":
    x = hemi.init_params(dev_expval.wires)
    weights = rcnp.init_params(dev_expval.wires, 2)
    
    drawer = qml.draw(combined_expval)
    print(drawer(weights=weights, x=x, wires=dev_expval.wires))

    # expval classifier output for sensor data x (weights were not optimized)
    print(combined_expval(weights=weights, x=x, wires=dev_expval.wires))

    # 1shot classifier output for sensor data x (weights were not optimized)
    print(combined_1shot(weights=weights, x=x, wires=dev_1shot.wires))
