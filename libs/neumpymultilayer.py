import numpy as np

class neumpymultilayer:

    def __init__(self, x_input, y_target, w1_matrix,    learning_rate, model_name):
        self.x_input = x_input
        self.y_target = y_target
        self.w1_matrix = w1_matrix
        self.w2_matrix = np.random.rand(3,3) * 0.1
        self.learning_rate = learning_rate
        self.model_name = model_name
        self.z_matrix = np.array([])
        self.h_matrix = np.array([])
        self.p_matrix = np.array([])
        self.e_matrix = np.array([])
        self.epoch = 0

    def prediction_Stage(self):
        self.z_matrix = self.x_input @ self.w1_matrix
        print(f"Z_Matrix: {self.z_matrix}\n")
        self.h_matrix = self.relu(self.z_matrix)
        print(f"H_Matrix: {self.h_matrix}\n")
        self.p_matrix = self.h_matrix @ self.w2_matrix
        print(f"P_Matrix: {self.p_matrix}\n")

    def error_Stage(self):
        self.e_matrix = self.p_matrix - self.y_target
        print(f"Error matrix: {self.e_matrix}")
    def gradient_Stage(self):

        gs2 = self.h_matrix.T @ self.e_matrix
        self.w2_matrix = self.w2_matrix - (gs2 * self.learning_rate)
        E_signal = self.e_matrix @ self.w2_matrix.T
        E_hidden = E_signal * self.dervative_relu(self.z_matrix)
        gs1 = self.x_input.T @ E_hidden
        self.w1_matrix = self.w1_matrix - (gs1 * self.learning_rate)

    def startResearch(self, learning_cycles):
        cycle = 1
        for self.epoch in range(learning_cycles):
            print(f"----------------Cycle Start : {cycle} ------------------")
            self.prediction_Stage()
            self.error_Stage()
            self.gradient_Stage()
            print(f"Weight 1: {self.w1_matrix} \n Weight 2: {self.w2_matrix}\n")
            print(f"----------------Cycle End : {cycle} ------------------")
            cycle += 1
        self.saveData()
        result = self.p_matrix
        print(result)
        if(np.allclose(result, self.y_target)):
            print("Close enough")
    def relu(self, z):
        return np.maximum(0,z)
    
    def dervative_relu(self,z):
     return (z > 0) * 1.0
    
    
# 3x3 A *   B
    # Function to load matrix by name
    def loadData(self):
        self.w1_matrix =  np.load(f"./models/{self.model_name}w1.npy")
        self.w2_matrix =  np.load(f"./models/{self.model_name}w2.npy")
    #function to save data by the name of the model you give it at the start
    def saveData(self):
        np.save(f"./models/{self.model_name}w1", self.w1_matrix)
        np.save(f"./models/{self.model_name}w2", self.w2_matrix)
