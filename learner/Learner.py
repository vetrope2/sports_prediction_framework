import pandas as pd
from datawrapper.DataWrapper import DataWrapper
from learner.Trainer import Trainer
from learner.Tester import Tester
from transformer.DataSelector import DataSelector


class Learner:
    def __init__(self, trainer: Trainer=None, tester: Tester=None, scope: DataSelector=None, **kwargs):
        self.trainer = trainer
        self.tester = tester
        self.scope = scope
        if self.scope is None:
            raise ValueError("Scope has to be set!")

    def compute(self, wrapper: DataWrapper) -> DataWrapper:
        features = self.train_test(wrapper)
        if features is None:
            return wrapper
        features = features[~features.index.duplicated(keep='first')]
        pwrapper = wrapper.deepcopy()
        pwrapper.add_predictions(features)
        return pwrapper

    def train_test(self, dataset: DataWrapper) -> pd.DataFrame:
        train_wrapper = self.scope.transform_train(dataset)
        test_wrapper = self.scope.transform_test(dataset)
        #print(f"{len(train_wrapper.get_dataframe())} +  + {len(test_wrapper.get_dataframe())}")
        if train_wrapper.empty() or test_wrapper.empty():
            return pd.DataFrame()
        self.train(train_wrapper)
        return self.test(test_wrapper)

    def train(self, dataset: DataWrapper):
        if self.trainer is not None:
            if not dataset.get_dataframe().empty:
                self.trainer.train(dataset)
            else:
                raise ValueError("Missing data!")

    def test(self, dataset: DataWrapper) -> pd.DataFrame:
        if self.tester is not None:
            if not dataset.get_dataframe().empty:
                return self.tester.test(dataset)
            else:
                raise ValueError("Missing data!")
        return None

    def reset_state(self):
        self.trainer.reset_state()

    def update(self):
        self.scope.update()