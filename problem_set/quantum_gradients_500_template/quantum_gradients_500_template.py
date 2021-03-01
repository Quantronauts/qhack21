#! /usr/bin/python3
import sys
import pennylane as qml
from pennylane import numpy as np

# DO NOT MODIFY any of these parameters
a = 0.7
b = -0.3
dev = qml.device("default.qubit", wires=3)


def natural_gradient(params):
    """Calculate the natural gradient of the qnode() cost function.

    The code you write for this challenge should be completely contained within this function
    between the # QHACK # comment markers.

    You should evaluate the metric tensor and the gradient of the QNode, and then combine these
    together using the natural gradient definition. The natural gradient should be returned as a
    NumPy array.

    The metric tensor should be evaluated using the equation provided in the problem text. Hint:
    you will need to define a new QNode that returns the quantum state before measurement.

    Args:
        params (np.ndarray): Input parameters, of dimension 6

    Returns:
        np.ndarray: The natural gradient evaluated at the input parameters, of dimension 6
    """

    #natural_grad = np.zeros(6)

    # QHACK #

    gradient = np.zeros([6], dtype=np.float64)

    # gradient
    s = 0.1
    for i in range(6):
        params[i] += s
        plus_s = qnode(params)
        params[i] -= 2*s
        minus_s = qnode(params)
        gradient[i] = (plus_s - minus_s) / (2*np.sin(s))
        params[i] += s

    # Fubini-Study metric
    @qml.qnode(dev)
    def my_qnode(params):
        variational_circuit(params)
        return qml.state()

    s = np.pi/2

    base_state = my_qnode(params)
    conj_base_state = np.conj(base_state)

    F = np.zeros([6, 6], dtype=np.float64)

    for i in range(6):
        for j in range(6):
            params[i] += s
            params[j] += s
            plusplus_state = my_qnode(params)
            pp = np.abs(np.dot(conj_base_state, plusplus_state)) ** 2
            params[j] -= 2*s
            plusminus_state = my_qnode(params)
            pm = np.abs(np.dot(conj_base_state, plusminus_state)) ** 2
            params[i] -= 2*s
            params[j] += 2*s
            minusplus_state = my_qnode(params)
            mp = np.abs(np.dot(conj_base_state, minusplus_state)) ** 2
            params[j] -= 2*s
            minusminus_state = my_qnode(params)
            mm = np.abs(np.dot(conj_base_state, minusminus_state)) ** 2
            F[i,j] = (-pp + pm + mp - mm) / 8
            params[i] += s
            params[j] += s

    #print(np.round(qml.metric_tensor(qnode)(params), 8))
    #print(F)

    natural_grad = np.matmul(np.linalg.inv(F), gradient)

    # QHACK #

    return natural_grad


def non_parametrized_layer():
    """A layer of fixed quantum gates.

    # DO NOT MODIFY anything in this function! It is used to judge your solution.
    """
    qml.RX(a, wires=0)
    qml.RX(b, wires=1)
    qml.RX(a, wires=1)
    qml.CNOT(wires=[0, 1])
    qml.CNOT(wires=[1, 2])
    qml.RZ(a, wires=0)
    qml.Hadamard(wires=1)
    qml.CNOT(wires=[0, 1])
    qml.RZ(b, wires=1)
    qml.Hadamard(wires=0)


def variational_circuit(params):
    """A layered variational circuit composed of two parametrized layers of single qubit rotations
    interleaved with non-parameterized layers of fixed quantum gates specified by
    ``non_parametrized_layer``.

    The first parametrized layer uses the first three parameters of ``params``, while the second
    layer uses the final three parameters.

    # DO NOT MODIFY anything in this function! It is used to judge your solution.
    """
    non_parametrized_layer()
    qml.RX(params[0], wires=0)
    qml.RY(params[1], wires=1)
    qml.RZ(params[2], wires=2)
    non_parametrized_layer()
    qml.RX(params[3], wires=0)
    qml.RY(params[4], wires=1)
    qml.RZ(params[5], wires=2)


@qml.qnode(dev)
def qnode(params):
    """A PennyLane QNode that pairs the variational_circuit with an expectation value
    measurement.

    # DO NOT MODIFY anything in this function! It is used to judge your solution.
    """
    variational_circuit(params)
    return qml.expval(qml.PauliX(1))


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block

    # Load and process inputs
    params = sys.stdin.read()
    params = params.split(",")
    params = np.array(params, float)

    updated_params = natural_gradient(params)

    print(*updated_params, sep=",")
