##############################
# Combine sensor + classifier
##############################

import pennylane as qml
import sys
from os import path

sys.path.append(path.abspath('../sensors'))
sys.path.append(path.abspath('../classifiers'))

from u2_u3_sensor import sensor
from simple_1rot_classifier import classifier


@qml.template
def combine(datas, theta, wires):
    sensor(datas, wires=wires)
    classifier(theta, wires=wires)


##################################################################
# Testing

# dev = qml.device('default.qubit', wires=1)
#
#
# @qml.qnode(dev)
# def circuit(datas, params):
#     combine(datas, params, wires=[0])
#     return qml.probs(0)
#
#
# theta = [3.14]
# sensor = [3.14, 3.14, 0.12]
#
# result = circuit(sensor, theta)
# prob = result[0]
# print(prob)
