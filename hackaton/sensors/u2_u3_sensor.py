######################################
# Simple sensor using RX and RZ gates
######################################

import pennylane as qml


@qml.template
def sensor(datas, wires):
    qml.RX(datas[0], wires[0])
    if len(datas) == 3:
        qml.RY(datas[1], wires[0])
        qml.RZ(datas[2], wires[0])
    else:
        qml.RZ(datas[1], wires[0])
    #return qml.probs(0)


##############################################################################
# Testing

# dev = qml.device('default.qubit', wires=1)
# toto = [2.14, 3.14]
# circ = qml.QNode(sensor, dev)
# circ(toto)
# print(circ.draw())

