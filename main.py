import numpy as np
from libs.neumpy import neumpy

from libs.neuron_numpy import neuronNumpy
r = 0/255
g = 255/255
b = 0/255

# Defining our input matrix 
x = np.array([[r,g , b]], dtype=float)
# defining our target matrix
b = np.array([[0,1,0]], dtype=float)
# defining our weights matrix
weights = np.array([[0.0,0.0,0.0],
                    [0.0,0.0,0.0],
                    [0.0,0.0,0.0],
                    ], dtype=float)
# intating a new research using the library i made for the neuron
# newResearch = neuronNumpy(x, weights, b, 0.05, "color_recognizer_4")
# # loading data inorder  to not keep over learning
# newResearch.loadData()
# newResearch.startResearchEpoch(1000)

newResearch = neumpy(x,weights,b,0.05,"Neumpy1")
newResearch.startResearch(1000)