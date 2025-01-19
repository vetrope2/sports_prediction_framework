from DataWrapper import DataWrapper
import pandas as pd
import numpy as np

class DataTransformer:

    def remove_IQR_outliers(self, column_name, dataWrapper: DataWrapper):
        """
        Remove outliers from the specified columns based on the Interquartile Range (IQR).

        This function identifies and removes rows in a DataFrame where the values
        in the specified columns fall outside the acceptable range defined by the
        Interquartile Range (IQR). The IQR is the difference between the 75th and
        25th percentiles, and outliers are defined as values that are either below
        the lower bound or above the upper bound, typically calculated as:
        - Lower bound = Q1 - 1.5 * IQR
        - Upper bound = Q3 + 1.5 * IQR

        :param column_name: The name of the column to fix outliers in.
        :param dataWrapper: The data being modified.
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
        """
        Remove outliers from the specified columns based on Z-scores.

        This function identifies and removes rows in a DataFrame where the Z-score
        of values in the specified columns exceed a given threshold. The Z-score is
        a measure of how many standard deviations a value is from the mean. Values
        with a Z-score greater than the threshold (in absolute value) are considered
        outliers and are removed.

        :param column_name: column_name: The name of the column to fix outliers in.
        :param dataWrapper: The data being modified.
        :param threshold: The threshold for the Z-score.
        """
        mean = np.mean(dataWrapper.get_data()[column_name])
        std_dev = np.std(dataWrapper.get_data()[column_name])
        dataWrapper.get_data()['z_score'] = (dataWrapper.get_data()[column_name] - mean) / std_dev

        dataWrapper.set_data(dataWrapper.get_data()[np.abs(dataWrapper.get_data()['z_score']) <= threshold])


    def winsorize(self, column_name: str, dataWrapper: DataWrapper, lower_quantile: float = 0.05, upper_quantile: float = 0.95):
        """
        Winsorize (cap) the extreme values of the specified columns in a DataFrame.

        This function replaces the values in the specified columns of a pandas DataFrame
        that are below the lower percentile or above the upper percentile with the
        values corresponding to those percentiles. This process, known as Winsorization,
        is useful for limiting the effect of extreme outliers.

        :param dataWrapper: Data.
        :param lower_quantile: Lower quantile threshold (default is 0.05).
        :param upper_quantile: Upper quantile threshold (default is 0.95).
        :return: A DataWrapper with winsorized values.
        """

        winsorized_df = dataWrapper.get_data()

        lower_bound = winsorized_df[column_name].quantile(lower_quantile)
        upper_bound = winsorized_df[column_name].quantile(upper_quantile)

        winsorized_df[column_name] = np.clip(winsorized_df[column_name], lower_bound, upper_bound)
        dataWrapper.set_data(winsorized_df)
        return dataWrapper


    def create_dummies(self, dataWrapper: DataWrapper, columns:list):
        """
        Convert categorical columns of a DataFrame into dummy/indicator variables.

        This function takes a pandas DataFrame and converts specified categorical
        columns into dummy/indicator variables.
        It uses pandas' `get_dummies()` function to generate new columns for each
        category in the categorical columns. The new columns are named after the
        original column with each category being represented as a separate column.

        """
        return DataWrapper(pd.get_dummies(dataWrapper.get_data(), columns=columns, drop_first=True, dtype=int))


    def remove_all_outliers(self, column_name, dataWrapper: DataWrapper, threshold = 3.0):
        """
        Combination of IQR and Z-score.

        :param column_name:
        :param dataWrapper: Data.
        :param threshold: Z-score threshold.
        """
        self.remove_IQR_outliers(column_name, dataWrapper)
        self.remove_Z_score_outliers(column_name, dataWrapper, threshold)