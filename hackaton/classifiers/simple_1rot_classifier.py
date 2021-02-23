#################################
# Simple one rotation classifier
#################################

import pennylane as qml


@qml.template
def classifier(params, wires):
    qml.Rot(*params[0], wires=wires[0])
