# The program asks the user for input N (positive integer) and reads it.
# Then the program asks the user to provide N (x, y) pairs (one by one) and reads all of them: first: x value, then: y value for every pair one by one. X is treated as the input feature and Y is treated as the class label. X is a real number, Y is a non-negative integer.
# This set of pairs constitutes the training set TrainS = {(x, y)_i}, i = 1..N.
# Then the program asks the user for input M (positive integer) and reads it.
# Then the program asks the user to provide M (x, y) pairs (one by one) and reads all of them: first: x value, then: y value for every pair one by one. X is treated as the input feature and Y is treated as the class label. X is a real number, Y is a non-negative integer.
# This set of pairs constitutes the test set TestS = {(x, y)_i}, i = 1..M.
# In the end, the program outputs: the best k for the kNN Classification method and the corresponding test accuracy. kNN Classifier should be trained on pairs from TrainS, tested on x values from TestS and compared with y values from TestS.
# The basic functionality of data processing (data initialization, data insertion), should be done using Numpy library while the computation (ML) part should be done using Scikit-learn library as much as possible (note: you can combine with what you've done from the previous tasks). 
# Note: you can try the following range of k: 1 <= k <= 10.

import numpy as np
from data_handler import data_handler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

class KNNGridSearch:
    def __init__(self, data_handler_instance):
        self.X_train = data_handler_instance.X_train.reshape(-1, 1)
        self.y_train = data_handler_instance.y_train
        self.X_test = data_handler_instance.X_test.reshape(-1, 1)
        self.y_test = data_handler_instance.y_test

        print(f"Training data points (X_train, y_train):")
        for x, y in zip(self.X_train, self.y_train):
            print(f"({x[0]}, {y})")
        print(f"Test data points (X_test, y_test):")
        for x, y in zip(self.X_test, self.y_test):
            print(f"({x[0]}, {y})")

    def perform_grid_search(self):
        # Tryiing k values from 1 to 10
        params = {'n_neighbors': list(range(1, 11)),
         'weights': ['uniform', 'distance'],
         'leaf_size': [5, 10, 15]}
        knn = KNeighborsClassifier()
        grid_search = GridSearchCV(knn, param_grid=params, scoring='accuracy', cv=5)
        grid_search.fit(self.X_train, self.y_train)
        print(f"Best cross-validation accuracy: {np.round(grid_search.best_score_, decimals=2)}")
        return grid_search.best_params_
    
    def evaluate_best_model(self, best_params):
        knn_best = KNeighborsClassifier(n_neighbors=best_params['n_neighbors'],
                                        weights=best_params['weights'],
                                        leaf_size=best_params['leaf_size'])
        knn_best.fit(self.X_train, self.y_train)
        y_pred = knn_best.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        return np.round(accuracy, decimals=2)

def main():
    data_handler_instance = data_handler()
    data_handler_instance.initialize_N()
    data_handler_instance.initialize_M()
    data_handler_instance.initialize_data_points_module_9()
    knn_grid_search = KNNGridSearch(data_handler_instance)
    best_params = knn_grid_search.perform_grid_search()
    print(f"Best k: {best_params['n_neighbors']}")
    print(f"Best weights: {best_params['weights']}")
    print(f"Best leaf size: {best_params['leaf_size']}")

    test_accuracy = knn_grid_search.evaluate_best_model(best_params)
    print(f"Test Accuracy: {test_accuracy}")

if __name__ == "__main__":
    main()