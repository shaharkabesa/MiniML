import numpy as np
import enum


class neumpy:

    def __init__(self, x_input, w_matrix, y_target, learning_rate, model_name):
        self.x_input = x_input # our input
        self.w_matrix = w_matrix # our weight 1
        self.y_target = y_target # our target 
        self.learning_rate = learning_rate
        self.model_name = model_name
        self.epoch = 0


    class colorEnum(enum.Enum):
        red = 0
        green = 1
        blue = 2

    def prediction_stageY(self):
        P_Matrix = self.x_input @ self.w_matrix # prediction matrix
        return P_Matrix
    
    def error_StageE(self, P_Matrix):
        E_Matrix = P_Matrix - self.y_target
        return E_Matrix
    
    def gradient_StageJ(self, E_Matrix):
        J_Matrix = self.x_input.T @ E_Matrix
        return J_Matrix
    
    def weightRecalibrationStage(self, J_Matrix):
        self.w_matrix = self.w_matrix - (J_Matrix * self.learning_rate)
    
    def startResearch(self, trainingRange):
        for self.epoch in range(trainingRange):
            P_Matrix = self.prediction_stageY()
            E_Matrix = self.error_StageE(P_Matrix)
            J_Matrix = self.gradient_StageJ(E_Matrix)
            self.weightRecalibrationStage(J_Matrix)
            print(f"\nNew weight: {self.w_matrix}")
        self.results(self.w_matrix)
        #save data of model
        self.saveData()


    def results(self,last_weight):
        final_answer = self.x_input @ last_weight
        if np.allclose(final_answer ,self.y_target):
            print("Found correct pattern")
            self.determineColor(final_answer)
        else :
            print("Research failed")

    # Function to load matrix by name
    def loadData(self):
        self.w_matrix =  np.load(f"./models/{self.model_name}.npy")

    #function to save data by the name of the model you give it at the start
    def saveData(self):
        np.save(f"./models/{self.model_name}", self.w_matrix)

    def determineColor(self, final_answer):
        winning_score = np.max(final_answer)
        score_index = np.where(winning_score == final_answer[0])
        winning_index = score_index[0][0]
        color = self.colorEnum(winning_index).name

        print(f"The color is {color}")

    def relu(x):
        return np.maximum(0,x)