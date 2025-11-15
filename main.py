import numpy as np


from neuron_numpy import neuronNumpy
r = 255/255
g = 0/255
b = 0/255

# Defining our input matrix 
x = np.array([[r,g , b]], dtype=float)
# defining our target matrix
b = np.array([[1,0,0]], dtype=float)
# defining our weights matrix
weights = np.array([[0.0,0.0,0.0],
                    [0.0,0.0,0.0],
                    [0.0,0.0,0.0],
                    ], dtype=float)
# intating a new research using the library i made for the neuron
newResearch = neuronNumpy(x, weights, b, 0.05, "color_recognizer_3")
# loading data inorder  to not keep over learning
newResearch.loadData()
newResearch.startResearchEpoch(1)
