##########################################################################################
# This script to launch the entire program on our data set and glue every module together
##########################################################################################

from datas import *
from devices import *
from classifiers import *
from combine import *
from training import *
from testing import *
from graphs import *

import sys
import pennylane as qml
from pennylane import numpy as np
