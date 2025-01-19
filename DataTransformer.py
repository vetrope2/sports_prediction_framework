from DataWrapper import DataWrapper
import pandas as pd
import numpy as np

class DataTransformer:

    def remove_IQR_outliers(self, column_name, dataWrapper: DataWrapper):
        """
        Remove outliers from a specified column using the interquartile range (IQR) method.

        :param column_name: The name of the column to fix outliers in.
        """
        data_frame = dataWrapper.get_data()
        if column_name not in data_frame.columns:
            print(f"Error: Column '{column_name}' not found in the DataFrame.")
            return

        Q1 = data_frame[column_name].quantile(0.25)
        Q3 = data_frame[column_name].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        data_frame = data_frame[(data_frame[column_name] >= lower_bound) &
                                          (data_frame[column_name] <= upper_bound)]

        dataWrapper.set_data(data_frame)


    def remove_Z_score_outliers(self, column_name, dataWrapper: DataWrapper, threshold: float):
        mean = np.mean(dataWrapper.get_data()[column_name])
        std_dev = np.std(dataWrapper.get_data()[column_name])
        dataWrapper.get_data()['z_score'] = (dataWrapper.get_data()[column_name] - mean) / std_dev

        dataWrapper.set_data(dataWrapper.get_data()[np.abs(dataWrapper.get_data()['z_score']) <= threshold])


    def winsorize(self, dataWrapper: DataWrapper, lower_quantile: float = 0.05, upper_quantile: float = 0.95):
        """
        Winsorize a DataFrame by capping extreme values at specified quantiles.

        :param dataWrapper: Data.
        :param lower_quantile: Lower quantile threshold (default is 0.05).
        :param upper_quantile: Upper quantile threshold (default is 0.95).
        :return: A DataWrapper with winsorized values.
        """

        winsorized_df = dataWrapper.get_data()

        for column in winsorized_df.select_dtypes(include=[np.number]).columns:
            lower_bound = winsorized_df[column].quantile(lower_quantile)
            upper_bound = winsorized_df[column].quantile(upper_quantile)

            winsorized_df[column] = np.clip(winsorized_df[column], lower_bound, upper_bound)
        dataWrapper.set_data(winsorized_df)
        return dataWrapper


    def create_dummies(self, dataWrapper: DataWrapper, columns:list):
        return DataWrapper(pd.get_dummies(dataWrapper.get_data(), columns=columns, drop_first=True, dtype=int))


    def remove_all_outliers(self, column_name, dataWrapper: DataWrapper, threshold = 3.0):
        self.remove_IQR_outliers(column_name, dataWrapper)
        self.remove_Z_score_outliers(column_name, dataWrapper, threshold)