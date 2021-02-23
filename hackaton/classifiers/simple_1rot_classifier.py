#################################
# Simple one rotation classifier
#################################

import pennylane as qml


@qml.template
def classifier(params, wires):
    qml.Rot(params, wires=wires[0])
