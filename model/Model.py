import pandas as pd
import numpy as np
from datawrapper.DataWrapper import *


class Model:

    in_cols = []
    model = None

    def fit(self, features: pd.DataFrame, labels: pd.DataFrame):
        raise NotImplementedError

    def predict(self, data: pd.DataFrame) -> np.ndarray:
        raise NotImplementedError

    def set_parameters_from_wrapper(self, wrapper:DataWrapper):
        pass

    def reset_state(self):
        raise NotImplementedError


    def set_params(self, params: dict):
        for key,value in params.items():
            setattr(self.model, key, value)