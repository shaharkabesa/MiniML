import numpy as np
import chromadb



class neumpyv2:
    def __init__(self, target, input, learning_rate, name):
        self.weight_matrix = []
        self.target = target
        self.input = input
        self.input_memory = []
        self.prediction = 0
        self.error = 0
        self.learning_rate = learning_rate
        self.input_shape = self.input.shape
        self.grad = []
        self.hidden_error = []
        self.traning_complete = False
        self.cycles = 0
        self.name = name
        self.objectname = ""
        self.vectordb = chromadb.PersistentClient("./vecordb")
        self.collection = self.vectordb.get_or_create_collection(name="testcollection")
    def predictionStage(self):
        self.grad.clear()
        self.hidden_error.clear()
        self.input_memory.clear()
        
        self.input_memory.append(self.input)
        for i in range(len(self.weight_matrix)):
            self.predict(self.input_memory[i],self.weight_matrix[i])
        final_prediction = self.input_memory[-1]
        self.prediction = final_prediction
        print(f"Prediction : {final_prediction}\n")
        
        self.errorStage()



    def predict(self ,input, weight):
        z = input @ weight          # Linear step
        a = np.maximum(0, z)        # Activation (ReLU) step
        self.input_memory.append(a) # Store the ACTIVATED value

    def errorStage(self): 
        self.error = self.prediction - self.target
        
        
        print(f"Error: {self.error} \n")
        for i in range(len(self.weight_matrix) -1,-1,-1):
                
            self.gradientCalculation(self.input_memory[i], self.weight_matrix[i], self.error)
        self.weightsUpdate()

    def gradientCalculation(self, input_memory,weight, error):
        grad = input_memory.T @ error
        self.grad.append(grad)
        self.error = self.error @ weight.T
        print(grad, self.error)
        

    def weightsUpdate(self):
        self.grad.reverse()
        for i in range(len(self.weight_matrix) -1, -1 , -1):
                self.weight_matrix[i] = self.weight_matrix[i] - (self.grad[i] * self.learning_rate)

    def createLayers(self, amount): 
        for i in range(amount):
            new_matrix = np.random.uniform(-0.5, 0.5,(self.input_shape[1],self.input_shape[1]))

            self.addMatrix(new_matrix)
        print(f"Populated list of {amount} matrix succesfully\n")
        print(f"The dimension of each matrix\n rows: {self.weight_matrix[1].shape[1]} columns: {self.weight_matrix[1].shape[1]}")
        
    def addMatrix(self, matrix):
        self.weight_matrix.append(matrix)

    def startResearch(self, amount, objectname):
        self.loadData()
        self.objectname = objectname
        for i in range(amount):
            self.cycles += 1
            if self.traning_complete:
                break
            self.predictionStage()
            self.checkAnswer(self.prediction)
        

    def checkAnswer(self,final_predicition):
        result = np.allclose(final_predicition, self.target)
        if result:
            print(f"found target it took {self.cycles} cycles to reach")
            self.traning_complete = True
            self.saveData()


    def checkAnswerDB(self):
        self.predictionStage()
        match = self.collection.query(query_embeddings=self.prediction, n_results=1)
        print(match["metadatas"][0][0])

    def cleardata(self):
        self.grad.clear()
        self.hidden_error.clear()
        self.input_memory.clear()

    def saveData(self):
        np.save(f"models/{self.name}", self.weight_matrix)
        does_exist = self.collection.query(query_embeddings=self.target, n_results=1)
        print()
        closest_distance = does_exist["distances"][0][0]
        
        if closest_distance < 0.0004:
            print("already exists")
            print(does_exist["metadatas"][0][0])
        else:
            print("saved to db")
            self.collection.add(ids=f"{self.objectname}",embeddings=self.target, metadatas={
                "object_name": self.objectname 
            }, )

    def loadData(self):
      self.weight_matrix = np.load(f"models/{self.name}.npy")

    