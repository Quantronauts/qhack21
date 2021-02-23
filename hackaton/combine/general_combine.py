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
def circuit(datas, params):
    qml.inv(sensor(datas, wires=[0]))
    qml.inv(classifier(params, wires=[0]))

