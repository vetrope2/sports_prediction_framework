from sklearn.base import BaseEstimator
from sklearn.model_selection import train_test_split
from mlflow_logger import log_mlflow_experiment


class Model():
    """
    A class representing a scikit-learn model.
    """

    def __init__(self, model: BaseEstimator, model_name="model ntraame"):
        """
        Initialize the class with a scikit-learn model.

        :param model: A scikit-learn model instance.
        """
        self.model = model
        self.model_name = model_name

    def train(self, X, y):
        """
        Train the model on the provided data.

        :param X: Features for training (array-like or sparse matrix).
        :param y: Target values (array-like).
        """
        self.model.fit(X, y)

    def predict(self, X):
        """
        Predict using the trained model.

        :param X: Features for prediction (array-like or sparse matrix).
        :return: Predicted values (array-like).
        """
        return self.model.predict(X)

    def train_and_test(self, X, y, test_size=0.2, random_state=42):
        """
        Train the model on the provided data.

        :param X: Features for training (array-like or sparse matrix).
        :param y: Target values (array-like).
        :param test_size: Which part of the data is used for testing.
        """
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        self.train(X_train, y_train)
        self.print_score(X_test, y_test)

    def print_score(self, X_test, y_test):
        """
        Print the score of the model.

        :param X_test:
        :param y_test:
        """
        metrics = {"accuracy": self.model.score(X_test, y_test)}
        log_mlflow_experiment("Experiment 1", "Model 1", None, metrics , self.model, None)

        print(f"Model accuracy of {metrics.get('accuracy')}")


