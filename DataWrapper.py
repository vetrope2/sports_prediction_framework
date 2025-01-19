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

    def get_data(self):
        """
        Returns the data_frame variable.
        """
        return self.data_frame

    def set_data(self, data_frame):
        """
        Sets the data_frame variable.
        :param data_frame:
        """
        self.data_frame = data_frame
