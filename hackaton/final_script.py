#############################################################################################
# This script is to launch the entire program on our data set and glue every module together
#############################################################################################

import pennylane as qml
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

from sensors.u2_u3_sensor import sensor
from classifiers.simple_1rot_classifier import classifier

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
    n_layers : deep level
    weights : the angle for the classifier
"""

dev = qml.device('default.qubit', wires=1, shots=1)
n_qubits = len(dev.wires)
n_layers = 2
weights = np.random.uniform(low=-np.pi, high=np.pi, size=(n_layers * n_qubits, 3))

if csv_training.shape[1] == 3:
    prediction = [[], [], []]
else:
    prediction = [[], [], [], []]

# for i in range(len(csv_training[0])):
for i in range(20):
    if csv_training.shape[1] == 3:
        data_training = [csv_training[0][i], csv_training[1][i]]
        label_training = csv_training[2][i]
    else:
        data_training = [csv_training[0][i], csv_training[1][i], csv_training[2][i]]
        label_training = csv_training[3][i]


    @qml.qnode(dev)
    def circuit(datas, params):
        sensor(datas, wires=[0])
        classifier(params, wires=dev.wires)
        return qml.sample(qml.PauliZ(0))


    result = circuit(data_training, weights)
    prob = result

    # Graph and check error
    prediction[0].append(data_training[0])
    prediction[1].append(data_training[1])
    if csv_training.shape[1] == 3:
        prediction[2].append(prob)
        print("Data : {} ; {} = {}".format(data_training[0], data_training[1], prob))
    else:
        prediction[2].append(data_training[2])
        prediction[3].append(prob)
        print("Data : {} ; {} ; {} = {}".format(data_training[0], data_training[1], data_training[1], prob))

print("\nTraining done !")

if len(prediction) == 3:
    plt.scatter(prediction[1], prediction[0], c=prediction[2], cmap="coolwarm")
    plt.plot([0,2*np.pi], [np.pi/2, np.pi/2], linestyle='--', c='#000000')
    plt.colorbar()
else:
    fig = plt.figure().gca(projection='3d')
    fig.scatter(prediction[0], prediction[1], prediction[2], c=prediction[3], cmap="coolwarm")
plt.show()



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
