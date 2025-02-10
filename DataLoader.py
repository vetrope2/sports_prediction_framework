from abc import ABC, abstractmethod
import csv
import pandas as pd
from DataWrapper import DataWrapper
from logger import framework_logger

class DataLoader(ABC):
    """
    Abstract base class for data loaders.
    """

    @abstractmethod
    def load_data(self, file_path):
        """
        Abstract method to load data from a specified file path.
        """
        pass

class CSVDataLoader(DataLoader):
    """
    Data loader class for loading data from CSV files.
    """

    def load_data(self, file_path):
        """
        Load data from a CSV file, create a DataWrapper object, and return it.

        :param file_path: Path to the CSV file.
        :return: DataWrapper object containing the loaded data.
        """
        try:
            data_frame = pd.read_csv(file_path)
            return DataWrapper(data_frame)
        except FileNotFoundError:
            framework_logger.error(f"Error: File not found at {file_path}")
            return DataWrapper()
        except Exception as e:
            framework_logger.error(f"An error occurred: {e}")
            return DataWrapper()


