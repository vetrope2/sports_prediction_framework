# Sports Prediction Framework

# Components

## DataLoader

DataLoader is an abstract base class that defines a standard interface for data loaders. Any specific data loader, such as one for CSV files, must inherit from this class and implement the load_data method.

## CSVDataLoader

CSVDataLoader is a concrete implementation of the DataLoader class, designed to handle data loading from CSV files. It reads the file, converts it into a pandas DataFrame, and returns a DataWrapper object for further data manipulation.

## DataWrapper

DataWrapper is a utility class that encapsulates a pandas DataFrame. It provides an interface for managing and analyzing tabular data. The DataWrapper can be initialized with a DataFrame or can load data directly from a CSV file.


# Example

```python
from framework import CSVDataLoader

# Create a CSVDataLoader instance
csv_loader = CSVDataLoader()

# Load data into a DataWrapper
data_wrapper = csv_loader.load_data('path/to/your/file.csv')

# Access the pandas DataFrame
print(data_wrapper.data_frame)
```
