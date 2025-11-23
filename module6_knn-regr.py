import numpy as np

class KNNRegressor:
    def __init__(self, data_handler_instance):
        self.N = data_handler_instance.get_N()
        self.k = data_handler_instance.get_k()
        if self.k > self.N:
            raise ValueError("k cannot be greater than N.")
        self.data = data_handler_instance.get_data()

    def predict(self, x):
        # Calculate distances from the input x to all x in the dataset using manhattan distance(L1), since we are in 1D, L2 and L1 are the same
        distances = np.abs(self.data[:, 0] - x)
        
        # Get the k nearest neighbors' indices
        knn_indices = np.argsort(distances)[:self.k]
        print(f"Indices of the {self.k} nearest neighbors: {knn_indices}")

        y_values = self.data[:, 1]
        k_indices_y_values_mean = np.mean(y_values[knn_indices])

        return k_indices_y_values_mean

class data_handler:
    def __init__(self):
        self.N = None
        self.k = None
        self.data = None
        self.initialize_N()
        self.initialize_k()
        self.initialize_data_points()
    
    def initialize_N(self):
        while True:
            try:
                n = int(input("Enter a positive integer N: "))
                if n > 0:
                    self.N = n
                    return n
                else:
                    print("N must be a positive integer. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
    
    def initialize_k(self):
        while True:
            try:
                k = int(input("Enter a positive integer k: "))
                if k > 0:
                    self.k = k
                    return k
                else:
                    print("k must be a positive integer. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

    def initialize_data_points(self):
        self.data = np.zeros((self.N, 2))
        print("Please enter N data points (x, y):")
        for i in range(self.N):
            while True:
                try:
                    x = float(input(f"Enter x value for point {i+1}: "))
                    y = float(input(f"Enter y value for point {i+1}: "))
                    self.data[i] = [x, y]
                    break
                except ValueError:
                    print("Invalid input. Please enter real numbers for x and y.")

    def get_N(self):
        return self.N
    
    def get_k(self):
        return self.k
    
    def get_data(self):
        return self.data

    def get_X(self):
        while True:
            try:
                x = float(input("Enter the X value for prediction: "))
                return x
            except ValueError:
                print("Invalid input. Please enter a real number.")


def main():
    data_handler_instance = data_handler()
    data_handler_instance.initialize_N()
    data_handler_instance.initialize_k()
    data_handler_instance.initialize_data_points()
    knn_regressor = KNNRegressor(data_handler_instance)

    x_input = data_handler_instance.get_X()
    prediction = knn_regressor.predict(x_input)
    print(f"The predicted y value for x={x_input} is: {prediction}")



if __name__ == "__main__":
    main()