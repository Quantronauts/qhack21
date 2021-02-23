######################################
# Simple sensor using RX and RZ gates
######################################

import pennylane as qml


@qml.template
def sensor(datas, wires):
    qml.RX(datas[0], wires=wires[0])
    if len(datas) == 3:
        qml.RY(datas[1], wires=wires[0])
        qml.RZ(datas[2], wires=wires[0])
    else:
        qml.RZ(datas[1], wires=wires[0])
