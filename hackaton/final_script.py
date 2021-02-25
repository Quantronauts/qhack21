#############################################################################################
# This script is to launch the entire program on our data set and glue every module together
#############################################################################################

import pennylane as qml
from pennylane import numpy as np
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

print("##################################################################\n"
      "# TRAINING")
"""
    Variables :
    data_training : the xy // xyz data for only 1 qubit
    label_training : the label for only 1 qubit
    n_layers : deep level
    weights : the angle for the classifier
    wires : number of qubits for the classifier
    shots : number of shots
    error_rate : number of error
    circuit_run : number of circuit loop
    optimizer_run : number of optimizer iteration
"""

dev = qml.device('default.qubit', wires=1, shots=1)
n_qubits = len(dev.wires)
n_layers = 2
weights = np.random.uniform(low=-np.pi, high=np.pi, size=(n_layers * n_qubits, 3))
opt = qml.GradientDescentOptimizer(stepsize=0.1)

# Stats var
error_rate = 0
circuit_run = 0
optimizer_run = 0

if csv_training.shape[1] == 3:
    prediction = [[], [], []]
elif csv_training.shape[1] == 4:
    prediction = [[], [], [], []]
else:
    print("Only two or three angles are allowed in training data set")

# for i in range(len(csv_training[0])):
for i in range(1000):
    if csv_training.shape[1] == 3:
        data_training = [csv_training[0][i], csv_training[1][i]]
        label_training = csv_training[2][i]
    elif csv_training.shape[1] == 4:
        data_training = [csv_training[0][i], csv_training[1][i], csv_training[2][i]]
        label_training = csv_training[3][i]
    else:
        print("Only two or three angles are allowed in training data set")


    @qml.qnode(dev)
    def entire_circuit(datas, params):
        sensor(datas, wires=[0])
        classifier(params, wires=dev.wires)
        return qml.sample(qml.PauliZ(0))


    def count_prob(result):
        prob_qat = 0
        prob_doq = 0
        if dev.shots > 1:
            for i in result:
                if i == 1:
                    prob_qat += 1
                else:
                    prob_doq += 1
            if prob_qat > prob_doq:
                prob = 1
            elif prob_qat == prob_doq:
                prob = 0
            else:
                prob = -1
        else:
            prob = result
        return prob


    @qml.qnode(dev)
    def optimizer_circuit(params):
        classifier(params, wires=dev.wires)
        return qml.expval(qml.PauliZ(0))


    def cost(x):
        return optimizer_circuit(x)


    # Run a first time the entire circuit
    result = entire_circuit(data_training, weights)
    prob = count_prob(result)
    circuit_run += 1

    # Optimize th weights is the output is bad
    if (prob == -1 and label_training != "doq") or (prob == 1 and label_training != "qat"):
        steps = 100
        for i in range(steps):
            weights = opt.step(cost, weights)
            result = entire_circuit(data_training, weights)
            prob = count_prob(result)
            circuit_run += 1
            optimizer_run += 1

            # if (i + 1) % 10 == 0:
            # print("Cost after step {:5d}: {: .7f} -> {}".format(i + 1, prob, label_training))

            if (prob == -1 and label_training == "doq") or (prob == 1 and label_training == "qat"):
                break

    # Calculate error rate
    if (prob == -1 and label_training != "doq") or (prob == 1 and label_training != "qat"):
        error_rate += 1

    # Graph and check error
    prediction[0].append(data_training[0])
    prediction[1].append(data_training[1])
    if csv_training.shape[1] == 3:
        prediction[2].append(prob)
    else:
        prediction[2].append(data_training[2])
        prediction[3].append(prob)

print("\nTraining done !")

if len(prediction) == 3:
    plt.scatter(prediction[1], prediction[0], c=prediction[2], cmap="coolwarm")
    plt.plot([0,2*np.pi], [np.pi/2, np.pi/2], linestyle='--', c='#000000')
    plt.colorbar()
elif len(prediction) == 4:
    fig = plt.figure().gca(projection='3d')
    fig.scatter(prediction[0], prediction[1], prediction[2], c=prediction[3], cmap="coolwarm")
plt.show()

print("Error rate : {} %".format(round(error_rate / len(prediction[0]) * 100, 3)))
print("\nRessources used : \nCircuit run : {}, Optimize run : {}, Deph {}, Shot(s) : {}, Qubit(s) : {}"
      .format(circuit_run, optimizer_run, n_layers, dev.shots, n_qubits))

print("##################################################################\n"
      "# Testing")
"""
    Variables :
    data_training : the xy // xyz data for only 1 qubit
    label_training : the label for only 1 qubit
    n_layers : deep level
    weights : the angle for the classifier
"""

dev = qml.device('default.qubit', wires=1, shots=1)

if csv_testing.shape[1] == 2:
    prediction = [[], [], []]
else:
    prediction = [[], [], [], []]

for i in range(len(csv_testing[0])):
    # for i in range(20):
    if csv_testing.shape[1] == 2:
        data_testing = [csv_testing[0][i], csv_testing[1][i]]
    else:
        data_testing = [csv_testing[0][i], csv_testing[1][i], csv_testing[2][i]]


    @qml.qnode(dev)
    def entire_circuit(datas, params):
        sensor(datas, wires=[0])
        classifier(params, wires=dev.wires)
        return qml.sample(qml.PauliZ(0))


    # Run the circuit
    result = entire_circuit(data_testing, weights)
    prob = result

    # Graph and check error
    prediction[0].append(data_testing[0])
    prediction[1].append(data_testing[1])
    if csv_testing.shape[1] == 2:
        prediction[2].append(prob)
    else:
        prediction[2].append(data_testing[2])
        prediction[3].append(prob)

print("\nTesting done !")

if len(prediction) == 3:
    plt.scatter(prediction[1], prediction[0], c=prediction[2], cmap="coolwarm")
    plt.plot([0,2*np.pi], [np.pi/2, np.pi/2], linestyle='--', c='#000000')
    plt.colorbar()
else:
    fig = plt.figure().gca(projection='3d')
    fig.scatter(prediction[0], prediction[1], prediction[2], c=prediction[3], cmap="coolwarm")
plt.show()
