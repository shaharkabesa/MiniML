import numpy as np
import enum
# A Neuron classes that uses grediant and matrices to accomplish research into colors
class neuronNumpy:
    # Defining the neuron at the start of intatation 
    def __init__(self, matrix_value, matrix_weight , matrix_target, learning_rate, model_name):
        self.matrix_value = matrix_value
        self.matrix_weight = matrix_weight
        self.matrix_target = matrix_target
        self.learning_rate = learning_rate
        self.model_name = model_name

    class colorEnum(enum.Enum):
        red = 0
        green = 1
        blue = 2


    #Seperated function to calculate the prediction
    def calculatePrediction(self):
        # predicition is our matrix input multiplied by weights 
        prediction = self.matrix_value @ self.matrix_weight
        print(f"Current prediction {prediction}\n")
        return prediction
    # Seperated error function to seperate function measuring how off are we from target 
    def calculateError(self, prediction):
        # we used the prediction we minus it by our target to see the margin of error and fix the direction 
        error = prediction - self.matrix_target
        print(f"Error margin: {error}\n")
        return error
    # Here we do the recalculation of weight after collecting information each cycle    
    def calculateWeight(self, error):
        grediant = self.matrix_value.T @ error 
        self.matrix_weight = self.matrix_weight - (grediant * self.learning_rate)
        print(f"New weight: {self.matrix_weight}")
    # This is the starting function to start research 
    def startResearchEpoch(self, trainingLoops):
        
        # i am using fixed loop like in real life ml model training
        for epoch in range(trainingLoops):
            #first step is prediction calulation
            prediction = self.calculatePrediction()
            #second is error gathering
            error = self.calculateError(prediction)
            #final step is recalculating our weight matrix
            self.calculateWeight(error)
        
        #display if research was successful
        self.results(self.matrix_weight)
        #save data of model
        self.saveData()
        
    # a function used to check if data is indeed correct at the end of research 
    def results(self,last_weight):
        final_answer = self.matrix_value @ last_weight
        if np.allclose(final_answer ,self.matrix_target):
            print("Found correct pattern")
            self.determineColor(final_answer)
        else :
            print("Research failed")
    
    #function to load data by the name of the model you give it at the start
    def loadData(self):
        self.matrix_weight =  np.load(f"./models/{self.model_name}.npy")

    #function to save data by the name of the model you give it at the start
    def saveData(self):
        np.save(f"./models/{self.model_name}", self.matrix_weight)

    def determineColor(self, final_answer):
        winning_score = np.max(final_answer)
        score_index = np.where(winning_score == final_answer[0])
        winning_index = score_index[0][0]
        color = self.colorEnum(winning_index).name

        print(f"The color is {color}")
