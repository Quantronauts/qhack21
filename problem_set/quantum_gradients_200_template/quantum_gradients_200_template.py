#! /usr/bin/python3

import sys
import pennylane as qml
import numpy as np


def gradient_200(weights, dev):
    r"""This function must compute the gradient *and* the Hessian of the variational
    circuit using the parameter-shift rule, using exactly 51 device executions.
    The code you write for this challenge should be completely contained within
    this function between the # QHACK # comment markers.

    Args:
        weights (array): An array of floating-point numbers with size (5,).
        dev (Device): a PennyLane device for quantum circuit execution.

    Returns:
        tuple[array, array]: This function returns a tuple (gradient, hessian).

            * gradient is a real NumPy array of size (5,).

            * hessian is a real NumPy array of size (5, 5).
    """

    @qml.qnode(dev, interface=None)
    def circuit(w):
        for i in range(3):
            qml.RX(w[i], wires=i)

        qml.CNOT(wires=[0, 1])
        qml.CNOT(wires=[1, 2])
        qml.CNOT(wires=[2, 0])

        qml.RY(w[3], wires=1)

        qml.CNOT(wires=[0, 1])
        qml.CNOT(wires=[1, 2])
        qml.CNOT(wires=[2, 0])

        qml.RX(w[4], wires=2)

        return qml.expval(qml.PauliZ(0) @ qml.PauliZ(2))

    gradient = np.zeros([5], dtype=np.float64)
    hessian = np.zeros([5, 5], dtype=np.float64)

    # QHACK #
    s = np.pi/2
    
    exp_vals_plus = np.zeros([5], dtype=np.float64)
    exp_vals_minus = np.zeros([5], dtype=np.float64)

    exp_val_zero = circuit(weights)

    # gradient
    for i in range(5):
        weights[i] += s
        plus_s = circuit(weights)
        exp_vals_plus[i] = plus_s
        weights[i] -= 2*s
        minus_s = circuit(weights)
        exp_vals_minus[i] = minus_s
        gradient[i] = (plus_s - minus_s) / (2*np.sin(s))
        weights[i] += s

        # tricky
        #if i == 2 or i == 4:
        #    weights[i] += s
        #    plus_s = circuit(weights)
        #    gradient[i] = plus_s
        #    weights[i] -= s
        #else:
        #    weights[i] += s
        #    plus_s = circuit(weights)
        #    weights[i] -= 2*s
        #    minus_s = circuit(weights)
        #    gradient[i] = (plus_s - minus_s) / (2*np.sin(s))
        #    weights[i] += s

    # Hessian
    #for i in range(5):
    #    for j in range(5):
    #        weights[i] += s
    #        weights[j] += s
    #        plusplus = circuit(weights)
    #        weights[j] -= 2*s
    #        plusminus = circuit(weights)
    #        weights[i] -= 2*s
    #        weights[j] += 2*s
    #        minusplus = circuit(weights)
    #        weights[j] -= 2*s
    #        minusminus = circuit(weights)
    #        hessian[i,j] = (plusplus - minusplus - plusminus + minusminus) / (4*np.sin(s)*np.sin(s))
    #        weights[i] += s
    #        weights[j] += s

    for i in range(0,4):
        for j in range(i+1,5):
            weights[i] += s
            weights[j] += s
            plusplus = circuit(weights)
            weights[j] -= 2*s
            plusminus = circuit(weights)
            weights[i] -= 2*s
            weights[j] += 2*s
            minusplus = circuit(weights)
            weights[j] -= 2*s
            minusminus = circuit(weights)
            hessian[i,j] = (plusplus - minusplus - plusminus + minusminus) / (4*np.sin(s)*np.sin(s))
            hessian[j,i] = hessian[i,j]
            weights[i] += s
            weights[j] += s

    for i in range(0,5):
        hessian[i,i] = (exp_vals_plus[i] - 2*exp_val_zero + exp_vals_minus[i]) / 2

    # QHACK #

    return gradient, hessian, circuit.diff_options["method"]


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    weights = sys.stdin.read()
    weights = weights.split(",")
    weights = np.array(weights, float)

    dev = qml.device("default.qubit", wires=3)
    gradient, hessian, diff_method = gradient_200(weights, dev)

    print(
        *np.round(gradient, 10),
        *np.round(hessian.flatten(), 10),
        dev.num_executions,
        diff_method,
        sep=","
    )
