#############################################################################################
# This script is to launch the entire program on our data set and glue every module together
#############################################################################################

import pennylane as qml
import numpy as np
import pandas as pd
import sys

from sensors.u2_u3_sensor import sensor

# from classifiers.simple_1rot_classifier import classifier
# from combine.general_combine import combine


"""
   To use your dataset just change the csv file call 
"""
csv_training = pd.read_csv('datas/training_data_xz.csv', header=None)
csv_testing = pd.read_csv('datas/testing_data_xz.csv', header=None)

##################################################################
# Training phase

print("##################################################################\n"
      "# TRAINING")
"""
    Variables :
    data_training : the xy // xyz data for only 1 qubit
    label_training : the label for only 1 qubit
    theta : the angle for the classifier
"""

params = [np.pi/4]

#for i in range(len(csv_training[0])):
for i in range(20):
    if csv_training.shape[1] == 3:
        data_training = [csv_training[0][i], csv_training[1][i]]
        label_training = csv_training[2][i]
    else:
        data_training = [csv_training[0][i], csv_training[1][i], csv_training[2][i]]
        label_training = csv_training[3][i]

    dev = qml.device('default.qubit', wires=1, shots=3)


    @qml.qnode(dev)
    def circuit(datas, params):
        sensor(datas, wires=[0])
        for u in range(6):
            qml.RZ(params, wires=[0])
            qml.RY(params, wires=[0])
        return qml.sample(qml.PauliZ(0))

    result = circuit(data_training, params)
    prob = result
    print("Data : {} ; {} = {}".format(data_training[0], data_training[1], prob))



##################################################################
# Testing phase

# print("##################################################################\n"
#       "# TESTING")
# """
#     Variables :
#     data_testing : the xy // xyz data for only 1 qubit
#     theta : the angle for the classifier (given during the training phase)
# """
#
# for i in range(len(csv_testing[0])):
#     if csv_testing.shape[1] == 2:
#         data_testing = [csv_testing[0][i], csv_testing[1][i]]
#     else:
#         data_testing = [csv_testing[0][i], csv_testing[1][i], csv_testing[2][i]]
#
#     dev = qml.device('default.qubit', wires=1)
#
#
#     @qml.qnode(dev)
#     def circuit(datas, params):
#         sensor(datas, wires=[0])
#         classifier(params, wires=[0])
#         return qml.expval(qml.PauliZ(0))
#
#
#     result = circuit(data_testing, theta)
#     prob = result
#     print(prob)
