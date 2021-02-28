#!/usr/bin/env python
# coding: utf-8

# In[8]:


#################################################################################################

""""Sensor using the ArbitraryStatePreparations from @qml.templates
Implements an arbitrary state preparation on the specified wires.
An arbitrary state on n wires is parametrized by 2**n+1−2 independent real parameters. 
This templates uses Pauli word rotations to parametrize the unitary.

Parameters:
weights (array[float]) – The angles of the Pauli word rotations, needs to have length 2(n+1)−2 where n is the number of wires the template acts upon.

wires (Iterable or Wires) – Wires that the template acts on. Accepts an iterable of numbers or strings, or a Wires object.

Also check: https://pennylane.readthedocs.io/en/stable/code/api/pennylane.templates.state_preparations.ArbitraryStatePreparation.html"""

#################################################################################################

import pennylane as qml
#from pennylane import numpy as np
from pennylane.templates.state_preparations import ArbitraryStatePreparation


# In[9]:


def sensor(weights, wires):
    dev = qml.device("default.qubit", wires=wires)

    @qml.qnode(dev)
    
    def device(weights):
        for i in range (wires):
            qml.template.ArbitraryStatePreparation(weights, wires=i)
        return qml.probs(wires)

