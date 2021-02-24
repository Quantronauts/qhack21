#############################################################################################
# This script is to launch the entire program on our data set and glue every module together
#############################################################################################

import pennylane as qml
import numpy as np
import pandas as pd
import sys

from sensors.u2_u3_sensor import sensor
from classifiers.simple_1rot_classifier import classifier
#from combine.general_combine import combine


csv_training = pd.read_csv('datas/training_datas_xz.csv', header=None)
csv_testing = pd.read_csv('datas/testing_datas_xz.csv', header=None)


##################################################################
# Training phase

print("##################################################################\n"
      "# TRAINING")
for i in range(len(csv_training[0])):
    if csv_training.shape[1] == 3:
        data_training = [csv_training[0][i], csv_training[1][i]]
        label_training = csv_training[2][i]
    else:
        data_training = [csv_training[0][i], csv_training[1][i], csv_training[2][i]]
        label_training = csv_training[3][i]

    dev = qml.device('default.qubit', wires=1)


    @qml.qnode(dev)
    def circuit(datas, params):
        sensor(datas, wires=[0])
        classifier(params, wires=[0])
        return qml.expval(qml.PauliZ(0))


    theta = [3.14]
    result = circuit(data_training, theta)
    prob = result
    print(prob)


##################################################################
# Testing phase

print("##################################################################\n"
      "# TESTING")
for i in range(len(csv_training[0])):
    if csv_training.shape[1] == 3:
        data_training = [csv_training[0][i], csv_training[1][i]]
        label_training = csv_training[2][i]
    else:
        data_training = [csv_training[0][i], csv_training[1][i], csv_training[2][i]]
        label_training = csv_training[3][i]

    dev = qml.device('default.qubit', wires=1)


    @qml.qnode(dev)
    def circuit(datas, params):
        sensor(datas, wires=[0])
        classifier(params, wires=[0])
        return qml.expval(qml.PauliZ(0))


    theta = [3.14]
    result = circuit(data_training, theta)
    prob = result
    print(prob)
