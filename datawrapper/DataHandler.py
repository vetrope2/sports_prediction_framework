import pandas as pd
from typing import Self


class DataHandler:
    def __init__(self, dataframe: pd.DataFrame = None, feature_cols=None, label_cols=None, prediction_cols=None):
        self.dataframe = dataframe
        self.prediction_cols = prediction_cols  # cols that will be created by different learners

        if label_cols is None:
            self.label_cols = set()
        else:
            self.label_cols = set(label_cols)

        if feature_cols is None:
            self.feature_cols = set()
        else:
            self.feature_cols = set(feature_cols)
    def get_dataframe(self):
        return self.dataframe

    def set_dataframe(self, dataframe:pd.DataFrame):
        self.dataframe = dataframe

    def get_features(self):
        return self.dataframe[self.feature_cols]

    def add_features(self, features, on=None):
        if on is None:
            self.dataframe = self.dataframe.join(features)
        else:
            self.dataframe = self.dataframe.join(features, on=on)
        for col in features.columns.tolist():
            self.feature_cols.add(col)

    def get_labels(self):
        return self.dataframe[self.label_cols]

    def add_labels(self, labels):
        self.dataframe = self.dataframe.join(labels)
        for col in labels.columns.tolist():
            self.label_cols.add(col)

    def get_predictions(self):
        return self.dataframe[self.prediction_cols]

    def add_predictions(self, predictions):
        self.dataframe = self.dataframe.join(predictions)
        if self.prediction_cols is None:
            self.prediction_cols = []
        self.prediction_cols += predictions.columns.tolist()

    def get_columns(self, columns):
        return self.dataframe[columns]

    def add_columns(self, data):
        self.dataframe = self.dataframe.join(data)


class DataMerger:
    @staticmethod
    def merge_data_handlers(self, handlers: [DataHandler]) -> DataHandler:
        merged = handlers[0].copy()
        merged.dataframe = pd.concat([handler.dataframe for handler in handlers], ignore_index=True)
        merged.dataframe.sort_index(inplace=True)
        return merged
