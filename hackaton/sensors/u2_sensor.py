######################################
# Simple sensor using RX and RZ gates
######################################

import pennylane as qml


def sensor(datas):
    qml.RX(datas[0], wires=0)
    qml.RY(datas[1], wires=0)
    return qml.probs(0)


##############################################################################
# Testing

#dev = qml.device('default.qubit', wires=1)
#toto = [2.14, 3.14]
#circ = qml.QNode(sensor, dev)
#circ(toto)
#print(circ.draw())

