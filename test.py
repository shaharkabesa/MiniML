import numpy as np

from libs.neunmpyv2 import neumpyv2



redg = np.array([[0.50,0.50,0.0]])
redgtarget = np.array([[0.002, 0.022, 0.0]])

inputarray = np.array([[0.2,0.5,0.3]])
targetarray = np.array([[0, 0.55, 0.75]])


newp = neumpyv2(redgtarget, redg, 0.10, "model002", "colors")

def choices():
    choice = input("Hello welcome to the simple CLI for my ML Library\n Pick what you want to do: \n 1: Recognize \n 2: Research \n 3: Quit program\n")        
    choice = int(choice)
    
    if choice == 1:
            newp.checkAnswerDB()
            
    elif choice == 2:
            researchname = input("\n Please write researchname: ")
            newp.startResearch(10000, researchname)
            
    elif choice == 3:
            quit()



newp.createLayers(2)
newp.loadData()
choices()