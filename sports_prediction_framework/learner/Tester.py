from sports_prediction_framework.model.Model import *
from sports_prediction_framework.model.Scikit import *


class Tester:

    def __init__(self, model: Model = None):
        self.model = model

    def compute(self, dataset: DataWrapper) -> pd.DataFrame:
        return self.test(dataset)

    def test(self, wrapper: DataWrapper) -> pd.DataFrame:
        if not self.model.in_cols:
            features = wrapper.get_features()
        else:
            features = wrapper.get_dataframe()[self.model.in_cols]
        if isinstance(self.model, ScikitModel):
            if features.isnull().values.any():
                print('Features contain nulls or nan in scikit predicting')
                return pd.DataFrame()
            preds = self.model.predict(features)

            if preds.shape[1] > 1:
                cols = self.model.scikit_model.classes_
            else:
                cols = wrapper.data_handler.label_cols

            return pd.DataFrame(index=wrapper.get_dataframe().index, data=preds, columns=cols)
        else:
            preds = self.model.predict(features)
            return pd.DataFrame(index=wrapper.get_dataframe().index, data=preds)
