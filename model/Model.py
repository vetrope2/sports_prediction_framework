import pandas as pd
import numpy as np
class Model:

    in_cols = []

    def fit(self, features: pd.DataFrame, labels: pd.DataFrame):
        raise NotImplementedError

    def predict(self, data: pd.DataFrame) -> np.ndarray:
        raise NotImplementedError

    def reset_state(self):
        raise NotImplementedError