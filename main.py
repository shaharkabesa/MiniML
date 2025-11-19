import numpy as np
from libs.neumpy import neumpy

from libs.neuron_numpy import neuronNumpy
from libs.neumpymultilayer import neumpymultilayer
r = 255/255
g = 255/255
b = 0/255

# Defining our input matrix 
x = np.array([[r,g , b]], dtype=float)
# defining our target matrix
b = np.array([[r,g,b]], dtype=float)
# defining our weights matrix
weights = np.random.rand(3,3) * 0.1
# intating a new research using the library i made for the neuron
# newResearch = neuronNumpy(x, weights, b, 0.05, "color_recognizer_4")
# # loading data inorder  to not keep over learning
# newResearch.loadData()
# newResearch.startResearchEpoch(1000)

# newResearch = neumpy(x,weights,b,0.05,"Neumpy1")
# newResearch.startResearch(1000)
newResearch = neumpymultilayer(x,b,weights,0.005,"Newmodel")
newResearch.loadData()
newResearch.startResearch(1)