from model.Model import *
from datawrapper.DataWrapper import *
class Trainer:

    def __init__(self, model: Model=None):
        self.model = model

    def compute(self, dataset: DataWrapper):
        self.train(dataset)

    def train(self, wrapper: DataWrapper):
        if not self.model.in_cols:
            features = wrapper.get_features()
        else :
            features = wrapper.get_dataframe()[self.model.in_cols]

        self.model.set_parameters_from_wrapper(wrapper)

        self.model.fit(features, wrapper.get_labels())



    def reset_state(self):
        self.model.reset_state()