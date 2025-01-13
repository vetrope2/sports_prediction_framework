import pandas as pd


class DataWrapper:
    """
    A class that wraps a pandas DataFrame for data manipulation and analysis.
    """

    def __init__(self, data_frame=None):
        """
        Initialize the DataWrapper with an optional pandas DataFrame.

        :param data_frame: A pandas DataFrame (default is None).
        """
        self.data_frame = data_frame if data_frame is not None else pd.DataFrame()

    def load_from_csv(self, file_path):
        """
        Load data from a CSV file into the pandas DataFrame.

        :param file_path: Path to the CSV file.
        """
        try:
            self.data_frame = pd.read_csv(file_path)
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def fix_outliers(self, column_name):
        """
        Remove outliers from a specified column using the interquartile range (IQR) method.

        :param column_name: The name of the column to fix outliers in.
        """
        if column_name not in self.data_frame.columns:
            print(f"Error: Column '{column_name}' not found in the DataFrame.")
            return

        Q1 = self.data_frame[column_name].quantile(0.25)
        Q3 = self.data_frame[column_name].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        self.data_frame = self.data_frame[(self.data_frame[column_name] >= lower_bound) &
                                          (self.data_frame[column_name] <= upper_bound)]