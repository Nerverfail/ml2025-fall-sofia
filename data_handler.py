import numpy as np


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