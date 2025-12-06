import numpy as np

from neunmpyv2 import neumpyv2 

inputarray = np.array([[0.2,0.5,0.3]])
targetarray = np.array([[0, 0.25, 0.75]])
newp = neumpyv2(targetarray, inputarray, 0.05)

newp.createLayers(4)

newp.startResearch(100000)