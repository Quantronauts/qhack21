#############################################################################################
# This script is to launch the entire program on our data set and glue every module together
#############################################################################################

from datas import *
from sensors import *
from classifiers import *
from combine import *
from training import *
from testing import *
from graphs import *

import sys
import pennylane as qml
from pennylane import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from qutip import *
from qutip.ipynbtools import plot_animation
