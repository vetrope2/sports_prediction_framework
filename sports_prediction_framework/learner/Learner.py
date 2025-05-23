import pandas as pd
from sports_prediction_framework.datawrapper.DataWrapper import DataWrapper
from sports_prediction_framework.learner.Trainer import Trainer
from sports_prediction_framework.learner.Tester import Tester
from sports_prediction_framework.transformer.DataSelector import DataSelector
from sports_prediction_framework.utils.Merger import Merger


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
                predictions = self.tester.test(dataset)  # Quick sanity check
                return predictions
            else:
                raise ValueError("Missing data!")
        return None

    def set_model_hyper_params(self, params):
        self.trainer.model.set_params(params)
        self.tester.model.set_params(params)
        #print(self.trainer.model.model.__getattribute__("dense_dim"))

    def reset_state(self):
        self.trainer.reset_state()

    def update(self):
        self.scope.update()

class LearnerWithoutScope(Learner):

    def __init__(self, trainer: Trainer=None, tester: Tester=None, **kwargs):
        super().__init__(trainer, tester, None, **kwargs)

    def train_test(self, dataset: DataWrapper) -> pd.DataFrame:
        self.train(dataset)
        return self.test(dataset)


class UpdatingLearner(Learner):
    """Represents a looping, self-updating learner while a given condition holds true"""

    def __init__(self, trainer: Trainer = None, tester: Tester = None, scope: DataSelector = None, learners: list = None):
        self.learners = learners
        if self.learners is not None:
            if not isinstance(self.learners, list):
                self.learners = [self.learners]
            self.merger = Merger()
        else:
            self.learners = []
        super().__init__(trainer, tester, scope)

    def train_test(self, wrapper: DataWrapper):
        outputs = []
        copy = wrapper.deepcopy()
        # iteratively check if still within dataset scope
        while self.scope.holds():
            if self.learners:
                wrappers = []
                for learner in self.learners:
                    wrappers.append(learner.compute(copy))
                    learner.update()
                wrapper = self.merger.compute(wrappers)
            outputs.append(super().train_test(wrapper))
            self.update()

        if self.tester is not None:
            if len(outputs) == 0:
                return pd.DataFrame()
            features = pd.concat([data for data in outputs])
            return features
        return None

    def reset_state(self):
        if self.learners is not None:
            for learner in self.learners:
                learner.reset_state()
        self.scope.reset_state()
        self.trainer.reset_state()

