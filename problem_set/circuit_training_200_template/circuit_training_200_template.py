#! /usr/bin/python3
import json
import sys
import networkx as nx
import numpy as np
import pennylane as qml


# DO NOT MODIFY any of these parameters
NODES = 6
N_LAYERS = 10


def find_max_independent_set(graph, params):
    """Find the maximum independent set of an input graph given some optimized QAOA parameters.

    The code you write for this challenge should be completely contained within this function
    between the # QHACK # comment markers. You should create a device, set up the QAOA ansatz circuit
    and measure the probabilities of that circuit using the given optimized parameters. Your next
    step will be to analyze the probabilities and determine the maximum independent set of the
    graph. Return the maximum independent set as an ordered list of nodes.

    Args:
        graph (nx.Graph): A NetworkX graph
        params (np.ndarray): Optimized QAOA parameters of shape (2, 10)

    Returns:
        list[int]: the maximum independent set, specified as a list of nodes in ascending order
    """

    max_ind_set = []

    # QHACK #
    wires = range(NODES)
    depth = N_LAYERS
    dev = qml.device('default.qubit', wires=wires)

    cost_h, mixer_h = qml.qaoa.max_independent_set(graph, constrained=True)

    def qaoa_layer(gamma, alpha):
        qml.qaoa.cost_layer(gamma, cost_h)
        qml.qaoa.mixer_layer(alpha, mixer_h)

    def circuit(params, **kwargs):
        qml.layer(qaoa_layer, depth, params[0], params[1])

    cost_function = qml.ExpvalCost(circuit, cost_h, dev)

    optimizer = qml.GradientDescentOptimizer()
    steps = 2

    for i in range(steps):
        params = optimizer.step(cost_function, params)

    @qml.qnode(dev)
    def probability_circuit(gamma, alpha):
        circuit([gamma, alpha])
        return qml.probs(wires=wires)

    probs = probability_circuit(params[0], params[1])

    result = probs.tolist()
    data = result.index(max(result))
    binary = '{0:06b}'.format(data)
    binary_str = str(binary)

    compteur = 0
    while compteur < 6:
        if binary_str[compteur] == "1":
            max_ind_set.append(compteur)
        compteur += 1

    max_ind_set = list(dict.fromkeys(max_ind_set))
    # QHACK #

    return max_ind_set


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block

    # Load and process input
    graph_string = sys.stdin.read()
    graph_data = json.loads(graph_string)

    params = np.array(graph_data.pop("params"))
    graph = nx.json_graph.adjacency_graph(graph_data)

    max_independent_set = find_max_independent_set(graph, params)

    print(max_independent_set)
