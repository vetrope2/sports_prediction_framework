from abc import ABC, abstractmethod
import csv


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
        Load data from a CSV file and return as a list of dictionaries.

        Each row in the CSV is converted to a dictionary where keys are the column headers.

        :param file_path: Path to the CSV file.
        :return: List of dictionaries containing the data.
        """
        data = []
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
        return data

# Example usage:
#csv_loader = CSVDataLoader()
#data = csv_loader.load_data('input_example/closing_odds.csv')
#print(data)