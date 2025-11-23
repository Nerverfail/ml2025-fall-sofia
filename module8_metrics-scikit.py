
import numpy as np
from data_handler import data_handler
from sklearn.metrics import precision_score, recall_score

class MetricsCalculator:
    def __init__(self, data_handler_instance):
        self.y_true = data_handler_instance.y_true
        self.y_pred = data_handler_instance.y_pred

    def compute_precision(self):
        return np.round(precision_score(self.y_true, self.y_pred), decimals=2)

    def compute_recall(self):
        return np.round(recall_score(self.y_true, self.y_pred), decimals=2)


def main():
    data_handler_instance = data_handler()
    data_handler_instance.initialize_N()
    data_handler_instance.initialize_data_points_module_8()
    calculator = MetricsCalculator(data_handler_instance)

    precision = calculator.compute_precision()
    recall = calculator.compute_recall()

    print(f"Precision: {precision}")
    print(f"Recall: {recall}")


if __name__ == "__main__":
    main()