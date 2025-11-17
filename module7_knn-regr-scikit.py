import numpy as np
# pulling data_handler from previous module out since the file name can't have hyphens if we want to import the module
from data_handler import data_handler
from sklearn.neighbors import KNeighborsRegressor


class KNNRegressorModule:
    def __init__(self, N, k, x_train, y_train):
        if k > N:
            raise ValueError("Error: k cannot be greater than N.")
        self.k = k
        self.x_train = x_train
        self.y_train = y_train
        self.model = KNeighborsRegressor(n_neighbors=self.k)
        self.model.fit(self.x_train, self.y_train)

    def predict(self, X):
        # X: array-like, sparse matrix of shape (n_queries, n_features) has to be 2-D array
        X_reshaped = np.array([[X]])
        return self.model.predict(X_reshaped)[0]

    def variance(self):
        return self.y_train.var()



def main():
    data_handler_instance = data_handler()
    N = data_handler_instance.get_N()
    k = data_handler_instance.get_k()
    data = data_handler_instance.get_data()
    print(data)
    # Error: Reshape your data either using array.reshape(-1, 1) if your data has a single feature or array.reshape(1, -1) if it contains a single sample.
    x_train = data[:, 0].reshape(-1, 1)
    y_train = data[:, 1]
    print(x_train)
    print(y_train)

    X = data_handler_instance.get_X()
        
    knn_regressor = KNNRegressorModule(N, k, x_train, y_train)
    Predication = knn_regressor.predict(X)
    print(f"Predicted Y value: {Predication}")
    print(f"Variance of labels in the training dataset: {knn_regressor.variance()}")


if __name__ == "__main__":    
    main()