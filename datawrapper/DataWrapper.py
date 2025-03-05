from datawrapper.DataHandler import DataHandler
import pandas as pd


class DataWrapper:

    season_column = 'Season'

    name_columns = None
    name_id_columns = None
    prediction_columns = None

    def __init__(self, data_handler: DataHandler, home_advantage=None):
        self.data_handler = data_handler

    def get_dataframe(self):
        return self.data_handler.dataframe

    def set_dataframe(self, dataframe):
        self.data_handler.dataframe = dataframe

    def get_features(self):
        return self.data_handler.get_features()

    def add_features(self, features, on=None):
        self.data_handler.add_features(features, on)

    def add_features_from_csv(self, filename, index=None, on=None):
        dataframe = pd.read_csv(filename,index_col=index)
        self.add_features(dataframe, on)

    def get_labels(self):
        return self.data_handler.get_labels()

    def add_labels(self, labels):
        self.data_handler.add_labels(labels)

    def get_predictions(self):
        return self.data_handler.get_predictions()

    def add_predictions(self, predictions):
        self.data_handler.add_predictions(predictions)

    def add_columns(self, data):
        self.data_handler.add_columns(data)

    def get_columns(self, column_names):
        return self.data_handler.get_columns(column_names)
